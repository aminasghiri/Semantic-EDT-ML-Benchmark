# Semantic Energy Digital Twin: Machine Learning Benchmark and Reproducibility

### Comparing Tabular, Sequential, and Graph-Based Representation–Model Pipelines

This repository provides the experimental code, selected results, and supporting materials for the research manuscript:

**Data Representation Paradigms in Semantic Energy Digital Twins: Comparing Tabular, Sequential, and Graph-Based Representation–Model Pipelines**

*Submitted to Energy Informatics — Under Review.*

The study investigates short-term indoor temperature forecasting using different machine learning representation–model pipelines derived from a common semantic Energy Digital Twin (EDT).

The experiments use real-world building operational data from Tallinn University of Technology (TalTech), Estonia, and compare tabular, sequential, and graph-based learning approaches under controlled experimental conditions.

The repository is intended to support methodological transparency, experimental verification, and reproducibility.

> **Repository status:** Research reproducibility package under validation. The archived experimental results have undergone consistency checks, but a complete independent rerun of all notebooks has not yet been performed.

---

## 1. Research Objectives

The study investigates four research questions:

- **RQ1:** How do tabular, sequential, and graph-based representation–model pipelines compare in short-term indoor temperature forecasting?
- **RQ2:** How do temporal dependencies, neighboring-device information, and graph connectivity influence predictive performance?
- **RQ3:** How robust are the evaluated pipelines to missing data, measurement noise, and observed temporal distribution shifts?
- **RQ4:** What methodological role does the semantic Energy Digital Twin play in constructing consistent and traceable machine learning datasets?

The experiments distinguish the effects of data representation, model architecture, input information, temporal characteristics, and graph connectivity.

## 2. Dataset

The experiments use operational measurements and BIM data from the **SmartLivingEPC public building dataset**, associated with the Ehituse Mäemaja building at Tallinn University of Technology (TalTech), Estonia.

**Dataset reference:**

Veliskaki et al. (2025). *SmartlivingEPC public building BIM model and measurements.*

https://doi.org/10.5281/zenodo.15782433

The forecasting experiments use:

| Characteristic | Description |
|---|---|
| Building | Ehituse Mäemaja, TalTech |
| Study period | February 7 – June 27, 2025 |
| Operational devices | 7 |
| Measured variables | Indoor temperature, relative humidity, CO₂ |
| Temporal resolution | 15 minutes |
| Primary forecasting horizon | 15 minutes |
| Additional forecasting horizons | 30, 60, and 120 minutes |
| Historical input context | 60 minutes |
| Training samples | 64,701 |
| Validation samples | 13,825 |
| Test samples | 13,790 |

The forecasting dataset is constructed using chronologically aligned operational observations.

The original TalTech dataset is publicly available from the source referenced above. Raw input files and some large intermediate datasets are not redistributed in this repository.

## 3. Semantic Energy Digital Twin

The semantic data infrastructure combines:

- **IFC:** Representation of building information.
- **Brick Schema:** Semantic modeling of building entities and sensor points.
- **SOSA:** Representation of sensor observations.
- **RDF:** Knowledge graph representation.
- **SPARQL:** Extraction of operational observations.
- **SHACL:** Semantic data validation.

The production RDF graph used in the study contains:

| Characteristic | Value |
|---|---:|
| RDF triples | 2,909,492 |
| Operational observations | 323,266 |
| Operational device identifiers | 7 |
| Semantic points | 21 |

No verified native correspondence between the selected operational UUIDs and individual IFC spaces was available.

Consequently, graph connections between devices were constructed analytically from operational similarities rather than inferred from verified physical or spatial relationships.

## 4. Machine Learning Models

Three representation–model pipelines are evaluated.

| Representation | Models |
|---|---|
| Tabular | Ridge Regression, Random Forest, XGBoost |
| Sequential | Long Short-Term Memory (LSTM), Temporal Convolutional Network (TCN) |
| Graph-based | Graph Convolutional Network (GCN) |
| Reference baseline | Persistence |

The primary forecasting experiment uses equivalent local sensor histories for the tabular and sequential models.

The graph-based experiments additionally investigate the effects of neighboring-device observations and alternative graph connectivity configurations.

## 5. Experimental Scenarios

