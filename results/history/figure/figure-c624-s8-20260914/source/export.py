"""Supplemental exact coordinate tables and display-only mesh; no acceptance by OBJ."""
import sys,json
from fractions import Fraction as F
from pathlib import Path
from math import lcm
sys.set_int_max_str_digits(0)
C=lambda z:json.dumps(z,sort_keys=True,separators=(',',':')).encode()
def run(src,out):
 a=json.loads((src/'A.json').read_text());p=[tuple(map(F,v)) for v in a['raw_vertices']];g=tuple(map(F,a['raw_centroid']));h=lcm(*(v.denominator for x in p for v in x),*(v.denominator for v in g));X=[[int(v.numerator*(h//v.denominator)-z.numerator*(h//z.denominator)) for v,z in zip(x,g)] for x in p]
 out.mkdir(parents=True,exist_ok=False);obj=dict(denominator=str(h),integer_vertices=[[str(v) for v in x] for x in X],faces=a['faces'],true_edges=a['edges'],interpretation='exact centred vertex = integer row / positive denominator');(out/'CENTRED_INTEGER.json').write_bytes(C(obj))
 # Exact readback without costly reduction of huge fractions.
 rr=json.loads((out/'CENTRED_INTEGER.json').read_text());hh=int(rr['denominator']);XX=[[int(v) for v in x] for x in rr['integer_vertices']];assert hh==h and XX==X
 for i,x in enumerate(p):
  for k,v in enumerate(x):assert XX[i][k]*v.denominator*g[k].denominator==hh*(v.numerator*g[k].denominator-g[k].numerator*v.denominator)
 (out/'RAW_EXACT.json').write_bytes(C(dict(vertices=a['raw_vertices'],faces=a['faces'],true_edges=a['edges'])))
 (out/'MOMENTS.json').write_bytes(C({k:a[k] for k in ['ordinary_volume','raw_first_moments','raw_centroid','centred_first_moments','centred_centroid']}))
 lines=['# Display-only mesh: exact acceptance uses rational generators and true maximal faces.']
 lines+=['v '+' '.join(format(float(F(v,h)),'.17g') for v in x) for x in X]
 lines+=['f '+' '.join(str(i+1) for i in cy) for cy in a['faces']];(out/'DISPLAY_ONLY.obj').write_text('\n'.join(lines)+'\n')
 (out/'EXPORT_RECEIPT.json').write_bytes(C(dict(status='COORD_CAP_RL_C624_EXACT_COORDINATE_READBACK_PASS',vertices=len(p),true_edges=len(a['edges']),maximal_faces=len(a['faces']),denominator_bits=h.bit_length(),integer_max_bits=max(abs(v).bit_length() for x in X for v in x))))
 print('COORD_CAP_RL_C624_EXACT_COORDINATE_READBACK_PASS',flush=True)
if __name__=='__main__':run(Path(sys.argv[1]),Path(sys.argv[2]))
