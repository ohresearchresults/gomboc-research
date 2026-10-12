# figure-0468

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
>
> The reported C=486 checkpoint still has two stable, two unstable and two saddle equilibria.
<!-- historical-status:end -->

---

# Calm Comet 31 — exact minimal three-cut NW37 continuation under C<500

## Status

I read the continuation `research-journal.md` completely through EOF: 1999 lines, 257970 bytes, SHA-256 `c6f8b861262f9535c6dbb80d3cb5918d9e1d53ed2a7e0b38ce445651aec8b29f`. The literal source-complete authority is `figure-0447` (SHA `efbc9084f0bedab80a14b39769917edcf445ab6af765170cb4e101f77ad12022`); its exact MONO85_G6 packet/census and embedded 41-unit recovery are present in the supplied parent payload. I found no conflict between that literal payload and the branch summary. The previous cycle-credit result `figure-0465` is also consistent with the new exact computation.

No strict110 endpoint was obtained. The main advance is stronger than a failed one-cut test:

1. **One whole-packet cut is exactly impossible** on the fixed source-complete `NW37_MONO85_QUARTER_G6` while retaining all 125 old outside vertices.
2. **Two such cuts are also exactly impossible.** A three-vertex pairwise incompatibility certificate proves that at least three cuts are necessary.
3. An explicit **three-cut cover exists**, so the fixed-outside cap-cover number of the certified 41-vertex packet is exactly **3**.
4. Those three exact cuts give a genuine **C486** body, `V/E/F=162/243/83`, but its own-centroid class is initially `44/11/53`.
5. A rational affine reconsolidation of that same C486 body gives the much stronger exact checkpoint **`NW37_MONO85_PACKET3CUT_T999_AFFINE_M1E5` = strict222/weak000/zero000**, with exactly **one positive P bar and one positive Q bar**. It is not a winner, but it is a durable C<500 two-packet endpoint with only two roots on each side.

The active final bound `E<=249` and the cycle-credit accounting are therefore respected throughout.

## 1. Exact obstruction: the 41-vertex packet is not one-cut separable

Let

```text
X = [24,25,26,27,28,29,30,33,49,55,58,59,62,64,67,71,81,97,117,129,130,134,138,139,140,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165]
Y = {0,...,165} \ X.
```

Here `X` is exactly the parent positive physical dying component and `Y` contains the other 125 old vertices. Exact rational arithmetic gives

```text
conv{x24,x130,x150} ∩ conv{x21,x133} != empty.
```

All five coefficients are strictly positive; their complete rational values are embedded in the recovery capsule below and are verified by exact `Fraction` equality. Consequently `conv(X) ∩ conv(Y) != empty`, so no strict plane can put all of `X` in the removed open halfspace while retaining every vertex of `Y`.

## 2. Exact two-cut obstruction: a three-vertex incompatibility clique

A stronger finite certificate shows that **two** preserving cuts cannot cover `X`. Each of the three segments below meets `K=conv(Y)` at an explicitly certified point:

```text
[x24,x129]  meets conv{x72,x21,x61}
[x129,x153] meets conv{x131,x147,x114}
[x153,x24]  meets conv{x148,x137,x149}
```

For each row, the exact segment parameter `0<t<1` and the three nonnegative barycentric coefficients summing to one are literal in the capsule and checked exactly. If one halfspace retains all of `Y` but removes two endpoints `u,v`, then the entire segment `[u,v]` lies in its removed open halfspace and therefore cannot intersect `K`. Hence **one preserving cut can remove at most one of {24,129,153}**. Two cuts can remove at most two of those three vertices. Therefore at least three cuts are necessary.

This is a genuine exact lower bound on the fixed-vertex/fixed-outside cap architecture, not a numerical search failure and not an obstruction to retained-support motion or to changing the outside vertex set.

## 3. Exact three-cut cover: C486

The following three primitive integer halfspaces are added to the source-complete MONO85_G6 input:

```text
C1:  99625584*x -  6215664*y +  6009034*z <= 64782498
C2: -19700797*x - 95755566*y - 21041631*z <= 65803022
C3:  35823626*x - 34307854*y + 86831095*z <= 52547148
```

They retain every vertex in `Y` strictly. Their exact old-packet removal sets are

```text
C1 removes [138,139,140,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165]
C2 removes [24,25,26,27,28,29,30,33,49,55,58,59,62,64,67,71]
C3 removes [81,97,117,129,130,134,138,139,140,156,162,164]
```

whose union is exactly `X`. Exact nearest signed margins (`n·x-h`) are:

