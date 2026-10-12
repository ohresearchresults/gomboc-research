# figure-0110

AI research report · 2026-08-27 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Slot-4 exact two-collar continuation — certified finite negative result

## Verdict

**No homogeneous convex polyhedral Gömböc occurs in the certified finite atlas.** I rebuilt the deterministic 4,324-row family with two exact complete-one-ring collar controls and three separated distributed moment fields, certified rank three, isolated the simultaneous five-equation root and the formal moment root in each of the four adjacent two-circuit cells, rebuilt the actual H/V lattice in every root box, and proved that all four formal roots are counterfactual: the inherited incidence formulas have already ceased to describe the polytope, while the actual x-moment is strictly positive.

The first genuine continuation primitive is not either prescribed wall. On the compensated ray it is the exact circuit `{551,552,586,587}` at `alpha≈1.1529416975455552e-4`, strictly before the two inherited circuits near `alpha=1`. I crossed that wall by exact dyadic pre/post points, rebuilt both chambers, and stopped there as required. The post-wall chamber is the first root-unclassified actual topology. This is therefore a rigorous chamber-by-chamber result through the first genuinely new wall, not a global exclusion of every disconnected component of the five-parameter family.

The supplied journal identified the two inherited walls and required a root strictly inside an actual own-centroid mechanical chamber. :contentReference[oaicite:0]{index=0} It also fixed the deterministic 4,324-row source and the two diagonal identities used below. :contentReference[oaicite:1]{index=1}

## Verified artifact

The complete exact atlas, ledgers, verifier, and meshes are in [slot4_two_collar_verified_nonwinner.zip](sandbox:/mnt/data/slot4_two_collar_verified_nonwinner.zip); its SHA-256 is

`b2e4d2f67d9bf86a6f1a142524df193e8c00755aad38fd74ed623af3d06513e3`.

The checksum file is [slot4_two_collar_verified_nonwinner.zip.sha256](sandbox:/mnt/data/slot4_two_collar_verified_nonwinner.zip.sha256). In this runtime I independently re-ran the original manifest check, deterministic generator, full geometry verifier, and certificate verifier. All passed. The deterministic regeneration reports digest `cdaf6a4996b69a0cc41a021a4221277a77806d73362cc6b6befb7de8b67090f8`; the normative `two_collar_generator.json` file SHA-256 is `0992bea5c756b3a9f385e7d1fda0c20bae2ff09e11c51a80b44035daa3cf4e95`.

## Exact deterministic five-variable family

Let `p=(c1,c2,t0,t1,t2)`. For every row `i=0,…,4323`,

`q_i(p) = (Qint_i/2^48) · (1 + 2^-24 (C1_i c1 + C2_i c2 + D0_i t0 + D1_i t1 + D2_i t2))`,

and

`P(p)={x∈R^3 : q_i(p)·x≤1 for all i}`.

`Qint` and all five integer field columns are stored verbatim in `two_collar_generator.json`; `generate_two_collar_family.py --check` reconstructs them deterministically from `provenance/source_endpoint_generator.json`.

The complete collar supports are

- `C1={512,513,514,515,547,548,549,550,582,583,584,585,618,619}`;
- `C2={530,531,532,533,565,566,567,568,600,601,602,603,636,637}`.

Every listed collar coefficient is nonzero, the two supports are disjoint, and rows `0,4321,4322,4323` are frozen in all five fields. The three distributed supports are pairwise disjoint noncritical bands: rings `3–28` with 772 rows, `48–76` with 910 rows, and `94–117` with 802 rows.

Inside any fixed incidence cell, a primal vertex with active triple `I=(i,j,k)` is exactly

`v_I(p) = [q_i(p);q_j(p);q_k(p)]^-1 (1,1,1)^T`.

For an oriented boundary triangulation `T`, the exact ordinary volume and first moment equations are

`V(p)=Σ_(a,b,c∈T) det(v_a,v_b,v_c)/6`,

`M(p)=Σ_(a,b,c∈T) det(v_a,v_b,v_c)(v_a+v_b+v_c)/24`,

and the centring equations are `M_x=M_y=M_z=0`. All fixed-cell evaluations in the atlas use these rational formulas with outward interval enclosures.

## Exact circuit equations and diagonal identities

For an ordered quadruple define

`Δ_abcd(p)=det(q_b-q_a,q_c-q_a,q_d-q_a)`.

After clearing the common positive dyadic denominator and primitive content, the first controlled circuit depends only on `(c1,t0)`:

`f1(c1,t0)=A3 c1^3+B21 c1^2 t0+A2 c1^2+B11 c1 t0+A1 c1+B01 t0+A0`,

where

