# material-803cab20caf7

AI research material

---

# J71 L18 root-pair theorem and exact G3 turnover — Recovery capsule part 1/2

Object identity: J71_L18_ROOTPAIR_G3. BOTH parts are required. Part1 contains the complete exact input, mathematical scope, recovery commands and observed output identities. Part2 contains the complete12447-byte standard-library executable rootpair_exact.py. No source sandbox, external optimizer, omitted helper, archive, SciPy, or earlier material is needed once both parts are supplied. Observed with Python3.13.5. This preserves a theorem and a useful NONRECORD body, not an own110 construction.

## Scientific statement and scope
Let the original L18 actual homogeneous centroid be g0, computed by exact filled-volume integration from the literal points below. Let z replace material vertex62. Retain the named original support faces and indicated local edge stars, keeping their other anchors fixed. It suffices to fix anchors6,49,54,55,58,59,64,65,68,70,73. Changes elsewhere are allowed only while these support/star conditions remain valid. A root is a strict unstable equilibrium. The theorem does NOT assume g0 remains the own centroid; it bounds the actual homogeneous centroid g.

Six necessary support halfspaces give a relaxed convex cell containing every admissible z. They arise from fixed faces(65,73,70),(54,58,59), and variable support faces(62,64,59) against58,(62,65,70) against68,(62,49,65) against58,(62,58,49) against55. Exact nonnegative dual combinations give coordinate bounds. For every62-neighbor except58, exact rational separation from the diameter ball with endpoints g0 and that neighbor implies a strictly negative root score over the WHOLE cell. This is not a sampled ray or a numerical optimizer certificate.

If ||g-g0||_infinity<=1/20 and the original62/58 stars remain, at least one of62 and58 is strictly U. Fixed point6 has larger squared radius than either throughout this cube and cell, so a global radial maximizer is a different strict U. Hence U>=2 in this entire retained-anchor/fan family. The minimum certified centre-drift threshold is approximately.05214859316859358, strictly greater than1/20.

With the original59/64 stars retained too and ||g-g0||_infinity<=1/1000, losing strict U at62 forces58,59,64 all to be strict U. Each possible non-U condition at59 or64 adds a linear halfspace. Exact ball separation, including the centre-dependent relaxation of that halfspace, excludes it simultaneously with loss of U62. Point6 ensures a fourth strict U. Thus loss of the old label62 is not cancellation of its basin. These are conditional geometric exclusions, NOT global impossibility of changed-support L18 descendants or of own110 belowC500.

For scores q(v,w;g)=(v-g).(w-v), strict U means all adjacent scores are negative. The identities q(v,w;g)+q(w,v;g)=-|v-w|^2 and q(z,w;g)=|w-g|^2/4-|z-(w+g)/2|^2 drive the proof. All terminal inequalities are rational assertions.

## Executed exact body and its evidence
L18_ROOT_TURNOVER_G3 changes ONLY vertex62 to(.491,-.349,-.698). It retains all original maximal facets, V75/E204/F131,C408. At its actual new filled-volume centroid the exact census is(S,U,H)=(3,4,5), additionalweak000, primitivezero000; U labels6,58,59,64. It is a useful simple-arithmetic nonrecord, NOT110.
Three positive primal bar depths are.092590923915317,.004107098034639459,.001019146954040274. Two positive polar depths are.06740628542377615,.0006750653393351598. The output reconstructs complete exact fractions, components, cuts, attaining edges and paths. Small extra bars are never floored away. Parent L18 remains exact222/weak000 with stable triangle14,16,24 and the18-gon, U6/62,H13--22 and6--63.

## Recovery, verification and exact identities
Extract the two source units from parts1/2 verbatim, including one terminal newline, into l18_exact_points.json and rootpair_exact.py. Run:

    python -B -S rootpair_exact.py --input l18_exact_points.json --out rootpair_exact.json

