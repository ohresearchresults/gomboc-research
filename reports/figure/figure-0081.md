# figure-0081

AI research report · 2026-08-26 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Complete research handoff — deleting X's obstruction edge

## Verdict

**No homogeneous convex polyhedral Gömböc was obtained; no `(S,U,H)=(1,1,0)` claim is made.** The branch does, however, leave X's semialgebraically closed edge cell and supplies the requested strongest exact post-edge-deletion body with a proof-level obstruction.

Starting from the exact B continuation, the 12-vertex double bridge D deletes source edge `(1,8)`. A connected asymmetric two-point successor patch gives the exact 14-vertex endpoint E and also deletes source edge `(0,9)`. Exhaustive rebuilding of every E input-vertex subhull with at least eight retained vertices selected deletion of source vertex `6`. Exactifying that subhull gives endpoint **F** below. F has both forbidden source edges absent, exact uniform-volume centroid, exact zero centered first moments, complete independently rebuilt incidence, positive inactive separation, a nonzero exact sign box, and strict class `(2,2,2)`.

## Label map and explicit edge deletion

F labels `0,…,12` correspond to E source labels

```text
new:    0  1  2  3  4  5  6  7  8  9 10 11 12
source: 0  1  2  3  4  5  7  8  9 10 11 12 13
```

Hence source edge `(1,8)` would be new edge `(1,7)`, and source edge `(0,9)` would be new edge `(0,8)`. Neither is present in the exact true-edge list.

## Exact rational V-representation of F

These are uncentered vertices `q_i`; mechanics uses `x_i=q_i-C`.

```text
0  (-20277141908976133959/7812500000000000000,
    -125667065080732073/10000000000000000000,
     17736943665204684451/250000000000000000000)
1  (-41122184924285328767/500000000000000000000,
    -2404406102639473019/500000000000000000000,
    -15970564992678652339/500000000000000000000)
2  ( 288631495896785291333/125000000000000000000,
      8399810662288265539/500000000000000000000,
     -9476949011347238533/500000000000000000000)
3  ( 293438886428594639009/500000000000000000000,
     -1460681088680317047/500000000000000000000,
     -15929344798875656793/500000000000000000000)
4  (-8087345328858996007/50000000000000000000,
    -1272919853612624151/250000000000000000000,
    -1705022732523466619/62500000000000000000)
5  ( 328168949098010062819/125000000000000000000,
      2146219826084730353/250000000000000000000,
     -2000714927544242051/25000000000000000000)
6  (-674514891469926453459148920329/7812500000000000000000000000000,
     136318819055460269635263591779/15625000000000000000000000000000,
     722522671260991636193741172361/15625000000000000000000000000000)
7  (-20135847254542424323449202598201/250000000000000000000000000000000,
      1097097465166593446980178728849/125000000000000000000000000000000,
      5784125525572408717013252011637/125000000000000000000000000000000)
8  (-40554222715350022526900462635719/15625000000000000000000000000000,
     -689284724862560154855753857537/62500000000000000000000000000000,
      4478008109177350832608436195041/62500000000000000000000000000000)
9  (-51787489629654907168697983579943/20000000000000000000000000000000,
     -174871096833213199216975536773/20000000000000000000000000000000,
      1448613291922183099241858916611/20000000000000000000000000000000)
10 (-1264412342001562236566097800551659/500000000000000000000000000000000,
      -4144026336604103052081592195477/500000000000000000000000000000000,
       35993471176727251275727571522363/500000000000000000000000000000000)
11 (-162217469000069/62500000000000,
     -2941975551619/250000000000000,
      4447297451389/62500000000000)
12 (-324433603003711/125000000000000,
     -11827379726411/1000000000000000,
      1116238212141/15625000000000)
```

The machine-readable V-representation and the complete 20-row primitive centered H-representation are candidate.json and halfspaces_centered_integer.csv.

## Exact uniform volume and moment closure

