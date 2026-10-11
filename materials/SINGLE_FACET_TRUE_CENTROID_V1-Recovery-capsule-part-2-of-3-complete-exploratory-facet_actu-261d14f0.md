# material-261d14f02258

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""CANONICAL_C622_ONE_FACET_CENTROID_ACTUATOR_V1.
Exact differential certificate and a separate floating locator, NOT a new endpoint.
Parents: canonical scoped16 recovery, plus complete exact_ears.py helpers.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from exact_ears import *
from itertools import combinations
PIN='142ddb5d88fdc8b1721dbb62f52d9b71b78ac4c36e8600131235c6c4289698a0'

def loadexact(path):
 data=Path(path).read_bytes();assert sha256(data).hexdigest()==PIN
 r=json.loads(data);X=[tuple(map(F,p)) for p in r['raw_vertices']]
 adj=[set() for x in X]
 for i,j in r['edges']:adj[i].add(j);adj[j].add(i)
 return r,X,adj

def outer(a,b):return [[x*y for y in b] for x in a]
def matadd(a,b):return [[x+y for x,y in zip(c,d)] for c,d in zip(a,b)]
def matscale(a,t):return [[t*x for x in r] for r in a]

def exact_audit(path,out):
 r,X,adj=loadexact(path);g=tuple(map(F,r['raw_centroid']));V=F(r['ordinary_volume'])
 movable=[i for i,face in enumerate(r['faces']) if all(len(adj[v])==3 for v in face)]
 assert movable==[48,55,69,70,89,93,99,100,101,105,110,112,113,114,115,117,120,123,124,125]
 rows=[]
 for f in movable:
  cy=r['faces'][f];N=cross(sub(X[cy[1]],X[cy[0]]),sub(X[cy[2]],X[cy[0]]));h=dot(N,X[cy[0]])
  if h<0:N=tuple(-x for x in N);h=-h
  assert h>0;q=tuple(x/h for x in N)
  assert all(dot(q,X[i])==1 for i in cy)
  assert all(dot(q,x)<1 for i,x in enumerate(X) if i not in cy)
  w=F(0);c=(F(0),)*3;T=[[F(0)]*3 for _ in range(3)]
  for j in range(1,len(cy)-1):
   tri=[X[k] for k in [cy[0],cy[j],cy[j+1]]];weight=det(*tri)/2
   assert weight>0
   s=tuple(sum(p[k] for p in tri) for k in range(3));w+=weight
   c=tuple(c[k]+weight*s[k]/3 for k in range(3))
   K=outer(s,s)
   for p in tri:K=matadd(K,outer(p,p))
   T=matadd(T,matscale(K,weight/12))
  c=tuple(x/w for x in c);T=matscale(T,1/w)
  assert all(dot(T[i],q)==c[i] for i in range(3))
  # All leading principal minors certify the true facet SECOND moment positive.
  pm=[T[0][0],T[0][0]*T[1][1]-T[0][1]**2,det(*T)];assert min(pm)>0
  A=matadd(T,matscale(outer(g,c),-1));gap=1-dot(q,g);assert gap>0
  assert det(*A)==gap*pm[2]
  rows.append(dict(facet=f,vertices=cy,area_over_normal=str(w),surface_centroid=list(map(str,c)),second_moment_sha256=sha256(B(T)).hexdigest(),jacobian_determinant_sha256=sha256(B(-w**3*det(*A)/V**3)).hexdigest(),centroid_interior_gap_sha256=sha256(B(gap)).hexdigest(),positive_gram_minors=3,determinant_identity=True))
 report=dict(object='CANONICAL_C622_ONE_FACET_CENTROID_ACTUATOR_V1',parent_A_sha256=PIN,facets=movable,rows=rows,exact_facets=20,positive_gram_minors=60)
 Path(out).write_bytes(B(report));print('CANONICAL_C622_TWENTY_SINGLE_FACET_COM_ACTUATORS_EXACT_PASS',len(B(report)),sha256(B(report)).hexdigest(),flush=True)

