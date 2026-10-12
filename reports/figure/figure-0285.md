# figure-0285

AI research report · 2026-09-04 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Calm Finch 13 — exact finite determination

## Disposition

**Exact topology-changing nonwinner.** I did not obtain strict `(S,U,H)=(1,1,0)`. I did materialize the requested smallest nine-active-vertex carrier-splitting basin insertion. It removes the parent adverse carrier `[AT,AW]`, leaves `[0,AT]` absent, deactivates `AT`, destroys both parent stable/saddle roles, keeps `C` unstable, and gives both replacement edges strict negative external arrows at the exact ordinary-volume centroid. The endpoint is nevertheless strict `(2,2,2)` because a new carrier-free Euler-neutral packet is born at `AX`.

Parent authority: `figure-0279`, SHA-256 `ef634da1ba4229d09a956635d8a24a879b52b66f54c57e14dc6322b64e1052ff`; 58 supplied rows, active `{0,C,H,AS,AT,AU,AV,AW}`, `(V,E,F)=(8,17,11)`, stable `[C,AU,AW]`, `[0,AW,AT,H]`, unstable `C,AT`, saddles `[0,C]`, `[AT,AV]`, and unique nonprotected all-external-positive edge `[AT,AW]`. The completed 1,681-point one-plane atlas and compatible collar were nonwinning.

## Exact deterministic construction

Let `D=2^27=134217728`. Supplied order is

```text
0,1258,1371,1975,2152,2369,2515,2732,3290,3296,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,AA,AB,AC,AD,AE,AG,AH,AI,AJ,AK,AL,AM,AN,AO,AP,AQ,AR,AS,AT,AU,AV,AW,AX
```

For parent position `i=0,...,57`, use `(8(i+1),-16(i+1),24(i+1))/D`, except `B=(0,0,0)`, then replace/apply these numerator triples:

```text
0 =(  19057904, -50471568,  369374232)/D
C =(-157248112,-100564064, -673203608)/D
H =( -13428904,  95484952, -203825632)/D
AS=(  13481528, 106209064, -370999584)/D
AT=( 215035232, 155090168,  624881392)/D
AU=(  62805192,  67862424, -143066648)/D
AV=(  46873424, 109782944, -360206208)/D
AW=( 100671104,  -9875047,  608489383)/D
AX=( 707139249, 189989663, 4124289023)/D
```

Active rows are exactly `{0,C,H,AS,AT,AU,AV,AW,AX}`. The other 50 rows are strictly inactive:
`{1258,1371,1975,2152,2369,2515,2732,3290,3296,A,B,D,E,F,G,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,AA,AB,AC,AD,AE,AG,AH,AI,AJ,AK,AL,AM,AN,AO,AP,AQ,AR}`.

## Coupled incidence event

Put `M=(AT+AW)/2` and `AX(s)=M+s(AX-M)`, `0<=s<=1`. At `s=0`, `AX` lies in the relative interior of `[AT,AW]`. Its exact endpoint signed outward numerators are positive for exactly two parent maximal planes:

```text
[0,AW,AT,H] : 264385157837613794897480
[AT,AW,AU]  : 237088770303346811674415
```

Every other parent facet value is strictly negative. Hence for every `0<s<=1` the same two planes are crossed simultaneously: the two positive heights equal `s` times their endpoint values, while every other height is a convex combination of two strict negative values. The operation removes `[0,AW,AT,H]`, `[AT,AW,AU]`, and edge `[AT,AW]`; it cones the pentagonal boundary `0-H-AT-AU-AW-0` to `AX`, inserting faces
`[0,AX,H]`, `[0,AW,AX]`, `[H,AX,AT]`, `[AT,AX,AU]`, `[AU,AX,AW]`
and edges `[0,AX]`, `[H,AX]`, `[AT,AX]`, `[AU,AX]`, `[AW,AX]`.

The three exact positive cap tetrahedron volumes are

```text
[0,AW,AT,AX] : 33048144729701724362185/37778931862957161709568
[0,AT,H,AX]  : 33048144729701724362185/9444732965739290427392
[AT,AW,AU,AX]: 237088770303346811674415/604462909807314587353088
```

with total gain `2880940348679484760649215/604462909807314587353088>0`. This is a genuine two-support-plane positive-volume cap, not an `AW` reparameterization or serial diagonal transfer; it has nine active vertices and `[AT,AW]` is absent, so it lies outside both completed parent atlases.

## Fresh hull and exact H/V certificate

Fresh enumeration from all 59 V-rows gives exactly 14 primitive irredundant inequalities `n·(D x)<=b`:

```text
0  [0,H,C]     (-1413156603516698,524910611565993,213752795704821)              <=25529910238959260504456   w=128
1  [0,C,AW]    (948348700958992,-1341583566669987,-95912562075723)             <=50357735758395450932648   w=32
2  [0,AX,H]    (-42867915043584994,17026433593959997,6765111027253753)          <=822534279570751074134824  w=16
3  [0,AW,AX]   (18987710721166246,-28383987422176621,-1661779646830309)         <=1180631738592112497922424 w=5
4  [C,H,AS]    (-32819401714747,31835060312774,-3240825016833)                  <=4141061008104500087592    w=1152
5  [C,AS,AV]   (17995924998547,128881502208201,-98349680311992)                 <=50418686765482794885008   w=64
6  [C,AV,AU]   (918682352048195,-614629039877515,-186063760363576)              <=42607323510009728845328   w=64
7  [C,AU,AW]   (20974181173822161,-18163533535921113,-2935501238903905)         <=504638383961617276962440  w=8
8  [H,AT,AS]   (-29455603842338,94522057066656,1321988860053)                   <=9151535343314434819568    w=640
9  [H,AX,AT]   (-22457686384656302,48959885687713301,2669835406967669)          <=4432333560177285750807752 w=8
10 [AS,AT,AV]  (-47368233870934,485607954179778,-14248499835651)                <=56223557624798153369824   w=64
11 [AT,AU,AV]  (798958986277085,-325318654610120,-121425853390503)              <=45473849884114869738384   w=64
12 [AT,AX,AU]  (34805554275784333,-19350581039019820,-4701546462052231)         <=1545426676582804305504944 w=8
13 [AU,AX,AW]  (84703780148175290,-64533166441252163,-10942671871025363)        <=2505991456984599169075792 w=5
```

All weights are positive and their weighted normal sum is exactly `(0,0,0)`. Normals 0,1,2 have nonzero determinant `466900306563407432156973383149762891342447104`, so the recession cone is `{0}`. Every H-row has exactly its three affinely independent equality vertices and strict slack at all other supplied rows, proving irredundancy. Exact H-plane triple intersection reconstructs precisely the nine active numerator triples. Minimum inactive squared facet distance is
`10184004950145576340502511543069768431185249/652524577959168480524825053224006026593828864>0`; minimum active nonincidence squared distance is
`9121175689484171883782780802048600995188225/5141076290951016464224610672491048149662564352>0`.

## Volume and own centroid

```text
Vol = 13927739138863031418107597/1813388729421943762059264
c = (8880453107810947224991087343079669/7477398013579490320524078915518464,
     508408188203593583718080615647367/934674751697436290065509864439808,
     21672968208057635806944934654565499/3738699006789745160262039457759232)
```

Translate by `-c`. The oriented surface formula has `V6_num=111421913110904251344860776`; exact recomputation after translation gives first moments `(Mx,My,Mz)=(0,0,0)`.

## Incidence and exhaustive equilibrium classification

Maximal faces:

```text
[0,H,C] [0,C,AW] [0,AX,H] [0,AW,AX] [C,H,AS] [C,AS,AV] [C,AV,AU]
[C,AU,AW] [H,AT,AS] [H,AX,AT] [AS,AT,AV] [AT,AU,AV] [AT,AX,AU] [AU,AX,AW]
```

True edges:

```text
[0,C] [0,H] [0,AW] [0,AX] [C,H] [C,AS] [C,AU] [C,AV] [C,AW] [H,AS] [H,AT]
[H,AX] [AS,AT] [AS,AV] [AT,AU] [AT,AV] [AT,AX] [AU,AV] [AU,AW] [AU,AX] [AW,AX]
```

Every edge has two incident faces; `(V,E,F,C)=(9,21,14,42)` and `9-21+14=2`. `[0,AT]` and `[AT,AW]` are absent.

Using exact own-centred face-foot barycentrics, directed supports `sigma(v->w)=-v·(w-v)`, and edge tuples `(t,1-t,beta1,beta2)`, the complete sign ledger is:

```text
faces (lambda signs):
[0,H,C] ++-; [0,C,AW] -++; [0,AX,H] +++ STABLE; [0,AW,AX] -+-;
[C,H,AS] -+-; [C,AS,AV] -+-; [C,AV,AU] --+; [C,AU,AW] -++;
[H,AT,AS] ++-; [H,AX,AT] ++-; [AS,AT,AV] ++-; [AT,AU,AV] ++-;
[AT,AX,AU] -++; [AU,AX,AW] +++ STABLE.

vertices (neighbor sigma signs):
0: C-,H-,AW+,AX+; C: 0+,H+,AS+,AU+,AV+,AW+ UNSTABLE;
H:0+,C-,AS-,AT+,AX+; AS:C-,H+,AT+,AV+; AT:H-,AS-,AU-,AV-,AX+;
AU:C-,AT+,AV-,AW+,AX+; AV:C-,AS-,AT+,AU+; AW:0-,C-,AU-,AX+;
AX:0+,H+,AT+,AU+,AW+ UNSTABLE.

edges (t,1-t,beta1,beta2 signs):
[0,C]-+++ [0,H]-++- [0,AW]+--+ [0,AX]++++ SADDLE [C,H]+--+ [C,AS]+--+
[C,AU]+-+- [C,AV]+-++ [C,AW]+-+- [H,AS]-++- [H,AT]+-+- [H,AX]++-+
[AS,AT]+--+ [AS,AV]+-+- [AT,AU]-++- [AT,AV]-+++ [AT,AX]++++ SADDLE
[AU,AV]-++- [AU,AW]+-+- [AU,AX]+++- [AW,AX]+++-.
```

