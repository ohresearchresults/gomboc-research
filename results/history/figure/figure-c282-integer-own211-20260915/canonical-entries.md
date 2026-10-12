
## 2026-09-15T21:02:48.655Z

### Recovery capsule part 1/2 — COORD_C282_OPPOSED_CHAIN_G1000_OWN211: exact integer monounstable body

A new coordinator-owned finite construction is **V49/E141/F94, C282, own strict(2,1,1), weak000**. Every maximal facet is a triangle. This is NOT a Gömböc or a replacement for the accepted C622 own110 record. It is a materially different small, simple-coordinate architecture with one remaining S/H pair and 169-edge headroom up to E310. It is not an alias of the Finch C182 or either C592. The complete exact definition and validation unit are below; part2 preserves the numerical production and bounded negative affine methods. Do not dispatch descendants until both parts are committed.

The starting point was the literal Finch C182_TWO_PLANE222 from fully read immutable parent asg_9_3jUNaB9fDmUrfQOxs-5B7l, SHA243b10b026bbadf9b085000d4490d02db4f2273c1836e07188b407ad662a66ee. Instead of an affine deformation trapped by the newly proved shape obstructions, two opposed radial point chains were added between its old raw-lex vertices32 and13. A three-variable fixed-point solve recomputed the actual uniform hull-volume centroid and made it coincide with the chain construction centre. Two16-link chains, bow0 and bulge0, yielded a numerical V52/E149/F99 own211 proposal; rounding ALL84 input points ties-to-even to grid1000, removing duplicates, and translating the integer-scaled body by(-14,15,272) produced81 distinct integer points. Complete exact supporting-plane enumeration and BOTH independent full auditors then found the49 extreme vertices below and own211. A cold replay from ONLY these49 listed vertices produced byte-identical raw/A/B/MASS outputs. No trigonometric, numerical root, or old sandbox is required to reconstruct this exact nonwinner.

**Exact mass and indices.** Ordinary volume=335046491/6. Own centroid=(-181946001/670092982,335691589/1340185964,-100923148/335046491). Raw first moments=(-60648667/4,335691589/24,-50461574/3). Centre by subtracting this exact centroid from every listed vertex; common centred denominator has31bits and integer numerators at most40bits. The unique unstable vertex is NEW raw-lex21=(6,0,643), not old Finch raw-lex13. Stable maximal faces28 and93, saddle true edge(14,34), all in the lexicographically sorted primitive H table generated below. All94 facets are triangles; third centred integration uses94 positive tetrahedra and yields exactly zero for all three first moments. Full audits classify all49vertices,94facets and all564 true-edge cone/projection primitives, and agree on every returned field, not only totals.

**Complete exact input.** Save the next single line as POINTS49.json, UTF-8 with NO final newline. It is776bytes, SHAc01c8c5eb79a099250ea9f2c8cf8d85a17546abe7ab2b58129a78a6df3e1aaa7. The body is the convex hull of these integer coordinates with uniform filled density.

```json
{"object":"COORD_C282_OPPOSED_CHAIN_G1000_OWN211","points":[[-507,187,93],[-503,185,-16],[-491,182,204],[-479,176,-120],[-452,168,312],[-437,160,-215],[-394,146,411],[-379,139,-297],[-316,118,498],[-308,113,-363],[-229,83,-412],[-221,83,568],[-144,52,-442],[-112,43,617],[-57,20,-453],[-41,84,59],[-40,103,-185],[-31,103,-231],[-25,99,-257],[-22,52,345],[-13,84,-311],[6,0,643],[26,-5,-438],[29,-53,-407],[30,-54,-406],[36,-68,-385],[37,-99,-122],[38,-103,-159],[38,-79,-367],[39,-105,-181],[40,-106,-214],[40,-105,-261],[40,-96,-338],[40,-95,-340],[110,-42,-441],[118,-41,616],[192,-72,-420],[221,-79,568],[269,-100,-382],[311,-113,502],[340,-126,-328],[386,-141,420],[402,-148,-259],[443,-162,327],[451,-166,-176],[482,-177,226],[485,-179,-84],[502,-184,121],[503,-185,17]]}
```

**Complete exact reconstruction/verification unit.** Save the entire following source as exact_points.py, UTF-8/LF with final newline;2031bytes, SHAe0cd67ba8ee150996c387c03cb91629dea8ce5fb1252fb1af832018cdac980db. CPython3.13.5, standard library only, assertions enabled. Its ONLY external code dependencies are the three unchanged, completely preserved FINCH3 source-capsule files: core/check_A.py(5483bytes,SHAad72cc198140249c1e52a615513354036c04f4c718333a7beed64fba4b43d7f3), core/check_B.py(6351bytes,SHAb0cb62d5486b32d020b60f717f3dfe9d07c6c9a978492928f54c3a38f396fc24), core/centred_mass.py(1398bytes,SHA5f1afafa0432436bfe953a94d94ca1027c12549504f9452491f0287c2a29d1a8). Those literal files are in the six-part FINCH3 recovery ending20:31:06 and immutable parent named above; this is an explicit durable dependency, not a request for the vanished originating sandbox.

