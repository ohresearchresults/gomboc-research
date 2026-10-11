"""Reproduce every new rational control from the entire saved numerical proposal."""
from pathlib import Path
from fractions import Fraction as Q
import sys,json
s=Path(__file__).resolve().parent
p=json.loads((s/'PARAMETERS.json').read_text());r=json.loads((s/'CHECKPOINT.json').read_text())
assert len(r['z'])==25
assert [round(Q(str(v))*10**12) for v in r['z']]==p['numerators']
assert p['denominator']==10**14
print('EXACT_INTERFACE25_PARAMETERS_FROM_FROZEN_PROPOSAL_PASS')
