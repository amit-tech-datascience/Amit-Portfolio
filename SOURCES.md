# Content sources — reviewed 13 October 2026

This is a curated snapshot, not a live LinkedIn integration.

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