```python
"""Complete exact supporting-plane enumeration from an integer point cloud."""
import argparse,hashlib,json,sys
from itertools import combinations
from math import gcd
from pathlib import Path
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def encoded(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def make(points):
 P=sorted(set(tuple(map(int,p)) for p in points));H=set()
 for a,b,c in combinations(P,3):
  n=cross(sub(b,a),sub(c,a))
  if n==(0,0,0):continue
  h=dot(n,a);positive=False;negative=False
  for x in P:
   z=dot(n,x)-h;positive|=z>0;negative|=z<0
   if positive and negative:break
  if positive and negative:continue
  assert positive or negative
  if positive:n=tuple(-t for t in n);h=-h
  assert h>0,'Origin must be interior; translate the input by an interior point.'
  d=gcd(*n,h);H.add(tuple(t//d for t in n)+(h//d,))
 return {'H':[list(r) for r in sorted(H)]}
def main():
 p=argparse.ArgumentParser();p.add_argument('points');p.add_argument('out');p.add_argument('--core',required=True);a=p.parse_args();out=Path(a.out);out.mkdir(parents=True,exist_ok=False)
 data=json.loads(Path(a.points).read_bytes());P=data['points'];raw=make(P);(out/'raw.json').write_bytes(encoded(raw));sys.path.insert(0,str(Path(a.core).resolve()));import check_A,check_B,centred_mass
 aa=check_A.run(raw);bb=check_B.run(raw);assert aa==bb
 pp=set(tuple(map(int,p)) for p in P);from fractions import Fraction as F
 assert all(tuple(map(F,v)) in pp for v in aa['raw_vertices'])
 for name,obj in [('A.json',aa),('B.json',bb),('MASS.json',centred_mass.run(aa))]:(out/name).write_bytes(encoded(obj))
 print('EXACT_INTEGER_POINT_HULL_AB_MASS_PASS',aa['V'],aa['E'],aa['F'],aa['counts'],aa['weak'],flush=True)
 for f in sorted(out.iterdir()):b=f.read_bytes();print(f.name,len(b),hashlib.sha256(b).hexdigest(),flush=True)
if __name__=='__main__':main()
```

Run `python -B -S exact_points.py POINTS49.json recovered282 --core finch3-source/core`, where recovered282 does not exist. Observed terminal marker: `EXACT_INTEGER_POINT_HULL_AB_MASS_PASS 49 141 94 [2, 1, 1] [0, 0, 0]`.

Reproduced outputs: raw.json2483bytes,SHA8254152f25df690b4da9ab394ab44c25041d449bfaa552272f5455c43b09c1e7; A.json and B.json each10127bytes,SHA374a1eda3378fbee5cb42d9fe11d52312215fa3a15b222768a2d5f8d2a16bbce; MASS.json216bytes,SHAc84b76eda223c2c426545c4f51b602c0e6e4d0262a72be0f069a351576dcd2a0. MASS.json literal content is {"common_centred_denominator_bits":31,"common_centred_integer_coordinate_max_bits":40,"filled_first_moments":[0,0,0],"status":"EXACT_CENTRED_INTEGER_TETRAHEDRA_PASS","tetrahedra":94,"volume_agrees_with_A_and_B":true}.

**New geometric frontier.** The physical U/H pair has actually been removed at exact own mass in a tiny-integer body; the remaining task is now the complete S/H region, not another U2 repair. Candidate mechanisms are genuine transverse body redesign, a far-enough affine metric that retains U1, or coupled physical cuts/polar escape completion with recalculated actual volume. None is yet claimed to succeed. The prior C182 affine shape certificate must not be transferred unchanged to this new body. Existing five healthy assignments remain untouched; this new exact nonwinner becomes a durable continuation source when the next capsule part is committed.

## 2026-09-15T21:06:14.339Z

### Recovery capsule part 2/2 — COORD_C282_OPPOSED_CHAIN_G1000_OWN211: complete production and bounded-search methods

This completes the capsule begun at21:02:48.655. The exact C282 integer own211 nonwinner, not an own110 record, is now durably reconstructible. The current accepted own110 benchmark remains C622. Every complete new runnable method and every checkpoint actually reused as an input are below. Dependencies: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, OPENBLAS_NUM_THREADS=1; exact audits use the unchanged FINCH3 standard-library sources identified in part1. Floating search results remain numerical proposals, not exact exclusions or alternative accepted bodies.

**Bounded results and an important correction.** The32-start five-parameter affine search on Finch C182 found no own110 or improvement over the original S2/U2. Its run-best by(S+U,loss) was S3/U2, loss1.0834090973344681e-8, physical condition23.760968394898597; other stationary outputs included S3/U3 with still smaller loss, so the loss alone must never stand for the census. The original four-step primal mixed-integer PSD outer approximation returned indefinite matrices. The strengthened four-step primal and four-step polar searches, including fixed-witness continuous PSD refinement, also produced no valid single-root metric. Time-limited solver solutions even had margins below their nominal bounds by solver feasibility tolerance; explicit positivity/PSD checks rejected them. These are bounded numerical failures, NOT a proof about the whole affine orbit.

A first single-chain exploratory classifier used an absolute unnormalized dot threshold and incorrectly omitted the exact parent's second U: its largest raw escape was about-9.109255067e-14, but its normalized escape cosine was about-2.040792828e-6. That initial classifier and its equilibrium claims are EXCLUDED. The complete corrected chain_search2.py below uses normalized signs and explicit uncertain counters; it reproduces parent S2/U2 with no uncertain feature. Its corrected60 single-chain solves found no successful own-centroid closure. Its60 opposed-chain solves had12 converged closures (all bow0); n16/bulge0 and n20/bulge0 gave numerical S2/U1, while the other converged cases retained more U. The successful n16 source has closure norm2.0798421525e-14 and V52/E149/F99 numerically. Its exact rounded descendant is the independently audited C282 body in part1.

**Input recovery.** Reconstruct Finch C182 from the already complete six-part FINCH3 capsule: call radial.reconstruct on CASES.json entry C182_TWO_PLANE222's generator, apply every entry of its `replace` dictionary to raw['H'], serialize with sorted keys and separators(',',':'), and run core/check_B.py. The required raw.json is11449bytes SHA3a3d80e75979c004f995115dd4bfb491560af0f661af0840c6868f3b5f046d86; B.json is51790bytes SHAcaf78ccee9abec82174d346227b2da7d99a13b823c88a4ef405e3e8cb9d1967d. The loader below enforces both hashes. Both are already exactly reproducible from immutable parent asg_9_3jUNaB9fDmUrfQOxs-5B7l; do not replace them with any other C182/222 object.

