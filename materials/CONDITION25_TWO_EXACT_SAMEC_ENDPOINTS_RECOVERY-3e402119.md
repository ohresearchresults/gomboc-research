# material-3e402119afca

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---

# Two exact same-C own110 endpoints — complete recovery capsule

## Exact identities and scope
COORD_C622_CONDITION25_EXT11_G12 and COORD_C622_EDGE131135_V2_30_G12 are two DISTINCT homogeneous filled convex own-centroid bodies. Both are V176/E311/F137,C622,strict110,weak000,all equilibrium primitives nonzero,Ssupport3,Urawlex94. Neither improves complexity. Both independent exhaustive rational auditors agree, and a third centered-integer integration over348positive tetrahedra gives the same volume and exactly zero first moments.

CONDITION25_EXT11: continuation from CONDITION25 requested25stages/factor1.6, stopped after11attempts with4successful new targets. Numerical minangular4.865139689999497e-7. Exact balanced rooted trees both >1/2100000. A=B312607bytes SHA5de9ea2d20a11c9b3c6b43847a23164e1a12e731111df2328ab9570f70f29b19;centered denominator56982bits. Minimal recovery generator11841bytes SHA6fa9bd0f16ced1f6aa3066f376562281cbebeebe6be02b8d86d3c3cfe5fcb04d.
EDGE131135_V2_30: signed-edge continuation30attempts,initialfraction.075,inner35,eqtol1e-7,gamma1e-8,trust.1,qbound.01,grid1e12. Parent-labeled131–135 length ratio numerically.8877255326316954,about11.2%shorter; the edge did NOT collapse. A=B312192bytes SHA8c61f1af8ff36da3c2478ae08778e3ba2a158edaad2bf53955bd689773da3d96;centered denominator56866bits. Minimal recovery generator11841bytes SHA9a6eefa37779271b565a10e671d027a63680d2a5b78e8cde72d1862c204ce333. Both exact balanced trees >1/1000000000,depths94/75. The physical tree differs from the parent's tree in11arrows; blindly reusing the old tree fails and was NOT treated as body failure.

## Complete durable source closure
This material plus ALL THREE CONDITION25 source materials is sufficient, without any originating sandbox or numerical optimization:
[internal-source-reference] SHA20469536cc4461b597cd92b9c7420b89ad4f1efd82ef72aa4f934b9bb772067a;
[internal-source-reference] SHAa527d91c2ba70ee5220ca4b6ba30964e804fd4fa52a8619d3ae6567608cc8087;
[internal-source-reference] SHAecb59180686fbea53343e4b78e64b70478df5ede3679acd200c163185c1e29d4.
Decode their complete24-file dictionary into SOURCE. All deterministic generator metadata, plan, contacts and original controls are taken literally from that parent. This capsule supplies every changed FREE coordinate as an integer delta at grid1e12, in the complete314-element ordering explicitly defined by REPLAY_TWO.py. Solved coordinates and the fixed apex are recomputed exactly. Constrained-control placeholders left unchanged make the minimal recovery generator bytes differ from the original search dump, but RECONSTRUCT equality of the full exact H representation was checked for both bodies. Thus these are identical exact bodies, not approximate aliases.

Payload no-whitespace length5900 SHA256ef74bf7dd77b0a2af2b659277b6be39069d94483d41b2df1d84b43ea14f6728c; decoded8728bytes SHA256b5865a3eb42ca37f36c66015324848b5fba8d8af98364bc97b171e0a49f0f343. The data contain BOTH full314delta arrays, complete expected generator/raw/A/B/mass/cost hashes and exact receipts. No omitted rows. Standard-library replay CPython3.13.5; search dependencies NumPy2.3.5/SciPy1.17.0 are NOT needed for exact recovery.

Save this whole material as MATERIAL.md and the complete code below as REPLAY_TWO.py. Command `python -B -S REPLAY_TWO.py MATERIAL.md SOURCE NEW_OUTPUT`. Never use -O. Expected terminal CONDITION25_TWO_SAMEC_EXACT_AB_MASS_GATES_COLD_PASS. All16body output files (eight per body) are byte/hash checked. The final receipt names both bodies and expressly disclaims a smaller edge record. Numerical methods are separately preserved in the original parent capsule and CONTACT_CONTINUATION sources [internal-source-reference] + [internal-source-reference]; they are not dependencies of this exact replay.

