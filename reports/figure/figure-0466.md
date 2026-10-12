# figure-0466

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Quiet Finch 32 — C40 support-stack handoff

## Outcome

I did **not** find an own-centred strict `110` / additional-weak `000` C40 member, and I do not claim a C40 exclusion. I did obtain two new exact rational C40 checkpoints that materially improve the branch in the requested whole-basin sense: **both complete transferred positive packets contract to two vertices simultaneously**. The primary low-arithmetic body `C40_PACKET2X2_COARSE100` is still strict `222/weak000/zero000`, but its physical dying component is `2 vertices / 6 cut edges` and its same-centre-polar dying component is `2 vertices / 4 cut edges`, versus the exact parent ROBUST_TRANSFER packets `4/8` and `5/6`. The second exact checkpoint `C40_PACKET2X2_THICK1000` has the same `2/6 + 2/4` packet sizes with substantially larger normalized edge and inradius guards.

The supplied parent establishes the ROBUST_TRANSFER exact class and its complete two residual basins; I used that literal payload as authority, not the journal synopsis. :contentReference[oaicite:0]{index=0} The supplied metric material gives the exact 315,000 rooted-tree reduction for fixed-geometry mono-U feasibility; I use that below as the cleanest next exact subproblem, but I did **not** complete that atlas and therefore make no affine-metric exclusion claim. :contentReference[oaicite:1]{index=1} No supplied source was truncated, no required dependency was missing, and I found no conflict between the literal parent and the journal summary.

## 1. Primary exact checkpoint: `C40_PACKET2X2_COARSE100`

### Literal rational input

~~~text
knots = [19/25, 81/100]
kappa = [
  [103/100,  7/50],
  [54/5,     119/25],
  [53/25,    971/100],
  [21/100,   17/100]
]
A = [
  [3/4,   0,     0],
  [13/10, 99/50, 0],
  [23/20, 97/100,17/25]
]
~~~

All eight curvature coefficients are strictly positive and `0 < 19/25 < 81/100 < 1`. This is not the proved-sterile fixed-profile shear ray: both knots, all four positive curvature profiles, and a genuinely oblique affine metric changed.

`det(A)=5049/5000>0`. The exact Gram matrix is

~~~text
G=A^T A =
[ 143/40       7379/2000    391/500   ]
[ 7379/2000    48613/10000  1649/2500 ]
[ 391/500      1649/2500    289/625   ]
~~~

with leading principal minors

~~~text
143/40,
15066949/4000000,
25492401/25000000,
~~~

all positive, so the metric is exactly SPD. In particular `G13=391/500` and `G23=1649/2500` are nonzero: this checkpoint genuinely uses oblique transverse/vertical metric coupling rather than the parent's `G13=G23=0` mechanism.

### Exact mass and maximal complex

The exact slabwise homogeneous mass is

~~~text
raw volume = 470168128829/250000000000
raw first moment = (
  2621448277551605719/1500000000000000000,
 -382070260240729697/300000000000000000,
  60409439239709/50000000000000
)
raw centroid = (
  1037375653957897/1116346962000000,
 -151195195979711/223269392400000,
  23905595267/37211565400
)
transformed volume = 2373878882457621/1250000000000000
transformed actual centroid = (
  1037375653957897/1488462616000000,
 -185305112567341/1395433702500000,
  394733102081993/465144567500000
)
~~~

The working own-centred body is obtained by subtracting that transformed actual centroid. The inherited exact auditor checks mass three ways: the slabwise Simpson formula, the oriented maximal-boundary tetrahedral identity, and 16 positive tetrahedra from an interior anchor; all agree exactly.

Exhaustive supporting-triple reconstruction gives exactly `V/E/F/C = 10/20/12/40`, not a nominated complex. The maximal faces are

~~~text
0 [0,2,1]       1 [0,3,2]       2 [0,4,3]       3 [0,1,4]
4 [1,2,6,5]     5 [2,3,7,6]     6 [3,4,8,7]     7 [4,1,5,8]
8 [9,5,6]       9 [9,6,7]      10 [9,7,8]      11 [9,8,5]
~~~

