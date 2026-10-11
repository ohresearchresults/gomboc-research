# material-f9d0364dbcae

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Exact five-dimensional actual-centroid H5 hybrid via the orthogonal shell.
All source dependencies and every nondefault parameter are literal.
"""
from fractions import Fraction as F
from itertools import combinations
import json,hashlib,sys
from pathlib import Path
import hybrid_exact_region as h
from hybrid_reference_frontier import body,inv,dot,quad,strings
from orthogonal_shell_exact import THETA,reference,BOUND,bound_all
RADIUS=F(1,10000)
BOX=[(x-RADIUS,x+RADIUS) for x in THETA]
EPS=F(1,1000);UPSILON=F(241,50)
ALPHA=[F(51,100),F(51,100),F(47,100)]
CHI=[F(1,8),F(1,8),F(1,1000000)]
CEILING=[F(8),F(8),F(4)];GAMMA_UP=F(73,250)

def product_guard(K,chi,L):
    load=4*K*L-(K+1)**2*(1+chi)-(K-1)**2*chi
    discriminant=load**2-4*(K+1)**2*(K-1)**2*chi*(1+chi)
    assert load>0 and discriminant>0
    return dict(K=K,chi=chi,L=L,load=load,discriminant=discriminant)

def region(box,z0,v0,q0,C):
    _,z,D,K,planar,ns,hs,H,V=h.build(box);Ci=inv(C)
    gg=[('volume',D),('gamma_positive',K[2]),('gamma_upper',GAMMA_UP*D-K[2])]
    for f,(n,hh,face) in enumerate(zip(ns,hs,h.FACES)):
        gg.append((f'support_positive_{f}',H[f]))
        for i in range(10):
            sl=hh-h.dot(n,z[i])
            if i in face:assert sl.zero()
            else:gg.append((f'nonincident_{f}_{i}',sl))
    for i in range(10):
        inc=[f for f in range(9) if i in h.FACES[f]];chosen=None
        for triple in combinations(inc,3):
            p=h.det([ns[f] for f in triple]);lo,hi=p.bound()
            if lo>0:chosen=p;break
            if hi<0:chosen=-p;break
        assert chosen is not None,('vertex_rank',i)
        gg.append((f'vertex_rank_{i}',chosen))
    for j in range(3):
        alpha=ALPHA[j]
        gg.extend([(f'alpha_lower_{j}',2*K[2]-(1-alpha)*D),
                   (f'alpha_square_{j}',K[2]-alpha*alpha*D),
                   (f'turn_r_{j}',2*alpha*(D-K[2])-(1+alpha)*K[2])])
        for f,(n,hh,t,face) in enumerate(planar):
            for i in range(7):
                p=(D-K[2])*hh-(1+alpha)*h.dot(n,K[:2])+alpha*(D-K[2])*h.dot(n,z[i][:2])+(1+alpha)*K[2]*h.dot(n,z[j+7][:2])
                gg.append((f'R_{j}_{f}_{i}',p))
            gg.append((f'A_{j}_{f}',2*H[face]-D*(t-h.dot(n,z[j+7][:2]))))
        gg.append((f'chi_{j}',(1+CHI[j])*(D-K[2])**2-C[2][2]*h.quad(V[j+7],Ci)))
    for i in range(10):
        for f in range(9):
            gg.append((f'outer_{i}_{f}',(1+EPS)*D-h.dot(q0[f],V[i])))
            gg.append((f'inner_{i}_{f}',H[f]-(1-EPS)*D*h.dot(ns[f],v0[i])))
    return gg

def main():
    z0,v0,q0,D0,g0,edge,planar=body(THETA);C=reference(g0)
    endpoint=bound_all(v0,q0,edge,C)
    assert ((1+EPS)/(1-EPS))**2*BOUND<UPSILON
    factor=F(16,27);K=factor*UPSILON**2
    pg=[product_guard(K,x,y) for x,y in zip(CHI,CEILING)]
    gaps=[a*a-GAMMA_UP*(1-1/L) for a,L in zip(ALPHA,CEILING)]
    assert min(gaps)>0
    # Exact elementary trigonometric majorants, with Machin's identity.
    pil=16*sum(((-1)**j*F(1,5)**(2*j+1)/F(2*j+1) for j in range(6)),F(0))-4*F(1,239)
    assert pil>F(333,106)
    cup=lambda t:1-t*t/2+t**4/24
    assert cup(F(333,106)/7)<F(901,1000) and F(901,1000)**7<F(1,2)
    assert cup(F(333,106)/20)**20*cup(F(333,106)/18)**18<factor
    guards=region(BOX,z0,v0,q0,C);bad=[];rows=[]
    for name,p in guards:
        lo,hi=p.bound();rows.append(dict(name=name,terms=len(p.d),lower=lo,upper=hi))
        if lo<=0:bad.append((name,float(lo),float(hi)))
    out=dict(version=1,theta0=THETA,box=BOX,radius=RADIUS,reference=C,
             epsilon=EPS,endpoint_upsilon_bound=BOUND,regional_upsilon_bound=UPSILON,
             endpoint_pair_count=endpoint['edge_pair_count'],endpoint_intervals=endpoint['feasible_intervals'],endpoint_leaves=endpoint['leaf_count'],
             alpha=ALPHA,chi_bounds=CHI,product_guards=pg,gamma_upper=GAMMA_UP,hybrid_gaps=gaps,
             guard_count=len(guards),coefficient_count=sum(len(p.d) for n,p in guards),all_positive=not bad,guards=rows)
    path=Path(sys.argv[1] if len(sys.argv)>1 else 'ORTHOGONAL_HYBRID_BOX.json')
    data=(json.dumps(strings(out),sort_keys=True,indent=2)+'\n').encode();path.write_bytes(data)
    print('GUARDS',len(guards),'COEFFICIENTS',out['coefficient_count'],'BAD',len(bad))
    if bad:print(bad)
    print(path.name,len(data),hashlib.sha256(data).hexdigest())
    assert not bad,'The asserted whole physical box did not close'
    print('H5_ORTHOGONAL_SHELL_HYBRID_WHOLE_BLIND_FRONTIER_BOX_PASS')
if __name__=='__main__':main()