### REPLAY_TWO.py
```python
import argparse,base64,copy,concurrent.futures,hashlib,json,re,subprocess,sys,zlib
from pathlib import Path
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
assert __debug__
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
H=lambda b:hashlib.sha256(b).hexdigest()
def main():
 p=argparse.ArgumentParser();p.add_argument('material',type=Path);p.add_argument('source',type=Path);p.add_argument('out',type=Path);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=False)
 s=a.material.read_text();m=re.findall(r'```base64\s*([A-Za-z0-9+/=\s]+)```',s);assert len(m)==1;b=''.join(m[0].split()).encode();assert len(b)==5900 and H(b)=='ef74bf7dd77b0a2af2b659277b6be39069d94483d41b2df1d84b43ea14f6728c';b=zlib.decompress(base64.b64decode(b,validate=True));assert len(b)==8728 and H(b)=='b5865a3eb42ca37f36c66015324848b5fba8d8af98364bc97b171e0a49f0f343';data=json.loads(b)
 for name,w in json.loads((a.source/'MANIFEST.json').read_text()).items():
  b=(a.source/name).read_bytes();assert len(b)==w['bytes'] and H(b)==w['sha256'],name
 b=(a.source/'GENERATOR.json').read_bytes();assert len(b)==11841 and H(b)=='8b8c74c7995098ff531e5d7652da20c1afa9cbaefaeea42cd78ea54e3e7e86f5';base=json.loads(b);axes={i:ax for i,deps,ax in base['plan']};free=[(i,k) for i in range(len(base['controls'])) if i!=base['n_supports'] for k in range(3) if k not in axes[i]];assert len(free)==314
 sys.path[:0]=[str(a.source),str(a.source/'methods/parent')];import RECONSTRUCT,centred_mass;from EXACT_ROUTE_GATE import verify
 receipts={}
 for name,obj in data.items():
  d=a.out/name;d.mkdir();G=copy.deepcopy(base);assert len(obj['delta_free'])==314
  for (i,k),v in zip(free,obj['delta_free']):G['controls'][i][k]+=v
  raw=RECONSTRUCT.recover(G);(d/'GENERATOR.json').write_bytes(B(G));(d/'RAW.json').write_bytes(B(raw))
  def audit(w):
   rr=subprocess.run([sys.executable,'-B','-S',str(a.source/'methods/parent'/('check_'+w+'.py')),str(d/'RAW.json'),str(d/(w+'.json'))],capture_output=True,text=True);assert rr.returncode==0,(w,rr.stderr[-3000:]);print(rr.stdout,end='',flush=True)
  with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:list(pool.map(audit,['A','B']))
  ab=(d/'A.json').read_bytes();assert ab==(d/'B.json').read_bytes();r=json.loads(ab);assert [r[k] for k in ['V','E','F']]==[176,311,137] and r['counts']==[1,1,0] and r['weak']==[0,0,0];assert [r[k] for k in ['face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']]==[0,0,0]
  mass=centred_mass.run(r);(d/'MASS.json').write_bytes(B(mass))
  def stats(v):
   v=list(map(F,v));return [max(abs(x.numerator).bit_length() for x in v),max(x.denominator.bit_length() for x in v)]
  costs=dict(planes=max(abs(x).bit_length() for row in raw['H'] for x in row),vertices=stats([x for row in r['raw_vertices'] for x in row]),centroid=stats(r['raw_centroid']),first_moments=stats(r['raw_first_moments']),volume=stats([r['ordinary_volume']]));(d/'COSTS.json').write_bytes(B(costs))
  for fn,w in obj['expected'].items():
   b=(d/fn).read_bytes();assert len(b)==w['bytes'] and H(b)==w['sha256'],(name,fn)
  gate=json.loads((a.source/'GATE_INPUT.json').read_text())
  if 'gate_margin' in obj:
   gate['margin']=obj['gate_margin'];expected_gate=obj['gate_expected']
  else:
   gate['margin']=[1,1000000000]
   for i,old,new in [(38,40,41),(40,50,36),(41,36,50),(51,41,40),(91,96,93),(131,135,134),(134,130,137),(135,138,130),(137,134,143),(138,143,135),(141,137,138)]:
    assert gate['systems'][0]['parents'][i]==old;gate['systems'][0]['parents'][i]=new
   expected_gate={'GATE_INPUT.json':{'bytes':1104,'sha256':'320decb3c11e36f56f8f14ddc23a71cc7b388f6609ba6946d89efc54ab714e22'},'GATE_REPORT.json':{'bytes':347,'sha256':'da7b9c47c9c68bf50f1a470c7ea81736ce50a0ec7a88ea1991488463147be094'}}
  gr=verify(r,gate);(d/'GATE_INPUT.json').write_bytes(B(gate));(d/'GATE_REPORT.json').write_bytes(B(gr))
  for fn,w in expected_gate.items():
   b=(d/fn).read_bytes();assert len(b)==w['bytes'] and H(b)==w['sha256'],(name,fn)
  receipts[name]=dict(C=622,VEF=[176,311,137],strict=r['counts'],weak=r['weak'],mass=mass,costs=costs,gate=gr)
 result={'marker':'CONDITION25_TWO_SAMEC_EXACT_AB_MASS_GATES_COLD_PASS','bodies':receipts,'scope':'Two distinct same-C own110 bodies. No smaller complexity claimed.'};(a.out/'RECEIPT.json').write_bytes(B(result));print(B(result).decode(),flush=True)
if __name__=='__main__':main()
```

```base64

[Encoded source block omitted; the code in this passage is incomplete.]
