# figure-0312

Historical AI scientific report · saved 2026-09-05 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: unreviewed-encoded-blocks-omitted.

---

# Sharp Atlas 56 — exact centroid-preserving reduction

## 1. Literal verdict

A genuinely reduced homogeneous convex polyhedral Gömböc was constructed and independently replayed:

**V=76,937; E=230,792 true edges; F=153,857 maximal faces; C=461,584. Its exact own-volume centroid is (0,0,0), and its strict equilibrium class is (S,U,H)=(1,1,0).**

There are no degenerate face, vertex, or edge equilibria. The unique stable maximal face is now a **16-gon**, not the parent's 256-gon, in x=-100327/102400. The unique unstable vertex remains (104473/102400,0,0). The volume is approximately 4.18310916308215355167536882062305431.

Relative to the mandated 134,131-vertex parent, this removes 57,194 vertices and 342,684 units of mechanical complexity: **42.6404% fewer vertices and 42.6082% lower C**. It does **not** meet C<1000. No minimality, worldwide-priority, or physical-manufacturing claim is made.

“Moment preserving” here means all three first moments stay exactly zero at fixed uniform density. **Total volume is not held constant.** This is not translation to a new artificial reference point, a projective recentering, or a density change.

[Complete exact archive, generators, certificates, independent replays, OBJ and ASCII STL](sandbox:/mnt/data/SHADOW_SURGERY_76937.zip)

Archive SHA-256: `b68ca6d26038f4cf5e35184f8b7c47fc6e00b244c9c36020369cfe6e817cf64e`.

## 2. Source authority and actual work

The normative parent was the user-specified Library file `file_000000007de881f4837ea5182ada2fb8`, `POLYHEDRAL_GOMBOC_VERIFICATION.zip`. Its local archive SHA-256 is `0848b0aef0cafd5a3ae6a69cbf387760fb1ae79e01b65720abdc65b54ffe365a`. The required input table `exact_polyhedron.npz` has SHA-256 `ac1e9893101e1be6c1be5d63d95538dc96894dfa8827b7b7b245fef4caef484d`.

This is the actual 134,131-vertex winner, not the lost 227,905-vertex construction, the distinct 171,167-vertex reconstruction, or the falsified J56 orphan. The journal's authoritative parent data and audit agree with this identification. :contentReference[oaicite:0]{index=0} The supplied parent verifier was actually rerun successfully before reduction.

The accepted construction proceeded as follows:

| Part | Actual result |
|---|---|
| Five paired inner-deletion batches, with an exact degree-three compensator | 134,131 → 108,607 vertices; stable 256-gon preserved |
| Two coupled safe outward caps, serving also as higher-capacity moment actuators | A separately replayed 108,569-vertex centred winner |
| Five further multi-ball inner-deletion batches, with the outer positive cap dependent on the moment equation | Inner core decreases to 77,215 vertices |
| Four genuine stable-face ear surgeries | Stable polygon 256 → 128 → 64 → 32 → 16; inner core becomes 76,975 vertices |
| Final outer-cap hull and exact dependent parameter | **76,937 actual vertices**, full class **(1,1,0)** |

The intermediate NPZ **cores alone are not the centred bodies**. Their specified compensator coordinates and, in the later batches, the two C2-paired outer caps are part of each complete body's exact definition. The scalar equations are maintained as dependent geometry, not promised as a later repair.

## 3. The improved no-birth mechanism

For a point w retained in the body, put phi_w(p)=p·(w-p). At an equilibrium about the origin, p must support the body with outward normal parallel to p, hence phi_w(p)≤0 for every retained w. Therefore a strict positive witness excludes **all equilibrium types at p**, including the complete normal cone of a seam vertex or edge.

The exact identity

`phi_w(sum lambda_i p_i) = sum lambda_i phi_w(p_i) + sum_{i<j} lambda_i lambda_j |p_i-p_j|²`

for nonnegative barycentric coefficients summing to one proves that checking the vertices of a convex cell suffices for the whole cell.

Requiring one witness for an entire vertex star was unnecessarily restrictive. I replaced it by a **finite tetrahedral multi-ball cover**. For deletion of v, compute the actual visible replacement triangles f of conv(neighbours(v)); the removed region is the union of tetrahedra conv(v,f). Each tetrahedron may use a different retained witness. When no single witness covers a tetrahedron, bisect an edge at its exact dyadic midpoint and continue on both children. A certificate records the split edge, both child branches, and the witness at each leaf. Every leaf's four inequalities are checked exactly in the same quadratic field. Prefix completeness is checked, so there is no omitted part of the cell.

