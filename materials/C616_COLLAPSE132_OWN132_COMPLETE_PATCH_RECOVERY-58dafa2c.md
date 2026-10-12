# material-58dafa2c45ec

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Complete recovery: COORD_C616_COLLAPSE132_OWN132

A distinct exact rational non-winner derived from COORD_C620_ALLWITNESS174_G12_OWN132. The contact operation forces support105 through point-control168 by solving its x coordinate, then topologically reorders the contact DAG. It collapses the predecessor's nearlycoincident raw-lex173–174 edge, but also makes input support84 redundant. Therefore the actual maximal complex is V174/E308/F136,C616, NOT C618 based on an assumed single-edge operation. Exact independent A/B and third centered mass integration give own132weak000,primitivezero000,S=input3,Urawlex94/166/173,H166–168 and172–173. 344positive tetrahedra, exact zero centered first moments;common centered denominator and coordinate maximum56869bits. No own110 achieved, and this is not an alias of the old delete99/117 C616 own121 bodies.

Complete dependencies: parent generator and audit_contact_checkpoint.py from [internal-source-reference], plus all THREE CONDITION25 source parts [internal-source-reference],[internal-source-reference],[internal-source-reference]. No numerical rerun and no original sandbox required. The complete deterministic patch below produces every exact input coordinate through the inherited complete contact generator. CPython3.13.5 standard library, assertions enabled.

Save following code as COLLAPSE132_REPLAY.py with final newline:2241bytes SHA256bf63f8c65d33dcbe3ef581fbc43214d5e99712a5a59595bee5d62d40a3e5ce21. Run `python -B -S COLLAPSE132_REPLAY.py collapse132_replay`, where the output directory does not yet exist. The generic audit emits CONTACT_CHECKPOINT_EXACT_AB_MASS_PASS; the wrapper expected terminal marker is C616_COLLAPSE132_EXACT_OWN132_REPLAY_PASS. The underlying generated body, both exact audits and mass were executed before storing this capsule; the wrapper encodes those exact observed output hashes.

```python
"""Recover a distinct C616 own132 contact-collapse non-winner, with exact A/B/mass."""
from pathlib import Path
import argparse,copy,hashlib,json,subprocess,sys
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
H=lambda x:hashlib.sha256(x).hexdigest()
def topological(plan,fixed):
 pending={int(i):(list(ds),list(ax)) for i,ds,ax in plan};out=[];seen=set(fixed)
 while pending:
  available=[i for i,(ds,ax) in pending.items() if set(ds)<=seen]
  if not available:raise ValueError('contact dependency cycle')
  for i in available:
   ds,ax=pending.pop(i);out.append([i,ds,ax]);seen.add(i)
 return out
p=argparse.ArgumentParser();p.add_argument('out');a=p.parse_args()
b=(ROOT/'shape_174_w1.0/GENERATOR.json').read_bytes();assert len(b)==11931 and H(b)=='38ebffa8f00ba3b67e105463bf162f8ac766ce2d738bf3e7a8271539d8d05cd6'
G=json.loads(b);G['groups'][168-137].append(105);G['groups'][168-137].sort();G['plan']=topological([[i,[168],[0]] if i==105 else [i,ds,axes] for i,ds,axes in G['plan']],[137]);b=B(G)
assert len(b)==11939 and H(b)=='4eb48034bf6d6d429c593977bee2b934759ba2c3a22865788880d4e18741720a'
q=ROOT/'COLLAPSE132_GENERATOR.json';q.write_bytes(b)
r=subprocess.run([sys.executable,'-B','-S',str(ROOT/'audit_contact_checkpoint.py'),str(q),a.out]);assert r.returncode==0
out=Path(a.out);receipt=json.loads((out/'RECEIPT.json').read_bytes());rr=json.loads((out/'A.json').read_bytes())
assert receipt['VEF']==[174,308,136] and receipt['strict']==[1,3,2] and receipt['weak']==[0,0,0]
assert rr['active_input_indices']==[i for i in range(137) if i!=84]
assert rr['unstable_vertices']==[94,166,173] and rr['saddle_edges']==[[166,168],[172,173]]
expected={'RAW.json':(15729,'6164d7be054148ebfa11a8c23edb448e94de6e7d84d5dd78d6b8a24b096f06f9'),'A.json':(312051,'ba4bd93b8fade753cea37dc5a7b36f030fc2d55127fb7c043e01893f4ff94eb9'),'B.json':(312051,'ba4bd93b8fade753cea37dc5a7b36f030fc2d55127fb7c043e01893f4ff94eb9'),'MASS.json':(223,'c00ede7e489ae618498a95fc114aa9e886af03807bdc9b814ed02ac7202f58af')}
for name,(n,h) in expected.items():
 b=(out/name).read_bytes();assert len(b)==n and H(b)==h,name
print('C616_COLLAPSE132_EXACT_OWN132_REPLAY_PASS',flush=True)
```
Expected COLLAPSE132_GENERATOR.json11939bytes SHA4eb48034bf6d6d429c593977bee2b934759ba2c3a22865788880d4e18741720a. Output RECEIPT.json944bytes SHAb317c04325f0ff87632841bda92faed8c476071e39325f18d52812d1ab10ad67. Full RAW/A/B/MASS names, bytes and hashes are in the complete wrapper. The inherited137 support rows contain exactly136 active facets, with84 inactive; count true maximal edges308 rather than preserving the predecessor's combinatorial label.
