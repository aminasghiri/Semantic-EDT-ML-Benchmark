# TalTech Energy Digital Twin — research reproducibility package (prepublication)

**Status: NOT RELEASE-READY; no full clean-room rerun has been performed.** This package is a curated snapshot of the authors' notebooks and selected *archived* evidence underlying the manuscript *Data Representation Paradigms in Semantic Energy Digital Twins: Comparing Tabular, Sequential, and Graph-Based Representation–Model Pipelines* (Energy Informatics, under review).

## What is included

- `notebooks/`: 47 original experimental notebooks (scientific computations preserved; limited local-path fixes in v2).
- `evidence/`: compact archived outputs and additional summary/protocol results from the original research archives (not newly computed).
- `scripts/check_archive_evidence.py`: checks archived E4-B/E5 result assertions, **not a full experiment rerun**.
- `scripts/restore_outputs.py`: restore author-supplied `outputs(1).zip` to expected `outputs/` location.
- `scripts/check_input_paths.py`: static diagnostic of literal dataset paths, not a complete dependency resolver.
- `scripts/capture_environment.py`: captures actual package versions; **must be run using the original environment**.
- `docs/EXPERIMENT_MAP.md`: provisional notebook-to-paper map; `docs/RUNBOOK.md`: practical workflow and limitations.

## Input data

The public TalTech building data are sourced from SmartLivingEPC: <https://doi.org/10.5281/zenodo.15782433>. Original redistribution rights must be checked. Input files, full production RDF, trained models, and several large arrays are **not included** here. Some notebooks expect `data/` inputs and an `outputs/` directory populated by earlier stages or restored from the private research archive.

## Initial setup

From the repository ROOT (not from within `notebooks/`):

```bash
python -m venv .venv
source .venv/bin/activate       # on Windows: .venv\Scripts\activate
pip install -r requirements-unpinned.txt
python scripts/check_archive_evidence.py
python scripts/check_input_paths.py
jupyter lab
```

The requirements file is derived from detected imports only; it is **not** a tested environment lock and these commands do not guarantee successful notebook runs. For exact version capture, execute `python scripts/capture_environment.py` in the original author's environment and then create/test pinned requirements.

## Using the private outputs archive, where authorized

```bash
python scripts/restore_outputs.py '/path/to/outputs(1).zip' --dry-run
python scripts/restore_outputs.py '/path/to/outputs(1).zip'
python scripts/check_input_paths.py
```

Never commit the full `outputs/`, `data/`, weights, or the private outputs ZIP before examining size, data rights, and privacy. Use a distinct external archive with checksums/DOI for larger reproducibility data, if authorized.

## Run order and verification

See [`docs/RUNBOOK.md`](docs/RUNBOOK.md) and [`docs/RELEASE_CHECKLIST.md`](docs/RELEASE_CHECKLIST.md). Notebooks should be launched from repository root because many assume `Path.cwd()` equals the project directory. The provisional stage order is extraction → reconciliation → semantic graph → SPARQL → temporal preprocessing → aligned representations → forecasting/graph/robustness/statistical audits. **Some notebooks are alternative experiments and should not be executed indiscriminately in sequence.**

### Interpretation and limits

- E5-A/E5-B archived audits reconcile CSV and a **precomputed RDF/SPARQL export**; they do not show that RDF is faster or more predictive.
- E5-B's RDF construction + SHACL + SPARQL demonstration involves **1,500 observations**, not the production graph.
- E4-B temporal lineage auditing groups source timestamps into 15-minute bins using **floor**, while the E5-B preparation rounds to the **nearest** 15-minute grid point: they answer different questions.
- Single archived SPARQL timing is **not** an RDF scalability curve.
- Graph relationships are operational correlations; native UUID–IFC links have not been verified.

**No GitHub upload or Zenodo publication has been performed.** The research team should approve public content, licenses and the final data-release policy before publishing.
