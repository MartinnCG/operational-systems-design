# Weekly evidence-delivery method

## Objective

Produce a small, defensible unit of engineering evidence every week without
optimizing for an artificial contribution count.

The default target is **one verified pull request per week**. During demanding
shift rotations, a documented investigation or release review may replace a
code change if it produces reusable evidence.

## Definition of a valuable contribution

A contribution is valuable when it includes all of the following:

1. a concrete system or analytical problem;
2. an explicit boundary and non-goals;
3. a change in code, data contract, test, architecture or documentation;
4. evidence that the change behaves as claimed;
5. limitations, risks or unresolved questions;
6. a traceable issue and pull request.

Formatting-only commits, generated activity and unexplained dependency changes
do not satisfy this definition.

## Weekly cycle

### 1. Inspect

Review the active repositories for:

- failing workflows;
- stale or blocked pull requests;
- unverified claims in documentation;
- missing tests or data contracts;
- unresolved failure modes;
- drift between the repository state and its roadmap.

**Output:** a short list of candidate work items.

### 2. Select

Choose one work item using this priority order:

1. correctness or confidentiality risk;
2. broken reproducibility or verification;
3. missing operational evidence;
4. reliability and observability;
5. new capability.

The task must be narrow enough to finish and verify within the available week.

**Output:** one issue with acceptance criteria and explicit non-goals.

### 3. Build

Create a named branch and make atomic commits.

Recommended prefixes:

- `fix/` for incorrect behaviour;
- `test/` for verification;
- `feat/` for a bounded capability;
- `docs/` for architectural or methodological evidence;
- `chore/` for repository or release maintenance.

Each commit message should state the engineering outcome, for example:
`test: enforce canonical segment coverage`.

### 4. Verify

Verification should match the claim. Examples include:

- automated unit or integration tests;
- data-contract checks;
- deterministic replay comparison;
- failure-injection results;
- reproducible metrics;
- a documented manual GIS inspection.

A screenshot alone is not sufficient evidence for a behavioural claim.

### 5. Review

Open a pull request that records:

- the problem and why it matters;
- the implemented decision;
- the evidence produced;
- what did not change;
- known limitations and follow-up work.

Do not merge a failed quality gate. Keep changes reviewable and avoid mixing
unrelated tasks.

### 6. Close

After merge:

- confirm the default branch workflow;
- close or update the related issue;
- update release notes or the roadmap when appropriate;
- record the next unresolved risk without automatically expanding scope.

## Automation boundary

Automation may:

- inventory repository state;
- run deterministic checks;
- identify stale documentation;
- draft issues from observable gaps;
- implement low-risk, bounded changes on a branch;
- prepare pull requests and verification summaries.

Human review is required before:

- changing analytical meaning or model weights;
- publishing new operational or safety claims;
- exposing field, client or location-sensitive data;
- changing the stated scope of a released project;
- merging a material pull request;
- publishing a release.

## Repository rotation

Work is selected by evidence value, not equal time allocation.

| Repository | Default role in the cycle |
|---|---|
| Corredor de Altura | Maintain release integrity and develop V2 deliberately |
| Edge Operational Evidence System | Primary systems-engineering build |
| AI/ML Systems Architecture Labs | Test patterns arising from real project questions |
| Operational Systems Design | Maintain the portfolio map and shared method |

## Monthly review

Every four weeks, evaluate:

- verified pull requests completed;
- tests or contracts added;
- documented failure modes;
- releases produced;
- stale or redundant repositories;
- whether public claims remain supported by evidence.

The review should change priorities when necessary. It should not create work
solely to preserve a visual contribution streak.
