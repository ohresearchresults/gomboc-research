# minimum-0137

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# PROTECTED_C618_RIDGE_LOCKED_CHAMBER_V1

## Result

**No smaller attaining body is claimed. I obtained an exact, finite geometric obstruction for the protected triangular-patch cancellation, together with a complete cycle-compatible two-arrow target for the next search.** The obstruction allows arbitrary motion of the unwanted facet134 pole and arbitrary geometry elsewhere; it is not merely persistence of strict equilibria inside a small neighborhood of the entire polytope.

The starting object remains the exact protected body with V/E/F=175/309/136, C618, own strict(S,U,H)=(2,2,2), physicalweak000, and M=N=I. The accepted attaining upper endpoint remains canonical C622; the inherited bracket is unchanged. The parent identifies stable facets3,134, unstable raw-lex vertices93,160, and saddle edges(5,93),(160,163). These are the parent's new labels, not canonical old labels or a projective delete78 identity.

## 1. Input authority and executed evidence

I read the complete 1783-line supplied journal, including its literal parent payload through EOF, decoded its fourteen-file capsule, and read every decoded source/data file. The initial truncation of the displayed attachment was resolved by reading the remaining lines through1783.

The required parent is minimum-0126, SHA-256 `6c9896535051e460d8c96881b69c2f101ea5510a026e7ef83d4ae27479f4ebe3`. With one terminal LF in result_markdown, its compact UTF-8 version2 envelope reproduces that hash exactly. That authenticated envelope is **58564 bytes**, not the journal's63707-byte description. This is a serialization-length metadata discrepancy; the declared parent identity and the frozen geometric input authenticate successfully.

The protected generator is12851 bytes, SHA `6c31d8ba6d2b688d20901a2eacdc67552e024e5009e0bf1c7d1cf1b4197a2edd`. I reconstructed its true halfspace body and executed the exact A auditor. It reproduced raw.json17907 bytes/SHA `da754f0583173d72d6bae0d808256efd9c526c25624af78a96bd7d69f5939d56` and A.json362259 bytes/SHA `5438455ed9f92d616c0357807a604117b4a22461e13bd14c2544cbbf0d59e533`.

This newly executed audit enumerates actual supporting-plane intersections, reconstructs maximal facet cycles and true edges, checks boundedness/Euler/orientation, integrates the true uniform volume and first moment, and recomputes the full strict/weak census after subtracting that exact centroid. There are346 positive integration triangles and1236 nonzero true-edge primitives. Independent B and third-mass agreement remain inherited parent evidence; I do not describe my repeated A execution as a newly independent B audit.

No old canonical numerical helper, transient optimizer vector, or thirty-file convenience download was used. The four-file capsule below contains every computational dependency of the new certificate.

## 2. Exact complementary-tree target:307 safe arrows and only two missing arrows

Write x_i=v_i-g for the actual own-centroid coordinates and q_f for the corresponding normalized facet poles. Use one reciprocal pair M,N=M^-1. Define

    Dv(i,j) = x_i^T M(x_j-x_i),
    Df(f,h) = q_f^T N(q_h-q_f).

At the protected parent, choose the largest **raw, unnormalized true-edge** outgoing primitive at each nonroot, with larger destination label breaking an exact tie. The complete source reconstructs these choices exactly, rather than comparing floating near-zero values.

The vertex forest has roots93,160 and basin sizes19,156. The facet forest has roots3,134 and basin sizes42,94. Their173 primal and134 dual selected edges are disjoint. **The only two unassigned true edges are exactly the two saddle edges(5,93) and(160,163).**

Consequently the natural cancellation target is

    vertex160 -> vertex163,
    facet134 -> facet8.

Adding these arrows produces a primal spanning tree of174 edges rooted at93 and a dual spanning tree of135 edges rooted at3. They are complementary and together partition all309 true edges. Their complete reconstruction is in the capsule; no historical catalogue mapping is needed.

