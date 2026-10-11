# material-a945804df15a

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""TWO_APEX_BASE_ESCAPE_801_V1, exact finite algebra and negative controls.
CPython 3.11+, standard library; assertions enabled; no input data or randomness.
In one directory: python -S two_apex_base_escape.py build
Then:             python -S two_apex_base_escape.py check
The continuous proof, including the base-maximum argument, is in the capsule.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib, json, sys
assert __debug__
def add(*ps):
    out={}
    for p in ps:
        for e,v in p.items():out[e]=out.get(e,F(0))+v
    return {e:v for e,v in out.items() if v}
def scale(p,c):return {e:v*c for e,v in p.items() if v*c}
def mul(p,q):
    out={}
    for a,u in p.items():
        for b,v in q.items():
            e=tuple(x+y for x,y in zip(a,b));out[e]=out.get(e,F(0))+u*v
    return {e:v for e,v in out.items() if v}
def sq(p):return mul(p,p)
def power(p,n):
    out={(0,)*len(next(iter(p))):F(1)}
    for _ in range(n):out=mul(out,p)
    return out
one={(0,):F(1)};p={(1,):F(1)}
Zminus=sq(add(scale(one,2),scale(p,-1)))
Zplus=sq(add(scale(p,2),scale(one,5)))
def gap(Z):return add(scale(sq(add(Z,scale(p,-1))),2),scale(add(Z,scale(sq(p),-1)),-25))
# 2 numerator^2 -25 denominator, at k=2-p and k=2p+5.
facminus=scale(mul(mul(add(p,scale(one,-1)),add(p,one)),add(sq(p),scale(p,-10),scale(one,34))),2)
facplus=mul(add(p,one),add(scale(power(p,3),32),scale(sq(p),272),scale(p,775),scale(one,625)))
assert gap(Zminus)==facminus and gap(Zplus)==facplus
# In the upper branch p=t-1, the gap has nonnegative coefficients.
shift=add(p,scale(one,-1))
shifted={}
for (n,),c in gap(Zplus).items():shifted=add(shifted,scale(power(shift,n),c))
assert shifted=={(1,):F(90),(2,):F(327),(3,):F(176),(4,):F(32)}
# Monotonicity in Z=k^2: (Z-p)(Z+p-2p^2)/(Z-p^2)^2 > 0.
# The second factor at Z=(2-p)^2 equals (1-p)(p+4).
assert add(Zminus,p,scale(sq(p),-2))==mul(add(one,scale(p,-1)),add(p,scale(one,4)))
assert 64*F(25,2)+1==801 and 801>729
# A discarded weaker relaxation DOES NOT imply u>=12.
p0=F(-6,5);k0=F(13,5)
u0=(k0*k0-p0)**2/(k0*k0-p0*p0)
assert k0==2*p0+5 and u0==F(39601,3325)<12 and k0+p0<2
# Crossed primal/polar weak arrows are not generically forbidden in rank 3.
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
b=(F(1),F(0),F(0));B=(F(1),F(1),F(0))
x=(F(3,2),F(-1),F(3));q=(F(0),F(5,2),F(7,6))
assert dot(b,B)==dot(x,q)==1 and dot(x,B)==F(1,2) and dot(b,q)==0
assert dot(b,sub(x,b))==dot(B,sub(q,B))==F(1,2)
report={'identity':'TWO_APEX_BASE_ESCAPE_801_V1',
 'strict_u_lower':'25/2','strict_a_lower':800,'strict_GJ_lower':801,'global_GJ_upper':729,
 'lower_branch_factorization':'2(p-1)(p+1)(p^2-10p+34)',
 'upper_branch_factorization':'(p+1)(32p^3+272p^2+775p+625)',
 'upper_shift_p_equals_t_minus_1':{'t':'90','t^2':'327','t^3':'176','t^4':'32'},
 'discarded_u12_relaxation':{'p':str(p0),'k':str(k0),'u':str(u0),'k_plus_p':str(k0+p0),'status':'not a physical body; violates k+p>=2'},
 'crossed_arrow_rank3_control':{'b':[str(t) for t in b],'B':[str(t) for t in B],'x':[str(t) for t in x],'q':[str(t) for t in q],'status':'four-vector algebraic control only, not an actual mono-monostatic body'},
 'scope':{'requires_second_apex_weak_exit_into_B':True,'requires_a_designated_base_to_root_exit':False,'requires_H0':False,'requires_closing_edge_endpoint_in_B':False,'arbitrary_V_and_F':True,'whole_two_apex_motif_closed':False}}
data=(json.dumps(report,sort_keys=True,indent=2)+'\n').encode();path=Path('two_apex_base_escape.json')
mode=sys.argv[1] if len(sys.argv)>1 else 'build';assert mode in ('build','check')
if mode=='build':path.write_bytes(data)
else:assert path.read_bytes()==data
print('TWO_APEX_BASE_ESCAPE_801_EXACT_TWO_CLOSED_BRANCHES_PASS')
print('BASE_MAXIMUM_FORCES_ROOT_EXIT_IS_ANALYTIC_NOT_ENUMERATED')
print('DISCARDED_RELAXATION_AND_RANK3_CROSSED_ARROW_CONTROLS_PASS')
print(path.name,len(data),hashlib.sha256(data).hexdigest())
print('TWO_APEX_BASE_ESCAPE_801_DURABLE_RECOVERY_PASS')
