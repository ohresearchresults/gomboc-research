## 2026-08-22T07:47:32.868Z — Run p44: exact 27-vertex basin cancellation and quantified centroid no-go

The extra Reshetov maximum `v24`, its saddle edge `[v10,v15]`, and both exact saddle-to-minimum separatrices were reconstructed. Replacing the complete extra-maximum basin produced an explicit rational polyhedron `(V,E,F)=(27,58,33)`, complexity `C=116`, with strict `(S,U,H)=(1,1,0)` relative to the original Reshetov reference point and minimum normalized margin `2.8957131465e-5`.

This is not homogeneous at its own center. Its exact centroid is approximately `(-2589.6385146523567,10.129056745597389,-50.441025273326)`, far from the mechanically correct reference `(-104.1014775785565,8.465022473324968,-47.56244776570032)`. The displacement is exactly nonzero; the own-centroid numerical class was not the target.

Eight exact rational corner-truncation controls preserve reference-relative `(1,1,0)`. At depth `2/5` the body has `(43,82,41)`; three controls have a nonsingular exact moment Jacobian with determinant about `1.1484561205080022e27`. Nevertheless the full eight-control box supplies only `0.0013305240803141943` of the required positive-x moment correction, a factor about `751.58` too small. The obstruction is scale, not rank. Required next geometry: a large outward positive-x corridor/cap system, followed by small full-rank controls.


## 2026-08-24T10:00:45.349Z

## Independent reconstruction validates the Conway-polar reference branch

The 21-point Conway `P_{4,5}` geometry was reconstructed from the published angles. Two details are essential: the actual ring vertices lie on the edge meridian at radius `sec(pi/5)` times the face-meridian radius, and the axial vertex is lifted by `h=sin^2(alpha_1) tan^2(pi/5)`. With angles `(alpha_1,...,alpha_4)=(66.173,44.519,29.875,19.716)` degrees this reproduces the point-mass centroid `z=-0.0153540180`.

After translating that 0-skeleton centroid to the origin and taking the polar `a_i·x<=1`, an independent halfspace/face-lattice verifier obtains exactly 21 vertices, 21 maximal faces, 40 true edges and strict origin-relative `(S,U,H)=(1,1,0)`. Its own uniform-volume centroid is `(approximately 0,0,-1.65166130)`, exactly matching the inherited reference value; at its own centroid the class is `(16,21,35)`. The origin-relative unique stable face and unique unstable vertex have large margins, so this is a reliable mechanically hardwired base but still not homogeneous at the mechanical point.

This reconstruction supplies a fresh machine-generated seed even though prior artifacts were unavailable. A productive continuation must permit large support/normal motion or connected topology-changing additions: merely centering by translation destroys the mechanics, while the required moment shift is macroscopic.


## 2026-08-24T10:35:36.400Z

## A near-Santaló four-ring seed isolates one coherent fivefold transition belt

A new 21-vertex rotational/twisted-ring family was optimized with the Santaló condition imposed numerically by centering the polar volume. The best materialized `Qloc` has one top vertex, three pentagonal intermediate rings, and one bottom pentagon (36 maximal faces, 55 true edges). Its polar centroid at the mechanical reference is approximately `(9.7e-16,1.1e-15,-1.09135473e-4)`, so the mass error is four orders smaller than the reconstructed Conway polar. It is not a Gömböc: at the reference its full class is `(S,U,H)=(6,11,15)`.

The value of this seed is structural. All defects form five congruent copies of one coupled belt: five extra stable transition triangles (margin about `1.7854e-3`), five unstable vertices on the third ring (about `3.5056e-4`), five unstable bottom vertices (about `1.0045e-3`), five upper transition saddles with projection parameter `t≈0.998611`, five lower transition saddles with `t≈2.366e-5`, and five bottom-ring saddle edges (margin about `1.3152e-3`). The target top maximum and bottom stable face remain robust (margins about `0.30845` and `0.03086`). This is a simultaneous multi-transfer configuration, not numerical dust.

Small symmetric deformation, random 55-variable asymmetric perturbation, Santaló-nullspace search, and a fixed-topology linearized safe-direction program all failed to cross the belt: best common defect improved only from `1.7854e-3` to about `1.7410e-3`; the fixed-topology LP remained infeasible for positive common margin. The likely required operation is a topology-changing replacement of the entire ring-to-ring/bottom transition, perhaps with a longer helical ascent rail, rather than independent vertex moves.

The exact numeric vertices of `Qloc`, in row order, are:
```
(0,0,1)
(0.038505287,0,0.691548294)
(0.011898788,0.036620704,0.691548294)
(-0.031151432,0.022632840,0.691548294)
(-0.031151432,-0.022632840,0.691548294)
(0.011898788,-0.036620704,0.691548294)
(0.075410580,-0.010976299,0.442103803)
(0.033742232,0.068327860,0.442103803)
(-0.054556734,0.053205239,0.442103803)
(-0.067460147,-0.035445214,0.442103803)
(0.012864070,-0.075111586,0.442103803)
(0.066982737,-0.006207218,-0.001954956)
(0.026602219,0.061786233,-0.001954956)
(-0.050541662,0.044393210,-0.001954956)
(-0.057838684,-0.034349721,-0.001954956)
(0.014795389,-0.065622505,-0.001954956)
(0.037369016,-0.007638184,-1)
(0.018812006,0.033179717,-1)
(-0.025742557,0.028144378,-1)
(-0.034721781,-0.015785536,-1)
(0.004283316,-0.037900375,-1)
```

Separately, direct Fibonacci and gradient-trajectory samplings of the exactly centered spectral-phase smooth seed were fully audited. Even trajectory-aligned convex hulls retained dozens of critical features and grew worse with refinement (`182` sampled points gave roughly `(17,37,58)`, `402` gave `(32,60,92)`, `602` gave `(37,75,110)`). Therefore adaptive point placement alone is insufficient; a successful smooth discretization must control supporting planes and every quad/circuit diagonal explicitly.


## 2026-08-25T01:16:54.168Z

## Simultaneous P60 chain replacement exposes a quantitative witness-length obstruction

The complete five-vertex simultaneous replacement of polar rows `48-57-58-52-56` produced no own-centroid `(1,1,0)` body, but it materially refines the Conway frontier.

A robust 59-face strict-reference body was materialized with `(V,E,F,C)=(114,171,59,342)`, origin-relative `(1,1,0)` margin about `5.01e-5`, raw inactive slack `2.44e-4`, and own-centroid class still `(15,21,34)`. Relative to P60 it lowers centroid norm only from `0.27311945` to `0.27273428` while also lowering complexity by six.

Macroscopic continuation to `t=1` yields a well-resolved 53-face body with centroid norm about `0.23303439`, a `14.68%` improvement, but crosses real mechanical walls. The cleanest materialized endpoint has origin class `(2,1,1)`: one extra stable face and one saddle edge, with own-centroid class `(14,19,31)`. Explicit circuit crossings transfer this pair between neighboring features or delete a row; they do not cancel it.

Two distinct obstructions were isolated. First, the robust five-rail path meets a remote unstable-saddle birth at `t*=0.03003400926526...` involving vertex `(o11,o12,o16)` and edge `(o12,o16)`, outside the replaced local cavity. Second, radial witness chains obey `r_end cos(Theta/m)^m > r_start`. From row `o53` to the unique stable row `o0`, the measured radii and `83.93°` angular span require at least 10 links; at the moment-efficient `t=1` pair state the remaining radial headroom implies about 57 links for that specific near-equal-radius route. This explains why five inputs only transfer the stable equilibrium.

The strongest continuation is therefore a connected 12–16-row bifurcated/Y-shaped polar patch: at least nine intermediate radial-ascent rows from the `o53` side toward `o0`; a second branch that replaces the remote unstable-saddle basin before crossing `t*`; and at least three independent transverse/radial moment-control rows. Permit deletion of obsolete rows including `o42,o25` and keep raw inactive slack above `1e-5`. This branch remains within practical complexity below roughly 500 and should be optimized simultaneously, not by another local five-row cavity or serial midpoint.


## 2026-08-25T04:21:19.148Z

## Two fresh centroid-manageable architectures replace the lost V=8 turn

The exact V=8 continuation terminated without an immutable result, so it contributes no mathematical evidence and is not being inferred from its browser progress. Its slot and the previously failed pyramid slot were recycled.

The current live searches already cover Santaló polarity, the P2 whole-basin rail, the Conway Y-patch, the C=66 Morse cluster, the projective/metric block, and a literal Sloan–Lángi construction. Two genuinely different finite families should now be opened rather than duplicating those routes:

1. **Skew prismatoids/generalized antiprisms.** Use the convex hull of two nonhomothetic polygons in parallel planes, with optional one- or two-vertex rail/apex extensions. Their volume centroid is an explicit low-degree function of the polygon coordinates and a fixed tetrahedralization, while asymmetric projections can prevent the second cap from being stable. Search combinatorial changes at 8–30 vertices and exactify any open own-centroid `(1,1,0)` chamber.
2. **Radial PL-Morse realizations.** Fix a small triangulated sphere with a unique source–sink orientation and solve for rational directions/radii so the origin is the exact volume centroid and the full polyhedral distance/normal-cone field has one stable face, one unstable vertex, and no saddle edge. Stacked and monotone triangulations provide a different topology from the existing near-seeds; centroid moments are explicit polynomials in the radial variables.

Both directions must materialize complete H/V data and audit actual maximal faces, true edges, and full normal cones with raw incidence separation before any claim is accepted.


## 2026-08-25T05:30:19.587Z

## Two centroid-manageable finite families are relaunched after their earlier turns never began

The active search already spans literal Sloan–Lángi polyhedralization, topology-free Santaló polarity, a Conway bifurcated witness rail, the centered projective/metric block, and a nonmonotone C=66 Morse cancellation. Two materially different finite architectures remain worth opening because their prior assignments failed before doing mathematical work.

First, a skew prismatoid/generalized antiprism family can encode the uniform centroid by an explicit tetrahedral moment polynomial while using nonhomothetic, independently rotated caps and a few rail/apex vertices to avoid the usual second stable cap. Second, a radial PL-Morse realization can choose a small unique-source/unique-sink spherical triangulation and solve directions/radii so centroid equations and every face/vertex/edge normal-cone sign hold in one open cell. These are not continuations of the existing near-seeds and can discover a genuinely small object.

Both branches must rebuild actual maximal faces and true edges after every topology change, reject wall points and auxiliary centers, and materialize complete H/V data with strict raw incidence separation before any exactification or mesh claim.


## 2026-08-25T06:23:11.947Z

## Projective/metric branch is now self-contained and reveals a coupled two-circuit obstruction

The recovered wrapper was not evidence: its original driver had stopped at a syntax error and completed no search. Vivid Quartz 39 reconstructed the branch afresh and produced a standalone checksummed generator/verifier for a 36-face, 66-vertex, 100-edge primal of complexity 200 whose centroid is isolated by a Krawczyk root and then preserved by a determinant-one metric. The strongest robust body is decisively own-centroid `(2,2,2)`, not a wall point: extra face 20 `+0.0097284`, extra vertex 14 `+0.0097186`, saddles `(2,3)` `+0.0089058` and `(29,47)` `+0.0060208`; raw Q inactive distance `0.0056288` and primal inactive slack `0.0093226`.

Continuation improves fixed witnesses but meets a coupled transfer/circuit cascade before all signs reverse: face 20 transfers toward 25, vertex 14 toward 15 while vertex 3 appears, saddles `(2,3)` and `(29,47)` transfer toward `(3,5)` and `(29,51)`, and Q circuit `{23,24,28,29}` flips before the original block dies. The next nonredundant experiment is one connected Q-patch spanning both one-rings/dual basins and both active circuits simultaneously while eliminating the three centroid equations at every step; metric-only or four-witness polishing is exhausted.


