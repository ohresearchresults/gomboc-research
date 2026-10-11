"""Finite full-contact union trials from an exact prescribed checkpoint."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from general_atlas import *
from REFINE import correct,warm
import argparse,time,hashlib,scipy,platform
sys.path.insert(0,str(ROOT/'parent'));import RECONSTRUCT
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--generator',type=Path,required=True);ap.add_argument('--edges',type=int,nargs='+',required=True);ap.add_argument('--warm',type=int,default=400);ap.add_argument('--steps',type=int,default=25);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--mechanic',type=float,default=1e-7);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False);G=json.load(open(a.generator));(a.out/'SOURCE_GENERATOR.json').write_bytes(B(G));raw=RECONSTRUCT.recover(G);from fractions import Fraction as F
 Q=np.array([[float(F(x,r[-1])) for x in r[:3]] for r in raw['H']]);(a.out/'INPUT.json').write_bytes(B(dict(edges=a.edges,warm=a.warm,steps=a.steps,mechanic=a.mechanic,versions=[platform.python_version(),np.__version__,scipy.__version__])));records=[]
 for edge in a.edges:
  out=a.out/str(edge);out.mkdir();print('BATCH_START',edge,flush=True);t=time.time()
  try:
   s=GeneralAtlas(edge,Q.copy());s.checkpoint_dir=out;s.floor[:s.mechlen-2]=a.mechanic;s.floor[s.mechlen-2:s.mechlen]=1e-5;s.floor[s.mechlen:s.mechlen+s.nq]=1e-9;s.floor[s.mechlen+s.nq:-s.nq-1]=1e-6
   z=warm(s,a.warm);(out/'WARM_Z.json').write_bytes(B([float(x).hex() for x in z]));z,h=correct(s,z,a.steps);v,J,g=s.evaluate(z);GG=copy.deepcopy(s.G);GG['grid']=10**12;GG['controls']=np.rint(g['Y']*GG['grid']).astype(np.int64).tolist();(out/'GENERATOR.json').write_bytes(B(GG));(out/'Z.json').write_bytes(B([float(x).hex() for x in z]));(out/'RECORDS.json').write_bytes(B(h));(out/'PATCH.json').write_bytes(B(s.patch));r=dict(edge=edge,mech=float(v[:s.mechlen].min()),slack=float(g['slack'].min()),det=float(g['v6'].min()),merit=float(np.linalg.norm(s.residual(z))),seconds=time.time()-t,sha=hashlib.sha256(B(GG)).hexdigest())
  except Exception as ex:r=dict(edge=edge,error=repr(ex),seconds=time.time()-t)
  records.append(r);(out/'STATUS.json').write_bytes(B(r));(a.out/'SUMMARY.json').write_bytes(B(records));print('BATCH_FINAL_NUMERICAL_ONLY',json.dumps(r),flush=True)
if __name__=='__main__':main()
