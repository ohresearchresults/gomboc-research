# figure-0025

AI research report · 2026-08-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
>
> The exclusion claimed here is restricted to the specified 14-normal, 24-vertex Reshetov support cell.
<!-- historical-status:end -->

---

# Exact global attack: completed exclusion theorem

## Outcome

No strict homogeneous polyhedral Gömböc was found. The completed reusable artifact is instead a **global exact exclusion** of the full Reshetov 14-normal, 24-vertex support cell, plus the exact centroid system and a complete finite certificate stack. This is not another local optimizer result. The supplied transcript shows the recurring failure mode that motivated the change: equilibria transferred to neighboring elements or disappeared only at topology/degeneracy walls, and the last candidate still lacked a strict certificate.

### Certified theorem

Let

\[
P(h)=\{x\in\mathbb R^3:n_i\cdot x\le h_i,\ i=1,\ldots,14\}
\]

use the fourteen Reshetov normals and the prescribed simple fan listed below. For **every** support vector preserving the strict nonincidence cone of that fan, and for **every** interior reference point \(o\), \(P(h)\) cannot have exactly one strict unstable vertex relative to \(o\). Hence every nondegenerate member has \(U=0\) or \(U\ge2\), and the cell contains no homogeneous polyhedral Gömböc.

This is stronger than a homogeneous exclusion: the proof does not use the centroid equations, so even an arbitrarily chosen interior mass point cannot make this cell mono-unstable.

## Finite semialgebraic/SAT formulation

For a prescribed simple vertex \(I=\{i,j,k\}\), with \(N_I\) the matrix whose rows are \(n_i,n_j,n_k\),

\[
v_I(h)=N_I^{-1}h_I.
\]

The strict topology constraints are rational linear forms

\[
C_{I,r}(h)=h_r-n_r\cdot v_I(h)>0\qquad(r\notin I).
\]

For one fixed oriented boundary triangulation \(T\), exact volume and first moment are

\[
6V(h)=\sum_{(a,b,c)\in T}\det(v_a,v_b,v_c),
\]

\[
24M(h)=\sum_{(a,b,c)\in T}\det(v_a,v_b,v_c)(v_a+v_b+v_c).
\]

Thus \(V\) is cubic, each component of \(M\) is quartic, and uniform-density centering is exactly

\[
M_x=M_y=M_z=0,\qquad V>0.
\]

After translating an arbitrary interior point \(o\) to the origin, set \(g_i=h_i-n_i\cdot o>0\). Face \(i\) is stable iff

\[
L^F_{ij}(g)=\lVert n_i\rVert^2g_j-(n_i\cdot n_j)g_i>0
\quad(j\ne i).
\]

For a simple vertex \(I\), define

\[
\lambda_I(g)=N_I^{-T}N_I^{-1}g_I.
\]

It is strictly unstable iff all three components are positive; strict exclusion is the SAT clause

\[
\lambda_{I,1}<0\ \lor\ \lambda_{I,2}<0\ \lor\ \lambda_{I,3}<0.
\]

For an edge incident to planes \(i,j\), with \(A=[n_i^T;n_j^T]\), its minimum-norm line point is

\[
q_{ij}=A^T(AA^T)^{-1}(g_i,g_j)^T=\alpha n_i+\beta n_j.
\]

Normal-cone membership is \(\alpha>0,\beta>0\); if the endpoints are \(v_I,v_J\) and \(d=n_i\times n_j\), segment membership is \((d\cdot v_I)(d\cdot v_J)<0\). Hence every face, vertex, and edge condition is a finite Boolean combination of rational polynomial signs.

## Exact chosen cell and best concrete object

Normals:

```text
n1=(19,70,-410); n2=(0,289,-186); n3=(-26,-389,-2); n4=(-6,207,-331); n5=(13,-329,101); n6=(1,-167,233); n7=(-5,-263,181); n8=(0,-73,253); n9=(-27,-85,-443); n10=(0,107,201); n11=(0,181,103); n12=(0,287,-27); n13=(32,-394,-134); n14=(0,18,244)
```

Reference supports \(h_i=\lVert n_i\rVert^2\):

```text
(173361, 118117, 152001, 152446, 118611, 82179, 101955, 69338, 204203, 51850, 43370, 83098, 174216, 59860)
```

Prescribed vertex triples:

```text
(1,2,4), (5,6,7), (3,5,7), (6,7,8), (3,7,8), (5,6,8), (1,4,9), (3,10,11), (3,9,11), (1,11,12), (9,11,12), (4,9,12), (2,4,12), (1,2,12), (10,11,13), (1,11,13), (1,9,13), (3,9,13), (3,5,13), (10,13,14), (5,13,14), (5,8,14), (3,8,14), (3,10,14)
```

This H-representation is already a complete exact coordinate specification: each of the 24 rational vertices is \(N_I^{-1}h_I\). The expanded 24-coordinate list is in the exact seed certificate.

The seed has

\[
F=14,\quad V=24,\quad E=36,\qquad(S,U,H)=(1,2,1),
\]

with stable face 11, unstable vertices 9 and 16, and saddle edge \((17,18)\). Key strict margins are:

```text
minimum topology slack: 274691282/117383 = 2340.1283150030245...
stable face 11 projection margin: 17323.706735954107...
unstable vertex 9 minimum lambda: 120.93591513931985...
unstable vertex 16 minimum lambda: 47.65324934369530...
saddle edge normal-cone coefficients: 0.5712108637815968..., 0.7000766473737112...
saddle edge endpoint parameters: -98295457.760704741..., +62798417.805633895...
```

