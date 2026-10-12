"""One actual changed-base deletion/repair step from a complete numerical checkpoint.
All attempted deletions and final geometric checkpoints are retained. Not exclusion.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,hashlib,json,sys
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import least_squares
import pyramid_coarsen as pc

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--max-nfev',type=int,default=250);ap.add_argument('--attempts',type=int,default=6);a=ap.parse_args()
 bb=Path(a.input).read_bytes();r=json.loads(bb);parents=[x for x in r['records'] if x.get('numerical_own211',False)];assert parents
 p=min(parents,key=lambda x:x['C']);B=np.array(p['base']);apex=np.array(p['apex'][:2]);n=len(B)-1;assert n>=8
 choices=[]
 for i in range(len(B)):
  Q=np.delete(B,i,axis=0);x=np.r_[Q.flatten(),apex];res=pc.residual(x,n);choices.append((float(res@res),i,x))
 choices.sort(key=lambda z:(z[0],z[1]));records=[]
 for cost,i,x in choices[:a.attempts]:
  fit=least_squares(pc.residual,x,args=(n,),max_nfev=a.max_nfev,ftol=1e-10,xtol=1e-10,gtol=1e-10,method='trf')
  d=pc.residual(fit.x,n,True);records.append({'deleted_parent_index':i,'initial_cost':cost,'nfev':int(fit.nfev),'success':bool(fit.success),'message':str(fit.message),**d})
  success=bool(d.get('numerical_own211',False));out={'input_sha256':hashlib.sha256(bb).hexdigest(),'parent_record':p,'n':n,'attempts':a.attempts,'max_nfev':a.max_nfev,'ranked_initial_costs':[[c,i] for c,i,x in choices],'records':records,'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'coarsen_source_sha256':hashlib.sha256(Path(pc.__file__).read_bytes()).hexdigest(),'terminal':'FINITE_DELETION_REPAIR_HAS_NUMERICAL_OWN211' if success else 'PARTIAL_CHECKPOINT','certified_exclusion':False}
  Path(a.out).write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n');print(n,'delete',i,d.get('squared_loss'),d.get('min_nonroot_u'),d.get('S'),d.get('U'),d.get('convex'),success,flush=True)
  if success:return
 out['terminal']='FINITE_DELETION_REPAIR_NO_NUMERICAL_OWN211';Path(a.out).write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
if __name__=='__main__':main()