Place the following files in sibling directories c182_affine and c182_chain. Sources are UTF-8/LF with final newline. The part1 exact_points.py goes in c182_chain as well.

**c182_affine/affine_search.py** —4858bytes,SHAe162a2c480f6ba6185460b858343db844f172199f8ac7c5339181acd330455a4:
```python
"""Bounded whole-affine-orbit exploration of the exact Finch C182 body.
The actual filled-volume centroid transforms affinely; it is never fitted.
Floating-point proposals only. Run exact audits before accepting a body.
"""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy.optimize import minimize

def load(audit,raw):
 b=Path(audit).read_bytes();assert hashlib.sha256(b).hexdigest()=='caf78ccee9abec82174d346227b2da7d99a13b823c88a4ef405e3e8cb9d1967d';A=json.loads(b)
 b=Path(raw).read_bytes();assert hashlib.sha256(b).hexdigest()=='3a3d80e75979c004f995115dd4bfb491560af0f661af0840c6868f3b5f046d86';H=np.array(json.loads(b)['H'],float)
 g=np.array([float(F(v)) for v in A['raw_centroid']]);P=np.array([[float(F(v)) for v in p] for p in A['raw_vertices']])-g
 Q=H[A['active_input_indices'],:3];offset=H[A['active_input_indices'],3]-Q@g;Q=Q/offset[:,None]
 ep=[set() for _ in P];eq=[set() for _ in Q];edgefaces={}
 for i,j in A['edges']:ep[i].add(j);ep[j].add(i)
 for f,cy in enumerate(A['faces']):
  for i,j in zip(cy,cy[1:]+cy[:1]):edgefaces.setdefault(tuple(sorted((i,j))),[]).append(f)
 for pair in edgefaces.values():
  assert len(pair)==2;i,j=pair;eq[i].add(j);eq[j].add(i)
 w,V=np.linalg.eigh(P.T@P/len(P));W=np.diag(w**-.5)@V.T
 if np.linalg.det(W)<0:W[0]*=-1
 W/=np.linalg.det(W)**(1/3)
 return P,Q,ep,eq,W

class Escape:
 def __init__(self,X,adj):
  self.X=X;self.nei=np.array([sorted(a)+[i]*(max(map(len,adj))-len(a)) for i,a in enumerate(adj)]);self.mask=np.array([[True]*len(a)+[False]*(max(map(len,adj))-len(a)) for a in adj]);self.D=X[self.nei]-X[:,None,:]
 def evaluate(self,G,tau):
  X,D=self.X,self.D;xx=np.einsum('ni,ij,nj->n',X,G,X);dd=np.einsum('nki,ij,nkj->nk',D,G,D);xd=np.einsum('ni,ij,nkj->nk',X,G,D)
  den=np.sqrt(np.maximum(xx[:,None]*dd,1e-300));v=np.where(self.mask,xd/den,-np.inf);j=np.argmax(v,axis=1);ii=np.arange(len(X));scores=v[ii,j];root=int(np.argmin(scores));deficit=np.maximum(tau-scores,0.);deficit[root]=0
  d=D[ii,j];dd=dd[ii,j];den=den[ii,j];outer=lambda a,b:np.einsum('ni,nj->nij',a,b)
  grad=(outer(X,d)+outer(d,X))/(2*den[:,None,None])-scores[:,None,None]/2*(outer(X,X)/xx[:,None,None]+outer(d,d)/dd[:,None,None])
  return float(deficit@deficit),np.einsum('n,nij->ij',-2*deficit,grad),scores,root

def matrices(x):
 a,b=np.exp(x[0]),np.exp(x[1]);c=np.exp(-x[0]-x[1]);L=np.array([[a,x[2],x[3]],[0,b,x[4]],[0,0,c]])
 dL=np.zeros((5,3,3));dL[0,0,0]=a;dL[0,2,2]=-c;dL[1,1,1]=b;dL[1,2,2]=-c;dL[2,0,1]=1;dL[3,0,2]=1;dL[4,1,2]=1
 G=L.T@L;K=np.linalg.inv(G);dG=np.array([d.T@L+L.T@d for d in dL]);return L,G,K,dG

def main():
 p=argparse.ArgumentParser();p.add_argument('--audit',required=True);p.add_argument('--raw',required=True);p.add_argument('--out',required=True);p.add_argument('--starts',type=int,default=32);p.add_argument('--seed',type=int,default=182443);p.add_argument('--maxiter',type=int,default=250);p.add_argument('--tau',type=float,default=1e-5);a=p.parse_args()
 P,Q,ep,eq,W=load(a.audit,a.raw);pr=Escape(P@W.T,ep);du=Escape(Q@np.linalg.inv(W),eq)
 def evaluate(x,full=False):
  L,G,K,dG=matrices(x);up,ug,us,ur=pr.evaluate(G,a.tau);sp,sk,ss,sr=du.evaluate(K,a.tau);gradient=ug-K@sk@K;grad=np.einsum('ij,kij->k',gradient,dG)
  if full:return {'x':x.tolist(),'transform':(L@W).tolist(),'objective':up+sp,'S':int(sum(ss<0)),'U':int(sum(us<0)),'stable_ids':np.where(ss<0)[0].tolist(),'unstable_ids':np.where(us<0)[0].tolist(),'min_nonroot_S':float(np.min(np.delete(ss,sr))),'min_nonroot_U':float(np.min(np.delete(us,ur))),'condition':float(np.linalg.cond(L@W))}
  return up+sp,grad
 rng=np.random.default_rng(a.seed);x=np.array([.3,-.2,.1,.2,-.1]);f,grad=evaluate(x);eps=1e-6;num=np.array([(evaluate(x+eps*np.eye(5)[i])[0]-evaluate(x-eps*np.eye(5)[i])[0])/(2*eps) for i in range(5)]);assert np.max(np.abs(grad-num))<2e-6
 print('GRADIENT_CHECK',np.max(np.abs(grad-num)),flush=True)
 out=Path(a.out);out.mkdir(exist_ok=False,parents=True);rows=[];best=None
 for k in range(a.starts):
  x0=np.zeros(5) if k==0 else rng.normal(size=5)*np.array([.85,.85,1.3,1.3,1.3])
  r=minimize(evaluate,x0,jac=True,method='L-BFGS-B',bounds=[(-4,4),(-4,4),(-5,5),(-5,5),(-5,5)],options={'maxiter':a.maxiter,'maxls':60,'ftol':1e-14,'gtol':1e-9})
  t=evaluate(r.x,True);t.update(start=k,status=int(r.status),evaluations=int(r.nfev),initial=x0.tolist());rows.append(t)
  rank=(t['S']+t['U'],t['objective'])
  if best is None or rank<best[0]:best=(rank,t);(out/'BEST.json').write_text(json.dumps(t,sort_keys=True,separators=(',',':')));print('BEST',k,t['S'],t['U'],t['objective'],t['condition'],flush=True)
  (out/'SEARCH.json').write_text(json.dumps({'parameters':vars(a),'whitener':W.tolist(),'rows':rows},sort_keys=True,separators=(',',':')))
 print('C182_BOUNDED_AFFINE_SEARCH_ENDED',len(rows),'best',best[0],flush=True)
if __name__=='__main__':main()
```

