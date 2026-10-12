# Agent 1 scientific findings

Goal active: own-centroid strict (S,U,H)=(1,1,0), weak000, C=2E<500. No new claimed solution.

## Initial source recovery

Current run brief and manifest copied read-only from `/opt/pro-research/profiles/figure/runs/run_STKzndEKqZbC2DiJMPEJgLeH/`. They report exact C622 own110 and small own211/121/222 bodies; these reports are not independent verification by this agent.

A literature search found https://arxiv.org/html/2609.07827v1 by Tancredi Schettini Gherardini (2026-09-07), reporting a 56,946-facet homogeneous monomonostatic polyhedron. It is outside the target.

## Independent exact reproduction and numerical finite experiments
The agent-written GMP auditor `audit_exact.py` reproduced C622 strict110/weak000/primitive000 with V176/E311/F137. Exact physical coordinates, maximal facets, volume and centroid match the independently executed inherited B report from agent-2. Known cube and weak-contact controls pass. This confirms an existing baseline, not a new solution.

The complete J90/J91 five-material set was recovered with SHA checks, extracted into `sources/j91`, and its exact input manifest verified. `recover_j91.py` reconstructs the literal J91_REBALANCED_C434_G18 physical body with exact facet-support checks. Independent rational audit confirms V135/E217/F84, strict211, weak000, primitive000. The body is not110. Its 84-support representation permits arbitrary bounded full-dimensional support motion while E<=246.

Executed support coarsening trials with seeds1024,1025,1026 started from 85 selected C622 supports (retaining the 44-plane apex). They produced reduced bodies with numerous additional equilibria. They are negative finite trials, not exclusions of support coarsening.

Actual-volume differentiable radial-persistence optimization is implemented in `persistence_search.py`. Linear total depth produces many shallow basins. Concave log consolidation from J91 C434 reduced the largest floating Q depth from about .162945 to .13084, but generated numerous tiny positive P/Q defects (P max around1e-7); it is NOT an exact211 or110 improvement. Polishing and constrained continuation are being investigated. Full inputs, scripts, logs, and best/final support arrays are retained.

## New exact nonwinner A1_C492_FLOW_G14
Rational support coordinates on a 10^14 grid, actual full homogeneous mass and centroid, maximal incidence and complete strict/closed signs are in `artifacts/A1_C492_FLOW_G14/`. Independent rational audit returns V164/E246/F84,C492, strict211, weak000, primitive000. This is a finite descendant of J91 C434 under free support motion, not110. The floating last-Q depth is about .16287141758; exact no-cutoff bars are being computed. Its source is `constrained_flow.py`, adaptive run checkpoint `artifacts/j91-constrained-adaptive/latest.npz`.

## New construction family
`SELF_POLAR_NOTES.md` gives the negative-self-polar source, the agent-derived physical cone-section map, its actual-centroid Jacobian, and limits of the executed finite searches. No own110 candidate exists in this family yet.

## New exact C468 own211 checkpoint and strict repair
`artifacts/A1_C468_Q013_G15/` is a complete new rational physical body: V156/E234/F80,C468, strict211, weak000, primitive000. Exact P is empty; sole exact normalized squared-radius Q depth is approximately0.13102251879575857, versus .162945 for the literal J91 C434 parent. This uses17more true edges and is NOT110. H.json alone defines it; audit.json contains full exact coordinates, incidence, uniform moments and centroid, all strict/closed signs; boundedness.json provides six rational normal-cone certificates; bars.json includes every positive exact bar.

`soft_forest_polish.py` adapts agent3's shared bottleneck-forest/L1 correction to our support-plane own-mass Jacobian with physical-coordinate SVD conditioning. It retracted the unconstrained47S/44U numerical output to2S/1U in2steps with guards~5e-7. This is substantive elimination of the small defects, followed by exact verification, not a tolerance-based zero claim. The current continuation alternates free support persistence descent and strict repair (`alternating_descent.py`, `artifacts/alternating-j91`).

## Own110 retirement path and independent density continuation
- The literal accepted C622 support body can be generically released while preserving its44-plane actual apex and then restored to numerical own110 by the bottleneck/SVD repair. This opens non-simple vertices and therefore initially INCREASES complexity. Greedy physical facet retirement followed by full shape correction deleted two supports. Complete exact G15 audits (both original rational sign engine and new homogeneous-integer sign engine, every field and serialized byte identical) confirm `artifacts/A1_BASE_RETIRE_TWO_G15`: V225/E358/F135,C716, own110, weak000, primitive000, P/Qempty. It does not improveC622 and is not the goal. This is evidence that deletion+shape correction can work; the earlier fixed-coordinate single-deletion failures remain valid. `coarsen_apex.py` continues attempting further retirement.
- `audit_integer.py` derives vi=Pi/di, g=G/D, Ai=PiD-Gdi and eij=Pjdi-Pidj. All equilibrium decisions reduce to integer signs: vertex sign Ai.eij; facet n.(Ai cross eij); edge foot signs -Ai.eij, Aj.eij; cone vector |eij|^2Ai-(Ai.eij)eij. Every removed denominator is positive. Exact controls against two previous C468/C454 reports match every field, and the C716 fresh original audit matchesbytewise. Original audit_exact.py retained.
- `mass_homotopy.py` constructs a separate explicit search path c_lambda=(1-lambda)sum wiXi+lambda*g_volume(X). lambda<1 is a nonuniform/artificial reference measure and is NEVER reported as own110. The planar spiral angles are inspired by Domokos/Kovacs arXiv2103.13727 Table1; our literal initial object did not reproduce the printed census and was independently deformed to a valid numerical pointmass110seed. Therefore this is not an author-body replay.
- The21point seed followed a strictly retracted reference110 path up tolambda0.11735957584109623. Adding one tiny outward vertex per facet (59supplied controls, newpoint weights0) extended it tolambda0.4736595775874554 with52actualvertices and E150, then the tested corrector stalled. Physical owncentroid atlambda1still has extra equilibria.
- `homotopy_predictor.py` couples shape andlambda in a maximum-progress LP plus nonlinear correction. A59control branch passedlambda0.4822 while stillrunning; a separate85control refinement is running. Onlylambda1andexactphysical auditcouldsatisfygoal. Sources savedwithhash in `sources/literature-provenance.json`; code and all finite intermediate bodies preserved.
- Exact apex-compression nonwinner `artifacts/A1_C454_APEX10_G15` has V149/E227/F80,C454, own211/weak000/primitive000, soleQ0.18324840843032. This savestrueedges butdeepensbasin; notanunconditionalimprovement.

## Complementary support parametrization from the exact peer cap body
The14smallest-area nonstable supports were removed from Peirce's literalC294 cap-flow input (98facets), then all84remaining supports were physically deformed by our full own-mass strict121 repair. Result `artifacts/A1_C486_CAP_RETRACT_G15`: exact V162/E243/F83,C486, own121, weak000, primitive000; one relativeP0.38344289404440074, Qempty. This is WORSE persistence and largerC than theC294 parent (.338758), but it has a substantially larger free-support deformation space while every generic body with84submittedsupports hasE<=246. Complete sourcepins/removal list at `artifacts/peer-c294-to-f84/source.json`; exactaudit/boundedness/bars/manifestallpreserved. It is notgoalprogressbyitself. A dualThales continuation is running from this body.

Initial dualThales logistic parameterization stopped explicitly at firstrechart becauserho saturatedits imposed cap; no numericalor exactwinner wasclaimed. Originalproducer retained asdual_thales_v1_logistic.py. Currentdual_thales.py useslogrho coordinates, explicitnegativebounds, and actualcentroidprojectionto1e-14; its independent directionalcheck passes (`artifacts/dual-thales-exp-gradient-check.json`). InitialKF49/KF84 lossreductions stillhave many tiny positive primalbars, not111.

## Current exact checkpoint and reference-centroid transport
ExactfinalretirementbodyA1_C698_RETIRE5_G15: V219/E349/F132,C698,own110weak000primitive000,P/Qempty. LargerthantheacceptedC622; notgoal. Thelower-edge originalHminus5rows is a different exactC620body with53/32/83, not110.