```text
V =
3168596165752729349899197159281391551870108597686969559898527171047662170615913391660451804507/
5859375000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
≈ 0.00054077374562179915

C = (
-518404746094399343480621220416048885673893200455401879663801522051714340564695206791371467791918575740943728371384653138170319/
6337192331505458699798394318562783103740217195373939119797054342095324341231826783320903609014000000000000000000000000000000000,

834311260996699455056949707148356240817932577068964699018710844988155997153106249883070858653013981568791210795190834009429/
6337192331505458699798394318562783103740217195373939119797054342095324341231826783320903609014000000000000000000000000000000000,

37454460026995681297966174539111691377982092768574321499801500215995836899665334916557131099326813296193633019470164343074741/
6337192331505458699798394318562783103740217195373939119797054342095324341231826783320903609014000000000000000000000000000000000
)
≈ (-0.081803536799276461, 0.00013165313870133101, 0.0059102608959475953)
```

The exact centered first-moment numerators are `(0,0,0)`. The primary verifier reconstructs all support planes from the V-data, merges coplanar triples into maximal polygons, obtains 22 positive tetrahedra, and integrates volume and moments exactly. A separately implemented exact pair-separator reconstructor obtains the same faces, edges, volume, centroid, and mechanics without trusting the declarations.

## Rebuilt maximal faces and true edges

`(V,E,F)=(13,31,20)` and `13-31+20=2`.

```text
Maximal faces:
F00 (1,4,0)       F01 (0,11,1)      F02 (3,2,0)
F03 (2,7,0)       F04 (4,3,0)       F05 (12,0,7)
F06 (12,11,0)     F07 (1,2,5)       F08 (6,7,2,1)
F09 (1,3,4)       F10 (5,3,1)       F11 (9,10,6,1)
F12 (11,9,1)      F13 (5,2,3)       F14 (10,7,6)
F15 (10,12,7)     F16 (9,11,8)      F17 (8,12,9)
F18 (12,8,11)     F19 (12,10,9)

True edges:
(0,1) (0,2) (0,3) (0,4) (0,7) (0,11) (0,12)
(1,2) (1,3) (1,4) (1,5) (1,6) (1,9) (1,11)
(2,3) (2,5) (2,7) (3,4) (3,5)
(6,7) (6,10) (7,10) (7,12)
(8,9) (8,11) (8,12)
(9,10) (9,11) (9,12) (10,12) (11,12)
```

## Exhaustive own-centroid feature margins

Margins below are the primary verifier’s directed normalized limiting primitives. Positive means equilibrium; every negative entry is an explicit strict witness. The linked primitive tables contain every constituent exact rational, not only each feature’s limiter.

