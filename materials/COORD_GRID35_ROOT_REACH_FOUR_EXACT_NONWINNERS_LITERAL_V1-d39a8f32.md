# material-d39a8f32aec3

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# COORD_GRID35_ROOT_REACH_FOUR_EXACT_NONWINNERS_LITERAL_V1

This complete literal source preserves four new exact uniformly filled own-centroid nonwinners, not a new Gömböc. All four have actual V35/E99/F66,C198,strict211,weak000 and all primitive-zero counters0. They were obtained from completed global root-reaching geometry runs06 and07. The numerical method and its complete finite-search evidence are a separate preservation unit; this capsule independently reconstructs the exact bodies without any floating checkpoint or original sandbox.

The two literal fine-grid banks below are the complete exact geometry. For THESE two banks, nearest-even rounding from denominator100000000 to100000 reproduces the original binary64 checkpoint's independently frozen coarse input byte-for-byte. This equality was checked before constructing this source-only replay; it is not a general claim about double rounding. Raw bit costs are17,27,17,27 and common centred denominator costs67,107,68,106 respectively in the order row06 coarse/fine,row07 coarse/fine. Equilibria: row06coarse S18,65,U16,H11--17; row06fine S1,63,U16,H11--17; row07coarse S1,64,U15,H11--17; row07fine S1,48,U15,H11--17. These are each audit's own raw-lex/maximal-face IDs, not globally shared labels.

Sole unchanged complete dependency: **[internal-source-reference]**,39762B SHA2567b9d113b63af0c9a7e9dda973cddaa2b0adf27dcebe107d615db90323b602d45, the eighteen-source COORD_GRID35_MULTIGENERATION_AND_NEAR_WALL_V1. Recover its LEAD_GATE_SOURCE. The five actually used file hashes are explicitly bound in the source below. No other source or worker result is needed for exact reconstruction of these four bodies.

Save the complete Python block as RECONSTRUCT_FOUR.py with its final LF. It is7243B SHA256**4b57cda8959782cc19b9cdc6bcaac447db18157b9ce0bc7c0fb5203c15fbcb82**. Run `python3 -B -S RECONSTRUCT_FOUR.py LEAD_GATE_SOURCE NEW_OUTPUT`, where NEW_OUTPUT does not exist. CPython3.13.5 standard library, assertions enabled, no randomness or numerical dependencies. This exact cold source-only command actually completed in a fresh directory. It reconstructs all four input files, runs both independent complete exact hull/filled-mass/all-feature audits and a third centred integration, and checks input and reproduced output bytes and SHA256 against the complete EXPECTED table below. Terminal markers include EXACT_VARIANT_TWO_AUDITS_AND_MASS_PASS, EXACT_INPUT_HULL_EQUALITY_PASS for each named body, and **FOUR_ROOT_REACH_BODIES_COLD_TWO_AUDITS_AND_MASS_PASS**. All filenames, byte counts and hashes for four inputs and sixteen principal outputs are literal below.

The root-reaching numerical study showed no S1 in eighteen completed cases. These four exact211 bodies are retained for their changed basin geometry and modest fractions, not as proof that any full deformation family is impossible. Subsequent global-tree experiments must name this exact source, not merely its old ephemeral numerical file.

