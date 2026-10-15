# Amit Amit — Portfolio

Personal portfolio for a Data Scientist at Sedeco Imaging in Gotha, Germany.
Eight case studies, professional experience, education, skills and a DLR
conference contribution. Professional history reviewed 13 October 2026;
Incident Lab added from verified v0.3.2 delivery records on 15 October 2026.

## Local preview

Open `index.html` directly, or run:

```powershell
python -m http.server 8080 --bind 127.0.0.1
```

Visit http://127.0.0.1:8080/ . Plain HTML, CSS and JavaScript: no Conda environment,
Node installation, API keys, backend, database or paid services required.
Python 3.10+ is only used for the optional preview, generator and checker.

## Edit and verify

Content/templates: `scripts/build.py`. Design: `assets/style.css`.
Progressive project filtering and recorded-example controls: `assets/site.js`.
Evidence gallery and charts: `scripts/evidence.py`.

```powershell
python scripts/build.py
python scripts/check.py
python scripts/check_bilingual.py
```

Commit generated `index.html`, `sources.html`, `projects/*.html` and their `de/`
counterparts with source.
All content/navigation works without JavaScript. No external fonts or analytics.

## GitHub Pages

Repository: https://github.com/amit-tech-datascience/Amit-Portfolio

1. Push `main`.
2. Settings → Pages → Deploy from a branch → `main` → `/(root)` → Save.
3. Wait for deployment, then visit https://amit-tech-datascience.github.io/Amit-Portfolio/ .

`.nojekyll` disables Jekyll. Committed HTML is the deployment output, with no
production compilation or environment variables. Relative links support the
`/Amit-Portfolio/` path. A custom domain is optional.
[Official setup](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site).

## Sources and boundaries

See [SOURCES.md](SOURCES.md) and `sources.html`. LinkedIn was read through Amit's
signed-in browser; there is no persistent integration or automatic sync.
Public contact uses LinkedIn only.

`Project_v1` remains private. Reviewed development aggregates and three selected
CC BY 4.0 VisA inputs with qualitative model overlays appear here. Attribution,
exact scores, hashes and preprocessing notes are in `assets/inspection/`.
No private source, dataset archives, model weights, certificates or employer
materials are copied. Conceptual diagrams and recorded outputs are distinguished.
The gallery browses saved predictions; it does not run an inference service.

`Project_v2` (Incident Lab) also remains private. The public English/German case
study summarizes architecture, separately labelled synthetic campaign results,
operational checks and delivery evidence. It links to LinkedIn for a walkthrough,
not an inaccessible private repository or a live application. No source code,
saved databases, release ZIPs, raw telemetry or credentials are copied. Independent
review and physical second-PC verification remain deferred. Both maintained
resumes include Incident Lab among the selected projects.

Speech scores/audio remain omitted until publishable materials are verified.
Older coursework is linked in the archive. PINN figures link to a pinned source
commit. No licensing terms are invented for the owner's content or third-party work.

## Public resume

`assets/Amit-Amit-Resume-EN.pdf` and `assets/Amit-Amit-Lebenslauf-DE.pdf` are
searchable, linked, two-page public resumes in English and German.
It uses current professional information and excludes the supplied application
bundle's home addresses, phone numbers, personal records, certificates and signatures.
LinkedIn is the public contact method. Review dates and results before each update.

To regenerate, use a separate optional environment with `reportlab==5.0.1`, then
run `python scripts/build_resume.py`. It builds both languages and rejects missing,
obsolete or empty German translations in `scripts/resume_de.json`. Render and inspect
all four pages before publishing;
the static website itself has no dependency on ReportLab or any Conda environment.

For local PDF readability checks, add `pypdf` and `pypdfium2` to that optional
environment and run `python scripts/check_resumes.py --render .qa/resume-review`.
The checker verifies every source paragraph and its reading order in two independent
PDF engines, visible profile URLs, page bounds, language metadata and HTTPS links.
These checks are not a commercial ATS certification, AI-authorship score or a
job-specific ranking. Keep actual contact information in the page body, expand
relevant abbreviations, and never add hidden keywords or unsupported achievements.
The public downloads intentionally use LinkedIn-only contact. Private applications
may require a direct email and phone in the application form or a separate private CV.

The earlier `assets/Amit-Amit-Resume.pdf` remains available for old shared links;
the language-labelled downloads above are the maintained versions.

## English and German

English is always the default at the root URL. German pages live in `de/`.
There is no automatic language detection, redirect, cookie or remembered preference.
The native dropdown works with keyboard and without JavaScript. Switching keeps
the matching page, and JavaScript also preserves the current section anchor.
Internal navigation stays in the chosen language. Both PDF languages are offered
on both homepages; the navigation download follows the current page language.

**Always update both languages together**, as requested by Amit. English content is
in `scripts/build.py` and `scripts/evidence.py`; reviewed German translations are in
`scripts/de.json`. The shared HTML parser translates text, accessibility labels and
metadata at build time and adjusts local URLs. Missing, obsolete or empty translations
stop the build before any pages are written. Names, official degree titles and code
identifiers intentionally retain their original spelling. Numeric text uses German
decimal commas; underlying scientific values and JSON provenance are unchanged.

When a fact changes, update both resumes as well. Run both builders and both check
scripts, inspect desktop/mobile layouts and PDF pages, then commit all generated files.
No online translation service or additional runtime dependency is used.
