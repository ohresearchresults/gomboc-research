# material-d747c6c7136b

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J89 — independent supporting normals and finite own-mass restoration

## Status and acceptance boundary
No new own110 was obtained. The target remains a homogeneous convex 3D polyhedron at its own uniform-volume centroid, strict (S,U,H)=(1,1,0), no additional weak equilibria and E<=249. The accepted own110 C622 is unchanged and is outside the target. All new constructions below are nonwinners.

The coordinator actually computed and exactly classified the new rational H-bodies using the complete inherited standard-library H auditor. Exhaustive independent plane triples, all halfspace inequalities, boundedness certificates, maximal facet cycles, oriented edge incidences, Euler characteristic, positive-tetrahedron volume/first moments, full strict/weak S/U/H and all positive primal bars were checked. This is coordinator-executed work with the author's existing auditor, not a second independent physics verifier. Q=[] is deduced from the exact sole strict polar root and absence of weak polar roots; a separate Q-filtration was not recomputed.

## Source continuity
The full shared notebook was read through EOF119503 at SHA19beeb908c23884fb8afd63f41ebc066ef694471fa66d7b64dc8712a004d93c3. The full finite-chart branch [internal-source-reference] was read through EOF10920 at SHAaf230702dd08275dd641985ae23014af9ae0d4a7453e88b3705b72d4ef950dc7. That branch is the relevant parent direction; its memory currently contains the distinct J88 vertex-family work, not J88H or J89.

The last archived coordinator output [internal-source-reference] was read completely:21577 characters,25828 bytes,SHA8627e922dab959ff1160d975e4b88938098af2319c3231c6e2709be4139644af. It contains the literal self-contained C474 input and exact auditor. Its J88H progression is not an alias of J88_FULL_B/C_G8 (C264).

J88H author-reported chronology: detached J85 own121 -> contact/cofacial C254 with83 facets -> independent-normal C486 own121,P.43446772759119673 -> J88_PROJECTED_C474_G14,V158/E237/F81,own121/weak000,P.4232689411630256. The last actual exact input is5483 bytes/SHA93b20d84d6167fff91687276bbe348f4e91aeb16b037ca72effececcc5674335. Its source was used as a concrete computational input without routinely replaying every earlier author endpoint.

Needed original numerical sources were recovered from visible Library files, not invented paths. J88H_CONTINUATION_SOURCE.md126935 bytes/SHAa08b93e8e8ab76bb6a1b160271b1142f374167eb8e9127b7a4ac7378e92fb1de yielded19 literal units with matching unit bytes/hashes. J88H_EXACT_RECOVERY.py.txt20895 bytes/SHAb3b54c205bee2ae108cca13819a85579cb92a215b4c844dbc27011471e35fe81 was also recovered. All code units actually reused in the new calculation were read completely. This does not imply reading all old unrelated archive data.

## Exact new constructions
All H rows define inequalities n.x<=h with positive h; row scaling does not change the geometry. Decimal conversion for numerical optimization is nomination only. Exact freezes round each literal decimal coefficient ties-to-even on the named grid, then reduce each integer row by its gcd.

| Body | V/E/F; C | Exact strict; weak | Positive P, Q |
|---|---|---|---|
| J89_PROJECTED_C468_G14 |156/234/80;468|121;000|.4129366845737945;Q=[]|
| J89_PROJECTED_C456_G14 |152/228/78;456|121;000|.3732871484677113;Q=[]|
| J89_NORMAL_C444_G10 |148/222/76;444|121;000|.3644890808206012;Q=[]|
| J89_NORMAL_C444_G12 |148/222/76;444|121;000|.3644890807833567;Q=[]|
| J89_NORMAL_C444_G14 |148/222/76;444|121;000|.36448908078350917;Q=[]|
| J89_NORMAL_C444_G8 |148/222/76;444|(9,3,10);000|.36448908567086036 and1.0946206353031966e-14;Q not computed|
| J89_TREE_C426_G12 |142/213/73;426|(1,28,27);000|27 positive P, largest.3533817452442938;Q=[]|

The 13.88711871485624% reduction in the sole P from the inherited C474 to the G10 C444 occurs while retaining exact own121/weak000. It is NOT cancellation, a proof that P can reach zero, or a new canonical own110 record. G10/G12/G14 are distinct rational bodies. G10 has a26457-bit common centroid denominator, versus32448 for G12 and38347 for G14. G8 has21067 bits but fails the desired one-sided class; its tiny additional P is real.

The tree endpoint has a smaller maximum bar but26 extra U relative to the own121 input; its next largest bars are.0015809370032500683 and.0008462144475220963. It is a preserved fragmentation control, not a better own121 body. No positive P was suppressed by a cutoff in exact certification.