The command reconstructs and verifies. Expected terminal markers:

    L18_EXACT_ENUMERATED_HULL_PASS 75 204 131
    L18_ROOTPAIR_CUBE_EXACT_PASS 1/20
    L18_ROOT62_LOSS_FOUR_U_CUBE_EXACT_PASS 1/1000
    L18_ROOT_TURNOVER_G3_EXACT_PASS [3, 4, 5] [0.092590923915317, 0.004107098034639459, 0.001019146954040274] [0.06740628542377615, 0.0006750653393351598]

Observed UTF-8/LF identities:
- l18_exact_points.json:2357 bytes,SHA256 90d0a3e009fe9a0ff5bef092a8ad6ac9071fa7d1242bb3cdc82b43531aa1f0f6.
- rootpair_exact.py:12447 bytes,SHA256 6db7a6739614e3a9318f9e12700874e1f05415fd718008edfe06c8aca3f44887.
- rootpair_exact.json:11428 bytes,SHA256 eb7e18e93f0cf1eadb57c003ed7a629d2a5bd62122db90e5e8ba6a6bd8e4d1ef.
An actual second execution wrote rootpair_replay.json with the same11428 bytes/hash. This is replay of the coordinator's own program, not an independent physical engine. Hashes identify bytes; the complete generator and input in this two-part capsule provide reconstruction.

## Complete l18_exact_points.json
```json
{"denominator":100000000,"points":[[-114525000,-38526902,2815000],[-114408000,-28813483,-21012000],[-110220000,-22670374,-38817000],[-102074000,-18012432,-55623000],[-95244000,-69231584,65065000],[-93745000,-15470943,-67376000],[-84871000,-82040002,89483000],[-83812000,-14029958,-77505000],[-76508000,-13554466,-83525000],[-64581000,-13912297,-90582000],[-61476000,25894000,-14839000],[-62395000,23368000,463000],[-56261000,23741000,8340000],[-52412000,-15218983,-95480000],[-51315000,23453000,14016000],[-52494000,34497000,-19706000],[-42771000,21590000,23057000],[-42863000,2890000,42398000],[-41427000,18386000,27657000],[-41360000,12530000,33866000],[-41047000,44227000,-22695000],[-39278000,42001000,-8155000],[-34778000,-18120125,-100114000],[-33227000,5517000,41437000],[-34030000,41543000,3065000],[-32655000,47126000,-31146000],[-27505000,-19593266,-101349000],[-26092000,6359000,40643000],[-29349000,-3094000,46727000],[-23601000,48813000,-36091000],[-20202000,-21347779,-101916000],[-22835000,44187000,7116000],[-19759000,39126000,14237000],[-15413000,37019000,17653000],[-12669000,-23440927,-101808000],[-11758000,47157000,-43142000],[-9937000,36825000,18784000],[-5171000,-25823125,-100970000],[-4354000,45931000,-43781000],[-656000,39016000,17643000],[-285000,7861000,35467000],[2454000,-27623000,-99473000],[1609000,5616000,35659000],[7524000,7250000,33248000],[9975000,-29293000,-97278000],[8760000,16281000,29866000],[12615000,42039000,15586000],[23787000,44736000,-31885000],[17334000,-30836000,-94391000],[30460000,-17220000,-87918000],[24468000,-32254000,-90824000],[38470000,40587000,-9618000],[31322000,-33549000,-86591000],[29555000,47228000,10455000],[33038000,-44403744,-80951000],[37731000,-34969000,-81714000],[36888000,40349000,12838000],[41804000,34722000,13816000],[43728000,-36211000,-76251000],[41605000,-51828881,-68494000],[44676000,31334000,13390000],[47360000,27874000,12796000],[49134000,-37619000,-70267000],[49897000,24291000,12029000],[52973000,-47543000,-55156000],[53765000,-8364000,-59155000],[55076000,17110000,8707000],[59503000,9479000,4527000],[58901000,-42244000,-45006000],[63005000,1560000,-490000],[63029000,-35973000,-35698000],[65329000,-6139000,-5970000],[66608000,-13854000,-12187000],[65610000,-28928000,-27007000],[66746000,-21494000,-19185000]],"cap":[0,1,2,3,5,7,8,9,13,22,26,30,34,37,54,59,6,4]}
```
