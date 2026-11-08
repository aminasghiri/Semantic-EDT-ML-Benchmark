# Execution runbook — PRELIMINARY (not end-to-end tested)

This document records *known* path and experiment dependencies. It is not a certified one-click reproducibility pipeline.

## 0. Obtain inputs and verify environment

1. Clone/download repository and run from its **root** (`Path.cwd()` is used by many notebooks).
2. Retrieve the original SmartLivingEPC TalTech data from <https://doi.org/10.5281/zenodo.15782433>; check reuse rights. The original `data/` directory structure expected by extraction and IFC notebooks must be reconstructed and documented from original experimental files.
3. Run `python scripts/capture_environment.py` **in the original scientific Python environment**, preserve the resulting JSON, and create a pinned environment only after an installation test.
4. Optional: restore the author-private `outputs(1).zip` (not bundled), safely via `python scripts/restore_outputs.py /absolute/path/to/archive.zip --dry-run` followed by the extraction command.
5. Run `python scripts/check_input_paths.py` for a *partial* missing-file diagnostic.
6. Run `python scripts/check_archive_evidence.py` for integrity assertions on E4-B and E5 archived summaries.

## 1. Semantic and representation pipeline (provisional)

1. `notebooks/data_semantic_pipeline/1_taltech_extraction_and_audit.ipynb`
2. `notebooks/data_semantic_pipeline/02_ifc_uuid_reconciliation.ipynb`
3. `notebooks/data_semantic_pipeline/02B – Reconciliation Evidence Search..ipynb` (supplementary audit)
4. `notebooks/data_semantic_pipeline/03 — BUILD NATIVE BRICK + SOSA RDF GRAPH.ipynb`
5. `notebooks/data_semantic_pipeline/4 — SPARQL TRACEABILITY FOR G_NATIVE.ipynb`
6. `notebooks/data_semantic_pipeline/5B — Data Quality Audit & Cleaning.ipynb` and/or `5_prepare_ai_ready_dataset_PORTABLE.ipynb` (**verify which alternative was used for manuscript final values**) 
7. `notebooks/data_semantic_pipeline/06 — construction du dataset expérimental et split chronologique.ipynb`
8. `notebooks/forecasting/07A Tabular.ipynb`, `07B Sequential.ipynb`, `notebooks/graph_experiments/07C Graph.ipynb`
9. `notebooks/data_semantic_pipeline/7D – Final Experimental Alignment.ipynb`

**Dependency caveat:** output filenames/roots are not yet completely unified with `evidence/outputs/`. Archived evidence is not a substitute for pipeline-produced `outputs/` files.

## 2. Modeling and analysis (run only after aligned inputs exist)

- S1 tabular and Persistence: `notebooks/forecasting/08A_PERSISTENCE_RIDGE_RF_XGBOOST.ipynb`
- S1 LSTM/TCN: `notebooks/forecasting/08B — LSTM + TCN.ipynb`
- S1 graph: `notebooks/graph_experiments/8C — GCN GRAPH ABLATION.ipynb`
- S2 noise/missingness: `notebooks/forecasting/10_S2_CONTROLLED_PERTURBATION_ROBUSTNESS (3).ipynb`
- S3 distribution shift: `notebooks/statistics_temporal/09 — Temporal Generalization Distribution-Shift Analysis.ipynb`
- Rolling origin: `notebooks/statistics_temporal/E3_K_ROLLING_ORIGIN_TEMPORAL.ipynb`
- Multi-horizon: `notebooks/forecasting/E3_06*`, `E3_07*`, `E3_08*`, `E3_10A*`, `E3_10B*`, `E3_10C*`, `E3_10D*`
- H1–H5: `notebooks/graph_experiments/E3_H_ABLATION_LOCAL_VOISINS_CORRIGE.ipynb`
- Graph topologies: `notebooks/graph_experiments/E3_I_ABLATION_TOPOLOGIES_DISTINCTES.ipynb`
- GCN k-sensitivity: `notebooks/graph_experiments/E3_K_GCN_connectivity_training.ipynb`
- Temporal/block bootstrap: notebooks under `notebooks/statistics_temporal/`

## 3. Semantic supporting audits

- E3-J: `notebooks/semantic_audits/E3_J_AUDIT_CONTRIBUTION_SEMANTIQUE_CHEMINS_CORRIGES.ipynb`
- E4-B: `notebooks/semantic_audits/E4_B_RDF_supervised_final_lineage_audit.ipynb`
- E5-A: `notebooks/semantic_audits/E5_semantic_vs_nonsemantic_preparation_TESTED.ipynb`
- E5-B: `notebooks/semantic_audits/E5_B_semantic_vs_nonsemantic_end_to_end.ipynb`

E4-B uses floor-based 15-minute temporal grouping for potential lineage matches; E5-B uses nearest-bin preparation to compare CSV and RDF-derived analytic records. These are *not interchangeable preprocessing rules*. In E5-B, only a bounded 1,500-observation simplified RDF/SOSA graph receives construction/SHACL/SPARQL testing; the production graph is not rebuilt by that test.

## 4. Verification gates

- Verify all reported manuscript table and figure values with the independently regenerated output files.
- Confirm chronological split, training-only fit of scalers/graph edges, fixed seeds and perturbation randomness.
- Validate H1–H5, graph-topology and k-sensitivity seeds and sample alignment.
- Check required source inputs and original script versions; do not rewrite code just to match the manuscript.
- Re-run in a clean environment; save execution log, precise software/hardware versions and file checksums.
- Check full data licensing and remove secrets/author-local paths and metadata before a public GitHub push.
