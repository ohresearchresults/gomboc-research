# material-72c94f7d83eb

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# COORD_C622_GUARDED_LINE_ANCHORED_RECOVERY_V2

This complete loader corrects a delimiter bug in the inline decoder of [internal-source-reference]: an unrestricted split on BEGIN_CORE9_BASE64 finds the decoder's own string literal before the payload. The literal compressed source payload and all body/checker hashes are unchanged. Use this line-anchored decoder instead. It has been exercised on both complete payloads with a deliberate earlier embedded marker string; both complete source-map hashes and every recovered file hash matched. This is a transport correction, not a mathematical or coordinate correction.

Save the code block as RECOVER_GUARDED_V2.py with LF and one trailing LF:1692bytes,SHA256188d4109aaeb7536ee7f4405e6bbe4ba0ca4a22907bb06eb343263f8936f5f4d.

Exact body-core recovery:
python -B -S RECOVER_GUARDED_V2.py CORE CORE9.md NEW_ADDITION
CORE9.md is the complete material [internal-source-reference],22864bytes,SHA256ce6b1895bca09c85cf9658dfd14b4d6790ed7748b4f2875013ebddcab0a06b10.
Expected marker: COORD_C622_GUARDED_CORE9_RECOVERY_PASS.
Then use the unchanged REPLAY_GUARDED_FAMILY.py command from that material with both canonical SCOPED16 dependencies [internal-source-reference] and [internal-source-reference].

Optional numerical-method recovery:
python -B -S RECOVER_GUARDED_V2.py METHODS METHODS22.md NEW_METHODS
METHODS22.md is the companion COORD_C622_GUARDED_NUMERICAL_METHODS22_V1 material,identified independently by the full payload hashes below. Expected marker: COORD_C622_GUARDED_METHODS22_RECOVERY_PASS. Numerical methods are not needed to reconstruct or exactly verify the four fixed rational bodies.

```python
"""Line-anchored recovery, avoiding marker text inside the embedded decoder source."""
import sys,json,base64,lzma,hashlib
from pathlib import Path,PurePosixPath
assert __debug__ and len(sys.argv)==4,'Usage: RECOVER_GUARDED_V2.py CORE|METHODS MATERIAL.md NEW_OUTPUT'
kind=sys.argv[1];specs={'CORE':('CORE9',9,15232,'7803cf928ac05be6507aa35ac2b9c2f71dc20e78d0f7232b5ba10cb9360a3420',11424,'11f349f3924d9a3c857246d71bb155641968ead500cccfed2a271de13fad747c',37306,'ca38598d9a57d510227351cf762adb9cd24025c9de626e3139ddb7647e65ee67'),'METHODS':('METHODS22',22,14304,'e1acba8d1226f4809d37dcb99e4e283fa7744a1e16cbaf5b0ab88c67a2ea8641',10728,'4f55f9470e1845833b386262f3f8955a0064794cae055611b1da9586c6df0775',49212,'2d5d304ea30cc9148452f5b5e4e87713bd4473e2b56209db86937e0100b8dc01')}
tag,count,ns,hs,nx,hx,nb,hb=specs[kind];lines=Path(sys.argv[2]).read_text().splitlines();out=Path(sys.argv[3]);assert not out.exists()
a=[i for i,s in enumerate(lines) if s.strip()=='BEGIN_'+tag+'_BASE64'];z=[i for i,s in enumerate(lines) if s.strip()=='END_'+tag+'_BASE64'];assert len(a)==len(z)==1 and a[0]<z[0]
s=''.join(''.join(lines[a[0]+1:z[0]]).split());h=lambda b:hashlib.sha256(b).hexdigest();assert len(s)==ns and h(s.encode())==hs
xz=base64.b64decode(s,validate=True);assert len(xz)==nx and h(xz)==hx;b=lzma.decompress(xz);assert len(b)==nb and h(b)==hb
m=json.loads(b);assert len(m)==count;out.mkdir(parents=True)
for n,t in sorted(m.items()):
 p=PurePosixPath(n);assert not p.is_absolute() and '..' not in p.parts and isinstance(t,str)
 q=out/n;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(t.encode());print(n,len(t.encode()),h(t.encode()))
print('COORD_C622_GUARDED_'+tag+'_RECOVERY_PASS')
```
