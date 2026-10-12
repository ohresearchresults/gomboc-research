# figure-0117

AI research report · 2026-08-27 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Slot-4 handoff: exact exclusion of the complete connected C3 chamber

## Immutable artifact

Complete exact C3 component archive (`slot4_c3_component_exclusion.zip`) · SHA-256 record (`slot4_c3_component_exclusion.zip.sha256`)

Archive SHA-256: `ec281c6865f3d616c5b1aa4799ad961fdb2fb119658e87da55a695cfc17f89f6`. Internal payload digest: `d4e721495e31728a5e765cca09963bfdb0388ee0f96be3fe2a6922b939dea0e0`; `MANIFEST.json` SHA-256: `db317150af440b3d35b7b3f1ebe4902339f34fbd116ca45b37e203941608713f`. The ZIP integrity test, 103-file manifest, deterministic generator, exact 12,966-circuit regeneration, component gate, directed moment exclusion, full prior H/V audit, exact path-wall/Sturm audit, endpoint perturbation audit, and watertight mesh checks all pass; transcripts are included.

## Literal verdict

**NONWINNER.** The connected open incidence chamber `C3` containing the certified sample has **no ordinary-centred point at all**. In particular it contains no homogeneous convex polyhedral Gömböc and no real centred branch segment. The actual rational moment map satisfies the chamber-wide directed inequality

`M_x > 2665339258142487901729251539505183575881020157 / 21267647932558653966460912964485513216000000000 > 0.12532364963885445`.

Consequently the three equations `M_x=M_y=M_z=0` have no solution in `C3`. Under the assignment's explicit topology-continuation rule, the next circuit `(2263,2298,2299,2334)` is **not crossed**, because no isolated centred continuation reaches it. The observed far-side ray signature `ac0cfc05c16540eeb4849333234d61069e05b838d3ca74e56a2a553a28f1a2f8` remains the first unaccepted topology, not a classified successor chamber.

This resolves the exact continuation boundary recorded in the supplied journal: the prior finite atlas left `C3`, signature `df816aedc2371b44a17a593ea9b00c3930b84444a5d4d2c6cbe62399d46781a8`, as the first chamber whose **actual** moment map still required elimination.

## What changed relative to the supplied journal

The prior immutable atlas proved only that a radius-`2^-32` neighborhood of its chosen C3 sample is noncentred. This continuation closes the **entire connected C3 incidence component**, rather than another local box:

1. all 12,966 current true-edge circuits were regenerated exactly from the deterministic five-field support family;
2. ten circuit gates give a rational outer box containing the whole connected chamber;
3. the actual C3 rational volume and first-moment map was differentiated by outward interval arithmetic on that box;
4. an exact-rational mean-value bound proves `M_x>0` everywhere in the box and therefore everywhere in C3;
5. the complete centred locus in C3 is empty, so there is no branch to continue through the certified next wall.

No nominal triangulation, fixed artificial centre, sampled metric surrogate, or formal root beyond an incidence wall is used.

## Deterministic exact family

With parameter order `p=(c1,c2,t0,t1,t2)`, every support row is

`q_i(p)=(Qint_i/2^48) [1+2^-24(C1_i c1+C2_i c2+D0_i t0+D1_i t1+D2_i t2)]`, `i=0,…,4323`,

and

`P(p)={x in R^3 : q_i(p)·x<=1 for all i}`.

The normative integer arrays are `prior_atlas/two_collar_generator.json`. Deterministic regeneration returns digest

`cdaf6a4996b69a0cc41a021a4221277a77806d73362cc6b6befb7de8b67090f8`.

The complete collar supports remain

- `C1={512,513,514,515,547,548,549,550,582,583,584,585,618,619}`;
- `C2={530,531,532,533,565,566,567,568,600,601,602,603,636,637}`.

The three distributed supports contain 772, 910, and 802 rows. Rows `0,4321,4322,4323` remain frozen in all five fields.

## Actual C3 rational volume and moment equations

Let `s_i(p)=1+2^-24 W_i·p`, `h_i(p)=1/s_i(p)`, and let `A_I(0)` be the `3×3` matrix of the base support rows for the active triple `I=(i,j,k)`. For every one of the 8,644 actual C3 vertices,

`v_I(p)=A_I(0)^(-1)(h_i,h_j,h_k)^T`.

For the stored outward-oriented 17,284-triangle boundary triangulation `T`,

`V(p)=Σ_(a,b,c in T) det(v_a,v_b,v_c)/6`,

`M(p)=Σ_(a,b,c in T) det(v_a,v_b,v_c)(v_a+v_b+v_c)/24`.

These are exact rational functions. Their exact derivative generator is

