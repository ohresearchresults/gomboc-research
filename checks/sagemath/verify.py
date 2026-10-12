"""Exact reconstruction and equilibrium census using SageMath's PPL backend.
Run: sage -python verify.py input.json output.json [reference-report.json]
Input: {"H": [[a,b,c,d], ...]} describes a*x+b*y+c*z <= d.
No imports from the original search or verification programs.
"""
import json, sys, time, platform
from pathlib import Path
from sage.all import QQ, Polyhedron, vector, matrix
from sage.env import SAGE_VERSION

def check(rows):
    start=time.monotonic()
    P=Polyhedron(ieqs=[[QQ(h[3])]+[-QQ(a) for a in h[:3]] for h in rows],base_ring=QQ,backend='ppl')
    if P.dim()!=3 or not P.is_compact(): raise ValueError('Expected bounded full-dimensional polyhedron')
    print('Reconstructed',P.f_vector(),flush=True)
    g=P.centroid(engine='internal')
    vol=P.volume(engine='internal')
    print('Computed volume centroid',flush=True)
    V=[vector(QQ,v) for v in P.vertices_list()]
    inequalities=list(P.inequalities())
    if not all(h.b()+h.A().dot_product(g)>0 for h in inequalities):raise ValueError('Centroid not interior')
    strict=[0,0,0];weak=[0,0,0]
    # Unstable vertices: the radial vector supports the body at this vertex.
    for v in V:
        zero=False
        for w in V:
            if w==v:continue
            z=(v-g).dot_product(w-v)
            if z>0:break
            zero=zero or z==0
        else:
            if zero:weak[1]+=1
            else:strict[1]+=1
    print('Vertex census complete',flush=True)
    # Stable facets: the perpendicular foot must lie in the facet polygon.
    for h in inequalities:
        a=h.A();foot=g-(h.b()+a.dot_product(g))/a.dot_product(a)*a
        zero=False
        for k in inequalities:
            if k==h:continue
            z=k.b()+k.A().dot_product(foot)
            if z<0:break
            zero=zero or z==0
        else:
            if zero:weak[0]+=1
            else:strict[0]+=1
    print('Facet census complete',flush=True)
    # Saddle edges: interior segment foot and nonnegative outward normal coefficients.
    for face in P.faces(1):
        x,y=[vector(QQ,v) for v in face.vertices()];d=y-x
        t=(g-x).dot_product(d)/d.dot_product(d)
        if not 0<=t<=1:continue
        foot=x+t*d
        normals=[-h.A() for h in inequalities if h.b()+h.A().dot_product(x)==0 and h.b()+h.A().dot_product(y)==0]
        if len(normals)!=2:raise ValueError('Edge must have two maximal adjacent facets')
        N=matrix(QQ,normals).transpose();weights=(N.transpose()*N).solve_right(N.transpose()*(foot-g))
        if N*weights!=foot-g:raise ValueError('Projection not in normal span')
        if min(weights)>0 and 0<t<1:strict[2]+=1
        elif min(weights)>=0:weak[2]+=1
    return {'V':len(V),'E':len(P.faces(1)),'F':len(inequalities),'strict':strict,'weak':weak,
        'volume':str(vol),'centroid':[str(x) for x in g],'vertices':[[str(x) for x in v] for v in V],
        'seconds':round(time.monotonic()-start,3)}

if __name__=='__main__':
    tetra=[[-1,-1,-1,1],[-1,1,1,1],[1,-1,1,1],[1,1,-1,1]]
    cube=[[s if j==i else 0 for j in range(3)]+[1] for i in range(3) for s in [-1,1]]
    weak_prism=[[1,0,0,1],[-2,3,0,1],[1,-3,0,1],[0,0,1,1],[0,0,-1,1]]
    fixtures=[]
    for rows,expected,expected_weak in [(tetra,[4,4,6],[0,0,0]),(cube,[6,8,12],[0,0,0]),(weak_prism,[4,4,6],[1,2,3])]:
        r=check(rows)
        if r['strict']!=expected or r['weak']!=expected_weak:raise ValueError('Fixture failure: '+str((r['strict'],r['weak'])))
        fixtures.append({'strict':r['strict'],'weak':r['weak']})
    r=check(json.loads(Path(sys.argv[1]).read_text())['H'])
    r.update(sage_version=SAGE_VERSION,backend='ppl',base_ring='QQ',platform=platform.platform(),fixtures=fixtures,input=sys.argv[1])
    if len(sys.argv)>3:
        old=json.loads(Path(sys.argv[3]).read_text())
        agreement={'vertices':{tuple(map(QQ,v)) for v in r['vertices']}=={tuple(map(QQ,v)) for v in old['raw_vertices']},
            'centroid':list(map(QQ,r['centroid']))==list(map(QQ,old['raw_centroid'])),
            'volume':QQ(r['volume'])==QQ(old['ordinary_volume']),
            'counts':r['strict']==old['counts'] and r['weak']==old['weak'],
            'combinatorial_counts':all(r[k]==old[k] for k in ['V','E','F'])}
        r['agreement_with_archived_report']=agreement
        if not all(agreement.values()):raise ValueError(str(agreement))
    Path(sys.argv[2]).write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps({k:v for k,v in r.items() if k not in ['vertices','centroid','volume']}),flush=True)
