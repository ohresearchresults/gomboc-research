# material-302ded340f27

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# ROOT_A_CONE_LOCATION_MOMENT_V1

## Status
Coordinator analytic necessary inequalities for actual proper root-only bodies and an exact formal control excluded by them. No actual high-trace polytope, stationary maximum, mechanical110 construction or new global bound is claimed. Bounds remain34<=Cmin<=622.

## Actual geometric hypotheses
A=0,B=e_z,C=e_y,D=e_x. P=conv(A,B,C,D,F), where F is a compact convex positive-area root in ell=0,x>0,y>0. ell=1-(1-d)x-(1-c)y-(1-b)z, with0<b,c,d<1. All integrals use the original uniform body. Write V=int_P1,t=6V,u=4int_Px/V,v=4int_Py/V,alpha=1-b,delta=1-d,epsilon=1-c. No stationarity or sign restriction onz.

Radial projection from A to ell=0 sends B,C,D to B0=(0,0,1/alpha),C0=(0,1/epsilon,0),D0=(1/delta,0,0). In scaled root coordinates X=delta*x,Y=epsilon*y let K=conv(F_scaled,Delta),Delta=conv((0,0),(1,0),(0,1)). Strict positivity of F's x,y makes BOTH axis edges of K exactly unit length. Put kappa=2Area(K)>=1. The A-cone Q=conv(A,K_root) contains P. For every q>=M=max(b,c,d), its section ell=q equals P's section: each projected generator at that height belongs to its actual A-to-generator segment, then use convexity. The normalized height density therefore has exact top formula
p_ell(q)=3*kappa*(1-q)^2/(alpha*delta*epsilon*t).
Define lambda=kappa/t by this actual top coefficient. In the accepted four-law decomposition this equals the coefficient of mu[1,c,min(b,d),max(b,d)], since the other laws end at or below M. No rebase approximation is involved.

## Elementary planar lemma
Let L be planar convex, h>=0 affine, with genuine base h=0 of length ell_base; beta=ell_base/|grad h| and area A_L. Coarea gives A_L=int_0^R f(s)ds, int_Lh=int_0^R s f(s)ds, with f concave,nonnegative,f(0)=beta,R=max h. Concavity implies f>=beta(1-s/R),hence R<=H=2A_L/beta. Compare g(s)=beta(1-s/H) on[0,H], extending f by zero after R. Their masses agree. On[0,R],f-g is concave and vanishes at zero, so (f-g)/s is nonincreasing. There is at most one positive-to-negative sign change; beyond R the difference is nonpositive. Equal mass yields int s f<=int s g=2A_L^2/(3beta). This includes a nonzero terminal section; zero-area limits are direct. Triangles attain equality.

Apply to K with h=X and h=Y,beta=1: int_KX,int_KY<=kappa^2/6. For their sum use L=K intersect{X+Y>=1}. Since K intersect{X+Y<=1}=Delta, AreaL=(kappa-1)/2. Its genuine base edge has length sqrt2 and |grad(X+Y-1)|=sqrt2, so beta=1. Therefore
int_K(X+Y)<=1/3+(kappa-1)/2+(kappa-1)^2/6=kappa(kappa+1)/6.
For kappa=1 use K=Delta directly.

## Actual body moment conclusion
Cone integration gives int_Q delta*x=(4alpha*delta*epsilon)^(-1)int_KX and the analogous Y identity. P subset Q and x,y>=0 give

delta*u <= kappa^2/(alpha*delta*epsilon*t)=t*lambda^2/(alpha*delta*epsilon),
epsilon*v <= kappa^2/(alpha*delta*epsilon*t),
delta*u+epsilon*v <= kappa(kappa+1)/(alpha*delta*epsilon*t)=lambda(t*lambda+1)/(alpha*delta*epsilon).

These are necessary, not sufficient realization conditions. They include negative-z bodies. No endpoint>=1 or zero-endpoint extension is claimed. No uniformly refilled projective image replaces the original centroid.

## Exact formal control
b=1/2,c=1/16,d=1/32,t=9/4,r=d,s=b,rho=1/20,omega=1/30,gamma=sH=9/20,lambda=7/15,S=1/12,H=9/10. The law is lambda*mu[1,c,r,s]+rho*mu[c000]+omega*mu[cr00]+gamma*mu[csr0]. It has m=4E/V=651/640,u=31/20,v=8/5,w=-3/80,T=12472/5859>51/25. Exact checks below establish nonnegative density of mass1 and meanm/4,C1 internal joins,doublezero at1,and p'^2-2pp''>=0 on every piece; hence sqrt(density) is concave on its full support. The full Dlow,Qmiddle,top and listed scalar moment conditions hold. A nonnegative FORMAL seven-type C-fan lift is (4/9,1/20,0,1/30,0,77/180,2/45) in orderT0,CFFF,CBFF,CDFF,CAFF,CBDF,CADF; equality of the entire pdf is checked, not just the mean. These are not actual determinant fractions of a common constructed body.

