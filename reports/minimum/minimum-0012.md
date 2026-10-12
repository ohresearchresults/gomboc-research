# minimum-0012

AI research report · 2026-09-07 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# C30_ADAPTED_ACTUAL_MASS_v2

## Result and status

I obtained a complete actual-volume formulation of the entire remaining C30 boundary in **14–16 real variables, with at most two cubic-or-lower incidence equations**. The formulation retains one arbitrary physical primal metric and its exact reciprocal dual metric, genuine vertices and maximal facets, the complete four-component edge exclusions, and every strict positive margin. It is necessary and sufficient for an actual C30 attainer, not merely for a free-weight or independent-metric relaxation.

I did **not** obtain a universal C30 exclusion or an exact C30 attainer. All 74 combinatorial types remain in the certified frontier below. No minimum larger than C30 is asserted. The substantive successor is the globally valid, substantially reduced, actual-volume-complete finite frontier and its reconstruction/verification program.

The most useful structural subdivision is:

| Primal degree multiset | Number of maps | Guaranteed maximum real variables | Guaranteed maximum incidence equations |
|---|---:|---:|---:|
| 3,3,3,3,3,3,4,4,4 | 47 | 16 | 2, each of degree at most 3 |
| 3,3,3,3,3,3,3,4,5 | 24 | 15 | 1, of degree at most 3 |
| 3,3,3,3,3,3,3,3,6 | 3 | 14 | 0 |

The program optimizes the corner within each map and can improve on the first two row-wise bounds. The three degree-six maps have a complete 14-variable formulation consisting entirely of strict polynomial inequalities, the inherited non-strict radius inequalities, and Boolean combinations of polynomial sign tests. No residual incidence equality is needed there.

The high polynomial degrees introduced by eliminating coordinates and mass are a tradeoff: the degree bound is 121 before the inherited radius cuts and 125 after including them. This is a reduction in continuous variables and low-degree incidence equations, not a claim that every resulting CAD or SMT computation is easy.

## Authority and scope

The lower-bound inputs are the immutable results:

- `minimum-0006`, SHA-256 `4480a792dec44a82e252175c8263360cd2cac11c705c881fe30da85b47087f08`: V >= 9.
- `minimum-0003`, SHA-256 `520200e9b9541f54133e00931fc6ce2021fa752d2e8bb06df574ed1248720893`: F >= 8.
- `minimum-0001`, SHA-256 `9cc634b1d007b03568764c4b4703096fe7216e39fbe9e0f5ea78b1ca4326a4f8`: the inherited actual-centroid and joint110 consequences, including R/r <= 27.

The matrix/mass input is the literal captured `AFFINE-MASS-8-v1` source, **22,204 bytes**, SHA-256:

`0ee887227b9259b90d956baa5e6f0b94535c8cb35fc39700fc87f19b8b3250f1`.

The reconstruction program loads that exact source from the journal and authenticates it before using its combinatorial routines. It does not run its old physical eight-vertex instances. The eight-vertex graphs used below are only combinatorial dual maps: their nine faces become the nine primal vertices. Every new physical system has **V=9, E=15, F=8**, never V=8, E=15, F=9. No volume-centroid condition is imposed on the eight polar vertices.

Euler's equation and the two new lower bounds leave exactly V=9,F=8 at E=15. Thus covering these maps covers the whole remaining C30 boundary. I found no relevant semantic conflict among the authoritative inputs; older weaker bounds are superseded, not contradictory.

## 1. Global adapted-corner gauge

Let c be a simple vertex, with its three neighbors ordered as a0,a1,a2. Use the affine chart

`c = 0, a0 = e0, a1 = e1, a2 = e2`.

This chart exists in every realization: the three edge directions at a simple vertex of a full-dimensional three-polytope are linearly independent. It does not make those directions physically orthogonal. The physical inner product remains an arbitrary positive-definite matrix M.

The three facets through c become coordinate planes, with inequalities `-xj <= 0`. Normalize each of the other five facets as `nf dot x <= 1`; this uses a positive normalization because c is strictly off each such facet.

For every neighbor aj and every non-corner facet f containing it, set `nf[j]=1`. These are distinct coefficient slots and hence independent eliminations of scalar variables.

Write

`s(c) = sum(deg(a)-3 : a is a neighbor of c)`.

There are `3+s(c)` fixed coefficient slots among the fifteen coefficients of the five non-corner normals. Therefore there are `12-s(c)` free shape coefficients. Normalize the irrelevant common physical scale by `M00=1`, leaving five physical metric coefficients. The total is

`17-s(c)` real variables.

Choose c to maximize s(c), breaking ties by vertex label. Since the total degree surplus is `2E-3V=3`, one has `1 <= s(c) <= 3`. A maximum-degree vertex has a simple neighbor: there are at most three nonsimple vertices, whereas its degree is at least four. Consequently the maximizing corner satisfies `s(c) >= max_degree-3`, proving the table above.

