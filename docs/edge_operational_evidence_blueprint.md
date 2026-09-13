# Edge Operational Evidence System — foundation blueprint

## Mission

Build a public, reproducible reference system that preserves and reconstructs
operational evidence at the edge when sensors, networks and processes are
imperfect.

The system should answer:

- What was observed?
- When was it observed and received?
- Was the observation accepted, rejected or qualified?
- What state was derived from the available evidence?
- Which rule produced an operational finding?
- Can the result be reproduced after a restart?

## Initial use case

A synthetic site contains environmental and occupancy sensors connected to a
Linux edge gateway. The gateway must continue operating without cloud access,
preserve the evidence needed to rebuild state and produce a human-readable
operational report.

The public repository will use simulated data. Hardware adapters may be added
later without changing the core contracts.

## System boundary

### In scope for v0.1

- deterministic sensor and fault simulation;
- canonical event validation;
- append-only local event persistence;
- idempotent ingestion;
- deterministic state reconstruction;
- explicit data-quality findings;
- rule evaluation over derived state;
- structured evidence bundles;
- health metrics and human-readable reports;
- automated tests and failure campaigns.

### Out of scope for v0.1

- direct actuator or equipment control;
- safety-certified alarms or decisions;
- cloud availability as a core dependency;
- machine-learning prediction;
- autonomous agents;
- customer dashboards;
- real client, property, employee or mine-site data.

## Reference flow

```text
sensor or simulator
        |
        v
protocol adapter -> canonical validation -> append-only event ledger
                                             |
                                             v
                                      deterministic projector
                                             |
                                             v
derived state + quality findings -> rules -> evidence bundle -> report
```

Adapters translate protocols. They do not determine operational meaning.
Accepted and rejected observations remain distinguishable. The ledger is the
replayable source of truth; derived state and reports are replaceable views.

## Canonical event envelope

Every accepted observation must contain:

| Field | Purpose |
|---|---|
| `event_id` | Globally unique idempotency key |
| `device_id` | Stable source identity |
| `event_type` | Versioned observation type |
| `observed_at` | Source observation time in UTC |
| `received_at` | Gateway receipt time in UTC |
| `sequence` | Optional device-local ordering evidence |
| `schema_version` | Contract version |
| `payload` | Type-specific observation data |
| `source` | Simulator or adapter identity |

Validation produces a separate disposition containing acceptance status,
reason codes and processing time. Raw input is never silently corrected.

## Core invariants

1. **Append-only evidence**  
   Accepted canonical events are never updated in place.

2. **Idempotent ingestion**  
   Reprocessing the same `event_id` does not change the ledger or derived
   state.

3. **Deterministic replay**  
   Replaying the same accepted event set under the same projector version
   produces the same state hash.

4. **Explicit time semantics**  
   Observation time and receipt time are stored separately. Late delivery is
   evidence, not an error to hide.

5. **Restart recovery**  
   A gateway restart cannot require cloud access to restore the last
   reproducible state.

6. **Qualified evidence**  
   Missing, stale, frozen, invalid and out-of-range readings remain explicit.

7. **Versioned interpretation**  
   Events, projectors and rules declare their versions in generated evidence.

8. **Human authority**  
   Findings support review. They do not silently execute physical actions.

## Initial component architecture

| Component | Responsibility | Persistent output |
|---|---|---|
| Simulator | Generate deterministic observations and injected faults | Scenario manifest |
| Adapter | Translate source messages into candidate canonical events | None |
| Validator | Validate schema, time and payload rules | Disposition record |
| Event ledger | Persist accepted events idempotently | SQLite event rows |
| Projector | Reconstruct device and site state | Replaceable state view |
| Quality evaluator | Identify stale, frozen, missing or invalid evidence | Quality findings |
| Rule engine | Evaluate explicit deterministic rules | Rule findings |
| Evidence builder | Connect findings to events, versions and state | Evidence bundle |
| Reporter | Produce operator-oriented summaries | JSON and Markdown report |
| Health monitor | Expose pipeline counters and processing state | Structured metrics |

