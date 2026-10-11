"""Fresh source-only replay; exact Python standard library only."""
import argparse,hashlib,json,shutil,subprocess,sys
from pathlib import Path
sys.set_int_max_str_digits(0);ROOT=Path(__file__).resolve().parent

def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def one(p):
 b=p.read_bytes();return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);ap.add_argument('--resume',action='store_true');args=ap.parse_args();out=args.out.resolve();out.mkdir(parents=True,exist_ok=args.resume)
 meta=json.loads((ROOT/'EXPECTED.json').read_text())
 for n,h in meta['sources'].items():
  assert one(ROOT/n)==h,n
  if (out/n).exists():assert args.resume and one(out/n)==h,n
  else:shutil.copyfile(ROOT/n,out/n)
 shutil.copyfile(ROOT/'EXPECTED.json',out/'EXPECTED.json')
 def run(*args):subprocess.run([sys.executable,'-B','-S',*map(str,args)],cwd=out,check=True)
 def done(names):return args.resume and all((out/n).exists() and one(out/n)==meta['outputs'][n] for n in names)
 if not done(['PARENT_COMPLEX.json','PARENT_A.json']):run(out/'PARENT.py')
 if not done(['HULL_RAW.json','HULL_COMPLEX.json','BUILD_REPORT.json']):run(out/'BUILD.py')
 if not done(['A.json']):run(out/'check_A.py',out/'HULL_RAW.json',out/'A.json')
 if not done(['B.json']):run(out/'check_B.py',out/'HULL_RAW.json',out/'B.json')
 assert (out/'A.json').read_bytes()==(out/'B.json').read_bytes()
 if not done(['REFERENCE_CENSUS.json']):run(out/'AT_CENTRE.py')
 if not done(['MIN_LINKS_REPORT.json']):run(out/'MIN_LINKS.py')
 sys.path.insert(0,str(out));import centred_mass,check_A,check_B
 a=json.loads((out/'A.json').read_text());bb=json.loads((out/'BUILD_REPORT.json').read_text());assert a['ordinary_volume']==bb['new_volume'] and a['raw_centroid']==bb['new_centroid'];assert (a['V'],a['E'],a['F'])==(163,296,135) and a['counts']==[17,26,41] and a['weak']==[0,0,0]
 cm=centred_mass.run(a);(out/'CENTRED_MASS.json').write_bytes(canon(cm))
 fixtures=[]
 for name,H,c,w in [('tetra',[[-1,-1,-1,1],[-1,1,1,1],[1,-1,1,1],[1,1,-1,1]],[4,4,6],[0,0,0]),('weak_prism',[[1,0,0,1],[-2,3,0,1],[1,-3,0,1],[0,0,1,1],[0,0,-1,1]],[4,4,6],[1,2,3])]:
  x=check_A.run({'H':H});y=check_B.run({'H':H});assert x==y and x['counts']==c and x['weak']==w;fixtures.append({'name':name,'counts':c,'weak':w})
 for n,h in meta['outputs'].items():assert one(out/n)==h,n
 receipt={'status':'COORD_C592_SOURCE_ONLY_TWO_AUDITS_AND_REFERENCE_GAP_PASS','counts':a['counts'],'weak':a['weak'],'VEF':[a[k] for k in ['V','E','F']],'reference_counts':[5,1,4],'reference_weak':[0,0,0],'fixtures':fixtures,'outputs':{n:one(out/n) for n in sorted(meta['outputs'])},'python':sys.version}
 (out/'REPLAY_RECEIPT.json').write_bytes(canon(receipt));print(receipt['status'],flush=True)
if __name__=='__main__':main()