For each of the five non-frame vertices choose the first three incident facets in label order and reconstruct the vertex by Cramer's rule. This fixed choice does not omit a rank stratum. Indeed, at a genuine vertex, cross-section the normal cone by a plane strictly positive on all its generating facet normals. The normalized incident normals are vertices of a strictly convex polygon. Any three are affinely independent: three collinear extreme points would put one between the other two. Thus any three distinct incident facet normals are linearly independent.

All incidences of c and its neighbors are already identities. The remaining number of incidence equations is exactly

`sum(deg(v)-3 : v is not c or one of its three neighbors) = 3-s(c)`.

For a reconstructed vertex `u/d`, an additional incidence is `nf dot u - hf*d = 0`, of degree at most three. I do not assume that these remaining equations are independent on every algebraic component.

## 2. Actual solid mass, with every denominator sign retained

For each non-frame vertex let `xi=ui/di` be its Cramer representation. For frame vertices use denominator one. Define the common, potentially negative denominator

`Delta = product(di)`

and polynomial coordinate numerators `Xi` satisfying `xi=Xi/Delta`.

For an outward-oriented triangulation of the maximal facets define

`Dt = det(Xa,Xb,Xc)`;

`W = sum(Dt)`;

`B = sum(Dt*(Xa+Xb+Xc))`;

`K = 4*Delta*W`;

`Zi = 4*W*Xi-B`.

The actual homogeneous centroid and centered vertices are

`g = B/K`,  `pi = Zi/K`.

This is the ordinary exact boundary volume-moment formula, not an affine-weight surrogate. The raw chart origin is a boundary vertex, so its incident facet cones can have zero volume. Those raw cones are used only in the boundary moment formula; they are not incorrectly installed as positive entries of T.

Let Wraw denote the outward raw-coordinate determinant sum. Then

`W = Delta^3*Wraw`,  `K = 4*Delta^4*Wraw > 0`.

Thus no sign choice for Delta is needed. The system guards every `di != 0` by `di^2>0`, tests nonincidence support by multiplying by Delta, and requires `W*Delta>0`. It covers arbitrarily small nonzero denominators of either sign.

Changing the physical metric corresponds to an invertible affine transformation of the chart. Its Jacobian is a common constant for all volume integrals. Consequently the actual centroid and relative cone masses transform affinely and do not acquire an independent dependence on M. Computing g before choosing M is therefore legitimate for homogeneous solid mass.

For each facet define

`sf = hf*K - nf dot B > 0`,  `qf = K*nf/sf`.

Then `Lf,i` in conventional vertex-by-facet order is `Lif=1-pi dot qf`. The system also includes the inherited strict nonpyramidal bound `Lif<4` at every nonincidence, equivalently `3*sf+nf dot Zi>0`. A nine-vertex pyramid would have an apex of degree eight, impossible at this boundary, whose maximum degree is six.

## 3. One physical metric and complete joint110 conditions

Use

`M = [[1,m01,m02],[m01,m11,m12],[m02,m12,m22]]`.

The two remaining Sylvester conditions are imposed strictly. The physical Gram matrices are exactly

`Gij = pi^T M pj`,  `Hfg = qf^T M^(-1) qg`.

There is no independently chosen dual metric.

For every genuine edge ij separating maximal facets f,g, use the polynomial scores

`Pij = Zi^T M (Zj-Zi)`;

`Dfg = nf^T adj(M) (sf*ng-sg*nf)`.

Their signs are exactly the physical escape signs, because

`Gij-Gii = Pij/K^2`;

`Hfg-Hff = K^2*Dfg / (det(M)*sf^2*sg)`.

All displayed denominators are positive. Each edge receives the full exclusion

`Pij>0 OR Pji>0 OR Dfg>0 OR Dgf>0`.

The unique primal root has all incident P scores negative; every other vertex has at least one positive incident P score. The analogous condition is imposed on the eight polar vertices using D. These are the complete strict U=1,S=1,H=0 tests. Zero scores not representing an equilibrium remain allowed; no global genericity condition or fixed tolerance is introduced.

The inherited joint110 radius bound is also included. For all i,f it becomes the polynomial inequality

`(Zi^T M Zi)*(nf^T adj(M) nf) <= 729*det(M)*sf^2`.

This is the all-pairs consequence of `R/r<=27`. Its non-strict boundary is retained.

Conversely, any real solution defines nine points whose stated facets are genuine maximal supporting facets and whose stated vertices are genuine extreme vertices. The strict facet-polygon tests, nonincidence slacks, and three independent active planes at every reconstructed vertex establish the listed boundary. The listed facets form a closed boundary across all their genuine edges, so no extra facet can be hidden. Applying a factor Bphys with `Bphys^T Bphys=M` to the centered chart produces a homogeneous physical polyhedron with precisely the asserted strict equilibria. Therefore these systems are **sufficient as well as necessary**.

