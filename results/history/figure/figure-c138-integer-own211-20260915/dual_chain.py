"""C282 finite polar escape-chain proposal; mass is always physical hull volume.
Exact input/audit hashes are bound. Numerical output is not an exact certificate.
"""
import argparse,hashlib,json,itertools
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy.spatial import ConvexHull,QhullError
from scipy.optimize import root

def encoded(o):return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def load():
 p=Path(__file__).resolve().parent/'recovered282';b=(p/'A.json').read_bytes();assert hashlib.sha256(b).hexdigest()=='374a1eda3378fbee5cb42d9fe11d52312215fa3a15b222768a2d5f8d2a16bbce';a=json.loads(b)
 P=np.array([[float(F(t)) for t in v] for v in a['raw_vertices']])/1000
 g=np.array([float(F(t)) for t in a['raw_centroid']])/1000
 H=np.array(json.loads((p/'raw.json').read_bytes())['H'],float);Q=H[:,:3]/H[:,3:]*1000
 return P,Q,g

def mass(P):
 h=ConvexHull(P);anchor=P[h.vertices].mean(axis=0);tri=h.simplices;A=P[tri]-anchor
 d=np.einsum('ni,ni->n',A[:,0],np.cross(A[:,1],A[:,2]));orientation=np.sign(np.einsum('ni,ni->n',np.cross(A[:,1]-A[:,0],A[:,2]-A[:,0]),h.equations[:,:3]));d*=orientation
 assert min(d)>0
 return d.sum()/6,anchor+np.einsum('n,ni->i',d,A.sum(axis=1))/(4*d.sum()),h

def invert(Q):
 h=ConvexHull(Q);b=-h.equations[:,3]
 if min(b)<=1e-11:raise ValueError('Unbounded polar')
 P=h.equations[:,:3]/b[:,None]
 # Merge only for numerical mass conditioning; exact reconstruction is separate.
 _,ix=np.unique(np.round(P,10),axis=0,return_index=True);return P[np.sort(ix)]

def escapes(X):
 D=X[None,:,:]-X[:,None,:];norm=np.linalg.norm(X,axis=1);dn=np.linalg.norm(D,axis=2)
 v=np.einsum('ik,ijk->ij',X,D)/np.maximum(norm[:,None]*dn,1e-300);np.fill_diagonal(v,-np.inf)
 return v.max(axis=1)

def census(P):
 v,g,h=mass(P);X=P[h.vertices]-g;u=escapes(X);n=h.equations[:,:3];b=-h.equations[:,3]-n@g;Q=n/b[:,None];_,ix=np.unique(np.round(Q,9),axis=0,return_index=True);Q=Q[np.sort(ix)];s=escapes(Q)
 return dict(V=len(h.vertices),F=len(Q),E_proposal=len(h.vertices)+len(Q)-2,S=int(sum(s<-1e-9)),U=int(sum(u<-1e-9)),S_uncertain=int(sum(abs(s)<=1e-9)),U_uncertain=int(sum(abs(u)<=1e-9)),stable_ids=np.where(s<-1e-9)[0].tolist(),unstable_ids=np.where(u<-1e-9)[0].tolist(),centroid=g.tolist(),volume=float(v),min_s=float(min(s)),min_u=float(min(u)))

def chain(Q,c,n,bow,bulge,gain,opposed=True,reverse=False):
 d=1-Q@c
 if min(d)<=1e-7:raise ValueError('Centre outside original body')
 R=Q/d[:,None];a=R[28 if not reverse else 93];b=R[93 if not reverse else 28]*gain
 ra,rb=np.linalg.norm(a),np.linalg.norm(b);u=a/ra;v=b/rb;cos=np.clip(u@v,-1,1);phi=np.arccos(cos);e=v-cos*u;e/=np.linalg.norm(e);w=np.cross(u,e)
 t=np.arange(1,n)/n;points=[b[None,:]]
 for angle in ([phi,phi-2*np.pi] if opposed else [phi]):
  direction=np.cos(t*angle)[:,None]*u+np.sin(t*angle)[:,None]*e;direction+=bow*np.sin(np.pi*t)[:,None]*w;direction/=np.linalg.norm(direction,axis=1)[:,None]
  radius=ra*(rb/ra)**t*np.exp(bulge*np.sin(np.pi*t)**2);points.append(radius[:,None]*direction)
 return np.r_[R,np.concatenate(points)]

def main():
 p=argparse.ArgumentParser();p.add_argument('--out',required=True);p.add_argument('--n',type=int,nargs='+',default=[12,20,32]);p.add_argument('--bow',type=float,nargs='+',default=[-1.,0.,1.]);p.add_argument('--gain',type=float,nargs='+',default=[1.,1.5,2.]);p.add_argument('--bulge',type=float,nargs='+',default=[0.]);p.add_argument('--single',action='store_true');p.add_argument('--reverse',action='store_true');p.add_argument('--maxfev',type=int,default=160);a=p.parse_args();out=Path(a.out);out.mkdir(exist_ok=False)
 P,Q,g=load();print('PARENT',census(P),flush=True);print('ENDPOINT_RADII',np.linalg.norm(Q[[28,93]]/(1-Q[[28,93]]@g)[:,None],axis=1),flush=True);records=[];best=None
 for n,bow,gain,bulge in itertools.product(a.n,a.bow,a.gain,a.bulge):
  def fun(c):
   try:return mass(invert(chain(Q,c,n,bow,bulge,gain,not a.single,a.reverse)))[1]
   except (ValueError,QhullError,AssertionError):return (c-g)*100+np.array([1.,1.,1.])
  r=root(fun,g,method='hybr',options={'xtol':1e-9,'maxfev':a.maxfev});c=r.x
  rec=dict(n=n,bow=bow,gain=gain,bulge=bulge,opposed=not a.single,reverse=a.reverse,c=c.tolist(),root_status=int(r.status),nfev=int(r.nfev),closure=float(np.linalg.norm(fun(c))))
  try:
   Z=chain(Q,c,n,bow,bulge,gain,not a.single,a.reverse);X=invert(Z)+c;rec.update(census(X));rank=(rec['S']+rec['U']+rec['S_uncertain']+rec['U_uncertain'],rec['E_proposal'])
   if best is None or rank<best:
    best=rank;(out/'BEST.json').write_bytes(encoded({'record':rec,'Q_about_chart_centre':Z.tolist(),'points':X.tolist()}));print('BEST',rank,rec,flush=True)
  except (ValueError,QhullError,AssertionError) as e:rec['error']=str(e)
  records.append(rec);(out/'SEARCH.json').write_bytes(encoded({'parameters':vars(a),'records':records}));print('CASE',len(records),rec.get('S'),rec.get('U'),rec['closure'],flush=True)
 print('C282_POLAR_CHAIN_SEARCH_FINISHED',len(records),best,flush=True)
if __name__=='__main__':main()
