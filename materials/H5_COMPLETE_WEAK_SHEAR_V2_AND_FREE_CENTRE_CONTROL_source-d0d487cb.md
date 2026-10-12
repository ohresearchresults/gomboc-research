# material-d0d487cbc4cf

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# H5 complete weak-stratum shear decision V2 and positive free-centre control

## Exact dependency and scope
This coordinator result extends the complete fixed-G open-cell method, proof [internal-source-reference] and literal h5_shear_cells.py in [internal-source-reference]. That source is REQUIRED:9742 bytes,SHA d4c753c4f64df7da26027452e6dcb528f690255841021c854a5a642bb0a5f89b. The literal H5 source authority remains the completely read result minimum-0250, SHA2cf87f1bc07e373e4dd87a52a48d1a91b98eb48ba17601cf28e76afe3e39c233. No additional missing atlas is required for these computations.

V2 decides U1 INCLUDING incidental weak contacts over every real shear v and eta>0, for a FIXED rational physical H5 shape and SPD tangential metric G. It is not all-G, all-H5, whole E17, or a proper110 attainment. The global interval34..622 is unchanged.

## Why only rational line strata must be added
At eta=0 use the exact allowed-exit rule: same-layer D>=0, cross-layer D>0. Every allowed arrow strictly increases projected squared norm: its increment is2D+|projected edge|_G²; same-layer projected edges are nonzero because G is SPD. Therefore this directed graph is acyclic and has a sink.

A full SPD U1 body at eta>0 gives an allowed exit at every nonroot when eta is contracted to zero. Same-layer exits do not change, and a nonnegative cross exit becomes strictly positive at eta0. The root cannot then acquire an allowed exit: that would give every vertex an exit, contradicting acyclicity. Conversely an allowed graph with exactly one sink lifts to a full SPD U1 body by choosing eta smaller than every selected positive normalized cross derivative. The root has negative same-layer and nonpositive cross derivatives at eta0, so all its full derivatives are strictly negative. Selected same-layer zeros are retained legitimately. The code checks the original full SPD derivatives and tree explicitly.

Consider the stratification of the shear plane by ONLY the twenty same-layer zero lines. On each relatively open stratum, the existence of exactly one allowed sink is a relatively OPEN property. At a feasible point choose one allowed exit at each nonroot. Same-layer signs, including zeros, are fixed on the stratum; the selected strictly positive cross derivatives persist nearby. Acyclicity still forces at least one sink, hence there remains exactly one. This is the key weak-boundary argument.

Consequently no separate sample of an irrational cross-ellipse intersection or arc is necessary. Two-dimensional strata are covered by V1. On every same-layer zero line, parameterize it rationally and cut it by all other lines and all cross ellipses: rational polynomials of degree<=2 yield exact real breakpoints, and one rational sample from each open interval covers every possible relatively open U1 set. The zero-dimensional strata are the rational intersections of pairs of same-layer lines. Cross-ellipse zeros at such points are tested as NOT allowed exits. The cap-derived finite box already excludes all U1 outside it. This exhausts the plane, including feasible configurations that exist only on same-layer weak walls. It is not a claim that weak U1 can always be perturbed to strict-escape U1.

## Executed controls
The exact original A/B/C shape/G pairs remain those literally specified in h5_shear_cells.py. V1 covered10089/15889/10287 open fiber intervals. V2 additionally checks all20 same-layer lines, with482/515/316 open line-interval samples and144/149/88 distinct rational line-intersection points. Every tested stratum has at least two allowed sinks. Thus all three fixed shape/G pairs have U>=2 for every shear and positive eta, EVEN WITH incidental weak contacts. They are still not all-G shape exclusions.
A line sink histogram {2:97,3:175,4:130,5:64,6:16}; point histogram {2:38,3:59,4:35,5:12}.
B line histogram {2:47,3:212,4:188,5:60,6:8}; point histogram {2:26,3:76,4:41,5:6}.
C line histogram {2:127,3:109,4:65,5:14,6:1}; point histogram {2:31,3:39,4:16,5:2}.

