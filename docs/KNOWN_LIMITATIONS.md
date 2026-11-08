# Current release blockers — checked 2026-11-08

1. **Full rerun not performed.** Archived checks pass only for selected E4-B/E5 summaries; training and graph construction are computationally substantial.
2. **Large required inputs absent from lightweight archive:** source TalTech data, full production RDF, private outputs archive, trained models and certain array artifacts. The `restore_outputs.py` helper makes original outputs usable when legitimately available, but does not replace regeneration.
3. **Exact original environment unknown.** `requirements-unpinned.txt` is not a validated reproducibility specification.
4. **Notebook working-directory assumption.** Launch from the repo root, not notebook folders. `check_input_paths.py` can only identify literal references; a complete path audit requires executing each stage.
5. **E4-B vs E5-B temporal mapping differs by design:** floor vs nearest bin. Verify this distinction in manuscript supplementary explanations.
6. **Graph experiment coverage:** extra E3-H2, E3-I2 and E3-K evidence summaries are incorporated in V3, but complete reruns and verification against all published figures remain pending.
7. **Public rights and confidentiality:** inspect author-supplied `outputs/`, SmartLivingEPC license, notebooks' metadata and dataset filenames before publication.
8. **Integrity:** V3 includes SHA-256 checksums of *bundled* files; this establishes package integrity only, not scientific validity.

9. Verified path correction: E3_08_common_multihorizon_evaluation notebook now refers to `outputs/07D_final_alignment/01_final_common_sample_keys.csv`, matching the original private outputs archive. No model calculation was changed.
