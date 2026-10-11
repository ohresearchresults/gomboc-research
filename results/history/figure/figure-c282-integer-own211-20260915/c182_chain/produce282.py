"""Reproduce the integer C282 checkpoint from the exact Finch C182 input."""
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy.optimize import root
import chain_search2 as m
from exact_points import make,encoded

def main():
 p=argparse.ArgumentParser();p.add_argument('--audit',required=True);p.add_argument('--raw',required=True);p.add_argument('--core',required=True);p.add_argument('--out',required=True);a=p.parse_args()
 P,Q,ep,eq,W=m.load(a.audit,a.raw)
 def fun(c):return m.mass(np.r_[P,m.chain(P,c,16,0.,0.,True)])[1]-c
 sol=root(fun,np.zeros(3),method='hybr',options={'xtol':1e-10,'maxfev':150});assert sol.status==1 and np.linalg.norm(fun(sol.x))<1e-10
 A=json.loads(Path(a.audit).read_bytes());g=np.array([float(F(x)) for x in A['raw_centroid']]);rawP=np.array([[float(F(x)) for x in row] for row in A['raw_vertices']]);Z=m.chain(P,sol.x,16,0.,0.,True)+g
 I=np.unique(np.rint(np.r_[rawP,Z]*1000).astype(np.int64),axis=0)-[-14,15,272]
 sys.path.insert(0,str(Path(a.core).resolve()));import check_B
 B=check_B.run(make(I.tolist()));assert [B['V'],B['E'],B['F'],*B['counts'],*B['weak']]==[49,141,94,2,1,1,0,0,0]
 V=[[int(F(x)) for x in row] for row in B['raw_vertices']];assert all(F(x).denominator==1 for row in B['raw_vertices'] for x in row)
 b=encoded({'object':'COORD_C282_OPPOSED_CHAIN_G1000_OWN211','points':V});assert len(b)==776 and hashlib.sha256(b).hexdigest()=='c01c8c5eb79a099250ea9f2c8cf8d85a17546abe7ab2b58129a78a6df3e1aaa7'
 out=Path(a.out);out.mkdir(parents=True,exist_ok=False);(out/'POINTS49.json').write_bytes(b)
 print('C282_SOURCE_ONLY_NUMERICAL_PRODUCTION_TO_EXACT_INTEGER_INPUT_PASS',len(I),len(V),flush=True)
if __name__=='__main__':main()
