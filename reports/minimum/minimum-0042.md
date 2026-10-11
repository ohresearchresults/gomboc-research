# minimum-0042

Historical AI scientific report · saved 2026-09-10 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# C32_ELEVEN_FRAME_JOINT_ROOT_EXCLUSIONS_AND_UNIQUE_MATCHING_V1

## 1. Determination

**New complete continuous root exclusions and a reconstructible joint frontier were obtained.** Relative to the assignment's accepted 17 whole types and eight partial unstable-root orbits:

* **11 additional unstable-root orbits are excluded without assuming S=1.** No homogeneous realization at its ordinary volume centroid, in any positive-definite metric, can have that orbit as its sole strict unstable vertex.
* **66 additional unstable-root orbits in total, including those 11, and five complete stable-root orbits are excluded for the strict (S,U,H)=(1,1,0) target.** The other 55 unstable-root exclusions are conditional on the joint target; they are not unconditional U>=2 theorems.
* **7,805 additional joint (U,S) automorphism orbits are excluded. Exactly 12,954 joint-root orbits remain**, across all 279 types outside the accepted 17. **No new whole type is excluded.**

The surviving complete sign-graph cover has **87,519 coupled primal/pole graph orbits** and **23,640 distinct compatible matching branches**, after actual vertex/facet automorphisms and duplicate broom labelings are removed. These are outer sign-domain covers, **not physical realizations**.

A further whole-domain consequence is new: **every putative homogeneous strict C32 target has exactly one sign-compatible complementary primal/dual matching.** Both permitted primal trees were enumerated before obtaining uniqueness. It is a conclusion of the complete incidence/sign intersection, not a preassigned-complement premise.

No C32 attainer, C>=34, F>=10, or V>=10 is claimed. The earlier proper four-triangle negative-minor counterexample is retained as an exact physical regression control.

## 2. Authority and inherited inputs

The full literal parent `minimum-0040`, `NOVA24_F9_11_SHADOW_FRAMES_V1`, was read and authenticated. Its compact version-2 envelope is **45,178 bytes**, SHA-256 **`2cd8dc8ea75a5a8d1eaa9fabfca75a65181325fab676cd95dec5cd1c16426a59`**. Exact authentication: extract the unique title-through-EOF Markdown from the supplied journal, append one LF, and serialize `{'version':2,'result_markdown':md+'\n'}` with `ensure_ascii=False,separators=(',',':')`. The supplied journal itself is 3,407,881 bytes, SHA-256 `ea13f43e8a98a505205a90ba7be96a304d228bee26920202f56f4851be7ef602`.

OJ supplies the 11 frames and their 25 base-tree-labelled subgraphs, including all weak shadows. Its five TREE ordinals are not catalogue IDs. Its old matrix certificates were **not rerun** here. The parent explicitly finds that its reciprocal counterterms are inessential to those certificates; this handoff makes no contrary coupling claim. No source/alias conflict was found. :contentReference[oaicite:0]{index=0}

Three inherited inputs are used distinctly:

**Actual-mass primal theorem.** With nine actual vertices and unique strict unstable vertex, the vertices can be labelled so that the weak escape tree is

```text
T     = (0,0,1,2,3,4,5,6,0),
T_alt = (0,0,8,2,3,4,5,6,0).
```

The analytical primal parent is `minimum-0032`, SHA-256 `3c4347c3beb52ca549da23ff0b0eb42a85251a52c2a920bbf1deb68b4b73fe4d`; its later completed coordinator recovery remains a separate inherited verification, not a replay claimed here. There are eight required nonnegative shadows of T; the only additional possibly nonnegative unequal pair is 2->8. All other 63 pairs are strictly negative. Facet 567 is an actual maximal triangle. The alternative tree is usable only when 28 is a true edge and its escape has the needed sign. These statements come from the journaled actual-moment theorem and its redirection consequences, not from new independent masses. :contentReference[oaicite:1]{index=1} :contentReference[oaicite:2]{index=2}

**Actual matching theorem.** Every strict target has some complementary pair of strict true-edge escape trees. Individual zero primitives at nonequilibria are allowed. An arbitrary prescribed complement need not work. :contentReference[oaicite:3]{index=3}

**Canonical catalogue.** The accepted 296-map catalogue was recovered and rerun, including its independent completeness/orbit checker. Its 240,929-byte JSON reproduces SHA-256 `efb10a4657a891cd13f6f62db94164bd4b3005e908dc55aae87db450930f704d`, with 21,682 joint-root orbits. The complete recovery source is included below; no unavailable catalogue or alias is required. :contentReference[oaicite:4]{index=4}

The accepted whole set remains the inherited set `{33,34,72,139,149,152,159,163,164,178,192,217,284,288,293,294,295}`. The prior partials remain `35/U3,45/U3,47/U3,49/U3,51/U3,53/U3,282/U0,290/U3`. The unpersisted 7954 transfer, late57 claims, and failed earlier matching assignment are not inputs. :contentReference[oaicite:5]{index=5}

## 3. Exact new exclusions

All labels below are **accepted canonical map labels**. U and S denote vertex and facet automorphism orbits, respectively. Joint-root representatives are lexicographically least `(u,s)` under the same map's full vertex automorphism group and its induced facet action. There is no polarity quotient.

### Unconditional unique-U exclusions

```text
40/U3   50/U3   102/U3  108/U3  109/U3  113/U3
114/U3  137/U3  191/U3  240/U3  260/U3
```

For each, the exhaustive list of actual-edge broom embeddings with genuine terminal triangular facet is empty at that root orbit. This proves the stated unique-U exclusion without the pole theorem, S=1, matching, or any metric restriction beyond positive definiteness. It does not exclude having a unique unstable vertex in another orbit of the same map.

### Complete joint-target unstable-root exclusions

The following **66** pairs are new relative to the accepted register; the preceding 11 are included, not added again:

```text
(0,7),(2,6),(3,7),(5,7),(7,8),(9,8),(13,8),(14,8),
(16,8),(20,1),(24,8),(25,0),(26,8),(29,8),(40,3),(50,3),
(62,8),(67,1),(73,8),(74,1),(81,1),(97,1),(102,3),(108,3),
(109,3),(113,3),(114,3),(115,7),(119,7),(121,0),(121,6),
(122,8),(127,8),(128,8),(131,3),(131,6),(137,3),(147,5),
(161,3),(162,3),(174,3),(174,5),(175,3),(177,7),(179,6),
(179,7),(180,8),(191,3),(193,8),(194,7),(195,7),(196,7),
(197,8),(199,8),(209,8),(215,8),(216,3),(229,3),(240,3),
(255,8),(260,3),(265,8),(266,5),(276,0),(276,1),(278,0).
```

Each excludes **all stable-facet choices** for the target at the specified unstable orbit. The five new stable-root exclusions, each covering **all unstable-vertex choices**, are

```text
22/S8, 57/S0, 73/S5, 76/S4, 126/S4.
```

The 66 U-root and five S-root closures are overlapping projections of the same joint exclusions, not additive counts. The complete joint partition is

```text
21,682 = 868 prior whole-type orbits
       + 55 prior partial-root orbits
       + 7,805 newly excluded joint-root orbits
       + 12,954 remaining joint-root orbits.
```

The generators emit every member of the 7,805 and 12,954 lists and every canonical map, oriented facet cycle, true edge, automorphism and label transport. These lists are outputs of the inline source, not missing irreducible inputs. All 279 previously unclosed whole types retain a graph-level case.

## 4. New geometric tests and full proofs

Let P have ordinary centroid zero, actual vertices x_i, and actual facet poles q_f satisfying q_f.x<=1. Fix **one** physical M>0 and N=M^-1. Write

```text
D_ij=x_i^T M(x_j-x_i),   A_fg=q_f^T N(q_g-q_f).
```

G and H are their complete nonnegative unequal-pair graphs. An absent arrow means **strictly negative**, not unspecified. The tests below apply to an arbitrary interior reference; actual ordinary mass enters through the inherited primal and pole graph restrictions. Applying the tests to the polar uses its actual incidence and N, **not its own volume centroid**.

### 4.1 Linear-functional cuts

For each actual vertex i put `S_i={j!=i:D_ij>=0}` and `f_i(x)=x_i^T M(x-x_i)`. Necessary conditions are:

1. The true graph induced by S_i is connected when nonempty; the graph induced by its strictly negative complement is connected.
2. The nonnegative incident edge rays form a cyclic interval in the vertex link, and at least one incident edge has strictly negative score.
3. On every maximal facet, the nonnegative vertices `{i} union S_i` form a cyclic interval.
4. On a facet containing i, if both boundary neighbors of i belong to S_i, every other facet vertex belongs to S_i. If neither boundary neighbor belongs to S_i, no other facet vertex does.

**Proof.** A vertex which is not a maximizer of a linear functional has a strictly increasing incident edge: otherwise the edge-generated tangent cone would make it a global maximizer. Increasing edge paths from nonnegative targets reach the connected maximum face, avoiding i once the value increases above zero. If the maximum is exactly zero, its exposed face contains i and S_i; deleting i leaves a polygonal path or a single edge endpoint, hence connected. Strictly negative vertices similarly descend to the connected minimum face. The functional is nonconstant because x_i is nonzero and M>0.

A positive section of the tangent cone is a convex vertex-figure polygon. A linear half-plane cuts its cyclic vertices in one interval; the same applies to every actual facet polygon. Since zero lies inside P, `-x_i` is a nonnegative combination of incident edge directions, and its score is `-x_i^T M x_i<0`; at least one incident score is negative. Finally, every other vertex direction in a facet's tangent cone at i is a nonnegative combination of its two boundary edge directions. This proves the two saturation assertions. Supporting-line equalities and zero scores are included throughout.

An immediate useful consequence in the inherited broom labels is