## 4. Nine-vertex actual-mass/slack compatibility

Every one of the 74 maps admits a triangulation into fourteen triangles whose adjacency across genuine edges is connected. A spanning tree has thirteen edges. The deterministic first successful triangulation occurs at trial numbers with histogram

`1:35, 2:30, 3:5, 4:3, 5:1`.

The six added triangulation diagonals form a forest; the recovery program checks this independently.

The exact checkpoint is `first_frontier.json`, **27,025 bytes**, SHA-256

`613ce3d88285e2c8faf2f41e08ee705ce279ec11430c6efbaf35b60273da925f`.

It contains all 74 complete facet-cycle arrays, all fourteen-triangle arrays, all thirteen-edge spanning trees, the degree multisets, and the trial indices. Its map identifier is the canonical edge bitmask of the eight-vertex dual graph; the physical vertex labels are its nine face indices.

For triangle t=(a,b,c) in facet f and adjacent triangle u=(b,a,d) in facet g across a genuine edge,

`omega[t]*L[d,f] = omega[u]*L[c,g] > 0`.

Starting with beta[0]=1 and propagating these ratios along the stored spanning tree determines all beta values positively; normalizing gives omega. The actual centered cone determinants satisfy the same ratios. Hence these thirteen equations force the normalized weights to be the actual solid-volume weights, not merely common affine weights.

With `T[f,i]=sum(omega[t] : t lies in f and contains i)`, the complete system consequently has

`L*T*L + L = 4*J`,  `rank(L)=4`,  `rank(J-L)=3`,  `G*T^T*H = J-L`.

In the reduced formulation the centroid and omega are computed from the actual solid, so these identities are consequences rather than additional free-variable equations. This is the point at which the false-mass and independent-dual-metric relaxations are eliminated.

## 5. Exact nine-vertex control, including a negative denominator

The recovery program uses the following complete rational polyhedron:

`V=[(0,0,0),(8,0,0),(0,8,0),(1,1,4),(5,1,4),(1,5,4),(1,1,-4),(5,1,-4),(1,5,-4)]`.

Its outward facet cycles are

`[(3,4,5),(6,8,7),(0,1,4,3),(1,2,5,4),(2,0,3,5),(1,0,6,7),(2,1,7,8),(0,2,8,6)]`.

Its volume is `448/3`, its actual centroid is `(71/28,71/28,0)`, its raw determinant sum is `896`, and its raw fourfold first-moment numerator is `(9088,9088,0)`.

The adapted chart chooses corner 3 with neighbors `(0,4,5)`. It has sixteen variables and two incidence equations. The chart centroid is `(1,71/112,71/112)` and its physical metric is

`[[1,-2/9,-2/9],[-2/9,8/9,0],[-2/9,0,8/9]]`, with determinant `512/729`.

Crucially, the fixed Cramer choices give

`Delta=-1/4`, `W=-7/32`, `K=7/32`, `B=(7/32,71/512,71/512)`.

Thus the control tests the negative-Delta branch, not just a positive-denominator chart. It also tests a genuinely non-diagonal physical metric. The exact verification checks the actual volume, coordinate recovery, all geometric guards, both ranks, LTL+L, all thirteen positive mass balances, the correctly transposed metric coupling, and both score-denominator identities.

All thirty directed primal edge scores of this control are negative. It has U=9 and is explicitly **not** an attainer.

## 6. Recovery capsule

The following is a complete load/append patch against the authenticated 22,204-byte captured AFFINE source. That parent source is already literal in the supplied journal. No sandbox object or numerical solver output is required to reconstruct the accepted successor.

Dependencies: CPython 3.13.5; standard library only. Assertions must remain enabled. The program does not invoke a SAT, SMT, CAD, floating-point geometry, or semidefinite solver.

Reconstruction command:

`python3 -S c30_adapted_recovery.py 'research-journal(20260907-093308).md' --emit-smt`

The command reconstructs and verifies the fixed 27,025-byte checkpoint, writes all 74 complete polynomial SMT-LIB instances, and writes a manifest containing every instance's exact variable/equation count, corner, neighbor order, surplus, degree bound, byte count, and SHA-256. Written instance bytes are read back and checked. The source's own byte count and SHA-256 are printed as well.

Expected terminal markers include `C30_NEGATIVE_DELTA_ACTUAL_MASS_METRIC_CONTROL_PASS`, `C30_ALL_74_TRUE_EDGE_FORESTS_PASS`, `C30_ALL_74_ACTUAL_VOLUME_COMPLETE_SYSTEMS_PASS`, and `C30_NO_SAT_OR_UNSAT_VERDICT`.

