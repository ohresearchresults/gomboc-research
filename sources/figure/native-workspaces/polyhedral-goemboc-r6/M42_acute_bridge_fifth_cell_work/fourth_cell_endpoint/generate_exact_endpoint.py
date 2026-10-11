#!/usr/bin/env python3
"""Deterministically regenerate and independently verify the exact M42 fourth-cell endpoint.

The complete authoritative input is input_rows_common_lattice.csv.  The exact
construction provenance is construction.json.  No search state is required.
"""
from pathlib import Path
import csv,json,subprocess,sys
R=Path(__file__).resolve().parent
rows=list(csv.DictReader(open(R/'input_rows_common_lattice.csv')))
ids=sorted(int(r['source_id']) for r in rows);assert len(rows)==140 and len(set(ids))==140 and ids[-1]==228
S={int(r['denominator']) for r in rows};assert len(S)==1
C=json.load(open(R/'construction.json'));assert C['new_rows']==list(range(223,229)) and C['absorbed_rows']==[130,153,154,176,182,201,220,221,222]
subprocess.run([sys.executable,str(R/'build_exact_endpoint.py')],check=True,cwd=R)
subprocess.run([sys.executable,str(R/'verify_exact_cleanroom.py')],check=True,cwd=R)
print('PASS deterministic finite endpoint regeneration from 140 exact lattice rows; common scale',next(iter(S)))
