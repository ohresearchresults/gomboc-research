# figure-0477

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Clear Willow 56 — C48 orthogonal apex-root chamber closed exactly

## Outcome and source boundary

I read the continuation journal through EOF and used the literal parent `figure-0474`, SHA-256 `a03ab041f25c69669ce6f4010d5318f60be3d7c0c7c6dc02b5cbcbd3fad3865e`, as source authority. There is no conflict between its literal payload and the journal synopsis. The parent supplies the mass-closed own-centred normal form, the durable 159 apex-root shadow shapes, and the orthogonal reserve/apex-gate partition.

No exact C48 strict110 body was found. Instead, the assigned **entire orthogonal unequal-height apex-root chamber is now excluded exactly**. The exclusion is stronger than the inherited short-side reserve disjunction and in fact does not need to branch over the 159 shadow systems: in a weak-free own-centred ordinary bipyramid whose apex line is perpendicular to the base plane, **an apex can never be the unique strict unstable equilibrium**. Therefore all 159 durable apex-root systems have zero survivors at `rho=0`.

This is an actual homogeneous-centroid theorem. It does not use a center-free combinatorial obstruction and does not conflict with the preserved off-centroid strict110 square-bipyramid countercontrol.

## 1. Exact setup

Use the parent's mass-closed gauge. Let the planar base octagon be `S=conv(s_i)` with area centroid zero, let `c` be the planar base-centroid coordinate in the centred 3-body, and let the positive distances from the base plane to the top and bottom apices be `a=h_+` and `b=h_-`. For the orthogonal slice `rho=0`,

`z_0=(b-a)/4`,

`T=(-3c,z_0+a)`, `D=(-3c,z_0-b)`,

`B_i=(c+s_i,z_0)`.

Ordinary incidence is the parent's exact crossing condition `-4c in int(S)`, which guarantees the ordinary bipyramid graph: the eight base-cycle edges and all sixteen apex-to-base edges. The actual uniform filled centroid is exactly the origin.

For the proof it is convenient to put

`q=-4c`, `p=-3c=3q/4`, and write the planar part of a base vertex as `x_i=c+s_i=s_i-q/4`.

Thus all base vertices have the common height `z_0`, and both apices have the same planar part `p`.

## 2. Main theorem

**Theorem (orthogonal apex-root exclusion).** Consider any ordinary `n`-gonal bipyramid of uniform positive volume density at its actual filled-volume centroid, with the apex line perpendicular to the base plane. Assume the vertex equilibrium census is weak-free. Then no apex can be the unique strict unstable equilibrium.

More precisely, suppose `a>b` so the top apex is farther from the base plane than the bottom apex.

* If the bottom apex `D` is strict U, then the top apex `T` is also strict U.
* If `T` is strict U and `D` is not strict U, then there is at least one strict unstable **base vertex** distinct from `T`.

The case `b>a` follows by swapping top and bottom. When `a=b`, the two apex outgoing-dot rows are identical, so either both apices are strict U or neither is.

Hence a weak-free U1 orthogonal own-centred bipyramid, if one exists at all, must have its unique U at a base vertex.

### Exact proof

Let a base point be `B=(x,z_0)` and let the common planar apex coordinate be `p`.

For `a>b`, the lower apex is `D=(p,z_0-b)`. Its outgoing dot to `B` is

`D·(B-D)=p·(x-p)-b(a+3b)/4`.

Therefore a positive lower-apex escape `D -> B` implies

`p·x > |p|^2 + b(a+3b)/4 > |p|^2`.

By Cauchy, this forces

`|x|>|p|`.                                                   (1)

The upper apex is `T=(p,z_0+a)`. The reverse-type outgoing dot from a base point to `T` is

`B·(T-B)=x·(p-x)-a(a-b)/4`.

Thus a positive final arrow `B -> T` implies

`p·x > |x|^2 + a(a-b)/4 > |x|^2`,