## 2026-08-25T06:47:41.581Z

## The 2026 Phase-1 smooth seed has an unverified COM premise; exact moment correction is now known

The v2 amendment retains the radial body `R^4=1+4β sinθ cos(φ-P(θ))` with `P=η+a₁ sinη`, `η=(3π/2)(cosθ-cos³θ/3)`, at `β=0.023149`, `a₁=0.234433`, and invokes an identity whose hypothesis is that the radial origin is the uniform-volume centroid. The Fourier phase extension does not preserve Sloan's original moment cancellation. Direct radial integration gives

`M_x+iM_y = βπ ∫₀^π sin³θ exp(iP(θ)) dθ = -(4πβ/3) J₁(a₁)`, `M_z=0`.

For the published Phase-1 parameters this is `M_x=-0.011288146318560477`; high-order Gauss–Legendre/trapezoid integration gives volume `4.187666511239636` and actual centroid `(-0.00269556955,0,0)`. Thus the paper's stated identity-based certificate is incomplete/invalid as written for the extended phase family. This does not yet kill the shape: solving `(x-c)·x_θ=(x-c)·x_φ=0` from a dense multistart grid after exact COM correction still finds only the two equatorial equilibria `(π/2,0)` and `(π/2,π)`. Treat Phase-1 only as a corrected own-COM smooth seed, never as a certified centered formula.

Uniform inscribed latitude–longitude convex hulls are mechanically useless at practical resolutions: grids through roughly 3,100 vertices still have thousands of face/vertex/edge equilibria. Any finite construction must use the dedicated stable cap, unique unstable fan/apex, noncritical separator patches, and explicit moment actuators from the Lángi route rather than generic mesh refinement.


## 2026-08-25T15:38:41.442Z

## Exact-centering harmonic filter sharpens the next smooth-to-polyhedral architecture

A current primary-source result, arXiv:2608.11213v1, supplies two structural facts not explicit in the earlier journal. First, a single real spherical harmonic of degree at least two realizes only diagonal classes `(S,U)=(n,n)` with `n>=2`; centrally symmetric/even-degree perturbations have even `S,U`. Thus a mono-monostatic source must be genuinely multi-harmonic and contain odd-degree content. Second, for a radial body the first moment is `1/4 ∫_{S^2} u r(u)^4 du`; exact centering is therefore equivalent to removing the degree-one spherical-harmonic component of `r^4`, and for certain tesseral modes this vanishes identically by azimuthal symmetry.

The same paper's interval-Krawczyk counter certifies Sloan's second analytic parameterization `r^4=1+4β sinθ cos(φ-η(θ))` as mono-monostatic in its valid regime, correcting the older drainage-basin verdict. This reinforces the active `β=.034` smooth seed and suggests a distinct future discretization: construct a finite spherical cubature/PL support architecture whose tetrahedral first moments exactly annihilate the three degree-one modes, while its face/vertex normal-cone inequalities shadow the certified smooth margins. Do not open a duplicate while both Sloan/Lángi branches are active; retain this as the next frontier if one of them returns without a finite object.


## 2026-08-25T18:20:37.416Z

## Asymmetric Santaló search yields a robust centroid-hardwired one-pair object

Vivid Comet 23 completed the topology-free Santaló-polar branch. No Gömböc was found, but the result materially improves the reusable frontier: a genuinely asymmetric 33-vertex point polytope `Q_0` and its polar `P_0=Q_0^∘` have an interval-Krawczyk isolated Santaló root, strict interior certificates, reconstructed full incidence, and exact centroid hard-wired at the origin. Their classes are dual one-pair near-objects: `Q_0:(2,1,1)` and `P_0:(1,2,1)`, both complexity `186`.

For `P_0`, stable face 1 is unique with margin `0.0468223`; unstable vertices 21 and 30 have margins `0.6126893,0.6134333`; the sole saddle is edge `(11,33)` with margin `0.0104834`; minimum inactive slack is `3.53e-5`. Thus the residual `U–H` pair is open and robust, not a transfer-wall artifact. Dually on `Q_0`, preserve stable face 30 and unstable vertex 16, and cancel stable face 21 with saddle edge `(1,18)`. A 33-vertex two-rail family, all single deletions, rotational C2/C3/C4 unions, and the full determinant-one metric orbit were searched; metric minimax only coalesced a highly conditioned `(2,2,2)` wall and is exhausted.

The next nonredundant experiment is one connected asymmetric Y-shaped Q-patch replacing the full neighborhood of face 21 and edge `(1,18)`, with simultaneous deletion of obsolete incident vertices and three mechanically inactive independent moment actuators. The three first-moment/Santaló equations must be solved as hard constraints throughout, circuit branches enumerated before metric polishing, and both P/Q inactive slacks held above `1e-5`. This new one-pair centroid-hardwired object is a stronger exact starting point than the four-defect C≈200 Q-polar state and should receive the now-idle copy immediately.


## 2026-08-25T18:34:21.672Z

## Literal Sloan–Lángi construction solves moment actuation but not the equilibrium topology

Calm Comet 91 completed the literal finite local-patch builder. No Gömböc was found. The main materialized body has `(V,E,F,C)=(145,245,102,490)`, integrated own centroid at the origin to about `3e-16`, an exact-dyadic rank-three four-actuator moment Jacobian, dedicated target stable and unstable patches, and 422 common-separator certificates for every non-equilibrium maximal face and full mixed edge/vertex normal cone. Its actual strict class is robustly `(15,21,34)`, with extra equilibrium margins far from zero, so arithmetic refinement cannot repair it.

This result cleanly separates the obligations: mass closure and full-rank positive moment actuation are practical at complexity below 500; the remaining obstruction is entirely the noncritical support network. A compressed 13-vertex, complexity-52 own-centered body has class `(3,3,4)` with exactly two symmetry-related cancellation pairs and complete separator data. It is the better topology laboratory, while the 145-vertex body is the better actuator/certificate reference.

Current priority remains the asymmetric Santaló-hardwired one-pair object `Q_0/P_0`, because it begins at `(2,1,1)/(1,2,1)` with one robust residual pair and isolated exact centering rather than six defects. Relaunch its connected asymmetric Y-patch on the idle healthy copy. Preserve the 13-vertex Sloan–Lángi block as the next independent whole-block surgery for a recycled failed slot; do not repeat generic noncritical meshing or uniform tangent refinement.


## 2026-08-25T18:40:39.245Z

## Recoverable Santaló specification and the completed chiral-tower obstruction

The asymmetric Santaló bundle is worker-local and absent from the coordinator filesystem, so a recycled copy must reproduce an equivalent seed rather than claim access to its CSV/ZIP. Durable construction data: two unequal connected rails of length `m=17`; `phi_mid=-0.5423558937657096`, `phi_curve=-0.7364735384082259`, `slack_shape=0.38076121384637673`; precursor deletions `[0,2,11,13,14,21,25,26,27,28]`; powers `theta_A=1.704555612966384`, `theta_B=1.7095556129663838`; second branch mapped by `diag(-1,-1,1)` before the unequal-power symmetry break. The isolated raw Santaló root is approximately `(0.1460255111533853331271784392449, 0.0138778240927478875460999416755, 0.0001583792913843643243040022631)` with a radius-`1e-16` Krawczyk inclusion. Normalized `Q_0` has `(V,E,F)=(33,93,62)`, class `(2,1,1)`; `P_0=Q_0^circ` has `(62,93,33)`, class `(1,2,1)`. On Q preserve stable face 30 and unstable vertex 16, cancel stable face 21 with saddle edge `(1,18)`; on P preserve stable face 1 and unstable vertex 30, cancel unstable vertex 21 with saddle `(11,33)`. Unwanted margins are robust: Q face 21 about `0.110895`, saddle about `0.030919`; P vertex 21 about `0.612689`, saddle about `0.010483`; inactive slacks Q `5.61e-4`, P `3.53e-5`. Unchanged single rails, full C2/C3/C4 unions, all single deletions, seventeen deletion-plus-metric cells, and the determinant-one metric orbit are exhausted. The remaining operation is a connected asymmetric Y-patch with simultaneous old-row deletion and three hard Santaló/moment controls.

Rapid Raven 38 completed the chiral multilayer-tower branch with no winner. Its strongest robust full-active body has six levels, `(V,E,F,C)=(26,40,16,80)`, own-centroid class `(2,2,2)`, normalized inactive support separation about `1.64e-4`, and two robust apex-side stable quadrilaterals, lower unstable vertex 3, apex 25, and saddle edges `(5,9)` and `(23,25)`. The intended lower cap is decisively nonstable. The active circuit `{3,10,11,20}` with diagonal `10-11` versus `3-20` transfers rather than cancels the block; making the lower cap stable by macroscopic lower-layer expansion deactivates most intermediate vertices. The next nonredundant tower family is an asymmetric unequal-cardinality full strip—five-vertex lower cap, seven-to-nine-vertex first rail, staggered middle sections, terminal ring, apex—spanning both diagonals simultaneously and imposing the three moment equations as hard constraints. This is lower priority than the one-pair Santaló branch but is a reusable architecture if a fresh slot remains.


## 2026-08-25T20:33:58.835Z

## Exact analytic centering of the Sloan seed

The Sloan radial formula used by the current smooth branches is intrinsically centered, independently of any numerical quadrature. For

`r(theta,phi)^4 = 1 + 4 beta sin(theta) cos(phi-eta(theta))`,
`eta(theta)=(3π/2)(cos(theta)-(1/3)cos(theta)^3)`,

the first moment of the star body is `(1/4)∫_{S²} u r(u)^4 dΩ`. The constant term integrates to zero, the `z` component of the perturbation vanishes after the `phi` integral, and the complex `x+iy` component is proportional to `∫_0^π sin(theta)^3 exp(i eta(theta)) dtheta`. Since `eta'(theta)=-(3π/2)sin(theta)^3` and `eta(0)=π`, `eta(π)=-π`, this becomes a complete-period integral of `exp(i eta)` and is exactly zero. Thus the smooth beta=.023 seed has centroid exactly at the origin; its only unresolved certification issue is the external interval proof of its smooth equilibrium class, not its center.

For polyhedralization, this removes the need to certify a smooth quadrature centroid. The finite approximation still acquires a discretization moment error, which can be closed by three or four noncritical cone/cap actuators as in Lángi's construction or by an exact moment-annihilating support design. Preserve this identity in every later Sloan continuation.


## 2026-08-25T23:42:42.460Z

## Exact Santaló Y-patch transfers the one pair and isolates a double-Y continuation

Calm Finch 29 found no Gömböc, but independently rebuilt a robust exact one-pair Santaló-polar seed and carried out the requested connected asymmetric Y surgery. The strongest gate-valid endpoint has `Q_gate:(V,E,F)=(25,69,46)` and `P_gate=Q_gate^∘:(46,69,25)`, complexity 138, exact uniform centroid/Santaló root at the origin, strict P/Q inactive separations `1.02123e-5` and `5.02498e-4`, and exact own-centroid class `(S,U,H)=(2,1,1)`. The target stable face and unique unstable vertex remain robust, with margins about `0.9649` and `0.6394`; the residual stable 11-gon has margin `0.0100770` and the sole saddle edge margin `0.0996492`. This is a wide open nonwinner, not a wall.