def numeric_scan(path,raw,out,begin,end):
 import numpy as np,scipy,platform
 from scipy.optimize import least_squares
 r,Xe,adj=loadexact(path);X=np.array(Xe,float);g0=np.array(list(map(F,r['raw_centroid'])),float)
 H=json.loads(Path(raw).read_bytes())['H'];Q0=np.array([[float(F(x,a[-1])) for x in a[:3]] for a in H])
 simple=[i for i in range(len(X)) if len(adj[i])==3];records=[]
 def escape(A):
  e=A[None,:,:]-A[:,None,:];d=np.einsum('ic,ijc->ij',A,e);np.fill_diagonal(d,-np.inf)
  return np.max(d,axis=1)
 for v in simple[begin:end]:
  cy=sorted(adj[v]);N=np.cross(X[cy[1]]-X[cy[0]],X[cy[2]]-X[cy[0]]);h=N@X[cy[0]]
  if N@X[v]<h:cy.reverse();N=-N;h=-h
  assert h>0
  oldids=[i for i,f in enumerate(r['faces']) if v not in f or len(f)>3]
  faces=[[i for i in r['faces'][f] if i!=v] for f in oldids]+[cy]
  Qbase=np.vstack((Q0[oldids],N/h));keep=[i for i in range(len(X)) if i!=v]
  tri=np.array([(f[0],f[j],f[j+1]) for f in faces for j in range(1,len(f)-1)])
  owners=[[f for f,cy0 in enumerate(faces) if i in cy0] for i in range(len(X))]
  originalU=[keep[i] for i,d in enumerate(escape(X[keep]-g0)) if d<0];badU=set(originalU)-{94}
  candidates=[f for f,cy0 in enumerate(faces) if all(len(owners[i])==3 for i in cy0) and badU<=set(cy0)]
  trials=[]
  for af in candidates:
   vs=np.array(faces[af]);others=np.array([[f for f in owners[i] if f!=af] for i in vs]);base=X.copy();last={}
   def evaluate(q):
    A=np.concatenate((np.repeat(q[None,None,:],len(vs),axis=0),Qbase[others]),axis=1)
    try:
     inv=np.linalg.inv(A);Y=base.copy();Y[vs]=inv@np.ones(3)
    except np.linalg.LinAlgError:return None
    DY=np.zeros((len(X),3,3));DY[vs]=-inv[:,:,0,None]*Y[vs,None,:]
    a,b,c=Y[tri[:,0]],Y[tri[:,1]],Y[tri[:,2]];da,db,dc=DY[tri[:,0]],DY[tri[:,1]],DY[tri[:,2]]
    vol6=np.einsum('ic,ic->i',a,np.cross(b,c))
    dv6=np.einsum('ic,icp->ip',np.cross(b,c),da)+np.einsum('ic,icp->ip',np.cross(c,a),db)+np.einsum('ic,icp->ip',np.cross(a,b),dc)
    V=vol6.sum()/6;mom=(vol6[:,None]*(a+b+c)).sum(axis=0)/24
    dm=(np.einsum('ip,ic->cp',dv6,a+b+c)+np.einsum('i,icp->cp',vol6,da+db+dc))/24
    centre=mom/V;Dg=(dm-centre[:,None]*dv6.sum(axis=0)[None,:]/6)/V
    Q=Qbase.copy();Q[af]=q;slack=1-Q@Y[keep].T
    for k,i in enumerate(keep):slack[owners[i],k]=np.inf
    return centre,Dg,Y,Q,float(slack.min()),float(vol6.min())
   q=Qbase[af].copy();trace=[];status='iteration_limit'
   for iteration in range(40):
    ev=evaluate(q)
    if ev is None:status='singular_plane_solve';break
    centre,Dg,Y,Q,slack,mindet=ev;error=float(np.linalg.norm(centre-g0))
    trace.append([iteration,error,slack,mindet])
    if error<2e-13:status='root';break
    try:step=np.linalg.solve(Dg,centre-g0)
    except np.linalg.LinAlgError:status='singular_jacobian';break
    accepted=False
    for k in range(35):
     qq=q-step/(2**k);test=evaluate(qq)
     if test is not None and test[4]>1e-12 and test[5]>1e-12 and np.linalg.norm(test[0]-g0)<(1-1e-4/(2**k))*error:
      q=qq;accepted=True;break
    if not accepted:status='geometry_or_descent_line_search_failed';break
   ev=evaluate(q)
   if ev is None:continue
   centre,Dg,Y,Q,slack,mindet=ev
   U=[keep[i] for i,d in enumerate(escape(Y[keep]-centre)) if d<0]
   poles=Q/(1-Q@centre)[:,None];S=[i for i,d in enumerate(escape(poles)) if d<0]
   trials.append(dict(actuator_face=oldids[af] if af<len(oldids) else 'ear',status=status,q=[float(a).hex() for a in q],centroid=[float(a).hex() for a in centre],error=float(np.linalg.norm(centre-g0)),slack=slack,mindet=mindet,U=U,S=S,trace=trace))
  record=dict(delete=v,old_fixed_reference_U=originalU,candidate_count=len(candidates),trials=trials,VEF=[175,175+len(faces)-2,len(faces)])
  records.append(record)
 report=dict(object='CANONICAL_C622_SINGLE_FACET_COMPENSATION_FLOAT_LOCATOR_V1_NOT_PROOF',parent_A_sha256=PIN,range=[begin,end],versions=[platform.python_version(),np.__version__,scipy.__version__],records=records)
 Path(out).write_bytes(B(report));print('FACET_ACTUATOR_FLOAT_LOCATOR_FINISHED_NOT_CERTIFICATE',len(B(report)),sha256(B(report)).hexdigest(),flush=True)
 print('SUMMARY',len(records),'trials',sum(len(r['trials']) for r in records),'roots',sum(t['status']=='root' for r in records for t in r['trials']),'US11',[(r['delete'],r['VEF'],t['actuator_face']) for r in records for t in r['trials'] if len(t['U'])==len(t['S'])==1 and t['slack']>0],flush=True)
if __name__=='__main__':
 if sys.argv[1]=='audit':assert len(sys.argv)==4;exact_audit(sys.argv[2],sys.argv[3])
 elif sys.argv[1]=='scan':assert len(sys.argv)==7;numeric_scan(sys.argv[2],sys.argv[3],sys.argv[4],int(sys.argv[5]),int(sys.argv[6]))
 else:raise ValueError('use audit A.json OUTPUT or scan A.json raw.json OUTPUT BEGIN END')