`∂_r v_I=A_I(0)^(-1)(-2^-24 W_{i,r}s_i^-2,-2^-24 W_{j,r}s_j^-2,-2^-24 W_{k,r}s_k^-2)^T`,

followed by the product rule in the tetrahedral formulas above. The complete active triples and oriented summands are in `prior_atlas/chambers/C3/geometry.npz`, `V_exact.tsv.gz`, and `surface_triangles.tsv`; `prior_atlas/actual_cell_equations.json` is the machine-readable equation specification.

## Exact C3 circuit census

`certificates/C3_all_circuit_polynomials.json.gz` contains the primitive exact determinant polynomial for every current true edge, together with current sign and both diagonals. Its canonical content digest is

`d5b5ae4fb1d43fb126e070d006a052d6556b6eddf779c3d599fd70e9e6c06463`.

The complete dependency histogram is:

| variables occurring in the circuit | circuits |
|---|---:|
| none | 4,714 |
| `t0` | 2,520 |
| `t1` | 3,032 |
| `t2` | 2,558 |
| `c1,t0` | 65 |
| `c2,t0` | 65 |
| `c1` | 6 |
| `c2` | 6 |
| **total** | **12,966** |

The verifier independently regenerates every polynomial from `Qint,Wint`, checks the current C3 sign, and compares the entire census byte-for-byte at the canonical JSON level.

## Circuit-gated outer box for the entire connected C3 chamber

The exact C3 sample is

`p* = 2^-81(4198946998153136,6902244202549751,82344751025395892224,-43613006256824983552,-83271822072157732864)`.

Every continuous path inside the connected C3 chamber remains in the rational box

`-97/10^6 < c1 < 3661/10^9`,

`-3/12500 < c2 < 3009/(5·10^8)`,

`5549/(2·10^8) < t0 < 463/7812500`,

`-21023/10^9 < t1 < 13359/10^9`,

`-22837/(5·10^8) < t2 < -12353/(5·10^8)`.

The six one-variable barriers have exact Sturm count one between the corresponding rational box face and `p*`:

| coordinate/side | circuit quad | isolated root, decimal |
|---|---|---:|
| `t0` lower | `(516,517,551,552)` | `2.774535459301755e-5` |
| `t0` upper | `(78,79,113,114)` | `5.9263336280933145e-5` |
| `t1` lower | `(2263,2298,2299,2334)` | `-2.1022344778245423e-5` |
| `t1` upper | `(2228,2263,2264,2299)` | `1.3358243156675889e-5` |
| `t2` lower | `(4155,4156,4190,4191)` | `-4.567326075813536e-5` |
| `t2` upper | `(4173,4174,4208,4209)` | `-2.4706649420080026e-5` |

For the collar sides, four exact two-variable circuit evaluations have a uniform sign opposite to C3 over the whole gated `t0` interval:

| coordinate/side | circuit quad | sign on box face | C3 sign |
|---|---|---:|---:|
| `c1` lower | `(480,481,515,516)` | `−` | `+` |
| `c1` upper | `(548,549,583,584)` | `+` | `−` |
| `c2` lower | `(498,499,533,534)` | `−` | `+` |
| `c2` upper | `(566,567,601,602)` | `+` | `−` |

All primitive coefficients, exact isolating fractions, Sturm counts, and exact rational sign intervals are in `certificates/C3_component_gate.json`. Since a circuit determinant cannot vanish inside an open incidence chamber, no path in C3 can cross a face of this box.

## First unclassified boundary

The lower `t1` wall is the certified next boundary. Its primitive exact equation is

`120805790938364358121941406492534423416005773045614510080`

`+5746736507615178773455764667584697822453824419511049402712064 t1`

`+9244056884312266510579850407093993405004088370076400018784256 t1^2`

`+3726169071051075546705280276867227830858564405221519555678289 t1^3 = 0`.

Its unique root between the C3 sample and the lower rational gate is isolated in

`(-43273469370729137627540126/2058451130318719729026213586905,`

` -37330700699942074208946831/1775762936709754474364865163556)`.

The diagonal identity is

`(2263,2298,2334),(2263,2299,2334)  <->  (2263,2298,2299),(2298,2299,2334)`.

The earlier ray parameterization places the same wall at `lambda≈2.737900609196016e-4`; the prior exhaustive 12,966-circuit Sturm census proves no other current circuit occurs first on that ray. It is not crossed here because the centred locus in C3 is empty.

## Chamber-wide moment exclusion

An independent outward-rounding verifier gives, at the exact dyadic C3 sample,

`M_x in [0.1260785168183331,0.12607851722719557]`.

On the full circuit-gated outer box, the directed interval enclosure for the first row of the moment Jacobian, in column order `(c1,c2,t0,t1,t2)`, is

