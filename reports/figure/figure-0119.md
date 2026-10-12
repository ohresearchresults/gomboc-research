# figure-0119

AI research report · 2026-08-27 UTC

---

# Slot-4 far-side independent-cell result

Complete exact archive (`slot4_far_side_component_result.zip`) · SHA-256 record (`slot4_far_side_component_result.zip.sha256`)

Archive SHA-256: `262ae52cf7f08d88c5d6daa7fd41205440d8cb5e21f49800b6dc909e7c0db06c`. Internal `MANIFEST.json` SHA-256: `48c75e73a3e49316bfb1e254a0ef3e11180d56820e1ec3dd9e36e40c3f09eeb5`; 73 payload files. I rechecked the ZIP, manifest, deterministic generator, full interval/circuit certificate, exact H/V reconstruction, and both watertight meshes in the current runtime; every verifier passed.

The supplied journal had already closed the entire connected `C3` component by a positive-`M_x` theorem and left the far-side signature `ac0cfc05c16540eeb4849333234d61069e05b838d3ca74e56a2a553a28f1a2f8` as an independent unclassified topology. This result enters that cell independently, closes its connected five-variable component, searches nearby same-signature fibres, and constructs the smallest one-new-field actual centred extension.

## Literal verdict

**NONWINNER.** No homogeneous convex polyhedral Gömböc occurs in the certified connected component of the five-variable far-side cell with incidence signature

`ac0cfc05c16540eeb4849333234d61069e05b838d3ca74e56a2a553a28f1a2f8`.

That entire connected component contains no ordinary-volume-centred point: the actual-cell first moment satisfies the chamber-wide exact/directed bound

`M_x > 2666174060904637760144532439940137300829483773 / 21267647932558653966460912964485513216000000000`

`= 0.12536290187609278... > 0`.

A finite exact-sign/fibre search found no nearby disconnected component with the same signature on the stated domains, but this is explicitly not a global cylindrical-algebraic decomposition.

Adding the smallest possible number of new controls—one exact belt-localized support-profile field—does produce a unique isolated actual ordinary-centred root. The complete root box retains one actual H/V lattice, but its strict own-centroid class is `(S,U,H)=(37,37,72)`, not `(1,1,0)`. Thus the extension is a rigorous root-ready nonwinner rather than a formal root in an obsolete triangulation.

## 1. Deterministic exact five-variable source

For `p=(c1,c2,t0,t1,t2)` and rows `i=0,...,4323`,

`q_i(p)=(Qint_i/2^48) [1+2^-24(C1_i c1+C2_i c2+D0_i t0+D1_i t1+D2_i t2)]`,

`P(p)={x in R^3 : q_i(p)·x<=1}`.

The normative arrays are in `source/two_collar_generator.json`, SHA-256

`0992bea5c756b3a9f385e7d1fda0c20bae2ff09e11c51a80b44035daa3cf4e95`.

Rows `0,4321,4322,4323` remain frozen. Row `0` is the protected stable cap, and the terminal triple `(4321,4322,4323)` is the protected unstable fan.

For every active triple `I=(i,j,k)`, the exact primal vertex is

`v_I(p)=[q_i(p);q_j(p);q_k(p)]^-1 (1,1,1)^T`.

For the stored outward-oriented actual surface triangulation `T`,

`V(p)=sum_(a,b,c in T) det(v_a,v_b,v_c)/6`,

`M(p)=sum_(a,b,c in T) det(v_a,v_b,v_c)(v_a+v_b+v_c)/24`.

All chamber moment and derivative evaluations use these actual-cell rational functions.

## 2. Exact entry into the independent far-side cell

The crossed C3 boundary circuit is `Q=(2263,2298,2299,2334)`. Its primitive polynomial in `t1`, coefficients low-to-high, is

`g(t1)=`

`120805790938364358121941406492534423416005773045614510080`

