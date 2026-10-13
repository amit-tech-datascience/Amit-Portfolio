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
Progressive project filtering: `assets/site.js`.

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

`Project_v1` remains private. Only reviewed development aggregates and a written
summary appear here. No private source, datasets, model weights, certificates or
employer materials are copied. Original diagrams are conceptual, not predictions.
No inference service runs here; proposed work is explicitly labeled.

Speech scores/audio and a public downloadable CV are omitted until publishable
materials are verified. Older coursework is linked in the archive. No licensing
terms are invented for the owner's content or third-party work.
