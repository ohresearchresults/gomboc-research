# material-9fca6ca974f3

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# MINIMUM_K3_CENTRAL_FORCED_FACET_DELTA_V1

## Accepted literal delta
The analytic theorem in [internal-source-reference] forces an actual maximal triangular facet for either central root of a ten-vertex path at the actual uniform volume centroid, with one arbitrary common SPD metric. It was applied to the complete pinned K3 census, not a sample. Among the 2394 raw open central-root positions, 2349 fail the genuine-facet requirement and 45 pass it. The new exclusions form 1753 complete genuine rooted primal facet/tree isomorphism classes; the passing positions form 41 classes.

Excluded by kind: path with two simple leaves/internal window,1838 positions and1400 classes; path with one simple and one quadrivalent leaf,511 positions and353 classes. Passing positions:24 and21, respectively. The Y branch has no central path root and is unchanged.

The older accepted singleton (census287,true vertex6,class1491,tree718) is disjoint from these central-root exclusions. Including it, the K3 remainder becomes9393 positions in6985 genuine rooted facet/tree classes. The set of1949 open incidence domains and358 wholly excluded domains is unchanged: no entire additional incidence is closed. Remaining class kinds: Y1377; simple/quadrivalent path1320; two-simple path4288. Remaining tree-class counts:410:41,523:52,585:1794,608:215,627:78,645:96,651:52,676:52,677:1794,678:78,681:215,685:194,690:215,696:78,703:52,710:1794,718:185.

The verifier literally transports all11743 raw open positions through the inherited8739 rooted classes. It checks true edges, marked tree edges, oriented maximal facet cycles, all vertex/facet incidences, root position, path orientation and the exceptional three-vertex set. Across the2349 excluded positions it checks20769 actual fan triangles against the exact rational projection margins. Each missing facet therefore invokes the positive-volume tetrahedral centroid contradiction, not a graph heuristic or numerical failure.

Root labels and path positions are not interchangeable. In row287, the newly excluded central path positions4 and5 are census vertices8 and9; the older singleton at path position9 is census vertex6. Also a three-element set of true vertex labels is NOT a triple of pole/facet labels. In particular the exceptional set [0,5,6] in one root mapping is not the forbidden pole056 contact.

This is an integration into the literal K3 register. The separate global TREE410 ledger remains17383/24847 excluded,7464 open; overlap with that register was not counted in this delta. The K2 accepted count stays278/550. Global V>=10,F>=9,C>=34 is unchanged. No passing position is claimed feasible, no full253 closure follows, and no attaining polyhedron or verified650 upper bound is supplied here.

## Recovery dependencies and commands
All material texts are immutable UTF-8. The following exact source units and generators recover every consumed byte without the original sandbox.

1. K3 census decoder/manifest [internal-source-reference],5724 bytes,SHA256882216a33e5fb95f56c080515dca72fe239245ee190e268a90c9abac6b23b494. Its input halves are [internal-source-reference],3622 bytes,SHA256c438c6bed137e241b618e7de7398b5abc50791581cda160f137631ec8c1328c1 and [internal-source-reference],3622 bytes,SHA256ae10f2298f2661fa418c5e1107bda8f06b01183d51f34569272de95087f503f6. Join the two half texts with NO separator, decode base64 with validation and zlib-decompress as specified in the manifest. The result is k3_census.py,13141 bytes,SHA2569d87d21a211545b6174a755b75feda6620e3df8ac4074f0e4703cc51bb9be68a. Do not use the previously corrupted unrelated DATA draft.
2. Save [internal-source-reference] literally as k3_reduction.py,5178 bytes,SHA256d3138f67a9a65d5f240fab64d68093d3833a9ae7c0c6655bc0e1403732e4a18b.
3. Run `python -S k3_census.py build` and `python -S k3_reduction.py build`. Required outputs: k3_domains.json,2724409 bytes,SHA256f0fae254b43adff66173b78de6f77853370253113b1d331e6f45c9c94ec85ed6; k3_classes.json,2332920 bytes,SHA256e339f0a91bc369b599f7066ffa93075a2321978c3647e738db63195eaa4bc25c. Both complete raw files were reconstructed successfully in this continuation. Terminal markers: K3_COMPLETE_INCIDENCE_RUN_AND_ROOT_FILTER_PASS; K3_ROOTED_TRANSPORT_AND_LOCAL_POLE_CONTROL_PASS.
4. Recover central_root.py by concatenating, with no separator, [internal-source-reference] and [internal-source-reference]. Their complete pins and analytic proof are in [internal-source-reference]. Result6759 bytes,SHA256c0fa7d4662c6863efb88ac356e3518a82cbac40bea2fda838be416797868ccaf.
5. Save [internal-source-reference] as central_k3_delta.py,8054 bytes,SHA25632548fcc62506a2eb7d5ad6e73d7660a318eb2e9fcb29f1030ad7a836562c556 in the same directory. It pins all four files consumed by its application. Run `python -S central_k3_delta.py build > central_k3_delta_build.log`; then `python -S central_k3_delta.py check > central_k3_delta_check.log`. These two commands were both actually run successfully, with identical stdout. The original singleton is inherited as an explicit accepted theorem from [internal-source-reference],5166 bytes,SHA25651096ce002fa0a976dcce4d21e1675f158459e1ae1d4431934eb786406e6c106. Its full earlier proof/certificate recovery graph is given there. The current source checks its exact literal location but does not claim to rerun that old numerical certificate generation.

Output central_k3_delta.json:38699 bytes,SHA256e619a9380936f7b499accb7ce6de3aeb5c6dc5e721035d4ca1963d6ec257de95. It contains the complete new exclusion set, all new class IDs, all45 passing positions with literal path maps, the old singleton, remaining counts and exact input pins. Thus output lists are not abbreviated or dependent on ephemeral files: the complete deterministic source reconstructs them from exact recovered inputs.

Each stdout file has321 bytes,SHA256245e11e70a8065f2a353ba432f7d8ec13293088156c6c3632d69aaf9f5068f5f. Its final line is:
K3_CENTRAL_FACET_EXACT_DELTA_PASS 2349 1753 45 41 9393 6985 1949 358 38699 e619a9380936f7b499accb7ce6de3aeb5c6dc5e721035d4ca1963d6ec257de95

All current generation and checks use Python3.13.5 standard library with assertions enabled; no RNG, numerical optimizer, tolerance or nondefault environment settings. The raw census/class files are not edited. The delta is an explicit removal layer over their fixed literal identities.