`+5746736507615178773455764667584697822453824419511049402712064 t1`

`+9244056884312266510579850407093993405004088370076400018784256 t1^2`

`+3726169071051075546705280276867227830858564405221519555678289 t1^3`.

Its unique nearby root is isolated by exact Sturm arithmetic in

`(-43273469370729137627540126/2058451130318719729026213586905,`

` -37330700699942074208946831/1775762936709754474364865163556)`.

Crossing from C3 to the independently rebuilt far side changes

`(2263,2298,2334),(2263,2299,2334)`

into

`(2263,2298,2299),(2298,2299,2334)`.

A strict exact-dyadic far-side sample `F0` is

- `c1=0x1.dd5d71082df60p-30`;
- `c2=0x1.8858df5d891f7p-29`;
- `t0=0x1.1db0d4b1b0ad2p-15`;
- `t1=-0x1.b778cc0000000p-16`;
- `t2=-0x1.20e83c3ed29fap-15`.

With common parameter denominator `2^81`, its numerators are

`(4198946998153136,6902244202549751,82344751025395892224,-63334570160455417856,-83271822072157732864)`.

The independently rebuilt actual body has:

- signature `ac0cfc05c16540eeb4849333234d61069e05b838d3ca74e56a2a553a28f1a2f8`;
- `H_active/H_inactive=4324/0`;
- `V/E/F/T=8644/12966/4324/17284` and Euler value 2;
- directed volume `[4.201121428513659,4.201121428514488]`;
- directed moments
  - `Mx=[0.126079524328787,0.12607952432915254]`,
  - `My=[-1.429192752580447e-6,-1.429192441518868e-6]`,
  - `Mz=[-4.846137524857145e-6,-4.8461372130515854e-6]`;
- construction-centre class `(1,1,0)`, with stable row `0`, unstable triple `(4321,4322,4323)`, and no saddle edge;
- own-centroid class `(2800,2860,5658)`;
- minimum of all nonincident H/V gaps `1.4689265359635326e-9`, attained at row `4298` against vertex triple `(4262,4263,4297)`.

The complete exact H rows, all exact rational vertices, every maximal-face cycle, every true edge, all mechanics ledgers, and the watertight mesh are under `F0/` and `meshes/F0.*`.

## 3. Complete exact circuit census of F0

`certificates/F0_all_circuit_polynomials.json.gz` contains all `12,966` current true-edge circuit polynomials. Its canonical content digest is

`5ba8eefa2a9103a6b629598474edec994ec68adaa4418320a5a0e220dba35cac`.

Dependency histogram:

| variables | circuits |
|---|---:|
| none | 4,714 |
| `t0` | 2,520 |
| `t1` | 3,032 |
| `t2` | 2,558 |
| `c1,t0` | 65 |
| `c2,t0` | 65 |
| `c1` | 6 |
| `c2` | 6 |

The first lower-`t1` gate from F0 is `Q=(2245,2280,2281,2316)`, with primitive polynomial

`h(t1)=`

`7731570620055318919804250015522203098624369474919328645120`

`+246498677005061157133953952957832834367660030904201017116590080 t1`

`+305083346611554802796683728140070115256908145689990849653374976 t1^2`

`+94175198503722208573371129850321556979054846814938097310320455 t1^3`.

Its unique gate root is isolated in

`(-166705638942598121509021657/5314718858111009462423348101249,`

` -5973851994406715845977575/190451529124157059019257670568)`

and is approximately `-3.136678409398493e-5`. Crossing it changes

`(2245,2280,2316),(2245,2281,2316)`

into

`(2245,2280,2281),(2280,2281,2316)`.

## 4. Exact connected-component exclusion

Ten exact circuit gates enclose the complete connected open far-side component containing `F0` in the rational box

`-97/10^6 < c1 < 3661/10^9`,

`-3/12500 < c2 < 3009/(5*10^8)`,

