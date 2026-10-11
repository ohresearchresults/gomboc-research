# material-91678762d123

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# LEAD_APEX_UNIFORM12R — an exact all-directions far-apex exclusion

## Status and scope
Original coordinator derivation, with a complete proof below. It concerns a fixed full-dimensional uniformly dense convex polyhedron K and one added point p, forming conv(K,p), always at its OWN volume centroid. It proves at least two strict unstable equilibria outside an explicit bounded region. It does not assert that finite apex changes fail, that a changing core fails, or that the target own110,C<500 is impossible. It is not a new own110 construction. The exact rational filter in recovery part 1 is a reusable sufficient exclusion test, not a complete equilibrium census. RA41 inspired the question, but this proof has no numerical or source dependency on RA41 or WIDE.

## Exact centroid decomposition
Let V0>0 and c0 be the volume and centroid of K. Let p be outside K. Decompose conv(K,p) minus K into the pyramids based on the facets of K strictly visible from p. Their interiors are disjoint; their common boundaries have zero volume. Write vi>0 for their volumes and fi for their planar area centroids. A uniform pyramid with base centroid fi and apex p has volume centroid (p+3fi)/4, by integrating the parallel sections of area proportional to the square of their distance from p.

Set A=sum vi, V=V0+A and alpha=A/(4V), so 0<alpha<1/4. The own centroid is exactly
c = [V0*c0 + sum vi*(p+3fi)/4]/V
  = alpha*p + (1-alpha)*q,
q = [V0*c0 + (3/4)*sum vi*fi]/[V0+(3/4)*A].
Every fi and c0 lies in K. The coefficients in the last expression are nonnegative and sum to one. Therefore q belongs to K. This is an exact disjoint-volume identity; it is not an unjustified weighted blend of overlapping bodies.

## Strict old-vertex witness without incidence assumptions
Choose any vertex v of K maximizing ||v-c|| over the finite old vertex set. For every other old vertex w,
||w-c||^2 - ||v-c||^2 = 2(v-c).(w-v)+||w-v||^2 <= 0,
so (v-c).(w-v) <= -||w-v||^2/2 < 0.
This stays strict even if several old vertices have the same maximal distance. A point satisfying this inequality for all other generators uniquely maximizes its own radial linear functional and is a strict unstable vertex. Thus the only extra chord that may invalidate this witness after adding p is the chord from v to p. No old facet or edge is assumed to survive the new hull.

Put b=p-q, x=v-q, B^2=||b||^2, D^2=max_{w in Vert K}||w-q||^2. Since q is in K and the convex function ||.-c||^2 reaches its maximum on an old vertex,
||x-alpha*b||^2=||v-c||^2 >= ||q-c||^2=alpha^2 B^2.
Hence 2alpha*b.x <= ||x||^2. Consequently,
(v-c).(p-v)
 = (x-alpha*b).(b-x)
 = (1+alpha)b.x - ||x||^2 - alpha*B^2
 <= [(1-alpha)/(2alpha)]||x||^2 - alpha*B^2
 <= [(1-alpha)/(2alpha)]D^2 - alpha*B^2.
Therefore the exact sufficient inequality
             2 alpha^2 B^2 > (1-alpha) D^2                  (1)
forces the additional chord margin to be strictly negative. Combined with all old chords, it proves that v remains a genuine vertex and a strict unstable equilibrium of conv(K,p) at its own centroid c.

For the apex and an arbitrary old vertex w, write y=w-q. Since p-c=(1-alpha)b,
(p-c).(w-p) = (1-alpha)b.(y-b)
 <= -(1-alpha) B(B-D).
Condition (1) implies B^2 > [(1-alpha)/(2alpha^2)]D^2 >= 6D^2, because alpha<1/4. In particular B>D, so every apex chord is strictly negative as well. The apex p is a second genuine strict unstable vertex.

THEOREM A. If (1) holds, conv(K,p) has at least two strict unstable equilibria at its own uniform-volume centroid. It cannot be own110, irrespective of its stable, saddle, or weak equilibria. Failure of (1) is inconclusive. The exact chord checks in the supplied program can succeed even when this sufficient inequality fails.

## Uniform compact search region for every apex direction
Translate coordinates so that a ball B_r(0), r>0, lies in K and K lies in B_R(0), R>0. Let s=||p||. Choose any two orthogonal directions perpendicular to p. The planar diamond whose four vertices are +/-r times those directions has area 2r^2 and lies in K. The cone from that diamond to p is contained in conv(K,p) and has volume (2/3)r^2 s.

