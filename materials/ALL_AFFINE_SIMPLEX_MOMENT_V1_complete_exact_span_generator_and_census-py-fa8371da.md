# material-fa8371daf690

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""All affine-simplex chain identities modulo genuine cofacial flat cells.
Requires exact flip_moments.py and native55.txt. Standard-library census:
  python -S affine_moments.py census
No coordinate realization or numerical search is a premise of this census.
"""
from pathlib import Path
from itertools import combinations
from fractions import Fraction as F
from functools import lru_cache
from math import gcd,lcm
import hashlib,json,sys
assert __debug__
HERE=Path(__file__).resolve().parent
SOURCE_PIN=[13811,'7542ef43f2e0e5b4759f076086c8de3539da8ef5051c80dae2a71e778a21faa7']
b=(HERE/'flip_moments.py').read_bytes()
assert [len(b),hashlib.sha256(b).hexdigest()]==SOURCE_PIN
import flip_moments as fm
ORIGINAL_SYSTEM=fm.system

def parity(seq):
    assert len(set(seq))==len(seq)
    return (-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))

def orientations(faces):
    """Coherently orient all polygon boundaries; either global orientation works."""
    faces=[list(c) for c in faces];sign=[None]*len(faces);sign[0]=1
    oriented_edges=[]
    for cy in faces:
        oriented_edges.append({tuple(sorted((a,b))):(1 if a<b else -1)
                  for a,b in zip(cy,cy[1:]+cy[:1])})
    todo=[0]
    while todo:
        i=todo.pop()
        for j in range(len(faces)):
            if i==j:continue
            common=set(oriented_edges[i])&set(oriented_edges[j])
            if not common:continue
            assert len(common)==1
            edge=next(iter(common));s=-sign[i]*oriented_edges[i][edge]*oriented_edges[j][edge]
            if sign[j] is None:sign[j]=s;todo.append(j)
            else:assert sign[j]==s
    assert None not in sign
    out=[cy if s==1 else cy[::-1] for cy,s in zip(faces,sign)]
    edges={}
    for cy in out:
        for a,b in zip(cy,cy[1:]+cy[:1]):
            edges.setdefault(tuple(sorted((a,b))),[]).append(1 if a<b else -1)
    assert all(len(v)==2 and sum(v)==0 for v in edges.values())
    return out

def integer_row(row):
    scale=1
    for x in row.values():scale=lcm(scale,F(x).denominator)
    vals={t:int(F(x)*scale) for t,x in row.items() if x};g=0
    for x in vals.values():g=gcd(g,abs(x))
    assert g>0
    vals={t:x//g for t,x in vals.items()}
    if vals[min(vals)]<0:vals={t:-x for t,x in vals.items()}
    return vals

def restricted_basis(rows,allowed,universe):
    """Exact row-space intersection with vectors supported on allowed columns."""
    order=sorted(set(universe)-set(allowed))+sorted(allowed)
    positions={t:i for i,t in enumerate(order)};piv={};out=[]
    for row in rows:
        v={t:F(c) for t,c in row.items() if c}
        while v:
            t=min(v,key=positions.__getitem__)
            if t not in piv:
                scale=v[t];v={k:c/scale for k,c in v.items()};piv[t]=v
                if t in allowed:
                    assert set(v)<=set(allowed);out.append(integer_row(v))
                break
            s=v[t];v=fm.add_sparse(v,{k:-s*c for k,c in piv[t].items()})
    return out,len(piv)

def build(row):
    old=ORIGINAL_SYSTEM(row);faces=orientations(old['faces']);allowed=set(old['cells'])
    universe=list(combinations(range(10),4));epsilon={}
    for cy in faces:
        for pos in combinations(range(len(cy)),3):
            tri=tuple(cy[p] for p in pos)
            for a in range(10):
                if a in cy:continue
                t=tuple(sorted((a,)+tri));s=parity((a,)+tri)
                if t in epsilon:assert epsilon[t]==s
                else:epsilon[t]=s
    assert set(epsilon)==allowed
    # Each row is the oriented boundary of the abstract 4-simplex (0,i,j,k,l).
    cycles=[]
    for quad in combinations(range(1,10),4):
        five=(0,)+quad
        cycles.append({five[:j]+five[j+1:]: (-1)**j for j in range(5)})
    flats=sorted({tuple(sorted(t)) for cy in faces for t in combinations(cy,4)})
    assert not set(flats)&allowed
    flat_rows=[{t:1} for t in flats]
    rb,full_rank=restricted_basis(cycles+flat_rows,allowed,universe)
    relations=[{t:c*epsilon[t] for t,c in h.items()} for h in rb]
    # Keep all prior exact relations first, then add only independent new ones.
    combined=fm.independent(old['basis']+relations)
    assert len(fm.independent(relations))==len(relations)
    assert len(combined)==len(relations)
    for rel in old['basis']:
        assert len(fm.independent(relations+[rel]))==len(relations)
    assert len(fm.independent(combined+[old['reference']]))==len(combined)+1
    d=dict(old);d['basis']=combined
    d['raw_relations']=126+len(flats)
    d['affine_metadata']={'oriented_faces':faces,'cofacial_flat_cells':flats,
        'epsilon':[[list(t),epsilon[t]] for t in sorted(epsilon)],
        'local_rank':len(old['basis']),'restricted_rank':len(relations),
        'full_relation_rank':full_rank,'ambient_cells':len(universe),
        'affine_cycle_generators':len(cycles)}
    return d

@lru_cache(None)
def _system(row):return build(list(row))
def system(row):return _system(tuple(row))

def census():
    report={'identity':'ALL_AFFINE_SIMPLEX_MOMENT_SPAN_V1',
        'input_pin':fm.INPUT_PIN,'source_pin':SOURCE_PIN,'rows':[]}
    for i,row in fm.inputs().items():
        d=system(row);m=d['affine_metadata']
        report['rows'].append({'native_index':i,'cells':len(d['cells']),
            'old_rank':m['local_rank'],'new_rank':len(d['basis']),
            'new_relations':len(d['basis'])-m['local_rank'],
            'flat_cells':len(m['cofacial_flat_cells']),
            'full_relation_rank':m['full_relation_rank'],
            'system_pin':fm.pin(fm.enc(fm.description(d))),
            'orientation_pin':fm.pin(fm.enc(m))})
    b=fm.enc(report);(HERE/'affine_census.json').write_bytes(b)
    print('ALL_AFFINE_SIMPLEX_EXACT_SPAN_PASS',len(report['rows']),
          sum(r['new_relations'] for r in report['rows']),*fm.pin(b),flush=True)
    return report

if __name__=='__main__':
    if sys.argv[1:]==['census']:census()
    else:raise ValueError('census')