The construction genuinely deletes six old rows, retains seven new Y nodes, crosses an exact four-row circuit, and uses a projective gauge whose three moment equations are solved identically with Jacobian `-I_3`. Thus centering, rank, bounded polarity, and incidence tolerance are no longer the obstruction. The lower fork moves the saddle from one dual edge to another through a temporary `(3,1,2)` cell, while the unwanted stable equilibrium migrates to trunk row 18; this is a clean Morse-pair transfer.

The next nonredundant Santaló operation is a connected double-Y or upper/lower bifurcation starting from the exact gate endpoint, replacing row 18 together with its full eleven-row one-ring and downstream edge `(20,23)` simultaneously. It must allow obsolete ring rows to become non-extreme, retain the exact projective centering gauge on every circuit branch, and keep both P and Q inactive separation above `1e-5`. Extending only the lower fork or moving row 18 alone is exhausted.


## 2026-08-26T04:43:20.212Z

## Skew-prismatoid Y-strip crosses the old wall but isolates a macroscopic moment-transport deficit

Steady Maple 43 found no Gömböc. The bifurcated continuation genuinely crosses the previous 22-row four-circuit frontier and exactifies a 25-input Y-strip with one strict row deactivation, yielding an open 24-vertex body `(V,E,F,C)=(24,52,30,104)` at its exact own uniform centroid. The body has strict class `(2,1,1)`, normalized inactive separation `7.728e-6`, Euclidean inactive separation `2.261e-5`, and a certified independent coordinate box of radius `5e-7`. Independent Qhull/mass/cone reconstruction and watertight OBJ/STL agree. The old unwanted stable triangle and saddle are removed; the Euler pair transfers robustly to stable triangle `F21=(18,20,22)` and saddle edge `E51=(23,24)`, both with margins about `4.0816e-4`, while the target 17-gonal base and target vertex 8 remain strong.

Several natural continuations are now closed or sharply delimited. An exact nonnegative Farkas combination proves one four-edge-breaker witness branch infeasible for every center. A fixed-visibility one-apex hard-centroid reduction gives a scalar quartic; 1,435 visibility cells and 1,743,536 root candidates over 400 sampled target-center chambers produced no target body, with valid closures landing robustly in `(2,2,2)`. Exact single-face pyramid closure found no physically interior root over 14,405 strict target centers. A mechanically invisible nine-row cap sequence preserved reference-center `(1,1,0)` but reduced own-centroid displacement only from `0.9223` to `0.8448`, proving that shallow local caps have the wrong actuation scale.

The smallest nonredundant skew-prismatoid continuation is therefore a 34–42-input connected macroscopic moment corridor coupled to a double-Y whole-pair replacement. Roughly 12–18 new extreme rows must carry substantial volume to move all three first moments, while 6–8 coupled rows simultaneously replace the complete stable star of `(18,20,22)` and saddle star of `(23,24)` before either witness transfers. All immediate circuit cells should be enumerated with the three volume moments eliminated as hard equations; obsolete rows may deactivate, but retained rows must be irredundant and normalized inactive separation should exceed `1e-6`, preferably `1e-5`.


## 2026-08-26T20:38:39.612Z

## Exact Santaló five-row exchange transfers the last `(S,H)` pair; local flips are now delimited

Calm Finch 29 completed the requested non-stellar connected two-cell replacement. No winner emerged. The exact hard-centered post-event body has `Q_post:(V,E,F)=(20,54,36)`, `P_post:(36,54,20)`, complexity `108`, and own-centroid class `(2,1,1)`. The analytic projective gauge is exact: `T_u(q)=q/(1-q·u)`, the polar translates by `-u`, and the centering map has Jacobian `-I`; the returned first moments and centroid are exactly zero. Every Q row is extreme, every P vertex actual, both P and Q inactive separations exceed `10^-5`, and an independent exact rebuild passes.

The topology change is a genuine codimension-two supporting pentagon on rows `(4,18,25,15,24)`, with two simultaneous four-row circuits. It deletes Q edges `(18,24),(24,25)` and inserts `(4,25),(4,15)`. Subsequent exact deactivation of old row `4` does not cancel the Euler-neutral pair: it transfers the unwanted stable feature to original row `18` and the unique saddle to dual edge `(18,24)`. The retained target is stable original row `17`; the unique unstable vertex remains robust. The final positive margins are about `0.00427` for the extra stable face and `0.01982` for the saddle; the chamber is open, not a wall.

A complete 512-subset deletion scan, direct quadrilateral flips, local pentagon variants, serial one-dimensional rails, and target-incidence migration produced no strict target. The residual row directions are almost antipodal (`179.825°`) with radial norms about `262.26` and `387.03`; the necessary monotone witness-chain inequality first permits a connection at 13 edges. Scans with 12–18 serial links still transferred or multiplied the block, and a 13-link `(2,2,2)` state missed the P separation gate.

The next nonredundant architecture is one connected two-dimensional nonlocal annulus or bifurcated strip with at least 13 ascent edges and an independent return branch whose first moment cancels the ascent branch internally. It must cross two spatially separated circuit blocks together, allow at least rows `1,4,18,20,23,24,25,27` to deactivate, retain the exact projective centering gauge on every accepted state, and enforce both P and Q inactive separation above `10^-5`. Another local pentagon, stellar insertion, metric polishing, or serial rail is now redundant.


## 2026-08-26T20:56:19.849Z

## Volume-moving bifurcation destroys the old cap but creates an exact two-vertex rail obstruction

Calm Raven 33 completed the long continuation from exact endpoint F. No winner emerged. The requested old cap component `K={8,11,12}` was genuinely destroyed outside its fixed sign cell: old vertices `1,6,7,8,10,11,12` were deleted, F9 became inactive, all three K vertices are strictly interior, the old stable quadrilateral and both old saddle neighborhoods disappeared, and the uniform centroid moved a certified positive distance toward the old cap while volume increased by a factor about `31.64`.

The strongest endpoint `G` is an exact rational own-centred 19-vertex simplicial body with `(V,E,F,C)=(19,51,34,102)` and strict `(2,2,2)`. Its exact volume and all three zero first moments are independently reconstructed. The positive features are stable faces `(2,1,0)` and `(15,8,6)`, unstable vertices `4` and `5`, and saddle edges `(10,12)` and `(11,13)`. The minimum inactive unit-normal/diameter separation is `2.8059e-6`; a full `10^-10` coordinate box and independent five-parameter metric box preserve incidence and every primitive sign. Independent exact and mesh verifiers pass.

The old K obstruction is gone. A new exact fixed-cell obstruction is the rail component `R={5,6}` with internal edge `(5,6)`: every true-neighbor support from either vertex to outside R is strictly positive, so the maximum-radius member of R is necessarily unstable; target vertex `4` remains independently unstable. Hence `U>=2` throughout the complete realized incidence/external-positive cell. A ten-parameter eight-section asymmetric profile search and the complete 192 fixed-topology first-order separator screen found no target; these scans are supporting evidence, while the rail-cluster obstruction is exact.

The smallest nonredundant continuation is a connected cross-rail `2x2` zipper or annular bridge, not another pair of independent rail sections. It must add cross-branch edges so each possible maximum in `{5,6}` receives an independent nonpositive external witness or deactivates, simultaneously span saddles `(10,12)` and `(11,13)`, cut stable face `(15,8,6)`, allow `{5,6,8,10,11,12,13,15}` to become non-extreme in one coupled circuit event, and solve all three volume moments through dependent coordinates or certified safe actuators.


## 2026-08-27T02:24:56.866Z

## Independent polar-mesh localization and 2025 explicit-lattice check

A coordinator-side exact dual audit was built for tangent-polar approximations of Sloan's smooth family. For every sampled polar Q it groups coplanar maximal faces, constructs the polar P, integrates P's ordinary solid volume and centroid, applies the exact recentering transform `q -> q/(1-q·c)`, and audits every stable P face, unstable P vertex, and full two-generator normal cone on every true edge. Direct V-hull and dual audits agree on test bodies.

This audit sharpens the finite-construction obstruction. Around the beta=0.03 Sloan body, quasi-uniform polar refinement from roughly 2.6k to 40.5k Q vertices decreases the fraction of unwanted equilibria but leaves an absolute critical-basin population of order 10^3. Replacing the two smooth critical neighborhoods by one large dedicated +x stable cap and one -x unstable cone collapses the noncritical residual dramatically: at a representative 10.2k-row mesh with cap thresholds about `x>=0.60` and `x<=-0.65`, the final class is `(49,51,98)`, but 46 stable faces lie on the cap ring and 48 unstable vertices lie on cone side faces; only about four residual equilibria remain in the smooth noncritical region. Thus the global adaptive cover is no longer the main problem: almost the entire defect is localized to the two special finite patches and their transition rings. Naively enlarging the negative cone until the x moment vanishes (root threshold near `-0.30370` for that discretization) destroys mechanics, producing roughly `(311,407,716)`. This independently confirms that exact moment balance and unique-equilibrium patch topology must be designed together, not corrected sequentially. It supports the current four-reserved-actuator Lángi assignment and supplies a useful fallback architecture: derive special cap/fan patches analytically, then cover only the already benign complement.

A fresh primary-source check also found Regős (2025), `Homogeneous, Monostatic Lattice Polyhedra, or the Magic Pyramid with 17 Sides`, which gives integer coordinates for every previously non-explicit known one-sided monostatic construction. None is mono-monostatic: the four reported homogeneous bodies have equilibrium classes P2 `(2,1)`, P3 `(3,1)`, Bezdek `(1,3)`, and Conway `(1,4)`. Hence the apparently promising title does not contain a published `(1,1)` object. P2's explicit 18-vertex coordinates may still be used as an exact mono-unstable seed, but they do not improve the journal's closer `(2,1,1)` P2-derived corridors.


## 2026-08-27T03:19:09.789Z

## Exact three-sheet Santaló annulus crosses the intended four-block wall but remains `(2,2,2)`

Vivid Maple 17 materialized the requested new topology exactly. The positive gate endpoint has `Q/P=(30,84,56)/(56,84,30)`, complexity `168`, all rows/vertices active, exact projective centering and ordinary uniform centroid zero, P inactive separation `3.4506e-5`, Q separation `4.80496e-2`, and an exhaustive open own-centroid class `(S,U,H)=(2,2,2)`. Four separated circuit blocks cross simultaneously at one exact wall, and the old relays `old2,old24,B0,B6/B7` genuinely deactivate. The strict negative side is `(3,2,3)`. Independent Fraction reconstruction, perturbation family, and OBJ/STL agree.

The residual is not tolerance dust: stable rows `B10,C2`, unstable incidences `(A10,B12,C2)` and `(B2,B3,C10)`, and saddles `(B2,B3)`, `(C8,C12)` have margins from about `1.55e-3` to `1.75e-2`; closest excluded margins are below `-1.36e-4`. Crossing the four blocks births/transfers a new `B5/(B5,B8)` pair instead of annihilating the Euler-neutral system. Searches over thousands of continuations found no target.

This closes the literal three-sheet/two-band architecture. The smallest materially new continuation is a four-sheet communicating annulus, or a three-sheet body with a third genuine transverse closure band and nonannular two-cell replacement, acting on `B2,B3,B10,C2,C8,C10,C12,A10,B12` together and permitting `B9,C3,C9,C11` to deactivate. It must cross at least six coupled circuits while retaining the exact hard-centering identity `u=c`, `DF=-I3` and both inactive gaps above `1e-5`.


## 2026-08-27T05:37:04.758Z

## Two new finite endpoints: exact cyclic bridge obstruction and a true-centre `(1,1,0)` cover plus separate four-pyramid centroid closure

