# figure-0500

Historical AI scientific report · saved 2026-09-23 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Clear Willow 56 — MORSE6 terminal-edge obstruction and an exact critical-apex continuation method

## Outcome

No new finite strict110/additionalweak000 polyhedron is verified in this handoff. The principal result is a rigorous obstruction to a natural **gradient-path polyhedralization of MORSE6**: sufficiently refined terminal stars formed from generic physical radial-gradient trajectories cannot have a unique unstable vertex at the actual finite-volume centroid. Refining those trajectories does not repair the last incoming edge.

The constructive consequence is explicit. The terminal edges need a different direction from the generic gradient approach, or the smooth maximum must be replaced by a sharpened apex. I derive an exact rational skew-meridian criterion for the former and a complete cubic/quartic actual-mass sign reduction for the latter. The reduction includes all strict and additional-weak S/U/H tests, allows equilibrium turnover, and does not freeze a physical escape tree.

The numerical submissions made during the unfinished execution do not have a retained terminal ledger or a replayed exact endpoint in the context available for this handoff. They are not reported as completed searches, exclusions, or accepted constructions. The durable successor here is the mathematical critical-star result and the source-complete exact continuation method, not an unobserved numerical body.

## 1. Sources and reading status

The complete new journal and all three supplied source files were read through EOF in the preceding execution segment. That reading is carried forward rather than restarted. The exact source identities are:

- `[internal-source-reference]`: complete `verify_morse6.py`, 5,289 bytes, SHA-256 `7c1af605fe40ec0ca1c7d3c623706dd0a518f5b9a070d84c20e152af959e2ea2`.
- `[internal-source-reference]`: MORSE6 theorem and observed parent replay manifest, 7,400 bytes, SHA-256 `4f7049ad41e6830c298512dbbe79d48eddb55e3e9e43ff8391fdcc6253225512`.
- `[internal-source-reference]`: complete `circle_family.py` finite auditor, 13,139 bytes, SHA-256 `81988ecb6ea4601709b7c0311332a48da6f1a7cb1171b19e2aadeb9f99039c68`.

The supplied journal is 277,322 bytes, SHA-256 `eb3fde2ca639aa3396dbd856a40ab4003a1801ff50d873e2535291918a45494f`.

The exact smooth parent remains MORSE6_RATIONAL_A7_100. In the notation of its source,

`y=x²`, `H(y)=(1-y)B(y)²`,

`K={(lambda*x,Y,Z): (Y-P(x²))²+(Z-xQ(x²))² <= H(x²)}`,

with `lambda=1029667/1000000`, `P(0)=a=7/100`, and `B(0)=1`. Its actual uniform centroid is zero, its unique smooth unstable point is `U=(0,107/100,0)`, and its unique smooth stable point is `S=(0,-93/100,0)`. It is invariant under `(X,Y,Z) -> (-X,Y,-Z)`. It is not a finite polyhedron. 

The prior C186, C330/C438 S1-first, and C486 U1-first families remain preserved in their earlier branch. None is relabelled as a new MORSE6 construction here. The coordinator's separately described paired-chain finite checkpoints were not supplied as exact inputs to this branch and are not reconstructed from their descriptions.

## 2. Why an increasing smooth radial trajectory does not supply its last polyhedral escape

For a convex polyhedron at its actual centroid g, a positive physical escape from v to w requires

`(v-g)·(w-v)>0`.

Strict increase of `|v-g|` along a smooth curve is not this condition. The exact identity is

`2(v-g)·(w-v)=|w-g|²-|v-g|²-|w-v|²`.

The radial increase must pay for the squared chord length. This becomes particularly restrictive at the terminal maximum.

### Exact local terminal cone

Let a smooth strictly convex C2-symmetric body have an axial radial maximum `U=(0,u,0)`. Write transverse coordinates as `w=(X,Z)`, and represent its boundary near U as

`Y=u-f(w)`,

`f(w)=1/2 wᵀK_U w+O(|w|⁴)`.

Here K_U is the positive second fundamental form in orthonormal transverse coordinates. The fourth-order remainder, rather than a third-order remainder, follows from the half-turn symmetry: the graph is even in w.

