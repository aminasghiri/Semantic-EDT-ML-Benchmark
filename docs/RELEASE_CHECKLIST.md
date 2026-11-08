# Release gate checklist

- [ ] Remove all remaining personal paths and verify notebook working directories.
- [ ] Capture **actual original** `python`, `numpy`, `pandas`, `scipy`, `scikit-learn`, `xgboost`, `torch`, `rdflib`, `pyshacl`, `pyoxigraph` etc. versions with `scripts/capture_environment.py`.
- [ ] Establish a clean Python environment and record OS/CPU/GPU/CUDA. Do not invent fixed versions.
- [ ] Write a fully tested input-download/unpacking guide for SmartLivingEPC and check its license.
- [ ] Reconstruct or provide required `outputs/` artifacts externally with documented checksums.
- [ ] Test sequential execution for the pipeline on one clean machine; resolve cross-notebook dependencies.
- [ ] Reproduce manuscript Tables 3–12 and Figures 2–10 from notebook outputs, including multi-horizon, GCN, bootstrap and rolling-origin.
- [ ] Verify archived E3-J/E4-B/E5 outputs and compare to manuscript figures/table values.
- [ ] Check notebooks for user identifiers, API tokens, service URLs and output metadata before public release.
- [ ] Decide which model weights and large arrays must be provided for exact evaluation vs training.
- [ ] License repository code only with the authors' authorization; do not assume source-data redistribution rights.
- [ ] Create a tagged GitHub release and Zenodo DOI only after successful verification.
- [ ] Update manuscript Data Availability with a **real**, resolvable DOI (not a placeholder).
