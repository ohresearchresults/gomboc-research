# NO575-SHORTCUT897-R — exact homogeneous polyhedral Gömböc

V=897, E=2684, F=1789, C=5368.
Strict own-volume-centred (S,U,H)=(1,1,0); no degenerate equilibria.
This does NOT attain C<1000 and is not a minimality or priority claim.

## The body
Let I_i be the raw integer rows, with D=10^14. Let T be the oriented
triangles. V6=sum det(I_i,I_j,I_k)=855681799493322778657557419455421981804886.
M24=sum det(I_i,I_j,I_k)(I_i+I_j+I_k)=['558840496445428043429906853565356143483254', '0', '0'].
C0=1711363598986645557315114838910843963609772; B0=['279420248222714021714953426782678071741627', '0', '0'];
Q=171136359898664555731511483891084396360977200000000000000.
The body is the FILLED convex hull of (C0*I_i-B0)/Q, at constant density1.
These are rational coordinates; the raw centre is B0/Q, not an adjustable point.
Volume=V6/(6*D^3). All centred first moments are exactly zero.

The stable maximal face is the quadrilateral[0,2,3,1]. Its centred x is
-46926040266069095867180068553646096716230986700933295651/Q.
The only unstable vertex is896, with20true neighbours, on the x-axis at
68141167948879082321657710041845623550185602154109028349/Q.
The remaining1788maximal faces are triangles. Only one diagonal is coplanar.
The stable support is the unique global minimum-distance plane; the apex is the
unique global maximum-radius vertex. All897points are genuine extreme vertices.

## Reproduce
python -S EXACT_BODY.py reconstructed
python -S verify_rational.py reconstructed --allpairs
GOMBOC_AUDIT_DIR=reconstructed python verify_second.py
python -S exact_ascent.py reconstructed

The first checker uses only the standard library and performs1604733exact
maximal-plane/all-point tests, closed oriented sphere topology and all vertex
links, exact convexity, complete maximal contact sets, rank-three normal cones,
exact ordinary-volume moments, and direct four-condition saddle tests.
The second implementation requires NumPy; it independently repeats geometric,
mass, and all-feature mechanical acceptance using distinct code and a different
radial ray. This is software-independent verification within this research,
not external human peer review or proof-assistant formalization.

python REPLAY.py
runs both on a fresh literal reconstruction, verifies the original file manifest,
checks exact translation invariance, and rejects corruptions. No numerical
optimizer, source reconstruction or network access is used for acceptance.

## Construction frontier
An actual-moment-constrained normal flow changes the coordinates and removes
vertices. Nonlinear projection repairs the exclusion and convex-hinge constraints
before rebuilding each numerical hull. Exact integer hull construction and both
complete audits, not the numerical path, determine each accepted endpoint.
Two subsequent path-targeted coordinate deformations shorten the ACTUAL shortest
all-point radial-ascent routes from the stable face:212 on the931-point stage,
201 on the911-point stage,188 on this897-point endpoint. These exact graph counts
are diagnostics of the named fixed bodies, not lower bounds for coordinate changes.
Numerical graph thresholds of10^-12 falsely disconnected paths with smaller but
strictly positive witnesses; exact integer graph tests resolve this.

The physical shape has an r/R ratio of approximately
0.68865917151984.
This is not a manufacturing-tolerance certificate. OBJ vertices are exact finite
raw decimals; the centroid translation is separately defined. A viewer renders
floating-point approximations. OBJ faces are maximal polygons, not a false count
of a triangulated display mesh.