`5549/(2*10^8) < t0 < 463/7812500`,

`-31367/10^9 < t1 < -21022/10^9`,

`-22837/(5*10^8) < t2 < -12353/(5*10^8)`.

The six one-variable gates are the circuits

- `t0`: `(516,517,551,552)` and `(78,79,113,114)`;
- `t1`: `(2245,2280,2281,2316)` and `(2263,2298,2299,2334)`;
- `t2`: `(4155,4156,4190,4191)` and `(4173,4174,4208,4209)`.

Each has exact Sturm count one between `F0` and the corresponding box face and opposite endpoint signs. Four coupled collar gates have a uniform sign opposite to F0 over the full gated `t0` interval:

- `c1` lower/upper: `(480,481,515,516)` and `(548,549,583,584)`;
- `c2` lower/upper: `(498,499,533,534)` and `(566,567,601,602)`.

A path inside one open incidence chamber cannot cross any of these circuit-zero faces. Outward interval automatic differentiation of the actual 8,644-vertex moment map over this complete box, followed by an exact rational mean-value bound from the exact dyadic sample, gives

`M_x >= 2666174060904637760144532439940137300829483773 / 21267647932558653966460912964485513216000000000 > 0`.

Therefore the connected far-side component has no centred point and no Gömböc.

## 5. Nearby same-signature search

The exact current-sign constraints were also searched for nearby disconnected components. This finite search is deliberately distinguished from the component theorem:

- all 2,520 `t0`-only, 3,032 `t1`-only, and 2,558 `t2`-only sign sets were exhaustively resolved on `[-0.01,0.01]`;
- their compatible sets are single intervals:
  - `t0 in (2.7745354593e-5,5.92633362809e-5)`,
  - `t1 in (-3.1366784094e-5,-2.10223447782e-5)`,
  - `t2 in (-4.56732607581e-5,-2.47066494201e-5)`;
- 1,001 exact-sign fibres across the coupled `(c1,t0)` and `(c2,t0)` constraints were sampled on collar domain `[-0.001,0.001]`; every fibre had exactly one feasible interval.

No nearby disconnected component sharing the signature was found. `certificates/F0_same_signature_nearby_search.json` records the domains and all boundary ranges. This is not asserted as a global CAD exclusion.

## 6. Smallest added control: one exact belt field

Because the original five-variable component is moment-one-sided, one additional support-profile direction was introduced. For `p=(c1,c2,t0,t1,t2,u)`,

`q_i(p)=(Qint_i/2^48) [1+2^-24(C1_i c1+C2_i c2+D0_i t0+D1_i t1+D2_i t2+E_i u)]`.

Let

`x_i=(Qint_i)_x/||Qint_i||_2`,

`raw_i=x_i(1-x_i^2)^24 / max_j |x_j(1-x_j^2)^24|`,

`E_i=round(2^24 raw_i)`,

then set `E_0=E_4321=E_4322=E_4323=0`.

The generator `scripts/make_extended_generator.py` determines the maximizing row and every nearest-integer decision by exact rational comparisons after squaring. The resulting field has 2,344 nonzero rows, integer range `[-16775012,16777216]`, and int64-column SHA-256

`fd1c42f8c2491fe3eb4429d8ec4b7db34c9765ff709a44c2d92d8bbc5d73766d`.

The complete six-field generator is `generator/extended_generator.json`, SHA-256

`12b9eda2f1d92a3bc9f07bfae4d4be2f6e3bc261f4709cbd6e0e1c987b02f686`.

## 7. Unique isolated actual centred root

Fix

- `c1=0x1.dd5d71082df60p-30`,
- `c2=0x1.8858df5d891f7p-29`,
- `t0=0x1.1db0d4b1b0ad2p-15`.

Use dependent-variable order `(u,t1,t2)`. The numerical centre is

`(0x1.f3df86aacab53p-3, 0x1.8e73f2373bdd9p-21, -0x1.7de20c7edbdabp-15)`.