A finite C2-symmetric body's actual centroid has the form `g=(0,c,0)`. Put `R=u-c`. For a boundary point `v=(w,u-f(w))`, the incoming score to the unchanged smooth point U is exactly

`(v-g)·(U-v)=(R-f(w))f(w)-|w|²`,

and hence

`(v-g)·(U-v)=1/2 wᵀ(R K_U-2I)w+O(|w|⁴)`.

Thus the local incoming directions are governed by **R K_U−2I**, not by the radial Hessian **R K_U−I**. A direction can be a direction of strictly increasing smooth radius and still be unsuitable for the final polyhedral edge.

This distinction is actual-centroid dependent. The coefficient is `R=u-c`, where c is the finite body's mass coordinate, not an adjustable reference parameter.

## 3. A mass-coupled MORSE6 obstruction to generic gradient-terminal refinement

This result uses only exact properties of the supplied smooth parent, not unretained numerical samples.

### The slow terminal direction has curvature at most one

The section of MORSE6 by X=0 is exactly the unit circle

`Y=a+cos(theta)`, `Z=sin(theta)`.

At U its normal is the positive Y direction. Consequently the normal curvature in the transverse Z direction is exactly one. The smallest principal curvature therefore satisfies

`k_min <= 1`.

Because U is a nondegenerate maximum of squared radius about the smooth body's centroid zero,

`k_min > 1/u = 100/107`.

For the physical radial-gradient ascent on the smooth surface, the linearized decay rates at U are proportional to `u*k_i-1`. Generic trajectories approach along the smallest-principal-curvature eigendirection. With distinct eigenvalues, the exceptional fast approach is confined to the one-dimensional strong stable manifold. With equal eigenvalues, every terminal tangent direction has the same curvature, which is at most one.

### The finite centroid is bounded by retained volume

Let L be a full-dimensional, uniformly filled, C2-symmetric convex polyhedron contained in MORSE6. Suppose

`Vol(L) >= alpha Vol(K)`.

Its actual centroid is `(0,c,0)`. Since the smooth parent's first moment is zero and every point of K has Y coordinate at most u,

`c >= -u(1-alpha)/alpha`,

so

`R=u-c <= u/alpha`.

For the convenient exact choice `alpha=3/5`,

`c >= -107/150`, `R <= 107/60 < 2`.

The analogous upper centroid bound is `c<=31/50`, using the exact lower support Y=-93/100. These are finite uniform-volume estimates, not a choice of centre.

### Theorem: refined generic-flow terminal stars force a second strict U

Consider a sequence of full-dimensional C2-symmetric polyhedra L contained in MORSE6, containing the exact point U as a vertex, and retaining at least three fifths of the smooth volume. Assume every true neighbour of U lies sufficiently close to U on one of a fixed finite collection of generic physical radial-gradient trajectories approaching U.

Then **L has at least two strict unstable vertices at its own filled-volume centroid**.

Proof. Along each such trajectory, the limiting transverse direction has curvature at most one. The leading incoming form therefore satisfies

`1/2 wᵀ(R K_U-2I)w <= -13/120 |w|²`

in its limiting direction, uniformly over the allowed finite-centroid range. Continuity of the direction and the fourth-order graph remainder make every sufficiently terminal incoming score strictly negative. The same conclusion holds in an open angular cone around the slow eigendirection; exact membership on an ODE trajectory is unnecessary.

U itself is strict U: it is the unique highest-Y point, and `u-c>0`, so every outgoing dot from U is negative. Now choose a vertex v of maximal squared distance from g among all vertices other than U. Every edge from v to another vertex in that complement has strictly negative outgoing dot, by the squared-radius identity and distinctness of its endpoints. If v is adjacent to U, that outgoing dot is also strictly negative by the terminal-star hypothesis. Therefore v is a second strict U. This argument does not assume that the remaining vertices are weak-free.

The volume threshold can be replaced by any fixed `alpha>107/200`; three fifths gives a useful rational margin. This is a sufficient threshold derived from the central-circle curvature bound, not an optimal threshold for MORSE6.