**c182_affine/metric_milp.py** —4476bytes,SHA3e338a0bffc721778a3356fc27e119aa3b6c1705e5f4c6343e361ff9e993d966:
```python
"""Finite PSD outer-approximation search for a single-root escape metric.
No numerical infeasibility status is an exact mathematical exclusion.
The input audit and raw object are hash-bound by affine_search.load.
"""
import argparse,itertools,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import Bounds,LinearConstraint,milp
from scipy.sparse import coo_matrix
from affine_search import load

def form(u,v):
 return np.array([u[0]*v[0],u[1]*v[1],u[2]*v[2],u[0]*v[1]+u[1]*v[0],u[0]*v[2]+u[2]*v[0],u[1]*v[2]+u[2]*v[1]])
def matrix(g):return np.array([[g[0],g[3],g[4]],[g[3],g[1],g[5]],[g[4],g[5],g[2]]])
def main():
 p=argparse.ArgumentParser();p.add_argument('--audit',required=True);p.add_argument('--raw',required=True);p.add_argument('--out',required=True);p.add_argument('--side',choices=['primal','polar'],default='primal');p.add_argument('--steps',type=int,default=20);p.add_argument('--seconds',type=float,default=15);p.add_argument('--floor',type=float,default=1e-5);p.add_argument('--margin',type=float,default=1e-7);a=p.parse_args()
 P,Q,ep,eq,W=load(a.audit,a.raw);X=P@W.T if a.side=='primal' else Q@np.linalg.inv(W);adj=ep if a.side=='primal' else eq
 arcs=[(i,j) for i,nb in enumerate(adj) for j in sorted(nb)];C=np.array([form(X[i]/np.linalg.norm(X[i]),(X[j]-X[i])/np.linalg.norm(X[j]-X[i])) for i,j in arcs]);n=len(X);ne=len(arcs);nv=7+ne+n;tindex=nv-1
 lb=np.r_[np.zeros(3),np.full(3,-.5),np.zeros(ne+n),a.margin];ub=np.r_[np.ones(3),np.full(3,.5),np.ones(ne+n),1.]
 obj=np.zeros(nv);obj[tindex]=-1;integ=np.r_[np.zeros(6),np.ones(ne+n),0]
 rows=[];lower=[];upper=[]
 def add(dic,l,u):rows.append(dic);lower.append(l);upper.append(u)
 add({0:1,1:1,2:1},1,1)
 add({6+ne+i:1 for i in range(n)},1,1)
 for i in range(n):add({**{6+k:1 for k,(s,j) in enumerate(arcs) if s==i},6+ne+i:1},1,np.inf)
 for k,c in enumerate(C):add({**{j:v for j,v in enumerate(c)},6+k:-2,tindex:-1},-2,np.inf)
 dirs=[]
 for vv in itertools.product([-1,0,1],repeat=3):
  if not any(vv) or next(x for x in vv if x)!=1:continue
  v=np.array(vv,float);v/=np.linalg.norm(v);dirs.append(v.tolist());add(dict(enumerate(form(v,v))),a.floor,np.inf)
 out=Path(a.out);out.mkdir(parents=True,exist_ok=False);records=[]
 for step in range(a.steps):
  ii=[];jj=[];dd=[]
  for i,dic in enumerate(rows):
   for j,v in dic.items():ii.append(i);jj.append(j);dd.append(v)
  M=coo_matrix((dd,(ii,jj)),shape=(len(rows),nv)).tocsc();tic=time.monotonic()
  r=milp(obj,integrality=integ,bounds=Bounds(lb,ub),constraints=LinearConstraint(M,lower,upper),options={'time_limit':a.seconds,'mip_rel_gap':0.,'presolve':True})
  rec={'step':step,'status':int(r.status),'message':r.message,'constraint_count':len(rows),'elapsed_seconds':time.monotonic()-tic}
  if r.x is not None:
   G=matrix(r.x[:6]);vals,vec=np.linalg.eigh(G);w=C@r.x[:6];scores=np.array([max(w[k] for k,(s,j) in enumerate(arcs) if s==i) for i in range(n)]);rec.update(G=G.tolist(),eigenvalues=vals.tolist(),margin=float(r.x[tindex]),scores=scores.tolist(),negative_vertices=np.where(scores<0)[0].tolist(),selected_arcs=[list(arcs[k]) for k in range(ne) if r.x[6+k]>.5],root_variables=np.where(r.x[6+ne:6+ne+n]>.5)[0].tolist(),solver_dual_bound=None if r.mip_gap is None else float(r.mip_dual_bound),gap=None if r.mip_gap is None else float(r.mip_gap))
   for j,e in enumerate(vals):
    if e<a.floor-1e-9:
     v=vec[:,j];dirs.append(v.tolist());add(dict(enumerate(form(v,v))),a.floor,np.inf)
   if min(vals)>=a.floor-1e-9 and sum(scores<0)==1:
    L=np.linalg.cholesky(G).T;T=L@W if a.side=='primal' else np.linalg.inv(L).T@W;rec['physical_transform']=T.tolist();rec['physical_condition']=float(np.linalg.cond(T));(out/'CANDIDATE.json').write_text(json.dumps(rec,sort_keys=True,separators=(',',':')));records.append(rec);print('NUMERICAL_SINGLE_ROOT_METRIC_FOUND',step,rec['margin'],rec['negative_vertices'],rec['physical_condition'],flush=True);break
  records.append(rec);print('STEP',step,'status',r.status,'eig',rec.get('eigenvalues'),'margin',rec.get('margin'),flush=True)
  (out/'SEARCH.json').write_text(json.dumps({'parameters':vars(a),'whitener':W.tolist(),'directions':dirs,'records':records},sort_keys=True,separators=(',',':')))
  if r.x is None:break
 (out/'SEARCH.json').write_text(json.dumps({'parameters':vars(a),'whitener':W.tolist(),'directions':dirs,'records':records},sort_keys=True,separators=(',',':')))
 print('C182_METRIC_MILP_FINISHED',a.side,len(records),flush=True)
if __name__=='__main__':main()
```