The search now uses a fully reconstructed C430 contactchart(V74/E215/F143) withstrictreference110andactualown33/40. Source/planunderartifacts/transport-merged-contact-e7, successfulfullfloatingnoncontact/orientationchecks. contact_centroid_flow.py minimizesactual |g|/Rmax, retainsreference110, andfixespositive normalizedvolumefloor topreventdegeneratescaling. Onlyexactactual-own111auditcouldqualify.

CAPACITY_MERIT_NOTE.md provesarealizableexamplewherechosen-tree direct-edgeL1meritjumpsataparentchange; actualwidest-pathcapacitiesremaincontinuousforfixedvectors/root. Sharedwithpeers; notapolyhedralsolutionorlowerbound.


# Positive basin transfers on actual own211 bodies

The complete method is `basin_transfer.py`. It deforms physical support normals, rebuilds the hull, integrates the same uniformly filled body, and keeps one primal maximum and two polar maxima. It selects a new polar arrow from outside the elder root's entire positive-reachability set into that set. All old positive arrows are initially retained; the junior root's negative guard is released when the junior root itself is the transfer source. The identity a.(b-a)+b.(a-b)=-|a-b|^2 explains why a target in a preserved return component is unsuitable. Relevant external scoped observation: `sources/J121_fixed_policy_exit.md`, exact source SHA fc95dbc358a615d254209a2ed7014fce814c4a8b3fbe019e52822cb20222c0be.

A whole-support Jacobian includes the actual centroid derivative. A linear predictor is followed by own211 correction and complete body checks; accepted stages increase the elder's positive-reachable set. The latest implementation additionally enforces positive margin1e-7 and rejects finite states with actual/committed capacity margin below8e-8, avoiding numerical boundary drift.

## Exact endpoint comparison
- `artifacts/A1_TRANSFER_INITIAL_G15`: V156/E234/F80,C468,own211,weak000,primitive000; soleQ .1121557474039721. Elder support18 is reachable from25 of84 supplied supports,22 of80 active facets.
- `artifacts/A1_BASIN_TRANSFER_CHECKPOINT_G15`: V154/E231/F79,C462,own211,weak000,primitive000; soleQ .3068431396600983. Elder18 is reachable from43 of84 supplied supports,39 of79 active facets. Junior stable carrier changes fromsupport7 tosupport5. Audit SHA 14a21a0a87bbd30f9888c0ff98582fb04b49affc92b265b396eae5e8f8695e95.
- `artifacts/exact-basin-transfer-reach.json` supplies exact positive adjacency and reachable sets for both physical bodies. `exact_polar_reach.py` derives integer sign n_i.(s_i n_j-s_j n_i) where s_i=h_i D-n_i.G>0 and G/D is the audited actual centroid.

The surviving basin became deeper. This is a constructive source for changing its ownership and carrier, not a persistence improvement and not the requested figure. Numerical continuation reached51 of84 supports after25accepted stages, stillown211; phase2 is ongoing. All true hull counts remain below the requested limit.


## Exact C456 own121 after facet-union reconstruction
`artifacts/A1_RECT_MERGED_C456_RECHART_G50` is a NEW rational physical body: V121/E228/F109,C2E456,V+E+F458,strict(S,U,H)=(1,2,1),weak000,primitive000. AuditSHAdc1ccbf3bef7701804a04e6575ef5a089d579d4ac5858b276388f03bc034fb7f. The actual uniform volume/centroid, every maximal facet/edge/vertex and all exact signs are in audit.json; H.json defines the body; boundedness.json proves completeness of the bounded halfspace body. This is not the requested Figure.

Starting from peer3's exact rectangular C488 own121 body (pinned in sources/peer-agent3-rect-C488), the full physical contact family reduced numerical P .35054331499->.34784432282 and reached coalescing support planes. Facet unions were proposed in merge_contact_facets.py; proposal-only thresholds do NOT establish true coplanarity. The merged graph is3-connected; only the `--quality` eligible-node ordering gave an accurate local reconstruction (condition133 versus3e12 undergreedy; balanced was also inaccurate here). The valid numerical reconstruction retained own121. Thus no peeling rule is universally best.

The longdepth65 rational chart caused expression growth before even writing H. It was explicitly stopped uncertified. rechart_high_precision.py evaluated its literal grid15controls at80/120decimaldigits (agreement3.57e-80), then rounded the FREE controls of the depth7chart to a50digit rational grid. These exact target controls define a DIFFERENT rational body. freeze_atlas.py directly reconstructed and audited THATbody, including exact primalvertexset/incidence agreement. This is an independent exact endpoint certificate, not acceptance by a small numerical residual. Complete sourcecontrols, newtargetcontrols and bothchart/sourcehashes are in artifacts/rect-C456-shallow-controls.

Subsequent numerical own121fullcontactdescent reached P~.3475957 before another nearlyflat contact. No smaller/own110 claim follows fromthatunfrozen continuation.


## Exact C374 own121 from explicit contact events, 2026-09-29
`artifacts/A1_RECT_C374_G50`: V105/E187/F84,C2E374,actualsum376,own(S,U,H)=(1,2,1),weak000,primitive000. Exact P=.2597910363407892,Qempty. AuditSHA18b4d2a3f0c2d9fedf8f1e969d11e78079c634de2fb417e85772bcc0f27f5deb. All physical H, exact genuine incidence, integrated volume/centroid and strict/weak signs, boundedness, bars and construction controls are complete. It is not110.

Starting from peer3's exactC488rectanglebody, alternatingfullcontactdescentandexplicitmergesofcoalescingsupportfacets ledtoC398, thenvanishingprimaledgeswerecontractedwithmerge_contact_vertices.py. Eachnewcontactcomplex wasindependentlyreconstructed andcheckedforallnoncontacts/orientations. TheexactcheckpointisdefinedbyG50freecontrolsofthedepth6chart, notbynumericaldistancethresholds. Longdepth66qualitychart was evaluatedat80/120digits, roundednewshallowfreecontrolsthenfullrationalaudit; sourcesinrect-C374-exact-controls.

The84supportspermitunrestrictednormalmotionwithuniversalE<=246. Tinyseededphysicalnormalperturbationplus2steppolishyieldednumericalown121E245 inrectangle-f84-release, thenrectangle-released-P-descentisrunning. Parallelcontactbranchcontinuesown121belowE187withP~.253. Newadaptive_contact_events.py choosesanexplicitvanishingprimalorpolaredgeevent; unreadmitttedtopologiesarefailedproposals, neveracceptedcoplanarity.

Own110C622margincontinuation atbalancedchartimprovedminimumangularselectedguardsfrom1.0698e-8to2.8715e-7 whilemaintainingphysicalnumerical1S1U. Its exactfreecontrolfreezeA1_C622_MARGIN_G15isrunning; Cstill622. Finitefacetretirementfromthisbodyisbeingtested. NoC<500own110claim.


## Local continuation checkpoint, 2026-09-29 19:20 UTC
The native persistent goal is active. The exact A1_C622_MARGIN_G15 freeze completed: same genuine V176/E311/F137, own110 weak000 primitive000; it remains over budget. A second floating strict branch reached minimum angular margin3.83023e-7, and new contact_maximin.py continues a strict own110 path by maximizing the least selected escape margin, using full physical retraction and an actual positive-volume floor. Margin improvement is not complexity reduction.
Literal deletion of each of137 facets from the earlier improved body yielded no own110. Deletion99 is an exact V174/E308/F136 own121 weak000 primitive000 body (artifacts/margin-retire99-exact); its floating full-contact P descent reduced remaining depth from.00120763 to about.000847. Still nonwinning and over budget. The separate old-reference-centre retirement screen also found no reference110 among those137 literal deletions; this is a finite screen, not an exclusion.
Rectangle adaptive contact events ended at floating V102/E182/F82 own121, P.2525912634. The last exact endpoint remains C374. Its released-support branch ended at floating V160/E240/F82 own121,P.2169381971. New facet_split_scout.py deliberately divides a polygon into two distinct true support facets; complete noncontact admission is required before mechanics. First split admitted V102/E183/F83 and retained own121, with only a small P improvement so far.
The unrestricted nine-stage support continuation from C468 fragmented equilibria and ended S52/U60 with Qmax.11621036; no winning nomination.64 seeded nonmonotone strict-chamber hops produced no110 and only minor Q movement around.112. Results are saved, not treated as exclusions.
New stable_face_augmentation.py screens800 literal one-vertex convex hulls beyond the unwanted stable face. Sampling inside a reference Thales ball does not transfer equilibrium claims through actual mass shift. All800 bodies were evaluated; none passed the ordinary <=84-support continuation entry condition. Many have actual E<249 with85+facets because the added apex has high valence. contact_augmentation_scout.py preserves that genuine contact pattern and searches those bodies instead. The contact-free bound was an experiment restriction, not a complexity claim. Sources, all candidate points, census and scores are in artifacts/C468-stable-face-augmentation-20260929.
Peer3 reports exact C492 own121 P.11578 after physical oblique caps and vertex retirement (inbox/20260929T190559Z_agent3_exact_C492_P01158.md); not110. Shared local feed read through19:07UTC; no VPS access on this resumed turn.


