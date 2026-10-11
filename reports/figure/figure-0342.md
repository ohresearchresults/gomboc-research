# figure-0342

Historical AI scientific report · saved 2026-09-08 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Quiet Willow 83 — finite compartment withdrawal, actual mass deficit, and a finite-generation obstruction

## 1. Verdict and acceptance boundary

**No new strict homogeneous own-centred (1,1,0) endpoint is promoted.** In particular, I do not identify a positive residual bar, a one-root certificate at an independently prescribed centre, or a numerically favourable loss with cancellation.

The strongest accepted input remains the corrected **COORD_H166_ROOT15_B023_R12**, with actual (V,E,F)=(316,480,166), strict own-centroid (S,U,H)=(2,1,1), and no weak equilibria. Its defining SHA-256 is `c240a5e8398bd2d4daf70ee6e456dd15af3b8b77141ca2e101d09a18d88e0765`. The journal records both independent exact audits and the whole-boundary check, but records the B023 cold replay as pending at dispatch. I do not upgrade that pending status on the basis of an unobserved terminal receipt. 

This handoff contributes three distinguishable things:

1. A completely specified finite withdrawal of the **19-support minor ball-sublevel component**, including the actual changed filled solid and its substantial ordinary first-moment error.
2. A proved **finite-generation radial-ascent inequality**, with explicit centroid-box certificates proposed for B023. Unlike the immutable parent's first-generation theorem, the inequality permits arbitrary intermediate generations, but its B023 application still has deliberately narrow hypotheses.
3. A standalone exact-arithmetic recovery and verification program, including the complete corrected parent table. It constructs the finite cavity trial, checks the proposed insertion and one-sided-material certificates, and optionally reconstructs the complete maximal-facet/true-edge geometry, ordinary moments, and strict/weak census.

**Verification limitation:** the new numerical cavity census and the proposed B023-specific certificate bounds are not promoted here as newly completed two-auditor results. The exact checking jobs were prepared/launched during the interrupted continuation, but I do not have a final terminal receipt available for those new results in this handoff. The standalone program below is therefore an explicit verification task, not a claim that two independent complete checks and a cold replay have already passed. The general inequality in Section 5 is proved analytically below.

## 2. Source integrity

The immutable parent `figure-0341`, SHA-256 `fac9d6d376e9a11897026a0d8a5e49b30c52507e43401b3eec0406e3b7d0ca71`, was treated as the authority for its audit implementations and its narrowly scoped original-witness theorem. It was not treated as the source of B023 coordinates or as an own110 object.

The B023 journal table contains the already disclosed transcription error in zero-based row 99. The correct row is

`[1319071116910,-112685548427,-1866813004671]`.

The complete table embedded below uses that corrected row. Its canonical compact sorted JSON must be 7336 bytes and must have the defining hash above. The mistakenly printed coordinate `-112685548427427` is never an input to the constructions below. 

For all constructions, an integer table I and denominator D define the **filled physical solid**

`P0 = {x in R^3 : I_i dot x <= D for every retained row i}`.

The normal-point hull is used only to reconstruct this solid. Its centroid is never substituted for the ordinary-volume centroid of P0.

## 3. The finite 19-support withdrawal

### Exact definition

Starting with the corrected B023 table, delete exactly the following original, zero-based support rows:

`C = [12,27,28,29,31,32,36,44,45,72,73,74,79,83,84,119,120,163,164]`.

Keep every other row unchanged, retain D=10^12, and retain density 1. Call the resulting physical intersection **CAVITY147**.

This is a finite containing surgery in the original physical frame:

`P0 subset CAVITY147`.

It removes neither nominal point weights nor a fictitious cap. The changed material is the actual measurable region

`Delta = CAVITY147 \ P0`.

The supplied exact program can independently reconstruct the parent boundary and check that C is the component containing stable support 12 immediately below the unique saddle's squared radius, using exact facet minima and exact true-edge segment minima.

**Important scope correction:** C is the complete minor **ball-sublevel component at that level**, not the complete supporting or escape-forest closure needed for cancellation. That distinction is exposed by the resulting new reference stable facets.

### Numerical diagnostic recovered from the interrupted work

The numerical physical reconstruction of this precisely defined table gave:

| Quantity | CAVITY147 numerical diagnostic |
|---|---:|
| Actual vertices / true edges / maximal facets | 283 / 428 / 147 |
| Own-centroid strict S / U / H | 26 / 63 / 87 |
| Ordinary volume | approximately 0.4915818026898697 |
| Raw centroid x | approximately 0.0005695967912693839 |
| Raw centroid y | approximately -0.0038257091082485647 |
| Raw centroid z | approximately 0.0035498716104596325 |
| Added ordinary volume | approximately 0.0058322873774013 |

The added volume is about 1.20 percent of the parent volume. Its moment is not negligible relative to the mechanical reserves. The raw first moment of CAVITY147 is approximately

`(2.80003e-4, -1.88065e-3, 1.74505e-3)`.

