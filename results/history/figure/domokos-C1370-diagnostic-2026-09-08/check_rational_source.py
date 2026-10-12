"""Fresh exact rational-source audit; no research verifier imports.

Uses GMP only for faster arbitrary-precision integer multiplication.
    uv run --with gmpy2 python check_rational_source.py SOURCE_DIRECTORY
"""
import csv, gzip, json, sys, time
from pathlib import Path
from collections import defaultdict, Counter
from functools import reduce
from gmpy2 import mpz, gcd, mpq

sys.set_int_max_str_digits(0)

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def rows(path):
    with gzip.open(path,'rt') as f: return [tuple(map(mpz,row)) for row in csv.reader(f)]

def main():
    start=time.monotonic()
    folder=Path(sys.argv[1])/'verified'
    report=json.loads((folder/'exact_report.json').read_text())
    raw=rows(folder/'raw_vertices.csv.gz')
    triangles=[tuple(map(int,t)) for t in rows(folder/'triangles.csv.gz')]
    denom=mpz(report['raw_denominator'])
    # Recompute solid moments directly from the closed oriented triangle surface.
    w=mpz(0); m=[mpz(0)]*3
    planes={}; triangle_planes=[]; occurrences=defaultdict(list)
    for triangle in triangles:
        a,b,c=(raw[i] for i in triangle)
        normal=cross(sub(b,a),sub(c,a)); h=dot(normal,a)
        div=reduce(gcd,(*normal,h)); key=tuple(x//div for x in (*normal,h))
        assert h>0
        planes.setdefault(key,len(planes)); triangle_planes.append(planes[key])
        for i,j in zip(triangle,triangle[1:]+triangle[:1]):
            occurrences[tuple(sorted((i,j)))].append((i,j,planes[key]))
        determinant=dot(a,cross(b,c)); w+=determinant
        for k in range(3): m[k]+=determinant*(a[k]+b[k]+c[k])
    assert w>0
    div=reduce(gcd,(4*w,*m)); scale=4*w//div; offset=[x//div for x in m]
    points=[tuple(scale*v[k]-offset[k] for k in range(3))for v in raw]
    q=scale*denom
    saved=rows(folder/'vertices.csv.gz'); saved_q=mpz(report['centred_denominator'])
    assert all(saved[i][k]*q==points[i][k]*saved_q for i in range(len(raw)) for k in range(3))
    print('Own-volume centroid independently recomputed; exact saved coordinates match',flush=True)
    facets=[]
    for pl in planes:
        n=pl[:3]; h=scale*pl[3]-dot(n,offset)
        side=[h-dot(n,p) for p in points]
        assert min(side)==0 and h>0
        facets.append((n,h,{i for i,x in enumerate(side) if x==0}))
    edges={}
    for e,inc in occurrences.items():
        assert len(inc)==2 and inc[0][:2]==inc[1][:2][::-1]
        if inc[0][2]!=inc[1][2]: edges[e]=(inc[0][2],inc[1][2])
    assert len(points)-len(edges)+len(facets)==2
    print('Convex supports verified:',len(points),len(edges),len(facets),flush=True)
    unstable=[]; degeneracies=[]; witnesses=[]
    for i,p in enumerate(points):
        j,value=max(((j,dot(p,sub(v,p))) for j,v in enumerate(points) if j!=i),key=lambda x:x[1])
        if value<0: unstable.append(i)
        if value==0: degeneracies.append(['vertex',i])
        witnesses.append(dict(vertex=i,witness=j,max_dot=float(mpq(value,q*q))))
    stable=[]
    # Project centroid to each facet plane, then test against EVERY halfspace.
    # This does not reuse a face-cycle/inward-edge predicate.
    for i,(n,h,contact) in enumerate(facets):
        length2=dot(n,n)
        values=[hh*length2-h*dot(nn,n) for j,(nn,hh,_) in enumerate(facets)if j!=i]
        if min(values)>0: stable.append(sorted(contact))
        if min(values)==0: degeneracies.append(['face',i])
    saddles=[]
    for (i,j),(f,g) in edges.items():
        a=points[i]; edge=sub(points[j],a); length2=dot(edge,edge); numerator=-dot(a,edge)
        if not (0<=numerator<=length2): continue
        foot=tuple(length2*a[k]+numerator*edge[k]for k in range(3))
        # An edge is an equilibrium exactly when its radial closest point
        # defines a supporting plane containing that entire edge.
        values=[dot(foot,sub(points[k],a))for k in range(len(points))if k not in(i,j)]
        if max(values)<0 and 0<numerator<length2: saddles.append([i,j])
        elif max(values)<=0: degeneracies.append(['edge',i,j])
    result=dict(V=len(points),E=len(edges),F=len(facets),SUH=[len(stable),len(unstable),len(saddles)],
                C=len(points)+len(edges)+len(facets)-len(stable)-len(unstable)-len(saddles),
                stable=stable,unstable=unstable,saddles=saddles,degeneracies=degeneracies,
                raw_volume=float(mpq(w,6*denom**3)),saved_centroid_coordinates_match=True,
                smallest_positive_vertex_dot=min(x['max_dot']for x in witnesses if x['max_dot']>0),
                nearest_vertex_witnesses=sorted(witnesses,key=lambda x:x['max_dot'])[:15],
                seconds=time.monotonic()-start)
    Path('rational-source-diagnostic.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)

if __name__=='__main__': main()
