# figure-0041

AI research report · 2026-08-23 UTC

---

# Exact eight-vertex attack: orbit-complete fallback result

## Outcome

No strict eight-vertex homogeneous polyhedral Gömböc was found, and the eight-vertex case was not completely excluded. Consequently, this result **does not prove a nine-vertex lower bound**. The rigorous lower bound remains eight vertices.

The completed fallback deliverable is an orbit-complete exact partition of the eight-vertex search space:

- all 14 simplicial eight-vertex combinatorial types were independently enumerated;
- all 3,237,069 labeled root/tree/root-tetrahedron necessary systems were generated and mapped to rooted automorphism classes;
- 3,212,234 systems were excluded by exact positive-definite rational certificates;
- the remaining 24,835 labeled systems form 17,253 rooted automorphism orbits;
- every unresolved orbit is accompanied by a generator for its complete strict three-dimensional realization, uniform-volume centroid, stable-face, unstable-vertex, and no-saddle semialgebraic chambers.

The primary paper supplies the simplicial reduction, rooted shadow-tree inequalities, and root-cone tetrahedral moment framework on which this extension is based. The exact finite audit follows the transcript's requirement to compute the volume centroid by oriented tetrahedra and to check every face, vertex, edge, and convexity determinant with strict signs.

## Reusable files

- Fourteen exact combinatorial types (`v8_graphs.json`)
- Independent graph enumeration (`graph_enumeration.py`)
- Abstract base certificate partition (`v8_abstract_base.json`)
- Universal vertex-moment partition (`v8_universal_moment1.json`)
- Complete labeled-system mapping (`v8_actual_partition.json`)
- Graph-specific moment partition (`v8_actual_moment_partition.json`)
- Exact branch-key mapping (`v8_actual_branch_keys.json`)
- All 17,253 unresolved rooted orbits (`v8_unresolved_orbits.json`)
- Complete QF_NRA chamber generator (`generate_semialgebraic.py`)
- Independent exact partition verifier (`verify_v8_partition.py`)
- Saved full verification result (`verification_summary.json`)
- Constructive-search summary (`v8_constructive_search_summary.json`)
- Exact rational polyhedron verifier (`exact_polyhedron_verifier.py`)
- Adaptive two-level centroid-moment scanner (`adaptive2_scan_stream.py`)
- Adaptive-certificate rationalizer (`rationalize_adaptive2.py`)

## 1. Complete combinatorial enumeration

A simplicial polyhedron with eight vertices has 18 edges and 12 triangular faces. Two independent generation routes were used:

1. legal inverse vertex splits from the complete seven-vertex list;
2. complete traversal under legal edge flips, followed by graph-isomorphism reduction.

Both routes produce exactly **14** maximal-planar graph types. Their graph6 identifiers, face sets, edge sets, automorphism groups, and cross-generation witnesses are stored in `v8_graphs.json`.

The graph bundle's internal SHA-256 is

`94d4413cb30e95a3867399519669e1b6c2d21f6a127aa591804ee660617f5870`.

The standard simplicial perturbation is sufficient for the necessary mono-unstable reduction: any hypothetical strict eight-vertex Gömböc must first satisfy the unique-unstable-root conditions represented by this enumeration.

## 2. Exact shadow-tree and centroid-moment partition

Translate the true uniform-volume centroid to zero and normalize the candidate unstable root to

`r=(1,0,0)`.

For every rooted spanning tree, each nonroot vertex `i` has a selected parent `p(i)` and satisfies the shadow inequality

`(r_i-r_p(i))·r_i <= 0`.

Coning the root to the triangular faces not incident with it produces a positive-volume tetrahedral partition. If `Delta_T` is six times the oriented volume and

`S_T=sum_{v in T} r_v`,

the exact degree-four uniform-volume centroid identity is

`sum_T Delta_T S_T = 0`, with every `Delta_T>0`.

For every direction `d`, therefore,

`sum_T Delta_T (d·S_T)=0`,

so at least one root-cone tetrahedron obeys `d·S_T<=0`. Choosing `d` to be a vertex vector gives the vertex-moment disjunctions used in the exact partition.

Every branch consists of homogeneous or affine quadratic inequalities

`f_k(x)<=0`.

A stored certificate gives positive integer weights `w_k` for which the integer matrix representing

`sum_k w_k f_k(x)`

is positive definite. Thus the weighted sum is strictly positive for every coordinate vector, contradicting simultaneous nonpositivity. Positive definiteness is checked by exact fraction-free or rational elimination, not floating-point eigenvalues.

## 3. Exact accounting

| Stage | Exactly excluded labeled systems | Remainder |
|---|---:|---:|
| Complete eight-vertex enumeration | 0 | 3,237,069 |
| Base shadow/root-moment certificates | 3,122,005 | 115,064 |
| Universal vertex-moment hierarchy | 78,010 | 37,054 |
| Graph-specific one-vertex moment hierarchy | 12,219 | 24,835 |
| **Certified total** | **3,212,234** | **24,835** |

The final 24,835 labeled systems collapse under root-fixing graph automorphisms to **17,253 rooted orbits**. They yield **207,036 stable-face chambers**, because every simplicial type has 12 triangular faces.

The exact certificate classes comprise:

- 2,392 abstract base positive-definite certificates;
- 3,470 universal moment-branch certificates;
- 1,057 graph-specific moment-branch certificates.

