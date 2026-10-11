"""Centroid closure using parallel offsets away from a literal new cap.

Only old facets whose vertices are all simple and avoid the cap horizon may
move. Each affected vertex is affine in the selected plane offsets. Existing
nonsimple vertices and the entire cap remain exact contact constraints.
The full uniform mass, all noncontacts and all reference/own counts are read
back after every accepted step. Exact final halfspaces define the real body.
"""
import argparse,json,time,hashlib
from pathlib import Path
from math import gcd,lcm
import numpy as np
from scipy.optimize import linprog
from scipy.linalg import svd
from scipy.sparse import csr_matrix,eye,hstack,vstack
from gmpy2 import mpq
from polyhedral_stable_cap import Cap
from section_polish import roots
from support_geometry import escape
from persistence_birth import bars_loss
from exact_audit_vertices import check_B,dot,cross,sub
from exact_projective_audit import inverse,apply
from exact_barcode_report import report

class SafeCap:
 def __init__(self,cap,g):
  self.cap=cap;self.base=g;self.faces=g['faces'];self.X0=g['X'];self.F=g['F'];self.V=g['V'];self.inc=np.zeros((self.F,self.V),bool)
  for f,cy in enumerate(self.faces):self.inc[f,cy]=True
  horizon={i for f,cy in enumerate(self.faces)if g['face_sources'][f]['type']=='cap'for i in cy};degree=self.inc.sum(0);self.safe=[f for f,cy in enumerate(self.faces)if g['face_sources'][f]['type']=='old'and all(degree[i]==3 and i not in horizon for i in cy)];self.d=len(self.safe)+3;assert self.d>=6;self.q0=np.zeros(self.d);Y=g['H']/(1+g['H']@g['centroid'])[:,None];self.DX=np.zeros((self.V,3,self.d));assert g['active_point_ids'][-1]==len(cap.X);self.DX[-1,:,:3]=np.eye(3)
  for i in range(self.V):
   adj=np.flatnonzero(self.inc[:,i]);selected=[(j,f)for j,f in enumerate(self.safe)if f in adj]
   if not selected:continue
   assert len(adj)==3 and i not in horizon;I=np.linalg.inv(Y[adj])
   for j,f in selected:self.DX[i,:,j+3]=I[:,list(adj).index(f)]
  self.T=np.array([(cy[0],cy[k],cy[k+1])for cy in self.faces for k in range(1,len(cy)-1)]);reps=[]
  for cy in self.faces:
   a=cy[0];j=max(cy,key=lambda i:np.linalg.norm(self.X0[i]-self.X0[a]));k=max(cy,key=lambda i:np.linalg.norm(np.cross(self.X0[j]-self.X0[a],self.X0[i]-self.X0[a])));reps.append([a,j,k])
  self.reps=np.array(reps)
 def physical(self,q):
  X=self.X0+np.einsum('icp,p->ic',self.DX,q);Y=np.linalg.solve(X[self.reps],np.ones((self.F,3,1)))[:,:,0];DY=np.linalg.solve(X[self.reps],-np.einsum('fc,facp->fap',Y,self.DX[self.reps]));gap=1-Y@X.T;non=gap[~self.inc];contact=float(max(abs(gap[self.inc])));Dgap=-(np.einsum('fcp,vc->fvp',DY,X)+np.einsum('fc,vcp->fvp',Y,self.DX));a,b,c=X[self.T[:,0]],X[self.T[:,1]],X[self.T[:,2]];da,db,dc=self.DX[self.T[:,0]],self.DX[self.T[:,1]],self.DX[self.T[:,2]];v6=np.einsum('ic,ic->i',a,np.cross(b,c));vol=v6.sum()/6;centre=np.sum(v6[:,None]*(a+b+c),axis=0)/(4*v6.sum());dv=np.einsum('ic,icp->ip',np.cross(b,c),da)+np.einsum('ic,icp->ip',np.cross(c,a),db)+np.einsum('ic,icp->ip',np.cross(a,b),dc);Dg=(np.einsum('ip,ic->cp',dv,a+b+c-4*centre)+np.einsum('i,icp->cp',v6,da+db+dc))/(4*v6.sum());valid=min(non)>0 and contact<1e-8 and min(v6)>0 and vol>0
  if not valid:raise ValueError('safe-offset contact realization is not convex and strict')
  den=1-Y@centre;assert min(den)>0;H=Y/den[:,None];Z=X-centre;P=bars_loss(Z,self.base['pe'],.03)[2];Q=bars_loss(H,self.base['qe'],.03)[2];return dict(X=X,Y=Y,DY=DY,g=centre,Dg=Dg,noncontact=non,Dgap=Dgap[~self.inc],reference_S=int(np.sum(escape(Y)[0]<0)),reference_U=int(np.sum(escape(X)[0]<0)),S=int(np.sum(escape(H)[0]<0)),U=int(np.sum(escape(Z)[0]<0)),P=max(P,default=0.),Q=max(Q,default=0.),Q_bars=Q,volume=vol,contact_error=contact)
 def guards(self,g,stable_quota=2):
  vals=[];Js=[]
  for A,DA,r in [(g['X'],self.DX,[int(np.argmax(np.sum(g['X']**2,axis=1)))]),(g['Y'],g['DY'],roots(g['Y'],self.base['qe'],stable_quota))]:
   v,w,J=escape(A,DA,angular=True);keep=np.ones(len(A),bool);keep[r]=False;vals.append(v[keep]);Js.append(J[keep])
  return np.r_[tuple(vals)],np.vstack(Js)

