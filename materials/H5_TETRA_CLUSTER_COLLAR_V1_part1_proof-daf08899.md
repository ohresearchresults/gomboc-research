# material-daf08899bf74

AI research material

---

# Recovery capsule part 1/2 — H5_TETRA_CLUSTER_COLLAR_V1

## Theorem and scope
For the literal H5 family below, for all 0<=x,r<=1, p,q>=0, p+q<=1, 511/512<=lambda<=1, every directed rooted spanning tree contains THREE arrows of weight one such that

P=-sum sym(z_i-g,z_j-z_i) > (125/65536)I > I/1024.

Here g is the ACTUAL homogeneous volume centroid. Thus no such tree has all arrow products (z_i-g)^T M(z_j-z_i)>=0 for any nonzero PSD common metric M. For genuine three-dimensional H5 bodies and SPD physical metrics this implies at least two strict unstable vertices, even permitting weak contacts. Degenerate parameter endpoints are included in the matrix theorem, not asserted to retain the genuine face lattice. This proves an all-basal-parameter collar at the opposite taper endpoint from the accepted small-lambda macro. It does NOT exclude all H5 or all V10/E17/F9, does NOT supply attainment, and does NOT change34<=C_min<=622.

## Literal family and true moments
Set s=1-lambda. The ordered basal vertices are
B0=(1/4,0), B1=(1-3x/4,0), B2=(1-p,p), B3=(q,1-q), B4=(0,1-3r/4), B5=(0,1/4), B6=(1/16,1/16).
Put z_i=(s B_i,0) for i0..6; z7=(0,0,1),z8=(lambda,0,1),z9=(0,lambda,1).
Outward facet cycles:
(6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),(9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9).
Let A be the basal area and b_x,b_y its unnormalized planar first moments. Exact formulas are
A=(31-24xp-24rq)/64;
b_x=509/3072-3xp/8+3x^2p/32+xp^2/8-rq^2/8;
b_y=509/3072-3rq/8+3r^2q/32+rq^2/8-xp^2/8.
Set c_x=1-3xp/4,c_y=1-3rq/4. Then
V=A s^2/3+lambda/6;
J_x=s^3 b_x/4+s^2 lambda c_x/24+lambda^2/24;
J_y=s^3 b_y/4+s^2 lambda c_y/24+lambda^2/24;
J_z=A s^2/12+lambda/12+lambda^2/24;
g=J/V.
The Part2 program derives and checks all seven identities as exact sparse multivariate polynomial identities, using shoelace integration and the stated facet triangulations, not sampled bodies. Since B lies in Delta={X,Y>=0,X+Y<=1}, 0<=b_x,b_y<=A<=1/2 and0<=c_x,c_y<=1.

## Lemma1: every rooted four-point tree has a uniform stress
For vectors y0+y1+y2+y3=0 and any tree directed toward a root,
sum_(i->j) y_i dot (y_i-y_j) > (1/8)sum_i ||y_i||^2
unless all y_i vanish. Prove the scalar version componentwise. Relabel the root0, eliminate y0=-y1-y2-y3, let Q be the left-hand quadratic matrix in (y1,y2,y3), and G=I+11^T the matrix on the right without factor1/8. The four rooted-tree isomorphism types have arrows
(1->0,2->0,3->0), (1->0,2->0,3->1), (1->0,2->1,3->1), (1->0,2->1,3->2).
Their matrices8Q-G are
[[14,7,7],[7,14,7],[7,7,14]],
[[14,7,-1],[7,14,3],[-1,3,6]],
[[14,-1,-1],[-1,6,-1],[-1,-1,6]],
[[14,-1,3],[-1,6,-5],[3,-5,6]].
Leading minors are respectively(14,147,1372),(14,147,700),(14,83,476),(14,83,124). Sylvester's criterion proves strict positivity. The code additionally checks all16 labelled unrooted and64 labelled rooted four-point trees.

## Lemma2: quotient selection retains three literal arrows
Partition ANY rooted directed tree into four nonempty clusters. Projecting its root paths shows every cluster reaches the root cluster in the quotient digraph. Reverse breadth-first distances therefore select a quotient arborescence: for each nonroot cluster choose an outgoing quotient arc decreasing its distance by one, retaining one literal original edge. The three selected original arrows form a rooted tree on the four cluster labels. Clusters need not induce connected subtrees. No metric inequalities are used in this lemma. For H5 use clusters{0,...,6},{7},{8},{9}. Exact enumeration of its48790 rooted trees selects260 distinct three-arrow supports and all64 quotient arborescences. These counts are supplementary: the lemma applies to every tree on the complete ten-label graph.