## Exact C478 own211 after a new physical vertex augmentation
`artifacts/A1_AUGMENT_C478_G15`: V156/E239/F85, true2E478, V+E+F480, own(S,U,H)=(2,1,1), weak000, primitive000. Exact soleQ=.10379059129166049; Pempty. AuditSHA 95bb7d32c6bf5ea7382662f2b1e751651f44be75379bacd44b3537391381f5ed. Complete physical halfspaces, rational free-control construction, actual uniform volume/centroid, genuine incidence, complete equilibrium/weak signs, boundedness and bars are linked in manifest.json. Every manifest entry was reread and hash-verified. This is not own110.
Starting from exact C468 own211 Q=.1121557474, stable_face_augmentation.py sampled a literal new point beyond the junior stable facet, within the diameter-(0,existingU) Thales ball in the OLD centroid frame. This only nominates a reference escape; every candidate is independently reintegrated. The best tested augmentation has a high-valence new vertex, F85 with E240. contact_augmentation_scout.py preserves that incidence instead of generically moving85 support planes. Strict actual-centroid correction then Q descent reached a vanishing old edge; explicit contraction independently reconstructed V156/E239/F85, giving the exact checkpoint above. Sources: artifacts/C468-stable-face-augmentation-20260929/sample100 in screen.json; artifacts/C468-augmented-contact-scout-20260929/trial02-sample00100; artifacts/augmented-Q-adaptive-events-20260929/event000-vertices/body. The exact G15 body uses a new shallow balanced chart and a complete rational audit, not a threshold-based edge count.
Further numerical contact events have reached E238,Q about.10286, stillown211. They remain unfrozen.


## 2026-09-29 new exact bodies and centroid-preserving cap method
A1_AUGMENT_C466_G15 is V150/E233/F85,2E466,sum468, own211weak000primitive000, soleQ .09958470308420042. It is a shallow-chart exact reconstruction of the second augmentation cycle followed by explicit primal edge retirements. Further floating endpointQ .09950038256 retains E233; the next augmentation cycle is running. The separate first augmentation branch ended at numerical V148/E229/F83 own211,Q .1024807233.
A1_BALANCED_CAP_C488_RAW is V153/E244/F93,2E488,sum490, own211weak000primitive000, soleQ .18163930006045279. This is a new exact literal four-point extension of exact C454. BALANCED_CAPS_NOTE.md proves the conditional old-vertex escape-ball lemma and describes three compensating facet pyramids and full-hull implicit moment closure. Every manifested exact file was reread and hash-verified. Neither body is110.
The rectangle facet-split scout finished8 independent splits; best floating E183 own121 P .2471996141. No winning result. Root-replacing one-vertex screen examined1600 physical bodies: reference U1 always, reference S>=2; ownS+U>=6. The all-witness escape-ball scout examined1600 candidates: no reference110. These finite results do not exclude their larger families.
C622 maximin stopped at numerical margin4.7895e-7 with same311edges; preserved checkpoint. C616 retired-facet P descent stopped at .0008441408, stillown121 and over budget. Literal retirement of nearly coincident facets in a bold S3/U1 augmentation did NOT annihilate its extra basin; a nearzero local inequality concealed positive Q depths~.049 and.097. Early explicit edge-event handling now prevents some numerical approach to coincident supports.
Peer2 independently replayed exact C478mass/counts and found support4deletion retainingown211E239 with84facets; he explores its unconstrained support release. Peer3 reports further exactown121P.1089533. Sharedlocalfeedreadthrough19:43UTC; noVPSaccess. Nativegoalactive, no blocker, no qualifying Figure.

Exact audits: {"A1_AUGMENT_C466_G15": {"E": 233, "F": 85, "V": 150, "audit_sha256": "d98dc00057536121fcc7187c515518568294051ecc54db84a73c4ffe6215b0ea", "counts": [2, 1, 1], "primitive_zero": [0, 0, 0], "weak": [0, 0, 0]}, "A1_BALANCED_CAP_C488_RAW": {"E": 244, "F": 93, "V": 153, "audit_sha256": "3af14cd766e5b98fd02d789c0d8b57c45686e660f39dd278651eb831766e2683", "counts": [2, 1, 1], "primitive_zero": [0, 0, 0], "weak": [0, 0, 0]}}


## 2026-09-29T20:23:46.122588+00:00: exact balanced-cap descent C480 own211
`artifacts/A1_BALANCED_FLOW_C480_G15`: V150/E240/F92,2E480,sum482,own211weak000primitive000, Pempty, exactsoleQ .08862848419014692. AuditSHA b5f1a32a375b85dc1734b8a8fd70904ba527d3d8758bf7c78451f8417d0a12a3; every manifest file was reread and hash-verified. This is not110.
Scientific chain: exactC466own211Q.0995847 -> literal four-point first-moment-balanced addition -> three-variable full-hull moment closure optimization (numericS3/U1,Qmain.09730 plusoneQ~1e-7) -> full-contact true-centroid class correction -> explicit facet and vertex retirements. contact_topology_continuation.py uses balanced charts and stops a flow at an explicitly nominated short edge, then independently reconstructs/admitsthe new body. Exact reconstruction audits actual hull counts; thresholds never certify coplanarity. A numpy boolean serialization error interrupted the first continuation after its second numerical event; it was fixed and the saved state resumed in continuation2. No geometric result was lost or promoted by that error.
`retire_compensation_vertices.py` reconstructs ancestry through literal vertex_groups and facet-union retained-vertex mappings. One of the3old compensator vertices had already disappeared. Two surviving tags are currentvertices129 and142. Their literal double retirement followed by full physical correction and events reached floatingown211E234,Q~.09205; individual retirements are still being tested. This recovers edge budget but has not improved Q beyondtheC480parent.
Other finite branches:1555 literal adjacent-facet-pair convex combinations on exactC622marginbody producednoown110andnoreference110; minimumE308, noexclusion. Existing-support centroid compensation had0admissiblepositive triples among22robusteligiblefacets foritsone testedmainpoint; noexclusion. Nine-parameter balancedcapsearch retainedU1butstallednearQ.17677withnearzeroextraQconditions. Completecensusremainsessentialwhenbarsfallbelowfloatingresolution.
Peer3's single-old-vertex mass compensator was pinned in sources/peer-agent3-vertex_mass_compensation.py. My adaptation restricts the moved vertex to an all-triangular maximal-facet star, preserving every nonincident polygon facet. On25mainpoints frommyC466parent therewasonlyoneeligibleoldvertex(144), andnonecompletedcentroidclosurewhilepreservingreferenceS<=2/U1. This is a finite negative experiment, not a theorem.

2026-09-29T20:48:00.349010+00:00

## Full-contact centroid compensation and broader stable-basin search
The twelve shallow literal caps from C480-reference-contact-mass-closure-20260929 all numerically closed their actual centroid to relative residual below1e-12 while preserving referenceU1/S<=2, and independently evaluated as own211. Best sample25 had Q=.0883785125816775. Its physical contact continuation ended V150/E242/F94 own211, Q=.08775369561415103. Reference and own equilibrium counts remain separate; these are numerical results, not exact110.

Compensator ancestry retirement completed. Removing oldtag compensation2 (currentvertex142) and admitting its actual contact complex gave numerical V148/E237/F91 own211,Q=.08856947041872165. Removing both remaining tags gives V145/E233/F90,Q=.09200156452359542; removing onlyvertex129 gives V146/E234/F90,Q=.09315693547700399. These all have one extra stable equilibrium and saddle. Exact C474 freeze of the first is running under A1_RETIRED_COMPENSATOR_C474_G15.

