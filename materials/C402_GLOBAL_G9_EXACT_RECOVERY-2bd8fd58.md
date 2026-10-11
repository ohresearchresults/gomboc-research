# material-2bd8fd58a3ad

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# C402_GLOBAL_G9 — exact nonwinner and certified global continuation progress

The uniformly filled rational polyhedron defined here has V134/E201/F69, C402, own strict[5,1,4], weak000 and no zero feature primitives. It is NOT own110. It is larger than C288 and has more stable equilibria, but its WHOLE centered-polar true-edge rooted bottleneck has strictly improved. These distinct diagnostics must not be conflated.

Exact accepted inequalities:
- C288_SUPPORT70: physical beta>1/1000000 and -559374/1000000<polar beta<-559373/1000000. Its polar obstruction cut contains18 vertices and all34 outgoing true arcs are checked.
- C402_GLOBAL_G9: physical beta>1/2000000 and -466582/1000000<polar beta<-466581/1000000. Its polar cut contains18 vertices and all53 outgoing true arcs are checked.
Here W(x,y)=x dot(y-x)/(|x| |y-x|), beta is the maximum possible minimum W over directed true-edge trees reaching the unique farthest root. A complete rooted tree proves the lower bound, and a nonempty root-excluding cut with every outgoing arc below the upper bound proves the upper bound. This is not merely a local saddle residual. Both bounds and all tree/cut incidences were executed with exact rational squared comparisons, not certified by floating decimals. Canonical own110 remains C622.

## Dependencies and recovery

C402 itself needs only the complete auditor source material [internal-source-reference] (C330 recovery part2) plus this material. To reproduce the C288 comparison also supply [internal-source-reference] and [internal-source-reference] and first reconstruct C288. Those materials provide every dependency, not an external path. Save the FILE blocks below beside exact_source/. Save each JSON block to its named file without a terminal newline. All are complete literal inputs, not abbreviated coordinate lists.

Execute `python -B -S RECONSTRUCT_C402.py OUT402` with a fresh output directory. Expected terminal marker C402_G9_EXACT_AB_MASS_GLOBAL_CERT_NONWINNER_PASS. For the comparison execute `python -B -S VERIFY_GLOBAL.py C288/A.json C288_CERT.json C288/PROOF.json`. Expected comparison marker EXACT_GLOBAL_CERT_PASS with338bytes SHA967ce5c886298461d6b96b1d56199de5c0fd7a0575dbfb8f48ead8ede4c6b36b. CPython3.13.5 standard library only, assertions enabled. The independent full audits, centered integration and both exact certificates were executed before preservation. The newly assembled reconstruction wrapper is not called cold-replayed merely because it is stored.

