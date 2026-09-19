# Portfolio Synchronization Policy

## Purpose

The central architecture must evolve with its component repositories. A release,
scope change or new limitation is incomplete at portfolio level until its impact
on `operational-systems-design` is explicitly classified.

This creates a self-correcting record: new evidence may strengthen a claim,
while failures, deprecations or changed boundaries may narrow one. The central
repository must represent both directions honestly.

## Changes that trigger a synchronization decision

- a public release or completed milestone;
- a changed objective, boundary or non-goal;
- a new evidence type or producer profile;
- a modified public metric, result or limitation;
- a contract or schema compatibility change;
- a repository being replaced, archived or demoted;
- a new dependency or cross-repository integration;
- a failed evaluation that invalidates a central claim.

## Required declaration

Every material pull request should classify central impact as one of:

- **none** — internal change with no effect on public scope or integration;
- **sync-required** — the central index, map, contract or case must change;
- **pending-evidence** — a possible change exists but cannot be claimed yet;
- **deprecation** — a previous central claim or integration must be narrowed or
  removed.

The declaration must explain why and link a central issue when action is
required. Silence is not treated as `none`.

## Synchronization workflow

1. A component PR states its portfolio impact.
2. If impact is material, it opens or links an issue in this repository.
3. The component merges only the evidence it owns.
4. The central PR updates roles, versions, claims, non-claims and integration
   state using the merged producer revision.
5. Links and automated checks are verified.
6. The central issue closes only after the public narrative matches reality.

## Status vocabulary

- **verified** — supported by merged public evidence at a pinned revision;
- **experimental** — executable work exists but the boundary remains a lab;
- **planned** — designed but not implemented;
- **deferred** — deliberately postponed with a recorded reason;
- **deprecated** — retained for history but no longer represents the preferred
  path;
- **pending verification** — change exists but evidence is incomplete.

## Scope hygiene

- New capability does not silently erase an old limitation.
- A failed or negative result is synchronized as evidence, not hidden.
- Simulated evidence never upgrades to observed because a consumer reused it.
- Central wording pins the component release, commit or artifact it describes.
- The central repository summarizes; producer repositories remain authoritative
  for their own implementation evidence.

## Periodic review

The weekly evidence-delivery cycle should include a brief staleness check:

1. Did a component merge a material change?
2. Does the portfolio table still describe its current verified boundary?
3. Do cross-repository links resolve to the intended revision or artifact?
4. Have any non-claims become outdated or been accidentally broadened?
5. Is a planned integration now verified, deferred or deprecated?

This review does not manufacture activity. If nothing material changed, no
central commit is required.