```python
"""Complete four-body source-only reconstruction. CPython3.13.5 stdlib.
Usage: python -B -S RECONSTRUCT_FOUR.py LEAD_GATE_SOURCE NEW_OUTPUT
Both fine grids were obtained from global root-reaching geometry searches.
For these two literal banks, coarse nearest-even rounding is byte-identical
with the independently frozen original binary64 checkpoint's coarse grid.
This exact capsule preserves the four bodies, not the entire optimizer trace.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json,sys,subprocess
BANKS={'6': [[-42383800, 36936837, 9074818], [-40780617, 37864606, 12607087], [-40244482, 38585933, -983233], [-41984689, 32758317, 23684599], [-38972081, 35743522, -11279010], [-39038257, 30989206, 31006876], [-38062433, 33369698, -17000823], [-37119645, 32318808, -19938327], [-36540487, 30114252, -22860572], [-33391336, 27805305, -27672517], [-32224943, 22570174, 46422051], [-30335367, 24709992, -32012949], [-23630374, 15831197, 54624455], [-11230539, 23780724, -14906718], [-2974357, 13985873, -31312094], [-2576353, 672166, 67921803], [-4071777, -11576065, -33909818], [2804185, -2251106, -45068692], [11220840, -9550392, -43364302], [14992452, -13628939, 56072815], [19174100, -16698744, -38660620], [22850108, -19984140, -35308640], [24186317, -21685107, 45286853], [26324511, -22780902, -31028219], [28376171, -25152374, 38801775], [29293580, -25666227, -26395952], [31533027, -27580961, 32667900], [32174996, -27496800, -20945185], [34159606, -29475969, 25819374], [34378351, -29195115, -15156688], [36051463, -30740267, 18719061], [36213532, -30270828, -8865273], [37246429, -31288872, 11617324], [37156192, -31288964, -2278081], [37425677, -31724839, 4620921]], '7': [[-42418135, 37323373, 9048465], [-41173536, 37928714, 12580587], [-40066938, 38498975, -902690], [-42136570, 32816246, 23666874], [-38882120, 36110563, -11334072], [-39121953, 31049074, 31052969], [-38681761, 32475041, -16868835], [-36370432, 32835579, -19766678], [-36666004, 29789190, -22716976], [-33186384, 27588666, -27399798], [-32146931, 22648331, 46415399], [-30524350, 24255409, -31363866], [-23539574, 15908062, 54576900], [-11243209, 23650284, -14950479], [-2240859, 15826445, -33283849], [-2777319, 416331, 67777807], [-4136601, -11780249, -33941841], [2620692, -3011153, -44089818], [11016044, -9719335, -43268950], [14960150, -13638354, 56051519], [19341440, -16584622, -38765568], [22897110, -19884627, -35278251], [24191589, -21650029, 45266144], [26307931, -22871081, -31076991], [28345764, -25174184, 38794121], [29375432, -25493816, -26369579], [31492326, -27615918, 32661259], [32139303, -27618836, -20976585], [34220536, -29423942, 25843200], [34376983, -29239985, -15168037], [35968312, -30847428, 18674549], [36236259, -30251678, -8866580], [37052250, -31456566, 11643944], [37349599, -31146140, -2282786], [37420956, -31712339, 4618493]]}
EXPECTED={'COORD_GRID35_ROOT_REACH_ROW06_D100000': {'input': {'bytes': 824, 'sha256': 'c9542f9743bf4fa2125a58533a3437874a5a4b538ce9ea994ec77cc94f40a491'}, 'outputs': {'A.json': {'bytes': 10258, 'sha256': '053656ff6d83867cf802c7a18a8c51f3a65f956ff9a88b224167113849140dd9'}, 'B.json': {'bytes': 10258, 'sha256': '053656ff6d83867cf802c7a18a8c51f3a65f956ff9a88b224167113849140dd9'}, 'MASS.json': {'bytes': 216, 'sha256': '634789f284417937eec9d5219ef852f98c187303483e14b648c3a70c3aea6cb6'}, 'RAW.json': {'bytes': 3768, 'sha256': 'd0973b5a0a0d363793987570492aa77b6f4b289e24bb27277fda3f1243ea1de4'}}}, 'COORD_GRID35_ROOT_REACH_ROW06_D100000000': {'input': {'bytes': 1145, 'sha256': '30f5e6ac1d021d135bb831508dae74230a51541fe86b8652e3f4dd4f4eb21f9d'}, 'outputs': {'A.json': {'bytes': 13491, 'sha256': '3f8dfe6888c0061ed540ebd8162a8a9f3d2029d151a774966b0e4b587ae51642'}, 'B.json': {'bytes': 13491, 'sha256': '3f8dfe6888c0061ed540ebd8162a8a9f3d2029d151a774966b0e4b587ae51642'}, 'MASS.json': {'bytes': 218, 'sha256': 'e5c3088cd2716c3e9880e7bc3e911a8c78316f2418c690e79a14ee55607bf704'}, 'RAW.json': {'bytes': 6194, 'sha256': 'f412753bef37f2fd366cfa0b2feed25e395d5fd62406ae0b392dc81760596af5'}}}, 'COORD_GRID35_ROOT_REACH_ROW07_D100000': {'input': {'bytes': 824, 'sha256': '8b39bebbeb6efe273d85683b172bf45f75ab8b0f18a83659540a5e4e1928fd32'}, 'outputs': {'A.json': {'bytes': 10318, 'sha256': '0fcd4b84ecf9b3b71608478d2fa568597b985f0f5e65bc4aa19b44dca1fd2df8'}, 'B.json': {'bytes': 10318, 'sha256': '0fcd4b84ecf9b3b71608478d2fa568597b985f0f5e65bc4aa19b44dca1fd2df8'}, 'MASS.json': {'bytes': 216, 'sha256': '956a5fe552ab7571f404e8b357442a17f105fac020b3df4da017046300858308'}, 'RAW.json': {'bytes': 3824, 'sha256': '11f3fc58602cec3eed971ebc940e4c012064cad868654fc48ac8e91063b1f1b1'}}}, 'COORD_GRID35_ROOT_REACH_ROW07_D100000000': {'input': {'bytes': 1145, 'sha256': '8e4c1463002db70013634c331aebe90b8e4a677ced1b51f15b64ded207619a93'}, 'outputs': {'A.json': {'bytes': 13408, 'sha256': '8b2c90482022538fc15f738c9bafa528ec72fdde5cbba3be07977b119a7ca261'}, 'B.json': {'bytes': 13408, 'sha256': '8b2c90482022538fc15f738c9bafa528ec72fdde5cbba3be07977b119a7ca261'}, 'MASS.json': {'bytes': 218, 'sha256': '47d2b6cd24976f53a518da3b5dbd71055aa8223f24725e41728cb3eb5c6cb79d'}, 'RAW.json': {'bytes': 6123, 'sha256': '355f9af4830873dc96c2d07e7f26e36f4157adab253c6f57a3ef65ed09b9230c'}}}}
DEPENDENCY={
'freeze_variants.py':'3cf9e0fb42a645ca0a70613c93f05ffd126a4ffdd1e6077c3c490532198f3124',
'CF7_SOURCE/grid7.py':'fdbfb8cb6783fdc3b4511d03d543b072c5eab51323043aafbdadf41855f4e292',
'CF7_SOURCE/core/check_A.py':'ad72cc198140249c1e52a615513354036c04f4c718333a7beed64fba4b43d7f3',
'CF7_SOURCE/core/check_B.py':'b0cb62d5486b32d020b60f717f3dfe9d07c6c9a978492928f54c3a38f396fc24',
'CF7_SOURCE/core/centred_mass.py':'5f1afafa0432436bfe953a94d94ca1027c12549504f9452491f0287c2a29d1a8'}
def pack(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def rnd(x):
 a=x.numerator//x.denominator;d=x-F(a)
 return a if d<F(1,2)or(d==F(1,2)and a%2==0)else a+1
def check(path,e):
 b=path.read_bytes();assert len(b)==e['bytes']and sha256(b).hexdigest()==e['sha256'],str(path)
def main():
 assert __debug__ and len(sys.argv)==3
 base=Path(sys.argv[1]).resolve();out=Path(sys.argv[2]).resolve();out.mkdir(parents=True,exist_ok=False)
 for name,h in DEPENDENCY.items():assert sha256((base/name).read_bytes()).hexdigest()==h,name
 records=[]
 for k,points in sorted(BANKS.items()):
  for D in(100000,100000000):
   name='COORD_GRID35_ROOT_REACH_ROW'+k.zfill(2)+'_D'+str(D)
   obj={'name':name,'denominator':D,'vertices':[[rnd(F(v*D,100000000))for v in row]for row in points]}
   inp=out/(name+'.json');inp.write_bytes(pack(obj));check(inp,EXPECTED[name]['input'])
   subprocess.run([sys.executable,'-B','-S',str(base/'freeze_variants.py'),str(inp),str(out/name)],check=True)
   for file,e in EXPECTED[name]['outputs'].items():check(out/name/file,e)
   A=json.loads((out/name/'A.json').read_text());assert[A[t]for t in('V','E','F')]==[35,99,66]and A['counts']==[2,1,1]and A['weak']==[0,0,0]
   summary=json.loads((out/name/'SUMMARY.json').read_text())
   records.append({'name':name,'input':EXPECTED[name]['input'],'summary':summary})
 (out/'INDEX.json').write_bytes(pack(records));print('FOUR_ROOT_REACH_BODIES_COLD_TWO_AUDITS_AND_MASS_PASS')
if __name__=='__main__':main()
```