### POLAR_POINTS.json — 2367bytes, SHA1d35b43651623a525e759a14787c16ca20ceb07107bfdef1cd4f1a460b2028ba
```json
{"grid":1000000000,"points":[[-1983861897,-1465830500,775989280],[-1849246027,-1436646573,634294277],[-1893278808,-1278523356,805150844],[-1127353126,-309622803,888715715],[-365620662,-837566353,-498050283],[-1718992063,-1015816867,830394240],[-546586971,-996342569,-339281369],[-1234200491,-401510356,881579009],[-527610996,25052873,919915123],[-1473490458,-1446287182,806024606],[-1025670909,-235306978,896534363],[-817115755,-104995002,910387984],[-919935866,-159339043,899604521],[-252345127,-839365241,-512599045],[-256903581,-931102181,-424672517],[-1578619137,-814316552,852953323],[-246579655,57078016,934485121],[-376942641,62659755,926659178],[-156913857,51707109,933487051],[-634185630,-1193095511,79595164],[-1980971238,-1444621330,787979367],[-1154253805,-262396907,250283154],[-1350517941,-505885183,870142028],[-263883506,938032738,-482637148],[-984883963,-86497464,3268876],[-567264558,117814907,822252989],[-17972373,1317916415,-539825930],[292458306,1395182654,-39628016],[290901235,1470787571,-134235656],[1238253376,-324643537,181599326],[41417001,-28989410,932100830],[251423126,1586934698,-361498355],[109515647,-1078139470,896385652],[313366228,1457293524,-1201872886],[362482686,1226857243,156632724],[393494792,-71621507,-930048632],[238397273,-894006427,-224303445],[1158735929,265660298,153996672],[509522332,712748056,494947899],[414971194,959094611,-1305421631],[246037141,1671211250,-735057838],[1157264430,-404733471,346495542],[350765406,1311656821,72163156],[787791502,303473010,531635440],[269526471,1513331048,-208889231],[249175792,1640883085,-868597760],[1186322284,509672379,-795371741],[626989710,-76195168,726884449],[421380172,966302833,360636876],[250464694,1658982059,-582580289],[436268258,1148908351,-1376770987],[299978248,-1004684933,766133513],[308676103,1418305449,-54911698],[303525514,1503301102,-1153014530],[748715688,-492499392,-540289450],[929080923,356398315,-882464880],[333704762,-941368812,-15102463],[593600494,1018838851,-1274477969],[1106217678,199849850,251264223],[885676536,-594798200,479436252],[199102778,-267681696,931423435],[1354271966,130522086,-332801451],[567062833,590324267,524526744],[657954477,-387381986,-697599399],[1348863149,189897637,-397288293],[1316268540,-368369058,-55746609],[1365358327,-169416656,-151430785],[1269284878,348090790,-591095545],[370122821,1286527579,-1325940202]]}
```
Each row is a polar support vector divided by10^9: the PHYSICAL body is {x: row dot x<=10^9 for every row}, not the convex hull of the listed points. This distinction is essential.

### C402_CERT.json — 849bytes, SHAc325bd12d4b7f5c537fc14e63ae5c94b6161d036f0fc24323831918faa59a731
```json
{"physical_lower":"1/2000000","physical_parent":[2,0,4,0,8,3,5,3,9,10,15,7,11,6,12,18,14,16,20,17,22,19,22,21,23,22,24,26,27,28,29,30,31,32,33,32,34,54,36,27,22,40,38,41,40,52,42,52,43,50,59,48,53,57,57,54,55,59,46,60,63,56,68,64,71,67,58,62,72,66,43,69,79,70,72,76,74,73,44,77,76,109,71,78,70,86,82,83,86,79,92,84,96,85,89,94,97,102,93,98,103,82,105,95,103,111,77,108,106,124,108,121,113,101,88,112,110,115,113,117,114,123,119,124,125,122,132,131,133,118,125,129,133,131],"physical_root":22,"polar_cut":[25,26,29,30,31,35,36,37,38,39,40,42,44,45,46,50,52,55],"polar_lower":"-466582/1000000","polar_parent":[0,0,0,18,18,4,4,18,6,4,1,9,4,0,2,12,2,12,1,17,16,16,16,19,23,36,36,32,13,42,55,30,28,41,43,36,30,35,37,38,37,28,40,28,42,44,31,65,57,56,52,61,46,49,49,62,28,47,62,60,41,60,68,60,62,60,68,68,63],"polar_root":0,"polar_upper":"-466581/1000000"}
```

### C288_CERT.json — 646bytes, SHAb1ca069314c59b0f87c997cf4b5caace2cc3d3d40c1881fd8441ef75cc8cff25
```json
{"physical_lower":"1/1000000","physical_parent":[1,2,5,5,0,6,9,4,7,12,8,10,16,12,11,14,16,15,17,18,19,20,21,22,22,23,16,25,27,16,28,34,35,30,41,36,44,33,31,37,26,48,43,26,39,41,45,40,47,43,44,60,49,50,48,54,55,56,53,58,61,63,49,69,62,50,65,64,66,73,68,50,71,70,75,71],"physical_root":16,"polar_cut":[23,26,27,28,31,34,35,40,41,43,45,46,50,51,53,54,58,69],"polar_lower":"-559374/1000000","polar_parent":[0,0,20,7,6,2,1,22,11,0,3,12,10,14,6,5,17,8,16,1,0,2,15,46,20,11,41,53,45,42,61,50,9,59,54,43,64,57,59,63,58,46,52,53,48,31,54,68,60,44,41,58,32,28,58,66,47,52,47,29,52,32,65,44,55,66,42,29,65,51],"polar_root":0,"polar_upper":"-559373/1000000"}
```

