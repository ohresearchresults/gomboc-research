# figure-0262

AI research report · 2026-09-03 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Calm Quartz 90 — exact wall-242 seventh-support linked cage

The journal requires a finite uniform-density body at its own exact ordinary-volume centroid with strict `(S,U,H)=(1,1,0)`, complete H/V/true-edge mechanics, independent verification, and matching OBJ/STL. The immutable parent is the exact six-support `(9,21,14)`, `(2,2,2)` cage with sole nonprotected carrier `[Z,AA]`; its next frontier is precisely a seventh-support/linked-cell replacement of that whole star.

## Disposition

**EXACT DELIMITED NONWINNER.** No strict own-centred `(1,1,0)` cell was obtained. One new extreme support `AG=40032` and simultaneous release of `AA=40027, AC=40029` realize a zero-bridge, same-boundary, positive-volume full-hull event. The target has 42 supplied dyadic rows, 8 active vertices, `(V,E,F,C)=(8,18,12,36)`, strict `(S,U,H)=(2,2,2)`, and an independent input-coordinate box of radius `2^-17`.

The parent packet `[Z,AA]`, stable `[Z,AD,AB]`, unstable `AA`, saddles `[Z,AD]`,`[AA,AB]` is genuinely absent. Protected stable `[0,H,C]` and unstable `C` survive. The replacement packet is stable `[C,AD,AG]`, unstable `0`, saddles `[0,AE]`,`[C,AD]`, with `[0,Z]` the unique nonprotected adverse edge. The adverse graph has one edge, no two-edge component, and cycle rank zero.

Parent authority is consistent:

```text
result id figure-0260
payload SHA-256 e8bb9a7cec8adfb962fe8969da0ab0aaf4cbfc67902ca5de5ecbffa5b0ab90e0
archive SHA-256 65e7506c7ea2613e375e25bcdc284ce18a456abd17be26f302da14c7b4e793e1
```

## Exact generator and centroid

Let `D=2^24`. Supplied order is

```text
[0,1258,1371,1975,2152,2369,2515,2732,3290,3296,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,AA,AB,AC,AD,AE,AG].
```

Aliases are `A=40001,…,AG=40032`. Any row not overridden is `(i+1,-2(i+1),3(i+1))/D`, with zero-based supplied index `i`; `B=(0,0,0)`.

Source overrides:

```text
0 (2382238,-6308946,46171779)/D; C (-19656014,-12570508,-84150451)/D;
H (-1678613,11935619,-25478204)/D; Z (12438538,-21632755,48020085)/D;
AA (30373224,23777502,105448088)/D; AB (13177543,25487323,-25166961)/D;
AC (-743651,14433279,-37431003)/D; AD (-3239372,-20688692,-53751897)/D;
AE (-1649398,-274969,-52946380)/D; AG (1,-2,3)/D.
```

Source active set `{0,C,H,Z,AA,AB,AC,AD,AE}`; `Vol_s=97139072585169626425407/9444732965739290427392`; source centroid

```text
(2154048737572818233120707778413/6518892811204276876713444507648,
30575775717435404605463621849/1629723202801069219178361126912,
476830870915663719533550360563/2172964270401425625571148169216).
```

Target overrides:

```text
0 (2382238,-6308946,46171779)/D; C (-19656014,-12570508,-84150451)/D;
H (-1678613,11935619,-25478204)/D; Z (8010895,-10409701,39298476)/D;
AB (1683954,13081292,-39025397)/D; AD (2466433,-19765281,18154812)/D;
AE (5834590,17237355,-20273721)/D; AG (7455840,3175317,-13504557)/D.
```

Target active set `{0,C,H,Z,AB,AD,AE,AG}`; all other 34 supplied rows are strict interior. Minimum exact inactive slack is `1789195435225345701723/4722366482869645213696>0`.

```text
Vol=44002819856051551745867/14167099448608935641088
c=(-692401880820759385581342313/11535075208344777980868558848,
   -258294341305269210560387714509/1476489626668131581551175532544,
   -531543412465115174050553320847/738244813334065790775587766272).
```

Centred vertices are `p_i=r_i-c`; exact tetrahedral summation gives `Mx=My=Mz=0`. For each oriented face `(i,j,k)`, `n=(p_j-p_i)×(p_k-p_i)`, `b=n·p_i`, `n·x<=b`; clearing denominators and dividing by the four-entry gcd reconstructs the primitive irredundant H row.

## Actual incidence and mechanics

Maximal faces:

```text
[0,H,C]* [0,C,AD] [0,AE,H] [0,AD,Z] [0,Z,AE] [C,H,AB]
[C,AB,AG] [C,AG,AD]* [H,AE,AB] [Z,AD,AG] [Z,AG,AE] [AB,AE,AG].
```