### Scope

This excludes a specific convergent **gradient-terminal inscription architecture**, including sufficiently small perturbations of its terminal directions. It does not exclude all inscribed MORSE6 polyhedra, all adaptive meshes, all finite critical patches, or E<=249 constructions. In particular, a deliberately chosen fast terminal direction or an altered apex lies outside the theorem.

For any finite rational nomination, there is a directly checkable version requiring no integration of the smooth flow. Under the same three-fifths volume hypothesis, a neighbour `(X,Y,Z)` is certainly unable to escape to U whenever

`(Y+107/150)(107/100-Y)-X²-Z² < 0`.

This is the worst-centroid incoming score over the proved finite-mass range. Checking it for every true U-neighbour gives the same second-root certificate.

As an exact elementary check, the central-circle point

`v=(0,67/100,4/5)`

satisfies

`(v-g)·(U-v)=-(2/5)(c+93/100) <= -13/150`.

A central-circle neighbour cannot provide the missing incoming edge. A full-dimensional U1 star must obtain its incoming escape elsewhere.

## 4. Exact rational skew meridians for a different terminal patch

The obstruction identifies what the final edges must change. It is possible to formulate that change using the supplied rational MORSE6 oracle.

Let

`p1=P'(0)`, `q0=Q(0)`, `h1=H'(0)=2B'(0)-1`.

These are exact rational coefficients of the literal parent. In orthonormal transverse coordinates `(X,Z)`,

```text
K_U = [[(q0²-2p1-h1)/lambda², -q0/lambda],
       [-q0/lambda,                     1]].
```

For rational t and gamma, set

`x=2t/(1+t²)`, `rho=(1-t²)B(x²)/(1+t²)`, `s=gamma*t`,

`e1=(1-s²)/(1+s²)`, `e2=2s/(1+s²)`,

`v(t)=(lambda*x, P(x²)+rho*e1, xQ(x²)+rho*e2)`.

Every such point is rational and lies exactly on the smooth parent. Its terminal transverse tangent is proportional to

`w=(lambda,q0+gamma)`.

At an actual finite centroid `(0,c,0)`, the sign of the leading incoming score is the sign of the rational quadratic

`F(gamma;c)=(R-2)gamma²-4q0 gamma-R(2p1+h1)-2lambda²-2q0²`,

where `R=107/100-c`. More precisely,

`(v(t)-g)·(U-v(t)) = 2t² F(gamma;c)+O(t⁴)`.

For every interior axial centre of the parent, R<2, so this is a concave quadratic in gamma. Its maximizer, for a fixed infinitesimal X displacement, is

`gamma_*(c)=-2q0/(93/100+c)`.

At the smooth parent's centre zero this becomes

`gamma_*(0)=-200q0/93`.

By contrast, the centre-aligned relative-phase meridian has `gamma_aligned=q0/a=100q0/7`. The optimum incoming skew is therefore exactly

`gamma_*(0)=-(14/93) gamma_aligned`.

It reverses the centreline's initial twist. This is an optimization of the leading incoming score for fixed X displacement, not an assertion that it is the steepest intrinsic gradient direction.

A nonempty positive skew interval exists exactly when the maximum of F is positive, equivalently

`-R(2p1+h1)-2lambda²+2R q0²/(2-R)>0`.

I do not report an evaluated MORSE6 interval or an accepted finite point from this criterion: that numerical/exact evaluation has no retained execution receipt here. The formula itself is exact and supplies a compact rational test. When the strict interval is nonempty, rational gamma values inside it exist, and sufficiently small rational t give positive terminal edges at the tested centre.

For actual finite mass `(V,M_Y)`, the alignment equation is

`gamma*((93/100)V+M_Y)+2q0 V=0`.

The mass is not an independent control. Adding the terminal points changes V and M_Y, and the full finite body must satisfy the resulting coupled equation or strict incoming inequalities after reintegration.

## 5. A finite critical-patch architecture within the edge budget

A practical alternative is to replace the smooth maximum by a movable axial apex.

