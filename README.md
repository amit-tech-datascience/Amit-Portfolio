# Amit Amit — Portfolio

Personal portfolio for a Data Scientist at Sedeco Imaging in Gotha, Germany.
Seven case studies, professional experience, education, skills and a DLR
conference contribution. Professional content reviewed 13 October 2026.

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
```

Commit generated `index.html`, `sources.html` and `projects/*.html` with source.
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

Speech scores/audio remain omitted until publishable materials are verified.
Older coursework is linked in the archive. PINN figures link to a pinned source
commit. No licensing terms are invented for the owner's content or third-party work.

## Public resume

`assets/Amit-Amit-Resume.pdf` is a searchable, linked, two-page public resume.
It uses current professional information and excludes the supplied application
bundle's home addresses, phone numbers, personal records, certificates and signatures.
LinkedIn is the public contact method. Review dates and results before each update.

To regenerate, use a separate optional environment with `reportlab==5.0.1`, then
run `python scripts/build_resume.py`. Render and inspect both pages before publishing;
the static website itself has no dependency on ReportLab or any Conda environment.
