# material-758d23825fee

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# OCTANT_SPECIAL_HIGH_ENDPOINT_VALUE_V1

Recovery capsule part 2 of 2: analytic proof, scope, exact reconstruction and verification manifest. Part 1 is immutable material [internal-source-reference], named Recovery capsule part 1 of 2 - OCTANT_SPECIAL_HIGH_ENDPOINT_VALUE_V1 source.txt. Its complete UTF-8 contents, without a wrapper, are the self-contained executable source. This two-part capsule does not depend on an originating sandbox. The geometric corollary uses the accepted literal result minimum-0171 (SPECIAL_B_OCTANT_ROOT_REDUCTION_V1), fully read by the coordinator, SHA-256 9b15d20252180b1b48406f3d65ea1211cd57c733e1cfbc3903deb332736ca3df. A descendant using that corollary needs this literal parent, not merely a paraphrase of its incidence types.

## 1. The new result and its boundary

The coordinator proves an exact value bound T <= 3/2 for the actual seven-parameter S5/corner-cut family specified below when c >= a, after normalizing a=1. The proof uses the volume and first moments of one actual uniformly filled body; it does not complete independent moment masses. It applies to S5 and to the actual ordinary-B cuts which realize I5 and its I4 boundary. It does not require stationarity, J, or separate G-sign restrictions within that family.

Using the structural theorem in the literal parent X, this closes the previously open high-endpoint part of the following sector: full joint marked body[private-runtime-path] maximum, a>b>0, c,d>0, true canonical marks, positive root area, G(C)<0<G(D), expanded Fx, true special BD facet, and the whole body in x,y,z>=0. The parent implies c>d, gives exactly S5/I4/I5, and proves T<=203/100 for max(c,d)<=a by the previously accepted J55 low-endpoint value theorem and actual root contraction/endpoint limits. The new high-endpoint result gives T<=3/2 for c>=a. Thus the entire stated positive-octant sector satisfies T<=203/100<51/25, with no inherited J needed. Reflection gives the C/D-exchanged statement.

This is NOT a whole-sector negative-z theorem, a theorem about every proper33 root polygon, a mechanical exclusion of all V10/E17/F9 types, a C>=36 proof, or a new 110 attainer. The global accepted bracket remains 34<=C_min<=622, exact minimum unresolved. E in T=N/(6VE) denotes the ell-volume moment and is not the edge count.

## 2. Exact geometric family

Normalize a=1. Assume 0<b<1, c>=1, d>0, 0<u<v<=2, alpha=1-b, and

Delta = b*c*(v-u) + d*((c-b)*u+b*(1-v+u)) > 0.

The Delta condition is retained: it must not be silently inferred from the other box inequalities. Let

A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
ell(x,y,z)=1+(d-1)x+(c-1)y+(b-1)z,
n(x,y,z)=(1+b+c)x+(1+b+d)y,

U=(0,u,(1+(c-1)u)/alpha),
R=(0,v,(1+(c-1)v)/alpha),
W=( b*c*(v-u)/Delta,
    d*u*((c-b)*v+b)/Delta,
    d*((c-b)*u+b)*(1+(c-1)*v)/(alpha*Delta) ).

All three U,R,W have ell=0. The two special supporting planes are

f_BD=1-x-beta*y-z=0, beta=-(b+(c-1)u)/(alpha*u),
f_CD=1-x-y-kappa*z=0, kappa=alpha*(1-v)/(1+(c-1)v).

W is their intersection with ell=0. Since c>=1 and 0<b<1, beta<0 and kappa<1. All vertex coordinates are nonnegative, and the strict off-face support checks reduce to positive factors. In particular,
f_BD(R)=b*(v-u)/(alpha*u)>0,
f_CD(U)=c*(v-u)/(1+(c-1)v)>0.
The marks A,B,C,D have their indicated positive ell values. Thus P0=conv(A,B,C,D,U,W,R) is the S5 body with maximal facets

Fx=ABURC, Fy=ABD, Fz=ACD, F0=UWR, F_BD=BDWU, F_CD=CDWR.

For t,z in [0,1], define U_t=U+t(R-U), V_z=U+z(W-U). Where the plane through B,U_t,V_z keeps A,C,D and produces the indicated ordinary-B corner cut, let P be the remaining convex body. Its removed part is exactly tetrahedron [B,U,U_t,V_z]. For t,z strictly between 0 and 1 this is I5; t=1 and 0<z<1 is I4; a zero-volume cut gives S5. The certificate below is valid on a larger algebraic parameter box, but only the actual corner cuts are asserted to be convex bodies with these moments. No point outside the actual incidence/support domain is promoted as a polytope.