**if 28 is a true edge and D_28>=0, then 128 is an actual maximal triangular facet.**

Indeed the only nonnegative targets from vertex 2 are 1 and 8. The two positive-or-zero rays must be consecutive in its link; their common facet cannot have a fourth vertex by saturation. This claim is deliberately conditional on 28 being a true edge. The optional nonedge shadow 2->8 remains explicitly represented in the enumeration.

### 4.2 Triangle-chain projection and its dual

For a true triangular facet `(a,b,c)`, assume `D_ba>=0`, `D_cb>=0`, and `D_ca<0`. Its unique positive adjacent pole escape is across true edge ac; its escapes across ab and bc are strictly negative.

**Proof.** Work after the physical square-root transform, so the metric is Euclidean. Put `y=x_b`, `u=x_a-x_b`, `v=x_c-x_b`,

```text
A=D_ba>=0, B=D_cb>=0, C=-D_ca>0,
a0=u.u, b0=v.v, u.v=-(A+B+C), Delta=a0*b0-(u.v)^2>0.
```

The plane foot is `p=y+alpha*u+beta*v`. Solving its two orthogonality equations gives

```text
alpha=[b0(B+C)+(A+B+C)B]/Delta>0,
beta-1=[a0 B+(A+B+C)(B+C)]/Delta>0.
```

Thus its barycentric signs at a,b,c are `(+,-,+)`. For the neighboring maximal facet g across ac, strict nonincidence gives `q_g.x_b<1`, and

```text
q_g.p-1=(1-alpha-beta)(q_g.x_b-1)>0.
```

Since `p=Nq_f/(q_f^T Nq_f)`, the pole escape is `(q_f^T Nq_f)(q_g.p-1)>0`. The other two sides have positive missing barycentric coordinates and therefore negative escapes. This proves the assertion with weak A or B equality. The same proof applies to triangular facets of the actual polar with reciprocal metric. The source applies it on **both sides**, recording every strictly positive implication.

This is the inherited terminal-foot calculation applied systematically to every genuine triangle, not a claim that the terminal triangle contributes an extra equilibrium. The original terminal escape through 57 is preserved. :contentReference[oaicite:6]{index=6}

### 4.3 A root-facet domination obstruction

A strictly stable facet cannot have a vertex adjacent to every other facet vertex in the **undirected complete nonnegative shadow graph**. In particular, a stable triangle has at most one nonnegative unordered shadow pair. Apply the same assertion to the polar facet corresponding to the proposed strictly unstable primal root.

**Proof.** Let p be the metric foot in the facet's relative interior and write `z_i=x_i-p` for its vertices. Orthogonality gives `D_ij=z_i^T M(z_j-z_i)`. Nonnegativity in either direction implies `z_i^T M z_j>0`, since neither z_i nor z_j vanishes. A dominating vertex v therefore has positive M-inner product with every z_i, including itself. This contradicts `0 in conv{z_i}`, because p is in the facet. The polar application uses only reference-point polarity and M,N, not a polar mass assumption.

## 5. Complete finite coverage and uniqueness of matching

The enumeration does not select a favorable incidence or complement. For every canonical map it performs two independent complete enumerations of all directed Hamiltonian paths: a vertex DFS and **all 12,870 eight-edge subsets** of its sixteen true edges. Their sets agree map by map. A directed path is relabelled as short leaf 8, root 0, then long arm 1 through 7. Only actual terminal facet 567 is accepted.

Every complete nine-label embedding is quotiented by the full map automorphism group; the action is free, and the raw count equals orbit count times group order. This gives **43,234** genuine-terminal broom embedding orbits over the 296 maps. For every embedding the code retains both T and the actual-edge-eligible T_alt, all nine stable roots, the actual complementary dual tree, and **every root-preserving isomorphism** to each allowed TREE. Every subgraph of each of OJ's 11 frames containing that base tree is tested. The optional primal shadow 2->8 is separately absent or nonnegative. Nonedge shadows are not deleted merely because they cannot own a true edge.

Each surviving record specifies both complete nonnegative graphs, all matching choices, the full tree-to-facet permutation, and all forced strict triangle exits. The source then independently rechecks **both** complementary choices directly from that final graph and asserts that their eligible-choice list equals the stored witness list. Thus an alternative is never lost by choosing a particular dual transport.

Observed counts before the final duplicate-broom quotient:

```text
                                  all 296 maps   outside accepted 17
terminal broom embeddings              43,234                41,914
actual primal-tree choices              57,350                55,586
rooted complementary trees             516,150               500,274
allowed five-shape complements           40,008                38,474
surviving complete graph records         93,843                90,350
matching cases                          25,795                24,821
joint-root orbits                       13,451                12,954
```

The final quotient canonically transports **both graph masks simultaneously** by actual vertex and induced facet automorphisms. It also identifies duplicate matched-tree descriptions obtained from exchanging broom labels 1 and 8. This is performed **after** all alternatives are retained and verified. The resulting counts are

```text
                                  all 296 maps   outside accepted 17
coupled graph orbits                    90,962                87,519
compatible matching branches            24,597                23,640
graphs with two compatible choices           0                     0
```

**Proof of the uniqueness theorem.** For any putative strict C32 target, inherited matching supplies at least one strict pair. Its complete physical graphs pass all the necessary tests above and occur in the exhaustive cover. If two different weak compatible pairs existed at the same roots, the inherited primal restriction makes them precisely T and T_alt in one broom labeling. Both would therefore be recorded for the same complete graph state. The explicit re-enumeration and the complete zero count above exclude that possibility. Consequently the unique weak compatible pair is the existing strict one. This does **not** say that only one primal escape tree exists, or that a complement can be fixed before knowing the signs.

The inherited eligibility-graph theorem consequently implies that, at a putative C32 target, each eligibility component is a tree with one half-edge; its parallel-cycle alternative cannot occur. :contentReference[oaicite:7]{index=7}

For attribution, a separately computed coarse cover using the five dual tree shapes, both complements, and the basic primal triangle/root tests leaves **13,019** joint roots outside the 17. The complete intersection leaves 12,954: **65 additional joint roots** are removed by the finer tests. Their full list is generated as `new_cut_gain_over_coarse`. The entire 7,805 gain is **not** attributed exclusively to replacing 25 old frames by 11, nor to essential Lambda-square coupling. No result from the unpersisted 7954 package is used or claimed reproduced.

## 6. A complete whole-root certificate: canonical 62/U8

This is a complete new target-U exclusion, not an old accepted type. Its canonical oriented facets are

```text
0 [0,1,3]       1 [0,2,4,1]       2 [0,3,6,7,5,2]
3 [1,4,6,3]     4 [2,5,4]         5 [4,5,8]
6 [4,7,6]       7 [4,8,7]         8 [5,7,8].
```

The sixteen true edges are

```text
(0,1),(0,2),(0,3),(1,3),(1,4),(2,4),(2,5),(3,6),
(4,5),(4,6),(4,7),(4,8),(5,7),(5,8),(6,7),(7,8).
```

Its full vertex automorphism group is

```text
(0,1,2,3,4,5,6,7,8),
(3,1,6,0,4,7,2,5,8).
```

There are exactly two genuine-terminal broom embedding orbits with root 8. The complete broom-label-to-canonical-vertex transports are

```text
pi_A=(8,5,2,4,6,3,0,1,7),
pi_B=(8,5,2,4,6,3,1,0,7).
```

In both, T_alt would require true edge `(2,7)`, which is absent. The terminal facet is canonical face 0. The two T-complementary dual edge sets, in canonical facet labels, are

```text
A: (0,3),(1,2),(1,3),(2,6),(2,8),(4,5),(5,7),(6,7)
B: (0,2),(1,2),(1,3),(2,6),(2,8),(4,5),(5,7),(6,7).
```

A is a three-arm tree with arm lengths **4,3,1**; B has a degree-four node. The permitted unrooted forms are paths, a three-arm **5,2,1** tree, and a three-arm **6,1,1** tree. Neither complement can therefore be any permitted rooted pole tree, **regardless of which of the nine facets is stable**. The inline checker binds these literal maps and permutations to the catalogue and independently tests all nine rootings of each complement. By actual matching necessity, every continuous realization at this U root is excluded for the target.

For comparison, the unconditional `40/U3` exclusion has the following literal facets:

```text
[0,1,3],[0,2,4,1],[0,3,5,2],[1,4,8,7,3],[2,5,4],
[3,6,5],[3,7,6],[4,5,8],[5,6,7,8].
```

Its true edges are

```text
(0,1),(0,2),(0,3),(1,3),(1,4),(2,4),(2,5),(3,5),
(3,6),(3,7),(4,5),(4,8),(5,6),(5,8),(6,7),(7,8).
```

Its automorphism group is trivial. There are 31 root-3 broom paths before the terminal-facet condition and **zero** afterward. Thus this root is excluded already by the actual-mass primal theorem, without any stable-root or matching premise. The full per-root before/after tables for all 296 maps are generated by the same two path enumerations.

## 7. Physical control, continuous scope, and remaining complement

The supplied exact control uses the earlier actual C32 four-triangle-fan body at t=1/500, not arbitrary matrices. Its complete nine rational coordinates and actual facet cycles are literal in `physical_cut_control.py`. The control reconstructs all maximal supports from triples, integrates volume and centroid with two different apices, recentres exactly, reconstructs every actual facet area centroid and cone weight, and verifies one physical

```text
d_i=3 omega_i,  Lambda_ij=d_j(1-q_i.c_j),
Lambda Q=-Q,  Lambda^2+Lambda=4*1*d^T,
rank Lambda=4,  rank(I+Lambda)=6.
```

Both M=I and `M=[[2,1,0],[1,3,1],[0,1,2]]`, with their exact reciprocals, pass all new cut, projection and root rules. The Euclidean control has stable faces `[0,3,4,7]` and unstable vertices `[1,2,6,8]`; it is not a target. The physical four-row minor remains