so the face histogram is exactly `8 triangles + 4 maximal quadrilaterals`. Every vertex has degree 4. The 20 true edges are

~~~text
0-1 0-2 0-3 0-4
1-2 2-3 3-4 4-1
1-5 2-6 3-7 4-8
5-6 6-7 7-8 8-5
5-9 6-9 7-9 8-9
~~~

which is the exact C40 graph recorded in the supplied metric-reduction material. :contentReference[oaicite:2]{index=2} The common denominator of all centred vertex coordinates is only **57 bits**.

### Full strict / weak mechanics

The exact maximal-face / true-vertex / mixed-true-edge census is

~~~text
strict(S,U,H) = (2,2,2)
additional weak = (0,0,0)
primitive zero = (0,0,0)
S faces = [0,9]
U vertices = [1,3]
H true edges = [[0,3],[5,6]]
~~~

Thus `H=0` is **not** inferred from Morse count; it is explicitly false here and the two strict mixed-edge equilibria are identified. Both apices remain rigorously non-U. Exact positive apex escape witnesses are `0->1` and `9->8`, with outgoing dots

~~~text
0->1 = 46859076915276633796987/55817348100000000000000 > 0
9->8 = 5359781412855549799111/44653878480000000000000 > 0.
~~~

Geometric guards:

~~~text
min true-edge length / R in [15883891986,15883891987]/1e12
inradius / R             in [31197388951,31197388952]/1e12
~~~

For scale/conditioning context only, the floating 2-norm condition number of this exact `A` is about `6.14846`; this floating diagnostic is not part of the certificate.

### Complete physical P landscape

There is exactly one positive physical H0 bar:

~~~text
peak = 1, elder = 3
birth = 244083549440822138940540734127739753
        /12462305395666294440000000000000000
death = 24828205149084927172301333473666032469
        /17821096715802801049200000000000000000
component = [1,5]
cut = [1-0, 1-2, 1-4, 5-6, 5-8, 5-9]
attaining path = [1,5,6,2,3]
~~~

Numerically, birth is about `19.5857461113`, death about `1.39319176283`, so the birth-relative depth is still about `0.928867057`. This is a **packet/interface contraction**, not a claim that the remaining well is shallow.

### Complete same-centre-polar Q landscape

There is exactly one positive same-centre-polar H0 bar:

~~~text
peak = face 0, elder = face 9
birth = 260595925734362099024537460551812500
        /7594086792631977731837288119980889
death = 2875218705413622315637006344980800000000000000
        /1985692068722890135053941284367531298647670781
component = [0,1]
dual cut = [0-3, 0-4, 1-2, 1-5]
attaining path = [0,1,2,6,5,9]
~~~

Numerically, birth is about `34.3156370016`, death about `1.44796806650`, so the birth-relative depth is about `0.957804424`. Again the exact advance is whole-packet contraction, not small scalar persistence.

### Exact coupled-interface observation

This checkpoint does more than shrink two unrelated packets. The unwanted physical peak is **vertex 1**, while the unwanted polar/stable peak is **face 0 = [0,2,1]**: the two unwanted peaks are incident. Moreover the Q cut dual adjacencies correspond to these primal true edges:

~~~text
dual 0-3  <-> primal edge 0-1
dual 0-4  <-> primal edge 1-2
dual 1-2  <-> primal edge 0-3
dual 1-5  <-> primal edge 2-3
~~~

The physical P cut is `0-1, 1-2, 1-4, 5-6, 5-8, 5-9`. Hence the two complete cuts share the **same two primal carriers `0-1` and `1-2`**. In addition, the two strict H edges already sit on the residual interfaces: `0-3` underlies the Q cut and `5-6` lies in the P cut. This is an exact, continuation-useful coupling that the ROBUST_TRANSFER seed did not expose so tightly. It does not prove that moving those carriers suffices—root transfer remains possible—but it gives a concrete joint interface to attack rather than two independent scalar objectives.

## 2. Secondary exact checkpoint: `C40_PACKET2X2_THICK1000`

I also preserved a distinct exact member with the same `2/6 + 2/4` packet sizes but stronger geometric guards. Literal input:

~~~text
knots = [921/1000, 473/500]
kappa = [
  [1717/1000,303/1000],
  [1034/125,689/200],
  [2013/1000,351/50],
  [43/200,41/200]
]
A = [
  [51/50,0,0],
  [71/50,127/50,0],
  [141/100,47/50,19/50]
]
~~~

Exact audit:

~~~text
V/E/F/C = 10/20/12/40
strict(S,U,H) = (2,2,2)
weak = (0,0,0), primitive zero = (0,0,0)
S=[0,8], U=[1,3], H=[[0,3],[1,2]]
P: peak1 -> elder3, component [1,5], cut6, path [1,2,3]
Q: peak0 -> elder8, component [0,1], cut4, path [0,1,2,6,5,4,8]
common centred denominator = 93 bits
minedge/R in [48881206363,48881206364]/1e12
r/R       in [42462890112,42462890113]/1e12
~~~

Its birth-relative depths are about `0.889689618` (P) and `0.944047039` (Q), and the floating condition number of exact `A` is about `12.3667`. It is therefore a useful alternative if continuation values thickness and edge reserve more than arithmetic simplicity. The complete exact birth/death fractions and mass are regenerated by the capsule below; no sandbox file is needed for them.

## 3. What changed relative to the exact parent

The authoritative parent `C40_ROBUST_TRANSFER_G1` is exact `222/weak000`, with physical component `[1,2,5,6]` and cut 8, and polar component `[7,8,9,10,11]` and cut 6. :contentReference[oaicite:3]{index=3} Both new exact checkpoints retain C40 and apex escapes, but reduce those complete packet sizes simultaneously:

~~~text
                         physical packet      polar packet
ROBUST_TRANSFER_G1          4 / cut 8           5 / cut 6
PACKET2X2_COARSE100         2 / cut 6           2 / cut 4
PACKET2X2_THICK1000         2 / cut 6           2 / cut 4
~~~

No own110 endpoint appears: both new bodies remain exact strict222 with two explicit strict H edges. Thus this is a substantial non-record checkpoint, not a promoted solution.

## 4. Fixed-geometry metric evidence and scope

For a fixed raw C40 geometry, the supplied exact reduction says mono-U is equivalent to one of 315,000 rooted-tree linear sign systems in the six symmetric entries of `G`, together with `G` SPD; every feasible strict cone contains rational `G`. :contentReference[oaicite:4]{index=4} I did not enumerate those 315,000 systems for either new raw profile, so I make **no** fixed-profile `U>=2` claim and no C40 obstruction claim.

I also did not reuse the parent's proved sterile shear half-line `s>=1673/500`; the discovery search varied knots, positive curvatures and oblique SPD metrics.

## 5. Exact recovery capsule

The exact findings depend only on the immutable parent source unit `RECOVER_C40_STACK_RESULT.py`, which the parent result contains literally through its base85 capsule. Required identity:

~~~text
parent assignment: figure-0459
parent result SHA-256: bdb999984adf0469cd9eba7849b5f0423d0f44580f0c3beda8a9fda4bbfdbff5
RECOVER_C40_STACK_RESULT.py: 14221 bytes
SHA-256: afa840b4f4b9b4ad4c949899adc2d083e787b81786479cefa0ef649b477f0bca
~~~

Save the following source exactly as `VERIFY_C40_PACKET2X2_PAIR.py`:

~~~python
from pathlib import Path
from fractions import Fraction as F
import importlib.util,hashlib,json,sys
PARENT_ASSIGNMENT='figure-0459'
PARENT_RESULT_SHA256='bdb999984adf0469cd9eba7849b5f0423d0f44580f0c3beda8a9fda4bbfdbff5'
PARENT_SOURCE_SHA256='afa840b4f4b9b4ad4c949899adc2d083e787b81786479cefa0ef649b477f0bca'
BODIES={
'C40_PACKET2X2_COARSE100':{
 'knots':['19/25','81/100'],
 'kappa':[['103/100','7/50'],['54/5','119/25'],['53/25','971/100'],['21/100','17/100']],
 'A':[['3/4','0','0'],['13/10','99/50','0'],['23/20','97/100','17/25']]},
'C40_PACKET2X2_THICK1000':{
 'knots':['921/1000','473/500'],
 'kappa':[['1717/1000','303/1000'],['1034/125','689/200'],['2013/1000','351/50'],['43/200','41/200']],
 'A':[['51/50','0','0'],['71/50','127/50','0'],['141/100','47/50','19/50']]}}

