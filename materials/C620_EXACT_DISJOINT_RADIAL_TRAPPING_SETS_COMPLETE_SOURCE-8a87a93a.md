# material-8a87a93a3769

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Complete exact source: disjoint radial trapping sets

This generalizes single-unstable-vertex near-isometry certificates to clusters whose unstable maximum may change identity. Let D be a nonempty subset of vertices of a fixed centered convex polyhedron. Suppose every directed true-edge escape x^TM(y−x) with x in D and y outside D is strictly negative. Choose a vertex x maximizing x^TMx within D. For any distinct neighbour y also in D, x^TM(y−x)=[y^TMy−x^TMx−(y−x)^TM(y−x)]/2<0 because M is SPD. External neighbours have negative escape by hypothesis. Thus D contains a strict unstable vertex. Two disjoint such sets force U>=2, regardless of changes to their internal escape witnesses or maximizing vertex identities.

For ||M−I||_2<=rho, each boundary escape is bounded above by x·d+rho||x||||d||, d=y−x. The exact sufficient conditions are c=x·d<0 and b²c²>a²(x·x)(d·d), rho=a/b. Positive homogeneous integer scalings of x,d preserve this test. Scaling an arbitrary SPD M by2/(lambda_max+lambda_min) yields the condition-number sufficient bound kappa(M)<=(1+rho)/(1−rho). These are fixed-body finite metric-neighbourhood exclusions, not whole-affine or nonaffine exclusions.

Executed certificates:
1. **COORD_C620_ALLWITNESS174_G12_OWN132** from [internal-source-reference]: rho278797/5000000=.0557594, hence kappa(M)<=5278797/4721203. Disjoint sets singleton94 and the161-vertex literal set below;44+59 boundary incidences checked exactly. U>=2 despite individual extra maxima having numerical escape deficits around5e−8. This corrects any interpretation that small max-hinge residual alone makes this shape close to own110. The near-coincident unstable pair173/174 masks a much larger basin escape obstruction. The certificate does not rule out shape changes or more anisotropic affine maps.
2. Original COORD_C620_EDGE69_73_Q129_A02_OWN121: rho66109/2500000,sets1/115vertices,44+76 boundary incidences. This is a cluster control, not an improvement on the earlier slightly larger singleton radius.
3. Original COORD_C620_EDGE174_175_Q84_A01_OWN121: rho315319/10000000,singletons94/171,44+3boundary incidences. Also a control, slightly weaker than the previous higher-precision singleton bound.

Dependencies: exact_metric_segment.py from complete capsule [internal-source-reference] supplies the homogeneous Geometry/dot helpers. Body132 exact generator and audits use [internal-source-reference] plus CONDITION25all3: [internal-source-reference],[internal-source-reference],[internal-source-reference]. Original69/174 bodies additionally need [internal-source-reference]. No numerical discovery routine is needed for certificate replay. Standard-library CPython3.13.5; enable ordinary assertions, never -O.

