"""Exact recovery of the selected dyadic physical parameters from saved proposals.
The decimal strings in SELECTED_PROPOSALS round to the same literal D4 endpoints.
This is not a rerun of platform-sensitive optimizer trajectories.
"""
from pathlib import Path
from fractions import Fraction as F
import json
R=Path(__file__).resolve().parent
proposals=json.loads((R/'SELECTED_PROPOSALS.json').read_text());expected=json.loads((R/'PARAMETERS.json').read_text())
for name,entry in proposals.items():
 p=entry['proposal'];r=expected[name];D=r['D'];assert D==4
 assert [round(F(str(x))*D) for x in p['t']]==r['t']
 assert [[round(F(str(x))*D) for x in row] for row in p['A']]==r['A']
print('TWO_COMPLETE_FROZEN_PROPOSALS_RECOVER_LITERAL_D4_PARAMETERS_PASS')