This covers the entire closed changed region, not merely the interiors of new facets. Consequently all new seam cones are covered too. For a deletion batch, every witness and its actual C2 partner is retained; selected centres are nonadjacent. The independent replays verified **292,605 representative tetrahedral leaves** across the ten ordinary inner batches and **6,102** across the four stable-face batches. Their reflected copies follow from the explicitly checked orthogonal involution.

The outward version is equally useful. If q is outside K, the added cap is the union of conv(q,f) over the **actually visible old boundary triangles**. Cover this complete union by retained-witness shadow balls. Old witnesses remain points of conv(K,q) even if they cease to be extreme. The two maximal outer caps have 60 and 10 visible triangles, respectively, and require 301 and 22 leaf cells. An independent audit checked **every one of the 153,946 final-core supporting triangles against each maximal cap point**, reproduced the complete 60/10 visibility sets, and verified all 323 leaves. Thus the outer-cap envelope is not based on a partial floating-point visibility list.

One-common-ball scans found no useful outward coarsening in the tested sample; subdivision covers found many numerical proposals. Only the two frozen, fully exact-audited caps are used in the claimed successor.

## 4. Actual hulls and exact moments through topology changes

For ordinary deletion, the replacement is **only the visible side of the neighbour hull**, not every facet of that hull. Supporting triples are enumerated exactly. Acceptance checks the oriented patch boundary, positive radial determinants, new internal hinges, and new-to-old seam hinges. The final full table is independently checked as a closed convex boundary. Nonadjacent deletion caps have disjoint interiors: the vertices of one cap are retained by the deletion of the other, placing the first cap in the other's retained convex hull.

A continuous contraction can keep the moving vertex's x-coordinate fixed: choose q in conv(neighbours(v)) with q_x=v_x, and move v to (1-u)v+u q. For non-base vertices the neighbour x-coordinates bracket v_x; for a base ear use the midpoint of its two retained base neighbours. The full swept region lies in the certified cap.

Within each actual incidence cell, its x-moment is affine in u: a tetrahedral determinant is affine in the one moving vertex, and the sum of its four x-coordinates is constant. Hull events are linear determinant roots. Rebuild the actual local hull at each event, giving a continuous **piecewise-affine** moment function rather than continuing an inverted old fan.

To preserve the centroid throughout a batch, use a common fraction of each cap's signed final moment loss, not a common fraction of its coordinate displacement. Invert the monotone piecewise-affine moment functions to obtain the individual displacements. The disjoint compensator then carries the negative of the sum. This supplies a continuous exact moment-balanced path through the actual cells. C2 pairing kills the y- and z-moments identically.

The first compensator is original vertex 24472 and its actual partner 24473. Its three neighbours are 24322,24522,24530, with replacement triangle (24322,24530,24522). Its fixed-x target is the midpoint of the two intersections of that triangle with x=Ix_24472. Witness 25048, and its partner 25049, covers the complete control tetrahedron. In raw moment units 1/(24D⁴), the removed moment of one complete control cap is

`Rc = -2062447256072555370603159342097350393824437500000`.

If S(t) is the sum of the representative inner-cap losses in the first five batches, the control parameter is **alpha=-S(t)/Rc**, strictly between zero and one. The final alpha is approximately 0.7092270952073112588. Every accepted batch's identity and interval membership was checked independently.

The two outer caps provide much greater physical leverage. The negative maximal cap contributes approximately -1.8578612285909764e-6 to Mx per representative cap; the positive maximal cap contributes approximately +4.03944712853915e-6. These are actual added-volume moments, not Jacobian rank estimates.

For a visible old triangle f=(a,b,c), in scaled coordinates, define

`G_f(u) = det(b-a,c-a,q(u)-a) * (q_x+a_x+b_x+c_x)`.

The actual added x-moment is G_f(u)/(24D⁴). With q_x fixed, each visible-cell contribution is affine in u. Facet visibility thresholds are isolated and sorted exactly. The negative cap is used at full depth; the positive depth s is the unique applicable cell solution of

