# material-e977e23e8b16

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: unreviewed-encoded-blocks-omitted.

---

# Recovery capsule part 1/3 — COORD_CORRECT_ROOTS_ADAPTIVE_U_HEMISPHERE_V1

ALL THREE parts required in order. Complete scoped60-file dictionary: corrected literal stable roots and genuinely enforced barycentric constraints (V3); adaptive all-point escape witnesses (V4); rigorous support-hemisphere lemma/checker and hemisphere-aware root switches (V5); all six finite two-stage campaign configurations, retained BEST/TREE/LAST checkpoints, legacy V2 for explicit defect evidence; complete independent exact A/B hull, filled-volume centroid and strict/weak all-feature verification, centered positive tetrahedra, rooted cut/path certificates and deterministic exact rational freezing. The six exact bodies are nonwinners: all V23/E63/F42,C126,weak000. V4 grids1000,100000,1000000,10000000 give own(6,10,14),(6,6,10),(6,1,5),(6,1,5), centered denominator/integer bits47/49,73/74,87/88,101/102. V5 grids1000000,10000000 give own(5,1,4),bits87/89,101/102. Canonical record remains C622. Finite failures are not a family exclusion.

Exact recovered-source replay succeeded with final marker COORD_CORRECT_ROOTS_ADAPTIVE_U_HEMISPHERE_SIX_NONWINNERS_SOURCE_ONLY_PASS. Every recovery file has bytecount/hash in MANIFEST.json; all12 generated body/rooted report filenames, bytecounts and SHA256 values are in EXPECTED_V4_LEDGER.json and EXPECTED_V5_LEDGER.json. Additional generated HEMISPHERE_CERTIFICATES.json9472bytes SHA256235c0481b338f21ca289c3229df1a466638380662d0ac8c785b14283fbae6812. All six final rational bodies still contain the old reference unit disk: do not claim V5 broke that disk. Parent passes both sufficient hemisphere tests; V4 passes only positive; V5 passes neither. Failing a sufficient test does not prove absence of stable equilibria.

CPython3.13.5 standard library suffices for recovery/replay; assertions mandatory, no optimizer required. Numerical producer versions were NumPy2.3.5,SciPy1.17.0,Torch2.10.0+cpu,one thread,all exact nondefaults in CONFIG and README. Numeric reruns are not promised byte-identical; deterministic reconstruction starts at preserved exact hexadecimal inputs. V4B retained actual escape positivity but missed its requested1e-5 optimization margin, as README explicitly distinguishes; complete rational verification is the equilibrium evidence.

Save this and next two materials as part1.md,part2.md,part3.md. Save the complete loader below as RECOVER_CORRECT_ROOTS_HEMISPHERE.py,1616bytes SHA256b155240f4bbe7a779a73bbc762ae5262c5f920c6da637ac76b218b7b35bb5457. Run `python -B -S RECOVER_CORRECT_ROOTS_HEMISPHERE.py part1.md part2.md part3.md recovered`; marker CORRECT_ROOTS_HEMISPHERE_SIXTY_SOURCE_FILES_RECOVERED. Then run `python -B -S recovered/REPLAY_VERIFIED.py` for the full final marker above. Loader has been tested with all three complete local payloads; stored-material rereading is a separate transport operation, not claimed here.

Whitespace-stripped base64 parts:1=11512bytes SHA256bfcd1a6ecad726d25ae72c96100708ec73ad75836016d8dc18521aab46c03f89;2=11512bytes SHA25659e73e68bf070775acd97e3919faeade1835fcecc66cddd65da51d856ddc9dcf;3=11516bytes SHA256df611929022663ee7b7bd97e06b7ad805909c2a03ae2df45b65d83593a0db981. Combinedbase6434540bytes SHA25601f8991b43bb60b162f549f03a4b191f234f66aae5f2d74f6fa1ac36ecce9a97. XZ25904bytes SHA256ed9757595ba812ac53dc586ae30e4916ccc42bab89a7f65c6ea469711ae82743. Dictionary152827bytes SHA2566d33993f5da52a8dd71564a5733b8683f483e793d497c164b9a739b3d2a6926e. The dictionary itself and all exact inputs are preserved by the three literal payloads, not merely by these hashes.

```python
#!/usr/bin/env python3
import base64,hashlib,json,lzma,re,sys
from pathlib import Path
assert __debug__ and len(sys.argv)==5,'three material Markdown files and output directory required'
parts=[]
for fn in sys.argv[1:4]:
 blocks=re.findall(r'(?ms)^```text\n(.*?)^```[ \t]*$',Path(fn).read_text())
 assert len(blocks)==1
 parts.append(''.join(blocks[0].split()))
expected=[(11512,'bfcd1a6ecad726d25ae72c96100708ec73ad75836016d8dc18521aab46c03f89'),(11512,'59e73e68bf070775acd97e3919faeade1835fcecc66cddd65da51d856ddc9dcf'),(11516,'df611929022663ee7b7bd97e06b7ad805909c2a03ae2df45b65d83593a0db981')]
for p,(n,h) in zip(parts,expected):assert len(p)==n and hashlib.sha256(p.encode()).hexdigest()==h
s=''.join(parts);assert len(s)==34540 and hashlib.sha256(s.encode()).hexdigest()=='01f8991b43bb60b162f549f03a4b191f234f66aae5f2d74f6fa1ac36ecce9a97'
z=base64.b64decode(s,validate=True);assert len(z)==25904 and hashlib.sha256(z).hexdigest()=='ed9757595ba812ac53dc586ae30e4916ccc42bab89a7f65c6ea469711ae82743'
b=lzma.decompress(z);assert len(b)==152827 and hashlib.sha256(b).hexdigest()=='6d33993f5da52a8dd71564a5733b8683f483e793d497c164b9a739b3d2a6926e'
f=json.loads(b);assert len(f)==60
out=Path(sys.argv[4]);out.mkdir(exist_ok=True,parents=True)
for n,t in f.items():
 p=Path(n);assert not p.is_absolute() and '..' not in p.parts
 q=out/p;q.parent.mkdir(exist_ok=True,parents=True);q.write_bytes(t.encode())
for n,v in json.loads(f['MANIFEST.json']).items():
 d=(out/n).read_bytes();assert len(d)==v['bytes'] and hashlib.sha256(d).hexdigest()==v['sha256']
print('CORRECT_ROOTS_HEMISPHERE_SIXTY_SOURCE_FILES_RECOVERED')
```


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]
