"""Two exact full reference-centre censuses of an already defined filled body.
The actual volume/first moments remain physical; reference mechanics is labelled.
"""
import sys,json,hashlib,types
from pathlib import Path
from fractions import Fraction
R=Path(__file__).resolve().parent
sys.set_int_max_str_digits(0)
C=lambda z:json.dumps(z,sort_keys=True,separators=(',',':')).encode()
def run(raw,centre,out):
 out.mkdir(parents=True,exist_ok=False);records=[];reference=tuple(map(Fraction,centre))
 for tag in ['A','B']:
  s=(R/'parent'/('check_'+tag+'.py')).read_text()
  anchor=' C=lcm(*(x.denominator for x in centre));' if tag=='A' else ' C=lcm(*(v.denominator for v in centre));'
  assert s.count(anchor)==1
  s=s.replace(anchor,' actual_centre=centre;centre=REFERENCE\n'+anchor)
  assert s.count('raw_centroid=centre')==1
  s=s.replace('raw_centroid=centre','raw_centroid=actual_centre,mechanical_reference=centre')
  old='centred_first_moments=Z,centred_centroid=Z' if tag=='A' else 'centred_first_moments=ZERO,centred_centroid=ZERO'
  new='centred_first_moments=tuple(moment[i]-volume*centre[i] for i in range(3)),centred_centroid=tuple(actual_centre[i]-centre[i] for i in range(3))'
  assert s.count(old)==1;s=s.replace(old,new)
  env=dict(REFERENCE=reference,__name__='patched_reference_'+tag);exec(compile(s,'<exact-reference-'+tag+'>','exec'),env)
  a=env['run'](raw);records.append(a);(out/(tag+'.json')).write_bytes(C(a));print('REFERENCE_EXACT',tag,a['counts'],a['weak'],flush=True)
 assert records[0]==records[1];a=records[0];assert a['counts']==[1,1,0] and a['weak']==[0,0,0]
 assert a['centred_centroid']!=[0,0,0] and any(Fraction(v)!=0 for v in a['centred_first_moments'])
 rec=dict(status='BQ13_REFERENCE_ONLY_110_NOT_OWN_CENTRED',records_identical=True,bytes=len(C(a)),sha256=hashlib.sha256(C(a)).hexdigest(),actual_raw_centroid=a['raw_centroid'],reference=a['mechanical_reference'],actual_shifted_centroid=a['centred_centroid'])
 (out/'RECEIPT.json').write_bytes(C(rec));print(rec['status'],flush=True);return rec
if __name__=='__main__':
 raw=json.loads(Path(sys.argv[1]).read_text());g=json.loads(Path(sys.argv[2]).read_text())['raw_centroid'];run(raw,g,Path(sys.argv[3]))
