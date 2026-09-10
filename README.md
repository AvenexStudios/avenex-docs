# Avenex Documentation Hub

Public documentation hub for Avenex Studios projects.

## Local preview

```powershell
python -m pip install -r requirements.txt
python -m mkdocs serve -f AvenexRaceControl/mkdocs.yml
```

## Publish

Build both language configurations in order: mkdocs.yml, then mkdocs.es.yml.
Run `python tools/check-docs.py` after building to validate pages and links.
Use mkdocs.es.yml for a Spanish preview.

Public pages are customer documentation only. Keep architecture, QA evidence,
approval history and migration plans in the private product repository docs/.
The product repository versions.json is the version source of truth; update
the public copy and both version pages together after an approved baseline change.

This repository is configured for GitHub Pages through GitHub Actions. In the
repository settings, set Pages source to **GitHub Actions**.

## Projects

- `AvenexRaceControl/` builds the public Avenex Race Control documentation at
  `/AvenexRaceControl/` (English) and `/AvenexRaceControl/es/` (Spanish).