def freeze(c,q,out):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);cap=c.cap;g=c.base;a=cap.a;centre=[mpq(float(v))for v in cap.g0];scale=mpq(float(cap.scale));P=[tuple((mpq(v)-centre[k])/scale for k,v in enumerate(x))for x in a['raw_vertices']];pp=c.X0[-1]+q[:3];point=tuple(mpq(float(v))for v in pp);old=[(tuple(mpq(v)*scale for v in n),mpq(h)-sum(mpq(v)*cc for v,cc in zip(n,centre)))for n,h in zip(a['normals'],a['offsets'])];planes=[];offs={f:mpq(float(q[j+3]))for j,f in enumerate(c.safe)}
 for f,desc in enumerate(g['face_sources']):
  if desc['type']=='old':n,h=old[desc['index']]
  else:
   i,j=desc['edge'];n=cross(sub(P[j],P[i]),sub(point,P[i]));h=dot(n,P[i]);assert h!=0
   if h<0:n=tuple(-v for v in n);h=-h
  if f in offs:h*=1+offs[f]
  planes.append((n,h))
 expected=[(P+[point])[i]for i in g['active_point_ids']]
 for i in range(c.V):
  adj=np.flatnonzero(c.inc[:,i])
  if any(f in offs for f in adj):assert len(adj)==3;expected[i]=apply(inverse([planes[j][0]for j in adj]),[planes[j][1]for j in adj])
 rows=[]
 for n,h in planes:
  v=(*n,h);D=lcm(*(int(x.denominator)for x in v));r=[int(x*D)for x in v];common=gcd(*r);rows.append([x//common for x in r])
 B=lambda x:json.dumps(x,default=str,sort_keys=True,separators=(',',':')).encode();raw=dict(H=rows);(out/'raw.json').write_bytes(B(raw));(out/'coordinates.json').write_bytes(B(dict(points=expected,density=1)));(out/'construction.json').write_bytes(B(dict(source=str(cap.source.resolve()),source_audit_sha256=hashlib.sha256((cap.source/'audit.json').read_bytes()).hexdigest(),frame_centre=centre,frame_scale=scale,point=point,safe_facets=c.safe,offsets=offs,face_sources=g['face_sources'],formula='exact affine source planes and literal cap planes; named safe planes have their offsets multiplied by1+the saved exact dyadic offset; uniform density1')))
 for f,(n,h)in enumerate(planes):
  for i,x in enumerate(expected):assert (h-dot(n,x)==0 if c.inc[f,i]else h-dot(n,x)>0),'exact incidence or convexity failure'
 a=check_B.run(raw);assert {tuple(mpq(v)for v in x)for x in a['raw_vertices']}==set(expected);assert [a[k]for k in ['V','E','F']]==[g[k]for k in ['V','E','F']];(out/'audit.json').write_bytes(B(a));s={k:a[k]for k in ['V','E','F','counts','weak','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};s.update(C_2E=2*a['E'],VplusEplusF=a['V']+a['E']+a['F'],goal_met=a['counts']==[1,1,0]and a['weak']==[0,0,0]and 34<=2*a['E']<500 and a['V']+a['E']+a['F']<500,audit_sha256=hashlib.sha256((out/'audit.json').read_bytes()).hexdigest());(out/'summary.json').write_text(json.dumps(s,indent=2));report(out);print('EXACT_SAFE_OFFSET_CAP',out,s,flush=True)
 if s['goal_met']:
  from goal_nomination import ExactGoalCandidateFound
  raise ExactGoalCandidateFound('Exact Figure candidate at '+str(out))
 return s

def close(c,out,steps=120,move_apex=False):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);q=c.q0.copy();trace=[];trust=.05;start=time.time();quota=2
 for it in range(steps):
  g=c.physical(q);norm=float(np.linalg.norm(g['g']));v,J=c.guards(g,quota);row=dict(it=it,mass_norm=norm,reference_S=g['reference_S'],reference_U=g['reference_U'],S=g['S'],U=g['U'],Q=g['Q'],P=g['P'],guard=float(min(v)),gap=float(min(g['noncontact'])),trust=trust,seconds=time.time()-start);trace.append(row);np.save(out/'latest_q.npy',q);(out/'trace.json').write_text(json.dumps(trace,indent=2))
  if it%10==0:print('SAFE_OFFSET_MASS',out,row,flush=True)
  if g['S']==g['U']==1:freeze(c,q,out/f'exact_goal_it{it}')
  if norm<1e-13:
   np.save(out/'closed_q.npy',q);return q,g
  quota=min(quota,g['reference_S']);cols=np.arange(0 if move_apex else 3,c.d);sx=np.sqrt(np.mean(g['X']**2));sy=np.sqrt(np.mean(g['Y']**2));M=np.vstack((c.DX[:,:,cols].reshape(-1,len(cols))/sx,g['DY'][:,:,cols].reshape(-1,len(cols))/sy,.01*np.eye(len(cols))));_,sv,V=svd(M,full_matrices=False,check_finite=False);W=V.T/sv;d=len(cols);vv=np.r_[g['noncontact'],v];JJ=np.vstack((g['Dgap'][:,cols],J[:,cols]))@W;target=np.r_[np.minimum(g['noncontact']*.9,1e-9),np.minimum(v*.9,1e-8)];bound=trust/np.sqrt(d);rhs=vv-target;keep=rhs<=bound*np.sum(abs(JJ),axis=1)+1e-10;I=eye(d);A=vstack([hstack([-csr_matrix(JJ[keep]),csr_matrix((int(sum(keep)),1+d))]),hstack([I,csr_matrix((d,1)),-I]),hstack([-I,csr_matrix((d,1)),-I])],format='csr');b=np.r_[rhs[keep],np.zeros(2*d)];ms=1e5;AE=hstack([csr_matrix(ms*g['Dg'][:,cols]@W),csr_matrix((ms*g['g'])[:,None]),csr_matrix((3,d))],format='csr');r=linprog(np.r_[np.zeros(d),-1.,np.full(d,1e-6)],A_ub=A,b_ub=b,A_eq=AE,b_eq=np.zeros(3),bounds=[(-bound,bound)]*d+[(0,1)]+[(0,None)]*d,method='highs',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-10,time_limit=15.))
  if not r.success:row['error']=r.message;trust*=.4
  else:
   dq=np.zeros(c.d);dq[cols]=W@r.x[:d];row['fraction']=float(r.x[d]);ok=False
   for k in range(16):
    qq=q+2.**-k*dq
    try:gg=c.physical(qq)
    except (ValueError,np.linalg.LinAlgError,AssertionError):continue
    if gg['S']==gg['U']==1:freeze(c,qq,out/f'exact_goal_it{it}_line{k}')
    if gg['reference_U']!=1 or not 1<=gg['reference_S']<=quota:continue
    if np.linalg.norm(gg['g'])<norm-max(1e-15,norm*1e-6):q=qq;ok=True;row['alpha']=2.**-k;break
   if ok and k==0:trust=min(.3,trust*1.3)
   if not ok:trust*=.4
  if trust<1e-10:break
 return None,None

def run(scout,out,number):
 scout=Path(scout);out=Path(out);out.mkdir(parents=True,exist_ok=False);de=json.loads((scout/'definition.json').read_text());cap=Cap(de['source']);rows=json.loads((scout/'screen.json').read_text());selected=sorted((r for r in rows if 1<=r['reference_S']<=2),key=lambda r:r['reference_Q'])[:number];records=[];best=np.inf
 for row in selected:
  g=cap.body(row['controls']);c=SafeCap(cap,g);d=out/f"case{row['it']}";d.mkdir();(d/'nomination.json').write_text(json.dumps(row,indent=2));(d/'safe_facets.json').write_text(json.dumps(c.safe));rec=dict(case=row['it'],safe_offsets=len(c.safe),V=g['V'],E=g['E'],F=g['F'],reference_Q=row['reference_Q'])
  try:
   q,gg=close(c,d/'closure')
   if q is None:rec['result']='finite safe-offset mass closure failed'
   else:
    rec.update(result='actual mass closure numerical',S=gg['S'],U=gg['U'],P=gg['P'],Q=gg['Q'],mass_norm=float(np.linalg.norm(gg['g'])))
    if gg['Q']<best:
     a=freeze(c,q,d/'exact');rec['exact']=str(d/'exact')
     if a['counts']==[2,1,1]and a['weak']==[0,0,0]:best=gg['Q']
  except (ValueError,AssertionError,np.linalg.LinAlgError)as err:rec.update(result='explicit failed realization or numerical correction',error=repr(err))
  records.append(rec);(out/'results.json').write_text(json.dumps(records,indent=2));print('SAFE_OFFSET_CAP_RESULT',rec,flush=True)
 print('SAFE_OFFSET_CAP_DONE',out,best,flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('scout');p.add_argument('out');p.add_argument('--number',type=int,default=18);a=p.parse_args();run(a.scout,a.out,a.number)
