"""Report exact rational bit sizes from complete own-centroid audit outputs."""
import argparse,json,sys
from fractions import Fraction as F
from pathlib import Path
sys.set_int_max_str_digits(0)
def stats(values):
 a=[F(x) for x in values]
 return {'max_numerator_bits':max(abs(x.numerator).bit_length() for x in a),'max_denominator_bits':max(x.denominator.bit_length() for x in a)}
def run(root):
 result={}
 for branch in ['coupled','c80']:
  for p in sorted((root/branch).glob('*/A.json')):
   a=json.loads(p.read_bytes());b=json.loads((p.parent/'B.json').read_bytes());assert a==b
   centroid=list(map(F,a['raw_centroid']));vertices=[list(map(F,v)) for v in a['raw_vertices']]
   raw=json.loads((p.parent/'RAW.json').read_bytes())['H']
   result[branch+'/'+p.parent.name]={'counts':a['counts'],'weak':a['weak'],'V':a['V'],'E':a['E'],'F':a['F'],'C':2*a['E'],'primitive_support_rows':stats(x for row in raw for x in row),'raw_vertices':stats(x for v in vertices for x in v),'raw_centroid':stats(centroid),'centred_vertices':stats(x-c for v in vertices for x,c in zip(v,centroid)),'volume':stats([a['ordinary_volume']]),'raw_first_moments':stats(a['raw_first_moments']),'third_centred_mass':json.loads((p.parent/'MASS.json').read_bytes())}
 return result
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);a=ap.parse_args();assert __debug__
 (a.root/'METRICS.json').write_text(json.dumps(run(a.root),sort_keys=True,separators=(',',':')))
 print('EXACT_RATIONAL_BIT_METRICS_PASS')
