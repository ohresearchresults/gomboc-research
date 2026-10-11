# material-1b954cbca536

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""PAIR_FACET_MERGE_HIGH_TRACE_H_24_V1: exact finite algebra and true-body controls.
Run with assertions enabled, CPython >= 3.11, standard library only:
  python -S pair_facet_merge_exact.py build
  python -S pair_facet_merge_exact.py check
No external inputs, random numbers, or optimizer. The continuous proof and the
inherited boundary-trace theorem are analytic inputs, not proved by this script.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sys
assert __debug__

IDENTITY = 'PAIR_FACET_MERGE_HIGH_TRACE_H_24_V1'
OUTPUT = 'pair_facet_merge_exact.json'
ZERO = (F(0), F(0), F(0))

def add(a, b): return tuple(x+y for x,y in zip(a,b))
def sub(a, b): return tuple(x-y for x,y in zip(a,b))
def scale(a, s): return tuple(s*x for x in a)
def dot(a, b): return sum((x*y for x,y in zip(a,b)), F(0))
def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def det(a, b, c): return dot(a, cross(b,c))
def tet(a, b, c, d): return abs(det(sub(b,a),sub(c,a),sub(d,a)))/6

def polygon(points, indices, normal):
    """Exact planar hull; remove interior and collinear supplied points."""
    drop = next(i for i in range(3) if normal[i])
    keep = [i for i in range(3) if i != drop]
    projected = sorted((points[k][keep[0]], points[k][keep[1]], k) for k in indices)
    def turn(a,b,c):
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lo=[]
    for z in projected:
        while len(lo)>=2 and turn(lo[-2],lo[-1],z)<=0: lo.pop()
        lo.append(z)
    hi=[]
    for z in reversed(projected):
        while len(hi)>=2 and turn(hi[-2],hi[-1],z)<=0: hi.pop()
        hi.append(z)
    cyc=[z[2] for z in lo[:-1]+hi[:-1]]
    assert len(cyc)>=3
    if dot(cross(sub(points[cyc[1]],points[cyc[0]]),sub(points[cyc[2]],points[cyc[0]])),normal)<0:
        cyc.reverse()
    pos=cyc.index(min(cyc));cyc=cyc[pos:]+cyc[:pos]
    assert dot(cross(sub(points[cyc[1]],points[cyc[0]]),sub(points[cyc[2]],points[cyc[0]])),normal)>0
    return tuple(cyc)

def hull(points):
    """All maximal facets, true cyclic edges, and actual volume/first moment."""
    assert len(set(points))==len(points)
    supports={}
    for i,j,k in combinations(range(len(points)),3):
        n=cross(sub(points[j],points[i]),sub(points[k],points[i]))
        if n==ZERO: continue
        b=dot(n,points[i]); signs=[dot(n,x)-b for x in points]
        if all(s==0 for s in signs): continue
        if all(s<=0 for s in signs): pass
        elif all(s>=0 for s in signs): n=scale(n,-1);b=-b
        else: continue
        ids=tuple(i for i,x in enumerate(points) if dot(n,x)==b)
        supports.setdefault(ids,(n,b))
    facets=[]
    for ids,(n,b) in sorted(supports.items()):
        cyc=polygon(points,ids,n)
        facets.append({'cycle':cyc,'normal':n,'offset':b})
    facets.sort(key=lambda f:tuple(sorted(f['cycle'])))
    assert len({tuple(sorted(f['cycle'])) for f in facets})==len(facets)
    edges=sorted({tuple(sorted((c[i],c[(i+1)%len(c)]))) for f in facets for c in [f['cycle']] for i in range(len(c))})
    vertices=sorted({i for f in facets for i in f['cycle']})
    assert len(vertices)-len(edges)+len(facets)==2
    volume=F(0);moment=ZERO
    for f in facets:
        c=f['cycle'];a=points[c[0]]
        for j in range(1,len(c)-1):
            b=points[c[j]];d=points[c[j+1]];v=det(a,b,d)/6
            volume+=v;moment=add(moment,scale(add(add(a,b),d),v/4))
    assert volume>0
    center=scale(moment,1/volume)
    for f in facets:
        assert dot(f['normal'],center)<f['offset']
    return {'points':points,'facets':facets,'edges':edges,'vertices':vertices,
            'volume':volume,'moment':moment,'center':center}

def facet_by_set(body, ids):
    matches=[f for f in body['facets'] if set(f['cycle'])==set(ids)]
    assert len(matches)==1
    return matches[0]

def ell_value(ell, x): return ell[0]+dot(ell[1:],x)

