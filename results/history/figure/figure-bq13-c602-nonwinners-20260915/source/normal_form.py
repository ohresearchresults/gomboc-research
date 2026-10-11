"""Erase only control entries provably overwritten by the ordered contact plan.
This is an equivalent exact definition, not coordinate rounding or a new body.
"""
import json

def normalize(data):
    z=json.loads(json.dumps(data));n=z['n_supports'];seen={n}
    z['controls'][n]=[0,0,z['grid']]
    for i,deps,axes in z['plan']:
        assert i not in seen and set(deps)<=seen
        for k in axes:z['controls'][i][k]=0
        seen.add(i)
    assert seen==set(range(len(z['controls'])))
    return z
