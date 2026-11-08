#!/usr/bin/env python3
"""Check *archived* evidence against key manuscript values; no notebook execution."""
import json,csv
from pathlib import Path
root=Path(__file__).resolve().parents[1]
def load(path):return json.loads((root/'evidence'/path).read_text(encoding='utf-8'))
e5=load('E5_B_results/01_source_reconciliation.json')
e4=load('E4_B_lineage_results/07_e4b_aggregate_summary.json')
e5a=load('E5_comparison_results/01_record_reconciliation.json')
assert e5['raw_rows']==e5['semantic_export_rows']==323266
assert e5['raw_only']==e5['rdf_only']==e5['unit_disagreements']==0
assert e5['max_absolute_value_difference'] < 1e-5
assert e5a['n_common_keys']==323266
assert e4['n_final_samples']==92316 and e4['n_checked_values']==1477056
print('PASS: archived E5-A/E5-B reconciliation and E4-B sample counts')
print('NOTE: This only checks stored evidence files, not RDF reconstruction or full model training.')
