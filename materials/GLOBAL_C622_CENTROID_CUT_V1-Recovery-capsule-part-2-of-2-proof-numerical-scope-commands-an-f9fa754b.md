# material-f9fa754b9629

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# GLOBAL_C622_CENTROID_CUT_V1 — complete recovery and evidence boundary

## 1. Scientific status
The new contribution is a complete executed floating-point locator that crosses actual hull cells while restoring the true volume centroid by one clipping plane. It replaces the older failed fixed-lattice Newton search. It is NOT an exact equilibrium certificate, a continuous exclusion, a smaller own110 attainer, or a proof of local minimality of C622. The accepted endpoint remains the exact canonical C622, and 34<=C_min<=622 remains unchanged.

The analytic existence of a global centering cut and the one-facet derivative were already proved in SINGLE_FACET_TRUE_CENTROID_V1. This material adds the maximum-volume characterization in section2, the cell-crossing implementation, a fully specified completed 780-trial negative locator run, and literal reusable checkpoints. Original 133 simple-ear deletions at the new COM had already been exactly excluded near M=I; restoring the centroid changes the shape, so those exclusions do not apply automatically to the present children.

## 2. Analytic interpretation: unique maximum-volume centered subset
Let K be a bounded full-dimensional convex body with 0 in its interior. For q in R^3 set P_q=K intersect {q.x<=1} and

    Phi(q)=integral_K max(1-q.x,0) dx.

It is convex and continuously differentiable, with grad Phi=-J(P_q), where J(L)=integral_L x dx is the actual unnormalized first moment. A ball of radius r around0 contained inK gives Phi(q)>=pi*r^4*|q|/4, so Phi is coercive and attains a minimum q*. Hence J(P_q*)=0. The clipping plane is unique whenever the clipped body is essential; if K already has COM0, every redundant cut gives the unchanged body.

A useful further characterization is exact and independent of the numerical solver: **P_q* is the unique up to null sets largest-volume measurable subset L of K with J(L)=0.** For any such L,

    Vol(L)=integral_L(1-q*.x)dx
          <=integral_K max(1-q*.x,0)dx
          =Phi(q*)=Vol(P_q*).

Moreover for arbitrary q and measurable L contained inK,

    Phi(q)-[Vol(L)-q.J(L)]
       =integral_(P_q minus L)(1-q.x)dx
        +integral_(L minus P_q)(q.x-1)dx >=0.

Equality forces L=P_q up to measure-zero subsets of the cutting plane. If q=0, equality instead says L=K up to null sets, with the same uniqueness of the body. This is also a constructive linear-programming dual certificate for maximum retained volume under exact first-moment zero. It does not optimize edge count or equilibrium count.

On a proper active two-dimensional cut F, H(q)=integral_F xx^T/|q| dA is positive definite and D_qJ=-H. For an outward integration triangle a,b,c on q.x=1, d=det(a,b,c)>0,

    contribution to H = d[(a+b+c)(a+b+c)^T+aa^T+bb^T+cc^T]/24.

Thus a Newton step for J=0 is dq=H^-1 J. The locator evaluates actual newly intersected hulls after every step; it does not continue a formula beyond a fixed face-lattice chamber. The exact maximum-volume theorem is not a guarantee that a floating line search converges or that its reconstructed facets are correct.

## 3. Complete immutable dependencies
Recovery capsule part1 is `[internal-source-reference]`, literal complete source `global_cut.py`,7740 bytes,SHA-256 `5b2e8e0ac2a2c9db4001d40e0641b00fbe2ec39bfaaaebc80cbe595ac3adfac1`.

Its only geometric input dependency is the COMPLETE canonical scoped16 capsule:

1. `[internal-source-reference]`, COORD_C622_CANONICAL_SCOPED16 part1,15305 bytes,SHA `d5846089dd79e70e4aa35f67d5d66b8480c3dd72bca1de45359a281931f632aa`.
2. `[internal-source-reference]`, corresponding part2,20685 bytes,SHA `c4a0ef05c36066f7b2851dc18ea1c3cda599f724130ec0ce7a89785613cde5b1`.

