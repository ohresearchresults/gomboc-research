"""Exact source vertices plus one literal rational physical apex.
Preserve all original rational coordinates. Only the new absolute-frame apex
is rounded to a declared decimal grid; source centroid is never substituted.
Visible facets, horizon and both hull containments are rechecked exactly.
"""
import sys,json,hashlib
from pathlib import Path
from collections import defaultdict
from math import gcd,lcm
from gmpy2 import mpq as Q
ROOT=Path(__file__).resolve().parents[1];sys.set_int_max_str_digits(0)
sys.path.insert(0,str(ROOT/'sources/full76/decoded/methods/parent'));import check_B
check_B.Q=Q
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def plane(a,b,c):
    n=cross(sub(b,a),sub(c,a));h=dot(n,a)
    assert n!=(0,0,0) and h
    if h<0:n=tuple(-x for x in n);h=-h
    den=lcm(*(int(x.denominator) for x in (*n,h)));v=[int(x*den) for x in (*n,h)];d=gcd(*v)
    return tuple(x//d for x in v)
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def run(src,screen,sample,out,grid=10**14):
    src=Path(src);screen=Path(screen);out=Path(out);out.mkdir(parents=True,exist_ok=False)
    r=json.loads(src.read_text());d=json.loads(screen.read_text());row=next(x for x in d['rows'] if x['sample']==sample)
    X=[tuple(map(Q,p)) for p in r['raw_vertices']];H0=[tuple(map(int,(*n,h))) for n,h in zip(r['normals'],r['offsets'])];c=list(map(Q,r['raw_centroid']))
    p=tuple(Q(int(round((float(c[k])+row['point'][k])*grid)),grid) for k in range(3));D=[h[3]-dot(h[:3],p) for h in H0];assert all(v for v in D)
    visible={i for i,x in enumerate(D) if x<0};assert visible==set(row['visible'])
    ef=defaultdict(list)
    for i,f in enumerate(r['faces']):
        for a,b in zip(f,f[1:]+f[:1]):ef[tuple(sorted((a,b)))].append(i)
    horizon=[e for e,ff in ef.items() if (ff[0] in visible)!=(ff[1] in visible)]
    H=[h for i,h in enumerate(H0) if i not in visible]+[plane(X[a],X[b],p) for a,b in horizon]
    P=X+[p];assert all(dot(h[:3],x)<=h[3] for h in H for x in P)
    body={'H':[list(h) for h in H]};(out/'H.json').write_bytes(B(body))
    (out/'construction.json').write_bytes(B(dict(source=str(src),source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),screen=str(screen),screen_sha256=hashlib.sha256(screen.read_bytes()).hexdigest(),sample=sample,grid=grid,absolute_apex=[str(x) for x in p],source_vertex_coordinates_preserved=True,visible=sorted(visible),horizon=[list(x) for x in horizon])))
    z=check_B.run(body);actual={tuple(map(Q,p)) for p in z['raw_vertices']};assert actual<=set(P) and p in actual
    assert (z['V'],z['E'],z['F'])==(row['V'],row['E'],row['F'])
    (out/'audit.json').write_bytes(B(z));s={k:z[k] for k in ['V','E','F','counts','weak','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};s.update(C2E=2*z['E'],VplusEplusF=z['V']+z['E']+z['F'],audit_sha256=hashlib.sha256(B(z)).hexdigest());(out/'summary.json').write_text(json.dumps(s,indent=2)+'\n');print('EXACT_APEX',sample,s,flush=True)
    return z
if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],int(sys.argv[3]),ROOT/sys.argv[4])