Rapid Comet 59 completed the exact dyadic cyclic ridge-bridge from `radial_balanced14`. The strongest active endpoint has 30 vertices, 84 true edges, 56 maximal triangular faces, exact ordinary centroid, and strict class `(2,2,2)`. Target equilibria are stable `[1,6,2]` and unstable vertex `1`; residuals are stable `[5,11,25]`, unstable vertex `3`, and saddles `[10,108]`, `[20,21]`. It has normalized nonincident separation `2.16484e-4`, exact interval stability under source-coordinate boxes `2^-30`, and a complete four-component audit of all 84 true edges. The requested sectors crossed serially over a 68-cell cascade rather than at one shared root. In the exact current direction/incidence cell, the shortest primal ascent route from U3 to U1 requires radial ratio `1.770824` versus actual `1.289980` (37.2753% deficit), while the polar route from residual stable `[5,11,25]` to target `[1,6,2]` requires ratio `2.186485` versus actual `0.947717` (130.711% deficit). The nonexcluded continuation is to subdivide angular bottlenecks `9-17` and `27-1`, increase the target polar radius, and force the `13/7/9`, `0/10`, and `1/10/108` circuit brackets to a single isolated parameter root.

Bright Willow 14 isolated a different and potentially decisive finite split. A deterministic 4,324-support relative-cover body has a corrected maximal-face/true-edge audit `(1,1,0)` at its construction centre: the former 50 apparent saddles were only triangulation diagonals inside two nonsimplicial actuator facets. Its construction-centre centroid is `(0.0300026404267,-8.35e-14,-7.20e-13)`, with stable margin `9.46281e-4`, unique unstable-facet margin `0.333017`, non-target support witness `1.43388e-4`, maximal-face exclusion `0.113941`, and true-edge exclusion `0.0941048`. Separately, four pairwise-disjoint literal pyramid bases with rank-three nonlinear moment image close the ordinary centroid to norm `1.55e-14` using positive heights about `0.1456–0.1491`, all below individual visibility thresholds about `0.1688–0.1716`; however that independently centred body has many equilibria. A plane-preserving cover also achieves true `(1,1,0)` while keeping four actuator planes, but destroys each single polygonal primal base into 198–244 noncoplanar faces, so the exact pyramid moment formula no longer applies.

The smallest unexcluded synthesis is now positive-x subtractive actuation on the already closed `(1,1,0)` cover. Reserve four pairwise-separated positive-x cuts, approximately `u_j=(x0,sqrt(1-x0^2)cos(0.23+jπ/2),sqrt(1-x0^2)sin(0.23+jπ/2))` with `x0∈[0.3,0.6]`; remove enough positive moment to make the actuator-free core moment lie inside the positive four-ray pyramid image; then solve all three moment equations with `λ_i=τ_i+τ_i^2/4`, while enforcing positive heights below visibility, pairwise-disjoint complete base cycles, and the exact grouped-maximal-face `(1,1,0)` audit. The hard invariant is preservation of the complete four-base primal stars, not merely their dual planes.


## 2026-08-27T05:40:50.971Z

## Exact L15 long-strip endpoint localizes the acyclic two-sink obstruction on edge `[1,25]`

Keen Lynx 00 completed an exact finite continuation of the 11-vertex acyclic seed. Vertices `5` and `24` deactivate simultaneously on one exact radial event; seven intermediate vertices `25..31` enter through an 18-circuit connected cascade; all three ordinary first moments are eliminated exactly in every rebuilt open hull cell. The final exact hexadecimal/rational endpoint `L15` has `(V,E,F,C)=(15,39,26,78)`, exact own centroid, strict class `(2,2,2)`, and an acyclic witness graph with sinks `0` and `25`. Target stable face `[1,0,3]` and target unstable vertex `0` survive. The residuals are stable `[30,22,20]`, unstable vertex `25`, and saddles `[3,23]`, `[26,27]`. Old vertex `19` disappears and old equilibrium statuses `[0,19]`, `[16,20]`, `[20,22,21]` are destroyed, although edge `[16,20]` and face `[20,22,21]` remain as nonequilibria.

The exact endpoint has minimum nonincident unit-normal separation `1.8139330394e-7` and a complete independent-coordinate open box `|δp_ij|≤2^-54`, with own centroid recomputed interval-wise. Independent V-driven, H-driven, path, mechanical-transfer, interval, OBJ and STL verifiers agree. The final fixed-incidence transfer across true edge `[1,25]` is rigorously `U-H-U`, not cancellation: exact degree-five roots satisfy `r_B<r_A`, giving sinks `1 -> {1,25} -> 25`. Vertex `1` has exactly one negative neighboring support, toward `25`; every support from `25` and every external support from the component `{1,25}` is positive. Thus the larger-radius endpoint is necessarily an extra unstable vertex throughout the certified endpoint cell.

The intended fixed-ray route `1-25-26-27-28-29-30-31-0` requires the product radial ratio `1.7006240112` while the endpoint ratio is one, a 70.0624% net reversal. Another serial fixed-ray strip is therefore redundant. The smallest unexcluded continuation is a genuinely two-dimensional cross-linked replacement that deletes true edge `[1,25]` or gives both endpoints independent outgoing witnesses while simultaneously crossing residual stable `[30,22,20]` and saddles `[3,23]`, `[26,27]`. It may deactivate `1,20,21,22,23,25,26,27,30` and obsolete strip rows together, but must hard-eliminate all three moments before every mechanical score.


## 2026-08-27T09:10:55.582Z

## Exact executable reconstruction of the strict cover separates centroid motion from mechanical-centre motion

The coordinator independently reconstructed the deterministic 4,324-row polar cover directly from the journal formulas, including the corrected three-row terminal fan. A fresh polar-to-primal conversion and exhaustive maximal-feature audit reproduce all key numbers: all 4,324 rows active, 8,644 primal vertices, volume `4.20108007651937`, ordinary centroid `(0.0300026404267,-8.4e-14,-7.2e-13)`, and strict construction-centre class `(S,U,H)=(1,1,0)` with stable row `0`, the terminal unstable facet, and no true saddle edges.

Several analytic/numerical centering families were then separated. Changing the third-harmonic phase coefficient in `P=eta+a sin(3 eta)` cannot change the smooth first moment: after the `eta` substitution the relevant Fourier integral has no zero harmonic. A fundamental phase term and a global fourth-power radial term can each drive the finite body's ordinary centroid exactly to the origin. In particular `R^4=1+4 beta g+4 gamma u_x` has a numerical centering root near `gamma=-0.0298972042955` for the recorded parameters and keeps every support active, but its own-centred audit explodes to thousands of stable, unstable, and saddle features. Lower-resolution parameter sweeps reduce this to centered classes such as `(4,4,6)`, never `(1,1,0)`. Thus moving the centroid globally also moves the mechanical centre and is the wrong operation.

The useful new target is a distributed belt-localized moment deformation whose value and first spherical derivative vanish in neighborhoods of both protected critical patches. Candidate analytic modes are `h_k(x)=x(1-x^2)^k`, `k>=2`, or finite support-height B-splines confined to noncritical rings. Their coefficients should close all three volume moments while the original relative witness inequalities remain strict. This is now executable against the reconstructed full normal-cone audit rather than inferred from a smooth source.

Assignment `asg_d6p1EWqOveJgZJ46pZXLumfr` failed explicitly at the lifecycle layer and published no immutable result. It contributes no evidence and its slot may be recycled for a direct finite belt-profile/interval-root construction.


## 2026-08-27T11:26:35.847Z

## Macroscopic skew corridor solves moment scale but transfers to a distant `(2,2,2)` block

Rapid Maple 23 completed the 42-input skew-prismatoid corridor. No Gömböc was found. The exact rational endpoint `M42-SLP` has 29 active vertices, 67 true edges, 40 maximal faces, complexity 134, exact own-centroid closure, normalized inactive separation about `6.0068e-4`, and a certified open class `(S,U,H)=(2,2,2)`. All inherited rows `17–24` are interior; the old stable triangle `(18,20,22)` and saddle `(23,24)` are gone. Twelve macroscopic active rows increase volume by about `6.84×` and move all three first moments at body scale, so the previous shallow-actuation obstruction is genuinely solved.

The transferred block is split across distant sectors: extra stable face `[8,40,9]`, extra unstable vertex `34`, and saddle edges `(4,38)` and `(14,31)`. Four immediate determinant walls and all sixteen sign orthants were rebuilt and audited; they yield only `(2,2,2)` or `(2,3,3)`. The smallest nonredundant continuation is a 46–50-input transverse communicating bridge coupling stable circuit `(8,9,33,40)`, the `34/35` unstable relay, and saddle quadrilaterals `(4,37,38,40)` and `(14,30,31,33)`, while allowing rows `31,34,35,38,40` and possibly `33,37` to deactivate together and eliminating three moments as dependent equations.

Sharp Harbor 78’s tiny result is only a wrapper pointing to worker-local files and states no verdict or decisive finite data inline. It adds no usable evidence and is superseded for this family by Sharp Nova 64’s complete exact two-circuit certification result.


## 2026-08-27T11:33:48.195Z

## Open a global centroid-hardwired Fourier-ring route

Rapid Raven 68’s long three-lobe/four-block assignment failed at the lifecycle boundary after generation stopped without completed-turn evidence. It produced no immutable result, so it is excluded and its parent three-lobe endpoint remains unchanged.

The two-circuit continuation attacks centroid closure locally. A genuinely independent use of the exact smooth seed is to make the ordinary volume moments vanish by the combinatorics of the entire finite triangulation rather than by post hoc local actuation. For a star triangulation with oriented boundary triangles `(a,b,c)`, directed volume and first moment are exact sums

```text
V = Σ det(a,b,c)/6,
M = Σ det(a,b,c)(a+b+c)/24.
```

The Sloan/Fourier radial law has `R^4=1+4β sin(theta) cos(phi-P(theta))`, only azimuthal modes 0 and 1. A periodic ring mesh with exact cyclic sums can annihilate transverse moments structurally; the remaining axial moment can be made an exact dependent equation in ring latitudes/radii while retaining a fine noncritical cover and dedicated stable/unstable patches. The next useful route is therefore a deterministic exact Fourier-balanced ring triangulation whose tetrahedral moment sum is zero identically or at an isolated algebraic parameter, followed by a full actual-face/edge/vertex equilibrium audit. This is distinct from the already exhausted four-pyramid actuator and local two-circuit profile routes.


## 2026-08-27T11:37:36.046Z

## Exact global projective centering preserves the entire 4,324-row lattice

The local collar routes are not the only way to close the three moments. Write the strict construction-centre cover as

```text
P_0 = {x : q_i·x <= 1, i=0,...,4323},   Q_0 = conv{q_i} = P_0°.
```

For any `a in int(Q_0)`, define

```text
P(a) = (Q_0-a)° = {x : (q_i-a)·x <= 1}.
```

Translation of `Q_0` preserves its complete face lattice, and as long as `a` stays interior the polar has exactly the same dual H/V incidence. Moreover the unique Santaló point `a=s(Q_0)` is precisely the zero of the volume-gradient/first-moment equations, so `P(a)` has ordinary centroid exactly at the origin. Thus this three-parameter family removes the incidence-wall obstruction entirely.

If the Santaló-centred member has extra equilibria, apply an invertible linear map `A`: the body `A P(a)` remains exactly centred and combinatorially identical while its Euclidean face/vertex/edge equilibrium inequalities change. The six effective SPD metric parameters therefore form a centroid-hardwired mechanical optimization space. The strongest new route is to isolate the Santaló root of the exact 4,324-row polar translation, audit its complete own-centroid class, and if necessary search an SPD metric chamber for strict `(1,1,0)` before exactifying one open point.