Finite vertex splitting uses a genuine diagonal in a nonsimple vertex's polar face, adding one edge and one vertex. Infinitesimal first trial was explicitly stopped because it immediately remerged at the event threshold. New vertex_split_scout.py initially opens the new physical edge to normalized1e-5 using the explicit edge_minimum argument to contact_forest.correct, then releases it to Q descent. First finite trial admitted the split but remerged that edge under descent, then retired another edge; endpoint V149/E239/F92 own211 Q=.08856115671921372. Other trials are live. This is not evidence against the whole split family.

New contact_multibasin_flow.py keeps only the actual-centroid unique-unstable guards, allows stable roots to split and merge, and minimizes the sum eta*log(1+Q/eta) of ALL positive polar persistence intervals. Exact census is still mandatory. Three independent centred directional derivative checks had absolute errors <=6.2e-10. The C474 start reached E236 with many shallow stable roots; largestQ fell to .0734 in an early phase, but later consolidation raised it to about.08744 and still had ~60 stable roots. A strict own211 correction is running; no small bar is discarded.

Deep cap reference mass closure with unrestricted referenceS did not close any of6 tested caps in70 iterations; ownU remained28-31 and residual mass ~1e-3. The source and failures are in C480-largecap-uniqueU-mass-closure-20260929. New deep_cap_recombine.py instead corrects ACTUAL unstable guards directly (old reference centre unconstrained), then full-contact multibasin flow and complete strict correction. It is running locally. No VPS was accessed; native goal remains active, no blocker, no qualifying Figure.

## 2026-09-29T20:48:56.016461+00:00 Exact compensation-vertex retirement
`artifacts/A1_RETIRED_COMPENSATOR_C474_G15` is a new rational V148/E237/F91 body: true2E474, actual V+E+F476, strict own211, weak000, primitive000, soleQ=.08856947041872196 and Pempty. AuditSHA b9a6852eecd46f95b093eb7dc216cadfa913b41bf7237fb50fc6925077534b42. Every manifest entry was reread and hash-verified. It removes the old surviving compensation2 vertex from the C480 continuation, then admits and optimizes the new full contact body. Complete rational controls, H, actual uniform mass/centroid, maximal facets/edges/vertices, all strict and weak signs, exact no-cutoff bars, and boundedness are included. It has an extra stable equilibrium and saddle; not the requested Figure.

## 2026-09-29T21:07:25.207016+00:00: exact C472 and new finite physical families
A1_MULTIBASIN_C472_G15 is V147/E236/F91,2E472,sum474,strict own211/weak000/primitive000; Pempty and exactsoleQ=.08741259195186439. AuditSHA 5c448110cdc6e85946120ae6ace93ccf004c7b436d0f062e5fb3a186044bac8d. All manifested files were reread/hash-verified. Allowing stable basins to split temporarily under actual unique-U guards, then full strict211 repair, produced this body from exactC474. Still not110.

Multiple-point flower augmentation tested1500 literal simultaneous additions of2-4 points, each with an explicit old positive escape witness. None achieved reference110. Best referenceQmax=.05689442225922403 had referenceS5/U1, actualS14/U30, V136/E234/F100. It has four positive Q bars, not an eliminated basin. `multiple_flower_points.py` and artifacts/C472-multiple-flower-points-20260929 preserve all points, witnesses, reference/own landscapes and input. Three candidates are now undergoing ACTUAL unique-U correction and all-Q flow in C472-multiple-point-recombination-20260929.

1200 balanced four-point candidates from exactC472 produced a numericalown211E248 bestQ=.0872562851578752, candidate00111-triple00825. This still has an extra stable root. Six deeper single caps are undergoing the separate C480-deepcap-recombination-20260929 experiment; first repaired endpoint was own211E239Q=.09419277, worse thanparent.

Local one-stable class exchange approached coincident normals5/7 but could not remove the whole stable basin. Explicit compound facet union with recursive retirement of degenerate neighboring polygons was admitted; it still had extraS/U and Q~.115. The capacity-guard variant reached S52/U32,Pmax~.00044,Qmax~.05738 in200steps; not a goal. `merge_contact_facets.py --compound-cleanup` records all retired facet groups, verifies a closed manifold and3connectivity, then reconstructs the proposed body; numerical thresholds are only proposals.

A revisit of the old direct C622 edge247 contraction found a healthy-volume E310 body with many microscopic positive basins. Its old chart depth79 was reconstructed in a new depth5 chart (coordinate discrepancy5.63e-14; independently complete physical-domain checked). Physical actual110 correction then removed tiny extra roots but ended own211,Q~1.94524e-7,E310. This remains OVER BUDGET and nonwinning. `C620-small-Q-cancellation-20260930` now tests that tiny remaining Q with full actual mass and strict nonjunior guards. Even a true110 endpoint atE310 would not finish the goal.

`cross_class_support_paths.py` explores literal affine interpolation of matched support vectors from exact A1_TRANSFER_INITIAL_G15 own211 and the own121 rectangle-released endpoint. Source centroids are normalized, orthogonal alignments explicit; every intermediate mass is freshly integrated. At most84 supports ensureE<=246.56orientations and47t values, then8 finite joint-correction attempts, are running. No verified goal figure. Native goal remains active; no VPS access.

2026-09-29T21:31:38.033636+00:00

## Local sustained research checkpoint, additional families
`full_vertex_release.py` replaces whole polar polygons by fans, releasing sum(degree-3) primal contacts. Simultaneously releasing C472 vertices146/145/141 uses10 new true edges initially: V157/E246/F91. The coincident proposal is admitted as a strict convex contact realization, then every new primal edge is explicitly opened to relative length.002 while recovering actualown211. Subsequent Q flow and explicit edge retirements have numerically reached E237,Qabout.08630. Three fan rotations are being tested. This is numerical, not a new exact goal result.

`multiple_cap_mass_balance.py` balances2-4 purposeful flower points with3 compensation caps that may cross old facet visibility boundaries. All actual hull moments/derivatives are recomputed. Among60 main proposals,303 first-moment closures succeeded;30 bodies hadE<249 and uniqueactualU, but all retained at least5stable equilibria. Lowest-sumQ body main00604-triple16192 hasE248,S5/U1,Q=[.0032362563,.0054009514,.0816935568,.0004543253]. A bounded all-Q flow explicitly limits maxQ<=.084 and is saved in C472-bounded-balanced-recombination-20260930; it reached one largeQplusmany~1e-5 positivebars, not211. Bounded class correction is testing the complete root guards with that cap retained. Unbounded strict repair from the same state is a separate live comparison.

`cross_class_support_paths.py` completed2632 interpolated physical support bodies across56 alignments between own211 andown121 parents, with at most82actual input supports. Minimum observedS+U21. All8 finite joint corrections failed to reach110. Sources, rotations, support arrays and fresh own-mass counts are saved. This is a finite negative screen, not a class-path exclusion.

`release_support_subset.py` greedily beams through7 literal support retirements from exact C472 to84rows, then releases all84normal vectors. Rank2 strict211 repair succeeded at numericalE246,Q=.1099641948, worse persistence thanparent; no110. This provides an unrestricted <=246-edge support family, but no improvement by itself.

The old E310near-110 contracted body was recharted fromdepth79 todepth5, coordinate discrepancy5.63e-14, with all strict noncontacts/orientations rechecked. Complete local correction reached actual211,Q=1.94523567587e-7,E310. The old persistence flow failed to move; dimensionless scaling of the QP progress row and relative decrease resolution then produced small real improvements. The finite over-budget branch was explicitly stopped at Q=1.94434667034e-7, still211; FROZEN_FINITE_CHECKPOINT and STOP_REASON retained. Neither smallbars nor E310 is goal evidence.

The lower-margin eps2e-9 C472 branch was stopped after125+ iterations at numericalown211,Q=.08740459626 (see its immutable checkpoint for exact stopped number), only a small improvement from.08741259. This does not exclude thinner figures. Its compute lane now tests the global maximum-bottleneck escape capacity toward the elder polar root. `contact_persistence_flow.py` explicitly supports objective_mode=capacity; its derivative passed3 directional checks with maximumabsoluteerror4.33e-9. This objective may increase radialQ depth while opening an actual escape path; neither objective alone constitutes acceptance. ActualS/U and complete physical contacts remain checked eachstep. Capacity-flow sources under C472-bottleneck-capacity-flow-20260930.

