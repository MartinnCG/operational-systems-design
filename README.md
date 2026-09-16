# Operational Systems Design

Engineering evidence-driven systems for real-world operations.

This repository is the central index for my work in **operational data and AI
systems**: systems that transform field, sensor and analytical data into
reproducible, traceable and decision-oriented evidence.

## Professional focus

I work at the intersection of:

- geospatial data science;
- edge and IoT systems;
- reliability and observability;
- deterministic event and state reconstruction;
- governed automation and human oversight.

My differentiating direction is the connection between operational field
context and defensible digital evidence. The goal is not to add AI to every
process. The goal is to build systems whose inputs, transformations,
limitations and outputs can be inspected and defended.

## Portfolio architecture

| Repository | Role | Public evidence | Status |
|---|---|---|---|
| [Corredor de Altura](https://github.com/MartinnCG/corredor-altura) | Applied geospatial data science | Calibrated 130 km corridor, reproducible feature pipeline, relative-exposure model, GIS products, dashboard and automated data-contract checks | [Analytical v1.0](https://github.com/MartinnCG/corredor-altura/releases/tag/v1.0) |
| [Edge Operational Evidence System](https://github.com/MartinnCG/edge-operational-evidence-system) | Flagship systems engineering | Canonical events, durable ledger, deterministic replay, quality campaigns, verified bundles, real MQTT, recovery and certificate-based authorization | [v0.2.0](https://github.com/MartinnCG/edge-operational-evidence-system/releases/tag/v0.2.0) |
| [AI/ML Systems Architecture Labs](https://github.com/MartinnCG/ai-ml-systems-architecture-labs) | Focused technical experiments | Explicit boundaries, invariants, failure modes and minimal reference implementations | Active laboratory; experiments only when tied to a concrete system question |
| [Deterministic Replay System](https://github.com/MartinnCG/deterministic-replay-system) | Reference mechanism | State reconstruction from an ordered event stream and integrity verification | Prototype; the mechanism is represented in the Edge evidence path |

## Flagship directions

### Geospatial operational intelligence

Corredor de Altura demonstrates how heterogeneous spatial and operational
sources can be transformed into a common, segment-level analytical model.

The published index represents **relative exposure within the studied
corridor**. It is not an absolute-risk score and does not predict incidents,
failures, closures or maintenance demand.

### Edge operational evidence

Edge Operational Evidence System demonstrates an edge-first evidence path built
through executable milestones rather than a feature-first prototype.

Release v0.2.0 proves, within its documented test boundary:

- deterministic synthetic events and controlled failure scenarios;
- transactional, idempotent and append-only SQLite ingestion;
- versioned replay, state digests and traceable quality findings;
- portable evidence bundles with independent verification;
- real Mosquitto/Paho transport, retained QoS 1 delivery and reconnect;
- mutual TLS, certificate-derived identities and role-separated ACLs;
- negative campaigns in which unauthorized inputs cannot mutate the ledger.

The next field milestone, M9, is intentionally deferred until the physical
hardware inventory is confirmed. It will target 30 active device-days across
repeated deployments and will distinguish planned offline windows from
unplanned failures. It will not claim uninterrupted availability or calibrated
sensing.

## Engineering principles

Every substantial contribution should strengthen at least one of these
properties:

1. **Reproducibility** — another person can repeat the procedure.
2. **Traceability** — outputs can be connected to inputs and transformations.
3. **Reliability** — expected failure modes are explicit and tested.
4. **Decision relevance** — evidence is structured for a real operational use.
5. **Governance** — limitations, uncertainty and human authority remain visible.

## Evidence standard

A completed work item should contain:

- a defined problem and boundary;
- explicit acceptance criteria;
- an implementation or analytical change;
- automated or documented verification;
- a record of limitations and unresolved risks;
- a pull request that explains the decision, not only the code.

Activity without evidence is not the objective. The public record should show a
consistent ability to frame, build, verify and communicate operational systems.

## Current sequence

1. Maintain the frozen Corredor de Altura analytical v1 release.
2. Maintain Edge Operational Evidence System v0.2.0 as the verified software
   boundary.
3. Inventory the minimum field kit before implementing M9.
4. Execute M9 only when physical data and repeated deployments can be evidenced
   honestly.
5. Publish architecture labs only when they test a concrete system question.
6. Connect proven components into governed operational workflows.

## Scope boundary

This portfolio does not claim professional authority in safety, geotechnical,
environmental or operational auditing. Public examples exclude private
credentials, precise operational locations and personal schedules. Domain
interpretation must be supported by appropriate evidence and subject-matter
expertise. Findings support human review and do not authorize control of
physical equipment.

---

**Martin CG**  
Operational systems · geospatial analytics · edge evidence · reliability