```text
C1: max over Y at vertex147 = -14921965399572342289406/45389553292744047
    min over removed X at vertex150 = 92018320012054280894/279465866949591697
C2: max over Y at vertex61  = -3509348569949607309986/11337383795241863
    min over removed X at vertex71 = 74428317275813494486/240015785740488387
C3: max over Y at vertex131 = -16229522238148695115124/33095037361097663
    min over removed X at vertex156 = 47666183438131470908/96986003417795379
```

Thus no sign is a floating tolerance decision.

The parent packet has `k=41,b=33,r=5`; five old maximal facets lie wholly inside `X`. With `t=3` new facets, the simple cycle-credit formula predicts

```text
F' = 85 - 5 + 3 = 83
E' = 249 + 3*(3-5) = 243
V' = 162
C' = 486.
```

The exhaustive exact H-auditor confirms exactly `V/E/F=162/243/83,C486`, all vertices trivalent. So the prior conditional cycle-credit formula is realized by an actual rational body.

### Raw three-cut body

`NW37_MONO85_PACKET3CUT_T999_1000.json`: **3003 bytes**, SHA-256 `a516a685346266b398faa61bd0c1f85a53e327b71098d74a9dad9d2eb97563de`.

Its exact report is **32380217 bytes**, SHA-256 `409cb400df465cb8687f51123f2bb315c5326f6e9e0f1c67858433feb41538cf`. Audit result:

```text
HULL_EXACT 162 243 83
MASS_MECH_EXACT [44, 11, 53] [0, 0, 0]
FULL_PQ_BASINS_EXACT 10 43
```

So removing every old packet vertex does **not** cancel the equilibrium packet: it produces extensive root transfer after the actual uniform centroid moves. This is an exact version of the earlier warning that destroying a named basin at the old centre is not enough.

## 4. Exact affine reconsolidation: C486 strict222 with one P and one Q packet

Apply the rational/integer linear map `y=M x` with

```text
M = [[161995,-64699, 41355],
     [     0, 96527,-31557],
     [     0,     0, 63951]]
det(M) = 999994839683115 > 0.
```

For each exact input plane `n·x<=h`, the capsule transforms it to the integer plane

```text
(n * adj(M)) · y <= h * det(M)
```

and primitive-reduces the four coefficients. Incidence and true `V/E/F` are unchanged; uniform filled mass transforms exactly, and the audit recomputes the actual transformed centroid rather than substituting a reference centre.

The resulting exact input `NW37_MONO85_PACKET3CUT_T999_AFFINE_M1E5.json` is **6775 bytes**, SHA-256 `d79f7ae7bbca7fdb575c4fca57f271dce1d75c43bafe0b40afc9a842c0929d59`.

Exact report: **26927176 bytes**, SHA-256 `7ac1c60514e3599159de003527bdfbe973159d3658e65bb8992c351673db2db7`.

### Complete actual-centroid mechanics

```text
V/E/F = 162/243/83, C486; simple (all 162 vertices trivalent)
strict S faces = [15,25]
strict U vertices = [1,161]
strict H edges = [[11,135],[51,69]]
additional weak S/U/H = [[],[],[]]
primitive mechanical zero counts = [0,0,0]
```

Stable maximal-face cycles:

```text
face15 = [27,37,98,95,29]
face25 = [0,5,113,116,141]
```

Face-size histogram:

```text
9×3, 17×4, 28×5, 14×6, 6×8, 3×9, 1×10, 2×12, 1×14, 1×15, 1×29 = 83 faces.
```

Actual transformed uniform volume is approximately `1.1957021337505132e15`; actual raw-frame centroid approximately

```text
(-10674.030858030454, 449.65811727994685, -3004.2884786521486)
```

with exact centred common-denominator bit length `16360`. Exact rationals are regenerated by the audit.

Exact global brackets:

```text
TP          in [1847088105165,1847088105166]/1e12
TQ          in [5120315380525,5120315380526]/1e12
minedge/R   in [9611192,9611193]/1e12
inradius/R  in [140452743366,140452743367]/1e12
Vol/R^3     in [134046652991,134046652992]/1e12
min positive physical forest cosine in [68903388624,68903388625]/1e12
```

### Complete physical P landscape

Physical roots are exactly `[1,161]`; there is exactly one positive P bar:

```json
{"peak":161,"older":1,"death_edge":[51,69],"component":[69,70,72,91,94,96,99,100,102,103,104,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161],"boundary":[[141,0],[150,1],[151,2],[149,3],[113,5],[129,9],[132,10],[135,11],[136,12],[130,13],[140,13],[138,14],[134,15],[133,16],[128,17],[142,21],[144,21],[108,22],[114,24],[111,26],[145,28],[148,28],[106,37],[117,48],[69,51],[113,60],[70,63],[103,63],[91,77],[96,78],[107,86],[102,92],[115,92],[108,97],[106,98],[107,101],[124,105]],"path":[161,159,155,112,110,104,103,72,69,51,42,40,31,25,7,5,0,1]}
```

