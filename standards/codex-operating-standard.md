# Avenex Codex Operating Standard

## Status

Accepted baseline for new Avenex planning and documentation work.

## Purpose

Avenex projects use Codex as the execution agent for planning support,
architecture drafting, implementation, QA preparation and documentation updates.
There is no separate Kiro layer in this standard.

The product owner remains responsible for product direction, public release
approval, business priorities and any decision that changes user-visible scope.

## Codex Role Modes

Codex must operate in the role that matches the work being performed:

| Role | Use when | Output |
| --- | --- | --- |
| Product / BA / SM | Backlog, tickets, acceptance criteria, prioritization, workflow | Phase plans, tickets, scope, dependencies |
| Architect | Architecture, module boundaries, ADRs, integration strategy, technical risk | ADRs, architecture notes, migration plans |
| Developer | Code, refactors, tests, build/lint verification, release wiring | Commits, implementation notes, verification evidence |
| Tester | Manual QA, repro steps, validation gates, regression risk | Test plans, evidence checklist, approval criteria |
| Docs | Public/customer docs and private product docs | MkDocs pages, internal docs, validation results |

Codex may switch roles within a task, but must make role-sensitive decisions
explicit. For example, architecture changes should be written as ADRs or
architecture notes before implementation tickets are executed.

## Repository Responsibilities

### Product repositories

Product repositories are the source of truth for:

- Runtime code and assets needed to build, test, install and run the product.
- Product-specific architecture and ADRs.
- Planning, tickets, tracker state and phase review notes.
- QA evidence, manual validation and troubleshooting used by development.
- Private migration plans and internal risks.

### `avenex-docs`

`avenex-docs` is the source of truth for:

- Shared Avenex operating standards.
- Public customer-facing product documentation.
- Public installation, admin, user, troubleshooting, versions and downloads
  pages.

Public docs must not expose private tickets, internal approval history,
unapproved architecture, secrets, private migration notes or incomplete plans.

## Planning Rules

- Use phase plans for cohesive deliverables.
- Use small tickets with clear repository ownership.
- Every ticket must state its owning repository and whether it changes runtime,
  private docs, public docs or tooling.
- Split public documentation tickets from runtime implementation unless the docs
  change is required to make the implementation usable.
- Keep customer docs aligned with approved behavior, not aspirational backlog.

## Ticket Shape

Use this minimum shape unless a product repository has a stricter template:

```markdown
# <ID> — <Title>

**Status:** NOT-STARTED
**Repository:** <repo-name>
**Area:** <Runtime | Architecture | Private Docs | Public Docs | QA | Tooling>

## Goal

## Scope

## Out of Scope

## Acceptance Criteria

## Evidence

## Notes
```

Cross-repository work should be split into separate tickets whenever possible.
When one ticket must touch multiple repositories, list each repository and the
expected change in `Scope`.

## Architecture Rules

- Product modules communicate through explicit capabilities and events.
- Feature modules must not hard-depend on other feature modules.
- Product-specific architecture belongs in the product repository.
- Shared operating standards belong in `avenex-docs/standards`.
- Public docs describe approved user behavior only.

## Verification Rules

For product repositories:

- Run the repository's build, test and lint checks for implementation changes.
- Add focused tests for new behavior or regressions.
- Keep troubleshooting entries for repeated build, launch or runtime failures.

For `avenex-docs`:

- Build every affected MkDocs language configuration.
- Run the docs validation script when available.
- Preserve language parity for public docs.
- Keep product version metadata consistent.

## Git Rules

- Prefer trunk-based development with small, reviewable commits.
- Do not batch unrelated tickets.
- Keep repo-specific commits in the repository that owns the change.
- Do not commit local reference clones, generated caches or secrets.

## Approval Rules

Product owner approval is required before:

- Publishing new customer-facing documentation.
- Changing product scope or release policy.
- Introducing paid external services into runtime behavior.
- Moving private planning or architecture content to public documentation.

Codex can draft the work and prepare tickets, but should not treat drafts as
approved public release content until the product owner approves them.
