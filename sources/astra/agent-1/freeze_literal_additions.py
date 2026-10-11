"""Exact convex hull of a complete rational parent plus literal new points.

Qhull proposes supporting triples only. Every proposed plane is checked against
every exact input point. The complete exact H audit must have all its vertices
among those input points; boundedness and both inclusions then identify the same
convex body. Original planar parent faces are never independently rounded.
"""
import pathlib,json,sys,math,hashlib,subprocess
import numpy as np,gmpy2
from scipy.spatial import ConvexHull
from audit_integer import run as audit
from audit_persistence import run as bars
sys.set_int_max_str_digits(0);R=gmpy2.mpq

def run(construction,out):
    construction=pathlib.Path(construction);recipe=json.loads(construction.read_text());parent=pathlib.Path(recipe['parent_audit']);assert hashlib.sha256(parent.read_bytes()).hexdigest()==recipe['parent_audit_sha256'];a=json.loads(parent.read_text());frame=recipe.get('parent_frame','exact-centred')
    if frame=='exact-centred':g=list(map(R,a['centroid']))
    elif frame=='raw':g=[R(0)]*3
    else:raise ValueError('Unknown explicitly specified parent coordinate frame')
    X=[tuple(R(v)-g[j] for j,v in enumerate(row)) for row in a['raw_vertices']]
    for replacement in recipe.get('replace_vertices',[]):
        index=int(replacement['index']);assert 0<=index<len(X);X[index]=tuple(map(R,replacement['point']))
    X+=list(map(lambda row:tuple(map(R,row)),recipe['added_points']));points=np.array([[float(v) for v in row] for row in X]);qh=ConvexHull(points);planes=set()
    for s in qh.simplices:
        a,b,c=[X[int(i)] for i in s];u=[b[j]-a[j] for j in range(3)];v=[c[j]-a[j] for j in range(3)];n=[u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]];h=sum(n[j]*a[j] for j in range(3));assert h!=0
        if h<0:n=[-t for t in n];h=-h
        assert all(sum(n[j]*x[j] for j in range(3))<=h for x in X),'Qhull proposed a plane which fails exact support'
        row=n+[h];D=math.lcm(*(int(t.denominator) for t in row));I=[int(t*D) for t in row];d=math.gcd(*I);planes.add(tuple(t//d for t in I))
    H=list(map(list,sorted(planes)));out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);(out/'H.json').write_text(json.dumps(dict(H=H),separators=(',',':')));(out/'input_points_exact.json').write_text(json.dumps([[str(v) for v in row] for row in X],separators=(',',':')));(out/'construction.json').write_bytes(construction.read_bytes());(out/'parent-audit.json').write_bytes(parent.read_bytes());b=audit(H);verts={tuple(map(R,row)) for row in b['raw_vertices']};assert verts<=set(X),'Exact H-body has a vertex outside the proposed literal input set';(out/'audit.json').write_text(json.dumps(b,separators=(',',':')));print('EXACT_LITERAL_ADDITION_BODY',{k:b[k] for k in ['V','E','F','C','counts','weak','primitive_zero']},flush=True)
    subprocess.run([sys.executable,'certify_boundedness.py',str(out/'H.json'),str(out/'boundedness.json')],check=True);bars(out/'audit.json',out/'bars.json');manifest={p.name:dict(bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in out.iterdir() if p.is_file()};(out/'manifest.json').write_text(json.dumps(manifest,indent=2))

if __name__=='__main__':run(sys.argv[1],sys.argv[2])
