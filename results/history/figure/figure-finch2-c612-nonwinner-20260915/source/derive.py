"""Deterministic rational derivative generators; no numerical geometry is used."""
import json,copy
from pathlib import Path
from fractions import Fraction as Q

def blob(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def quantize(g,power):
 g=copy.deepcopy(g);old=g['grid'];new=10**power
 g['controls']=[[round(Q(v*new,old)) for v in row] for row in g['controls']];g['grid']=new;return g

def close82_85(g):
 g=copy.deepcopy(g);assert len(g['controls'])==179
 assert next(r for r in g['plan'] if r[0]==16)==[16,[],[]]
 g['plan']=[r for r in g['plan'] if r[0]!=16];j=len(g['controls']);g['controls'].append([0,0,0]);g['groups'].append([16,55,94,118]);g['plan']+=[[j,[55,94,118],[0,1,2]],[16,[j],[2]]];return g

def main():
 root=Path(__file__).resolve().parent
 for power in [5,6,7]:
  g=quantize(json.loads((root/'MARGIN2_GENERATOR.json').read_text()),power);(root/f'MARGIN2_GRID{power}_GENERATOR.json').write_bytes(blob(g))
 for seed,name in [('FINCH_SEQUENTIAL','CLOSED_ORIGINAL'),('EDGE1','CLOSED_EDGE1')]:
  g=close82_85(json.loads((root/(seed+'_GENERATOR.json')).read_text()));(root/(name+'_GENERATOR.json')).write_bytes(blob(g))
 print('DERIVED_EXACT_GENERATORS_COMPLETE')
if __name__=='__main__':main()
