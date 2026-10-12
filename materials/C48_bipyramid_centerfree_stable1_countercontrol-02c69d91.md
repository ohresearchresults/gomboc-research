# material-02c69d917f7d

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Exact countercontrol: an ordinary bipyramid can have one strict stable facet at an arbitrary interior reference point

Purpose: this closes a tempting but false proof route. It does **not** concern the uniformly filled centroid. It proves that no center-free theorem of the form "every ordinary bipyramid has at least two stable facets about every interior point" can be used for the C48 branch.

Work in the polar prism Q. Let the four vertices of the near base be
A0=(1,1,1), A1=(-1,1,1), A2=(-1,-1,1), A3=(1,-1,1).
Let tau=(99/10, 99/70, 11/10, 33/10) and Bi=tau_i Ai. The four B_i lie in the plane
(-3/5)x+(-1/5)y+z=99/50,
because the corresponding denominators on the A_i are (1/5,7/5,9/5,3/5).
Thus Q=conv(A0..A3,B0..B3) is an ordinary quadrilateral prism/frustum: its four lateral edges AiBi are concurrent at the origin and its side faces are planar quadrilaterals.

Take the reference point
g=(-41/50,-13/25,51/50).
It is strictly interior to Q: z=51/50>1, |x|=41/50<51/50, |y|=13/25<51/50, and
(-3/5)g_x+(-1/5)g_y+g_z = 202/125 < 99/50.

For a vertex v of Q, strict instability about g is equivalent to
(v-g)·(w-v)<0
for each of its three adjacent vertices w. In cyclic order, the exact outgoing-dot triples are:

A0: (-76/25,-91/25,7387/250)
A1: (-9/25,-76/25,87/125)
A2: (-24/25,-9/25,8/125)
A3: (-91/25,-24/25,1311/250)

B0: (-33363/125,-498861/1750,-133589/500)
B1: (159687/12250,-31691/6125,-29667/24500)
B2: (-1177/875,11/50,-47/500)
B3: (-1463/50,693/125,-10557/500).

Hence B0 is the **unique** strict unstable vertex of Q; every other vertex has at least one strictly positive escape. There are no zero signs in this vertex test.

Translate by g and polarize:
K=(Q-g)^∘.
Since Q is a prism, K is an ordinary quadrilateral bipyramid. Polarity about the reference origin exchanges strict stable facets of K with strict unstable vertices of Q, so K has exactly **one** strict stable facet about that reference origin. The reference origin is not asserted to be the filled-volume centroid of K.

Therefore the observed S>=2 behavior in own-centroid bipyramid experiments, if it is a theorem at all, must use the homogeneous-centroid/Santaló condition. Prism combinatorics, lateral-edge concurrence, or arbitrary interiority alone are insufficient.

All numbers above are literal rationals and the sign verification is direct integer/rational arithmetic; no floating-point computation is part of the claim.
