# material-4ef1fe90e4d9

AI research material

---

"""PLANAR3_OWN_COM_SHEAR_RESCUE_V1: exact geometric control and interval proof.
CPython 3.13.5, SymPy 1.14.0, assertions enabled, no other dependencies.
Run in this source's directory: python planar3_own_com.py build|check
Every input is literal below. No network, seed, external checkpoint or solver.
"""
from pathlib import Path
from itertools import combinations
from math import comb
import hashlib
import json
import sys
import sympy as s

if not __debug__:
    raise SystemExit('Assertions required; do not use -O')
if sys.argv[1:] not in (['build'], ['check']):
    raise SystemExit('Use build|check')
assert s.__version__ == '1.14.0', s.__version__
R=s.Rational
t=s.Symbol('t')
I=s.eye(3)
Z3=s.zeros(3,1)
EPS=R(1,1024)
EXPECTED_REPORT_SHA='668f508a9de55a6d595fc138c0ec5749eff98409bad29667010ce1c736b81ce9'


def simp(x):
    return s.cancel(x)


def smat(A):
    return A.applyfunc(simp)


def det3(a,b,c):
    return s.det(s.Matrix.hstack(a,b,c))


def sym(a,b):
    return (a*b.T+b*a.T)/2


def hull(V):
    """Exact maximal supports, their genuine edges, oriented polygon cycles."""
    supports={}
    for ijk in combinations(range(len(V)),3):
        A=s.Matrix.vstack(*(V[i].T for i in ijk))
        if not A.det():
            continue
        q=A.inv()*s.ones(3,1)
        if all(q.dot(v)<=1 for v in V):
            inds=tuple(i for i,v in enumerate(V) if q.dot(v)==1)
            supports[inds]=q
    fs=sorted(supports)
    Q=[supports[f] for f in fs]
    E={}
    for i,j in combinations(range(len(fs)),2):
        ab=tuple(sorted(set(fs[i]) & set(fs[j])))
        if len(ab)==2:
            assert ab not in E
            E[ab]=(i,j)
    cycles=[]
    for f in fs:
        adj={a:[] for a in f}
        for a,b in E:
            if a in f and b in f:
                adj[a].append(b);adj[b].append(a)
        assert all(len(n)==2 for n in adj.values())
        a=min(f);cyc=[a,min(adj[a])]
        while len(cyc)<len(f):
            candidates=[b for b in adj[cyc[-1]] if b!=cyc[-2]]
            assert len(candidates)==1 and candidates[0] not in cyc
            cyc.append(candidates[0])
        assert cyc[0] in adj[cyc[-1]]
        if det3(*(V[i] for i in cyc[:3]))<0:
            cyc=cyc[:1]+cyc[:0:-1]
        cycles.append(cyc)
    assert len(V)-len(E)+len(Q)==2
    assert all(sum(i in f for f in fs)>=3 for i in range(len(V)))
    return Q,fs,cycles,E


def triangulate(cycles):
    return [(c[0],c[j],c[j+1]) for c in cycles for j in range(1,len(c)-1)]


def volume_centroid(V,tri):
    ds=[simp(det3(*(V[i] for i in z))) for z in tri]
    den=simp(sum(ds))
    g=smat(sum((d*sum((V[i] for i in z),Z3) for d,z in zip(ds,tri)),Z3)/(4*den))
    return simp(den/6),g,ds


def covariance(V,tri,ds,vol,g):
    Q=s.zeros(3)
    for z,d in zip(tri,ds):
        a=sum((V[i] for i in z),Z3)
        Q += d*(a*a.T+sum((V[i]*V[i].T for i in z),s.zeros(3)))
    return smat(Q/(120*vol)-g*g.T)


def primitives(V,Q,E,M):
    N=M.inv()
    out=[]
    for (a,b),(q,r) in sorted(E.items()):
        vals=[(V[a].T*M*(V[b]-V[a]))[0],
              (V[b].T*M*(V[a]-V[b]))[0],
              (Q[q].T*N*(Q[r]-Q[q]))[0],
              (Q[r].T*N*(Q[q]-Q[r]))[0]]
        out.append({'edge':[a,b],'facets':[q,r], 'values':[simp(v) for v in vals]})
    return out


