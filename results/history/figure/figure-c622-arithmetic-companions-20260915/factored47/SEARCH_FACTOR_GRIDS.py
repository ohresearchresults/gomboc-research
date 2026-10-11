"""Finite factored-denominator continuation of the complete 13-grid screen."""
import hashlib,sys
from pathlib import Path
assert __debug__,'Assertions must be enabled'
assert len(sys.argv)==5,'Usage: SEARCH_FACTOR_GRIDS.py METHODS26_SOURCE FULL76_SOURCE C622_FULL_PROOF NEW_SCREEN'
p=Path(sys.argv[1])/'COARSEN_SCREEN.py';b=p.read_bytes()
assert len(b)==2850 and hashlib.sha256(b).hexdigest()=='3ff560c5905e3795316d589e625d6081bc6bb8a9661df390ae4f1ea593d479fd'
s=b.decode();line="for D in [10**k for k in range(11,4,-1)]+[2**k for k in [34,31,28,25,22,19]]:"
assert s.count(line)==1
s=s.replace(line,'for D in sorted(set([n*2**28 for n in range(4,33)]+[n*10**8 for n in range(8,21)])):')
s=s.replace('C622_FINITE_GRID_NUMERICAL_SCREEN_DONE','C622_42_FACTORED_GRIDS_NUMERICAL_SCREEN_DONE')
sys.argv=[sys.argv[0],*sys.argv[2:]]
exec(compile(s,str(p),'exec'),{'__name__':'__main__','__file__':str(p)})