**c182_affine/metric_milp2.py** —6250bytes,SHAfc984d98253a2c756e7748cd43dc211a6422cf3e9b78c2e287c796ddb58c2443:
```python
"""Finite PSD outer-approximation search for a single-root escape metric.
No numerical infeasibility status is an exact mathematical exclusion.
The input audit and raw object are hash-bound by affine_search.load.
"""
import argparse,itertools,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import Bounds,LinearConstraint,NonlinearConstraint,milp,minimize
from scipy.sparse import coo_matrix
from affine_search import load

def form(u,v):
 return np.array([u[0]*v[0],u[1]*v[1],u[2]*v[2],u[0]*v[1]+u[1]*v[0],u[0]*v[2]+u[2]*v[0],u[1]*v[2]+u[2]*v[1]])
def matrix(g):return np.array([[g[0],g[3],g[4]],[g[3],g[1],g[5]],[g[4],g[5],g[2]]])
def main():
 p=argparse.ArgumentParser();p.add_argument('--audit',required=True);p.add_argument('--raw',required=True);p.add_argument('--out',required=True);p.add_argument('--side',choices=['primal','polar'],default='primal');p.add_argument('--steps',type=int,default=20);p.add_argument('--seconds',type=float,default=15);p.add_argument('--floor',type=float,default=1e-5);p.add_argument('--margin',type=float,default=1e-7);p.add_argument('--cuts-from');a=p.parse_args()
 P,Q,ep,eq,W=load(a.audit,a.raw);X=P@W.T if a.side=='primal' else Q@np.linalg.inv(W);adj=ep if a.side=='primal' else eq
 arcs=[(i,j) for i,nb in enumerate(adj) for j in sorted(nb)];C=np.array([form(X[i]/np.linalg.norm(X[i]),(X[j]-X[i])/np.linalg.norm(X[j]-X[i])) for i,j in arcs]);n=len(X);ne=len(arcs);nv=7+ne+n;tindex=nv-1
 lb=np.r_[np.zeros(3),np.full(3,-.5),np.zeros(ne+n),a.margin];ub=np.r_[np.ones(3),np.full(3,.5),np.ones(ne+n),1.]
 obj=np.zeros(nv);obj[tindex]=-1;integ=np.r_[np.zeros(6),np.ones(ne+n),0]
 rows=[];lower=[];upper=[]
 def add(dic,l,u):rows.append(dic);lower.append(l);upper.append(u)
 add({0:1,1:1,2:1},1,1)
 add({6+ne+i:1 for i in range(n)},1,1)
 for i in range(n):add({**{6+k:1 for k,(s,j) in enumerate(arcs) if s==i},6+ne+i:1},1,np.inf)
 for k,c in enumerate(C):add({**{j:v for j,v in enumerate(c)},6+k:-2,tindex:-1},-2,np.inf)
 dirs=[]
 for vv in itertools.product([-1,0,1],repeat=3):
  if not any(vv) or next(x for x in vv if x)!=1:continue
  v=np.array(vv,float);v/=np.linalg.norm(v);dirs.append(v.tolist());add(dict(enumerate(form(v,v))),a.floor,np.inf)
 # Every true-edge difference and vertex direction also gives a valid PSD cut.
 extra=list(X)+[X[j]-X[i] for i,j in arcs]
 if a.cuts_from:extra+=json.loads(Path(a.cuts_from).read_text())['directions']
 for v in extra:
  v=np.array(v,float);v/=np.linalg.norm(v);dirs.append(v.tolist());add(dict(enumerate(form(v,v))),a.floor,np.inf)
 out=Path(a.out);out.mkdir(parents=True,exist_ok=False);records=[]
 for step in range(a.steps):
  ii=[];jj=[];dd=[]
  for i,dic in enumerate(rows):
   for j,v in dic.items():ii.append(i);jj.append(j);dd.append(v)
  M=coo_matrix((dd,(ii,jj)),shape=(len(rows),nv)).tocsc();tic=time.monotonic()
  r=milp(obj,integrality=integ,bounds=Bounds(lb,ub),constraints=LinearConstraint(M,lower,upper),options={'time_limit':a.seconds,'mip_rel_gap':0.,'presolve':True})
  rec={'step':step,'status':int(r.status),'message':r.message,'constraint_count':len(rows),'elapsed_seconds':time.monotonic()-tic}
  if r.x is not None:
   G=matrix(r.x[:6]);vals,vec=np.linalg.eigh(G);w=C@r.x[:6];scores=np.array([max(w[k] for k,(s,j) in enumerate(arcs) if s==i) for i in range(n)]);rec.update(G=G.tolist(),eigenvalues=vals.tolist(),margin=float(r.x[tindex]),scores=scores.tolist(),negative_vertices=np.where(scores<0)[0].tolist(),selected_arcs=[list(arcs[k]) for k in range(ne) if r.x[6+k]>.5],root_variables=np.where(r.x[6+ne:6+ne+n]>.5)[0].tolist(),solver_dual_bound=None if r.mip_gap is None else float(r.mip_dual_bound),gap=None if r.mip_gap is None else float(r.mip_gap))
   # With witnesses fixed, solve the convex continuous PSD problem in seven variables.
   chosen=np.where(r.x[6:6+ne]>.5)[0];CC=C[chosen]
   def eigfun(z):return np.linalg.eigvalsh(matrix(z[:6]))
   def eigjac(z):
    _,v=np.linalg.eigh(matrix(z[:6]));return np.array([np.r_[form(v[:,j],v[:,j]),0] for j in range(3)])
   constraints=[LinearConstraint(np.array([[1,1,1,0,0,0,0]]),1,1),LinearConstraint(np.c_[CC,-np.ones(len(CC))],0,np.inf),NonlinearConstraint(eigfun,a.floor,np.inf,jac=eigjac)]
   zz=np.r_[np.array([1/3,1/3,1/3,0,0,0]),0.]
   rr=minimize(lambda z:-z[6],zz,jac=lambda z:np.r_[np.zeros(6),-1],method='SLSQP',bounds=Bounds(np.r_[np.zeros(3),np.full(3,-.5),-1.],np.r_[np.ones(3),np.full(3,.5),1.]),constraints=constraints,options={'maxiter':300,'ftol':1e-12})
   GG=matrix(rr.x[:6]);ww=C@rr.x[:6];sss=np.array([max(ww[k] for k,(s,j) in enumerate(arcs) if s==i) for i in range(n)])
   rec['fixed_witness_sdp']={'status':int(rr.status),'margin':float(rr.x[6]),'G':GG.tolist(),'eigenvalues':np.linalg.eigvalsh(GG).tolist(),'negative_vertices':np.where(sss<0)[0].tolist(),'minimum_selected_slack':float(min(CC@rr.x[:6]-rr.x[6]))}
   if min(np.linalg.eigvalsh(GG))>=a.floor-1e-9 and rr.x[6]>a.margin and min(CC@rr.x[:6])>=a.margin/2 and sum(sss<0)==1:
    G=GG;vals,vec=np.linalg.eigh(G);scores=sss;rec['refined']=True
   for j,e in enumerate(vals):
    if e<a.floor-1e-9:
     v=vec[:,j];dirs.append(v.tolist());add(dict(enumerate(form(v,v))),a.floor,np.inf)
   if min(vals)>=a.floor-1e-9 and sum(scores<0)==1 and min(np.delete(scores,np.argmin(scores)))>a.margin/2:
    L=np.linalg.cholesky(G).T;T=L@W if a.side=='primal' else np.linalg.inv(L).T@W;rec['physical_transform']=T.tolist();rec['physical_condition']=float(np.linalg.cond(T));(out/'CANDIDATE.json').write_text(json.dumps(rec,sort_keys=True,separators=(',',':')));records.append(rec);print('NUMERICAL_SINGLE_ROOT_METRIC_FOUND',step,rec['margin'],rec['negative_vertices'],rec['physical_condition'],flush=True);break
  records.append(rec);print('STEP',step,'status',r.status,'eig',rec.get('eigenvalues'),'margin',rec.get('margin'),flush=True)
  (out/'SEARCH.json').write_text(json.dumps({'parameters':vars(a),'whitener':W.tolist(),'directions':dirs,'records':records},sort_keys=True,separators=(',',':')))
  if r.x is None:break
 (out/'SEARCH.json').write_text(json.dumps({'parameters':vars(a),'whitener':W.tolist(),'directions':dirs,'records':records},sort_keys=True,separators=(',',':')))
 print('C182_METRIC_MILP_FINISHED',a.side,len(records),flush=True)
if __name__=='__main__':main()
```

