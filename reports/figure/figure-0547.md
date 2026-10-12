# figure-0547

AI research report · 2026-09-25 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Rapid Atlas 40 — finite bulk surgery, a complete saddle-apex ray, and an exact solver obstruction

## Result and source authority

**No own-centred strict110 body was found. No new own121 record is claimed.** The constructive output is four exactly audited non-target bodies, an entire sub-500-complexity apex family proved to retain at least two strict unstable equilibria, a proved interval of constant geometry after macroscopic basin contraction, and an exact diagnosis of an incompatible pair of target witnesses.

The authority is literal parent `figure-0539`, SHA-256 `12c1f6d2f1e438a75699643bf65aadcb0cd412504b2a5f109af66dd641802c33`. The supplied journal was read through EOF; its 300372 bytes have SHA-256 `1d748c0a5fedbc41ba9f5fa03e6b7588a0679360eb0299ecfebedacc8ed87de8`. Its 37-unit source capsule was restored and its manifest verified. No required source for the work below was missing.

The reconstructed WIDE parent has **V/E/F = 146/219/75**, strict **S/U/H = 1/2/1**, additional closed weak counts **0/0/0**, one positive P bar of relative depth **0.21772143250484546**, and no positive Q bar. Its exact input is the 78-row, denominator-1000000000 file of 2674 bytes, SHA-256 `9f6147c741742045d435f4c42e6112302d476ad7c0c0b8ea244e17f37d847940`. The three inactive input rows remain input redundancy, not extra facets. A fresh parent replay reproduced its 52076449-byte audit, SHA-256 `93dc044b552f096b51dd41e4c419606272419645b309f4e69c32f9b49a2f6ea1`.

`RA41` below is only the local artifact prefix for this continuation, not a new research branch. All exact constructions use this WIDE parent. The new apex family is not a claim that the initial mixed-contact four-reservoir rank survives.

## 1. Exact constructive endpoints

Counts are true maximal-hull V/E/F, not triangulation counts. Complexity is C = 2E. All four rows have additional closed weak counts **0/0/0** and reported primitive-zero counters **0/0/0**. Decimal statistics are renderings of exact rational calculations, not the definitions of the bodies.

| Body | V/E/F | C | Strict S/U/H | Positive P/Q bars | Largest P / largest Q |
|---|---:|---:|---:|---:|---:|
| AMPUTATE59 | 87/154/69 | 308 | 10/7/15 | 6/9 | 0.5208931411089835 / 0.3144519752816125 |
| RAY_3 | 114/201/89 | 402 | 4/5/7 | 4/3 | 0.5781615868319139 / 0.6621414889374773 |
| RAY_100 | 100/189/91 | 378 | 3/2/3 | 1/2 | 0.9980217907714137 / 0.7192081932335724 |
| PROJECTIVE_037_114_m044 | 146/219/75 | 438 | 40/39/77 | 38/39 | 0.05769630565829992 / 0.008837496465723845 |

### A. Macroscopic removal of the current 59-vertex P component

Let P be the exact canonically sorted raw vertices of WIDE, and let J be

```text
[46,48,49,50,52,54,55,57,60,61,64,66,69,73,75,76,77,78,79,82,88,89,93,94,96,99,102,103,104,106,110,111,112,113,115,117,118,119,120,121,122,123,124,125,127,128,130,132,133,135,137,138,139,140,141,142,143,144,145]
```

Define **AMPUTATE59 = conv{P_i : i not in J}**. This deletes the entire current junior component, not an arbitrary historical patch. It removes 0.4879087900388383 units of volume, approximately **25.5403303095%** of the parent's volume. Its E=154 leaves **95 edges** of room under E≤249, although its equilibrium class is substantially worse.

There is also an exact interval statement. Let c0 be the parent's actual homogeneous centroid and

```text
K_lambda = conv({P_i : i not in J} union {c0 + lambda*(P_j-c0) : j in J}).
```

For every **0 ≤ lambda ≤ lambda_star**, K_lambda is exactly AMPUTATE59, where

```text
lambda_star = min (h_f - n_f.c0) / (n_f.(P_j-c0)),
```

with the minimum over maximal facets of AMPUTATE59 and j in J for which the denominator is positive. The exact minimum is approximately **0.4952125499507164**, attained by parent vertex **117** and new canonical facet **67**. The capsule reconstructs the exact rational minimum and checks every containment inequality at it. In particular the whole simple interval **[0,49/100]** is certified. Affinity in lambda proves containment throughout the interval; this is not an interpolation from sampled equilibrium counts. The body, actual volume and moment, every bar, and the strict/closed-weak census are constant there, including the endpoint where an otherwise redundant material point first reaches a facet.

This is physical basin removal but **not equilibrium cancellation to 110**: the changed interface and homogeneous centroid create six positive P bars and nine Q bars. The old junior vertex118 lies outside the new body. The old elder7 remains unstable; the other unstable material vertices are parent labels **26,45,59,71,116,136**. The connecting interval from lambda=1 down to this plateau has not been certified as class-preserving or E≤249-preserving. Numerical near-parent contractions opened many interface facets; they must not be mistaken for an admissible continuous path.

### B. Two simple-arithmetic apex endpoints

In the raw construction frame, put **d=(-2/5,-19/20,1/3)** and K(t)=conv(K_WIDE,t*d). Then RAY_3 has apex **(-6/5,-57/20,1)**, and RAY_100 has apex **(-40,-95,100/3)**.

At t=3, the unstable material labels are **parent7, parent128, parent130, parent132, and the new apex**. The former elder7 has become the largest finite-bar junior, with the new apex as elder. At t=100 only **parent132 and the apex** are unstable. Both original unstable vertices7 and118 still survive as hull vertices at t=100, but neither is then unstable. Thus the surviving basin has genuinely migrated; eliminating an ancestral root's instability is not the same as eliminating the last P bar.

For both bodies, the complete actual volume and first moment agree exactly with the independent sum of the original body and its visible-facet pyramids. These are uniform solid convex hulls, not point-mass constructions.

### C. A finite, same-grid projective bulk deformation

Define **T_b(x)=x/(1+b.x)** with **b=(37,114,-44)/1000** and take PROJECTIVE_037_114_m044 = T_b(K_WIDE). Equivalently, add the integer vector **[37000000,114000000,-44000000]** to **every** original H-input row, leaving denominator1000000000 unchanged. Positivity of 1+b.x over the original vertices is checked exactly. The true incidence and E=219 are preserved.

This reduces the largest P depth from 0.2177214325 to **0.0576963057** by a finite three-parameter bulk change, but fragments the landscape into **38 P and 39 Q bars**. It is not an own121 improvement. The dominant P root is now the image of parent vertex120, not parent118; the latter has a smaller positive bar. The dominant P component/cut sizes change from **59/33** to **33/25**. The new body's homogeneous centroid is recomputed from its volume; it is not obtained by projectively moving the old centroid or transporting the old density.

This simple-arithmetic construction is retained because it isolates an incidence-preserving fragmentation mechanism without using any of WIDE's edge room. Its smallest positive Q bar is still **2.069037364473705e-8**, not zero or weak.

### Actual mass data

Density is one and the moment is about the raw construction origin.

**AMPUTATE59**: V=1.4224376468541444; M=[-0.201886298294052, -0.02998280363880708, 0.26318614327521744]; c=[-0.1419298053173316, -0.021078466043918963, 0.1850247312121403].

**RAY_3**: V=3.2881359068446252; M=[-0.7776961572386354, -1.4931408237617936, 0.641020497620622]; c=[-0.2365158190754139, -0.45409948556373625, 0.19494951418713125].

**RAY_100**: V=82.577765741245628; M=[-822.1074913033004, -1937.1843244801726, 683.7437751901659]; c=[-9.955555032565835, -23.45890939396772, 8.279998484490992].

**PROJECTIVE_037_114_m044**: V=2.0304761332294317; M=[-0.107360403830433, -0.2689875992569065, 0.15672596750991571]; c=[-0.05287449681059704, -0.13247513470108466, 0.07718680606240183].

## 2. A proved obstruction for the entire saddle-directed apex ray, with a true complexity bound

**Theorem for the explicit family above:** for every finite t≥0, K(t) has **at least two distinct strict unstable equilibria at its actual homogeneous centroid**, while its true maximal hull has **E≤234**, hence **C≤468<500**.

Thus there is no110 endpoint anywhere on this whole ray, and the failure is not an exhausted edge budget. This theorem is restricted to the fixed WIDE core and the stated raw-origin direction d. It does not exclude an off-ray apex, a moving core, several exterior points, or a joint junction/bulk surgery.

For a core facet n.x=h with area A and area centroid f, let beta=A/(3*||n||). Once visible from a=t*d, its pyramid contributes

```text
Delta V = beta*(t*n.d-h),
Delta M = Delta V*(3*f+t*d)/4.
```

The ratios used for beta and f are rational and are evaluated by oriented triangle sums. The ray crosses exactly **33 distinct positive facet-plane events**, giving **34 visibility cells**. On every cell, V(t) is affine and M(t) is quadratic. With s=t/(1+t), set v(s)=(1-s)V(t) and m(s)=(1-s)^2 M(t). The centered vector at an old vertex p has positive-denominator numerator

```text
w_p(s) = (1-s)*v(s)*p - m(s).
```

Its dot products with old edge rays are degree≤2 polynomials; the additional dot product toward the apex is degree≤3 after clearing the positive factor1-s. The apex's own tests against every original vertex are likewise degree≤3. Strict negativity is proved by exact rational Bernstein coefficients on each **closed** cell interval. All34 cells passed without bisection. The old-vertex tests use the original true tangent-cone generators plus the new apex, so they remain sufficient even after the true hull changes.

Here is a compact description of the certified witness cover, using **parent material labels**, not the new hull's canonical indices. Let

```text
A=60000000000/36470860829,
B=60000000000/15074588573,
C=1000000000/157347127,
D=30000000000/4485886879.
```

| Parameter range | Two certified strict unstable points |
|---|---|
| [0,A] | parent7 and parent118 |
| [A,B] | parent7 and apex |
| [B,C] | apex and parent128 |
| [C,D] | apex and parent9 |
| [D,infinity) | apex and parent132 |

These are sufficient witness-cover boundaries, **not asserted equilibrium bifurcation times**. At shared boundaries more than two of these witnesses can coexist.

The complexity proof is separate. Away from old facet-plane contacts, the maximal facets of conv(K,a) are the nonvisible old facets and triangles over the horizon edges. Hence incidence is constant within each visibility cell. Each finite contact is then rebuilt with exact coplanar-face merging and planar removal of redundant/collinear points. The certificate checks **34 open cells and 34 finite boundary bodies**, with maximum E=234. Proposed facet polygons are verified against every input point, and the resulting closed facet surface is checked as the complete maximal hull. No triangulation diagonals enter E. This is an analytic visibility-cell atlas plus exact contact checks, not a path theorem inferred from a sparse scan.

This theorem does not supply the complete S/H/closed-weak census at every ray parameter. The two certified strict unstable points are sufficient to exclude110, including at contacts.

## 3. Exact obstruction in the usual best-chord target retraction

At the own-centred WIDE parent, the all-pairs best outgoing chord of the junior vertex118 goes to121, while the best outgoing chord of121 goes back to118. The exact unnormalized values render as

```text
(P118-c0).(P121-P118) = -0.009449778488770499,
(P121-c0).(P118-P121) =  1.209609550203376e-7.
```

For any positions x,y and any common centre c, their sum is identically **-||x-y||^2**. Therefore an update that simultaneously freezes the target arrows118→121 and121→118 and demands both be positive is impossible while both labelled vertices remain distinct. Normalizing the inequalities by positive squared radii does not repair this sign contradiction. This is an actual incompatibility of that witness selection, not merely a badly conditioned numerical solve.

I replaced these choices with minimum-cost **acyclic rooted trees** on both current P and Q landscapes, rooting each at its current farthest point. The included implementation differentiates the actual homogeneous mass and allows all current H normals to move. Its three finite repair runs did not find a target. The tree method removes this particular logical incompatibility; it does not prove global feasibility or solve the macroscopic barrier. Dynamic changes of witness choices or actual vertex deletion are outside the frozen two-cycle obstruction.

## 4. Complete positive-bar ledger and current interfaces

The following lists contain **every positive relative depth**, in decreasing order, for the four exact endpoints: **49 P bars and 53 Q bars in total**. These are decimal renderings only. The recovery code enumerates their exact rational births, deaths and relative depths, every complete cut/component, and an attaining path; it has no small-bar suppression threshold.

**AMPUTATE59**

```text
P = [0.52089314110898355, 0.34028522738143469, 0.15222974464122235, 0.0067346497905569781, 0.00085707321221523938, 0.00032538277550397173]
Q = [0.31445197528161251, 0.25333513713796019, 0.085368115951236057, 0.025444880637333311, 0.017661303191486698, 0.0027052781860845069, 0.0013044219063668989, 0.00092682631767740495, 5.0538447152766504e-05]
```

**RAY_3**

```text
P = [0.57816158683191388, 0.48110417376123082, 0.0010900748494137771, 0.00040012609062584255]
Q = [0.66214148893747726, 0.0011986350785498773, 0.00026910855731033032]
```

**RAY_100**

```text
P = [0.99802179077141373]
Q = [0.71920819323357243, 0.0044239555625117883]
```

**PROJECTIVE_037_114_m044**

```text
P = [0.057696305658299918, 0.012070500647735486, 0.0042300420250003263, 0.0041784074778683095, 0.0039550746725668228, 0.0031180735950136615, 0.0028913912609371036, 0.0028279716484872932, 0.002298299916571048, 0.002069005608382155, 0.0020194109242003583, 0.0019500807343011406, 0.001817869896770175, 0.0015313924597916966, 0.0013643849388814602, 0.0011038279077205707, 0.00091175966141533119, 0.00077405280636336454, 0.00065883581922769174, 0.00064128372995732818, 0.00063137574928686226, 0.00048601057935968419, 0.00046208059469847544, 0.00030052569883091225, 0.00026378972776144584, 0.00012987636254056635, 0.00012170721410236783, 0.0001111238040864309, 0.00010686248193431629, 9.6274559984893437e-05, 6.8713028432055461e-05, 6.4363871677422063e-05, 2.2085517835971517e-05, 1.785426724691095e-05, 1.3276873863111296e-05, 1.0645347788938633e-05, 4.6161159225010679e-06, 5.0313968947606394e-07]
Q = [0.0088374964657238451, 0.0017137231181208342, 0.0016966864490923516, 0.001524235568830586, 0.0014860992098802131, 0.0013494911517338297, 0.0013304200797053327, 0.0013270474706750122, 0.0013250138911864184, 0.0012354203127201229, 0.0012288872831364701, 0.0011796752044203301, 0.0011782740084554199, 0.0010835922318091511, 0.001083437633817028, 0.00097168422573086347, 0.00083173638764952556, 0.0007372888959937241, 0.00062062786438966358, 0.0005196729855044235, 0.00044281807738471326, 0.00037177299891333007, 0.00032427058847951272, 0.00029545338335637506, 0.00020829999337009561, 0.0001758754149967327, 0.0001595435825835622, 0.00011061772527559459, 7.8894098869638924e-05, 5.9623871193513897e-05, 3.2957393621043376e-05, 3.0192523944326671e-05, 2.17665730562121e-05, 9.5171300010133422e-06, 1.6077258308871924e-06, 1.046777079124433e-06, 1.6460169408792494e-07, 1.6383969204476178e-07, 2.069037364473705e-08]
```

