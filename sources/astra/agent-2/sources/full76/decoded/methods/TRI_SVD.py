"""Exact-contact triangular union, inherited parent rooted exits, full-mass SVD repair."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from union_atlas import *
from CROSS_CAP import inherited
from TREE_REPAIR import arrows
from SVD_CORRECT import repair
import argparse,platform,scipy
sys.path.insert(0,str(ROOT/'parent'));import RECONSTRUCT
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--generator',type=Path,required=True);ap.add_argument('--report',type=Path,required=True);ap.add_argument('--pair',type=int,nargs=2,required=True);ap.add_argument('--steps',type=int,default=80);ap.add_argument('--goal',type=float,default=1e-7);ap.add_argument('--dynamic',action='store_true');ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False);G=json.load(open(a.generator));rep=json.load(open(a.report));raw=RECONSTRUCT.recover(G);Q=np.array([[float(F(x,r[-1])) for x in r[:3]] for r in raw['H']]);s=UnionAtlas(G,rep,a.pair,Q)
 if not a.dynamic:
  s.forcedp,mp,ch=inherited(rep,s.owners);c=np.array([float(F(x)) for x in rep['raw_centroid']]);aq=arrows(Q/(1-Q@c)[:,None]);sp=np.argmax(aq,axis=1);s.forcedq={i:int(sp[i]) for i in range(s.nq) if i!=s.S};(a.out/'WITNESSES.json').write_bytes(B(dict(primal=s.forcedp,polar=s.forcedq,mapping=mp)))
 s.last=None;(a.out/'SOURCE_GENERATOR.json').write_bytes(B(G));(a.out/'PATCH.json').write_bytes(B(s.patch));(a.out/'INITIAL_GENERATOR.json').write_bytes(B(s.G));(a.out/'INPUT.json').write_bytes(B(dict(pair=a.pair,steps=a.steps,goal=a.goal,dynamic=a.dynamic,versions=[platform.python_version(),np.__version__,scipy.__version__])));repair(s,np.zeros(s.n),a.out,steps=a.steps,goal=a.goal)
if __name__=='__main__':main()
