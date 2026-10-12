"""Mass-balanced finite outward pyramids on fixed maximal facets.
Analytic incremental moments nominate the added apex heights. Actual closed
boundary, support inequalities, uniform mass, and full numerical root/bar census
are rebuilt. No small-bar cutoff is an exact weak-equilibrium certificate.
"""
import json,sys,itertools
from pathlib import Path
import numpy as np
from scipy.optimize import linprog,root
from j90 import geometry,report,score
ROOT=Path(__file__).parent

def poly(points,faces):
 x=np.array(points);faces=[list(c) for c in faces];ys=[];tris=[];ed={}
 for fi,cy in enumerate(faces):
  a,b,c=x[cy[:3]];n=np.cross(b-a,c-a);h=n@a
  if h<0:cy=list(reversed(cy));a,b,c=x[cy[:3]];n=np.cross(b-a,c-a);h=n@a
  assert h>0
  ys.append(n/h)
  for a,b in zip(cy,cy[1:]+cy[:1]):ed.setdefault(tuple(sorted([a,b])),[]).append(fi)
  tris.extend([[cy[0],cy[j],cy[j+1]] for j in range(1,len(cy)-1)])
 y=np.array(ys)
 if np.max(x@y.T-1)>1e-8:raise ValueError('combined pyramids are not convex')
 assert all(len(v)==2 for v in ed.values());assert len(x)-len(ed)+len(faces)==2
 t=x[np.array(tris)];D=np.einsum('ij,ij->i',t[:,0],np.cross(t[:,1],t[:,2]));assert D.min()>0;vol=D.sum()/6;g=(D[:,None]*t.sum(1)).sum(0)/(4*D.sum())
 return dict(x=x,p=x-g,y=y,q=y/(1-y@g)[:,None],vol=vol,g=g,edges=np.array(list(ed)),dual_edges=np.array(list(ed.values())),faces={i:c for i,c in enumerate(faces)},active=np.arange(len(faces)))

def face_data(z,fi):
 cy=z['faces'][fi];x=z['x'][cy];t=np.array([[x[0],x[j],x[j+1]] for j in range(1,len(x)-1)]);a=np.linalg.norm(np.cross(t[:,1]-t[:,0],t[:,2]-t[:,0]),axis=1)/2;cf=(a[:,None]*t.mean(1)).sum(0)/a.sum();n=z['y'][fi]/np.linalg.norm(z['y'][fi]);return cf,n,float(a.sum())

def add_caps(z,apexes):
 x=z['x'].tolist();faces=[]
 for fi,cy in z['faces'].items():
  if fi not in apexes:faces.append(cy);continue
  w=apexes[fi];ix=len(x);x.append(w.tolist())
  for a,b in zip(cy,cy[1:]+cy[:1]):faces.append([a,b,ix])
 return poly(x,faces)

def reference(z):
 zz=z.copy();zz['p']=z['x'];zz['q']=z['y'];zz['g']=np.zeros(3);return report(zz)

