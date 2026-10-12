# minimum-0223

AI research report · 2026-09-24 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# TWO_CAP_POSITIVE_FUNCTIONAL_WEDGE_ALL_PSD_AND_AFFINE_IDENTIFIABILITY_V1

## 1. Main result: a complete two-direction wedge, not another thin box

For the literal parent family P_epsilon, form the positive-projective image with

```
0<epsilon<=5,
a>=0, b>=0, a+b>0,
c=(0,a-b,7b-1),
P_epsilon,c=conv{Y_i(epsilon)/(1+c.Y_i(epsilon))}.
```

Refill that image uniformly and subtract its **new actual solid volume centroid**. **Every member has at least TWO strict unstable vertices for EVERY SPD physical metric.** This covers every possible unstable root, arbitrary metric conditioning, and all finite weak-arrow walls. All physical members have the unchanged true maximal-facet lattice and (V,E,F)=(10,17,9), of cap-size type(4,7).

Equivalently, in c=(0,beta,gamma), the complete newly certified domain is

```
gamma>=-1,
7beta+gamma+1>=0,
(beta,gamma)!=(0,-1).
```

It includes arbitrarily large positive beta, arbitrarily large negative beta accompanied by gamma>=-1-7beta, and genuinely nonzero gamma with no upper bound. In particular, it closes the **entire maximal admissible line c=(0,beta,-1), beta>0**. The apex is not required to be unstable.

The proof is an executed exact whole-domain certificate after an explicit full-dimensional affine normalization: **4,112 integer stress rows,19,118 nonzero weights,43 closed cells,17,791 row/cell applications,163,268,007 positive-definite Bernstein matrices and489,804,021 positive leading minors**. Every cell covers all43,200 true rooted spanning trees. The stronger conclusion excludes a complete weak true tree for **every nonzero PSD matrix** in the normalized closed chart; it does not interpret a singular arrow count as a physical equilibrium census.

A second, independent result identifies the entire remaining shape freedom: **two members of this full positive-projective family are affinely equivalent, even without prescribed labels, if and only if their epsilon and all three projective parameters agree.** Every member has trivial affine automorphism group. Thus the omitted alpha/beta/gamma sectors cannot be eliminated by declaring them affine copies of the old block or axial family. There is an explicit exact recovery algorithm for these four affine invariants.

A new rational negative-beta control has strict(S,U,H)=222 and physicalweak000 for a whole reciprocal metric pencil L>=1024, with U={1,6} and apex0 NOT unstable. The same body at L=128 is233, not222; this failed smaller threshold is preserved. Seven complete reciprocal control records have all476 true-edge primitives nonzero.

**This is not a whole-orbit exclusion and does not construct U1 or110.** The remaining admissible strip in the alpha=0 plane is identified in section8; alpha!=0 remains genuine additional freedom. No canonical type/count or global minimum bound changes:34<=C_min<=622 remains the accepted interval.

## 2. Reading, authority and settled antecedents

The authoritative parent is `minimum-0219`, SHA-256 `fe20565818ac05c081e8e74a1100e8c91162a3ed09b48755b46a2f09f9424284`, TWO_CAP_TRANSVERSE_PROJECTIVE_BOX_ALL_PSD_U2_V1. Its completed block is

```
0<epsilon<=5,
alpha in[-1/2,1/2], beta in[0,1/4], |gamma|<=2^-75.
```

That theorem remains a working premise, not the subject of a generic replay. Its domain is not an enclosing box for hypothetical U1 members. The new wedge and that block are different sets, neither containing the other.

The new coordinator material `[internal-source-reference]`, FULL_COMPONENT_FIVE_PHYSICAL_WEAK_CONTACTS_V1, was also read completely. It strengthens the singular-disconnected component alternative to at least five genuinely weak-unstable nonroot sources, not merely five zero primitives. Exactly five permit strict-U1 perturbation on the same actual body; this does not imply S1 or110. No new five-contact census is claimed here. The all-PSD/tree proof below eliminates both singular-connected and singular-disconnected feasible components on the wedge without assuming that every SPD component approaches rank two.

The entire updated journal, including its complete literal parent payload and recovery capsule, was read consecutively through EOF. Input pins are