These decimal figures are numerical diagnostics, not reduced rational output receipts. The program below regenerates the exact volume and every first moment as rational numbers.

At the old reference zero, the numerical census had three stable facets and five unstable vertices. The stable support identities, expressed in the **original B023 row numbering**, were

`[3,50,75]`.

Thus deleting the whole minor sublevel component does not leave a single reference stable face. It exposes additional supporting closure through original rows **50 and 75**. Removing only row 12, or treating the 19 withdrawn rows as an isolated replaceable panel, misses that closure.

### Physical moments and translations

Let `(V0,M0,g0)` be the exact parent volume, first moment, and centroid, and `(VC,MC,gC)` those of the raw CAVITY147 intersection. Then

`V(Delta) = VC - V0`,

`M(Delta) = MC - M0`.

In the common frame in which the parent is translated by `-g0`, the added-region moment is

`M(Delta - g0) = MC - M0 - (VC-V0)*g0 = MC - VC*g0`.

The last equality uses the actual identity `M0=V0*g0`.

Separately translating CAVITY147 by `-gC` gives its own-centred homogeneous body, but does **not** prove that its surgery has zero added moment relative to the unchanged centred parent. It also does not preserve the original-frame inclusion statement without applying the same translation to both bodies.

### Edge headroom after the finite withdrawal

The retained common-root-plane rows are

`[0,2,3,41,42,46,49,161,162,165]`.

There are N=147 rows and R=10 protected root-plane rows. The same protected-incidence bound gives

`E <= 3*147 - 10 - 3 = 428`.

Consequently this architecture has **71 edges of potential headroom** below 500, rather than the original 19. In the generic simple-away-from-the-root stratum this would accommodate 23 additional off-plane normals or 35 additional root-plane normals. Those are budget calculations, not existence or equilibrium claims. The actual lattice must be reconstructed after insertion.

## 4. The real mass-carrying side cannot be ignored

There is a particularly useful exact certificate to test for this withdrawal. For each deleted row i, seek retained rows a,b and rational nonnegative coefficients satisfying

`I_i = lambda_a*I_a + lambda_b*I_b - mu*e_y`,

`lambda_a + lambda_b <= 1`,

`mu > 0`.

The complete finite pair search in the program below either emits and checks all 19 identities or raises an assertion. It uses no numerical linear-programming multiplier as proof.

If these identities pass, every point x of CAVITY147 with `x_y >= 0` satisfies every withdrawn inequality, because

`I_i dot x <= D*(lambda_a+lambda_b) - mu*x_y <= D`.

Therefore

`CAVITY147 \ P0 subset {x : x_y < 0}`.

This is an actual material-domain statement, not a Jacobian statement. It implies that every nontrivial containing intermediate

`P0 subset Q subset CAVITY147`

adds strictly negative y first moment at reference zero. If, as the parent exact centroid check indicates, `g0_y >= 0`, the added first moment relative to the parent's own centroid is also strictly negative in y. Such a containing intermediate cannot preserve the old ordinary centroid merely by redistributing additions within that same cavity envelope.

The statement does **not** prohibit an own-centred Gömböc whose centroid moves. It does not prohibit removing material, changing major-side supports, or rebuilding a compensator outside this envelope. It says precisely why a claimed old-centre mass closure needs another real material region.

The P72 actuator in the immutable parent is not available here. Its finite capacity belongs to its specified P72 facets and support cube; neither its polynomial nor its million-unit moment ball transfers to CAVITY147. 

No finite actuator of sufficient capacity on the changed CAVITY147 domain is certified in this handoff.

## 5. A finite-generation insertion obstruction

### General endpoint-angle inequality — proved

Consider a strict radial-ascent chain of nonzero vectors

`v0 -> v1 -> ... -> vk`,

where every arrow satisfies

`v_i dot (v_(i+1)-v_i) > 0`.

Write `r_i=|v_i|`, and let theta_i be the angle between consecutive vectors. Then

`r_i < r_(i+1)*cos(theta_i)`.

In particular each theta_i is less than pi/2 and the radii strictly increase. If Theta is the angle between the endpoints, spherical triangle inequality gives `sum theta_i >= Theta`. Concavity of `log cos` on the relevant interval gives

`r0 < rk * product cos(theta_i) <= rk*cos(Theta/k)^k`.

For a bound k<=L one can pad the list of angles with zeros and apply the same concavity argument with L terms. Hence every chain with at most L arrows satisfies

`r0 < rk*cos(Theta/L)^L`.

This is a finite-generation bound: intermediate vectors are arbitrary, need not belong to old witness balls, and need not follow the old witness forest.

### Application to support insertion at the actual centroid

Keep the original B023 supports unchanged and add at most m new normals, all satisfying `q_z<=1`. Let the actual ordinary-volume centroid of the resulting physical intersection be g. The corresponding centred polar source points are

`p_i(g) = I_i / (D-I_i dot g)`.

Directions of the old points do not depend on g.

