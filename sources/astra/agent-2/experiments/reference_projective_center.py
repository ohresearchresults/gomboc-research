"""Physically center a far monostatic reference chamber by a projective map.
The transformed uniform centroid is integrated afresh. Reference110 never implies own110.
"""
import sys,json,numpy as np,time
from pathlib import Path
from scipy.optimize import linprog
import jax,jax.numpy as jnp
from canonical_atlas import ROOT
from geometry import angular_scores
from support_persistence import barcode
source=ROOT/'artifacts/monostatic_center_C490_fullbody';r=json.loads((source/'result.json').read_text());data=np.load(source/'numerical_chamber.npz');X=data['X'];Y=data['Y'];c=data['reference_center'];raw=json.loads(Path(r['source']).read_text());faces=raw['faces'];tr=np.array([[f[0],f[k],f[k+1]] for f in faces for k in range(1,len(f)-1)]);eu=np.array(raw['edges']);ef={}
for fi,f in enumerate(faces):
 for a,b in zip(f,f[1:]+f[:1]):ef.setdefault(tuple(sorted((a,b))),[]).append(fi)
es=np.array([ef[tuple(e)] for e in eu]);chosen={}
for ar in r['selected_arrows']:
 key=(ar['kind'],ar['node']);score=np.array(ar['a'])@c+ar['b']
 if key not in chosen or chosen[key][0]<score:chosen[key]=(score,ar)
A=np.array([x[1]['a'] for x in chosen.values()]);b=np.array([x[1]['b'] for x in chosen.values()]);inside=Y/np.linalg.norm(Y,axis=1)[:,None];off=1/np.linalg.norm(Y,axis=1);LP=linprog([0,0,0,-1],A_ub=np.vstack([np.c_[-A,np.ones(len(A))],np.c_[inside,np.ones(len(Y))]]),b_ub=np.r_[b,off],bounds=[(-1.01,1.01)]*3+[(0,.5)],method='highs');assert LP.success;center=LP.x[:3];Z=X-center;Q=Y/(1-Y@center)[:,None];print('ROBUST_REFERENCE_CHAMBER',dict(center=center.tolist(),margin=float(LP.x[3]),S=int((angular_scores(Q).max(1)<0).sum()),U=int((angular_scores(Z).max(1)<0).sum())),flush=True)
@jax.jit
def mass(B):
 P=jnp.asarray(Z)/(1+jnp.asarray(Z)@B)[:,None];a,b,c=P[tr[:,0]],P[tr[:,1]],P[tr[:,2]];six=jnp.sum(a*jnp.cross(b,c),axis=1);v=six.sum()/6;g=jnp.sum(six[:,None]*(a+b+c),axis=0)/(4*six.sum());return g,v
jac=jax.jit(jax.jacfwd(lambda x:mass(x)[0]));B=np.zeros(3);hist=[]
for it in range(60):
 g,v=map(np.asarray,mass(B));norm=np.linalg.norm(g);hist.append(dict(it=it,B=B.tolist(),centroid=g.tolist(),volume=float(v),denominator_min=float((1+Z@B).min())))
 if norm<1e-13:break
 step=np.linalg.solve(np.asarray(jac(B)),-g)
 for k in range(50):
  BB=B+2**-k*step
  if min(1+Z@BB)<=1e-6:continue
  gg,vv=map(np.asarray,mass(BB))
  if np.linalg.norm(gg)<norm*(1-1e-6):B=BB;break
 else:raise ValueError('projective centering Newton search stalled')
P=Z/(1+Z@B)[:,None];H=Q+B;g,v=map(np.asarray,mass(B));XX=P-g;YY=H/(1-H@g)[:,None];S=angular_scores(YY).max(1);U=angular_scores(XX).max(1);depth=[]
for A,ee in [(XX,eu),(YY,es)]:
 p,w,bb=barcode(A,np.ones(len(A)),ee);depth.append(sorted((bb/np.sum(A[p[:,0]]**2,axis=1)).tolist(),reverse=True))
out=ROOT/'artifacts/reference_projective_C490';out.mkdir(exist_ok=False);np.savez(out/'body.npz',X=P,Y=H,tri=tr,eu=eu,es=es);res=dict(source=str(source),reference_center=center.tolist(),reference_margin=float(LP.x[3]),projective_B=B.tolist(),history=hist,actual_centroid=g.tolist(),actual_S=int((S<0).sum()),actual_U=int((U<0).sum()),P=depth[0],Q=depth[1],minimum_denominator=float((1+Z@B).min()));(out/'result.json').write_text(json.dumps(res,indent=2)+'\n');print('PROJECTIVE_PHYSICAL_RESULT',{k:res[k] for k in ['reference_center','reference_margin','projective_B','actual_centroid','actual_S','actual_U','minimum_denominator']},'P',depth[0][:3],'Q',depth[1][:3],flush=True)
