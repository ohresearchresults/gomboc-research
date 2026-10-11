# material-ae119dce474a

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Exact nonwinner isolating the remaining actual-chord information.
Dependency: the complete preserved lift_core.py, no numerical solver.
"""
from lift_core import *
import json

def run():
    B=geometry((R(1,10),R(9,10),R(3,25),R(3,5),R(3,20)))
    c=B['g'][:2,0];ga=B['g'][2];H=1-ga;k=1-2*ga
    sig=B['Sigma'];z=sig[2,2];D=sig.inv()[:2,:2];m=sig[:2,2]/z
    a=B['raw'][9][:2,0];b=B['raw'][3][:2,0]
    l=S.Matrix((0,R(66,5)))
    ap=a-c-H*m;L=(l.T*D.inv()*l)[0];s=(1-l.dot(ap))/H
    w=s*D.inv()*l/L;v=w-m
    yy=[q[:2,0]+q[2]*v for q in B['v']];A=yy[9]
    assert l.dot(A)==1
    h=S.Matrix((-A[1],A[0]));G=l*l.T+h*h.T/10000
    assert G.det()==R(1,10000) and pd(G)
    C=D.inv()+z*w*w.T;t=(z*w.T*D*w)[0];ev=ELL*(1+t)
    assert 0<ev<1
    lower=ev*S.trace(G*C)/(z*(1-ev))
    upper=((A.T*G*yy[3])[0]-1)/H
    assert 0<lower<upper
    eta=(lower+upper)/2
    top=[1-(yy[j].T*G*yy[j])[0] for j in (7,8)]
    assert min(top)>0 and (A.T*G*A)[0]==1
    beta=c+ga*v;near=[R(0)];far=[];slacks=[]
    for p,q in zip(B['raw'][:7],B['raw'][1:7]+B['raw'][:1]):
        e=q[:2,0]-p[:2,0];n=S.Matrix((e[1],-e[0]));hh=n.dot(p[:2,0]);ee=n.dot(A);ff=n.dot(beta)-hh
        slacks.append(hh-n.dot(beta-A))
        if ee>0:near.append(ff/ee)
        elif ee<0:far.append(ff/ee)
        else:assert ff<=0
    tau=min(far)
    assert max(near)<ga/H<tau
    r=k*yy[3]+2*ga*A
    lens=tau*tau-(r.T*G*r)[0]
    kap=R(924733153857541,21600000000000);rho=kap/(1+kap)**2
    tangential=(C.det()*G.det()-rho*S.trace(C*G)**2,
                D.det()*G.det()-rho*S.trace(D*G.adjugate())**2)
    assert lens>0 and min(slacks)>0 and tau>1 and max(tangential)<0
    portrait=audit(B,v,G/eta)
    assert portrait['counts']==(4,3,5) and not portrait['weak'] and portrait['zero_primitives']==0
    return dict(theta=B['theta'],l=l,shear=v,G=G,eta=eta,amplified_eta_lower=lower,
        spoke_eta_upper=upper,top_norm_gaps=top,actual_chord_tau=tau,
        strict_chord_lens_slack=lens,chord_necessary_point_slacks=slacks,
        tangential_conic_slacks=tangential,physical=portrait)

if __name__=='__main__':
    out=run()
    print(json.dumps(encode(out),sort_keys=True,indent=2))
    print('REGRESSION_RANK_ONE_ACTUAL_CONTROL_V1_PASS')
