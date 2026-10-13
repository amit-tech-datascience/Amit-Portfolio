# Amit Portfolio

Public, dependency-free static portfolio for `amit-tech-datascience/Amit-Portfolio`.

- Source content and HTML generation: `scripts/build.py`.
- Design: `assets/style.css`; progressive project filtering: `assets/site.js`.
- Build: `python scripts/build.py` (Python standard library only).
- Validate: `python scripts/check.py`.
- Preview: `python -m http.server 8080 --bind 127.0.0.1`.
- GitHub Pages: `main`, root folder. Commit generated HTML alongside source.
- No Conda environment, package installation, API keys, backend or database required.

Preserve accurate attribution and evidence boundaries. Distinguish personal,
academic, collaborative and employment work. Keep PCB metrics labeled development;
never imply an independent benchmark or production performance. Keep private
Project_v1 code, models, dataset archives and employer materials out of this repository.
The owner-approved exception is three licensed VisA inputs and their qualitative
overlays in assets/inspection; preserve attribution and recorded provenance.
Do not publish personal records, certificates, private profile fields or credentials.
Use relative site links so the site works under `/Amit-Portfolio/`.
Record new factual sources in `SOURCES.md`. Do not invent results or dates.

Recorded evidence rendering: scripts/evidence.py. Public resume source:
scripts/build_resume.py (optional reportlab dependency); generated PDF is committed.
Never copy the source application bundle or its records into the public repository.

## Bilingual maintenance (owner preference)

Always update English AND German together, including both resumes when facts change.
English at the repository root is always the default. German pages live under `de/`.
Do not add browser-language redirects, cookies or stored language preferences.
`scripts/build.py` generates both locales with shared templates; `scripts/de.json`
contains reviewed translations. Missing/changed English text must block the build
until its German entry is updated. Never silently fall back to English on German pages.
Translate navigation, labels, alt text, metadata, results and limitations as well as prose.
Preserve names, official qualifications, metrics, attribution and honest language levels.
`scripts/build_resume.py` generates both PDFs; update `scripts/resume_de.json` with it.
Run both builders, `scripts/check.py`, and `scripts/check_bilingual.py`. Render and
inspect all PDF pages, and test language switching, mobile layouts, gallery controls,
filters and both downloads before publishing. Commit all 18 HTML pages and both PDFs.
For resume changes, also run `scripts/check_resumes.py` in the optional PDF environment
(reportlab, pypdf, pypdfium2). It checks complete text extraction and reading order
in two engines. Do not describe these local checks as a universal ATS or AI-detector
pass. Preserve LinkedIn-only public contact unless Amit changes that preference.