SQLite is the initial local persistence mechanism because it is inspectable,
transactional, portable and sufficient for a single-gateway reference system.
It is an implementation decision, not a universal infrastructure claim.

## Failure campaign

Each failure scenario must have a deterministic fixture and observable
acceptance result.

| Scenario | Required evidence |
|---|---|
| Duplicate delivery | One ledger event; duplicate counter increments |
| Out-of-order arrival | Receipt order retained; deterministic projection documented |
| Delayed event | Positive delivery delay and explicit late-data finding |
| Invalid payload | Rejected disposition with reason; no accepted ledger event |
| Frozen sensor | Repeated value pattern produces a qualified finding |
| Missing sensor | State records absence or staleness without fabricated values |
| Gateway restart | Rebuilt state hash equals the pre-restart reference |
| Network loss | Local ingest and reporting continue; no cloud call is required |
| Partial write attempt | Transaction leaves no ambiguous accepted event |

## Evidence bundle

A v0.1 evidence bundle should include:

- bundle id and generation time;
- scenario and software version;
- event-set digest;
- projector and rule versions;
- derived-state digest;
- relevant quality and rule findings;
- event ids supporting each finding;
- explicit limitations;
- report-generation status.

The bundle makes a result inspectable. It does not certify that the underlying
sensor measured reality correctly.

## Delivery milestones

### M0 — Repository contract

**Build**

- repository skeleton;
- README with boundaries and invariants;
- Python packaging and test configuration;
- CI quality gate;
- contribution and security notes.

**Acceptance evidence**

- clean installation;
- one command runs all tests;
- CI passes on the initial repository.

### M1 — Deterministic simulator and event contract

**Build**

- versioned event schema;
- deterministic scenario manifest;
- normal observation stream;
- invalid and duplicate fixtures.

**Acceptance evidence**

- identical seed produces identical event digest;
- invalid events return stable reason codes;
- schema examples validate in CI.

### M2 — Durable idempotent ledger

**Build**

- SQLite ledger;
- accepted and rejected dispositions;
- unique `event_id` constraint;
- transactional ingestion.

**Acceptance evidence**

- duplicate ingestion does not increase accepted-event count;
- partial transaction leaves no ambiguous record;
- ledger export can be independently inspected.

### M3 — Deterministic state reconstruction

**Build**

- versioned projector;
- device and site state;
- canonical ordering policy;
- state digest.

**Acceptance evidence**

- clean replay produces the expected digest;
- restart and full replay reproduce the same state;
- ordering assumptions are documented and tested.

### M4 — Data-quality findings

**Build**

- stale, missing, frozen, late and out-of-range evaluations;
- evidence links from finding to supporting events.

**Acceptance evidence**

- each injected fault produces the expected finding;
- normal scenarios do not produce false fixture findings;
- no missing value is silently imputed.

### M5 — Operational evidence report

**Build**

- evidence bundle;
- JSON and Markdown reports;
- pipeline health metrics.

**Acceptance evidence**

- every report finding traces to event ids and component versions;
- report generation is reproducible;
- limitations and human-review boundary are present.

### M6 — Edge integration

**Build**

- MQTT adapter;
- containerized gateway runtime;
- controlled disconnection and restart campaign.

**Acceptance evidence**

- the same canonical contract works with simulator and MQTT input;
- core operation continues offline;
- recovery results are recorded in a repeatable run report.

## Repository creation gate

Create the new public repository only when the following are accepted:

- name: `edge-operational-evidence-system`;
- this system boundary;
- the append-only ledger decision;
- M0 acceptance criteria;
- simulated-data-only public policy.

The first implementation pull request must deliver M0 only. It must not include
sensor logic, dashboards, agents or predictive models.
