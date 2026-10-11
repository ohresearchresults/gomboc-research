"""Actual C620 support114 disappearance, then coherent second-quad turnover.
The obsolete ghost point181 and inactive support114 are removed together. The
remaining exact support rows are unchanged by the cleanup. Opening the distinct
quad[87,108,122,127] costs one actual edge, subject to complete reconstruction.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from TURNOVER import *
from SOFT_SVD import repair

def clean(G):
 G=copy.deepcopy(G);assert G['n_supports']==137;assert len(G['controls'])==182;remove={114,181};mapping={i:i-int(i>114) for i in range(181) if i!=114};plan=[]
 for i,deps,axes in G['plan']:
  if i in remove:continue
  assert not(set(deps)&remove);plan.append([mapping[i],[mapping[j] for j in deps],axes])
 GG=dict(n_supports=136,grid=G['grid'],controls=[r for i,r in enumerate(G['controls']) if i not in remove],groups=[[mapping[q] for q in o] for i,o in enumerate(G['groups']) if 137+i!=181],plan=plan);assert RECONSTRUCT.recover(GG)['H']==[r for i,r in enumerate(RECONSTRUCT.recover(G)['H']) if i!=114];return GG,mapping

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--generator',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--sign',type=int,choices=[-1,0,1],required=True);ap.add_argument('--steps',type=int,default=500);ap.add_argument('--eps',default='1/10000000');a=ap.parse_args();out=a.out;out.mkdir(parents=True,exist_ok=False);G=json.load(open(a.generator));GG,mapping=clean(G);changes=dict(inactive_original_support=114,removed_ghost_point=181,old_to_new=mapping);(out/'CLEAN_GENERATOR.json').write_bytes(B(GG))
 if a.sign:
  GG,turn=open_contact(GG,179);GG['controls'][126][2]+=a.sign*round(F(a.eps)*GG['grid']);changes['turnover']=turn
 raw=RECONSTRUCT.recover(GG);rep=check_B.run(raw);(out/'INITIAL_GENERATOR.json').write_bytes(B(GG));(out/'INITIAL_B.json').write_bytes(B(rep));(out/'CHANGES.json').write_bytes(B(changes));(out/'INPUT.json').write_bytes(B(dict(sign=a.sign,steps=a.steps,eps=a.eps,versions=[platform.python_version(),np.__version__,scipy.__version__])));print('CLEAN_TURN_INITIAL_EXACT_B',rep['V'],rep['E'],rep['F'],rep['counts'],rep['weak'],flush=True);Q=np.array([[float(F(x,r[-1])) for x in r[:3]] for r in raw['H']]);s=FlexibleAtlas(GG,rep,Q);repair(s,np.zeros(s.n),out,steps=a.steps)
if __name__=='__main__':main()
