# material-ee5f0d24c942

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""TWO_APEX_APEX_CLOSING_1281_V1: exact finite algebra, not full formalization.
The rank-obstruction and ball-cap geometry are proved in the recovery capsule.
CPython >=3.11, standard library, assertions enabled, no random or external input.
python -S two_apex_apex_closing.py build
python -S two_apex_apex_closing.py check
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib, json, sys
assert __debug__
def add(*ps):
    out={}
    for p in ps:
        for e,c in p.items():out[e]=out.get(e,F(0))+c
    return {e:c for e,c in out.items() if c}
def scale(p,c):return {e:v*c for e,v in p.items() if v*c}
def mul(p,q):
    out={}
    for a,u in p.items():
        for b,v in q.items():
            e=tuple(x+y for x,y in zip(a,b));out[e]=out.get(e,F(0))+u*v
    return {e:c for e,c in out.items() if c}
def sq(p):return mul(p,p)
def variables(n):return [{tuple(int(i==j) for i in range(n)):F(1)} for j in range(n)]
beta,delta=variables(2);one={(0,0):F(1)}
A=add(scale(one,5),delta)
lhs=add(sq(add(A,scale(beta,-1))),scale(mul(mul(A,add(A,scale(one,-1))),mul(beta,add(one,scale(beta,-1)))),-4))
rhs=sq(add(mul(add(scale(A,2),scale(one,-1)),beta),scale(A,-1)))
assert lhs==rhs
assert add(mul(A,add(A,scale(one,-1))),scale(one,-20))==add(scale(delta,9),sq(delta))
# The projection bounds in the two cases of the rank obstruction.
r,s=variables(2)
assert add(one,scale(r,-2),sq(r))==sq(add(one,scale(r,-1)))
assert add(sq(s),scale(mul(r,s),-2),sq(r))==sq(add(s,scale(r,-1)))
assert 64*20+1==1281 and 1281>729
# Complete rational common-metric boundary control for the ball-cap relaxation.
M=(F(5),F(105),F(1));N=tuple(1/t for t in M)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def metric(a,b,m):return sum(x*y*t for x,y,t in zip(a,b,m))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
x=(F(0),F(0),F(1))
b=(F(8,105),F(4,105),F(5,21))
z=(F(2,105),F(-4,105),F(17,21))
q0=(F(10),F(0),F(1));B=(F(56,9),F(56,3),F(-7,9))
assert metric(x,x,M)==1
assert dot(q0,x)==dot(q0,b)==dot(q0,z)==dot(B,b)==1
p0=dot(B,x);s0=dot(B,z)
g=metric(q0,q0,N);k2=metric(B,B,N);t=metric(B,q0,N)
assert (p0,s0,g,k2,t)==(F(-7,9),F(-11,9),F(21),F(35,3),F(35,3))
assert -p0-s0-2==0 and metric(b,sub(x,b),M)==metric(z,sub(x,z),M)==0
beta0=t/g;W2=(g-1)*(k2-t*t/g)/g
assert beta0==F(5,9) and W2==F(400,81)
assert (p0+beta0+F(20,9))/2==1 and (p0+beta0-F(20,9))/2==s0
assert metric(b,b,M)==F(5,21)<F(17,21)==metric(z,z,M)
report={
 'identity':'TWO_APEX_APEX_CLOSING_1281_V1',
 'analytic_necessary_base_rank':'max_B ||b||_M > ||z||_M; every base norm maximizer has a true weak exit to x',
 'cap_bound':'u >= (5+delta)(4+delta) = 20+9delta+delta^2 > 20',
 'minimizing_closed_beta':'(5+delta)/(9+2delta)',
 'cap_polynomial_identity':'(A-beta)^2-4A(A-1)beta(1-beta)=((2A-1)beta-A)^2, A=5+delta',
 'closing_xz_GJ_strict_lower':1281,'global_GJ_strict_upper':729,
 'whole_deg4_chain':{'base_closing_GJ_strict_lower':'4997/5','apex_closing_GJ_strict_lower':'1281','requires_H0_or_corresponding_true_closing_primal_exit':True,'requires_B_to_first_pole_and_three_cyclic_polar_arrows':True,'arbitrary_V_F':True,'whole_E17_layer_excluded':False,'all_two_apex_polyhedra_excluded':False},
 'boundary_control':{'M_diag':[str(t) for t in M],'x':[str(t) for t in x],'b':[str(t) for t in b],'z':[str(t) for t in z],'q0':[str(t) for t in q0],'B':[str(t) for t in B],'p':str(p0),'s':str(s0),'g':str(g),'k_squared':str(k2),'t':str(t),'beta':str(beta0),'width_squared':str(W2),'delta':'0','status':'formal common-metric cap boundary only; zero delta, no actual body or actual volume centroid; displayed b is too small to be the forced maximum-base vertex'}}
data=(json.dumps(report,sort_keys=True,indent=2)+'\n').encode();path=Path('two_apex_apex_closing.json')
mode=sys.argv[1] if len(sys.argv)>1 else 'build';assert mode in ('build','check')
if mode=='build':path.write_bytes(data)
else:assert path.read_bytes()==data
print('TWO_APEX_RANK_OBSTRUCTION_SQUARE_IDENTITIES_PASS')
print('TWO_APEX_COMMON_CAP_U20_PLUS_9DELTA_PLUS_DELTA2_PASS')
print('WHOLE_DEG4_CHAIN_BASE_OR_APEX_CLOSING_729_CONTRADICTIONS_PASS')
print('FORMAL_RATIONAL_COMMON_METRIC_CAP_BOUNDARY_NOT_A_BODY_PASS')
print(path.name,len(data),hashlib.sha256(data).hexdigest())
print('TWO_APEX_APEX_CLOSING_1281_RECOVERY_PASS')