```
research-journal(20260924-023923).md
296979 bytes
845be005a75959cadf66f6ae9d4310f5b50bdb110ed07b2e2e992525c9d5b3a3

FULL_COMPONENT_FIVE_PHYSICAL_WEAK_CONTACTS_V1(1).md
11817 bytes
3d9a495f54852bbaab9d638b687296cb0d01373bf1c0d62f30e1a6d5d57e89d3
```

No missing exact dependency or literal-incidence conflict affects the new result. All projective-boundary and epsilon-to-zero channels remain settled. The present certificate covers actual finite-distance members for the entire stated parameter wedge; it is not another unevaluated boundary collar. No historical open-boundary wording is revived.

## 3. Literal family and the full true lattice

The raw apex is Y0=0. In section z=1 put

```
L=(-1/4,5/4,1), T=(7/2,13/4,1), R=(1/40,27/4,1).
```

For t=(2/5,1/4,3/25,0), in that order,

```
b(t)=L+t(R-L)-epsilon*t*(1-t)*(1,0,0)
```

gives b1,b2,b3,b4. With s0=3/50 set

```
b5=L+s0(T-L)-epsilon*s0*(1-s0)*(0,1,0),
b6=T, b7=R.
```

Intersect their pointed cone with the two true cap halfspaces

```
l7(Y)=z-(2/7)x<=1,
l8(Y)=z+(5/7)x<=1.
```

For i1,...,5 use Yi=bi/l7(bi); for i6,7 use Yi=bi/l8(bi). The last two vertices are the x=0 intersections of[b5,b6] and[b7,b1]. The intersection formula on[p,q] is p-p_x(q-p)/(q_x-p_x).

The unchanged true maximal facets are

```
F0=(0,2,1)       F1=(0,3,2)       F2=(0,4,3)
F3=(0,5,4)       F4=(0,6,8,5)     F5=(0,7,6)
F6=(0,1,9,7)     F7=(1,2,3,4,5,8,9)
F8=(6,7,9,8).
```

The seventeen true edges are

```
01,02,03,04,05,06,07,12,19,23,34,45,58,67,68,79,89.
```

Neither08 nor09 is an edge. Triangle089 is an internal interface. The seven triangles used to integrate the two caps are

```
(1,2,3),(1,3,4),(1,4,5),(1,5,8),(1,8,9),(6,7,9),(6,9,8).
```

Their integration diagonals do not enter the mechanical graph.

For exact polynomial construction use homogeneous representatives Yi=Ui/s_i. For i1,...,7 take Ui=bi and s_i=1+k_i b_ix, where k_i=-2/7 on1,...,5 and k_i=5/7 on6,7. The seam representatives are

```
U8=(0,83/60-7epsilon/125,1), s8=1,
U9=(0,275+432epsilon,44+64epsilon), s9=44+64epsilon.
```

The program checks all35 nonincident section-polygon determinants as exact polynomials on0<epsilon<=5. Only powers of epsilon are removed at the nonphysical merged endpoint; every remaining polynomial has degree at most two and a strictly positive exact endpoint/critical-point minimum. Rays1,...,5 have x<0, rays6,7 have x>0. Thus both caps remain true, and their seam crosses exactly the two designated open sides.

The same exact checks give, for every section ray,

```
136/125<=b_y<=27/4<7,
b_z=1,
k_i b_x>=1/140.
```

In particular y and7z-y are strictly positive on the nonzero source cone, and the entire source body satisfies z<=1.

## 4. The positive-functional wedge and its actual normalization

### 4.1 All actual denominators, including the finite parameter walls

For c=(0,a-b,7b-1),

```
1+c.Y=(1-Y_z)+aY_y+b(7Y_z-Y_y).
```

For a,b>=0 not both zero this is strictly positive at every actual vertex: the last two functionals are positive away from the apex, while the apex denominator is1. By affinity it is positive throughout the body. This proves actual admissibility on the entire wedge, including a=0 and b=0. These walls are physical E17 members, not incidence degenerations. The sole excluded tip a=b=0 makes the seam denominator zero.

A raw support n.Y<=h transforms to(n+h c).Z<=h, with its slack divided by1+c.Y. All signs and contact sets are preserved. Therefore every physical wedge member has exactly the same nine maximal facets and seventeen true edges.

### 4.2 A single full-dimensional closed-cube chart

Put

```
s=a+b>0,
t=s/(1+s) in(0,1),
v=b/s in[0,1],
B_s=diag((1+s)/4,s,4s).
```