```text
-29225402286904272323120130050768458025941435
 /44476389385373086840084719020220335744901748548 <0.
```

No P0 property, independent Gram metric, fitted centroid, or free physical cone mass is used. The control tests the implementation; the continuous validity of the new predicates follows from the proofs in Section 4, not from sampling this body.

**Scope.** The new target exclusions cover every bounded full-dimensional convex realization of the specified canonical maximal-face lattice, at its own uniform-volume centroid, for arbitrary reciprocal SPD metrics. Polygonal facets are truly planar; their triangulation diagonals are never escape edges. Weak unused shadows, equal nonroot norms, zero nonroot escape primitives, and arbitrarily small positive tetrahedral/cone volumes are allowed. The strict-target matching hypothesis excludes degenerate equilibria, but does not exclude a zero primitive at a nonequilibrium feature. The 11 unconditional unique-U exclusions require no S/H nondegeneracy assumption beyond the inherited unique-strict-U theorem.

Coincident vertices, merged maximal facets, zero-volume solids and singular metrics are outside those actual incidence domains. Every admissible finite approach to such boundaries is covered, with no angle, coordinate, volume, or condition-number cutoff. No theorem about a different limiting lattice is inferred.

**Exact unresolved complement.** Retain precisely the 12,954 generated joint-root orbits and their 87,519 complete graph-orbit refinements, or the coarser 23,640 matched-tree branches together with those refinements. Every one of the 279 unclosed types retains a branch. A surviving graph must still satisfy actual convex geometry, one reciprocal rank-three Gram pair, the same ordinary mass map and physical Lambda; graph survival does not assert any of these are attainable.

The most useful continuation is now the **uniquely owned matching** in each retained state: impose its sixteen strict true-edge escapes together with the generated absent-pair strict negatives and triangle implications, then use actual shared moments or the valid three-triangle pivot. The four-row physical inverse shortcut remains unavailable. No further algebraic or numerical feasibility of the retained states has been established here.

## 8. Complete recovery capsule and observed checks

Save the four complete source units below, UTF-8/LF with one final LF each. They use **CPython 3.13.5, standard library only, assertions enabled**; no numerical library, randomness, optimizer, scheduler, external catalogue download, or missing checkpoint is needed. The first is the unchanged accepted catalogue recovery; the other three are new.

Run in an empty directory:

```sh
export PYTHONHASHSEED=271828
python -S recover_c32_complete.py > catalogue.log
for a in 0 40 80 120 160 200 240 280; do
  b=$((a+40)); [ "$b" -le 296 ] || b=296
  python -S joint_frontier.py part "$a" "$b"
done
python -S joint_frontier.py join > joint_frontier.log
python -S quotient_frontier.py > quotient_frontier.log
python -S physical_cut_control.py > physical_cut_control.log
```

Two clean **batched** executions completed, including the independent catalogue checker, and reproduced every part, all four JSON outputs and all four logs byte-for-byte. The second used the displayed hash seed. These are two replays of the same implementation, not two independently authored full proofs. Within each replay the path coverage uses the two independent enumeration algorithms described above. The parent cap9/ninth-arrow numerical certificate engines were not rerun.

| File | Bytes | SHA-256 |
|---|---:|---|
| recover_c32_complete.py | 6337 | 35da62544738dbc2177f4c6ef09768d41b5fd208bd6042006421481b9d9168a0 |
| joint_frontier.py | 15918 | 8af3e767f2af574daba639ecf7da05f36a4e1915116962383a6e16e51ff4cfa6 |
| quotient_frontier.py | 5792 | f4fb7b12fb017d13f0f61d90486bcb04b7c29d84e7bc345556d06f7139736289 |
| physical_cut_control.py | 5749 | 9bc3c0ac6ecacfa8ad760d34703ead5ac587a21bfdf4db0597cc2c6f054e7518 |
| c32_catalogue.json | 240929 | efb10a4657a891cd13f6f62db94164bd4b3005e908dc55aae87db450930f704d |
| joint_frontier.json | 10444324 | 4ddd4d8f8b33c502ceedb617ab7f1c75c5dd3b22dbca0d30a6235ef991df9e93 |
| quotient_frontier.json | 9498762 | 95911c6144747036ed4095f6ba035baf205b195fbf757f97718068379b4806f9 |
| physical_cut_control.json | 11453 | e4354cb415d916e1985c0e529ba71297802e4ae2f8c478d5cdebd38376c10944 |
| catalogue.log | 642 | 0b6c9fc3c56411623406c54b3f6ae8f707cc402635adc0ae635ef2d98f21e743 |
| joint_frontier.log | 1825 | 03e8b6fb7e75b69a5afaec4a0b4348c33ad6b4a27f0a1ae2cd0392570230a6c3 |
| quotient_frontier.log | 759 | cf28106fbc58d20922c57f66f590c7bf372954b87bc90e7e9d28724dd304cee5 |
| physical_cut_control.log | 416 | 2e33b72927d67f5878a1a6e470014d9b71efabf648f3725ab312774e29db087c |

The complete generated quotient transcript is:

```text
ALL_VERTEX_FACET_AUTOMORPHISM_AND_BOTH_MATCHING_TRANSPORTS_PASS
COUNTS {"graph_orbits":90962,"matching_orbits":24597,"two_matching_states":0}
OUTSIDE_17 {"graph_orbits":87519,"matching_orbits":23640,"two_matching_states":0}
ALL_ALT_BRANCHES_RETAINED_THEN_IDENTIFIED_BY_ACTUAL_RELABELING_PASS
CANONICAL62_U8_TWO_COMPLEMENTS_ALL_NINE_S_ROOTS_EXCLUDED_PASS
UNIQUE_COMPATIBLE_MATCHING_FOR_EVERY_PUTATIVE_C32_TARGET_PASS
ADDITIONAL_JOINT_ROOTS_BEYOND_COARSE 65
JOINT_PARTITION 868 55 7805 12954
NEW_UNCONDITIONAL_U 11 NEW_TARGET_U 66 NEW_TARGET_S 5 NEW_WHOLE_TYPES 0
GRAPH_ORBITS_NOT_PHYSICAL_ATTAINABILITY
REPORT 9498762 95911c6144747036ed4095f6ba035baf205b195fbf757f97718068379b4806f9
SOURCE 5792 f4fb7b12fb017d13f0f61d90486bcb04b7c29d84e7bc345556d06f7139736289
```

### Output semantics needed for continuation

In each map of `joint_frontier.json`, a record is

```text
[bi,toggle,s,hm,witnesses,forced_primal,forced_dual].
```

`brooms[bi]` is the complete broom-label-to-canonical-vertex permutation. Toggle 1 includes the optional nonnegative shadow 2->8, whether or not it is a true edge. `s` is the canonical stable facet. `hm=sum(2^(9*i+j))` over nonnegative unequal pole arrows. Each witness `[choice,TREE,sigma,exid]` gives T/T_alt choice 0/1, literal TREE ordinal, full tree-label-to-canonical-facet permutation, and index in the report's sorted `graphs[TREE]` extra lists. Matching arrows and recorded triangle implications are strict in the physical target; other listed nonnegative arrows may vanish. All omitted unequal arrows are strictly negative.

In `quotient_frontier.json`, each graph state is

```text
[primal_mask,pole_mask,matched_parent_arrays_and_S,origins].
```

An origin `(ri,ai)` points to a complete unquotiented record and the actual coupled vertex/facet automorphism transporting it to the canonical graph pair. Each matching branch is `[actual_primal_parent_array,S,origins]`; its unique diagonal parent entry identifies U. For a matching-branch origin `(ri,choice)`, reconstruct that record's actual parent array and minimize `(parent,S)` under the printed coupled automorphisms, exactly as the quotient source does. Original records retain every dual transport and complementary choice. This supplies all exact label reconstruction, not just orbit totals.

Supplementary [complete sources, literal maps, full frontier ledgers and transcripts](sandbox:/mnt/data/C32_ELEVEN_FRAME_JOINT_ROOT_EXCLUSIONS_V1.zip). The following inline sources alone reconstruct the entire new frontier; the archive is not a required input.

### 8.1 — `recover_c32_complete.py`

