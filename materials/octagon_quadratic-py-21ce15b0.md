# material-21ce15b04af5

AI research material

---

"""OCTAGON_NEUTRAL_SHARP_GERMS_V2.
Companion to the exact pinned neutral_germ.py; same SymPy1.14.0 dependency.
python octagon_quadratic.py build ; python octagon_quadratic.py check
"""
from pathlib import Path
import hashlib,json,sys
import sympy as S
import neutral_germ as G


def build():
    v,f,q,m=G.fixtures();v=G.center(v,f,q)
    a,b=v[8],v[9];h_a,h_b=1-q.dot(a),1-q.dot(b)
    C=S.S.Zero;B=S.S.Zero;CB=S.zeros(3,1);HB=S.zeros(3,1)
    for ids in f:
        if 8 in ids:continue
        for i in range(1,len(ids)-1):
            tri=[v[k] for k in (ids[0],ids[i],ids[i+1])]
            vol=(tri[0]-a).dot((tri[1]-a).cross(tri[2]-a))/6
            assert vol>0
            if 9 not in ids:
                assert set(ids)==set(range(8))
                C+=vol;CB+=vol*sum(tri,S.zeros(3,1))
            else:
                assert len(ids)==3
                B+=vol;HB+=vol*sum([v[k] for k in ids if k!=9],S.zeros(3,1))
    assert C>0 and B>0
    assert (C+B)*a+B*b+CB+HB==S.zeros(3,1)
    u=G.SIGMA;w=G.TAU;da=1+u*h_a;db=1+u*h_b
    W=C*db+B;Q=h_a*db*W+B*h_b*da;H=db*CB+HB
    va=((B*h_b*a-h_a*B*b-h_a*db*H)/Q).applyfunc(S.cancel)
    vb=(((h_a*b-h_b*a)*W-h_b*da*H)/Q).applyfunc(S.cancel)
    xx=v[:8]+[va,vb]
    reference=G.center([z/(1+u*(1-q.dot(z))) for z in v],f,q)
    assert all((z-y).applyfunc(S.cancel)==S.zeros(3,1) for z,y in zip(xx,reference))
    assert G.moments(xx,f)[1]==S.zeros(3,1)
    pp=[]
    for ids in f:
        base=[i for i in ids if i<8]
        if len(base)==8:pp.append(q);continue
        assert len(base)==2
        outside=next(i for i in ids if i>=8)
        n=v[base[0]].cross(v[base[1]])
        pp.append((q+(1-q.dot(xx[outside]))*n/n.dot(xx[outside])).applyfunc(S.cancel))
    for i,ids in enumerate(f):
        assert all(S.cancel(pp[i].dot(xx[j])-1)==0 for j in ids)
    def deg(expr):
        n,d=S.fraction(S.cancel(expr))
        return max(0,int(S.degree(n,u))) if n else 0,max(0,int(S.degree(d,u)))
    vertex_degrees=[[deg(c) for c in z] for z in xx]
    pole_degrees=[[deg(c) for c in z] for z in pp]
    assert all(max(deg(c))<=2 for z in xx+pp for c in z)
    mt=m+w*q*q.T;nt=mt.inv();ee=G.census(v,f,m)['rows'];degrees={}
    for key in ee:
        typ,i,j=key.split(':');i,j=int(i),int(j)
        if typ=='P':expr=(xx[i].T*mt*(xx[j]-xx[i]))[0]
        else:expr=(pp[i].T*nt*(pp[j]-pp[i]))[0]
        num,den=S.fraction(S.cancel(expr))
        assert den.subs({u:0,w:0})!=0
        ds=max(0,int(S.degree(num,u))) if num else 0
        dt=max(0,int(S.degree(num,w))) if num else 0
        assert ds<=(4 if typ=='P' else 6) and dt<=1
        degrees[key]=(ds,dt)
    assert len(degrees)==68
    sharp_tests={}
    for d in (1,2,4,6,15):
        decision=G.decide([(-u**d,S.S.One),(u**d,u**d-1)])
        assert decision['feasible'] and decision['orders']==[2*d,2*d]
        sharp_tests[d]=decision
    return dict(name='OCTAGON_NEUTRAL_SHARP_GERMS_V2',C=C,B=B,CB=CB,HB=HB,
                common_denominator=Q,vertices=xx,poles=pp,vertex_degrees=vertex_degrees,
                pole_degrees=pole_degrees,row_degrees=degrees,
                algebraic_sharp_order_tests=sharp_tests,
                mixed_degree=6,mixed_comparison_degree=12,mixed_carrier_order=13,
                VE_only_degree=4,VE_only_comparison_degree=8,VE_only_carrier_order=9,
                scope='Conditional calibrated-family escape; literal non-S1U1 strict244 control.')


def main():
    assert __debug__ and S.__version__=='1.14.0'
    assert len(sys.argv)==2 and sys.argv[1] in ('build','check')
    assert hashlib.sha256(Path(G.__file__).read_bytes()).hexdigest()=='13029a0a2ece104b85e4bbc3739b652a05029d8b844f8eb556a5de87a62666e0'
    data=(json.dumps(G.clean(build()),sort_keys=True,indent=2)+'\n').encode()
    p=Path('octagon_quadratic_report.json')
    if sys.argv[1]=='build':p.write_bytes(data)
    else:assert p.read_bytes()==data
    print('OCTAGON_NEUTRAL_SHARP_ALL_68_ROWS_PASS')
    for p in (Path(__file__),p):
        z=p.read_bytes();print(p.name,len(z),hashlib.sha256(z).hexdigest())
if __name__=='__main__':main()
