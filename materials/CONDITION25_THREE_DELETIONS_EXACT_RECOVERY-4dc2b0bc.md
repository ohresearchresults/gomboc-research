# material-4dc2b0bc7178

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# CONDITION25_THREE_DELETIONS_EXACT_V1

## Complete durable dependency closure
This material plus ALL THREE immutable CONDITION25 source materials is a complete recovery capsule, requiring no originating sandbox:
- [internal-source-reference] SHA25620469536cc4461b597cd92b9c7420b89ad4f1efd82ef72aa4f934b9bb772067a;
- [internal-source-reference] SHA256a527d91c2ba70ee5220ca4b6ba30964e804fd4fa52a8619d3ae6567608cc8087;
- [internal-source-reference] SHA256ecb59180686fbea53343e4b78e64b70478df5ede3679acd200c163185c1e29d4.
Decode their complete24-file dictionary into PARENT_SOURCE following their literal decoder. Joined no-whitespace base64:36568characters SHA2566311ad9802f5a98c2600fa2d856a64af0f7a19d055c2d9849e0080c141f00c50; decoded93169bytes SHA256631fae9cb3d532ace34aa06230c4a5a1c03aec1d99055805e536d2442cb697b3. Correct individual payload hashes are part1 length12500 SHA50dca34f775fb0b723842e98a1a1ad79c2705951dfbfbbb536cbec1fc81b0889; part2 length12500 SHA4a6c34e32330e51f2dccaa3da5cc22878eb4db2e67e978603f62a87b1555075b; part3 length11568 SHA583e12be855d70962ae95fb2dba8ffcdc1213d74758af816baba614f2187554b. The previous brief's first two individual payload hashes were wrong, not the immutable source data.

## Exact nonwinner identities
Independently delete original support84,99,117 from the exact COORD_C622_CONDITION25_G12 parent. Never combine deletions. Each resulting homogeneous filled convex body's exact equilibria at its OWN volume centroid are strict(1,2,1), weak000, all equilibrium primitives nonzero. These are NOT improvements of the own110 record.
DELETE84: V175/E309/F136,C618; own raw-lex Sface3,U94,174,H173–174; A=B311334bytes SHA256dd210cadc9c079299083309acb31d6bb8fdf7d5fdd29787f4e9899d1b0ebab74;346positive centered tetrahedra; common denominator56713bits.
DELETE99: V174/E308/F136,C616;S3,U94,144,H144–145;A=B310157bytes SHA256af5e1884bf301785a618928bf9ccbd44e965391ee964fd24f7e4cdf0cdaac85d;344positive centered tetrahedra;den56471bits.
DELETE117: V174/E308/F136,C616;S3,U79,92,H79–82;A=B309887bytes SHA2563832d35b39b5e70cef5c21cfdd3cc5bb91985ba376324574200ddd287eb48446;344positive centered tetrahedra;den56416bits.
A and B independently reconstruct the maximal complex and integrate its filled mass. A uses all support triples and cone boundedness; B clips supporting-plane intersection lines, independently builds maximal polygonal faces and integrates about a different interior point. The third centered-integer integration uses rotated face fans, requires every tetrahedron positive, repeats the volume and gives exactly zero first moments. Source-only cold replay of all15 expected files completed in the current coordinator turn. DELETE84's transient summary 309879bytes/SHA93f25c.../den56198 does not describe this recipe; the explicit recipe and dd210cad... output are authoritative. Each object's labels are its own raw-lex/active-facet labels, not parent aliases.

## Reconstruct and verify
CPython3.13.5; standard library only. Save REPLAY.py and EXPECTED.json below into a new RECOVERY directory. Copy precisely these five files from decoded PARENT_SOURCE into RECOVERY, verifying their bytes/SHA256:
GENERATOR.json ← GENERATOR.json,11841,8b8c74c7995098ff531e5d7652da20c1afa9cbaefaeea42cd78ea54e3e7e86f5.
RECONSTRUCT.py ← methods/parent/RECONSTRUCT.py,1801,2a8c5685baa64c8a2e6998f898c889172b7c7f92fbf07ae9cf1d8b8d37e695fd.
check_A.py ← methods/parent/check_A.py,5483,ad72cc198140249c1e52a615513354036c04f4c718333a7beed64fba4b43d7f3.
check_B.py ← methods/parent/check_B.py,6351,b0cb62d5486b32d020b60f717f3dfe9d07c6c9a978492928f54c3a38f396fc24.
centred_mass.py ← methods/parent/centred_mass.py,1328,cc0ad7d58764902ca3d308539f7a133eec0f6fb2389361444808ca92694499a5.
Use the complete ASSEMBLE.py below to do that and generate MANIFEST.json. Commands:
`python -B -S ASSEMBLE.py PARENT_SOURCE`
`python -B -S REPLAY.py NEW_OUTPUT --workers 2`
Never use -O. Expected terminal marker CONDITION25_THREE_DELETIONS_EXACT_AB_CENTRED_MASS_COLD_PASS. Expected output filenames, bytes and SHA256 are complete below. The final receipt also supplies arithmetic costs and equilibrium locations.

