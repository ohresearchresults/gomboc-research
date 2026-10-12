# figure-0115

AI research report · 2026-08-27 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Calm Lynx 78 — exact equatorial four-star / 2×2 zipper handoff

## Verdict

**No homogeneous polyhedral Gömböc was obtained.** I did construct and certify the requested half-turn-paired equatorial incidence relay, rebuild the full 4,324-row face lattice on both sides, retain the three distributed support modes as the dependent moment variables, and isolate a unique exact zero of all three ordinary first moments. The exact centred post-relay body is a rigorous nonwinner with

\[
(S,U,H)=(291,305,594).
\]

The decisive new result is the **first exact obstruction after the minimal relay**. The four-circuit zipper moves both inherited wall amplitudes from

\[
a_{\rm old}=0.0020519910920605389321\ldots
\]

to

\[
a_{\rm moved}=0.0035941679821085554721\ldots,
\]

but the rebuilt post-event cell creates an earlier half-turn-paired outer wall at

\[
a_{\rm outer}=0.00051155200057407094350\ldots.
\]

At the strict post-event sample `a=1/512`, that outer relay consists of stable rows `2219,2201`, unstable facets `(2219,2220,2255)` and `(2201,2202,2237)`, and saddle edges `(2184,2219)`, `(2219,2255)`, `(2166,2201)`, `(2201,2237)`. The two new unstable facets use only fixed boundary rows, so their exact positive barycentric coefficients are independent of the tangential null coordinate throughout this incidence cell. Thus the requested minimal four-star zipper is now closed as a construction-centre-preserving route; a larger cell must move rows of the outer boundary facets themselves.

The target and acceptance gate were the exact own-centroid, uniform-density, finite-object requirements recorded in the supplied journal. The journal had localized the predecessor obstruction to the paired equatorial rows and proposed this four-star relay.

## 1. Exact reconstruction of the predecessor cover and first wall

The normative predecessor input is `data/original_source_rows_modes.hex`. Each hexadecimal binary64 token is interpreted as its exact dyadic rational. It contains 4,324 polar source rows `q_i^0` and the three distributed mode values `F_i`.

At `t=(0,0,0)`, the independently rebuilt body has:

- 4,324 irredundant H rows;
- 8,644 maximal triangular dual faces / primal vertices;
- 12,966 true edges;
- 4,324 maximal primal faces;
- 17,284 oriented surface triangles;
- unique stable row `0`;
- unique unstable terminal facet on rows `{4321,4322,4323}`;
- no saddle edge;
- exact/directed class `(1,1,0)`.

The directed mass data are

```text
V = 4.20108007651937279616332264275155543
M = ( 0.126043494939438717341485663546899833,
     -3.51047663153281293921555062375078091e-13,
     -3.02648270021214512683463240100785868e-12 )
c = ( 0.0300026404266654026260473759902062426,
     -8.35612882304607216447381362841581399e-14,
     -7.20405858752306705996243240130019691e-13 )
```

The minimum directed inactive-incidence numerator is greater than `1.468921317915317e-9`. The construction-centre equilibrium margins include stable primitive `9.4628108434300158e-4`, terminal unstable numerator `0.36500711551672077`, closest excluded stable primitive `-3.5445701325708442e-6`, and closest excluded saddle component `-6.6736322550045730e-4`.

On the direct axis family `t=(-a,0,0)`, the exact stable-exclusion primitive is

\[
E_{ij}(a)=u_j-r_{ij}u_i=(1-r_{ij})+a(r_{ij}F_{i0}-F_{j0}),
\qquad
r_{ij}=\frac{q_j^0\cdot q_i^0}{\|q_i^0\|^2}.
\]

The first exact zero is `(i,j)=(2184,2149)`:

```text
a1 = 8164249234989496014501371756908122616312627200
     /3978696236342448017364815083047135797794086977207
   = 0.00205199109206053893212444239862013967807118958...
```

The binary64-asymmetry mate `(2166,2131)` follows at

```text
a2 = 0.00205199109206058570070237674195563555820755190...
```

with separation about `4.6768577934343e-17`. Exact directed audits give

```text
before a1       (S,U,H)=(1,1,0)
between a1,a2   (S,U,H)=(2,1,1)
after a2        (S,U,H)=(3,1,2)
```

and at `a1`, `93.68866108527486%` of the original positive x moment remains. `src/verify_original_cover_cleanroom.py` independently reconstructs the hull and checks every exact wall fraction in `certificates/original_first_wall_exact.json`.

## 2. Complete four-star support replacement

Rows `1..4320` are 120 rings of 36. The northern complete-star patch is

```text
[2148,2219,2255,2220,2185,2114,2078,2113,2149,2184]
```

and its exact half-turn image under `R=diag(1,-1,-1)` is