### Scenario S1 — Nominal Predictive Performance

Evaluates forecasting accuracy using the prepared operational data without additional artificial perturbations.

Complementary experiments examine forecasting horizons of 15, 30, 60, and 120 minutes.

### Scenario S2 — Robustness

Evaluates model sensitivity to controlled perturbations:

- **S2-M:** 10% missing input observations.
- **S2-N:** Gaussian noise with a standard deviation corresponding to 5% of the training standard deviation of each variable.
- **S2-C:** Combined missingness and noise.

Perturbations are applied to evaluation inputs without retraining the models.

### Scenario S3 — Forward Temporal Generalization

Evaluates model performance under chronological training, validation, and testing.

The study also includes a complementary rolling-origin evaluation using four successive temporal periods for Persistence, Ridge, and Random Forest.

### Graph-Based Experiments

Additional experiments investigate:

- Native graph configuration without inferred inter-device connections.
- Operational-similarity graph constructed from training data.
- Degree-preserving shuffled graph.
- Local and neighboring-device information ablations (H1–H5).
- Alternative graph topologies.
- Sensitivity to the nearest-neighbor parameter \(k\).

### Statistical Evaluation

Model comparisons include paired temporal block-bootstrap analyses to assess uncertainty in predictive performance differences.

## 6. Semantic Evaluation and Data Consistency

Complementary experiments assess the methodological contribution of the semantic infrastructure.

| Experiment | Purpose |
|---|---|
| E3-J | Semantic observation completeness and identifier consistency |
| E4-B | Cross-stage correspondence between RDF observations and aligned learning samples |
| E5-A | Reconciliation of source CSV observations with RDF/SPARQL exports |
| E5-B | Comparison of CSV-based and RDF-derived analytical preparation |
| ICEIS-related indicators | Descriptive interoperability, query-performance, and temporal-quality evaluation |

The E5 comparison confirms that equivalent preparation procedures produce matching analytical records.

However, this equivalence does not demonstrate that RDF improves predictive accuracy or data-preparation efficiency relative to conventional CSV processing.

The bounded RDF construction, SHACL validation, and SPARQL extraction experiment in E5-B involves **1,500 observations** and does not represent a complete reconstruction of the production Brick graph.

The E4-B lineage audit and E5-B temporal preparation also employ different timestamp-grouping conventions:

- E4-B uses 15-minute floor-based grouping for candidate matching.
- E5-B uses alignment to the nearest 15-minute grid point.

These experiments address different methodological questions and should not be interpreted as equivalent lineage-validation procedures.

## 7. Repository Structure

```text
Semantic-EDT-ML-Benchmark/
│
├── notebooks/
│   ├── data_semantic_pipeline/
│   ├── forecasting/
│   ├── graph_experiments/
│   ├── statistics_temporal/
│   ├── semantic_audits/
│   └── figures/
│
├── evidence/
│   └── Selected archived experimental results
│
├── scripts/
│   ├── capture_environment.py
│   ├── check_archive_evidence.py
│   ├── check_input_paths.py
│   └── restore_outputs.py
│
├── docs/
│   ├── EXPERIMENT_MAP.md
│   ├── RUNBOOK.md
│   ├── RELEASE_CHECKLIST.md
│   └── KNOWN_LIMITATIONS.md
│
├── requirements.txt
├── requirements-original.txt
├── README.md
└── .gitignore
```

The repository contains 47 selected experimental Jupyter notebooks.

Some notebooks represent complementary or alternative experiments and should not be executed indiscriminately in alphabetical order.

## 8. Software Environment

The author's documented computing environment is:

- **Operating system:** Ubuntu 22.04
- **Python:** 3.10.12
- **PyTorch:** 2.9.1+cpu
- **Scikit-learn:** 1.7.1
- **XGBoost:** 3.1.1
- **NumPy:** 2.2.6
- **Pandas:** 2.3.0
- **RDFLib:** 7.1.4
- **pySHACL:** 0.30.1
- **PyOxigraph:** 0.5.11
- **IfcOpenShell:** 0.8.2
- **NetworkX:** 3.4.2

The file `requirements-original.txt` documents the installed Python packages in the author's environment at the time of environment capture.

The file `requirements.txt` contains the selected project dependencies.

