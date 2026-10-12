# material-18a96fa5b221

AI research material

---

#!/usr/bin/env python3
"""ROOT_CONE_SLICE_DEFICIT_V2. Exact FORMAL nonbody separator.
CPython 3.13.5, standard library, no inputs/RNG; assertions enabled.
This is a new source unit reconstructed from literal rational parameters.
It is NOT a replay of the unavailable prior ephemeral source.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import hashlib

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

def mix(laws,x):
    return tuple(sum((w*pdf_jet(h,x)[i] for h,w in laws),F(0)) for i in range(3))

def integ(jet,mid,lo,hi,power=0):
    assert power in (0,1)
    if power:jet=(mid*jet[0],jet[0]+mid*jet[1],jet[1]+mid*jet[2],jet[2])
    return sum(v*((hi-mid)**(i+1)-(lo-mid)**(i+1))/(i+1) for i,v in enumerate(jet))

def evalq(jet,x):return jet[0]+jet[1]*x+jet[2]*x*x

def minq(jet,lo,hi):
    vals=[evalq(jet,lo),evalq(jet,hi)]
    if jet[2]>0:
        x=-jet[1]/(2*jet[2])
        if lo<x<hi:vals.append(evalq(jet,x))
    return min(vals)

def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x

def build():
    b,c,d,t,rho,omega,gamma,u,v=map(lambda n:F(n,10**6),
        (698790,429624,269604,4553454,315569,146601,314802,2433965,3116075))
    lam=1-rho-omega-gamma
    alpha,epsilon,delta=1-b,1-c,1-d
    eta=alpha*epsilon*delta;M=max(b,c,d);kappa=t*lam
    m=(1+b+c+d)*lam+c*rho+(c+d)*omega+(b+c+d)*gamma
    w=(4-delta*u-epsilon*v-m)/alpha
    W=delta*u+epsilon*v
    T=((1+b+c)*u+(1+b+d)*v)/(t*m)
    assert T>F(51,25)
    assert 0<d<c<b<1 and lam>0 and kappa>1 and b+c>F(9,8)
    laws=[((1,c,d,b),lam),((c,0,0,0),rho),((c,d,0,0),omega),((c,d,b,0),gamma)]
    knots=[F(0),d,c,b,F(1)]
    mass=mean=loss0=loss1=F(0);previous=None;pieces=[]
    for lo,hi in zip(knots,knots[1:]):
        mid=(lo+hi)/2;j=mix(laws,mid)
        assert j[0]>0 and minq(j,lo-mid,hi-mid)>=0
        disc=j[1]**2-4*j[0]*j[2]
        assert disc>=0
        left=(evalq(j,lo-mid),j[1]+2*j[2]*(lo-mid))
        right=(evalq(j,hi-mid),j[1]+2*j[2]*(hi-mid))
        if previous is not None:assert previous==left
        previous=right
        cone=(kappa*(1-mid)**2,-2*kappa*(1-mid),kappa)
        deficit=tuple(cone[i]-eta*t*j[i]/3 for i in range(3))
        assert minq(deficit,lo-mid,hi-mid)>=0
        if lo>=M:assert deficit==(0,0,0)
        mass+=integ(j,mid,lo,hi)
        mean+=integ(j,mid,lo,hi,1)
        loss0+=integ(deficit,mid,lo,hi)
        loss1+=integ(deficit,mid,lo,hi,1)
        pieces.append(dict(lo=lo,hi=hi,mid=mid,pdf_jet=j,discriminant=disc,
                           deficit_jet=deficit,deficit_min=minq(deficit,lo-mid,hi-mid)))
    assert mass==1 and mean==m/4 and previous==(0,0)
    D0=kappa-eta*t;D1=kappa-eta*t*m
    L=kappa*(kappa+1)-eta*t*W
    Lx=kappa*kappa-eta*t*delta*u;Ly=kappa*kappa-eta*t*epsilon*v
    assert loss0==D0/3 and loss1==D1/12
    assert min(D0,D1,L,Lx,Ly)>0
    gaps={'Jensen':27*M*L*L-64*D0**3,
          'first_height_moment':L*L*D1-4*D0**4,
          'reflected_height_moment':L*L*(4*M*D0-D1)-4*D0**4,
          'strip_X':4*kappa*Lx-(8*D0**2-8*D0*D1+3*D1**2),
          'strip_Y':4*kappa*Ly-(8*D0**2-8*D0*D1+3*D1**2),
          'radial':lam*(4-m)**3-27*eta}
    assert gaps['Jensen']<0 and gaps['first_height_moment']<0
    assert t+1-u-v>0 and 2-t<w<t+2-u-v
    assert t*(m-c)>1+b+d and t*(m-d)>1+b+c
    # Finite-support weighted-Cauchy strip bound, stronger than M=1.
    aa=M-M*M/2;bb=M*M/2-M**3/3;cc=M**3/3-M**4/4
    det=aa*cc-bb*bb
    assert det==M**4*(M*M-6*M+6)/72>0
    strip_rhs=16*cc*D0**2-8*bb*D0*D1+aa*D1**2
    gaps['finite_strip_X']=48*det*kappa*Lx-strip_rhs
    gaps['finite_strip_Y']=48*det*kappa*Ly-strip_rhs
    # A rational member of the full affine positive-part Holder family.
    h=M
    gaps['affine_test_h_M']=27*L*L*h**4-4*max(4*h*D0-D1,F(0))**3
    # Exactly diagnose the previously unverified proposed seven-law lift.
    last=(lam-1/t)/(1-b);j=gamma-b*last
    oldmass=[1/t,rho,F(0),omega,F(0),j,last]
    oldknots=[(1,c,d,b),(c,0,0,0),(c,b,0,0),(c,d,0,0),
              (c,1,0,0),(c,1,d,0),(c,1,b,0)]
    oldlift=list(zip(oldknots,oldmass))
    lift_identity=all(mix(laws,(lo+hi)/2)==mix(oldlift,(lo+hi)/2)
                      for lo,hi in zip(knots,knots[1:]))
    # Correct C-fan law ordering: T0,CFFF,CBFF,CDFF,CAFF,CBDF,CADF.
    fanmass=[1/t,rho,F(0),omega,F(0),j,last]
    fanknots=[(1,b,c,d),(c,0,0,0),(c,b,0,0),(c,d,0,0),
              (c,1,0,0),(c,b,d,0),(c,1,d,0)]
    fanlaws=list(zip(fanknots,fanmass))
    corrected=all(mix(laws,(lo+hi)/2)==mix(fanlaws,(lo+hi)/2)
                  for lo,hi in zip(knots,knots[1:]))
    assert not lift_identity and corrected and sum(fanmass)==1 and min(fanmass)>=0
    # Strict improvement of the affine family over the three simple bounds.
    # This is only scalar data (D0,D1,M,L), not a density or a body.
    sd0,sd1,sm,sl,sh=F(3),F(4),F(1),F(901,100),F(3,2)
    simple=[27*sm*sl*sl-64*sd0**3,sl*sl*sd1-4*sd0**4,
            sl*sl*(4*sm*sd0-sd1)-4*sd0**4]
    sharper=27*sl*sl*(sh**4-(sh-sm)**4)-4*(4*sh*sd0-sd1)**3
    assert min(simple)>0 and sharper<0
    scalar_separator=dict(D0=sd0,D1=sd1,M=sm,L=sl,h=sh,
                          old_slacks=simple,affine_slack=sharper,
                          status='SCALAR_MOMENT_TEST_ONLY_NOT_A_DENSITY_OR_BODY')
    return dict(identity='ROOT_CONE_SLICE_DEFICIT_V2',
       status='FORMAL_RELAXATION_CONTROL_NOT_A_POLYTOPE_OR_FULL_MAXIMUM_OR_110',
       parameters=dict(b=b,c=c,d=d,t=t,rho=rho,omega=omega,gamma=gamma,
                       lam=lam,u=u,v=v,w=w,m=m,eta=eta,M=M,kappa=kappa,T=T),
       cone=dict(D0=D0,D1=D1,L=L,Lx=Lx,Ly=Ly),gaps=gaps,pieces=pieces,
       scalar_separator=scalar_separator,
       lift_diagnostic=dict(old_identity=lift_identity,corrected_identity=corrected,
                            masses=fanmass,min_mass=min(fanmass),
                            corrected_knots=fanknots)),laws,fanlaws

def main():
    out,laws,fanlaws=build()
    raw=(json.dumps(encode(out),sort_keys=True,indent=2)+'\n').encode()
    Path('deficit_control.json').write_bytes(raw)
    print('FOUR_LAW_FULL_INTERVAL_SQRT_DENSITY_CONCAVITY_PASS')
    print('POINTWISE_CONE_DOMINANCE_AND_EXACT_DEFICIT_MOMENTS_PASS')
    print('OLD_CONE_LOCATION_BOUNDS_AND_B_PLUS_C_SCREEN_PASS')
    print('NEW_JENSEN_AND_HEIGHT_MOMENT_BOUNDS_EXCLUDE_FORMAL_CONTROL')
    print('EXACT_CORRECTED_SEVEN_C_FAN_LAW_IDENTITY_PASS')
    print('AFFINE_HOLDER_FAMILY_STRICTLY_STRENGTHENS_SIMPLE_BOUNDS_PASS')
    print('lift_diagnostic='+str(out['lift_diagnostic']['old_identity'])+','+str(out['lift_diagnostic']['corrected_identity']))
    print('T='+str(out['parameters']['T']))
    print('report_bytes='+str(len(raw)))
    print('report_sha256='+hashlib.sha256(raw).hexdigest())
    print('ROOT_CONE_SLICE_DEFICIT_V2_RECOVERY_PASS')

if __name__=='__main__':main()