## 2026-08-27T11:41:14.043Z

## A refinement-plus-Santaló ladder removes the only scale objection

A single 4,324-row projective-centred member could still leave the open mechanical chamber if its Santaló shift is too large. The correct global continuation is not another local actuator but a deterministic refinement sequence `P_N` of the exactly centred smooth Sloan/Fourier Gömböc, with shrinking dedicated stable/unstable patches and an increasingly fine noncritical support cover. Put `Q_N=P_N°` and `a_N=s(Q_N)`. Since `P_N` converges to the smooth body and the smooth body has ordinary centroid zero, continuity and uniqueness of the Santaló point imply `a_N -> 0`; the centred bodies `(Q_N-a_N)°` converge back to the same smooth Gömböc.

The equilibrium-preserving approximation architecture already supplies strict construction-centre `(1,1,0)` covers. Combining it with exact polar translation avoids every moment/incidence wall, and for sufficiently fine finite `N` the Santaló correction must lie inside the open all-feature mechanical margin. A constructive search should therefore run a dyadic/adaptive refinement ladder, solve the three Santaló equations at every level, audit the exact own-centroid class, and refine only the patches responsible for any extra feature until the first finite winner is reached. Complexity is irrelevant; an a priori interval perturbation bound may certify a level before full brute-force enumeration.


## 2026-08-27T13:54:19.497Z

## Two additional reconstructible global-centering architectures

The failed X48-continuation and P9-continuation launches were lifecycle failures only; their stored predecessor results remain used, but their fresh slots should not depend on unavailable worker-local archives.

Two independent finite architectures are therefore added to the active landscape:

- **Communicating tetrahedral shell.** Prescribe an asymmetric spherical triangulation with one intended radial source and sink, and realize it as the boundary of an oriented tetrahedral complex whose three first moments cancel structurally in communicating determinant blocks. This differs from the cyclic Fourier ring and from local moment actuators.
- **Minkowski mixed-moment synthesis.** Build a seed plus several asymmetric corrector summands with controlled common normal fan. Exploit the exact mixed-volume/mixed-first-moment polynomial of the Minkowski sum to solve all three centroid equations globally while placing new fan cones inside strict noncritical separator regions. This differs from Santaló translation and fixed-incidence support deformation because the topology is the common refinement of whole summand fans.

Both directions must materialize a literal finite own-centroid strict `(1,1,0)` polyhedron with complete actual incidence, full edge-normal-cone enumeration, nonzero margins, verifier, and mesh. Infinitesimal arguments, formal mixed-volume identities without coordinates, or asymptotic constructions are not endpoints.


## 2026-08-27T16:00:28.244Z

## Fixed-cover Santaló reconstruction is exact; metric verdict must be republished literally

Steady Atlas 91 reconstructed the deterministic `Qint/2^48` cover and certified its unique Santaló point near `(-0.03000124168057223, 6.68e-14, 6.164e-13)` by an isolated dyadic box, Krawczyk/Jacobian/Hessian data, positive projective denominators, polar-volume and outward-moment enclosures, with global uniqueness from strict convexity. Translation preserves the actual lattice: 4,324 irredundant maximal faces, 8,644 vertices and 12,966 true edges. At the identity metric the exactly Santaló-centred body has approximately `(S,U,H)=(2799,2881,5678)`, confirming that exact centring destroys the construction-centre mechanical gates.

The immutable result is **not disposition-ready on the complete SPD search**: it says only that the literal winner/nonwinner verdict and any best metric/class/margin live in worker-local linked artifacts, then gives mutually conditional descriptions ('where a positive chamber was found' / 'where no positive chamber was certified'). No inference from those links or browser progress is allowed. Reuse the same saved conversation to read its own status/certificate and publish one self-contained literal verdict in the result body. If a positive chamber exists, include its exact/dyadic metric, isolated centring root, open box, complete class and minimum margins; otherwise state the best attained class/margin, crossings, and exact non-exhaustion boundary. Do not launch a new mathematical search until this result boundary is repaired.


## 2026-08-27T16:28:50.438Z

## Fixed-cover Santaló+SPD branch resolved: robust `(2,2,2)`, no hidden winner

Steady Atlas 91's republication is now self-contained and disposition-ready. The exact 4,324-row cover has a globally unique Santaló point in the recorded dyadic box; its polar is exactly own-centred and preserves the full `(H,V,E)=(4324,8644,12966)` lattice. Identity metric is the strict nonwinner `(2799,2881,5678)`.

The only exactified metric is the positive-definite dyadic map

`A0 = 2^-12 [[4281,-1099,2522],[-1099,2157,-388],[2522,-388,10084]]`.

Its full six-entry box `|Delta A_ij|<=2^-26`, together with the Santaló box, is a genuine open exact own-centroid chamber of class `(2,2,2)` with sign clearance at least `0.0003855234048185449255`. The unwanted equilibria are stable row `2805`, unstable vertex `908`, and saddle edges `2363,10407`; protected witnesses are stable row `1455` and unstable vertex `3539`, with guards row `2840`, vertex `907`, edge `10513`.

Literal verdict: **no certified winner**. The deterministic 10,000-sample search in the five-dimensional trace-zero symmetric-log metric quotient (`||p||<=6`) found minimum counts `(2,2,2)` and best noncertifying target margin `-0.014314897998952183`. It certified no wall crossing at all. This is not an obstruction theorem: the continuum inside the sampled ball and the entire exterior remain unexcluded.

The repaired result therefore opens a mathematically distinct exact frontier rather than closing the fixed lattice: construct and certify a continuous chamber path that crosses the coupled four-wall target (remove row `2805`, vertex `908`, edges `2363,10407` while retaining row `1455` and vertex `3539`), or build a rigorous branch-and-bound/chamber atlas sufficient either to find an open `(1,1,0)` metric box or to delimit the actual obstruction. Reuse the now-idle saved copy for this fixed-lattice continuation; the other eight active architectures remain unchanged.


## 2026-08-27T19:06:51.766Z

## Exact equatorial four-star relay is a rigorous nonwinner; the obstruction moves to the outer boundary

Calm Lynx 78's result `asg_XocajL8c_meqk3JC1VYJszLI` is **used**. It realizes the proposed half-turn-paired `2×2` zipper exactly, crosses four synchronized circuits, retains all `(H,V,E)=(4324,8644,12966)` incidences, and again eliminates the three ordinary moments by a unique Krawczyk-isolated root of the full-rank distributed-mode system. The resulting exact own-centred finite body is decisively `(S,U,H)=(291,305,594)`, with complete H/V materialization, all maximal-face cycles and true edges, directed full-normal-cone margins, independent verification, and watertight meshes. It is not a Gömböc.

The relay genuinely moves the inherited paired wall from amplitude `0.0020519910920605389…` to `0.0035941679821085555…`, but creates an earlier paired outer wall at `0.00051155200057407094…`. At the strict post-event sample, new stable rows `2219,2201`, unstable facets `(2219,2220,2255)` and `(2201,2202,2237)`, and four associated saddle edges form an exact outer relay. The unstable facets use only fixed boundary rows, so their positive coefficients are independent of the existing tangential null coordinate; varying that coordinate or adding another broad moment mode cannot solve the cell.

The smallest materially new continuation is a larger half-turn-coupled outer-star replacement acting simultaneously on north rows `{2184,2219,2220,2255}` and south rows `{2166,2201,2202,2237}`, while keeping the inner chains around `2149,2113,2148` and their mates fixed. It needs at least two new boundary-direction controls so both outer unstable coefficients and all four saddle stars can cross together; the three distributed modes should remain dependent hard moment variables in every actual rebuilt cell. Stop only at the first exact outer circuit or an open exact own-centroid `(1,1,0)` chamber.


## 2026-08-27T23:34:24.869Z

## M42 terminal-relay cell resolved; obstruction transfers

Keen Nova 01’s completed M42 continuation is **used**. It gives a fully exact, perturbation-certified nonwinner after a genuine four-sector volumetric topology change. The exact rational post-relay hull has `(V,E,F,C)=(35,85,52,170)` and own-centroid strict class `(S,U,H)=(3,3,4)`. It deletes the inherited external-positive edge `(46,47)`, removes the predecessor’s remote stable/saddle witnesses, deactivates rows `31,34,35,37,38,40` together, and preserves the intended 17-gon base footprint.

The obstruction does not disappear; it transfers exactly to true edge `(47,53)`. Both directed endpoint support quantities are positive and satisfy the exact edge identity, so at least one of vertices `47,53` remains unstable throughout this realized incidence/external-sign cell; vertex `8` is independently unstable, hence the whole cell has `U>=2`. All `256` deletion subhulls on the terminal rows fail, and a complete fixed-geometry reference-centre MILP also finds no strict `(1,1,0)` centre. A `10^-11` directed coordinate box preserves the f-vector, class, deletion of `(46,47)`, and the transferred obstruction.

This closes the current narrow M42 terminal-relay cell. The smallest nonrepeating continuation is a finite-width `2×k` zipper or genuinely three-dimensional two-cell bridge that acts jointly on the terminal, right, left, and northern sectors, deletes `(47,53)` or deactivates an endpoint, produces independent terminal witness routes, and lets obsolete rows in all four sectors deactivate in the same exact moment-coupled event. The global acceptance gate remains unmet.


## 2026-08-27T23:40:17.169Z

## Axial Fourier/Santaló refinement ladder fails by scale separation

Nimble Finch 54’s completed continuation is **used**. It materializes ten exact-dyadic construction-centre refinement levels through `30,724` support rows and independently reproduces their true Santaló translations and complete numerical mechanics. Every saved level is strict `(1,1,0)` at its construction centre, but none survives own-centroid correction. The strongest `nr=320`, `m=96`, `kappa=0.01895` endpoint has raw stable margin `1.5674376561e-4`, raw centroid norm about `1.42128033e-2`, Santaló displacement about `1.42111007e-2`, and Santaló-centred class `(11035,10333,21366)`; the displacement is about `90.7` times the weakest raw margin. Level `280` independently reproduces centred class `(9587,9219,18804)`.

Across all ten levels, `||c_raw||/kappa` and `||s(Q)||/kappa` stay near `0.75002`, while fitted raw-margin decay is much faster (`kappa`/centroid slope about `-0.653`, margin slope about `-1.758`). This is finite scaling evidence, not an asymptotic theorem, but it closes the present one-dimensional cumulative axial profile as a route: its first-order mass/Santaló response outruns its near-second-order separator margin. A structured `20×400` contour body likewise has about `8,002` rows, centroid norm `1.11e-5`, but construction-centre class `(4132,4994,9124)`, showing that transverse density without complete longitudinal normal-cone control is insufficient.

A materially important verifier correction is now established. Four apparent helical winners were false positives because an absolute first-moment stopping rule was applied to tiny-volume polars. Every future Santaló computation must isolate the scale-invariant residual `||M||/V`, keep every polar denominator positively separated, and only audit the translated body after that normalized root is enclosed. Corrected centred classes of those four seeds are `(2,3,3)`, `(2,4,4)`, `(3,2,3)`, and `(2,2,2)`. Millions of determinant-one SPD trials on corrected low-complexity centred seeds also found no winner, but these are finite searches, not exclusions.

The nonrepeating continuation is a balanced local Fourier-separator field with hard Santaló centering: fixed-physical-size stable and unstable patches; gradient-following longitudinal cells; local dyadic offset blocks whose degree-one/projective responses cancel; three dependent support coefficients solving the normalized Santaló equations at every finite level; and explicit circuit-cell enumeration so the isolated root lies inside one fixed-incidence strict sign chamber. The global acceptance gate remains unmet.