Assume the target is strict own110, without weak equilibria, retaining original support 3 as its unique stable facet and the protected apex A=(0,0,1) as its unique unstable vertex. The original point `p_12(g)` lies on the retained polar facet

`(A-g) dot p = 1`.

For the small centroid cubes below, `p_12(g)` cannot be that facet's radial foot: its y/z ratio is incompatible with the direction A-g. It is not the intended unique polar unstable point `p_3(g)`, and a strict own110 target has no polar saddle or weak equilibrium there. Thus it has a positive radial escape.

Follow positive escapes through actual polar vertices until the first other **old** source point is reached. Radii strictly increase, so no point repeats. Before that first old endpoint the path uses at most m new points. It therefore has at most m+1 arrows.

Consequently, if every old endpoint j different from 12 obeys

`|p_j(g)|*cos(angle(I_12,I_j)/L)^L < |p_12(g)|`

throughout a centroid domain, no such target can be obtained with `m<=L-1` inside that domain.

This argument permits old supports to become inactive. The starting point need not remain an exposed polar vertex; its location on the protected polar facet and the absence of additional or weak equilibria provide the initial escape.

### Proposed exact B023 specializations

The numerical screening identified the following useful candidates for exact certification:

- L=10, at most **9** new normals, with `|g|_infinity <= 1/500`.
- L=11, at most **10** new normals, with `|g|_infinity <= 1/2000`.

The standalone program below checks 165 old endpoints at all eight corners for each specialization, using only rational arithmetic. It generates the necessary rational angular bounds by finite integer bisection. It does not call an optimizer or evaluate a floating-point angle.

These B023-specific bounds should be accepted only after the emitted assertions and receipt are observed. I do not claim a completed receipt for them here.

### Exact angular and centroid-box certificates

For each endpoint j the program constructs a rational t with

`t >= cos(Theta/L)`.

It uses the Chebyshev recurrence `T_0=1`, `T_1=t`, `T_(n+1)=2*t*T_n-T_(n-1)`. On the branch `t>cos(pi/L)`, the condition

`T_L(t) >= (I_12 dot I_j)/sqrt((I_12 dot I_12)*(I_j dot I_j))`

implies the required angular bound. The code compares this expression by signed rational squaring, never by an unsigned squaring that loses the sign.

The rational lower branch endpoint `1-4/L^2` is valid for L>=3: it exceeds the Taylor upper bound for cos(3/L), and pi>3.

At each centroid-box corner the code checks

`|I_12|^2*(D-I_j dot g)^2 > |I_j|^2*t^(2L)*(D-I_12 dot g)^2`,

with both denominators positive. Before squaring, this is an affine strict inequality in g with fixed positive square-root coefficients. Positivity at all corners therefore proves positivity throughout the complete cube, not merely at eight sampled centres.

### Scope, including the edge budget

This is not a general E<500 obstruction. It does not cover deleting or moving old normals, a different intended stable facet, leaving the centroid cube, leaving the protected-root support architecture, or using more new normals.

In the unchanged generic stratum where every nonroot physical vertex remains trivalent and all old normals remain active, a root-plane insertion costs two edges and an off-plane insertion costs three. In that stratum the original 19-edge headroom permits at most nine new normals, so the L=10 certificate would exclude that particular finite insertion repair near the old centre.

The upper bound `E<=3N-R-3` must not be reversed into a universal lower bound on the number of edges added. Old support loss and additional nonsimple contacts can change that accounting. The CAVITY147 architecture deliberately leaves the insertion theorem's hypotheses by deleting old supports and creates substantially more headroom.

## 6. Numerical exploration not retained as an accepted endpoint

The finite work was not limited to moving the old bar downward. It included the whole 19-support withdrawal, a finite reversal of the entire minor route with radius changes propagated into dependent normal subtrees, actual-moment-coupled feasibility repair, and global affine-metric changes of the actual centred physical solid.

The minor route used for the finite reversal was

`27 -> 28 -> 72 -> 74 -> 73 -> 29 -> 36 -> 119 -> 120 -> 79 -> 32 -> 163 -> 31 -> 164 -> 12`.

Reversing labels alone is not a geometric construction. The finite proposal propagated the required reductions in normal radii into all affected descendants and reconstructed the new filled physical intersection. It was still only a numerical proposal; its reference-centre escape inequalities did not establish actual homogeneous moment closure.

No final optimizer state from these runs is offered as a new parent in this handoff. In particular, I do not turn a stalled repair into an impossibility theorem.

A numerical implementation issue also needs to be kept out of the evidence: shortest-path repair graphs used extremely small positive costs for already valid escape arrows. Such graphs must be tested with explicitly stored sparse edges rather than assuming dense graph conversion preserves every tiny positive entry. The following regression is sufficient to expose a difference on the installed implementation:

```python
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
M=np.array([[0.,1e-10,1.],[1.,0.,1e-10],[1.,1.,0.]])
print(dijkstra(M,indices=0))
print(dijkstra(csr_matrix(M),indices=0))
```

