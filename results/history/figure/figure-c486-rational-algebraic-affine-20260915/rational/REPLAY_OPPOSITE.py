"""Source-only C486 own727 nonwinner replay through the durable C592 parent.
Usage: python -B -S REPLAY_OPPOSITE.py CORE_SOURCE C592_SOURCE NEW_DIRECTORY
"""
import json,subprocess,sys
from pathlib import Path
import augment_exact as ag
import verify_opposite
assert __debug__
sys.set_int_max_str_digits(0)
def main():
 core,parent_source,out=map(Path,sys.argv[1:]);here=Path(__file__).resolve().parent
 for n,row in json.loads((here/'MANIFEST.json').read_text()).items():
  b=(here/n).read_bytes();assert len(b)==row['bytes'] and ag.SHA(b)==row['sha256']
 out.mkdir(parents=True,exist_ok=False)
 subprocess.run([sys.executable,'-B','-S',str(parent_source/'REPLAY_C592.py'),str(core),str(out/'C592')],check=True)
 ag.run(out/'C592',out/'C486')
 sys.path.insert(0,str(core));import check_A,check_B
 raw=json.loads((out/'C486/raw.json').read_bytes())
 for label,fn in [('A',check_A.run),('B',check_B.run)]:
  b=ag.B(fn(raw));assert len(b)==302426 and ag.SHA(b)=='8ee12742068e4246b3b7daf688703b3ce6f1c9803202a7d05f96e3ad8806ac21'
  (out/'C486'/f'{label}.json').write_bytes(b)
  print('FULL_EXACT_OPPOSITE_C486',label,flush=True)
 verify_opposite.run(core,out/'C592',out/'C486')
 for name,record in json.loads((here/'EXPECTED.json').read_text()).items():
  b=(out/'C486'/name).read_bytes();assert len(b)==record['bytes'] and ag.SHA(b)==record['sha256']
 print('SOURCE_ONLY_C486_OPPOSITE_R12_OWN727_REPLAY_PASS',flush=True)
if __name__=='__main__':main()