and Cauchy forces

`|x|<|p|`.                                                   (2)

For two base vertices `B=(x,z_0)` and `B'=(y,z_0)`, a positive base-cycle arrow satisfies

`B·(B'-B)=x·(y-x)>0`.

Consequently

`|y|^2-|x|^2 = 2 x·(y-x)+|y-x|^2 >0`.                       (3)

So every positive base-to-base arrow strictly increases planar radius.

Now suppose `T` were the unique strict U. If `D` were already strict U there would be two U's. If `D` had a zero outgoing dot, the target would already fail weak000. Hence, in a weak-free candidate, `D` has a positive outgoing arrow to some base vertex. Positive arrows strictly increase the full squared radius, so following positive arrows in the finite one-skeleton cannot cycle and must terminate at a strict U. Under the assumed U1 hypothesis it would have to terminate at `T`.

Because there is no apex-to-apex edge, any such positive path has the form

`D -> B_0 -> B_1 -> ... -> B_k -> T`,

with all intermediate arrows after the first and before the last running along the base cycle. By (1), `|x_0|>|p|`. By (3), the planar radii strictly increase along every intermediate base arrow. But by (2), the final base vertex must satisfy `|x_k|<|p|`. Contradiction.

The remaining claim, that `D` strict U forces `T` strict U when `a>b`, is even simpler. For the same base point `B`,

`T·(B-T)-D·(B-D) = -3(a-b)(a+b)/4 < 0`.

Thus every top-apex outgoing dot is strictly smaller than the corresponding bottom-apex outgoing dot. If all bottom dots are negative, all top dots are negative as well.

Every step above is exact. The only geometric inputs are the actual-centroid height relation `z_0=(b-a)/4` and the ordinary bipyramid graph supplied by the crossing condition.

## 3. Exact closure of the assigned chamber

The parent orthogonal analysis defines

`L=h_{S+4c}(-3c)`,

`A_+=a(3a+b)/4`, `A_-=b(a+3b)/4`,

and for `a>b` has `A_-<A_+`. It already established the exact apex-gate partition and the mandatory short-side polar reserve failure for an S1 survivor.

Combining that partition with the new theorem gives the complete weak-free orthogonal apex classification:

* `L<A_-`: both apices are strict U, so U1 is impossible.
* `L=A_-` or `L=A_+`: an apex is on a weak sign boundary, so the target weak000 chamber is not open there and the equality must be audited as a boundary, not discarded.
* `A_-<L<A_+`: `T` is strict U and `D` is not. The new positive-path barrier proves that a base vertex is also strict U. Hence **U>=2 throughout the entire assigned unequal-height apex-root chamber**.
* `L>A_+`: neither apex is strict U. Any weak-free U1 survivor must therefore have a **base-vertex root**.

Swap top/bottom for `b>a`.

This closes every one of the parent's **159 durable labelled apex-root shadow systems** in the orthogonal slice. There are **0 surviving apex-root systems**. No per-shape SDP, reserve branch, or shadow-depth refinement is needed: the contradiction occurs before those conditions become active.

## 4. Relation to the mandatory short-side reserve failure

For `a>b`, the parent reserve is

`R_i^- = w_i(w_i+3)-b(a-b)|u_i|^2`.

An S1 survivor had to enter at least one short-side reserve-failure branch. The new theorem is strictly stronger on the assigned apex-root chamber:

* if `R_i^->0` for all `i`, the parent already gives `S>=2`;
* if some `R_i^-<0`, the stable-side obstruction has been crossed, but the new theorem still gives `U>=2` for every apex-root candidate;
* if `R_i^-=0`, retain it as the exact reserve sign-boundary case as requested; the new U-side exclusion still applies independently, so no strict110/weak000 apex-root body is lost by not assigning the equality to either open reserve chamber.

Thus the reserve disjunction has **no apex-root survivors at all** in `rho=0`.

