# material-752a1a3748e8

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Exact material-envelope exclusions and release of protected anchors

## Exact inputs and source identity
The literal JOINT75 body K is the convex hull of the75 D10^7 rows reproduced in fully read accepted result figure-0552, SHA ad8dc7c434c78f9d6a7bbd334969fdbfdab83f3a56202484b2698ad9bf1c95d4. Its six bridge rows A0,...,A5 have denominator10^8. Here global input IDs0,...,74 denote those75 rows in their literal order; IDs75,...,80 denote A0,...,A5. No sorted-hull reindexing is implicit.

Let O=conv(K,A0,...,A5), with true79/231/154. Let J={22,26,30,34,37,41,44,48,49,50,52,54,55,58,59,62,64,68,70}, and W62=conv({P_i:i notin J},A0,...,A5), with true62/180/120. The ambient metric is the given ordinary Euclidean metric and density is uniform. No frozen nominated equilibrium centre is assumed.

## Universal affine-moment lemma
Let W subset L subset O be measurable sets of positive volume and let delta=V_O-V_W. For an affine function ell,

integral_W ell + delta min(0,min_O ell) <= integral_L ell <= integral_W ell + delta max(0,max_O ell).

Proof: optional material L minus W has volume between0 and delta, and its pointwise ell lies between the displayed extrema. This statement requires no guessed centroid of L. Convexity is used below to interpret retained vertices and facets.

For a vertex v of O contained in W and any other vertex w of O, let ell_vw(x)=(v-x) dot (w-v). If every displayed upper bound is strictly negative, then (v-g(L)) dot (w-v)<0 for every w. Thus v-g(L) lies in the interior of the normal cone of O at v; since L subset O and v belongs to L, v is a strict unstable equilibrium of L at its ACTUAL homogeneous centroid. This tests all outer directions, not merely a guessed adjacency in L.

For a maximal facet of O whose whole polygon lies in W, that facet remains exactly the same maximal facet of every intermediate convex L. For outward normal n and each oriented boundary edge a to b, use ell_ab(x)=(n cross (b-a)) dot (x-a). Strictly positive lower bounds for all its boundary edges put the centroid projection in the facet's relative interior, proving strict S for every L.

## First exact exclusion
The integer certificate proves, for every homogeneous convex L with W62 subset L subset O,

U(L)>=14 and S(L)>=4.

The protected U input IDs are [0,1,2,3,6,7,8,51,65,73,74,75,76,77]. The four protected facet vertex sets are {6,14,18}, {51,65,66}, {47,51,65}, {6,63,80}. These are lower bounds, not an asserted exact census of every body in the envelope. Consequently the entire envelope has no own110, at ANY edge budget. This includes arbitrary deletion, relocation within O, or replacement of the19 selected old points while the remaining56 old points and the six route points remain literally contained. It is not merely a local optimization failure.

The exact affine coordinate bounds also show, relative to c=g(K),

(g(L)-c)_y <= -0.1154161949523081...,
(g(L)-c)_z >= 0.028496446131455556... .

These decimals render exact rational inequalities in the output, not tolerance assertions. They follow from relative moment upper_y=-0.20026437801925773... and lower_z=0.04944560044310407..., dividing by V_O=1.7351497170913524... with the appropriate sign. The old centre is excluded by a macroscopic margin, but the equilibrium proof is stronger: it already permits the centre to move.

## A smaller mandatory core
A floating greedy deletion was used only to nominate a smaller sufficient core. The FINAL core and its bounds were then established by the complete integer certificate, without using the floating trajectory.

Define B14=conv(P0,P2,P6,P13,P31,P47,P63,P65,A0,A1,A2,A3,A4,A5), with true14/36/24. For EVERY homogeneous convex L with B14 subset L subset O, the two distinct original points P6 and P65 are both strict unstable equilibria at g(L). Hence this larger envelope also excludes own110. Notably P65 is not the old junior U62: changing old roots by itself does not evade physical mass protection.

Therefore, preserving this six-point route and those EIGHT old anchors inside the unchanged O cannot be repaired by moving any or all of the other67 old points within O, or by adding arbitrary new material points there. A successful continuation must leave this specific envelope: omit at least one of the14 retained anchors, change the route/outer geometry, or change the allowed metric. The original goal does not require this envelope. No claim of a minimum-cardinality core is made; greedy nomination is not exhaustive. Dropping one anchor is not proved sufficient for own110, and the conclusion is not a global nonexistence theorem.

## Exact arithmetic and reproducibility
The complete standalone standard-library Python source is immutable material [internal-source-reference], raw file10342 bytes, SHA d52513d686575ffc61a7752514533ecf6631b6e5947bd0b9cdeb59876b6b3ad8. It includes every coordinate and parameter, enumerates every possible support plane, merges exact equal planes, builds true polygon facets and edges, and integrates volume/first moment at two different references using integers only. It does not depend on SciPy, NumPy, floating topology nominations, the originating sandbox, FULL76, or the older35-file optimizer capsule.

Save the raw source text as exact_material_envelope.py and run:

    python -B -S exact_material_envelope.py --out exact_material_envelope.json

Observed on Python3.13.5, standard library only. Expected terminal markers:

    JOINT75_MATERIAL_ENVELOPE_EXACT_PASS 4 14
    JOINT75_FOURTEEN_ANCHOR_CORE_EXACT_PASS [6, 65]

The reproducible JSON is65719 bytes, SHA15c5a5524e8215ebd404848d63f23e316a7042a7a8805ef6ce566adcae8e93c1. It contains all four exact hulls, exact volume and first-moment numerators, all tested vertex/facet bound extrema and their attaining witnesses, and rational coordinate-moment bounds. This receipt was actually observed.

For the integer formula, coordinates are R_i/D, D=10^8, V_W=V6_W/(6D^3), M_W=Mnum_W/(24D^4). With d=R_w-R_v and delta6=V6_O-V6_W, the U upper-bound numerator over24D^5 is

4 V6_W (R_v dot d) - Mnum_W dot d + 4 delta6 max(0,R_v dot d-min_i R_i dot d).

The analogous S lower-bound numerator uses a=n cross (R_j-R_i):

a dot Mnum_W -4 V6_W(a dot R_i)+4 delta6 min(0,min_l a dot R_l-a dot R_i).

All decisive signs are strict integer comparisons. The preserved source constructs the full proof data, not merely a hash inventory.