Take four bottom vertices at a common height b, whose transverse coordinates are `±u,±v` with u and v linearly independent. Add k other C2 pairs strictly above that plane, and a single axial point `A(h)=(0,h,0)` above all other vertices. Form their convex hull.

Its actual centroid lies on the Y axis. The bottom quadrilateral is always a strict stable facet, because the orthogonal foot is its centre. A(h) is always a strict unstable vertex, because every neighbour has smaller Y coordinate. These are genuine finite-body statements at the actual centroid.

There are at most `2k+5` vertices. The retained quadrilateral improves the usual simplicial edge bound by one:

`E <= 3V-7 <= 6k+8`.

Thus **k=40 gives E<=248, C<=496**. This is a guaranteed complexity and critical-carrier architecture, not a uniqueness theorem. Other stable and unstable equilibria are paired by C2; in a weak-free member the counts have the form

`S=1+2s`, `U=1+2u`, `H=2(s+u)`.

This structural principle overlaps the paired critical-patch ideas already recorded in the shared memory. The new ingredient here is the terminal-direction diagnosis and the complete actual-mass height reduction below, not a priority claim for C2 symmetry itself.

## 6. Complete cubic/quartic mechanics for an axial-apex height chart

Fix all other rational vertices and a labelled maximal complex in an open height interval. Incident apex facets are triangles; nonincident maximal polygons are fixed. Let the boundary be consistently oriented and triangulate fixed polygons only for integration.

The actual volume and first moment are

`V(h)=v1*h+v0`,

`M(h)=(0,m2*h²+m1*h+m0,0)`,

with the exact identity

`m2=v1/4`.

These follow directly from signed tetrahedral volume and first-moment formulas. The centroid is the rational quotient `M/V`; it is not held at the smooth parent's centre.

For a facet write its raw supporting plane as

`n_f(h)·x=b_f(h)`.

Both n_f and b_f are affine in h, and the Y component of n_f is constant. Define the volume-cleared centred support

`sigma_f(h)=V(h)b_f(h)-n_f(h)·M(h)`.

It has degree at most two. The centred polar point is

`q_f(h)=V(h)n_f(h)/sigma_f(h)`.

### Physical and polar primitive degrees

For a directed true physical edge i→j, use

`D_ij(h)=[V(h)v_i(h)-M(h)]·[v_j(h)-v_i(h)]`.

Its degree is at most three, and its sign is exactly the physical outgoing sign because V>0.

For adjacent facets f,g, use

`C_fg(h)=(n_f·n_g)sigma_f-(n_f·n_f)sigma_g`.

Its degree is at most four. Since the centred supports are positive,

`q_f·(q_g-q_f)=V² C_fg/(sigma_f² sigma_g)`.

No primitive-zero prohibition is introduced. Strict U means every incident D is negative; additional weak U means their maximum is zero. Strict S and additional weak S use the identical complete-maximum tests on the C rows.

### Mixed edges require no higher-degree event polynomial

Let physical edge i–j have adjacent facets f,g. Its perpendicular foot lies strictly inside the edge exactly when

`D_ij<0` and `D_ji<0`.

Its radial vector is a strictly positive combination of the two adjacent outward normals exactly when

`C_fg<0` and `C_gf<0`.

Therefore strict H is precisely the conjunction of these four negative signs. An additional weak edge equilibrium occurs when all four are nonpositive and at least one is zero. This is the complete segment-and-normal-cone test, not a facet-only surrogate.

Consequently every S/U/H and additional-weak event on the fixed maximal-complex height chart is a root of a polynomial of degree at most four. Identically zero rows remain zero and are classified through the complete maxima/conjunctions.

### Coverage and geometry changes

Factoring these rational polynomials, isolating all real roots in the interval, and sampling each intervening rational open cell decides the complete open mechanics arrangement. A weak-free110 point cannot exist only on a noncritical primitive-sign boundary: its strict equilibria and positive escape witnesses persist in a neighbourhood.