Both were read completely, decoded according to their literal instructions into the exact sixteen source files, and executed in this coordinator segment with

    python -B -S SOURCE/REPLAY_SCOPED.py PROOF

The markers SCOPED_EXACT_A_PASS, SCOPED_EXACT_B_PASS, and COORD_C622_SCOPED_CANONICAL_AB_MASS_CONTROLS_PASS were observed. The two independent exact auditors reproduce the canonical actual176/311/137 body, true uniform COM,strict110,physicalweak000. This source replay is a real exact computation, not a scientific conclusion inferred from a hash receipt.

Decoded source map68603 bytes,SHA `63b9a7de970fa8fb01f43ce10bec573441e5afeebe4ef2d3b7031ea6fb64c9ca`. Normalized base64 fragments are14000 and13840 characters; combined27840-character SHA `6a7d42eeabc1365c9dc122a9e62e6127e779db025765c6cbb37107cb31788638`. The capsules themselves contain all bytes and commands, so these pins are identifiers, not substitutes for source content.

Required generated inputs:
- PROOF/A.json:311825 bytes,SHA `142ddb5d88fdc8b1721dbb62f52d9b71b78ac4c36e8600131235c6c4289698a0`.
- PROOF/raw.json:15437 bytes,SHA `ac01d1625274b64f336a715e1f5462f40686f647f0b7d1a4d90a5ee21765adb5`.

The locator checks both hashes before use. It uses the literal raw H planes and the EXACT raw mass centroid from A, not the numerical zero approximation. Raw plane n.x<=h is centered and normalized as q=n/(h-n.g). Exact Fraction arithmetic constructs every ear plane and tests the old mass center strictly on its retained side.

The earlier analytic global existence proof and exact actuator-incidence checks are separately durable in `[internal-source-reference]`,15294 bytes,SHA `6bb96b86f9ea7b91744503d2d0eb3b8de93d6ee82c95b5649cd314f01be581c8`. Its own exact source dependency is not needed to run the present locator: canonical geometry and all ear construction used here are fully in the source above. A successor needing to rely on the old global incidence audit as evidence should also receive that complete proof and its explicitly listed dependencies.

## 4. Run and non-default parameters
Executed environment CPython3.13.5,NumPy2.3.5,SciPy1.17.0,assertions enabled. Source sets OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1 before NumPy import. No RNG is used. Floating reproducibility on other library/platform builds is not asserted.

Save part1 literally as global_cut.py, UTF-8 with LF and one final LF. After recovering SOURCE and PROOF above:

    python -B global_cut.py PROOF/A.json PROOF/raw.json global_000_003.json 0 3 reducing
    python -B global_cut.py PROOF/A.json PROOF/raw.json global_003_039.json 3 39 reducing

The runs both finished, printing

    GLOBAL_C622_CENTROID_CUT_LOCATOR_FINISHED_NOT_CERTIFICATE 60
    GLOBAL_C622_CENTROID_CUT_LOCATOR_FINISHED_NOT_CERTIFICATE 720

The max_steps100,root_tol2e-13,active_tol2e-8,dedup_decimals10,Armijo1e-4,max_halvings35,spectral_floor1e-12,max_step0.2 are literal in the source. It also uses eigenvalue absolute floor1e-16, hull support tolerance1e-7, line-search potential tie tolerance3e-14, improvement factor0.999, and S/U sign and possible-zero threshold1e-12. All these values are part of the exact method. A reported numeric root means norm(J)/V<2e-13, not exact J=0.

