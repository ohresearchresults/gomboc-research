"""Exact physical freeze of conv(base halfspaces, one added point).
Round ONLY the base halfspace data and the added point. Reconstruct rational
base vertices, preserve all old nonvisible planes, derive rational horizon
planes, verify both hull inclusions, then audit the SAME capped body's own
uniform centroid, true incidence and every equilibrium/weak sign. Independent
triple-plane auditor A runs only if pair-line auditor B first qualifies it.
"""
import sys,json,hashlib,math
from pathlib import Path
from collections import defaultdict
import numpy as np
from gmpy2 import mpq
from support_persistence import ROOT
sys.set_int_max_str_digits(0)
sys.path.insert(0,str(ROOT/'sources/full76/decoded/methods/parent'))
import check_B,check_A
check_B.Q=mpq;check_A.F=mpq
encode=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def primitive(row):
    row=list(map(mpq,row));L=math.lcm(*(int(v.denominator) for v in row));z=[int(v*L) for v in row];g=math.gcd(*z);z=[v//abs(g) for v in z]
    if z[-1]<0:z=[-v for v in z]
    if z[-1]<=0:raise ValueError('a constructed facet passes through the interior origin')
    return tuple(z)
def run(base_path,point_path,out,grid=10**16):
    base_path=Path(base_path);point_path=Path(point_path);out=Path(out);out.mkdir(parents=True,exist_ok=False);H=np.load(base_path);p0=np.load(point_path);base_rows=sorted(set(primitive([*[mpq(int(round(v*grid)),grid) for v in h],1]) for h in H));p=tuple(mpq(int(round(v*grid)),grid) for v in p0);base={'H':base_rows};(out/'base_H.json').write_bytes(encode(base));(out/'cap_point.json').write_text(json.dumps(list(map(str,p)))+'\n')
    report=check_B.run(base);(out/'base_geometry_audit_B.json').write_bytes(encode(report));X=[tuple(map(mpq,v)) for v in report['raw_vertices']];oldplanes=[tuple(map(mpq,[*n,h])) for n,h in zip(report['normals'],report['offsets'])];visible=[check_B.inner(row[:3],p)>row[3] for row in oldplanes];adj=defaultdict(list)
    for i,f in enumerate(report['faces']):
        for a,b in zip(f,f[1:]+f[:1]):adj[tuple(sorted((a,b)))].append(i)
    if not all(len(v)==2 for v in adj.values()):raise ValueError('base incidence is not a closed manifold')
    newplanes=[primitive(row) for i,row in enumerate(oldplanes) if not visible[i]];horizon=[]
    for edge,ff in adj.items():
        if visible[ff[0]]==visible[ff[1]]:continue
        a,b=(X[i] for i in edge);n=check_B.outer(check_B.minus(b,a),check_B.minus(p,a));h=check_B.inner(n,a);newplanes.append(primitive([*n,h]));horizon.append(list(edge))
    final={'H':sorted(set(newplanes))};inputs=set(X)|{p}
    if not all(check_B.inner(row[:3],x)<=row[3] for row in final['H'] for x in inputs):raise ValueError('constructed cap halfspaces exclude a defining point')
    (out/'H.json').write_bytes(encode(final));B=check_B.run(final);(out/'audit_B.json').write_bytes(encode(B));actual={tuple(map(mpq,v)) for v in B['raw_vertices']}
    if not actual<=inputs:raise ValueError('constructed halfspace hull has a vertex outside the defining point hull')
    construction=dict(base_source=str(base_path),base_source_sha256=hashlib.sha256(base_path.read_bytes()).hexdigest(),point_source=str(point_path),point_source_sha256=hashlib.sha256(point_path.read_bytes()).hexdigest(),grid=grid,visible_base_facets=[i for i,v in enumerate(visible) if v],horizon_edges=horizon,two_hull_inclusions_verified=True,definition='convex hull of exact base halfspace body and exact rational cap point',mass='uniform filled volume of that final convex hull')
    (out/'construction.json').write_text(json.dumps(construction,indent=2)+'\n');qualified=B['counts']==[1,1,0] and B['weak']==[0,0,0] and 34<=2*B['E']<500 and not any(B[k] for k in ['face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count'])
    summary={k:B[k] for k in ['V','E','F','counts','weak','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};summary.update(C2E=2*B['E'],VplusEplusF=B['V']+B['E']+B['F'],B_qualified=qualified,independent_A_qualified=False,audit_B_sha256=hashlib.sha256(encode(B)).hexdigest())
    if qualified:
        A=check_A.run(final);(out/'audit_A.json').write_bytes(encode(A));different=[k for k in set(A)|set(B) if A.get(k)!=B.get(k)];(out/'independent_comparison.json').write_text(json.dumps(dict(differing_fields=different),indent=2)+'\n')
        if different:raise ValueError('independent exact auditors disagree')
        summary.update(independent_A_qualified=True,audit_A_sha256=hashlib.sha256(encode(A)).hexdigest())
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print('EXACT_CAP_GOAL_VERIFICATION',summary,flush=True);return summary
if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],ROOT/sys.argv[3],10**int(sys.argv[4]) if len(sys.argv)>4 else 10**16)
