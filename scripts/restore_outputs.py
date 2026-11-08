#!/usr/bin/env python3
"""Safely restore the *author-provided* original outputs archive at repo root.

The outputs ZIP is NOT included in this lightweight public-ready draft.
It may include sensitive/private files: review it before any publication.
"""
import argparse, hashlib, zipfile
from pathlib import Path

def main():
    p=argparse.ArgumentParser()
    p.add_argument('archive',type=Path,help='Path to original outputs(1).zip (not bundled)')
    p.add_argument('--dry-run', action='store_true',help='Check archive without extracting')
    p.add_argument('--overwrite',action='store_true',help='Allow replacement of existing outputs files')
    a=p.parse_args(); root=Path(__file__).resolve().parents[1]
    if not a.archive.is_file(): p.error(f'Archive not found: {a.archive}')
    with zipfile.ZipFile(a.archive) as z:
        bad=z.testzip()
        if bad: raise RuntimeError(f'Corrupted ZIP member: {bad}')
        files=[m for m in z.infolist() if not m.is_dir()]
        for m in files:
            name=Path(m.filename)
            if name.is_absolute() or '..' in name.parts or name.parts[0]!='outputs':
                raise RuntimeError(f'Unsafe or unexpected member: {m.filename}')
            dest=(root/name).resolve()
            if not dest.is_relative_to(root.resolve()): raise RuntimeError(f'Unsafe path {name}')
            if dest.exists() and not a.overwrite and not a.dry_run:
                raise FileExistsError(f'{dest} exists; use --overwrite or remove outputs/')
        print(f'Validated {len(files)} files; total {sum(m.file_size for m in files):,} bytes')
        if a.dry_run: return
        for m in files:
            dest=root/m.filename;dest.parent.mkdir(parents=True,exist_ok=True)
            with z.open(m) as inf, dest.open('wb') as outf:
                import shutil
                shutil.copyfileobj(inf,outf,1024*1024)
        print('Restored to:',root/'outputs')
if __name__=='__main__':main()
