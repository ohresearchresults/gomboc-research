# figure-0097

AI research report · 2026-08-27 UTC

---

# P9 communicating-annulus post-event body — exact fallback handoff

The starting seed and acceptance gate are those fixed in the attached journal: exact nine-row P9, exact own-centering, the localized four-feature block, and the requirement that a transferred `(2,2,2)` state not be called a Gömböc.

## Verdict

No homogeneous polyhedral Gömböc was obtained. The body below is an exact, finite, own-centred, strictly separated **nonwinner** with class `(S,U,H)=(2,2,2)`. It must not be presented as a Gömböc. It is the strongest fully reconstructible post-event body from this assignment because it deactivates both source rows, discards every obsolete original row except `o27`, retains 13 cross-linked new extreme supports, and has raw inactive slack `0.013598898595190763`.

## What changed

- Final f-vector `(F,E,V,C)=(14,36,24,72)`.
- Original P9 rows `o13` and `o15` are strictly redundant by raw support separations `0.2205373501588912` and `0.22006413380978965`.
- The other obsolete originals `o09,o26,o32,o100,o102,o103` are also redundant. Only `o27` remains extreme.
- The 13 new rows induce a connected graph; the complete 14-row support graph is biconnected and has no articulation vertex.
- The original target was deliberately rebuilt: stable `n17` has margin `0.7414544929429717`; unstable vertex `[n17,n22,n24]` has normalized full-cone margin `7.416914983451878`.
- Residual transferred block: stable `n16` `+0.0027181704193414754`; unstable `[n09,n18,n21]` `+0.06836474008568874`; saddles `[n11,n17]` `+0.04776696728614949` and `[n17,n24]` `+0.07524673629048033`.

## Exact generator data

Each hexadecimal binary64 below is interpreted as its exact dyadic rational. Let `B_i` be these rows and define the raw polytope `P={x:B_i·x<=1}`. Enumerate all feasible triple intersections, integrate the ordinary uniform-volume centroid `c` exactly, and output the own-centred rows `H_i=B_i/(1-B_i·c)`. The active vertices are the feasible intersections of the resulting `H` rows. This deterministic rule is implemented in `post_event_exact.py`.

```text
o27: [ -0x1.b2257479720e7p+4, 0x1.6d8cb417f7403p+2, 0x1.e848d175dee16p-5 ]
n09: [ 0x1.d3aa7b9264b9fp+3, -0x1.d7f6566676966p+2, -0x1.d64e8329828cep+1 ]
n10: [ 0x1.f70d7273166b1p+3, 0x1.5d25f3e1d090fp+3, 0x1.dbf0524932645p+0 ]
n11: [ -0x1.c3a86418d24a2p+3, 0x1.29690b894a715p+4, 0x1.9823349432be6p+2 ]
n13: [ 0x1.bca66cd1358efp+3, -0x1.2b603a5c975dbp+3, -0x1.037715d736558p+2 ]
n14: [ -0x1.2e22514454920p+3, -0x1.81bbc0e6b23b8p+3, -0x1.8aaba73c68de5p+3 ]
n16: [ -0x1.a0b3ea0698507p+4, 0x1.5eb21b2198f89p+2, 0x1.14b9fd26999d0p-3 ]
n17: [ 0x1.0714ae0d32c31p+4, -0x1.1e36654c94173p+3, -0x1.75ae447b2563cp+0 ]
n18: [ -0x1.d4856ce420c11p+1, 0x1.49136a8e6aa1ep+3, -0x1.269e86badde6cp+4 ]
n21: [ 0x1.f1981a3c94482p+3, 0x1.3d8c05b335556p+2, -0x1.026a304bf2f2ep+1 ]
n22: [ -0x1.938f20defd89ep+2, 0x1.a23287603c186p+2, 0x1.4ff19bf423ae1p+1 ]
n23: [ -0x1.fc1ae1acbabf6p+1, 0x1.e3e6f12385ffep+3, 0x1.3047e3aa0bdcfp+2 ]
n24: [ -0x1.74ccaf4626368p+4, 0x1.1d4d1ef20afd8p+2, 0x1.4d3d4fcb7e9d0p-5 ]
n26: [ -0x1.6065140585c0fp+4, 0x1.46503f1d9eaf7p+3, 0x1.44570a31fb5adp+1 ]
```