**Note:** The environment snapshot has not yet been validated through a complete independent rerun of every experiment.

## 9. Installation

Clone the repository:

```bash
git clone https://github.com/aminasghiri/Semantic-EDT-ML-Benchmark.git
cd Semantic-EDT-ML-Benchmark
```

For a clean Python environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The installation procedure is provided for testing and has not yet been confirmed to reproduce all experiments in a clean environment.

Some dependencies may require additional operating-system packages or platform-specific installation procedures.

## 10. Reproducing the Experiments

Before running the notebooks, consult:

- `docs/EXPERIMENT_MAP.md`
- `docs/RUNBOOK.md`
- `docs/KNOWN_LIMITATIONS.md`

The general workflow is:

1. Obtain the original TalTech dataset.
2. Prepare the operational and semantic data.
3. Construct or restore the required intermediate datasets.
4. Generate the aligned tabular, sequential, and graph-based representations.
5. Execute forecasting experiments S1, S2, and S3.
6. Run complementary graph-based and statistical analyses.
7. Execute the semantic audits and CSV–RDF consistency checks.
8. Compare generated outputs with the archived experimental results.

Many notebooks assume that the working directory corresponds to the repository root.

Some experiments require intermediate files, full RDF graphs, trained models, or output arrays that are not included in this lightweight repository.

### Archived Evidence Verification

Selected archived results can be checked using:

```bash
python scripts/check_archive_evidence.py
```

Static input-path checks can be performed using:

```bash
python scripts/check_input_paths.py
```

These checks validate selected archived evidence and file references; they do not constitute a complete rerun of the research experiments.

### Restoring Additional Outputs

Where authorized, the original research outputs archive can be restored using:

```bash
python scripts/restore_outputs.py "/path/to/outputs(1).zip" --dry-run
python scripts/restore_outputs.py "/path/to/outputs(1).zip"
```

The private outputs archive is not distributed through this repository.

## 11. Reproducibility Status and Limitations

The repository currently provides:

- Experimental notebooks and scripts.
- Selected archived numerical results.
- Documented model configurations and evaluation procedures.
- Semantic validation and data-consistency evidence.
- Software-environment information.
- Instructions for restoring additional experimental files.

However, several limitations remain:

- A complete clean-environment rerun has not yet been performed.
- Some large intermediate datasets and model artifacts are not included.
- The exact execution order and dependencies of all complementary experiments are still being validated.
- The published semantic evaluations do not establish a causal predictive advantage attributable to RDF.
- The available operational dataset does not provide verified native UUID–IFC spatial correspondences.
- A single archived SPARQL query timing does not establish RDF scalability.

These limitations should be considered when interpreting the reported experimental results.

## 12. Data Availability

The original building information and operational measurements are available through the SmartLivingEPC public dataset:

https://doi.org/10.5281/zenodo.15782433

Selected derived experimental results and supporting scripts are included in this repository.

The availability of additional intermediate data and trained models is subject to data redistribution rights, file size, and the research team's release policy.

## 13. Citation

If you use this repository, please cite the associated research manuscript:

Sghiri, A., Gallab, M., Merzouk, S., and Assoul, S.

*Data Representation Paradigms in Semantic Energy Digital Twins: Comparing Tabular, Sequential, and Graph-Based Representation–Model Pipelines.*

**Energy Informatics — Manuscript under review.**

A permanent software archive DOI will be added following the release of a validated version on Zenodo.

## 14. Authors

**Amina Sghiri**  
Mines-Rabat School (ENSMR), LISTD Laboratory, Morocco  
Moroccan School of Engineering Sciences (EMSI), SMARTiLab Laboratory, Morocco

**Maryam Gallab**  
Mines-Rabat School (ENSMR), LISTD Laboratory, Morocco

**Safae Merzouk**  
Moroccan School of Engineering Sciences (EMSI), SMARTiLab Laboratory, Morocco

**Saliha Assoul**  
Mines-Rabat School (ENSMR), LISTD Laboratory, Morocco

## 15. License

A software license has not yet been assigned.

Reuse and redistribution permissions will be specified following verification of the applicable rights and approval by the research team.

---

**Repository status:** Experimental materials are available for methodological inspection and archived-result verification. Full end-to-end reproducibility remains under validation.