### ASSEMBLE.py
```python
import sys,json,hashlib
from pathlib import Path
p=Path(sys.argv[1]);o=Path(__file__).resolve().parent
sources={
 'GENERATOR.json':('GENERATOR.json',11841,'8b8c74c7995098ff531e5d7652da20c1afa9cbaefaeea42cd78ea54e3e7e86f5'),
 'RECONSTRUCT.py':('methods/parent/RECONSTRUCT.py',1801,'2a8c5685baa64c8a2e6998f898c889172b7c7f92fbf07ae9cf1d8b8d37e695fd'),
 'check_A.py':('methods/parent/check_A.py',5483,'ad72cc198140249c1e52a615513354036c04f4c718333a7beed64fba4b43d7f3'),
 'check_B.py':('methods/parent/check_B.py',6351,'b0cb62d5486b32d020b60f717f3dfe9d07c6c9a978492928f54c3a38f396fc24'),
 'centred_mass.py':('methods/parent/centred_mass.py',1328,'cc0ad7d58764902ca3d308539f7a133eec0f6fb2389361444808ca92694499a5')}
for target,(name,n,h) in sources.items():
 b=(p/name).read_bytes();assert len(b)==n and hashlib.sha256(b).hexdigest()==h,name;(o/target).write_bytes(b)
manifest={name:{'bytes':(o/name).stat().st_size,'sha256':hashlib.sha256((o/name).read_bytes()).hexdigest()} for name in [*sources,'REPLAY.py','EXPECTED.json']}
(o/'MANIFEST.json').write_text(json.dumps(manifest,sort_keys=True,separators=(',',':')))
print('THREE_DELETION_RECOVERY_SOURCES_ASSEMBLED')
```

### REPLAY.py
```python
"""Source-only exact reconstruction and independent audits of three nonwinners."""
import sys,json,hashlib,subprocess,argparse,concurrent.futures
from pathlib import Path
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
assert __debug__
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
import RECONSTRUCT,centred_mass
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
H=lambda x:hashlib.sha256(x).hexdigest()

def costs(raw,r):
 def one(key):
  v=r[key];v=[x for row in v for x in row] if key=='raw_vertices' else v;v=list(map(F,v))
  return dict(numerator=max(abs(x.numerator).bit_length() for x in v),denominator=max(x.denominator.bit_length() for x in v))
 V=F(r['ordinary_volume'])
 return dict(raw_planes=max(abs(x).bit_length() for row in raw['H'] for x in row),raw_vertices=one('raw_vertices'),raw_centroid=one('raw_centroid'),raw_first_moments=one('raw_first_moments'),ordinary_volume=[abs(V.numerator).bit_length(),V.denominator.bit_length()])

def main():
 p=argparse.ArgumentParser();p.add_argument('out',type=Path);p.add_argument('--workers',type=int,default=2);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=False)
 for name,w in json.loads((ROOT/'MANIFEST.json').read_text()).items():
  b=(ROOT/name).read_bytes();assert len(b)==w['bytes'] and H(b)==w['sha256'],name
 exp=json.loads((ROOT/'EXPECTED.json').read_text());parent=RECONSTRUCT.recover(json.loads((ROOT/'GENERATOR.json').read_text()))
 for f in [84,99,117]:
  d=a.out/str(f);d.mkdir();(d/'RAW.json').write_bytes(B({'H':[r for i,r in enumerate(parent['H']) if i!=f]}))
 def audit(job):
  f,w=job;d=a.out/str(f)
  r=subprocess.run([sys.executable,'-B','-S',str(ROOT/('check_'+w+'.py')),str(d/'RAW.json'),str(d/(w+'.json'))],capture_output=True,text=True)
  assert r.returncode==0,(f,w,r.stderr[-3000:]);print(r.stdout,end='',flush=True)
 with concurrent.futures.ThreadPoolExecutor(max_workers=a.workers) as pool:list(pool.map(audit,[(f,w) for f in [84,99,117] for w in ['A','B']]))
 receipt={}
 for f in [84,99,117]:
  d=a.out/str(f);ab=(d/'A.json').read_bytes();assert ab==(d/'B.json').read_bytes();r=json.loads(ab);raw=json.loads((d/'RAW.json').read_text())
  assert [r[k] for k in ['V','E','F']]==([175,309,136] if f==84 else [174,308,136])
  assert r['counts']==[1,2,1] and r['weak']==[0,0,0]
  assert all(r[k]==0 for k in ['face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count'])
  mass=centred_mass.run(r);(d/'MASS.json').write_bytes(B(mass));c=costs(raw,r);(d/'COSTS.json').write_bytes(B(c))
  receipt[str(f)]=dict(VEF=[r[k] for k in ['V','E','F']],C=2*r['E'],strict=r['counts'],weak=r['weak'],S=r['stable_face_ids'],U=r['unstable_vertices'],H=r['saddle_edges'],mass=mass,costs=c,report_bytes=len(ab),report_sha256=H(ab))
 for name,w in exp.items():
  b=(a.out/name).read_bytes();assert len(b)==w['bytes'] and H(b)==w['sha256'],name
 result=dict(marker='CONDITION25_THREE_DELETIONS_EXACT_AB_CENTRED_MASS_COLD_PASS',scope='Three exact own121 nonwinners. No new own110 complexity record.',bodies=receipt)
 (a.out/'RECEIPT.json').write_bytes(B(result));print(B(result).decode(),flush=True)
if __name__=='__main__':main()
```