```python
from fractions import Fraction as F
from itertools import product
from collections import Counter, defaultdict
from pathlib import Path
import hashlib, json, sys

assert __debug__
NL = chr(10)
assert len(sys.argv) >= 2, 'Supply the journal as the first argument'
journal = Path(sys.argv.pop(1)).read_text(encoding='utf-8')
a = journal.index('# AFFINE-MASS-8-v1:')
a = journal.index('```python' + NL, a) + 10
code = journal[a:journal.index(NL + '```', a)] + NL
assert len(code.encode()) == 22204
assert hashlib.sha256(code.encode()).hexdigest() == '0ee887227b9259b90d956baa5e6f0b94535c8cb35fc39700fc87f19b8b3250f1'
parent = {'__name__': 'captured_affine_parent'}
exec(compile(code, '<captured-AFFINE-MASS-8-v1>', 'exec'), parent)
edges, spheres, allgraphs, triang = (parent[k] for k in ('edges', 'spheres', 'allgraphs', 'triang'))


def dual8(faces):
    out = []
    for v in range(8):
        nxt = {}
        for f, c in enumerate(faces):
            if v not in c:
                continue
            b = c[(c.index(v) + 1) % len(c)]
            other = [j for j, d in enumerate(faces) if j != f and v in d and b in d]
            assert len(other) == 1
            nxt[f] = other[0]
        first = min(nxt)
        cycle = [first]
        while nxt[cycle[-1]] != first:
            cycle.append(nxt[cycle[-1]])
        assert set(cycle) == set(nxt)
        out.append(tuple(cycle))
    spheres(tuple(out), 9)
    return tuple(out)


def picktri(faces):
    true = set(edges(faces))
    for trial, parts in enumerate(product(*(triang(c) for c in faces)), 1):
        ts = sum(parts, ())
        uses = spheres(ts, 9)
        adj = defaultdict(list)
        for e, ls in uses.items():
            if e in true:
                t, u = ls[0][0], ls[1][0]
                adj[t].append(u)
                adj[u].append(t)
        seen, todo, span = {0}, [0], []
        for t in todo:
            for u in sorted(adj[t]):
                if u not in seen:
                    seen.add(u)
                    todo.append(u)
                    span.append((t, u))
        if len(seen) != 14:
            continue
        assert len(span) == 13
        ds = set(edges(ts)) - true
        par = list(range(9))
        def root(i):
            while par[i] != i:
                i = par[i]
            return i
        for x, y in sorted(ds):
            x, y = root(x), root(y)
            assert x != y
            par[x] = y
        assert len(ds) == 6
        return ts, span, trial
    raise AssertionError('No connected genuine-edge triangle graph')


def frontier():
    out = []
    for mask, old in sorted(allgraphs().items()):
        if len(edges(old)) != 15:
            continue
        fs = dual8(old)
        ts, span, trial = picktri(fs)
        es = edges(fs)
        out.append(dict(mask=mask, faces=fs, triangles=ts, span=span, trial=trial,
                        degree=sorted(sum(i in e for e in es) for i in range(9))))
    assert len(out) == 74
    assert Counter(tuple(g['degree']) for g in out) == {
        (3,3,3,3,3,3,4,4,4): 47,
        (3,3,3,3,3,3,3,4,5): 24,
        (3,3,3,3,3,3,3,3,6): 3}
    assert Counter(g['trial'] for g in out) == {1:35, 2:30, 3:5, 4:3, 5:1}
    return out


class Algebra:
    def __init__(self):
        self.variables, self.nodes, self.guards, self.booleans = [], [], [], []
        self.degrees = {}
    def real(self, name):
        assert name not in self.degrees
        self.variables.append(name)
        self.degrees[name] = 1
        return name
    def degree(self, x):
        return 0 if x.isdecimal() else self.degrees[x]
    def node(self, op, args):
        name = 'z' + str(len(self.nodes))
        ds = [self.degree(x) for x in args]
        self.nodes.append((name, op, tuple(args)))
        self.degrees[name] = sum(ds) if op == '*' else max(ds, default=0)
        return name
    def add(self, *args):
        args = [x for x in args if x != '0']
        return '0' if not args else args[0] if len(args) == 1 else self.node('+', args)
    def mul(self, *args):
        if '0' in args:
            return '0'
        args = [x for x in args if x != '1']
        return '1' if not args else args[0] if len(args) == 1 else self.node('*', args)
    def sub(self, a, b):
        return '0' if a == b else a if b == '0' else self.node('-', [a, b])
    def neg(self, a):
        return self.sub('0', a)
    def dot(self, a, b):
        return self.add(*(self.mul(x, y) for x, y in zip(a, b)))
    def cross(self, a, b):
        return [self.sub(self.mul(a[1],b[2]),self.mul(a[2],b[1])),
                self.sub(self.mul(a[2],b[0]),self.mul(a[0],b[2])),
                self.sub(self.mul(a[0],b[1]),self.mul(a[1],b[0]))]
    def det(self, a, b, c):
        return self.dot(a, self.cross(b, c))
    def vsub(self, a, b):
        return [self.sub(x, y) for x, y in zip(a, b)]
    def guard(self, op, x, tag):
        self.guards.append((op, x, tag))
    def evaluate(self, values):
        assert set(values) == set(self.variables)
        env = {k:F(v) for k,v in values.items()}
        def val(x):
            return F(int(x)) if x.isdecimal() else env[x]
        for name, op, args in self.nodes:
            xs = [val(x) for x in args]
            if op == '+':
                v = sum(xs)
            elif op == '-':
                v = xs[0] - xs[1]
            else:
                v = F(1)
                for x in xs:
                    v *= x
            env[name] = v
        return val
    def smt(self, label):
        out = ['; C30_ADAPTED_ACTUAL_MASS_v2 ' + str(label),
               '; Actual solid mass and one reciprocal metric; no solver verdict.',
               '(set-logic QF_NRA)']
        out += ['(declare-fun ' + v + ' () Real)' for v in self.variables]
        out += ['(define-fun '+n+' () Real ('+op+' '+' '.join(xs)+'))'
                for n,op,xs in self.nodes]
        out += ['(assert ('+op+' '+x+' 0))' for op,x,tag in self.guards]
        out += ['(assert '+x+')' for x in self.booleans]
        out += ['(check-sat)', '(exit)']
        return (NL.join(out) + NL).encode('ascii')