def load_parent(path):
 p=Path(path);b=p.read_bytes();h=hashlib.sha256(b).hexdigest();assert h==PARENT_SOURCE_SHA256,(h,PARENT_SOURCE_SHA256)
 s=importlib.util.spec_from_file_location('c40_parent_exact',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def gram(m,d):
 A=[[F(x) for x in r] for r in d['A']];G=[[sum(A[k][i]*A[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
 assert G[0][0]>0 and G[0][0]*G[1][1]-G[0][1]**2>0 and m.det(*G)>0
 return A,G

def main(parent_path,out_path):
 m=load_parent(parent_path);aud={};Gs={}
 for name,d in BODIES.items():
  A,G=gram(m,d);r=m.audit(d,name);aud[name]=r;Gs[name]=G
  assert r['VEFC']==[10,20,12,40] and r['strict']==[2,2,2] and r['weak']==[0,0,0] and r['primitive_zero']==[0,0,0]
  assert r['U']==[1,3] and len(r['Pbars'])==len(r['Qbars'])==1
  p,q=r['Pbars'][0],r['Qbars'][0]
  assert len(p['component'])==2 and len(p['boundary'])==6 and len(q['component'])==2 and len(q['boundary'])==4
  assert q['component']==[0,1] and q['boundary']==[(0,3),(0,4),(1,2),(1,5)]
 if True:
  r=aud['C40_PACKET2X2_COARSE100'];p,q=r['Pbars'][0],r['Qbars'][0]
  assert r['S']==[0,9] and r['H']==[[0,3],[5,6]] and r['commonD_bits']==57
  assert r['edge_R_1e12']==[15883891986,15883891987] and r['r_R_1e12']==[31197388951,31197388952]
  assert (p['peak'],p['elder'],p['component'],p['boundary'],p['path'])==(1,3,[1,5],[(1,0),(1,2),(1,4),(5,6),(5,8),(5,9)],[1,5,6,2,3])
  assert (q['peak'],q['elder'],q['path'])==(0,9,[0,1,2,6,5,9])
  assert r['raw_volume']==F(470168128829,250000000000) and r['volume']==F(2373878882457621,1250000000000000)
  assert m.det(*[[F(x) for x in z] for z in BODIES['C40_PACKET2X2_COARSE100']['A']])==F(5049,5000)
  assert Gs['C40_PACKET2X2_COARSE100']==[[F(143,40),F(7379,2000),F(391,500)],[F(7379,2000),F(48613,10000),F(1649,2500)],[F(391,500),F(1649,2500),F(289,625)]]
 if True:
  r=aud['C40_PACKET2X2_THICK1000'];p,q=r['Pbars'][0],r['Qbars'][0]
  assert r['S']==[0,8] and r['H']==[[0,3],[1,2]] and r['commonD_bits']==93
  assert r['edge_R_1e12']==[48881206363,48881206364] and r['r_R_1e12']==[42462890112,42462890113]
  assert (p['peak'],p['elder'],p['component'],p['boundary'],p['path'])==(1,3,[1,5],[(1,0),(1,2),(1,4),(5,6),(5,8),(5,9)],[1,2,3])
  assert (q['peak'],q['elder'],q['path'])==(0,8,[0,1,2,6,5,4,8])
  assert r['raw_volume']==F(162171375242301147,10**18) and r['volume']==F(19957295951443306053261,125000000000000000000000)
  assert m.det(*[[F(x) for x in z] for z in BODIES['C40_PACKET2X2_THICK1000']['A']])==F(123063,125000)
 data={'parent_assignment':PARENT_ASSIGNMENT,'parent_result_sha256':PARENT_RESULT_SHA256,'parent_source_sha256':PARENT_SOURCE_SHA256,'bodies':BODIES,'gram':Gs,'audit':aud}
 b=(json.dumps(m.enc(data),sort_keys=True,separators=(',',':'))+'\n').encode();Path(out_path).write_bytes(b);h=hashlib.sha256(b).hexdigest()
 print('C40_PACKET2X2_PAIR_EXACT_PASS',len(b),h,[(n,aud[n]['strict'],len(aud[n]['Pbars'][0]['component']),len(aud[n]['Qbars'][0]['component'])) for n in BODIES])
if __name__=='__main__':
 if len(sys.argv)!=3:raise SystemExit('usage: python -B -S VERIFY_C40_PACKET2X2_PAIR.py PARENT_RECOVER_C40_STACK_RESULT.py OUT.json')
 main(sys.argv[1],sys.argv[2])
~~~

Environment: CPython `3.13.5`, standard library only for exact replay. Run:

~~~text
python -B -S VERIFY_C40_PACKET2X2_PAIR.py RECOVER_C40_STACK_RESULT.py C40_PACKET2X2_PAIR.json
~~~

Expected marker:

~~~text
C40_PACKET2X2_PAIR_EXACT_PASS 9313 565b8f5e4635b9e8eb90f12a27f0dfa2e29480d315f38d255aa47a32f7ca2a7b [('C40_PACKET2X2_COARSE100', [2, 2, 2], 2, 2), ('C40_PACKET2X2_THICK1000', [2, 2, 2], 2, 2)]
~~~

Observed deterministic files:

~~~text
VERIFY_C40_PACKET2X2_PAIR.py  3999 bytes
SHA-256 b24cc30cf9008fc68564b83b07b1090dea673ea9d215dc814145c17fc68717a7

C40_PACKET2X2_PAIR.json       9313 bytes
SHA-256 565b8f5e4635b9e8eb90f12a27f0dfa2e29480d315f38d255aa47a32f7ca2a7b
~~~

The JSON contains the literal inputs, exact Gram matrices and the full exact audit objects, including actual mass, all S/U/H labels, full P/Q bar data, raw/transformed centroids, `own_H`, feature guards and exact normalized intervals. Convenience copies from this execution are [verifier](sandbox:/mnt/data/VERIFY_C40_PACKET2X2_PAIR.py) and [full exact report](sandbox:/mnt/data/C40_PACKET2X2_PAIR.json); they are supplements only, not the recovery authority.

Evidence tier: one inherited exhaustive exact H/V mechanics-and-mass implementation, not two independent full auditors. It nevertheless performs three mutually consistent exact mass calculations and reconstructs the maximal complex from supporting triples rather than trusting nominations.

## 6. Most useful continuation

1. **Run the exact 315,000-tree mono-U atlas on the COARSE100 raw profile first.** Its 57-bit centred arithmetic is much cheaper than the thicker alternative. If a strict SPD U1 cone exists, rationalize an interior `G` and immediately audit S and mixed-H exactly. If none exists, preserve a genuine finite certificate cover (positive-definite/Farkas style) and then move the raw profile; do not elevate another random screen into an obstruction.
2. In shape space, target the exact shared interface around **vertex 1 / face 0** and the common cut carriers **`0-1` and `1-2`**. Allow root exchange and temporary births, but score the complete P and Q components/cuts after every move. Because `H=[0-3,5-6]` is already embedded in the two residual interfaces, include explicit H elimination rather than waiting for a Morse count.
3. Use `PACKET2X2_COARSE100` for exact sign-cell/certificate work and `PACKET2X2_THICK1000` for finite geometric surgery where larger `minedge/R` and `r/R` guards are valuable. They are materially different continuation resources, not aliases.
4. Keep birth-relative depth in the objective: both exact packet2x2 bodies still have deep residual wells even though their complete components are tiny. The advance is topology/interface contraction, not scalar near-cancellation.
5. Do not return to the fixed-profile shear half-line already closed by the parent. C42 remains secondary; nothing here excludes it, but C40 now has a much smaller coupled two-packet interface to exploit.

No C<500 strict110/weak000 body is promoted by this handoff. The strongest durable new result is an exact, low-arithmetic C40 strict222 checkpoint in which **both complete residual basins have contracted to two-node packets whose cuts overlap on two true primal carriers**, plus a thicker exact companion and a complete source-only replay.