Latest exact under-budget source remains A1_MULTIBASIN_C472_G15 own211/weak000 Q=.08741259195186439. Agent2 received a substantive source-exchange message with its exact audit hash. Sharedlocalfeedreadthrough21:03UTC; noVPSaccess. Nativegoalactive, noblocker, noqualifyingFigure.

## 2026-09-29T21:42:35.753231+00:00: exact full-release checkpoint and new multi-root path
A1_FULL_RELEASE_C474_G15 is exactly V148/E237/F91, true2E474, sum476, own211/weak000/primitive000, Pempty and soleQ=0.08629952738133978. AuditSHA56a9728da3a6e30a610b69e881543779b0994994546901922f9893c880b6c47f. Every manifest hash was reread and verified. This is a new body from simultaneous full polar triangulations at three high-valence vertices, finite opening, actual-class flow and subsequent true contact retirements. It is NOT110.

The new complete escape-tree capacity objective is in contact_persistence_flow.py objective_mode=capacity-tree. It constructs an actual widest-path arborescence in the complete geometric chord graph, whose minimum edge weight equals the global bottleneck capacity. The collective LP raises ALL tree links together, then an actual physical retraction and fresh global capacity evaluation decide acceptance. Chords are not counted in genuine hull complexity. The3 directional gradient checks and rooted-tree reachability/minimum checks are saved.

The initial own211-constrained capacity-tree branch improved negative bottleneck magnitude .0772556->about.07133 and retired edges toE234, while Q deepened toabout.0898. No success. More substantially, trial1 of multiple-point recombination had failed the strict211 correction atS52/U3,Qmax.0379724, withtinyP. Correcting ONLY actualU restoredU1. A separate tree-capacity continuation holdsU1 and permits all stable roots, using the full same-body mass derivative and contacts. It has reached maximumQ near.0035 andE223 while Sremainsdozens. This is not a goal or count improvement by itself. The complete physical numerical checkpoint is immediately preserved at MULTIROOT_CAPACITY_CHECKPOINT_20260930_A, including raw physical coordinates/supports, z, chart/source links, mass/centroid, allQbars, capacity andvolume. Current source and live continuation: C476-multiroot-tree-capacity-20260930.

Bounded maxQ=.084 stable-basin consolidation generatedmanytinyQroots. Adding the cap to complete211correction failed its bound: numericalS2/U1butQ=.087789358, corrected=false. The constraint was NOT declared satisfied. Unbounded continuation fromthatbranch is independent. NoVPSaccess; nativegoalactive; noqualifyingFigure.

## 2026-09-29T21:52:00.725657+00:00 Two additional complete exact sources
[
  {
    "name": "A1_MULTIPOINT_C426_G15",
    "V": 125,
    "E": 213,
    "F": 90,
    "counts": [
      2,
      1,
      1
    ],
    "weak": [
      0,
      0,
      0
    ],
    "primitive_zero": [
      0,
      0,
      0
    ],
    "P_count": 0,
    "Q_count": 1,
    "Qmax": 0.10581803499944686,
    "Qsum": 0.10581803499944686,
    "audit_sha256": "cec50ce687421314bceec90faa8e3e6c3e72f17f6eab041877d9ef548d47bcde"
  },
  {
    "name": "A1_TREE_MULTI_C432_G15",
    "V": 132,
    "E": 216,
    "F": 86,
    "counts": [
      51,
      1,
      50
    ],
    "weak": [
      0,
      0,
      0
    ],
    "primitive_zero": [
      0,
      0,
      0
    ],
    "P_count": 0,
    "Q_count": 50,
    "Qmax": 0.003199219605819565,
    "Qsum": 0.07422622960279852,
    "audit_sha256": "9abfd045cd4b54fa627612b4fddc1e9e351859b8686d047936412762adb61a15"
  }
]
Both are nonwinning bodies, with complete physical rational halfspaces/free-controls, actual uniform mass and centroid, genuine maximal incidence, all strict/weak signs, exact no-cutoff bars and boundedness. All manifest files were reread and hash-verified. C426 is the new small-complexity own211 multipoint descendant. C432 has51stable equilibria,1unstable and50saddles; reducing maximumQ is not eliminating those roots. It is useful as a complete unique-U shallow-multibasin input.

The live multi-root capacity path has reached F85 with its actual unstable vertex ofdegree4. This permits full support release preserving only that four-plane vertex star, with E<=3F-k-3=248. release_apex_supported.py uses an explicit orthogonal similarity to put that old point at(0,0,1), retains literalq_z=1 on its4incident planes, perturbs all other coordinates, rebuilds the actual body, and independently corrects actualU1. No equilibrium conclusion is inherited through centroid change. The branch C426-multiroot-apex-release-20260930 is running from the saved physical entrance. The previous E213/F90 own211 release plan is a separate unexecuted proposal.

## 2026-09-29T22:16:30.364606+00:00 Joint capacity and disjunctive escape experiments
The exact C432 multiroot checkpoint was independently reconstructed by agent2 at G14; peer auditSHA0bb0bce07acb97d51c76189b4219380e5a72cf88d451e7be8f23cd93a6aa0701, with identical V132/E216/F86 own51/1/50 and weak000. Message inbox/20260929T215334Z_agent2_exact_multiroot_C432_and_apex_family.md links the complete separate rational source. No goal claim.

New EssentialMaxima/joint-tree mode simultaneously optimizes the minimum primal and polar complete escape-tree capacities while allowing both extra-root counts to change. It reached a finite numerical E206,S58/U68 body with Pmax.0017213749211,Qmax.0009682404343 and joint negativecapacity.0242540127435. Full same-body mass/contact snapshot JOINT_ESCAPE_MILP_ENTRANCE_20260930 preserves that input. Neither small bars nor improved capacity cancels those roots.

contact_escape_choices.py implements finite mixed-integer choices of outgoing physical arrows. Full tangent Jacobians passed directional checks (max2.41e-9). A3-second unrestricted381binary smoke produced no descending incumbent and was rejected. An explicit rotating14point/2parent group gives28binary proposals, each independently physically retracted and completely re-evaluated. The local-arrow L1 version reached E206,S16/U15 with tiny merging edges, Pmax.06355,Qmax.04971; thus its low angular residual is not persistence cancellation. Its explicit contact-retirement continuation and a separate acyclic radius-ordered-parent variant are running. Sources, definitions, solver statuses and selected arrows retained. Parent arrows are not hull edges. No figure is accepted from MILP feasibility.

The C426 own211 plan releasing35contact excesses at10vertices was executed for2polar fan rotations. Both failed finiteopening.002: several new edges stayed essentially coincident; one end stillS2/U1, the otherS2/U2. E248 combinatorial proposals are not accepted exact bodies. Saved C426-full-thirtyfive-contact-release-20260930. Large support hops' only generic amplitude stratum produced a failed Ucorrection, endingS49/U2; its tiny local angular residual coexists with Pmax.01002. This motivates explicit tree/acyclic alternatives, not a success claim.

The earlier own211 capacity-tree comparison completed E233,own211,Q.09076544. The unrestricted-S unique-U tree continuation completed E211,S51/U1,Qmax.00317126723. Full three-vertex release fan2 and small-apex support release remain separate finite comparisons. No VPS access. Native goal active, no owner blocker, no qualifying Figure.


New own analytic source: artifacts/TWISTED_LATITUDE_ANALYTIC_20260930/construction.md. The sphere diffeomorphism T(x,y,z)=(x,y cos(kx)-z sin(kx),y sin(kx)+z cos(kx)) turns ordinary height into f=z cos(kx)+y sin(kx), which has exactly2criticalpoints. The radial smooth body r=1+epsilon*f has actual-centroid0 when I1(k)+(3/4)epsilon^2 I2(k)=0; volume4pi(1+epsilon^2)/3. A global Hessian bound proves strict convexity at epsilon=.01 for k in(4,5); a100000-direction screen is only numerical evidence for epsilon up to.043. This is a smooth input, NOT the requested polyhedron. Any discrete hull requires its own mass and complete equilibrium audit.

