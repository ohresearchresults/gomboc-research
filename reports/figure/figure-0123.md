# figure-0123

Historical AI scientific report · saved 2026-08-27 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Vertically mode-one Conway collar — terminal exact handoff

## Verdict

**No homogeneous convex polyhedral Gömböc was found.** The run’s gate remains a literal independently checkable own-centroid strict `(S,U,H)=(1,1,0)` polyhedron; it was unmet before this continuation. :contentReference[oaicite:0]{index=0} The planar predecessor had reduced the Conway mass gap but made two almost coincident fivefold packets birth/transfer rather than cancel, so the journal opened the present asymmetric mode-one cell. :contentReference[oaicite:1]{index=1}

The strongest fully exact all-active endpoint breaks physical `C5` rotational symmetry, has exact own-centroid moments, actual lattice

```text
(V,E,F,C)=(31,85,56,170),
```

and strict class

```text
(S,U,H)=(6,3,7).
```

Along an exact corrugation homotopy, three lower unstable–saddle pairs cancel, but two lower pairs survive and a complete upper fivefold stable–saddle packet stays strict. A separate exact 20-vertex topology-changing endpoint, after two whole source layers and one further vertex deactivate, is still `(6,3,7)`. The packets therefore **partially cancel, then transfer/persist; they do not jointly cancel.**

## Exact finite generator

Work in

```text
K=Q(theta), theta=2*cos(pi/10), theta^4-5*theta^2+5=0, 19/10<theta<2,
D=2^48=281474976710656.
```

The six planar mode-one ring parameters are

```text
u = [7367329326,1906429424305,27372781458595,
     23115024387335,18870173567634,4509504332422]
v = [0,-2026680465414,1787496808432,
     -18458249412805,20312977868846,922791250719]
z = [-281474976710656,-270467295991892,-147073462758634,
     -147068003266357,-53418412216737,269300378901153]
corr = [35450450129,151959969633,349632248028,-222888038286].
```

For `phi_j=2*pi*j/5`, `i=0,…,5`, `j=0,…,4`,

```text
x_(i,j)=(u_i*cos(phi_j)-v_i*sin(phi_j))/D
y_(i,j)=(v_i*cos(phi_j)+u_i*sin(phi_j))/D
z_(i,j)=z_i/D
```

with

```text
ring 1: z += (35450450129*cos(phi)+151959969633*sin(phi))/D
ring 2: z += (349632248028*cos(phi)-222888038286*sin(phi))/D,
```

and raw apex `(0,0,1)`. Subtract the exact algebraic solid centroid. This gives all 31 exact V rows. For each actual outward maximal face cycle `f=(a,b,c,…)`, set

```text
n_f=(v_b-v_a)×(v_c-v_a), h_f=n_f·v_a>0, q_f=n_f/h_f,
```

so the irredundant H representation is `q_f·x<=1`, `f=0,…,55`. Every expanded centred V row, normalized H row, face cycle and true edge is supplied in the certificate and row tables:

- [Exact V/H/topology/moment/mechanics certificate](sandbox:/mnt/data/conway_mode1_exact/mode1_certificate.json)
- [Centred vertex rows](sandbox:/mnt/data/conway_mode1_exact/vertices_centered_exact.csv)
- [Normalized support rows](sandbox:/mnt/data/conway_mode1_exact/support_rows_exact.csv)
- [All 85 true edges with incident faces](sandbox:/mnt/data/conway_mode1_exact/true_edges.csv)

## Exact moments and actual hull

The 58 outward boundary triangles satisfy

```text
V=sum det(a,b,c)/6,
M=sum det(a,b,c)(a+b+c)/24.
```

The exact volume is the `K` element with descending `theta` coefficients

```text
3584794003630694301637590860010004535575/33451117797795934712303577408972542258970624
16748145473143948416637192984301707061045/267608942382367477698428619271780338071764992
2374649672673912938986077341833556326319855/267608942382367477698428619271780338071764992
610380986672332219075962274106288463445425/89202980794122492566142873090593446023921664
```

and numerically

```text
V=0.0246850952633203444168939834537945430243659689.
```

The raw centroid is the exact field point whose decimal enclosure is