def cone_integrals(body, facet, ell):
    """H*area and H*integral ell, relative to origin, for outward facet.
    Used only when the origin is in the body's strict interior.
    """
    pts=body['points'];cyc=facet['cycle'];a=pts[cyc[0]]
    mass=F(0);weighted=F(0)
    for j in range(1,len(cyc)-1):
        b=pts[cyc[j]];c=pts[cyc[j+1]];s=det(a,b,c)/2
        assert s>0
        mass+=s
        weighted+=s*(ell_value(ell,a)+ell_value(ell,b)+ell_value(ell,c))/3
    return mass,weighted

def clip(body,p,t):
    pts=body['points'];values=[dot(p,x)-t for x in pts]
    out={x for x,v in zip(pts,values) if v<=0}
    for i,j in body['edges']:
        if values[i]*values[j]<0:
            lam=-values[i]/(values[j]-values[i])
            out.add(add(pts[i],scale(sub(pts[j],pts[i]),lam)))
    return hull(sorted(out))

def poly_add(a,b):
    out=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a):out[i]+=x
    for i,x in enumerate(b):out[i]+=x
    while len(out)>1 and not out[-1]:out.pop()
    return out

def poly_scale(a,c): return [c*x for x in a]
def poly_mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    while len(out)>1 and not out[-1]:out.pop()
    return out

def arithmetic():
    D=poly_mul([F(1)]*3,[F(3),F(2),F(1)])
    A=[F(1),F(2),F(3)]
    P=poly_add(poly_scale(D,111),poly_scale(A,-300))
    assert P==list(map(F,[33,-45,-234,333,111]))
    a=F(117,250)
    quotient=[F(9413937,62500),F(54612,125),F(111)]
    remainder=[F(38866407,3906250000),F(2284461,7812500)]
    identity=poly_add(poly_mul([a*a,-2*a,F(1)],quotient),remainder)
    assert identity==P and all(x>0 for x in quotient+remainder)
    tau=F(51,25);cap=F(111,100);h=F(1,24);alpha=12/tau
    t=1-alpha*h
    psi=t*((2-h)*t+h)*(tau-10*h)/(2*(1-h)*(1-3*h))
    log_margin=alpha-F(24,23)-F(24,7)
    assert t==F(77,102)
    assert psi==F(19933397,17946900)
    assert psi-cap==F(6169,8973450)>0
    assert log_margin==F(3860,2737)>0
    assert tau<2*cap<4 and 12*h<tau and 3*h<1
    return {'boundary_cap':cap,'sharp_cap_polynomial':P,'square_center':a,
            'positive_square_quotient':quotient,'positive_remainder':remainder,
            'tau':tau,'h_cutoff':h,'t_at_cutoff':t,'psi_at_cutoff':psi,
            'psi_cap_gap':psi-cap,'log_derivative_margin':log_margin,
            'pair_product_lower_bound':F(1,576)}

