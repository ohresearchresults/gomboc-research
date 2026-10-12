"""Source-only exhaustive replays of finite nonwinning rational constructions.
No saved vertices, mass, A/B record or mechanical witness is supplied as geometry.
"""
import argparse,concurrent.futures,hashlib,json,sys
from pathlib import Path
from types import SimpleNamespace
R=Path(__file__).resolve().parent
sys.set_int_max_str_digits(0)
if not __debug__:raise RuntimeError('Run without -O')
import audit_new,compare_new,check_centre,fixed_chain

def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def sh(b):return hashlib.sha256(b).hexdigest()
def bound_file(p,expected):
 b=p.read_bytes();assert len(b)==expected['bytes'] and sh(b)==expected['sha256'],str(p)
def manifest_check():
 m=json.loads((R/'SOURCE_MANIFEST.json').read_text())
 for n,h in m.items():assert sh((R/n).read_bytes())==h,n
 return sh(canon(m))
def one(args):
 alias,out=args;exp=json.loads((R/'EXPECTED.json').read_text())[alias];spec=json.loads((R/'specs'/f'{alias}.json').read_text());path=R/exp['path']
 b=(path/'GENERATOR.json').read_bytes();assert len(b)==exp['normal_generator_bytes']and sh(b)==exp['normal_generator_sha256']
 audit_new.run(SimpleNamespace(generator=path/'GENERATOR.json',out=out))
 bound_file(out/'raw.json',dict(bytes=exp['raw_bytes'],sha256=exp['raw_sha256']))
 z=json.loads((out/'A.json').read_text());raw=json.loads((out/'raw.json').read_text())
 cmp=compare_new.run(z,raw,spec);(out/'COMPARISON.json').write_bytes(canon(cmp))
 for n,e in exp['files'].items():bound_file(out/n,e)
 assert [z[k]for k in ['V','E','F']]==exp['VEF']and z['counts']==exp['counts']and z['weak']==exp['weak']
 assert z['stable_face_ids']==exp['S']and z['unstable_vertices']==exp['U']and z['saddle_edges']==exp['H']
 receipt=dict(alias=alias,status='BQ13_FINITE_NONWINNER_SOURCE_ONLY_TWO_AUDITS_PASS',VEF=exp['VEF'],strict=z['counts'],weak=z['weak'],generator_sha256=sh(b),halfspaces_sha256=sh((out/'raw.json').read_bytes()),complete_AB_sha256=sh((out/'A.json').read_bytes()),whole_parent_complex_comparison_sha256=sh((out/'COMPARISON.json').read_bytes()),centred_mass_sha256=sh((out/'CENTRED_MASS.json').read_bytes()))
 if alias=='TRI9_TRIANGLE9_STEP8':
  cert=json.loads((R/'C602_CENTRE_ACTIVE_TRIPLES.json').read_text());assert sh((out/'A.json').read_bytes())==cert['source_audit_sha256']
  result=check_centre.run(z,cert);(out/'CENTRE_OBSTRUCTION.json').write_bytes(canon(result));receipt['centre_obstruction_sha256']=sh(canon(result));print(result['status'],flush=True)
  links=fixed_chain.run(z);(out/'FIXED_CENTRE_CHAIN.json').write_bytes(canon(links));receipt['fixed_chain_sha256']=sh(canon(links));print(links['status'],flush=True)
 (out/'COLD_RECEIPT.json').write_bytes(canon(receipt));print(receipt['status'],alias,flush=True);return receipt

def main(a):
 mh=manifest_check();exp=json.loads((R/'EXPECTED.json').read_text());names=sorted(exp)if a.object=='ALL'else[a.object];assert all(n in exp for n in names)
 a.out.mkdir(parents=True,exist_ok=False)
 jobs=[(n,a.out/n)for n in names]
 if a.jobs==1:results=[one(j)for j in jobs]
 else:
  with concurrent.futures.ProcessPoolExecutor(max_workers=a.jobs)as ex:results=list(ex.map(one,jobs))
 assert manifest_check()==mh
 summary=dict(status='BQ13_ALL_REQUESTED_SOURCE_ONLY_EXACT_REPLAYS_PASS',source_manifest_sha256=mh,objects=results,python=sys.version)
 (a.out/'COLD_REPLAY_RECEIPT.json').write_bytes(canon(summary));print(summary['status'],len(results),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--object',default='ALL');p.add_argument('--out',type=Path,required=True);p.add_argument('--jobs',type=int,default=1);main(p.parse_args())