def bop(op, parts):
    parts = list(parts)
    assert parts
    return parts[0] if len(parts) == 1 else '('+op+' '+' '.join(parts)+')'
def positive(x):
    return '(> '+x+' 0)'
def negative(x):
    return '(< '+x+' 0)'


def corner_system(g):
    fs = tuple(tuple(f) for f in g['faces'])
    es = sorted(edges(fs))
    inc = [[f for f,c in enumerate(fs) if i in c] for i in range(9)]
    neighbors = lambda v: sorted(b if a == v else a for a,b in es if v in (a,b))
    score = lambda v: sum(len(inc[w])-3 for w in neighbors(v))
    c = min((i for i in range(9) if len(inc[i]) == 3), key=lambda i:(-score(i),i))
    surplus = score(c)
    assert 1 <= surplus <= 3
    nbr = neighbors(c)
    axis = {v:j for j,v in enumerate(nbr)}
    cf = set(inc[c])
    chosen = [min(f for f in inc[v] if f not in cf) for v in nbr]
    fixed = {(f,j) for j,v in enumerate(nbr) for f in inc[v] if f not in cf}
    assert len(fixed) == 3 + surplus
    A, N, h, slots = Algebra(), [], [], {}
    for f, cyc in enumerate(fs):
        if f in cf:
            missing = [axis[v] for v in nbr if v not in cyc]
            assert len(missing) == 1
            N.append([A.neg('1') if j == missing[0] else '0' for j in range(3)])
            h.append('0')
        else:
            row = []
            for j in range(3):
                if (f,j) in fixed:
                    row.append('1')
                else:
                    name = A.real('n'+str(f)+'_'+str(j))
                    slots[name] = (f,j)
                    row.append(name)
            N.append(row)
            h.append('1')
    assert len(slots) == 12 - surplus
    M = [['1',A.real('m01'),A.real('m02')],
         [None,A.real('m11'),A.real('m12')],
         [None,None,A.real('m22')]]
    M[1][0], M[2][0], M[2][1] = M[0][1], M[0][2], M[1][2]
    adj = [[None]*3 for _ in range(3)]
    for j in range(3):
        for k in range(3):
            rr = [r for r in range(3) if r != k]
            ss = [s for s in range(3) if s != j]
            z = A.sub(A.mul(M[rr[0]][ss[0]],M[rr[1]][ss[1]]),
                      A.mul(M[rr[0]][ss[1]],M[rr[1]][ss[0]]))
            adj[j][k] = A.neg(z) if (j+k)%2 else z
    dm = A.det(*M)
    A.guard('>',A.sub(M[1][1],A.mul(M[0][1],M[0][1])),'SPD')
    A.guard('>',dm,'SPD')
    U, den, extra = [], [], []
    for v in range(9):
        if v == c:
            ids, u, d = sorted(cf), ['0']*3, '1'
        elif v in axis:
            j = axis[v]
            ids = sorted(f for f in cf if v in fs[f]) + [chosen[j]]
            u, d = ['1' if k == j else '0' for k in range(3)], '1'
        else:
            ids = inc[v][:3]
            r0,r1,r2 = [N[f] for f in ids]
            hs = [h[f] for f in ids]
            d = A.det(r0,r1,r2)
            u0,u1,u2 = A.cross(r1,r2),A.cross(r2,r0),A.cross(r0,r1)
            u = [A.add(A.mul(hs[0],u0[k]),A.mul(hs[1],u1[k]),A.mul(hs[2],u2[k])) for k in range(3)]
            A.guard('>',A.mul(d,d),'chart')
        assert len(ids) == len(set(ids)) == 3
        for f in inc[v]:
            if f not in ids and v != c and v not in axis:
                z = A.sub(A.dot(N[f],u),A.mul(h[f],d))
                extra.append(z)
                A.guard('=',z,'incidence')
        U.append(u)
        den.append(d)
    assert len(extra) == 3-surplus
    assert max((A.degree(x) for x in extra), default=0) <= 3
    Delta = A.mul(*den)
    X = [[A.mul(u,A.mul(*(den[j] for j in range(9) if j != i))) for u in U[i]] for i in range(9)]
    for i in range(9):
        for f in range(8):
            if f not in inc[i]:
                A.guard('>',A.mul(A.sub(A.mul(h[f],Delta),A.dot(N[f],X[i])),Delta),'support')
    f = min(cf)
    cyc = fs[f]
    k = cyc.index(c)
    aa,bb = axis[cyc[k-1]],axis[cyc[(k+1)%len(cyc)]]
    missing = next(j for j in range(3) if j not in (aa,bb))
    sign = -(1 if (bb,aa,missing) in ((0,1,2),(1,2,0),(2,0,1)) else -1)
    if sign < 0:
        fs = tuple(tuple(reversed(f)) for f in fs)
    ts = tuple(tuple(t) if sign > 0 else (t[0],t[2],t[1]) for t in g['triangles'])
    fi = [next(f for f,cyc in enumerate(fs) if set(t) <= set(cyc)) for t in ts]
    for f,cyc in enumerate(fs):
        for a,b in zip(cyc,cyc[1:]+cyc[:1]):
            for d in cyc:
                if d not in (a,b):
                    A.guard('>',A.dot(N[f],A.cross(A.vsub(X[b],X[a]),A.vsub(X[d],X[a]))),'polygon')
    Dt = [A.det(*(X[i] for i in t)) for t in ts]
    W = A.add(*Dt)
    A.guard('>',A.mul(W,Delta),'volume')
    B = [A.add(*(A.mul(Dt[t],A.add(*(X[i][k] for i in ts[t]))) for t in range(14))) for k in range(3)]
    K = A.mul('4',Delta,W)
    Z = [[A.sub(A.mul('4',W,x),B[k]) for k,x in enumerate(row)] for row in X]
    heights = [A.sub(A.mul(h[f],K),A.dot(N[f],B)) for f in range(8)]
    for x in heights:
        A.guard('>',x,'centroid_interior')
    for i in range(9):
        for f in range(8):
            if f not in inc[i]:
                A.guard('>',A.add(A.mul('3',heights[f]),A.dot(N[f],Z[i])),'centroid_slack_upper')
    def quadratic(x,M,y):
        return A.dot(x,[A.dot(row,y) for row in M])
    normp = [quadratic(z,M,z) for z in Z]
    normq = [quadratic(n,adj,n) for n in N]
    for i in range(9):
        for f in range(8):
            A.guard('>=',A.sub(A.mul('729',dm,heights[f],heights[f]),A.mul(normp[i],normq[f])),'joint110_radius')
    ps,ds = {},{}
    pn,fn = [[] for _ in range(9)],[[] for _ in range(8)]
    for i,j in es:
        for a,b in ((i,j),(j,i)):
            ps[a,b] = quadratic(Z[a],M,A.vsub(Z[b],Z[a]))
            pn[a].append(b)
        f,gf = [f for f in range(8) if i in fs[f] and j in fs[f]]
        for a,b in ((f,gf),(gf,f)):
            y = [A.sub(A.mul(heights[a],N[b][k]),A.mul(heights[b],N[a][k])) for k in range(3)]
            ds[a,b] = quadratic(N[a],adj,y)
            fn[a].append(b)
        A.booleans.append(bop('or',map(positive,(ps[i,j],ps[j,i],ds[f,gf],ds[gf,f]))))
    def unique(adj, scores, n):
        return bop('or',(bop('and',(bop('and' if i == r else 'or',
               ((negative if i == r else positive)(scores[i,j]) for j in adj[i]))
               for i in range(n))) for r in range(n)))
    A.booleans += [unique(pn,ps,9),unique(fn,ds,8)]
    assert len(A.variables) == 17-surplus and len(A.booleans) == 17
    return A,dict(corner=c,neighbors=nbr,surplus=surplus,slots=slots,M=M,N=N,h=h,
                  Delta=Delta,X=X,W=W,B=B,K=K,Z=Z,heights=heights,
                  triangles=ts,triangle_facets=fi,primal=ps,dual=ds)