`G_positive(s) + G_negative(1) = R_extra(t)`.

Here R_extra includes the five later inner batches and all stable-face ears. The final value is approximately **s=0.53604528416373337475**. The exact formula is given below. All inner replacement planes were checked against both maximal actuator points and their C2 partners: **165,896 ordinary-batch checks plus 1,012 base-batch checks**. Thus these surgeries do not silently change the reserved actuator visibility geometry.

The complete raw x-moment identity is

`-2*S(t) - 2*alpha*Rc - 2*R_extra(t) + 2*G_negative(1) + 2*G_positive(s) = 0`.

The factors two are the C2 partners. The global verifier separately reintegrates the final actual boundary; it does not trust this surgery identity.

## 5. Stable-face surgery and symmetry discipline

The base was reduced by changing its **true ear stars**, not by treating long planar display diagonals as physical neighbours. Before each batch, triangulate each selected polygon corner as an ear and triangulate the retained central polygon separately. Replace the actual ear-plus-lateral star, verify its complete shadow cover, and reconstruct the smaller maximal polygon. The origin's projection stays strictly inside it by exact oriented-edge tests.

The final stable face uses these original vertex IDs:

`10,21,42,53,74,86,105,118,137,150,169,181,202,213,234,245`.

These are its members, not a claimed cyclic ordering; the verifier reconstructs its outward boundary cycle. It remains in x=-100327/102400. There are now **13**, not 253, coplanar display diagonals: all other maximal faces are triangles. Keeping the original 256-gon would itself force E≥512 and C≥1024, so this surgery removes that particular obstruction to the eventual C<1000 objective.

C2 was not inferred from index parity. The original table has **280 exceptions** to adjacent-index pairing. The involution is recovered by the exact lookup

`(Ix,Iy,Iz,B) -> (Ix,-Iy,-Iz,B)`.

The final algebraic coordinate set is checked independently under (x,y,z)->(x,-y,-z); its only fixed vertex is the apex. Asymmetric triangulations inside a flat maximal face are not mistaken for a failure of body symmetry.

A subsequent conservative 16-to-8 ear search returned no certified ears. This is a search/certificate failure, **not** an exclusion of eight-sided stable faces or other base surgeries.

## 6. Executed verification

The following are completed calculations, not proposed checks:

* `audit_surgery.py enhanced`: `INDEPENDENT_LOCAL_SURGERY_REPLAY_PASS`; ten exact batches, all recorded cap moments, dyadic covers, witness retention, C2 stars, replacement and seam hinges, fixed-x control, and outer-actuator separation.
* `audit_base.py`: `INDEPENDENT_EXACT_BASE_SURGERY_PASS`; all four stable-face batches, 6,102 leaf covers, exact strict stable-foot tests and moment budgets.
* `audit_macro.py`: `INDEPENDENT_FULL_OUTER_CAP_AUDIT_PASS`; complete maximal visibility, 323 leaf covers, retained-core witnesses and exact final moment closure.
* `final/verify.py`: `INDEPENDENT_EXACT_AUDIT_PASS`. It reconstructs every volume moment, 230,805 triangulated edges, 13 coplanar diagonals, 153,857 maximal faces, 230,792 true edges, all vertex links, all rank-three normal cones, and all equilibrium predicates. The exact radial degree is one using ray (5,7,19). Every true hinge is strictly convex. It returns strict **(1,1,0)** and zero degenerate equilibria.
* A vertex-only Qhull reconstruction, without reading the endpoint triangle table during construction, includes **all 76,937 vertices** and proposes 153,870 triangles. Exact hinge checking needs **zero corrective flips**. Every non-base maximal face and the stable polygon agree with the exact endpoint. Result: `INDEPENDENT_VERTEX_ONLY_HULL_REPLAY_PASS`.
* The compact generator below, using only the normative parent, retained-orbit mask and the two explicit scalar formulas, reproduces the final compressed vertex table **byte for byte**.
* The archive was extracted afresh; all **73 manifest entries** matched, and its global exact verifier was rerun successfully in that fresh extraction.

The global verifier is the supplied independent verifier adapted for sparse Q(t) y/z coordinates, with additional exact C2 checks and explicit lattice exports. It imports neither construction engine. The local ledger auditors were separately written. This is computational independence, not a claim of external human peer review or proof-assistant formalization.