The direct polyhedral family twisted_latitude_polyhedra.py uses at most83 literal support planes, half-turn pairs, a4plane axial vertex and one axial bottom facet; E<=243, and oftenE<=242. Old sampled smooth supports that cut the chosen apex are explicitly retired. Every body uses its own integrated centroid.2200 literal samples completed without110; minimumS+U10. Four fuller-complexity seeds are now undergoing direct actual110 correction with complete rooted bottleneck capacities, after releasing symmetry in a full contact chart: artifacts/twisted-direct-own110-correction-20260930.

contact_arborescence_flow.py uses a complete directed minimum-cost rooted arborescence (Chu-Liu/Edmonds) for each actual primal/polar landscape. Costs max(eps-arrow,0) ensure zero cost means every point escapes to the unique farthest point without a cycle. Unbounded comparisons concentrated barriers, ending numericE197own211Q.167488 andE213own22 withtinyP; boundedP/Q<=.004 comparison endedE216S46/U2, Qatbound. None qualifies; no exact partial audits started. The earlier local-choice continuation hit a3-connectivity failure; an explicit polar-first compound proposal reducedE202->199 but stillfailed the next vertex contraction. All finite failures retained.

900 geometric-cover flower additions from a12000point witness pool also failed110. A single allowed point can retire22of50oldstablefacets, but facet retirement does not equal root cancellation. Best reference count wasS10/U1atE233 after5points removing46oldstablefacets; actualS11/U27 andcentroidshift~.08. No follow-up replay or polishing planned for these partial bodies.

Two64trial physical projective orbit screens on ownC474/C432 sources failed110. All transformations used actual uniform integration and consistent duals. No exact audits of their nonqualifying endpoints. Nativegoalactive, no blocker, noqualifyingFigure.

## 2026-09-29T23:06:17.930908+00:00 Direct construction campaign and curved mass closure

New local direct physical methods and complete sources:
- twisted_convex_masscut.py: C2point hull of twisted radial samples, then horizontal truncation solving the actual uniform g_z=0.1200finite samples, all failed110. Independent final hull integration verifies the numerical moment closure; origin mass closure alone never counts as the goal.
- twisted_support_closure.py: for each unwanted reference-U, optimize a literal radial support witness and add it together with its exact half-turn image.48finite unpruned experiments mostly hitE>=249 before closingU. Explicit pruning of nonroot half-turn vertex pairs preserves every existing positive escape witness and checks origin containment;16pruned trials run for70rounds each. Some referenceU1 states occur but their actual-centroid census is different. No exact partial audits.
- apex_balanced_base_family.py: raising an axial positive-z apex preserves all positive reference escape arrows into it, because their source z must be positive. All other arrows are unchanged. Thus negative axial centroid can be moved towardzero without losing those references, but every changed hull and bottom cut is still independently audited numerically.90cut heights ontrial000 produced no110; most deepercuts exceededE249.
- stable_pair_retirement_mass.py: literally removes two reference-stable support rows and adds a horizontal lower plane, then solves an upward-apex first-moment closure when possible.360finite candidates from6ownpruned seeds, no110. Some new numericown211 atE211 occur; this is not a goal and is not being exactly frozen.

The analytic smooth construction and convexity proof remain in TWISTED_LATITUDE_ANALYTIC_20260930/construction.md. They are not polyhedral success evidence. The old cyclic helper's absent-axis substitution was explicitly removed before reuse; it now fails withValueError.

Current goal-directed branch: reference_mass_curved_flow.py and artifacts/C430-curved-actual-mass-closure-20260930b. It starts from our own saved reference110E215body, actualown33/40 and |g|/R=.0864089178. Unlike the earlier straight-ray mass constraint Dg*d=-alpha*g, this minimizes |g|/R while allowing transverse centroid changes. It uses the modern full physical contact retraction, dimensionless LP/QP rows, and strict reference110/noncontact/volume checks. ActualownS/U are independently recomputed and are the ONLY candidate gate. The initial attempt hit a missing derivative on a derivative-free retracted state; fixed by computing scalar centroid/volume directly, preserving failed log and starting explicit b-run. No physical result was accepted from that failure.

Sharedlocal DISCOVERIES checked through22:23UTC solely for a qualifying update; none reported. No peer follow-up was requested. NoVPSaccess. Nativegoalactive,noownerblocker,noqualifyingFigure.

## 2026-09-29T23:48:24.574676+00:00 Explicit monostable families and direct free-support search
The curved reference110 mass continuation ended at E211 with actualS34/U40 and normalized centroid distance .0863262649643. Twelve mass-neutral reference chamber excursions also failed to close the actual centroid. These are finite failures, not a Figure; no new exact partial audits were made.

Public primary source consulted locally: Tancredi Schettini Gherardini, An explicit mono-monostatic polyhedron, arXiv2609.07827v1 (7Sep2026), https://arxiv.org/html/2609.07827v1. Article, provenance, GitHub tree and four small Reshetov benchmark source/data/certificate files are saved in sources/schettini_2026_primary. Repository pinned at72aabdb1dc4ab5a42c0cb9b51189778e0b82dfce. The author claims a much larger explicit example (F56946,E170832,V113888); it does not meet this goal. Reshetov14 is merely an own121 construction seed. Full exact source hashes are in reshetov-source-manifest.json. No claimed paper result was substituted for same-body verification.

A union of polar sets whose every nonroot has a strict positive arrow to a common root retains referenceS1. With C2 symmetry and root q*=(0,0,-1/h), the allowed root height is h<min(-qz/|q|²) over sinks of the nonroot set, provided their z<0. Actual uniform mass closure is then a single lower-plane height equation, followed by independent complete hull boundary integration. New code rotated_monostable_intersections.py and translated_intersection_mass.py. Finite2500 top escape-ball completions,480 translated intersections,20 compact-parent cyclic intersections, and two physical affine Reshetov campaigns all failed110. No exact audits of the nonqualifying endpoints were done.

centred_polar_spiral.py constructs39 strict polar escape-chain pairs plus an extra top-plane pair and a root,81 total supports.6000 finite samples completed;388 admitted this scalar own-centroidS1 closure, none own110. polar_spiral_direct_optimization.py now directly searches the9shape parameters and checks intermediate mass-infeasible height-limit bodies at their OWN centroids too. Current output artifacts/centred-polar-spiral-own110-opt-20260930. Objective reductions still leave many unstable equilibria.

polyhedral_slab_mass.py represents horizontal cross-section area by a quadratic in each height slab and integrates volume/first moment in closed form numerically. Its coefficients are search floats, not an exact certificate. Three independent cut-hull checks in artifacts/slab-mass-closure-check-20260930.json gave max volume discrepancy1.07e-14 and centroid5.55e-17. Every accepted candidate is independently rehulled and reintegrated.

New direct free-plane method free_centred_polar_flow.py allows119 individual C2 support coordinates to change and rebuilds the genuine hull after every proposal. The bottom mass-closing plane is implicitly differentiated, retaining the same physical body in all derivatives. Independent objective directional check error1.36e-9. artifacts/free-centred-polar-own110-20260930 reduced Pmax from.50278 to~.49597 while preserving ownS1; still U27, not a nomination. It hit the strict mass-height search margin. Further work is directed only toward a qualifying actual body. No peer replays/exchanges, no VPS checks, no blocker, goal active.

## 2026-09-30T00:12:13.691304+00:00 Dynamic hulls, direct chains, and common projective embeddings
No qualifying Figure has been found and no new exact nonwinning body was audited. The81support polar spiral DE completed46202calls; bestP objective.5123541747, not110. Its free-plane ownS1 continuation stopped at the scalar height-margin boundary with manyU.

free_cyclic_actual_flow.py permits actual S and U changes, retains literal C2 symmetry and the prospective4plane axialstar, and rebuilds the true hull after every proposal. Full same-body derivative checks: persistence directional error7.19e-9, angular capacity2.73e-7. Three finite runs (bars, capacity, prescribed axial roots) all failed110. The bar endpoint had77S/83U; a low objective was explicitly not a census claim. Prescribed axial root mode rejects a missing actual axial carrier instead of substituting a different vertex.

