"""Dependency-free contract checks for public Operational Evidence examples."""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "contracts" / "operational-evidence-envelope-v1.schema.json"
EXAMPLES = ROOT / "examples"
DIGEST = re.compile(r"^[0-9a-f]{64}$")
IDENTIFIER = re.compile(r"^[a-z0-9][a-z0-9._:-]{2,127}$")
REQUIRED = {
    "schema_version",
    "evidence_id",
    "evidence_type",
    "classification",
    "producer",
    "evidence_time",
    "facts",
    "scope",
    "integrity",
}


def canonical_digest(value):
    encoded = json.dumps(
        value, allow_nan=False, separators=(",", ":"), sort_keys=True
    ).encode()
    return hashlib.sha256(encoded).hexdigest()


def utc(value):
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.utcoffset() is None or parsed.utcoffset().total_seconds() != 0:
        raise ValueError("timestamp must use UTC")
    return parsed


def validate(value, path):
    errors = []
    missing = sorted(REQUIRED - set(value))
    if missing:
        errors.append("missing fields: " + ", ".join(missing))
        return errors
    if value["schema_version"] != "1.0":
        errors.append("unsupported schema_version")
    if not IDENTIFIER.fullmatch(value["evidence_id"]):
        errors.append("invalid evidence_id")
    if value["classification"] not in {"public", "sanitised"}:
        errors.append("public boundary forbids classification")
    producer = value["producer"]
    for field in (
        "repository_uri",
        "revision",
        "artifact_path",
        "source_mode",
        "transform_version",
    ):
        if not producer.get(field):
            errors.append(f"missing producer.{field}")
    if producer.get("source_mode") not in {
        "observed",
        "historical-import",
        "derived",
        "simulated",
    }:
        errors.append("invalid source_mode")
    try:
        start = utc(value["evidence_time"]["observed_from"])
        end = utc(value["evidence_time"]["observed_to"])
        utc(value["evidence_time"]["generated_at"])
        if start > end:
            errors.append("observation interval is reversed")
    except (KeyError, TypeError, ValueError):
        errors.append("invalid evidence_time")
    if not isinstance(value["facts"], dict) or not value["facts"]:
        errors.append("facts must be a non-empty object")
    scope = value["scope"]
    for field in ("purpose", "supports", "does_not_support"):
        if not scope.get(field):
            errors.append(f"missing scope.{field}")
    integrity = value["integrity"]
    if integrity.get("algorithm") != "sha256" or not DIGEST.fullmatch(
        integrity.get("digest", "")
    ):
        errors.append("invalid integrity")
    if producer.get("source_mode") == "simulated":
        if value["facts"].get("simulation") is not True:
            errors.append("simulated evidence must declare facts.simulation=true")
        if not any("real" in item.lower() for item in scope.get("does_not_support", [])):
            errors.append("simulated evidence must deny a real observation claim")
        expected = canonical_digest(value["facts"])
        if integrity.get("subject") == "simulated facts object in this contract example":
            if integrity.get("digest") != expected:
                errors.append("simulated facts digest mismatch")
    if any(term in json.dumps(value).lower() for term in ("private_key", "credential")):
        errors.append("forbidden private field marker")
    return [f"{path.name}: {error}" for error in errors]


def main():
    json.loads(SCHEMA.read_text())
    files = sorted(EXAMPLES.glob("*-envelope-v1.json"))
    if len(files) < 2:
        raise SystemExit("expected at least two v1 envelope examples")
    errors = []
    for path in files:
        errors.extend(validate(json.loads(path.read_text()), path))
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"validated {len(files)} Operational Evidence Envelope v1 examples")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