def balanced(z,si,w,tag):
 cf,n,A=face_data(z,si);height=(w-cf)@n;assert height>0
 moment=A*height*(3*cf+w)/12
 U=report(z)['U'][0];S=report(z)['S'];choices=[]
 for fi,cy in z['faces'].items():
  if fi==si or fi in S or U in cy:continue
  c,v,a=face_data(z,fi);slack=1-z['y']@c;den=z['y']@v;ix=[j for j in range(len(den)) if j!=fi and den[j]>0];cap=min(slack[ix]/den[ix])
  if cap<=1e-10:continue
  choices.append((fi,c,v,a,cap*.8,len(cy)))
 # Each unknown is cap volume, so first derivative of moment is base centroid.
 C=np.array([x[1] for x in choices]).T;cost=np.array([x[-1] for x in choices],float)
 bounds=[(0,a*cap/3) for _,c,n,a,cap,k in choices]
 op=linprog(cost,A_eq=C,b_eq=-moment,bounds=bounds,method='highs')
 if not op.success:return None,dict(reason='linear moment capacity infeasible')
 selected=np.where(op.x>1e-12)[0]
 if sum(choices[i][-1] for i in selected)+len(z['edges'])+len(z['faces'][si])>249:return None,dict(reason='true-edge budget',selected=[choices[i][0] for i in selected])
 # Exact quadratic pyramid moment, solved numerically here, then rebuilt.
 def eq(v):
  total=moment.copy()
  for j,i in enumerate(selected):
   _,c,n,a,cap,k=choices[i];h=3*v[j]/a;total+=v[j]*(c+h*n/4)
  return total
 initial=op.x[selected]
 if len(selected)==3:sol=root(eq,initial,tol=1e-12);vv=sol.x
 else:
  from scipy.optimize import least_squares
  scale=max(float(np.linalg.norm(moment)),float(np.max(initial)));sol=least_squares(lambda v:eq(v*scale)/scale,initial/scale,bounds=(np.zeros(len(selected)),np.array([bounds[i][1] for i in selected])/scale),gtol=1e-13,xtol=1e-13,ftol=1e-13,max_nfev=500);vv=sol.x*scale
 if np.max(abs(eq(vv)))>1e-11 or min(vv)<=0:return None,dict(reason='quadratic moments not closed',residual=eq(vv).tolist(),volumes=vv.tolist())
 ap={si:w};extra=[]
 for v,i in zip(vv,selected):
  fi,c,n,a,cap,k=choices[i];h=3*v/a
  if h>cap:return None,dict(reason='height capacity',fi=fi)
  ap[fi]=c+h*n;extra.append(dict(face=fi,height=float(h),volume=float(v),apex=ap[fi].tolist()))
 try:zz=add_caps(z,ap)
 except Exception as e:return None,dict(reason=str(e))
 return zz,dict(primary_face=si,primary_apex=w.tolist(),primary_volume=float(A*height/3),compensators=extra,residual=eq(vv).tolist(),source=tag)

def main(src,tag='MASSCAP'):
 y=np.array(json.loads(Path(src).read_text())['planes']);z=geometry(y);z=geometry(z['q'][z['active']]);r=report(z);si=r['Q'][0]['root'];f=z['y'][si]/sum(z['y'][si]**2);table=[];best=None
 for ci in z['faces'][si]:
  for lam in [.15,.35,.65]:
   for beta in [.001,.003,.006]:
    w=(1-lam)*f+lam*z['x'][ci]+beta*f
    if np.max(np.delete(z['y']@w,si))>=1:continue
    try:single=add_caps(z,{si:w});ref=reference(single)
    except Exception:continue
    if len(ref['U'])!=1 or len(ref['S'])>2:continue
    zz,meta=balanced(z,si,w,src);rec=dict(corner=ci,lam=lam,beta=beta,reference=ref,balance=meta)
    if zz is not None:
     rr=report(zz);rec['report']=rr;key=(len(rr['S'])+len(rr['U']),sum(b['depth'] for b in rr['P'])+sum(b['depth'] for b in rr['Q']))
     if best is None or key<best[0]:
      best=(key,zz,rec);print('BEST',ci,lam,beta,'VEF',rr['V'],rr['E'],rr['F'],'SU',len(rr['S']),len(rr['U']),'Q',[b['depth'] for b in rr['Q']],'g',rr['centroid'],flush=True)
      (ROOT/f'J90_{tag}_BEST.json').write_text(json.dumps(dict(planes=zz['y'].tolist(),points=zz['x'].tolist(),faces=zz['faces'],info=rec),indent=2)+'\n')
    table.append(rec)
 (ROOT/f'J90_{tag}_SCAN.json').write_text(json.dumps(dict(original_planes=z['y'].tolist(),source=src,results=table),separators=(',',':'))+'\n')
 print('MASSCAP_FINISHED',len(table),'success',sum('report'in t for t in table),'failures',[t['balance'].get('reason') for t in table if 'report'not in t],flush=True)
if __name__=='__main__':main(sys.argv[1],sys.argv[2] if len(sys.argv)>2 else 'MASSCAP_E')