def control(r):
    """Seven genuine vertices with a genuine root triangle outside A,B.
    This is a geometric control only, not a 110 mechanical witness.
    """
    e=F(1,100);z=-(2*r-1)/2
    raw=[ZERO,(F(0),F(0),F(1)),(F(0),F(1),F(0)),(F(1),F(0),F(0)),
         (r-e,r+e,z),(r+e,r-e,z),(r,r,z+e)]
    original=hull(raw);g=original['center']
    pts=[sub(x,g) for x in raw];body=hull(pts);V=body['volume']
    assert body['center']==ZERO and V==original['volume']
    assert body['vertices']==list(range(7))
    f1=facet_by_set(body,(0,1,2));f2=facet_by_set(body,(0,1,3))
    root=facet_by_set(body,(4,5,6))
    raw_mu=2*r-g[0]-g[1]
    ell=(F(1),-1/raw_mu,-1/raw_mu,F(0))
    values=[ell_value(ell,x) for x in pts]
    assert all(0<=x<=4 for x in values)
    assert all(values[i]==0 for i in root['cycle'])
    assert all(values[i]>0 for i in (0,1,2,3))
    q1=scale(f1['normal'],1/f1['offset']);q2=scale(f2['normal'],1/f2['offset'])
    c1,w1=cone_integrals(body,f1,ell);c2,w2=cone_integrals(body,f2,ell)
    m1=c1/V;m2=c2/V;m=m1+m2;T=(w1+w2)/V
    A,B,C,D=pts[:4];h=tet(A,B,C,D)/V
    assert 1-dot(q1,D)==3*h/m1 and 1-dot(q2,C)==3*h/m2
    assert m>=T/4 and 0<T<2*F(111,100)
    assert m>3*h
    p=scale(add(scale(q1,m1),scale(q2,m2)),1/m)
    t=1-3*h/m
    assert 0<t<1
    assert dot(p,A)==dot(p,B)==1 and dot(p,C)==dot(p,D)==t
    Ap=scale(A,t);Bp=scale(B,t)
    image_points=[Ap,Bp,C,D]
    for x in image_points:
        assert dot(p,x)==t
        assert all(dot(f['normal'],x)<=f['offset'] for f in body['facets'])
    s1=dot(cross(sub(Bp,Ap),sub(C,Ap)),p)
    s2=dot(cross(sub(Bp,Ap),sub(D,Ap)),p)
    assert s1*s2<0
    image_weight=F(0)
    for source,image,mass in (((A,B,C),(Ap,Bp,C),m1),((A,B,D),(Ap,Bp,D),m2)):
        old_cone=abs(det(*source))/2;new_cone=abs(det(*image))/2
        assert old_cone==mass*V and new_cone==t*t*old_cone
        image_weight+=new_cone*sum((ell_value(ell,x) for x in image),F(0))/3
    edge_sum=values[0]+values[1];opp_sum=values[2]+values[3]
    L=image_weight/V
    assert L==t*t*(T+h*(2-edge_sum))
    assert L>=t*t*(t*T+2*h)>0
    lower=clip(body,p,t);v=lower['volume'];gq=lower['center']
    cut=[f for f in lower['facets'] if all(dot(p,lower['points'][i])==t for i in f['cycle'])]
    assert len(cut)==1
    _,actual_H_integral=cone_integrals(lower,cut[0],ell)
    Bq=v*ell_value(ell,gq)
    pg=dot(p,gq)
    actual=(1-pg/t)*actual_H_integral/Bq
    R=1+h*(1+t)/(2*t*(1-h))
    denom=1-T*(1-t)/4
    bound=t*((2-h)*t+h)*(t*T+2*h)/(2*(1-h)*denom)
    assert v<=(1-h)*V and pg<=-h*(1+t)/(2*(1-h))<0
    assert 0<Bq<=V*(1-h*(edge_sum+opp_sum)/4)<=V*denom
    assert actual_H_integral>=image_weight
    assert actual>=R*L/denom>=bound
    assert actual<F(111,100)
    lambda12=h*m2/m1;lambda21=h*m1/m2
    assert lambda12*lambda21==h*h
    return {'r':r,'epsilon':e,'raw_points':raw,'own_center':g,'volume':V,
            'true_facets':[f['cycle'] for f in body['facets']],
            'true_edges':body['edges'],'f_vector':[len(body['vertices']),len(body['edges']),len(body['facets'])],
            'root_values':values,'h':h,'m1':m1,'m2':m2,'T':T,'p':p,'t':t,
            'projected_points':image_points,'projected_weighted_trace':L,
            'opposite_side_product':s1*s2,'cut_points':lower['points'],
            'cut_true_facets':[f['cycle'] for f in lower['facets']],
            'cut_true_edges':lower['edges'],'cut_volume':v,'cut_own_center':gq,
            'cut_root_integral':Bq,'cut_actual_facet_trace':actual,
            'merge_lower_bound':bound,'tetrahedron_removal_distance_factor':R,
            'pair_coefficients':[lambda12,lambda21],
            'geometric_control_only_not_110_witness':True}

def serialize(value):
    if isinstance(value,F):return str(value)
    if isinstance(value,dict):return {k:serialize(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):return [serialize(v) for v in value]
    return value

def run():
    report={'identity':IDENTITY,'arithmetic':arithmetic(),
            'controls':[control(F(r)) for r in (2,4,8,16)],
            'analytic_statement':'For genuine adjacent triangular facets, T>=51/25 implies h>1/24.',
            'uniform_mass_gap':'Positive existence follows from the accepted equality/compactness theorem; no numerical gap computed.',
            'C_lower_bound_unchanged':34,'full_E17_exclusion':False,'exact_minimum_found':False}
    data=(json.dumps(serialize(report),sort_keys=True,indent=2)+'\n').encode('utf-8')
    if len(sys.argv)!=2 or sys.argv[1] not in ('build','check'):
        raise SystemExit('Usage: python -S pair_facet_merge_exact.py build|check')
    path=Path(OUTPUT)
    if sys.argv[1]=='build':path.write_bytes(data)
    elif not path.exists() or path.read_bytes()!=data:
        raise SystemExit('Exact report comparison failed; run build in a clean directory first.')
    print('PAIR_BOUNDARY_CAP_111_100_SOS_PASS')
    print('PAIR_FACET_MERGE_H_24_EXACT_ARITHMETIC_PASS 19933397/17946900 6169/8973450')
    print('TRUE_PAIR_CUT_OWN_CENTROID_CONTROLS_PASS 4')
    print('PAIR_FACET_MERGE_RECOVERY_PASS',len(data),hashlib.sha256(data).hexdigest())

if __name__=='__main__':run()