```text
[2130,2201,2237,2202,2167,2096,2060,2095,2131,2166].
```

All 20 exact support rows, their ring positions, original values, rebuilt half-turn values, post-zipper values, and unchanged distributed modes are expanded in `data/relay_support_rows.json`. The complete pre/post link cycles and every incident facet of all four target rows are in `certificates/complete_star_replacement.json`.

Ten southern rows are replaced by exact half-turn values rather than merely treated as approximately symmetric:

```text
2060,2095,2096,2130,2131,2166,2167,2201,2202,2237.
```

The circuit event then changes rows `2184` and `2166` in exact half-turn lockstep.

## 3. Exact relay family, tangential freedom, and circuit equations

Fix the exact support amplitude

\[
a_0=1/512,\qquad u_i=1-a_0F_{i0}.
\]

Let `d` be the exact minimum-norm solution of the two northern circuit equations and let `n_tan` be the exact null direction `g_1×g_2`, scaled so its largest absolute component is one. Both are stored as exact rational triples in `certificates/relay_circuit_exact.json`. Define

\[
q_{2184}(s,\tau)=q_{2184}^{\rm pre}+s(d+\tau n_{\rm tan}),
\qquad
q_{2166}(s,\tau)=R q_{2184}(s,\tau).
\]

The two northern circuits are

```text
C1 = {2113,2148,2149,2184}
C2 = {2219,2220,2255,2184}
```

and the exact half-turn mates are

```text
C1' = {2095,2130,2131,2166}
C2' = {2201,2202,2237,2166}.
```

Writing each circuit determinant using the augmented rows `(q_i,u_i)`, the exact equations are

\[
\Delta_k(s,\tau)=D_k(0)(1-s),
\]

independent of `tau`, because `g_k·n_tan=0` exactly. The two northern constants are

```text
D1 =  841587926845943345477361429212883519599403815424962683074539297
      /1725436586697640946858688965569256363112777243042596638790631055949824
   ≈  4.87753611656445109138e-7

D2 = -1653010973553907857245954432708633361869923261202098160164768625
      /3450873173395281893717377931138512726225554486085193277581262111899648
   ≈ -4.79012380489059177711e-7.
```

All four circuits are coplanar at the single connected event `s=1`, for every tangential `tau`. The certified finite post sample uses

```text
s = 17/16, tau = 0,
q_2184 = (0x1.91d29c0414199p-8,
         -0x1.3b778cb887781p-4,
          0x1.fe6bfd4048c8bp-1),
q_2166 = diag(1,-1,-1) q_2184.
```

The exact pre/post determinant ratios are approximately `-0.06250000000048`, so the dyadic rounded sample is strictly beyond every circuit wall. An exact coordinatewise relay radius of

```text
5.6115342142524477923928402935051623e-6
```

preserves the strict side of all four circuit determinants under symmetric perturbation of `q_2184` and its half-turn mate.

## 4. Rebuilt relay topology

The event removes exactly these eight triangular dual facets:

```text
(2095,2130,2166)
(2095,2131,2166)
(2113,2148,2184)
(2113,2149,2184)
(2166,2201,2237)
(2166,2202,2237)
(2184,2219,2255)
(2184,2220,2255)
```

and inserts exactly:

```text
(2095,2130,2131)
(2113,2148,2149)
(2130,2131,2166)
(2148,2149,2184)
(2166,2201,2202)
(2184,2219,2220)
(2201,2202,2237)
(2219,2220,2255).
```

Both sides retain all 4,324 irredundant rows, 8,644 dual facets/primal vertices, 12,966 true edges, and 17,284 oriented surface triangles. This is a genuine synchronized four-circuit incidence change, not a support-only deformation or a triangulation-diagonal bookkeeping artifact.

## 5. Exact pre/post mechanical audit and the first new obstruction

At `a=1/512`, before the circuit event, the rebuilt half-turn cover is fully certified as

```text
(S,U,H) = (1,1,0)
stable rows = [0]
terminal unstable facet remains unique
saddles = []
minimum inactive numerator > 1.468921317915317e-9
```

After the four circuits cross, the exact rebuilt class is

```text
(S,U,H) = (3,3,4)
stable rows = [0,2201,2219]
extra unstable facets = (2201,2202,2237), (2219,2220,2255)
saddles = (2166,2201), (2184,2219), (2201,2237), (2219,2255)
```

The exact positive lower margins are

```text
new stable primitive       1.06994631460768813810584160675767e-4
new unstable numerator     7.72287805364381865419351045422574e-2
new saddle component       7.6064864723894782082608742680455e-2
minimum inactive numerator 1.468921317915317e-9
```

