# material-04184117e8af

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# REDUNDANT_POSITIVE_MARK_FACET_REDUCTION_V1

## Evidence, scope and exact dependencies
This is an analytic coordinator result about the genuine full marked-body maximum problem, not a numerical search, a claim about arbitrary convex polytopes, or an exclusion of the full mechanical10/17/9 layer. No computation materially produced the result and no omitted program or input is needed to recover it. Its full proofs are given below.

Exact antecedents read completely in this coordinator turn:
- POLYHEDRAL_TRACE_STATIONARITY_RIGIDITY_V1, [internal-source-reference], SHA256 8dc6ce8812298f59a61b404ccba7c09fef867bb8844a8952bf1cacc638bcc2b9.
- ROOT_DUALITY_JOINT_VARIATIONS_V1, [internal-source-reference], SHA256 73eb04d63deeab693d29533819d3b95c4e1af3cc01d756987381aaa2bb4c2ed8.
- NONPOSITIVE_MARK_COORDINATE_PATCH_ROOT_CHAIN_V2, [internal-source-reference], SHA256 0fdbce320bac57c70047fa72690c53148726aa159ecbfa6d6075fbe7cab488c1, authored and preserved in this same turn.

The theorem studies a mixed-sign complement not covered by a two-adjacent-true-marks polygon lemma: the positive canonical mark D is INSIDE a true edge, not a true vertex. The negative mark C is a true vertex. All integrals below belong to one actual uniformly filled body.

## 1. Setup and necessary variations
Let
A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
ell=a+(d-a)x+(c-a)y+(b-a)z,
a>b>0, c>0, d>0, s=a+b,
n=(s+c)x+(s+d)y.
Let T0=conv(A,B,C,D) be contained in the full-dimensional convex polytope P, with P contained in x>=0,y>=0,ell>=0. Fx=P intersect{x=0}, Fy=P intersect{y=0} and F0=P intersect{ell=0} are true positive-area facets, with F0 the root. The protected coordinate facets need not be the canonical triangles.

Use actual integrals V=int_P1, E=int_Pell, N=int_Pn, T=N/(6VE), q=N/E, r=N/V and G=n-r-qell. At the full marked maximum the established body variations imply: A,B are true vertices and AB is the whole true edge Fx intersect Fy; GA=-r-qa<GB=-r-qb<0; every auxiliary true vertex, meaning a true vertex other than A,B,C,D, has strictly positive G; every ordinary facet contains a canonical mark; and an ordinary facet with exactly one canonical mark X is a true triangle XUV with X true, GX<0, GU=GV=-GX/3.

Canonical mark variation gives the actual supporting inequality
h_D=ell+(s+d)x-(s+2d)<=0 on Fy,
with equality at D and strict negativity at A,B. Its C-reflection, together with the nonpositive-mark theorem, ensures that GC<=0 forces C to be true.

For this result assume
GC<0, GD>0, and D is not a true vertex.
The reflection exchanging x/y and C/D gives the corresponding other mixed-sign case. The strict ordering a>b distinguishes A and B and is essential in the anchor exclusion below.

## 2. The true edge containing the redundant mark
Since h_D is a nonconstant affine support of the true polygon Fy and vanishes at D, the nonvertex D lies in the relative interior of a true exposed edge UV. Its endpoints cannot be A or B because h_D is strictly negative there, so they are auxiliary true vertices and GU,GV>0.

Put alpha=s+d, beta=s+2d, and k=(b+2d)/(a-b)>0. On the supporting line in Fy,
z=k(x-1), ell=beta-alpha x.
The coordinate x is nonconstant on that line: x,y,ell would otherwise fix z as a>b. Orient the endpoints by x_U=l<1<x_V=h. Because U,V are auxiliary and Fx intersect Fy is exactly AB, both have x>0. Nonnegativity of ell gives
0<l<1<h<=beta/alpha=1+d/(s+d)<2.
In particular U lies strictly off the root, with ell_U>d>0 and z_U<0. The endpoint V may or may not be on the root.

