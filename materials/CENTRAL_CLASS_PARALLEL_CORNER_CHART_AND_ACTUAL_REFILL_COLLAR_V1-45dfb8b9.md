# material-45dfb8b9580e

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Central classification, parallel corner chart and actual-refill collar

## Evidence boundary
These are coordinator analytical proofs, not a complete exclusion of any E17 incidence. The motivating exact moment parent minimum-0287 (SHA c727d65c5ee2199479e3391cdbc57a4fec7396ce8065950aec4e6175e5e5cf8e) and later mechanical interval source [internal-source-reference] (SHA815cf4234123d317ae260187088725bcbcf5c451318665d11996f3a73e69fa0b) were fully read. The new four- and five-parameter exact computations described below are completed in the current coordinator computation, but their complete source storage was blocked. They are therefore ephemeral / not yet persisted. This mathematical note does NOT replace their exact runnable sources or supply their bytes. A future archived coordinator output containing both complete sources can close that specific gap. No upper bound or canonical construction is advanced:34<=C_min<=622 remains unchanged.

## 1. Complete affine classification of central8/14/8 parents
Every central full-dimensional convex8/14/8 polytope is affinely equivalent to K_d=conv{+/-e1,+/-e2,+/-e3,+/-(1,d,d)},0<d<1.

Proof. A facet contains at most one vertex from each of the four antipodal pairs. Thus all facets are triangles or quadrilaterals. Their total numbers satisfy f3+f4=8 and3f3+4f4=28, giving four of each and two opposite quadrilateral pairs. Three vertices of one quadrilateral are linearly independent because their plane avoids the centre. Its fourth vertex has a two-against-two Radon partition. Flipping the sign of the basis vector having negative coefficient gives v=(a,b,c)>0 and the support equation a+b-c=1. Any other quadrilateral, after central inversion, contains v and has normal epsilon in{+1,-1}^3 with epsilon.v=1. Positivity and the first equation leave only (++-),(+-+),(-++). One of the latter two must occur; subtraction gives, up to permutation, a=1,b=c=t. At t=1 the body is a parallelotope with six facets, not eight. If t>1 use the basis(-e3,-e1,v); the remaining e2 has coordinates(1,1/t,1/t). Hence d=min(t,1/t) is in(0,1).

The four simple vertices are +/-e1 and +/-(1,d,d). The linear map e1->(1,d,d),e2->-e2,e3->-e3 swaps the two positive representatives and preserves the hull. Together with central inversion it is transitive on the four simple vertices. Consequently every genuine single-simple-vertex truncation of every such central parent is represented by cutting A=-e1 at fractions a,b,c in(0,1) toward e2,e3,-(1,d,d), independently.

The ten vertices, in labels0..9, are
(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1),(-1,-d,-d),(1,d,d),(a-1,a,0),(b-1,0,b),(-1,-dc,-dc).
Their outward true maximal cycles are
(2,3,5,9,7),(2,7,8,4),(1,4,8,9,5),(0,1,3),(0,3,2,6),(0,6,4,1),(1,5,3),(2,4,6),(7,9,8).
They have17 true edges and16 positive fan tetrahedra. Put z=abc,D=4+2d-dz. The actual remaining volume and centroid are
Vol=D/3, g=dz(4-a-b,dc-a,dc-b)/(4D).
Indeed the removed tetrahedron has determinant2dabc and centroid(-1+(a+b)/4,(a-dc)/4,(b-dc)/4). The old interval is exactly d=1/2,a=b=t/2,c=t; this recovers Vol=(40-t^3)/24 and g=(t^3(4-t)/(4(40-t^3)),0,0).

## 2. Genuine noncentral seven-parameter extension
Let0<r<1, |p|<1-r, |k|<r, |q|<1 and0<a,b,c<1. On |x|+|y|<=1 define m=k|x| and w=1+px+qy-r|x|. The parent is m-w<=z<=m+w. Its width is positive; its upper graph is concave and lower graph convex. It has four quadrilateral side facets and two triangular facets on each cap, so8/14/8. Parallel rails and a parallelogram transverse base are real restrictions; this is not every realization of the incidence.

Put h=1-p-r,hplus=1+p-r,A=(-1,0,k+h). Retain
X0=(1,0,k-hplus),X1=(0,-1,-1+q),X2=(0,1,1+q),X3=(0,1,-1-q),X4=(0,-1,1-q),X5=(-1,0,k-h),X6=(1,0,k+hplus).
Let E1=X2-A,E2=X4-A,E3=X5-A, and X7=A+aE1,X8=A+bE2,X9=A+cE3. The same nine cycles above are the true maximal cycles. The eight old support normals, offset1 in cycle order, are
(-1,1,0),(-p+k-r,-q,1),(-1,-1,0),(-p+k+r,-q,-1),(1,1,0),(1,-1,0),(-p-k-r,-q,-1),(-p-k+r,-q,1).
The new cut normal is (X9-X7) cross(X8-X7), its offset is its dot product with X7, and its z component is2ab>0. The origin stays strictly inside: its E1,E2,E3 coordinates based at A are(1/2,1/2,1/(2h)), so its cut-plane sum1/(2a)+1/(2b)+1/(2hc)>1.

Direct diamond integration gives parent Vol=4(3-r)/3 and unnormalized first moment (2/3)(p,q,k(2-r)). The cap has volume2habc/3 and centroid c_cap=A+(aE1+bE2+cE3)/4. Thus with R=6-2r-habc,
Vol(P)=2R/3,
g_P=[(p,q,k(2-r))-habc c_cap]/R.
Equivalently Kvec=4(p,q,k(2-r))-habc(4A+aE1+bE2+cE3), g=Kvec/(4R), D6=4R and J6=Kvec. The noncentral parent moment must not be dropped.