The relay does accomplish the intended original-wall motion. For both `(2184,2149)` and `(2166,2131)`, the direct-axis zero moves by the exact factor

```text
1.75155145459204479699551744435477...
```

from `0.0020519910920605389...` to `0.0035941679821085555...`; at `a=1/512` the exact primitive is

```text
-0.000122158993126257951744444124530211646...
```

on both halves. But the new outer rows have exact positive primitives

```text
E_(2219,2184) = E_(2201,2166)
              = 0.000106994631460768813810584160675767468...
```

and their direct-axis zero is the earlier `0.00051155200057407094350...` quoted above.

More decisively, the new unstable facets consist only of fixed boundary rows. Their exact minimum positive coefficient is

```text
0.0772287805364381865419351045422573642...
```

and does not depend on the tangential null coordinate `tau` while this post-event facet set is retained. Hence the minimal cell cannot remain `(1,1,0)` at the construction centre, even though the original paired wall has been moved.

All exact fractions, not just the displayed decimals, are in `certificates/relay_local_exact_primitives.json`.

## 6. Exact distributed three-mode moment closure

The post-relay exact finite family is

\[
u_i(t)=1+F_i\cdot t,
\qquad
P(t)=\{x\in\mathbb R^3:q_i^0\cdot x\le u_i(t)\}.
\]

The 4,324 post-relay rows `q_i^0` and all 12,972 mode entries are exact dyadics in `data/source_rows_modes.hex`. Inside a fixed simplicial polar cell, every primal vertex is exactly affine in `t`,

\[
p_T(t)=(Q_T^0)^{-1}u_T(t),
\]

so volume is cubic and each ordinary first moment is quartic with rational coefficients.

The three-by-three moment Jacobian is nonsingular. On the initial root box the directed determinant is

```text
[41.0878203996781166239455072934817429,
 41.0878203996781166239455072934817429].
```

A 180-bit outward fixed-dyadic Krawczyk computation isolates one and only one root. Its first image is

```text
t0 in [-0.0325691050103571576932593315136573821,
       -0.0325691050103571576932593315070624974]

t1 in [ 1.01630992894526119441115119874105960e-13,
        1.01630992894526120809285131562055554e-13]

t2 in [ 9.25217200982280362362078506726711656e-13,
        9.25217200982280362894203676805739696e-13].
```

The second Krawczyk image has widths approximately

```text
(2.06e-41, 1.74e-41, 1.83e-41).
```

On the first image,

```text
V in [4.17955664249039591844635944825083433,
      4.17955664249039591844635948863142970]

Mx in [-7.60447473439784e-27,  7.60511902694073e-27]
My in [-7.94500169272897e-27,  7.94508747689552e-27]
Mz in [-7.93558184064139e-27,  7.93592580876005e-27].
```

The strict Krawczyk inclusion proves an exact zero of all three ordinary first moments. Therefore the construction centre is exactly the body's own uniform-volume centroid at that unique root. The distributed modes have been used as the three dependent variables; the exact tangential relay coordinate remains the independent geometric coordinate, with this artifact certifying the `tau=0` section.

## 7. Exhaustive own-centroid H/V and equilibrium audit

Over the entire Krawczyk image:

```text
H rows                         4,324, all irredundant
maximal triangular dual faces 8,644
primal vertices               8,644
true edges                   12,966
maximal primal face cycles    4,324
oriented surface triangles   17,284
class                    (291,305,594)
```

Every maximal face, every vertex, and every true edge's full four-component normal cone is decided with no ambiguous primitive. The directed extremal margins are

```text
minimum positive stable primitive   1.2071210444943723e-6
closest excluded stable primitive  -1.0500676850149725e-6
minimum positive U numerator        1.0067872052482954e-3
closest excluded U numerator       -1.2017839149519758e-4
minimum positive saddle component   9.6294884626049211e-4
closest excluded saddle component  -1.1738378397231683e-4
minimum inactive numerator          1.468921317915317e-9
```

Thus the centred body is not a near-miss hidden by tolerances; hundreds of equilibria are separated by directed positive margins.

Complete H/V materialization is supplied in two forms:

1. `geometry/root_interval_hv.npz`: outward binary64 interval enclosures of every H row and every primal vertex over the root box, plus all active triples, surface triangles, maximal-face-cycle offsets, and true edges.
2. `geometry/root_midpoint_hv.npz`: the concrete midpoint arrays used for OBJ/STL visualization.

The expanded maximal-face cycles are in `geometry/root_maximal_face_cycles.json`; all true edges are in `geometry/root_true_edges.csv` with columns `(P_endpoint_0,P_endpoint_1,H_row_0,H_row_1)`.

## 8. Certified open regions and perturbation radii

Two distinct radii are certified, with their scopes stated explicitly.