Apply B_s to the already projectively transformed, uniformly refilled body. This is an affine change of that new body, not transport of the old density or old centroid.

For a section ray p=(x,y,1), define h_v(p)=(1-v)y+v(7z-y). Its normalized endpoint is

```
d_i=(1-t)k_i x+t h_v(p),
Z_i=(x/4,t y,4t z)/d_i.
```

For a seam representative p=(0,y,z), use

```
Z=(0,y,4z)/h_v(p).
```

The apex stays0. All these denominators are positive on the complete closed cube

```
E=epsilon/5 in[0,1], t in[0,1], v in[0,1].
```

The ray denominators are at least1/140; the seam denominators are also bounded away from zero. The normalized hull stays full-dimensional even at the algebraic endpoint strata. Indeed the homogeneous numerator determinant of the persistent tetrahedron(0,6,9,8) is

```
(7/2)*gap(epsilon),
gap(epsilon)=3212/15+(129724/375)epsilon+(448/125)epsilon^2>0.
```

Every coordinate remains bounded because all numerator polynomials are bounded and all denominators are positive. Thus the normalized actual uniform moments extend continuously to the closed cube. Endpoint label mergers are retained in the polynomial weak-tree system; they are not counted as genuine ten-vertex mechanical examples.

For physical s, the actual volume centroids satisfy

```
g_normalized=B_s g_raw_refilled.
```

A normalized physical M corresponds in the raw projective frame to B_s^T M B_s, and its inverse is B_s^-1 M^-1 B_s^-T. All-SPD coverage is therefore equivalent in the two frames.

### 4.3 Genuine coupled moments and one common arrow scale

Write the normalized vertices as Z_i=U_i/d_i, with U0=0,d0=1. Here U_i,d_i are the normalized polynomial representatives just defined. Set

```
W=product(i=1,...,9) d_i,       W_i=W/d_i,
V_* = sum_T det(U_i,U_j,U_k)*W/(d_i d_j d_k),
J_* = sum_T det(U_i,U_j,U_k)*W/(d_i d_j d_k)
                           *sum(l in T) W_l U_l,
C=4 V_* W.
```

Every division here is an exact polynomial division. The positive apex tetrahedra give

```
6 Vol=V_*/W,
g=J_*/C,
X_i=Z_i-g.
```

This is the newly uniformly filled solid's actual centroid. Both caps use the same volume law and the same moment sum; no cap or vertex masses are independently assigned.

For a true directed edge i->j let

```
n_i=4 V_* W_i U_i-J_*=C X_i,
v_ij=d_i U_j-d_j U_i,
L_ij=n_i v_ij^T+v_ij n_i^T,
A_ij=sym[X_i(X_j-X_i)^T].
```

Then identically

```
L_ij=2 C d_i d_j A_ij.
```

The useful synchronization is

```
K_ij=[W/(d_i d_j)]L_ij=2 C W A_ij.                 (1)
```

The multiplier2CW is **the same positive scalar for every edge**. This eliminates denominator-dependent relative arrow scaling before selecting integer stresses. The subsequent primitive-integer, factorial, gcd and power-of-two normalizations in the source are constant positive rescalings of individual matrices. They do not introduce independent physical metrics or masses. Three exact actual-volume calculations check the resulting positive proportionalities; the identities themselves follow from the displayed polynomial construction.

## 5. Exact continuum and all-root coverage

The source generates all34 directed true-edge matrices in(1), clears only positive rational constants, and converts them to a common tensor-Bernstein degree(18,20,22). There are19*21*23=9177 coefficient matrices per row. An exact inverse transformation reconstructs the full power coefficients in all three variables, including the factorial scale. The regenerated coefficient file matches the frozen coefficient pin; there is no interpolation from selected numerical shapes.

The43 dyadic cells have a full binary prefix tree with85 nodes and maximum depth8. Their depth distribution is

```
depth3:2, depth5:9, depth6:29, depth7:1, depth8:2.
```

Axes split cyclically E,t,v. Every internal prefix has both children, every leaf is terminal, and the dyadic volumes sum exactly1. The cells cover the entire CLOSED cube, including their common walls. There is no infeasible-cell pruning.

There are4,112 frozen nonnegative integer rows with19,118 nonzero weights and maximum weight1,000,000,000. Their support sizes are