## Minimal76-plane representation of the simpler exact C444
J89_C444_G10_MINIMAL76 is exactly the SAME geometric body as J89_NORMAL_C444_G10. Removed original plane indices are[10,33,35,37,42,58,79]. Exhaustive reconstruction after removal gave identical homogeneous vertices, exact volume and exact centroid. Its maximal-facet input has76 rows, all active; this is representation simplification, not a geometry mutation or an extra progress claim.

Exact input4065 bytes/SHA6c615d3a9729fdcf5986913ee6d9feace2610ffb491207c092a7ce85da1d20d3. Canonical full report122649 bytes/SHA345c782c9ef824eb41d182fcfd919e5079a1763dc0a41af3eb9234760d4a2806. In this exact sorted-vertex/retained-plane ordering:S=[54],U=[4,132],H=[[90,97]]. U incidence triples are[14,23,57] and[43,56,67]. Do not substitute numerical Qhull indices or the original83-plane labels.

A bounded full-dimensional convex3-polytope with F facets satisfies3V<=2E and V-E+F=2, hence E<=3F-6. Thus ANY bounded3D geometry represented by these76 independently movable planes has E<=222, and at most nine additional supporting planes allow F<=85 and E<=249. This is a sufficient complexity mechanism, not a class certificate. Keep boundedness/full dimensionality and actual active-plane counts explicit.

## The substantive method correction
The prior polar repair used scale=10 times the largest separate witness deficit divided by that row's L1 Jacobian norm, then bounded every normalized displacement by1. The maximum of the separate deficit/row-norm ratios is only a LOWER bound on the necessary joint correction. Multiplication by10 does not supply a guaranteed upper bound. Using it as a cap can make a feasible coupled linear repair appear infeasible. For example, d1>=r and -d1+epsilon*d2>=r require d2>=2r/epsilon although each separate lower bound is approximately r. This elementary example proves the logical distinction; it is not a family exclusion.

On the actually executed FREE89_A_FINAL checkpoint the old bounded polar repair stopped infeasible at scale1.296480466753783e-6. The unbounded joint Chebyshev LP found minimum correction radius1.577573506321367e-6, and its actual finite step restored S1 with minimum positive nonstable score1.9996942990374578e-7. U19 still remained. These numerical LP figures are not exact rational dual certificates.

The new repair89.py minimizes the full joint infinity correction without imposing that guessed upper bound, then line-searches on ACTUAL own-centroid witness residuals. The same correction was essential in support/centroid projection. On the selected cycle-A3 endpoint the old residual-based radius was2.6668007538891043e-5, while the joint support correction needed7.84439363558082e-5. Finite current-kernel corrections reduced actual centered-cell residual2.6668007538891043e-6 ->1.791526313150299e-9 ->5.739853122015354e-16, yielding the exact C456 freeze. The second minimum radius was3.7877269485628604e-8.

center89.py solves A*delta<=b-A*a with the current centroid Jacobian Jg*delta=0 and a fixed one-offset gauge, minimizes ||delta||infinity, recomputes actual mass after the finite correction, and repeats. Linear programming is normalized in a small variable scale WITHOUT imposing a corresponding displacement cap; this also avoids declaring a1e-9 physical residual solved merely by a1e-9 LP feasibility tolerance. The finite iteration is not an exact mass or equilibrium proof. Rational endpoint census supplies those claims. No global convergence guarantee or proof of feasibility for arbitrary policies is asserted.

## Actually executed continuation, not just a proposal
Initial FreeNormals release from literal C474: normal trust.003,150 iterations,35-second numerical evaluation budget,tau1e-6,weight.001. Its final point was numerically S21/U16 with mainP.4126619238457965, not a valid endpoint. Corrected polar repair eps1e-7, then original support cleanup/centroid projection trust.01,eps1e-9, produced C468.

CycleA:8 completed cycles,180 SLSQP iterations per release,35-second evaluation budget,initial trust.003,polar eps1e-7,cleanup trust.015/eps1e-9. It used the ORIGINAL center_project88;4 cycles were accepted numerically, endingP.38190457111430676. The previously failed cycle3 was separately repaired using corrected center89, producing C456/P.3732871484677113.

CycleB:12 completed cycles from the C456 floating checkpoint,initial trust.006,180 SLSQP iterations, same budgets and polar tolerance, but corrected center89.4 cycles were accepted, with mainP.36997566529632986,.36629089537857273,.36623513419228415,.36448908078351117. The last accepted checkpoint, not an unchecked final optimizer state, produced all C444 freezes. Trust multiplied1.3 after acceptance (cap.025),.55 after rejected projected candidates (floor.0001),.6 after restoration failure. Each finite candidate rebuilt the hull and actual own centroid. Complete sources, exact inputs, all nondefault parameters and outcome summaries are preserved in the readable numerical archive.

The separate whole-root tree objective used an acyclic radial envelope on actual own-centred primal vertices and penalized every selected negative tree chord, not only the undesired root. It ran250 iterations,trust.006,40-second budget from the last C444 floating checkpoint; polar repair restored S1 but two-root support-cell cleanup failed. Exact G12 frozen post-polar-repair geometry is the C426/(1,28,27) control above. This failure is scoped to the executed policy/path, not all tree policies or H-normal changes.

