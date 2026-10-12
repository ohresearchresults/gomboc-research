# figure-0034

AI research report · 2026-08-22 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Pattern A resolved by a global exact obstruction

## Outcome

The assigned **stable-facet-preserving Pattern A cannot contain a homogeneous polyhedral Gömböc**. The obstruction is exact and global over

\[
r=\alpha n_9+\beta n_{11}+\gamma n_{13},\qquad \alpha>0,\ \gamma>0,\ \beta<0,
\]

and over **every** choice of positive nonincident supports, through every support-chamber transition and every higher-valence tie at the far endpoint of the relevant edge. It is therefore stronger than an interval exclusion on a normalized finite box.

The reason is not that the intended four-valent vertex fails. It is universally and strictly unstable, exactly as desired. The failure is that preserving facet 11 as the strict stable face forces a **new strict saddle on the true edge `(9,11)`**. Thus removing the old saddle pair `(9,13)` by making it a diagonal merely relocates the unavoidable saddle:

\[
F_{11}\text{ strict stable}\quad\Longrightarrow\quad H\ge 1.
\]

The same exact argument excludes the requested fallback **Pattern B**, with its forced saddle on edge `(1,11)`.

The inherited Reshetov data identify facet 11 as the unique stable face, the two forced unstable cones, and the original saddle pair `(9,13)`.

## 1. Exact reduction of Pattern A

Use the integer normals

```text
n9  = (-27,-85,-443)
n11 = (  0,181, 103)
n13 = ( 32,-394,-134)
```

and delete old facets 1 and 3. The concurrence equation is

\[
\alpha h_9+\beta h_{11}+\gamma h_{13}-h_r=0.
\]

Translate the common four-plane vertex to `O=0`. Then

\[
h_9=h_{11}=h_{13}=h_r=0,
\]

while every genuinely nonincident physical facet has positive support.

Three nominally retained old normals are exact positive combinations of `(n9,n11,n13)`:

\[
\begin{aligned}
n_2={}&\frac{253732}{230605}n_9+\frac{3813527}{922420}n_{11}+\frac{1712691}{1844840}n_{13},\\
n_4={}&\frac{312682}{230605}n_9+\frac{890743}{230605}n_{11}+\frac{220587}{230605}n_{13},\\
n_{12}={}&\frac{137792}{230605}n_9+\frac{683443}{230605}n_{11}+\frac{116262}{230605}n_{13}.
\end{aligned}
\]

Hence their inequalities are strict redundancies throughout the tangent cone and can never terminate an outgoing edge. The entire physical support problem reduces to the six cap normals

\[
J=\{5,6,7,8,10,14\}.
\]

After quotienting by overall scale, fixed-ray Pattern A has only five effective support degrees of freedom; varying the ray adds two coefficient ratios. The theorem below excludes this whole seven-dimensional open family when facet 11 is preserved as the strict stable face.

## 2. The four-valent common vertex is universally unstable

Let

\[
A=[n_9\ n_{11}\ n_{13}].
\]

Its Gram matrix and adjugate are

\[
A^TA=
\begin{pmatrix}
204203&-61014&91988\\
-61014&43370&-85116\\
91988&-85116&174216
\end{pmatrix},
\]

\[
\operatorname{adj}(A^TA)=
\begin{pmatrix}
311014464&2799964416&1203748064\\
2799964416&27113637704&11768386716\\
1203748064&11768386716&5133575914
\end{pmatrix}.
\]

Every adjugate entry is positive. For the body’s uniform-volume centroid `c`, interiority gives

\[
s=(-n_9\!\cdot c,-n_{11}\!\cdot c,-n_{13}\!\cdot c)^T>0.
\]

Therefore

\[
(\lambda,\mu,\nu)^T=(A^TA)^{-1}s>0,
\qquad -c=\lambda n_9+\mu n_{11}+\nu n_{13}.
\]

This is also strict interior membership in the **full four-ray** normal cone. For sufficiently small `epsilon>0`,

\[
-c=(\lambda-\epsilon\alpha)n_9+(\mu-\epsilon\beta)n_{11}+(\nu-\epsilon\gamma)n_{13}+\epsilon r,
\]

and all four coefficients are positive because `alpha,gamma>0>beta`. Thus `O` is strictly unstable under the correct nonsimple full-cone predicate for every allowed support and ray choice.

## 3. Global forced-saddle lemma

