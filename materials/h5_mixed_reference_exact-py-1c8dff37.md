# material-1c8dff377cfe

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Exact finite geodesic mixed-reference obstruction, stdlib only.
Input body theta=(3/20,3/20,3/20,9/20,13/100), marked top9 and basal pole0.
All rational witnesses are reconstructed here. No floating locator output is read.
Requires h5_reference_core.py and Python>=3.11; assertions must be enabled.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib,json,sys
from h5_reference_core import *

THETA=(Q(3,20),Q(3,20),Q(3,20),Q(9,20),Q(13,100))
W=((Q(223142,1000000),Q(-130077,1000000)),(Q(-130077,1000000),Q(219126,1000000)))
LOWER=Q(14,3)

def solve(A,b):
    n=len(b);R=[list(row)+[v] for row,v in zip(A,b)]
    for k in range(n):
        pivot=next(i for i in range(k,n) if R[i][k])
        R[k],R[pivot]=R[pivot],R[k];d=R[k][k];R[k]=[v/d for v in R[k]]
        for i in range(n):
            if i!=k:
                d=R[i][k];R[i]=[x-d*y for x,y in zip(R[i],R[k])]
    return tuple(row[-1] for row in R)

def make_pairs(B):
    V=B['v'];P=B['poles'];gx,gy,gamma=B['g']
    def on_polar_edge(w,k=5,l=6):
        t=-dot(w,P[k])/dot(w,sub(P[l],P[k]));assert 0<t<1
        n=add(P[k],scale(t,sub(P[l],P[k])));assert dot(w,n)==0
        return n,t
    w1=V[1];n1,t1=on_polar_edge(w1)
    s2=-V[3][0]/(V[4][0]-V[3][0]);assert 0<s2<1
    w2=add(V[3],scale(s2,sub(V[4],V[3])));n2=(-1/gx,Q(0),Q(0))
    s3=-V[5][1]/(V[6][1]-V[5][1]);assert 0<s3<1
    w3=add(V[5],scale(s3,sub(V[6],V[5])));n3=(Q(0),-1/gy,Q(0))
    s4=Q(1,16);w4=add(V[1],scale(s4,sub(V[2],V[1])));n4,t4=on_polar_edge(w4)
    pairs=((w1,n1),(w2,n2),(w3,n3),(w4,n4))
    for w,n in pairs:
        assert dot(w,n)==0
        assert all(dot(w,q)<=1 for q in P)
        assert all(dot(n,v)<=1 for v in V)
    return pairs,{'w2_edge_parameter':str(s2),'w3_edge_parameter':str(s3),'w4_edge_parameter':str(s4),
                  'n1_polar_parameter':str(t1),'n4_polar_parameter':str(t4)}

def gradients(B,pairs):
    gamma=B['g'][2];h=1-gamma;a=B['v'][9];b=a[:2]
    d=W[0][0]*W[1][1]-W[0][1]**2;assert W[0][0]>0 and d>0
    Wi=((W[1][1]/d,-W[0][1]/d),(-W[0][1]/d,W[0][0]/d))
    G=[];Gb=[];prod=[]
    for w,n in pairs:
        t=w[2]/h;y=sub(w[:2],scale(t,b));z=mv(Wi,y);nn=n[:2];nb=dot(n,a)
        A=dot(y,z)+t*t;BB=quad(nn,W)+nb*nb;p=A*BB
        assert A>0 and BB>0 and p>LOWER
        gw=((-z[0]**2*BB+A*nn[0]**2)/p,
            (-2*z[0]*z[1]*BB+2*A*nn[0]*nn[1])/p,
            (-z[1]**2*BB+A*nn[1]**2)/p)
        gb=add(scale(-2*t/A,z),scale(2*nb/BB,nn))
        G.append(gw);Gb.append(gb);prod.append(p)
    coeff=tuple(tuple(G[i][k] for i in range(4)) for k in range(3))+((Q(1),)*4,)
    weights=solve(coeff,(Q(0),Q(0),Q(0),Q(1)))
    assert all(x>0 for x in weights) and sum(weights)==1
    assert all(sum(weights[i]*G[i][k] for i in range(4))==0 for k in range(3))
    bg=tuple(sum(weights[i]*Gb[i][k] for i in range(4)) for k in range(2))
    load=quad(bg,W);assert load<Q(2,5)<1
    return prod,G,Gb,weights,bg,load

