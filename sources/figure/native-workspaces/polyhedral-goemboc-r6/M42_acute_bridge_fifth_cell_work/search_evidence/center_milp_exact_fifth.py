from __future__ import annotations
import sys,math,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
sys.path.insert(0,str(Path(__file__).parent))
from numeric_hull_proposer import evaluate
import csv
pall={}
for z in csv.DictReader(open('/mnt/data/M42_acute_bridge_fifth_cell_exact/input_rows_common_lattice.csv')):
 D=int(z['denominator']); pall[int(z['source_id'])]=np.array([int(z[k])/D for k in ('x_int','y_int','z_int')],float)
rfull=evaluate(pall,plane_tol=1e-8,strict_tol=1e-10); assert rfull.valid
pts={i:pall[i] for i in rfull.active};r=evaluate(pts,plane_tol=1e-8,strict_tol=1e-10);assert r.valid
ids=sorted(pts);P=np.array([pts[i] for i in ids]);id2={i:k for k,i in enumerate(ids)};lo=P.min(0);hi=P.max(0)
def aff(fn):
 b=float(fn(np.zeros(3)));a=np.array([fn(np.eye(3)[k])-b for k in range(3)],float);return a,b
def scale(a,b):
 vals=[]
 for m in range(8):
  c=np.array([hi[k] if m>>k&1 else lo[k] for k in range(3)]);vals.append(abs(a@c+b))
 s=max(vals+[1e-12]);return a/s,b/s
features=[]
for fi,f in enumerate(r.faces):
 cyc=f['cycle_local'];n=f['n'];ref=P[cyc].mean(0);forms=[]
 for ia,ib in zip(cyc,cyc[1:]+cyc[:1]):
  e=P[ib]-P[ia];el=np.linalg.norm(e);sg=1 if np.dot(np.cross(e,ref-P[ia]),n)>=0 else -1
  def fn(c,ia=ia,e=e,el=el,sg=sg,n=n,off=f['off']):
   foot=c-(n@c+off)*n;return sg*np.dot(np.cross(e,foot-P[ia]),n)/el
  forms.append(scale(*aff(fn)))
 features.append(('face',fi,forms))
for i in r.active:
 ii=id2[i];forms=[]
 for j in sorted(r.neighbors[i]):
  jj=id2[j];d=P[jj]-P[ii];dl=np.linalg.norm(d);forms.append(scale(d/dl,-P[ii]@d/dl))
 features.append(('vertex',i,forms))
for e,inc in r.edge_faces.items():
 ia=id2[e[0]];ib=id2[e[1]];pa=P[ia];pb=P[ib];d=pb-pa;dd=d@d;n1=r.faces[inc[0]]['n'];n2=r.faces[inc[1]]['n'];aa=n1@n1;bb=n1@n2;cc=n2@n2;den=aa*cc-bb*bb
 def comps(c):
  x=pa-c;t=-(x@d)/dd;p=x+t*d;r1=p@n1;r2=p@n2;l1=(r1*cc-r2*bb)/den;l2=(r2*aa-r1*bb)/den;return [t,1-t,l1,l2]
 forms=[]
 for k in range(4):forms.append(scale(*aff(lambda c,k=k:comps(c)[k])))
 features.append(('edge',tuple(e),forms))
inside=[scale(-f['n'],-f['off']) for f in r.faces]
tf=next(i for i,f in enumerate(r.faces) if set(f['cycle'])==set(range(17)))
bins=[]
for kind,label,forms in features:
 target=(kind=='face' and label==tf) or (kind=='vertex' and label==8)
 if not target:
  bins += [(kind,label,k) for k in range(len(forms))]
idx={z:4+i for i,z in enumerate(bins)};n=4+len(bins);rows=[];lbs=[];ubs=[]
def add(co,l,u):rows.append(co);lbs.append(l);ubs.append(u)
for kind,label,forms in features:
 target=(kind=='face' and label==tf) or (kind=='vertex' and label==8)
 if target:
  for a,b in forms:
   co=np.zeros(n);co[:3]=a;co[3]=-1;add(co,-b,np.inf)
 else:
  zs=[]
  for k,(a,b) in enumerate(forms):
   j=idx[(kind,label,k)];zs.append(j);co=np.zeros(n);co[:3]=a;co[3]=1;co[j]=2.5;add(co,-np.inf,2.5-b)
  co=np.zeros(n);co[zs]=1;add(co,1,np.inf)
for a,b in inside:
 co=np.zeros(n);co[:3]=a;co[3]=-1;add(co,-b,np.inf)
A=np.array(rows);print('fvec',len(r.active),len(r.edges),len(r.faces),'class',len(r.stable),len(r.unstable),len(r.saddles),'vars',n,'bins',len(bins),'cons',len(rows))
out=milp(np.r_[np.zeros(3),-1,np.zeros(len(bins))],integrality=np.r_[np.zeros(4,dtype=int),np.ones(len(bins),dtype=int)],bounds=Bounds(np.r_[lo,0,np.zeros(len(bins))],np.r_[hi,.2,np.ones(len(bins))]),constraints=LinearConstraint(A,np.array(lbs),np.array(ubs)),options={'time_limit':600,'mip_rel_gap':1e-9,'disp':True})
print(out.status,out.message,out.fun,out.x[:4] if out.x is not None else None,getattr(out,'mip_gap',None))
if out.x is not None:json.dump({'center':out.x[:3].tolist(),'eps':out.x[3],'status':out.status,'message':out.message},open('/mnt/data/m42_fifth_search/center_milp_exact_fifth_result.json','w'),indent=2)
