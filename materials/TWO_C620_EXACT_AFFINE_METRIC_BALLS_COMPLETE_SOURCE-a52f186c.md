# material-a52f186ca874

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Two exact affine-metric exclusion balls — complete source and recovery

## Exact identities and scope
This is an exact negative result for two FIXED homogeneous filled C620 own121 bodies, not an exclusion of C620 constructions or nonaffine shape changes. Both original seeds were reconstructed in this producing turn from the four immutable dependencies below; exhaustive A and independent support-pair B agreed bytewise, and the separate centered-volume integration gave346 positive tetrahedra and exact zero first moments. No new own110 body is asserted. Canonical C622 is unchanged.

First: COORD_C620_EDGE69_73_Q129_A02_OWN121, V175/E310/F137, own(S,U,H)=(1,2,1), weak000, S3,U67/93,H67–72. Second: COORD_C620_EDGE174_175_Q84_A01_OWN121, V175/E310/F137, own121/weak000, S3,U94/171,H173–174. The edge numbers in the identity name belong to the CONDITION25 parent, whereas the equilibrium labels are those of the exact descendant.

## Theorem and proof
Let x_i=v_i-g be vertices centered at the true FILLED uniform volume centroid. For an invertible real affine linear part A, the new filled centroid is Ag, by the change-of-variables formula in volume and first-moment integrals. Put M=A^T A. At vertex i the escape toward a true neighbor j has sign p_ij=x_i^T M(x_j-x_i). Strict negativity for all incident edges makes the supporting plane perpendicular to Ax_i meet the transformed body only at Av_i; the neighbor directions generate the tangent cone, so this is a strict unstable equilibrium.

Write M=I+Delta, with spectral operator norm ||Delta||_2<=rho. Then
p_ij <= x_i·d_ij + rho ||x_i|| ||d_ij||.
The complete exact code below checks, for BOTH indicated unstable vertices and every true neighbor, that x_i·d_ij<0 and
(x_i·d_ij)^2 > rho^2 (x_i·x_i)(d_ij·d_ij).
Thus every one of these escapes stays strictly negative, INCLUDING the closed ball boundary. Each body has at least two strict unstable equilibria for every metric in the stated ball, independently of S and H. No such image is own110.

Metrics may be multiplied by any positive scalar without changing signs. A positive-definite M with condition number kappa=lambda_max/lambda_min can be scaled to distance (kappa-1)/(kappa+1) from I, using scale2/(lambda_max+lambda_min). Hence the same exclusion applies whenever kappa(M)<=(1+rho)/(1-rho). For A this is equivalently cond_2(A)^2<=(1+rho)/(1-rho). This is not a statement about arbitrary large anisotropic maps, and it does not constrain any nonaffine shape deformation.

## Observed exact results
- First body: rho=26443627/1000000000; preserves U67 and U93; all47 incident inequalities strictly certified. Metric-condition-number bound1026443627/973556373.
- Second body: rho=31531903/1000000000; preserves U94 and U171; all47 incident inequalities strictly certified. Metric-condition-number bound1031531903/968468097.
The radii are downward-rounded strict bounds on a grid10^9. No floating arithmetic determines them. The program calculates floor(sqrt(p^2*grid^2/A)) using integer division and isqrt; if equality occurs it subtracts1. The true cosine denominator is cleared using exact integer homogeneous coordinates; all final gap tests are strict integer comparisons.

## Complete exact input dependencies
Recover ALL THREE CONDITION25 source materials, in order:
1. [internal-source-reference], SHA25620469536cc4461b597cd92b9c7420b89ad4f1efd82ef72aa4f934b9bb772067a,16573UTF8bytes.
2. [internal-source-reference], SHA256a527d91c2ba70ee5220ca4b6ba30964e804fd4fa52a8619d3ae6567608cc8087,13041bytes.
3. [internal-source-reference], SHA256ecb59180686fbea53343e4b78e64b70478df5ede3679acd200c163185c1e29d4,12100bytes.
Their RECOVER_JOIN.py creates source/ with24 complete files; then `python -B -S source/REPLAY.py condition_cold` must emit C622_CONDITION25_G12_COLD_EXACT_AB_MASS_BALANCED_PASS. The complete standalone decoded source dictionary is93169bytes SHA256631fae9cb3d532ace34aa06230c4a5a1c03aec1d99055805e536d2442cb697b3.
4. [internal-source-reference], SHA256225fc6c1539d3c2842e4bc61af14965bcbd8a17ed1ba1fc421e5578ae77251a8,7050UTF8bytes. Decode its single complete RECOVER_TWO_C620_CONTACTS.py and run `python -B -S RECOVER_TWO_C620_CONTACTS.py --source source --parent condition_cold --out two_contact_cold`. Required marker TWO_C620_CONTACTS_COLD_EXACT_OWN121_PASS. RECEIPT.json1225bytes SHA2565bae0cc1e1a1463105ddb02822ec220a5457982edd4eaf8808acd08c237dfbf2.
The two exact input reports are:
- two_contact_cold/e69_73_q129_a02/A.json315807bytes SHA256b15545919f3ab22b5bca850dd82e4b5d0b38fbb7bdd13e9c48becb04ff4d5fbf.
- two_contact_cold/e174_175_q84_a01/A.json313393bytes SHA256e80c5c1d93c99675d416e2fec4f88075dbc8a9ff29336ee493a2e116e771f059.
Each contains every exact raw coordinate, maximal facet, true edge and filled centroid. Their complete data are deterministically reconstructed and hash-checked by the listed self-contained dependencies; no originating sandbox or unlisted ancestor is needed.

