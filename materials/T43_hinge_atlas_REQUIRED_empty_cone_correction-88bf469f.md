# material-88bf469fede8

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# REQUIRED correction to the full-hinge eligibility atlas: empty crossed-facet fan

This correction supersedes the critical-plane completeness/count claims in [internal-source-reference] and earlier atlas sources. It is an exact patch to that material's complete17773byte source, not a new alias of an old object. A computational successor needs BOTH the complete base material [internal-source-reference] and this correction. The full C272 body, strict/closed audit, finite quadratic root certificates and C<=408 bound remain unchanged. The prior claim of1219 eligible critical-plane occurrences was wrong: the corrected count is1231.

## Found boundary omission
When no original facet is crossed, T_H={v:n.v=0} is the WHOLE tangent plane, not {0}. The earlier tangent_rays routine looped over an empty list and returned no rays, incorrectly marking such a critical plane ineligible. Four original nonfacial triangular sections of T43 have this case:
- old triangle(0,6,13): n=(-183326,165982,136361),h=147404849; the positive side consists only of old vertex4.
- (11,16,18): n=(13460,-19941,-5325),h=-12477095; the negative side consists only of vertex17.
- (21,28,29): n=(9488,-104865,-63450),h=-50994355; the negative side consists only of vertex25.
- (29,33,36): n=(-288188,-164734,-100329),h=-198390803; the negative side consists only of vertex34.
All coordinates here use the original integer rows before division by1000. These planes contain a closed cycle of old edges, have zero strictly crossed old edges and zero crossed facets. Every sufficiently small tangent velocity is admissible; finite amplitudes are still bounded by the remaining support inequalities. They represent tetrahedral-ear shears at fixed base/height, not unbounded free translations of a half-body.

The four distinct planes appear under their three old edges each, so12 previously false-ineligible critical occurrences become eligible. Correct counts:123 old edges;5166 old-vertex-sign intervals;5028 interior;238 flat-angle cuts;1142 eligible and4124 impossible open cells unchanged;4905 edge-indexed critical interior occurrences, NOW1231 eligible, comprising1209 old-vertex occurrences and22 chart infinities. With the238 flat-angle boundary cases,1469 eligible boundary occurrences have crossed-edge counts0..26. Open-cell maximum27 remains unchanged. Thus the entire single-convex-full-hinge/affine-post-map family still has V<=70,C<=408. The omitted cases actually have no new section vertices and C<=246. The family bound was unaffected, but the old geometric-plane eligibility completeness claim required this correction.

The patch returns four exact generators +/-u,+/-w for the full tangent plane when the crossed-facet list is empty. They are generators, not extreme rays of that nonpointed cone. For every nonempty crossed-facet list the original exact cone test is unchanged. The standalone source was rerun completely after this correction, including the full atlas, complexity census, true-hull/own-mass/weak audit of C272 and the two finite-domain root certificates. This is one exact implementation, not independent verification.

## Exact patch and reconstruction
Base: extract T43_hinge_atlas_and_turnover_recovery.py from [internal-source-reference],17773bytes SHA c68703403c31dcef466a5ded85a353ed98b8e58b755d57b304c3dcab81fb0c1c.
Save the complete diff below as T43_fullspace_hinge_fix.patch including final newline:602bytes SHA e403a8d9171ebafd0c2e6664f1ea0b48147cf0a9b038ed501ab27ec123420f7d.
Apply `patch -p0 < T43_fullspace_hinge_fix.patch`, then run `python -B -S T43_hinge_atlas_and_turnover_recovery.py`.
Corrected source:18033bytes SHA50d0ec077f6d9d6fb7b29cb897d9a678f2e573daca42cc94b61fce63cf7815e6.
Corrected outputs:
- T43_HINGE_ELIGIBILITY_ATLAS.json1992388bytes SHA8381d4a8de9903002080cb56b25b77ee3da6a31089a0fd0159bc961157a7c47e.
- T43_HINGE_COMPLEXITY_COUNTS.json791bytes SHA4261282ae08bd2e51d1c62133e76d40e9bc94ac0d947ed07bde2908b1233d642.
Unchanged outputs:
- T43_FULL_HINGE_ROOT_TURNOVER.json28568bytes SHAfd97dee5919f820b239604377b30cfa07d0f32fe7223cab4b547fde1023ab4f1.
- T43_TWO_PLANES_ROOT_PROTECTION.json127762bytes SHA7c2e2081ce28d641c2289eb46ddd56de4d326a1eb1e46e9b3ce1efa2a221ce95.
Expected markers: EXACT_HINGE_PLANE_ATLAS_PASS with critical_eligible_planes1231; EXACT_FULL_HINGE_COMPLEXITY_PASS27 70 408; EXACT_FULL_HINGE_TURNOVER_PASS[49,136,89]272[2,2,2][0,0,0][0,0,0],U[41,46],S[23,73]; EXACT_ROOT_PROTECTION_PASS[[True,True],[False,False]].
The corrected atlas is not an equilibrium-family exclusion, and neither the new boundary cases nor the retained222 body establishes own110. Canonical own110 remainsC622.

```diff
--- T43_hinge_atlas_and_turnover_recovery.py
+++ T43_hinge_atlas_and_turnover_recovery.py
@@ -264,6 +264,11 @@
  return [f for f,(ids,m,h) in enumerate(faces) if min(zz[i] for i in ids)<0<max(zz[i] for i in ids)]
 def tangent_rays(n,fs):
  ns=[faces[f][1] for f in fs];rays=set()
+ if not ns:
+  # The entire tangent plane is feasible; four generators, not extreme rays.
+  k=min(range(3),key=lambda j:abs(n[j]));e=tuple(int(j==k) for j in range(3))
+  u=primitive(cross(n,e));w=primitive(cross(n,u))
+  return sorted([u,mul(u,-1),w,mul(w,-1)])
  for m in ns:
   r=cross(n,m)
   if not any(r):continue
```
