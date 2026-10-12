# material-e75611e233be

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# H5_LOCAL_SOURCE_SUBTREE_REFLECTION_CUTS_V1

## Statement and evidence boundary

The fully read literal parent is minimum-0245,
SHA256 3a4889dd902249e2904ddfa747f00575a10c16646d44cf15224164893c8056be,
H5_BASAL_MAXIMUM_ROOT_CHILD_AND_SHARP_REFLECTION_THRESHOLD_V1.
Its global basal-maximum and basal-root/apical-only-child results are accepted
author work. They were not independently replayed here.

The new theorem replaces its global highest-nonroot test by a test on the
actual basal hull of ONE source subtree. Exact new scalar certificates and
complete labelled-tree enumeration give:
* all genuine H5 shapes with x,r in (0,1), p,q>0, p+q<1 and
  0<lambda<=1/16: 22,941 excluded complete rooted primal trees,
  3,387 more than the parent's 19,554;
* on the additionally restricted closed macro box
  x in [15/16,1], r in [1/4,1/2], still the ENTIRE physical p/q triangle
  and 0<lambda<=1/16, with genuine x<1:
  26,409 excluded trees, 6,855 more than the parent.

Both statements hold for every nonzero PSD common metric, not only SPD,
and use the actual uniformly filled body's moving volume centroid.
The lambda band in these new statements is four times the earlier
original-cubic prism's [0,1/64]. Degenerate shape parameters and lambda=0
are excluded from these NEW geometric tree statements; their polynomial
guards were evaluated on closed boxes but span/strict-hull arguments use
genuine geometry. The stronger indexed-boundary conclusions of the parent
are not silently inherited.

On the original cubic prism with lambda<=1/64, adding the original
20-tree certificate [internal-source-reference] raises 26,409 to 26,424,
leaving 22,366 outside this specific union. The report's union-with20
counts have this intersection-of-domains interpretation, including in
full mode; they do not expand that 20-tree certificate to lambda<=1/16
or to all x,r. The half-triangle all-root theorem remains separate.

These are not canonical graph-orbit counts, all-root or whole-H5/E17
exclusions, weak-equilibrium density, a new body, or a new complexity
bound. The global accepted bounds and separate attaining construction
remain 34<=C_min<=622.

## 1. Actual geometry

Let s=1-lambda. The basal polygon, in counterclockwise order, is
B0=(1/4,0), B1=(1-3x/4,0), B2=(1-p,p), B3=(q,1-q),
B4=(0,1-3r/4), B5=(0,1/4), B6=(1/16,1/16).
The actual basal vertices are (s B_i,0); the three top vertices are
(0,0,1), (lambda,0,1), (0,lambda,1), indexed 7,8,9.
The unique apical neighbours of basal vertices 0..6 are
(7,8,8,9,9,7,7). Facets, edges, oriented fan, and every exact volume and
first-moment formula are literal in the accompanying source. They use
the parent's unchanged incidence, not a relabelling.

Write the actual centroid g=(c,gamma)=J/V. The source checks four
oriented-fan polynomial identities for V,J. The parent formulas give
A=(31-24xp-24rq)/64>=7/64, V=A s^2/3+lambda/6>0, and
V/2-Jz=(2 A s^2-lambda^2)/24>0 on lambda<=1/16.
For the last inequality the source checks
(7/32)(1-lambda_max)^2>lambda_max^2.
Also gamma>=1/4. Thus t=2gamma lies strictly between 0 and 1.

For a basal point b and a top horizontal coordinate a define the actual
basal reflected point
    w(b,a)=2c-2gamma a-(1-2gamma)b.

## 2. Local source-subtree lemma

Consider ANY two-layer convex body with actual g as above and 0<gamma<1/2.
Let a selected directed tree edge go from a top vertex a to a basal
vertex b. Let D be the basal vertices in the source component after
deleting that edge, and let S={b} union D. Suppose S contains three
noncollinear basal vertices and w(b,a) lies in the relative interior of
conv(S), in the basal plane.

Then the selected tree's weak arrow inequalities cannot hold for any
nonzero PSD common metric M.

Proof. Map centred vectors by M^(1/2), writing A for the top source,
B for the basal target, and X_i for the basal descendants. Along a weak
arrow Y->Z,
    ||Z||^2-||Y||^2=2 Y.(Z-Y)+||Z-Y||^2>=0.
Every descendant in D therefore has norm <=rho=||A||, while a->b implies
A.B>=rho^2. Put
    W=-(1-t)B-tA,  t=2gamma.
This is exactly the mapped centred reflected point. We have
    ||B||^2>=rho^2,
    ||W||^2 >= (1-t)^2 ||B||^2 + (2t-t^2)rho^2 >=rho^2.
B cannot vanish: otherwise A=0, every descendant vector vanishes, and
the three noncollinear basal centred vectors in S span R^3 because
gamma>0, forcing M=0. Consequently
    W.B=-(1-t)||B||^2-t A.B<0,
so W is nonzero. For every i in D,
    W.X_i<=||W||rho<=||W||^2.
Interior containment gives a convex representation of W using the
vectors in S with positive coefficient on B. Apply the linear functional
W to this representation: the B term is strictly below ||W||^2 and all
others are at most ||W||^2, a contradiction. QED.

In particular b need not be the root. This is the new point:
an INTERNAL top-to-base transition is also forbidden whenever its
source subtree already spans an enclosing basal hull.
For SPD one can weaken interior containment to closed containment,
because nontrivial tree paths then strictly increase squared norm.
The executed counts use the stronger interior/PSD test only.

