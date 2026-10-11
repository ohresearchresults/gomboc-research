"""Cold standard-library replay of three C64 bodies and two geometric gates."""
import argparse,hashlib,json,sys
from pathlib import Path
import audit_pyramid as audit
import half_round_certificate as gate
ROOT=Path(__file__).resolve().parent

def specs(root):
 return {str(p.relative_to(root)):{'bytes':len(p.read_bytes()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(root.rglob('*')) if p.is_file()}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',required=True,type=Path);ap.add_argument('--record-expected',action='store_true');a=ap.parse_args();assert __debug__;sys.set_int_max_str_digits(0)
 if not a.record_expected:
  for n,s in json.loads((ROOT/'SOURCE_MANIFEST.json').read_bytes()).items():
   b=(ROOT/n).read_bytes();assert len(b)==s['bytes'] and hashlib.sha256(b).hexdigest()==s['sha256']
 a.out.mkdir(parents=True,exist_ok=False)
 for D,expected in [(1000,[2,6,6]),(10000,[2,4,4]),(100000,[2,1,1])]:
  result=audit.run(json.loads((ROOT/('POINTS_C64_G'+str(D)+'.json')).read_bytes()));sub=a.out/('C64_G'+str(D));sub.mkdir()
  for n,o in result.items():(sub/n).write_bytes(audit.enc(o))
  s=result['SUMMARY.json'];assert s['strict']==expected and s['weak']==[0,0,0] and (s['V'],s['E'],s['F'])==(17,32,17)
  print('EXACT_C64',D,s['strict'],s['weak'],s['raw_centred_num_max_bits'],s['raw_centred_den_max_bits'],flush=True)
 sub=a.out/'half_round';sub.mkdir()
 for n,o in gate.run().items():(sub/(n+'.json')).write_bytes(gate.enc(o))
 observed=specs(a.out)
 if a.record_expected:(ROOT/'EXPECTED.json').write_bytes(audit.enc(observed))
 else:assert observed==json.loads((ROOT/'EXPECTED.json').read_bytes())
 (a.out/'REPLAY_RECEIPT.json').write_bytes(audit.enc({'outputs':observed,'all_20_outputs_match':True,'accepted_best_unchanged':'VQ20_C622_ROUTE88_118_G12','new_verified_nonwinner':'COORD_PYRAMID_C64_BASE16_G100000_OWN211','terminal':'C64_NONWINNER_AND_HALF_ROUND_SOURCE_ONLY_REPLAY_PASS_NO_NEW_OWN110'}))
 print('C64_NONWINNER_AND_HALF_ROUND_SOURCE_ONLY_REPLAY_PASS_NO_NEW_OWN110',flush=True)
if __name__=='__main__':main()
