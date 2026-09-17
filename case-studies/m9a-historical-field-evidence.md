# Case study: qualifying historical field evidence

## Executive summary

A previous edge deployment produced a useful longitudinal event stream, but the
records could not be presented as current live-system evidence and could not be
published safely. M9A established a controlled migration boundary that converts
that private historical stream into canonical operational events, preserves
provenance and verifies deterministic state reconstruction without disclosing
raw telemetry or operational identities.

This case demonstrates an engineering capability rather than a dataset for
sale: bringing legacy or field-derived evidence into a governed system whose
transformations, limitations and replay results can be inspected.

## Operational question

Can a private historical event stream cross a public canonical boundary, enter
an append-only ledger and reconstruct the same state twice without fabricating
missing transport history or exposing private operational information?

## Approach

1. Recognise only the two documented source shapes and reject unknown shapes
   without echoing their contents.
2. Preserve original observation time while recording historical import time
   separately; no unavailable receipt timestamp is invented.
3. Pseudonymise event and source identities with a private keyed transform.
4. Derive source sequences deterministically from accepted input order.
5. Validate every mapped record against the canonical event contract.
6. Ingest the mapped stream into two fresh ledgers and replay each independently.
7. Publish only sanitised aggregates, limitations and cryptographic source
   digests.

## Verified result

| Measure | Result |
|---|---:|
| Historical records inspected | 38,349 |
| Canonical events accepted | 38,349 |
| Rejected records | 0 |
| Pseudonymised source streams | 6 |
| Independent replay result | Matching final state |
| Observation range | 2026-02-13 to 2026-05-25 |
| Documented active evidence days | 70 across intermittent windows |

The implementation, tests and sanitised machine-readable result are available
in the
[M9A evidence record](https://github.com/MartinnCG/edge-operational-evidence-system/blob/main/docs/m9a-historical-qualification-v1.md).

## Why this matters

For an employer, this is evidence that I can work across data contracts,
migration, privacy, stateful systems, testing and technical communication rather
than only produce a dashboard or model.

For a prospective client, the reusable service pattern is:

- assess whether historical operational data is fit for controlled migration;
- define a canonical contract and explicit provenance boundary;
- transform and pseudonymise sensitive source records;
- test deterministic reconstruction and quantify rejected evidence;
- deliver a reviewable result with limitations and private/public separation.

The commercially useful asset is the method and implementation discipline. The
private source data is not the product.

## Claims deliberately excluded

M9A does not demonstrate:

- a current physical deployment or uninterrupted availability;
- original message receipt latency;
- sensor calibration, accuracy or safety suitability;
- current MQTT, mutual-TLS or hardware continuity;
- continuity across pack-down and physical redeployment;
- production certification or autonomous control authority.

A future M9B campaign is required before making live redeployment claims.

## Professional signal

This case supports positioning for edge/IoT systems, data-platform, reliability,
observability and operational analytics roles. It also provides a credible base
for scoped services in legacy telemetry migration, evidence readiness,
reproducible operational reporting and failure/replay testing.
