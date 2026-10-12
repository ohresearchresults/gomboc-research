"""Literal checkpoint and optional mass-correction replay. Exact GENERATOR is authoritative."""
import argparse,hashlib,json,os,shutil,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--proof',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--refine',action='store_true');ap.add_argument('--optimize',action='store_true');a=ap.parse_args()
 proof=a.proof.resolve();out=a.out.resolve();r=json.loads((proof/'RECEIPT.json').read_text());assert r['status']=='VQ20_C626_TWO_EXACT_AUDITS_COLD_SOURCE_ONLY_PASS'
 assert H(proof/'baseline/A.json')=='bb013ccd179cd000f50b09f030b731bd85661d149e9cd2039d08b0952de877c4'
 assert H(proof/'chart_exact.json')=='14b68b4b81fb2b59c7064e55a0203d4f66f79d31ce42d5e596f5f8a4808a46b1'
 out.mkdir(parents=True,exist_ok=False)
 for f in ['contact.py','general_atlas.py','numeric.py','qp.py','REFINE.py','DISCOVERY.json']:shutil.copyfile(ROOT/f,out/f)
 shutil.copytree(ROOT/'parent',out/'parent');shutil.copytree(proof/'baseline',out/'baseline');shutil.copyfile(proof/'chart_exact.json',out/'chart_exact.json')
 code='''from general_atlas import *
from REFINE import correct,warm
from numeric import Chart
import hashlib,sys
sys.path.insert(0,str(ROOT/'parent'));import RECONSTRUCT
p=json.loads((ROOT/'DISCOVERY.json').read_text());Q=np.array([[float.fromhex(v) for v in row] for row in p['initial_Q_hex']]);s=GeneralAtlas(p['edge'],Q);assert s.n==316 and s.patch==p['patch']
c=Chart();w=c.w.copy();w[p['edge']]=0;initial=c.solve(w)[0];initial_difference=float(abs(initial-Q).max());assert initial_difference<1e-9
z=np.array([float.fromhex(v) for v in p['final_z_hex']]);records=[]
if sys.argv[1]=='optimize':z,records=correct(s,warm(s))
elif sys.argv[1]=='refine':z,records=correct(s,np.array([float.fromhex(v) for v in p['warm_z_hex']]))
v,J,g=s.evaluate(z);G=copy.deepcopy(s.G);G['grid']=p['grid'];G['controls']=np.rint(g['Y']*G['grid']).astype(np.int64).tolist();raw=RECONSTRUCT.recover(G)
blob=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
(ROOT/'GENERATOR.json').write_bytes(blob(G));(ROOT/'raw.json').write_bytes(blob(raw));(ROOT/'CORRECTION.json').write_bytes(blob(records))
sha=hashlib.sha256(blob(G)).hexdigest();ok=sha==p['generator_sha256'];receipt=dict(status='IDENTICAL_EXACT_GENERATOR_REPLAY_PASS' if ok else 'DIFFERENT_FLOATING_PROPOSAL_NOT_CERTIFIED',generator_sha256=sha,expected=p['generator_sha256'],mode=sys.argv[1],initial_stress_seed_max_difference=initial_difference,minimum_mechanical=float(v[:s.mechlen].min()),minimum_nonowner_slack=float(g['slack'].min()),free_coordinates=s.n,final_z_hex=[float(x).hex() for x in z]);(ROOT/'DISCOVERY_REPLAY.json').write_bytes(blob(receipt));print(receipt['status'],sha,receipt['minimum_mechanical'],flush=True)
assert ok,'Use the literal exact candidate; floating optimization is not the certificate.'
'''
 (out/'CHECKPOINT_REPLAY.py').write_text(code)
 mode='optimize' if a.optimize else 'refine' if a.refine else 'checkpoint'
 env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
 subprocess.run([sys.executable,'-B',str(out/'CHECKPOINT_REPLAY.py'),mode],cwd=out,env=env,check=True)
if __name__=='__main__':main()
