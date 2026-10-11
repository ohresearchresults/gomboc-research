# material-d73ac86644ab

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Exact countercontrol: an ordinary bipyramid can have one strict unstable vertex at an arbitrary interior reference point

Purpose: this refutes the open center-free hypothesis “every ordinary bipyramid has at least two unstable vertices”. It does **not** use the uniformly filled centroid and does not produce a homogeneous Gömböc.

Take the square base in z=0:
b0=(1,1,0), b1=(-1,1,0), b2=(-1,-1,0), b3=(1,-1,0).

Take apices
T=(531/1000,1511/1000,17/125),
B=(33/500,-1477/1000,-27/200).

The apex segment crosses z=0 at
I=(80661/271000,3113/271000,0),
strictly inside the square, so conv(T,B,b0,b1,b2,b3) is an ordinary quadrilateral bipyramid.

Choose p=(-99/100,-99/100,0), strictly inside the base, and the reference point
g=(3/5)p+(2/5)B
 =(-1419/2500,-1481/1250,-27/500).
Because both coefficients are positive and p is in the relative interior of the base, g is strictly inside the bottom pyramid and hence strictly inside the bipyramid.

For a vertex v, strict instability about g is equivalent to
(v-g)·(w-v)<0
for every adjacent vertex w.

Order the vertices as T,B,b0,b1,b2,b3. The exact outgoing-dot lists, with each row ordered by its natural adjacent vertices, are:

T -> b0,b1,b2,b3:
[-277547/312500,
 -241043/78125,
 -2649047/312500,
 -981211/156250].

B -> b0,b1,b2,b3:
[-35733/250000,
 -352533/250000,
 -206433/250000,
  110367/250000].

b0 -> T,B,b3,b1:
[971431/2500000,
 -3441589/500000,
 -2731/625,
 -3919/1250].

b1 -> T,B,b0,b2:
[1154431/2500000,
 -2939989/500000,
 -1081/1250,
 -2731/625].

b2 -> T,B,b1,b3:
[-476569/2500000,
 -278189/500000,
 231/625,
 -1081/1250].

b3 -> T,B,b2,b0:
[-659569/2500000,
 -779789/500000,
 -3919/1250,
 231/625].

Thus T has all four outgoing dots strictly negative and is a strict unstable equilibrium. Every other vertex has an explicitly listed strictly positive outgoing dot. There are no zero vertex signs. Therefore **T is the unique strict unstable vertex** at this strict interior reference point.

This exact countercontrol complements material [internal-source-reference], which instead gave an ordinary bipyramid with exactly one strict stable facet at a non-centroid reference point. Together they show that neither S>=2 nor U>=2 follows from ordinary bipyramid/prism combinatorics plus arbitrary interiority alone. Any universal exclusion of the homogeneous C48 own-centroid route must use the filled-centroid condition or a stronger coupled S/U/H argument.

No claim is made here about the full strict S/H census of this countercontrol; only the unique-U statement above is promoted, and it is sufficient for the stated proof-boundary purpose.