The early repair stalls are not used as negative geometric evidence without resolving that test. Numerical exploration used Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0. None of those numerical packages is required for the recovery program below.

## 7. Complete standalone recovery and exact checks

Save the following as `qw83_recover.py` and run:

```sh
python -S qw83_recover.py
python -S qw83_recover.py --mechanics
```

Do not use `-O`. The first command reconstructs both defining tables and checks the finite insertion and material-side certificates. The second additionally performs exhaustive exact support-triple reconstruction, maximal polygon reconstruction, ordinary mass integration, strict/weak face and vertex tests, every four-component true-edge test, a second mass integration using a different interior reference and polygon fan, and the exact parent sublevel-component check.

This program is **one complete geometric implementation**, with an independent second mass integration inside it. It is not presented as two independently completed full mechanical audits. Promotion still requires the unchanged independent parent auditors A and B, their full agreement, and an observed fresh cold replay. The definitions and all new certificate logic are nevertheless fully recoverable from this handoff alone.

The program prints actual canonical hashes rather than inventing unobserved output receipts. Reduced rational volumes and all first moments are emitted without truncation.

```python
from fractions import Fraction as F
from itertools import combinations, product
from functools import reduce
from math import gcd
from pathlib import Path
import hashlib, json, sys
sys.set_int_max_str_digits(0)
D=1000000000000
I=[[-1293372543188,2168809884040,1000000000000],[-2358266687961,573268948071,956815273681],[-1812519934768,1683679498820,1000000000000],[369947641527,2879849457949,1000000000000],[-2364610286991,-333181283172,908284150594],[-2300051256799,-603219409694,892071957316],[-1514256330505,-178024685341341,-779282055092]]
# The next assignment replaces the temporary prefix above with the complete
# authoritative table. No prefix coordinate is used in a computation.
I=[[-1293372543188,2168809884040,1000000000000],[-2358266687961,573268948071,956815273681],[-1812519934768,1683679498820,1000000000000],[369947641527,2879849457949,1000000000000],[-2364610286991,-333181283172,908284150594],[-2300051256799,-603219409694,892071957316],[-1514256330505,-178024685341,-779282055092],[-1497260592435,-413706360980,-731680823432],[-2209501099673,-854350248368,875461697533],[-1304850705343,-747747119946,-824764021645],[-2398595754975,-45444408146,925422122620],[-2398347743707,257812665339,941022556620],[720258795951,-2103165937847,1000000000000],[2058255501824,-1122718114729,348476694869],[362878482764,-477632303742,-2079725889428],[536531735061,-402401828762,-2122844334016],[-7419547620,526577345162,-1754311674747],[505863281852,206520045557,-2064868133105],[386028816681,325315675845,-1964909216491],[-27467790661,2031802939065,-264916629811],[-122284946077,1881114527876,-436329530773],[143310073690,457532650877,-1838599551130],[280202229798,385028615299,-1914795299594],[-1956650209610,-1299579034625,853754005575],[-2093938267685,-1086346648204,863762792471],[-1496211847776,212944814002,-786745645564],[-988328753203,-2069692617390,819470015237],[-577774948542,-2193853000354,812431398680],[-469590473438,-2219203755408,820978388100],[-23981640441,-2256473205398,882703201657],[521733898476,-1928609733910,-599234452610],[598997914336,-2138910313266,1000000000000],[455062387133,-2171529184046,1000000000000],[-1799788939101,-1493540264434,844962414861],[-1623064743087,-1668683469199,838426330564],[-2299512404715,799486508142,966155966372],[84513974765,-2249149092020,904434794619],[-1215653633627,-1958455930580,826314140265],[-1428621896896,-1823600406593,832689523359],[1774661793305,-1331361400756,882823049490],[1846399879090,-1293127738059,775740279563],[567625757278,2305451274657,1000000000000],[658956757581,2029787531245,1000000000000],[2015893524572,-1166923604207,456412487047],[1068374783866,-1946097088368,969335691438],[899083571959,-2031328139092,984864366347],[1178543357649,-1305515163367,1000000000000],[1694301745433,-1367422240313,990040796761],[1591344748725,-1493522463272,992122073963],[1159629953874,-978514753654,1000000000000],[1478164001986,-1613729821372,992757098128],[1616396971601,-235072940013,-1620275836465],[352169721999,2825575544421,880591949002],[235813722323,2575396078795,445648400379],[861523560685,55936584373,-2078950690803],[2119696181970,-818300520737,-576955129857],[2151727822595,-878256477789,-350136806525],[2139025238652,-848368756094,-463382919782],[1848173291162,-412356289619,-1336794507501],[2093805637297,-1078590339836,233130052527],[-1199382979053,561777962919,-1053751981801],[-1022618152768,1128534162559,-755127307411],[-1311141084999,754034807105,-779095730592],[-1303906750003,576021537333,-938318783971],[-1400908317013,596582381674,-790929942376],[-1132196832937,-731918028251,-1082136238560],[-1121614809107,-907263399580,-983397205825],[-399808767015,1330188737066,-955895296761],[-984939191056,1067541282317,-872287649196],[-335013280770,1464590874301,-844622618848],[-216616933258,1767282409263,-556742516334],[-279022146741,1626003114636,-696179425397],[-357383375781,-2240081865652,828788717613],[-134358709714,-2258751774204,859395314397],[-243973637179,-2255962741954,834833618061],[-90563620448,-2137735218408,-246530976630],[49687524817,-1941286741010,-813297137017],[-300128008109,-1630669658926,-921179877617],[-682831388122,-1880210709819,-47165464810],[369128469331,-2197516133940,973877156428],[-1979005238095,1462798878800,993521933935],[1910081071255,-1252961608914,669084553121],[1966421148192,-1210877188681,562659250679],[1215787141649,-1842902719507,980454511316],[1352040527950,-1730799533494,990304704771],[1437943960803,-151834130284,-1780481340019],[1530419282433,-193460674342,-1702274226118],[335811931248,2638813906058,585987007880],[337323854391,2767555697953,764395463727],[642988839271,98654142006,-2145205620857],[750346898689,80249446349,-2117405078536],[52288697260,2192736411152,-65612899083],[144488555193,2394609640852,192894519363],[1076203895642,-359690522553,-1957128521677],[819589222207,-398201635341,-2052121482253],[564625783394,-1805024483836,-792027255848],[224580415706,-1939766996509,-781738099605],[62208128976,-2055886633931,-540303352163],[399217476073,-1911446963014,-761209863306],[1319071116910,-112685548427,-1866813004671],[1197493854982,-72671123890,-1943206324517],[2096216976000,-683475117914,-776625065591],[2098765534777,-775927506613,-688447361587],[1343827535555,887699403594,175240599539],[1704962500649,-293186997944,-1523521049249],[1745458218746,-456090760108,-1446885347833],[2066833418425,-620765889079,-888707604885],[-1167909990218,585428201546,-1080231540636],[-808063371236,987453305566,-1082998159688],[-902152778727,1043061679080,-975045434585],[-1136962009966,-622635419750,-1137178248015],[-200478128796,-715313014834,-1708570008315],[-154290143103,-691951087567,-1740709532708],[-1015249246137,-1042535635011,-979941490332],[-837791193928,-1258259529602,-934318966223],[-344037390205,-773665784187,-1599501496093],[-514356444751,-782729495827,-1509289846157],[-1200371599918,178181068605,-1159104783568],[-156393524203,573090293252,-1679660205904],[183317832260,-2236701575243,926216468822],[279407215001,-2220500098854,946381480739],[-2218362256882,1020440060545,976526385943],[-2112971097252,1241955195048,984530696140],[710610087303,1292508505331,-726788078226],[552484500085,1939345273467,-81957891610],[564348884214,2456044375319,691533505096],[2029609108562,-566593917704,-995393447963],[1103593243014,1393825495635,409237827657],[2153759915817,-920698975452,-231334274326],[2150282141612,-958937388712,-111746032333],[889042403734,1837759353263,596257633474],[2119392812286,-1039429400011,120002322596],[2138246424293,-1000211672537,10389865247],[627936060382,2370646594079,807263811567],[-1115082307937,559374341850,-1133805716613],[-705874128263,294809775929,-1512410874455],[-1099348032934,-470814296494,-1228876300137],[-1459319578521,-165713929957,-873380249400],[-1384299101113,-50055227394,-984692824976],[-1312621878222,44062326836,-1068815392756],[-1061429912309,397331540702,-1226106058372],[-1107385793377,232105864962,-1232001900437],[-1036622450398,26560817682,-1320200670714],[-833847605354,162692219638,-1456475040447],[-473110687207,1225277555176,-1028649459128],[-334169857329,777432740726,-1451248354316],[-583380023070,1120244785248,-1079762746916],[-714723753239,1048871465232,-1085222542181],[-438510555783,605859776586,-1530806528311],[1037586259971,1416121411220,-39485806995],[1918270119696,-466885126488,-1223099386910],[1981414218912,-515997005729,-1105359592713],[-828447095035,859595288849,-1157257372893],[-934573403310,-299749858112,-1385183512097],[-1055646075533,-355205452747,-1296131694753],[-1011763940191,-157313144417,-1347639079870],[-585205537878,35334133598,-1619326890884],[-986264605499,629923656834,-1189332508095],[-922168122290,732065813204,-1176236806746],[-644165330432,423800665289,-1505631012444],[-668381546413,595998488919,-1408692650608],[-784388062775,2472375189926,1000000000000],[-1595820151945,1917000696825,1000000000000],[528570135408,-2156150083494,1000000000000],[661526377463,-2121424829736,1000000000000],[914111548065,-1865925940809,1000000000000]]
C=[12,27,28,29,31,32,36,44,45,72,73,74,79,83,84,119,120,163,164]
PARENT_SHA='c240a5e8398bd2d4daf70ee6e456dd15af3b8b77141ca2e101d09a18d88e0765'

def canon(x):
 return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def save(path,x):
 b=canon(x);Path(path).write_bytes(b)
 print(path,len(b),hashlib.sha256(b).hexdigest(),flush=True)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(a,t):return tuple(t*x for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def encoded(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):encoded(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [encoded(v) for v in x]
 return x

def cheb(t,L):
 a,b=F(1),t
 for k in range(2,L+1):a,b=b,2*t*b-a
 return b if L else a

def cosine_ge(T,uw,uu,ww):
 if T>=0:return uw<=0 or T*T*uu*ww>=uw*uw
 return uw<0 and uw*uw>=T*T*uu*ww

def insertion_certificate(L,delta):
 u=I[12];uu=dot(u,u);corners=list(product((-delta,delta),repeat=3))
 den=10**15;base=F(1)-F(4,L*L)
 assert L>=3
 assert F(1)-F(9,2*L*L)+F(81,24*L**4)<base
 start=(base.numerator*den)//base.denominator+1
 rows=[];minimum=F(1)
 for j,w in enumerate(I):
  if j==12:continue
  ww=dot(w,w);uw=dot(u,w)
  ds=[(F(D)-dot(u,g),F(D)-dot(w,g)) for g in corners]
  assert all(a>0 and b>0 for a,b in ds)
  def gaps(t):return [1-F(ww,uu)*t**(2*L)*(a/b)**2 for a,b in ds]
  t=F(1)
  if min(gaps(t))<=0:
   lo,hi=start,den
   while lo<hi:
    mid=(lo+hi)//2
    if cosine_ge(cheb(F(mid,den),L),uw,uu,ww):hi=mid
    else:lo=mid+1
   t=F(lo,den)
  assert base<t<=1
  T=cheb(t,L)
  assert cosine_ge(T,uw,uu,ww)
  gg=gaps(t)
  assert min(gg)>0,(L,str(delta),j)
  minimum=min(minimum,min(gg))
  rows.append({'j':j,'t':t,'T':T,'corner_squared_relative_gaps':gg})
 assert len(rows)==165
 assert abs(u[1])*(1-delta)>abs(u[2])*delta
 return {'L':L,'maximum_new_normals':L-1,'centroid_cube_radius':delta,
         'corner_comparisons':8*len(rows),'minimum_gap':minimum,'rows':rows}

def material_side_certificate():
 keep=[i for i in range(len(I)) if i not in C];rows=[]
 for i in C:
  found=None
  for a,b in combinations(keep,2):
   A,B,w=I[a],I[b],I[i]
   z=A[0]*B[2]-A[2]*B[0]
   if z==0:continue
   la=F(w[0]*B[2]-w[2]*B[0],z)
   lb=F(A[0]*w[2]-A[2]*w[0],z)
   if la<0 or lb<0 or la+lb>1:continue
   mu=la*A[1]+lb*B[1]-w[1]
   if mu<=0:continue
   rhs=sub(add(mul(A,la),mul(B,lb)),(0,mu,0))
   assert rhs==tuple(w)
   found={'deleted':i,'retained':[a,b],'lambda':[la,lb],'mu':mu}
   break
  assert found is not None,('no material-side pair certificate',i)
  rows.append(found)
 return rows

def polygon(ids,X,n):
 drop=max(range(3),key=lambda k:abs(n[k]));axes=[k for k in range(3) if k!=drop]
 ordered=sorted(ids,key=lambda i:(X[i][axes[0]],X[i][axes[1]],i))
 def area(a,b,c):
  u,v=sub(X[b],X[a]),sub(X[c],X[a])
  return u[axes[0]]*v[axes[1]]-u[axes[1]]*v[axes[0]]
 def chain(seq):
  out=[]
  for i in seq:
   while len(out)>=2 and area(out[-2],out[-1],i)<=0:out.pop()
   out.append(i)
  return out
 if len(ordered)<3:return []
 cy=chain(ordered)[:-1]+chain(list(reversed(ordered)))[:-1]
 if len(cy)<3:return []
 if dot(n,cross(sub(X[cy[1]],X[cy[0]]),sub(X[cy[2]],X[cy[0]])))<0:cy.reverse()
 k=cy.index(min(cy));return cy[k:]+cy[:k]

def exact_audit(normals):
 N=len(normals);assert N>=4 and len(set(map(tuple,normals)))==N
 planes={}
 for ia,ib,ic in combinations(range(N),3):
  a,b,c=normals[ia],normals[ib],normals[ic]
  n=cross(sub(b,a),sub(c,a))
  if n==(0,0,0):continue
  h=dot(n,a);pos=neg=False
  for p in normals:
   v=dot(n,p)-h;pos=pos or v>0;neg=neg or v<0
   if pos and neg:break
  if pos and neg:continue
  if pos:n=mul(n,-1);h=-h
  assert h>0,('origin is not strictly inside normal hull',n,h)
  common=reduce(gcd,[abs(x) for x in n]+[abs(h)])
  n=tuple(x//common for x in n);h//=common
  planes[(n,h)]=True
 assert len(planes)>=4
 X=sorted({tuple(F(D*x,h) for x in n) for n,h in planes})
 faces={}
 for i,n in enumerate(normals):
  slacks=[F(D)-dot(n,x) for x in X];assert min(slacks)>=0
  ids=[k for k,v in enumerate(slacks) if v==0]
  cy=polygon(ids,X,n)
  if cy:faces[i]=cy
 edge_faces={};directed={}
 for f,cy in faces.items():
  for a,b in zip(cy,cy[1:]+cy[:1]):
   e=tuple(sorted((a,b)));edge_faces.setdefault(e,[]).append(f)
   directed.setdefault(e,[]).append((a,b))
 assert set(v for cy in faces.values() for v in cy)==set(range(len(X)))
 for e,fs in edge_faces.items():
  assert len(fs)==2
  a,b=directed[e];assert a==b[::-1]
 assert len(X)-len(edge_faces)+len(faces)==2
 adjacency=[set() for x in X]
 for a,b in edge_faces:adjacency[a].add(b);adjacency[b].add(a)
 seen={0};todo=[0]
 while todo:
  for j in adjacency[todo.pop()]-seen:seen.add(j);todo.append(j)
 assert len(seen)==len(X)
 W=F(0);K=[F(0)]*3
 for cy in faces.values():
  for k in range(1,len(cy)-1):
   a,b,c=(X[j] for j in (cy[0],cy[k],cy[k+1]));w=det(a,b,c)
   assert w>0;W+=w
   for j in range(3):K[j]+=w*(a[j]+b[j]+c[j])
 V=W/6;M=tuple(k/24 for k in K);g=tuple(m/V for m in M)
 assert V>0
 # Different reference point and last-vertex fans: independent mass integration.
 r=tuple(sum(x[j] for x in X)/len(X) for j in range(3))
 V2=F(0);M2=[F(0)]*3
 for cy in faces.values():
  zz=cy[-1:]+cy[:-1]
  for k in range(1,len(zz)-1):
   a,b,c=(X[j] for j in (zz[0],zz[k],zz[k+1]))
   v=det(sub(a,r),sub(b,r),sub(c,r))/6;assert v>0;V2+=v
   for j in range(3):M2[j]+=v*(r[j]+a[j]+b[j]+c[j])/4
 assert V2==V and tuple(M2)==M
 assert tuple(M[j]-V*g[j] for j in range(3))==(0,0,0)
 Y=[sub(x,g) for x in X]
 S=[];WS=[];U=[];WU=[];H=[];WH=[]
 zf=[];zv=[];ze=[];face_levels={};edge_levels={};edge_values=[]
 for f,cy in faces.items():
  n=normals[f];foot=add(g,mul(n,(F(D)-dot(n,g))/dot(n,n)))
  vals=[dot(n,cross(sub(X[b],X[a]),sub(foot,X[a]))) for a,b in zip(cy,cy[1:]+cy[:1])]
  for k,v in enumerate(vals):
   if v==0:zf.append([f,k])
  if min(vals)>0:S.append(f)
  elif min(vals)==0:WS.append(f)
  if min(vals)>=0:face_levels[f]=dot(sub(foot,g),sub(foot,g))
  else:face_levels[f]=None
 for i,y in enumerate(Y):
  vals=[dot(y,sub(x,X[i])) for j,x in enumerate(X) if j!=i]
  if max(vals)<0:U.append(i)
  elif max(vals)==0:WU.append(i)
  for j,x in enumerate(X):
   if j!=i and dot(y,sub(x,X[i]))==0:zv.append([i,j])
 for e,fs in sorted(edge_faces.items()):
  i,j=e;a=Y[i];v=sub(X[j],X[i]);vv=dot(v,v)
  t=-dot(a,v)/vv;w=add(a,mul(v,t))
  n,m=(normals[f] for f in fs);nn=dot(n,n);mm=dot(m,m);nm=dot(n,m)
  den=nn*mm-nm*nm;assert den>0
  al=(dot(w,n)*mm-dot(w,m)*nm)/den
  be=(dot(w,m)*nn-dot(w,n)*nm)/den
  vals=[t,1-t,al,be]
  assert add(mul(n,al),mul(m,be))==w
  for k,z in enumerate(vals):
   if z==0:ze.append([i,j,k])
  if min(vals)>0:H.append(list(e))
  elif min(vals)==0:WH.append(list(e))
  edge_values.append({'edge':list(e),'facets':fs,'primitives':vals})
  tc=max(F(0),min(F(1),t));p=add(a,mul(v,tc));edge_levels[e]=dot(p,p)
 for f,cy in faces.items():
  if face_levels[f] is None:
   face_levels[f]=min(edge_levels[tuple(sorted((a,b)))] for a,b in zip(cy,cy[1:]+cy[:1]))
 report={'VEF':[len(X),len(edge_faces),len(faces)],'strict_counts':[len(S),len(U),len(H)],
         'weak_counts':[len(WS),len(WU),len(WH)],'stable_support_rows':S,'unstable_vertices':U,
         'saddle_edges':H,'weak_faces':WS,'weak_vertices':WU,'weak_edges':WH,
         'raw_vertices':X,'maximal_faces':faces,'true_edge_values':edge_values,
         'zero_face_primitives':zf,'zero_vertex_primitives':zv,'zero_edge_primitives':ze,
         'volume':V,'raw_first_moments':M,'raw_centroid':g,'own_first_moments':[F(0)]*3}
 return report,face_levels,edge_levels,edge_faces

def check_component(report,fl,el,ef):
 assert report['strict_counts']==[2,1,1]
 saddle=tuple(report['saddle_edges'][0]);threshold=el[saddle]
 live={f for f,h in fl.items() if h<threshold};adj={f:set() for f in live}
 for e,(a,b) in ef.items():
  if el[e]<threshold:
   assert a in live and b in live
   adj[a].add(b);adj[b].add(a)
 seen={12};todo=[12]
 while todo:
  for j in adj[todo.pop()]-seen:seen.add(j);todo.append(j)
 assert sorted(seen)==C,('different exact component',sorted(seen))
 return {'component':sorted(seen),'saddle_squared_radius':threshold}

def main():
 raw={'D':D,'I':I,'scale':1};b=canon(raw)
 assert len(I)==166 and I[99]==[1319071116910,-112685548427,-1866813004671]
 assert len(b)==7336 and hashlib.sha256(b).hexdigest()==PARENT_SHA
 root=Path('qw83_recovery');root.mkdir(exist_ok=True)
 save(root/'H166B023_R12.json',raw)
 keep=[i for i in range(len(I)) if i not in C]
 cavity={'D':D,'I':[I[i] for i in keep],'scale':1}
 save(root/'CAVITY147.json',cavity)
 save(root/'ORIGINAL_ROW_MAP.json',keep)
 cert={'parent_sha256':PARENT_SHA,'withdrawn_rows':C,
       'material_side':material_side_certificate(),
       'finite_insertion':[insertion_certificate(10,F(1,500)),insertion_certificate(11,F(1,2000))]}
 save(root/'CERTIFICATES.json',encoded(cert))
 print('RATIONAL_CERTIFICATE_ASSERTIONS_PASS',flush=True)
 if '--mechanics' in sys.argv:
  a,fl,el,ef=exact_audit(I)
  component=check_component(a,fl,el,ef)
  c,cf,ce,cc=exact_audit(cavity['I'])
  V0,VC=a['volume'],c['volume'];M0,MC=a['raw_first_moments'],c['raw_first_moments'];g0=a['raw_centroid']
  assert VC>V0
  moment={'added_volume':VC-V0,'added_raw_first_moments':sub(MC,M0),
          'added_first_moments_in_parent_centred_frame':sub(MC,mul(g0,VC)),
          'parent_centroid_y_nonnegative':g0[1]>=0,'component':component}
  save(root/'PARENT_EXACT_SINGLE_IMPLEMENTATION.json',encoded(a))
  save(root/'CAVITY_EXACT_SINGLE_IMPLEMENTATION.json',encoded(c))
  save(root/'ACTUAL_MATERIAL_MOMENTS.json',encoded(moment))
  print('PARENT',a['VEF'],a['strict_counts'],a['weak_counts'],flush=True)
  print('CAVITY',c['VEF'],c['strict_counts'],c['weak_counts'],flush=True)
  print('ONE_GEOMETRY_IMPLEMENTATION_TWO_MASS_INTEGRATIONS_COMPLETE',flush=True)

if __name__=='__main__':main()
```

The temporary seven-row prefix in this source is overwritten before any computation; the canonical-hash assertion applies to the complete subsequent table. It may be deleted without changing any generated definition or certificate. Its presence is not a second parent or a permitted alternative input.

## 8. Most useful continuation

The useful next construction is a **whole closure replacement through original supports 50 and 75, not another isolated deletion of support 12**. CAVITY147 supplies a deterministic finite starting domain with substantially more edge headroom and a measurable, nonzero ordinary-moment deficit. A successful replacement must use that additional room for new contact geometry while simultaneously changing a genuinely opposite-side mass-carrying region or otherwise accounting for the moved actual centroid.

Before treating any of the proposed obstructions as a closed branch, obtain the exact certificate receipts above. Before treating any repaired body as an endpoint, run both unchanged independent full physical audits, inspect all maximal polygons and true mixed edges, account for every weak equilibrium and zero primitive, and observe a fresh source-only cold replay.

**Final status:** a finite, fully specified nonwinning cavity trial and a proved general finite-generation inequality; no new certified own110/E<500, no certified sufficient actuator on the changed cavity domain, and no general impossibility claim.