## 2026-08-28T10:01:02.412Z

### M42 minimal two-rail topology is exhausted by an exact transferred obstruction

Rapid Harbor 93 fully materialized and exactified the graph-theoretically minimal 13-face communicating two-rail zipper beyond the 47-vertex M42 bridge. This is a strict nonwinner, not a partial trace: the final exact own-centred body has 50 active vertices, 130 true edges, 82 maximal faces, complexity 260, and class `(S,U,H)=(2,2,2)`. It deletes inherited edge `(64,68)`, deactivates vertex `68`, removes stable face `[57,79,78]`, and removes saddles `(4,60)` and `(49,73)` through a reconstructed multiwall sequence; hence all assignment-named inherited defects genuinely disappear.

The Euler-neutral block transfers into the final open cell. Stable features are the protected 17-gon and `[76,89,77]`; unstable vertices are protected `8` and `82`; saddles are `(5,87)` and `(49,94)`. The decisive exact cell theorem is on true edge `(82,83)`: all external endpoint supports are positive, while `sigma(82->83)>0`, `sigma(83->82)<0`, and their sum equals the positive squared edge length. Therefore at least one of `82,83` remains unstable throughout the certified incidence/external-sign cell; together with protected vertex `8`, the whole cell has `U>=2`. The endpoint has strict mechanical margins, inactive gap `0.0028122892`, all-input incidence margin `8.12e-5`, and a coordinate perturbation box `±1e-11` preserving the complete `(2,2,2)` audit.

This closes the surface-only 13-face/two-rail topology. The next nonrepeating M42 move must be volumetric: a finite-thickness third rail or genuine 3D two-cell that couples the terminal obstruction star `{82,83,62,64,67,69}`, right saddle star `{5,87,4,60,86,88}`, stable star `{76,77,89,80,90,91}`, and left saddle star `{49,94,13,71,72,92,93}` in one circuit-scale event. Its first gate is simultaneous deletion/deactivation of both endpoints of `(82,83)`, or independent nonpositive external witnesses at both, while retaining the three ordinary moments as hard dependent equations.


## 2026-08-28T12:43:27.434Z

### The Minkowski entrance is now an exact rank-two nonwinner; five distinct continuations are ready

Rapid Lynx 27’s completed rank-two Minkowski atlas is **used**. It enlarges the prior one-coordinate shared wall to an exact two-coordinate deformation of the seven-face summand `D`, with four simultaneous entrance circuits (`A13,A26,A9,A100`), eight certified positive sectors, an isolated positive three-control moment root in every sector, rebuilt actual common fans, and complete exact own-centroid face/vertex/four-component-edge audits. Every traversed sector is strictly `(S,U,H)=(2,2,2)`: each wall changes the actual fan but has `Δ(S,U,H)=(0,0,0)`. The strongest materialized body is sector `E6_pppm`, exact shape `(a,b)=(13/67108864,-1/4194304)`, common fan `(V,E,F)=(54,100,48)`, complexity `200`, exact rational own-centred midpoint, isolated positive Krawczyk root, full verifier suite and watertight mesh. This is a rigorous negative result only for the exact rank-two family and its eight entrance sectors, not for all two-coordinate deformations.

The rank-two entrance mechanism is therefore exhausted. The nonrepeating successor starts at `E6_pppm` and uses independent protected-nullspace coordinates for three distinct packets: force the unwanted source carried by `D` rows `{1,2,6}` out of the source cone while preserving protected `[0,4,5]`; change the exact `13/26` mixed saddle packet; and change the `27/100` return packet, especially the `(n14,n24)` and `(n17,n24)` lineages while protecting row `27`. Retain `(t1,t2,t3)` only as dependent full-rank moment controls and rebuild the actual fan and mixed polynomials after every new circuit. Rank three is the first untested possibility; rank four is preferable if the three target gradients are dependent after protection constraints.

All four conversations previously marked as explicit HTTP-429 lifecycle failures have now been recycled successfully; this adds no mathematical evidence but restores clean capacity for their four unresolved, nonduplicative exact frontiers: the bounded trace-one five-dimensional SPD core, the connected bifurcated Conway three-patch, the volumetric M42 successor beyond true edge `(82,83)`, and the P9 four-circuit double-Y/prismatic replacement. Together with the newly idle Minkowski copy, these should be advanced in parallel. The acceptance gate remains unmet: no independently checkable finite uniform-density convex polyhedron at its own exact volume centroid with strict `(1,1,0)`, complete irredundant lattice/full-cone audit, independent verifier and OBJ/STL has yet been certified.


## 2026-08-30T06:11:13.960Z

### R41 joint breaker succeeds topologically but exposes a new seven-packet obstruction

Rapid Quartz 33’s `asg_WVUZRXaA9N0cJIoYqPx4tocV` is a **USED exact nonwinner**. It recovered a 141-file archive, reran an independent verifier to `ALL_CHECKS_PASS`, and supplied exact-dyadic generators, isolated hard-moment roots, complete H/V/E lattices, four-component edge-cone ledgers, perturbation certificates, and watertight OBJ/STL. The construction genuinely destroys all eight original R41 forcing edges and all eight intermediate transfer edges, so it is not another within-cell polishing failure.

The strongest open endpoint is `J40_final` (and count-equivalent exact post-wall `J41_postwall`) with `(H,V,E)=(2686,5368,8052)` and `(S,U,H)=(7,39,44)`. Its stable rows are `{0,2348,2349,2351,2366,2367,2369}`; all three ordinary moments have a unique Krawczyk-isolated root, the full audit has strict margins, and a five-dimensional parametric box preserves the lattice and class. A new row-disjoint true-edge matching
`(0,36), (2348,2453), (2349,2384), (2351,3404), (2366,2471), (2367,2402), (2369,3386)`
forces `S>=7` throughout that box, with equality attained. Thus the eight-pair obstruction was not destroyed globally; it was compressed and rerouted into seven nonlocal packets. The exact isolated `J40→J41` wall changes the lattice but not the class. The first unclassified exit is the bracketed quad `(2351,2456,3439,3474)` near `g∈[0.0625,0.0635]`; no exact wall box is yet claimed.

This strengthens the global lesson that joint endpoint control alone still transports Euler-neutral Morse packets unless it changes the whole connected S–H/U–H incidence complex. The evidence-implied successor should start from `J40/J41`, preserve row `0` as the intended stable feature, and use one genuinely volumetric shared-incidence replacement to destroy the six nonprotected forcing pairs together with the attached unstable–saddle network, while keeping at least two independent antibirth channels and three dependent moment controls. A serial seven-edge breaker would likely repeat the same transport mechanism.


## 2026-08-31T00:08:14Z — Exact sixth-stage carrier atlas has full local rank, but every finite path transfers the pair

The six residual core rows form a combinatorial octahedron with opposite pairs `(198,247)`, `(224,228)`, `(229,258)`. A concrete short-relay complex, `OCT_X_SHORT_RELAY`, consists of twelve tetrahedral relays `[198,224,k,k-1]` for `k=241..230` and a four-tetrahedron fan with diagonal `(198,247)`. Its boundary ball has `(V,E,F,T)=(18,49,48,16)`, minimum determinant about `13.09575178`, an 18-cycle attachment, and two 16-triangle disks; it deletes edges `(198,224)` and `(229,247)`.

Three natural exact carrier parameters `(rho,sigma,eta)` have rank three, but their common event is not globally supporting: none of the intended 16 faces is exposed, and both the base and short rail fail. An exact eight-control Jacobian has rank eight; a moment-closed five-control subfamily has rank five on rows `198,224,228,232,248`, determinant about `178066.356`. Its first wall is at `q≈0.114916`, circuit `{198,224,257,258}`, and transfers the stable feature to `[198,224,257]`. The fixed-topology supremum is `0.997866<1`; the codimension-three root already has an unrelated stable face `[198,241,224]` with margin about `0.002071`. A regular cap realizes all 16 local target faces but only 56 intended global faces, class `(2,18,18)`, and meets remote circuit `{54,257,258,259}` first. Local rank is therefore not the obstruction; global support transport is.


## 2026-08-31T01:20:48Z — Rational combined endpoint has no graph obstruction

The exact `(61,161,102)` combined endpoint admits complementary spanning trees of 60 and 101 edges covering all 161 true edges. A complete 164-sign assignment includes both acute rails and has no graph-level separator obstruction. Failure must therefore occur in support geometry, incidence order, or mass closure, not in the primal/dual routing graph.


## 2026-08-31T01:28:27Z — Mega supporting shell is exact but rank deficient for the full mechanics

An exact plane with normal `N=(100,20,-6)` and support `H=3700` supports the intended 16-gon. Positive small `s,h` insert shortcut edge `(197,227)`. The supporting shell has class `(3,8,9)`; its own stable shell survives, but the base and `U8` fail. The first anti-birth wall is `1.39678e-6`, the inherited death is only at `8.09e-5`, and the first hull wall is `[69,228,233,234]` at `0.0044555`; 25 walls intervene. The combined support/mechanics event has rank at least four.


## 2026-08-31T03:28:22Z — Exact supporting-shell reconstructions separate rank from realizability

Two lost support tracks were reconstructed from the authoritative fifth-cell lattice. First, projecting rows `231..246` to `100x+20y-6z=3700` and replacing row `228` by `(-19,-35,-12)` gives an exactly audited `(V,E,F)=(61,150,91)` body of class `(3,4,5)`. Five rational controls have exact cancellation-gradient rank five, but adding the selected `H(8,246)` wall raises the augmented rank to six. An exact inequality-form Farkas certificate inside `|control_k|<=10` proves the selected five-control first-order branch infeasible; a sixth independent control or a different witness branch is necessary.

Second, an exact rational finite row-228 carrier activates dormant rows `226,227` and gives `(V,E,F)=(63,169,108)`, strict `(2,1,1)`: stable base plus `[198,224,258]`, unique unstable `8`, and sole saddle `(228,229)`. The smallest exact mechanics component is about `1.75463e-3`. Six hundred fresh-hull scans of each natural stable actuator show an unstable-saddle birth before the stable wall. Thus a finite global carrier can move the saddle without paying `U228`, but carrier plus one serial stable actuator still transfers the pair.


## 2026-08-31T03:28:22Z — Deep-target rank-five root exists, but complete guards force transfer first

On the robust `(61,163,104)` target sphere, five projective-chart walls—death of the extra stable foot, `U1`, both saddles, and relay face `[228,247,258]`—have rank five and a nonlinear shared root with projective increment approximately `(-.0471169,-.0441643,+.0493350,-.242303,-.0946592)`. The fresh hull remains exactly the same numerical cell, the five residuals are below `9e-14`, and the minimum projective denominator is `0.15984`. The path is nevertheless pre-empted: the neighboring `S[8,245,7]/H(8,245)` pair reaches its wall at `alpha≈0.571284`, followed by `U10/H(10,11)` near `0.91243`.

An independent complete fixed-cell guarded LP used 113 plane-compatible modes, 7,322 primitive rows and 6,362 guards, enumerating all sixteen saddle-component choices. Every branch has normalized first guard loss `delta>1`; the best is `delta=1.0073999413` for deaths `F0@(8,245)`, `U1->2`, `H67:t`, `H910:(1-t)`. Its dual is dominated by the nonunstable witness `2->1`, explicitly identifying the `U1`-to-`U2` transfer, with thin carrier support slacks as secondary blockers. This is a strong first-order obstruction for the realized fixed cell and mode family, not a global topology exclusion.


## 2026-08-31T04:38:00Z — Row-54 has exact local rank six, but the shared root leaves the actual cell

