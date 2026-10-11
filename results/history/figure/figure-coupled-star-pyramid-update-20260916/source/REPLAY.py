"""Restore the immutable ATLAS57 parent, regenerate every new endpoint, compare receipts.
Usage: python -B -S source/REPLAY.py --parent-capsule ATLAS57_CAPSULE.b85 --out cold
No network, third-party libraries, prior generated body, or numerical seed is used.
"""
import argparse,base64,hashlib,json,lzma,subprocess,sys
from pathlib import Path,PurePosixPath
sys.set_int_max_str_digits(0)
def sha(b):return hashlib.sha256(b).hexdigest()
def inventory(root):
 return {str(p.relative_to(root)):{'bytes':len(p.read_bytes()),'sha256':sha(p.read_bytes())} for p in sorted(root.rglob('*')) if p.is_file()}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--parent-capsule',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();assert __debug__
 source=Path(__file__).resolve().parent
 for name,spec in json.loads((source/'SOURCE_MANIFEST.json').read_bytes()).items():
  b=(source/name).read_bytes();assert len(b)==spec['bytes'] and sha(b)==spec['sha256'],name
 payload=b''.join(a.parent_capsule.read_bytes().split());assert len(payload)==41775 and sha(payload)=='9372158b106c03f1804a225bf3636814fe72535cdf690bfdd24ba1cf2d61eb9d'
 decoded=lzma.decompress(base64.b85decode(payload));assert len(decoded)==112244 and sha(decoded)=='75670b87e53f119fa26c5127589e0dfb63d5a4ac986cdb755de7e67d5b5d9360'
 files=json.loads(decoded);assert len(files)==26
 work=a.out.resolve();work.mkdir(parents=True,exist_ok=False);parent=work/'parent';parent.mkdir();results=work/'results';results.mkdir()
 for name,text in files.items():
  q=PurePosixPath(name);assert not q.is_absolute() and '..' not in q.parts
  p=parent/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(text.encode('utf-8'))
 for name,spec in json.loads((parent/'MANIFEST.json').read_bytes()).items():
  b=(parent/name).read_bytes();assert len(b)==spec['bytes'] and sha(b)==spec['sha256'],name
 print('ATLAS57_26_EXACT_SOURCES_RESTORED',flush=True)
 commands=[['coupled_trials.py','--parent',str(parent),'--out',str(results/'coupled'),'--audit'],['c80_gate.py','--parent',str(parent),'--out',str(results/'c80')],['round_base_gate.py','--out',str(results/'round_base')],['METRICS.py',str(results)]]
 for cmd in commands:subprocess.run([sys.executable,'-B','-S',str(source/cmd[0]),*cmd[1:]],check=True,cwd=work)
 expected=json.loads((source/'EXPECTED_OUTPUTS.json').read_bytes());actual=inventory(results);assert actual==expected,{'missing':sorted(set(expected)-set(actual)),'extra':sorted(set(actual)-set(expected)),'changed':sorted(k for k in set(actual)&set(expected) if actual[k]!=expected[k])}
 coupled=json.loads((results/'coupled/SUMMARY.json').read_bytes())
 for name,c,counts in [('PAIR',616,[3,2,3]),('COMP111',620,[4,2,4]),('COMP7',620,[6,1,5])]:
  s=coupled[name];assert s['C']==c and s['strict']==counts and s['weak']==[0,0,0] and s['status']=='TWO_FULL_EXACT_AUDITS_AND_JOINT_MASS_BOUND'
 small=json.loads((results/'c80/SUMMARY.json').read_bytes())
 for name,counts in [('C80_ORIGINAL_CENTRED',[2,1,1]),('C80_FORCED_REFERENCE_CENTROID',[2,2,2])]:
  s=small[name];assert s['C']==80 and s['strict']==counts and s['weak']==[0,0,0]
 gates=json.loads((results/'round_base/SUMMARY.json').read_bytes());assert all(s['passes_all_apex_exclusion'] for s in gates.values())
 marker='COLD_SOURCE_ONLY_ALL_FIVE_BODIES_TWO_AUDITS_AND_BOTH_BASE_EXCLUSIONS_PASS_NO_NEW_OWN110'
 receipt={'status':marker,'compared_files':len(actual),'expected_outputs_sha256':sha((source/'EXPECTED_OUTPUTS.json').read_bytes()),'python':sys.version,'dependencies':'Python standard library only; assertions enabled; no site imports','canonical_best_unchanged':'VQ20_C622_ROUTE88_118_G12'}
 (work/'RECEIPT.json').write_text(json.dumps(receipt,sort_keys=True,separators=(',',':')))
 print(marker,flush=True)
if __name__=='__main__':main()
