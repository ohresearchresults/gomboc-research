"""Recover four exact physical bodies; certify each from independent full A/B geometry.
Only Python's standard library is required. Keep assertions enabled.
"""
import argparse,hashlib,json,sys
from pathlib import Path
import RECONSTRUCT,check_A,check_B,centred_mass,check_centre,fixed_chain,proof_checks
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent
blob=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
sha=lambda b:hashlib.sha256(b).hexdigest()
def run(name,out):
 r=json.loads((ROOT/'CASES.json').read_text())[name];b=(ROOT/r['generator']).read_bytes()
 assert len(b)==r['generator_bytes'] and sha(b)==r['generator_sha256']
 gen=json.loads(b);full=RECONSTRUCT.recover(gen)
 raw={'H':[h for i,h in enumerate(full['H']) if i not in r['deleted']]}
 b=blob(raw);assert sha(b)==r['raw_sha256'];out.mkdir(parents=True,exist_ok=False);(out/'raw.json').write_bytes(b)
 a=check_A.run(raw);ab=blob(a);bb=blob(check_B.run(raw));assert ab==bb
 assert len(ab)==r['report_bytes'] and sha(ab)==r['report_sha256']
 assert [a[k] for k in ['V','E','F']]==r['V_E_F'] and a['counts']==r['counts'] and a['weak']==r['weak']
 assert len(a['active_input_indices'])==len(raw['H'])
 (out/'A.json').write_bytes(ab);(out/'B.json').write_bytes(bb)
 mass=centred_mass.run(a);(out/'MASS.json').write_bytes(blob(mass));extra={}
 if name=='BQ13_C602':
  cert=json.loads((ROOT/'C602_CENTRE_ACTIVE_TRIPLES.json').read_text());extra['centre']=check_centre.run(a,cert);extra['chain']=fixed_chain.run(a)
 elif name in ['D16_ONE_GRID7','MARGIN2_GRID6']:
  key='D16_ONE' if name=='D16_ONE_GRID7' else 'MARGIN2'
  spec=json.loads((ROOT/'PROOF_SPECS.json').read_text())[key]
  extra['farkas']=proof_checks.run(a,r['deleted'],spec);extra['preserved146']=proof_checks.preserved_pair(a,r['deleted'])
 (out/'EXTRA.json').write_bytes(blob(extra))
 receipt=dict(name=name,counts=a['counts'],weak=a['weak'],V_E_F=r['V_E_F'],raw_sha256=r['raw_sha256'],report_sha256=r['report_sha256'],common_centred_denominator_bits=mass['common_centred_denominator_bits'],status='FOUR_FRONTIERS_EXACT_CORE_REPLAY_PASS')
 (out/'RECEIPT.json').write_bytes(blob(receipt));print(json.dumps(receipt,sort_keys=True),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--case',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();run(a.case,a.out)