The two joining paths are, in full,

    160 ->163 ->165 ->167 ->169 ->172 ->174 ->173 ->171 ->170
        ->168 ->166 ->164 ->162 ->161 ->158 ->155 ->99 ->93

    134 ->8 ->9 ->1 ->29 ->95 ->96 ->62 ->2 ->128 ->0 ->127 ->3.

### Why these targets, rather than the locally least-negative escape

The exact existing arrows include152->160 and159->160. Thus160 cannot escape back to152 or159 while those guards remain nonnegative. For any distinct endpoints,

    Dv(i,j)+Dv(j,i) = -||x_i-x_j||_M^2 < 0.

The same identity holds for the poles with N. The existing dual arrows5->134 and6->134 therefore block134->5 and134->6. The only cycle-compatible root exits through the current true neighbors are160->163 and134->8.

In particular, the largest raw true-edge escape at160 points to159. A corrector that tries to make that escape nonnegative while preserving159->160 has an **all-orders geometric contradiction**, not merely a difficult optimization landscape. I have not assumed that an unavailable historical numerical helper selected this exact normalization or witness; this diagnosis concerns the freshly reconstructed, explicitly specified forest.

### Sufficiency of the target packet

For any genuine realization of this same lattice, at its actual centroid and with one reciprocal metric, positivity of these309 selected arrows would certify strict110weak000. Each nonroot has an increasing-norm path to its designated root. A root cannot have a weak outgoing escape, since that would contradict the increasing-norm return path. Every true edge carries a selected positive primal or dual primitive, precluding both a strict saddle and every physical weak packet.

**The parent does not satisfy the two added arrows.** This is an exact sufficient target, not an attaining construction or a certified trajectory.

## 3. Finite frozen-ridge obstruction: rotating facet134 alone cannot reach its admissible exit

The unwanted triangle is134=[5,10,93], with neighbors5,6,8. The parent already establishes the nonsimple nature of the patch and the genuine independent plane actuators99,135.

Fix the actual centered vectors

    a=x_10, b=x_93, p=q_8,

and keep N=I. Allow q, the candidate pole of facet134, to range over the **entire affine line**

    a.q=b.q=1.

This includes every plane rotation through the fixed ridge[10,93], and deliberately overcovers the convexly admissible rotations.

Let A have rows a^T,b^T, K=AA^T, and r=(1,1)^T-Ap/2. Exact completion of squares gives

    max_{Aq=(1,1)} q.(p-q) = ||p||^2/4 - r^T K^-1 r.

The generator verifies K positive definite and proves

    -29154/1000000 < maximum < -29153/1000000.

Thus **every candidate pole through that ridge has Df(134,8)<-29/1000**, even before convex-hull restrictions are imposed.

For comparison the present pole satisfies

    -29171/1000000 < Df(134,8) < -29170/1000000.

The entire relaxed optimization can improve that primitive by only a value between17/1000000 and18/1000000. The exact relative improvement is less than3/5000, or0.06% of the present deficit. These are rationally verified inequalities, not decimal optimization tolerances.

This explains a specific finite obstruction: pivoting134 while keeping10,93 and8 fixed cannot cancel its stable-saddle pair through8, regardless of the pivot magnitude. Arbitrary actual mass compensation elsewhere does not change this conclusion when it restores the same centroid and metric. The conclusion does not depend on assuming that facet134 is a freely movable three-parameter plane.

## 4. Stronger closed geometric/metric collar, with a small literal certificate

The preceding obstruction persists when the ridge endpoints, the adjacent pole, the true centroid, and the reciprocal metric change. The following statement is analytic and covers a whole continuous family, not a finite sample.

### Theorem

Consider any genuine full-dimensional convex3-polytope at its own volume centroid, in coordinates with that centroid0. Suppose134 remains a triangular maximal facet whose three true neighboring facets are5,6,8. Put a=x_10,b=x_93,p=q_8 and q=q_134. Set

    a0=(-491035,-218400,-224365)/1000000,
    b0=(  13533,  -5720,1009434)/1000000,
    p0=(-2273503,-390444,1018922)/1000000,
    epsilon=1/2500.