```text
FACES
F00 -7.211887726211320687903337E-3
F01 -2.746024860157518584729528E-3
F02 +3.228144819598872646541007E-3  STABLE
F03 -3.609687760801483799999238E-3
F04 -3.088870668774159875927866E-3
F05 -5.656638990710795366030211E-3
F06 -6.292855312137461894116194E-3
F07 -7.300384028030856397731879E-3
F08 +4.580734797214169450150096E-4  STABLE
F09 -6.435632864632718500084978E-3
F10 -7.084664263128607042422296E-3
F11 -4.578606799432766776654831E-4
F12 -4.116937132631105750090020E-3
F13 -8.427245064403298882878711E-3
F14 -7.874716438751470758635234E-3
F15 -4.438668710467019099989412E-3
F16 -2.276734697383669814643878E-1
F17 -2.261080000741965259129880E-1
F18 -5.144845569443144934142281E-3
F19 -2.731579219652538948548479E-2

VERTICES
V0  -8.125346987188517070827248E-3
V1  -5.420859926560901021910511E-3
V2  -9.832606517067506517065875E-1
V3  -9.994102140386580346767769E-1
V4  -9.058828676024916263037708E-1
V5  +9.869793772193933274957866E-1  UNSTABLE
V6  -1.180969687636918818772148E-1
V7  -4.536654137353824958867220E-3
V8  +3.576544494423316022897041E-4  UNSTABLE
V9  -9.274180938549119977372482E-1
V10 -9.997982576892792874379667E-1
V11 -4.594990573725858190231149E-6
V12 -1.049501172030350544601849E-2

TRUE EDGES
(0,1)   +4.343699511670710942036645E-4  SADDLE
(0,2)   -1.285356199047216015261560E+1
(0,3)   -4.492405849824931779096109E+0
(0,4)   -4.564955254905872316902384E+1
(0,7)   -1.112605292035262887145601E+0
(0,11)  -2.474431254131004565853767E+1
(0,12)  -1.161162266743547758901106E+1
(1,2)   -3.651116813285223723979324E+2
(1,3)   -9.181845703111390300264521E+0
(1,4)   -7.000373487178034708891666E+1
(1,5)   -7.641692074459764663712696E-5
(1,6)   -1.200322780702599242911574E+3
(1,9)   -7.029849944223106502412089E-1
(1,11)  -1.775201700335793271447080E+0
(2,3)   -4.150353215349809442439228E+1
(2,5)   -7.295705581328539938395152E+0
(2,7)   -7.837365308745845124639429E-5
(3,4)   -1.313797264753447720170557E+2
(3,5)   -3.061975859358921459714286E+0
(6,7)   -2.328240871033983927833128E+1
(6,10)  -2.326236413441888348972997E+1
(7,10)  +3.661094994844753982269739E-4  SADDLE
(7,12)  -2.808758803786543784196092E+0
(8,9)   -3.548054632347341725457687E+2
(8,11)  -1.301477742810494021176214E-2
(8,12)  -1.133651755664008586895969E+1
(9,10)  -4.041795164543382978596803E+1
(9,11)  -3.174567105232037357194009E+2
(9,12)  -3.200119393310236555923440E+2
(10,12) -3.661055475062206000152424E+1
(11,12) -9.135433841673774578416245E+1
```

Therefore

```text
(S,U,H)=(2,2,2),  S+U-H=2.
stable: F02=(3,2,0), F08=(6,7,2,1)
unstable: V5, V8
saddles: (0,1), (7,10)
```

Full exact data: face primitives (`face_primitives.csv`), vertex primitives (`vertex_primitives.csv`), edge primitives (`edge_primitives.csv`), and complete limiting table (`complete_margin_summary.csv`).

## Inactive separation and exact open cell

The minimum strict nonincident raw support is

```text
3639735487298899993958255147573835836341518040712851743/
15625000000000000000000000000000,
```

with unit-normal/diameter-normalized directed value

```text
[7.487687842709326042854244E-7,
 7.487687842709326042854244E-7].
```

Closed exact Fraction intervals certify the five-parameter shape box

```text
A(t)=I+t0 diag(1,0,-1)+t1 diag(0,1,-1)
       +t2(E01+E10)+t3(E02+E20)+t4(E12+E21),
|tk|<=10^-12 independently.
```

Throughout the box, `det A>0`; the maximal faces and true edges are unchanged; the exact centroid is `A(t)C`; the centered first moments stay exactly zero; every individual face, vertex, and full edge-normal-cone primitive keeps its sign; and the class remains `(2,2,2)`. This is a nonzero exact five-dimensional combinatorial/mechanical cell.

## Proof-level obstruction for this realized cell

Let `K={8,11,12}`. Its three internal edges `(8,11),(8,12),(11,12)` are true, and every support from a K vertex to a true neighbor outside K is strictly positive. The smallest exact external support is

```text
7874105421088842165524369664914862974324970566717361581707101543202939760179083549787496689377191708501378207666078597853879666281688733903869/
792149041438182337474799289820347887967527149421742389974631792761915542653978347915112951126750000000000000000000000000000000000000000000000000000
≈ 9.940181719835258e-6.
```

Choose `v* in K` with maximum radius. For each internal neighbor `u in K`,

```text
-x_v*·(x_u-x_v*)
 = ||x_v*||^2-x_v*·x_u
 >= ||x_v*||^2-||x_v*|| ||x_u||
 >= 0.
```

Equality would require equal radii and equal direction, hence the same point, so the inequality is strict. All external supports are strict by the certificate. Thus some K vertex is necessarily unstable. Target V5 is independently unstable, so **every realization preserving this incidence and these external-support signs has `U>=2`**. The exact support certificate is cluster_obstruction_certificate.json.

