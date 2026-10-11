"""Exact finite moment closure of the three cheap J91 C434 controllers.
Requires the complete immutable J90 core and literal J91_REBALANCED_C434_G18
input/audit. Density remains uniformly one. The two primary apexes do not move.
The corrected VF must pass the complete GMP auditor; no tolerance is evidence.
"""
from fractions import Fraction as F
from pathlib import Path
from itertools import product
import json, sys
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(a,s): return tuple(x*s for x in a)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def load(name): return json.loads((ROOT/name).read_text())
def write(name,obj): (ROOT/name).write_text(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n')

def main():
    base=load('J90_DETACHED_C390_G8_AUDIT.json')
    data=load('J91_REBALANCED_C434_G18_INPUT.json')
    raw=load('J91_REBALANCED_C434_G18_AUDIT.json')
    assert raw['strict']==[2,1,1] and raw['weak']==[0,0,0]
    old=[tuple(map(F,row)) for row in base['vertices']]
    ap=[tuple(map(F,row)) for row in data['apexes']]
    assert len(old)==130 and len(ap)==5
    g=tuple(map(F,base['centroid'])); volume=F(raw['volume'])
    residual=mul(sub(tuple(map(F,raw['centroid'])),g),volume)
    x=old+ap; faces=data['faces']
    cycles=dict(zip(base['active_input_planes'],base['faces']))
    lines=(ROOT/'J90_DETACHED_C390_G8.txt').read_text().splitlines()
    normals=[tuple(map(int,row.split())) for row in lines[1:]]
    ids=[6,43,63]; cap_vol=[]; tangent_options=[]
    for k,fi in enumerate(ids):
        vertex=130+k; cy=cycles[fi]
        observed={frozenset(f) for f in faces if vertex in f}
        expected={frozenset((a,b,vertex)) for a,b in zip(cy,cy[1:]+cy[:1])}
        assert observed==expected, ('not an isolated pyramid',fi)
        w=x[vertex]; v=F(0)
        for j in range(1,len(cy)-1):
            a,b,c=(old[q] for q in (cy[0],cy[j],cy[j+1]))
            dv=-det(sub(a,w),sub(b,w),sub(c,w))/6
            assert dv>0
            v+=dv
        cap_vol.append(v)
        n=normals[fi]
        tangent_options.append([(0,n[2],-n[1]),(-n[2],0,n[0]),(n[1],-n[0],0)])
    chosen=None
    for ts in product(*tangent_options):
        delta=det(*ts)
        if delta:
            chosen=(ts,delta);break
    assert chosen is not None
    ts,integer_det=chosen
    cols=[mul(t,v/4) for t,v in zip(ts,cap_vol)]
    den=det(*cols); rhs=mul(residual,-1)
    ss=[det(rhs,cols[1],cols[2])/den,det(cols[0],rhs,cols[2])/den,det(cols[0],cols[1],rhs)/den]
    shifts=[mul(t,s) for t,s in zip(ts,ss)]
    final_residual=residual
    for k,(fi,t,s,shift) in enumerate(zip(ids,ts,ss,shifts)):
        assert dot(normals[fi],shift)==0
        x[130+k]=add(x[130+k],shift)
        final_residual=add(final_residual,mul(shift,cap_vol[k]/4))
    assert final_residual==(F(0),)*3
    assert x[133:]==ap[3:]  # unchanged two-apex primary patch
    U=base['U'][0]
    # Exact positive old-body chords for all five added vertices.
    witnesses=[]
    for i,w in enumerate(x[130:],130):
        scores=[dot(sub(w,g),sub(v,w)) for v in old]
        j=max(range(len(old)),key=scores.__getitem__)
        assert scores[j]>0
        witnesses.append(dict(vertex=i,old_witness=j,score=str(scores[j]),score_approx=float(scores[j])))
    # Unique old U remains strictly supporting even after all additions.
    root=old[U]
    assert all(dot(sub(root,g),sub(v,root))<0 for i,v in enumerate(x) if i!=U)
    name='J91_EXACT_CENTER_C434'
    with (ROOT/(name+'_VF.txt')).open('w') as f:
        f.write(f'{len(x)} {len(faces)}\n')
        for p in x:f.write(' '.join(map(str,p))+'\n')
        for cy in faces:f.write(' '.join(map(str,[len(cy),*cy]))+'\n')
    write(name+'_CORRECTION.json',dict(name=name,base='J90_DETACHED_C390_G8',source=data['name'],controller_faces=ids,tangent_vectors=ts,tangent_integer_determinant=str(integer_det),pyramid_volumes=list(map(str,cap_vol)),shifts=[list(map(str,p)) for p in shifts],shift_approx=[list(map(float,p)) for p in shifts],expected_volume=str(volume),expected_centroid=list(map(str,g)),moment_residual=list(map(str,final_residual)),unchanged_primary_apexes=data['apexes'][3:],positive_old_chord_witnesses=witnesses))
    print('J91_EXACT_C434_MOMENT_CLOSURE_INPUT_READY',[(fi,list(map(float,s))) for fi,s in zip(ids,shifts)],flush=True)

if __name__=='__main__':main()