def trig_lower():
    # Machin identity gives pi<22/7 using alternating arctangent bounds.
    a5=sum(((-1)**k*Q(1,5)**(2*k+1)/Q(2*k+1) for k in range(7)),Q(0))
    a239=Q(1,239)-Q(1,239)**3/3
    assert 16*a5-4*a239<Q(22,7)
    # cos(x)>1-x^2/2 for 0<x<pi/2; both factors positive.
    lo=(1-(Q(22,7)/20)**2/2)**20*(1-(Q(22,7)/18)**2/2)**18
    assert lo>Q(59,100)
    return lo

def serial(x):
    if isinstance(x,Q):return str(x)
    if isinstance(x,dict):return {k:serial(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [serial(v) for v in x]
    return x

def main():
    if not __debug__:raise RuntimeError('Assertions are required; do not use python -O')
    B=body(THETA);pairs,locations=make_pairs(B);p,G,Gb,weights,bg,load=gradients(B,pairs)
    C=aligned_reference(B,9,W);a=B['v'][9];q=B['poles'][0];c=dot(a,q)
    assert quad(a,inv(C))*quad(q,C)==c*c
    J=tuple(tuple(Q(i==j)-2*a[i]*q[j]/c for j in range(3)) for i in range(3))
    assert mm(J,J)==tuple(tuple(Q(i==j) for j in range(3)) for i in range(3))
    assert mm(mm(J,C),transpose(J))==C
    f_lower=trig_lower();k=Q(59,100)*LOWER**2;ceiling_floor=(k+1)**2/(4*k)
    assert k>1 and ceiling_floor>Q(37,10)
    gamma=B['g'][2];alpha=B['amax'][2];target_max=gamma/(gamma-alpha*alpha)
    assert alpha*alpha<gamma and target_max<Q(18,5)
    # This bound is top9-specific R, not only the smaller common-R parameter.
    assert B['limiting'][2]==(0,4,9)
    assert B['Amin']>0
    chosen=(Q(1,2),Q(1,2),Q(23,50))
    for j,alpha0 in zip(range(7,10),chosen):
        assert 0<alpha0<1 and alpha0>=1-2*gamma
        assert all(B['Rval'](alpha0,i,j,k0)>0 for i in range(7) for k0 in range(7))
        assert gamma*(1+alpha0)<2*alpha0*(1-gamma)
    # The simple exact bound cos(pi/7)^7<1/2, using pi>333/106.
    pi_lower=16*sum(((-1)**k0*Q(1,5)**(2*k0+1)/Q(2*k0+1) for k0 in range(6)),Q(0))-4*Q(1,239)
    assert pi_lower>Q(333,106)
    x=Q(333,106)/7;cu=1-x*x/2+x**4/24;assert cu**7<Q(1,2)
    # Actual body remains a nonattaining physical control, not an artificial pole set.
    standard=census(B,((5,1,2),(1,3,-1),(2,-1,4)))
    top9M=((3,1,-1),(1,5,2),(-1,2,4));top9c=census(B,top9M)
    norms=[quad(v,top9M) for v in B['v']]
    assert norms[9]>norms[7] and norms[9]>norms[8]
    assert not standard['weak_edges'] and standard['zero_primitives']==0
    assert not top9c['weak_edges'] and top9c['zero_primitives']==0
    out={'theorem':'H5_ALL_REFERENCE_ORTHOGONAL_MIXED_TEMPLATE_BARRIER_V1','theta':THETA,'volume':B['volume'],'centroid':B['g'],
         'W':W,'C':C,'J':J,'pairs':pairs,'locations':locations,'products':p,'gradients_W':G,'gradients_b':Gb,
         'positive_weights':weights,'summed_b_gradient':bg,'b_dual_norm_squared':load,'universal_U_times_exp_delta_lower':LOWER,
         'f10_f9_rational_lower':f_lower,'K_floor':k,'product_ceiling_floor':ceiling_floor,
         'top9_alpha_max':alpha,'top9_maximum_geometric_target':target_max,
         'strict_floor_minus_target':ceiling_floor-target_max,'standard_census':standard,'top9_max_control_census':top9c,
         'R_parameters':chosen,'scope':'All auxiliary references C>0 for marked (top9,basal pole), NOT physical joint110 existence or exclusion.'}
    raw=(json.dumps(serial(out),sort_keys=True,indent=2)+'\n').encode()
    path=Path(sys.argv[1] if len(sys.argv)>1 else 'H5_MIXED_REFERENCE_EXACT.json');path.write_bytes(raw)
    print(path.name,len(raw),hashlib.sha256(raw).hexdigest())
    print('H5_ALL_REFERENCE_ORTHOGONAL_MIXED_TEMPLATE_BARRIER_PASS')
if __name__=='__main__':main()