- `A3=20992678081426850848214386615094515394670194512906413313635867`;
- `B21=1480033472221726809287228952138075897775040447595073695`;
- `A2=47093514686061041837810133390844954015667882899270093997342720`;
- `B11=3309772022768492598395550567298839154526435072844759040`;
- `A1=26510205309975610854261502393831577309941020840121345471676416`;
- `B01=1856964586281187228389627182603555964613474506044866560`;
- `A0=-97044266239109786635689299201586362028915363863175626752`.

Its primitive content is 8. Crossing `f1=0` changes

`(548,549,584),(548,583,584)  ↔  (548,549,583),(549,583,584)`.

The second controlled circuit depends only on `(c2,t0)`:

`f2(c2,t0)=A3 c2^3+B21 c2^2 t0+A2 c2^2+B11 c2 t0+A1 c2+B01 t0+A0`,

where

- `A3=18381692582053203283900965284436790889889003307903026772171793`;
- `B21=2127343107821260857226295214434870917604273377663873600`;
- `A2=68771731502537149136842910566569067158768368517231305209937920`;
- `B11=7939213086264848256729923398416337125391603699149701120`;
- `A1=64509428278184679976345281572956456469466805647290050895937536`;
- `B01=7427858345124935468785041865424875910989058839622451200`;
- `A0=-388177065112947777668651793289210636333269723104164184064`.

Its primitive content is 2. Crossing `f2=0` changes

`(566,567,602),(566,601,602)  ↔  (566,567,601),(567,601,602)`.

With `t0=0`, exact Sturm counts give one positive root for each cubic:

- Q1 root in `(10668840318370588925243/2914494564568632474600492379, 20996929577409947727350/5735903369049372963974181443)`, approximately `3.6606142444289165e-6`; exact dyadic pre/post values are `4024887/2^40` and `4024888/2^40`.
- Q2 root in `(28665599825594198879028/4763839713056565714131805593, 21852344891638760092469/3631567769436676247018666647)`, approximately `6.017330882697107e-6`; exact dyadic pre/post values are `6616125/2^40` and `6616126/2^40`.

Each pure pre/post body and all four combined local collar chambers have 4,324 active rows, 8,644 primal vertices, 12,966 true edges, stable row `0`, unstable facet `{4321,4322,4323}`, no saddles, and strict construction-centre class `(1,1,0)`.

## Rank-three distributed moment elimination

At `c1=c2=t0=t1=t2=0`, the directed Jacobian midpoint for `(M_x,M_y,M_z)` with respect to `(t0,t1,t2)` is

`[[0.4316667330752608,-0.12359311397898406,-0.5247873316437295],[-0.015588690845281899,0.051420626688693405,-0.012669908729611452],[0.028313321739089663,0.18620270225425178,0.027312964612132583]]`.

Its determinant enclosure is

`[0.003903652691018969,0.0039036528984675175]`,

so the distributed moment Jacobian has certified rank three.

## Isolated five-equation root

The inherited fixed-incidence system

`M_x=M_y=M_z=f1=f2=0`

has a unique Krawczyk-isolated root in the following five-dimensional box. All displayed endpoints are the exact binary64 dyadics stored in the certificate.

Center:

`(3.6561846431139604e-6,6.010049487546052e-6,0.0632378256514446,-0.051947393741720256,-0.07980545019853842)`.

Exact center encodings:

`(0x1.eab98c3a29b29p-19,0x1.9353dd2e25cd1p-18,0x1.0305aa90b08e5p-4,-0x1.a98d94a775bf9p-5,-0x1.46e2146a53105p-4)`.

Initial box lower endpoint:

`(3.1793474849108354e-6,5.533212329342927e-6,0.0632373488142864,-0.05194787057887846,-0.07980592703569662)`.

Initial box upper endpoint:

`(4.133021801317085e-6,6.486886645749177e-6,0.06323830248860281,-0.05194691690456205,-0.07980497336138022)`.

Krawczyk image:

`K_lo=(3.6561570771980095e-6,6.010033537901569e-6,0.06323762005812951,-0.05194772727378368,-0.079805530037941)`,

`K_hi=(3.6562122083165714e-6,6.010065438352063e-6,0.06323803124476103,-0.05194706020965571,-0.07980537035913476)`.

The image is strictly inside the initial box. This proves a unique root of the inherited formulas, but not a root of the actual rebuilt polytope.

## Four adjacent nominal circuit cells

The exact collar coordinates are dyadics with denominator `2^50`:

| cell | `c1` | `c2` |
|---|---:|---:|
| `--` | `3047743124/2^50` | `5701169676/2^50` |
| `-+` | `3047743124/2^50` | `7848653324/2^50` |
| `+-` | `5195226772/2^50` | `5701169676/2^50` |
| `++` | `5195226772/2^50` | `7848653324/2^50` |

For each fixed collar pair, interval Newton/Krawczyk isolates one unique zero of the three inherited moment equations:

- `--`: root centre `(0.06323796977468923,-0.05194671736044218,-0.07980511375479442)` and `K(X)⊂[0.06323780931976158,0.06323813022961908]×[-0.051946976707563326,-0.05194645801331666]×[-0.07980517786645938,-0.07980504964312767]`.
- `-+`: root centre `(0.06323849751923563,-0.05194634554981158,-0.07980512317262295)` and `K(X)⊂[0.06323833706377269,0.06323865797469913]×[-0.05194660490324402,-0.051946086196379825]×[-0.07980518728505746,-0.07980505906018866]`.
- `+-`: root centre `(0.06323721081953752,-0.05194854948243791,-0.07980587369833571)` and `K(X)⊂[0.06323705036292684,0.06323737127614915]×[-0.05194880881274,-0.05194829015213939]×[-0.0798059378053116,-0.07980580959136155]`.
- `++`: root centre `(0.06323773854464138,-0.05194817775182024,-0.07980588313556732)` and `K(X)⊂[0.06323757808779212,0.06323789900149357]×[-0.05194843708792413,-0.05194791841571764]×[-0.07980594724321467,-0.07980581902792071]`.

### Exact rejection of the nominal incidence cells

At every isolated root, 4,766 expected facets disappear. The expected facet `[0,1,2]` violates row `341`; the four directed violation intervals are respectively

- `--`: `[0.006781998103126962,0.006782634809231914]`;
- `-+`: `[0.00678234748962958,0.00678298419573431]`;
- `+-`: `[0.0067814956466114565,0.006782132352716409]`;
- `++`: `[0.006781845020242149,0.006782481726346879]`.

Thus none of the four inherited incidence formulas describes the actual polytope at its formal root. Rebuilding all H/V primitives gives the same actual topology in all four boxes, signature

`0ad0f82816dbd72b79636fbe40db88163489ae07869d405d37366fbec9691a69`,

with `H_active/H_inactive/V/E/maximal_faces/surface_triangles = 2687/1637/5370/8055/2687/10736`.

Tight actual root-box moment enclosures are:

| cell | actual `M_x` | actual `M_y` | actual `M_z` |
|---|---|---|---|
| `--` | `[0.18859675184583488,0.1886074842006364]` | `[-0.0012748400384093145,-0.001267791001622308]` | `[0.0028765151642232995,0.002884226460599741]` |
| `-+` | `[0.18859716292051704,0.18860789285076052]` | `[-0.001274854080957691,-0.001267806621950404]` | `[0.0028765438606016148,0.002884253407870625]` |
| `+-` | `[0.188596246495759,0.18860697054527592]` | `[-0.0012748150521051061,-0.0012677714743000905]` | `[0.0028765589019491503,0.002884264231329486]` |
| `++` | `[0.1885966555537801,0.1886073811870377]` | `[-0.0012748304098145666,-0.0012677857780725441]` | `[0.00287658616175584,0.002884292620846064]` |

Therefore each actual tight box contains **zero** moment roots because `M_x>0`. In every box all 23,203,770 nonincident H/V inequalities remain strict; the common minimum is row `4298` against vertex `V5285=[4262,4263,4297]`, with gap `[1.468904553547645e-9,1.4689498506470502e-9]`.

At the four isolated formal-root centres, the actual own-centroid class is identically `(955,956,1909)`. Complete face, vertex, and full two-face edge-normal-cone ledgers for every centre are in `cell_root_mechanical_ledgers.json.gz`.

## First genuinely new wall

Let `p(alpha)=alpha p*`, where `p*` is the exact binary64 centre above. Exact Sturm isolation orders the positive circuit roots as

1. `{551,552,586,587}` at `alpha≈0.00011529416975455552005`;
2. `{548,549,583,584}` at `alpha≈0.99999999998588254048`;
3. `{566,567,601,602}` at `alpha≈1.00000000008409234162`.

The first circuit has the exact primitive linear equation

`g(alpha)=2100330490797324800790965654010289579979611690003851011588785461·alpha-242155860146655676091624565174441995963264859895166142513152`,

with its unique positive root in

`(258361969265861/2240893618609474953,71249378703133/617979025780857268)`.

The two inherited ray roots are isolated in the disjoint exact intervals

- Q1: `(18670081581918894372/18670081582182468493,18730685049467962297/18730685049732391985)`;
- Q2: `(605235685265805947/605235685214910261,2878992454776630543/2878992454534529326)`.

The new wall changes

`(551,552,587),(551,586,587)  ↔  (551,552,586),(552,586,587)`.

Exact dyadic chamber samples are `alpha_pre=3961477/2^35` and `alpha_post=3961478/2^35`. Both have all 4,324 rows active, 8,644 primal vertices, 12,966 true edges, stable row `0` with construction margin `0.0009462810843413605`, terminal unstable facet with margin `0.3330166967265903`, no saddle edges, and strict construction-centre class `(1,1,0)`. Both have own-centroid class `(2799,2864,5661)`, hence are not winners.