Assume every component of a-a0,b-b0,p-p0 has absolute value at most epsilon; N is symmetric and every entry of N-I has absolute value at most epsilon; M=N^-1; and

    Df(5,134)>=0, Df(6,134)>=0.

Then134 is **strictly stable**. If the designated stable facet3 is retained, S>=2. Therefore this entire protected chamber contains no desired strict110weak000 endpoint.

There is no bound on q134 and no bound on the other vertices or supports apart from genuine convex incidence and the two stated incoming guards. This is why the result is stronger than a small full-body strict-persistence ball.

### Proof with explicit rational data

Let lambda=(219/50,989/500), so its entries are positive and sum to3179/500. Since a.q=b.q=1, define

    z=Np+lambda1*a+lambda2*b.

Then exactly

    q^T N(p-q)
      = -(q-N^-1*z/2)^T N(q-N^-1*z/2)
        + z^T N^-1*z/4 - lambda1-lambda2.

The entrywise metric bound gives N>=(2497/2500)I. Write m=2497/2500 and z0=p0+lambda1*a0+lambda2*b0. The componentwise error is bounded by

    eta=epsilon*(1+lambda1+lambda2+sum_j |p0_j|+3*epsilon).

Indeed z-z0=(N-I)p+(p-p0)+lambda1(a-a0)+lambda2(b-b0). Therefore

    Df(134,8)
      <= sum_j (|z0_j|+eta)^2/(4m)-lambda1-lambda2
      = -53891603560050241/12485000000000000000
      < -1/250.

The two remaining outgoing primitives satisfy

    Df(134,5)=-||q134-q5||_N^2-Df(5,134)<0,
    Df(134,6)=-||q134-q6||_N^2-Df(6,134)<0.

The poles of distinct maximal facets are distinct. All three outgoing true dual-edge primitives are therefore strictly negative, proving strict stability of134.

The exact protected body lies strictly inside the stated feature box: every component of its a,b,p differs from the displayed rational center by less than1/2000000. Its metric is I and both incoming guards are strictly positive. The capsule verifies these memberships using the actual exact centroid, not its rounded display value.

### Consequence for genuine mass actuators

Moving the real plane actuators99/135, solving actual volume/first-moment equations, and pivoting the nonsimple134 patch cannot overcome this obstruction while the three centered features and N remain in the stated boxes and the two incoming guards remain protected. Rank4 moment control alone cannot supply the missing mechanical exit.

A successful continuation must instead change the locked local geometry enough to leave this sufficient collar, change the metric beyond it, reroute the selected dual guards before reversing them, or change the actual patch architecture. None of these alternatives is excluded by the theorem. In particular this is **not** local minimality ofC622, exclusion of all312 contact directions, or an all-metric obstruction to protectedC618.

## 5. What remains useful for continuation

The exact new information is a complete complementary target packet and a proof that its stable-side cancellation cannot be achieved inside the specified protected chamber. A fresh nonlinear search should use160->163 and134->8 as the two explicit negative target rows, protect the307 existing positive rows, and include actual convexity, coplanarity and own-volume-moment constraints.

On the stable side, merely optimizing the134 plane through fixed10,93 is now analytically exhausted. Genuine motion of the degree-four vertex10 and/or adjacent facet8 is a concrete next direction, coupled to the real99/135 moment actuators. Escape-tree rerouting is another possibility, but changing a selected parent must be distinguished from allowing a new equilibrium. The complete target trees in the report make such exchanges testable.

No new coupled nonlinear cancellation path, exact deformed endpoint, or whole-path sign certificate was obtained. The certificate below is the durable successor **method and obstruction**, not a successor attaining body. The preexisting protected strict222 construction remains available unchanged.

## 6. Complete standalone recovery

The decoder below contains four complete files: the exact protected generator, its exact atlas reconstructor, the full exact A geometry/mass/contact auditor, and the complete new locked_patch.py. No parent file, source download, external numerical library, random seed, or old sandbox is required.