The principal internal hashes are:

- complete actual partition: `e17d791bc234050c1556b239cf448a33dd9bf5b8ed7bf410b34a28da391c47ef`;
- graph-specific moment partition: `dec47278ebcc67777c37d7ae366891442e5469204ce7592d78b37285e8124112`;
- unresolved-orbit index: `28a35ebab97178bbfc37089d283473ab26828cdccc0978c2525c829e2b845dec`.

## 4. Independent exact verification

Running

```bash
cd /mnt/data/v8_complete_attack
python verify_v8_partition.py --full
```

performs a fresh enumeration of all 3,237,069 labeled systems, reconstructs every certificate matrix, checks every rooted automorphism mapping, and verifies the certified-versus-unresolved partition is disjoint and exhaustive.

The saved audit reports:

- full re-enumeration: passed;
- exact system total: 3,237,069;
- exact unresolved total: 24,835;
- unresolved rooted orbits: 17,253;
- stable-face chambers: 207,036;
- smallest exact positive LDL diagonal encountered:

`9056661687164/200819291871199 > 0`.

## 5. Fully specified systems for every unresolved orbit

For unresolved ID `u` and stable-face index `f`, run

```bash
python generate_semialgebraic.py u --stable-face f --out chamber.smt2
```

The emitted SMT-LIB system is exact `QF_NRA` and contains no floating-point constants. It uses 21 real variables after fixing the root to `(1,0,0)` and imposes all of the following:

1. **Actual three-dimensional convex realization.** Every one of the 12 oriented triangular faces has positive support, and every nonincident vertex lies strictly behind its plane.
2. **Positive root-cone topology.** Every tetrahedral determinant in the root-cone decomposition is strictly positive.
3. **Exact uniform-volume centroid.** The three degree-four equations `sum_T Delta_T S_T=0` are asserted coordinate by coordinate.
4. **The orbit's complete shadow tree.** All seven selected strict shadow inequalities are asserted.
5. **Unique unstable root.** Every true edge leaving the root has the strict downhill sign; each other vertex has a strict witness edge showing that it is not an unstable equilibrium.
6. **Exactly one stable face.** The chosen face has all three strict projection-inside signs, and every other face has a strict escaping-edge witness.
7. **No saddle edge.** For each of the 18 true edges, the system asserts a disjunction negating at least one of the four strict saddle conditions: interior projection parameter and the two positive adjacent-normal-cone coefficients.

Thus the unresolved index is not merely a list of relaxed shadow systems: it is an implementation-ready exact realization-and-equilibrium problem for every remaining chamber.

## 6. Constructive search

A topology-preserving differentiable search was run over every root/stable-face pair orbit of all 14 types:

- root/stable-face pair orbits: 573;
- optimizer trajectories: 6,560;
- strict candidates found: 0.

At every trajectory the uniform-volume centroid was recomputed from the oriented boundary integral, while all face, vertex, and convexity signs were optimized jointly. The best objective value was

`-0.0003011277720846817`

on graph type 7, but that point had minimum triangular area approximately

`8.30e-9`

and volume approximately

`8.13e-5`.

It is therefore a collapse/transfer-wall point, not an admissible near-certificate. This search result is negative empirical evidence only and is not used in the exact exclusion count.

## 7. New adaptive hierarchy discovered during this continuation

A stronger exact consequence was implemented after the orbit-complete partition.

Choose a shared direction

`d_alpha=sum_i alpha_i r_i`.

The centroid equation forces some first tetrahedron `T_1` with

`d_alpha·S_T1<=0`.

For each possible `T_1`, choose a branch-dependent second direction

`d_beta(T_1)=sum_i beta_i(T_1) r_i`.

The same centroid equation then forces some `T_2` with

`d_beta(T_1)·S_T2<=0`.

Every leaf `(T_1,T_2)` is again a finite quadratic system. If all leaves possess positive-definite weighted-sum certificates, the orbit is excluded. This adaptive rule is strictly stronger than using one common direction or testing one vertex direction at a time.

The implementation produced exact rational certificates for 12 of the first 20 diagnostic unresolved orbits, including several systems that resisted every single-direction test. The integer directions and all leaf matrices passed the same exact Fraction-LDL routine. However, the complete 17,253-orbit adaptive sweep and a separately implemented merged verifier were not completed, so these diagnostic exclusions are deliberately **not included** in the certified totals above.

## 8. Exact equilibrium audit for a future winner

`exact_polyhedron_verifier.py` accepts rational vertices and maximal oriented face cycles and checks:

- strict convexity and origin interiority;
- two-face incidence of every true edge and Euler topology;
- exact signed tetrahedral volume and first moment;
- all stable-face projection signs;
- all unstable-vertex edge derivatives;
- all saddle-edge projection and normal-cone signs;
- `S+U-H=2`;
- minimum positive and negative robustness margins.

Any numerical eight-vertex candidate must pass this verifier after rationalization before it can be called a homogeneous polyhedral Gömböc.

## Conclusion

The eight-vertex problem remains open in this result. What is closed is its complete finite front end: all combinatorial types and rooted necessary systems are enumerated, 3,212,234 of 3,237,069 systems are exactly excluded, and every one of the 24,835 remaining labeled systems has a fully specified exact realization-and-equilibrium chamber generator. No degeneracy or floating-point near-wall has been accepted as a figure.