Thus the dying P packet is **67 vertices / 37 cut edges**.

### Complete same-centre polar Q landscape

Polar roots are exactly `[15,25]`; there is exactly one positive Q bar:

```json
{"peak":15,"older":25,"death_edge":[47,65],"component":[0,2,4,5,6,7,8,9,10,11,12,14,15,19,21,22,24,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,49,51,53,54,55,59,61,62,64,65,75,77],"boundary":[[0,1],[0,16],[0,17],[0,20],[0,52],[0,60],[2,20],[4,20],[9,20],[10,20],[41,13],[41,20],[41,25],[27,72],[30,45],[38,45],[39,45],[40,72],[41,47],[41,48],[41,50],[41,66],[41,67],[41,69],[41,70],[41,73],[41,76],[44,52],[44,72],[51,45],[54,45],[59,45],[65,47],[53,82],[54,79],[54,82],[59,72],[59,74],[62,79],[65,80],[65,82],[75,79],[77,79],[77,82]],"path":[15,41,43,61,62,75,77,53,65,47,67,50,69,76,73,66,70,48,25]}
```

Thus the dying Q packet is **49 vertices / 44 cut edges**. The polar is formed at the same actual physical centroid; there is no independent polar recentering.

The exact terminal audit was:

```text
NW37_GMP_FRACTION_ARITHMETIC_CONTROLS_PASS 6.3.0
TURNOVER_EXACT_TETRA446_PRISM446_WEAK123_CONTROLS_PASS
HULL_EXACT 162 243 83
POSITIVE_CENTERED_TETS_AND_ZERO_MOMENTS_PASS
BOUNDARY_MASS_PASS
MASS_MECH_EXACT [2, 2, 2] [0, 0, 0]
INDEPENDENT_MECHANICS_PASS
LANDSCAPES_PASS
FULL_PQ_BASINS_EXACT 1 1
NW37_EXACT_H_DOUBLE_MECHANICS_PASS NW37_MONO85_PACKET3CUT_T999_AFFINE_M1E5_EXACT.json 162 243 83 [2, 2, 2] {'bytes': 26927176, 'sha256': '7ac1c60514e3599159de003527bdfbe973159d3658e65bb8992c351673db2db7'}
```

As in the authoritative parent, the primary exact mechanics/mass audit and AREA_RADIUS implementation are independent mechanics/mass implementations but share the exhaustive H-hull enumerator; this is not claimed as two independent hull enumerators.

## 5. Durable exact recovery capsule

The new patch below is **5970 bytes**, SHA-256 `5a1c3376bbc1c17e5c5d258892fdb8165da58f76b89078cb8c918a38821ce2d3`. It contains the direct one-cut convex-intersection certificate, all three pairwise two-cut obstruction certificates, all three exact cut rows/removal-set checks, and the exact affine map. No numerical optimizer is needed to reconstruct either new exact body.

