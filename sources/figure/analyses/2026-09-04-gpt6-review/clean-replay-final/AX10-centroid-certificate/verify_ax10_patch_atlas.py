"""Exhaustive exact support-removal atlas through six changed old halfspaces."""
from itertools import combinations
from fractions import Fraction as F
from pathlib import Path
import json
from verify_ax10_centroid_obstruction import POINTS, hull, dot, mass
from verify_ax10_four_face_capacity import hpoly_mass

root = Path(__file__).resolve().parent
fs = hull(POINTS)
w = tuple(-x/3 for x in POINTS['C'])
mandatory = [(f,n,h) for f,n,h in fs if dot(n,w)>h]
remaining = [(f,n,h) for f,n,h in fs if dot(n,w)<=h]
assert len(mandatory) == 4 and len(remaining) == 12
clip = ((F(0),F(1),F(0)),F(0))
source_minus = hpoly_mass([(n,h) for f,n,h in fs]+[clip])
positive_source_moment = mass(POINTS,fs)[1][1]-source_minus['moments'][1]
ledger = []
for count in range(3):
    cases = []
    for ids in combinations(range(12),count):
        retained = [(n,h) for i,(f,n,h) in enumerate(remaining) if i not in ids]
        container = hpoly_mass(retained)
        negative = hpoly_mass(retained+[clip])
        lower = positive_source_moment+negative['moments'][1]
        cases.append(dict(additional_removed_faces=[remaining[j][0] for j in ids],
                          negative_moment=str(negative['moments'][1]), moment_lower=str(lower),
                          moment_lower_decimal=float(lower), closed=lower>0,
                          container_volume=str(container['volume']),
                          container_f_vector=container['f_vector'],
                          container_boundedness=container['boundedness']))
    ledger.append(dict(removed_count=4+count,cases=cases))
    print('REMOVED',4+count,'TOTAL',len(cases),'EXACTLY_EXCLUDED',sum(x['closed'] for x in cases))
assert len(ledger[1]['cases']) == 12
assert all(x['closed'] for level in ledger[:2] for x in level['cases'])
survivors = [x for x in ledger[2]['cases'] if not x['closed']]
assert len(ledger[2]['cases']) == 66 and len(survivors) == 1
assert {frozenset(x) for x in survivors[0]['additional_removed_faces']} == {
    frozenset(('0','H','AY')),frozenset(('0','AW','AY'))}
payload = dict(verdict='ANY_CENTROID_ZERO_SUPERSET_MUST_CROSS_AT_LEAST_SIX_OLD_SUPPORT_PLANES',
               mandatory_four=[list(f) for f,n,h in mandatory], atlas=ledger,
               unique_six_plane_pattern_not_excluded=survivors[0],
               scope='A necessary condition for centroid-zero convex supersets of the fixed AX10 source. The surviving pattern is not a feasibility certificate and not a Goemboc.')
(root/'ax10-patch-atlas.json').write_text(json.dumps(payload,indent=2)+'\n')
print('EXACT_AX10_79_CASE_PATCH_ATLAS_PASS')
