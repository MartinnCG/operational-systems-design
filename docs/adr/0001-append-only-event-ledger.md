# ADR-0001: Use an append-only event ledger as the source of truth

- **Status:** Proposed
- **Date:** 2026-09-13
- **Decision owners:** Repository maintainer
- **Applies to:** Edge Operational Evidence System v0.1

## Context

The system must preserve operational evidence on an intermittently connected
edge gateway. Sensor messages may be duplicated, delayed, invalid or received
out of order. The process may restart after state has already been derived.

Persisting only the latest device state would make it impossible to explain
which observations produced that state or to rebuild it after interpretation
logic changes.

## Decision

Persist accepted canonical events in an append-only local ledger and treat that
ledger as the replayable source of truth.

Derived device state, site state, quality findings and reports are projections.
They may be discarded and rebuilt using a declared projector or rule version.

For the v0.1 reference implementation:

- SQLite provides the local transactional store;
- `event_id` is unique and enforces idempotency;
- observation and receipt timestamps are both preserved;
- validation disposition is recorded explicitly;
- accepted events are not updated in place;
- correction is represented by a new event, not silent mutation;
- evidence bundles include event-set and state digests.

## Consequences

### Benefits

- state can be reconstructed after restart;
- outputs remain traceable to observations;
- interpretation changes can be compared through replay;
- duplicate delivery can be handled deterministically;
- failure campaigns can assert ledger and state integrity;
- core evidence remains available without cloud access.

### Costs

- storage grows with event volume;
- ordering and correction policies must be explicit;
- schema evolution requires version-aware replay;
- deletion and retention policies require deliberate design;
- a ledger preserves received evidence but cannot prove sensor truth.

## Alternatives considered

### Persist only current state

Rejected because it loses history, weakens auditability and prevents
independent replay.

### Use a cloud event service as the source of truth

Rejected for v0.1 because core evidence preservation must survive network loss.
Cloud replication may be added later as a secondary capability.

### Store raw files without a transactional ledger

Rejected as the primary design because duplicate handling, atomicity and
queryable dispositions would be harder to verify consistently.

## Validation

This decision is accepted for implementation when automated tests demonstrate:

1. duplicate ingestion does not create a second accepted event;
2. a failed transaction leaves no partial accepted record;
3. restart plus replay reproduces the expected state digest;
4. accepted records are never changed by normal processing;
5. a correction is represented by an additional linked event.

## Revisit conditions

Revisit the storage implementation if measured volume, retention requirements,
multi-writer concurrency or deployment constraints exceed a single-gateway
SQLite design. The append-only evidence principle remains independent of the
specific database.