```python
"""C32_POLYHEDRAL_MAP_CATALOGUE_V1 complete recovery and finite verification.
CPython 3.13.5, standard library only; assertions required.
Save as recover_c32_complete.py (UTF-8/LF, final LF) in an empty directory.
Run: python -S recover_c32_complete.py
No external files, seeds, numerical solvers or downloads are required.
"""
from pathlib import Path
import base64,hashlib,json,subprocess,sys,zlib
assert __debug__
B=r"""
c-p->4RfQol7EGrt6RfH@!HPEPVCXE@?^Zbd6jiiN#?4i2#*p**u)t806S)~x!-=>k^q67nSJ-_E>mNS)ZJ>e`dfZ^H#-@)GnTU`
nQwS^UA!B<dldgBJ2uOWb;M$p9<SKi;PGa~Q<jHGY$Sn^FSrr&XXBEd42<A-%V&9#8s-J*pOXu#`xxIA`2s*sy8Zr<k>xD*S?U{6
=%p+zMh43=o+7c#NclfEVak0#y4%D<V=Xa{?~OKhkMU))T1PzRG0!q%lkv=$C2<Ukb6*T8&is(glbA)vK@_fydCJxcoXXY<o^m5k
Ll)0Bk=RTI%gQZ3#zC5_fM65>LBU$MS|@34Tqc`1=P5CKV3jMl5JvJOi7KdBvhu=M5>+s3mM>t-CB!YfKE~>0!7`j9##5HW#K;Oj
l2S2T*XQ15?z)fhlwJUTvCjizR?H%92G;N~HsCMi`6i8xRT!Ir9S)tNz#fK<5x_BoMi?6@?2(%hhiS{QN+NNRu2>X)1wvViQoaGv
ni=rMeN!$bhX7xY4UjCLRm8%07WzD%>BKmFc~xYSoZ2t10@bZKnp%#W$MGc*L`&t;3E`iThup;9=!pSpq~0jSXU216uf{;4PlUCI
>NN4sqk(Nc9rdmMl*F8oF@vF}<G#}bR1BDmcoxVm7j&B-+=fYqE)OEkN+b}5&056em_2i-CnppViz3tX2(!d$VoR`uc(H2HrHbrf
aix{GP(&$+OFX+<7HxQD>LT0HnD25E^%(%Ik&)3Yd~hBM91Ze$5k}nDmU}{wq4?}F-#53`XiHOj>+CVKh1IL0LwI$1snyu`^cV-Z
_4ChzBXKSnzzrHY$_ebaG6)tYaX4d<rZv)(AJW3$TMnN-coy^yASqy)`*SWB@sfN|x`QMQd7M|y0I7^)H42F6{K5=OALIkZ1|wbp
#-E|=r8@-E&G~91mVoJxzuqH4#a&nDOc@DogEq`ZPIx@a=`@M?NPG=4@lqdp7S3Z7z1b(neO;^5l%{wpfdHYjZ}2GNhW+9VnXW-;
7tVPF3h>%cBByCVrMk7uCSo2?r7vvQdmS0z3OAgB27@<`XNx4o3GWr<@SIV*rR+#{heQQhi?CEfNyXkdg2Wz$l8W2(ZYg3|)&Yw6
2Lh?|RkHsEV7))kV4<Dz%^C@YyKKGYu~2fwCP3{DlLF>T@QR|a4dk?89~wqhqDY?$Bf5>YtXr{0>9h&5<OQwpvlc#x0(A;?6P3z9
_sfe9ICelLLK9*Bz!`v6g2wLYnp{{dkJgt#961m>4y^<v>&PTYDADblT6F@QR%J8FH6R%xX_XElU!<J7Rfb^l%1y*Pq;}8wX<D0B
sq@(oXF;w1r2P*clxK#$vbZpJT`$amAfyAP_2H!E3^1&rV&qo_(ol3aQAAB3GqsNUdrRpFgINYgGH3+AC`z8WPm$0+kPx%P!vi;+
Cw@W|z>ml3i*nq(w$n!7)+ui(4*qzIpOV@?O2_{v-8Nxy_D_m(*$NSW63+953A=KBELr$(#H`U!Jz(I6lEnk!Q6mp2CROUlL~a&g
h*Io=YS?Cv^g%ELo+qRa&ptfyeE`p1BcZ6B!zr0IL`ggXK|brQleO8?Q--Vy@efVU#5hluKo>y8b4D0EORWWSAiz!?cN*Cg9LX|H
o@4p~aKj*bm7ar&q|vm4%u!_IiM0J75SE?>_=|V|3O3>yaSug_mL92;jc08qh+6wMZwLmEhw-MBw*(*yn`a_>aYl3X25E=Wa!@mw
AM7+cM9RC;t%~HRW!L^5&iuPLFc0$fEoFs=xt@XSe9c$bxk~x+y*v^LK2-~<of5T2%Q>=fHDH67KAbkQoEASzNKOOou*K5*JTI5!
8shYa;?rI(9U279*bxLxk0l^W#rHYZHEzTTNW&6XsPa_LRYonGUxrHoK$XgAhyH)7Fl4T)40%&wK(p+i8^X4BCbMK^Qopx==X7q*
)ue~Ob9-37A5O;uyYEoyiA-)TzOyFWf`WosKx!aX?+=~5ePS40SU*%%!~#-?!~5o3<iQ}V;}@Z~L?q|0dn8c}_CgM~{vR}X@z->B
1j?i|v!RGET&dxvkxqj`y^*QvrJ0tAB%8cS+=RyIg`cKvo?di_Itcw|&`A2~WKRIJbTuf=O3A|-c~n(Yo<;;1YGzhdxu`aO$eRO_
WkG&WN`-Cm#Dzj2`;KTvXkipfa*i);Vf^da`*yeym>aVF>)E>k=IvB>wZ;s6L%iYkbtJL}Tj;Yh@*y9T#oj1cQW=kR%sPh<HkT|9
B#b*!h=fAK*8^#uaR0y-uJwjVh{yrcqMY1Wquq|K)>sb|1%4@<gH%Nk00$3MfHY^!v*Be3TM@~|$V)j}eyf-e*l$-51p=+s->4h_
NHF*VEsF21E3^mZzfG@DtJZ%0uh5m}44eQXhatonDT^=*vIDy-sFVPpp{S+&?4sEBn#r=N<5z36`r)2^!Rq^MsA-i$p-rgxg9;}s
ZKRxusvSxU5$HB~!&=3=G|CkNJ1eaS0wUFN$C1d<p;R68hsZ1jROPVOX$aYS=i%;ZJpJwS_4wiHW_sTtB@_vwO|}p=u<z**fYP&G
ZPKfHj{`_j&sv6!Z0$vM#hks8b!O7YDinLSH`iZ&pM1I-U%S`iFO$0tS$%^=NI0`ns$vBZKOqqvhVmrHvKdqmp%zFIfO%(BwK+k0
s)7e6fz8(xGX9MAMj4L+j1RQe%D0hPGm`}-?4>h0>?3`Ui3&4&ts>t?f`WZ*4s@pBg7vjH@MZ^T@|DN38>rWtx@TlFo+ANjt3ZIL
D$}U(=dFsfS-y&wIlcft8u65`s{?pJ{||IF4q4cNqj1OqvA%|D6EI1|jH18MO{HG39C_7ttewe`ba$|}RUOU|1@Y?L$nBaoI=iy*
)`%Zqfk6ujctc2nbxlJ%rLNf9H3`<v5$$U-(3%*2ID_EsQz2c@1i9f1@<)O_xJp*CvDzrVMG^`HE@@S(pdEbY`g{%vRz`7sB<W@l
uYvBG2+fr1`MyI?Usg%FUWC~yL+xqNdrH90Tx{97Ai$JovIn>YVnU#Lr!{$&f_lz|N=@;*4Ig#~m+d%C`Grz38u}fl^jp~Nr%E8O
NSGJ2b9pjwH5311eCuA0AI8@=zkQy#|JCmh+-^7nW~NGD{d2Kl9H=(ZxX6%g32;tCcp4~Eg_j|Du?8#|B%d>jprW|QtSe_q#i_~S
8*u3=!#6A3qY@Tdv_zAjg49&ArdGKZTgX73V|9Mw=p^T{R0LC~mPKN%QYmSa>5t_QVado<z0#Z~E1su?%Xc&Ikl0qCJ;L%F0tHXq
09Ns31T8Z__DoH@e(Cy~6?hhTRs<Jyg-b;j3j$j+aGD8-)a(%WH|$u}QRne7?pR&$YKhOwd<QRh%ue&#3h4vja|*n>UXgR`^*mdR
V1(*$dGp8Z_2glK%An$rJh0CF<oZ|l)93MZhg65v`TNb)^ufKmxp{DJ?mk{U0E#C5Ci%O`?akeTq6upgb@$ZG7Hn{KF2=eGzVk!S
w7j|;K=Ftjxh_iIb*(NW9=_UyHB!{?Z$95$PX1-;&8>gDnvNfC?yfHH-J9w47k7H&jvpSzSJTNI?9aVCIdw0u$5(%J#N`vX2-l6-
3V5Ql<GPp%xNc`CQ-a6%9eD?O76ye2XR&{+32UNVf}MzL2IBJytv@ZWC0E}s&K7*O9PM3R8c7@#^0Lxk0R+swdrJKdv%yE}s`0N}
52E^1gN=nCWE!hOcZSuu9o9ts3@h~V@F*Re_AUk&)x>uW6U5I0uis;*=V!mL_ZR({-#-b?gY$v!U7YsMPd)$CJL&b#_(ku%KRY{P
jKBZI_fF4x7bm^om)@!00Z~$6g;B!%(mMXb_!XQ%{DEE=lT8Fd2Hybg&yWGY_&`rZ6mI&!t}#{s$D$BNGScCw{z?YnvqFlv1`pmL
JqVlqbHh?TLQ)Ln#IoGL_IY{7jQw=xVfcVyar>OW2NruiCwNzcLw`?FpNZKd<*P0ddsu9+l_UD(A~}JV>P{ThvYgWy6r4$jlvmmc
^j6&|J$;O!?5C@4UDBH0>71f5VvY)#V(>aL%B=Zx*oWj0y>VQpA!nrDD|1_1E*{C=)M!g%y}SL*4wY<ih(7Dg`qtHN-69Dxd-&uW
!Q<(uKXi^{mv*bVv|H7s-L~6_ZBeYcb$u_}A*vtZ&_M5?QEc+$wi)8}@ClTWPjB~SWNzKMZO--9(7)Yvdm<5Sb$q_to&`xc|BDta
;6>lZlZT>GXeEK*V9P43$iOBJk~yMg>kv^jeDU<fA^+QlirNh$Wz7}qHCK5_FSTB%JvoE_=feT{Wq3y35BsO&VtCejtzbpXDyl&I
w(4p%ClFLIZE`*NV={dh-+gf>C+_65itW?M{k{9}``yjw-+p(e5Zv6`@jXOt$${{C6LD=Fgy>o14_DB?$iCun)mH@Xf~GI8uu&3t
P2DvvF=82<%@#;XmdpUG=fdcuL`Erm3=qu1EEmqJz6Ku|9{~{^7<#N2X<=fGnLU6+g_4-K1qa8*Q&_{?#1JSw{C$9MqQp?IBF(c5
nU{d40_MULi^!2ySk}Kas0yq*yMsAi$Eoju^czOK&YRmEnM`&ZtE@R!-ETK7IW{dJ52$`og6|jN6;5^k;!qXZ#BJyw*0YM}QvX@R
sQOjJvRazwQfHvD5?dg^cB4uG?wfq-{g4aU4?!|}KNgX2%=YZi*=xOMh;>J{dh^P+swpah4%II)b)>_;Ho<){3kA40{bFJ{%%G|!
%q|=Y68D|<Do=4o3U!V`H9O8L-ItY`(p>^}OS8S6@lM}-%hwjIzBB%GVDz=_e>I^6{j#R*qfZkZW&m|;WFK!H?5~dO)*kn*H-#ez
p@8&yS&I5kDkkk75UavyxZ^&}HY*eVGkXJbn|7lB4)!OUu6q}()w`hdt-grWJk_S!iPgm~qr@C7`#t*f&p&JP_!SQ5?UK4v-cOW$
i#Cms@(M>(Nu`mPs-FxEF3yF0mL7zj^<_I+`Vl(lpT8eeh=ZR1{<wxc?N|O8YYwckT!3(IZsm6Xa6f*&o8Di2n&@?vE67SmZ8b<-
O+QU;C-4D<Si{4Qr=KLU3zgUP_)CTS?)85Fof!+P
"""
r=zlib.decompress(base64.b85decode(''.join(B.split())))
assert len(r)==10611 and hashlib.sha256(r).hexdigest()=='3a783a1fdbd6c771c0db30d2f567f14779458e299913ee787dde876e3207c05b'
M={'c32_catalogue.py': [7169, 'eb78c9ea5e89db65b791e8ac0298f0a21e6607e97c05cd32be8ecee6e8317d20'], 'verify_c32.py': [3133, '0ccbfb67b413046531801adef23567e2f791396070c3976ad70f201b912570ff'], 'c32_catalogue.json': [240929, 'efb10a4657a891cd13f6f62db94164bd4b3005e908dc55aae87db450930f704d']}
S=json.loads(r)
assert set(S)=={'c32_catalogue.py','verify_c32.py'}
for n,t in S.items():
    d=t.encode('utf-8');assert [len(d),hashlib.sha256(d).hexdigest()]==M[n]
    Path(n).write_bytes(d)
for n in ('c32_catalogue.py','verify_c32.py'):
    subprocess.run([sys.executable,'-S',n],check=True)
for n,h in M.items():
    d=Path(n).read_bytes();assert [len(d),hashlib.sha256(d).hexdigest()]==h
print('C32_COMPLETE_SOURCE_AND_CHECKER_RECOVERY_PASS')
```

### 8.2 — `joint_frontier.py`

```python
"""C32_ELEVEN_FRAME_INCIDENCE_FRONTIER_V1. CPython 3.13.5, stdlib only.
Run after the inline recover_c32_complete.py: python -S joint_frontier.py
No locator, coefficient replay, random seed, or external geometric input.
"""
from itertools import combinations,permutations,product
from collections import Counter
from functools import lru_cache
from pathlib import Path
import json,hashlib,sys
assert __debug__
PARENT=['minimum-0040','2cd8dc8ea75a5a8d1eaa9fabfca75a65181325fab676cd95dec5cd1c16426a59']
CATPIN=[240929,'efb10a4657a891cd13f6f62db94164bd4b3005e908dc55aae87db450930f704d']
TREES={253:(0,0,1,2,3,4,5,0,7),266:(0,0,1,2,3,4,5,4,0),272:(0,0,1,2,3,4,5,5,0),278:(0,0,1,2,3,4,5,6,0),285:(0,0,1,2,3,4,5,6,7)}
FRAMES={253:[[]],266:[[(5,7),(6,7)],[(6,7),(7,5)],[(7,5),(7,6)]],272:[[(6,4),(6,7)],[(6,4),(7,6)],[(6,7),(7,4)],[(7,4),(7,6)]],278:[[(6,4),(7,5)],[(7,4),(7,5)]],285:[[]]}
PRIMAL=[(0,0,1,2,3,4,5,6,0),(0,0,8,2,3,4,5,6,0)]
WHOLE={33,34,72,139,149,152,159,163,164,178,192,217,284,288,293,294,295}
PARTIAL={35:3,45:3,47:3,49:3,51:3,53:3,282:0,290:3}
ALL=set(range(9))
def serial(x):return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
def und(a,b):return (min(a,b),max(a,b))
def code(p,root):
 ch=[[] for _ in p]
 for i,j in enumerate(p):
  if i!=root:ch[j].append(i)
 def walk(i):return '('+''.join(sorted(walk(j) for j in ch[i]))+')'
 return walk(root)
CODES={code(p,0):o for o,p in TREES.items()}
def rooted(edges,root):
 adj=[[] for _ in range(9)];p=[-1]*9;p[root]=root;todo=[root]
 for a,b in edges:adj[a].append(b);adj[b].append(a)
 for a in todo:
  for b in adj[a]:
   if p[b]<0:p[b]=a;todo.append(b)
 assert len(todo)==9 and len(edges)==8
 return tuple(p)
def outrows(arcs):
 es=tuple(arcs);return tuple(frozenset(b for a,b in es if a==i) for i in range(9))
def arcs(rows):return tuple((i,j) for i,r in enumerate(rows) for j in sorted(r))
def graph_mask(rows):return sum(1<<(9*i+j) for i,r in enumerate(rows) for j in r)
def from_mask(mask):return tuple(frozenset(j for j in range(9) if mask>>(9*i+j)&1) for i in range(9))
def connected(vs,adj):
 if not vs:return True
 seen={min(vs)};todo=list(seen)
 for v in todo:
  for w in adj[v]&vs:
   if w not in seen:seen.add(w);todo.append(w)
 return seen==vs
def interval(vs,cyc):
 flags=[v in vs for v in cyc]
 return sum(flags[i]!=flags[i-1] for i in range(len(flags)))<=2
class Map:
 def __init__(self,faces):
  self.faces=tuple(tuple(f) for f in faces);self.edges={};rot=[{} for _ in range(9)];dart={}
  for i,f in enumerate(self.faces):
   assert len(f)>=3 and len(set(f))==len(f)
   for k,v in enumerate(f):
    w=f[(k+1)%len(f)];prev=f[k-1]
    assert (v,w) not in dart;dart[v,w]=i;rot[v][prev]=w
    self.edges.setdefault(und(v,w),[]).append(i)
  assert len(self.edges)==16 and all(len(v)==2 for v in self.edges.values())
  assert all((b,a) in dart for a,b in dart)
  self.adj=tuple(frozenset(w for a,w in dart if a==v) for v in range(9))
  links=[];dual=[]
  for v in range(9):
   w=min(rot[v]);cy=[];df=[]
   while w not in cy:cy.append(w);df.append(dart[v,w]);w=rot[v][w]
   assert w==cy[0] and set(cy)==set(rot[v]) and len(cy)>=3
   links.append(tuple(cy));dual.append(tuple(df))
  self.links=tuple(links);self.dual_faces=tuple(dual)
 def cut_ok(self,G):
  # Linear-functional cuts of a genuine convex polytope, not fitted metrics.
  for i,S in enumerate(G):
   if S and not connected(set(S),self.adj):return False
   if not connected(ALL-{i}-set(S),self.adj):return False
   if self.adj[i]<=S or not interval(S,self.links[i]):return False
   nonneg=set(S)|{i}
   for f in self.faces:
    if not interval(nonneg,f):return False
    if i in f:
     k=f.index(i);two={f[k-1],f[(k+1)%len(f)]}
     if two<=S and not set(f)-{i}<=S:return False
     if not two&S and (set(f)-{i})&S:return False
  return True
 def projection(self,G,H):
  # Weak two-edge triangle chain, strict missing skip: forced positive dual exit.
  forced=set()
  for f,vs in enumerate(self.faces):
   if len(vs)!=3:continue
   for a,b,c in permutations(vs):
    if a not in G[b] or b not in G[c] or a in G[c]:continue
    other=next(j for j in self.edges[und(a,c)] if j!=f)
    neighbors={j for e,ff in self.edges.items() if f in ff for j in ff if j!=f}
    if other not in H[f] or (H[f]&neighbors)!={other}:return None
    forced.add((f,other))
  return tuple(sorted(forced))
 def no_dominator(self,G,face):
  vs=self.faces[face]
  return not any(all(w==v or w in G[v] or v in G[w] for w in vs) for v in vs)
# All 25 graphs of the immutable parent's 11-frame cover, in exact tree labels.
COVER={}
for o,frames in FRAMES.items():
 xs=set()
 for fr in frames:
  for bits in range(1<<len(fr)):xs.add(tuple(sorted(fr[k] for k in range(len(fr)) if bits>>k&1)))
 COVER[o]=sorted(xs)
 assert len(COVER[o])=={253:1,266:8,272:9,278:6,285:1}[o]
 for extra in COVER[o]:
  ee={(i,TREES[o][i]) for i in range(1,9)}|set(extra);G=outrows(ee)
  orders=[]
  for choices in product(*(sorted(G[i]) for i in range(1,9))):
   p=(0,)+choices
   for i in range(1,9):
    seen=set();j=i
    while j:assert j not in seen;seen.add(j);j=p[j]
   assert code(p,0) in CODES;orders.append(p)
  assert len(orders)<=4 and len(ee)<=10
assert sum(map(len,COVER.values()))==25
@lru_cache(None)
def transports(p,s,o):
 # Every root-preserving isomorphism from literal TREE o to this actual cotree.
 source=TREES[o];cs=[[] for _ in range(9)];ct=[[] for _ in range(9)]
 for i in range(1,9):cs[source[i]].append(i)
 for i in range(9):
  if i!=s:ct[p[i]].append(i)
 def shape(ch,i):return '('+''.join(sorted(shape(ch,j) for j in ch[i]))+')'
 def rec(a,b):
  aa=cs[a];bb=ct[b]
  if len(aa)!=len(bb):return []
  out=[]
  for order in permutations(bb):
   if any(shape(cs,x)!=shape(ct,y) for x,y in zip(aa,order)):continue
   lists=[rec(x,y) for x,y in zip(aa,order)]
   for parts in product(*lists):
    d={a:b}
    for part in parts:d.update(part)
    out.append(d)
  return out
 result=sorted({tuple(d[i] for i in range(9)) for d in rec(0,s)})
 assert result and all(sorted(pi)==list(range(9)) and pi[0]==s and all(p[pi[i]]==pi[source[i]] for i in range(1,9)) for pi in result)
 return result

def paths_dfs(M):
 # Directed Hamiltonian paths: short leaf, root, then the seven-edge long arm.
 raw=[]
 def walk(p,used):
  if len(p)==9:raw.append(tuple(p[1:]+p[:1]));return
  for w in sorted(M.adj[p[-1]]-used):walk(p+[w],used|{w})
 for v in range(9):walk([v],{v})
 return set(raw)
def paths_subsets(M):
 # Independent exhaustion of all binomial(16,8) true-edge subsets.
 result=set();ee=sorted(M.edges)
 for ids in combinations(range(16),8):
  adj=[[] for _ in range(9)]
  for k in ids:
   a,b=ee[k];adj[a].append(b);adj[b].append(a)
  ends=[i for i in range(9) if len(adj[i])==1]
  if len(ends)!=2 or any(len(a) not in (1,2) for a in adj):continue
  p=[ends[0]]
  while len(p)<9:
   ns=[w for w in adj[p[-1]] if len(p)==1 or w!=p[-2]]
   if not ns:break
   p.append(ns[0])
   if len(set(p))!=len(p):break
  if len(p)!=9 or p[-1]!=ends[1] or len(set(p))!=9:continue
  for q in (p,p[::-1]):result.add(tuple(q[1:]+q[:1]))
 return result

def run_map(m):
 M=Map(m['facets']);D=Map(M.dual_faces);assert {frozenset(f) for f in D.dual_faces}=={frozenset(f) for f in M.faces}
 assert sorted(M.edges)==[tuple(e) for e in m['edges']]
 aut=[tuple(a) for a in m['automorphisms']];fsets=list(map(frozenset,M.faces));fperm=[]
 for a in aut:
  assert sorted(a)==list(range(9))
  fperm.append(tuple(fsets.index(frozenset(a[v] for v in f)) for f in M.faces))
 def orbit(pi):return min(tuple(a[v] for v in pi) for a in aut)
 def rootpair(u,s):return min((a[u],b[s]) for a,b in zip(aut,fperm))
 allpaths=paths_dfs(M);assert allpaths==paths_subsets(M)
 brooms=sorted({orbit(pi) for pi in allpaths if frozenset(pi[5:8]) in fsets})
 assert sum(frozenset(pi[5:8]) in fsets for pi in allpaths)==len(aut)*len(brooms)
 root_pre={min(a[u] for a in aut):0 for u in range(9)};root_post=root_pre.copy()
 for pi in {orbit(pi) for pi in allpaths}:root_pre[min(a[pi[0]] for a in aut)]+=1
 for pi in brooms:root_post[min(a[pi[0]] for a in aut)]+=1
 counts=Counter();states={};coarse=[];coarse_roots=set();strict_graphs=0
 @lru_cache(None)
 def qcut(mask):return D.cut_ok(from_mask(mask))
 for bi,pi in enumerate(brooms):
  base={(pi[i],pi[PRIMAL[0][i]]) for i in range(1,9)};opt=(pi[2],pi[8])
  GP=[outrows(base),outrows(base|{opt})]
  pcut=[M.cut_ok(g) for g in GP]
  if und(*opt) in M.edges and pcut[1]:assert frozenset(pi[i] for i in (1,2,8)) in fsets
  for choice,p in enumerate(PRIMAL):
   pe={und(pi[i],pi[p[i]]) for i in range(1,9)}
   if not pe<=M.edges.keys():continue
   counts['actual_primal_tree_options']+=1
   de=[tuple(M.edges[e]) for e in sorted(M.edges) if e not in pe]
   rooted(list(pe),pi[0]);assert len(set(de))==8
   for s in range(9):
    counts['rooted_complements']+=1;dp=rooted(de,s);treecode=code(dp,s)
    if treecode not in CODES:continue
    o=CODES[treecode];counts['five_shape_complements']+=1
    for toggle in (0,1):
     if choice and not toggle:continue
     G=GP[toggle]
     if not pcut[toggle] or not M.no_dominator(G,s):continue
     # Every isomorphism, not an arbitrary assignment of the canonical dual labels.
     for sigma in transports(dp,s,o):
      for exid,extra in enumerate(COVER[o]):
       he={(sigma[i],sigma[TREES[o][i]]) for i in range(1,9)}|{(sigma[i],sigma[j]) for i,j in extra}
       H=outrows(he);hm=graph_mask(H);counts['raw_frame_graph_instances']+=1
       if not qcut(hm) or not D.no_dominator(H,pi[0]):continue
       ph=M.projection(G,H)
       if ph is None:continue
       hp=D.projection(H,G)
       if hp is None:continue
       key=(bi,toggle,s,hm);wit=(choice,o,sigma,exid)
       if key not in states:states[key]={'witnesses':set(),'forced_primal':hp,'forced_dual':ph}
       states[key]['witnesses'].add(wit)
       assert states[key]['forced_primal']==hp and states[key]['forced_dual']==ph
  # Independent minimal-graph coarse ledger for root comparisons.
  for choice,p in enumerate(PRIMAL):
   pe={und(pi[i],pi[p[i]]) for i in range(1,9)}
   if not pe<=M.edges.keys():continue
   for s in range(9):
    dp=rooted([tuple(M.edges[e]) for e in sorted(M.edges) if e not in pe],s)
    if code(dp,s) not in CODES:continue
    H=outrows((i,dp[i]) for i in range(9) if i!=s)
    if not M.no_dominator(GP[0],s) or M.projection(GP[0],H) is None:continue
    coarse.append((bi,choice,s,CODES[code(dp,s)]));coarse_roots.add(rootpair(pi[0],s))
 records=[];roots=set();matches=set();frame_types=Counter()
 for (bi,toggle,s,hm),r in sorted(states.items()):
  pi=brooms[bi];choices=sorted({w[0] for w in r['witnesses']});H=from_mask(hm)
  # Re-enumerate both actual complementary choices from the final graph itself.
  eligible=[]
  for choice,p in enumerate(PRIMAL):
   if choice and not toggle:continue
   pe={und(pi[i],pi[p[i]]) for i in range(1,9)}
   if not pe<=M.edges.keys():continue
   dp=rooted([tuple(M.edges[e]) for e in sorted(M.edges) if e not in pe],s)
   if all(i==s or dp[i] in H[i] for i in range(9)):eligible.append(choice)
  assert choices==eligible
  if len(choices)==2:
   e0=und(pi[1],pi[2]);e1=und(pi[2],pi[8]);common=set(M.edges[e0])&set(M.edges[e1])
   assert len(common)==1
   f=next(iter(common));assert set(M.faces[f])=={pi[1],pi[2],pi[8]}
   for e in (e0,e1):assert next(j for j in M.edges[e] if j!=f) in H[f]
  for choice in choices:matches.add((bi,choice,s))
  for w in r['witnesses']:frame_types[w[1]]+=1
  roots.add(rootpair(pi[0],s))
  records.append([bi,toggle,s,hm,sorted(r['witnesses']),r['forced_primal'],r['forced_dual']])
 assert roots<=coarse_roots
 counts['brooms']=len(brooms);counts['joint_nonnegative_graph_states']=len(records);counts['matching_cases']=len(matches);counts['joint_root_orbits']=len(roots)
 counts['coarse_cases']=len(coarse);counts['coarse_root_orbits']=len(coarse_roots)
 ur=sorted(root_pre);sr=sorted({min(a[s] for a in fperm) for s in range(9)})
 uremaining={min(a[u] for a in aut) for u,s in roots};sremaining={min(a[s] for a in fperm) for u,s in roots}
 return dict(id=m['id'],facets=M.faces,edges=sorted(M.edges),dual_facets=D.faces,automorphisms=aut,facet_automorphisms=fperm,
  root_pre_terminal=sorted(root_pre.items()),root_post_terminal=sorted(root_post.items()),brooms=brooms,
  counts=dict(counts),records=records,remaining_joint_roots=sorted(roots),coarse_joint_roots=sorted(coarse_roots),
  closed_U=[u for u in ur if u not in uremaining],closed_S=[s for s in sr if s not in sremaining],
  all_joint_roots=m['joint_root_representatives'])

def main():
 raw=Path('c32_catalogue.json').read_bytes();assert pin(raw)==CATPIN
 cat=json.loads(raw);assert cat['types']==296 and cat['joint_root_orbits']==21682
 rows=[];tot=Counter()
 if len(sys.argv)>1 and sys.argv[1]=='part':
  a,b=map(int,sys.argv[2:]);assert 0<=a<b<=296
  rows=[run_map(m) for m in cat['maps'][a:b]]
  Path('part_%03d_%03d.json'%(a,b)).write_bytes(serial(dict(parent=PARENT,range=[a,b],rows=rows)))
  print('PART_PASS',a,b,sum(r['counts']['joint_nonnegative_graph_states'] for r in rows));return
 if len(sys.argv)>1:
  assert sys.argv[1:] == ['join']
  for a in range(0,296,40):
   b=min(a+40,296);p=json.loads(Path('part_%03d_%03d.json'%(a,b)).read_bytes())
   assert p['parent']==PARENT and p['range']==[a,b] and [r['id'] for r in p['rows']]==list(range(a,b))
   rows.extend(p['rows'])
 else:
  rows=[run_map(m) for m in cat['maps']]
 for r in rows:tot.update(r['counts'])
 newU=[];newS=[];unconditional=[];newjoint=[];remainder=[];newwhole=[]
 for r in rows:
  k=r['id']
  if k in WHOLE:continue
  if not r['remaining_joint_roots']:newwhole.append(k)
  for u in r['closed_U']:
   if PARTIAL.get(k)!=u:newU.append([k,u])
  for s in r['closed_S']:newS.append([k,s])
  for u,n in r['root_post_terminal']:
   if n==0 and PARTIAL.get(k)!=u:unconditional.append([k,u])
  rem=set(map(tuple,r['remaining_joint_roots']))
  for u,s in r['all_joint_roots']:
   if PARTIAL.get(k)==u:assert (u,s) not in rem;continue
   (remainder if (u,s) in rem else newjoint).append([k,u,s])
 priorwhole=sum(len(r['all_joint_roots']) for r in rows if r['id'] in WHOLE)
 priorpartial=sum(sum(u==PARTIAL.get(r['id']) for u,s in r['all_joint_roots']) for r in rows if r['id'] not in WHOLE)
 assert priorwhole==868 and priorpartial==55
 assert len(newjoint)+len(remainder)+priorwhole+priorpartial==21682
 assert tot['brooms']==43234 and tot['actual_primal_tree_options']==57350 and tot['rooted_complements']==516150 and tot['five_shape_complements']==40008
 active=Counter()
 for r in rows:
  if r['id'] not in WHOLE:active.update(r['counts'])
 report=dict(tag='C32_ELEVEN_FRAME_INCIDENCE_FRONTIER_V1',parent=PARENT,catalogue_pin=CATPIN,
  inherited_whole_types=sorted(WHOLE),inherited_partial_U=sorted(PARTIAL.items()),trees=TREES,frames=FRAMES,graphs=COVER,
  primal_trees=PRIMAL,counts=dict(tot),counts_outside_inherited_whole=dict(active),
  new_unconditional_U=unconditional,new_target_U=newU,new_target_S=newS,new_whole_types=newwhole,
  prior_whole_joint_orbits=priorwhole,prior_partial_joint_orbits=priorpartial,
  newly_excluded_joint_roots=newjoint,remaining_joint_roots=remainder,maps=rows)
 out=serial(report);Path('joint_frontier.json').write_bytes(out)
 print('INDEPENDENT_DFS_AND_ALL_12870_EDGE_SUBSETS_PER_MAP_PASS',296,43234)
 print('ALL_TRUE_EDGE_PRIMAL_AND_DUAL_TRANSPORTS_MATCHINGS_PASS')
 print('COUNTS',json.dumps(dict(tot),sort_keys=True,separators=(',',':')))
 print('OUTSIDE_ACCEPTED_17',json.dumps(dict(active),sort_keys=True,separators=(',',':')))
 print('NEW_UNCONDITIONAL_U',unconditional)
 print('NEW_TARGET_U',len(newU),newU)
 print('NEW_TARGET_S',len(newS),newS)
 print('JOINT_ROOT_PARTITION',priorwhole,priorpartial,len(newjoint),len(remainder))
 print('NEW_WHOLE_TYPES',newwhole)
 print('GRAPH_SURVIVAL_NOT_PHYSICAL_ATTAINABILITY_NO_C34_CLAIM')
 print('REPORT',*pin(out));print('SOURCE',*pin(Path(__file__).read_bytes()))
if __name__=='__main__':main()
```

### 8.3 — `quotient_frontier.py`

```python
"""C32_ELEVEN_FRAME_CANONICAL_JOINT_QUOTIENT_V1.
CPython 3.13.5, stdlib; run after joint_frontier.py join:
python -S quotient_frontier.py > quotient_frontier.log
The complete generator and both exact inputs are supplied inline in the handoff.
"""
import json
from pathlib import Path
from collections import Counter
from joint_frontier import PARENT,CATPIN,WHOLE,PRIMAL,Map,serial,pin,outrows,graph_mask,rooted,code,CODES
assert __debug__
INPIN=[10444324,'4ddd4d8f8b33c502ceedb617ab7f1c75c5dd3b22dbca0d30a6235ef991df9e93']
b=Path('joint_frontier.json').read_bytes();assert pin(b)==INPIN
x=json.loads(b);assert x['parent']==PARENT and x['catalogue_pin']==CATPIN
rows=[];total=Counter();active=Counter()
def mask_image(mask,pi):
 return sum(1<<(9*pi[i]+pi[j]) for i in range(9) for j in range(9) if mask>>(9*i+j)&1)
def tree_image(p,pi):
 out=[0]*9
 for i in range(9):out[pi[i]]=pi[p[i]]
 return tuple(out)
for r in x['maps']:
 aut=r['automorphisms'];fa=r['facet_automorphisms'];M=Map(r['facets'])
 states={};branches={};zerochoices=set()
 for ri,(bi,toggle,s,hm,ws,fp,fq) in enumerate(r['records']):
  pi=r['brooms'][bi]
  ee=[(pi[i],pi[PRIMAL[0][i]]) for i in range(1,9)]
  if toggle:ee.append((pi[2],pi[8]))
  gm=graph_mask(outrows(ee))
  images=[(mask_image(gm,a),mask_image(hm,b)) for a,b in zip(aut,fa)];key=min(images)
  z=states.setdefault(key,dict(matches=set(),origins=set()))
  for ai,k in enumerate(images):
   if k!=key:continue
   a,b=aut[ai],fa[ai];z['origins'].add((ri,ai))
   for choice in {w[0] for w in ws}:
    p=[0]*9
    for i in range(9):p[pi[i]]=pi[PRIMAL[choice][i]]
    p1=tree_image(p,a);s1=b[s];z['matches'].add((p1,s1))
  for choice in {w[0] for w in ws}:
   p=[0]*9
   for i in range(9):p[pi[i]]=pi[PRIMAL[choice][i]]
   keyb=min((tree_image(p,a),b[s]) for a,b in zip(aut,fa))
   branches.setdefault(keyb,set()).add((ri,choice))
   if choice==0:zerochoices.add((bi,s))
 assert len(branches)==len(zerochoices)
 for (gm,hm),z in states.items():
  assert 1<=len(z['matches'])<=2
  for p,s in z['matches']:
   u=next(i for i in range(9) if p[i]==i)
   pe={tuple(sorted((i,p[i]))) for i in range(9) if i!=u}
   assert pe<=M.edges.keys() and all(i==u or gm>>(9*i+p[i])&1 for i in range(9))
   dp=rooted([tuple(M.edges[e]) for e in sorted(M.edges) if e not in pe],s)
   assert code(dp,s) in CODES and all(i==s or hm>>(9*i+dp[i])&1 for i in range(9))
 qstates=[[g,h,sorted(z['matches']),sorted(z['origins'])] for (g,h),z in sorted(states.items())]
 qbranches=[[p,s,sorted(orig)] for (p,s),orig in sorted(branches.items())]
 counts=dict(graph_orbits=len(states),matching_orbits=len(branches),two_matching_states=sum(len(z['matches'])==2 for z in states.values()))
 total.update(counts)
 if r['id'] not in WHOLE:active.update(counts)
 rows.append(dict(id=r['id'],counts=counts,states=qstates,matching_branches=qbranches))
assert total['graph_orbits']==90962 and total['matching_orbits']==24597
assert active['graph_orbits']==87519 and active['matching_orbits']==23640
assert total['two_matching_states']==0
gained=[]
for r in x['maps']:
 if r['id'] not in WHOLE:
  remaining=set(map(tuple,r['remaining_joint_roots']))
  gained.extend([r['id'],u,s] for u,s in r['coarse_joint_roots'] if (u,s) not in remaining)
assert len(gained)==65
# Small literal whole-root certificate, checked against the complete enumeration.
f62=[[0,1,3],[0,2,4,1],[0,3,6,7,5,2],[1,4,6,3],[2,5,4],[4,5,8],[4,7,6],[4,8,7],[5,7,8]]
r=x['maps'][62];assert r['facets']==f62
pi62=[(8,5,2,4,6,3,0,1,7),(8,5,2,4,6,3,1,0,7)]
assert [tuple(p) for p in r['brooms'] if p[0]==8]==pi62
M=Map(f62);dual_edges=[];profiles=[]
for pi in pi62:
 assert tuple(sorted((pi[2],pi[8]))) not in M.edges
 pe={tuple(sorted((pi[i],pi[PRIMAL[0][i]]))) for i in range(1,9)}
 de=sorted(tuple(sorted(M.edges[e])) for e in sorted(M.edges) if e not in pe);dual_edges.append(de)
 assert all(code(rooted(de,s),s) not in CODES for s in range(9))
 deg=Counter(v for e in de for v in e);profiles.append(sorted(deg.values()))
assert profiles==[[1,1,1,2,2,2,2,2,3],[1,1,1,1,2,2,2,2,4]]
proof62=dict(map=62,U=8,facets=f62,edges=sorted(M.edges),automorphisms=r['automorphisms'],
 terminal_brooms=pi62,dual_complement_edges=dual_edges,degree_profiles=profiles,stable_roots_checked=9)
assert x['new_unconditional_U']==[[k,3] for k in [40,50,102,108,109,113,114,137,191,240,260]]
assert len(x['new_target_U'])==66 and len(x['new_target_S'])==5
assert len(x['newly_excluded_joint_roots'])==7805 and len(x['remaining_joint_roots'])==12954
report=dict(tag='C32_ELEVEN_FRAME_CANONICAL_JOINT_QUOTIENT_V1',parent=PARENT,input_pin=INPIN,
 counts=dict(total),counts_outside_17=dict(active),new_unconditional_U=x['new_unconditional_U'],
 new_target_U=x['new_target_U'],new_target_S=x['new_target_S'],new_whole_types=x['new_whole_types'],
 newly_excluded_joint_roots=x['newly_excluded_joint_roots'],remaining_joint_roots=x['remaining_joint_roots'],
 literal_root62_certificate=proof62,new_cut_gain_over_coarse=gained,maps=rows)
out=serial(report);Path('quotient_frontier.json').write_bytes(out)
print('ALL_VERTEX_FACET_AUTOMORPHISM_AND_BOTH_MATCHING_TRANSPORTS_PASS')
print('COUNTS',json.dumps(dict(total),sort_keys=True,separators=(',',':')))
print('OUTSIDE_17',json.dumps(dict(active),sort_keys=True,separators=(',',':')))
print('ALL_ALT_BRANCHES_RETAINED_THEN_IDENTIFIED_BY_ACTUAL_RELABELING_PASS')
print('CANONICAL62_U8_TWO_COMPLEMENTS_ALL_NINE_S_ROOTS_EXCLUDED_PASS')
print('UNIQUE_COMPATIBLE_MATCHING_FOR_EVERY_PUTATIVE_C32_TARGET_PASS')
print('ADDITIONAL_JOINT_ROOTS_BEYOND_COARSE',len(gained))
print('JOINT_PARTITION',868,55,7805,12954)
print('NEW_UNCONDITIONAL_U',11,'NEW_TARGET_U',66,'NEW_TARGET_S',5,'NEW_WHOLE_TYPES',0)
print('GRAPH_ORBITS_NOT_PHYSICAL_ATTAINABILITY')
print('REPORT',*pin(out));print('SOURCE',*pin(Path(__file__).read_bytes()))
```

### 8.4 — `physical_cut_control.py`

```python
"""Actual C32 regression for the new cut/triangle/root tests; NOT a Gomboc.
CPython 3.13.5, stdlib only. python -S physical_cut_control.py
Uses the complete Map implementation supplied in joint_frontier.py.
Geometry inherited from C32_FOUR_TRIANGLE_FAN_PHYSICAL_BOUNDARY_V1,
minimum-0038 / de9cd99e6171b5909689e636d347b20d427f837b702d67eb007279b34f4fbaeb.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
from joint_frontier import Map,outrows,graph_mask,serial,pin
assert __debug__
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det3(a,b,c):return dot(a,cross(b,c))
def mm(a,b):return [[dot(r,c) for c in zip(*b)] for r in a]
def elim(a):
 a=[list(map(F,r)) for r in a];r=0;d=F(1)
 for j in range(len(a[0])):
  k=next((k for k in range(r,len(a)) if a[k][j]),None)
  if k is None:continue
  if k!=r:a[k],a[r]=a[r],a[k];d=-d
  z=a[r][j];d*=z;a[r]=[t/z for t in a[r]]
  for i in range(len(a)):
   if i!=r:
    z=a[i][j];a[i]=[t-z*w for t,w in zip(a[i],a[r])]
  r+=1
  if r==len(a):break
 return r,d,a
def det(a):
 r,d,_=elim(a);return d if r==len(a) else F(0)
def inv(a):
 n=len(a);_,_,b=elim([list(a[i])+[F(i==j) for j in range(n)] for i in range(n)])
 assert [r[:n] for r in b]==[[F(i==j) for j in range(n)] for i in range(n)]
 return [r[n:] for r in b]
P=[(0,0,0),(0,0,1),(0,1,0),(F(125249,249748),-F(499,249748),F(125249,249748)),
 (F(93812,155563),-F(499,155563),F(62375,155563)),(F(3,4),-1,F(3,4)),(1,0,0),
 (F(25449,19939),-F(26946,19939),F(7984,19939)),(F(3,2),-F(3,2),F(1,4))]
P=[tuple(map(F,p)) for p in P]
FAC=[[0,6,8],[0,2,6],[0,1,2],[0,5,1],[0,8,7,5],[2,3,4,6],[4,7,8,6],[1,5,7,4,3],[1,3,2]]
M=Map(FAC);D=Map(M.dual_faces);fs=set()
for i,j,k in combinations(range(9),3):
 n=cross(sub(P[j],P[i]),sub(P[k],P[i]))
 if not any(n):continue
 sl=[dot(n,sub(p,P[i])) for p in P]
 if (min(sl)<0<max(sl)) or not any(sl):continue
 fs.add(frozenset(a for a,s in enumerate(sl) if not s))
assert fs==set(map(frozenset,FAC))
def integrate(p,apex):
 v=F(0);mom=[F(0)]*3
 for f in FAC:
  for j in range(1,len(f)-1):
   a,b,c=[p[k] for k in [f[0],f[j],f[j+1]]]
   w=det3(sub(a,apex),sub(b,apex),sub(c,apex))/6;assert w>=0;v+=w
   for k in range(3):mom[k]+=w*(apex[k]+a[k]+b[k]+c[k])/4
 return v,tuple(t/v for t in mom)
v,g=integrate(P,(F(0),)*3)
assert (v,g)==integrate(P,tuple(sum(p[k] for p in P)/9 for k in range(3)))
assert v==F(743992554601211,1549322036088872)
X=[sub(p,g) for p in P];assert integrate(X,(F(0),)*3)==(v,(0,0,0))
Q=[];C=[];d=[]
for f in FAC:
 a,b,c=[X[i] for i in f[:3]];n=cross(sub(b,a),sub(c,a));h=dot(n,a);assert h>0
 q=tuple(t/h for t in n);Q.append(q)
 assert all(dot(q,X[j])==1 if j in f else dot(q,X[j])<1 for j in range(9))
 mass=F(0);mom=[F(0)]*3
 for j in range(1,len(f)-1):
  a,b,c=[X[i] for i in [f[0],f[j],f[j+1]]];w=det3(a,b,c);assert w>0;mass+=w
  for k in range(3):mom[k]+=w*(a[k]+b[k]+c[k])
 C.append(tuple(t/(3*mass) for t in mom));d.append(mass/(2*v))
L=[[d[j]*(1-dot(Q[i],C[j])) for j in range(9)] for i in range(9)]
assert sum(d)==3 and all(sum(row)==3 for row in L)
assert all(sum(d[i]*Q[i][k] for i in range(9))==sum(d[i]*C[i][k] for i in range(9))==0 for k in range(3))
assert [[sum(d[i]*C[i][j]*Q[i][k] for i in range(9)) for k in range(3)] for j in range(3)]==[[F(i==j) for j in range(3)] for i in range(3)]
LL=mm(L,L);assert all(LL[i][j]+L[i][j]==4*d[j] for i in range(9) for j in range(9))
assert mm(L,Q)==[[-t for t in q] for q in Q]
K=[[L[i][j]+F(i==j) for j in range(9)] for i in range(9)]
bad=det([r[:4] for r in K[:4]])
assert bad==-F(29225402286904272323120130050768458025941435,44476389385373086840084719020220335744901748548)
assert elim(L)[0]==4 and elim(K)[0]==6
controls=[]
for metric in [[[1,0,0],[0,1,0],[0,0,1]],[[2,1,0],[1,3,1],[0,1,2]]]:
 assert all(det([r[:k] for r in metric[:k]])>0 for k in range(1,4));reciprocal=inv(metric)
 GS=[[dot(X[i],mm([sub(X[j],X[i])],metric)[0]) for j in range(9)] for i in range(9)]
 HS=[[dot(Q[i],mm([sub(Q[j],Q[i])],reciprocal)[0]) for j in range(9)] for i in range(9)]
 G=outrows((i,j) for i in range(9) for j in range(9) if i!=j and GS[i][j]>=0)
 H=outrows((i,j) for i in range(9) for j in range(9) if i!=j and HS[i][j]>=0)
 assert M.cut_ok(G) and D.cut_ok(H)
 ph=M.projection(G,H);hp=D.projection(H,G);assert ph is not None and hp is not None
 assert all(HS[i][j]>0 for i,j in ph) and all(GS[i][j]>0 for i,j in hp)
 stable=[i for i in range(9) if all(HS[i][j]<0 for j in range(9) if i!=j)]
 unstable=[i for i in range(9) if all(GS[i][j]<0 for j in range(9) if i!=j)]
 assert all(M.no_dominator(G,s) for s in stable) and all(D.no_dominator(H,u) for u in unstable)
 controls.append(dict(metric=metric,reciprocal=reciprocal,primal_shadow_mask=graph_mask(G),dual_shadow_mask=graph_mask(H),
  stable=stable,unstable=unstable,forced_dual=ph,forced_primal=hp))
assert controls[0]['stable']==[0,3,4,7] and controls[0]['unstable']==[1,2,6,8]
def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [enc(v) for v in x]
 return x
report=dict(vertices=P,facets=FAC,edges=sorted(M.edges),volume=v,centroid=g,facet_area_centroids=C,
 omega=[z/3 for z in d],d=d,poles=Q,Lambda=L,negative_four_minor=bad,controls=controls)
b=serial(enc(report));Path('physical_cut_control.json').write_bytes(b)
print('ACTUAL_C32_HULL_TWO_VOLUME_INTEGRATIONS_ONE_LAMBDA_SQUARE_PASS')
print('ALL_NEW_CUT_PROJECTION_AND_ROOT_RULES_TWO_RECIPROCAL_METRICS_PASS')
print('PHYSICAL_NEGATIVE_FOUR_MINOR_RETAINED',bad)
print('REPORT',*pin(b));print('SOURCE',*pin(Path(__file__).read_bytes()))
```
