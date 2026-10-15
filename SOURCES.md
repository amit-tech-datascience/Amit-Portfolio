# Content sources — reviewed 13 October 2026

This is a curated snapshot, not a live LinkedIn integration.

## Incident Lab addition - reviewed 15 October 2026

- Owner requested a public portfolio update for private Project_v2. Reviewed
  `docs/progress.md`, `docs/architecture.md`, `docs/portfolio-case-study.md`,
  `docs/release-checklist.md` and the v0.3.2 release records. Runtime source freeze:
  `c28f5be75842bc7405c11cc8ece49418663179fc`; delivery record: `21158e5`.
- Original synthetic campaigns: AI ML 5/9 and generic 6/9; later v0.3.1 campaigns:
  AI ML 9/9 and generic 8/9. Full-evidence rules matched 9/9 in all four. Each
  denominator includes scheduled failures and controls/abstentions. These are
  separate campaigns on known fault families, not an independent improvement
  estimate. v0.3.2 adds no new diagnosis-quality score.
- Delivery: 134 Python tests; JavaScript checks; successful clean Windows/Linux
  CI run 38721134019. Portable saved demo: 36 observation windows, 72 jobs,
  64 completed and eight failed. Mock cooldown/restart drill: two scripted HTTP
  responses, zero external calls, no retry of the original failed attempt.
- Original project attribution: solo, AI-assisted engineering. Independent human
  review and a physical second-PC exercise remain deferred. No production
  availability, autonomous remediation, model superiority or people-management
  claim. Groq live-tested; OpenAI adapter not verified live.
- Public scope: original editorial text, conceptual architecture flow and aggregate
  result table only. No copied implementation, snapshots, databases, screenshots,
  raw telemetry, source ZIP, provider configuration or credentials. The private
  release is not advertised as publicly downloadable; contact stays LinkedIn-only.
- Both English and German pages and the two maintained public resumes are updated.
  Other professional history and project evidence retain their earlier review dates.
- Portfolio validation: 20 generated pages pass link/accessibility-structure and
  bilingual parity checks; JavaScript syntax passes. Both two-page PDFs pass
  extraction and reading-order checks in pypdf and PDFium; all four rendered
  pages were visually inspected. Browser checks cover desktop/mobile layouts,
  bidirectional language switching, project filtering, gallery controls in both
  languages and both PDF downloads (matching local hashes), with no console errors.

The English and German pages share the same reviewed facts and evidence. German
translations cover all portfolio pages, labels and metadata; both public resumes
preserve English C1 / German A2. Official names, degree titles, source repositories,
external documents and machine-readable provenance may remain in their source language.

- Professional experience and education: https://www.linkedin.com/in/amit-tech/
- Speech enhancement: owner's LinkedIn description; CPC, HiFi-GAN,
  LJ Speech/Libri-Light, EffCRN comparison, NISQA/PESQ/DNSMOS. No verified public
  repository, metric values or shareable audio.
- Landslide: https://deep-learning-igp-tubs-sose2023.github.io/Group_C/
  Reiko Lettmoden and Amit Amit. F1 .721 baseline / .756 augmented Lovasz UNet.
  Half of original training data, locally split; not official test scores.
- Thesis: https://github.com/muecke-math/Master-Amit-Amit
  Adapts TensorDiffEq and pinns-tf2. Final numeric comparison not established.
- App: https://github.com/ak06645/rick-and-morty-ai-app
  Manifest and chat route checked. Live demo not verified.
- Leakage: https://github.com/ak06645/FPDS_Final
  Standard/equivariant experiments; no unverified metric claim.
- Water: https://github.com/ak06645/Acea-Smart-Water-Analytics
  Aquifer preprocessing, chronological split, XGBoost; lake and river notebooks.
- Coursework: https://github.com/ak06645/Project_2 (VGG19 style transfer),
  https://github.com/ak06645/Project_3 (GRU text generation),
  https://github.com/ak06645/Mini-Project-ML (KNN/validation).
- Conference: https://elib.dlr.de/220248/
  Janko Kreikemeier, Amit Amit, Steffen Opitz. Conference speech, Singapore,
  2 December 2025. Not refereed; restricted PDF not redistributed.
- Inspection: private Project_v1 README, docs/progress.md, docs/data_protocol.md
  and local aggregate evaluation records reviewed read-only. PCB2 full256 /
  roi256 / roi512: detection 36/50, 41/50, 43/50; false alarms 3/50, 2/50, 1/50;
  AUROC .9308, .9564, .9888; median decode+inference 22.8, 25.2, 38.5 ms.
  Custom development split; independently normal-calibrated models; physical
  independence unestablished; near-duplicates unadjudicated. RTX 5070 Ti Laptop
  GPU warm-cache batch-one, 3 warmups/20 repetitions. Innodisk roi512 AUROC .5023,
  false alarms 3/4. No independent final evaluation. Aggregate evaluations not rerun.
  One false-alarm overlay regenerated using the frozen model; score, crop and
  artifact hash matched the saved evaluation. No retraining or weight download.

## Public resume and new evidence

- Owner-supplied resume/application bundle reviewed locally, including the two CV
  pages. Public resume reconciled with current LinkedIn details (Sedeco, Gotha).
  Education: M.Sc. Oct 2021-Jun 2025; B.Tech. Electronics and Communication
  Engineering, New Delhi, Aug 2014-Jun 2018. Languages: English C1, German A2.
  The source bundle, contact details, personal records and certificates are private.
- Selected VisA examples and qualitative model overlays: see
  [attribution](assets/inspection/ATTRIBUTION.md) and
  [exact scores and provenance](assets/inspection/examples.json).
  Three selected outcomes from development data; not a representative sample.
  Source inputs unchanged; overlays crop and resize inputs and add anomaly color.
- Landslide chart: selected F1 results from the linked team report: baseline
  .721, RGB+height .718, augmented CE .736, augmented Lovasz .756,
  augmented Swin-UNet Lovasz .745. Zero-based 0-1 scale; no new evaluation.
- PINN figure/script links pinned to commit
  b91b3aaace9229319ca4f3c85e90055be5766d0a, authored by ak06645, 14 April 2025.
  TensorDiffEq/examples/Allen-Cahn/Baseline/train includes AC_SA_baseline.png,
  AC_residual.png and AC_absolute_error.png; related script AC-SA-new.py.
  Configuration is associated source, not a verified execution manifest.
  Figures are linked, not copied; underlying frameworks are credited.

Design references: https://huyenchip.com/ , https://eugeneyan.com/ ,
https://madewithml.com/ , https://brittanychiang.com/ . Original implementation;
no reference-site code, branding, photos or illustrations copied.