The central family is p=q=k=0,r=1-d under the determinant-two linear map(x,y,z)_new=(x_old,y_old-z_old,y_old+z_old-d*x_old); the cut fractions are unchanged. The full(r,p,k) domain is a tetrahedron with positive barycentric coordinates lambda0=(1-r+p)/2,lambda1=(1-r-p)/2,lambda2=(r+k)/2,lambda3=(r-k)/2. They sum to1, and r=lambda2+lambda3,p=lambda0-lambda1,k=lambda2-lambda3. Hence the seven-parameter domain is exactly a3-simplex times four intervals, not an independent box for r,p,k. Its full mechanical exclusion remains open.

## 3. Completed computations, still awaiting their complete source capsule
For the central four-parameter cube the actual-centred matrices are Qij=-sym((Xi-g)(Xj-Xi)^T). With C_i=4DXi-Kvec, their numerator is -(C_i Eij^T+Eij C_i^T), denominator8D. The integer polynomial2^24*numerator-8D*I has tensor degree(3,3,3,3). A single unsplit domain with2030 positive integer stresses covers all52780 rooted true-edge trees. All519680 coefficient matrices are exactly positive definite by integer Sylvester minors. The weighted-mean gap is>2^-24I. True geometry/moments have157 exact guards and270 positive coefficients. The normal build and a fresh source-only build are byte-identical. Subject to preserving the exact source, this proves U>=2 for every SPD in the whole strict cube, and Section1 extends it to every single-simple-vertex truncation of every central8/14/8 parent.

The noncentral five-parameter subfamily p=k=0 is also completely covered for all r in(0,1),q in(-1,1),a,b,c in(0,1). With u=(q+1)/2 its degree is(3,2,3,3,3). It has6636 integer stresses,15 nodes,8 complete leaves at the eight equal u subintervals,13693 stress uses and10516224 positive coefficient matrices, again covering all52780 rooted systems with weighted-mean gap>2^-24I. Geometry/moments have157 guards and332 positive coefficients. The normal build and exact check have completed; this note does not claim a finished source-only rerun.

A rooted system means all its true outgoing arrows have (Xi-g)^T M(Xj-Xi)>=0. Every nonzero PSD is excluded by the stress. For SPD, a unique strict unstable vertex would supply such a rooted tree: choose a nonnegative outgoing arrow from each other vertex; squared M-norm strictly increases along every chosen arrow, so no directed cycle is possible. Thus U>=2, independently of possible other physical weak equilibria. The boundary of the normalized parameter cube is used for the polynomial certificate but is not declared to consist of genuine ten-vertex bodies.

Source pins, not supplied bytes: central_cut_four.py14250B SHA429e5cd128546506c6f53e01261f50a431f9ab087237ded842a515f2bc73d46e; central full certificate165284B SHA9f3507781e2af15c1043f334661a82fd5017dd75914c937d06698116fb78d826; report454B SHAf8e53c3d57cf174aaef2610324101dd39c10ee6caf5decf01c6c7ecba50b5509. parallel_corner_five.py6653B SHAd3788b56ea04be73e8952e76539066dec156e49dcc9a157755951c15886cdfea depends on that entire central source, not its output. Five-parameter certificate594127B SHA74bc548e3cdcf624febbbf8e75651a72adb2f5f93b1ab7982e6c40f9da611d87; report473B SHAc560f70869adc03b6efa9077b240af103f227b3c081435f7b0a23d64b8f59c91. Exact recovery requires both complete Python sources, the documented versions and commands, not these hashes alone.

## 4. Actual-refill collar and a seven-dimensional tube
This is an analytical consequence of either computed mean-stress gap, conditional on its source preservation. In both reference families every uncentred vertex has norm<=3, the actual centroid has norm<=3, there are16 fan tetrahedra, and six-volume D6>=8. For the five-parameter reference the stronger D6>=16 holds. Use the common conservative bound8 for both.

Let a genuine convex realization of the same labelled lattice have each vertex within Euclidean distance delta of its reference, with delta<=1, and assume the origin remains inside so the same boundary fan has positive tetrahedra. Each determinant changes by at most(27+9+1)delta=37delta, hence |D6'-D6|<=592delta. If delta<=1/148, then D6'>=4. The centroid difference, using the ACTUAL volume formula rather than a frozen centre, is

g'-g=[sum(det'-det)(sum_three_X-4g)]/(4D6') + [sum det' sum_three_deltaX]/(4D6').

The first numerator has norm<=21*592delta, and the second contribution is<=3delta/4. Thus ||g'-g||<778delta. Each centred vertex changes by<779delta, each edge vector by<=2delta, while original centred vertices and edge vectors have norm<=6. Consequently

||Qij'-Qij|| <=(779*6+12+2*779)delta=6244delta<2^13delta.

For delta<=2^-39 this is<2^-26. Every old weighted-mean stress therefore stays>3*2^-26 I>2^-25 I. All rooted systems remain impossible for every nonzero PSD, so the actual uniformly refilled body still has U>=2 for every physical SPD.

For the full seven-parameter chart, compare it with the reference at the SAME r,q,a,b,c and p=k=0. Each vertex differs only in its z coordinate, by at most |p|+|k|; the cut vertices obey the same bound because they are convex combinations with the same cut fractions. The full chart already proves true incidence and origin interior. Therefore the exact seven-dimensional tube

|p|+|k|<=2^-39,
0<r<1, |p|<1-r, |k|<r, |q|<1,0<a,b,c<1

is covered with mean-stress gap>2^-25I. All five base parameters remain unrestricted, including every strict cut depth. This is a narrow genuine-shape tube, not the full seven-parameter exclusion and not a complete E17 graph theorem.
