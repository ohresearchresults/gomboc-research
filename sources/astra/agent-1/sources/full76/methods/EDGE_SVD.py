"""True-edge tangent-cone escape conditioning in the full filled-mass atlas.
On a convex polyhedron a positive linear escape exists iff a true incident edge
has one. This changes the numerical conditioning, not the required exact census.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from flexible import *
from SVD_CORRECT import repair
import argparse,platform,scipy
sys.path.insert(0,str(ROOT/'parent'));import RECONSTRUCT,check_B
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def attach(s):
 pe=sorted({tuple(sorted((i,j))) for cy in s.faces for i,j in zip(cy,cy[1:]+cy[:1])});qe=[]
 for i,j in pe:
  ff=sorted(set(s.owners[i])&set(s.owners[j]));assert len(ff)==2;qe.append(ff)
 maskp=np.eye(s.nv,dtype=bool);maskq=np.eye(s.nq,dtype=bool)
 for i,j in pe:maskp[i,j]=maskp[j,i]=True
 for i,j in qe:maskq[i,j]=maskq[j,i]=True
 blockedp=list(zip(*np.where(~maskp)));blockedq=list(zip(*np.where(~maskq)));s.blockedp=blockedp;s.blockedq=blockedq;s.forcedp={};s.forcedq={};s.last=None
 return pe,sorted(set(map(tuple,qe)))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--generator',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--steps',type=int,default=100);ap.add_argument('--goal',type=float,default=1e-8);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False);G=json.load(open(a.generator));raw=RECONSTRUCT.recover(G);rep=check_B.run(raw);Q=np.array([[float(F(x,r[-1])) for x in r[:3]] for r in raw['H']]);s=FlexibleAtlas(G,rep,Q);pe,qe=attach(s);(a.out/'SOURCE_GENERATOR.json').write_bytes(B(G));(a.out/'SOURCE_B.json').write_bytes(B(rep));(a.out/'EDGES.json').write_bytes(B(dict(physical=pe,polar=qe)));(a.out/'INPUT.json').write_bytes(B(dict(steps=a.steps,goal=a.goal,versions=[platform.python_version(),np.__version__,scipy.__version__])));print('EDGE_INITIAL_EXACT_B',rep['V'],rep['E'],rep['F'],rep['counts'],rep['weak'],flush=True);repair(s,np.zeros(s.n),a.out,steps=a.steps,goal=a.goal)
if __name__=='__main__':main()