<!-- FILE RECONSTRUCT_C402.py -->
```python
import sys,json,hashlib,math
from pathlib import Path
sys.set_int_max_str_digits(0)
sys.path.insert(0,str(Path(__file__).resolve().parent/'exact_source'))
import check_A as A,check_B as B,centred_mass as M
from VERIFY_GLOBAL import verify
J=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
assert __debug__ and len(sys.argv)==2
bb=Path('POLAR_POINTS.json').read_bytes();assert (len(bb),hashlib.sha256(bb).hexdigest())==(2367,'1d35b43651623a525e759a14787c16ca20ceb07107bfdef1cd4f1a460b2028ba');cfg=json.loads(bb);H=[]
for p in cfg['points']:
 r=p+[cfg['grid']];d=math.gcd(*r);H.append([v//d for v in r])
raw={'H':sorted(H)};a=A.run(raw);b=B.run(raw);assert J(a)==J(b);m=M.run(a)
cb=Path('C402_CERT.json').read_bytes();assert (len(cb),hashlib.sha256(cb).hexdigest())==(849,'c325bd12d4b7f5c537fc14e63ae5c94b6161d036f0fc24323831918faa59a731');proof=verify(a,json.loads(cb))
assert [a['V'],a['E'],a['F']]==[134,201,69] and a['counts']==[5,1,4] and a['weak']==[0,0,0]
assert [a['face_primitive_zero_count'],a['vertex_max_zero_count'],a['edge_primitive_zero_count']]==[0,0,0]
assert m['tetrahedra']==264 and m['filled_first_moments']==[0,0,0] and m['common_centred_denominator_bits']==21371
expected={'RAW.json':(3085,'47ddc4d6502aa40944298bee721aba6516f4669feed9e8855528014f990a7e84'),'A.json':(118734,'3f9b502950323c6a3ed307576e7aa79d24d3bb690e9b84d6852f38283f0c46eb'),'B.json':(118734,'3f9b502950323c6a3ed307576e7aa79d24d3bb690e9b84d6852f38283f0c46eb'),'MASS.json':(224,'1144e98f12ef2273148220ea63060d346cb385a00b7b433c63e6fb13094a7727'),'PROOF.json':(340,'11cc71858c00d8e02aa7fe416a3fe340469e75cf968c3d4422ab2588b1d7a192')}
out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False)
for name,value in [('RAW.json',raw),('A.json',a),('B.json',b),('MASS.json',m),('PROOF.json',proof)]:
 bb=J(value)+(b'\n' if name=='MASS.json' else b'');assert (len(bb),hashlib.sha256(bb).hexdigest())==expected[name],name;(out/name).write_bytes(bb)
print('C402_G9_EXACT_AB_MASS_GLOBAL_CERT_NONWINNER_PASS',flush=True)
```