```text
(-1.9996409297596169e-5,
  6.7904495762191830e-6,
 -0.1879953077886372715349464868841).
```

After exact algebraic translation by that point,

```text
(Mx,My,Mz)=(0,0,0) exactly.
```

A fresh Qhull proposal followed by exact cyclotomic reconstruction independently recovers all `31` vertices, `56` maximal polygons, `85` true edges, Euler equality, and all `1,566` positive nonincident support slacks. The actual OBJ has 56 maximal faces; the watertight STL has 58 triangles and every triangulation edge has multiplicity two.

## Complete own-centroid mechanics

Stable maximal faces are

```text
F06=(21,26,20) F14=(23,28,22) F16=(25,24,20)
F20=(22,27,21) F32=(24,29,23) F55=(4,3,2,1,0).
```

Unstable vertices are

```text
0,4,30.
```

Saddle true edges are

```text
(0,4) (2,3) (20,25) (21,26) (22,27) (23,28) (24,29).
```

The intended bottom pentagon `F55` is stable and apex `30` unstable, but neither is unique. The exact ledger contains `170` face primitives, `170` vertex primitives, `340` full edge-cone primitives and `31` nonzero incident-normal spanning witnesses. Exact minima are

```text
raw inactive support slack   3.4785505628327185e-11
raw face/vertex |primitive|  3.265934026244237e-20
raw edge-cone |primitive|    1.019771640478688e-48
raw normal-span |det|        5.930066957953590e-17.
```

All signs are exact in `K`; decimals are diagnostic only.

## Exact ordered wall and circuit atlas

Scale only the four corrugation coefficients by `lambda∈[0,1]`. The actual `(31,85,56)` lattice never changes: all 1,566 nonincident oriented face-volume slacks are affine in `lambda` and positive at both endpoints. The class sequence is

```text
(6,6,10) -> (6,5,9) -> (6,4,8) -> (6,3,7).
```

There are exactly three class-changing events, each an isolated simple shared primitive:

```text
lambda1≈0.728577382030993981: V3 cancels with E(3,4)
lambda2≈0.892012192819044092: V1 cancels with E(0,1)
lambda3≈0.909295989679479333: V2 cancels with E(1,2).
```

The exact rational isolating intervals, exact field roots, derivative signs and four directed open-cell boxes are in the [wall-event certificate](sandbox:/mnt/data/conway_mode1_exact/lambda_event_certificate.json).

The initial lower packet is

```text
U={0,1,2,3,4},
H={(0,1),(1,2),(2,3),(3,4),(0,4)}.
```

After the three cancellations,

```text
U={0,4}, H={(0,4),(2,3)}.
```

The upper packet

```text
S={F06,F14,F16,F20,F32},
H={(20,25),(21,26),(22,27),(23,28),(24,29)}
```

remains strict throughout. Thus no cancellation-oriented joint topology event occurs on this exact path; there are no hull circuits at all.

## Open perturbation certificate

All 22 dyadic coefficients—six `u`, six `v`, six mean heights and four corrugation coefficients—vary independently by `±2^-45`. Directed interval arithmetic preserves

```text
topology=(31,85,56), class=(6,3,7), physical C5 symmetry broken,
V in [0.024685095263246404,0.02468509526339428],
raw support slack >3.4778655999507053e-11,
positive primitive >8.777701426169157e-49,
exclusion clearance >1.3330854626136012e-19.
```

See the [box certificate](sandbox:/mnt/data/conway_mode1_exact/parameter_box_output.json) and [box verifier](sandbox:/mnt/data/conway_mode1_exact/verify_parameter_box.py).

## Exact topology-changing fallback

A second exact state deactivates source labels

```text
5,6,7,8,9,10,20,21,22,23,24
```

and retains only 20 extreme vertices. Its rebuilt lattice and mechanics are

```text
(V,E,F,C)=(20,52,34,104),
V=0.0185582018453924688097481019141522549113798586,
centered moments=(0,0,0) exactly,
(S,U,H)=(6,3,7).
```

Two complete source layers disappear and direct ring-to-return-layer cross-links form, but the upper fivefold stable–saddle packet survives. A separate `±2^-45` box preserves this cell. This shows that the 31-vertex failure is not merely an artifact of retaining obsolete collar layers.