```python
"""Calm Comet 31 exact NW37 3-cut/minimality + affine-reconsolidation patch.
Requires the source-complete asg_Rz1ST... parent to have been recovered, frozen,
and NW37_MONO85_QUARTER_G6 replayed in the current directory.
CPython 3.13 stdlib only for this patch; exact audit uses parent [internal-source-reference].py.
"""
import json,sys,hashlib,math
from fractions import Fraction as F
from pathlib import Path
sys.set_int_max_str_digits(0)
BASE='NW37_MONO85_QUARTER_G6.json'
REPORT='NW37_MONO85_QUARTER_G6_EXACT.json'
assert hashlib.sha256(Path(BASE).read_bytes()).hexdigest()=='419fcff38d180a217980990f023a366ebb3b55f20f354de2ed44120bd4753f90'
assert hashlib.sha256(Path(REPORT).read_bytes()).hexdigest()=='61f281b8a7dd2766d022fc0e5462e983d103701912dcc2452be07c68cca2937e'
base=json.loads(Path(BASE).read_text()); rep=json.loads(Path(REPORT).read_text())
P=[[F(z) for z in r] for r in rep['raw_points']]
X=[24,25,26,27,28,29,30,33,49,55,58,59,62,64,67,71,81,97,117,129,130,134,138,139,140,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165]
XS=set(X);Y=[i for i in range(len(P)) if i not in XS]
assert len(P)==166 and len(X)==41 and len(Y)==125

def eqpt(a,b):return all(x==y for x,y in zip(a,b))
def comb(ids,w):return [sum(F(q)*P[i][j] for i,q in zip(ids,w)) for j in range(3)]
# Direct conv(X) cap-separation obstruction: triangle(24,130,150) meets segment(21,133).
DX=F(155319373893692105821136431833421278746260966922999799367545463590783)
wx=[F(139438429772737978352651422612987928694008314525115824168421020914592,DX),F(4070862141405176594878963234490048276632952403613904838716600161828,DX),F(11810081979548950873606045985943301775619699994270070360407842514363,DX)]
DY=F(51773124631230701940378810611140426248753655640999933122515154530261)
wy=[F(43753963332291008084709063392731939723387856738984125640029692498019,DY),F(8019161298939693855669747218408486525365798902015807482485462032242,DY)]
assert sum(wx)==sum(wy)==1 and all(q>0 for q in wx+wy)
assert eqpt(comb([24,130,150],wx),comb([21,133],wy))
# Pairwise segment-vs-K certificates. Each tuple is (u,v,Ytriangle,t,lambdas).
paircerts=[
(24,129,[72,21,61],F(69102174089082820882053647263528737647289707574794268208414743,1150353936655443881237137066161285792128664104171929944728447434),[
F(183426976950907050504177923675416358552474084097175654465326159,2875884841638609703092842665403214480321660260429824861821118585),
F(14346051054302102339633530070581847519921778160786686437713532511,23007078733108877624742741323225715842573282083438598894568948680),
F(7193611863199518881075787863240537454231711249874507221132806897,23007078733108877624742741323225715842573282083438598894568948680)]),
(129,153,[131,147,114],F(8304997250156871349152762309750692234138117228034813572788991051856,14700903697077665375286629466600588471130371790020492436817170174147),[
F(6776007628804931825647483520894271980236152312906570914511082939575,14700903697077665375286629466600588471130371790020492436817170174147),
F(7605948420420175179353734403149166381009889919005026557587558391308,14700903697077665375286629466600588471130371790020492436817170174147),
F(318947647852558370285411542557150109884329558108894964718528843264,14700903697077665375286629466600588471130371790020492436817170174147)]),
(153,24,[148,137,149],F(5752003414587725493901391455836437737657916340093565437374935,196235907975950195448796809398395802711778373426641479580056767),[
F(812919164076174362928168482159707730971294321936432191351667865,2354830895711402345385561712780749632541340481119697754960681204),
F(109799233978053790790343984673101126470197882182498432261275975,2354830895711402345385561712780749632541340481119697754960681204),
F(358028124414293547916762311486985193774962069250191782836934341,588707723927850586346390428195187408135335120279924438740170301)])]
for u,v,tri,t,lam in paircerts:
    assert 0<t<1 and sum(lam)==1 and all(q>=0 for q in lam)
    q=[P[u][j]+t*(P[v][j]-P[u][j]) for j in range(3)]
    assert eqpt(q,comb(tri,lam))
# Minimal 3-cut cover. All rows are exact integer halfspaces n.x<=h.
CUTS=[[99625584,-6215664,6009034,64782498],[-19700797,-95755566,-21041631,65803022],[35823626,-34307854,86831095,52547148]]
expected_removed=[
[138,139,140,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165],
[24,25,26,27,28,29,30,33,49,55,58,59,62,64,67,71],
[81,97,117,129,130,134,138,139,140,156,162,164]]
def sign(row,i):return sum(F(row[j])*P[i][j] for j in range(3))-row[3]
for row,want in zip(CUTS,expected_removed):
    assert all(sign(row,i)<0 for i in Y)
    got=[i for i in X if sign(row,i)>0]
    assert got==want
assert set().union(*map(set,expected_removed))==XS
spec={'planes':base['planes']+CUTS}
out=Path('NW37_MONO85_PACKET3CUT_T999_1000.json');out.write_text(json.dumps(spec,separators=(',',':'),sort_keys=True))
assert len(out.read_bytes())==3003 and hashlib.sha256(out.read_bytes()).hexdigest()=='a516a685346266b398faa61bd0c1f85a53e327b71098d74a9dad9d2eb97563de'
# Rational affine reconsolidation: y=M x. Transform n.x<=h by n*adj(M).y<=h*det(M).
M=[[161995,-64699,41355],[0,96527,-31557],[0,0,63951]]
a,b,c=M[0];d,e,f=M[1];g,h,i=M[2]
det=a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
adj=[[e*i-f*h,c*h-b*i,b*f-c*e],[f*g-d*i,a*i-c*g,c*d-a*f],[d*h-e*g,b*g-a*h,a*e-b*d]]
assert det==999994839683115
assert [[sum(M[r][k]*adj[k][cc] for k in range(3)) for cc in range(3)] for r in range(3)]==[[det if r==cc else 0 for cc in range(3)] for r in range(3)]
planes=[]
for row in spec['planes']:
    n=row[:3];H=row[3]; nn=[sum(n[k]*adj[k][j] for k in range(3)) for j in range(3)]; rr=nn+[H*det]; gg=math.gcd(*rr);planes.append([z//gg for z in rr])
aff=Path('NW37_MONO85_PACKET3CUT_T999_AFFINE_M1E5.json');aff.write_text(json.dumps({'planes':planes},separators=(',',':'),sort_keys=True))
assert len(aff.read_bytes())==6775 and hashlib.sha256(aff.read_bytes()).hexdigest()=='d79f7ae7bbca7fdb575c4fca57f271dce1d75c43bafe0b40afc9a842c0929d59'
print('CC31_PACKET3_MINIMALITY_AND_AFFINE_INPUTS_PASS',det)
```