def qdot(a,b):
    return sum(x*y for x,y in zip(a,b))
def qcross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def qdet(a,b,c):
    return qdot(a,qcross(b,c))
def transpose(A):
    return list(map(list,zip(*A)))
def matmul(A,B):
    return [[qdot(r,c) for c in zip(*B)] for r in A]
def inverse(A):
    n = len(A)
    B = [[F(x) for x in r]+[F(i==j) for j in range(n)] for i,r in enumerate(A)]
    for j in range(n):
        i = next(i for i in range(j,n) if B[i][j])
        B[i],B[j] = B[j],B[i]
        z = B[j][j]
        B[j] = [x/z for x in B[j]]
        for i in range(n):
            if i != j:
                z = B[i][j]
                B[i] = [x-z*y for x,y in zip(B[i],B[j])]
    return [r[n:] for r in B]
def rank(A):
    A = [[F(x) for x in r] for r in A]
    k = 0
    for j in range(len(A[0])):
        i = next((i for i in range(k,len(A)) if A[i][j]),None)
        if i is None:
            continue
        A[k],A[i] = A[i],A[k]
        z = A[k][j]
        A[k] = [x/z for x in A[k]]
        for i in range(k+1,len(A)):
            z = A[i][j]
            A[i] = [x-z*y for x,y in zip(A[i],A[k])]
        k += 1
        if k == len(A):
            break
    return k