For the largest P bar in each endpoint, the following are **new canonical labels**. All other positive bars receive the same full interface/path checks in the exact report.

**AMPUTATE59**: peak58 → elder7, component/cut=12/25; attaining path `[58,46,45,41,38,35,34,33,31,29,26,4,7]`.

**RAY_3**: peak6 → elder11, component/cut=32/46; attaining path `[6,5,4,3,2,1,0,11]`.

**RAY_100**: peak86 → elder0, component/cut=99/49; attaining path `[86,84,75,72,61,60,6,7,0]`.

**PROJECTIVE_037_114_m044**: peak121 → elder7, component/cut=33/25; attaining path `[121,116,110,90,82,73,69,64,60,57,52,50,49,48,46,41,39,37,36,35,32,31,28,23,18,1,7]`.

The exact reports also preserve every stable face, unstable vertex and saddle edge, their closed tests, maximal planes and face polygons, edge owners, root-material correspondence, and actual volume/moment. In particular, the projective report carries an exact146-entry parent-to-new vertex correspondence; historical indices are not silently reused.

## 5. Finite unsuccessful searches and the remaining physical obstruction

The source capsule retains the complete producing units, all nondefaults, seeds and the exact binary64 input text used by the numerical repair experiments. These discovery computations are not closed-weak certificates or global exclusions.

| Mechanism tested | Recorded finite search |
|---|---|
| One free apex over WIDE | Three differential-evolution runs, seeds4125–4127; state-call counter3865. No improved certified own121 or110 endpoint. |
| Macroscopic saddle-apex jump plus all core normals free | Initial scales1.15,1.3,1.5; target margin2e-7. Joint retraction failed to reach target; no inherited contact rank was assumed. |
| New support cut plus projective bulk motion | 128 spherical directions, 11 cut levels, three six-variable local searches; counter3190. Large-bar reduction was accompanied by many new P/Q bars. |
| Whole P-component homothety plus translation | Two four-variable searches, seeds7410–7411, 12880 differential-evolution evaluations. The exact amputation endpoint above is retained independently of their nonwinning floating endpoints. |
| Acyclic P/Q rooted-tree repair | WIDE and two pinned cut/projective starts; all three runs stopped after30 iterations without a target. |
| Greedy support deletion | 12 runs of60 steps each. No certified target; pruning did not supply a better own121 successor. |
| AMPUTATE59 plus a free replacement apex | Seeds7420–7422; state-call counter18964. No target. This tested a joint finite bulk-removal/interface-replacement route rather than merely pushing the original apex. |
| WIDE projective plus affine-metric deformation | Three projective parameters plus five determinant-one metric parameters; seeds8410–8412; score-call counter51666, plus additional analytic-gradient calls. No target; the balanced objective still had many P/Q bars. This was not the separate W51 metric search. |

The main physical distinction is now explicit. **The old basin can be removed as material, and the original unstable labels can lose their instability, without removing the final positive bar.** Uniform mass redistribution and replacement interface geometry create different basins. A single growing apex on the certified saddle ray stays within the complexity budget but merely transfers the surviving instability to different core vertices. The finite projective change uses no edge room but trades one macroscopic basin for a large number of smaller strict basins.

The most useful continuation is a finite junction/vertex-deletion or interface-replacement construction coupled to bulk mass control, with an explicitly acyclic escape structure selected on the **current** P and Q complexes. The exact AMPUTATE59 endpoint offers substantially more edge room, but is not a near110 seed; the projective endpoint offers a simple-grid flattened landscape, but has77 positive bars. Neither should displace WIDE as an own121 record. Any next construction must audit the newly selected roots, full current cuts and all small positive bars rather than preserve ancestral labels or drive the incompatible118↔121 target pair.

## 6. Durable recovery capsule and receipts

The inline program below contains the complete losslessly encoded **28-file** source/input capsule, including all exact inputs and every required helper. It does not fetch a Library item, use this sandbox, require C622 data, or depend on the journal remaining available. The archive includes the numerical producing units as well as the exact generator/verifier.

Exact replay environment: **Python3.13.5, NumPy2.3.5, SciPy1.17.0**. Numerical searches additionally used **Torch2.10.0+cpu**, CPU float64 and one thread. NumPy/SciPy propose hull facets for the amputation/projective constructors; the exact verifier checks support, complete hull equality, maximal faces/true edges, the actual mass and both strict/closed-weak censuses. The ray sign and complexity certificates and all final acceptance tests use rational arithmetic.

Save the program as `RECOVER_RA41_INLINE.py`, then run:

```sh
python RECOVER_RA41_INLINE.py
cd RA41_RECOVERED
python REPLAY_RA41.py
```

The source-ready marker is `RA41_SOURCE_CAPSULE_READY 28 96574 b19d77888bde0f3fa1930e627f32f8e2413f73221108de74925621237f062cc4`. The decoded JSON is96574 bytes with that SHA-256. The decoder itself is41121 bytes, SHA-256 `f664fb587196d8f0b77972a4db00742636a9ba6c3d402cbe64b16585bc1a619c`.

Expected scientific terminal markers include:

```text
WHOLE_SADDLE_APEX_RAY_TWO_STRICT_UNSTABLE_EXACT_PASS 34 34 0
WHOLE_SADDLE_APEX_RAY_TRUE_E_MAX234_EXACT_PASS 34 34
RA41_EXACT_ENDPOINT_ALL_HULL_MASS_WEAK_BARS_INTERFACES_PASS
AMPUTATION_WHOLE_INTERVAL_AND_WITNESS_CYCLE_EXACT_PASS
RA41_FOUR_EXACT_ENDPOINTS_WHOLE_RAY_PLATEAU_CYCLE_ALL_RECEIPTS_PASS
```

The four endpoint cold replays reproduced their exact audit bytes. The Bernstein ray certificate, the full ray-complexity atlas, and the material/cycle certificate were also reconstructed from the exact parent input. The source manifest and final receipt checks detect changes rather than silently accepting an approximately similar body.

| Exact output | Bytes | SHA-256 |
|---|---:|---|
| `MATERIAL_CERTIFICATES.json` | 112436 | `20310603f8c31f2b93dd172e810bdab5312f1f1d26a8e62d46ca88c04ede75f3` |
| `WHOLE_RAY_CERT.json` | 7525 | `e11dfc8d3ec0454ed93fe716274aeb558e7691fc2e1f10523fcf569cf5a19c91` |
| `WHOLE_RAY_COMPLEX_CERT.json` | 12573 | `f8504559915b278ac29c765f7babe34d4b5ee625dd90836cbc8d2ae5ccfbdd6b` |
| `exact/AMPUTATE59/audit.json` | 23195827 | `7f4bfb478c442356c8f1a5ed93863830c2d27802f015295e8c052ec9548e6f19` |
| `exact/PROJECTIVE_037_114_m044/audit.json` | 59412194 | `d3ff2d1beacd5dcce549bb83ded43b6d8f04809520d0f66d0a8e6062250d5615` |
| `exact/RAY_100/audit.json` | 31575791 | `52ecb51e520bce4840c9ecfec9324093ef161b86c9f4bd294797c942a3e4a8d5` |
| `exact/RAY_3/audit.json` | 38244021 | `94a02b6af215a78270033338d31fefbcf65ec14a32bf6fbc1e7f95925be4ef66` |

For convenience, the same sources and generated exact reports are also packaged in [the continuation archive](sandbox:/mnt/data/RA41/RA41_sources_and_exact_audits.zip). That file is supplementary; the following literal capsule is sufficient on its own.