Raw exact centroid, decimal enclosure: `['-0.047462743046490556', '-0.23412983059209866', '0.54201459244776384']`.
Own centroid after translation: exactly `(0,0,0)`.
Exact volume is the rational `certificate.json.volume_exact` (2251 characters); directed interval `['0.015348886418373765', '0.015348886418373769']`. Its exact value begins `737563908086049210453920422090092423148305400330159493491255145334407853272004895288340769903572...` and ends `...143574511689178409874607948011300651206195938607280904661254347816050246245259747666181660723355`.

### Own-centred H rows (display decimals; exact fractions are in the certificate)

```text
o27: -26.67756712035208 5.6156037795130009 0.058602080958706657
n09: 7.4617908921256886 -3.7651700715647261 -1.8759812330463317
n10: 4.7738562565063978 3.3133390224949313 0.56456907612694296
n11: -11.515977689853575 15.166220634119812 5.2031679983263128
n13: 8.3379538904018595 -5.613812709831322 -2.4327091034247927
n14: -2.1387693830613164 -2.7305588532322114 -2.7938235319956513
n16: -26.750419792280081 5.6282667976153524 0.13878579076881889
n17: 34.435238534435854 -18.73149969380049 -3.056994774880808
n18: -0.27699348700659698 0.77820911503080703 -1.3934500773921916
n21: 3.8933265444394816 1.2422915495717046 -0.50547881113750148
n22: -7.8034845313193486 8.0865400121880011 3.2480151818643068
n23: -2.2361971708607244 8.5187158728959744 2.678312142045947
n24: -25.442692494596709 4.8677848926750391 0.044419554836059957
n26: -22.735729040472812 10.526508485364966 2.6157116862736927
```

## Complete incidence

### Maximal-face cycles

```text
o27: 18 20 21 22 23 19
n09: 0 1 3 2
n10: 4 5 7 6 8
n11: 4 18 19 11 9 10 5
n13: 0 12 13 1
n14: 12 14 21 20 13
n16: 15 23 22
n17: 0 2 6 7 10 9 16 14 12
n18: 1 13 20 18 4 8 3
n21: 2 3 8 6
n22: 9 11 17 16
n23: 5 10 7
n24: 14 16 17 15 22 21
n26: 11 19 23 15 17
```

### True edges (vertex ids / incident rows)

```text
0-1 : n09 n13
0-2 : n09 n17
0-12 : n13 n17
1-3 : n09 n18
1-13 : n13 n18
2-3 : n09 n21
2-6 : n17 n21
3-8 : n18 n21
4-5 : n10 n11
4-8 : n10 n18
4-18 : n11 n18
5-7 : n10 n23
5-10 : n11 n23
6-7 : n10 n17
6-8 : n10 n21
7-10 : n17 n23
9-10 : n11 n17
9-11 : n11 n22
9-16 : n17 n22
11-17 : n22 n26
11-19 : n11 n26
12-13 : n13 n14
12-14 : n14 n17
13-20 : n14 n18
14-16 : n17 n24
14-21 : n14 n24
15-17 : n24 n26
15-22 : n16 n24
15-23 : n16 n26
16-17 : n22 n24
18-19 : n11 o27
18-20 : n18 o27
19-23 : n26 o27
20-21 : n14 o27
21-22 : n24 o27
22-23 : n16 o27
```

### Active vertices