```
3:666, 4:1033, 5:1672, 6:566, 7:168, 8:7.
```

For every one of the17,791 assigned row/cell pairs, the matrix polynomial

```
Q=-sum_(i,j) weight_ij Khat_ij
```

has ALL9177 Bernstein coefficient matrices positive definite on that cell. Exact arbitrary-precision integer arithmetic checks all three leading principal minors and two independent3x3 determinant expansions. This yields163,268,007 PD matrices and489,804,021 positive leading minors. Since Bernstein basis values are nonnegative and sum1, Q is pointwise positive definite throughout its assigned closed cell.

The program independently enumerates the4,320 undirected spanning trees of the seventeen-edge graph and matches this count with the exact Matrix-Tree determinant. Orienting toward each of the ten roots produces43,200 distinct true rooted trees. In EACH of the43 cells, every one of these trees contains the directed support of an assigned PD row.

Suppose a nonzero PSD M made every arrow of some tree weak. Its contained row would give

```
tr(M Q)=-sum weight_ij*positive_scale_ij*D_ij(M)<=0.
```

But Q is PD and M is nonzero PSD, so tr(M Q)>0. This contradiction excludes the complete weak rooted system, even at singular metrics and collapsed endpoint labels. It does not infer anything from singular strict-U counts.

For an actual SPD metric, every non-strictly-unstable vertex has a true weak escape. Along a distinct true edge,

```
|X_j|_M^2-|X_i|_M^2=2D_ij(M)+|X_j-X_i|_M^2>0.
```

A body with sole strict U would therefore produce a true arborescence toward it by choosing one escape at each other vertex. Every such arborescence is excluded. Since a global maximum-radius vertex is always strict U, the physical result is **U>=2**, with no prescribed root and no weak-freedom assumption.

These are labelled graph/tree counts, not canonical catalogue IDs or new whole-type counts.

## 6. Global affine identifiability: the omitted directions are real shape freedom

This theorem applies to **the entire positive-projective family**, not only the new wedge or old block. It is a geometric classification, not an equilibrium exclusion.

### 6.1 The only possible label exchange is forbidden by a six-ray determinant

Vertex0 is the unique degree-seven vertex. Vertices8,9 are the only vertices not adjacent to0. After removing0, the graph has three internally disjoint8--9 paths of distinct lengths1,3,6:

```
8-9,
8-6-7-9,
8-5-4-3-2-1-9.
```

Thus its only automorphisms are identity and

```
sigma=(0,5,4,3,2,1,7,6,9,8).
```

For ray representatives b1,b2,b4,b5,b6,b7, in this order, form the6x6 matrix whose row is

```
(x^2,y^2,z^2,xy,xz,yz).
```

The exact determinant is

```
D6(epsilon)=41877*epsilon*P(epsilon)/3200000000000000,
P(epsilon)=1294454067500+189702807800epsilon
          -54098881683epsilon^2-4431758538epsilon^3
          -40066560epsilon^4.
```

Its positivity on0<epsilon<=5 follows from the identity

```
P(epsilon)=(1-epsilon/5)*1294454067500
 +(epsilon/5)*311484647175
 +epsilon*(5-epsilon)*[
   54098881683+4431758538*(5+epsilon)
   +40066560*(25+5epsilon+epsilon^2)].                (2)
```

Under an invertible linear change A of the three-dimensional ray coordinates, this determinant is multiplied by(det A)^4>0. Rescaling individual ray representatives multiplies it by a product of squares. These facts follow directly from the symmetric-square representation; on a diagonal A the six factors have product(det A)^4, and the identity extends to every invertible A.

The graph reflection sigma acts on these six selected rays by three transpositions, so it reverses the determinant sign. Equation(2) makes that impossible between ANY two positive-epsilon members. Consequently every affine equivalence between two members preserves all labels. This also gives a canonical orientation of the two otherwise exchangeable seam labels, unaffected by a spatial reflection.

### 6.2 Epsilon is recovered from the actual apex rays

In the basis with columns L,T,R,

```
B=((-1/4,7/2,1/40),(5/4,13/4,27/4),(1,1,1)),
B^-1 e_x=(-140/803,20/73,-80/803).
```

The barycentric coordinates of b(t) are

