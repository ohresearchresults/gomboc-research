# material-dcca7d113e90

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# C126_WIDE_FOUR_GRIDS_EXACT_AB_RECOVERY_V1

New non-record full-coordinate bulk deformation of CA95 integer126_g100; these coordinates are not an affine-only modification or an unchanged-point deletion. Numerical discovery maximized filled volume under an own-centroid primal escape tree using a full 69-coordinate SLSQP search. The complete frozen binary64 endpoint below, not optimizer reproducibility, defines the four exact rounded bodies. The detailed numerical producer is a separate source unit, not a prerequisite for recovering these frozen objects.

Complete dependencies: this material; EXACT_POINTS.py in [internal-source-reference] (source5247bytes SHAa120fc81b941666aa6b2fc78857c0a8a6b63e62732939a8e68bab2b6c78b8f6b); VERIFY_H_B.py in [internal-source-reference] (source5167bytes SHAc8069c3bd1e43399dde7c2e487aa559d150cb356970e684218757bf160665d56). No original sandbox or additional worker result is required. The exact original CA95 worker result figure-0399, SHAc30ee459df73233920d909ab76375f089eae0cb264d9520a9db9ac700549c7da, was read from0 through EOF in this coordinator turn, but its other bodies are not relabeled here.

All four new objects have true V23/E63/F42,C126 and weak000. Grids1000 and10000 are mechanically worse controls, respectively strict(4,13,15) and(4,9,11), centered denominator/numerator bits43/43 and57/57. Grids100000 and1000000 are strict(4,1,3), centered bits70/70 and84/83. These are NOT own110 and do not improve canonical C622. For C126_WIDE_G100000 the unique unstable input16, stable maximal input facets {1,13,14},{1,14,15},{12,16,19},{18,20,22}, and saddle input edges1-14,18-22,20-22. Volume2726528115431833/6000000000000000. Centroid(-145630446499071/545305623086366600000,879041064543/5453056230863666000,8943368186557/218122249234546640000). Its frozen numerical producer had volume/circumradius^3 approximately0.454418 compared with0.197253 for the source; improved bulk is not improved equilibrium class.

Independent A and B full hull, genuine incidence, actual filled mass and all-feature checks passed for every grid. B rejected all1722 nonzero oriented recession candidates and examined11480 full-rank support triples for the grid100000 object. All42 centered tetrahedra were positive; both mass formulations gave zero centered moments. A fresh-directory cold replay reproduced every expected point/A/B file hash and both terminal markers.

Save the following source exactly, including final newline, as REPLAY_WIDE.py. Source4276bytes SHA256971a2046fd47970c868e4fdee7eeb4bff8b04cc4d9d9b720ea03cdff3ac4f545. CPython3.13.5 standard library, assertions enabled. Reconstruction and verification: `python -B -S REPLAY_WIDE.py NEW_OUTPUT_DIRECTORY`. Expected terminal markers: C126_WIDE_FOUR_GRIDS_EXACT_AB_AND_CENTERED_MASS_PASS and NO_NEW_OWN110_CLAIM. All exact output filenames, byte counts and hashes are embedded below. Rounding is exact Fraction times integer grid followed by nearest integer, ties to even.