The full axial line can additionally be split at the rational hull events: every nontrivial four-point coplanarity determinant containing the moving apex is affine in h. At those rational events, rebuild the maximal hull separately; do not continue a triangulated chart through a maximal-face merger without auditing it. On each open hull interval the cubic/quartic result applies again.

This is an algorithmic completeness theorem. **No particular new MORSE6-derived height atlas is claimed to have been executed or excluded here.** The degree-four assertion concerns equilibrium signs, not the ordering of every persistence birth/death value; full P/Q landscapes must still be rebuilt at promoted endpoints.

## 7. Attempted numerical directions and limits

The unfinished numerical work submitted three related ideas: free C2 paired vertices with a planted bottom facet and axial apex; positive-reference chain coordinates with the actual scalar mass equation; and physical radial-gradient trajectories of MORSE6 with directed chord compression. The first implementation had an axial-root-loss failure before hard slab bounds were added. That is an implementation failure, not geometric evidence.

I have no retained terminal ledger or exact replay for the later submissions. In particular, I do not report their requested iteration budgets as completed, do not promote a low numerical loss, and do not infer that a sparse MORSE6 realization is impossible. The exact terminal-star theorem above is proved independently of those calls.

## 8. Self-contained exact continuation source

The following unit is an exact compiler, rational-point auditor, complete tied-level P/Q calculator and open-cell height enumerator for the labelled C2 apex chart. It uses SymPy1.14.0 for rational polynomial factorization and real-root isolation. All geometry and mechanics tests are exact.

It is supplied as **unexecuted continuation source in this handoff**. No new byte count, SHA-256 or observed terminal receipt is asserted. The built-in square-pyramid example is only a calibration input, not a research endpoint or an alleged MORSE6 realization. Its mass identity is `V=4(h+1)/3`, `M_Y=(h+1)(h-3)/3`; at h=3 its expected class is558/weak000.

Save as `critical_apex_atlas.py`. Commands:

```text
python -B critical_apex_atlas.py
python -B critical_apex_atlas.py rational_chart.json
```

The JSON input schema is demonstrated literally by the default input in the source. A new finite nomination must provide all rational vertices, all true maximal oriented face cycles, the axial apex index, and a rational height interval. The supplied complex is validated at every accepted rational sample. Geometry-boundary heights need a separately rebuilt complex, as stated above.