## Lemma3: a uniform quantitative collar
At s=0 the cluster points are a0=(0,0,0),a1=(0,0,1),a2=(1,0,1),a3=(0,1,1), with g0=(1/4,1/4,3/4). Their centered second moment is
S0=[[3/4,-1/4,1/4],[-1/4,3/4,1/4],[1/4,1/4,3/4]]=I-vv^T/4, v=(1,1,-1).
Thus S0>=I/4, and Lemma1 gives every quotient reference stress P0>S0/8>=I/32.
For s<=1/8 write D=6V=1-s+2As^2. The exact centroid formulas imply
g_x-1/4=s[-1+(1+c_x-2A)s+(6b_x-c_x)s^2]/(4D),
g_y-1/4=s[-1+(1+c_y-2A)s+(6b_y-c_y)s^2]/(4D),
g_z-3/4=-s[1+(4A-1)s]/(4D).
Use D>=1-s,0<=1+c-2A<=2,|6b-c|<=3,|4A-1|<=1. This gives
|g_x-1/4|,|g_y-1/4|<=(83/224)s<s/2,
|g_z-3/4|<=(9/28)s<s/2.
Hence ||g-g0||<=sqrt(3)s/2<s. Every literal vertex is within s of its cluster point because B is contained in Delta. Each centered vertex changes by at most2s, and each edge vector by at most2s. Reference centered-vertex norms are at most sqrt(11)/4<1; reference intercluster edge lengths are at most sqrt(2)<3/2. One symmetric outer-product perturbation has operator norm at most
(2s)(3/2)+(1)(2s)+(2s)(2s)=5s+4s^2.
For three arrows, ||P-P0||<=15s+12s^2. At s<=1/512,
P>[1/32-15/512-12/512^2]I=(125/65536)I>I/1024.
Since V>=lambda/6>=511/3072, for H_ij=sym(Vz_i-J,z_j-z_i) the scaled stress -sum H_ij=VP>I/8192. Taking traces against nonzero M>=0 forces a strictly negative sum of the three arrow products. Thus they cannot all be nonnegative.

## Equilibrium implication
For SPD M and distinct neighboring vertices, an arrow product>=0 strictly increases squared radial norm, because its increase equals twice that product plus ||z_j-z_i||_M^2. With just one strict unstable vertex, every other vertex has a nonnegative incident arrow (including a zero arrow at a weak contact). Choosing these arrows yields an acyclic rooted tree ending at the unique unstable vertex, contradicting the theorem. This handles weak contacts without assigning a genuine equilibrium signature to degenerate parameter endpoints.

## Complete recovery manifest
Part2 supplies all runnable source as verify_h5_tetra_collar.py (UTF-8,LF,final newline):10020 bytes,SHA256 c25d5ca3adfb35bca0f1f5f82f41053ef2b91133e63bb0897952733623a3d04a. No external input, seed, solver, nondefault parameter or package is required; Python3.13 standard library and exact fractions.Fraction arithmetic.
Reconstruct by saving the complete Python fence from Part2 under that filename. Run: python3 verify_h5_tetra_collar.py.
Generated h5_tetra_collar_report.json:1612 bytes,SHA25683e0c232fde6e2f1bfdb72086b1a6f630d3e3021ea39f6bc9261a0a098c6d0dd.
Expected terminal lines:
H5_TETRA_CLUSTER_COLLAR_V1 PASS
ROOTED_TREES 48790
THREE_ARROW_SUPPORTS 260
COORDINATE_MARGIN 125/65536
Coordinator exact execution passed: seven symbolic moment identities; four minor lists;64 endpoint rooted trees;48790 H5 rooted-tree lifts; rational perturbation bounds. The continuum theorem is the proof above, not an inference from finite sampling. The accepted small-lambda atlas is a separate worker theorem and was not replayed. Classical background is Almadi et al., On equilibria of tetrahedra, arXiv:2304.06984; the quantitative cluster extension here is proved explicitly, not inferred from that background.
