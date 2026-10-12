# material-7c1af605fe40

AI research material

---

"""MORSE6_RATIONAL_A7_100: exact smooth filled-centroid body, NOT a polyhedron.
Standalone Python >=3.10 standard library. Run: python -B -S verify_morse6.py
Exact parameters, polynomial proof, rational boundary oracle and replay output.
"""
from fractions import Fraction as F
from math import comb
import json, hashlib
from pathlib import Path

SCALE=10**6
A0=F(7,100)
LAM=F(1029667,SCALE)
# P/A0 coefficients at powers 1,3,4,5,6; power2 is exact volume-moment closure.
P_FREE=[-7736016, -11309209, 49285282, -72918101, 33874704]
Q_SHAPE=[3992830, -9033836, 7320751, -36032083, 88425030, -81073624, 27231889]
B_FREE=[-42040, 19011, -150151]
MU=F(3,10)
EPS=F(1,2000)

def trim(p):
    p=list(map(F,p))
    while len(p)>1 and p[-1]==0:p.pop()
    return p

def add(*ps):
    z=[F(0)]*max(map(len,ps))
    for p in ps:
        for i,v in enumerate(p):z[i]+=v
    return trim(z)

def scale(p,a):return trim([a*x for x in p])
def mul(p,q):
    z=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):z[i+j]+=a*b
    return trim(z)

def power(p,k):
    out=[F(1)]
    for _ in range(k):out=mul(out,p)
    return out

def deriv(p):return trim([i*p[i] for i in range(1,len(p))] or [0])
def shift(p,k=1):return [F(0)]*k+list(p)
def value(p,y):
    z=F(0)
    for a in p[::-1]:z=z*y+a
    return z

def moment(p):return sum((a/F(2*i+1) for i,a in enumerate(p)),F(0))

def build():
    p=[A0]+[F(0)]*6
    for k,z in zip([1,3,4,5,6],P_FREE):p[k]=A0*F(z,SCALE)
    q=[A0*F(z,SCALE) for z in Q_SHAPE]
    b=[F(1)]+[F(z,SCALE) for z in B_FREE]
    h=mul([1,-1],mul(b,b))
    p[2]=-moment(mul(h,p))/moment(shift(h,2))
    assert moment(mul(h,p))==0
    return p,q,b,h

def bernstein(p):
    n=len(p)-1
    return [sum((p[j]*F(comb(k,j),comb(n,j)) for j in range(k+1)),F(0)) for k in range(n+1)]

def split(bs):
    rows=[bs]
    while len(rows[-1])>1:
        r=rows[-1];rows.append([(a+b)/2 for a,b in zip(r,r[1:])])
    return [r[0] for r in rows],[r[-1] for r in rows[::-1]]

def positive(p,max_depth=32):
    # Exact subdivision cover of [0,1]. A positive minimum Bernstein coefficient
    # is a rigorous lower bound on each closed leaf, including both endpoints.
    stack=[(bernstein(p),F(0),F(1),0)];leaves=[]
    while stack:
        bs,l,r,depth=stack.pop()
        if min(bs)>0:
            leaves.append([str(l),str(r),str(min(bs))]);continue
        if max(bs)<=0 or depth>=max_depth:
            raise ArithmeticError(('NOT_CERTIFIED',l,r,depth,min(bs),max(bs)))
        left,right=split(bs);m=(l+r)/2
        stack.append((right,m,r,depth+1));stack.append((left,l,m,depth+1))
    return leaves

def boundary(t,s):
    """Rational boundary point for t>=0 and rational s (circle stereography).
    t=0 is the +x tip; the -x tip is the t->infinity limit.
    s->infinity completes each circular section.
    """
    t,s=F(t),F(s)
    if t<0:raise ValueError('t must be nonnegative')
    p,q,b,h=build();x=(1-t*t)/(1+t*t);y=x*x
    rho=2*t/(1+t*t)*value(b,y)
    co=(1-s*s)/(1+s*s);si=2*s/(1+s*s)
    return [LAM*x,value(p,y)+rho*co,x*value(q,y)+rho*si]

def main():
    p,q,b,h=build();hp=deriv(h);hpp=deriv(hp)
    d=add(mul(p,p),shift(mul(q,q)))
    r=mul(h,d);rp=deriv(r);j=add([0,LAM*LAM],h,d);jp=deriv(j)
    aa=add(mul(h,hp),scale(shift(mul(h,hpp)),2),scale(shift(mul(hp,hp)),-1))
    n=add(scale(deriv(p),2),scale(shift(deriv(deriv(p))),4))
    ll=add(scale(deriv(q),6),scale(shift(deriv(deriv(q))),4))
    k=add(scale(rp,-1),scale(d,-MU))
    c=add(scale(aa,-1),[-EPS])
    polys={'B':b,'D':d,'K':k,
           'K2_minus_HD_Jprime2':add(mul(k,k),scale(mul(mul(h,d),mul(jp,jp)),-1)),
           'minusA_minusEPS':c,
           'curvature_square_gap':add(mul(c,c),scale(mul(power(h,3),add(mul(n,n),shift(mul(ll,ll)))),-1))}
    cert={}
    for name,poly in polys.items():
        cert[name]={'degree':len(poly)-1,'leaves':positive(poly)}
        print(name,'degree',len(poly)-1,'positive leaves',len(cert[name]['leaves']),flush=True)
    assert value(d,F(1))>0 and LAM>0
    volume_over_pi=2*LAM*moment(h)
    fp=value(jp,0)+value(rp,0)/A0
    fm=value(jp,0)-value(rp,0)/A0
    assert fp<-MU*A0 and fm>MU*A0
    data={'object':'MORSE6_RATIONAL_A7_100','status':'exact smooth body; NOT a finite polyhedron',
          'lambda':str(LAM),'P':list(map(str,p)),'Q':list(map(str,q)),'B':list(map(str,b)),
          'volume_over_pi':str(volume_over_pi),'centroid':['0','0','0'],
          'radial_min':['0',str(A0-1),'0'],'radial_max':['0',str(A0+1),'0'],
          'r_over_R':str((1-A0)/(1+A0)),'mu':str(MU),'curvature_gap':str(EPS),
          'fplus_prime_at_0':str(fp),'fminus_prime_at_0':str(fm),
          'boundary_t1_s2':list(map(str,boundary(F(1),F(2)))),
          'certificate':cert}
    raw=(json.dumps(data,sort_keys=True,separators=(',',':'))+'\n').encode()
    path=Path('MORSE6_RATIONAL_A7_100.json');path.write_bytes(raw)
    print('MORSE6_EXACT_MASS_CONVEXITY_TWO_CRITICAL_POINTS_PASS')
    print('MORSE6_NORMALIZED_RADIAL_GAP_GT_3_10_PASS')
    print(path.name,len(raw),hashlib.sha256(raw).hexdigest())
    print('fplus_prime0',float(fp),'fminus_prime0',float(fm),'V/pi',float(volume_over_pi))
    print('INPUT_SOURCE',len(Path(__file__).read_bytes()),hashlib.sha256(Path(__file__).read_bytes()).hexdigest())

if __name__=='__main__':main()