Here kappa=21/20 and alpha*delta*epsilon*t=4185/4096. The combined actual-body inequality would require1921/640<=73472/34875, with exact violation3993023/4464000>0. Both individual inequalities also fail. Thus a full concave height law plus these scalar conditions is not sufficient for body realization. Independently b+c=9/16 violates the accepted high-trace full-maximum condition b+c>9/8: the control is not stationary.

## Complete source-only recovery
Save the literal source below as a_cone_exact.py, UTF8,LF,one final LF. Run in an empty writable directory with assertions enabled:
python -S a_cone_exact.py
It uses CPython3.13.5 standard library only,no input files,no seed,no optimizer. Expected markers:
EXACT_ALL_INTERVAL_BM_FORMAL_CONTROL_PASS
ROOT_A_CONE_LOCATION_MOMENT_CONTROL_EXCLUSION_PASS

Executed exact source/output pins:
a_cone_exact.py 4887bytes SHA2566e7ed46a44a2d28ad1bc6df42ea4d45bbfacdad3eaccad8ba2f27288d946eec9
slice_control.json 1263bytes SHA256edeed8a9f128bb10514200f6fc5d0079a83d4df350eb6765f23dec12914f4f19
cone_control.json 742bytes SHA2568237dc7953396a507a7b795e73f3479b13579c01e281875e093fc8e0b102f724
The introductory docstring comes from an earlier exploratory source; this complete retained unit has no numerical quadrature or third-party dependency.