## 3. Complete exact scalar guards

For each ordered basal chord i->j, i!=j, put
    n_ij=(B_j,y-B_i,y, B_i,x-B_j,x), h_ij=n_ij.B_i.
For target b, let a be its literal apical neighbour's horizontal
coordinate and use the polynomial
    R[b,i,j] = V s h_ij - 2 n_ij.J_horizontal
               + 2 Jz n_ij.a + (V-2Jz) s n_ij.B_b.
Then R/V is exactly the signed support slack of w in the half-plane
bounded by the corresponding scaled basal chord. No surrogate masses,
frozen centroid, independent metric, stress lowering or covariance cap
appears.

There are 7*7*6=294 guards. Exact cancellation yields degrees
(2,2,total-triangle-2,3) in (x,r,p/q,lambda), hence 216 Bernstein
coefficients per guard. The source derives rather than assumes these
degrees and checks them.

All coefficients of an accepted guard are nonnegative. To prove strict
positivity also on the macro box's allowed boundary faces, the source
requires a positive coefficient on EVERY relevant x/r/lambda face:
intrinsic degeneracies x=0,1,r=0,1,lambda=0 are not included, while genuine
macro endpoints and lambda=1/16 are included. The physical p/q triangle
is open, so all its Bernstein basis functions are positive.

For each S with 3<=|S|<=7, take its cyclically ordered chord edges.
When every chord guard for target b in S passes, the reflected point is
strictly inside conv(s B_i:i in S). Full mode has 64 accepted guards
and 14 target/subset pairs. Prism mode has 86 accepted guards and 43
target/subset pairs. Each accepted guard uses 216 exact scalar
coefficients; negative coefficients of UNaccepted chords are retained
in the output, never interpreted as physical infeasibility.

For every one of the 4,879 unrooted spanning trees and every root, the
source tests the actual source component of each top-to-base tree edge.
There is no guessed correspondence between an arbitrary subset and a
tree component.

The global parent plus local cuts give rootwise counts:
    full:  (1560,948,686,686,948,1560,1916,4879,4879,4879) =22941;
    prism: (2172,1779,1271,1355,1245,1725,2225,4879,4879,4879)=26409.
The parent alone has
    (693,678,686,686,678,693,803,4879,4879,4879)=19554.
The original twenty-tree support adds only fifteen root-2 trees,
on its own stated domain. The remaining five were already apical-root
exclusions.

For example, the rooted tree
    root4; 0->1,1->2,2->3,3->9,5->4,6->0,7->0,8->1,9->4
was not in the parent's two excluded families. The edge 9->4 has
source-subtree basal hull S={0,1,2,3,4,6}; the new lemma excludes it.
Changing 4->5 and making root5 gives an explicit internal-transition
example. Both are in the full x/r theorem, not just the macro prism.

## 4. Recovery and observed evidence

The complete standalone source is immutable material
[internal-source-reference], saved as h5_local_reflection.py:
11008 bytes,
SHA256 9e76632309f3ddff40cb7fbe52c6a7df417a009b965cb510bb42dbdee3ab567d.
It embeds every exact input, helper, domain, edge, moment, transform and
tree-enumeration rule. It needs no other source or generated matrix file.
The parent result remains the scientific source for its existing
19,554 exclusions and original geometry; this is not a replay claim.

CPython 3.13.5 was observed. The source uses only the standard library
and supports Python>=3.11, with assertions enabled. Reconstruct and
verify with:
    python -B -S h5_local_reflection.py --mode full --lambda-max 1/16 --out full
    python -B -S h5_local_reflection.py --mode prism --lambda-max 1/16 --out prism

Expected terminal markers:
    H5_LOCAL_SUBTREE_REFLECTION_PASS full 294 216 64 14 22941
    H5_LOCAL_SUBTREE_REFLECTION_PASS prism 294 216 86 43 26409

Both modes passed normally and after copying ONLY the source into a
clean directory and rerunning. Both coefficient files and reports
were byte-identical in that source-only cold reproduction.

full/local_reflection_coefficients.json:
561320 bytes, SHA256
0b68607249efcb1739681c1002c3a842d284afb05369399254d2cee2455f4852.
full/local_reflection_report.json:
2075 bytes, SHA256
bc0f3fdbdfc82de4b644b25d4aab3d74d2ed6d11dcedf07d2316fd00d6cf017c.
prism/local_reflection_coefficients.json:
736487 bytes, SHA256
212e8b9801bfc4dc5e22cb01193189aa743cb37139f5f62c634a4e7837d1c4b1.
prism/local_reflection_report.json:
2897 bytes, SHA256
2e105bb97841bd909450a0be274fe9d5626e3b91243fbe1c6bc017339be57529.

This is an executed rational/integer certificate plus the analytic
local lemma, not proof-assistant formalization. A failed chord test,
an unexcluded tree, or the remaining 22,366 on the original prism is
NOT an actual feasible PSD/SPD tree witness.

## 5. Next mathematical connection

The new mechanism combines local source-subtree geometry with monotone
tree norms. Useful continuations are a quantitative version that
couples several otherwise insufficient subtrees, original-polynomial
all-root coverage on the residual p+q>1/2, and genuine common-metric
feasibility in the remaining trees. Basal-only tree routes and small
source components are not excluded by this local lemma.
Neither a fixed-layer U argument (disproved by the parent's controls)
nor more subdivision of the same globally lowered cubic should be
reintroduced as an automatic completion.