```python
#!/usr/bin/env python3
"""Recover four exact C126_WIDE nonwinners from complete frozen binary64 input.
Needs EXACT_POINTS.py from [internal-source-reference] and VERIFY_H_B.py
from [internal-source-reference]. Standard library CPython3.13.5, no -O.
Usage: python -B -S REPLAY_WIDE.py NEW_OUTPUT_DIRECTORY
"""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,sys
from EXACT_POINTS import audit as audit_A
from VERIFY_H_B import audit as audit_B
assert __debug__
HEX_ROWS="""0x1.bf44b49666a8cp-4 -0x1.78bc69bc6cc7ep-2 0x1.08909d68c6d1bp-1
0x1.cfe30c0d3f65dp-4 -0x1.9c0da96123032p-4 0x1.208fe1b63e662p-1
0x1.baf2e3db6bb76p-4 -0x1.22f6ea08d0f6dp-1 0x1.7f4b2c61b5d47p-2
-0x1.637396733d329p-5 -0x1.395a77ad2432ap-1 0x1.682b982cb1fb0p-2
-0x1.950da1709abf8p-3 -0x1.3ef8f7768e450p-1 0x1.412529fa79327p-2
-0x1.63deab97e6a86p-2 -0x1.3436130839f8bp-1 0x1.0b3b9be026c39p-2
-0x1.e94756fc11274p-2 -0x1.2066a2b1fc12fp-1 0x1.6a06c5a57b6dfp-3
-0x1.2d71aaa2a5b96p-1 -0x1.0035c2150fe9ap-1 0x1.3c9bdf7e4172dp-4
-0x1.5a6690fb4af5ap-1 -0x1.a7f7649a06a18p-2 -0x1.072a4132ebedcp-5
-0x1.79e6f74e1fadfp-1 -0x1.3808dc176abbbp-2 -0x1.2a15e7637a20ep-3
-0x1.8a879e9d89d25p-1 -0x1.62a588b9b329fp-3 -0x1.0688d83ace770p-2
-0x1.8ae108b25b575p-1 -0x1.520e0e0f6f360p-6 -0x1.6dfe81dfc0f9bp-2
-0x1.795a920690850p-1 0x1.33b7334fd1da1p-3 -0x1.c3c6c9fae574fp-2
-0x1.53d8990c623c3p-1 0x1.567e78fe055d8p-2 -0x1.0072288a32f82p-1
-0x1.130b33e70a660p-1 0x1.081e2028a5e26p-1 -0x1.1853d03525dd0p-1
-0x1.667ba67fbab7ap-2 0x1.5d447b9d59a59p-1 -0x1.261e9f35e0f51p-1
-0x1.891c9ee6ee90cp-4 0x1.a0f1ca231f4bep-1 -0x1.2510727e2c0ffp-1
0x1.46e66a354c3e2p-2 0x1.7e26c33a845eap-1 -0x1.2afcd14061c51p-2
0x1.1c9d34f8edee7p-1 0x1.064bd0ae75b44p-1 -0x1.86ede3ef52c8dp-5
0x1.a5e4042b86585p-3 -0x1.22f4c9c056a1fp-1 0x1.0b52ae4ee155fp-4
0x1.3bd494c74e815p-1 0x1.fa6d683659f73p-4 -0x1.078aaf9010e77p-3
0x1.4492447092573p-2 -0x1.c868e4d5ca531p-2 0x1.5c7a2947789ddp-2
0x1.a4f8f8729c8d1p-2 -0x1.c56ef6174419ep-3 0x1.7ac76bd0601fap-2"""
EXPECTED={'C126_WIDE_G1000000_A.json': [5774, '6c0f1c890c791dab5ea752f736547846ac71be5efc9b05789c485aaf5ea1f66c'], 'C126_WIDE_G1000000_B.json': [548, '15bf4c0c7ddb157f6c44993a71300a24044e3b19ba46c4de4b993510048d0023'], 'C126_WIDE_G1000000_POINTS.json': [1176, '2fba843e2252f422708e35103a6fccbe57948e4506f8891b7f8501d249cb69cd'], 'C126_WIDE_G100000_A.json': [5097, 'c8a761de30d90aa4dc23f6e6f7c6dabf5614953c9001abbeda75ca88d05047a5'], 'C126_WIDE_G100000_B.json': [513, 'febdbba6154abbbef10be1ebdba27947aef7e2016b449f06b133862b5a098b78'], 'C126_WIDE_G100000_POINTS.json': [1035, 'd25ce3b6713f4134e1f43f77050ad5f37f0848deceef999f81161d3a72be328c'], 'C126_WIDE_G10000_A.json': [4472, '5cd7050323e6e980b6c0db96d9e1956d7a1c0ac403c5daf136446e0e610add92'], 'C126_WIDE_G10000_B.json': [577, 'b28d7f4b599eefb3603f878a67d7edd0ceecf1caff963099bf3d3a073384f62f'], 'C126_WIDE_G10000_POINTS.json': [900, '1557d9c7a8126e0a6e3424a07f5d5f433ffe10e23d4f3222396e7594ec4f003c'], 'C126_WIDE_G1000_A.json': [3872, '56f8d87a47c6826c98d5dd6567e511f1eff0928e898b78b26a4bac0f524d6ffe'], 'C126_WIDE_G1000_B.json': [578, '74106701c0b20c111df9bfb50f366f835a0349ec206e4df7fcf0c153d71a4343'], 'C126_WIDE_G1000_POINTS.json': [770, '4b82007615121839c1cbd19b3f2af5e7ad4496f7f352d118cd3a5f17ee2e193d']}
def dump(path,value):
 data=(json.dumps(value,sort_keys=isinstance(value,dict),separators=(',',':'))+'\n').encode()
 path.write_bytes(data);assert [len(data),hashlib.sha256(data).hexdigest()]==EXPECTED[path.name],path.name
def main(folder):
 out=Path(folder);out.mkdir(exist_ok=False,parents=True)
 p=[[Q.from_float(float.fromhex(t))for t in row.split()]for row in HEX_ROWS.splitlines()]
 assert len(p)==23 and all(len(row)==3 for row in p)
 for grid in (1000,10000,100000,1000000):
  points=[[Q(round(t*grid),grid)for t in row]for row in p]
  stem='C126_WIDE_G'+str(grid)
  dump(out/(stem+'_POINTS.json'),[[str(t)for t in row]for row in points])
  a=audit_A(points);dump(out/(stem+'_A.json'),a)
  b=audit_B(a);dump(out/(stem+'_B.json'),b)
  assert a['C']==126 and a['weak']==[0,0,0]
  assert a['strict']==({1000:[4,13,15],10000:[4,9,11],100000:[4,1,3],1000000:[4,1,3]}[grid])
 print('C126_WIDE_FOUR_GRIDS_EXACT_AB_AND_CENTERED_MASS_PASS')
 print('NO_NEW_OWN110_CLAIM')
if __name__=='__main__':main(sys.argv[1])
```