<!-- FILE VERIFY_GLOBAL.py -->
```python
"""Exact true-edge rooted-tree and closed-cut certificates at the OWN filled centroid.
The input A report must already come from complete rational maximal-hull auditing.
No numerical routing routine or floating value is used by this verifier.
"""
import json,sys,hashlib
from fractions import Fraction as Q
from pathlib import Path
sys.set_int_max_str_digits(0)
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def sub(x,y):return tuple(a-b for a,b in zip(x,y))
def greater(x,y,q):
 e=sub(y,x);D=dot(x,e);AR=dot(x,x)*dot(e,e);assert AR>0
 return D>0 and D*D>q*q*AR if q>=0 else D>=0 or D*D<q*q*AR
def lesser(x,y,q):
 e=sub(y,x);D=dot(x,e);AR=dot(x,x)*dot(e,e);assert AR>0
 return D<0 and D*D>q*q*AR if q<=0 else D<=0 or D*D<q*q*AR
def verify(a,c):
 g=tuple(map(Q,a['raw_centroid']));X=[sub(tuple(map(Q,r)),g) for r in a['raw_vertices']];Y=[tuple(Q(v)/(Q(h)-dot(n,g)) for v in n) for n,h in zip(a['normals'],a['offsets'])]
 E={tuple(r) for r in a['edges']};adj={}
 for f,cy in enumerate(a['faces']):
  for i,j in zip(cy,cy[1:]+cy[:1]):adj.setdefault(tuple(sorted((i,j))),[]).append(f)
 assert set(adj)==E and all(len(v)==2 for v in adj.values());DE={tuple(sorted(v)) for v in adj.values()}
 def tree(P,parents,root,edges,bound):
  assert len(parents)==len(P) and parents[root]==root
  assert all(dot(P[root],P[root])>dot(x,x) for i,x in enumerate(P) if i!=root)
  for i in range(len(P)):
   if i==root:continue
   assert tuple(sorted((i,parents[i]))) in edges and greater(P[i],P[parents[i]],bound)
   seen=set();j=i
   while j!=root:assert j not in seen;seen.add(j);j=parents[j]
 tree(X,c['physical_parent'],c['physical_root'],E,Q(c['physical_lower']))
 tree(Y,c['polar_parent'],c['polar_root'],DE,Q(c['polar_lower']))
 cut=set(c['polar_cut']);assert cut and c['polar_root'] not in cut;out=[]
 for i,j in DE:
  if (i in cut)==(j in cut):continue
  if j in cut:i,j=j,i
  assert lesser(Y[i],Y[j],Q(c['polar_upper']));out.append((i,j))
 assert out and a['unstable_vertices']==[c['physical_root']]
 return dict(status='EXACT_OWN_TRUE_EDGE_GLOBAL_TREE_CUT_PASS',VEF=[a['V'],a['E'],a['F']],strict=a['counts'],weak=a['weak'],physical_root=c['physical_root'],polar_root=c['polar_root'],physical_tree_arrows=len(X)-1,polar_tree_arrows=len(Y)-1,physical_beta_lower=c['physical_lower'],polar_beta_lower=c['polar_lower'],polar_beta_upper=c['polar_upper'],polar_cut_size=len(cut),polar_cut_outgoing=len(out))
if __name__=='__main__':
 a=json.loads(Path(sys.argv[1]).read_text());c=json.loads(Path(sys.argv[2]).read_text());r=verify(a,c);b=json.dumps(r,sort_keys=True,separators=(',',':')).encode();Path(sys.argv[3]).write_bytes(b);print('EXACT_GLOBAL_CERT_PASS',len(b),hashlib.sha256(b).hexdigest(),r,flush=True)
```

## Producing path and remaining limits

A finite width6/depth40 support deletion beam produced exact C288. A root-free actual-centroid H-description saddle/U1 conditioning search produced generic70-support checkpoints. A sequential linear whole-tree continuation then improved the global polar threshold while accepting only physical beta>=2.5e-7. The1000-step invocation was killed by the200-second container timeout after at least371 accepted steps; do not call all1000 complete. A subsequent50-step continuation completed but made only two microscopic accepted steps and mostly encountered LP infeasibility at tiny trust. The69 active support vectors were selected (input support33 omitted) and rounded ties-to-even to grid10^9. This literal rational H-input, not the optimizer's time limit or tolerance, defines C402.

Numerical variants identified two method limits. The first adaptive physical margin could decay toward zero and was not treated as strict robust progress. The fixed-margin LP used a restoration target larger than the current accepted minimum; after excessive backtracking this made the local LP infeasible even though the family was not excluded. A later numerical contact-crossing variant reached about-0.46566 while keeping physical beta about2.5e-7, but is not yet exactified and is not this C402 object. No support-family, affine, projective or global existence exclusion is asserted. Full numerical producer units and their finite options are separate method materials; they are not required for exact reconstruction here.

The small number of equilibrium defects is not an arithmetic bit bound. C288's centered denominator is5173bits, the C318 protected15 body's is10574bits, and C402's is21371bits; all are worse arithmetic than the C33072-bit V-description. The stray phrase '16-bit-looking' in the C318 capsule has no mathematical significance and supplies no bit-size claim.