## 3. Why every high-endpoint S5/I4/I5 from X is covered

In X's mixed sector, c>d. Hence max(c,d)>=a can be normalized to c>=1. The true mark-C support on Fx is

(b+2c)(y-1)-alpha*z <= 0.

On the root plane with x=0 this implies

(1+b+c)y <= 1+b+2c.

Consequently the upper Fx/root vertex R has v<= (1+b+2c)/(1+b+c)<2. For S5 the lower root vertex U and the special planes give the chart directly.

For I4/I5, remove only the ordinary-B supporting plane; do not alter the other planes or the root. Let U_actual be its actual Fx/root endpoint. It lies strictly on the inside of the special BD plane, which at an x=0 root point of ordinate y has value

-[b+((c-1)+alpha*beta)y]/alpha.

Therefore p=(c-1)+alpha*beta<0, and the missing BD/Fx/root corner has ordinate u=-b/p with 0<u<y(U_actual)<=v. The CD/root endpoint R gives kappa=alpha*(1-v)/(1+(c-1)v), so the recovered U lies strictly inside CD. The already present positive W gives the positive denominator Delta. The body after dropping the ordinary plane is exactly the S5 outer body with the same remaining supports; reinstating the plane removes the tetrahedron based on the corner of root triangle UWR. Its two root-edge fractions lie in [0,1]. I4 is exactly the t=1 limit; I5 has t,z interior. This is a facet-incidence argument using the literal X types, not an assertion that deleting an arbitrary facet of an arbitrary body has this effect.

## 4. One-body moments and polynomial gap

Use the positive B-fan tetrahedra

[B,A,C,D], [B,U,W,R], [B,C,D,W], [B,C,W,R].

Their volumes, in that order, are

w0=1/6,
wR=b^2*c*(v-u)^2/(6*alpha*Delta),
w1=d*((c-b)*u+b)*((c-b)*v+b)/(6*alpha*Delta),
w2=b*c*(v-u)*((c-b)*v+b)/(6*alpha*Delta).

Every one is positive on the retained domain. With vertex sums S_i, set V0=sum w_i and J0=sum w_i*S_i/4. These give the actual volume and first moment of P0. Let E0=V0+(d-1,c-1,b-1).J0 and N0=(1+b+c,1+b+d,0).J0.

The removed tetrahedron has

vc=t*z*wR,
Jc=vc*(B+U+U_t+V_z)/4,
Ec=b*vc/4,
Nc=vc*(n(U)+n(U_t)+n(V_z))/4.

Hence V=V0-vc, J=J0-Jc, E=E0-Ec and N=N0-Nc are actual moments of P. In particular V,E>0, since at least the first, third and fourth positive B-fan pieces survive. Integrating ell on the root-based removed tetrahedron gives Ec exactly; no centroid is chosen independently.

Define the exact rational gap

Pgap=48*alpha^2*Delta^2*(9*V*E-N).

Direct symbolic simplification gives a polynomial with 502 nonzero integer terms in b,c,d,u,v,t,z. Its positive-coefficient certificate is constructed as follows. First substitute c=1+C and u=v*F. In variables (b,C,d,F,v,t,z) the resulting polynomial has degree list (5,5,3,4,4,2,2). Then make

b=B/(1+B), c=1+C, d=D,
v=2*R/(1+R), u=2*R*F/((1+R)*(1+F)),
t=T/(1+T), z=Z/(1+Z),

with B,C,D,F,R,T,Z>=0, clearing the denominators in b,F,v,t,z with their listed degrees. Do NOT divide by a factor whose sign is merely guessed: all cleared factors are powers of 1+nonnegative_variable, and the original multiplier uses Delta^2 and alpha^2.

The transformed polynomial has exactly 12,258 nonzero integer coefficients, all strictly positive; the smallest is 1. The omitted coefficients are zero. The exact complete coefficient array is generated by part 1. Nonnegativity holds throughout the nonnegative orthant; continuity gives the closed parameter boundaries v=2, t=1 and z=1 when the actual body remains nondegenerate. Therefore Pgap>=0 and 9VE-N>=0, proving T=N/(6VE)<=3/2.

This is an exact rational symbolic certificate, not a numerical grid, optimization output, or independent formal theorem-prover kernel verification. The coordinator derived and executed it. The symbolic identity plus the explicit coefficient sign check are the computational part of the proof; geometric applicability is Sections 2-3.

