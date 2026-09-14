# Avenex Documentation Hub

Public documentation hub for Avenex Studios projects.

## Standards

Shared Avenex operating standards live under `standards/`.

- [Codex operating standard](standards/codex-operating-standard.md)
- [GitHub Projects to Jira migration and epic organization](standards/github-to-jira-migration.md)

Product repositories use these standards to define how planning, architecture,
implementation, QA and public documentation work are handled. Customer-facing
pages remain inside each product documentation site.

## Local preview

```powershell
python -m pip install -r requirements.txt
python -m mkdocs serve -f AvenexRaceControl/mkdocs.yml
python -m mkdocs serve -f CoDriverAIRaceEngineer/mkdocs.yml
```

## Publish

Build both language configurations in order: mkdocs.yml, then mkdocs.es.yml for
every project folder. Run `python tools/check-docs.py` after building to
validate pages and links. Use mkdocs.es.yml for a Spanish preview.

Public pages are customer documentation only. Keep product-specific
architecture, QA evidence, approval history and migration plans in the private
product repository docs/.
The product repository versions.json is the version source of truth; update
the public copy and both version pages together after an approved baseline change.

This repository is configured for GitHub Pages through GitHub Actions. In the
repository settings, set Pages source to **GitHub Actions**.

## Projects

- `AvenexRaceControl/` builds the public Avenex Race Control documentation at
  `/AvenexRaceControl/` (English) and `/AvenexRaceControl/es/` (Spanish).
- `CoDriverAIRaceEngineer/` builds the public CoDriver AI Race Engineer
  documentation at `/CoDriverAIRaceEngineer/` (English) and
  `/CoDriverAIRaceEngineer/es/` (Spanish).
