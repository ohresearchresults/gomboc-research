from pathlib import Path
import sys,json,hashlib,time
p=Path(__file__).resolve().parents[1];src=p/'sources/full76/decoded'
sys.path[:0]=[str(src/'methods'),str(src/'methods/parent')]
import G_FREE_CODEC,RECONSTRUCT,check_B
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
out=p/'artifacts/baseline';out.mkdir(exist_ok=True)
gen=G_FREE_CODEC.decode(json.loads((src/'inputs/C622_ROUTED.json').read_text()))
raw=RECONSTRUCT.recover(gen)
(out/'generator.json').write_bytes(B(gen));(out/'H_exact.json').write_bytes(B(raw))
print('Reconstructed supports',len(raw['H']),'largest bits',max(abs(x).bit_length() for r in raw['H'] for x in r),flush=True)
t=time.time();rep=check_B.run(raw)
w=json.loads((src/'EXPECTED.json').read_text())['cases']['C622_ROUTED'];h=hashlib.sha256(B(rep)).hexdigest();assert h==w['report_sha256']
(out/'B_exact.json').write_bytes(B(rep))
print('EXACT BASELINE',*[rep[k] for k in ('V','E','F','counts','weak')],h,'seconds',time.time()-t,flush=True)