```text
id  active triple             x y z                              normalized U-cone margin
00  n09,n13,n17              0.098886210731585933 0.2248593504097379 -0.59103228238588545 -6.5519421650540979
01  n09,n13,n18              0.09655407158215086 0.22912724579064672 -0.60887429809029581 -0.23029375081646439
02  n09,n17,n21              0.10516967461149899 0.23597161356243906 -0.58834231256564407 -6.3776802514477726
03  n09,n18,n21              0.10225321492037286 0.23840469875327616 -0.60482594862653849 0.068364740085688727 U
04  n10,n11,n18              0.06330509056164893 0.30591489165632541 -0.55938088727805979 -0.15750098565495374
05  n10,n11,n23              0.093439857490144648 0.19707616408343362 -0.17544105289496387 -83.777224103288532
06  n10,n17,n21              0.10952638435918501 0.23777931697781385 -0.55034311663315372 -3.9728191307584377
07  n10,n17,n23              0.10831816869997873 0.14565459749984594 0.00053416130817461464 -1.3363485327526663
08  n10,n18,n21              0.0961763568606602 0.26368590865990926 -0.58949901410705963 -0.41649615388451444
09  n11,n17,n22              -0.033865102096073893 -0.25705742045784147 0.86651051735185081 -13.128827461839679
10  n11,n17,n23              0.10536957523315717 0.13521874916174192 0.03126485517477659 -2.4231028957213328
11  n11,n22,n26              -0.070568925676724931 -0.24071567117572107 0.73764229920804092 -17.172113027674524
12  n13,n14,n17              0.056274786051790752 0.13743437096003619 -0.53533496682264714 -14.038487418737882
13  n13,n14,n18              0.077863068236660157 0.20547932511853123 -0.61836566160652451 -0.023061388045086617
14  n14,n17,n24              -0.069472551904339444 -0.15629642506415381 -0.15199157748272968 -0.22938478970463572
15  n16,n24,n26              -0.074916517229992402 -0.19068671953924801 0.498519673143687 -245.28646130125645
16  n17,n22,n24              -0.13215498418372018 -0.49650086319574449 1.2265043414043633 7.4169149834518775 U
17  n22,n24,n26              -0.12939522736751316 -0.481802887507012 1.1965414122213269 -61.857956058444572
18  o27,n11,n18              0.01921832259235997 0.27529852086027667 -0.56771573286773447 -0.19552785271329884
19  o27,n11,n26              0.010637070006431968 0.23345780114753795 -0.46475075585843012 -116.48932039708414
20  o27,n14,n18              0.0097608204353850855 0.23061040148763823 -0.59079301123619976 -0.24476494703759077
21  o27,n14,n24              -0.056831890588453109 -0.08954320731378887 -0.22691007062196911 -34.094549921568245
22  o27,n16,n24              -0.05735381267043211 -0.09400171570372956 -0.037264839426445998 -102.46421602429407
23  o27,n16,n26              -0.029054942622079718 0.040388463823080117 -0.032776857761695651 -272.06031199414679
```

## Exhaustive equilibrium audit

### Stable-face test (minimum support slack; positive means stable)

```text
o27    -0.0027169768149895497 witness=n16
n09       -3.5412555538307369 witness=n17
n10       -1.9512775189966911 witness=n17
n11      -0.11643818868886732 witness=n26
n13       -2.7372112316802624 witness=n17
n14       -1.0951934010267441 witness=o27
n16      0.002718170419341475 witness=o27 STABLE
n17       0.74145449294297161 witness=n13 STABLE
n18       -3.4503805190310008 witness=o27
n21       -5.6252456472429442 witness=n17
n22      -0.98074051812427954 witness=n26
n23      -0.99291407731363734 witness=n11
n24     -0.055106735953459163 witness=n16
n26     -0.052377194924387069 witness=n16
```

### Unstable-vertex full-cone test

The vertex table above lists all 24 normalized minimum cone coefficients. Exactly vertices 3 and 16 are positive. Exact unnormalised cone coefficients for every vertex are in `certificate.json`.

### Saddle-edge full-cone test (normalized minimum of `t,1-t,mu_1,mu_2`)

```text
n09 -n13  v=00-01      -32.966528995815736
n09 -n17  v=00-02      -8.9904992500295187
n13 -n17  v=00-12      -5.2734077945366886
n09 -n18  v=01-03      -1.5640730423721938
n13 -n18  v=01-13     -0.44596028788837355
n09 -n21  v=02-03      -34.827634472783011
n17 -n21  v=02-06      -13.644629601707171
n18 -n21  v=03-08      -3.2419540477039086
n10 -n11  v=04-05      -0.5369038192333323
n10 -n18  v=04-08      -1.5937665671865613
n11 -n18  v=04-18      -1.5401223435060738
n10 -n23  v=05-07     -0.17096409368105106
n11 -n23  v=05-10      -2.1173792815358268
n10 -n17  v=06-07     -0.34131249011597431
n10 -n21  v=06-08      -11.016327281127282
n17 -n23  v=07-10     -0.71661056348163299
n11 -n17  v=09-10      0.04776696728614948 SADDLE
n11 -n22  v=09-11      -8.4040284282432509
n17 -n22  v=09-16       -1.916773387982631
n22 -n26  v=11-17      -1.9306268736117318
n11 -n26  v=11-19     -0.38234945764645017
n13 -n14  v=12-13      -4.5883740789660274
n14 -n17  v=12-14    -0.014535298815090416
n14 -n18  v=13-20      -1.8506566892584597
n17 -n24  v=14-16     0.075246736290480315 SADDLE
n14 -n24  v=14-21     -0.20603457400631522
n24 -n26  v=15-17     -0.70887950704449809
n16 -n24  v=15-22       -50.52563040864144
n16 -n26  v=15-23     -0.79502812893807795
n22 -n24  v=16-17      -38.603166169283959
n11 -o27  v=18-19      -4.6444589248174228
n18 -o27  v=18-20     -0.23558446135788258
n26 -o27  v=19-23     -0.74432736416860612
n14 -o27  v=20-21     -0.20939147172236397
n24 -o27  v=21-22      -50.851184344362501
n16 -o27  v=22-23      -231.85169196753802
```