The only intermediate mixed-integer checkpoint consumed by a later search was the list of PSD cut directions from the first four steps. The strengthened code reads ONLY the `directions` key. Its complete minimal equivalent input CUTS.json is869bytes,SHA6445be4d8103d0409f34238510d5f9f04584e86ade306f099439ada869cb681a, UTF-8 without final newline:
```json
{"directions":[[0.0,0.0,1.0],[0.0,0.7071067811865475,-0.7071067811865475],[0.0,1.0,0.0],[0.0,0.7071067811865475,0.7071067811865475],[0.5773502691896258,-0.5773502691896258,-0.5773502691896258],[0.7071067811865475,-0.7071067811865475,0.0],[0.5773502691896258,-0.5773502691896258,0.5773502691896258],[0.7071067811865475,0.0,-0.7071067811865475],[1.0,0.0,0.0],[0.7071067811865475,0.0,0.7071067811865475],[0.5773502691896258,0.5773502691896258,-0.5773502691896258],[0.7071067811865475,0.7071067811865475,0.0],[0.5773502691896258,0.5773502691896258,0.5773502691896258],[-0.5199079020069671,-0.8142629806494337,0.258208388273142],[0.4546284603417234,-0.8061913095470933,-0.3786403774798154],[0.8809923343763272,0.4695592864344325,0.05802226549641489],[-0.30427994970969335,0.9182431148159959,-0.2534626092694628],[0.9454340876986054,-0.1023516749993556,-0.3093194472423815]]}
```

