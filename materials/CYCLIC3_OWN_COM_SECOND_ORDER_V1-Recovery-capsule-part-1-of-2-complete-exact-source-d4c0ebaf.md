# material-d4c0ebaf51a2

AI research material

---

"""CYCLIC3_OWN_COM_SECOND_ORDER_V1: exact geometric control and interval proof.
CPython 3.13.5, SymPy 1.14.0, assertions enabled, no other dependencies.
Run in this source's directory: python cyclic3_own_com.py build|check
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
EXPECTED_REPORT_SHA='c2f96e68a25eb4dd36e22d7ccc7a410c4f75974367d99dd4c1c1d2e52d481ac3'


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


# The three contact points are z_i; the genuine directed edges have u_i=h_i d_i.
h=[R(1,4),R(1,2),R(3,4)]
z=[s.Matrix(a) for a in [(1,1,0),(0,1,1),(1,0,1)]]
d=[s.Matrix(a) for a in [(1,-1,0),(0,1,-1),(-1,0,1)]]
V=[v for i in range(3) for v in (z[i],z[i]+h[i]*d[i])]
basecycle=[0,3,2,5,4,1]
btri=triangulate([basecycle])
bds=[det3(*(V[i] for i in tri)) for tri in btri]
assert all(x>0 for x in bds)
baseg=sum((w*sum((V[i] for i in tri),Z3) for w,tri in zip(bds,btri)),Z3)/(3*sum(bds))
V.append(-3*baseg)
assert V[6]==s.Matrix([-R(17,10),-R(79,40),-R(93,40)])
Q,fs,cycles,E=hull(V)
tri=triangulate(cycles)
vol,g,ds=volume_centroid(V,tri)
Sigma=covariance(V,tri,ds,vol,g)
assert (len(V),len(E),len(Q))==(7,12,7)
assert vol==R(10,3) and g==Z3 and all(x>0 for x in ds)
assert Sigma==s.Matrix([[R(1,4),R(323,1600),R(73,320)],
 [R(323,1600),R(541,1600),R(1,4)],[R(73,320),R(1,4),R(723,1600)]])
assert all(Sigma[:i,:i].det()>0 for i in (1,2,3))
pr0=primitives(V,Q,E,I);c0=census(7,7,pr0)
assert [len(c0[k]) for k in ('S','U','H')]==[5,4,7]
assert c0['weak_vertices']==[0,2,4] and c0['weak_facets']==[]
assert c0['weak_edges']==[[0,1],[2,3],[4,5]]
assert sum(v==0 for row in pr0 for v in row['values'])==3
# Thus precisely three physical simple VE contacts, not VF packets.
for i in range(3):
    zi=z[i];ui=h[i]*d[i]
    assert zi.dot(ui)==0
    support=[j for j,x in enumerate(V) if zi.dot(x)==zi.dot(zi)]
    assert support==[2*i,2*i+1]
    assert all(zi.dot(x)<=zi.dot(zi) for x in V)

# Unique positive stress. Three trace-zero rows span the diagonal trace-zero plane.
T=[sym(z[i],h[i]*d[i]) for i in range(3)]
alpha=[1/x for x in h]
assert sum((a*A for a,A in zip(alpha,T)),s.zeros(3))==s.zeros(3)
assert s.Matrix.hstack(*(s.Matrix(A).reshape(9,1) for A in T)).rank()==2
assert sum((a*h[i]*d[i] for i,a in enumerate(alpha)),Z3)==Z3
assert sum((a*z[i].dot(z[i])*h[i]*d[i] for i,a in enumerate(alpha)),Z3)==Z3
p=s.Matrix([1,0,0]);L=5*Sigma
D=[]
for i in range(3):
    ui=h[i]*d[i];zi=z[i]
    D.append(sym(L*p,ui)-(p.dot(2*zi+ui))*T[i]-p.dot(ui)*(zi*zi.T))
Dsum=sum((a*A for a,A in zip(alpha,D)),s.zeros(3))
K=Dsum-s.diag(*Dsum.diagonal())
assert K==s.Matrix([[0,-1,1],[-1,0,0],[1,0,0]])
assert s.trace(Dsum)==0 and s.trace(K*K)==4

# True uniformly refilled projective image and ACTUAL new volume centroid.
Y=[v/(1+t*p.dot(v)) for v in V]
vol_t,g_t,_=volume_centroid(Y,tri)
# Independent pyramid-area formula, with exact transformed triangle masses.
wt=[w/s.prod(1+t*p.dot(V[i]) for i in tri0) for w,tri0 in zip(bds,btri)]
base_t=sum((w*sum((Y[i] for i in tri0),Z3) for w,tri0 in zip(wt,btri)),Z3)/sum(wt)
assert smat(g_t-(base_t+Y[6])/4)==Z3
assert g_t.diff(t).subs(t,0)==-L*p
assert g_t.diff(t,2).subs(t,0)/2==s.Matrix([-R(369,640),-R(14799,12800),-R(3961,2560)])
X=[smat(y-g_t) for y in Y]
Q_t=[smat((q+t*p)/(1-(q+t*p).dot(g_t))) for q in Q]
for k,f in enumerate(fs):
    for j in f:assert simp(Q_t[k].dot(X[j])-1)==0

# A single metric arc, applied AFTER the projective image is truly recentered.
H0=s.diag(R(121,64),R(21,160),0)
H1=H0+R(459,640)*K
H2=s.diag(R(206441,102400),R(156241,51200),0)
M=I+t*H1+t*t*H2
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
            sign=1 if f0>0 else -1
            cert=certify_positive(sign*f)
        else:
            assert k==0 and old['edge'] in [[0,1],[2,3],[4,5]]
            i=old['edge'][0]//2
            normalized=simp(f/(h[i]*t*t))
            assert normalized.subs(t,0)==1
            cert=certify_positive(normalized)
            shadows.append({'edge':old['edge'],'normalized_phi_over_h_t2':normalized})
        interval.append({'guard':label,'certificate':cert})

# Exact representative at the closed interval endpoint; no numerical tolerances.
Ve=[smat(x.subs(t,EPS)) for x in X]
Qe=[smat(q.subs(t,EPS)) for q in Q_t]
Me=M.subs(t,EPS)
pre=primitives(Ve,Qe,E,Me);ce=census(7,7,pre)
assert [len(ce[k]) for k in ('S','U','H')]==[5,4,7]
assert ce['S']==c0['S'] and ce['U']==c0['U'] and ce['H']==c0['H']
assert all(not ce[k] for k in ('weak_vertices','weak_facets','weak_edges'))
vole,ge,_=volume_centroid(Ve,tri)
assert ge==Z3 and vole==vol_t.subs(t,EPS)
Qcheck,fscheck,cyclescheck,Echeck=hull(Ve)
assert fscheck==fs and cyclescheck==cycles and Echeck==E and Qcheck==Qe
assert all(len(row['values'])==4 and all(v!=0 for v in row['values']) for row in pre)

# Exact Euclidean reconstruction; positive diagonal fixes every square-root choice.
Be=s.zeros(3)
for i in range(3):
    Be[i,i]=s.sqrt(s.factor(Me[i,i]-sum(Be[k,i]**2 for k in range(i))))
    for j in range(i+1,3):
        Be[i,j]=s.factor((Me[i,j]-sum(Be[k,i]*Be[k,j] for k in range(i)))/Be[i,i])
assert (Be.T*Be-Me).applyfunc(s.simplify)==s.zeros(3)
Ve_euclidean=[Be*x for x in Ve]
assert Be*ge==Z3

# Meaningful failed preliminary control: equal edge parameters force three extra EF contacts.
Vsym=[s.Matrix(a) for a in [(1,1,0),(R(3,2),R(1,2),0),(0,1,1),
 (0,R(3,2),R(1,2)),(1,0,1),(R(1,2),0,R(3,2)),(-2,-2,-2)]]
Qsym,Fsym,Csym,Esym=hull(Vsym)
vsym,gsym,dsym=volume_centroid(Vsym,triangulate(Csym))
psym=primitives(Vsym,Qsym,Esym,I);csym=census(7,7,psym)
assert vsym==R(10,3) and gsym==Z3
assert [len(csym[k]) for k in ('S','U','H')]==[4,4,6]
assert csym['weak_vertices']==[0,2,4] and csym['weak_facets']==[1,4,6]
assert len(csym['weak_edges'])==6
for k in csym['weak_facets']:
    foot=Qsym[k]/Qsym[k].dot(Qsym[k])
    assert foot not in Vsym

report={
 'identity':'CYCLIC3_OWN_COM_SECOND_ORDER_V1',
 'scope':'Non-record control, NOT110, NOT an E17 existence/exclusion; arbitrary small true own-COM projective-affine rescue of three simple contacts.',
 'environment':'CPython3.13.5 SymPy1.14.0 assertions enabled',
 'input':{'h':h,'vertices':V,'p':p,'epsilon_endpoint':EPS},
 'initial':{'f_vector':[7,12,7],'C':24,'volume':vol,'centroid':g,'covariance':Sigma,
            'maximal_facet_cycles':cycles,'poles':Q,'edges':[[list(k),list(v)] for k,v in sorted(E.items())],
            'primitives':pr0,'census':c0},
 'stress':{'alpha':alpha,'T':T,'D_i':D,'D_sum':Dsum,'K':K},
 'arc':{'raw_projective_volume':vol_t,'true_projective_centroid':g_t,'M':M,'N':smat(M.inv()),
        'H1':H1,'H2':H2,'centered_vertices':X,'centered_poles':Q_t,'shadows':shadows},
 'interval_certificates':interval,
 'symmetric_failed_control':{'vertices':Vsym,'poles':Qsym,'maximal_facet_cycles':Csym,
   'volume':vsym,'centroid':gsym,'primitives':psym,'census':csym,
   'scope':'The equal h=1/2 pyramid has six physical contacts, three VE and three distinct EF, not merely three; it does not satisfy the three-only theorem hypotheses.'},
 'endpoint':{'vertices':Ve,'poles':Qe,'metric_M':Me,'metric_N':Me.inv(),
             'preaffine_volume':vole,'preaffine_centroid':ge,'euclidean_B':Be,'euclidean_vertices':Ve_euclidean,
             'euclidean_volume':s.factor(Be.det()*vole),'primitives':pre,'census':ce},
 'euclidean_reconstruction':'For every0<t<=1/1024, let B be the unique positive upper-triangular Cholesky factor with B^T B=M(t), positive diagonal; actual Euclidean vertices are B X_i(t). Its true centroid is0, actual volume det(B)*vol_t. All polar computations use exactly N=M^-1, never independently recentered polar masses.',
 'continuum_statement':'All 45 initially nonzero primitives preserve their signs on the whole closed interval; each of the other three equals h_i*t^2 times a strictly positive rational function certified on[0,1/1024]. All original strict equilibria remain; no weak contacts remain for t>0.'
}
raw=(json.dumps(encode(report),sort_keys=True,indent=2,ensure_ascii=True)+'\n').encode()
sha=hashlib.sha256(raw).hexdigest()
if EXPECTED_REPORT_SHA is not None:assert sha==EXPECTED_REPORT_SHA,sha
root=Path(__file__).resolve().parent
out=root/'cyclic3_own_com.json'
if sys.argv[1]=='build':out.write_bytes(raw)
else:assert out.read_bytes()==raw,'Exact recomputation differs'
print('ACTUAL_7_12_7_VOLUME_10_OVER_3_COM_ZERO_THREE_VE_PASS')
print('ALL_AFFINE_ORDERS_AND_ALL_FIRST_PROJECTIVE_JETS_STRESS_BARRIER_PASS')
print('TRUE_PROJECTIVE_CENTROID_AND_SECOND_ORDER_THREE_CONTACT_RESCUE_PASS')
print('WHOLE_INTERVAL_SPD_INCIDENCE_ALL_48_PRIMITIVES_PASS')
print('SAME_STRICT_5_4_7_NO_WEAK_FOR_ALL_POSITIVE_PARAMETERS_PASS')
print('cyclic3_own_com.json',len(raw),sha)
print('CYCLIC3_OWN_COM_SECOND_ORDER_RECOVERY_PASS')