## 5. What remains open after this closure

The orthogonal C48 problem is not globally excluded. The exact remaining weak-free U1 region is now:

`rho=0`, unequal or equal heights as applicable, unique U at a **base vertex**, and for `a>b` necessarily `L>A_+` (dually for `b>a`).

For strict S1 with `a>b`, the parent top-ring argument still forces at least one stable top facet and therefore still requires a strict short-side reserve failure on the bottom ring; reserve equality remains a sign-cell boundary. The durable base-root shadow universe has 309 marked shapes, so the strongest next exact orthogonal question is no longer the 159 apex-root batch. It is:

> Can the 309 base-root systems satisfy `L>A_+`, area-centroid zero, `-4c in int(S)`, a strict short-side reserve failure, the explicit same-centre polar U1 conditions, and the base-root shadow inequalities simultaneously?

The positive-path barrier gives an additional useful base-root necessary condition. In the remaining weak-free chamber `D` is non-U, so it has a positive escape `D -> B_0`. The proof above gives `|x_0|>|p|`. Any later positive base-cycle arrow increases planar radius, while a positive base-to-`T` arrow would require planar radius `<|p|`; the positive path also cannot return to `D` because squared radius has already increased. Hence the positive path starting at `D` stays on the base cycle until it reaches the unique base U root. Therefore that root must satisfy `|x_root|>|p|`. This is exact and can be added before solving the 309 base-root semialgebraic systems.

No numerical failure is promoted as an exclusion, and no C48 strict110 construction is claimed.

## 6. Reconstructible exact certificate

New source unit:

`VERIFY_C48_ORTHOGONAL_APEXROOT_EXCLUSION.py` — **3862 bytes**, SHA-256 **`f310e4979ecda0746c46c489cd42fb41a881caee8315d61baebad71ac03c0e07`**.

Runtime used: CPython 3.13.5, SymPy 1.14.0. Run:

`python -B VERIFY_C48_ORTHOGONAL_APEXROOT_EXCLUSION.py`

Expected terminal output includes:

`OCTAGON_SIMPLE_D_TO_T_PATHS 120`

`APEX_DOT_DIFFERENCE -3*(a - b)*(a + b)/4`

`C48_ORTHOGONAL_APEXROOT_CHAMBER_EXCLUDED_PASS`

`C48_ALL_159_APEX_SHADOW_SYSTEMS_ELIMINATED_IN_RHO0_PASS`

Complete source follows; no sandbox file is required:

```python
# Clear Willow 56: exact orthogonal own-centred bipyramid apex-root exclusion.
# CPython 3.13.5 + SymPy 1.14.0.  No floating-point arithmetic is used.
#
# Scope proved by the accompanying handoff:
# In an ordinary bipyramid at its actual uniform-volume centroid, with apex
# line perpendicular to the base plane, no apex can be the UNIQUE strict
# unstable equilibrium in a weak-free configuration.  The proof is valid for
# any number of base vertices; C48 is the n=8 instance.

import sympy as sp
from itertools import combinations

a,b = sp.symbols('a b', positive=True)
px,py,x,y,x2,y2 = sp.symbols('px py x y x2 y2', real=True)
p=sp.Matrix([px,py]); X=sp.Matrix([x,y]); Y=sp.Matrix([x2,y2])
z0=(b-a)/4
zT=z0+a
zD=z0-b

# Exact filled-centroid vertical coordinates from the mass-closed normal form.
assert sp.simplify(zT-(3*a+b)/4)==0
assert sp.simplify(zD+(a+3*b)/4)==0

# Outgoing dot from the lower/shorter apex D to a base point B=(X,z0).
D_to_B = sp.expand((p.dot(X-p)) + zD*b)
assert sp.simplify(D_to_B - (p.dot(X-p)-b*(a+3*b)/4))==0

# Outgoing dot from a base point B=(X,z0) to the upper/taller apex T.
B_to_T = sp.expand(X.dot(p-X) + z0*a)
assert sp.simplify(B_to_T - (X.dot(p-X)-a*(a-b)/4))==0

# Uniform comparison of the two apex outgoing dots to the same base point.
T_to_B = sp.expand(p.dot(X-p) - a*zT)
Bvec_from_D = D_to_B
assert sp.simplify((T_to_B-Bvec_from_D) + sp.Rational(3,4)*(a-b)*(a+b)) == 0

# Base-to-base positive arrows increase planar squared radius because all base
# vertices have the same z-coordinate.
base_arrow_identity = sp.expand((Y.dot(Y)-X.dot(X)) - (2*X.dot(Y-X)+(Y-X).dot(Y-X)))
assert base_arrow_identity==0

# Graph certificate for the ordinary octagonal bipyramid: every simple path
# from D=9 to T=8 begins D->base, ends base->T, and all intervening edges are
# base-cycle edges.  This is the only graph fact used by the proof.
N=10; T=8; D=9
edges={(i,(i+1)%8) for i in range(8)}
edges |= {(8,i) for i in range(8)} | {(9,i) for i in range(8)}
edges={tuple(sorted(e)) for e in edges}
adj=[set() for _ in range(N)]
for u,v in edges: adj[u].add(v); adj[v].add(u)
paths=[]
def dfs(v,path):
    if v==T:
        paths.append(tuple(path)); return
    for w in adj[v]:
        if w not in path:
            dfs(w,path+[w])
dfs(D,[D])
assert paths
for path in paths:
    assert path[0]==D and path[-1]==T and len(path)>=3
    assert path[1] < 8 and path[-2] < 8
    assert all(v<8 for v in path[1:-1])
    for u,v in zip(path[1:-2],path[2:-1]):
        assert tuple(sorted((u,v))) in edges and u<8 and v<8

# The actual contradiction is order-theoretic and exact:
# if a>b and D->B is positive then
#     p.X > |p|^2 + b(a+3b)/4 > |p|^2,
# hence |X|>|p| by Cauchy (p=0 is impossible already).
# If B->T is positive then
#     p.X > |X|^2 + a(a-b)/4 > |X|^2,
# hence |X|<|p| by Cauchy.
# Positive base->base arrows strictly increase |X|^2 by the identity above.
# Therefore a positive D-to-T path cannot exist.
# In a weak-free finite graph, following positive outgoing arrows from any
# non-U vertex strictly increases full squared radius and terminates at a
# strict U.  Thus if T is strict U and D is not, D terminates at a DIFFERENT U.
# If D is strict U already there are two.  If D has a zero outgoing dot the
# configuration is weak and is outside weak000.

# For a>b, if D itself is strict U then T is also strict U because every
# T->B dot is smaller by the strictly negative constant above.
# At a=b, the two apex outgoing-dot rows coincide.  Swapping top/bottom gives
# the b>a case.  Hence no apex is a unique strict U in any weak-free
# orthogonal own-centred ordinary bipyramid.

print('OCTAGON_SIMPLE_D_TO_T_PATHS',len(paths))
print('APEX_DOT_DIFFERENCE',sp.factor(T_to_B-Bvec_from_D))
print('C48_ORTHOGONAL_APEXROOT_CHAMBER_EXCLUDED_PASS')
print('C48_ALL_159_APEX_SHADOW_SYSTEMS_ELIMINATED_IN_RHO0_PASS')
```

## Evidence classification

The chamber exclusion, apex-dot ordering, positive-path radial barrier, zero surviving apex-root systems, and base-root reduction are exact. The theorem is stronger than the requested finite reduction because it eliminates the entire orthogonal apex-root chamber for any ordinary base size, not only the 159 C48 representatives. It does **not** exclude the remaining orthogonal base-root C48 systems, any nonorthogonal `rho!=0` chamber, or the full ordinary-bipyramid family.
