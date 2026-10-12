"""Finite whole-material orbit starting from a complete rational quotient."""
import json,argparse,numpy as np,radial
from fractions import Fraction as F
from global_family import Global,run
import global_family as engine
class Body(Global):
 def __init__(self,nodes=False):
  G=json.load(open(SOURCE));raw,p=radial.reconstruct(G);self.P=np.array(p,float);self.q=np.array([[float(F(v,h[-1])) for v in h[:3]] for h in raw['H']]);self.faces=G['faces'];self.E=np.array(sorted({tuple(sorted((i,j))) for c in self.faces for i,j in zip(c,c[1:]+c[:1])}));self.root=0;self.stable=114;self.nodes=False;self.K=8
  self.tris=np.array([(c[0],c[k],c[k+1]) for c in self.faces for k in range(1,len(c)-1)]);self.ue=np.array([(a,b) for i,j in self.E for a,b in [(i,j),(j,i)]]);self.ui=[np.flatnonzero(self.ue[:,0]==i) for i in range(len(self.P))];efs={tuple(e):[] for e in self.E.tolist()}
  for f,c in enumerate(self.faces):
   for i,j in zip(c,c[1:]+c[:1]):efs[tuple(sorted((i,j)))].append(f)
  self.fe=np.array([(a,b) for fs in efs.values() for a,b in [fs,fs[::-1]]]);self.fi=[np.flatnonzero(self.fe[:,0]==i) for i in range(len(self.q))];self.last=None;self.reslast=None
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--start',default='QUOT_11_1.json');p.add_argument('--tag',default='QGLOBAL');p.add_argument('--starts',type=int,default=30);p.add_argument('--seed',type=int,default=59233);p.add_argument('--maxeval',type=int,default=200);a=p.parse_args();SOURCE=a.start;engine.Global=Body;run(a.tag,a.starts,a.seed,a.maxeval,False,None)