free_primal_goal.py uses freely moving physical hull vertices, with a full maximal-facet/true-edge rebuild and fresh uniform mass every proposal. V<=84 guaranteesE<=246 for these inputs. Directional errors from the exactC162 input were7.00e-10 for bar sum and6.15e-9 for angular capacity. Angular and explicit radius-squared capacity variants both ended with extra roots; no exact partial audit was started. bottleneck_capacity.py now exposes the named normalization parameter; its existing angular default is unchanged. The raw variant is a search residual only, and actual counts remain the acceptance criterion.

New live direct construction families:
- two_branch_polar_goal.py: two independent20-orbit C2 polar chains, common stable root, and a4plane top completion at the ACTUAL maximum polar z. At most83supports andE<=242. The root-plane height solves actual mass whenever the strict sink bounds admit it. artifacts/two-branch-polar-own110-20260930.
- primal_chain_mass_goal.py: the dual geometric idea applied to actual physical points,40orbit chain pairs plus a bottom completion and a moving positive axial apex, at most83vertices. Nonroot positive-z sinks impose r>max(|p|²/pz). Raising r then solves the uniform first moment; oriented tetrahedra provide the scalar root, independently checked by the maximal-facet integration. Artifacts/primal-chain-mass-own110-20260930. This produces ownU1 but still manyS; no success yet.

reference_projective_goal.py searches ONE physical map y=A x/(1+b.x), detA=1, dualA^-T(q+b), then integrates that same physical solid and translates by its own centroid. Positive denominators preserve the existing true incidence. Projective mass centering for our reference110C430 source found b=(-.00534677958,.06049908822,.24161470114), but reference equilibria do not transfer. The first raw local-arrow score was minimized by a severely elongated own22 body with actualP~.9999,Q~.9916; this finite failure demonstrates why residual size is not near-success. A separate bounded persistence objective endedC430 with64S/39U andP,Q~.0594.

The full global persistence search applied directly to our exact-sourceC474 body instead found a distinct moderate common projective image with shallow P and Q~.0027 but dozens of roots. This is not a Figure and was not exactly frozen. Current direct goal step: projective_cancellation_goal.py re-encodes that single physical embedding in a balanced complete contact chart and attempts one fewer actual stable or unstable root at a time, with full physical retraction and independent census. It only adopts a lower total root count within an explicit maxbar.03 search chamber, and immediately preserves any actual110 regardless of that chamber. artifacts/C474-projective-individual-own110-20260930.

Finite end records available now:
```json
{
  "centred-polar-spiral-own110-opt-20260930": {
    "calls": 46202,
    "best": 0.51235417465312,
    "seconds": 1197.4736161231995,
    "scope": "Finite direct search; no qualifying body found"
  },
  "free-centred-polar-own110-20260930": {
    "iterations": 50,
    "best": 0.5082089853827884,
    "minU": 17,
    "seconds": 11.59546709060669,
    "scope": "Finite numerical direct search; no qualifying body found"
  },
  "free-cyclic-actual-bars-20260930": {
    "iterations": 900,
    "best": 0.44326516517917525,
    "seconds": 220.9722511768341,
    "scope": "Finite numerical direct search ended without a qualifying figure"
  },
  "free-cyclic-actual-capacity-20260930": {
    "iterations": 144,
    "best": 22.148729731045798,
    "seconds": 53.8980872631073,
    "scope": "Finite numerical direct search ended without a qualifying figure"
  },
  "free-cyclic-axis-goal-20260930": {
    "iterations": 169,
    "best": 36.44415052048171,
    "seconds": 63.5255560874939,
    "scope": "Finite numerical direct search ended without a qualifying figure"
  },
  "C162-free-primal-capacity-20260930": {
    "iterations": 306,
    "best": 6.291556110800192,
    "seconds": 20.750762939453125,
    "scope": "Finite direct same-body search; no qualifying figure found"
  },
  "C162-free-primal-raw-goal-20260930": {
    "iterations": 85,
    "best": 3.367938140543057,
    "seconds": 5.464329957962036,
    "scope": "Finite direct same-body search; no qualifying figure found"
  },
  "C430-reference-projective-own110-20260930": {
    "calls": 82354,
    "best": 0.00020000493509654102,
    "seconds": 16.528892993927002,
    "scope": "Finite physical projective search ended without a qualifying own110 body"
  },
  "C430-projective-persistence-own110-20260930": {
    "calls": 120966,
    "best": 0.1053482742458239,
    "seconds": 87.42170691490173,
    "scope": "Finite physical projective search ended without a qualifying own110 body"
  },
  "C474-projective-global-own110-20260930": {
    "calls": 120680,
    "best": 0.006626230787901849,
    "seconds": 98.4052038192749,
    "scope": "Finite physical projective search ended without a qualifying own110 body"
  }
}
```
NoVPSchecks, no newpeerreplays/exchanges, noownerblocker. Goalactive.

## 2026-09-30T00:37:13.452495+00:00 Individual root paths and negative self-polar construction
Still no qualifying own110. No exact audit of a new partial candidate was performed. C474 common-projective image ended numerically53S/40U with maxP=.0027086900,maxQ=.0027090802 after120680objective calls. Individual cancellations reduced93total roots to36 before the explicit maxbar.03 search boundary. The alternate-target continuation then reduced this to own33 atE237 withPmax=.09331466547,Qmax=.07165269332; all four remaining unwanted-root trials failed to reduce the census. These are actual numerical census changes, not a result satisfying the goal.

New explicit numerical methods in contact_forest.py: optional excluded_roots identifies the specific equilibrium to remove; the primary global maximum cannot be silently substituted if excluded. Optional hard_side requires one allowed root on that side and zero LP slack there, plus complete nonlinear readback. Optional Armijo acceptance compares actual progress with predicted progress instead of requiring a fixed relative objective decrease. All existing defaults remain explicit and the same. A controlled Armijo comparison on the blocked primalroot129 produced only~1e-8 residual reduction and still33; it did not solve that barrier. No mathematical exclusion is claimed.

The primal escape-chain DE completed36490calls, bestobjective.4340988453,minS3, no110. A separate physical contact source withV83/E242/F161 own27/1 was released for direct root cancellations. Seven soft trials created extra tiny-bar unstable roots without any adopted result. Verified own process72175(cwd/stdout/argv checked) was stopped with STOP_CHECKPOINT.json; all trials preserved. The explicit hard-U1 comparison tried12different stable targets, preservedU1 but cancellednone. This establishes only those finite failures.

Literal carrier retirements from the new C474 own33 state: deleting primal74 ->E236own75; deletingprimal129 ->E238own12/6; deletingpolar29 ->E236own96; deletingpolar5 ->E236own10/4. Every hull/mass was rebuilt. Projective mass-centering of these changed bodies was also checked and did not produce110. Direct new-complex continuation is running at artifacts/C474-retired-carriers-own110-20260930 (casesP129,P74,Q29,Q5 sequentially). No old equilibrium claim transfers across deletion.

New scientific family: negative self-polar body P=-P^polar, so the two reference escape landscapes are isometric. Own proof and primary-source discovery links in artifacts/SELF_DUAL_CONE_BRANCH_20260930/derivation.md. Jensen arXiv1902.00784 and Gouveia/Lourenco arXiv2207.11747 are background sources; direct SIAM HTML download returned403 and that fact is recorded. No claim of a monomonostatic theorem from these sources.

Paired add-and-cut: choosev violating onlythe facet indexed by oldvertexw, then stackv beyond that facet and cutw byv.dotx>=-1. The regions are disjoint and the operations commute; negative polarity swaps them, giving a new self-polar polyhedron. Vertex coordinates are the literal retained points, v, and edge-cut intersections. V=F,E=2V-2,soV<=125fitsboth complexity readings below500. A common O4 rational projective section transformation is used to solve the actual uniform centroid. selfdual_pair_goal.py checks true hull self-polarity and independent mass; after two necessary construction intermediates all equilibrium search is atC>=34. artifacts/selfpolar-paired-own110-20260930 is running160trajectories; initiallyminimumcount4/4, not a figure.

selfpolar_mass_flow.py now deforms ALL existing physical vertex coordinates while retracting every symmetric contactx_i.dotx_j=-1 and the actual3component uniform centroid. The tangent dimension is computed from the full contact/mass Jacobian with rank failure explicit. Numerical proposals must keep strict noncontacts and pass a freshly rebuilt negative-self-polar hull identity; only actualS=U=1 nominates exact verification. Current artifacts/selfpolar-contact-mass-own110-20260930, sourcebody copied locally before optimization. No independent-metric relaxation or omitted physical embedding.