## Reconstruction and verification commands
Save the complete Python fence, including its trailing newline, as metric_ball.py:2405bytes SHA2563188e10f7664b4e4f12f824c772a80a4be8ee0505d639dfd2f20ebef98063a84. CPython3.13.5 standard library only; no nondefault argument other than the two input/output paths; grid is literally10^9.

`python -B -S metric_ball.py two_contact_cold/e69_73_q129_a02/A.json e69_73_q129_a02.ball.json`
Expected and observed EXACT_AFFINE_METRIC_BALL_TWO_UNSTABLE_PASS 26443627/1000000000 [67, 93] 47.
Output6390bytes SHA256c70f45b7551835b1ffc8ad8f46e8ba4c2e912ee8e8bfdf54fe55f475ed4a3934.

`python -B -S metric_ball.py two_contact_cold/e174_175_q84_a01/A.json e174_175_q84_a01.ball.json`
Expected and observed EXACT_AFFINE_METRIC_BALL_TWO_UNSTABLE_PASS 31531903/1000000000 [94, 171] 47.
Output6408bytes SHA2568f5847a43f651d3d34013892ea968744b3056809efaf8fcff0fc7d497c8c374f.

```python
"""Exact operator-norm affine-metric exclusion balls for two existing U vertices.
For every symmetric M with ||M-I||_2 <= radius, those vertices remain strict U.
An overall positive scaling of M is immaterial. Shape changes are NOT excluded.
"""
from pathlib import Path
from fractions import Fraction as F
from math import lcm,isqrt
import sys,json,hashlib
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def dump(x):return json.dumps(x,sort_keys=True,separators=(',',':'))
def certify(path,grid=10**9):
 data=Path(path).read_bytes();r=json.loads(data);X=[[F(x) for x in v] for v in r['raw_vertices']];g=[F(x) for x in r['raw_centroid']]
 C=lcm(*(x.denominator for x in g));G=[int(x*C) for x in g];bs=[lcm(*(x.denominator for x in v)) for v in X];aa=[[int(x*b) for x in v] for v,b in zip(X,bs)];z=[[C*x-b*y for x,y in zip(a,G)] for a,b in zip(aa,bs)]
 neighbors=[[] for _ in X]
 for i,j in r['edges']:neighbors[i].append(j);neighbors[j].append(i)
 U=r['unstable_vertices'];assert len(U)==2
 rows=[];radius_n=grid
 for i in U:
  for j in sorted(neighbors[i]):
   d=[bs[i]*x-bs[j]*y for x,y in zip(aa[j],aa[i])];p=dot(z[i],d);A=dot(z[i],z[i])*dot(d,d);assert p<0 and A>0
   n=isqrt((p*p*grid*grid)//A)
   if p*p*grid*grid==n*n*A:n-=1
   assert n>0 and p*p*grid*grid>n*n*A
   radius_n=min(radius_n,n)
   rows.append({'vertex':i,'neighbor':j,'strict_cosine_bound':str(F(n,grid)),'negative_dot':True,'strict_squared_gap_bits':(p*p*grid*grid-n*n*A).bit_length()})
 radius=F(radius_n,grid)
 # Loewner band ((1-r)I,(1+r)I), together with Cauchy-Schwarz, preserves p<0.
 # Any SPD M with eigenvalue ratio <= (1+r)/(1-r) can be scaled into this band.
 return {'input_sha256':hashlib.sha256(data).hexdigest(),'V':r['V'],'E':r['E'],'F':r['F'],'C':2*r['E'],'preserved_strict_U':U,'operator_norm_radius':str(radius),'maximum_metric_condition_number':str((1+radius)/(1-radius)),'affine_map_condition_number_squared_upper_bound':str((1+radius)/(1-radius)),'all_tested_incidences':rows,'conclusion':'For every SPD metric scalable into this closed operator-norm ball about I, U>=2; no own110. This does not exclude other metrics or nonaffine shape changes.'}
if __name__=='__main__':
 r=certify(sys.argv[1]);Path(sys.argv[2]).write_text(dump(r));print('EXACT_AFFINE_METRIC_BALL_TWO_UNSTABLE_PASS',r['operator_norm_radius'],r['preserved_strict_U'],len(r['all_tested_incidences']),flush=True)
```