```python
"""Exact four-law rational control and exploratory slice-location bounds.
Python 3.13.5; no external input. Fractions are the proof layer; numerical
quadrature is exploratory only and is explicitly labelled in output.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib

def pdf_jet(knots,mid):
    h=sorted(map(F,knots));mid=F(mid)
    cur=[(F(h[i]<=mid<h[i+1]),F(0),F(0)) for i in range(3)]
    def mul(q,a,b):return (a*q[0],a*q[1]+b*q[0],a*q[2]+b*q[1])
    for deg in (1,2):
        nxt=[]
        for i in range(3-deg):
            q=[F(0)]*3
            den=h[i+deg]-h[i]
            if den:q=[x+y for x,y in zip(q,mul(cur[i],(mid-h[i])/den,1/den))]
            den=h[i+deg+1]-h[i+1]
            if den:q=[x+y for x,y in zip(q,mul(cur[i+1],(h[i+deg+1]-mid)/den,-1/den))]
            nxt.append(tuple(q))
        cur=nxt
    return tuple(3*x/(h[-1]-h[0]) for x in cur[0])
def mix(laws,x):return tuple(sum((w*pdf_jet(h,x)[i] for h,w in laws),F(0)) for i in range(3))
def integ(jet,mid,lo,hi,power=0):
    # Powers 0 and 1 suffice for exact total mass and height mean.
    assert power in (0,1)
    if power:jet=(mid*jet[0],jet[0]+mid*jet[1],jet[1]+mid*jet[2],jet[2])
    return sum(v*((hi-mid)**(i+1)-(lo-mid)**(i+1))/(i+1) for i,v in enumerate(jet))
def control():
    b=F(1,2);c=F(1,16);d=F(1,32);t=F(9,4)
    rho=F(1,20);om=F(1,30);ga=F(9,20);la=F(7,15)
    s=b;r=d;S=rho+om;H=ga/s
    m=c+r+(1+s)*(1-S)-r*rho-ga
    u=F(31,20);v=F(8,5);w=(4+(d-1)*u+(c-1)*v-m)/(1-b)
    T=((1+b+c)*u+(1+b+d)*v)/(t*m)
    D=om*(c*S-r*rho)-c*r*rho*H
    Q=(c*S-r*rho)*((c*(1+s)-s)*H-(c-r)*(1-S))+s*c*c*H*H-c*r*(c-r*rho)*H
    top=1-S-H
    laws=[((1,c,r,s),la),((c,0,0,0),rho),((c,r,0,0),om),((c,s,r,0),ga)]
    knots=[F(0),r,c,s,F(1)];pieces=[];mass=mean=F(0)
    for lo,hi in zip(knots,knots[1:]):
        mid=(lo+hi)/2;j=mix(laws,mid);disc=j[1]**2-4*j[0]*j[2]
        assert j[0]>0 and disc>=0
        mass+=integ(j,mid,lo,hi);mean+=integ(j,mid,lo,hi,1)
        pieces.append(dict(lo=str(lo),hi=str(hi),mid=str(mid),jet=list(map(str,j)),disc=str(disc)))
    assert mass==1 and mean==m/4
    assert min(D,Q,top)>0 and la>1/t
    assert T>F(51,25) and u>=1 and v>=1 and u+v<=t+1
    assert (1+b+c)*u/(t*m)<F(10,9) and (1+b+d)*v/(t*m)<F(10,9)
    assert 2-t<=w<=t+2-u-v
    masses=[1/t,rho,F(0),om,F(0),F(77,180),F(2,45)]
    assert sum(masses)==1 and min(masses)>=0
    # Original true-C-fan type laws: T0,CFFF,CBFF,CDFF,CAFF,CBDF,CADF.
    fanlaws=list(zip([(1,b,c,d),(c,0,0,0),(c,b,0,0),(c,d,0,0),(c,1,0,0),(c,b,d,0),(c,1,d,0)],masses))
    for lo,hi in zip(knots,knots[1:]):assert mix(laws,(lo+hi)/2)==mix(fanlaws,(lo+hi)/2)
    record={k:str(z) for k,z in dict(b=b,c=c,d=d,t=t,rho=rho,omega=om,gamma=ga,lam=la,S=S,H=H,m=m,u=u,v=v,w=w,T=T,D_low=D,Q_middle=Q,top=top).items()}
    record['density_pieces']=pieces;record['formal_C_fan_masses']=list(map(str,masses))
    record['status']='FORMAL_RELAXATION_CONTROL; no polytope or 110 realization asserted'
    return record,laws,knots,(b,c,d,t,u,v)


def main():
 rec,laws,knots,(b,c,d,t,u,v)=control()
 last=None
 for lo,hi in zip(knots,knots[1:]):
  mid=(lo+hi)/2;j=mix(laws,mid)
  def value(q):return j[0]+j[1]*(q-mid)+j[2]*(q-mid)**2
  def slope(q):return j[1]+2*j[2]*(q-mid)
  assert value(lo)>=0 and value(hi)>=0
  if j[2]>0:
   q=mid-j[1]/(2*j[2])
   if lo<q<hi:assert value(q)>0
  assert j[1]**2-4*j[0]*j[2]>=0
  if last is not None:assert last==(value(lo),slope(lo))
  last=(value(hi),slope(hi))
 assert last==(0,0)
 la=F(rec['lam']);k=t*la;alpha=1-b;delta=1-d;epsilon=1-c
 den=alpha*delta*epsilon*t
 lhs=delta*u+epsilon*v;rhs=k*(k+1)/den
 indi=k*k/den
 assert k>=1 and lhs>rhs and delta*u>indi and epsilon*v>indi
 out={'identity':'ROOT_A_CONE_LOCATION_MOMENT_V1',
      'status':'EXACT_FORMAL_BM_CONTROL_EXCLUDED_BY_ACTUAL_BODY_MOMENT_NECESSITY',
      'b':str(b),'c':str(c),'d':str(d),'t':str(t),'lambda':str(la),'kappa':str(k),
      'alpha_delta_epsilon_t':str(den),'u':str(u),'v':str(v),
      'combined_lhs':str(lhs),'combined_upper_bound':str(rhs),'combined_violation':str(lhs-rhs),
      'individual_upper_bound':str(indi),'delta_u':str(delta*u),'epsilon_v':str(epsilon*v),
      'T':rec['T'],'stationary_b_plus_c':str(b+c),
      'stationary_status':'Also excluded by the previously accepted full-maximum necessary condition b+c>9/8; this is an arbitrary-VALUE relaxation control, not a full-maximum candidate.'}
 raw=(json.dumps(out,sort_keys=True,indent=2)+'\n').encode()
 Path('cone_control.json').write_bytes(raw)
 raw2=(json.dumps(rec,sort_keys=True,indent=2)+'\n').encode()
 Path('slice_control.json').write_bytes(raw2)
 for name,bs in [('slice_control.json',raw2),('cone_control.json',raw)]:
  print(name,len(bs),hashlib.sha256(bs).hexdigest())
 print('EXACT_ALL_INTERVAL_BM_FORMAL_CONTROL_PASS')
 print('ROOT_A_CONE_LOCATION_MOMENT_CONTROL_EXCLUSION_PASS')
if __name__=='__main__':main()
```

## Interfaces still open
Fullheightconcavity plus these necessary moments has not been shown sufficient or enough for the51/25threshold. No numerical scalar search is a body construction. New actual negative-cap erasure minimum-0175 SHA7fdabeeb8e9da0f3dde099dfe8da71f49287ef9d85d5ba6e17d4742f24a32bdd supplies another route: compare the cost of its specific positive-ell clipping auxiliary against the strict gain from erasing the very same negative cap. The present theorem complements, but does not settle, that comparison.