def control():
    V = [(0,0,0),(8,0,0),(0,8,0),(1,1,4),(5,1,4),(1,5,4),(1,1,-4),(5,1,-4),(1,5,-4)]
    fs = ((3,4,5),(6,8,7),(0,1,4,3),(1,2,5,4),(2,0,3,5),(1,0,6,7),(2,1,7,8),(0,2,8,6))
    spheres(fs,9)
    assert len(edges(fs)) == 15
    ts,span,trial = picktri(fs)
    rawd = [qdet(*(V[i] for i in t)) for t in ts]
    moments = tuple(sum(rawd[j]*sum(V[i][k] for i in t) for j,t in enumerate(ts)) for k in range(3))
    assert sum(rawd) == 896 and moments == (9088,9088,0)
    assert tuple(F(x,4*896) for x in moments) == (F(71,28),F(71,28),0)
    A,m = corner_system(dict(faces=fs,triangles=ts,span=span))
    assert (m['corner'],m['neighbors'],m['surplus']) == (3,[0,4,5],1)
    values = {'n1_0':F(1,2),'n1_1':0,'n1_2':0,'n3_0':-1,
              'n5_1':0,'n5_2':-2,'n6_0':0,'n6_1':F(1,2),'n6_2':F(1,2),
              'n7_1':-2,'n7_2':0,'m01':F(-2,9),'m02':F(-2,9),
              'm11':F(8,9),'m12':0,'m22':F(8,9)}
    value = A.evaluate(values)
    for op,x,tag in A.guards:
        v = value(x)
        assert (v == 0 if op == '=' else v > 0 if op == '>' else v >= 0),(tag,x,v)
    assert value(m['Delta']) == F(-1,4)
    assert value(m['W']) == F(-7,32) and value(m['K']) == F(7,32)
    assert tuple(value(x) for x in m['B']) == (F(7,32),F(71,512),F(71,512))
    Y = [(1,0,0),(1,2,0),(1,0,2),(0,0,0),(0,1,0),(0,0,1),
         (2,F(1,2),F(1,2)),(2,F(3,2),F(1,2)),(2,F(1,2),F(3,2))]
    assert [tuple(value(x)/value(m['Delta']) for x in row) for row in m['X']] == Y
    K = value(m['K'])
    assert tuple(value(x)/K for x in m['B']) == (1,F(71,112),F(71,112))
    P = [[value(x)/K for x in row] for row in m['Z']]
    Q = [[K*value(x)/value(m['heights'][f]) for x in row] for f,row in enumerate(m['N'])]
    M = [[value(x) for x in row] for row in m['M']]
    assert qdet(*M) == F(512,729)
    L = [[1-qdot(p,q) for q in Q] for p in P]
    D = [qdet(*(P[i] for i in t)) for t in m['triangles']]
    assert min(D) > 0
    om = [x/sum(D) for x in D]
    T = [[sum(om[t] for t in range(14) if m['triangle_facets'][t] == f and j in m['triangles'][t])
          for j in range(9)] for f in range(8)]
    E = matmul(matmul(L,T),L)
    assert all(E[i][f]+L[i][f] == 4 for i in range(9) for f in range(8))
    C = [[1-x for x in row] for row in L]
    assert rank(L) == 4 and rank(C) == 3
    for t,u in span:
        a = next(iter(set(m['triangles'][t])-set(m['triangles'][u])))
        b = next(iter(set(m['triangles'][u])-set(m['triangles'][t])))
        assert om[t]*L[b][m['triangle_facets'][t]] == om[u]*L[a][m['triangle_facets'][u]] > 0
    G = matmul(matmul(P,M),transpose(P))
    H = matmul(matmul(Q,inverse(M)),transpose(Q))
    assert matmul(matmul(G,transpose(T)),H) == C
    assert all(value(x) < 0 for x in m['primal'].values())
    for (i,j),x in m['primal'].items():
        assert value(x)/K**2 == G[i][j]-G[i][i]
    for (f,g),x in m['dual'].items():
        sf,sg = value(m['heights'][f]),value(m['heights'][g])
        assert K*K*value(x)/(qdet(*M)*sf*sf*sg) == H[f][g]-H[f][f]
    print('C30_NEGATIVE_DELTA_ACTUAL_MASS_METRIC_CONTROL_PASS',flush=True)


