#!/usr/bin/env python3
"""Capture the *actual running* Python environment, without installing packages."""
import importlib.metadata as md
import json,platform,sys
from pathlib import Path
pkgs=['numpy','pandas','scipy','scikit-learn','xgboost','torch','matplotlib','rdflib','pyshacl','pyoxigraph','ifcopenshell','networkx','jupyterlab','ipykernel','nbformat']
versions={}
for name in pkgs:
    try: versions[name]=md.version(name)
    except md.PackageNotFoundError: versions[name]=None
snapshot={'python':sys.version,'platform':platform.platform(),'packages':versions}
p=Path('environment-original.json');p.write_text(json.dumps(snapshot,indent=2),encoding='utf-8')
print('Saved',p.resolve())