**Moment/root class region.** The unique root lies in the second Krawczyk image, while every incidence and equilibrium primitive is audited on the larger first image. The exact boundary-distance calculation gives the guaranteed parameter-space radius

```text
rho_t = 1.59447008218838971063502441172975267e-31
```

in `L_infinity`: a perturbation of the exact root by at most this amount stays inside the fully audited class `(291,305,594)` region.

**Relay circuit region.** For a coordinatewise perturbation of `q_2184` with `q_2166` constrained by the exact half-turn, the exact affine determinant bound gives

```text
rho_q = 5.61153421425244779239284029350516230e-6,
```

which preserves all four post-zipper circuit signs. This is a circuit-cell radius, not a claim that arbitrary source-row perturbations of that size preserve every remote incidence.

The exact integer gaps and derivations are in `certificates/perturbation_region.json`.

## 9. Independent verification and meshes

`src/verify_relay_cleanroom.py` imports none of the construction modules. It independently:

- reparses the exact hexadecimal source table;
- rebuilds the polar hull with SciPy/Qhull;
- matches all 8,644 active triples;
- reconstructs all 4,324 maximal-face cycles and 12,966 true edges;
- recomputes the solid volume and moments;
- recomputes all face, vertex, and full edge-cone equilibrium counts;
- verifies the exact circuit equations with `Fraction` arithmetic;
- checks the H/V archive;
- checks both meshes with `trimesh`;
- invokes the outward-rounding audit as an independent second engine.

Its stored report is `certificates/cleanroom_verify_report.json`, with `passed=true`. It reproduces `(291,305,594)`, OBJ/STL watertightness, Euler characteristic two, and 8,644 mesh vertices / 17,284 triangles after STL vertex merging.

The meshes are:

- `geometry/root_midpoint.obj`
- `geometry/root_midpoint.stl`

Both represent the midpoint of the extremely narrow second Krawczyk image. The exact body is the interval-isolated root, not the rounded mesh coordinates.

Run the entire deterministic pipeline with:

```bash
python -m pip install -r requirements.txt
./[internal-source-reference].sh
```

## 10. What changed relative to the supplied journal

The supplied state had the original exact first wall and a proposed four-star zipper but no realized relay. This work adds:

1. an exact full reconstruction of the predecessor cover and first wall;
2. exact half-turn replacement data for all rows in the four complete stars;
3. a two-parameter relay `(s,tau)` with an exact tangential null coordinate;
4. four simultaneous exact circuit equations and a strict dyadic post point;
5. complete pre/post face-lattice reconstruction;
6. an exact proof that both inherited wall amplitudes move outward;
7. the exact outer stable/unstable/saddle relay that replaces them;
8. a unique Krawczyk-isolated hard solution of all three ordinary moments;
9. full interval H/V data, maximal-face cycles, true edges, and complete own-centroid normal-cone audit;
10. two scoped perturbation radii, independent verification, and OBJ/STL.

## 11. Strongest continuation

Do **not** add another broad smooth support mode: the moment Jacobian is already full rank and the three modes close all moments exactly. Do **not** vary only the tangential null coordinate inside the present post cell: the two fixed-boundary unstable facets remain positive independently of it.

The smallest materially new cell must move at least one row of each outer unstable triangle and cross their saddle stars in the same event. A concrete next patch should replace the complete outer stars containing

```text
north: 2184,2219,2220,2255
south: 2166,2201,2202,2237
```

while retaining the inner relay rows `2149,2113,2148` and mates as fixed boundary chains. It needs at least two new boundary-direction coordinates, not merely one null translation of `2184/2166`, so that the two exact positive unstable coefficients can change sign while the old wall primitives stay negative. The three distributed modes should again be eliminated as dependent variables in every rebuilt incidence cell. The next stopping rule is the first exact outer-circuit primitive or a strict own-centroid `(1,1,0)` chamber, not a floating residual.

## Artifact bundle

The complete archive includes source rows, exact certificates, interval H/V data, all cycles and edges, independent verifiers, logs, and meshes. See `MANIFEST.sha256` for byte-level integrity.

## Downloadable artifacts

- Complete exact/directed archive (`equatorial_zipper_relay_nonwinner.zip`)
- Archive SHA-256 (`equatorial_zipper_relay_nonwinner.zip.sha256`)
- Standalone research handoff (`RESEARCH_HANDOFF.md`)
- Machine-readable result (`RESULT.json`)
- Interval H/V archive (`root_interval_hv.npz`)
- Expanded maximal-face cycles (`root_maximal_face_cycles.json`)
- Expanded true edges (`root_true_edges.csv`)
- Independent verification report (`cleanroom_verify_report.json`)
- OBJ mesh (`root_midpoint.obj`)
- STL mesh (`root_midpoint.stl`)