For each released facet f and ear i, keep every old halfspace except f, add the exact ear halfspace, and optimize one new normalized cut q.x<=1. The start is the old q_f. The normal always describes a real single clipping plane, not independent mass variables. Numerical HalfspaceIntersection followed by ConvexHull recomputes the actual clipped vertex hull, tetrahedral volume and first moment for every proposed q. Integration triangles are not mechanically counted as edges.

The twenty released simple facets, in exact canonical raw H/A face order, are

    [48,55,69,70,89,93,99,100,101,105,110,112,113,114,115,117,120,123,124,125].

Numerical incidence comparison also confirmed that all137 raw plane labels coincide with A's face labels. Only the39 ears whose unmodified deletion removes at least one old triangular face were scanned:

    [0,2,5,7,8,15,21,36,42,51,60,71,79,80,81,82,85,89,91,95,97,99,101,103,104,106,110,112,113,121,126,133,137,139,142,145,146,170,175].

The other94 degree3 ears were NOT scanned by this global method. They could in principle change complexity after centering; no exclusion is claimed for them.

## 5. Completed output pins and honest exclusions
- global_000_003.json:121060 bytes,SHA `2c171411e679ac2734ea4cca3a5c0098fd07ccf6a9ef5b82dc4899a54b7d82a8`.
- global_003_039.json:1273818 bytes,SHA `e4337c31118bf3d442e9b53d7de28fdaff900f323a0e4bb5f856e2cb2c55708e`.

The complete source plus exact canonical inputs and all listed parameters reconstruct the entire report, including every trial cut and iteration trace, without the originating sandbox. The literal selected cut checkpoints below also allow direct continuation without repeating the solver. These numeric reports are not promoted to exact geometric certificates merely by these pins.

Of780 trials,778 returned numerical_root and2 iteration_limit. The latter are (ear79,release99), final centroid norm8.169597232963703e-7, and (ear82,release99),1.4356736130553309e-7. Both remain unconverged.

The floating facet reconstruction satisfies Euler V-E+F=2 for775 trials. Five numeric-root records fail it and are discarded as geometric census evidence: (71,105):0;(81,48):0;(106,120):-45;(139,105):1;(146,99):-6. These discrepancies are a concrete tolerance/reconstruction failure, not exotic polytope topology. The run did not silently repair them.

Therefore773 records satisfy BOTH numerical_root and Euler2. Their numerical U counts are

    {2:25,3:150,4:246,5:170,6:95,7:52,8:20,9:11,10:2,11:2}.

All773 have U>=2 numerically, and97 have S=1. None has S=U=1. One record (5,105) flags possible_zero_U=1; exclude it from any strictly positive numerical margin claim. The remaining772 have no possible-zero flag among the max guards; this is NOT a complete physical-weak audit. The unaccepted (82,99) iteration-limit record also flags one such zero.

The numerical C values among these773 range604..710. Examples include (7,120):C618,S2,U2; (60,123):C604,S2,U3; (139,99) and(139,123):C620,S2,U2; several C620,S1,U3 checkpoints below. The lowest S+U=3 record (133,99) has C710,S1,U2 and does not improve complexity. Numerical strict H and grouped physical weak points were not computed for these children. No whole-neighborhood or all-SPD exclusion is proved by this finite scan.

## 6. Literal checkpoint20: exact continuation input, non-record bodies
Save the next single JSON line including one final LF as global_checkpoint20.json. Expected2254 bytes,SHA `189ad64e23592936d2094b9d8fcdfd661bef49fe62759808ec94bcd9abc832bd`.

The ordering is deterministic: take the773 numeric-root/Euler2 records and sort by (C>=622,S+U,C,ear,released), then retain the first20. `float_CSU` records the unverified locator census, not an attainer claim. Every decimal is the complete original Python float serialization; do not shorten it. To define an exact rational child, those decimal strings may instead be interpreted literally as rationals together with the exact old centered planes and exact ear plane. That is a new fully specified rational cut body, but its TRUE volume centroid and full mechanics must then be recomputed. The root certificate does not transfer automatically from floating q to decimal-rational q.