```
L-coordinate=(1-t)[1+(140/803)epsilon*t],
T-coordinate=-(20/73)epsilon*t(1-t),
R-coordinate=t[1+(80/803)epsilon*(1-t)].             (3)
```

For observed vertices V_i in any affine frame, subtract the observed apex ONLY to recover geometric invariants:

```
W_i=V_i-V_0,
H=[W4 W6 W7],
u1=H^-1 W1, u2=H^-1 W2,
rho=(5/8)*u1_T*u2_L/(u1_L*u2_T).
```

The positive radial factors caused by all projective denominators and by the three anchor lengths cancel. Equation(3) gives

```
rho=[1+(140/803)epsilon/4]/[1+(140/803)epsilon*2/5],
326/361<=rho<1,
epsilon=803(1-rho)/[7(8rho-5)].                    (4)
```

Thus epsilon is an exact affine invariant throughout the whole orbit. These apex-relative coordinates are not substituted for the mechanical centre.

A labelled linear map between the two ray configurations fixes the three anchor rays L,T,R and is diagonal in that basis. The ratios in(3) first force epsilon to agree. Since a bowed ray has all three basis coordinates nonzero, the diagonal map is then a scalar lambda I.

### 6.3 All three projective parameters are nonredundant

At fixed epsilon an affine equivalence, after aligning the apex, would obey

```
lambda*Y_i/(1+c.Y_i)=Y_i/(1+c'.Y_i), i=1,...,9.
```

All denominators are positive, so lambda>0. The nonapical vertices affinely span R^3: one cap contains three noncollinear points and the other has a vertex strictly outside its plane. Therefore the affine equality

```
lambda(1+c'.Y)=1+c.Y
```

on these points forces lambda=1 and c'=c. Together with sections6.1--6.2, this proves the claimed **unlabelled** affine identifiability and trivial affine automorphisms.

There is also a direct exact recovery algorithm. Once epsilon is obtained from(4), regenerate the canonical Y_i and solve the27 linear equations in the twelve unknown entries of A and c:

```
A Y_i-W_i(c.Y_i)=W_i, i=1,...,9.                   (5)
```

Their coefficient matrix has rank12 on this family. Otherwise a nonzero homogeneous solution would give nearby distinct solutions with invertible A and positive denominators, contradicting the uniqueness just proved. The source recovers epsilon,c and the affine normalizer exactly for every one of the seven physical controls.

This is a complete classification within the specified four-parameter orbit, NOT a classification of every realization of the abstract(4,7) lattice. It nevertheless removes a global false simplification: genuinely different alpha/beta/gamma values cannot be hidden affine copies of the already closed block.

## 7. Exact actual negative-beta body and its full reciprocal mechanics

At epsilon=5,c=(0,-1,6), we have s=1 and B_s=diag(1/2,1,4). The normalized raw vertices Z_i are

```
0:(0,0,0)
1:(-469/2753,2415/2753,2800/2753)
2:(-1253/10516,1470/2629,2240/2629)
3:(-1043/14848,1337/3712,175/232)
4:(-7/326,35/163,112/163)
5:(-175/82868,3808/20717,14000/20717)
6:(7/25,13/25,16/25)
7:(7/150,126/5,224/15)
8:(0,331/1769,1200/1769)
9:(0,2435/113,1456/113).
```

Their true maximal facets and edges are exactly those of section3. The genuine uniform volume and centroid are

```
V=4928047752831071414707/4441450836742305290000,
g=(
1200133220762889974274109888215689803733/
32847367067294489212534271271210916915200,
41859382075015660110854730541925250241607493/
6289358366523914281722186996457134730457600,
14811102476548886272604812509451183175384219/
3537764081169701783468730185507138285882400).
```

Both a positive apex fan and an independent interior-point fan agree through second moments. Reintegrating the raw projective image agrees after applying B_s. The actual new centroid differs from the projective image of the old source centroid; that incorrect substitution is explicitly tested and rejected in every control record.

For L>=1024, define

```
C_L=((L^2,0,0),(0,L,L),(0,-1,1)),
M_L=C_L^T C_L, N_L=M_L^-1.
```

The actual Euclidean body has vertices C_L(Z_i-g), uniform centroid0 and volume2L^3 V. For rational L all coordinates are rational. Its complete whole-pencil census is

```
S={F5,F8},
U={1,6},
H={06,79},
physicalweak000; all68 true-edge primitives nonzero.
```