### Reconstruction and verification commands

Starting from the literal parent payload `figure-0447`:

```text
python -B -S RECOVER_NW37_CONTINUATION.py NW37_CONTINUATION
cd NW37_CONTINUATION
python -B -S FREEZE_CONTINUATION.py
python -B -S REPLAY_CONTINUATION.py NW37_MONO85_QUARTER_G6
# save the above 5970-byte block as RECOVER_CC31_PACKET3.py in this directory
python -B -S RECOVER_CC31_PACKET3.py
python -B -S [internal-source-reference].py NW37_MONO85_PACKET3CUT_T999_1000.json NW37_MONO85_PACKET3CUT_T999_AFFINE_M1E5.json
```

Expected patch marker:

```text
CC31_PACKET3_MINIMALITY_AND_AFFINE_INPUTS_PASS 999994839683115
```

Expected promoted endpoint markers include:

```text
HULL_EXACT 162 243 83
MASS_MECH_EXACT [2, 2, 2] [0, 0, 0]
FULL_PQ_BASINS_EXACT 1 1
```

The parent source dictionary remains the authoritative 41-unit dictionary (287207 bytes, SHA `939ee82786c952c9abebbb2f8df72c02a2c9c862cf7a5948cd69116f3be2cb1c`); the new handoff is an exact patch on the parent input, not a substitute reconstruction from approximate coordinates.

## 6. Scientific interpretation and next continuation

The fixed MONO85_G6 packet-removal architecture is now sharply resolved:

- **1 cut impossible exactly.**
- **2 cuts impossible exactly.**
- **3 cuts sufficient exactly.**
- The three-cut topology pays the predicted cycle credit and lands at **E243/C486**, leaving only **6 final true-edge units** under the E249 bound.
- Pure packet removal causes massive root transfer (`44/11/53`), but a rational affine change reconsolidates it all the way to exact **222/weak000 with one P and one Q packet**. This is meaningful finite control, not a winner.

A finite numerical metric nomination led to the rational matrix `M`; no sampled metric-cell failure is promoted to an affine exclusion. The exact endpoint itself needs no numerical source for recovery.

The most useful next work is therefore one of two paths:

1. **Fixed C486 semialgebraic/affine cell:** start from the exact 222 matrix above and solve the coupled five-dimensional SPD sign problem for killing one physical and one polar root while checking mixed-H. Because the exact endpoint already has only two S and two U roots and no weak equilibria, this is much narrower than the raw three-cut body. However the final cell must be exact; finite high-condition metric scouts are not evidence of impossibility.
2. **Changed geometry:** use the exact three-cut minimality theorem as a reason not to spend effort on one-/two-cap MONO85 variants. A fourth surviving replacement facet on the original E249 architecture would violate the simple edge budget unless compensated by extra old-facet turnover or nonsimple excess. If broad packet-interface surgery is required, switch deliberately to source-complete MONO47 C270 or MONO49 C282, where the edge reserve is far larger.

For the affine C486 checkpoint, the surviving P packet is 67/37 and Q packet 49/44, so root-count reconsolidation came at the cost of large whole-basin interfaces. Any successor must continue to score complete P/Q components/cuts, not only root count or local escape margins.

**No strict110/weak000 C<500 body is claimed.** The durable new results are the exact cap-cover number `tau(X|Y)=3`, an actual exact C486 three-cut realization, and a source-recoverable exact C486 strict222/weak000/zero000 affine reconsolidation with one complete P and one complete Q bar.
