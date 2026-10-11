# material-83f3d8da0e88

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Exact all-G/all-positive-height certificate in a macroscopic W-only shear box.
Dependencies: complete lift_core.py, SymPy. Uses actual moments and true facets.
"""
from lift_core import *
from itertools import product
from math import comb
import json

LOW=(R(2,25),R(23,100));HIGH=(R(7,50),R(7,25))

def bernstein(poly,variables,lo,hi):
    # Affine power-basis substitution, then exact tensor-product Bernstein basis.
    poly=S.Poly(poly,*variables);n=poly.degree_list();power={}
    for exps,c in poly.terms():
        for kk in product(*(range(a+1) for a in exps)):
            value=c
            for i,(a,k) in enumerate(zip(exps,kk)):
                value*=comb(a,k)*lo[i]**(a-k)*(hi[i]-lo[i])**k
            power[kk]=power.get(kk,S.S(0))+value
    vals=[]
    for kk in product(*(range(a+1) for a in n)):
        value=S.S(0)
        for aa,c in power.items():
            if all(a<=k for a,k in zip(aa,kk)):
                v=c
                for k,a,d in zip(kk,aa,n):v*=R(comb(k,a),comb(d,a))
                value+=v
        vals.append(value)
    return dict(degrees=n,count=len(vals),minimum=min(vals),maximum=max(vals))

def algebra(B):
    x,y,u=S.symbols('x y u');p=S.Matrix((x,y));g=B['g'];gamma=g[2];H=1-gamma;k=1-2*gamma
    v=(2*g[:2,0]-B['raw'][9][:2,0]-p)/k
    yy=[a[:2,0]+a[2]*v for a in B['v']]
    sig=B['Sigma'];zz=sig[2,2];D=sig.inv()[:2,:2];m=sig[:2,2]/zz;w=v+m
    t=S.expand((zz*w.T*D*w)[0]);ee=S.expand(ELL*(1+t))
    C=(sig[:2,:2]+sig[:2,2]*v.T+v*sig[2,:2]+zz*v*v.T).applyfunc(S.expand)
    J=S.Matrix.hstack(yy[9],yy[3]);det=S.expand(J.det());adj=J.adjugate()
    Tn=(adj*C*adj.T).applyfunc(S.expand)
    # Basal true edge 3->4 supplies an upper bound for the actual chord endpoint.
    a=B['raw'][3][:2,0];b=B['raw'][4][:2,0];edge=b-a;normal=S.Matrix((edge[1],-edge[0]));height=normal.dot(a)
    den=S.expand(-k*normal.dot(yy[9]));num=S.expand(height-normal.dot(p))
    Xnum=den+u*num
    P=S.expand(ee*H*(Tn[0,0]*den**2+2*Tn[0,1]*den*Xnum+Tn[1,1]*Xnum**2)-zz*(1-ee)*u*num*den*det**2)
    J7=S.Matrix.hstack(yy[9],yy[7]);det7=S.expand(J7.det());cd=(J7.adjugate()*yy[4]).applyfunc(S.expand)
    # Y4=c*Y9+d*Y7. Both c+d<1 and c-d<1 imply c+abs(d)<1.
    # This excludes port94 even where the [Y9,Y4] chart is singular.
    tests=dict(normal_denominator=den,chord_slack=num,port93_determinant=det,
               negative_top97_determinant=-det7,port94_plus=cd[0]+cd[1]-det7,
               port94_minus=cd[0]-cd[1]-det7,one_minus_effective_floor=1-ee)
    beta=g[:2,0]+gamma*v
    tests['negative_basal_foot_y']=-beta[1]
    tests['top78_necessary_point_above_base']=y+B['theta'][4]-max(a[1] for a in B['raw'][:7])
    for i,(a,b) in enumerate(zip(B['raw'][:7],B['raw'][1:7]+B['raw'][:1])):
        edge=b[:2,0]-a[:2,0];n=S.Matrix((edge[1],-edge[0]));hh=n.dot(a[:2,0])
        tests['interior_basal_point_slack_'+str(i)]=hh-n.dot(p)
    return (x,y,u),P,tests,dict(shear=v,regression_t=t,effective_floor=ee,actual_covariance=sig,
                             actual_centroid=g,volume=B['volume'],chord_normal=normal,chord_support=height)

def hypotheses(B):
    g=B['g'];ga=g[2];k=1-2*ga;z=B['raw']
    assert B['volume']==R(881291,9600000)
    assert g==S.Matrix((R(7368835529,28201312000),R(3427883561,28201312000),R(50317,153268)))
    assert R(1,4)<ga<R(1,3)
    base=[]
    for a,b in zip(z[:7],z[1:7]+z[:1]):
        d=b[:2,0]-a[:2,0];n=S.Matrix((d[1],-d[0]));base.append((n,n.dot(a[:2,0])))
    W=[];RR=[];alpha=ga+R(1,4);beta=ga*(1+alpha)/(1-ga)
    for i in range(7):
        for j in (7,8,9):
            point=2*g-k*z[i]-2*ga*z[j];assert point[2]==0
            W.extend(h-n.dot(point[:2,0]) for n,h in base)
            rpoint=(1+alpha+beta)*g-alpha*z[i]-beta*z[j]
            RR.extend(h-n.dot(rpoint[:2,0]) for n,h in base)
    A=[1+q.dot(z[j]-g) for q in B['poles'][1:] for j in (7,8,9)]
    assert min(W)>0 and min(A)>0 and min(RR)<0
    return dict(minimum_W_slack=min(W),minimum_A_slack=min(A),minimum_R7_slack=min(RR))

def countercontrol(B):
    # A physical local-gate witness that passes BOTH tangential condition conics
    # and the older unamplified normal floor, but is excluded by the new theorem.
    g=B['g'];ga=g[2];H=1-ga;k=1-2*ga
    p=S.Matrix((R(1,10),R(6,25)));v=(2*g[:2,0]-B['raw'][9][:2,0]-p)/k
    yy=[a[:2,0]+a[2]*v for a in B['v']];J=S.Matrix.hstack(yy[9],yy[3])
    Gram=S.Matrix(((1,R(1173,1000)),(R(1173,1000),R(2821,1000))))
    G=(J.T.inv()*Gram*J.inv()).applyfunc(S.factor);eta=R(23,100)
    assert pd(G) and (yy[9].T*G*yy[9])[0]==1
    top=[1-(yy[j].T*G*yy[j])[0] for j in (7,8)]
    spoke=(yy[9].T*G*(yy[3]-yy[9]))[0]-H*eta
    beta=g[:2,0]+ga*v;cuts=[]
    for a,b in zip(B['raw'][:7],B['raw'][1:7]+B['raw'][:1]):
        edge=b[:2,0]-a[:2,0];n=S.Matrix((edge[1],-edge[0]));h=n.dot(a[:2,0]);den=n.dot(yy[9])
        if den<0:cuts.append((n.dot(beta)-h)/den)
    tau=min(cuts);r=k*yy[3]+2*ga*yy[9];lens=tau*tau-(r.T*G*r)[0]
    sig=B['Sigma'];zz=sig[2,2];D=sig.inv()[:2,:2];m=sig[:2,2]/zz;w=v+m;t=(zz*w.T*D*w)[0]
    C=sig[:2,:2]+sig[:2,2]*v.T+v*sig[2,:2]+zz*v*v.T
    old=eta-ELL*S.trace(G*C)/(zz*(1-ELL))
    ee=ELL*(1+t);new=eta-ee*S.trace(G*C)/(zz*(1-ee))
    kap=R(924733153857541,21600000000000);rho=kap/(1+kap)**2
    ellipse1=C.det()*G.det()-rho*S.trace(C*G)**2
    ellipse2=D.det()*G.det()-rho*S.trace(D*G.adjugate())**2
    assert min(*top,spoke,lens,old,ellipse1,ellipse2)>0 and new<0
    portrait=audit(B,v,G/eta)
    assert portrait['counts']==(2,3,3) and portrait['U']==[3,6,7] and portrait['S']==[1,5]
    assert not portrait['weak'] and portrait['zero_primitives']==0
    return dict(basal_parameter=p,shear=v,G=G,eta=eta,tau=tau,top_gaps=top,
                true_spoke=spoke,strict_lens_slack=lens,old_normal_floor_slack=old,
                amplified_normal_floor_slack=new,tangential_conic_slacks=(ellipse1,ellipse2),
                physical_census=portrait)

def run():
    B=geometry((R(1,10),R(9,10),R(3,25),R(3,5),R(3,20)))
    vars,P,tests,data=algebra(B);x,y,u=vars
    results={}
    # The port93 determinant has positive sign at the centre; all tests chosen positive.
    for name,f in tests.items():results[name]=bernstein(f,(x,y),LOW,HIGH)
    results['port93_floor_polynomial']=bernstein(P,vars,LOW+(0,),HIGH+(1,))
    assert results['port93_floor_polynomial']['minimum']>R(1,3000000)
    return dict(box=(LOW,HIGH),source=data,checks=results,geometry_hypotheses=hypotheses(B),
                strict_local_nonwinner=countercontrol(B),all_positive=all(r['minimum']>0 for r in results.values()))

if __name__=='__main__':
    if not __debug__:raise RuntimeError('Assertions must be enabled')
    out=run();print(json.dumps(encode(out),sort_keys=True,indent=2))
    assert out['all_positive']
    print('AMPLIFIED_NORMAL_W_ONLY_MACRO_SHEAR_BOX_V1_PASS')