This generalizes X's two-endpoint identity: after deleting both offending edges, the transferred maximum becomes trapped in an externally positive three-vertex cap component.

## Closed families and search evidence

Exactly closed:

1. endpoints E and F, with exact V/H reconstruction, moments, complete mechanics and independent verification;
2. F's full five-parameter box `|tk|<=10^-12`, identically `(2,2,2)`;
3. F's entire fixed-incidence external-sign cell, where the cap theorem gives `U>=2`.

Every subset of E's 14 input vertices with at least eight retained vertices was rebuilt numerically: 6,476 valid hulls, distributed as

```text
(2,2,2): 6126; (2,3,3): 297; (2,4,4): 36; (3,2,3): 17.
```

No target occurred. Requiring both source edges `(1,8)` and `(0,9)` absent left 3,570 valid hulls:

```text
(2,2,2): 3439; (2,3,3): 106; (2,4,4): 14; (3,2,3): 11.
```

This is exhaustive only for deletion subsets of E's finite vertex set and is not presented as an exact exclusion of arbitrary coordinate motion. Adjacent bridge cells, metric refinements, bridge ladders through 20 inputs, residual-edge bridges, free/radial continuations, short Y rails, negative-cap rings and moment-curve replacements also yielded no positive chamber; those are empirical search evidence only.

## Smallest nonredundant continuation

Another apex or short bridge that leaves K externally positive is rigorously redundant. A new connected replacement must simultaneously:

1. make an external support nonpositive for every cap vertex that can become the radius maximum, or deactivate enough of K to destroy the positive component;
2. connect the cap to the intended sole maximum through independent outward witnesses rather than create another maximum;
3. retriangulate or deactivate residual stable quad `(6,7,2,1)` and both saddle neighborhoods `(0,1)` and `(7,10)`; and
4. solve the new exact volume moments rather than inherit F's centroid.

At F's fixed centroid, cap maximum V8 and target V5 are `179.671046276368°` apart with radius ratio `1.07714344237`. In a fixed-endpoint monotone radial chain, convexity of `log(sec)` gives `r_target/r_cap >= sec(theta/m)^m`; the first admissible `m` is 67. This is diagnostic, not a global lower bound after moving the centroid. The smallest genuinely different continuation is therefore a **volume-moving bifurcated patch** that shifts the centroid toward the cap, supplies two asymmetric external-witness branches, and deactivates the central quad/saddle vertices during the same circuit crossing.

## Reproducibility and exports

Run `bash RUN_ALL_VERIFIERS.sh` after extracting the archive. The independent exact verifier does not trust the declared faces. The mesh verifier reconstructs the exact hull and confirms that OBJ/STL contain 13 vertices and the same 22-triangle maximal-face fan triangulation.

- Complete portable bundle ZIP (`post_edge_deletion_bridge_research_bundle.zip`)
- Standalone full report (`post_edge_deletion_bridge_research_REPORT.md`)
- Combined verifier transcript (`RUN_ALL_VERIFIERS.txt`)
- Fresh-extraction manifest/verifier transcript (`post_edge_deletion_bridge_research_FRESH_VERIFY.txt`)
- SHA-256 manifest (`SHA256SUMS.txt`)
- ZIP SHA-256 record (`post_edge_deletion_bridge_research_bundle.zip.sha256`)
- F exact verifier (`verify_exact.py`)
- F independent verifier (`verify_independent.py`)
- F metric-box verifier (`verify_metric_box.py`)
- F mesh verifier (`verify_mesh.py`)
- F OBJ (`body.obj`)
- F STL (`body.stl`)
- Parent E candidate (`candidate.json`)
- Deletion enumeration (`subhull_exhaustion_summary.json`)

The final archive contains 110 manifest-tracked files. Fresh extraction verified every hash and all exact, independent, interval-box, mesh and diagnostic checks. ZIP SHA-256:

```text
d37aed67f9fb4d6147df3731b4c651900aeb32ee0e210833eb69fdeec1b8cdd3
```