For both rail-valid row-54 endpoint and far geometries, five explicitly rationalized zero-equivalent wall functions have exact gradient rank five. Adding the selected sixth wall retains gradient rank five but raises the augmented rank `[G|f]` to six. A primitive exact integer left-null vector satisfies `lambda^T G=0` and `lambda^T f != 0`, proving exact affine incompatibility of that six-wall set. Adding the base-tangent actuator on row 54 has exact nonzero `lambda` response and makes the `6x6` determinant nonzero; hence the first jet itself has no rank obstruction once that actuator is admitted. The reproducible exact artifacts are `tracks/piecewise_transfer/rank6_row54_exact_affine.py/json` and the rank-six report/verifier.

After removing unrelated edge-singularity failures from the nonlinear evaluator, the endpoint does have an actual six-scalar common algebraic root using the rail-safe `row11:base_v` actuator: maximum wall residual `4.39e-13`, minimum projective denominator `0.77708`, and all 37 forced rail edges present. But its one-sided hull is not the source cell: it has `(V,E,F)=(61,177,118)` rather than `(61,162,103)`, the fixed-face test fails, and the full class remains `(2,2,2)`. Thus exact rank lift produces a shared algebraic event but not a guarded cancellation event. The far-side five-root remains incomplete and meets unrelated walls first.

Independently, a 13-dimensional actual-Qhull search over row-54/row-246/metric controls improved the complete guarded defect by a factor about `15.3`. Its best admissible member has `(61,162,103)`, all 61 rows, the enlarged base, U8 and both rails, with hard score `-3.551203073e-4`; the four remaining errors are `U1=-3.551e-4`, `H(198,263)=-3.493e-4`, `H67=-2.475e-4`, and `S[7,245,246]=-2.414e-4`, while U54 is barely excluded by `+8.41e-7`. Nonlinear all-guard refinement crosses `U54=0` and immediately opens `H(1,54)` around `-3.5e-4`, entering `(2,3,3)`. The next actual event is therefore the elementary `U54/H(1,54)` wall, not a sign-only four-death root.


## 2026-08-31T04:15:25Z — A six-primitive row-54 compensating packet has full rank but remains a nonwinner

A corrected raw-hard local continuation materializes `row54_multicell_rawmin_local_831593.csv` with a fresh all-active `(61,162,103)` hull, the enlarged base, all 37 rail edges, and strict class `(2,3,3)`. Its target hard margin is `-0.00519655`; the active compensating packet is `S[7,8,246]=-0.00104372`, `U6=-0.00326719`, `U54=-0.00519655`, `H56=-0.000289056`, `H67=-0.000814388`, and `H910=-0.00519655`. The six-row first-jet packet has rank six in the metric-eight, base-36 and joint-44 mode sets. Joint singular values are approximately `(233.995,31.958,10.9035,.68862,.03441,.0116194)`; the metric-only smallest singular value is `6.33e-6`. Thus there is no local rank obstruction, but the compensating root is ill-conditioned and currently sits in a larger Euler-neutral `(2,3,3)` packet. The reproducible rank and full-hull artifacts are `row54_rawmin_stationary_rank.json` and the corresponding CSV/face/audit files.


## 2026-08-31T04:15:25Z — Exact intrinsic base actuation does not turn the row-54 rank lift into a fixed-cell event

The row-54 rank-six construction was rebuilt with intrinsic base-tangent motions applied before the projective map, so base coplanarity is preserved identically rather than repaired extrinsically. The best endpoint residual floors are about `2.278e-3` for `row11:base_v`, `2.02152e-5/2.02155e-5` for the two row-54 tangents, and `2.02251e-5/2.14548e-5` for the two row-1 tangents. Every candidate retains all 37 acute rails, but none retains the requested fixed cell; the typical fresh lattice is `(60,160,102)`. The exact artifact `rank6_row54_intrinsic_actuator.py/json` and updated verifier pass with `accepted_fixed_cell_event=false`. Hence the earlier extrinsic row-11 algebraic six-root was not hiding a genuine intrinsic fixed-cell cancellation.

The same exact artifact now also contains inequality-form Farkas certificates, rather than only the affine left-null identity. The endpoint necessary subset is infeasible throughout the five-control box `|c_k|<=1/5`, with primitive `mu>0`, exact `mu^T A=0` and `mu^T b<0`; the far subset has the analogous certificate in `|c_k|<=1/100`. The reported base-10 magnitudes of the exact negative right sides are about `440.481` and `164.150`, respectively.


## 2026-08-31T04:27:40Z — Three fixed-cell first-order obstructions now have exact or directed certificates

The earlier numerical Farkas evidence for the local-octahedral/row-54 track was rebuilt independently with exact analytic derivatives. In the shared three-dimensional row-54 model, a four-row exact rational dual supported on `U54` death, `H67` death, topology of face 15 against row 8, and the `263-264` anti-edge component has `y>0`, `sum(y)=1`, `A^T y=0` exactly as Fractions, and `b^T y=-87.0567876011`. In the full thirteen-dimensional fixed-cell model, all 6,305 primitive rows were rebuilt exactly; a fourteen-row exact rational nullspace certificate has strictly positive weights, exact `A^T y=0`, and `b^T y=-3.9185958887276e-5`.

For the original normalized core-beta model, the raw sign-primitives alone become feasible, showing that the old finite-difference certificate was representation-dependent. Replacing those derivatives by analytic interval AD and 90-digit directed square-root bounds yields a nineteen-row strict Krawczyk inclusion with `A^T y=0`, `sum(y)=1`, and `b^T y` enclosed in `[-0.009100078605714657,-0.009100078605713246]`. `M42_acute_bridge_fifth_cell_work/tracks/local_oct_cell_search/rigorous_farkas/RUN_ALL.sh` finishes with `ALL RIGOROUS FIXED-CELL FIRST-ORDER CERTIFICATES PASS`; the report records and rechecks all source/face hashes. These are rigorous obstructions only for the named fixed-sign, fixed-cell affine first-order systems, not for actual-cell nonlinear continuation or the global construction.


## 2026-08-31T05:45:34Z — The grouped passage reaches its first independent mandatory-rail topology obstruction

Continuing beyond the exact round-two and round-three null bypasses and the now-exact round-four cross reaches a new actual circuit on the quad `{9,198,263,264}` at path parameter `alpha=3.441866632876038e-5`. The isolated wall removes triangles `(9,263,264),(198,263,264)` and edge `(263,264)`, and inserts `(9,198,263),(9,198,264)` and edge `(9,198)`. The root determinant is about `2.395e-19` after an exact plane correction of row 264 of size about `1.153e-16`.

The strict pre-cell has all 61 rows, `(61,162,103)`, class `(2,2,2)`, the enlarged base, both acute rails, old guards `U263,H(10,263),U1,H(1,54)`, and old-packet hard value about `-2.757234589e-4`. At the wall and on the open far side the mechanics class and old guards remain valid, but the mandatory long rail fails exactly because its required edge `(263,264)` has disappeared. Thus this is a genuine topology obstruction for the current two-rail continuation contract, not a Farkas or numerical-floor obstruction; it is not yet a global mechanics obstruction because an alternative acute route or a higher-dimensional bypass may exist.

The standalone grouped verifier checks 51 round-two, 51 round-three and 123 round-four fresh path samples, the exact endpoint identities, the terminal pre/wall/far flip and a 39-file SHA-256 manifest, with all hashes matching. Reproducible artifacts are `row54_round8_topology_event*`, `grouped_escape_verification.json`, `grouped_escape_manifest.json`, and `verify_grouped_escape.py`.


## 2026-08-31T05:45:34Z — A sixth supporting-shell control gives exact rank six but a physical-trust blocker

For the exact supporting shell `(V,E,F)=(61,150,91)`, class `(3,4,5)`, the row-246 tangent direction `(-7,8,-90)` satisfies the shell plane identity `(100,20,-6)·d=0` exactly. Both exact probes `+/- d/900`, each with coordinatewise physical displacement `0.1`, rebuild to the same actual hull and class while preserving the stable 17-gon base, protected unstable vertex 8 and all 37 forced rails. Adding this control makes the selected six-death gradient matrix exact rank six.

Rank is nevertheless not physical realizability. The unique affine common root requires maximum coordinate displacement about `58.62500824`; its fresh exact hull collapses to `(24,65,43)`, class `(3,5,6)`, loses the base and protected `U8`, and retains only 20 rails. More strongly, the six-death system together with `|Dc|_infinity<=0.1` has a literal repaired rational Farkas certificate with `y>=0`, exact `A^T y=0`, and `b^T y=-0.17565499476121785<0`. The verifier ends with `ALL_EXACT_RANK5_SIXTH_SUPPORT_CONTROL_VERIFIERS_PASS`. Therefore the selected fixed shell cell is blocked at physical trust despite full local rank; its useful continuation must cross an actual support/incidence wall rather than pursue the macroscopic formal root.


## 2026-08-31T14:24:56Z — The grouped U6/H56 obstruction has an exact bounded affine-body bypass

The simultaneous degree-nine `U6/H(5,6)` birth at `t≈2.291066601001303` on the recovered round-twelve line is not a full-body obstruction.  An exact bounded deformation from checkpoint `A` at parameter `9/4` to checkpoint `B` at `23/10` changes the complete body rather than crossing that root.  The relevant exact Jacobian ranks are ten and eleven.  The whole bypass retains `(61,162,103)`, own-centroid class `(2,2,2)`, all 61 active rows, the enlarged base, protected `U8`, the accumulated positive-dot route and all 7,904 certified support/mechanics primitives.

At strict checkpoint `B`, the mechanics are stable base plus `[7,8,245]`, unstable vertices `8,54`, and saddles `(6,7),(198,263)`.  A subsequent fixed anisotropic affine line has another exact degree-nine common root for `vertex:6:5` and `edge:(5,6):one_minus_t` at `t≈150.1038672836875`, where class would become `(2,3,3)`; that continuation is recorded but rejected.  The useful frontier is exact `bypass_B_t23_10.csv`, from which a different full-control nonbirth continuation must start.

The coordinator's canonical `RUN_ALL.sh` rerun ends with `EXACT_U6_H56_BOUNDED_AFFINE_BODY_BYPASS_AND_NEXT_EVENT_PASS` and `INDEPENDENT_EXACT_U6_H56_AFFINE_BODY_BYPASS_PASS`, followed by a full manifest readback.  Certificate, verification, builder, verifier and exact-B SHA-256 values are `4be2565adc8ac47f98769b2ff3a5f2107d3efc053ccda6ef7254c51f2f59b918`, `b951e38cf9ce07f067ec60d2d627047fe9f599fb0816c1a9c8fbf8cdb9992adf`, `b01666e45efdc205ed6347d4b0c7030de944e68b394a41c18689d97048cfea12`, `93511834cab7d9c7e706cedc51d8652e7daef5c98821a5617ba2bb0b4b8cd2a2`, and `2bb67ca51ea25c9e5c1b168dfcc68c3295559374df660b4c1bed4673daf73a52`.  This is still a strict nonwinner; the next attack must avoid the new common root rather than extending the fixed affine ray.


## 2026-08-31T23:40:19Z — The reciprocal U1 event is promoted from obstruction to an ordered carrier relay