Along this edge,
G=[(s+c)+q(s+d)]x-r-q(s+2d),
whose x-slope is strictly positive. Hence
0<GU<GD<GV.
The edge UV is therefore not a constant-G edge.

## 3. A second true facet and its global support
Let F be the second true facet of UV. It is not Fx, since x_U,x_V>0, and is not F0, since U is off-root. It is ordinary and contains D. It cannot contain A or B: two distinct true facets have intersection exactly their common face UV, while A,B belong to Fy outside that edge. It cannot contain only D, since the one-anchor theorem would make D a true vertex. Consequently its canonical set is exactly {C,D}; C is a true vertex of F and D remains interior to its edge UV.

The unique plane through C,U,V has affine support
H_F=beta-ell-alpha x-(beta-c)y=0.
It satisfies H_F(A)=b+2d>0, H_F(B)=a+2d>0, H_F(C)=H_F(D)=0. Actual convexity fixes the global halfspace
H_F>=0 throughout P.
All true vertices of F except C are auxiliary and have positive G. They form one boundary chain from one neighbor of C to the other; UV is a distinguished edge in that chain.

## 4. At most five vertices on F
Consider another edge WZ of this auxiliary chain. Its second facet cannot be Fx, since C lies on both Fx and F but not on WZ; it cannot be Fy, since F intersect Fy is precisely UV. If it is not the root, its canonical marks can only be A or B: C and D lie on F outside WZ. It cannot contain both A and B, because AB already is a true edge with incident facets Fx,Fy, and no third true facet can contain AB. Therefore the second facet is a one-anchor true triangle XWZ, with X in {A,B}, and
GW=GZ=L_X=-GX/3>0.

On the convex polygon F, this constant-G true edge is supporting. Since GC<0<L_X, its supporting side is G<=L_X. Thus it is the global maximum-G face of F. There can be at most one such nonroot edge: an affine function on a convex polygon has a unique exposed maximizing face, not two distinct true edges. There is at most one root edge as F and F0 have only one common face. Besides those, there is only the distinguished UV edge.

If there are j auxiliary vertices on F, their boundary chain has j-1 edges. Hence j-1<=3 and F has at most five true vertices. If F is a pentagon, its three auxiliary-chain edges consist exactly of UV, a root edge, and one ordinary one-anchor edge. If there is no ordinary one-anchor auxiliary edge, F has at most four vertices. No cardinality bound on the root polygon itself was used.

## 5. Only the lower endpoint B can anchor the ordinary edge
Suppose the ordinary auxiliary edge WZ exists, with its second facet XWZ and L=-GX/3. The plane through X,W,Z is
G+(4L/H_F(X))H_F=L.
This affine equation is valid because H_F(W)=H_F(Z)=0, GW=GZ=L, and GX=-3L. At C the left side is GC<0, so true convex support gives
G+(4L/H_F(X))H_F<=L throughout P.
As H_F>=0, the global maximum of G on P is L and its entire maximizing face is WZ.

Take X=A. Then H_F(A)=b+2d, H_F(B)=a+2d, L=(r+qa)/3. Evaluating the global support at B and multiplying by the positive quantity3H_F(A) would require
(a-b)[4r+q(4a+3b+6d)]<=0.
All factors are strictly positive, a contradiction. Thus X=A is impossible. The ordinary auxiliary-chain edge, when present, is anchored only at B, has endpoint value
L_B=(r+qb)/3,
and is the entire global maximum-G face of the actual body.

This is a global body support consequence of the redundant positive mark; it is not merely a relation among abstract polygon moments. A pentagonal F therefore has exactly the three distinguished kinds of edges: UV, root, and B-anchored global-max edge.