## Positive centre-binding countercontrol, NOT a homogeneous attainer
Use the parent's exact theta=(9/20,1/50,4/5,1/10,3/11) body. Actual homogeneous COM is (76658/533665,536644/2668325,14953/38812), volume9703/90750.
Instead prescribe the different interior point g_free=(1143/1250000,1960127/10000000,1/10000), shear v=(107/125,-127/1000), G=[[41415/10000,13839/10000],[13839/10000,10806/10000]], eta=116062876011/22000000. This g_free is NOT the body's uniform centroid.
All actual support inequalities place g_free strictly inside the same body. The exact full metric and its actual inverse give S={0,6}, U={8}, H={45}, no weak contacts, all68 primitives nonzero. Thus its NON-homogeneous-centre signature is(S,U,H)=(2,1,1), not110. Keeping the SAME body and metric but restoring the actual homogeneous COM gives S={1,4,6}, U={5,6,8}, H={18,49,56,67}, again no weak contacts and all68 primitives nonzero: signature(3,3,4). This isolates actual-centroid binding as essential; incidence-only or arbitrary-centre arguments cannot replace it.

The end-to-end shear decision was also run with an explicitly labelled free-centre adapter. It found a different rational U1 witness after1259 open fiber samples, root9; its full physical audit gives S={6,7},U={9},H={57},weak0. Complete fractions, M,N and all68 derivatives are reconstructed in the output JSON, not omitted checkpoint data. Both positive controls remain excluded from the homogeneous target.

## Reconstruction and pins
Save the three source blocks below under their filenames, together with the exact required h5_shear_cells.py from [internal-source-reference]. CPython3.13.5 standard library is sufficient for all acceptance/recovery commands:
python -B -S h5_shear_weak.py A
python -B -S h5_shear_weak.py B
python -B -S h5_shear_weak.py C
python -B -S h5_shear_positive_control.py
First three end H5_FIXED_G_ALL_WEAK_SHEAR_EXACT_PASS; last ends H5_FREE_CENTRE_POSITIVE_CONTROL_EXACT_PASS. These were executed by the coordinator, not a replay attributed to another author. Timing is excluded from exact JSON bytes.

Source pins:
h5_shear_weak.py4532 bytes,SHA13542139e8040d78a213e9f482c2adade89ebe0fb9f759f497d7dc9d9b5a03f3
h5_shear_positive_control.py3903 bytes,SHA0ee99a9ba4a6d60975681d01f0ed8b4334c16e697039548f79e1607db5f81091
find_free_center.py1123 bytes,SHAf8972c70d3210296401268d3cba2dc9f200294cdfb01617105dea9eedd270151

Output pins:
h5_shear_weak_A.json1368 bytes,SHA3db022b2ab545f8d67419bd07cfe2e9a68b6ec537baf0f51983d50e9b8d1f759
h5_shear_weak_B.json1318 bytes,SHAc2e6957ccf45235bea4b221bac4a1170c22a59528710621485ac9826f2754153
h5_shear_weak_C.json1351 bytes,SHA54d0381e57cea339ff8e549630c1c863bba75486b006d192bfb10b0fab697cf0
h5_shear_positive_control.json41450 bytes,SHAef1548c60076b40ecf63ab729daae6e7197f742af157a038350b038f0857bc5c

The optional discovery program find_free_center.py is preserved because it materially located the positive calibration. It uses NumPy2.3.5/SciPy1.17.0, RNG seed19, up to100 shears/metrics, with a linear program over every rooted shadow-cycle spanning path. Run OPENBLAS_NUM_THREADS=1 python find_free_center.py. Its floating output is only a proposal. The exact rational control above and exact audit below, not a floating solver pin, establish the finding.

