# material-eb6f1d43de0d

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Exact supplemental proofs and actual-body controls for the MINIMUM pair frontier.
Run with assertions: python -S exact_pair_frontier.py build|check
Only Python standard library; the continuous root-CD argument is a separate premise.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import json,hashlib,sys
assert __debug__
G={(0,0):3,(2,0):200,(1,2):-203,(2,2):-203,(1,3):200,(3,3):-200,(3,4):203}

def coefficients(box):
    la,ha,le,he=box
    q={(k,l):sum(F(v)*comb(i,k)*la**(i-k)*(ha-la)**k*comb(j,l)*le**(j-l)*(he-le)**l
                    for (i,j),v in G.items() if i>=k and j>=l)
       for k in range(4) for l in range(5)}
    b=[[sum(q[k,l]*F(comb(i,k),comb(3,k))*F(comb(j,l),comb(4,l))
             for k in range(i+1) for l in range(j+1)) for j in range(5)] for i in range(4)]
    # Independently expand the Bernstein polynomials into powers of the local variables.
    for k in range(4):
        for l in range(5):
            back=sum(b[i][j]*comb(3,i)*comb(3-i,k-i)*(-1)**(k-i)
                     *comb(4,j)*comb(4-j,l-j)*(-1)**(l-j)
                     for i in range(k+1) for j in range(l+1))
            assert back==q[k,l]
    assert all(t>=0 for row in b for t in row)
    assert all(t>0 for t in b[0]) # Strict positivity when the local first variable is <1.
    return b

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def rank3(rows):return any(det(a,b,c)!=0 for a,b,c in combinations(rows,3))
def hull(points):
    p=[tuple(map(F,x)) for x in points]
    assert p[0]==(0,0,0) and len(set(p))==len(p)
    candidates={}
    for i,j,k in combinations(range(len(p)),3):
        n=cross(sub(p[j],p[i]),sub(p[k],p[i]))
        if n==(0,0,0):continue
        vals=[dot(n,sub(x,p[i])) for x in p]
        if not (all(v>=0 for v in vals) or all(v<=0 for v in vals)):continue
        if all(v==0 for v in vals):continue
        if any(v<0 for v in vals):n=tuple(-v for v in n); vals=[-v for v in vals]
        key=tuple(t for t,v in enumerate(vals) if v==0)
        candidates[key]=n
    verts=[i for i in range(len(p)) if rank3([n for f,n in candidates.items() if i in f])]
    vset=set(verts)
    facets=sorted(set(tuple(i for i in f if i in vset) for f in candidates))
    assert all(len(f)>=3 for f in facets)
    edges=sorted(set(tuple(sorted(set(f)&set(g))) for f,g in combinations(facets,2) if len(set(f)&set(g))==2))
    assert len(verts)-len(edges)+len(facets)==2
    assert all(sum(set(e)<=set(f) for f in facets)==2 for e in edges)
    cycles=[];vol=F(0);moment=[F(0)]*3
    for facet in facets:
        adj={i:sorted(j for j in facet if i!=j and tuple(sorted((i,j))) in edges) for i in facet}
        assert all(len(js)==2 for js in adj.values())
        cyc=[facet[0],adj[facet[0]][0]]
        while True:
            nxt=next(j for j in adj[cyc[-1]] if j!=cyc[-2])
            if nxt==cyc[0]:break
            assert nxt not in cyc
            cyc.append(nxt)
        assert len(cyc)==len(facet)
        cycles.append(cyc)
        for j in range(1,len(cyc)-1):
            triangle=[p[cyc[0]],p[cyc[j]],p[cyc[j+1]]]
            v=abs(det(*triangle))/6
            vol+=v
            for k in range(3):moment[k]+=v*sum(t[k] for t in triangle)/4
    assert vol>0
    centroid=tuple(x/vol for x in moment)
    return {'vertices':verts,'facets':facets,'cycles':cycles,'edges':edges,'V':vol,'g':centroid}

def pair(points,ell,ix,iy):
    H=hull(points);p=[tuple(map(F,x)) for x in points]
    # ell=(constant, x coefficient, y coefficient, z coefficient).
    def slack(x):return ell[0]+dot(ell[1:],x)
    assert all(slack(x)>=0 for x in p)
    root=tuple(i for i in H['vertices'] if slack(p[i])==0)
    assert root in H['facets']
    fx=tuple(i for i in H['vertices'] if p[i][0]==0)
    fy=tuple(i for i in H['vertices'] if p[i][1]==0)
    assert fx==tuple(sorted((0,1,ix))) and fy==tuple(sorted((0,1,iy)))
    assert fx in H['facets'] and fy in H['facets']
    assert p[1]==(0,0,1) and p[ix][0]==p[ix][2]==0 and p[iy][1]==p[iy][2]==0
    V=H['V'];g=H['g'];sg=slack(g);assert sg>0
    # True areas of the coordinate triangles and their true facet mean slacks.
    ax=p[ix][1]/2;ay=p[iy][0]/2
    dx=ax*g[0]/V;dy=ay*g[1]/V
    tx=dx*sum(slack(p[i]) for i in fx)/(3*sg)
    ty=dy*sum(slack(p[i]) for i in fy)/(3*sg)
    H.update(points=p,root=root,coordinate_facets=(fx,fy),ell=ell,ell_g=sg,trace_parts=(tx,ty),trace=tx+ty)
    return H

