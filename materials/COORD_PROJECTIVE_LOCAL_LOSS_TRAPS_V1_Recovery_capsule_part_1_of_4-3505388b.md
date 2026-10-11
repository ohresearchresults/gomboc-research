# material-3505388bccd6

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: unreviewed-encoded-blocks-omitted.

---

# Recovery capsule part 1/4 — COORD_PROJECTIVE_LOCAL_LOSS_TRAPS_V1

All FOUR parts are mandatory. This self-contained 29-file source/input capsule preserves three exact uniformly filled rational nonwinners, their independent full hull/mass/strict-and-weak feature checks, exact fixed-body rooted-escape counterexamples, a complete analytic degeneration proof and all materially used numerical producer/diagnostic code with frozen exact input checkpoints and non-default parameters. No originating sandbox, ancestor source or external input file is required. The exact bodies are the convex hulls of the literal dyadic rational values of the preserved binary64 physical_hex arrays, NOT asserted exact projective images of their rational parents. No own110 or improvement to canonical C622 is claimed.

COORD_FROZEN_integer126_g100_HARDU_BEST_R41: V23/E63/F42,C126,own312/weak000,centered maxinteger239/minimalden234bits. The C174 BEST_R0 and BEST_R54 objects are31/87/58,C174,own312 andown413/weak000,237/233 and231/228bits. For each, every non-root centered-polar vertex has some normalized escape>-1/1000, but every crossing from its listed pool to the outside has escape<-999/1000. Therefore every finite-vertex path from the pool to the chosen root crosses a nearly maximally adverse step, despite tiny local defects. All245/645/480crossing pairs are checked by exact signs and squared rational inequalities using actual filled mass. This excludes those fixed point sets only, not projective families or new relay geometry.

Cold recovery from the final FOUR complete parts was run successfully: all29source hashes passed; all6REPORT/TRAP outputs reproduced byte-identically; all independent full feature/mass and rational trap checks passed. Exact replay uses CPython3.13.5 standard library only, with assertions enabled. Numerical discovery was pinned to NumPy2.3.5,SciPy1.17.0,PyTorch2.10.0+cpu,binary64,one BLAS/OMP/MKL/Torch thread; discovery trajectories/clock fields are not cross-platform identity promises. Frozen hex arrays and exact outputs are authoritative. README, OBSERVATIONS, CASES, EXPECTED_EXACT and MANIFEST contain full commands, options, input/output hashes and scope. Some numerical MILP outer relaxations were SPD but failed the required escape margin; do not describe all of them as indefinite or as an exact infeasibility proof.

Save the decoder below as RECOVER_PROJECTIVE_TRAPS.py, and the four raw payload blocks as PROJECTIVE_TRAP_PAYLOAD_1.b64 through PROJECTIVE_TRAP_PAYLOAD_4.b64 beside it. Run `python -B -S RECOVER_PROJECTIVE_TRAPS.py NEW_DIRECTORY`. From the recovered source directory, `python -B -S REPLAY_EXACT.py NEW_EXACT_DIRECTORY` independently reconstructs all exact outputs without numerical dependencies. Expected terminal markers: PROJECTIVE_TRAP_29_SOURCE_FILES_RECOVERY_PASS; COORD_PROJECTIVE_FROZEN_THREE_AB_MASS_AND_GLOBAL_TRAPS_PASS; COORD_PROJECTIVE_LOCAL_LOSS_TRAPS_V1_IMMUTABLE_CAPSULE_PASS. Do not use -O.