### h5_shear_weak.py
```python
"""Complete fixed-G shear decision, including weak same-layer exits.
Requires exact h5_shear_cells.py (source pin in the companion proof).
Standard library only. No all-G or all-shape claim.
"""
from h5_shear_cells import *

def value(row,v):
 a,b,c,d,e,f=row;x,y=v
 return a*x*x+b*x*y+c*y*y+d*x+e*y+f

def line_key(row):
 q=primitive(row)
 return q if next(x for x in q if x)>0 else tuple(-x for x in q)

def analyze(z,g,G,rows,v):
 vals=[value(r,v) for r in rows]
 allowed=[(t>=0 if z[i][2]==z[j][2] else t>0) for (i,j),t in zip(ARROWS,vals)]
 sinks=[i for i in range(10) if not any(allowed[k] for k in ADJ[i])]
 assert sinks
 if len(sinks)!=1:return len(sinks),None
 tree=[];caps=[]
 for i in range(10):
  if i==sinks[0]:continue
  choices=[k for k in ADJ[i] if allowed[k]]
  k=min(choices,key=lambda k:(vals[k]<=0,k));_,j=ARROWS[k];tree.append((i,j))
  if z[i][2]!=z[j][2]:caps.append(vals[k])
 assert caps and min(caps)>0;eta=min(caps)/2
 Y=[tuple(z[i][k]-g[k]+(z[i][2]-g[2])*v[k] for k in range(2)) for i in range(10)]
 D={}
 for i,j in ARROWS:D[i,j]=bil(Y[i],G,sub(Y[j],Y[i]))+(z[i][2]-g[2])*(z[j][2]-z[i][2])*eta
 assert all(D[e]>=0 for e in tree)
 assert [i for i in range(10) if all(D[ARROWS[k]]<0 for k in ADJ[i])]==sinks
 par=dict(tree)
 for i in range(10):
  cur=i;seen=set()
  while cur!=sinks[0]:assert cur not in seen;seen.add(cur);cur=par[cur]
 return 1,{'shear':v,'eta':eta,'root':sinks[0],'weak_tree':tree,'zero_tree_arrows':[e for e in tree if D[e]==0]}

def line_parameter(A,B,C,box):
 base=(F(0),-F(C,B)) if B else (-F(C,A),F(0))
 direction=(F(1),-F(A,B)) if B else (F(0),F(1))
 lo=None;hi=None
 for b,d in zip(base,direction):
  if not d:
   if not -box<b<box:return None
   continue
  a,c=sorted(((-box-b)/d,(box-b)/d));lo=a if lo is None else max(lo,a);hi=c if hi is None else min(hi,c)
 if lo is None or hi is None or lo>=hi:return None
 return base,direction,lo,hi

def compose(row,base,direction):
 a,b,c,d,e,f=row;x,y=base;u,v=direction
 return (a*u*u+b*u*v+c*v*v,2*a*x*u+b*(x*v+y*u)+2*c*y*v+d*u+e*v,value(row,base))

def decision_full(theta,G):
 out=decision(theta,G)
 if out['witness']:
  out['identity']='H5_FIXED_G_COMPLETE_WEAK_SHEAR_DECISION_V2';out['scope']='Fixed exact shape/G; all real shear and eta>0; weak U1 allowed; a U1 witness is not automatically proper110.'
  return out
 G=tuple(tuple(map(F,r)) for r in out['normalized_G']);z,g,vol=geometry(theta);rows=polys(z,g,G);box=out['rational_shear_box']
 lines=sorted({line_key(r[3:]) for r in rows if not r[0]});points=set();witness=None
 stats={'same_layer_zero_lines':len(lines),'line_interval_samples':0,'line_sink_histogram':{},'intersection_points':0,'point_sink_histogram':{}}
 for l1,l2 in combinations(lines,2):
  A,B,C=l1;D,E,FF=l2;det=A*E-B*D
  if det:
   p=(F(B*FF-C*E,det),F(C*D-A*FF,det))
   if all(-box<t<box for t in p):points.add(p)
 for p in sorted(points):
  n,w=analyze(z,g,G,rows,p);stats['intersection_points']+=1;stats['point_sink_histogram'][n]=stats['point_sink_histogram'].get(n,0)+1
  if w:witness=w;break
 if not witness:
  for line in lines:
   param=line_parameter(*line,box)
   if param is None:continue
   base,direction,lo,hi=param;ll,hh=rat(lo),rat(hi);events=[ll,hh]
   for row in rows:
    cc=compose(row,base,direction)
    if any(cc):events+=roots(*cc)
   events=sorted_roots(t for t in events if compare(ll,t)<=0 and compare(t,hh)<=0)
   for aa,bb in zip(events,events[1:]):
    t=between(aa,bb);v=tuple(b+t*d for b,d in zip(base,direction));n,w=analyze(z,g,G,rows,v)
    stats['line_interval_samples']+=1;stats['line_sink_histogram'][n]=stats['line_sink_histogram'].get(n,0)+1
    if w:witness=w;break
   if witness:break
 out['identity']='H5_FIXED_G_COMPLETE_WEAK_SHEAR_DECISION_V2';out['scope']='Fixed exact shape and G only; every real shear and eta>0; incidental weak contacts allowed. No all-G or whole-H5 claim. A U1 witness needs a separate complete physical audit for proper110.'
 out['verdict']='EXACT_U1_WITNESS_WEAK_ALLOWED' if witness else 'NO_U1_AT_ANY_SHEAR_OR_POSITIVE_ETA_WEAK_ALLOWED';out['weak_stratum_stats']=stats;out['witness']=witness
 return out

def main():
 key=sys.argv[1] if len(sys.argv)>1 else 'A';theta,G=CONTROLS[key];out=decision_full(theta,G);out['stats'].pop('elapsed_seconds',None)
 raw=(json.dumps(enc(out),sort_keys=True,indent=2)+'\n').encode();p=Path('h5_shear_weak_'+key+'.json');p.write_bytes(raw)
 print(raw.decode());print('OUTPUT',p.name,len(raw),hashlib.sha256(raw).hexdigest());print('H5_FIXED_G_ALL_WEAK_SHEAR_EXACT_PASS')
if __name__=='__main__':main()
```

