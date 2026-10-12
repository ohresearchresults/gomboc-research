# material-e3f913c240f5

AI research material

---

"""Exact certificate and physical controls: adjacent-triangle root-gap sum cut.
Reconstruct: python -S pair_extension_exact.py build
Verify:      python -S pair_extension_exact.py check
Python standard library only. Assertions must be enabled.
Continuous premises: the proved root-CD cap 203/100, the actual-facet mass
bound 3/4, and the visible-pyramid extension argument in the companion proof.
This program proves finite polynomial identities; it does not claim a Gomboc.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb
from pathlib import Path
import hashlib
import json
import sys
assert __debug__
KAPPA, TAU = F(203,100), F(51,25)
ZERO = (0,0,0)
ONE = {ZERO:F(1)}

def add(*ps):
    out = {}
    for p in ps:
        for k,v in p.items(): out[k] = out.get(k,F(0)) + v
    return {k:v for k,v in out.items() if v}

def scale(p,a): return {k:F(a)*v for k,v in p.items() if a*v}

def mul(p,q):
    out = {}
    for a,u in p.items():
        for b,v in q.items():
            k = tuple(x+y for x,y in zip(a,b))
            out[k] = out.get(k,F(0)) + u*v
    return {k:v for k,v in out.items() if v}

def power(p,n):
    out = ONE
    for _ in range(n): out = mul(out,p)
    return out

def substitute(p,variables):
    out = {}
    for exponents,a in p.items():
        term = ONE
        for variable,n in zip(variables,exponents): term = mul(term,power(variable,n))
        out = add(out,scale(term,a))
    return out

def value(p,x):
    return sum(a*x[0]**i*x[1]**j*x[2]**k for (i,j,k),a in p.items())

def polys():
    b,c,d = ({(1,0,0):F(1)},{(0,1,0):F(1)},{(0,0,1):F(1)})
    q0 = add(ONE,b); q1 = add(q0,c); q2 = add(q0,d)
    u = add(ONE,scale(c,-1)); v = add(ONE,scale(d,-1)); w = mul(u,v)
    rhs = scale(add(ONE,scale(w,-1)),10353)
    p1 = add(scale(mul(q0,mul(w,v)),5100),rhs,scale(q1,-5075))
    p2 = add(scale(mul(q0,mul(w,u)),5100),rhs,scale(q2,-5075))
    p12 = add(scale(mul(q0,mul(w,add(u,v))),5100),rhs,scale(add(q1,q2),-5075))
    return {'P1':p1,'P2':p2,'P12':p12}

def bernstein_check(p,degrees):
    """Convert all powers to tensor Bernstein coefficients and back exactly."""
    assert all(all(e<=n for e,n in zip(ex,degrees)) for ex in p)
    indices = list(product(*(range(n+1) for n in degrees)))
    coefficients = {}
    for i in indices:
        total = F(0)
        for e,a in p.items():
            if all(x<=y for x,y in zip(e,i)):
                factor = a
                for ii,ee,nn in zip(i,e,degrees): factor *= F(comb(ii,ee),comb(nn,ee))
                total += factor
        coefficients[i] = total
    # Rebuild using the literal polynomials B_i^n = choose(n,i)t^i(1-t)^(n-i).
    back = {}
    for i,a in coefficients.items():
        for e in product(*(range(ii,nn+1) for ii,nn in zip(i,degrees))):
            factor = a
            for ii,ee,nn in zip(i,e,degrees):
                factor *= comb(nn,ii)*comb(nn-ii,ee-ii)*(-1)**(ee-ii)
            back[e] = back.get(e,F(0)) + factor
    back = {e:a for e,a in back.items() if a}
    assert back == p
    return coefficients

def finite_certificates():
    b,t,u = ({(1,0,0):F(1)},{(0,1,0):F(1)},{(0,0,1):F(1)})
    originals = polys()
    records = {}
    # c=t*u/253, d=t*(1-u)/253 covers exactly c,d>=0,c+d<=1/253.
    substitution = [b,scale(mul(t,u),F(1,253)),scale(mul(t,add(ONE,scale(u,-1))),F(1,253))]
    for name,p in originals.items():
        local = substitute(p,substitution)
        co = bernstein_check(local,(1,3,3))
        assert len(co)==32 and all(a>0 for a in co.values())
        records[name] = {'original_power':[[*e,a] for e,a in sorted(p.items())],
                         'local_power':[[*e,a] for e,a in sorted(local.items())],
                         'bernstein':[[*e,a] for e,a in sorted(co.items())],
                         'minimum':min(co.values())}
    assert records['P1']['minimum']==F(668759,64009)
    assert records['P2']['minimum']==F(668759,64009)
    assert records['P12']['minimum']==F(4634,64009)
    # These are failures of this sufficient criterion, NOT physical counterexamples.
    assert value(originals['P12'],(F(1),F(0),F(1,252)))==F(-428,1323)
    assert value(originals['P12'],(F(1),F(1,505),F(1,505)))==F(-2213253,25757525)
    # The weaker unconditional volume-and-moment transfer has fourth, not seventh, power.
    assert KAPPA*F(815,814)**4<TAU<KAPPA*F(814,813)**4
    return records

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def rank3(rows): return any(det(a,b,c)!=0 for a,b,c in combinations(rows,3))
def slack(ell,p): return ell[0]+dot(ell[1:],p)

def hull(points):
    """All support triples, true coplanar maximal facets, true edges, A-fan moments."""
    p = [tuple(map(F,x)) for x in points]
    assert p[0]==(0,0,0) and len(set(p))==len(p)
    candidates = {}
    for i,j,k in combinations(range(len(p)),3):
        n = cross(sub(p[j],p[i]),sub(p[k],p[i]))
        if n==(0,0,0): continue
        vals = [dot(n,sub(x,p[i])) for x in p]
        if not (all(v>=0 for v in vals) or all(v<=0 for v in vals)): continue
        if all(v==0 for v in vals): continue
        if any(v<0 for v in vals): n=tuple(-v for v in n); vals=[-v for v in vals]
        candidates[tuple(t for t,v in enumerate(vals) if v==0)] = n
    verts = [i for i in range(len(p)) if rank3([n for f,n in candidates.items() if i in f])]
    vset = set(verts)
    facets = sorted(set(tuple(i for i in f if i in vset) for f in candidates))
    assert all(len(f)>=3 for f in facets)
    edges = sorted(set(tuple(sorted(set(f)&set(g))) for f,g in combinations(facets,2) if len(set(f)&set(g))==2))
    assert len(verts)-len(edges)+len(facets)==2
    assert all(sum(set(e)<=set(f) for f in facets)==2 for e in edges)
    cycles=[]; vol=F(0); moment=[F(0)]*3
    for facet in facets:
        adj = {i:sorted(j for j in facet if i!=j and tuple(sorted((i,j))) in edges) for i in facet}
        assert all(len(js)==2 for js in adj.values())
        cyc = [facet[0],adj[facet[0]][0]]
        while True:
            nxt = next(j for j in adj[cyc[-1]] if j!=cyc[-2])
            if nxt==cyc[0]: break
            assert nxt not in cyc
            cyc.append(nxt)
        assert len(cyc)==len(facet)
        cycles.append(cyc)
        for j in range(1,len(cyc)-1):
            tri = [p[cyc[0]],p[cyc[j]],p[cyc[j+1]]]
            v = abs(det(*tri))/6
            vol += v
            for k in range(3): moment[k] += v*sum(t[k] for t in tri)/4
    assert vol>0
    return {'points':p,'vertices':verts,'facets':facets,'cycles':cycles,'edges':edges,
            'f_vector':[len(verts),len(edges),len(facets)],'V':vol,'g':tuple(x/vol for x in moment)}

def pair(points,ell,ix,iy):
    H=hull(points); p=H['points']; V=H['V']; g=H['g']
    assert all(slack(ell,x)>=0 for x in p)
    root=tuple(i for i in H['vertices'] if slack(ell,p[i])==0)
    assert root in H['facets'] and not ({0,1}&set(root))
    fx=tuple(i for i in H['vertices'] if p[i][0]==0)
    fy=tuple(i for i in H['vertices'] if p[i][1]==0)
    assert fx==tuple(sorted((0,1,ix))) and fy==tuple(sorted((0,1,iy)))
    assert fx in H['facets'] and fy in H['facets']
    assert p[1]==(0,0,1) and p[ix][0]==p[ix][2]==p[iy][1]==p[iy][2]==0
    mu=slack(ell,g); assert mu>0
    masses=(p[ix][1]*g[0]/(2*V),p[iy][0]*g[1]/(2*V))
    assert all(0<x<=F(3,4) for x in masses)
    parts=tuple(m*sum(slack(ell,p[i]) for i in f)/(3*mu) for m,f in zip(masses,(fx,fy)))
    H.update(ell=ell,root=root,coordinate_facets=(fx,fy),mu=mu,masses=masses,trace_parts=parts,trace=sum(parts))
    return H

def extension_audit(points,ell,opposite):
    """Check every visible pyramid, and both complete exact moment differences."""
    H=hull(points); p=H['points']; c=slack(ell,p[opposite])
    assert ell[0]==1 and 0<c<1 and all(slack(ell,x)>=0 for x in p)
    s=1/(1-c); Q=tuple(s*x for x in p[opposite])
    assert slack(ell,Q)==0 and Q not in p
    J=hull(p+[Q]); V=H['V']; B=V*slack(ell,H['g']); Vnew=J['V']; Bnew=Vnew*slack(ell,J['g'])
    rows=[]; added_V=F(0); added_B=F(0)
    for cyc in H['cycles']:
        n=cross(sub(p[cyc[1]],p[cyc[0]]),sub(p[cyc[2]],p[cyc[0]]))
        vals=[dot(n,sub(x,p[cyc[0]])) for x in p]
        if any(a<0 for a in vals): n=tuple(-x for x in n)
        assert all(dot(n,sub(x,p[cyc[0]]))>=0 for x in p)
        hA=dot(n,sub(p[0],p[cyc[0]])); hQ=dot(n,sub(Q,p[cyc[0]]))
        if hQ>=0: continue
        assert hA>0
        ratio=-hQ/hA
        assert 0<ratio<=s-1
        VF=F(0); BF=F(0)
        for j in range(1,len(cyc)-1):
            tri=[p[cyc[0]],p[cyc[j]],p[cyc[j+1]]]
            volume=abs(det(*tri))/6
            VF += volume
            BF += volume*sum(slack(ell,x) for x in tri)/4
        dv=ratio*VF; db=ratio*BF
        added_V+=dv; added_B+=db
        rows.append({'facet':cyc,'relative_height':ratio,'A_pyramid_volume':VF,'added_V':dv,'added_B':db})
    assert Vnew-V==added_V and Bnew-B==added_B
    assert Vnew<=s*V and Bnew<=s*B-(s-1)*V/4
    return {'original':H,'extended':J,'ell':ell,'gap':c,'s':s,'new_point':Q,'visible_pyramids':rows,
            'B':B,'Bnew':Bnew,'volume_margin':s*V-Vnew,'moment_margin':s*B-(s-1)*V/4-Bnew}

def controls():
    base=[(0,0,0),(0,0,1),(0,1,0),(1,0,0)]
    # This actual disjoint-root control lies in the new sum region but OUTSIDE the 1/506 max-gap box.
    b,c,d=F(1,4),F(1,300),F(1,3000)
    ell=(F(1),d-1,c-1,b-1); z=F(2,9); tiny=F(1,1000)
    root1=((1-(1-b)*z-(1-c)*tiny)/(1-d),tiny,z)
    root2=(tiny,(1-(1-b)*z-(1-d)*tiny)/(1-c),z)
    z3=z+F(1,100000)
    t3=(1-(1-b)*z3)/(2-c-d)
    root3=(t3,t3,z3)
    points=base+[root1,root2,root3]
    original=pair(points,ell,2,3)
    assert set(original['root']).isdisjoint({0,1,2,3})
    first=extension_audit(points,ell,2)
    second=extension_audit(first['extended']['points'],ell,3)
    extended=pair(second['extended']['points'],ell,len(points),len(points)+1)
    r=1/((1-c)*(1-d)); V=original['V']; mu=original['mu']
    assert extended['V']<=r*V
    assert extended['V']*extended['mu']<=r*V*mu-(r-1)*V/4
    assert c+d<=F(1,253) and c>F(1,506)
    assert F(2)<original['trace']<TAU and extended['trace']<KAPPA
    assert all(value(p,(b,c,d))>0 for p in polys().values())
    # Reproduce the inherited true-body refutation of unconditional trace monotonicity.
    badpoints=base+[(F(7,3),F(3,2),F(-11,4)),(F(8,3),F(11,6),F(-47,12)),(F(14,5),F(13,5),F(-47,10))]
    badell=(F(1),F(-3,5),F(-1,10),F(-1,5))
    bad=pair(badpoints,badell,2,3)
    bad1=extension_audit(badpoints,badell,2)
    bad2=extension_audit(bad1['extended']['points'],badell,3)
    badextended=pair(bad2['extended']['points'],badell,7,8)
    assert bad['trace']==F(7433004,6563417)
    assert badextended['trace']==F(2459853,2506235)
    assert bad['trace']-badextended['trace']>F(3,20)
    # The one-point volume and affine-moment bounds can both be exact.
    sharp=extension_audit(base,(F(1),F(-1),F(-1,2),F(-1)),2)
    assert sharp['volume_margin']==sharp['moment_margin']==0
    return {'asymmetric_near_root':{'original':original,'extended':extended,'first':first,'second':second,'r':r},
            'nonmonotonic_trace':{'original':bad,'extended':badextended,'first':bad1,'second':bad2},
            'sharp_one_extension_simplex':sharp}

def encode(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,dict): return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [encode(t) for t in x]
    return x

def build():
    data={'identity':'ACTUAL_ADJACENT_TRIANGLE_SUM_GAP_253_V1','kappa':KAPPA,'threshold':TAU,
          'sum_gap_threshold':F(1,253),'implied_max_gap_threshold':F(1,506),
          'substitution':'b=b,c=t*u/253,d=t*(1-u)/253; b,t,u in [0,1]',
          'bernstein_degrees':[1,3,3],'certificates':finite_certificates(),'controls':controls(),
          'scope':'Conditional on the proved continuous extension and root-CD lemmas. The 96 positive coefficients cover the full closed simplex, not samples. No equilibrium, f-vector exclusion, exact minimum, or unrestricted trace monotonicity is claimed.'}
    return (json.dumps(encode(data),sort_keys=True,separators=(',',':'),ensure_ascii=True)+'\n').encode('ascii')

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else 'check'
    assert mode in ('build','check')
    out=Path('pair_extension_exact.json'); raw=build()
    if mode=='build': out.write_bytes(raw)
    else: assert out.read_bytes()==raw
    obj=json.loads(raw); cc=obj['controls']['asymmetric_near_root']
    print('SUM_GAP_253_EXACT_BERNSTEIN_PASS',3,96,96)
    print('SINGLE_VERTEX_VOLUME_MOMENT_EXTENSION_EXACT_PASS',5)
    print('ASYMMETRIC_TRUE_TRIANGLES_SUM_REGION_PASS',cc['original']['trace'],cc['extended']['trace'])
    print('INHERITED_TRACE_MONOTONICITY_COUNTEREXAMPLE_REPRODUCED')
    print('PAIR_EXTENSION_EXACT_RECOVERY_PASS',len(raw),hashlib.sha256(raw).hexdigest())
