"""Same positive floors, without requiring a fresh ten-percent margin inflation."""
import sys,argparse
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R))
import leaf_general as g
import leaf_contract
class Leaf(g.Leaf):
 def rows(self,s):
  A,b=super().rows(s);b[:len(self.floor)]=self.floor-s['vals'];return A,b
if __name__=='__main__':
 leaf_contract.Leaf=Leaf
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--keep',type=int,required=True);p.add_argument('--drop',type=int,required=True);p.add_argument('--moved',type=int,required=True);p.add_argument('--release',action='store_true');p.add_argument('--preserve-drop',action='store_true');p.add_argument('--steps',type=int,default=60);a=p.parse_args();g.PRESERVE_DROP=a.preserve_drop;leaf_contract.run(a)