Let `a,b` be two incident zero-support facet normals whose intersection leaves `O` along a true edge `Oq`. Let a cap normal `m` terminate that edge at `q`, with `h=m·q>0`. Define the projections into `b^perp`

\[
\bar a=a-\frac{a\cdot b}{b\cdot b}b,
\qquad
\bar m=m-\frac{m\cdot b}{b\cdot b}b.
\]

Assume

\[
\frac qh=\kappa\bar a+\mu\bar m,
\qquad \kappa>0,\ \mu>0,
\]

and `a·b<0`. Let `p` be the orthogonal projection of the centroid onto facet `b`. If facet `b` is strictly stable, then `p` lies in the strict interior of its complete polygon, so

\[
a\cdot p<0,\qquad m\cdot p<h.
\]

Because `a·q=b·q=0` and `m·q=h`,

\[
q\cdot(p-q)=h\kappa\,a\cdot p+h\mu\,(m\cdot p-h)<0.
\]

Since `q` is perpendicular to `b`, `q·p=q·c`; hence `q·c<q·q`. Strict instability of `O`, tested on the true outgoing edge `Oq`, gives `q·c>0`. Therefore the centroid projection onto the edge line has parameter

\[
t=\frac{q\cdot c}{q\cdot q}\in(0,1).
\]

At `z=tq`, the vector `z-c` is perpendicular to `q`, hence belongs to `span(a,b)`, and

\[
a\cdot(z-c)=-a\cdot c>0,
\qquad
b\cdot(z-c)=-b\cdot c>0.
\]

The inverse of the pair Gram matrix is entrywise positive when `a·b<0`, so `z-c` is a strict positive combination of `a,b`. Thus `z` is a **strict saddle equilibrium in the relative interior of the true edge**. No triangulation diagonal is involved.

## 4. Applying the lemma to every Pattern A support chamber

Take

\[
a=n_9,\qquad b=n_{11}.
\]

The intersection `(9,11)` is always a genuine outgoing cone edge: in its feasible direction,

\[
n_{13}\cdot q<0,
\qquad
r\cdot q=\gamma\,n_{13}\cdot q<0.
\]

Moreover,

\[
n_9\cdot n_{11}=-61014<0.
\]

Boundedness forces the edge to terminate at one or more normals in `J`. For each possible terminator `j`, normalize `q_j` by

\[
n_9\cdot q_j=n_{11}\cdot q_j=0,
\qquad n_j\cdot q_j=1.
\]

The exact projected-normal coefficients are:

| `j` | `kappa_j` | `mu_j` |
|---:|---:|---:|
| 5 | `1870739387/115186560392` | `2566787957/115186560392` |
| 6 | `2121068531/1173006494450` | `2566787957/1173006494450` |
| 7 | `85382217/77861682962` | `2566787957/1946542074050` |
| 8 | `2551/1388016` | `2566787957/1035970725888` |
| 10 | `17857/4621860` | `2566787957/234420739200` |
| 14 | `35714/15421995` | `2566787957/652504608450` |

Every entry is strictly positive. If several caps tie at the endpoint, choose any active terminator; the same proof applies. Consequently

\[
\boxed{F_{11}\text{ strict stable in Pattern A}\Longrightarrow (9,11)\text{ is a strict saddle edge}.}
\]

Hence no member of the assigned Pattern A chamber can have `S=1,U=1,H=0` while preserving facet 11 as the stable face.

## 5. Pattern B is excluded by the same exact mechanism

Pattern B deletes old facets 9 and 13 and uses

\[
r_B=\alpha n_1+\beta n_{11}+\gamma n_3,
\qquad \alpha,\gamma>0>\beta,
\]

with concurrence equation

\[
\alpha h_1+\beta h_{11}+\gamma h_3-h_{r_B}=0.
\]

For the basis `(n1,n11,n3)`,

\[
\operatorname{adj}(A_B^TA_B)=
\begin{pmatrix}
1605805145&6392975520&3254205880\\
6392975520&25627220145&13037169255\\
3254205880&13037169255&6644872970
\end{pmatrix}>0
\]

entrywise, so its common four-valent vertex is again universally unstable in the full cone. The unavoidable true edge is `(1,11)`, with

\[
n_1\cdot n_{11}=-29560<0.
\]

Normals `2,4,12` are again exact positive combinations of the common basis. For every remaining possible terminator `j in {5,6,7,8,10,14}`, the projected endpoint coefficients are strictly positive; the complete rational table is stored in the theorem certificate and independently recomputed by the verifier. Therefore