def census(nv,nf,pr):
    pv=[[] for _ in range(nv)];dq=[[] for _ in range(nf)]
    strict_edges=[];weak_edges=[]
    for row in pr:
        a,b=row['edge'];q,r=row['facets'];x=row['values']
        pv[a].append(x[0]);pv[b].append(x[1]);dq[q].append(x[2]);dq[r].append(x[3])
        if max(x)<0: strict_edges.append([a,b])
        elif max(x)==0: weak_edges.append([a,b])
    U=[i for i,z in enumerate(pv) if max(z)<0]
    Wu=[i for i,z in enumerate(pv) if max(z)==0]
    S=[i for i,z in enumerate(dq) if max(z)<0]
    Ws=[i for i,z in enumerate(dq) if max(z)==0]
    return dict(S=S,U=U,H=strict_edges,weak_vertices=Wu,weak_facets=Ws,weak_edges=weak_edges)


def bernstein_positive(poly):
    """All Bernstein coefficients on the WHOLE closed [0,EPS] are positive."""
    P=s.Poly(poly,t,domain=s.QQ)
    n=P.degree()
    coeff=[P.nth(j)*EPS**j for j in range(n+1)]
    B=[sum(coeff[j]*R(comb(k,j),comb(n,j)) for j in range(k+1)) for k in range(n+1)]
    assert all(x>0 for x in B), (P.as_expr(),min(B))
    return {'power_ascending':[P.nth(j) for j in range(n+1)],
            'degree':n,'bernstein_min':min(B)}


def certify_positive(f):
    """Exact nonzero numerator/denominator sign, not a sampled sign check."""
    n,d=s.fraction(simp(f))
    at0=d.subs(t,0)
    assert at0!=0
    if at0<0:n,d=-n,-d
    assert n.subs(t,0)>0
    return {'numerator':bernstein_positive(n),'denominator':bernstein_positive(d)}


def encode(x):
    if isinstance(x,s.MatrixBase):return [[str(z) for z in row] for row in x.tolist()]
    if isinstance(x,s.Basic):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(z) for z in x]
    return x


# Rational chart. Multiplication by diag(1,sqrt(3),1) gives physical Euclidean input.
M0=s.diag(1,3,1)
V=[s.Matrix(a) for a in [(1,0,0),(1,R(1,3),0),(-R(1,2),R(1,2),0),
   (-1,R(1,3),0),(-R(1,2),-R(1,2),0),(0,-R(2,3),0),
   (R(1,5),R(1,10),2),(-R(1,5),-R(1,10),-2)]]
Q,fs,cycles,E=hull(V)
tri=triangulate(cycles)
vol,g,ds=volume_centroid(V,tri)
Sigma=covariance(V,tri,ds,vol,g)
assert (len(V),len(E),len(Q))==(8,18,12)
assert vol==2 and g==Z3 and all(x>0 for x in ds)
assert Sigma==s.Matrix([[R(103,750),R(1,500),R(1,25)],
 [R(1,500),R(409,9000),R(1,50)],[R(1,25),R(1,50),R(2,5)]])
pr0=primitives(V,Q,E,M0);c0=census(8,12,pr0)
assert [len(c0[k]) for k in ('S','U','H')]==[9,5,12]
assert c0['weak_vertices']==[0,2,4] and c0['weak_facets']==[]
assert c0['weak_edges']==[[0,1],[2,3],[4,5]]
assert sum(v==0 for row in pr0 for v in row['values'])==3
for i in range(3):
    zi=V[2*i];ui=V[2*i+1]-zi
    assert (zi.T*M0*ui)[0]==0
    radial=lambda x:(zi.T*M0*x)[0]
    assert [j for j,x in enumerate(V) if radial(x)==radial(zi)]==[2*i,2*i+1]
    assert all(radial(x)<=radial(zi) for x in V)
T=[sym(V[2*i],V[2*i+1]-V[2*i]) for i in range(3)]
assert sum(T,s.zeros(3))==s.zeros(3)
assert s.Matrix.hstack(*(s.Matrix(A).reshape(9,1) for A in T)).rank()==2
assert sum((V[2*i+1]-V[2*i] for i in range(3)),Z3)==Z3

