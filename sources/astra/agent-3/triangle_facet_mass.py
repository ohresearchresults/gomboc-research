"""A literal cap with three uniform mass controls in one simple triangular facet.

Geometric motivation: Balancing Polyhedra, Lemma2 and Remarks3-4, archived in
sources/literature_mass_control_20260929.  All other planes remain fixed; the
three vertices of the compensating triangle move along their existing edges.
Their mass Jacobian is calculated on the whole filled physical polyhedron.
"""
import argparse,json,time,hashlib
from pathlib import Path
from math import gcd,lcm
import numpy as np
from gmpy2 import mpq
from polyhedral_stable_cap import Cap
from support_geometry import escape
from persistence_birth import bars_loss
from exact_audit_vertices import check_B,dot,cross,sub
from exact_projective_audit import inverse,apply
from exact_barcode_report import report

class FacetMass:
 def __init__(self,g,f):
  self.g=g;self.f=f;self.faces=g['faces'];self.X=g['X'].copy();self.Y=g['H']/(1+g['H']@g['centroid'])[:,None];self.cy=self.faces[f];assert len(self.cy)==3;self.inc=np.zeros((len(self.faces),len(self.X)),bool)
  for j,cy in enumerate(self.faces):self.inc[j,cy]=True
  self.other=[]
  for i in self.cy:
   ids=np.flatnonzero(self.inc[:,i]);assert len(ids)==3;self.other.append([int(j)for j in ids if j!=f])
  self.T=np.array([(cy[0],cy[k],cy[k+1])for cy in self.faces for k in range(1,len(cy)-1)])
 def physical(self,q,require_valid=True):
  X=self.X.copy();Y=self.Y.copy();Y[self.f]=q;DX=np.zeros((len(X),3,3))
  for i,other in zip(self.cy,self.other):
   M=np.vstack((Y[other],q));I=np.linalg.inv(M);X[i]=I@np.ones(3);DX[i]=-np.outer(I[:,2],X[i])
  gap=1-Y@X.T;contact=float(max(abs(gap[self.inc])));non=float(min(gap[~self.inc]));a,b,c=X[self.T[:,0]],X[self.T[:,1]],X[self.T[:,2]];da,db,dc=DX[self.T[:,0]],DX[self.T[:,1]],DX[self.T[:,2]];v6=np.einsum('ic,ic->i',a,np.cross(b,c));vol=v6.sum()/6;centre=np.sum(v6[:,None]*(a+b+c),axis=0)/(4*v6.sum());dv=np.einsum('ic,icp->ip',np.cross(b,c),da)+np.einsum('ic,icp->ip',np.cross(c,a),db)+np.einsum('ic,icp->ip',np.cross(a,b),dc);Dg=(np.einsum('ip,ic->cp',dv,a+b+c-4*centre)+np.einsum('i,icp->cp',v6,da+db+dc))/(4*v6.sum());valid=non>0 and contact<1e-8 and min(v6)>0 and vol>0
  if require_valid and not valid:raise ValueError('modified triangular facet is not an admitted convex realization')
  den=1-Y@centre;assert min(den)>0;H=Y/den[:,None];Z=X-centre;P=bars_loss(Z,self.g['pe'],.03)[2];Q=bars_loss(H,self.g['qe'],.03)[2];S=int(np.sum(escape(Y)[0]<0));U=int(np.sum(escape(X)[0]<0));return dict(X=X,Y=Y,H=H,Z=Z,g=centre,Dg=Dg,volume=vol,reference_S=S,reference_U=U,S=int(np.sum(escape(H)[0]<0)),U=int(np.sum(escape(Z)[0]<0)),P=max(P,default=0.),Q=max(Q,default=0.),Q_bars=Q,noncontact=non,contact_error=contact,valid=valid)
 def close(self):
  q=self.Y[self.f].copy();trace=[]
  for it in range(24):
   g=self.physical(q);norm=float(np.linalg.norm(g['g']));trace.append(dict(it=it,mass_norm=norm,S=g['S'],U=g['U'],reference_S=g['reference_S'],reference_U=g['reference_U'],Q=g['Q'],min_gap=g['noncontact']))
   if norm<1e-13:return q,g,trace
   step=-np.linalg.solve(g['Dg'],g['g']);ok=False
   for k in range(16):
    qq=q+2.**-k*step
    try:gg=self.physical(qq)
    except (ValueError,np.linalg.LinAlgError,AssertionError):continue
    if gg['reference_U']!=1 or not 1<=gg['reference_S']<=2:continue
    if np.linalg.norm(gg['g'])<norm-max(1e-15,norm*1e-5):q=qq;ok=True;break
   if not ok:raise ValueError('finite triangular-facet mass correction stalled')
  raise ValueError('triangular-facet mass correction exceeded24steps')