The exact dyadic initial box is

- lower:
  `(0x1.f3df86aac8b52p-3, 0x1.8e73ee373bdd8p-21, -0x1.7de20c8edbdacp-15)`;
- upper:
  `(0x1.f3df86aaccb54p-3, 0x1.8e73f6373bddap-21, -0x1.7de20c6edbdaap-15)`.

Its coordinate radii are `(2^-42,2^-43,2^-43)`. The strict Krawczyk image is

- lower:
  `(0x1.f3df86aacaf60p-3, 0x1.8e73f24fda354p-21, -0x1.7de20c82f6feep-15)`;
- upper:
  `(0x1.f3df86aacaf64p-3, 0x1.8e73f24fda570p-21, -0x1.7de20c82f6f90p-15)`.

It lies strictly inside the initial box. The midpoint Jacobian determinant is `-0.0013668612333817074`, and the full outward Jacobian interval is

`[[-0.46056943557319974,-0.2498829710063159,-0.5242076404587128],`

` [ 8.661590937456209e-8,-0.0628878953060278,-0.012631054680370042],`

` [-4.971077637494315e-7,0.370776665016252,0.027279296091423415]]`

through

`[[-0.46056943071919487,-0.2498829646671831,-0.5242075761108816],`

` [ 9.270994279339702e-8,-0.0628878883355295,-0.012631037254471294],`

` [-4.90760859763548e-7,0.370776672044972,0.027279314837539873]]`.

Hence a unique real zero of the three **actual-cell** ordinary moments lies in the box. At that unique algebraic root,

`(Mx,My,Mz)=(0,0,0)` exactly,

while

`V in [3.2991042182735053,3.2991042186569683]`.

The interval image of the moment map over the whole initial box is

- `Mx in [-1.1437620758882242e-10,1.1437735272480806e-10]`;
- `My in [-4.980586018460724e-11,4.98058704539619e-11]`;
- `Mz in [-4.6551215089506474e-11,4.6551031195771916e-11]`.

## 8. Complete actual root-cell expansion and mechanics

The root cell has signature

`1d1b021cf9b44702f1dcead2d7fa5b5dbc836c353d8756c0968a106a08f967c5`.

Across the complete initial box:

- `H_total/H_active/H_inactive=4324/2638/1686`;
- `V/E/F/T=5272/7908/2638/10540`, Euler value 2;
- all `22,780,312` nonincident H/V inequalities are positive;
- minimum gap lower bound is `1.4689099936404657e-9`, row `4298` against vertex triple `(4262,4263,4297)`;
- every face, vertex, and four-component true-edge cone is interval-decided;
- the strict class is identically `(37,37,72)`.

The protected features survive: row `0` is stable, and `(4321,4322,4323)` is unstable. They are no longer unique. Mechanical interval margins over the full root box are:

- minimum positive stable-face margin `0.0009462810843366974`;
- closest excluded face upper margin `-0.00019722744753214447`;
- minimum positive unstable-vertex margin `0.05627398570591824`;
- closest excluded vertex upper margin `-0.014839441727870419`;
- minimum positive saddle-cone margin `0.055652970630445726`;
- closest excluded edge upper margin `-0.02113114640197677`.

This nonzero dyadic box is simultaneously a root-isolation box, topology perturbation certificate, inactive-incidence certificate, and complete mechanics certificate. It proves the actual centred body is a robust nonwinner.

The exact expansion is in `extended_root/`; the full root-box ledgers are in `certificates/extended_root_box_*`; the rational centre representative meshes are `meshes/extended_root_center.obj` and `.stl`. Because topology is fixed throughout the isolated box, those meshes represent the exact algebraic root cell.

## 9. Exact circuit census and first gate of the extended root cell

The complete current census has 7,908 circuit polynomials and canonical digest