True edges:

```text
[0,C] [0,H] [0,Z] [0,AD] [0,AE] [C,H] [C,AB] [C,AD] [C,AG]
[H,AB] [H,AE] [Z,AD] [Z,AE] [Z,AG] [AB,AE] [AB,AG] [AD,AG] [AE,AG].
```

Every edge has two incident maximal faces, `8-18+12=2`, and minimum active nonincidence distance `0.09807303189834891`.

Exact stable faces are `[0,H,C]` and `[C,AG,AD]`; their minimum barycentrics are respectively

```text
103304070838852699590566925859697125774604086905973589/408035155254301536633960887967620600460279483337327592,
2523127445155030431186338058822657975926623473995155/21162745312557583764547294934211579276001597088842126.
```

Exactly `0,C` are unstable. Minimum outgoing supports are

```text
0→Z:32339204308819120668873028927997736223/24771385388370603860105686963405717504;
C→AB:5359173078177493796661440427577454859/387052896693290685314151358803214336.
```

Exactly `[0,AE]` and `[C,AD]` are saddles, with normalized `(t,1-t,beta1,beta2)` tuples

```text
(0.7906079248569022,0.2093920751430978,0.4739227994100063,0.8826267488581410),
(0.7010149530158559,0.2989850469841441,1.2364561267870182,1.0883584643459585).
```

Every other face, vertex, and edge has a fixed exact negative witness; closest excluded decisions are `-0.2585208704938105`, `-0.1471386397292707`, and `-0.10725992573444981`. All 12 faces, 36 directed vertex primitives, and 72 true-edge-cone components are audited.

## Connected full-hull surgery and arrow census

Removing common protected face `[0,C,H]` leaves dual-connected one-boundary disks with boundary `0-C-H-0`:

```text
source patch (9,21,13), target patch (8,18,11), both chi=1.
```

Source patch:

```text
[0,C,Z] [0,H,AA] [0,Z,AA] [C,H,AC] [C,Z,AD] [C,AB,AC]
[C,AB,AE] [C,AD,AE] [H,AA,AC] [Z,AA,AB] [Z,AB,AD] [AA,AB,AC] [AB,AD,AE].
```

Target patch:

```text
[0,C,AD] [0,H,AE] [0,Z,AD] [0,Z,AE] [C,H,AB] [C,AB,AG]
[C,AD,AG] [H,AB,AE] [Z,AD,AG] [Z,AE,AG] [AB,AE,AG].
```

All centroid-cone tetrahedra have positive exact volume; minima are `129533263274328916781039477272586541162496879/647613600781054113391573531681843142285328384` and `42893514982821901319250090521063287248758063/623392324919906263517140339520162727299383296`.

Removed edges:

```text
[0,AA] [C,Z] [C,AC] [C,AE] [H,AA] [H,AC] [Z,AA] [Z,AB]
[AA,AB] [AA,AC] [AB,AC] [AB,AD] [AD,AE].
```

Inserted edges:

```text
[0,AD] [0,AE] [C,AG] [H,AB] [H,AE] [Z,AE] [Z,AG] [AB,AG] [AD,AG] [AE,AG].
```

Star-changed inherited edges:

```text
[0,C] [0,H] [0,Z] [C,H] [C,AB] [C,AD] [Z,AD] [AB,AE].
```

Negative external-arrow witnesses exist for every inserted edge and for star-changed `[0,H],[C,H],[C,AD],[Z,AD],[AB,AE]`; `[0,C]` and `[C,AB]` are protected-`C` edges. The only nonprotected all-positive changed edge is `[0,Z]`.

For `[0,Z]`, every external endpoint arrow is positive, minimum

```text
5865539893527569625621339207628030095/1548211586773162741256605435212857344.
```

Mutual arrows are

```text
sigma(0→Z)=32339204308819120668873028927997736223/24771385388370603860105686963405717504,
sigma(Z→0)=-23913521012819517482261742231671146701/24771385388370603860105686963405717504,
```

with sum `||Z-0||²=95740265323483/281474976710656>0`. Hence one endpoint is unstable in addition to `C`; this proves `U>=2` throughout the certified sign chamber.

## Exact chronology and open box

The affine 42-row source-target chord, with actual hull and ordinary centroid recomputed in every side cell, has 16 simple Sturm-isolated decisive events:

```text
0.523589902 [2617/5000,2619/5000] Z/[Z,AA] birth;
0.542726029 [2713/5000,543/1000] [0,Z,AA]/[0,Z] birth;
0.552370433 [2761/5000,2763/5000] unstable 0/[0,AA] birth;
0.555795411 [1389/2500,139/250] [0,Z,AA]/[Z,AA] death;
0.608575546 [1521/2500,761/1250] unstable Z/[0,Z] death;
0.613690263 [767/1250,307/500] [C,AD]/unstable AD birth;
0.617726543 [386/625,309/500] unstable AA/[0,AA] death;
0.654554319 [409/625,1637/2500] [Z,AD]/unstable AD death;
0.712644663 [3563/5000,713/1000] stable Z-AB-AD→AB-AD-AG;
0.797713028 [997/1250,399/500] stable AB-AD-AG→C-AD-AG;
0.799876842 [3999/5000,4001/5000] AE activation;
0.800820475 [8008203/10^7,8008207/10^7] [AA,AE] birth;
0.800821201 [800821/10^6,4004107/5·10^6] [AA,AB] death;
0.867726078 [21693/25000,86773/100000] [0,AE] birth;
0.867840672 [86783/100000,17357/20000] [AA,AE] death;
0.871327367 [1089/1250,2179/2500] AA deactivation.
```

Replacement unstable `0` is born before `AA` dies; target saddle `[C,AD]` before `[Z,AD]` dies; bridge `[AA,AE]` before `[AA,AB]` dies; target `[0,AE]` before that bridge dies; and the stable component transfers without a gap. No strict `(1,1,0)` interval exists on this connector.

All 126 uncentred supplied coordinates vary independently by `2^-17`. Directed interval recomputation preserves the complete `(8,18,12)`, `(2,2,2)` body and gives

```text
Vol∈[43999877150896244518475/14167099448608935641088,
     44005762571664107503691/14167099448608935641088]
topology clearance 0.20259506645332925; face 0.2739408122149904;
vertex 0.14670132560921895; edge cone 0.14576108239108326;
forcing external 3.7874864916809634; anti-carrier 0.14670132560921895.
```

## Verification, exact scope, and successor

A fresh clean extraction independently reruns exact generation, source reconstruction, Fraction H/V/E and mechanics, a standard-library-only reconstruction, symbolic rederivation and Sturm replay of all 16 events and 32 side ledgers, the complete interval proof, and OBJ/STL matching. It passes all aggregate and package markers. OBJ/STL agree on 8 exact-centred vertices, 12 outward facets, 18 edges, Euler two, and edge multiplicity two.

Closed: this one-`AG` linked topology; release of `AA,AC`; exact parent-packet deletion; all 18 changed-edge decisions; absence of any nonprotected adverse two-edge component/cycle; the 16-event chronology; the `2^-17` chamber; and the `[0,Z]` theorem. Not closed: all seventh-support placements, other linked boundaries, an eighth-support annular/prismatic cage, or global existence.

The next nonserial cell must jointly couple `[0,Z]→[AD,AE]`, stable death `[AD,AG]→[C,Z]`, and saddle exchanges `[0,AE]→[H,Z]`, `[C,AD]→[0,AG]`, permitting `0` or `Z` to deactivate and preassigning negative external arrows before moment closure.

## Final statement

**NONWINNER, rigorously delimited.** The seventh-support surgery genuinely destroys the immutable six-support packet and reaches the eight-vertex lower-bound frontier, but inherited star-changed edge `[0,Z]` becomes the unique nonprotected forcing carrier and every replacement channel is born before its source channel dies.

## Artifacts

- Complete exact archive (`Calm_Quartz_90_wall242_twelfth_seventh_support_linked_cage_exact_NONWINNER.zip`)
- Complete handoff (`Calm_Quartz_90_wall242_twelfth_seventh_support_linked_cage_handoff.md`)
- Structured result (`Calm_Quartz_90_wall242_twelfth_seventh_support_linked_cage_result.json`)
- Clean verification (`Calm_Quartz_90_wall242_twelfth_seventh_support_linked_cage_clean_verification.json`)
- Exact generator (`generator_exact.json`)
- Irredundant H-data (`twelfth_cage8_exact_H_irredundant.csv`)
- Full mechanics ledgers (`twelfth_cage8_exact_faces.csv`)
- Independent verifier (`verify_independent.py`)
- Watertight OBJ (`body.obj`)
- Watertight STL (`body.stl`)

```text
archive SHA-256 c716f4279a8d692ac20cb5d90428b4bac69a98726f31c80b76199740f8b4e7a4
manifest entries 50; manifest SHA-256 b265d98c350217935433f9e360cdc53cbcd4dd41bcd2004de743a48e86eae4b4
clean extraction PASS
```