The global convexity argument is not “Qhull said convex.” Positive radial determinants and an oriented closed genus-zero manifold give a positively oriented radial map; the independently counted degree one makes it one-sheeted. The radial piecewise-linear gauge is convex because every hinge is convex. Hence the reconstructed surface is the actual global convex boundary. Exact rank-three incident-normal tests establish that every serialized vertex is extreme.

For mechanics, the verifier tests the face-edge primitives n·(vi×vj), the vertex escape primitives vi·(vj-vi), and all four true-edge conditions. An edge is a saddle only when both endpoint projections lie inward and both incident-normal coefficients have the required strict signs. Maximal faces are merged before these tests. No Euler-count shortcut or facet-only exclusion is used.

Exact final table hashes:

```
vertices.csv.gz   aa02467f39a8f6a6fe8aee2616242f6e7fb5637fcc0afea373e7f3400c8de7c0
triangles.csv.gz  4d3f37ee6d9324675ef0c313788e288361ab561a0c85329f0a420a889c80a4be
root.json        d16fcb3cb18013ebfe9b47adffaf7a4f6e75b3ce85a534acef3c0ce8beab2915
definition.json  fece4fce69b189983409f847cdba0d94dabe1eb0043baf40294bb966911f6321
```

OBJ and ASCII STL were exported and actually read back. They contain the same 153,870 oriented triangles and no zero-area triangle in the binary64 display coordinates. They are **display approximations**, not the exact certificate or a manufacturing-tolerance guarantee.

## 7. Complete exact successor definition, independent of the surgery logs

The only source input to this section is the **already supplied normative parent table**, identified by the NPZ SHA above. The archive also includes that table. No worker-local missing geometry, unspecified selector or smooth-source rounding is required.

Let

```
D = 109951162777600
A = 242532801191139787687932546990427414728876250
Bq = 101848919526731522877578696155796030367663848604515625
Cq = 357120335825870005344493551745618712701499207415356147
L = -3506373366228948793748504708011554915237434524020426433279451151733060427211
Q = 10^75
```

Let t be the unique root of A*t²+Bq*t+Cq=0 in **[L/Q,(L+1)/Q]**. Parent row i denotes ((Ix_i-t*B_i)/D,Iy_i/D,Iz_i/D).

### Retention mask

Recover the exact involution r from the coefficient quadruples. Form the sorted list of representatives i satisfying i≤r(i), including the one fixed apex. There are **67,066 orbits**. Base64-decode and zlib-decompress the following payload to **8,384 bytes**. Bit k, least-significant-bit first within each byte, says whether to retain both members of representative orbit k. Ignore the six trailing padding bits. The decompressed-byte SHA-256 must be

`6d769c4b690460559c80c8f5900655598cbe8129f86a5a3abb85ecb173617bc4`.

This retains **76,933 original IDs**. Replace the two control coordinates as specified next and append four new vertices. The resulting 76,937 points are all extreme.


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]


**Correction to the inline transport representation:** the retention mask must be taken from the complete, checksum-validated payload in the accompanying Markdown handoff, not from the incomplete transcription immediately above. The complete literal payload and the exact same coordinate recipe are contained in [the full self-contained handoff](sandbox:/mnt/data/shadow_surgery_result.md), and its machine-readable version is [result JSON](sandbox:/mnt/data/shadow_surgery_result.json). The mask is not a mathematical uncertainty: its complete reconstruction was executed and reproduced the final vertex table byte for byte. The abbreviated block above is not a usable decoder input.

### Exact scalar controls and all changed coordinates

For a triple p write p(t)=p0+p1*t+p2*t². Set

```
S = (
 381679933624462470917544704369178805873012138281250,
 108436511969235479577029309673802037576977253781250,
 138869109174947232241391792657024619140471875)
Rc = -2062447256072555370603159342097350393824437500000
alpha = -S(t)/Rc

U = (
 8518671250058152848015162198348022165727800745721086,
 318385981535212400127841992683239920765674611716250,
 -834603740657879877355999973090841247958936200)
V = (
 13813505588473730450187968403767622132959612553531250,
 1268080539207937749446043250174642120284700205000,
 -32326952872524410689821000785939601563997450)
s = U(t)/V(t)
```