## Separation, boundedness, and perturbation

Minimum nonincident support slack: `['0.013598898595190761', '0.013598898595190765']` at vertex 16 against row `n26`.
Origin-in-dual tetrahedron: rows `n11,n13,n17,n24` with positive exact barycentric weights; minimum weight interval `['0.21341523980931212', '0.21341523980931218']`.
Directed-rounding interval verification proves that all 42 raw coefficients may vary independently by `±2^-40`, with the body reintegrated and translated to its own centroid, while the complete incidence and `(2,2,2)` class remain fixed. The interval lower bound on nonincidence is `0.0131735978574910612`.

## Circuit/topology path

The deterministic path starts from exact P9 with all 13 new rows latent at scale `1/256`, raises all new rows together, and moves `o27` to its final value. It contains `48` actual circuit walls and `49` open hull cells. Each wall in `topology_path.json` has an exact dyadic isolating interval, determinant sign change, nonzero derivative certificate, removed/added Q facets and edges, and own-centroid mechanical class on both sides.
Source `o13` leaves at event `42` and source `o15` at event `43`. They are close, coupled walls (`t≈0.77697` and `t≈0.77907`) but **not one elementary simultaneous circuit**. This is a precise remaining failure relative to the requested stronger event.
The endpoint active new-row graph is connected, and the complete active support graph is biconnected, so the final replacement is communicating rather than a disjoint collection of caps.

## Reproduction and independent checks

- `post_event_exact.py`: exact Fraction generator, exact centroid/volume/incidence/mechanics, OBJ/STL writer.
- `verify_cleanroom.py`: independent exact reconstruction from `certificate.json`; returns `CLEANROOM PASS`.
- `verify_perturbation_box_iv.py 40`: independent directed-rounding perturbation proof.
- `topology_path.py`: exact-seed/dyadic circuit path generator.
- `post_event.obj` and `post_event.stl`: matching watertight meshes. Trimesh independently reports Euler number 2, 24 vertices, 44 triangles, volume `0.015348886418373772`, and centre of mass within `4e-17` of zero.

## Sharp next architecture

Do not continue by another short local cap. The residual block is concentrated on the communicating hub `n17`: extra stable `n16`, extra-U facet `[n09,n18,n21]`, and saddle edges `[n11,n17]`,`[n17,n24]`. The next cell should replace these four features and the near-transfer pair `o27/n16` in one coupled event. Use a 12-edge norm-ascent from the `n16/o27` lobe to the rebuilt stable `n17` lobe, two transverse closure bands through the `n11` and `n24` saddle stars, and a third branch through the `[n09,n18,n21]` facet. Permit `n16,n09,n18,n21,n11,n24` and `o27` to become non-extreme together; keep roughly 13–16 active supports by deleting obsolete nodes as new cross-links enter. Eliminate all three ordinary volume moments as dependent equations in every cell and enumerate the full four-component edge-cone branches, not selected witnesses.

## Files

- Bundle: p9_post_event_bundle.zip
- Exact certificate: certificate.json
- Manifest: manifest.json
- Generator: post_event_exact.py
- Independent verifier: verify_cleanroom.py
- Perturbation verifier: verify_perturbation_box_iv.py
- Topology path: topology_path.json / topology_path.py
- Meshes: post_event.obj, post_event.stl

- Full human-readable report: post_event_report.md
- Verification transcript: verification.log
- Mesh audit: mesh_audit.log