\[
\boxed{F_{11}\text{ strict stable in Pattern B}\Longrightarrow (1,11)\text{ is a strict saddle edge}.}
\]

Pattern B also cannot be a stable-facet-preserving homogeneous polyhedral Gömböc.

## 6. Correct equilibrium audit and exact reconstructed lattices

The verifier applies the required predicates directly:

- a polygonal face is stable only when the centroid projection lies in the strict relative interior of the **complete face cycle**;
- a vertex of any valence is unstable only when every true outgoing edge satisfies `-(w-v)·(v-c)>0`, equivalently `v-c` lies in the strict interior of the full normal cone;
- a saddle is audited only on a **true physical edge**, requiring an interior line projection and a strict positive combination of its two incident facet normals.

Two exact rational witnesses are included to exercise the entire reconstruction and audit pipeline. They are not claimed as Gömböcs.

### Pattern A exact witness

```text
physical normals: 5,6,7,8,9,10,11,13,14,r_A
supports:         30,36,47,31,0,13,0,0,23,0
r_A = n9-n11+n13 = (5,-660,-680)
(V,E,F) = (15,23,10)
(S,U,H) = (3,2,3)
common incidence = (9,11,13,r_A)
forced saddle = edge [0,3], facets (9,11)
exact centroid ≈ (-0.7054786375639266,-0.05682061026363991,0.07272020116065107)
```

The certificate stores the exact rational centroid, all 15 rational vertices, all ten complete polygon cycles, all 23 true edges, exact volume, every face sign, every full-cone vertex sign, and every edge coefficient.

### Pattern B exact witness

```text
listed normals:  1,3,5,6,7,8,10,11,14,r_B
supports:        0,0,30,36,47,31,13,0,23,0
r_B = n1-n11+n3 = (-7,-500,-515)
true (V,E,F) = (5,8,5)
(S,U,H) = (4,2,4)
forced saddle = edge [0,4], facets (1,11)
exact centroid ≈ (0.6545142205581712,-0.03053594812230316,0.03905928911392113)
```

The independent verifier does not trust stored incidences or equilibrium labels. It re-enumerates every feasible triple intersection, reconstructs the active face lattice, orders complete polygons, reconstructs true edges, recomputes exact volume and centroid, and audits every face, vertex, and edge in SymPy rational arithmetic. Its terminal status is `ALL EXACT CHECKS PASSED`.

## 7. Search outside the theorem’s exact scope

A topology-changing search also allowed the stable equilibrium to migrate away from facet 11. It varied six positive cap supports and both ray-coefficient ratios, rebuilt the actual nonsimple lattice after every evaluation, recomputed the uniform centroid, and audited complete polygons, full-valence vertices, and true edges.

A broad 20,000-sample run found no `S=1,U=1,H=0` point. Local maximin refinement ended at

\[
(V,E,F)=(7,11,6),\qquad (S,U,H)=(2,2,2),
\]

with score about `-0.3212709273`. This is empirical evidence only. It is **not** a global exclusion of the larger stable-migration family.

## 8. Reusable artifact package

- Complete package (`patternA_patternB_exact_exclusion.zip`) — SHA-256 `63a3f34a90becf06eedb3a9f3636c2524c33aca77764c73b4527b4b7d0de7f0a`.
- Full report (`REPORT.md`).
- Machine-readable global theorem certificate (`global_forced_saddle_certificate.json`).
- Independent exact verifier (`verify_forced_saddle.py`) and recorded output (`VERIFICATION_OUTPUT.txt`).
- Pattern A exact lattice certificate (`patternA_integer_witness.json`) and OBJ (`patternA_integer_witness.obj`).
- Pattern B exact lattice certificate (`patternB_integer_witness.json`) and OBJ (`patternB_integer_witness.obj`).
- Topology-changing search/auditor (`patternA_search.py`), ray/support optimizer (`patternA_opt.py`), and 20,000-sample search record (`patternA_20000_random_search.json`).
- Fresh SHA-256 manifest (`manifest_sha256.json`).

## Final status

No homogeneous polyhedral Gömböc is claimed. The assigned smallest stable-facet-preserving Pattern A route is **closed globally and exactly**, and the requested Pattern B fallback is closed by the same mechanism. The active obstruction is structural: preserving facet 11 as stable forces an incident saddle on an adjacent true edge, even though the original pair `(9,13)` has been removed from the edge set.