def freeze(cap,g,f,q,out):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);a=cap.a;centre=[mpq(float(v))for v in cap.g0];scale=mpq(float(cap.scale));P=[tuple((mpq(v)-centre[k])/scale for k,v in enumerate(x))for x in a['raw_vertices']];point=tuple(mpq(float(v))for v in g['point']);sourceplanes=[(tuple(mpq(v)*scale for v in n),mpq(h)-sum(mpq(v)*c for v,c in zip(n,centre)))for n,h in zip(a['normals'],a['offsets'])];visible=[i for i,(n,h)in enumerate(sourceplanes)if dot(n,point)>h];assert visible==g['visible'].tolist();planes=[]
 for desc in g['face_sources']:
  if desc['type']=='old':n,h=sourceplanes[desc['index']]
  else:
   i,j=desc['edge'];n=cross(sub(P[j],P[i]),sub(point,P[i]));h=dot(n,P[i]);assert h!=0
   if h<0:n=tuple(-v for v in n);h=-h
  planes.append((n,h))
 assert all(dot(n,x)<=h for n,h in planes for x in P+[point]);planes[f]=(tuple(mpq(float(v))for v in q),mpq(1));expected=[(P+[point])[i]for i in g['active_point_ids']];inc=np.zeros((g['F'],g['V']),bool)
 for j,cy in enumerate(g['faces']):inc[j,cy]=True
 for i in g['faces'][f]:
  ids=np.flatnonzero(inc[:,i]);assert len(ids)==3;mat=[planes[j][0]for j in ids];rhs=[planes[j][1]for j in ids];expected[i]=apply(inverse(mat),rhs)
 for j,(n,h)in enumerate(planes):
  for i,x in enumerate(expected):
   gap=h-dot(n,x)
   assert (gap==0 if inc[j,i]else gap>0),'literal exact contact/noncontact did not match proposal'
 rows=[]
 for n,h in planes:
  v=(*n,h);D=lcm(*(int(x.denominator)for x in v));r=[int(x*D)for x in v];common=gcd(*r);rows.append([x//common for x in r])
 B=lambda x:json.dumps(x,default=str,sort_keys=True,separators=(',',':')).encode();raw=dict(H=rows);(out/'raw.json').write_bytes(B(raw));(out/'coordinates.json').write_bytes(B(dict(points=expected,density=1)));(out/'construction.json').write_bytes(B(dict(source=str(cap.source.resolve()),source_audit_sha256=hashlib.sha256((cap.source/'audit.json').read_bytes()).hexdigest(),frame_centre=centre,frame_scale=scale,added_point=point,compensation_face=f,compensation_face_source=g['face_sources'][f],new_plane=planes[f],formula='exact affine source hull plus literal dyadic point; one triangular supporting plane replaced by literal dyadic coefficients, all other planes unchanged')));a=check_B.run(raw);assert {tuple(mpq(v)for v in x)for x in a['raw_vertices']}==set(expected);assert [a[k]for k in ['V','E','F']]==[g[k]for k in ['V','E','F']];(out/'audit.json').write_bytes(B(a));s={k:a[k]for k in ['V','E','F','counts','weak','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};s.update(C_2E=2*a['E'],VplusEplusF=a['V']+a['E']+a['F'],goal_met=a['counts']==[1,1,0]and a['weak']==[0,0,0]and 34<=2*a['E']<500 and a['V']+a['E']+a['F']<500,audit_sha256=hashlib.sha256((out/'audit.json').read_bytes()).hexdigest());(out/'summary.json').write_text(json.dumps(s,indent=2));report(out);print('EXACT_TRIANGLE_FACET_MASS',out,s,flush=True)
 if s['goal_met']:
  from goal_nomination import ExactGoalCandidateFound
  raise ExactGoalCandidateFound('Exact Figure candidate at '+str(out))
 return s

def run(source,out,trials,seed,number):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);cap=Cap(source);X=cap.X;normal=cap.normal;h=float(np.linalg.norm(cap.foot));caps=(X@normal+np.linalg.norm(X,axis=1))/2-h;parents=np.flatnonzero(caps>1e-8);b=cap.B[:,:2];rng=np.random.default_rng(seed);rows=[];start=time.time();(out/'definition.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),audit_sha256=hashlib.sha256((Path(source)/'audit.json').read_bytes()).hexdigest(),seed=seed,scope='old-parent Thales-ball point additions, whole-body uniform centroid corrected with one simple triangular facet; exact audit required'),indent=2))
 for it in range(trials):
  parent=int(rng.choice(parents));v=X[parent];height=caps[parent]*np.exp(rng.uniform(np.log(1e-5),np.log(.95)));delta=h+height-normal@v/2;rad=np.sqrt(v@v/4-delta**2);theta=rng.uniform(0,2*np.pi);rr=rad*np.sqrt(rng.random())*.98;point=v/2+normal*delta+b@np.array([rr*np.cos(theta),rr*np.sin(theta)]);assert point@(v-point)>0;controls=np.linalg.solve(cap.B,point-cap.foot);g=cap.body(controls)
  if g['V']+g['E']+g['F']>=500:continue
  Href=g['H']/(1+g['H']@g['centroid'])[:,None];S=int(np.sum(escape(Href)[0]<0));U=int(np.sum(escape(g['X'])[0]<0));assert U==1;Q=bars_loss(Href,g['qe'],.03)[2];rows.append(dict(it=it,parent=parent,point=point.tolist(),controls=controls.tolist(),reference_S=S,reference_U=U,reference_Q=max(Q,default=0.),V=g['V'],E=g['E'],F=g['F']))
 (out/'screen.json').write_text(json.dumps(rows,indent=2));selected=sorted((r for r in rows if 1<=r['reference_S']<=2),key=lambda r:r['reference_Q'])[:number];history=[];best=np.inf;print('TRIANGLE_FACET_SCREEN',len(rows),len(selected),min((r['reference_Q']for r in selected),default=None),flush=True)
 for row in selected:
  d=out/f"case{row['it']}";d.mkdir();g=cap.body(row['controls']);degree=np.bincount(g['pe'].ravel(),minlength=g['V']);eligible=[f for f,cy in enumerate(g['faces'])if len(cy)==3 and all(degree[i]==3 for i in cy)];record=dict(nomination=row,eligible=eligible,attempts=[])
  for f in eligible:
   trial=dict(facet=f)
   try:
    c=FacetMass(g,f);q,gg,trace=c.close();np.save(d/f'plane{f}.npy',q);np.save(d/f'points{f}.npy',gg['X']);(d/f'trace{f}.json').write_text(json.dumps(trace,indent=2));trial.update(result='uniform physical centroid closed numerically',S=gg['S'],U=gg['U'],P=gg['P'],Q=gg['Q'],mass_norm=float(np.linalg.norm(gg['g'])))
    if gg['Q']<best or gg['S']==gg['U']==1:
     aa=freeze(cap,g,f,q,d/f'exact_facet{f}');trial['exact']=str(d/f'exact_facet{f}')
     if aa['counts']==[2,1,1]and aa['weak']==[0,0,0]:best=gg['Q']
   except (ValueError,AssertionError,np.linalg.LinAlgError)as err:trial.update(result='explicit finite failure',error=repr(err))
   record['attempts'].append(trial)
  record['seconds']=time.time()-start;history.append(record);(out/'trials.json').write_text(json.dumps(history,indent=2));print('TRIANGLE_FACET_MASS_CASE',row['it'],'best',best,'successes',sum(a['result']=='uniform physical centroid closed numerically'for a in record['attempts']),time.time()-start,flush=True)
 print('TRIANGLE_FACET_MASS_DONE',out,best,flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--trials',type=int,default=8000);p.add_argument('--seed',type=int,default=84101);p.add_argument('--number',type=int,default=35);a=p.parse_args();run(a.source,a.out,a.trials,a.seed,a.number)
