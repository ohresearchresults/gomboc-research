# material-56d0c78a0c5a

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""ADJACENT_TRIANGLE_BIPYRAMID_81_40_V1. Exact polynomial certificate.
Python standard library only; assertions required; no arguments or solver.
Checks the rational-family Lambda sum upper bound, not a universal facet-pair bound.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib,json
assert __debug__
def add(*pp):
    out={}
    for p in pp:
        for k,c in p.items():out[k]=out.get(k,F(0))+c
    return {k:c for k,c in out.items() if c}
def scale(p,s):return {k:c*s for k,c in p.items() if c*s}
def mul(p,q):
    out={}
    for (h,u),c in p.items():
        for (i,j),d in q.items():out[h+i,u+j]=out.get((h+i,u+j),F(0))+c*d
    return {k:c for k,c in out.items() if c}
def ev(p,h,u):return sum(c*h**i*u**j for (i,j),c in p.items())
O={(0,0):F(1)};h={(1,0):F(1)};u={(0,1):F(1)}
A=mul(add(scale(O,2),mul(h,u)),add(O,scale(h,2),scale(mul(add(O,h),u),-1)))
B=mul(add(O,h),add(O,h,scale(u,-1)))
Q=add(scale(B,81),scale(A,-40))
a=add(scale(mul(u,u),40),scale(u,-80),scale(O,81))
b=add(scale(mul(u,u),40),scale(u,-41),scale(O,2))
c=add(O,scale(u,-1))
assert Q==add(mul(a,mul(h,h)),mul(b,h),c)
assert a==add(scale(mul(add(u,scale(O,-1)),add(u,scale(O,-1))),40),scale(O,41))
H=add(scale(mul(a,c),4),scale(mul(b,b),-1))
assert H=={(0,4):F(-1600),(0,3):F(3120),(0,2):F(-1361),(0,1):F(-480),(0,0):F(320)}
def bernstein(left,right):
    power=[F(0)]*5
    for (_,j),z in H.items():
        for k in range(j+1):power[k]+=z*comb(j,k)*left**(j-k)*(right-left)**k
    beta=[sum(power[k]*F(comb(i,k),comb(4,k)) for k in range(i+1)) for i in range(5)]
    # Rebuild ordinary coefficients from Bernstein basis as a separate equality.
    rebuilt=[F(0)]*5
    for i,z in enumerate(beta):
        for j in range(4-i+1):rebuilt[i+j]+=z*comb(4,i)*comb(4-i,j)*(-1)**j
    assert rebuilt==power and all(z>0 for z in beta)
    return beta
intervals=[(F(0),F(1,2)),(F(1,2),F(3,4)),(F(3,4),F(49,50))]
expected=[['320','260','3439/24','539/8','119/4'],
          ['119/4','175/16','163/96','55/32','71/16'],
          ['71/16','5551/800','703411/60000','684083/50000','201599/62500']]
rows=[]
for (l,r),pin in zip(intervals,expected):
    beta=bernstein(l,r);assert list(map(str,beta))==pin
    rows.append({'interval':[str(l),str(r)],'bernstein_coefficients':list(map(str,beta))})
assert intervals[0][0]==0 and intervals[-1][1]==F(49,50)
assert all(intervals[i][1]==intervals[i+1][0] for i in range(2))
assert ev(b,F(0),F(49,50))==F(59,250)>0
assert 80*F(49,50)-41>0
hh,uu=F(1,12),F(2,3)
control=ev(A,hh,uu)/ev(B,hh,uu)
assert control==F(1184,585)>2
assert F(81,40)<F(51,25) and F(51,25)-F(81,40)==F(3,200)
report={'identity':'ADJACENT_TRIANGLE_BIPYRAMID_81_40_V1',
    'domain':'h>0, 0<u<1; exact two-parameter own-volume-centred triangular bipyramid',
    'H_coefficients_low_to_high':[320,-480,-1361,3120,-1600],
    'positive_discriminant_complement_cover':rows,
    'last_interval':['49/50','1'],'b_at_49_50':'59/250',
    'control_parameters':['1/12','2/3'],'control_value':str(control),
    'strict_family_bound':'81/40','TREE253_necessary_threshold':'51/25','gap':'3/200',
    'universal_adjacent_triangle_bound_proved':False}
bb=(json.dumps(report,sort_keys=True,separators=(',',':'))+'\n').encode()
Path('bipyramid_bound_report.json').write_bytes(bb)
print('BIPYRAMID_81_40_POLYNOMIAL_IDENTITY_PASS')
print('BIPYRAMID_81_40_THREE_BERNSTEIN_INTERVALS_PASS')
print('BIPYRAMID_1184_585_NEGATIVE_CONTROL_RETAINED')
print('REPORT',len(bb),hashlib.sha256(bb).hexdigest())
print('ADJACENT_TRIANGLE_BIPYRAMID_81_40_EXACT_PASS')