The fixed-ledger identity `V(54,1)+V(1,54)=4*d6*||p54-p1||^2>0` does more than reject the old no-earlier-event U54 wall.  A fresh read-only component audit shows that the forced reciprocal event can be used as the birth half of an ordered `U54→U1` carrier relay.  Crossing `vertex:1:54 == edge:(1,54):t` from negative to positive changes class `(2,2,2)→(2,3,3)`, with unstable carriers `{1,8,54}` and saddles `{(1,54),(5,6),(10,11)}`.  A later crossing of `vertex:54:1 == edge:(1,54):one_minus_t` returns `(2,3,3)→(2,2,2)`, replacing U54 by U1 while retaining H56 and H1011.

The direct two-event ray is explicitly rejected.  Its approximate ordering is birth `λ≈0.0098198`, row-230 loss `λ≈0.108482`, U54 death `λ≈0.888889`, and its FAR has only 60 active vertices.  Therefore the attack is segmented and source-bound to independently verified `step15_transfer_far.csv`, SHA-256 `7f16c070aeba30199758815215774877bf759554d5dca1c6d875b85f27c8b94d`: exact birth and rational middle checkpoint first, then a mandatory fresh full-support row-230-inward rechart before the death epoch.  No relay artifact is accepted yet; a new isolated sidecar owns this contract.


## 2026-09-02T00:41:43.257Z

### Full-rank Minkowski continuation integrated; nonsimple shared circuit is the new frontier

Clear Raven 08's completed assignment `asg_8x6TbEVkF65Gx9RjjrnurqOf`, immutable SHA-256 `599aa5600d87686fdb92addf017959c97d8760994ee9c88cecd2692ccc845839`, is **USED**. It is an exact nonwinner, not a Gömböc.

The corrected post-`CU10` six-facet protected summand reaches its full physical quotient rank `3m-3=15` and remains strict own-centroid `(2,2,2)`. Adding an irredundant seventh facet produces a full rank-18 protected family with exact `D=(V,E,F)=(10,15,7)`, common refinement `(50,92,44)`, exact zero first moment at the unique positive control root `(t1,t2,t3)=(1,1,1)`, and an independently verified open 18-coordinate `(2,2,2)` cell. A stronger exact dyadic preserving-descent endpoint reduces all four unwanted margins but remains `(2,2,2)`; exact checkpoints show mechanical births and carrier transfers before the first common-fan change, then return to `(2,2,2)` by relay rather than cancellation. These are path/cell determinations, not a continuum exclusion of the full seven-facet family.

The first unclassified topology is now sharply localised: a **nonsimple seven-facet shared-circuit locus** connecting in one three-dimensional normal-fan cell the extra stable carrier `D(0,1,6)`, transferred source carrier `D(1,5,6)` or its `9/32/103` replacement, the `13/26` gates on `D` edges `(2,4)` and `(2,6)`, and the return gate on `(0,1)`, while preserving the intended stable and unstable lineages at `D(0,4,5)`. The smallest candidate has one four-valent `D` vertex adjacent to a triangular-prismatic or octahedral `2↔3 / 3↔2` shared cell; if unrealizable with seven planes, the directly implied next architecture is an eighth active facet furnishing the bridge.

No accepted homogeneous polyhedral Gömböc exists yet; the exact rational M42 acute-bridge fifth-cell remains the strongest accepted near-object at own-centroid `(2,1,1)`. The idle Clear Raven 08 slot should own the nonsimple seven-plane shared-circuit realization/exclusion before any eighth-facet enlargement.


## 2026-09-02T01:29:27.965Z

### Calm Quartz 90 nonlocal SPD obstruction integrated; stale handoff consumed; two lifecycle failures

Pending coordinator handoff `e84399dd…` adds no mathematical fact, accepted object, blocker, uncertainty, frontier, or next move beyond the durable journal. Its claim that all nine assignments were transport-healthy is stale and superseded by live events `2790–2792`. No homogeneous convex polyhedral Gömböc or completion ticket exists. The independently verified exact rational M42 acute-bridge fifth-cell `(V,E,F)=(61,163,104)`, own-centred strict `(S,U,H)=(2,1,1)`, remains the strongest accepted explicit near-object.

Calm Quartz 90 result `asg_LAlbUnRUF9qabnkbq9KzIH2P`, immutable SHA-256 `9ab6e7c9aef71c91d58ca1c73768be2f465fa6a94afd361ea6a164157cb7230e`, was read completely from cursor `0` through `eof:true` and is **USED**. It proves a rigorous component-level nonwinner for the exact Santaló-centred 4,324-row trace-one SPD family: throughout the full SPD orbit, stable row `2092` cannot remain the unique stable equilibrium. The parent spectral certificate covers the complement of `K >= (19/4115)I`; inside that region, a complete 67-node/56-leaf exact branch tree over relay faces `{2110,2145,2163,2180,2181,2216}` gives nonnegative six-support Farkas duals forcing the common strictness margin negative. Because this outer relaxation omits all unstable-vertex and saddle-edge requirements, retaining unstable vertex `2693` cannot evade the obstruction. The strongest connected endpoint remains exact `PRE_16494`, class `(2,2,2)`, with stable rows `{2092,2180}`, unstable vertices `{2028,2693}`, and saddle edges `{1603,11125}`. This result does **not** exclude fixed-lattice cells whose unique stable row differs from `2092`, nor topology-changing support/incidence families.

The direct nonrepeating fixed-lattice successor is therefore a simultaneous exchange across one of the six row-`2092` death walls—`12265,12475,12479,12686,12688,12690`—that installs another unique stable row while also cancelling the unwanted unstable/saddle packet. Calm Quartz 90 should own this alternate-stable-row chamber problem; preserving row `2092` would instead require topology change and is no longer the best use of this slot.

Steady Harbor 62 assignment `asg_z2QL9_H8lghNyTgUM1vhrxM9` and Steady Willow 02 assignment `asg_R5l7W_88uX8rH_zq5Oxpt5Fa` are explicit transport/lifecycle failures caused by HTTP 429 and published no immutable mathematical result. They are eligible for recycling; this is not evidence against their mathematical directions. Reopen, in fresh copies, the exact J45 higher-valence terminal-cell frontier and the exact P9 two-row/old-plane-motion terminal frontier already specified in the journal. Nimble Comet 70, Quiet Raven 13, Steady Quartz 25, Vivid Quartz 58, Sharp Nova 46, and Clear Raven 08 remain active on distinct useful directions.


## 2026-09-02T22:06:52.357Z

### Five exact terminal-volume continuations converge on one obstruction

No literal homogeneous polyhedral Gömböc was obtained in the five newly completed branches, but each produced a fully materialized own-centred topology change and the agreement between them materially sharpens the search.

- **M42/T37:** the original extra stable triangle `[198,224,258]` and saddle `(229,247)` are genuinely deleted, while the intended stable feature and unique unstable vertex `8` survive. The exact endpoint has `(V,E,F)=(91,253,164)` and strict `(2,1,1)`, with a replacement stable triangle `[198,3000,1025]` and saddle `(1027,3001)`. Frozen-boundary star pages require at least seven new apices, and the fixed-page continuation cannot escape without releasing or deactivating at least six old rows. The next admissible M42 topology is therefore a full-dimensional `T37-R6` event or changed-diagonal non-star prism/double-octahedron, not another page.
- **wall-242 third-support endpoint:** the old packet is deleted by a positive-volume full-star event, but the exact endpoint remains `(2,2,2)` because a new forcing component is carried by edge `[1975,2732]` together with the stable limiting edge `[2152,3290]` and the new saddle routes. The first unclassified successor is one fourth support participating in the same multi-cell event and jointly destroying the entire new component.
- **low-complexity `E19ZC -> E21S -> E17K`:** the unique actual `{F,8,U,V}` circuit and a finite-thickness shared-volume cell are exact, but edge `{F,M}` rigorously forces `U>=2` throughout the `E21S` chamber. The compact `E17K` successor leaves that chamber yet transfers the obstruction to `{A,B}`. A nonrepeating successor must give at least one endpoint a certified nonpositive external arrow or replace the intended carrier in the same nonsimplicial event.
- **post-CU10 closed-edge branch:** the closed double-octahedral/prismatic terminal volume deletes every predecessor carrier, but a new stable/unstable/two-saddle packet is born and the extra unstable star is rigorously external-positive. The first new topology is a second independent corrector summand `E` forming a non-boundary mixed three-cell, preferably a paired-Radon or cubical/antiprismatic `4<->4` event.
- **P9-XG8:** the three-row double-cap is an exact complexity-54 own-centred `(2,2,2)` body. It deletes both inherited forcing edges and all inherited unwanted features, but the new edge `Z1-Z2` is external-positive and forces `S>=2`. The smallest unclassified successor is a four-row closed octahedral/hexahedral two-cell that deletes `Z1-Z2`, source `T27/SU/Z0`, stable `Z2`, and both saddles jointly while preserving the intended pair.

The common mechanism is now explicit: every positive-volume event above honestly removes the predecessor lineage, yet an internal edge or paired vertices of the new cell acquire all-positive external arrows and force the Euler-neutral replacement equilibrium. Successor construction should therefore impose the external-arrow sign pattern **before** hull realization: every potential new internal carrier must have at least one certified nonpositive external arrow while the intended stable and unstable features remain strictly positive. The three ordinary moments should continue to be solved by dependent controls after reserving enough independent shape variables.

Priority order is: (1) M42 `T37-R6`, because it remains exact `(2,1,1)` with `U=1`; (2) the low-complexity P9-XG8 four-row closed two-cell; (3) wall-242 fourth-support full-star; (4) a second Minkowski corrector summand; (5) the compact E17K carrier-breaking cell.


## 2026-09-03T03:07:00.726Z

### Vivid Atlas 32 exact XG10 endpoint — edge carriers eliminated, obstruction contracts to one full row-star

Vivid Atlas 32 returned an **exact finite nonwinner** that advances the P9 branch to its first verified edge-level carrier-free full-star event. The endpoint has 27 supplied / 12 active support rows, `Q:(V,E,F)=(12,30,20)`, primal `P:(20,30,12)`, complexity 60, and exact own-centred strict class `(S,U,H)=(2,2,2)`. A connected positive-volume five-row triangular-bipyramid event on `V0,…,V4` deletes all four inherited `W0,…,W3` rows, the forcing edge `W2-W3`, and the complete XG9 residual packet; the interior diagonal `V0-V2` is not a boundary edge.

The new decisive fact is that **every inserted or inherited-star-changed nonprotected true edge has a strictly negative external arrow** (20/20; no non-`T27` external-positive edge). Thus edge-level anti-carrier inequalities are genuinely insufficient. The obstruction has contracted to a singleton/full-row-star sink: `G` has positive outgoing directed support to every true neighbour and is a second strict stable face beside protected `T27`. Its Euler-neutral packet is extra stable `G`, extra unstable `G/V2/V4`, and saddles `SC1-G`, `S102-G`; intended unstable `TR/S102/G` survives. Six independent shape controls remain after exact moment elimination (nonzero `6×6` Jacobian), and an open independent-coordinate chamber of radius `2^-23` preserves the full incidence, `(2,2,2)` mechanics, carrier-free edge audit, and `G` obstruction.

This is a stronger global full-star expansion from a `1/64` homothetic XG9 predecessor, not a local path certificate from the unscaled endpoint. Individual exact, interval, clean-room, and mesh checks pass; only clean one-command archive packaging is unfinished.

The first nonrepeating frontier is a **six-row target-star split / nonsimple closed-prism event** replacing `G` by communicating descendants: `G_T` must preserve intended unstable `TR/S102/G_T`, while `G_R` absorbs and cancels `G/V2/V4`, `SC1-G`, and `S102-G`. The event must exist as active positive volume before moment closure and make `T27` the unique sink of the complete directed row-star graph. If one extra support cannot separate target and return roles, move directly to a distributed seven-to-nine-row full-star prism.