def save(name,obj):
    raw = (json.dumps(obj,sort_keys=True,separators=(',',':'))+NL).encode('ascii')
    Path(name).write_bytes(raw)
    assert Path(name).read_bytes() == raw
    print(name,len(raw),hashlib.sha256(raw).hexdigest(),flush=True)
    return raw


def main():
    assert set(sys.argv[1:]) <= {'--emit-smt'}
    source = Path(__file__).read_bytes()
    print('RECOVERY_SOURCE',len(source),hashlib.sha256(source).hexdigest(),flush=True)
    control()
    gs = frontier()
    raw = save('first_frontier.json',gs)
    assert len(raw) == 27025
    assert hashlib.sha256(raw).hexdigest() == '613ce3d88285e2c8faf2f41e08ee705ce279ec11430c6efbaf35b60273da925f'
    directory = Path('c30_adapted_smt')
    if '--emit-smt' in sys.argv:
        directory.mkdir(exist_ok=True)
    manifest = []
    for g in gs:
        A,m = corner_system(g)
        data = A.smt(g['mask'])
        name = 'V9_E15_F8_'+str(g['mask'])+'.smt2'
        digest = hashlib.sha256(data).hexdigest()
        if '--emit-smt' in sys.argv:
            path = directory/name
            path.write_bytes(data)
            check = path.read_bytes()
            assert len(check) == len(data) and hashlib.sha256(check).hexdigest() == digest
        row = dict(map_id=g['mask'],file=name,bytes=len(data),sha256=digest,
                   variables=len(A.variables),equations=sum(op == '=' for op,x,t in A.guards),
                   degree_bound=max(A.degrees.values()),corner=m['corner'],
                   neighbors=m['neighbors'],surplus=m['surplus'])
        assert row['variables'] == 17-row['surplus']
        assert row['equations'] == 3-row['surplus']
        assert row['degree_bound'] <= 125
        assert row['surplus'] >= max(g['degree'])-3
        manifest.append(row)
    save('c30_adapted_manifest.json',manifest)
    print('ADAPTED_COUNTS',sorted(Counter((r['variables'],r['equations']) for r in manifest).items()),flush=True)
    print('C30_ALL_74_TRUE_EDGE_FORESTS_PASS',flush=True)
    print('C30_ALL_74_ACTUAL_VOLUME_COMPLETE_SYSTEMS_PASS',flush=True)
    print('C30_NO_SAT_OR_UNSAT_VERDICT',flush=True)

if __name__ == '__main__':
    main()
```

## 7. Coverage and unresolved frontier

The inherited catalogue routine generates the complete eight-vertex polyhedral-map catalogue by triangulation generation and valid edge deletions. At E=15 its 74 maps dualize bijectively to the required V9,E15,F8 maps. The fixed checkpoint hash guards the entire resulting incidence/triangulation payload, not just its count. The new corner selection is combinatorial and exists in every realization; the fixed normal triples cannot become singular in a genuine realization. Every denominator sign is included. Every physical metric is represented up to an irrelevant positive common scale. The centroid is the actual solid-volume centroid. The geometric and equilibrium constraints are sufficient, as well as necessary.

The unresolved set is explicitly **every map record in the authenticated `first_frontier.json`, with the complete root disjunctions generated in its corresponding SMT file**. Before symmetry quotienting, those root choices are the 9 by 8 labelled choices for each of 74 maps. No unreported root-pair pruning or numerically inferred exclusion is included.

I explored stronger cone/separator pruning as well, but do not promote late experimental outputs from those searches into this certified successor. They are not needed for the reduction and do not justify deleting any case from the frontier supplied here.

The most useful continuation is now algebraic rather than another graph catalogue: start with the three degree-six maps, whose complete actual-mass/metric systems have fourteen real variables and no incidence equalities; then attack the degree-five maps with at most one cubic incidence equation. A certified UNSAT result must cover the full strict real domain of the selected system. An exact SAT witness must be reconstructed as the physical solid and checked against all guards and all four edge components; the supplied nine-vertex negative control shows why ordinary geometric feasibility alone is not an attainer.
