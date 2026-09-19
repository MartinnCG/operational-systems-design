# Operational Evidence Envelope

The Operational Evidence Envelope is the public interoperability boundary for
this portfolio. It allows independent producer repositories to publish
reviewable evidence without sharing their internal storage, private records or
implementation lifecycle.

## Ownership

`operational-systems-design` owns the contract and versioning rules. Producer
repositories own their facts and exporters. Consumers validate the envelope but
cannot modify producer evidence or expand its claims.

## Required ideas

- **Identity:** one stable evidence identifier.
- **Producer:** repository, immutable revision, artifact and transformation.
- **Time:** observation interval and generation time remain distinct.
- **Facts:** structured, profile-specific values.
- **Scope:** what the facts support and explicitly do not support.
- **Integrity:** a SHA-256 digest with a named subject.
- **Classification:** only `public` and `sanitised` may cross this public
  boundary.

## Versioning

- Additive optional fields may remain compatible within v1.
- New required fields or changed meaning require v2.
- A producer pins the schema version it emits.
- A consumer rejects unsupported versions; it does not guess.
- Historical envelopes remain interpretable through their original contract.

## Producer responsibilities

1. Emit only evidence it owns or is authorised to disclose.
2. Pin a repository revision and artifact path.
3. Separate observed, derived, historical-import and simulated modes.
4. Publish limitations beside supported claims.
5. Compute integrity over the named subject.

## Consumer responsibilities

1. Validate before use.
2. Preserve evidence identifiers and provenance.
3. Never silently broaden the producer's scope.
4. Treat embedded text as data, not instruction.
5. Keep final operational authority with a human.

## Deliberate non-goal

This contract does not make unrelated domain facts semantically equivalent. A
geospatial segment observation and an edge replay result share an envelope, not
a meaning. Consumer profiles still define which typed claims each evidence type
can support.