Save the complete following block as metric_cut_certificate.py, preserving its final newline:2406bytes SHA25650ba621a0d63b11c97edcd71238e1bdb33e9c86e7fbfbc2879ba60d4a2401232.
```python
"""Exact near-isometry exclusion from two disjoint radial trapping vertex sets.
For each set D all directed true-edge escapes leaving D remain strictly negative
on the scaled SPD metric ball ||M-I||_2 <= rho. A maximum of x^T M x within D is
then a strict unstable vertex: inside-set neighbours have smaller/equal radius,
outside-set neighbours have strictly negative escape. Disjoint sets force U>=2.
No assumption about the identity of that maximum or the internal witnesses.
"""
from pathlib import Path
import argparse,json,hashlib,sys
from fractions import Fraction as F
from exact_metric_segment import Geometry,dot
sys.set_int_max_str_digits(0)
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
H=lambda x:hashlib.sha256(x).hexdigest()
def certify(report,config):
 g=Geometry(report);sets=[set(s) for s in config['sets']];rho=F(config['rho']);assert 0<rho<1 and len(sets)>=2
 assert all(D and D <= set(range(g.nv)) for D in sets)
 assert sum(map(len,sets))==len(set.union(*sets)),'Sets must be pairwise disjoint'
 answer=[]
 for D in sets:
  rows=[]
  for e,(u,v) in enumerate(g.edges):
   for k,(i,j) in enumerate([(u,v),(v,u)]):
    if i in D and j not in D:
     x,d=g.prows[2*e+k];c=dot(x,d);A=dot(x,x);E=dot(d,d)
     assert c<0,(i,j,'nonnegative escape')
     gap=rho.denominator**2*c*c-rho.numerator**2*A*E
     assert gap>0,(i,j,'metric ball inequality fails')
     rows.append(dict(edge=[i,j],negative_escape=True,strict_squared_metric_gap=True,escape_integer_sha256=H(str(c).encode()),gap_integer_sha256=H(str(gap).encode())))
  assert rows
  answer.append(dict(vertices=sorted(D),boundary_incidence_count=len(rows),rows=rows))
 return dict(marker='EXACT_DISJOINT_RADIAL_TRAPPING_SETS_PASS',VEF=[g.nv,g.ne,g.nf],rho=str(rho),metric_condition_bound=str((1+rho)/(1-rho)),guaranteed_unstable_minimum=len(sets),sets=answer,scope='Fixed rational filled-centroid body, scaled spectral metric ball only; not a whole-affine-orbit or shape exclusion.')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('report');p.add_argument('input');p.add_argument('output');a=p.parse_args();r=Path(a.report).read_bytes();i=Path(a.input).read_bytes();ans=certify(json.loads(r),json.loads(i));ans.update(report_sha256=H(r),input_sha256=H(i));Path(a.output).write_bytes(B(ans));print(ans['marker'],ans['rho'],[x['boundary_incidence_count'] for x in ans['sets']],flush=True)
```

Save each input block without a trailing newline (or use json.dumps(json.loads(block),sort_keys=True,separators=(',',':'))). CUT132_INPUT.json575bytes SHAb4159bcaaacfde0c6c340aec5acfc34dacca07740a6eb71a0ac385c4be5b00a1:
```json
{"rho":"278797/5000000","sets":[[94],[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,97,98,99,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,144,145,146,147,149,150,151,152,153,155,157,158,160,161,163,165,166,168,173,174]]}
```
CUT69_INPUT.json409bytes SHA7bd707b22a4c5936728602ffec6c245c18a48417e7aa587f56fff610efe4cdd6:
```json
{"rho":"66109/2500000","sets":[[93],[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,64,65,67,68,69,70,71,76,77,80,82,84,87,88,91,94,96,97,100,101,103,104,106,107,108,110,111,113,114,116,117,119,120,121,123,124,125,126,128,129,130,131,133,134,135,136,137,138,139,140,141,142,143]]}
```
CUT174_INPUT.json45bytes SHA0a002638bdd0c2a9fe556ac5611fd007da71b830c58f4fc158b6c9614e1035dc:
```json
{"rho":"315319/10000000","sets":[[94],[171]]}
```

Commands, with reconstructed reports at the indicated relative paths:
`python -B -S metric_cut_certificate.py shape_174_exact/A.json CUT132_INPUT.json CUT132_REPORT.json`
`python -B -S metric_cut_certificate.py two_contact_verified/e69_73_q129_a02/A.json CUT69_INPUT.json CUT69_REPORT.json`
`python -B -S metric_cut_certificate.py two_contact_verified/e174_175_q84_a01/A.json CUT174_INPUT.json CUT174_REPORT.json`
Expected terminal markers EXACT_DISJOINT_RADIAL_TRAPPING_SETS_PASS. Expected outputs, completely regenerable from this literal code and inputs:
CUT132_REPORT.json27114bytes SHAae67868cf90b70df8b38123ac24c9cd77632d6a706bd00bd9ece92548dcef439;
CUT69_REPORT.json31253bytes SHA4935c0960505052f9c1c0316a376f30e8f94d1632668666f700a63576f44c431;
CUT174_REPORT.json12442bytes SHA0a8c2f4732015f0938aef195074d2a9dff6bc5a9a12d57061992e2a1bb6ca0b4.
Input report hashes respectively f30fc15a826c78fb05d994a506d97e953e6793472657749f2abc99fce006660a, b15545919f3ab22b5bca850dd82e4b5d0b38fbb7bdd13e9c48becb04ff4d5fbf, e80c5c1d93c99675d416e2fec4f88075dbc8a9ff29336ee493a2e116e771f059. Certificate report boundary rows contain exact-derived integer hashes; the integers themselves are deterministically recomputed by the complete source, never substituted by a hash-only assertion.