### h5_shear_positive_control.py
```python
"""Positive NON-homogeneous-centroid calibration; never an H5 attainer.
Dependencies: h5_shear_cells.py and h5_shear_weak.py, exact pinned sources.
"""
import h5_shear_cells as C
import h5_shear_weak as W
from h5_shear_cells import *
THETA=('9/20','1/50','4/5','1/10','3/11')
G=((F(41415,10000),F(13839,10000)),(F(13839,10000),F(10806,10000)))
SHEAR=(F(107,125),-F(127,1000))
ETA=F(116062876011,22000000)
FREE=(F(1143,1250000),F(1960127,10000000),F(1,10000))

def bil3(a,M,b):return sum((a[i]*M[i][j]*b[j] for i in range(3) for j in range(3)),F(0))
def portrait(z,g,G,v,eta):
 b=tuple(dot(r,v) for r in G);M=(G[0]+(b[0],),G[1]+(b[1],),(b[0],b[1],bil(v,G,v)+eta))
 det=G[0][0]*G[1][1]-G[0][1]**2;assert G[0][0]>0 and det>0 and eta>0
 GI=((G[1][1]/det,-G[0][1]/det),(-G[1][0]/det,G[0][0]/det));u=(-v[0],-v[1],F(1))
 N=tuple(tuple((GI[i][j] if i<2 and j<2 else F(0))+u[i]*u[j]/eta for j in range(3)) for i in range(3))
 assert all(sum(M[i][k]*N[k][j] for k in range(3))==int(i==j) for i in range(3) for j in range(3))
 X=[sub(a,g) for a in z];poles=[];guards=[]
 for f in FACETS:
  n=cross(sub(z[f[1]],z[f[0]]),sub(z[f[2]],z[f[0]]));h=dot(n,sub(z[f[0]],g));assert h>0;guards.append(h);poles.append(tuple(a/h for a in n))
 EF=tuple(tuple(k for k,f in enumerate(FACETS) if i in f and j in f) for i,j in EDGES)
 DA=tuple(sorted((a,b) for c,d in EF for a,b in ((c,d),(d,c))))
 P={(i,j):bil3(X[i],M,sub(X[j],X[i])) for i,j in ARROWS}
 Q={(i,j):bil3(poles[i],N,sub(poles[j],poles[i])) for i,j in DA}
 U=[i for i in range(10) if all(P[i,j]<0 for a,j in ARROWS if a==i)]
 S=[i for i in range(9) if all(Q[i,j]<0 for a,j in DA if a==i)];H=[];weak=[]
 for (i,j),(a,b) in zip(EDGES,EF):
  p=(P[i,j],P[j,i],Q[a,b],Q[b,a])
  if max(p)<0:H.append((i,j))
  if max(p)<=0 and min(map(abs,p))==0:weak.append((i,j))
 assert not weak and all(t!=0 for t in tuple(P.values())+tuple(Q.values()))
 assert len(S)+len(U)-len(H)==2
 return {'centre':g,'M':M,'N':N,'minimum_interior_support_guard':min(guards),'S':S,'U':U,'H':H,'physical_weak_points':0,'zero_primitives':0,'primal':[(i,j,P[i,j]) for i,j in ARROWS],'polar':[(i,j,Q[i,j]) for i,j in DA]}

def main():
 z,own,volume=C.geometry(THETA);assert own!=FREE
 fixed=portrait(z,FREE,G,SHEAR,ETA);true=portrait(z,own,G,SHEAR,ETA)
 assert (fixed['S'],fixed['U'],fixed['H'])==([0,6],[8],[(4,5)])
 assert (true['S'],true['U'],true['H'])==([1,4,6],[5,6,8],[(1,8),(4,9),(5,6),(6,7)])
 # Explicitly override ONLY the centre for this separate calibration run.
 # The inherited original geometry still checks all facets and computes own COM.
 oldC,oldW=C.geometry,W.geometry
 def alternate(theta):
  assert tuple(theta)==THETA
  zz,gg,V=oldC(theta)
  return zz,FREE,V
 C.geometry=W.geometry=alternate
 try:found=W.decision_full(THETA,G)
 finally:C.geometry,W.geometry=oldC,oldW
 assert found['witness'] is not None
 found['stats'].pop('elapsed_seconds',None)
 v=tuple(map(F,found['witness']['shear']));eta=F(found['witness']['eta']);GG=tuple(tuple(map(F,r)) for r in found['normalized_G'])
 recovered=portrait(z,FREE,GG,v,eta);assert len(recovered['U'])==1
 out={'identity':'H5_SHEAR_DECISION_FREE_CENTRE_POSITIVE_CONTROL_V1','scope':'NON-homogeneous-centroid countercontrol only; not a proper110 attainer. The exact same body at its true uniform COM has U=3 under the displayed seed metric.','theta':THETA,'volume':volume,'actual_uniform_centroid':own,'nonphysical_for_uniform_body_centre':FREE,'fixed_free_centre_portrait':fixed,'same_metric_actual_COM_portrait':true,'end_to_end_free_centre_decision':found,'recovered_decision_portrait':recovered}
 raw=(json.dumps(enc(out),sort_keys=True,indent=2)+'\n').encode();p=Path('h5_shear_positive_control.json');p.write_bytes(raw)
 print('OUTPUT',p.name,len(raw),hashlib.sha256(raw).hexdigest());print('RECOVERED',recovered['S'],recovered['U'],recovered['H']);print('H5_FREE_CENTRE_POSITIVE_CONTROL_EXACT_PASS')
if __name__=='__main__':main()
```

