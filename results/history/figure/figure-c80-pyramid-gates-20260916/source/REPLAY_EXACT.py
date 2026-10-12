"""Source-only replay of C80 geometry, filled mass and exactly scoped exclusions."""
import argparse,hashlib,json,subprocess,sys
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('out');a=p.parse_args();root=Path(__file__).resolve().parent;out=Path(a.out).resolve();out.mkdir(parents=True,exist_ok=False)
 m=json.loads((root/'EXACT_MANIFEST.json').read_bytes())
 for name,r in m['sources'].items():
  b=(root/name).read_bytes();assert len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256'],name
 commands=[['exact_points.py',str(root/'C80_POINTS.json'),str(out/'C80'),'--core',str(root/'core')],['axis_certificate.py',str(out/'C80/A.json'),str(out/'axis_y'),'--axis','1'],['diagonal_cover.py',str(out/'C80/A.json'),str(out/'diagonal')],['diagonal_cover.py',str(out/'C80/A.json'),str(out/'diagonal'),'--check'],['reference_gate.py',str(out/'C80/A.json'),str(out/'reference')]]
 for i,c in enumerate(commands):
  r=subprocess.run([sys.executable,'-B','-S',str(root/c[0]),*c[1:]],text=True,capture_output=True,check=True)
  (out/('run_'+str(i)+'.log')).write_text(r.stdout,encoding='utf-8');print(r.stdout.splitlines()[0],flush=True)
 for name,r in m['outputs'].items():
  b=(out/name).read_bytes();assert len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256'],name
 assert (out/'C80/A.json').read_bytes()==(out/'C80/B.json').read_bytes()
 print('C80_EXACT_SOURCE_ONLY_REPLAY_ALL_EXPECTED_BYTES_PASS',len(m['outputs']),flush=True)
if __name__=='__main__':main()
