#!/usr/bin/env python3
"""Report missing *literal* outputs/data dependencies referenced in notebooks.

This is static analysis and cannot detect paths composed at runtime.
Run at the repo root after restoring outputs and source data.
"""
from pathlib import Path
import json,re
root=Path(__file__).resolve().parents[1]
notebooks=list((root/'notebooks').rglob('*.ipynb'))
refs=set();bad=[]
for p in notebooks:
 try: nb=json.loads(p.read_text(encoding='utf-8'))
 except Exception as e:bad.append((str(p),str(e)));continue
 for c in nb.get('cells',[]):
  if c.get('cell_type')!='code':continue
  s=''.join(c.get('source',[]))
  refs.update(re.findall(r"(?<![A-Za-z0-9_])(?:outputs|data)/[A-Za-z0-9_ .()/\-]+\.(?:csv|json|nt|ttl|parquet|npy|npz|pt|pkl|ifc|zip)",s,re.I))
missing=sorted(x for x in refs if not (root/x).exists())
print(f'Notebooks: {len(notebooks)}; literal referenced paths: {len(refs)}')
print(f'Missing literal paths: {len(missing)}')
for x in missing[:70]:print(' MISSING',x)
if len(missing)>70: print(f' ...and {len(missing)-70} more')
if bad:print('Invalid notebook files:',bad)
print('NOTE: dynamic paths, globs, and absolute file paths require manual review.')
