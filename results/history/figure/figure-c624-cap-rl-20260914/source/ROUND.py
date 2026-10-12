"""Exact ties-to-even rounding of free controls; incidence equations remain exact."""
import json,sys
from fractions import Fraction
from pathlib import Path
def rounded(d,k):
 d=json.loads(json.dumps(d));old=d['grid'];new=10**k
 d['controls']=[[round(Fraction(x*new,old)) for x in row] for row in d['controls']]
 d['grid']=new
 return d
if __name__=='__main__':
 d=rounded(json.loads(Path(sys.argv[1]).read_text()),int(sys.argv[2]))
 Path(sys.argv[3]).write_text(json.dumps(d,sort_keys=True,separators=(',',':')))