If s>=3V0/r^2 then vol(conv(K,p))>=2V0, which implies
alpha=(V-V0)/(4V)>=1/8.
Since q belongs to K, B=||p-q||>=s-R and D<=diam(K)<=2R.
If also s>=12R, then B>=11R. Therefore
2alpha^2 B^2-(1-alpha)D^2
 >= 2*(1/8)^2*(11R)^2 - (7/8)*(2R)^2
 = (121/32-112/32)R^2 = 9R^2/32 > 0.

THEOREM B. For EVERY direction, if
          ||p|| >= max(12R, 3V0/r^2),
then conv(K,p) has at least two strict unstable equilibria at its own volume centroid. The old farthest vertex and the added apex provide them. All possible own110 members of the one-apex extension of this fixed core must lie strictly inside this explicit ball. This is independent of the normal fan and remains valid across all visibility and hull-combinatorial changes.

The factor 12 is convenient rather than optimal. The first condition can use s>(1+4*sqrt(7))*R, together with the same volume bound; a circular base improves 3V0/r^2 to 6V0/(pi*r^2). The rational diamond/12 version avoids irrational constants and includes equality at the stated radius safely. None of these bounds excludes changing the core along with the apex.

## Exact finite filter: computation and limitations
For each outward triangle (a,b,c) of a triangulated maximal old facet, put
w0=det(a,b,c), wa=max(0,((b-a) cross (c-a)).(p-a)).
Then W0=sum w0=6V0, T0=sum w0*(a+b+c)=24M0,
Wadd=sum wa, Sadd=sum wa*(a+b+c),
W=W0+Wadd, T=T0+Sadd+Wadd*p,
c=T/(4W), alpha=Wadd/(4W), q=(T0+Sadd)/(4W0+3Wadd).
The source validates exact supporting outward maximal facets, strict convex facet cycles, closed oriented edges, connectivity, and Euler characteristic. It then computes the own centroid with Fraction arithmetic, chooses the farthest old vertex, and tests all its chords and all apex chords. It does not run a new convex-hull algorithm and does not presume the old incidence survives. TWO_STRICT_U_CERTIFIED is a rigorous exclusion once the supplied core passes validation. INCONCLUSIVE is not a positive construction, and NO_EXTERNAL_APEX means there was no positive added volume. The filter does not count S or H, does not check all weak equilibria, and does not report the new true edge count.

## Recovery capsule and exact manifest
Part 1 of 2 is the complete literal Python source in immutable material [internal-source-reference], named LEAD_APEX_UNIFORM12R recovery part 1 of 2 — exact_apex_filter.py.txt. Preserve those bytes without a Markdown fence or extra prefix. Save them under the filename exact_apex_filter.py.

Input/source: exact_apex_filter.py, 9290 bytes, SHA-256 d1fe096adc753dffedfa0d5903ab0df129694b2335126e70a360504fb42a9c80.
Dependencies: Python >=3.10, standard library only; rational arithmetic has no library-version-dependent tolerance. All self-test inputs are embedded in the source. There are no omitted datasets, seeds, helper modules, floating precisions, or non-default numerical parameters.

Reconstruction command after saving the part-1 text bytes:
  python -B -S exact_apex_filter.py --self-test > self_test_output.txt
Verification commands:
  sha256sum exact_apex_filter.py self_test_output.txt
  tail -n 1 self_test_output.txt
Expected terminal marker: EXACT_APEX_FILTER_SELF_TEST_OK.
Expected output: self_test_output.txt, 600 bytes, SHA-256 f9fe60065f20f5783db680f31dcca4dbeac29ae99a195ed48b9014b1b59d61f0.

These exact bytes were replayed locally in the coordinator turn. They supersede any earlier transient draft byte counts, hashes, or arithmetic examples; this manifest refers to the actual preserved source. A successful self-test is evidence for implementation behavior, not the proof of Theorems A/B: the proof is given above.

Complete expected output, with a final newline:
{
  "added_volume": "132",
  "alpha": "33/140",
  "apex_min_margin": "1049499/140",
  "apex_strict_U": true,
  "core_volume": "8",
  "farthest_old_vertex": 0,
  "new_centroid": [
    "0",
    "0",
    "3399/140"
  ],
  "new_volume": "140",
  "old_root_strict_U": true,
  "q": [
    "0",
    "0",
    "99/107"
  ],
  "root_apex_margin": "357719/140",
  "root_old_min_margin": "2",
  "status": "TWO_STRICT_U_CERTIFIED",
  "sufficient_slack": "121893776229/112200200",
  "visible_triangles": 2,
  "warning": "This is an exclusion filter, not a full equilibrium census."
}
EXACT_APEX_FILTER_SELF_TEST_OK