Pre-wall mass data are `V≈4.201090519356222`, `M≈(0.12605221162446215,-3.0442729121698644e-7,-1.1596983815424033e-6)`, centroid `≈(0.030004640710235987,-7.246387332392854e-8,-2.7604698737129717e-7)`. Post-wall data are `V≈4.201090519358857`, `M≈(0.12605221162665933,-3.044273677609235e-7,-1.159698674281277e-6)`, centroid `≈(0.03000464071074017,-7.246389154389923e-8,-2.7604705705276317e-7)`.

## Fully expanded representative actual topology

At the exact binary64-dyadic simultaneous-root centre, the rebuilt actual body has

`H_total/H_active/H_inactive=4324/2687/1637`, `V=5370`, `E=8055`, `F_max=2687`, `surface triangles=10736`, and Euler value `5370-8055+2687=2`.

Its directed mass enclosure is

- `V∈[4.205372926363553,4.205372927101383]`;
- `M_x∈[0.18860204114744167,0.18860204145238713]`;
- `M_y∈[-0.0012713112095465327,-0.001271310906941228]`;
- `M_z∈[0.002880398857181068,0.0028803991111045206]`;
- centroid `x∈[0.04484787542431782,0.04484787550469968]`, `y∈[-0.00030230641415334705,-0.00030230634214347736]`, `z∈[0.000684933038546578,0.0006849330990474714]`;
- minimum oriented tetrahedron determinant `∈[4.536258498498944e-9,4.536387958851974e-9]`.

The construction-centre class is `(123,146,267)` and the exhaustive own-centroid class is `(955,956,1909)`. Every primitive is interval-decided. Directed minimum margins at the own centroid are:

- stable-face primitive lower margin `3.0164380282471365e-7`; closest nonstable exclusion magnitude `2.853380072220801e-7`;
- unstable-vertex primitive directional margin `7.96031731136731e-9`; closest nonunstable exclusion margin `1.4612773274634712e-9`;
- saddle edge/full-normal-cone primitive margin `4.395058165895804e-5`; closest nonsaddle exclusion margin `2.8990634236606875e-4`.

All 23,203,770 nonincident H/V pairs are certified, with global gap lower bound `1.468904553547645e-9`.

The uniform five-parameter perturbation box of radius `2^-32` preserves this complete actual topology. Over that box,

- `V∈[4.205367786498124,4.205378066966809]`;
- `M_x∈[0.18859969566463916,0.18860438693518192]`;
- `M_y∈[-0.001272851706465778,-0.001269770410015254]`;
- `M_z∈[0.0028787136139427783,0.002882084354318355]`;

so `M_x>0` throughout.

## Complete finite evidence in the bundle

- `H_all_exact.tsv.gz`: all 4,324 exact dyadic H rows, including active/inactive status;
- `V_exact.tsv.gz`: all 5,370 exact rational vertices and active triples;
- `maximal_face_cycles.tsv.gz`: every maximal face cycle;
- `true_edges.tsv`: all 8,055 true edges and their incident faces;
- `nonincident_HV_interval_audit.tsv.gz`: all 23,203,770 inactive-incidence inequalities;
- `own_stable_face_interval_ledger.tsv.gz`: every own-centroid face margin;
- `own_vertex_interval_ledger.tsv.gz`: every own-centroid vertex directional margin;
- `own_edge_cone_interval_ledger.tsv.gz`: every edge-foot interval and both normal-cone coefficient intervals;
- `cell_root_mechanical_ledgers.json.gz`: complete mechanics at all four isolated formal roots;
- `third_wall_complete_ledgers.json.gz`: complete pre/post mechanics at the first new wall;
- `representative_perturbation_box.json`: the certified `2^-32` box;
- `representative.obj` and `representative.stl`: watertight 10,736-triangle meshes;
- `atlas_ledger.json`: machine-readable cell[private-runtime-path] index;
- `verify_atlas.py` and `verify_certificates.py`: clean-room verifiers.

Reproduction from `atlas_rechecked/`:

`python3 generate_two_collar_family.py --check`

`python3 verify_atlas.py`

`python3 verify_certificates.py`

All three commands pass in the supplied rechecked archive.

## Exact continuation boundary

The direct path to the two requested inherited walls is invalid because the actual lattice crosses `{551,552,586,587}` first. The next nonredundant step is to take the exact post-wall signature `f9ff70be8842745cf2bfbc15a8458871f6d04f2b5ae07f0c1c2027d65be22280`, re-eliminate `(t0,t1,t2)` from the three **actual-cell** moment equations, isolate the next circuit primitive, and rebuild again. No object in the certified atlas is an own-centroid strict `(1,1,0)` body, and none should be presented as a Gömböc.
