import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from union_atlas import *
from REFINE import warm,correct
import argparse,time,hashlib,scipy,platform
sys.path.insert(0,str(ROOT/'parent'));import RECONSTRUCT
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--generator',type=Path,required=True);ap.add_argument('--report',type=Path,required=True);ap.add_argument('--pair',type=int,nargs=2,required=True);ap.add_argument('--warm',type=int,default=1000);ap.add_argument('--steps',type=int,default=100);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False)
 G=json.load(open(a.generator));rep=json.load(open(a.report));raw=RECONSTRUCT.recover(G);Q=np.array([[float(F(x,r[-1])) for x in r[:3]] for r in raw['H']]);s=UnionAtlas(G,rep,a.pair,Q);s.checkpoint_dir=a.out;(a.out/'SOURCE_GENERATOR.json').write_bytes(B(G));(a.out/'SOURCE_REPORT.json').write_bytes(B(rep));(a.out/'INPUT.json').write_bytes(B(dict(pair=a.pair,warm=a.warm,steps=a.steps,versions=[platform.python_version(),np.__version__,scipy.__version__])));(a.out/'PATCH.json').write_bytes(B(s.patch));t=time.time();z=warm(s,a.warm) if a.warm else np.zeros(s.n);(a.out/'WARM_Z.json').write_bytes(B([float(x).hex() for x in z]));z,h=correct(s,z,a.steps);v,J,g=s.evaluate(z);G=s.G;G['grid']=10**12;G['controls']=np.rint(g['Y']*G['grid']).astype(np.int64).tolist();(a.out/'GENERATOR.json').write_bytes(B(G));(a.out/'Z.json').write_bytes(B([float(x).hex() for x in z]));(a.out/'RECORDS.json').write_bytes(B(h));status=dict(mech=float(v[:s.mechlen].min()),slack=float(g['slack'].min()),det=float(g['v6'].min()),time=time.time()-t,sha=hashlib.sha256(B(G)).hexdigest());(a.out/'STATUS.json').write_bytes(B(status));print('UNION_NUMERICAL_ONLY',json.dumps(status),flush=True)
if __name__=='__main__':main()