## 5. Controls and sharp geometric limit

The source constructs actual rational controls with
b=1/5,c=6/5,d=1/100,u=5/11,v=35/41
and respectively (t,z)=(0,0),(1/2,1/2),(1,1/2). Their actual (V_vertices,E_edges,F_facets) are (7,11,6),(8,13,7),(7,12,7). Exact supporting planes/facets/edges, Euler identity, positive fans from both A and B, and the same V,J are checked. It computes their own centroid g=J/V and own field G=n-N/V-(N/E)ell. Each has G(C)<0<G(D), but at least one auxiliary root G is negative; they are NONstationary controls and have no claimed mechanical 110 classification.

Their exact traces in S5,I5,I4 order are
464037448787/474626428445,
922100655949/938996292640,
457543754162/464379989195.

The bound 3/2 is sharp for this geometric family in the limiting S5 path
b=d=u=e, c=1, v=2e, t=z=0, 0<e<1/4.
The exact trace is

(e-1)*(8*e^6-32*e^5+44*e^4-6*e^3+16*e^2-45*e-27)
/((2*e^3-6*e^2+4*e+3)*(4*e^4-9*e^3+5*e+6)),

which tends to 3/2 as e decreases to zero. This is a degenerating geometric limit, not a stationary maximum or a 110 attainer. The report contains every coordinate, facet, edge and moment of the finite controls; the generator reconstructs it without external data.

## 6. Exact reconstruction and verification

Use CPython 3.13.5 and SymPy 1.14.0, assertions enabled (no python -O). There are no external inputs, seeds, numerical tolerances, randomness, or omitted helpers. Save the exact raw text of part 1 as octant_special_high_endpoint_v1.py in an empty writable directory. The stored source includes a harmless overwritten initial tetra-list assignment; the following four-tetra assignment is the executed list. This exact stored source, not just a pre-storage variant, was run successfully, and its three outputs compared byte-for-byte with the prior source-only cold reconstruction.

Reconstruction command:

    python octant_special_high_endpoint_v1.py > octant_special_high_endpoint_v1.out

Verification command:

    sha256sum octant_special_high_endpoint_v1.py octant_special_high_endpoint_v1.coefficients.json octant_special_high_endpoint_v1.report.json octant_special_high_endpoint_v1.out
    wc -c octant_special_high_endpoint_v1.py octant_special_high_endpoint_v1.coefficients.json octant_special_high_endpoint_v1.report.json octant_special_high_endpoint_v1.out

Expected files, byte counts and SHA-256:

- octant_special_high_endpoint_v1.py: 9478 bytes; c10e8c06deef6b4bcea07b0b40e6583fadfb8faae368704036c071fded018980.
- octant_special_high_endpoint_v1.coefficients.json: 295093 bytes; 74809c61e0d1100cb3afbcc6da011d0206a39e795e4afec364c3712a351814d9.
- octant_special_high_endpoint_v1.report.json: 3865 bytes; e520d410d0629c3b124b7172d72f9e81cbbbe3f613f1c21787aad76d9d4829c5.
- octant_special_high_endpoint_v1.out: 509 bytes; f494efa6d47ad026de4fa7b6c7d31b8f049a14e495e597dc8ebfd6a87efab801.

Expected terminal output:

    EXACT_ROOT_COORDINATES_AND_SAME_BODY_CORNER_CUT_MOMENTS_PASS
    CLOSED_DOMAIN_HIGH_ENDPOINT_TRACE_LE_3_OVER_2_PASS
    positive_coefficients=12258
    ACTUAL_S5_I5_I4_TWO_POSITIVE_FANS_AND_TRUE_FACETS_PASS
    SHARP_GEOMETRIC_LIMIT_THREE_HALVES_NOT_STATIONARY_CLAIM
    coefficient_bytes=295093
    coefficient_sha256=74809c61e0d1100cb3afbcc6da011d0206a39e795e4afec364c3712a351814d9
    report_bytes=3865
    report_sha256=e520d410d0629c3b124b7172d72f9e81cbbbe3f613f1c21787aad76d9d4829c5
    OCTANT_SPECIAL_HIGH_ENDPOINT_VALUE_V1_RECOVERY_PASS

The pins in this manifest were taken from the actually executed exact stored source. Exploratory/transient summaries are not alternative output identities. A hash alone is not recovery data; part 1 is the complete deterministic recovery unit for every file listed here.
