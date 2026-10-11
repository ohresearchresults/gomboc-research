from fractions import Fraction as F
from itertools import product

Z=[(F(1),F(1),F(1)),(F(1),F(-1),F(-1)),
   (F(-1),F(1),F(-1)),(F(-1),F(-1),F(1))]
I=[[F(i==j) for j in range(3)] for i in range(3)]

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

def outer(x,y):
    return [[a*b for b in y] for a in x]

def add(A,B):
    return [[A[i][j]+B[i][j] for j in range(3)] for i in range(3)]

def scale(c,A):
    return [[c*x for x in row] for row in A]

def subtract(A,B):
    return add(A,scale(-1,B))

def minors(A):
    a,b,c=A[0]
    d,e=A[1][1:]
    f=A[2][2]
    return (a,a*d-b*b,a*d*f+2*b*c*e-a*e*e-d*c*c-f*b*b)

P=[outer(z,z) for z in Z]
E=[[[F(i==j==k) for j in range(3)] for i in range(3)]
   for k in range(3)]

def row(A,B):
    return subtract(scale(32,subtract(A,B)),scale(7,I))

Wsec=[tuple((Z[0][k]+3*Z[j][k])/4 for k in range(3))
      for j in (1,2,3)]
C=[[row(P[2],E[k]) for k in (1,2)],
   [row(P[1],E[k]) for k in (0,2)],
   [row(P[1],E[k]) for k in (0,1)],
   [row(P[1],outer(w,w)) for w in Wsec]]
O=[scale(32,subtract(P[j+1],P[j])) for j in range(3)]

# Complete exact parent multiplier data, compressed only by repeated rows.
V=[(15,0,0,45,0,22,18),
   (0,13,0,38,0,34,15),
   (14,0,0,42,0,23,21),
   (0,5,8,39,0,34,14),
   (0,132,0,395,0,341,132),
   (151,0,0,452,0,226,171),
   (152,0,0,455,0,241,152),
   (0,123,0,368,0,326,184),
   (0,5,7,37,0,32,19),
   (0,0,123,368,0,326,184)]
INDEX=(0,1,2,0,1,2,0,3,2,0,4,2,
       5,6,7,5,6,8,5,6,9,5,6,9)
choices=list(product(range(2),range(2),range(2),range(3)))
assert len(choices)==len(INDEX)==24
for choice,k in zip(choices,INDEX):
    rows=[C[j][choice[j]] for j in range(4)]+O
    Q=[[F(0) for j in range(3)] for i in range(3)]
    for weight,A in zip(V[k],rows):
        assert weight>=0
        Q=add(Q,scale(weight,A))
    assert min(minors(Q))>0

# Exact Euclidean constants used for moved witnesses and section distances.
assert 24<25                       # 4+sqrt(24)<9
assert F(26)<F(51,10)**2            # sqrt(26)<51/10
for S in ([tuple(F(i==k) for i in range(3)) for k in (1,2)],
          [tuple(F(i==k) for i in range(3)) for k in (0,2)],
          [tuple(F(i==k) for i in range(3)) for k in (0,1)]):
    for y in S:
        for sign in (-1,1):
            yy=tuple(sign*x for x in y)
            for z in Z:
                assert dot(tuple(z[i]-yy[i] for i in range(3)),
                           tuple(z[i]-yy[i] for i in range(3)))<=F(13,2)
for y in Wsec:
    for z in Z:
        e=tuple(z[i]-y[i] for i in range(3))
        assert dot(e,e)<=F(13,2)
print('FOUR_SECTION_24_EXACT_PD_ALTERNATIVES_PASS')

def gate_parameters(Q,t):
    alpha=(1+Q)/(1+t)
    epsilon=Q*(1+Q)
    b=epsilon/(1+epsilon)
    d=(alpha+epsilon)/(1+epsilon)
    return alpha,b,d

REGIMES=[
    ('RIGHT_1024_TAIL_77',F(1,1024),F(77),
     F(1,1000),F(1,72),F(1,55),F(9,8800),F(1,32768)),
    ('RIGHT_512_TAIL_100',F(1,512),F(100),
     F(1,500),F(1,84),F(1,50),F(269,28000),F(1,4096))]

for name,Q,t,bmax,dmax,gmax,expected_gap,gamma in REGIMES:
    alpha,b,d=gate_parameters(Q,t)
    assert alpha<1 and 0<b< bmax<dmax<F(1,4)
    assert b<d<dmax
    volume=(1-bmax)**2*(1-dmax)
    product_bound=(dmax+2*bmax)*(dmax+6*bmax)
    assert product_bound < (volume*gmax)**2
    assert volume>F(4,5)
    gap=F(7,32)-9*dmax-F(51,10)*gmax
    assert gap==expected_gap and gap>18*gamma
    A=F(7,32)-9*d
    assert A>0
    assert 100*A*A*(1-b)**4*(1-d)**2 > 2601*(d+2*b)*(d+6*b)
    print(name,'b_bound',b,'d_bound',d,'gap',gap,'gamma',gamma)

assert 70858071**2-3025*25597*64000000==65287025841041
assert 20667083**2-41917*10000000000==7958319728889
assert F(9,8800)-18*F(1,32768)==F(2133,4505600)
assert F(1)-F(77,1024)==F(947,1024)
assert F(1)-F(100,512)==F(103,128)
assert F(256-77,256)==F(179,256)
print('ADAPTIVE_OUTER_TETRAHEDRON_77_100_RATIONAL_GUARDS_PASS')
