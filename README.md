# Operational Systems Design

Engineering evidence-driven systems for real-world operations.

This repository is the central index for my work in **operational AI systems**:
systems that transform field, sensor and analytical data into reproducible,
traceable and decision-oriented evidence.

## Professional focus

I work at the intersection of:

- geospatial data science;
- edge and IoT systems;
- reliability and observability;
- deterministic event and state reconstruction;
- governed automation and human oversight.

The goal is not to add AI to every process. The goal is to build systems whose
inputs, transformations, limitations and outputs can be inspected and defended.

## Portfolio architecture

| Repository | Role | Public evidence | Status |
|---|---|---|---|
| [Corredor de Altura](https://github.com/MartinnCG/corredor-altura) | Applied geospatial data science | Calibrated 130 km corridor, reproducible feature pipeline, relative-exposure model, GIS products, dashboard and automated data-contract checks | [Analytical v1.0](https://github.com/MartinnCG/corredor-altura/releases/tag/v1.0) |
| [AI/ML Systems Architecture Labs](https://github.com/MartinnCG/ai-ml-systems-architecture-labs) | Focused technical experiments | Explicit boundaries, invariants, failure modes and minimal reference implementations | Active laboratory |
| [Deterministic Replay System](https://github.com/MartinnCG/deterministic-replay-system) | Reference mechanism | State reconstruction from an ordered event stream and integrity verification | Prototype; future integration candidate |
| Edge Operational Evidence System | Flagship systems-engineering implementation | Edge ingestion, durable events, state reconstruction, failure handling, observability and evidence reporting | Planned |

## Two flagship directions

### 1. Geospatial operational intelligence

Corredor de Altura demonstrates how heterogeneous spatial and operational
sources can be transformed into a common, segment-level analytical model.

The published index represents **relative exposure within the studied
corridor**. It is not an absolute-risk score and does not predict incidents,
failures, closures or maintenance demand.

### 2. Edge operational evidence

The planned Edge Operational Evidence System will demonstrate how an
edge-first platform can continue collecting, validating and reconstructing
operational evidence under sensor faults, delayed data, gateway restarts and
network loss.

It will evolve through executable, testable increments rather than a
feature-first prototype.

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
- an explicit acceptance criterion;
- an implementation or analytical change;
- an automated or documented verification;
- a record of limitations and unresolved risks;
- a pull request that explains the decision, not only the code.

Activity without evidence is not the objective. The public record should show
a consistent ability to frame, build, verify and communicate operational
systems.

## Current roadmap

1. Maintain the frozen Corredor de Altura analytical v1 release.
2. Establish a repeatable weekly engineering and review method.
3. Build the Edge Operational Evidence System from event contracts upward.
4. Publish architecture labs only when they test a concrete system question.
5. Connect proven technical components into governed operational workflows.

## Scope boundary

Commercial concepts and domain-specific applications may build on this work,
but this repository does not claim professional authority in safety,
geotechnical, environmental or operational auditing. Domain interpretation
must be supported by appropriate evidence and subject-matter expertise.

---

**Martin CG**  
Operational AI systems · geospatial analytics · edge evidence · reliability