# General planar equilateral contact sector: arbitrary positive edge lengths h_i.
r=s.sqrt(3)
z=[s.Matrix([1,0]),s.Matrix([-R(1,2),r/2]),s.Matrix([-R(1,2),-r/2])]
d=[s.Matrix([-a[1],a[0]]) for a in z]
h=s.symbols('h1 h2 h3',positive=True)
p1,p2,l1,l2,hh=s.symbols('p1 p2 l1 l2 hh')
pp=s.Matrix([p1,p2]);ell=s.Matrix([l1,l2])
Hplane=s.Matrix([[hh+2*l1-2*p1,-l2+p2],[-l2+p2,hh]])
Dnormalized=s.zeros(2);BETA=0
for zi,di,hi in zip(z,d,h):
    ui=hi*di;a=pp.dot(zi);b=pp.dot(ui)
    zd=ell-a*zi;ud=-(a+b)*ui-b*zi
    # A common -g2 term drops out after summation because sum_i d_i=0.
    z2=a*a*zi;u2=(a+b)**2*ui+(2*a*b+b*b)*zi
    Ti=sym(zi,ui);Di=sym(zd,ui)+sym(zi,ud)
    assert s.simplify(s.trace(Di)+s.trace(Hplane*Ti))==0
    Dnormalized+=Di/hi
    BETA+=(z2.dot(ui)+zd.dot(ud)+zi.dot(u2)+s.trace(Hplane*Di))/hi
assert sum(d,s.zeros(2,1))==s.zeros(2,1)
Dnormalized=Dnormalized.applyfunc(s.simplify)
assert s.simplify(s.trace(Dnormalized))==0
assert s.simplify(BETA-R(9,2)*(p1*l2-p2*l1))==0
L11,L12,L13,L22,L23,L33=s.symbols('L11 L12 L13 L22 L23 L33')
W=s.Matrix([[L12,(L22-L11)/2,L23/2],[(L22-L11)/2,-L12,-L13/2],[L23/2,-L13/2,0]])
Lgeneric=s.Matrix([[L11,L12,L13],[L12,L22,L23],[L13,L23,L33]])
rp=s.Matrix(s.symbols('a b c'))
assert s.expand((rp.T*W*rp)[0]-(rp[0]*(Lgeneric*rp)[1]-rp[1]*(Lgeneric*rp)[0]))==0
assert s.trace(W)==0
sigma,tau,delta=s.symbols('sigma tau delta',positive=True)
Shear=s.Matrix([[1,0,delta],[0,1,0],[0,0,1]])
ShearedSigma=Shear*s.diag(sigma,sigma,tau)*Shear.T
assert ShearedSigma[0,2]==delta*tau
assert Shear*s.Matrix([p1,p2,0])==s.Matrix([p1,p2,0])

# Explicit true-volume-centred projective-then-affine arc for the actual body.
p=s.Matrix([1,0,0])
Y=[smat(v/(1+t*p.dot(v))) for v in V]
vol_t,g_t,_=volume_centroid(Y,tri)
assert g_t.diff(t).subs(t,0)==-5*Sigma*p
assert g_t.diff(t,2).subs(t,0)/2==s.Matrix([R(1,8),R(7,48),0])
X=[smat(y-g_t) for y in Y]
Q_t=[smat((q+t*p)/(1-(q+t*p).dot(g_t))) for q in Q]
for k,f in enumerate(fs):
    for j in f:assert simp(Q_t[k].dot(X[j])-1)==0
H1=s.Matrix([[-R(47,75),-R(3,100),0],[-R(3,100),0,0],[0,0,0]])
H2=s.Matrix([[-R(16181,9000),R(4731,10000),0],[R(4731,10000),0,0],[0,0,0]])
M=M0+t*H1+t*t*H2
co2=[]
for i in range(3):
    f=simp((X[2*i].T*(M0+t*H1)*(X[2*i+1]-X[2*i]))[0])
    assert f.subs(t,0)==0 and f.diff(t).subs(t,0)==0
    co2.append(simp(f.diff(t,2).subs(t,0)/2))