### find_free_center.py
```python
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import linprog
from h5_shear_cells import geometry, F
TH=('9/20','1/50','4/5','1/10','3/11')
z,gg,V=geometry(TH);Z=np.array(z,dtype=float)
def search(v,G):
 P=Z[:,:2]+Z[:,2,None]*v
 hull=ConvexHull(P);cy=list(hull.vertices);n=len(cy)
 # Every cycle spanning tree, rooted at every hull vertex.
 for cut in range(n):
  cyc=cy[cut+1:]+cy[:cut+1]
  for r in range(n):
   E=[]
   for j in range(n):
    if j!=r:E.append((cyc[j],cyc[j+1] if j<r else cyc[j-1]))
   AB=[];bb=[]
   for i,j in E:
    d=(P[j]-P[i])@G;AB.append([d[0],d[1],1]);bb.append(P[i]@d)
   for a,b,c in hull.equations:AB.append([a,b,1]);bb.append(-c)
   res=linprog([0,0,-1],A_ub=AB,b_ub=bb,bounds=[(None,None)]*3,method='highs')
   if res.success and res.x[2]>1e-7:return v,G,res.x,cy,E
 return None
rng=np.random.default_rng(19)
for k in range(100):
 v=np.array([-1/50,9/20]) if k==0 else rng.uniform(-1,1,2)
 U=rng.normal(size=(2,2));G=np.diag([1.,2.]) if k==0 else U.T@U+np.eye(2)*.02
 rr=search(v,G)
 if rr is not None:print('FOUND',repr(rr),flush=True);break
else:print('NONE')
```
