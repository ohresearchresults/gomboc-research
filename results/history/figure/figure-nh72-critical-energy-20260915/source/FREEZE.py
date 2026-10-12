"""The frozen numerical input is only provenance. Literal PARAMETERS defines
our exact endpoint independently of future optimizer trajectories."""
import json
from fractions import Fraction as Q
from pathlib import Path
r=Path(__file__).resolve().parent
s=json.loads((r/'LOCAL_MASS_CHECKPOINT.json').read_text());p=json.loads((r/'PARAMETERS.json').read_text())
z=[round(Q.from_float(float(x))*10**12) for x in s['z'][:12]]
assert z==p['control_numerators'] and p['control_denominator']==10**12
print('EXACT_R12_PARAMETERS_FROM_COMPLETE_FROZEN_PROPOSAL_PASS')