Final transport identities: dictionary106496bytes SHA256068805334c6aef809972d18ff7c0e487238a581f39061ec9c6970b30ff6dbbac; XZ30840bytes SHAd4896508b14a56445a6a32fc1e7b03435f66c231a3663fc062b2b7eed55a754b; joinedbase6441120chars SHAecb859493265d57a6e6f993824a98a009d8afb6f26c66dedffb5ee1c2124855e. Each part is10280unwrappedchars. Part1 SHA741fdb1d7d2cc2aa82dba5baeb22b3cb46716e989751c602b71d47633f0f4911; part2 SHA82d9f70f5d9687bcafef9af93df8f870a542ead650ef22fa0380bb424d554b29; part3 SHA8936013437abf08405f63201543e111ba144fca78f84e68ccb3f3918aa134fcd; part4 SHAdafac6ef303bed637e87d16d442eebfa90200acf6f0e002b1caf2d574d53361f. Decoder1781bytes SHA975dbcc6a93dea780933ccf16e2eece3e6f5bd1e288f469abdb0f4f2a8b07280. Earlier local split-length metadata was wrong and those truncated parts were never stored; only these final four complete parts and identities are authoritative.

Expected exact outputs: C126R41 REPORT15301bytes SHAf798d0a6b5e05742b080a36d4ee8e5266f6f1b5f99ff2a7febabb5a3a919b2c7,TRAP2129 SHA9f25d9531932db8e8fc80536c3ee962b2757e103319ec3ea61d50d3b6db856ce; C174R0 REPORT19977 SHAb3ce875df2e19f6735032af4ed2725a3ad3d197287ba06647905dffcf96c34db,TRAP2420 SHAf79ec2b7d5eade50be0d060f4f0f9e391de462945d1755f0fa978848d1380a42; C174R54 REPORT19872 SHA2178f9b3bae3ad11b2c50dd478bc8ddbad4c2c4d51c10c0966c886f1ea83d89c,TRAP2379 SHA0844183661b5bf9e176e4786cb79ba1783b948a79bb1fd679ffd3ae58150e24a.

## Complete decoder
```python
#!/usr/bin/env python3
"""Four-part exact capsule COORD_PROJECTIVE_LOCAL_LOSS_TRAPS_V1.
Run: python -B -S RECOVER_PROJECTIVE_TRAPS.py NEW_DIRECTORY
Requires only Python standard library; assertions must remain enabled.
"""
import base64,hashlib,json,lzma,subprocess,sys
from pathlib import Path,PurePosixPath
assert __debug__
def main(out):
 here=Path(__file__).resolve().parent
 e=b''.join(b''.join((here/f'PROJECTIVE_TRAP_PAYLOAD_{i}.b64').read_bytes().split()) for i in range(1,5))
 assert len(e)==41120 and hashlib.sha256(e).hexdigest()=='ecb859493265d57a6e6f993824a98a009d8afb6f26c66dedffb5ee1c2124855e'
 z=base64.b64decode(e,validate=True)
 assert len(z)==30840 and hashlib.sha256(z).hexdigest()=='d4896508b14a56445a6a32fc1e7b03435f66c231a3663fc062b2b7eed55a754b'
 raw=lzma.decompress(z)
 assert len(raw)==106496 and hashlib.sha256(raw).hexdigest()=='068805334c6aef809972d18ff7c0e487238a581f39061ec9c6970b30ff6dbbac'
 data=json.loads(raw);assert len(data)==29
 out=Path(out).resolve();out.mkdir(parents=True,exist_ok=False);src=out/'source';src.mkdir()
 for name,text in data.items():
  p=PurePosixPath(name)
  assert not p.is_absolute() and all(t not in ('..','.') for t in p.parts) and '\\' not in name
  dest=src.joinpath(*p.parts);dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(text.encode('utf-8'))
 for name,m in json.loads(data['MANIFEST.json']).items():
  b=(src/name).read_bytes();assert len(b)==m['bytes'] and hashlib.sha256(b).hexdigest()==m['sha256'],name
 print('PROJECTIVE_TRAP_29_SOURCE_FILES_RECOVERY_PASS',flush=True)
 subprocess.run([sys.executable,'-B','-S',str(src/'REPLAY_EXACT.py'),str(out/'exact')],check=True)
 print('COORD_PROJECTIVE_LOCAL_LOSS_TRAPS_V1_IMMUTABLE_CAPSULE_PASS',flush=True)
if __name__=='__main__':main(*sys.argv[1:])
```

## PROJECTIVE_TRAP_PAYLOAD_1.b64

[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]