## Angular-cone alternative and its limit
For a simple H vertex x=N_T^-1*1, p=x-g, r=column_l(N_T^-1), alpha=N_T^-T*p, its inward-edge angular witness is -alpha_l/(||r||||p||). It is independent of the corresponding edge's length, unlike a raw short-chord score. Under changing normals:
dalpha_l=-r^T*dg-sum_k[(r^T*column_k(invN))*x+alpha_k*r]^T*dn_Tk.
The derivatives of ||p|| and ||r|| complete the normalized derivative. The full own-centroid shape Jacobian was included.

A regular30-normal test with seed890027 and matched active-triple labels gave maximum central-difference errors2.2500061191976783e-7,1.469619093086294e-9,1.4521859803551251e-7 at steps1e-5,1e-6,1e-7. The earlier raw-index --check was invalid because Qhull vertex ordering changes. The corrected diagnostic is preserved separately; numerical difference tests are not proofs of the derivative formula.

A60-step cone-guard LP run reduced the main floating P only to.42309220218534316 and drove nonstable floating scores to zero. Those endpoints are NOT promoted even to exact own121; sign-count instability after recentering was observed. This is a failed local numerical path, not an exclusion of the cone formulation.

## Remaining geometric obstacle and next question
The H-normal family has NOT inherited the low-stable-carrier separation of J85's separate C276 construction. At inherited C474, three stable-face vertices lie in the unwanted high component above the main death; the whole stable polygon is not below that death. The same holds at C468. Those diagnostics were numerical and are not exact whole-basin exclusion theorems. Do not merge this family with Quiet Willow49's low-S source.

The new C444 has stronger demonstrated class-preserving progress than the old local vertex charts, and a76-plane exact input permits nine additional planes under the target bound. The next substantive problem is removal of the entire remaining maximum-saddle basin while retaining/restoring S1, through continued independent-normal changes, changed policies, finite extra support planes or controlled high-component surgery. More reduction of the largest bar alone is not enough. A selected policy can be changed; its linear infeasibility does not exclude the physical family. The minimal pack's continue89.py is a PROPOSED entrypoint with explicit defaults, not an already executed extra batch.

## Reconstruction and preservation
J89_C444_SELF_CONTAINED.py is12631 bytes/SHAe013ad40bbb5f769ab766f92051d0c94e1930ec9eb3f038ae13ffe0fca2c9c8d. It contains all76 literal integer rows and the complete exact auditor; no parent sandbox, numerical optimizer or FULL76 is needed. Run python J89_C444_SELF_CONTAINED.py under Python3.13.5. A clean source-only execution reproduced both exact input/report hashes and terminal marker J89_C444_MINIMAL76_EXACT_OWN121_NOT_110_PASS. This closes local source completeness, not an independent verifier claim.

J89_EXACT_NONWINNERS_AND_AUDITOR.md:48436 bytes/SHA2f14279d7eceb09a8f04d2f3973682e1c01bd915b15fad56ea47599de779e320,9 readable units. J89_NUMERICAL_CONTINUATION_SOURCE.md:371418 bytes/SHA1b0ec68e4301e809a9926167ac807906e5158fc1cd1ba4adaf3606b613acd7c3,30 readable units including full numerical reports. That archive is for preservation, not a requirement to overload a successor.

J89_MINIMAL_CONTINUATION_PACK.md:52293 bytes/SHA0e782a6e4b40d05b97621793924c4762b6bcb1fe8cc23a37a2f82ed0158d5503,13 complete units, suffices for direct continuation from the literal minimal76 input. Extract with the unchanged J88H_EXTRACT.py1066 bytes/SHAb7626d1ef1a032105a7ef2b75f480dd97fd8c0ece7ba0a203ed22e3f065d419f. The manifest supplies every canonical report hash; canonicalization removes only the variable seconds field.

No research_store_material/update_brief/update_branch/dispatch actions existed in this chat's actual discovered Pro Research catalog. No mutation or dispatch was claimed. Subsequently research_wait after event1493 returned 'has no active coordinator capability'. That is the actual current access boundary; it is not permission to finish the scientific run. Latest successful state was revision1567/event1493, research mode,dispatchAllowed=true,drainActive=false. Later state/results are unavailable. The full shared notebook and branch still need this J89 addition, plus reconciliation of J88H from its archived output.

All new files are supplementary local artifacts, ephemeral/not yet persisted via a successful material-store receipt. The self-contained recovery is complete, but hashes/Library visibility alone do not promote a canonical record. The final handoff includes literal geometry and an exact reconstruction patch against the already immutable J88H auditor so the runtime can archive the new object independently of these sandbox files; the next coordinator must confirm that archival/material preservation before a computational dispatch. No completion ticket was requested.
