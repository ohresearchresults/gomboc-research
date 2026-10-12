"""Complete standard-library cold reconstruction and exact checking.
No saved support/vertex/mass/audit/certificate output is used as geometry input.
python -B -S REPLAY.py --out NEW_DIRECTORY
"""
import sys,json,hashlib,argparse,subprocess,concurrent.futures
from pathlib import Path
assert __debug__
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent
import RECONSTRUCT,check_A,check_B,edge_slide_exclusion as producer,edge_slide_verify as independent,edge_endpoint,cap_moment_jacobian,SEPARATORS

def dump(path,value):path.write_text(json.dumps(value,sort_keys=True,separators=(',',':')))
def meta(path):
 b=path.read_bytes();return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def sources():
 m=json.loads((ROOT/'MANIFEST.json').read_text())
 for name,v in m.items():assert meta(ROOT/name)==v,name
 return len(m)+1

def one(case,out):
 sources();k=int(case[3:]);assert k in [99,117,84];out.mkdir(parents=True,exist_ok=False)
 H=RECONSTRUCT.recover(json.loads((ROOT/'BASE_GENERATOR.json').read_text()))['H'];assert len(H)==137;raw={'H':[row for i,row in enumerate(H) if i!=k]};dump(out/'raw.json',raw)
 a=check_A.run(raw);b=check_B.run(raw);assert a==b and a['counts']==[1,2,1] and a['weak']==[0,0,0];dump(out/'A.json',a);dump(out/'B.json',b);print('PARENT_TWO_EXACT_AUDITS_IDENTICAL',case,flush=True)
 # Generate cover afresh; the compact frozen tiles must agree exactly.
 wanted=json.loads((ROOT/'TILES.json').read_text())[str(k)];families=[]
 for old in wanted:
  new=producer.prove(a,old['u'],old['w']);assert all(new[key]==v for key,v in old.items());assert new['status']=='EXACT_TWO_WEAK_UNSTABLE_COVER_PASS';families.append(new)
 cover=dict(parent_sha256=meta(out/'A.json')['sha256'],families=families,claim='For every 0<s<1, each specified homogeneous convex edge-slide has at least two distinct weakly unstable vertices relative to its own exact volume centroid. Hence none has strict110 and weak000. Endpoint s=1 is not included.');dump(out/'COVER.json',cover)
 receipt=independent.verify(a,cover);receipt['cover_sha256']=meta(out/'COVER.json')['sha256'];dump(out/'INDEPENDENT.json',receipt)
 rank=cap_moment_jacobian.run(a);rank['parent_sha256']=meta(out/'A.json')['sha256'];dump(out/'CAP_MOMENT.json',rank);dump(out/'SEPARATORS.json',SEPARATORS.run(a))
 eraw=edge_endpoint.build(a);dump(out/'ENDPOINT_raw.json',eraw);ea=check_A.run(eraw);eb=check_B.run(eraw);assert ea==eb;expected_class={99:[25,36,59],117:[37,48,83],84:[2,3,3]}[k];assert ea['counts']==expected_class and ea['weak']==[0,0,0];assert ea['V']==a['V']-1 and ea['E']==a['E'] and ea['F']==a['F']+1;dump(out/'ENDPOINT_A.json',ea);dump(out/'ENDPOINT_B.json',eb)
 expected=json.loads((ROOT/'EXPECTED.json').read_text())[case]
 for name,v in expected.items():assert meta(out/name)==v,(case,name,meta(out/name),v)
 print('ONE_CASE_FULL_SOURCE_ONLY_CAP_SLIDE_PASS',case,flush=True)

def main():
 p=argparse.ArgumentParser();p.add_argument('--out',required=True,type=Path);p.add_argument('--case',choices=['DEL99','DEL117','DEL84']);args=p.parse_args()
 if args.case:one(args.case,args.out);return
 n=sources();args.out.mkdir(parents=True,exist_ok=False);cases=['DEL99','DEL117','DEL84']
 def job(case):
  with (args.out/(case+'.log')).open('w') as log:subprocess.run([sys.executable,'-B','-S',str(ROOT/'REPLAY.py'),'--case',case,'--out',str(args.out/case)],stdout=log,stderr=subprocess.STDOUT,check=True)
 with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:list(pool.map(job,cases))
 sources();receipt=dict(status='COORD_S8_NINE_SLIDES_TWO_CAPS_SOURCE_ONLY_COLD_PASS',source_files=n,parent_bodies=3,exact_open_interval_families=9,all_interval_covers_independently_checked=True,full_support_complex_and_mass_checked=True,exact_rank_three_centroid_controllers=3,common_slide_endpoints_independently_audited=3,new_own110=False,cases={case:{p.name:meta(p) for p in sorted((args.out/case).glob('*.json'))} for case in cases});dump(args.out/'RECEIPT.json',receipt);print(receipt['status'],flush=True)
if __name__=='__main__':main()