**c182_chain/chain_search2.py** —4090bytes,SHAbfdf1c1ff606b69df6888aa56d836d56e03842a155ba9dc24e8bafd9a7ad47e1:
```python
"""Finite point-chain completion with its own actual hull-volume centroid.
Numerical candidates only; the exact parent raw/audit hashes are enforced.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import root
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'c182_affine'))
from affine_search import load

def mass(P):
 h=ConvexHull(P);tri=h.simplices;anchor=P[h.vertices].mean(axis=0);A=P[tri]-anchor
 determinant=np.einsum('ni,ni->n',A[:,0],np.cross(A[:,1],A[:,2]));sgn=np.sign(np.einsum('ni,ni->n',np.cross(A[:,1]-A[:,0],A[:,2]-A[:,0]),h.equations[:,:3]));determinant*=sgn
 assert min(determinant)>0
 vol=determinant.sum()/6;g=anchor+np.einsum('n,ni->i',determinant,A.sum(axis=1))/(4*determinant.sum());return vol,g,h

def census(P):
 vol,g,h=mass(P);X=P-g
 # A positive escape to any point implies one along some true incident edge.
 U=[];um=[]
 for i in h.vertices:
  D=P-P[i];values=(X[i]@D.T)/np.maximum(np.linalg.norm(X[i])*np.linalg.norm(D,axis=1),1e-300);values[i]=-np.inf;mx=max(values);um.append(mx)
  if mx<-1e-10:U.append(int(i))
 # Distinct supporting planes of maximal facets are enough for the dual test.
 ns=h.equations[:,:3];bs=-h.equations[:,3]-ns@g;Q=ns/bs[:,None];ids=[]
 for i,q in enumerate(Q):
  if all(np.linalg.norm(q-Q[j])>1e-7*max(1,np.linalg.norm(q)) for j in ids):ids.append(i)
 Q=Q[ids];S=[];sm=[]
 for i,q in enumerate(Q):
  D=Q-q;vals=(q@D.T)/np.maximum(np.linalg.norm(q)*np.linalg.norm(D,axis=1),1e-300);vals[i]=-np.inf;mx=max(vals);sm.append(mx)
  if mx<-1e-10:S.append(i)
 return {'volume':float(vol),'centroid':g.tolist(),'V_qhull':len(h.vertices),'F_grouped':len(Q),'E_euler_proposal':len(h.vertices)+len(Q)-2,'S':len(S),'U':len(U),'unstable_input':U,'stable_grouped':S,'minimum_primal_max_escape':float(min(um)),'minimum_polar_max_escape':float(min(sm)),'uncertain_primal':int(sum(abs(t)<=1e-10 for t in um)),'uncertain_polar':int(sum(abs(t)<=1e-10 for t in sm))}

def chain(P,c,n,bow,bulge,opposed=False):
 a=P[32]-c;b=P[13]-c;ra=np.linalg.norm(a);rb=np.linalg.norm(b);u=a/ra;v=b/rb;phi=np.arccos(np.clip(u@v,-1,1));w=np.cross(u,v);w/=np.linalg.norm(w)
 t=np.arange(1,n)/n;e=(v-(u@v)*u)/np.sin(phi);out=[]
 for angle in ([phi,phi-2*np.pi] if opposed else [phi]):
  dirs=np.cos(t*angle)[:,None]*u+np.sin(t*angle)[:,None]*e;dirs+=bow*np.sin(np.pi*t)[:,None]*w;dirs/=np.linalg.norm(dirs,axis=1)[:,None]
  radius=ra*(rb/ra)**t*np.exp(bulge*np.sin(np.pi*t)**2);out.append(c+radius[:,None]*dirs)
 return np.concatenate(out)

def main():
 p=argparse.ArgumentParser();p.add_argument('--audit',required=True);p.add_argument('--raw',required=True);p.add_argument('--out',required=True);p.add_argument('--opposed',action='store_true');a=p.parse_args()
 # load returns centred points; uniform translations do not change equilibria.
 P,Q,ep,eq,W=load(a.audit,a.raw);out=Path(a.out);out.mkdir(exist_ok=False,parents=True);rows=[];best=None
 print('PARENT',census(P),flush=True)
 for n in [9,12,16,20]:
  for bow in [-2.,-1.,0.,1.,2.]:
   for bulge in [-.2,0.,.2]:
    def fun(c):return mass(np.r_[P,chain(P,c,n,bow,bulge,a.opposed)])[1]-c
    sol=root(fun,np.zeros(3),method='hybr',options={'xtol':1e-10,'maxfev':150});c=sol.x;Z=chain(P,c,n,bow,bulge,a.opposed);Y=np.r_[P,Z];res=census(Y);res.update(n=n,bow=bow,bulge=bulge,chart_centre=c.tolist(),fixed_point_error=float(np.linalg.norm(fun(c))),root_status=int(sol.status),evaluations=int(sol.nfev));rows.append(res)
    rank=(res['S']+res['U'],res['E_euler_proposal'])
    if best is None or rank<best[0]:
     best=(rank,res);(out/'BEST.json').write_text(json.dumps({'record':res,'added_points_in_parent_centred_coordinates':Z.tolist()},sort_keys=True,separators=(',',':')));print('BEST',rank,'n,bow,bulge',n,bow,bulge,'SU',res['S'],res['U'],'closure',res['fixed_point_error'],flush=True)
    (out/'SEARCH.json').write_text(json.dumps({'parameters':vars(a),'records':rows},sort_keys=True,separators=(',',':')))
 print('C182_CHAIN_FIXED_CENTRE_SEARCH_ENDED',len(rows),best[0],flush=True)
if __name__=='__main__':main()
```

