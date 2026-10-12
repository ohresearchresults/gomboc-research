"""Introduce an exact common primal apex to recover support-plane budget."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,json,pathlib,argparse
from geometry import halfspace_mesh,census,arrows
from basin_scout import score

def run(input,out):
 out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);Q=np.load(input)['Q'];m=halfspace_mesh(Q);Q=Q[m['active']]/(1-Q[m['active']]@m['g'])[:,None];P=m['X']-m['g'];u=P[np.argmax((P*P).sum(1))];scale=np.linalg.norm(u);z=u/scale;a=np.eye(3)[np.argmin(abs(z))];a=a-(a@z)*z;a/=np.linalg.norm(a);b=np.cross(z,a);B=np.column_stack([a,b,z]);Q=Q@B*scale;order=np.argsort(-Q[:,2]);hist=[]
 for k in [3,4,5,6,8,10,12,16,20,24,28,32,36,40]:
  q=Q.copy();q[order[:k],2]=1
  try:
   s=score(q);row=dict(concurrent=k,complexity_upper=2*(3*len(q)-k-3),**s);hist.append(row);np.savez(out/f'k{k:02d}.npz',Q=q);print('APEX',k,s['V'],s['E'],s['F'],s['S'],s['U'],max(s['Q'],default=0),flush=True)
  except Exception as e:hist.append(dict(concurrent=k,error=str(e)))
 (out/'history.json').write_text(json.dumps(hist,indent=2));(out/'frame.json').write_text(json.dumps({'input':str(pathlib.Path(input).resolve()),'orthogonal_columns':B.tolist(),'length_scale':float(scale),'concurrent_order':order.tolist()},indent=2))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);a=ap.parse_args();run(a.input,a.out)
