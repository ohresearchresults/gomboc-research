"""Finite cap heights within the exactly identified visible-one-facet region."""
import sys,json,numpy as np
from gmpy2 import mpq
from selected_projective import ROOT,load
from support_persistence import barcode
from geometry import mass,angular_scores
source=ROOT/'artifacts/retire_current/exact_concave_checkpoint1/exact_E245/audit.json';X,Y,tri,eu,es,r=load(source);c=np.array([float(mpq(v)) for v in r['raw_centroid']]);Z=X-c;Q=Y/(1-Y@c)[:,None];bp,bw,bb=barcode(Q,np.ones(len(Q)),es);j=int(np.argmax(bb));f=int(bp[j,0]);u=r['unstable_vertices'][0];n=Y[f];foot=c+n*(1-n@c)/(n@n);direction=foot-c;rows=[]
for t in [.05,.1,.25,.5,.75,.9]:
 p0=(1-t)*foot+t*X[u];den=Y@direction;bounds=(1-Y@p0)/np.where(den>0,den,1);bounds[(den<=0)| (np.arange(len(Y))==f)]=np.inf;capmax=float(bounds.min())
 for frac in [.0001,.001,.01,.1,.3,.6,.9]:
  eps=frac*capmax;p=p0+eps*direction;XX=np.vstack([X,p]);faces=[vs for i,vs in enumerate(r['faces']) if i!=f];ids=r['faces'][f];faces+= [[ids[i],ids[(i+1)%3],len(X)] for i in range(3)];tt=np.array([[ff[0],ff[k],ff[k+1]] for ff in faces for k in range(1,len(ff)-1)]);v,cc=mass(XX,tt);ZZ=XX-cc;norm=np.array([np.cross(XX[ff[1]]-XX[ff[0]],XX[ff[2]]-XX[ff[0]]) for ff in faces]);hh=np.einsum('ij,ij->i',norm,np.array([XX[ff[0]]-cc for ff in faces]));YY=norm/hh[:,None];uc=int((angular_scores(ZZ).max(1)<0).sum());sc=int((angular_scores(YY).max(1)<0).sum());rows.append(dict(mix=t,epsilon=eps,fraction=frac,capmax=capmax,S=sc,U=uc,centroid_shift=(cc-c).tolist(),centroid_inf=float(abs(cc-c).max())))
print('CAP_SCREEN',rows,flush=True);out=ROOT/'artifacts/detached_main_cap';(out/'height_screen.json').write_text(json.dumps(rows,indent=2)+'\n')