def controls():
    base=[(0,0,0),(0,0,1),(0,1,0),(1,0,0)]
    near=base+[(F(2497,3000),F(1,1000),F(2,9)),(F(1,1000),F(2497,3000),F(2,9))]
    H=pair(near,(F(1),F(-1),F(-1),F(-3,4)),2,3)
    assert (len(H['vertices']),len(H['edges']),len(H['facets']))==(6,11,7)
    assert H['trace']==F(8312670000,4097560009)
    assert F(507,250)<H['trace']<F(203,100)
    # Exact disjoint-root example: the two original opposite vertices have positive root gaps.
    points=base+[(F(7,3),F(3,2),F(-11,4)),(F(8,3),F(11,6),F(-47,12)),(F(14,5),F(13,5),F(-47,10))]
    ell=(F(1),F(-3,5),F(-1,10),F(-1,5))
    original=pair(points,ell,2,3)
    extended=pair(points+[(0,10,0),(F(5,3),0,0)],ell,7,8)
    assert set(original['root']).isdisjoint({0,1,2,3})
    assert 7 in extended['root'] and 8 in extended['root']
    assert original['trace']>extended['trace']+F(3,20)
    # The extension is a true convex hull containing all original points; no COM is reused.
    return {'root_cd_near_control':H,'failed_unconditional_extension':{'original':original,'extended':extended,'difference':original['trace']-extended['trace']}}

def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [encode(t) for t in x]
    return x

def build():
    cells=[]
    for i in range(16):
        for j in range(16):
            box=(F(i,16),F(i+1,16),F(j,16),F(j+1,16))
            cells.append({'indices':[i,j],'box':box,'coefficients':coefficients(box)})
    count=sum(t>0 for cell in cells for row in cell['coefficients'] for t in row)
    # For kappa=203/100 the lower-cap quadratic comparison has positive coefficients.
    kap=F(203,100)
    assert 3*kap-6>0 and 3-kap>0 and kap-1>0
    data={'identity':'ROOT_CD_203_100_AND_EXTENSION_COUNTERCONTROL_V1','polynomial':[[i,j,v] for (i,j),v in sorted(G.items())],
          'cells':cells,'positive_count':count,'coefficient_count':5120,'controls':controls(),
          'near_root_constants':{'epsilon':F(1,1500),'bound':kap*F(1500,1499)**7,'threshold':F(51,25),'margin':F(51,25)-kap*F(1500,1499)**7},
          'scope':'G>0 for 0<=a<1,0<=e<=1; continuous actual-body root-CD proof is inherited separately. Quantitative near-root extension uses a separate homothety proof; no unrestricted-root cap or equilibrium claim.'}
    assert data['near_root_constants']['margin']>0
    assert kap*F(1425,1424)**7<F(51,25) and kap*F(1424,1423)**7>F(51,25)
    return (json.dumps(encode(data),sort_keys=True,separators=(',',':'),ensure_ascii=True)+'\n').encode('ascii')
if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else 'check';assert mode in ('build','check')
    out=Path('exact_pair_frontier.json');raw=build()
    if mode=='build':out.write_bytes(raw)
    else:assert out.read_bytes()==raw
    d=json.loads(raw);ctr=d['controls'];old=ctr['failed_unconditional_extension']
    print('ROOT_CD_203_100_EXACT_BERNSTEIN_PASS',256,5120,d['positive_count'])
    print('TRUE_ROOT_CD_CONTROL_PASS',ctr['root_cd_near_control']['trace'])
    print('TRUE_EXTENSION_MONOTONICITY_COUNTEREXAMPLE_PASS',old['original']['trace'],old['extended']['trace'],old['difference'])
    print('NEAR_ROOT_HOMOTHETY_RATIONAL_THRESHOLD_PASS',d['near_root_constants']['epsilon'],d['near_root_constants']['margin'])
    print('EXACT_PAIR_FRONTIER_RECOVERY_PASS',len(raw),hashlib.sha256(raw).hexdigest())