`[-1.9156420184534086, 1.9346309867172387]`,

`[-1.366277278648097, 1.3762836124360975]`,

`[-5.387620454096739, 6.257671542916109]`,

`[-1.2965653614088208, 1.0495082298281264]`,

`[-3.422530834762667, 2.374096041538371]`.

The interval row scalings remain in `[0.999857107110023,1.000059264000001]`; hence every denominator in the actual-cell rational map stays positive. Multiplying the outward derivative bounds by the exact rational coordinate distances from `p*` gives the exact total deviation bound

`|M_x(p)-M_x(p*)| <= 16054249408995478590852120747902120118979843 / 21267647932558653966460912964485513216000000000`.

Subtracting this from the directed sample lower bound gives

`M_x(p) >= 2665339258142487901729251539505183575881020157 / 21267647932558653966460912964485513216000000000`

`= 0.12532364963885445… > 0`.

Therefore:

- the actual ordinary first-moment system has no root in C3;
- the implicit centred branch set over `(c1,c2)` is empty;
- there is no branch endpoint or wall intersection to isolate;
- no successor cell is admissibly reached under the assignment rule.

This is a chamber-wide exact/directed exclusion, not a sampled search and not merely the previous `2^-32` local box.

## Complete actual H/V and mechanics audit

At the exact C3 sample:

- `H_total/H_active/H_inactive = 4324/4324/0`;
- `V/E/F = 8644/12966/4324`;
- boundary triangles `=17284` and Euler value `=2`;
- construction-centre class `=(1,1,0)` with stable row `0`, unstable triple `(4321,4322,4323)`, and no saddle edge;
- ordinary-centroid class `=(2800,2861,5659)`;
- minimum nonincident H/V gap is at least `1.4689044425253426e-9` in the independent audit.

The exhaustive ordinary-centroid interval margins are:

- stable: minimum positive `1.0153564766746113e-8`, closest excluded `-1.6587388920186184e-6`;
- unstable: minimum positive `9.047254744610429e-5`, closest excluded `-2.0828358106846892e-4`;
- full four-component edge cones: minimum positive `1.5601494813610724e-5`, closest excluded `-2.833144047220114e-4`.

The inherited radius-`2^-32` parameter box preserves the complete H/V lattice and construction-centre `(1,1,0)` class, with all 37,350,724 nonincident H/V pairs separated and `M_x>0`. The complete exact ledgers are in `prior_atlas/chambers/C3` and `prior_atlas/certificates`:

- all 4,324 exact H rows;
- all 8,644 exact rational vertices and active triples;
- all 4,324 maximal-face cycles;
- all 12,966 true edges;
- the complete face, vertex, and four-component edge-normal-cone ledgers;
- nonincident separation and perturbation certificates.

`prior_atlas/endpoint_C3.obj` and `.stl` are matching watertight 17,284-triangle meshes; every mesh edge has multiplicity two.

## Prior exact chamber sequence retained in the bundle

The embedded immutable atlas remains part of this result. It certifies

`C0[f9ff70…] -> C1[e897f3…] -> C2[e6c636…] -> C3[df816a…]`

through the exact flips

1. `(569,570,604,605)`;
2. `(4173,4174,4208,4209)`;
3. `(516,517,551,552)`.

Every accepted chamber has all 4,324 rows active and construction-centre `(1,1,0)`. Its two earlier five-equation formula roots are Krawczyk-isolated but rejected after actual hull rebuilding because 1,500-plus rows become inactive and actual `M_x` is strictly positive. Those negative results remain unchanged.

## Reproduction and verification

Run from the archive root:

`python verify_c3_component.py`

This independently regenerates all 12,966 C3 circuit polynomials, checks every gate and exact Sturm count, reconstructs the outward interval derivative of the actual C3 moment map, and proves the exact positive `M_x` lower bound.

Run:

`python verify_all.py --deep`

for the new proof plus the embedded atlas generator, complete H/V/mesh audit, prior exact wall/Sturm census, Krawczyk certificates, 37,350,724-pair endpoint incidence audit, and exhaustive own-centroid mechanics. `verification_transcript.txt` records successful runs; the embedded prior atlas also retains its original successful transcript.

## Scope and continuation boundary

The literal result is: **C3 is a rigorous nonwinner and contains zero centred branches.** This is stronger than the supplied local finite atlas but is not a global exclusion of the five-variable family. The far side of `(2263,2298,2299,2334)`, other disconnected incidence components with a repeated signature, and other support families remain unclassified. The mathematically valid next move is not to cross the wall from C3; it is to start a separate centred component or redesign the profile/collar fields so that a moment root exists before the first incidence gate.