```python
from collections import defaultdict, deque
from pathlib import Path
import json
import sys
import sympy as s

h = s.Symbol('h', real=True)
R = s.Rational

def expand_vec(v):
    return v.applyfunc(s.expand)

def sign(x):
    x = s.cancel(x)
    if x == 0:
        return 0
    if x.is_positive:
        return 1
    if x.is_negative:
        return -1
    raise ArithmeticError('A rational sign was not resolved')

def packed(x):
    if isinstance(x, s.MatrixBase):
        return [packed(v) for v in x]
    if isinstance(x, s.Basic):
        return str(x)
    if isinstance(x, dict):
        return {str(k): packed(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [packed(v) for v in x]
    return x

def chord(a, b):
    d = b-a
    t = max(R(0), min(R(1), -a.dot(d)/d.dot(d)))
    p = a+t*d
    return s.cancel(p.dot(p))

def landscape(points, edges):
    rr = [s.cancel(p.dot(p)) for p in points]
    ww = [chord(points[i], points[j]) for i, j in edges]
    levels = defaultdict(list)
    for k, w in enumerate(ww):
        levels[w].append(k)
    parent = list(range(len(points)))
    peak = list(range(len(points)))
    members = [{i} for i in range(len(points))]
    bars = []
    ties = []
    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    for level in sorted(levels, reverse=True):
        current = levels[level]
        graph = defaultdict(set)
        for ei in current:
            a, b = [root(v) for v in edges[ei]]
            if a != b:
                graph[a].add(b)
                graph[b].add(a)
        seen = set()
        groups = []
        for a in sorted(graph):
            if a in seen:
                continue
            group = [a]
            seen.add(a)
            for b in group:
                for c in sorted(graph[b]):
                    if c not in seen:
                        seen.add(c)
                        group.append(c)
            groups.append(group)
        for group in groups:
            elder = max(group, key=lambda v: (rr[peak[v]], -peak[v]))
            ep = peak[elder]
            for old in sorted(group, key=lambda v: peak[v]):
                bp = peak[old]
                if old == elder or rr[bp] <= level:
                    continue
                comp = set(members[old])
                cut = [e for e in edges if (e[0] in comp) != (e[1] in comp)]
                death_edges = [edges[k] for k in current
                               if (edges[k][0] in comp) != (edges[k][1] in comp)]
                assert death_edges
                adj = [[] for _ in points]
                for (i, j), w in zip(edges, ww):
                    if w >= level:
                        adj[i].append(j)
                        adj[j].append(i)
                pred = {bp: None}
                todo = deque([bp])
                while todo and ep not in pred:
                    i = todo.popleft()
                    for j in sorted(adj[i]):
                        if j not in pred:
                            pred[j] = i
                            todo.append(j)
                assert ep in pred
                path = [ep]
                while path[-1] != bp:
                    path.append(pred[path[-1]])
                path.reverse()
                bars.append(dict(peak=bp, elder=ep, birth=rr[bp], death=level,
                    component=sorted(comp), cut=cut, path=path,
                    death_edges=death_edges,
                    all_edges_at_death=[edges[k] for k in current]))
            merged = set().union(*(members[g] for g in group))
            for g in group:
                parent[g] = elder
            members[elder] = merged
            peak[elder] = ep
        if len(current) > 1:
            ties.append(dict(level=level, edges=[edges[k] for k in current]))
    assert len({root(i) for i in range(len(points))}) == 1
    return dict(radii2=rr, edge_levels=ww, positive_bars=bars, tied_levels=ties)

class Chart:
    def __init__(self, data):
        self.data = data
        self.apex = int(data['apex'])
        self.v = [s.Matrix([R(str(z)) for z in p]) for p in data['vertices']]
        self.v[self.apex] = s.Matrix([0, h, 0])
        self.faces = [tuple(map(int, f)) for f in data['faces']]
        self.N = len(self.v)
        reflected = {tuple((-p[0], p[1], -p[2])) for p in self.v}
        assert reflected == {tuple(p) for p in self.v}
        assert len({tuple(p) for p in self.v}) == self.N
        assert set(i for f in self.faces for i in f) == set(range(self.N))
        assert len({tuple(sorted(f)) for f in self.faces}) == len(self.faces)
        self.owners = defaultdict(list)
        orientation = defaultdict(list)
        V = s.S(0)
        M = s.zeros(3, 1)
        self.normal = []
        self.offset = []
        self.geometry = []
        for fi, f in enumerate(self.faces):
            assert len(f) >= 3 and len(set(f)) == len(f)
            if self.apex in f:
                assert len(f) == 3
            a, b, c = [self.v[i] for i in f[:3]]
            n = expand_vec((b-a).cross(c-a))
            off = s.expand(n.dot(a))
            assert s.Poly(n[1], h).degree() <= 0
            self.normal.append(n)
            self.offset.append(off)
            self.geometry.append(s.expand(n.dot(n)))
            for j, p in enumerate(self.v):
                slack = s.expand(off-n.dot(p))
                if j in f:
                    assert slack == 0
                else:
                    assert slack != 0
                    self.geometry.append(slack)
            for k, i in enumerate(f):
                j = f[(k+1) % len(f)]
                l = f[(k+2) % len(f)]
                turn = s.expand(n.dot((self.v[j]-self.v[i]).cross(self.v[l]-self.v[j])))
                self.geometry.append(turn)
                e = tuple(sorted((i, j)))
                self.owners[e].append(fi)
                orientation[e].append(1 if i < j else -1)
            for k in range(1, len(f)-1):
                a, b, c = [self.v[i] for i in (f[0], f[k], f[k+1])]
                dv = s.expand(a.dot(b.cross(c))/6)
                V += dv
                M += dv*(a+b+c)/4
        self.V = s.expand(V)
        self.M = expand_vec(M)
        assert self.M[0] == self.M[2] == 0
        assert s.Poly(self.V, h).degree() <= 1
        assert s.Poly(self.M[1], h).degree() <= 2
        assert s.expand(self.M[1]).coeff(h, 2) == self.V.coeff(h, 1)/4
        self.edges = sorted(self.owners)
        assert all(len(self.owners[e]) == 2 and sum(orientation[e]) == 0
                   for e in self.edges)
        assert self.N-len(self.edges)+len(self.faces) == 2
        self.sigma = [s.expand(self.V*b-n.dot(self.M))
                      for n, b in zip(self.normal, self.offset)]
        assert all(s.Poly(z, h).degree() <= 2 for z in self.sigma)
        self.geometry += [self.V] + self.sigma
        self.P = {}
        self.Q = {}
        self.pa = [[] for _ in self.v]
        self.qa = [[] for _ in self.faces]
        for i, j in self.edges:
            for a, b in ((i, j), (j, i)):
                z = s.expand((self.V*self.v[a]-self.M).dot(self.v[b]-self.v[a]))
                assert z == 0 or s.Poly(z, h).degree() <= 3
                self.P[a, b] = z
                self.pa[a].append((a, b))
            f, g = self.owners[i, j]
            for a, b in ((f, g), (g, f)):
                na, nb = self.normal[a], self.normal[b]
                z = s.expand(na.dot(nb)*self.sigma[a]-na.dot(na)*self.sigma[b])
                assert z == 0 or s.Poly(z, h).degree() <= 4
                self.Q[a, b] = z
                self.qa[a].append((a, b))
        self.qedges = sorted({tuple(sorted(v)) for v in self.owners.values()})
        assert len(self.qedges) == len(self.edges)

    def evaluate(self, t, with_landscapes=False):
        t = R(t)
        ev = lambda p: s.cancel(p.subs(h, t))
        if not all(sign(ev(p)) > 0 for p in self.geometry):
            return None
        V = ev(self.V)
        M = self.M.subs(h, t)
        c = M/V
        raw = [p.subs(h, t) for p in self.v]
        x = [p-c for p in raw]
        q = [expand_vec(V*n.subs(h, t)/ev(z))
             for n, z in zip(self.normal, self.sigma)]
        assert len({tuple(p) for p in q}) == len(q)
        pd = {e: sign(ev(z)) for e, z in self.P.items()}
        qd = {e: sign(ev(z)) for e, z in self.Q.items()}
        U = [i for i, es in enumerate(self.pa) if max(pd[e] for e in es) < 0]
        wU = [i for i, es in enumerate(self.pa) if max(pd[e] for e in es) == 0]
        S = [i for i, es in enumerate(self.qa) if max(qd[e] for e in es) < 0]
        wS = [i for i, es in enumerate(self.qa) if max(qd[e] for e in es) == 0]
        H = []
        wH = []
        for i, j in self.edges:
            f, g = self.owners[i, j]
            z = [pd[i, j], pd[j, i], qd[f, g], qd[g, f]]
            if max(z) < 0:
                H.append((i, j))
            elif max(z) == 0:
                wH.append((i, j))
        weak = [wS, wU, wH]
        if not any(weak):
            assert len(S)+len(U)-len(H) == 2
        result = dict(height=t, volume=V, first_moment=M, centroid=c,
            raw_vertices=raw, vertices=x, faces=self.faces, edges=self.edges,
            edge_faces=[self.owners[e] for e in self.edges], polar=q,
            polar_edges=self.qedges, S=S, U=U, H=H, additional_weak=weak,
            physical_signs=[[a, b, pd[a, b]] for a, b in sorted(pd)],
            polar_signs=[[a, b, qd[a, b]] for a, b in sorted(qd)])
        if with_landscapes:
            result['P_landscape'] = landscape(x, self.edges)
            result['Q_landscape'] = landscape(q, self.qedges)
            if not any(weak):
                assert len(result['P_landscape']['positive_bars']) == len(U)-1
                assert len(result['Q_landscape']['positive_bars']) == len(S)-1
        return result

    def atlas(self, left, right):
        left, right = R(left), R(right)
        assert left < right
        factors = {}
        rows = self.geometry + list(self.P.values()) + list(self.Q.values())
        for row in rows:
            if row == 0:
                continue
            for f, multiplicity in s.factor_list(row, h)[1]:
                p = s.Poly(f, h, domain=s.QQ).monic()
                if p.degree() == 0:
                    continue
                assert p.degree() <= 4
                key = tuple(p.all_coeffs())
                factors[key] = p
        bits = 16
        while True:
            roots = []
            ambiguous = False
            for key in sorted(factors, key=str):
                p = factors[key]
                for (a, b), multiplicity in p.intervals(eps=R(1, 2**bits)):
                    if b <= left or a >= right:
                        continue
                    if not left < a or not b < right:
                        ambiguous = True
                    roots.append((a, b, key))
            roots.sort(key=lambda z: (z[0], z[1], str(z[2])))
            if any(roots[i][1] >= roots[i+1][0] for i in range(len(roots)-1)):
                ambiguous = True
            if not ambiguous:
                break
            bits *= 2
        boundaries = [(left, left, ())] + roots + [(right, right, ())]
        cells = []
        for a, b in zip(boundaries, boundaries[1:]):
            sample = (a[1]+b[0])/2
            audit = self.evaluate(sample, with_landscapes=True)
            cells.append(dict(left_root=a, right_root=b, sample=sample,
                              valid_maximal_complex=audit is not None, audit=audit))
        return dict(interval=[left, right], factor_coefficients=list(factors),
                    isolating_bits=bits, roots=roots, open_cells=cells,
                    identically_zero_physical=[e for e, p in self.P.items() if p == 0],
                    identically_zero_polar=[e for e, p in self.Q.items() if p == 0])

DEFAULT = {
    'vertices': [['-1','-1','-1'], ['-1','-1','1'],
                 ['1','-1','1'], ['1','-1','-1'], ['0','0','0']],
    'apex': 4,
    'faces': [[0,3,2,1], [4,0,1], [4,1,2], [4,2,3], [4,3,0]],
    'interval': ['0','6']
}

def main():
    data = json.loads(Path(sys.argv[1]).read_text()) if len(sys.argv) > 1 else DEFAULT
    chart = Chart(data)
    if len(sys.argv) == 1:
        assert s.expand(chart.V-4*(h+1)/3) == 0
        assert s.expand(chart.M[1]-(h+1)*(h-3)/3) == 0
        test = chart.evaluate(R(3), with_landscapes=True)
        assert [len(test[k]) for k in ('S','U','H')] == [5,5,8]
        assert not any(test['additional_weak'])
        print('SQUARE_PYRAMID_CALIBRATION_558_WEAK000')
    result = chart.atlas(*data['interval'])
    result['volume_polynomial'] = chart.V
    result['moment_polynomial'] = chart.M
    result['physical_polynomials'] = [[a,b,z] for (a,b),z in sorted(chart.P.items())]
    result['polar_polynomials'] = [[a,b,z] for (a,b),z in sorted(chart.Q.items())]
    Path('critical_apex_atlas.json').write_text(
        json.dumps(packed(result), sort_keys=True, separators=(',',':'))+'\n')
    print('CRITICAL_APEX_CUBIC_QUARTIC_OPEN_ATLAS_COMPLETE', len(result['open_cells']))

if __name__ == '__main__':
    main()
```

## 9. Continuation priority

The next finite realization should not terminate all its ascent tracks along generic MORSE6 gradient approaches to the unchanged smooth U. Use the exact skew-meridian quadratic to nominate deliberately different terminal edges, or sharpen the apex and decide its actual-mass cubic/quartic height chart. Retain a single horizontal C2 stable facet, use the scalar volume moment rather than a freely chosen centre, and rebuild both whole landscapes after each accepted finite change.

The current accepted exact parent for this branch remains the supplied smooth MORSE6 source. No finite checkpoint, complete height-chart exclusion, numerical optimum, or observed new replay receipt is asserted beyond the proofs and source explicitly given above.