```python
import base64,hashlib,json,lzma
from pathlib import Path
DATA='''{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;dwoL>s<gnh=heAU-i+k?WUyeGN>3^&w`uu-kvG9I8m~GYUN)xpVmfx>?cyF3B5Uw*z5G$E!pcLfX!}g<GC`vyED6R`#SR;OIRy%?&-PF4n;d7L>^oz0Tm4%+NJ@l<y(1Q
{Uj-MdYd&6df7)C)e%}SF@nB2_wX*gY)O}A2f)vtKL>S<Ck!KbYUt(N29mvmU94W<UhuhU8%pGC)u8|?x&w};-gQf@AJ(~glR=)>E$e{Lf_(10I_M))<&ajBNKP4cW}LXS56Ciepj2O8)`pXss61f2?5!g_(Gt-m
_EEm}mPIgn2>-#UMWAY%v^T&q?g_K?+0Bme3IbUs3gXr>O*cv}dH5-x^x2wD3^fmg5Q>_oIRc_W_OhC8F1p$D982>uI0WgZ#<o!2))El3rhG<uFzJyD3u%o^W0^cq8Ie{Y)riJqc?Dk+L=OkZDwdINwq3#NGD<hO
=7e3<sUP+eaUb!BTsXYFkg~uA!T|Sr)<N%EN?KkYUuokg#JqB2rkfQD!c))S&7)SAJ-6F^CzhjaL#78mywWF*Pj_IGwSOaJh$cvZ8SW(P0XX0u5==IERj+m3a{ZtOaDN`6Stn|wq=~b(%kSzD35re?GYk94s3qb^
?+qsdXsr5lnrkpodp@Gi#`<jMC;>VH1^;wOAV;xgX}R>K2csJ)n0-hmZ;s!`$GGiqX`FtQ3KI-&@xw{xglOg2aR(9O4T98U(YoW%?a!bM?%=w^;C+Y22xbon0KVxA6p;BW&;F5h0PgYBlJ=VYt*{)imqz&MB!$*k
apHO{hw@MF6x4z8zzd7-@!#YUivywVM?;Gco?%Hoor?8pWVTOV*QMO#i`FP{bie`I<PZwCSqzcrH8}0NMkNCD3tg^#Up}DV1@9%73y7k$=#V<}C10-L=P{cq3mAS~9*GdS{cTtF(JQ`74vc=EMNJRbkC}n%nRGNu
;!A=<7OxoMXKSEm#HG~LOdR3uo<-*_y@c}IIPM!rnZzDd8PFf@SH=CNsbRkZnKm+1K5AO3gm%>b2d6ZO2Pc$_ZQVcfvD9)3mZ#(PJuGh0mejQ>YT1dlsK5!P^+4}9ZQHo7`6Gf^T{Cu*u)@^Jp<7VV`Ir8vwzlb<
VhW@~YgG`1{2TU$F<!iQyHHdSJ)k`b*Eu&4d&qCg?U=%(9aqI2ncS)f4owE(UPDG|j$#S}d&N3qGdEAP%fRgE5{#w6PoS>rBIj{P$51MEl$?Zxq4#)!Eowia+(xha>%^VDgvjv38aY2-gJDZsyiqArP{ySBQ8`xG
x?$#_Ua+A<W9DiEXL^_GKDQ@O+H0|D27T42S8>K_-_%+s^n4xhq3T{Zm?|iT3sia+B(&tJ8z+f<2oI)9PijjOr)wgBDdQhU@4(UuBvccmNX5So&o_pRTL5dGpa>ZO*E}rJ@f&-Ns=}aHDFDX(%Kf*&aQiriFeK&s
6kM(?7_6_XogVV^O=mHNaM(d|{Bt__IJnLcSV`pE@tm|w!T@d|;^b-S$a}MJn^E>Go@~~}>;#nSk|*XrE-J)QiFD^dT^<y)Px?vmSR4R0_2`iY&p>}CPZ;Bcw4)#*?<Xhc&mX5MUGD;4*~x5a(54rGW%n|~w*%e%
ie(ql_RsW{jJEbA^Frb%>Gt2P>z}y^UYGEzp%z?O=IW5-_usY+ewrEcZ@*a{Dnzbq0|(wggni;1OWg7SgRvbnHqrk6ss;Q=Lj8u3(Uha=$OTFd$wEG}=q4Mp{4fnc4CV+D)C}UaqkUs6?BE4*F9MJ?9A$A?F_NV)
zsIxxDJfSoUhi72_!bI`%#D5Hsu=RamnzY41CV2G$USY6GwTppgB85c;5`Wa&`BkPf)+hXf3{q2z&{z3ECndTX>kW)M**6$qK9ii=Df^W1GG?G8y?Y<GsN3CSQGp2<L{qZ!IFc@GJ$8MRC9?bmNRhO1VyshglyyL
10X9saXcycN+z8Zq(7QP4v<gMSHSBDZAJ5CA2yblk)Y`%4_s++A-_KsSM_M)VE<IwES)OYKvJD6w9z7<clStoX5^{rq^(|@LTFCFQJeA*wkW4^L$qPr-b&aC&f!(9%g!BjQ>pdUy>5S86?np+VJ2!{L>j?c8tQ@y
_^Qqnr+*-)ZFI|P)Af!s?h%R46HgBuRW2CS<s4nRmP;JM!mNnsEWiKE81Mv_8G%XLwU^$s*mc!It0&;u|Cm|R`$HWWFi!@^t+D!<`)E3fkDgr>mDrx^NkdWmyh4H}DYUcu*5CH-;n**JJKrZWyzoC)G$oxm<(XrA
Bv6eA8SnMRI)-qW6%Pm|*m1#Y*aHNH#CChVUr<Zu9#`QB4QW5JO(#kv=*<aO+1rxg(SPA_Oq(x5trISm&y6yEzJw=Ur{L3}>4^qG9p&k%%X^^Ky}`u>qdp&E^ag@H`ko9p0~{8q%a8Xzm}e&<#qQTq>LyGBree5>
IsFg^EejmGV0DRT+fbAfJUj4!m4xu6NSv}Y+fZkSfN-vL&}4l@I~+$06xHN28qY2u4%a=sz}BRzCX$g76Ki($8qcO3TV@YDr7Wlh+i}c}8{G=^8y;d@iprJUi3(+f;gEO7_;zU=RGCdHSay0cuIbz6YnFshaN)O#
L>E$9uJI@BcI}k11mXI1tEx>Lbk*2jMR)xOJgxO{^g0I+$js~#quUrxq>fMQA!DTY#9qM>oN#5gSq6e|?)q-f)^;$=>6$}p;gxNMk>t;yOPGF@_upoax>^-w*||lSZtmg-KN*4Tl_20lE8dS+U1?^>&HuVObxqBm
AXLE%pt7G|>+I6yu|0(|IjeU@eP5r{WvthJA;v2Usb<OAJgL$Vr}v65qIM;Ii|%K)QEDglf}~ah((gP_v(kK7ajjznQWKfFom7zO|29Y#ItM-$w>J|mq#^&Qawf*a)<%vLPSx?EvxY~q%S^O#ptv|wNp#P@x`N1O
A^ZMCIXS5B_zK2@$9FIN?o|<4ucF3mjJdn?Xg>(`;P)g8k63Q%^br{6DMx)@|9|`On`>m^<I2V;(v!wzK3<O(y#r=0DtAFMxBqWwh&PQQ;z<@>^7~NDogkQKWX$Cznvfk5Jl_<%MQGY2Vu?5U=~k(?iOyfn*a{Y`
JsQ#wg5Qn=_@%{i7S!9sBt`fmMu}LT&8pLa*plIFdJ0)f$3Gr-2Bc7T5boeFdi4)oyUtf$LJ=e<Emn>dbyU7=h+3L**|a~M!AdNj__;Z(6=yfWhSdeNvO3JKIul1TbQC-t4}0X%sLuh;a*QXv*nTe+tliV0u?OtV
FCm`ZPMNfpml{MMKOXdfmK^B%P1Kv%@6r6eCV`T=_B8P35-*anV{0$|WjU4Pd{Sb7RhlgwNQ^z&(=sA-J?>2elPAn;v#*kDUigRbkN6L}b3yDFUGPrsj2vEnz*?l4O{l5a1<7VylsyK{;<4K#QOIvoW5{6G<LgOj
p3v1A!&n0*$zCDc|B;di@afHQ)81}3BQ}BQ@XTwO<<Dq@RG4LGuJ=-I2S?!hj|Gys*`a5$L*@UdPvFj!fGj(bFQ0Y+H4%N7>Fj(?{V<M8xpSL_F@@DAK`41e>lLiJ%-uQKq=U~ocUU;`c<q<eXKEs%Mq~Y$QI(w7
k|Y*{Q42i3%B$CR%vzYV91%dt;(OBp-9$irV;Rlxn;&Dnp3E&>-MJ^)Z^*i`tt^Eie%40);%FNUx*jb%WdM@4Z?hbr6EKId!Ir!tmuy5nL`Re^C)~#S>xYGPBsAoLOmWCJ6QrlbG-}AVi}!Ifg<{XkcuaUd<!D#<
^+#2oX#6|b>Rs&pzvdYxwYX&>zT0lqcRaOOPu<N|E84H)gAbSk&f4O+aEqD`0Z3>9cg(jcbe9#Qm#N?3miYL#e`*%hAEg7Qr_VShA8q;Qej-{JV0O`E0#oz#+-bu|3Y3cXVU>c*TmQmo{QU5k{0l+Fo)l&+5Q_6R
9hfDyb2%LG?G?i;=5VbJ>2;BP3LXe5L`Dkl%`(}d3aRZD&w=T~a0z{jPlrjbFlDy{YVxKW;koSI%pm2e5R@ahPjt{b1@@QD36iG@D%z4C#Fw-V=$poIAIFIs^wUEC*K9-GTmyV_sz#6L1au@?6g8PM2@<|oSSZfu
B-w+kBt5hG{sssZVhT>6_`w4<XYN=<A5ButrWdv1HqszuBzU23g1`M0MVLq<x$LJH*^p6n?`!myTQ|NJ-a|xn_ig=fP&<Wo$t0VAR5sH3&U`vv;W7*uHyj3Q9?0bGTmZfNX8Xd-f<$%>&v^aF`*SwK0f}M=J|cr2
wJ5m-S3atdq$5eH)E;NVJ?b2fFe&4^oE4L%UzBT4EGaD`Y0)IlhJV?hM4|QuSG!<Ja~#sS|811XY3WAEdx|-$Tura6$<_=a?6^U?e625gYbC?LEiI@nn_?X*Dd*5zhDT>pD%9_8B(3Eis)I{H$X_}m!uu#j(14it
8M_TujZ)q0O-z=kI^Bs{jiU>SknLVkClw9960Mn0dOsS~B4^RwgSdEKw*n8Gs6b@x<NfkohJY4?%@|#M!3meiq@hrr0taLRACv>ueI3^!S*IHYDR)f0Ub*<{rN@@z<DY5g3Z^7?bSih;1ETzk$*wc}HYGO%)+Bvr
>!JLpMw({C*4+bFlC0}DE_6()`>6>zjhuG#?2!&qMVtfhSqa^|3Yzru-;_M{MfJzb8x|&&CxH+qfWTV70w>U>=jyRCTgHI;O9G{35WSgi5l?B*pdRj1xZu2Uy<HPHG;_z(vyWQ=sHet$&1SRa3o`3j)|s9Q6${?J
OyQ7iz2%Fz5eP5G7&`z0IX-)qLD25AaRaDEi@L$E36+lyRK;}9^|k_jqj^e-E#g1O{_ycjX@F-~<w3vXhvc9~IQpUSx2Bo^$S_BmmpvV=3Aaj?vkWvXkRYDSzbwF>?$K{AsbJ(exj<X>`tR8qG#DkV9)aW`MrQjR
d!g-DGN=T-nS8sG>&v~2%XkP*j_itr-KI7LS)h5z*ZFaxPs;WV2bE?@w0tW6roeP6zREHDs?v%FO+#0Fl?b`-F@Zc`E{3DXzc*gqviQ-ju?O%Oh)rEi116x0l2hdJkGsS(*TuQ--M5pk)}Po#?3!jGQJ63yOb>^i
J>k7uIDtky^@Hee*baAq5nIuZJ@MEpqTh=Ie87Qu6nvv+H#1!wZ7F42L_6a06CxjL-$q7{iM&BP%vWtU@-(W%5!B`iBXk`&H@WwDZC`1GcZ7X1+@j#~g~b8AkG4wk2MDp*3LJ&aaOs1-x^#o&1e=vYv$%$G5(Xp6
k>lvZKj|NIpR!sD_aN8!z#-^+ZNr$IvwOoka+QZuBk*hPxe#(T(0j<bNMoTmj}8WZHG)4WpVvQsq2X^ROuarTB%k%Np|dw$X2(RnRz9FQWhR1?FRxh>p#<Ni(_BZb73x7E+h-3{Za)JdiR?x~mI9SeJ=8EMV`TOh
6p29D$M{U}L|~2%`}AIi1$}J&I>Ain7Zyk5ERT$}>3eA$w$7Y-;6acbVHd1+K6?=p6?j>`nwG{5Z{LWbyJhGww_XLbzeGx3o=WCxegCrUbYHs(iN={JD9Or#T$&@flCM<`TKGk%jk7oc;2E<d6_MOmjj@g9TD$2|
25;nhrvT#zX$PpNegwQP4*0$N#W~kITQVjkuB?(1JhKZxJ54xDiib?yCh|R9TY`In%Mjcvd`xM*Zx!hz8c4PLW?iT!N5c=@R$<0XA<grsM5pzc-*)>k@u0`QvyH&|gps6px^58s$)KATSCz(1w()~36$@t@Q->jV
YnBevjG~@0nX6;3-D<zg>@LuRE)D-VrxXfgB*<oS7HqGZydCI?hZY@2&FAuB_l%Y%7MPXQWm~ymyRw|M4J86JXwMTOvsr=5%h9h|&zZ80sbI0^2vi9KBvFGWGWA`gSO<i}RXB3eyXAI<2~Tia1#pS->CU>M8N0FL
(!m@$(qr-XyffRO|2(|~nubwV*RhxR^eohZRE9ZsvJeO%%v^#>A}pj5MTS3=w=TSJL=%;DReh=3?8sPW#0K$jsMz(0J5D&;Y^2eB?R_)xf6$4N!fR1ON@pakyo8VqCLfyjf4_Lw$!`BVp|QXP>XQ=8wBHPCSg>)u
vf+2R)kc5%z=iz3P(kfW=HD+=g5A|ELa&!v5G;dF9c}TnNrB%J0><e(gc`@D{irb9%@dDAz&$9(y<WQuwwttvYmi*N<i4?H1x~rQ2iAgm&ClL0YaW#dW$x($(a4qLb}>G~A44AEz<dTLWzBf;$IkkC8M+>QrC4Z6
y+_l|M!fUTXUM149?Yj*igaCpEc?PK8#URX+wRDSNwYF=!9?D2p3`fqh<#K|QJrZ0v%Qxr58*#q=vraQ`y=x+uHGXJH!ESB@j^EV5Yd+S3BE{nJ44w0g5bkdN{O&>aw31N;a2wUM^(DF)KJ&JE3$#FodW|g*YFOH
Ha<Z#MNcU;<Arla@#s}ug&!g*N%h;#q+I5^BP8DY)poma&P955g|g10(?D;Rz1w0C@S18D0TW(l;sHIla0`MUwi)0SD;xeDu7Jg1t?%fY>r$QT<ZOxD7K*6N4CM4No6Oy>d6o5z1m9BDupe!+I!VvmdiNQyQtN#H
hFh`2cwYS?X_ImnZxb1d%E#9?2X%kY07K`7L#cl19y>xrUGQ(<Wwpum0bf(#k(n5>RzP4zvbquLF?Qjtnb}wJt?nBWOKRg7arpy_OeKK}?ojw)3ZPi7zVOKHiNt%##;8k;g&nJKDD0?)bVNvu5SD)NQ7_X%%q4Vl
<q+&Gqg!QH4M(GY(+lRBWf=IyFM|C%r(wVD_qy8`yhEioP;<(QO>vG#*+nV=T5IG5-gKlvQinLU4n$yo53ZXq@}o)*4~%B~<Fznlspuw0o*js!daBJ0OpuWggI+N`R)4(X4sKZh9Aq|JO@liCb^h_B^M@OU3ttz>
HJ7wiZw2g=T6$un?@S(Hy+NvD2bqJQPm}25J2;mnp)chZ1(uDDg=wm87Bm?RDa{KF-fkH*VR^!wT;BhlwGMO09YbCCjnSYbE=Y(|UEK(+rexBr&4<L2a*$F+rxY5Iy-UDx<QX)^+Zs!L%IoQzaL|eYjK}mKlma?@
otkw2V*IrUNI@nlBFvM=*rvOp0Ym<#{>lbUabd^U0_hP!3h1tB>>b>|AE|>NhMY5M2((ev89G@WxyT2-=Z=!hh(MS^Fhb8$PAJ^NSFw3O;-B=V6}PtDR2c&me?)4sR!hXYWj@9KwD79?#IO8AX~37&5m1qw{Y|F3
baGU<J--w856XM&5nFV8brmL+&rk${)<_?DnXc4M<j!C0>#Zl~IdwGY>@F)_p;6o1JucqD@R4A^l+z&4`XuyQsmfS)SS)i0lo<xpv_S^XlA@5nqIEGC4!z*PqCRGDt@i0T+pULFt4|hNwQ|B+9ttfwxIzmM9R!B%
X+NPE=sUG)ATqXVei5KPu}~MfD*GzE<0Lv!V!j}r&~Xtk4j4L%^c6_Ij9$B&I<(Mhn*cd*SjM}_*xU0H|8_ZCO|(u2;)|e!sV`Hxfpwrg7;kZ!nONnx`ydx;I*YptGRjJ`<vvNEoeJPGvg0NOg)%VRG`TXBT91(W
u8Yp_ym;5D&qJ~-li_I1HlsHIfmPCruUdDN_8KK|Ha066SbVZDh%vYNEfSe;Gplb(N-J_#%yFRu4$k#rnw#vS*Ik*)7!P;7xS+}hJ&;e;!189RTVYV@+@LPs+*}=wcSIRen?N{(Y|%n~q^RJJ%LV%>(EdebtEosQ
m#oPQU$TB2B`IM$m9ED1?6OTUXzEm7Mnm41zuR}Vv}Edtcryj<0l)HEZaczZeoPOVj|0+=bkBUx%Pdqj*$Es?cz<<VfPuvQxE#rmk~=d$Z@fr~@RWmSN4O2%G<Ce`@3KJ{caLj|D=MeF$M=&6XJDNwn150xXPkLI
@7f<7pgI@c1jDf<b36}}$A)1u{~{JMnKQuE<l&9l_$tGRW#FqHST5222p^0RvQy@sGzpUTP~zo7tem(7WzdyKmwK=v32uw6H()Mp?-gen`o&Lr)*B7ttitpN+muk*E9z@$EggN@kC8KFlFjKQ#yi^b7b9LvoX;az
{W)hZ{?h{~<of)7haVTNV!jL1y4UNkUEu=+UprjNUu{3p>?O7RDVT8GGh6(Uik;1?u#K*wnV_Xu&ivCzymXuuY!z={iSC;(A@zo>U}}3WY;9)~pL2pj<k*tzn+jmgDZc6E%|{?#VrKnqpma*2eet?;kUUdPR(x4%
yFVBl-_&XEPxvMha0$})7!z<KpfEQ-O$eRk1$_|SYy|Fj!)=nQ%-r0|EK<d-rjKrDw64a4t+<ih-}$9!N)o5%bw<bj6%y%a_vs+m<~He7D&vH{pR88#H0(!a_P%$@E;4x?h@tL{0hL@#oP8_i;VrL&fdDGXuV4h2
xl~Q3ppt5F!{<uTcE5Ms$JO=!o23!4VCj36WKTw(y-v>~?N&b&qjM&gfl?a=ZtE(0?2EImL-x)Uc2=-CmRNBm8pqfiGTR0NXQBZ{9B0cb;g(*@2?I?hRk%ep#ZO!jUMiVNPZ1f3*#cuE?HbB*?Tz<I2>q?D8KU=4
Dr@kE*m_|5YRrSGo$bAlqoz)>e)e9nk+-bMUy4o4bv67u{2gcMDpSP~8F&Jior&m#wAWnzd{!PZ6Llxde$U))yLLud!HLKD*!k=1+NKRe46U7DNA<y<sNjX!5dEq+N_QM!Vkf^SoUsfK#>*~ifd)m4&j)8O)!hPm
llrs258cpVElZLsZTEK>fCJ*LlVcZ<MAaP769Lu*rW*9*$ik3qhtULL-!P17rK_gevAGNLEAM30jK+ztY-K+Zq&TVc9fW(d+?t2pgH{ch4r3y*+*f(7g}Bhj8CG?#j?Yj~jf;@pI)pa~zWi#3+rl|nEVcl3-0GG9
V3Xs7q!n5EwK1p2A*pIWkWzQWc1}Qv3b|Ic8j&^H%A9(a`E{R5>DT0cfX<l~pMLH(h|SIfHEjuf8OWJle&cfow?<tJ5jEb^lH>c2xLyFwR6I_SNRhwBp$5Wg(t1)@BLilaEo|)8U`|^g&u5=rj#!Bm02^ZMl8Kes
#qN~HoodwG+`e~2=25rv1QDiSA=e{Lk8Wqd>iL*4_5YmXiJ7KSU)pMqoG?RFG09Q=vogz7LIh21)r`UQ@S;KBeizl<Oukh^k|nj$WZwzuw_}8NFaSp5tiw_ouwjGbt}q?WQs(|LOS-VDV%Zcz`=Hj+?;>fke5U}a
YuFNmIrf%K1*)qV6DkuI1+Ys^e<2Cu`9B*)@a*e^#Q^Cr7@bT9gu!B(GOw&*G%w96E|#2Zg?`Q=6*8G=um?5W7D)$r6lf=NRmM=1M*6$LV?+63=c`bq1DsxV1xR!w3_8#O4zBYB=bc^&Z<@I7LHOcdpq4iHki6#R
9U)S;pK|`gZ*lHitqE-enQ0OUp6k?~oGNE5T9+yd8eCVixeg~j)EBoNr|E||Zz%%nX@xi${m^z4BueS%Bm-jYHjq$ZnB8B<+etxo1#)}K<r;iiFLc)XXQ2~vnlMWI%E@;j&S(n-7fTQ!Vb&GBR_7GHBuxvJIZs@h
z29gDZ2)rF<r_^{9F$J5;8BIs({G*veyi(07P=Y2CboWMS^o#01xh0FgkH{}tt_I`{FecE_Vet}W86V`NbJ|aW#%JKs}V$-BaCyOAp--?RR5?)$Mw=WlzTrOS-Wnh+)ooV>_P#XiVG#W$0Gm6^#8{V$YRR5FTc!1
2nwD#hyK0MH;>0o)TNUUFXjVXy;tK^W#Az(W?+2PJa@hR`U@y65&32QM}2h;+uz?uL`;WQbqfQJ32Z<6^4sAVlldSg2-{=6s|&JkQfEit2fyW^(K^z6XL9%U%SQ)UXAS5urVA)OsvdU<$XDUS%_)Wi=q!FB2>sob
Ye08O@@zAAcZOu}h13vI6j$!+s$I&Vli6DsL;4$Xr;kxwInM7nX>XnOcduvzbVrmq0Vz%(=mOl|NK*-)MiA{!Uz0@Pi}sa^^DPj{7j~{2*J}oVs3duZU2unFFYNhrb|J2k1k#)&BwFc5>LQ5o*1Rs!<Ls_^r5yAd
RVm;N?Bwz`mm~clJ7egq=13kG0#o;4lXsem@>+Lg%~oUmB)c8rULQb;!egD~FDAR%`7bb54@>wdw-TYVK~tFzd{e2=knA|*_`x;@+!Tx13mx;%5d5c|U%LFP=A5_v##x_rK!4`nRZn!m=N($z4Cg7^+&t-yRbP|b
wkl*m0DtuP%C_QTOJ%TpUanGkBXO9IG(7-hb%6ZifCnefBwLwcdA-N^HcY!M300IiG6)|*z_Zt|W_GCWRlZ>b<FLXrijsH_zs!c^Ua_KHx#3S>H6D!v`cP#w`H5ljeZ=(kir?B^?ruuG2-&S|QYJe;<cYrv=>xg$
yUEn0#38+AstS6}5BA|NZNo?yB(%d)LzNholV;><n?$2%pH(D$U5Ji41eJZp=3NvK&?&KPxDH~_<rtuRU=Jc=o^U_&OA>r(W~?VoPCC?@*wJ1KJrFVvU9Wb^)mL620O8I*v(JjiK@77ApdMVc%2Se$y-{7Bvng`t
>xPZJN-Pb=m<hw>H?(zQx<zW40J_>w`S<cfg`4jzopv#FPe6Z+i%r$~jT-VuDUNSd5RR#<GkPQ*Zu7O4Q3Jf}APJUliwWD*-ZBa1>fQ`=UT<0E2id95I|CLfpAk86$!L<{e8Y9h2MvQv>8Ha;hyh~}d#x(@kuP0i
3Em0Ccn)WlO84`UKPtC}t%+{)gNpAeUHWXzgkJn9xaT)GJ)F>O^v2^-G&<2<?`q8fc1C<>3fpxAN;hCG_Pp_~x7=*8&2IEJ;C>9d>3icK5Xxhv-=QgeX60uH@1yVQWzhM|pt^%JTsP<8n@mlOM9-Bd6@Q!~qSDHv
pT=QFRPHdI9i;T=T4);>XYr9-VvhCt>b{Q*`qMjM1)`o;Ae`#}w9V&?3PVOF)1NO&q>+w>Oz_<O*Y0?~hGMqm!Iyz7S_fD88+)Y1NNNK-f#(T&t3AozKC*Mactx9jyD&Y<!mPM1y%Ybg{qoA5xhuHWl_Uo)zak)?
ZEy#SH;7Qii<CQ>!+~}+it+H43g|S<t52s$x`aVMy&3qTYg1OEVCP>ftQ8s8UW{&1NVAjHokF9+$e6Hft%Cvwi;uz&$|>+H1`wsAK&C`ClT<KxN-QHD>Ukh%w@=!?blByoKl_b&#5t!G!byzu>s3d#)D`Nvb{T;~
59l)mSZK<NzBCX+w!0d=^N4Ke|MK06&wi>`1e}6v7tuvu_`6P+vW|Nu9Ce+dD3?T+7Th3{!#6+z(di_|ApB2&(!N*eu`)Ot_d1KN+9a$j-R;KK-BYuMVc#3<fNj@yrP(|63UDB*;`CV~3=<r6&1@^{WeXL!1l?y>
QjNkQ!@{VVDb(9!dYEu3yn2`(DzApANn4yk`d$KeK|%D$1hfu{)KhFfLdJK(TvJ)gds9N8C$Ew*3w&w4TWJ!Zb~5;(f)cSK7Mr8rsd6tZSTlNj^>4Q-A?dOF*Yji48uWc%EfsB&54AI_$Bwn?J*Q!@KuEqtwf`tt
@v!3Pgw-(?$7Gopp29Ja155(v{tPveStB{PX}!PW0D>L80t%}W%1OfWbf#&c5@m(40n}C6&B47wK6f&0AqPmn9UR<|PZGMbZz4^q_7tD+jL>Ibb5}M6(E?GnH(Y6$zrsCY4pJ&G1ADG_=s^{PKQGgCABm65Ve+9u
hL)ch=+!?8<Oan17*Vi>==Zc*X&vYdbq3<>I#`7pG!H>;hL_WuIUE$-DX+TUbz1!?B!ycPAC(f==)Uoa;|*l^pm?>ehW{Rp?T21t&P!6VVA_1@%J#BMW<%rG&i&SgM04<FGy!RE&Lh<N&DhWh6EmzThH`d35Z&>&
jNU^$6u#!kP+uwaof!e7tf@&Zu;+=(vPNEIArG4|a^jv8Y3p8-O$L-FGmAG_px&Q^M=bO0Q?|$M?e{moI(^rpe`%CRgNT7Z@S;`YJ#XBt<E{CUf~eVr1k6say;CylLp-M2<*_N}@o;bn`{?aQN82XgKTZI%Y=!wn
{uUk7Z7t4$gQM*(qb_BG0_hRls`ZJ5M83MY!BSnA9MYB)jGJlbx~IKja_^21jRNM3NTn<`Tdfk!a=GLUhCi{3xG|KuSm=fok6Db_M$V!Uj@TKcA~-!nX?wgs!0<2p?QNmabma62Eb4R6b{s0~fsZryNew}4ZOOle
MGNJ^ChI@@+cbPxV$9fxgHa`}A@EyzE79E_6|f5S#yJ=`z{=S#T9V+`)J?hwlGLR9)njlkYGn_VIBO01JwSsJtZjx5S&k*m*e)^Su9aQ@CE$@G8du$~7uz3^JG~H{hH0;dU+dpncy{HXjJm(xC*@H(sIl4w*KpC^
th&7})m<QBZhDf4q56M|>W*kyKf_SHnzF+9QByJC1MB*xI9qVMS8ktyy+j&d#+y|iDEio2ob+$={b3kNoV^A=C#opmyDl6>`)W~G*J_o-dOl|ZGb42w*~%tQcB^>09>Gk^u->8(zJ^&T;wes}ww2CADgX1`Q<zvF
TWg@7zSt+3nI`RbJdp=CCLih5hSgMA&`w~l@&7Rgspo6fO8tea5iRkyTWv5G{RLal;7ZTM3E|p9$U>2YHGh819Lf*@>}Ir9EFqxQ58YM@>b?Zkq2-YZ=xj%iQh-|h12V{+>1$(WeHTIa9!56g2gIN7)$duDJfD91
R>6Zj|4%M@4ezZAt>HG?JI=H2Lz#Ul+T%}lq_TnxzcOXGch!W!L{v4<>XXIx_~jeat!%t;(R>nkRC#B`{NDV+g~NEq#rHVyHUzT$Z%*fPYBY5<_G1tSmY64mwkj}|kw3(6iuW+n(BDn0&kNM4A1R5*V%iK(rUzyG
O`6*j@s_H)#Y5QWp&Iix+OgBXMd`q;hf&JgS`7F{O?vTrx*jPEhVwiWhL-LXO=SUpeucp-XXSVqf0;vZaoxf>U^~Y$j57h*(RHfq$n9h%?#;Ot+06q1?OX-UFCQ~hVBsB$0<1h0`{m$IxCl(K&M*OS>jjoaWPVSa
_EuLjFnJ8o*g+J^`bSq68u)Jyp}U@aQ(7%jj9(Tv$G3z!!d+4OgH03>Wb^1m<t)fZTh~+oXo4YDqwS{0M@O?^fLRc7J{me0KDA%(me|{KptD|;ISK#q=X%n08p}6YxqiOd?E@ncp0z?1Yb4h_P{u24fRIGJR#Tpt
qlEio$vxp@?;VDZOse;%w`NeqZb-{5pf+yJZr0zQ4g$^wZQrR0P4}smQ|%J>8S6@BtNORzD7)zQ0RJW!t6(auBLUGTrO_nN&3iEJE|%k-dz<p$oaC~k5-gnHfuUJ4JAR5X!6!wKrGyFnbYLM?-_$*6+f<T;y*kyb
k(pLcjS#9;YEJ)?naaa=ZDl^{KoE6A9m2)FIh)1msaL#X<ZV%#mn*Ev1W|+6FE6wag!l$Q%M1f5r3OtnGRAL+o5nNaDZc7x)o(3qGXT97&1b02RLx-8<-ZaQ<&cF+X>I{XbYb3853wFdjj`CPYGtWU))|MYd0SbI
{7HxcX>%qG#BX}!vV`R33#x}ctwvDJ`MqjGdD5xcn#=MXk&DrRflRO1MD)74Rxtbyn;zaTGGR7_KA)F}&%q0lpDXZ}7`=1Mx-$d$xK@g3X?KiHH8XmFjd~GRFt;p}-Q6n*SE;%wn2>kr=ahi~4BH`;56pN!dK#op
^u8p?(u08Irb^%;uul_--NS`YX##6+GfYhI%_GK4ec!e`J}h7f&oU$D=_0uR;)E>Uq-&T)xMFIveDI7JTpNTgXS%c}cEH2uJf(YAaEW4%7?I_bCIinbhlSMvVHVPRVs)M`;Bm}m8y-k^x;v)FG(D&REhaM!uG*U0
4B&Yn!pw>xk<;K;4$(g32ulhj63&*K9y!O@eiz5RawN|<@VIxVbWg1hC8Hh-KhyaDazNDt;wPMzR8@@qDZy}Daj`%Vhj|nf##!mmm>$g@(#eLVkl?veEDUN<axM%E*PN+4c;LezJ5~=>3OL>FFB#nL(y4EqV*<>*
E9=29_qZ8eppmA7Iu4hH2iv4TG9^B^__ZY|P#Fhq!-L+s&@wd*l4T2Y9rpw=q_Sk((b1>l(?%dMN5pe<m&bK*`SO-PJF+-BXhok(6Q+>Bd99)M`GF*lgt-~<IUPqHF)c8z@K25a@N@dz)|{L1=s+X9=RY@PK4CF@
6XL0-Kj4LEZnd?wuD4Eyq5%04uNFT;xA2wYE$NjYdO!d&u)@Sgq*mJ1)#eQ*(5DxcXN-G~wM~G^?_xmZ?F`c8Iu(hg&U<_~r5+me0}|yw{bw$w_`9m98B9&lV9Oi+arJSxL_H6JDMGp5Ph=E&)$oh6!88S*5BmJB
Y-LX(DJ9kCyOG6q4!3)`3xUvH6az%Z(imL;JDqe6vcNE@z(@7fpEnro$X<Il(E}ra-`HEA__!EwI_%+8TrG4`pF_EB@}gY(&od7&`rLrl5k{DgN)zhR{(IFQm^EKEO$~=*01<gV$wY8wr~Vt#%~3~OCYwBFL9Zp+
p#*vNL(M(Ty4!Ic-R8MQ?(K?0my=e?L=jwh2{qT#hMj*g&#sD(%BSp}jrZquzu~;O;v_ZGfeo6JlPF^~%MU56RLL52V&D^7dm-j9XgzB+3(EOp!q<g94k2mw@erfg^H@3^yY7^w?AH1<;Yg%ITSd4vu?#Z1%z2pk
l+8aZB;sJWoUW=Zb_ZHeUo03vVZDmS8!uN?2UvyY#JbR}E1l=yT*Tvnno6EI&o28=Kd$vgq#+fsz@8nz`(nZ1TR3%Gjkt>UWXAb0hK(#09#2%1*}Ec$RyvTB6=0#Eh36}0u#%I@4OI`6vtDcgx}1&wddWL;+8(5y
!Fw$CK^Zqw`d6ogClm@HDjpn;#nU6C@xE?z+2g<A#;0j3+2lbYGOmD2)UkLCdT1<H)GKwZLH94~GTdg-@^pkTYdZ`K5u}KhzZ-|W97_P9*~qJbb^e7{Wv`qte{%+M=E-cdDnc!FVJ4dySv^yM9DBMA(%skbBy7_V
NU__ivC&^7zAG{7hUFvnF`TPo(3-xy*hhH;`PVx*T<I8h_sJZoxJhbo&|4dO-4*U-q$*dO&5D-@NIyLnRr5}d@qO7D)*_nI-d^RKJ?~_YZ@0!P9J?z+UqXcwf9k8?dB{ik<f-ER{}6Y%sc=g$b$D&9%*w#sib2L!
I$;fqB>>DDn~XClyU0S*+z!qy>aOB%AU`A_Av^A6*|?J`s!HfQUzS>!iTi>u>M4iFEbc|M+*O}|;Ke}2SemZYov@igoE^(%fC|0ab1$jl-H;fH=IoBd!ik$%Zd3R@h?D~Eg&xmlTlG$4mlXc}{O#i?5|G*JdkGi5
h%X$3cICYjsv#+TjRflQnVK@SddBnB{fO>QXXohH9EVOD`uboWejzKjMzcfVA?DJt_%TJNkTCZY)<;BsEDE;aJSo*pW`}dFAmJY#zSl}F_k^`K6#4xra2FY%D&7ALq?2jQY0V-DD$eOgVppTBw>=4d$*n_pII?$n
iXPTAejK%%MZHo!+%J=}4!!j8mZ49uZcpM#RCEb`b>x(eApDr?VIKm7-BF<B{>^sY5?vD8MXqqhE}fk#D|BrSGYweupGf*TY#$$Z_KyOVlKaw_>U+k<5+w0U0xYYJDem?f;7KwIZE4*(wooFfcAtl)SZ`I$goq~&
C^KHYu7UJ@vz>;~MUb0OBpJVJI^PP^0+y`TbbwGCJ$nd-ysT{y7Qrmrq0-@=2C;0e5-3slBUj@=sM$u!XZWztr1>9!z1xyGubZU;PVe4)G902EoK11KZ}$!cTp_GEF+`@>-6D-|=(~bC4DeqX`9jJBF@ANg8U(l9
xkTYK_Y`9SZHfgnXpop&&}w393m&n1vcqI?`@0>TVZf#I*@-={uZwDQTl7CF+mqZD4$HJp6s~AuVMUu^3tO?hR8a0xc=97xWaSGkhnsoyOz;voU+HQNW?#1|d~0O^?D{TkSxh-ANZ=a^Aw{IO!!$qGg>!jFA(738
--1R4-Y|d%WbDkX4r+Vnr1d@`BKHBeRS@5KsS~6K_G$1BWn-2_JHfDzR8L1DnI#23D07)InjKTL5<t*DKBf>9s2LXwvh>6uL|)U*yiB5G$eM=pd82NgxIh-yFc~7?2iLLFd<3<Ab<bI*3!lVAJtRb%<}Fqxru1Kx
bm}p)CaRKF9t<yCCD4qYu|P&apV=i8`IUHXwN0mKLLv%CvhA&_<cb(zdwX^zi^zToB;~kIxl66NkKffpR1do+GF%bht5Uh}ltOQ5Pk6x`b3@>`Uq}!{Ns2jltP7%}?Ut#rafesYZL-|G@K7yClvD_iw+froCws1|
HR{(%U>-Ny8s{!BOuN4C5}JCkWuCOgTa5;3ES;O&gJH%>Ju{jo_cTVbJzB=UNk?=VI_T}HcL3Kq=-7pTkbI_*^X;brNo{0m54m;y|270_Lw?%2&J&Z$6e1N7Ec?^?e=9xuu44Xt>`^#{ZuhSS#8vG63tGM7ss2wE
J^+*RZh{_Mk|rQYld(2>jh!HiU=65jSryPMnp<T_8v<vqQ8c8`@+^WEja3OTi+C0+{#~pBW6@N;ykP+#2{BLJe@u<1%XT@*_CI;%=`mfrj6g5&>Szn&kWCNO3or57T9p{}QD8K}Llid;I{U%zHR)F*<*4bW^@ouY
ma|;ueuzckNC(6W2_31iQ=_X81LoCfa!WCH;3u)P!z}c$9CWk+edt{CF;M;tf~4zK#lBonFLlW1+0%#S8<SqvH60!}p;p~KDEOsZaX(1bYtuSVpE`wNKzeOdC$Q6=II|E>^(LsM;U~xIvi89nA>NajhjShv!vn7V
t^`QV4zIyWm%J*kwcs*3<d3p6cXdg8AMIFitaziyoU)C2j$R=iTw%00BRaRW+#8CixyQ)A)U^<bzth67eUS!CXmKOtGt=9nw=)<75+4f*r^e)jqJAjrxeanEn3X`X0553y_JPutWc;y<o#%4b6T;k)l9~Y_$hA^z
VcNCN@29SB&Y^mNF%xBM+q8579n@+=FJ(ndB0lXL{G$JVkVmy!@A~-IZATCZP((mk)2f(&Tc5uhr@3&hh^7~aZ~v<78|ja8NFtQ+5Y(2QPX_&QaVA}`d6p7P4gug2=NW;*>O|op&5YL`2|9X7y;Es^1CmIEcyxDC
5?{KMq80bKH-@!Y`bJUbNXAzalG`4%Gf-0ZyU$;L-W?_h*sjSnygZ__h0Y<#{jg@Bsu7huUAeEPx@0n%InhF*%fnO(HUmq-kEZKc)Xeo?5q~_J2M!07u3#MfClVC|XN`u6t9=bUZM;z%mDgCUZ6*72ggIYWKsEh!
l^3+tJ=Rto2+kQVnl<N%cSoaJ9RV8TUNl!mRQar$u4ijXvOHgEU`fy3GeOM0gi`P+XdIG?9(NzEfTTvg(9Y>pG#TKEj?#BxaXZhU#i_l&3VeEX8Qcokem=W>Zd6(eKogN4pg130;=UYYsD;)PWnW3o?EhT=*g?T4
x#jMT<yc47t{|pt?ihXTB?G+?8z+&SHLJpXer}=-a$WL#OaxriB~S^uQy@X@IA<>qIie=vWSJ}r5caMZE57ebYpd?u!+4ggP-<C|9&3%~=BfVlcZ1x>{4^)g3H6xcU8L>LAZ$@7y;s?|qH`s_F{4$zHHO~~OCuo7
M;fnXbu0RM?fnq`q14Tn(}c^7W-1i^z0{#lUf%#bL$Zy+Fce>eL=^nK|0`39(xPI;hu5?upjkLi;%T>3%wW>8e75YI9RBq&iv$j7XdsOv`nRrPi-Gv6a794OEO*)GM`ZecuVJw*zj+h~_H)(&{IUSrKx>J=qKs}v
^y!zBUuQN|5!8P4lpMt1QKRVT8+ChpqdXLF&$ORbsE#y<LuK7>9(Dg-m_>HM#){a#^~<56c=?dlSbL+X*)AkdV#A~!gWn{coY1QxH7D6z#D&6_`NIs3tgl*gF6s0AALqA2K1G6+%F>AjC`;3h3pLU8t>tTeOr#*_
2sA$+I*!X1*lAi2bScAqyFfqw!sX419X2HP=hXYnoox%N1j;i0IT8v)=EQ40Xdp%TFK?-$%aHRloxOf)xMpY)9}wQCc?@>}p#AN=VT1vg>yC?I0KGVwePXIQ7!T%X#6u_Hoe&vc*=Tld3!uXRsn6ou5KAcv804Ce
Zn<m|K$HP)g}8UpJce5@)=i;#5dAXyEi;!e_S5&r%W=UCc9Zoe^1}j07hZJ3Sp$Zu?lQ4f%LSG);gl<-%OsS`L=b?&OF$!=4Mwb<55e=K+o%i)%dc!th;r*3igU1V2tIZ1+0a=H&8cu|yI>u~Rk}#C6CaZ>!=6em
NPp!b)i+90Q0#w_8Q!IIB5(Ivimu%=yhTF<C6RKJ*=U~6Zf@+l0UiDWZ|m$ceOFln*i{44>9cTxm*^Ifn~APpq#lA{*E8S9eTuNJgrvn+AJ*_LGcl=w-;XiY{2*3@9=ZW$!S806>v@z0qVeN$S)!MlsPZqvIrl(?
a(!Sw^C|cflHP}~!S1C^28_W^jXRkG5$`em$!pW<62Uy?VEo|H%1GT^WT1t9tyn<{KVj-w3T0$!ceRIc<P%@+Noxt}HIvx<>LZ%A<tq0WGf6j)d$JU2%j<#1TEDNadq7~PpQa6i`^iY40;3e^uXJL#_%p2ZnWBd7
?WeG@)c>SAt6S?A=rO8<;y@-IhVDf3_SYwn3-f8n58`o}B1EHE+r(mjL&&kpwaqsxtbIK59SZ%k;hDL007Q-{4Rh-6IFoya(GOe~f3DjOo8%>$g+IKAB9}u3vbRc8NiUzN$$x^P7Nm25K8+rYhRvB6;)7G(&OPef
59Y9ccd0iQmPL^@VQIQQH{l*)LfmVXe%mop=>?fkf#{dRh~Un1ahp*1OAv9yZtr@$*khs5O2+`!P3LiA@2_3$np<Rh<<f+*j)lNL6{fz=vsWBFm(4az+=&mUI1{9gnb2Z@bUO2`AnV)XGhqP48rwv+H#pywJmo|a
OGa7JhO!`U0+>D68(M^^MGmCtq~0HdoB`aWaXBHd(WuSIjg)(D`pR8ujL(UN#5J!z)-%{NyL0ks4~cRN_Qw89E0WoSG<+N{vu7=MBV$f6)tFSEHt?2K{f~pr9!%A*FVuHLpNi)6EDPrBo{e*32_Z~H60qonV0!zM
Q(?EJW%#4n#RBo#*)jRnm7E$-kZSWM-;aWlwFQ+Bx)$p)ab2ByBg>@W)+kpA1#PhorWI&H0lSbz@>;><`#DyJFvw!5S`&c!Xew8_e*kM@6p_fLljM)vFoOFdIk(SLpYG`54Ow8`2!tw<4cN%i+PNOEN!`MW4WFt1
uosR`0wwAAqhA5bDT~eKW2m?fQ{t;F;2rC#ZW@k>+Hph+a?clsJRZ$kkl+x0xLeH49JNi)J%fHHH6_f&Y?53BpGj28RB0K>7xKSwhwae+;v2su)K7DcG|1%kpdli6JF|g7aG$o_VU|2}a9Z2z&X=~<FV|LmVp>h`
H>`gm5N19yduF$rwOoypKVHlGdkvzWn9lzV_-UAKsr+%-@S91HVg|Q$1i6M&o_cGJd<Mw&R^C)t_0oH#6q|rG!(cH89R#-CskeITS}L2}ebJy4I(`-ikh36CCxtYD1l2$_TAfiUrbvh_z>Mpjjo#7yJ%WZawe9@;
zk}&YCUVqaA;<f&vG%sdzE-?#;(*gh1Dm15qOF^HwW`Xc_87CD7g`6dbh)O|P>0#Gci{`p;E*z?@4SEe!eJdPd>)s)%y^|Rt(;%+WP}L&9PpFft;vWxdQt?qpK83^2|=dMiXYTRNU?u;EDQCX=`c|K)Sa?eEw(fx
8SxhXesfNGZo{AY*^VE-YEeGZX|}%Z8r>jUdyM>VPU4t>i%^EFWK;GkU1fW$D6R>nl-0Nc<93LC0S=WaDd3Z+%-w!i!~Z9@V62gR7!%dAj#q^(=@d4cUB|t>zTxV3*K+eHSfb!8tF@vxthLeoY=J}H%c1I3gPd}a
r)z~AUt|P9JiWTH0>?89Ec4UQ6i<6J%ddBzB#YJ$99<bKPcBctLLZxF#z#j|)~y*dHubg=x~mrG(Tai4_o~$sB2OzS7<LQA0xZeMrCLD@ThpeZPbOVzFs-4`{rU%{NRyhyX^J~BMTF%NdS>I|btqg%cqpD5MD<!-
9?+z_St06s=~_~I`%5|#?)9ugM(UDAF|SXLJnjP=#YKt~PEAMO_x;I<avv;rW(DKl%XQLzzNsOxw3-rbg!@a_VL718*)Q>LR6-pTwz&jQEh3+$Jj#~_tSv*C{*EKgJUnsY^$8KhwQi)ejVq(%De(@pR{nRAk^hgZ
R+a-LZ{EeBYpCOc#YC9q`01Gp@zUmb=VoriML&%b&UqbBavj|g)S?-vx<2lF*0u6hkvH36&_|}?I!vgQ#yT+DX`u<Yu&mNd_?2auzg3BFyTEeKX;TklUbrs{Z+RqAQ$@5{6r;oYRaPo<y-_o5kc{gv<?M_XWz^k|
k-kYz9fM*Z%4tTUbmR+tg0#gVzHCzszFm=QD~iI==F)A%&bh)<TZMMb*2aiNm-O(zZt2NA*kd+*O%iRxzi3Ry@mjJ+b`j&MaazAB5W_gUFhbYhm-Sou^T@*jLDhiDHHAE~1O|KbSMbF>b4@RlrYFdY8~dg#_Ub>y
vKne`Ap1I3ZgSOynx8~d_V&L<bs4&^A21bum$b*4tKFP=4CD*}Ft9tq9{ufs@AkADuo3z&#z_Q`o+@Ht-~WSQ2fM+0V2<?c*CPiE5#hrUw5ewug4_~ksQpL!$t%K#Q+xI_IJOsXWQ0x{b7U8{2$PD+Obsvbm<zA{
uD0REJ8M{FS;=1w>8a=&lu*G6C_|cGEKmNvKdvow4@*fULrhh$eM<~*Co%L7*rKb2vH;*P|3R3-QSF=g(h;`b4)%#(+!5W-uZLH&9E%=cZ9rTORb102>|ZzANDVWh{xb+UCX)*?)&kQE8%*@+uv4|zCM8<svcOC-
QGK^+j=xB@!wRkYvwZ+2>6XL_h_C@>F^KWg#&FJclXN5O_Ji_qvg<qCp0To8YS8K?0d<T|R>{^4>=pvSwWq@C3N;~G<~ht7#A(Bh9ESo1?s2An2RtpwtR+KB<e>e&x`19z-}7()B$rspyN53PwQ^rDu!SOKC9Lq+
Q}Q?ivz7uIyVp~5p8s?1Ytwt}k|7;neTn7{Zr4f{?;oQS^?c~h_nQd@lOYw!*Eyb%ZYoYCz5uS#R=Q0upX>v>Sa1OB+M?nICp$>0im4~qPx@N7l3>jS@kq?ony~c_;@eM*<iaw{mR^EC2f01JKzXovAzT9B-=GAL
h)Uf%2h0`&i`Q^`p7=`K;S53mb2-xn1wj2!C9d5BZ|xLF{eEFtwcgX6P1*k6Lz(-Zn72$Au+qjKfO3atrcG4@z{whZ<PiLEHw{Y!&%x$cdW!a&yDXZP@}3ck&3yzO7dOrgC_=>l0t_AF|63;ewP9E<4ZD?7AcA9r
)%|={Rqh1g(xo7WfMOnpqTPyln`q$m4uE64a(q7JtR>Vj;Ny5OSX+{L6HR23By`AV7Wn)vq)1U+aDs<lT(SNzW;KDHs+9LA%lz>%Cf$$ifuV49y%c5O^%;er;lzCdZVMYn(QVZRr>|Lu(;IFD;6(P8<npiLlaL(6
77Y#sjt^=p>4SlW5k2z$5%4{F2KJVvO4427y|Y9p4YrzRh6KUUgC>61t-{*is)w!L;w6-&MHz)O{$1OQaF1g{0&)HasuGeq=hfo%jrlm1i=Lrcmc6M$B(A0`_8ZQ-w@fB&IEXp{aa(CNe?g9~**)FCIwvy!Xgmzk
!B*Jj#UGT-J}PfOjD0wpr~fOtPxi&`?UlpGcAh9A&{nbEy7sb0a`%|ro2qba06)BQq%&69u#<@g9gyXFn_j0?iHsah>JHoKj|`{#PV^;{@4(+y|3=`boxCodYZy*O9Q7NKl4I*R$1Y7Idw(Ms7S$&u#h8+(t=uPf
8si+txzyd&(g=$_eVAcOqfj|ujQVVZyvPiW4zy;^BaEq^KhS>L4f=8xjccrde=RUzGe$GuOc<R}JTh!L%0VG@Pi7#5z6aKE%5v~1pK*lF>OW>($J37Q9eRo{H-KVSs=m|eO9}A-x2ka469N|Sdt969ds3=LV;`zb
`X-(#UgVwC{X{ZVPKz^c9yLvxj@s)?^W1jFtfT4?deFlCSd(7AfRuWV>7<`s^k@n&=D(D&x0s=FuD8s7T_3=1XPv1T4|@bL#FN}113nH*E49gbcSM)Bdc|Ff-yMd7Z$ALSBRYAt7K6a5^dx@1bH+|3x}*uY&=xXV
Aie$;O6yS_oE*1%VGFv0+z2sbGtOajiMB=*P=L9lCchsD>r*G|P#s_RqL4|k!mgz$|IH|lZ|CWA)SOB3r}(+7CF2;i@3j>ils&+1h6ub2uK(+|`&fD}>`jIWuY;rQ)$<9WJU@@?U@YxD12!#2B2woB9z)5ui>r@U
9Y(cOaFY;;s7vf(+s0%ZsWZL%a}gAj>03eMX$5BTy|-F6oTqqMf;w?KYDKi`kioP+P%4x`94gK9j78l1T7%+ar*X3|6_4@0NQaW?n2`6r1hQg%22_CK>z#Ia5mUZB7yN>p!S&O-=gyoCwh><h>Q5Fa8;6?`Zq?VS
f&`l3X{cZYAL9@6eCDS2vCM#bVpebO@3+0OD7CnNIBWLryZywTqOOqD!|+*Fw8YT||MBe_Hrrxo!F0voyAhR-vZ-n_`QKO)KbR!HQI6NAg`uv<^Ibhf_FY5kg}_<?>bL*!Xs_wtRoof7!L=LjBr6%&GvBb)H?l|~
=JmC~SbK9c@L}0SydS0$|3v!!v|gHdu6gXb60pz~l8Z!yX$8HzD6DIGxvjPR9uEYA!f99S0eJK-_sL_%6myjy*B5{LbaGm`1Hdn93A+Rzk`ER$+dQPxX5(`u@mvR|^nA|61QK1(M;b{|#xO1jMjdE3LHv0k5g`C;
^F6k&(8Kpx^%rnyA!@<rx~p(15FaN6?O_R${SWX|sQB(-P3USR#<Dto1xB(2kjXe`=bp?=9_SpD*=f$!Y%U2Nv}oLF1$p_t_YDFO1;7-XWc#gC-hxAq`21ous(&bjXxO_uTa^1ixZ$eeY*JhbMQ&<+Z9g29LNdAA
GJTHf!<Zu0Q@OfZm%zx*92{8bSYQFh2jfw{XINpA!Wc8NI71Zz1=VpFkTx<EIpB*=@K<6OwL{ih7h|TXkx~a{@%C*>nbi{AEa7pH;DFE20p_ZcU-^ihq2f3%QV}|}huwTUEQKF%`$PY64vUN6ZZL>xy=k^x8xvf7
3_@EC9(SR=i&&49Q+-xe9|ILWMdL_tO*o+Y`85$lYL=fEQEezp<8jN~dhew}u+C@vOw>7#pt))#CKK@g5^eo>N$`IibmnVN6`WN?Vl352?5j%{aUPkKc8cJ(6MV#HbVS9nHg<mRM;j-5<r5(Wh&D{JO99Moec0UJ
dzSPTd{M@>t=9%<m&;F5%Y<@c$w=+<a-#cIt_I~sUUr#ltXa!=Kw|o<&jBY}^ETp6>UXO+i7T>=Lf*3a&{pZr>R1Q-3BsE)OvGaW)E9BZhLN%|B*U5s$e&68GF-<Mc%d+Fsv6ue&H)QAJ^zkk8#(bk2p=3fQvTs+
1(m2hYp~rNCOlbM@+IxqkI8?)wJWXMMi)>1AA-5%GnvqMoeyQWh0~Hu@Hlkmr;T`ebPMS_@yE(<3=?eT0FI2=aqZ(eXPHh*HVq}jKXdY28-5)~`Q=%Urm;LGW&>gLCG(*L8gcZ+c;IktqgnGH2XcL7sYZ#qR{f8E
iHHC(znj)>O-VujQoCq*3(=3(e7HRm@7q~kXkJ0q7=6!+jpTFK)uxrFryU|8MOzuVg!#Fa#OSL5JV&-o5AJWpkDzUE)$@IDB>*f8{%(g&&No|wUYgEop1qVhaJzHp{=MtIvw=3Y?R;s(;-kg59DKOg1Bx|>JYhPe
HORh=6yza-5g0KhsBW(q8VG&E3Y;j<L}kC=L`5wXCXa=JJyyrKwMI4b`H0ee9_AU?q%5{mp?kYslP}LLYSoA&nd3NuCD6r32@Z;%1O~KQ2yk6%#txo~lzjgoL=&vHdAu~5h4P-|H`C@0=R}74UOu0SR$dcJUKrZ_
7hp-J-pYA>LvMpSFx!DqGgd_qE+h(U8-SH$)?qs_$FLTgf*>Jx16n>vPY&@Bp|8UfKRV`mFAJ?Vs-3CoqSXte^M#=9hUEE1Q!9lTfY82?mD-90-SB<2>$#@c7VA}7r3XtKm>%fV>+ZUHv{v5mwFFz>xr6srEjxK>
UvgL;qyC_3awQ&|0_;_wLQsATzGq<3Ux(Ta#E|1Ta1;wx-~zXh5XVAvh^c?>B4vhcjH%vL{_1>E&fHzp9gjyz29V4s^$tn9;tc=B(F}Q@;YNje;DE-?jGZ3%3fR}9XB{N@bnRKV2mJD2Z^i>|olSD^rz+*+p^};r
QrHF-wJ6|&Zb*AAAR|agl+!LZIt+bW19F(Gdf|q{aU5dj5Gq-){<5ayTQ~?XO-PWd;%9<Hk*#2>38VRVrl3RgILKTmJm)b}{i{e7H{}m^UVT**&rv?s4R(+_v}E&%h^>EBap|$beWRgy=^u1!getIFE?re;2}Rm_
z;~@l%v5;TD}Blqe0~BqC;GT%7Mmts!6LLeg~ICSyqp6w41|3q@H-Jlv<TXOr=&bRBRFbIdjx}(&pqpzG``$U>*tYo!{)rbx}Ye8qNNNd%$)}mfxRf1JtM7IsNZ1K#{w~|5DH3!Zhd66grK>*Mif;Hn;`=q4RLkE
xK0yF{WFnnPt%51a>e_~i%vX-I-*((1mer-)5Hz=L=<4xS1Sw^ostz`He4V({H9A=#xb;!+;dM&9xR8~SWzsjzYQ~KVJXL`Mz}At*TMq}9G17HbV4G;t3BS0lrm6itK0uPz*ScOWI$*hNmM^cYQ~@H;*Q~k`Ju3*
(f*EAEE74@?$vV@7?sb7+0wju0_iX!Goatgi9iHIjhkn(vYJt4j7%t0o6nH5`UVQ6#1~>GRqP9`KWhdwEKCZffZZ8$xRfMJw@O;VD)`>Fi5^ffp!J_7va8J)tlSh?>ETDOTR#~GXv4-p-CCkxd+*!hi-(=lD>eXK
!6A5RUqMm9yrsZ%sh?Sp)b*Oh&Jvm!0_!`nLqf0~yB9NOLEpTzhi4u89*L)<c5P7q%m0(y+DjS-k}=;0{pY}NktiHdR2k0!;E<gv%E>zwq;nvCP8bf$TlVmm(8^M+s6(QSPf+hLl|DMp?}!NmYEm14FzHtbLO7_7
N>;1pc=)^R{dV{L;_=0?8TJ~!@Ya(FtSZEsAbsfEkBV!Y(br^_sUdhY_)hGwiK&!nte1^~Xu<=@$mXe{VZEvb6D`8o>n}CbXbs9a$+orduUA*=plbM-;Gu^_Ujz*ZE9&YU*Io_KtSu2d?%As;<TaMI3$UZZwL=(y
+)U&6*<RgsE*(%8VzyDLk_QoG#BJ;!xxTgSj?el<wm5wvzs?UPj)OZ$04Ea!I%km{jz6MPUxE#`rg(p5pE0XtfA9gwFq{+{XjhpBpzvvHYmisQBp%H$|80XLN0+FMC+bfmury4sMLL$~6#|ZQH|QH|AL4}@M*7$=
MD>y*zQIsgg70&UbPTZ0g=SgFzjR?mknMi5^zj=E-uLC~iBIGoS;mZ<3s!(&mb~M)+b_}lukLVMZq!uoQpraEneJjS)oZ;biOasp(vQfec{~9I{I3r@LQJjBJj1^t@$-YSrKvCG)R2Js9&Q69V|sUZ8g4OQcIIUq
2p*|NA@9vL#F)W|q*1*X`yx``Tzud$m_G*DjMG63HOKG!?knHmOK0zi<Qcw4FRU%d7`NPgxN~cHQC#$22Sz!<;bJf@z*l$-ZjU#-oNd|0`D6Ro@+uZA`n07h$qoN5E0<4^Z9?y$)bq`t?((Cnh<)MtOQm;<t+Q`v
6Y1ly-a?L!s3Cb{wHQl3Rrh;rCL-qzjT-+l>o=aO;qfQiXW7>dw$&NHGktzc=!<GOF{H1v@~uGez7;&=)c|%Kof_F<V-=TuK7h?WeHPs@_y@ZbnmqRQaxTAlsDBthyf{V}+-HHll72trfU1l44Jv<t7Y0+(<g%3P
iTBb+4tv;b@cN7C^s<#Dic~H=Bt@Vu8?^uyVLzBxOsdboO9uoLk&?+uHMq`*#%vbVkWS6itMrD#Dd6!S`wem^D5XDEwsP@dDCJ!E=Ff&KDX`5)dPDMhLFz0nPA#Qcz>J&Ka$HFG@4Z+jky=RBVxRLdK1;p>2E!7(
0M57iKu3de+ELXSyqi|HP)dY_fZk2u61YD2867>tOgzGoW4z(PA{eg;zgd5@Kr9h_cfcFSW&y>e<mUnY_>8@9YFB)7)le#nuyLPXKUT6N;S#q3!P0p+e~$e%L!GxPdusLWsffTmRVVEOkyymZ?_taQgx__FThWX5
`&o&X&V^GXE@=Z=%`G!fe(4pgNdBEZydUOX3O{gbgzQ5#*D6$+U}wbCl4?-GG;yfBizZWIS7H|#f#jpg8OBOqw7o?j876^g`mRC>vm@{=^s>kf2&PYI&H;PGqQlLM)#)Vw9~SbcewsQ0@Val(-p|M~7@O0$4bmC|
Ofi?*6Ev2kiffJ3W>_;TfgG40m@pYsjyQ;0IJTM>R<slKRSd{PgPZW*5@Dq<smL5B#-ceDA_o?w&WJb4w{KHZqNhV_c6AY+>VMrmymT6is$+MtV3P-gy>wgsNAn`+P&>Z#C56xG>U)-t4X2$H>FMxQgACj^t6~iF
(AOpje@1jg)DlS+*J9amW4#jC2+CCLK{GF>CnEHaY(Bm43x$vbf|G+A^OQt2uFgX;=RCJ7pE`4ruDL5>Ef387(}VQH!Y0iuaY;SVtt0`Pu_$yMhDP_;Bof=y`yZ-*U6ep?`@b-WeXZv$S8lo+qH?-)G?3g-h}{Im
j)=~E*#s;nfOciIHOvBUd~*t4vhMfEA`pvYT3``GFNgHg6xyPRTjp4|=G>Yyvg$9oY{4BC8Ayo(UPOhbmEpC8KJSS$)B!lVf8Qg=)qAhMioi7kz#b=0=4pBCW}rXztCl}@9qvc?7#Su#b-zz`J~+@VKy5}4lHnSQ
1s6&(Xl5qs+rzMj{*92zcmsJKV-iySZYdzJW(I^q7`G?q8k?ywczZF2HY(%UEB!FFMoKEMm*?lR?gq&<;kDD!pq^a$dS~4JCrcG#9i2E*?62bo14~#^;A@%2yFIG$JlUa@>s0Ty3xSKDR$#cH>mq1eD+jXOX6L4`
D~kT___nt)`68}k@p?}I(kg`tP2~V581?OgokU+=Id8ED48uE}55t40IZVz2@dLaQH5?cHoWD~RY_kgO_YjgP@u>%7`-Xm`*r#QT60yk)+2uv=k=gvHz`@6cDA%6*TMySUy%9i9X}?PfsR&jq5gjh<S~jnKDS=z8
gG2xEC))1O03=R%Zre=tw)CKKb^p2%1YxO9McXp0K6JtphB5<520?u$_ZRh$OMY?Ml>G`M(*ZmqDb_zp8BkpCaMdC!KkD`kR7h&CklF%xYiDsMAWwjxC3ZsO{wP_SX}PQ)_<FXjw;Q37&q|HG;)HD7`g(F<q>w0X
MOITunFXo?>;U>A4X`tpg}W)=N)v!&ySOy_7Jru>_v1mm?GPxFVA`CVq|<DhSxV`OW>(WJ!T_Ix_3dhAEWJ6qGpn`e)9${!n#<~8KMM0>5uWCcFBIA#C(`gHDD`mk+IYLYZ)!ikO{Wi+lg(*qP`|?gBxyMJve#uD
oA$loIHg_USzRm{lo91{K<*V~@*yY^O~-kMaZZX4!n|0IISwxl6E($&h;vN4r`<#h?;<DX&-|MJ1mUVS&jAhy#1Ot}dziwAtN<fQ-b<&F7B`6Hxrstm+&YmM_FkCC^NTm=_gizuwT;}bz4RkYj$jB&(OoKHS`M|h
y3m6;Nr9=8!-i-o09pZNj;<pt@S`MvKbe8AW1rC*Pxs61<`x&mE50sk#>&_~l1inj@Zwxzk7FINsLQlcgCR*jE$>0vGbE@En?u$86piNJ9W0q6Z!(zt&X4OVA+h2y6Y##fI${B<b?YV9p?8=Vn^kqe#nrlseWQaN
pzo@@Ra8_KVV~H<nsI^L$r+ho9_J6YL~eHkW<e|SU4a$J!LYc{TNz1!Yer*|+#D|XClUcipBzA*<Vv4>BA-c$SC-Y5*MaDLubr!axx4XF-4FJz`xI0N7irj*&ujs2usP*5i~bGsTb{v+yu@W0J)KoX;#nguQh?a{
S)<8;g_i<p$LanCO(skLA-Mfpe#ImMAXsHS-UN<oY>=e-*}E<`WGavPQpjf#6u!ND+`0gzsc=D^5eqrJMKMZO!B=u==s^f2&0ZE*a}R+cYb%u7G7)r{PhOc`nQ`scoZfPtq&hePYvUu;PlXP58A=N}t*qbU$pEDY
ubWvr?izyEx~xNIP?Z|r*gKGByoiXJaJ$(NHV_UFO2y+z8iDUh5NL#CJcfrs(a38qy)^L?B?u?%4^{VYq(L@@6Ga!*1%{GEB%g;A*mj>yW|qaEK|pWBhCEBpu|~p|zlqhB9G3<UgJlPa1u9>*Y6|V0ZyV3~hYnK}
^0?gzSpcS8(Ij5wL~VehwtVyX4nh&Z3f_7_77m36!USbSDB+Hk8GWwwZqK=~|6p=oc0hWc&?45#hycg=!gm1Y<ugGxcg!=!Rt9&hrrrbyjL3zV8IgY9XQY`{93y~47gRjJZQ4i_G~~w3p4EI;dbgH(Y@~ggT3V{n
%~O4<_^Zb(!}%cLXOy^nEe<<@n0Y64E<17%0uY7!e0#`8&#>AMWpQ-;_*s!8qjk^@Ka$3qb7o8!2c0QY(ZBzc)lf3@01%dBGlKakP)e=k)(>)VoNM8=kJ86kik%_LT+k%hNLdKRUneho>J+yW9G~dpvh)SmGoVrZ
Pbt*gTO*?^!YT7dfhaV`+J&2RE4xWyccta_;M&)*39XIuxs4oEdKQODdB%4@FPw9leo#9m1#F}Lfkd7cN|sMadr)KvUIaQkeP0<N3$Nh_u?s@Ec!7Jmxq5JFhurrs4M*RHoOx>3MxYP(`hLn?)ro-h%t$SZ4KVzV
^!}r?0Pg!(>&twP=VBm-U>jE8>?rXIRMIAQ=((yN@|*mq)|Q5#uEj5`=N>fkj?H#U<Q*<=VUphJU9cRBy$v$l-T7Jn)&^zFVd|qVx~d7q0E4eA8fP%l@WS%JwsvG)RUZhjfQKsB$WRvsi7Wo?-DBJ<IEISkn#EtK
JSi0BkC96|^7YSC(qzjC(G_7jlBTWBb8I05hOvAUGEG{cA`O-B_R%G6O+;5KhD3;;ya6Gy%SKTLcIWT{@TDwfRYcX#^N1#g@c^Pht}X$bbcr_dL~{I$Qihx#z4ns#WZ#tBvr$Y5W`Lg#?o1WKX;NB9y5vHY(72NN
^u;pB9TYLe0087w1UAO>*$^CU?`Ve(wN0g6_xO7%4@YTq?&}hu*_*?oE`0uWwnHmDBPri|#z4%C@?Cd!cTMpd*t-#R1(KcUs$&vtjwXRrS%MueDyRdOvnFPE5ewOT1uGz>7TtB+8uVAKSI9u#Y9;)}e%!u~d#QIL
j4>}`FIqr4GO{t3-|%6ecj8I6|2!n)B(8^n<XcJG`z}1``I8Y0wyckM=|WS}$E$Nj1le*$niApDCVR<~-v+8|RK&8F>XcpxEX2(i(|s3lFyIzkSO~0bUM<duk=D0F5DP{v*IA#i>^PSdZNnp3487b0Q(CXIop~oz
pu$Wzu-Tb+=g&M8g`O6UPDxGd2$;>e^Oh7UkX?_hx<nr0761EK3Hnr+m{!}RxR8ALi46oPdA~$lcm;U#{OXW4XiE7nE-7OXBiNZjIq}eMp~cs;FGNw<;`5=S>^~*uE|F#2C{{wsezol)s*DC$Jlfyl(fTV@&OEMJ
j3(?|T^4vfr*`4F1&&w>hp5I_>Z}N*VEGU}X=6@mQ^s>5bM$6if?z22?<?uxw3t)wDw-QPA|x(RoKbkVv3Fg1@nB<V=R`Wgdkd;J1}i;CE%qDLuJp`i$r0+}a&92ZXxK#Rh4w~dcgw_-^g9O^a*~mzM>qPVMuCmb
)&ej+MTLyIc=q}HABzVvls9zv2zaTipim4^Qf0KGD6njzhPOW^5l*0XqUY7b<x^KHIwFYlpM}!d+2QMYRQr!my4N{~W<}Hy;^Xsl#1xmf9>pN*judiNVuSu6w0W7)#3#^py0*9>`bl`H-NxrLt&i*z0VV_SxP^H=
_{T*)?G8iIDnxuLqSz}JpWbxDk%v6AMb(bdI*W5W@W$R?m|2KYHz$E3O^XEtNNJl&vGGI`Ws;@_zeSOcGLN4IX(0f1s<?*8`4T*aaJDe42F5-rGWR~J5&D5sKd1d(8oXhlA_#?pg+d6>-s3)Ox@&CdjLMt)wd5Vr
{#le3>a=W$G<JX|UygW;__G9PEh+x?^hdc>Cs<eB0OQ_4vQ`1pbqb{lcMR8pb4UQiRsuIH=2JJ$CLq=Gf^-e;4xqr$uH?boHPuvR3JjJ{s|%XK6JC^ruS`|120>&jg#@CqsCl$hZjO`evg+)t9jgo3d^Jve(fS0*
;07AB64<05!8u<&A%7)!z)wZ?xA4-Re4XH$=|y4Qt^B9>Mb;bN$>GmM6Uqdq$%e|-({iEXC@Z0N9qn6vn#eK2Z$|VAe^f(bmF8xGJPC8I;9ckIGfAq{=ePleGguuT9Hx?Kp6q<*-cJ|ngbF*^;dfPf*=|%}8Y5EE
{gf7l8}RPf_uU>EvtS1an`muQQ{!o65BOwpOmXZ?rq@4`-H!AkD6`WtLvJRyHx2jUi%vR;TY;(emEH^93n`#ffaka7G#D6TzDI`10Un04F$W{0E|3r{55Pshi=Zb6agVQ=4p=FN5ZZPfvTaX7GY(B~%OK#J<{8VP
^l>vzcE1W31T7AzxY%Fs*cfWUxKOuT0(z<=S7D!>v0ibB3{r3__oxEFXg_tOZd_qV{jjRX-10RkchIx7l#T5E@TD2<C7K9RMx2%dblKIOYp3%5{-xa}Pb}kSWYj&{3(F2`fzVGGL_1ZG7P3Dt9>Y1vk7qao@}tu~
#KS~S@oqVK#FE1n6O5@WK4G|~btOP)XQ7{wnvNZO=wT8V;Q(rtk5t%wP7jP!R4_d0cs?|8W7O4{A=r19CbsX^`mR86a4u(VOs6%il3%x(L$Oq}tSuzVh<CGqB-lK3tYa%JBiFWZbVqssljf2>UWF;|h)-xCKwV!g
3bsyOtICZ?So2?NtfVpUlBm?rTUg8&d(#x<&DGY7Uy?l#Q*3Q8kB`&hq?V0H*>`^W$U|}~8KQ8NuxmF%yM#w3@0Sf9>%s!fYk!LaFFktZYp}BC3C>EoekUEz?f@-IK-Ps+>KhN&*wzCI4HK$mfI@0{bPh#pR((qX
U^LFE36<4fdUZVOE&ttJIQ|rt+xs5HFThnXZ@wTLx;EQ&tmDQ7M!bF+-&cfnxj3uXlPD{xRMMF>DTYJgu9bNFZ`yh7<<-CV`qH0NE4S5^#5#;VR${J)abZX471{L(Qf&rH7JLZZF^&V26$N3(QH~ChOH>Gyo;)_M
^es#~D!F|_?wi`g<bm#%FJn?hM65bN7x(1U3KTto9tmA|y*G4ty5!iWq)G#4$IkRu38#%#pWSjjQe>FEg?b$u;u}w9s6rWR9Rfdxl^Kmc`Ye#k^iu4%d8(7Ws!)q94sBd<`Z(`*(P4%*q*`UEe<xL#`17*3KLE63
3PM{9F16T=P|TUTy~wX2d!R&oqz_E<a)cEfk2UeC>N$m^0*}47S#p@#E+Q+y*kJH0tS#_}YGT&6yCk7w&hj)pA@diU{+03iHql9qjl1c|Pg9bKy^g2hD8aV1fNYQbu4OXtukq0kH63AW9NR<8K*scs&Wa{Bng=nL
o4P_;+}IHLHckBDd<e$x8fk&_(Y2f~lxg^Z>&)z6*M4lK@zXb%WKZ@lr6FO0$YC%^2zCmXCvYhZ#Y=w<yI=&-Wv!#fnd=>BsyN#9IWCcpuGgg<&2$T$?FnC%z}kWSM7cS<5^BUKOY(j*qM73Bx@}@8l;U;dlRJp5
MjQV2jzv2M!X(DKA|>-dqLpjKjy@B<MpnT5orV2*S><j91M5;jW^rqT$*5^^&>R17@wGix(`nxXwT9K!>0m&avNjU`KK+wcE1tSY;dodM9KP`N+8h$zH}QZ`?;Z>2wg`D}a6|a{TG_*m^~afQ_o`z{f74c!3Z*OU
2u6FFsv}3uU}D4`gvKaTh}%JJSn7Byqiq$TZo38`i`!1zL$hfsU*73N(<gGtMq-`8>3uxv<TKhfCz`1`sCpSCu`wh%MttI^Lc2+vDAp_84_JDRgv?UQ`!@j05oyq2Qg!MI*-N2loVGYQ7(S{r!+OL3;OC_B>vhuf
f>TzpDf*^%vv{6b|Kub{mO}=-+wPTdgW}^*B1i&xB_`&hvgA^<v;vXD6yMKCkLa6yTA%9)zpSOF<G%O(2BLBAPyP4RoP689)Pw{8%duY5FHKNPlxp|Ugn`Ie>LQ;3^`@VX6J6;ctF5AC+!5~VJGw8sc*EECLlflh
;TG+$K5@D}W4?aT>KsrGlbNdOp-KoPPI9y}>9+0wKw{xJ%grT_uKETU$((u{)=AKNA0TGLo4ku5R-iSJw`kSy>ShLL0(##2;xDOpFai(8`H4#Wp?Vb(+SP<_P9f@A=kua1FA34#kLht!25wI7W@nmcq3KL%GH}G1
+|w7i793RZNpzBPk(Lfp9s5<3dSgvzcZ~4V4pOdhj(OPGhtsg(%$335zFhBiul>3);{Rx_ivoyV4)hXb#W6Mk+idC)oO6Yp!v1?tQT5IYFLK)&LcrDExkghX_!=g+DLbEp7EkO3$2ug#MN1?O<>h;FX=nsLR|eQ_
m_E6rO!15nTc*4+ihnNJ*TJ(q35~ZCsnseM==J+sSFi@S4%4FmHFoK47(r&Tkdlwi*%SMr6>*U-)MvxYv%5tR`8QxqRtQWAX#^!$>e=u|=@O_-Y%6_H_<uN~+UL9Ivr6@?2Kt2b>RmKyN=A+HRDMRBjwCg3M#XJH
m&1&y>%%(yT4uC@Zk>dP&N$W&Xg)i5!Bj!jc|!vgbg9g=b%7(7C$TJTr3~oza`L7ir<IfHA9-_i6mza_a02bv_*dBPfei^CU3R$7Tj@%R%t^y~4_8+l<hTvK4b0U7;dvCia!$bpC@gi&@?LWIe5Dx;o3_0xC+%yW
%LUP@y%^Uncu&kaa|(dRQVRDv3c1!3<Ay`j47nhnr4SzlIg!G1jKu_HK_4Et{!DdD95LZ-5KYN^_`+g|!y{71NY<!Yg$;)fx(e0g)`n{G<EY$);<l9sfnPm}J?<BHL@4jSAMAtL$aE>e!$+9aR3t4sqRZ<PIJ6E3
95Eg{#CA5_X0;(OCx%6TjUk+Of#<IPGR+n57r1Qr77PVu*{FRCREsk$L5J;QtYo@Zlr%6`-(hI<u0jn$e6S>7?8<27_@R(m<JcNOA<&K*O5}{N6<F^Q7uM@rERKQA_TX-4KDBMWTd}_JmS^zhiioP=KHmAUq+;(d
`p0<C<r#&3CV!cN1<=#=x^)X|Q>lNdg6Fsa-7iKOE~JIo{L_Fj-A9YSLRcQs*Tn}VGPgzn2j0dPXu9!(GP^-n+;>WOFt-ikW7V-KIW-E~Z_KbtSzc+-UEWoCRY2o?9Ebd=#)vyZvs46j+;JC&HepTFs`=5AeUQH{
nD_5(F{}90bfT#~pK0$FH(n@FENz01C?@L1>j)i|{=bMQ*THV~_sC%#%ciQ$PRiDxw03L3YF(pZ+8!&?i=&zs$%iFdU!QHq(1vyvCN@<0=Z!zTymD`ky78-)8lO0PuJmp;$X52~-$Hm$2??MW2DG_a`AzS7>%FjU
?@^R{ae;k-4?b}r9@%A|Q|&9Es#vY9#^x+%{k{4wY<Qb}UoVx>r{lg7A?UbHXy*NS^>H|tucULGH<|H2%?S<~UpZ64EXa+1l(^Wei}#JhE6)d{Qjg8u67_MGXdD4I-b*6_J>irMrr)(SZH&v&4?R02QBcpE|3_Ou
Kqn1|FQWKc#qCe3)XgJyg!8o1Cw17*A3>Z8P)^^URd+z+9>_t()I@rhRQm-oGZ5v%JI*#b4m0abKBam{ie$i1WK$-kN?iAttWBpeiGSI}(f4orElD4Z01B0FGDv_Xrr4<x9<xhvV)Q>mj3%}6t^xRSGc6sUtK=1|
pNxd;C@nhD#4%mq2Wrl)*nwaUaYfwljzp)Tnm;S!#~9&d2ugBE#-J4Y^6mxm4$^}xq2tC+TVoX^qmgGz-tLPgEYZTetT2NkAHaK?oX|3a#$7H0_}`D<@g^q5!8@z~z|yir`%g|mzAD0FCp}YBHid;b#_dv1HtwVV
42a4K<oC42a*3j1;;q!%UH&sG{SI{}LxOOyb=kw#SD}`teZHsNL5K?(RUo-2BJI~<zu|i(%h4O>hjiZP%2CXb4Cq%i?J?yQ(cvKw{o)d15ulQ-3e4w0qzS^3{4|G=gnm7wuc=@75-(Af>e7f|I!}G6-b|e1L}OrC
whKAg=#}_L*$M}O5GXo3PUPmPQ0-|=A?G7q5i2W~RwWLEq4%CDF=N<p&QTP+-K!iot*id`eEde21aA2BARGl;%_UxwSvQ+@5;3M2e3*+`+$x}jYrO%vU4s6v8yhlG5ls!>vwa-iX!C-{Xkgxz<q3W_Rjv%DQ)PU|
{7}TOAJ2=e>Gg&=Unh8y0`hp{)6|9Lqi_Kt{T#i@!Mu1Rm$&Niwi~A%anp5$KZp#3PZ0Ak`T@ysxs4IZe?i9^)-DW!M>Y3vPLNC8_Xx33*)&%aN6M*>go?TiQ)u*wt6=P@=ABqT;p48aGs1R33&?A4Pr9pm;05Tj
ZfP%S!h|C_7Vb+_MfSsG1aZT=NPhhJ{-(cdUA%Ges_788N#8bst&0Fu#rFE4QtZfPWBTvzS@b#}3jVydI2IBptX=Bk*Y&Y7S~`y_@^J{+1qxPo4fQs>V}bqZ@i%GObRAB~Dh$@zbKUbSq^pXdHBF9kxiMn?Q3U|`
(&tp*eWR!EAJ9oxa83C)nz1A~^M@`E#qa-3Pnm&LNX%`i&o(6f9<e+J*7mKL={9FsJK*TI*L2X;AW7uCYH0twme(1HZOROU&IG;V*TpC3bh04$o!)*zdnp36O1x_|X6;$)ER__2k|<$|RiHVHpqrZBn_~r~1iWNx
r2V3qj5;tL-y`sV86!m2uCZ1jnC=^9DZsG0hyJx!U<XB27020qdxCq}IHzsS<7({L)bvxi1FC-lX(xGFh%|%c-0r@kH)PYgko1kL)EptF{v6xOp(Jc*?|{Dr7%jZ4;tQ7)gIfV%Qh0=xvs5ZxdE64TzRCVH<WIYw
5lf4tHx|a!0fcp48SxErXCxnkiWDq!rQD}mp$hvF$W!N2T(HgU@Q4a;OwxX@Rw|K`IjL;Dup`TT^W|uS#Y7SWrqBIUmLumYu&X269jBACd<5k4Ozd0fsW?vwomeU8ZK#=R$0k8$<@pC6Z?!Ta0%~)f)A}+j5(E0s
tv5K78B_+#TYS|-a;w-d<i|{)LCHw_m{IH=p0XQ0+O<LvWrT`Lc1z8g*l-Q_SW6d&(yTJz&oxT#J@xQgdnd|l;Qw~Qw`^A|;Qz(tk503ef$vc9JPiCy@2AV&3)py`Wr>YV#1E>)QeMCH*fBq3Q3b{0{DI^<e)j?2
DhZ3^*gpxheMxa#%Gpi}ENFXj&|_4?$$StSkHRi+e<juuMUInC;b?NUrcg+06Wca?BV<rj>y$zR3=pL~?G@s1*@e*pyouEVRGBvCYP)+mWLEs0N*IW<8>6qOUXt%L-d|Pr=941Os?j#t<7}tvgE-!aGru<Xa9u)4
O;cwF$qS#(id`p=vI1odn(=m;GqeEbUa?cXAm5(`lBvD;NVYcTSGE73t$sy^c9zO78N&hGK^gTjh0+15;#a38GwNxK%6#YGbCh!>L&D+;9UvyddK?yyR<oi;z#$34)feC1TER`AllEp>?B<IXf3JEfpQ?(R@_MiJ
WL3zBl0m>b$BK)GElvC&-~-B`tC0x2Ku29M0%SR<8ZQsy^0qM|w0g9vQqnXl%p}|Kg*-UILZSJiq4cj?xJc9NQT%Oc<t9p!C7e&;=+Xhfl^09PHn^PT3}F-Brm69!KyoH?P-yW5lcTdlztsXeF<5_DsJQxnvzbFL
bZzY6^nh)|O#1-)mmd(jW6;o|%sycIoU-!HEsF{pGtr>-fxko)zxfwq6iolHQKp6>iF3rL7Qh~)<EVY0O$;fz-Ggzq8)}emzPMtkpM>vYmiu{16T11cDD4{3cC$&s_c<Q&AIi7nuWnSj(aSF}Rx@b0Pwh_h^q+-^
^+#AW@p2p79%G1A$zc8&!BPs3Ed2t>t~)h#T8p!jV>qZCFvJZr%8*IAMDr;4rt5&@Fr&{-neTM=SbcHcz0%&vvb=qXi0n>~sHXRU);Xn<a7xS!dX$|tt7kt2`?iAbBIlo;ag2c|^@ZPvTKiLk<EV^&X^vDAZbjA6
+tYHYE3Upl+A~t))Zz;q-oFX%^+_Dl*lHe3R{V&~>|<skLWu*6-IP~~F4W!8gyo@?@+zXo(FOFOqEC4Tm&af*NXT!pb2nq$Q?Uwkqf4>4zcCd)<pl}tqa<dmUnV^-f&6g+(rps9BzOJpySdx+lf-h#Wh)rhOG3^C
NXp9M%W*WEsT&(?D1@A?2)0t{98dfB3#`6lB$B8{5I7hubJP{DU`G11HJ(!G9UAwec#aqmG}t_RZihSW=-FJU<jzf_MEA`tA}1U#tGq7iwm{FgMqQc}7mtnXP~@gv$Lcn!s4A4s;}l*7zb!~OW5Nd-34M)J>|u}q
UX=BdvyVFzJ9GP^5P28CfFcZXL5S%?{&tOXw6%on&L?f}QRvobaz$co;EV7Y8D4Ji?)5j*^Ct$4VkV{Z{vJ~nBm6fCWd#P2*i@dYKnvt-nGD0Yfjc~5`?+^x9{wH#ar`uq1f`C2DUZFvQw4-r1A@r33_jK{b!&}?
6f$ifMOW46popJy45)4G<Rju`D8n%tydM$KUd4g(VFpDmM7t_)Fsap_qsP_arY0-^8IT>avN8(kTkdy0t1b>Ce>KxGJ)QnnA%u>k+!JO%w>wzZEsaz#xKUmD?^3@ZyFMyC0dCMubM``bP7Vta#gz=q4P2-6z|NA6
w344>p+#!`1X|Q)F_7g14^YETbCT!gV;LcVOuzD}C?B0j`3D<TOcyyF<s2%gNF$IBp)+~P;Ug)iNTJZ)b~Og7C)~o;u+YT--A_Wwev#M=y&3Cq@)?^E^gyG(xdTRgEVrvTaf@GafaD0;l*}ju+e8Z5h0l__)NCr<
IzVAH{z<WgcznnU_Gj@o7!UCLT9;MMNIBbEA^(Rh$nyDP53n~n{GAO_@VQUo?3jywI#2F-M^_sf;42`DB9{PoY;0ia(UB(w-!uZI(8_qi6d!rq6pk8NmHmcJ{Mjx#+YD6!tJE#eKK|<LkU%?+7ceZA2S)!6iOHzZ
1__{;U_)O^Y*#-&oAZ}93Hophdk;CzDNtgl1|_4fnX&!R=GhY9oDBRNO+A}#mZ*>No@t||@a2~@C{amli}n%zgG8n;CVOP}k$|PbTihjM?H$>QLCXbt%x%a}XrPjkS7ByumNtPV1l+L7R4|+8hXEPEmL2S)^+!_;
XVSB;#dY0zAC)6Z(=oQNkiH=oclw)X0Ioh)8W`!Za@mISLKLnO%q~k=TVYuAQxO=PaD~=1p=7S1v4w#xfHpnQf)hVpkS5)U-OnBEKybAn8`jYi0nx|lKZjN`C72{(t)5%51nXG58H$#l4F=izT8M(JYwg}I2=g7>
F3^|M3D_?|=lo?+CO`e9wXl$g-rbXkVbbxtJV~2o6=2*O)xUE%Yv;&)j<gTdSGyT{2tU-n7ZlC@ZHsgY)At1uLOoYszl+kxF?)jI`I`54aU`ds8f6nEur#js6@u=fb+t#ZDc^;fr~{@*A*4!2$_dgBMV4j}FghMi
Fj~hpgdQb|J$Ca4d(3b_N3_!oO{2t;kL;;;%BQ<bQ{3M#c-IOm1WfF7hX&y@EMs6gt7}qHh(#M#xnhBP+9ebVhSLx#^S~GaY}YzJ8}lmP*2@m<`soKy`H!h#X>KVKH*4W(P*Ell8?MDlJcMzm?jhN+l=eR^fREI4
@XDaFT=7C(mKJ}Qx*X=)Xod21-X1tGcucqNzv}PX2TGEg_fqm|bxZ)ZpA`S=(a^C1ic8Xy;#}b#2teD7FSlUUz;f3LEl(I34msG>_0e>U4l;=?I(-1Rqg&oa>5J&&<g?e*V!$Ez#cy*~*9B_7ML+^r0|U&MQN68N
+CV^tPok%H5+CaBCUny6UomUNckP(8tjredvo|7%m8o<OV!nMu1wgbA-qv4|-|me;7Cg}D`a6E7e9PZ7b~uc_ZC(uCr3BM5NB)UriTqEyJyHtQtQ<)49`Z{sVydr^$F3uGzO!Xe+j(NYDN}&1b_B*Hdff@kBIe4^
fAG+|N=u`UsOn=Y@GFB}@w2wM<-+PVALJUoZ%k=-j1Er50rq*vS-Fab*Hs=|ULakh((?z5^Izu;m$b(>ibK?dj##NCKx|J3MPH)H4KqT>=l+RT!J<Bd%Hey)IiVR<$NRlk`=&^k$a7aB$<H|WSg|%D>qZJQ)ED%h
6@-<Bzb{v(vBeS&3G{da167Z}9{(y1Z#zwRfR&(4muPs|bC3lf{>s=0hOxYXe8~g~l-p3Gq0Vv6%)dtaRhIwIY;dBJN@8>`7PJyztqvkCW?WAm=v`WvotYy!-DSodc|sZG5uis;)(45IZ`O>9y0WB3rXP7{VxSCP
Uc$QaB;<C*fGP~9-tf!3ed^V_A>(;bu<y(DWRBHxOF^k}Ic(BUZ+23Aa&i}^bf*l<7JP@v@<Lu^s3q&^TKA7_2fTn8h2pYIB548$)^kw%#cYVATc~LM;zW*8v;s67cLlUNR(EA+$sRAE33(Vj!j<O#e&8Cd4-d7+
dZDcI_@kcA?g!My6dC9|KO+fXic|>zh;Y~3ZQvp<nEWJl?;G3g|Ce{H!Fm^7l^*q@*8Sbycv>Va+1J|ErB0dQm4@bP60RCf<+15L4PU2t<nW`HW4Eu+WQWaps>dUj^N8sV;{u2*!|jC~^JI~#Rkpv3jy;oirDv5#
uzc^4ir9bbzdd|cX)ko#{MbHxwzp4Ivl8CqnNyz-j=3#xU8?LDiC;+zJxheja`4Dsw>%!X27pRuxBhttrDT0|Zm8o!MJ!(L3fx99VsAA_SAO}6D59cl#foiLc6hE#rFXZ4v6!o=ed;Z&z#kEF+tM&{1(waweg?Q6
)a~wQwKwVKy6bJicI;=!2Z-sqcuh!V(qu8&YF9l$ZKIjpt6i1^Uff)$?7QR6dKkAvf=%YXL5U|nCUccgJ2uPmk8kK^a5L3Io0g^79gHtX9jeR68lomBVWW5am!pTsv+%jpqR=6WZ0^DvSbkg_;S~~7z>_s>no1x|
b7b29CYObp;@ad>PV?@i{L$^1gZiH*R*VUEu5YNI$+JSlQIu)w{9*}UU<VrIxDU@njnA_n6<;mnz6y+{@*6*2Kds58pEJSuirUs6u5;x#|Ig$_mMb4u{3X1wO(0oR35dLkO4~TQ#Xjv9ntnVI3u-VLu0ig0PN_m=
6?VU+8EG=Td?=_;fT_{=X0QI;<|Bha3SnU)M5fvxHnq$N=gO|E&9fswa-8n$<XFL1fz#q-G6%a9+Tr@G^pka~(8L&DJu`oOc4k4GbRZ<hx%4T7c;B#FWJ_wHVNuzc)mMWy5De&MwgG>uUA?Psjx}~~@CzKLPJHi2
O1=jmW%J^+G>N%~^#fa!){CdZJnc43;KbhZ2wav@-Y!@3Esk%f9c&d|Y|TW#P@bfdY)p`}9uqg#Kg7X6b$4sCl7|^Ou}mIMx)aY$%Jw#f&B!VTvz%r=*NkcKZTgzIudcM8C=;l}>?MBz;(Vp+RmI@K0P4?WvR>2h
^m#~z0Hy0;?o2{hrwzFlByYr&I+_s>3+GidHx4`ELr`0H8y14cWGx6cUptV2<57S(>@Ix(+7`WDA}hO)ln`3mE^K0jL5d!%41(*9Tukwt6<%+1ITx~3EuY3g2t|y*<<hPsFFO+8l9?44QnJ=2Y&v6Nl43hFlW7sO
she!1UE|k#1CboPX+By=8o~R-*6%@KU~83CN!9bVx<*AjhK^SIwDoQ2BdJiB1&YiPeN3=`OXPcJ?Ja`6BLvD%1K-BTo=AN-JJ6t$%wy9GWkoQasypNtKcT~9?}!617hB;`@|m|M*6e$S1to|5-cKxbAxU0|r>50r
$U~iZC#G4M@V+vjo*QM`r+8UsPs-kg=s*m45N8<*pbx%wdgG(Yq{e!o5f@L2n=~rw5%@0(AnCuRnId0CuuKshH}~z-vKwS-peutJziSZb9&r`Mp%py1ac!j{PMz>l6;M(&7NmXtJLi`Jr6Aodo>f-A;1Wttoy-)@
;TwZcO<R*L9uB*B6H4xe4s!dyGdke`IyQ;XPZ(@m+=#AJySH6E5nJ7|i`&I#EkH!P*h97N{IS(zaGU!+g_9^zT$`KAPhJraE_Z>zj4@n7K<99;5{0<5Il;u2`21DH)j$l64Hj7)tx#c@N+{=M?5}`dccZDl`CNFx
{MmR5Y1xL|&0t)OS=8+v<OteDJ2Sbh`=Y%O(BePa9l<hMwe`7HtQqDpAP|x`$RU5V83tW=kH&c2+3%*T$g*Z7o<TI4*AEJkOOY5Nd0=`+GaUDsU)PYa&Rvibt|ljdJ18HY2rT01qivFH%Hlu)RA})Rh;8d+=(5t-
yu3ke7cB!Y*I?M*HX*5@NRbt}O)?v4A43+^m={Cn?WXOz2-N)YitzgC0hZAAnx4jUH6<FBU5%`!*w3M0)53X_j2{)@OC51Tbc{uS$c}941f4;Ky0E&Zf9(1!Dyrh}?b}<G$ws10$Hq;MC62K&vB79195GZI56Zx>
h8)`~HL`Ao02XP7j#(lnh9<(oz3GzYxRNUMrMG$3)%4XjU|9BvQjOb5yfU27H6nk9Cg5)XCtz2eahPc<PW5$8yYi>X%zMVFwyMN3gocg>VamRkl}6+GaGAAJ+RBaR=-YyEHbE52PXK74AwW9^rnC|}vlAXj1K!^B
JaY4=+9{cUMY|1uy*6BBk{&i8(MrPYGU-9zn4AkNcExp~)ZMrDeAks?mq!L;$NMV)B6bH$D23@LK5jgm(v1e#`%@=uBY0x2WN1_d(tr1j_UyMxq=LMj<;H`V)3?z4l3P;^)7Djk=RzuX$R7kgM3L_L0HhFhrlrm>
`e}*LK`NiQ{5}8x8{DM9;lr&v00D>k0lxADj(hmyvBYQl0ssI200dcD'''
raw=lzma.decompress(base64.b85decode(''.join(DATA.split())))
assert len(raw)==96574
assert hashlib.sha256(raw).hexdigest()=='b19d77888bde0f3fa1930e627f32f8e2413f73221108de74925621237f062cc4'
files=json.loads(raw);assert len(files)==28
root=Path('RA41_RECOVERED');root.mkdir(exist_ok=True)
for name,source in files.items():
 p=Path(name);assert not p.is_absolute()and '..'not in p.parts
 q=root/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(source.encode())
for name,r in json.loads(files['SOURCE_MANIFEST.json']).items():
 b=(root/name).read_bytes()
 assert len(b)==r['bytes']and hashlib.sha256(b).hexdigest()==r['sha256']
print('RA41_SOURCE_CAPSULE_READY',28,96574,'b19d77888bde0f3fa1930e627f32f8e2413f73221108de74925621237f062cc4')
```

**Scientific endpoint:** four durable exact non-target constructions; a complete, complexity-admissible fixed-core apex ray excluded by strict unstable witnesses; an exact constant-body contraction interval; and a rigorously scoped frozen-witness obstruction. The joint finite junction/interface-plus-bulk cancellation problem remains unresolved by these experiments.