`348dcaf59158355068bbe92d08b71d2e1fe432e2ffdc13c54d7b600ffb8e25d4`.

The first positive-`u` gate is `Q=(1390,1425,1426,2337)`, at

`u≈0.2441608085540372`, only `8.212271042365438e-5` above the root-box centre. Its primitive polynomial, coefficients low-to-high, is

`12111506861501835055100695131035663988089252374363360768085407966193156614868959232`

`-49055861695053259214084167697032118009281325986138947855361050883736457515431362560 u`

`-2249845099898644049399174747398199628181113529138552728917773975308964229245203695 u^2`

`+9301345342004075036341131013608340108704124582404995222823866901881218953904128 u^3`.

Its exact isolating interval is

`(4272041018522103868028636/17496833516492160199818945,`

` 2865087268539911582641321/11734427345270753994280054)`.

Crossing changes

`(1390,1425,1426),(1425,1426,2337)`

into

`(1390,1425,2337),(1390,1426,2337)`.

The far side of this gate is the first still-unclassified topology of the one-field extension.

## 10. Verification and file map

Run

`python verify_all.py`

for exact generator regeneration, static full-expansion checks, both watertight mesh checks, the F0 connected-component theorem, the Krawczyk root, all `22,780,312` root-box inactive-incidence tests, and every root-box face/vertex/four-component edge-cone decision.

Run

`python verify_exact_reconstruction.py`

for exact regeneration of every H row and every rational H-triple vertex in both bodies, signature checks, and an independent directed mass reconstruction. `verify_all.py` independently recomputes the complete root-box nonincident and face/vertex/four-component edge-cone ledgers. `source/build_point.py` and `scripts/build_extended_point.py` are supplied for a fresh Qhull-based materialization of either complete body.

The complete circuit and gate artifacts can be regenerated independently with

`python scripts/build_f0_census.py`

`python scripts/build_extended_census.py`

`python scripts/same_signature_search.py`

`python scripts/scan_extended_u_walls.py`.

Key files:

- `source/two_collar_generator.json`: exact five-variable source;
- `generator/extended_generator.json`: exact six-field extension;
- `F0/`: complete strict far-side H/V expansion;
- `extended_root/`: complete rational centre representative of the isolated root cell;
- `certificates/F0_component_gate.json`: ten exact component gates;
- `certificates/F0_moment_exclusion.json`: chamber-wide moment theorem;
- `certificates/F0_all_circuit_polynomials.json.gz`: all F0 circuits;
- `certificates/extended_root_certificate.json`: Krawczyk, moment, topology, and mechanics certificate;
- `certificates/extended_root_all_circuit_polynomials.json.gz`: all extended-root circuits;
- `certificates/extended_root_u_axis_walls.json`: exact first extended gates;
- `meshes/`: matching watertight OBJ/STL;
- `OUTCOME.json`: machine-readable result summary.

## 11. Precise continuation frontier

The original five-variable far-side connected component is closed by a component-wide positive-`Mx` theorem. A single unmodulated belt field solves the mass equations but creates a 36-sector stable/unstable/saddle relay. Adding another unmodulated distributed field is therefore low-value.

The smallest nonduplicative continuation is to keep `(u,t1,t2)` as dependent exact moment variables and add one azimuthally localized asymmetric belt field that splits the 36-sector relay. Enumerate the actual circuit cells beginning with `(1390,1425,1426,2337)`, preserve row `0` and terminal triple `(4321,4322,4323)`, and rebuild all inactive incidences and full edge cones after every accepted crossing. Exploratory `m=2` modulations reduce the number of stable faces but do not produce `(1,1,0)`; those searches are recorded only as empirical guidance under `exploration/`, not as exclusion evidence.

The result excludes the connected original far-side component exactly and certifies one actual centred extended root as a robust nonwinner. It does not exclude remote disconnected five-variable components, the far side of the first extended gate, or richer asymmetric extensions.
