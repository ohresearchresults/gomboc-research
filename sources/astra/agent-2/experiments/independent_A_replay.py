"""Independent triple-intersection/cone-boundedness native auditA replay.
Compares every field against auditB on the identical rational physicalHinput.
"""
from pathlib import Path
import sys,json,hashlib,time
from gmpy2 import mpq
ROOT=Path(__file__).resolve().parents[1];sys.set_int_max_str_digits(0)
sys.path.insert(0,str(ROOT/'sources/full76/decoded/methods/parent'));import check_A
check_A.F=mpq
folder=ROOT/sys.argv[1];raw=json.loads((folder/'H.json').read_text());b=json.loads((folder/'audit.json').read_text());t=time.time();a=check_A.run(raw);blob=json.dumps(a,sort_keys=True,separators=(',',':')).encode();(folder/'audit_A.json').write_bytes(blob);different=[k for k in set(a)|set(b) if a.get(k)!=b.get(k)];report=dict(seconds=time.time()-t,source_sha256=hashlib.sha256((folder/'H.json').read_bytes()).hexdigest(),audit_A_sha256=hashlib.sha256(blob).hexdigest(),different_fields=different,counts=a['counts'],weak=a['weak'],V=a['V'],E=a['E'],F=a['F']);(folder/'independent_A_comparison.json').write_text(json.dumps(report,indent=2)+'\n');print('INDEPENDENT_A',report,flush=True);assert not different
