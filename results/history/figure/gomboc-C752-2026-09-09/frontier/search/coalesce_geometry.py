"""Delete real maximal facets by supported convex-combination homotopies.
Each accepted body has a recomputed filled-volume centroid and full positive
physical/polar escape forests. Numerical discovery only; use exact auditors.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import sys,json,argparse,numpy as np
from pathlib import Path
from scipy.spatial import ConvexHull
from fast_mass_engine import load,repair,checkpoint,geom,ERR

def closest_triangle(p,T):
 a,b,c=T;M=np.array([b-a,c-a]).T;uv=np.linalg.lstsq(M,p-a,rcond=None)[0];w0=[1-uv.sum(),uv[0],uv[1]];poss=[]
 if min(w0)>=0:poss.append(np.array(w0))
 for i,j in [(0,1),(1,2),(2,0)]:
  d=T[j]-T[i];t=np.clip((p-T[i])@d/(d@d),0,1);w=np.zeros(3);w[i]=1-t;w[j]=t;poss.append(w)
 w=min(poss,key=lambda w:np.linalg.norm(w@T-p));return np.linalg.norm(w@T-p),w

def proposal(q,i):
 if q[i,2]==1:
  ids=np.flatnonzero((q[:,2]==1)&(np.arange(len(q))!=i));h=ConvexHull(q[ids,:2]);best=None
  for edge in h.simplices:
   js=ids[edge];a,b=q[js];d=b-a;t=np.clip((q[i]-a)@d/(d@d),0,1);w=np.array([1-t,t]);dd=np.linalg.norm(w@q[js]-q[i]);z=(dd,js,w)
   if best is None or dd<best[0]:best=z
 else:
  keep=np.array([j for j in range(len(q)) if j!=i]);h=ConvexHull(q[keep]);best=None
  for tri in h.simplices:
   js=keep[tri];dd,w=closest_triangle(q[i],q[js]);z=(dd,js,w)
   if best is None or dd<best[0]:best=z
 dd,js,w=best;w[w<1e-10]=0.;w=w/w.sum();sel=w>0;return dd,js[sel],w[sel]