```json
[{"ear":7,"float_CSU":[618,2,2],"q":[2.038643354757607,-0.6373527661839626,-0.837665249870615],"released":120},{"ear":133,"float_CSU":[620,1,3],"q":[-1.0553140645394297,0.36801412558045576,-1.2450796496006864],"released":114},{"ear":139,"float_CSU":[620,2,2],"q":[-2.0202774437946984,1.2893566834871781,1.020887334406466],"released":99},{"ear":139,"float_CSU":[620,2,2],"q":[-0.9961081708895719,-0.1961897448315886,-1.3702361147897162],"released":123},{"ear":145,"float_CSU":[620,1,3],"q":[-2.1419861273758416,1.0323573446341288,1.0123664555183638],"released":55},{"ear":145,"float_CSU":[620,1,3],"q":[-2.191879436383543,-0.6866001539925385,1.01455949338523],"released":115},{"ear":146,"float_CSU":[620,1,3],"q":[-1.0627966963540907,0.36184237599100993,-1.2411948154073664],"released":114},{"ear":146,"float_CSU":[620,1,3],"q":[2.027468653048001,-0.6169296034979802,-0.8031430222346453],"released":120},{"ear":170,"float_CSU":[620,1,3],"q":[-1.3690727976268589,0.09372140863692675,-1.0110032299676208],"released":117},{"ear":175,"float_CSU":[620,1,3],"q":[-2.15841033375801,-0.7680118740664786,1.0150571850126293],"released":99},{"ear":60,"float_CSU":[604,2,3],"q":[0.1804640482869794,2.1968942353434144,-0.10933038760371135],"released":123},{"ear":8,"float_CSU":[616,3,2],"q":[2.1273172021619433,-0.8622452368879129,-0.36519569092146303],"released":117},{"ear":91,"float_CSU":[616,2,3],"q":[-0.23627170190111688,1.4309298952830696,-0.9294563933992885],"released":55},{"ear":5,"float_CSU":[618,2,3],"q":[1.749601346320374,-0.3968564195699222,-1.3916118839283966],"released":55},{"ear":7,"float_CSU":[618,2,3],"q":[1.7853190442849358,-0.4255701383032672,-1.3406763788869527],"released":114},{"ear":7,"float_CSU":[618,2,3],"q":[1.752286292787691,-0.40256833663016384,-1.3889069580541955],"released":115},{"ear":51,"float_CSU":[618,2,3],"q":[0.2864769175687345,2.1443114818658136,-0.12711519809769603],"released":123},{"ear":71,"float_CSU":[618,2,3],"q":[-0.0065014487720881425,1.2863752875935,-1.0676597185519467],"released":123},{"ear":91,"float_CSU":[618,2,3],"q":[-0.5769974952381952,0.8847379751155273,-1.283515665333672],"released":114},{"ear":95,"float_CSU":[618,2,3],"q":[-0.6114119880638594,0.8746707249118522,-1.2765163924901404],"released":114}]
```

For a numerical direct reconstruction, `a,Q,ears,facets=global_cut.load(A,raw)`; select the ear by its literal vertex label, set `K=vstack(delete(Q,released,axis=0),ear['q'])`, then call `geometry(K,array(checkpoint['q']))`. That call recomputes the full volume centroid; `census` recenters both vertices and poles by that actual computed centroid. This fully specifies every checkpoint using only the durable capsule dependencies, not local transient filenames.

## 7. Next scientific question and unchanged endpoint
A single centered cut is now computationally viable across combinatorial changes, but centering alone did not produce own110 in the completed scan. The useful next questions are a COMMON reciprocal affine metric on the low-S/U repaired bodies, two-facet shape motion with moment control, or larger changes. All could change true complexity and require new exact hull/ownCOM/physical-packet checks. The fact that a centered subset retains maximal volume is not evidence that it has minimal E, minimal equilibria, or no further useful deformation.