Thus the apex0 is not U, and U>=2 is sharp for this excluded sector.

Writing tau=L^2,

```
M(tau)=((tau^2,0,0),(0,tau+1,tau-1),(0,tau-1,tau+1)),
det M=4tau^3,
adj M=((4tau,0,0),(0,tau^2(tau+1),tau^2(1-tau)),
                        (0,tau^2(1-tau),tau^2(tau+1))).
```

Primal arrows are quadratic polynomials in tau; polar arrows multiplied by the positive determinant are polynomials of degree at most three. After setting tau=1048576+u and multiplying each by its nonzero sign at u=0, all236 coefficient entries are strictly positive. This proves the full reciprocal census for every u>=0, not merely for sampled large metrics. Conditioning is unbounded along this pencil.

**The lower threshold L=128 fails on this same body:** S={5,8},U={1,6,7},H={06,19,67}, strict233,weak000. Thus the parent's old L>=128 control threshold cannot be transported to this new shape. No claim of the sharp transition value between128 and1024 is made.

### Seven complete records, all at epsilon5

Let G=((13,2,1),(2,11,3),(1,3,17)). Metrics are in each body's B_s-normalized coordinates and all use their actual reciprocal.

|c|Metric|S|U|H|
|---|---|---|---|---|
|(0,1,-1)|G|1,2,4,7,8|0,5|03,05,12,68,89|
|(0,1,-1)|M_L,L128|4,8|2,6|06,68|
|(0,-1,6)|G|5,6,8|0,7|07,19,67|
|(0,1,6)|M_L,L128|4,5|1,6|06,67|
|(0,-1,6)|M_L,L1024|5,8|1,6|06,79|
|(0,-1,6)|M_L,L128|5,8|1,6,7|06,19,67|
|(0,1,6)|G|0,4,5,6|0,5,7|01,05,06,07,89|

All seven records are actual10/17/9 bodies. Every one of their476 primal/polar edge primitives is nonzero, so the physicalweak000 assessment is complete. Supporting-triple enumeration verifies every maximal facet, strict convex cycle and true edge. The same-origin poles use the newly computed centroid and N=M^-1. The equality S+U-H=2 is checked, not used to guess omitted equilibria.

Weak000 is asserted for these seven records and the specified negative-beta tail, NOT for every metric in the all-SPD excluded wedge.

## 8. What remains and how this changes the global strategy

The new mechanism is a decomposition of the ACTUAL denominator into the cap slack1-z and positive cone functionals y,7z-y. An explicit affine normalization turns its complete two-parameter wedge into a bounded full-dimensional cube without losing the actual refilled centroid. Synchronizing all arrow denominators then permits a whole-tree common-metric certificate over every scale and both finite wedge walls. This is stronger than widening a tiny transverse band or examining one normal metric pencil.

For clarity, the remaining alpha=0 geometry can be described exactly. For each section ray b_i=(x_i,y_i,1), with the k_i of section3, and actual seam coordinates

```
y8=83/60-7epsilon/125,
y9=(275+432epsilon)/(44+64epsilon),
```

put

```
Gamma_min(epsilon,beta)=max(
 {-1-k_i*x_i-beta*y_i:i=1,...,7},
 -1-beta*y8,
 -1-beta*y9).
```

The full positive alpha=0 domain is gamma>Gamma_min. Apart from portions already closed by other accepted results, the newly uncovered strip is therefore

```
Gamma_min(epsilon,beta)<gamma<max(-1,-1-7beta).
```

General alpha!=0 is also not covered by the new theorem. The global affine-identifiability theorem proves that these parameters are real affine shape freedom, rather than metric gauge. It supplies a canonical way to recognize overlaps and prevent relabelled or affinely repeated coverage from being counted as progress.

All previously closed boundary and epsilon-to-zero channels remain closed; their compactness constants are still not evaluated here. No finite search failure in the residual strip, no loss of one stress row, and no five-contact screening is presented as an exclusion. A useful continuation is to cover the remaining positive-functional sectors with this same actual-moment normalization, or to release alpha while retaining the exact recovered invariants and full true-tree coverage. A future U1 member would still need a separate same-reciprocal-metric S/H/physical-weak audit before any110 claim.

## 9. Complete recovery and actual execution