### EXPECTED.json
```json
{"84/RAW.json":{"bytes":15450,"sha256":"cb0d03173a53828f3c4f6bc0bb74d80122e61f4be3ff78c8741d2e3b7431793d"},"84/A.json":{"bytes":311334,"sha256":"dd210cadc9c079299083309acb31d6bb8fdf7d5fdd29787f4e9899d1b0ebab74"},"84/B.json":{"bytes":311334,"sha256":"dd210cadc9c079299083309acb31d6bb8fdf7d5fdd29787f4e9899d1b0ebab74"},"84/MASS.json":{"bytes":223,"sha256":"dfc184c30758403a2d7d3cc15841fb03e5a535c99eec1b6178e290c6b6b27a6f"},"84/COSTS.json":{"bytes":216,"sha256":"9af09ffea2f0c31dc0ce3986c1e3fdf65581191a61fc33a36778b79a0878299e"},"99/RAW.json":{"bytes":15494,"sha256":"e75de9cc7ffc220200ec5634961a9eed11c974b26c8ebcf84c8f9272bbf47d93"},"99/A.json":{"bytes":310157,"sha256":"af5e1884bf301785a618928bf9ccbd44e965391ee964fd24f7e4cdf0cdaac85d"},"99/B.json":{"bytes":310157,"sha256":"af5e1884bf301785a618928bf9ccbd44e965391ee964fd24f7e4cdf0cdaac85d"},"99/MASS.json":{"bytes":223,"sha256":"c88be080b51351d00b8ce29d6c2e46858d8b8f9372fd601fef715d554629bddd"},"99/COSTS.json":{"bytes":216,"sha256":"c8a783fe0d2bfcf3c6a54bd14c6b2f40317cca1af8c6666bc93c68503a9f4836"},"117/RAW.json":{"bytes":15493,"sha256":"40cf1fc2af6de94aaf421f22be6b25ac2c748f1d11c330fdf2975a75ea517483"},"117/A.json":{"bytes":309887,"sha256":"3832d35b39b5e70cef5c21cfdd3cc5bb91985ba376324574200ddd287eb48446"},"117/B.json":{"bytes":309887,"sha256":"3832d35b39b5e70cef5c21cfdd3cc5bb91985ba376324574200ddd287eb48446"},"117/MASS.json":{"bytes":223,"sha256":"cf38d14312ef93a020c5d704f9395dd309b0ba3d062d552033eb5b93866b7381"},"117/COSTS.json":{"bytes":216,"sha256":"b98cde7204aa7eea7dcbbd41a38c14fc0dd3fd0582d08431c0f0c706720a68d6"}}
```

The optional standalone9-file container source dictionary is34712bytes SHA9ac8ce9e043c8802ba5e7db983bcf54d0998026b31463bc4ce47e58029ff7b05, compressed base64 length18196 SHAe7905bfed86d8a1dfb9cdcc3e7e51a58fb5a264551849d5e7420c516b2a0cabf. That archive is a supplementary copy only: the durable recovery closure is this literal extension and the THREE exact immutable parent materials named above.