Therefore stable faces are exactly `[0,AX,H]`, `[AU,AX,AW]`; unstable vertices exactly `C,AX`; saddle edges exactly `[0,AX]`, `[AT,AX]`. The endpoint is strict `(S,U,H)=(2,2,2)`.

## External-arrow antibirth census

The only all-external-positive true edge is protected `[C,AS]`. Every other edge has a strict negative witness. On every inserted or star-changed edge:

```text
[0,H]   H->C  = -3351853869963679051950846590329681631322799/125449921591794042277341705166699022516224
[0,AW]  0->C  = -198907998024912832469058456922835832320299/7840620099487127642333856572918688907264
[0,AX]  0->C  = same
[H,AT]  H->C  = -3351853869963679051950846590329681631322799/125449921591794042277341705166699022516224
[H,AX]  H->C  = same
[AT,AU] AU->C = -3554645588609450606786405186710513081214203/125449921591794042277341705166699022516224
[AT,AX] AT->AV= -479847691740504056859195144104949443473267/62724960795897021138670852583349511258112
[AU,AW] AU->C = -3554645588609450606786405186710513081214203/125449921591794042277341705166699022516224
[AU,AX] AU->C = same
[AW,AX] AW->C = -6685025556935822820392598532947711278027925/501799686367176169109366820666796090064896
```

Thus neither replacement edge is adverse and no nonprotected carrier substitutes for `[AT,AW]`. The parent one-edge forcing component is destroyed, not transferred.

## Positive endpoint cell

A directed exact rational interval verifier varies all 27 uncentered active coordinates independently by coordinate radius `2^-27=1/134217728`, fixes the 50 inactive rows, and recomputes the ordinary centroid interval-exactly. It proves 1,065 strict inequalities: all 59-row separation and support signs, all 42 face-barycentric signs, all 42 directed vertex-support signs, all 84 edge-cone component signs, and the full arrow antibirth property. Throughout the box, `[AT,AW]` stays absent, both replacement witnesses stay negative, no nonprotected all-positive edge is born, and the class remains `(2,2,2)`. This is the exact endpoint-cell death/antibirth certificate; no clean `(1,1,0)` chronology along the simple ingress is claimed.

## Residual obstruction and first unrepresented successor

The entire parent stable/saddle packet is gone, but a carrier-free `AX` packet remains: stable `[0,AX,H]`, `[AU,AX,AW]`; unstable `AX`; saddles `[0,AX]`, `[AT,AX]`. Relative to the intended `C` plus one stable face, the excess is Euler-neutral `(Delta S,Delta U,Delta H)=(1,1,2)`.

The first truly unrepresented successor is **joint AX-star metric cancellation** in or across this exact 27-dimensional cap chamber: retain `C` as the sole unstable vertex and exactly one current stable face, while simultaneously making `AX` nonunstable and both current saddle edges nonsaddles without creating a nonprotected all-positive edge. If that finite sign-disjunction is empty, add a tenth extreme vertex and replace the AX pentagonal cap by a connected two-cell cap with preassigned negative exits. Another one-plane carrier transfer is not the next move.

## Verification and artifacts

`verify_cleanroom.py` does not import the construction kernel or trust stored H/F/E ledgers. It independently rebuilds hull, H-to-V, volume, centroid, zero moments, all face/vertex/edge mechanics, arrows, and mesh incidence. The primary exact verifier, interval verifier, clean-room verifier, and clean extraction all pass. OBJ has 9 vertices, 14 oriented triangles, and 21 undirected edges each used twice; STL has the same 14 facets.

- Complete exact handoff with all rational mechanics rows (`HANDOFF.md`)
- Deterministic exact archive (`Calm_Finch_13_AX9_exact_NONWINNER.zip`), SHA-256 `099616b9ef7ef06ffba713e434d5fbcb2c5e28c07810b6f17bcb215332a6cb67`
- Immutable manifest (`MANIFEST.json`), SHA-256 `bb2ea6e2c2c73721b3d608840cc2c74b6fb5170978b4edbf214645508fc8b0ce`
- Independent clean-extraction receipt (`Calm_Finch_13_AX9_clean_extraction_receipt.json`)
- Watertight OBJ (`body.obj`) and STL (`body.stl`)

Exact generator SHA-256: `8fbd37ade9de63001afd4af3881b880265baac1f01a67e4992197de552166f0d`.