Environment actually executed: CPython3.13.5 standard library, assertions enabled. The new program uses no floating-point acceptance test. Save the decoder as recover_locked_patch.py with UTF-8/LF and run:

    python -B -S recover_locked_patch.py FRESH_DIRECTORY
    python -B -S FRESH_DIRECTORY/locked_patch.py FRESH_DIRECTORY/LOCKED_PATCH.json

Expected final markers are:

    LOCKED_PATCH_SOURCE_RECOVERY_PASS 4
    PROTECTED_PARENT_EXACT_A_REPLAY_PASS 175 309 136 2 2 2
    CYCLE_SAFE_TARGETS_PASS 160->163 134->8
    TWO_TARGETS_COMPLETE_TRUE_EDGE_PARTITION_PASS 174 135 309
    ALL_RIDGE_POLES_MAXIMUM_LT_MINUS_29_OVER_1000_PASS
    TRUE_FEATURE_AND_RECIPROCAL_METRIC_BOX_1_OVER_2500_PASS
    PROTECTED_RIDGE_LOCKED_PATCH_EXACT_OBSTRUCTION_PASS 3048 785761bcac48eb654e7b4737fc0407ea45ca66ce862a5bdbe45292f34cf8fc7a

A source-only cold extraction and execution completed and produced the same3048-byte report byte for byte. The report contains the complete175-entry primal parent array and136-entry dual parent array, both joining paths, edge-partition counts, all small rational certificate data and exact checkpoint pins.

Source and output pins:

    RECONSTRUCT.py:1801 bytes
    2a8c5685baa64c8a2e6998f898c889172b7c7f92fbf07ae9cf1d8b8d37e695fd
    check_A.py:5483 bytes
    ad72cc198140249c1e52a615513354036c04f4c718333a7beed64fba4b43d7f3
    protected_GENERATOR.json:12851 bytes
    6c31d8ba6d2b688d20901a2eacdc67552e024e5009e0bf1c7d1cf1b4197a2edd
    locked_patch.py:8878 bytes
    f9b1d3db5dbd66ff68be288d39f4a9964a6123b1837f83193914d4aa26d805cc
    recover_locked_patch.py:16050 bytes
    ae01ecfab6284ad3b0d4ca3862217d938f233d7074e698c28ae619457b542579
    source-map JSON:29455 bytes
    3105517980b6bb73832ee2d57b2cd921adf00a7d9d06c8ba3f5b63c07e62eef0
    XZ payload:11236 bytes
    d8450c96f82393577cbfb286576ee7aa79c3aefbcce07811ef7a91023bd2d9b4
    normalized base64:14984 characters
    c562b27972fbf368e615bda79ff25c4c40cda9d383286000dbb0be295689d353
    LOCKED_PATCH.json:3048 bytes
    785761bcac48eb654e7b4737fc0407ea45ca66ce862a5bdbe45292f34cf8fc7a

```python
"""Recover a self-contained exact C618 local-obstruction proof. Python 3.13.5."""
import base64, hashlib, json, lzma, sys
from pathlib import Path
assert __debug__ and len(sys.argv) == 2
B64 = """
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
"""
b = ''.join(B64.split()).encode('ascii')
assert len(b) == 14984 and hashlib.sha256(b).hexdigest() == 'c562b27972fbf368e615bda79ff25c4c40cda9d383286000dbb0be295689d353'
r = lzma.decompress(base64.b64decode(b, validate=True))
assert len(r) == 29455 and hashlib.sha256(r).hexdigest() == '3105517980b6bb73832ee2d57b2cd921adf00a7d9d06c8ba3f5b63c07e62eef0'
files = json.loads(r)
assert set(files) == {'RECONSTRUCT.py','check_A.py','protected_GENERATOR.json','locked_patch.py'}
out = Path(sys.argv[1])
assert not out.exists()
out.mkdir(parents=True)
for name, text in files.items():
    assert Path(name).name == name
    (out/name).write_bytes(text.encode('utf-8'))
print('LOCKED_PATCH_SOURCE_RECOVERY_PASS', len(files))
```

Convenience copies: standalone recovery source (`recover_locked_patch.py`) and exact certificate report (`LOCKED_PATCH.json`). These supplement the complete embedded recovery, not replace it.