**c182_chain/produce282.py** —1748bytes,SHAa9b3f3f3d0be38227a5ff34197547488954f54d7f3303ae12dc25214c5ae88e7. This is the smallest complete deterministic production replay for the exact object, without the irrelevant other59 starts. It was actually cold-run and produced the identical776-byte POINTS49.json from part1:
```python
"""Reproduce the integer C282 checkpoint from the exact Finch C182 input."""
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy.optimize import root
import chain_search2 as m
from exact_points import make,encoded

def main():
 p=argparse.ArgumentParser();p.add_argument('--audit',required=True);p.add_argument('--raw',required=True);p.add_argument('--core',required=True);p.add_argument('--out',required=True);a=p.parse_args()
 P,Q,ep,eq,W=m.load(a.audit,a.raw)
 def fun(c):return m.mass(np.r_[P,m.chain(P,c,16,0.,0.,True)])[1]-c
 sol=root(fun,np.zeros(3),method='hybr',options={'xtol':1e-10,'maxfev':150});assert sol.status==1 and np.linalg.norm(fun(sol.x))<1e-10
 A=json.loads(Path(a.audit).read_bytes());g=np.array([float(F(x)) for x in A['raw_centroid']]);rawP=np.array([[float(F(x)) for x in row] for row in A['raw_vertices']]);Z=m.chain(P,sol.x,16,0.,0.,True)+g
 I=np.unique(np.rint(np.r_[rawP,Z]*1000).astype(np.int64),axis=0)-[-14,15,272]
 sys.path.insert(0,str(Path(a.core).resolve()));import check_B
 B=check_B.run(make(I.tolist()));assert [B['V'],B['E'],B['F'],*B['counts'],*B['weak']]==[49,141,94,2,1,1,0,0,0]
 V=[[int(F(x)) for x in row] for row in B['raw_vertices']];assert all(F(x).denominator==1 for row in B['raw_vertices'] for x in row)
 b=encoded({'object':'COORD_C282_OPPOSED_CHAIN_G1000_OWN211','points':V});assert len(b)==776 and hashlib.sha256(b).hexdigest()=='c01c8c5eb79a099250ea9f2c8cf8d85a17546abe7ab2b58129a78a6df3e1aaa7'
 out=Path(a.out);out.mkdir(parents=True,exist_ok=False);(out/'POINTS49.json').write_bytes(b)
 print('C282_SOURCE_ONLY_NUMERICAL_PRODUCTION_TO_EXACT_INTEGER_INPUT_PASS',len(I),len(V),flush=True)
if __name__=='__main__':main()
```

**Exact commands and finite domains.** In the following commands `c182/B.json`, `c182/raw.json` and `finch3-source/core` mean the recovered exact dependencies, not inaccessible old paths; all output directories must be absent.

`OPENBLAS_NUM_THREADS=1 python c182_chain/produce282.py --audit c182/B.json --raw c182/raw.json --core finch3-source/core --out production282` observed `C282_SOURCE_ONLY_NUMERICAL_PRODUCTION_TO_EXACT_INTEGER_INPUT_PASS 81 49`. Then run the part1 exact_points command on production282/POINTS49.json for both complete independent audits and third integration. Both production-input hashes and all four exact output hashes are those in part1.

`OPENBLAS_NUM_THREADS=1 python c182_chain/chain_search2.py --audit c182/B.json --raw c182/raw.json --out opposed60 --opposed` observed `C182_CHAIN_FIXED_CENTRE_SEARCH_ENDED 60 (3, 149)`. The same command without --opposed observed `... 60 (4, 91)` and no successful chart-centroid closure. The numerical candidate at C298 is not an exact retained endpoint; use exact C282 instead. It survives all-point rounding at powers10^3 through10^9 numerically as own211, whereas10^2 gives S2/U14. Only grid1000 has been promoted after exact checks here.

`OPENBLAS_NUM_THREADS=1 python c182_affine/affine_search.py --audit c182/B.json --raw c182/raw.json --out affine32 --starts 32 --seed 182443 --maxiter 250 --tau 0.00001` observed gradient finite-difference discrepancy9.415751511809844e-11 and `C182_BOUNDED_AFFINE_SEARCH_ENDED 32 best (5, 1.0834090973344681e-08)`. This does not beat the original Finch222 census.

`OPENBLAS_NUM_THREADS=1 python c182_affine/metric_milp.py --audit c182/B.json --raw c182/raw.json --out mip1 --side primal --steps 4 --seconds 6 --floor 0.00001 --margin 0.0000001` observed `C182_METRIC_MILP_FINISHED primal 4`, no valid candidate. The exact reused cut list is fully literal above, so the next command does not depend on reproducing wall-clock-limited solver branch choices.

`OPENBLAS_NUM_THREADS=1 python c182_affine/metric_milp2.py --audit c182/B.json --raw c182/raw.json --out mip2 --side primal --steps 4 --seconds 5 --floor 0.00001 --margin 0.0000001 --cuts-from c182_affine/CUTS.json` and the same strengthened program with --side polar and WITHOUT --cuts-from both observed four-step end markers without a valid single-root metric. Time-limited search transcripts are not exact mathematical endpoints and their matrices/statuses are not used as proofs. No claim of full-orbit impossibility follows.

No recovery debt remains for the exact C282 nonwinner or the material methods used to produce it: its49 integer vertices alone define it, the complete source-only production is reproduced, and both independent full audits and centered integration match after cold49 replay. Earlier PM580 numerical-method preservation debt remains separate.