- [Compact exact certificate](sandbox:/mnt/data/conway_mode1_exact/compact20_certificate.json)
- [Compact generator](sandbox:/mnt/data/conway_mode1_exact/compact20_generator.json)
- [Compact OBJ](sandbox:/mnt/data/conway_mode1_exact/compact20.obj)
- [Compact STL](sandbox:/mnt/data/conway_mode1_exact/compact20.stl)

## Search conclusion and smallest new cell

Empirically, 12,000 moment-manifold samples, 6,395 retained topology signatures across two relaxed archive runs, 3,000 local samples, 2,432 broad accepted hulls, a 20,582-signature long manifold archive and a 3,199-state scale scan produced no target-valid `(1,1,0)` cell. The smallest target-valid class repeatedly observed was `(6,3,7)`. Fixed-cell multiwall continuation multiplied/transferred into `(6,11,15)` and `(11,6,15)` actual cells. The exact endpoint and compact fallback then prove the structural part of this observation: lower-only mode-one freedom removes only three lower `U-H` pairs and leaves the entire upper return-layer packet.

The smallest genuinely new topology adds **no vertices**: give one upper return layer an independent complex vertical mode-one amplitude. Keep the two lower complex amplitudes and one mean height/radius as dependent variables solving the three exact moments in each rebuilt cell; use the remaining three asymmetric real directions to cross the two surviving lower `U-H` pairs, the five upper `S-H` stars and the first upper strip hull circuit together. Another lower-only corrugation, planar ring, fixed axial profile or fixed-cell polishing is redundant.

## Verification and artifacts

The independent exact verifier reports `PASS`, independently reconstructing `(31,85,56)`, exact zero centred moments and `(6,3,7)`. The independent decimal mesh audit reports volume `0.024685095263320356`, centroid residual below `7e-17`, 56 OBJ faces, 58 watertight STL triangles and the same complete class.

- [Complete checksummed handoff ZIP](sandbox:/mnt/data/conway_mode1_collar_handoff.zip) — SHA-256 `6555e72ec5b1d299922b2966b42ddf151d59f5461973d76c83c122bba77067ed`
- [Full handoff Markdown](sandbox:/mnt/data/conway_mode1_exact/COMPLETE_HANDOFF.md)
- [Normative generator](sandbox:/mnt/data/conway_mode1_exact/mode1_generator.json)
- [Deterministic exact generator/verifier](sandbox:/mnt/data/conway_mode1_exact/generate_exact_mode1.py)
- [Independent exact verifier and output](sandbox:/mnt/data/conway_mode1_exact/independent_exact_verify.py), [output](sandbox:/mnt/data/conway_mode1_exact/independent_exact_verify_output.json)
- [Independent mesh auditor and output](sandbox:/mnt/data/conway_mode1_exact/independent_mesh_audit.py), [output](sandbox:/mnt/data/conway_mode1_exact/independent_mesh_audit_output.json)
- [Watertight OBJ](sandbox:/mnt/data/conway_mode1_exact/mode1_endpoint.obj)
- [Watertight STL](sandbox:/mnt/data/conway_mode1_exact/mode1_endpoint.stl)
- [Empirical search report](sandbox:/mnt/data/conway_mode1_exact/search_report.json)
- [Fresh verifier transcript](sandbox:/mnt/data/conway_mode1_exact/RUN_ALL_VERIFIERS.txt)
- [Reproduction script](sandbox:/mnt/data/conway_mode1_exact/[internal-source-reference].sh)
- [SHA-256 manifest](sandbox:/mnt/data/conway_mode1_exact/MANIFEST.sha256)

## Bottom line

The requested winner was not obtained. The exact mode-one collar breaks physical fivefold equilibrium symmetry and performs three genuine lower `U-H` cancellations, but two lower pairs and a complete upper fivefold `S-H` packet survive. Even a separate exact 20-vertex topology compression retains `(6,3,7)`. The next nonredundant move is upper-return-layer corrugation under hard exact moment elimination and first-circuit tracking, not another planar or lower-only collar.