The seed uniform-volume centroid is approximately

\[
(-104.1014775785565,\ 8.465022473324968,\ -47.56244776570032).
\]

The exact seed certificate (`reshetov_seed_exact_certificate.json`) contains all 24 rational coordinates, all 264 topology slacks, exact volume and centroid, all face inequalities, all 72 vertex coefficients, all 36 edge tests, and the final classification. A visualization-only OBJ (`reshetov_seed_nearmiss.obj`) is also included.

## Exact DPLL(LRA)/Farkas exclusion

Normalize

\[
g_i=\lVert n_i\rVert^2q_i,\qquad q_i>0,\qquad\sum_iq_i=1.
\]

For a proposed unique unstable target \(u\), introduce a common strict margin \(t\) and require

\[
q_i\ge t,\quad C_{I,r}(q)\ge t,\quad\lambda_{u,k}(q)\ge t,
\]

while each non-target vertex chooses one disjunct \(\lambda_{v,k(v)}(q)\le-t\). A strict realization exists iff some branch has \(t>0\).

At a DPLL leaf the problem is linear: maximize \(t\) subject to \(A(q,t)\le0\) and \(E(q,t)=1\). The certificate gives exact rational multipliers \(y\ge0,z\le0\) with

\[
A^Ty+E^Tz=e_t.
\]

Therefore every feasible point satisfies

\[
t=y^TA(q,t)+z\le z\le0,
\]

so the leaf cannot contain a strict solution.

Complete proof statistics:

```text
24 target roots
24 internal DPLL nodes
72 Farkas leaves
806 nonzero exact rational multipliers
0 uncertified leaves
```

Vertex 9 blocks every target except target 9; vertex 16 blocks target 9. All three possible exclusion components of the blocking vertex are separately refuted.

Exact certificate (`reshetov_exact_unsat_certificate.json`) — SHA-256 `9bd0afc9c27619de43477c4d8b488b163bcce2919b5762f721d3cc63c0a21147`.

## Exact centroid system

The sparse polynomial file (`reshetov_centroid_quartics.json`) contains:

```text
6V: 106 degree-3 monomials
24M_x: 190 degree-4 monomials
24M_y: 176 degree-4 monomials
24M_z: 176 degree-4 monomials
```

The coefficient verifier (`verify_reshetov_centroid_coefficients.py`) reconstructs every coefficient independently from the integer normals, triples, and face cycles using only `fractions.Fraction`. The direct evaluator (`verify_reshetov_centroid_polynomials.py`) compares the sparse polynomials with tetrahedral formulas at three rational support vectors. Polynomial SHA-256: `066108a509ebcc1a19132efc4a160bb9065c4e1e8d7cd67878568c1c99fd94b4`.

## Enumeration log

The HiGHS mixed-integer precursor solved every target pair:

```text
14 stable-face choices x 24 unstable-vertex choices = 336 cases
117,866 branch-and-bound nodes
all statuses optimal
largest maximin margin = 0
runtime = 188.4641385 s
```

The reduced 24-case mono-unstable model already had optimum zero for every target, exposing the stronger obstruction. Numerical output was used only to discover the compact exact proof. Reproducible files: results (`RESH_ALL_PAIRS.json`), solver log (`resh_all_pairs.log`), and DPLL summary (`reshetov_dpll_summary.csv`).

## Exact validation and package

Run:

```bash
cd /mnt/data/gomboc_global_sat_attack
./[internal-source-reference].sh
```

Checked output:

```text
EXACT CERTIFICATE VERIFIED
targets: 24
internal DPLL nodes: 24
Farkas leaves: 72
nonzero exact multipliers checked: 806
arithmetic: fractions.Fraction only

EXACT CENTROID COEFFICIENTS VERIFIED
comparison: coefficient-by-coefficient
terms: {'V6': 106, 'M24_x': 190, 'M24_y': 176, 'M24_z': 176}

EXACT CENTROID POLYNOMIALS VERIFIED
tests: 3
arithmetic: fractions.Fraction only

EXACT SEED CERTIFICATE REGENERATION MATCHED BYTE-FOR-BYTE
```

Complete package (`gomboc_global_sat_attack.zip`), SHA-256 `662dfb8a5a45a37372f9882a4554a12d03caad4054d503fc416c8aaa34cc217b`. See the README (`README.md`), verification log (`PACKAGE_VERIFICATION.log`), and manifest (`MANIFEST.sha256`).

## Consequence and next frontier

Optimizing only the fourteen supports inside this fan is now provably futile: no centroid solution can overcome the already-impossible \(U=1\) mechanics. A successful search must change a normal direction or cross a combinatorial wall.

The next global run should enumerate one-ridge-flip, truncation, stacking, and local basin-replacement fans adjacent to the exact extra maximum-saddle pair. For each topology: build the rational realization cone; run the unique-unstable DPLL filter first; add stable-face and edge clauses to surviving Boolean cells; solve the three centroid quartics by interval branch-and-bound and interval Newton/Krawczyk; then rationalize and exact-certify any positive-margin witness.

The explicit 21-vertex Conway object is a point-mass/0-skeleton construction rather than a uniform-volume example, and the exact homogeneous Conway-spiral family is separately ruled out in the source literature.

## Limit

The requested figure itself remains unfound outside the excluded cell. The theorem covers strict nondegenerate realizations; boundary points with \(t=0\) change topology or contain degenerate equilibria and are not certified \((1,1)\) objects.