assert co2==[-R(1427,10000),R(48899,90000),-R(16003,45000)]
assert sum(co2)==R(9,200)
pr_t=primitives(X,Q_t,E,M)
interval=[]
for i,v in enumerate(V):
    interval.append({'guard':'projective_den_'+str(i),'certificate':certify_positive(1+t*p.dot(v))})
for i in (1,2,3):
    interval.append({'guard':'metric_leading_minor_'+str(i),'certificate':certify_positive(M[:i,:i].det())})
for j,q in enumerate(Q):
    interval.append({'guard':'actual_centroid_facet_den_'+str(j),'certificate':certify_positive(1-(q+t*p).dot(g_t))})
shadows=[]
for old,new in zip(pr0,pr_t):
    assert old['edge']==new['edge'] and old['facets']==new['facets']
    for k,(f0,f) in enumerate(zip(old['values'],new['values'])):
        label='edge_'+str(old['edge'])+'_primitive_'+str(k)
        if f0!=0:
            cert=certify_positive((1 if f0>0 else -1)*f)
        else:
            assert k==0 and old['edge'] in [[0,1],[2,3],[4,5]]
            normalized=simp(f/t**2)
            assert normalized.subs(t,0)==R(3,200)
            cert=certify_positive(normalized)
            shadows.append({'edge':old['edge'],'phi_over_t2':normalized})
        interval.append({'guard':label,'certificate':cert})
Ve=[smat(x.subs(t,EPS)) for x in X]
Qe=[smat(q.subs(t,EPS)) for q in Q_t]
Me=M.subs(t,EPS)
pre=primitives(Ve,Qe,E,Me);ce=census(8,12,pre)
assert [len(ce[k]) for k in ('S','U','H')]==[9,5,12]
assert all(ce[k]==c0[k] for k in ('S','U','H'))
assert all(not ce[k] for k in ('weak_vertices','weak_facets','weak_edges'))
vole,ge,_=volume_centroid(Ve,tri)
assert ge==Z3 and vole==vol_t.subs(t,EPS)
Qcheck,fscheck,cyclescheck,Echeck=hull(Ve)
assert fscheck==fs and cyclescheck==cycles and Echeck==E and Qcheck==Qe
assert all(v!=0 for row in pre for v in row['values'])
Be=s.zeros(3)
for i in range(3):
    Be[i,i]=s.sqrt(s.factor(Me[i,i]-sum(Be[k,i]**2 for k in range(i))))
    for j in range(i+1,3):
        Be[i,j]=s.factor((Me[i,j]-sum(Be[k,i]*Be[k,j] for k in range(i)))/Be[i,i])
assert (Be.T*Be-Me).applyfunc(s.simplify)==s.zeros(3)
B0=s.diag(1,s.sqrt(3),1)
assert B0.T*B0==M0

# Preserved failures of the symmetric / one-axis apex choices, distinct bodies.
negative=[]
for ap,expected in ((s.Matrix([0,0,2]),[6,5,9,6]),(s.Matrix([R(1,5),0,2]),[8,5,11,2])):
    Vn=V[:6]+[ap,-ap]
    Qn,Fn,Cn,En=hull(Vn);vn,gn,dn=volume_centroid(Vn,triangulate(Cn))
    Sn=covariance(Vn,triangulate(Cn),dn,vn,gn)
    pn=primitives(Vn,Qn,En,M0);cn=census(8,12,pn)
    assert vn==2 and gn==Z3
    assert [len(cn[k]) for k in ('S','U','H','weak_facets')]==expected
    assert cn['weak_vertices']==[0,2,4]
    assert len(cn['weak_edges'])==3+expected[-1]
    for k in cn['weak_facets']:
        foot=M0.inv()*Qn[k]/(Qn[k].T*M0.inv()*Qn[k])[0]
        assert foot not in Vn
    negative.append({'vertices':Vn,'poles':Qn,'facet_cycles':Cn,'volume':vn,'centroid':gn,
      'covariance':Sn,'primitives':pn,'census':cn,'physical_weak_points':3+expected[-1]})
assert negative[0]['covariance']==s.diag(R(2,15),R(2,45),R(2,5))

