"""Finite next-union trials; numerical states are never exact acceptance."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from general_atlas import *
from REFINE import correct,warm
from numeric import Chart
import argparse,time,hashlib,platform,scipy
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def seed(c,e,mode):
 if mode=='stress':
  w=c.w.copy();w[e]=0.;return c.solve(w)[0]
 return c.Q.copy()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--edge',type=int);ap.add_argument('--steps',type=int,default=50);ap.add_argument('--warm',type=int,default=0);ap.add_argument('--mode',default='stress');ap.add_argument('--out',type=Path);a=ap.parse_args();c=Chart()
 if a.edge is None:
  results=[]
  for candidate in json.loads((ROOT/'ELIGIBLE.json').read_text()):
   for mode in ('stress','direct'):
    try:
     Q=seed(c,candidate['edge'],mode);s=GeneralAtlas(candidate['edge'],Q);v,J,g=s.evaluate(np.zeros(s.n))
     results.append(dict(**candidate,mode=mode,n=s.n,merit=float(np.linalg.norm(s.residual(np.zeros(s.n)))),mech=float(v[:s.mechlen].min()),slack=float(g['slack'].min()),det=float(g['v6'].min()),patch=s.patch))
    except Exception as ex:results.append(dict(**candidate,mode=mode,error=str(ex)))
  (ROOT/'SCREEN.json').write_bytes(B(results));print(json.dumps(sorted([r for r in results if 'merit' in r],key=lambda r:r['merit'])[:30],indent=2));return
 out=a.out;out.mkdir(parents=True,exist_ok=False);Q=seed(c,a.edge,a.mode);s=GeneralAtlas(a.edge,Q);s.checkpoint_dir=out;z=np.zeros(s.n);t=time.time()
 checkpoint=dict(edge=a.edge,mode=a.mode,patch=s.patch,initial_Q_hex=[[float(x).hex() for x in row] for row in Q],versions=[platform.python_version(),np.__version__,scipy.__version__],warm=a.warm,steps=a.steps)
 (out/'INPUT.json').write_bytes(B(checkpoint))
 if a.warm:z=warm(s,a.warm);(out/'WARM_Z.json').write_bytes(B([float(x).hex() for x in z]))
 z,records=correct(s,z,steps=a.steps);v,J,g=s.evaluate(z)
 G=copy.deepcopy(s.G);G['grid']=10**9;G['controls']=np.rint(g['Y']*G['grid']).astype(np.int64).tolist()
 (out/'GENERATOR.json').write_bytes(B(G));(out/'Z.json').write_bytes(B([float(x).hex() for x in z]));(out/'RECORDS.json').write_bytes(B(records))
 status=dict(edge=a.edge,mode=a.mode,merit=float(np.linalg.norm(s.residual(z))),mech=float(v[:s.mechlen].min()),slack=float(g['slack'].min()),det=float(g['v6'].min()),time=time.time()-t,gen_sha=hashlib.sha256(B(G)).hexdigest())
 (out/'STATUS.json').write_bytes(B(status));print('FINITE_TRIAL_END',json.dumps(status),flush=True)
if __name__=='__main__':main()
