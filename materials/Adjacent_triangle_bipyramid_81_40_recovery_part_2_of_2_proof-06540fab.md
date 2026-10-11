# material-06540fabf7f3

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# ADJACENT_TRIANGLE_BIPYRAMID_81_40_V1
## Recovery capsule part 2/2 — complete analytic proof and scope

### Theorem
Let h>0 and 0<u<1, and take the genuine triangular bipyramid with raw vertices

A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
E=((1+h)u/2,(1+h)u/2,-h).

Let F0=CDE, F5=ABC and F6=ABD. These local names designate these three particular facets only; this five-vertex, six-facet control is NOT the native nine-facet TREE253 polyhedron. Translate its actual uniform-volume centroid to zero and define its actual facet matrix Lambda in the usual way. Then

**Lambda_05+Lambda_06 < 81/40 < 51/25.**

This proves that the complete two-parameter physical family used in the previous >2 counterexample cannot cross the TREE253 necessary threshold 51/25. It does not prove a bound for arbitrary adjacent triangular facets or for bodies with extra vertices. It does not eliminate a new 17-edge catalogue incidence or change the universal C>=34 bound. In particular, 81/40 is not asserted to be the sharp maximum even within this family.

### Exact physical formula
The segment BE meets the plane z=0 at (u/2,u/2,0), in the relative interior of triangle ACD. Thus the hull is the union of the two tetrahedra ABCD and ACDE along their common face ACD. Their positive volumes are 1/6 and h/6. This also proves the asserted bipyramid combinatorics for every h>0, 0<u<1, including h arbitrarily large.

Uniform tetrahedron integration gives

Z=Vol(P)=(1+h)/6,
c=(1/4+hu/8,1/4+hu/8,(1-h)/4).

A raw supporting equation for F0 is n.x<=1, where

n=(1,1,((1+h)u-1)/h).

Both A and B lie strictly below it, so F0 is genuine. Put a=((1+h)u-1)/h and h0=1-n.c. Substitution gives

h0=(1+h-u)/(4h)>0.

After own-volume centering, q0=n/h0. The area of either F5 or F6 is 1/2; their respective distances from c are cx and cy=cx. Their area centroids in raw coordinates are (0,1/3,1/3) and (1/3,0,1/3). The raw F0 slack of either is (2-a)/3. Therefore, using the actual matrix formula Lambda_0i=A_i h_i (1-q0.c_i)/Z,

t:=Lambda_05+Lambda_06
 = cx(2-a)/(3Z h0)
 = (2+hu)[1+2h-(1+h)u]/[(1+h)(1+h-u)].

This derivation uses actual areas, heights, volumes and centroids, not adjustable coefficients or the centroid of the polar. It agrees with the fully read immutable parent `minimum-0078`, SHA-256 `2a0d3544bfb7f0c3b6366bdda3555bc650eede67a1444d51a2d7207a0079eecd`, and is repeated here so the present bound has no missing physical calculation.

### Exact polynomial positivity
The denominator B=(1+h)(1+h-u) is positive. Write A=(2+hu)[1+2h-(1+h)u]. The required inequality is equivalent to Q=81B-40A>0. Direct expansion gives

Q=a2(u)h^2+b2(u)h+(1-u),
a2(u)=40u^2-80u+81=40(u-1)^2+41>0,
b2(u)=40u^2-41u+2.

The negative of this quadratic's discriminant in h is

H(u)=4a2(u)(1-u)-b2(u)^2
    =-1600u^4+3120u^3-1361u^2-480u+320.

On each interval below, put u=l+(r-l)s with 0<=s<=1. In the Bernstein basis binom(4,i)s^i(1-s)^(4-i), i=0,...,4, H has the following exact coefficients:

[0,1/2]:
(320,260,3439/24,539/8,119/4).

[1/2,3/4]:
(119/4,175/16,163/96,55/32,71/16).

[3/4,49/50]:
(71/16,5551/800,703411/60000,684083/50000,201599/62500).

All coefficients are strictly positive, and the five Bernstein basis functions are nonnegative with sum one. Hence H>0 on the complete interval [0,49/50], not only at sampled points. There the discriminant is negative and a2>0, so Q>0 for every real h.

For 49/50<=u<1, b2(49/50)=59/250>0 and b2'(u)=80u-41>0. Therefore all three terms in Q are nonnegative and a2h^2 is strictly positive for h>0. This covers the remainder of the entire parameter domain and proves t<81/40. Finally

51/25-81/40=3/200>0.

### Retained negative control and honest boundary
At h=1/12, u=2/3, the exact formula gives t=1184/585>2. Thus the older universal claim t<=2 for adjacent triangles remains disproved; the present bound does not retract that counterexample. The absence of values above 51/25 within this two-parameter family is now proved, rather than inferred from numerical maximization near 2.023984. Bodies with additional actual vertices, other root facets or other geometries remain outside the theorem. No conclusion about their maximum, feasibility or mechanics is made.

The quantity Lambda and therefore this statement is affine-invariant when the actual uniformly dense body is transformed and recentered. This observation does not allow unrelated added-vertex families to be identified with this bipyramid.

### Complete recovery and finite verification
Part 1 is the complete standard-library source `[internal-source-reference]`. Save its literal text as `verify_bipyramid_bound.py`, UTF-8/LF, with one final LF.

Source: 3560 bytes, SHA-256
56d0c78a0c5a6e5a3615b5eef5488eb4e06d435750214bd8a8255a9e6985f573.

Command, with assertions enabled:

python -S verify_bipyramid_bound.py > exact_check.log

Expected `bipyramid_bound_report.json`: 787 bytes, SHA-256
11818ba58db5f2cf501f21b3cd2a76fd09ea962dc0b126c05212d5a9b5b8de47.

Expected `exact_check.log`: 254 bytes, SHA-256
1cf6d39a603749b93745196f2bf02e08455958a169752a73f74d85026ce252f8.

Expected transcript:

BIPYRAMID_81_40_POLYNOMIAL_IDENTITY_PASS
BIPYRAMID_81_40_THREE_BERNSTEIN_INTERVALS_PASS
BIPYRAMID_1184_585_NEGATIVE_CONTROL_RETAINED
REPORT 787 11818ba58db5f2cf501f21b3cd2a76fd09ea962dc0b126c05212d5a9b5b8de47
ADJACENT_TRIANGLE_BIPYRAMID_81_40_EXACT_PASS

Observed execution used CPython 3.13.5 and only Python's standard library, no optimizer, network, numerical tolerance or random input. The checker performs the exact bivariate expansion, constructs the exact Bernstein coefficients from ordinary coefficients, independently expands the Bernstein form back to ordinary coefficients, checks every strict sign, and retains the rational >2 control. The continuum conclusion is the analytic discriminant/Bernstein argument above; a successful script is not used as a substitute for that argument. All reconstruction inputs and every parameter are literal in the source and proof; no originating sandbox is required.