## 6. A real negative result for a tempting marker instability argument
Moving D along its exposed edge does NOT itself exclude this mixed-sign configuration. Hold the actual body P and physical root function fixed, move the mark to D_x=(x,0,k(x-1)) near x=1, and recanonicalize by
x'=old_x/x, y'=old_y, z'=old_z-k(x-1)old_x/x.
The positive Jacobian is1/x. The new canonical value is d_x=beta-alpha x. If X=int_P old_x and Y=int_P old_y, then the new marked objective is exactly
T(D_x)=[(s+c)X+Y x(s+d_x)]/(6VE)
      =[(s+c)X+(s+d)Y(2x-x^2)]/(6VE)
      =T(D)-(s+d)Y(x-1)^2/(6VE).
Thus D is a strict local maximum for this one-dimensional mark motion. This calculation rules out the proposed shortcut that every positive redundant mark must be unstable under displacement along its own exposed edge. It does NOT construct a joint stationary polytope and does not refute the full trace bound.

## 7. A mandatory actual subbody and coupled moments
The actual five-vertex pyramid
Q=conv(A,B,C,U,V) contained in P
has apex C and true base quadrilateral A,B,V,U in y=0. Its base triangulation ABV and AVU gives positive determinant masses h and k(h-l). Write
t0=h+k(h-l)>1.
Then direct actual tetrahedral integration gives
6Vol(Q)=t0,
int_Q x=[h^2+k(h^2-l^2)]/24,
int_Q y=t0/24,
int_Q ell={h(a+b+c+ell_V)+k(h-l)(a+c+ell_V+ell_U)}/24,
int_Q n={(s+c)[h^2+k(h^2-l^2)]+(s+d)t0}/24,
where ell_U=beta-alpha l and ell_V=beta-alpha h.

These are simultaneous moments of one true subbody, not independent mass variables. Since1,x,y,ell,n are nonnegative on P, each integral for P is bounded below by the corresponding Q integral. Such lower bounds alone do NOT imply an upper bound on the ratio T, whose numerator also increases. Any further value proof must retain the coupled actual added material.

## 8. Optional full-joint root moment connection, not a closure
This section requires full joint root stationarity in addition to the conditions used above. Put g=(u,v,z_g), p=u+v, t=6V, m=3p/t, w=(v/(3p),u/(3p),1/3). The exact antecedent yields
int_F0 Gh dnu=6V^2[T h(g)-m h(w)]
for affine h, where dnu=darea/|grad ell|, and
int_F0 G^2 dnu=6V^2m[r-n(w)]>0.
A direct substitution gives H_F(w)=(s+4d)/3. If the B-anchored max edge exists, let H_B=a+2d and L=L_B. Its support function K=L-G-4L H_F/H_B is nonnegative on P and positive in the relative interior of the distinct root facet. As G>0 on the root,
L{T[1-4H_F(g)/H_B]+m[4H_F(w)/H_B-1]}>m[r-n(w)]>0.
Actual coning from B, with H_F>=0, gives H_F(g)>=H_B/4. However the remaining necessary condition H_F(w)>H_B/4 is automatic, so this argument does not exclude the B case.

Even without the B edge, the root integral of G H_F is positive because F and F0 are distinct true facets. Its expansion gives
q{beta-alpha u-(beta-c)v}>(2s+4d+c)u+(2s+5d)v.
Again, this is a necessary full-joint condition, not a sufficient convex realizability test or a trace cap. A scalar fit to it cannot replace the actual body.

## 9. Scientific boundary and next question
The theorem reduces a mixed-sign redundant-mark ordinary facet to at most five vertices and removes its A-anchored auxiliary edge. It preserves an exact negative marker-Hessian result and a useful actual five-vertex moment core. It neither excludes all root-coupled protected quadrilaterals/pentagons nor settles the remaining B-anchored facet patterns. The positive redundant mark is not silently promoted to a true vertex. No use is made of the positive-level edge lemma whose hypotheses require a positive TRUE canonical vertex adjacent to a second marked vertex.

The next substantive question is whether the remaining UV[private-runtime-path] polygon configurations can satisfy all true neighboring-facet reactions and actual volume/root moments, or whether a real geometric countercontrol survives. Neither T<51/25 for the whole marked problem, nor the complete mechanical10/17/9 exclusion, nor a new attaining construction is established here. The accepted mechanical bounds remain34<=C_min<=622.