report={
 'identity':'PLANAR3_OWN_COM_SHEAR_RESCUE_V1',
 'scope':'Non-record actual control, NOT110, NOT10/17/9. Universal regularization of exactly three simple planar equilateral cyclic VE contacts, using true own centroid and a preliminary plane-fixing shear only when needed.',
 'environment':'CPython3.13.5 SymPy1.14.0 assertions enabled',
 'input':{'rational_chart_vertices':V,'initial_metric_M0':M0,'initial_Euclidean_B0':B0,
          'initial_Euclidean_vertices':[B0*v for v in V],'p':p,'epsilon_endpoint':EPS},
 'initial':{'f_vector':[8,18,12],'C':36,'chart_volume':vol,'Euclidean_volume':2*s.sqrt(3),
   'centroid':g,'chart_covariance':Sigma,'Euclidean_covariance':B0*Sigma*B0.T,
   'maximal_facet_cycles':cycles,'poles_in_chart':Q,'edges':[[list(k),list(v)] for k,v in sorted(E.items())],
   'primitives':pr0,'census':c0},
 'general_algebra':{'physical_z':z,'physical_unit_tangents':d,'arbitrary_edge_factors':h,
   'first_order_plane_metric':Hplane,'normalized_weighted_projective_tensor':Dnormalized,
   'normalized_weighted_second_coefficient':s.factor(BETA),'tracezero_covariance_form':W,
   'axisymmetric_covariance_shear':Shear,'sheared_covariance':ShearedSigma},
 'arc':{'raw_chart_projective_volume':vol_t,'true_chart_projective_centroid':g_t,'M':M,
   'N':smat(M.inv()),'H1':H1,'H2':H2,'centered_chart_vertices':X,'centered_chart_poles':Q_t,
   'before_second_correction_coefficients':co2,'shadows':shadows},
 'interval_certificates':interval,'negative_controls':negative,
 'endpoint':{'chart_vertices':Ve,'chart_poles':Qe,'metric_M':Me,'metric_N':Me.inv(),
   'chart_volume':vole,'chart_centroid':ge,'Euclidean_B':Be,'Euclidean_vertices':[Be*x for x in Ve],
   'Euclidean_volume':s.factor(Be.det()*vole),'primitives':pre,'census':ce},
 'continuum_statement':'Every rational guard numerator and denominator has strictly positive exact Bernstein coefficients on[0,1/1024]. All69 initially nonzero primitives retain signs; the other three are t^2 times positive functions. Thus every0<t<=1/1024 has unchanged strictS/U/H9/5/12 and no physical weak equilibrium. Physical vertices=B(t)X(t),B upper positive Cholesky ofM(t).',
 'general_limit':'For initially axial covariance the direct first and second weighted jets vanish, not an all-orders impossibility. An arbitrarily small actual affine shear fixing the contact plane pointwise changes covariance, preserves the three simple contacts and all other strict guards, and then the second-order theorem applies. No universal arbitrary-three-position or mixed A/B theorem is asserted.'
}
raw=(json.dumps(encode(report),sort_keys=True,indent=2,ensure_ascii=True)+'\n').encode()
sha=hashlib.sha256(raw).hexdigest()
if EXPECTED_REPORT_SHA is not None:assert sha==EXPECTED_REPORT_SHA,sha
root=Path(__file__).resolve().parent
out=root/'planar3_own_com.json'
if sys.argv[1]=='build':out.write_bytes(raw)
else:assert out.read_bytes()==raw,'Exact recomputation differs'
print('ACTUAL_8_18_12_TRUE_CENTROID_ZERO_THREE_VE_PASS')
print('ARBITRARY_EDGE_LENGTHS_EXACT_COVARIANCE_SECOND_JET_PASS')
print('PLANE_FIXING_SHEAR_REMOVES_AXIAL_COVARIANCE_EXCEPTION_PASS')
print('WHOLE_INTERVAL_ALL_72_PRIMITIVES_SPD_AND_INCIDENCE_PASS')
print('SAME_STRICT_9_5_12_NO_WEAK_FOR_ALL_POSITIVE_PARAMETERS_PASS')
print('SYMMETRIC_NINE_AND_ONE_AXIS_FIVE_CONTACT_NEGATIVE_CONTROLS_PASS')
print('planar3_own_com.json',len(raw),sha)
print('PLANAR3_OWN_COM_SHEAR_RESCUE_RECOVERY_PASS')
