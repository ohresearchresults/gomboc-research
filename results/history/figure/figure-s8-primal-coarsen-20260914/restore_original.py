from pathlib import Path
import base64,lzma,json,hashlib
chunks=[''.join(Path(f'METHOD_SMALL_{i}of6.b85').read_text().split())for i in range(1,7)]
lens=[8000]*5+[3065]
hashes=['b87e8a75ff69eb4a3f4af5192ce33ac1ccae4d53a1e6a828b0835afd13229185','4cc12e9dd252b9fa6a7e582307058f35edf111855ed4ec7bdb77ea8e015b254e','89a009fa5a74a58ba254c57fddc69984474bbfe5999072c0522919b6b30860d8','dc32a1e5a68a9c82c5d6276cb1d6be4651ebb47371e020097d9b8a72f62e1441','b7e94d9d8af67fde5afeefefeca84fd26389eb538625d173c882f3a68c309a6b','812c287ae02e8a01b5ab1e9b4a6e580e3d087498f4a929c02a162bbf56584b26']
for s,n,h in zip(chunks,lens,hashes):
 assert len(s)==n and hashlib.sha256(s.encode()).hexdigest()==h
s=''.join(chunks)
assert len(s)==43065 and hashlib.sha256(s.encode()).hexdigest()=='be898099f142dc8a7a5121ffdfb973db41dbc6004f32ba7561019361f50f2daa'
b=lzma.decompress(base64.b85decode(s))
assert len(b)==150446 and hashlib.sha256(b).hexdigest()=='d5aceb473245065e1b15f98fc0217dab2ed9549275e055558ccb68d4f50534a8'
f=json.loads(b);assert len(f)==22
p=Path('PRIMAL_METHOD');p.mkdir(exist_ok=False)
for n,t in f.items():
 q=Path(n);assert not q.is_absolute() and '..' not in q.parts
 d=p/q;d.parent.mkdir(parents=True,exist_ok=True);d.write_bytes(t.encode())
for n,v in json.loads(f['MANIFEST.json']).items():
 b=(p/n).read_bytes()
 assert len(b)==v['bytes'] and hashlib.sha256(b).hexdigest()==v['sha256']
print('PRIMAL_METHOD_SOURCE_RECOVERY_PASS',len(f))