The following source-only capsule contains ALL three necessary files: the autonomous Python generator/auditor, the exact arbitrary-precision C++ matrix checker, and the complete frozen table of4,112 rows with all43 cell assignments. It imports no parent code, old certificate, cached optimizer result, external geometry input or remote data. The binary table is included in full in the capsule, not represented only by its hash.

Tested versions:CPython3.13.5,SymPy1.14.0,NumPy2.3.5; g++14.2.0,Boost1.83.0 headers,GMP6.3.0. Assertions are enabled. All verification arithmetic is rational or arbitrary-precision integer; there are no floating tolerances. Numerical fitting located candidate weights, but all final rows are frozen exact inputs and every claimed coefficient is rechecked exactly.

The author regenerated the complete polynomial coefficient array with exact inverse power reconstruction and matched its pin. The full build and full check each verified all163,268,007 coefficient matrices; their reports and stdout matched. An additional Python-integer implementation checked all5,084,058 matrices of the first cell and matched its three minimum leading minors with the C++/GMP checker. The C++ native multiprecision alternative was also checked on that first cell. These are additional arithmetic cross-checks, not a separately authored whole geometric proof or proof-assistant formalization.

The decoder was executed in a fresh directory and all three recovered files matched byte-for-byte. No extra full cold polynomial regeneration after that transport check is claimed. A directory containing only the recovered three files is nevertheless sufficient: the verifier generates the exact coefficient file whenever it is absent, and accepts an existing one only after checking its exact hash.

Save the complete decoder fence below as `recover_two_cap_wedge.py`, retaining its final LF, then run

```sh
python -B -S recover_two_cap_wedge.py fresh
cd fresh
OPENBLAS_NUM_THREADS=1 python -B two_cap_wedge.py build --jobs 4 > build.stdout
OPENBLAS_NUM_THREADS=1 python -B two_cap_wedge.py check --jobs 4 > check.stdout
cmp build.stdout check.stdout
OPENBLAS_NUM_THREADS=1 python -B two_cap_wedge.py crosscheck --jobs 1
```

Only the decoder uses -S. Do not disable assertions. `two_cap_wedge.py coefficients` forces complete polynomial regeneration and exact inverse reconstruction. The C++ checker is compiled automatically with `g++ -O3 -std=c++17 wedge_pd.cpp -lgmp`.

|Object|Bytes|SHA-256|
|---|---:|---|
|recover_two_cap_wedge.py|67452|dfe343bf39ba6b57add408a5dc0ee0b03fdcd71fcec0f01a650e508c0b41bb07|
|two_cap_wedge.py|27427|3f6425354dfa806d49dd5c4fe754b367991926e06b0b884781d3f9ee331dc5ea|
|wedge_pd.cpp|3670|a7220baaa6f4e705120eb87ac347f246e25bc74aa03f2b5e83d27bbd4dca0802|
|wedge_table.bin|63152|858e9cb27fadb66a458ac03970b21ac7812d2203e4d722712ee22d732a2c7488|
|two_cap_wedge.json|551695|d85f8abe33c47ec5dd555c7074c4f6601e96bca3df0f40fdfd9a6ce85e368f33|
|identical build/check stdout|522|28ae2c13b4d4f4899179061e4b1d18c4ff7925b8df415031a81cfe8a4b3ded2e|

The decoded canonical row/cell JSON has262746bytes,SHA `60c883536a08438486997e504d2fdc57adfe0a1478796318cfa4dd92242f428a`. The generated coefficient text has154313441bytes,SHA `864fbe5b4bf52001d33372e1934e042de55aff92377c9dfcddc975af3383fbb7`; it is generated, not an additional recovery input. The packed three-file archive has94331bytes,SHA `78c77194626095ca51d0a4613d8599c80a1d0dc169e7177cfc3667d57aaef1b1`.

Observed terminal output:


[Encoded source block omitted; the code in this passage is incomplete.]


Additional observed marker:

```
PYTHON_GMP_CPP_ALL_FIRST_CELL_COEFFICIENT_MINIMA_MATCH 5084058
```

### Complete source-only capsule


[Encoded source block omitted; the code in this passage is incomplete.]


Convenience copies: complete recovery capsule (`recover_two_cap_wedge.py`), exact report (`two_cap_wedge.json`). The embedded capsule and proof suffice without these links.
