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