Goal active, noownerblocker, noVPSaccess, no newpeerreplays ormessages.


## 2026-09-30T01:20:56.733053+00:00 Literal C2 mass closure and topology escape
No qualifying own110 body has been found. Goal remains active; no blocker. No new exact partial audit, peer replay/message, browser use, or VPS check.

Completed single-cap C2 search: physical diameter-ball additions plus axial-apex uniform mass closure reduced own27/1 to15/1 atE248. Explicit C2 orbit exchange then reduced this to5/1 atE248. Complete fresh numerical maximal hull and volume integration were used, not integration triangle counts. Main source: artifacts/primal-cyclic-exchange-own110-20260930/round01/best.npz; finite search340.04s,3rounds. Actual remaining stable carriers are one horizontal bottom facet plus two off-axis C2pairs. The largest polar bar is.4924702954, so this is not a near-zero residual claim.

New cyclic_facet_coarsening_goal.py projects literal adjacent triangular patches and their C2mates into planes, recloses actual mass by the apex, and accepts only fresh true-edge decrease with U1 and no stable-count increase. One paired patch reduced E248 to246 (V85,F163,C492), still5/1. Secondroundfailed. Source and full trials: artifacts/cyclic-planar-coarsening-own110-20260930. Numerical coplanarity is a nomination only; no exact facet certificate asserted.

The separate free C2point/implicitmass flow completed1600steps,483s, still13/1,E248,Qmax.47728337. HardU1guard reached~1.6e-8. It did not approach110 by census.

New next step: cyclic_paired_cap_goal.py adds a target cap and a lower countercap simultaneously as literal physical C2pairs, both with strict reference escape witnesses, then recomputes all sinks after any explicit orbit deletion and solves actual uniform mass. This is uniform geometry, no point weights. It is running on the earlier own3/1,E194 chain body and on the new own5/1,E246 body. The smaller source is used for its larger available edge budget; only own110 will trigger exact verification. A single-cap control on own3/1 is also running.

Earlier carrier-retirement continuation finished allfourcases without110; Q5 reachedown2/2 atE236,Pmax.08194060,Qmax.10973722. Guard conditioning plus direct110 correction endedown8/9 at a genuine numerical contact boundary. Its minimumedge[46,145] is2.25e-14. Those two literal vertices were explicitly contracted, freshhull V147/E235/F90,own8/9. Rechartdeviationchecked<1e-8; direct rootcancellations on this NEWcomplex have restoredown2/2 and are testing the two deep remainingroots. Source artifacts/C470-contracted-boundary-own110-20260930; no old equilibrium claim transferred across contraction.

Negative self-polar family finished160trajectories,1367.66s, minimum4/4. Full self-polar contact+mass flow ended5/5; derivative checks contact2.10e-10,actualcentroid7.63e-11,escape2.13e-8. Releasing all self-polar constraints in six finite fullcontact trials didnotcancelaroot. Common physical projectivecensus search reached2/2,E186 after142005calls,133.3s, withP/Q~.684/.682. All are nonqualifying; no impossibility theorem inferred.


## 2026-09-30T01:47:46.431739+00:00 Asymmetric mass closure, strict coarsening, continuous shortest-path escape
Goal active, no qualifying figure, no owner blocker. All new work local in agent-1; no VPS/browser, no new peer replay or communication, no new exact nonwinner audits. Inbox/shared feed checked at this natural checkpoint; no newer goal discovery was present (shared feed still22:23UTC).

C2 joint physical countercaps: artifacts/cyclic-joint-caps-three-own110-20260930 ended6rounds378.81s, still3/1 atE248 withQmax.64782544; the own5/1 branch endedonefailedround75.23s. Single-cap control on the3/1 body ended11rounds,still3/1 atE248,Qmax.64261886. No disappearance inferred from changing local residuals.

New asymmetric_apex_mass_goal.py adds ONE literal physical vertex at a time, optionally explicitly retires an oldvertex, and solves all three components of uniform volume centroid by moving the existing apex. The analytic apex-centroid derivative matched independent finite difference to9.45e-12. All escapes and actual maximal hulls are rebuilt. Three-root branch endedV79/E230/F153,own3/1,Qmax.72683545 after19rounds106.65s. Five-root branch endedafter2rounds73.89s, still5/1,E249. Neither qualifies.

A separately named projective closure deforms the entire SAME physical body by y=x/(1+b.dotx) with positive denominators. Its centroid derivative is -(5E[xx^T]-4gg^T); finite difference error8.37e-12. In24rounds241.24s this asymmetriccap branch removed one stable equilibrium and endedown2/1,E243,Qmax.71686434. Captured earlierround18body is alsoown2/1,E243. The large remaining bar is not close-to-zero. Five-root projectivebranch ended2rounds24.80s,still5/1,E249.

New free_apex_mass_goal.py frees all asymmetric physical vertices (<=84) and eliminates the apex coordinates using the actual uniform-centroid equations and their full implicit Jacobian. Dynamic maximal hull is rebuilt, U1 is a hard nonlinear admission, and small generic contact release is explicit. Local polar escape objective ended35iterations12.13s at2/1,E243,Qmax.71758257. Capacity variant ended~42iterationsat3/1,E240,Qmax.71734009. Neither qualifies; local margin reduction didnotcancelthedeepbasin.

radial_cyclic_family_goal.py explored a literal radial deformation with planar anisotropy and fresh bottomquadcompletion. It remainedown3/1; last saved improvementcall35371,Qmax.81098129,E194. Own process81597 was verified by argv,cwd,andstdout,then stopped after~13minutes; STOP_CHECKPOINT.json preserves all identity and bestbody data. Last saved improvementcall is explicitly not totalexecutedcalls. This ends onlythat finitebranch, notthegoal.

New strict_equilibrium_coarsen_goal.py starts from this agent's improved acceptedC622geometry (artifacts/own110-maximin-20260929/latest-strict.npz; chart contact-baseline622-balanced). It shortens true primal/polar edges with BOTH own equilibrium classes hard, explicit normalizedvolume floor, then re-realizes candidate topology and admits onlystrictown110withreducedE. Overbudgetown110 is never a goal nomination. Straight variant's firstedge[131,132] shortened.03514167 to.03188212 withoutacontraction in180steps. It is trying otheredges. A separately declared predictor-corrector adds minimumL1physical correction of nonlinear escape drift while requiring edgeprogress; firstedge reached~.027 after30steps,stillE311. Both ongoing; no newedgecountclaim. No exact audit willbe spent onoverbudgetintermediates.

Scientific scoring change: shortest_escape_forest.py computes Dijkstra on nonnegative costs max(epsilon-angular_escape,0), WITHOUTaddedhopcost. Parentpointsarealreadyfinalized,sozero-costtiesremainacyclic. Sumofshortestrootpathcosts equals the sum of tree-edge deficits weighted by the number of descendant starts. That is a continuous objective forfixedrootset; LP retains the hinge of everychosenedge. ContactModel now has explicit merit='shortest' and escape_floor, with corrector enforcing exactlythe same epsilon. No defaultmethodchanged. Independent SciPy sparse shortestpaths agreedexactly in bothlandscapes; scalarphysicalmerit finite-difference error5.72e-6 on derivative212.7932 atstep1e-8. Largerstepschangeactivepaths, as recorded. Complete own derivation and validation: artifacts/SHORTEST_ESCAPE_METHOD_20260930. Localrouteidea informed by sources/full76/README.md; descendant-weighted continuousobjective is this agent's extension.

Main direct new search: artifacts/C474-shortest-path-own110-20260930, input own53S/40U atE237 withP/Qmax~.002709 from this agent's saved common physical projectivebody. Full actual-mass1/1correction,eps2e-8,1600steps,Armijo,physicalcontactretraction. Source chart is artifacts/C474-projective-individual-own110-20260930/chart. Anyactual110proposal is now saved immediately in contact_forest.correct BEFORE objective or hard-margin filtering; exactcompletehull/centroid/weak audit remains mandatory.

Live sessions atthischeckpoint: strict uncorrected22337,strict predictor-corrector43343,new shortestpath31716. Others mentioned above are finite. No qualification or weak000claim fornewnumericalcandidates.