All vectors in the rest of this definition are **scaled by D**; divide by D once, at the end.

Replace original row 24472, whose original scaled coordinates are

`c=(-101896499199350,-26993117626775,23278947803400)`,

by c+alpha*(q-c), where

```
q = (
 -101896499199350,
 -142419002349122019491996961152325/5239330502592358952,
 240714561967646715989719736131575/10478661005184717904)
```

Replace row 24473 by its exact C2 image. These replace the old control points; do not retain both old and moved versions.

Append the following two points and their C2 images:

```
q_minus = (
 -99622816193050,
 -39382199613307,
 -15514055579755)

q_plus = (
 83611031366750 - 2241374767*t,
 -53915192292400 - 119811067127*s,
 -46995397260425 - 104433805323*s)
```

Keep all other selected parent coordinates unchanged. **The convex hull of this explicit finite point set is the claimed successor.**

Arithmetic is closed in Q(t). Represent a field element by rational pair (a,b)=a+b*t. Addition is componentwise; multiplication is

`(a,b)*(c,d)=(a*c-(Cq/A)*b*d, a*d+b*c-(Bq/A)*b*d)`.

For division use the conjugate: the norm of (a,b) is a²-(Bq/A)*a*b+(Cq/A)*b², and its inverse is ((a-(Bq/A)*b)/norm,-b/norm). Compare signs at both endpoints of the isolating interval, refining the bracket if needed; all actual audit signs resolve at the supplied bracket. There is no new algebraic root to solve.

For practical reconstruction, `compact_generator.py` expands this definition using the complete retained-orbit mask. `reconstruct.py` independently rebuilds the same geometry from the ten inner-deletion masks and four base-ear batches. `hull_replay.py` supplies a fresh vertex-only hull proposal and exact hinge checks. The definitive all-feature verifier reads only the expanded exact coordinates, triangle table and root definition.

A minimal mask decoder, with I and b read from the parent, is:

```python
import base64
import hashlib
import zlib

lookup = {(*map(int,p), int(bi)): i for i,(p,bi) in enumerate(zip(I,b))}
r = [lookup[(int(p[0]),-int(p[1]),-int(p[2]),int(b[i]))]
     for i,p in enumerate(I)]
assert all(r[r[i]] == i for i in range(len(I)))
reps = [i for i,j in enumerate(r) if i <= j]
raw = zlib.decompress(base64.b64decode(payload))
assert len(reps) == 67066 and len(raw) == 8384
assert hashlib.sha256(raw).hexdigest() == '6d769c4b690460559c80c8f5900655598cbe8129f86a5a3abb85ecb173617bc4'
keep = set()
for k,i in enumerate(reps):
    if (raw[k//8] >> (k%8)) & 1:
        keep.update((i,r[i]))
assert len(keep) == 76933
```

## 8. Precise remaining gates and continuation

The result is a certified **43% reduction**, not a near-C1000 body. No minimum-complexity theorem, quantitative manufacturing tolerance, or independent-coordinate perturbation box has been obtained. Exact strict inequalities establish the endpoint; the constrained physical paths are protected by full shadow covers and dependent moment equations. Do not equate the narrow root interval with a manufacturing tolerance.

The ordinary enhanced coarsener stopped after its deliberately chosen five additional rounds, not because the final geometry was excluded. The last round still found 4,708 safe proposals and accepted 1,153 pairs. This is a genuine resumable construction frontier. The unsuccessful 16-to-8 ear attempt was conservative and likewise supplies no obstruction theorem.

The strongest continuation is to restart from the **complete final body**, retaining the two actuator envelopes and their witnesses, and replace connected multi-vertex caps by fewer extreme points. Use the dyadic multi-ball tetrahedral cover, not the excessively strong one-witness-per-star requirement. Protect an actuator's whole visibility region, or recompute its exact piecewise-affine moment response when that region changes. Continue using the same quadratic field and a hard scalar moment equation under the explicitly verified C2 symmetry. Recompute the actual hull after every circuit; do not score the actuator-free core as though it were centred.

The stable side count has already fallen from 256 to 16, so future work is no longer blocked by that combinatorial floor. The outstanding challenge is removing several hundred thousand true-edge complexity units while maintaining these complete geometric and moment certificates. The present calculation proves neither that this mechanism will reach C<1000 nor that it cannot.
