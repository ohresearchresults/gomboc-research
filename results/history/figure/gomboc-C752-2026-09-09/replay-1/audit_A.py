from itertools import combinations
from fractions import Fraction as Q
import sys, json, math, hashlib
from pathlib import Path
sys.set_int_max_str_digits(0)
Z = (0, 0, 0)
def add(a, b): return tuple(a[i]+b[i] for i in range(3))
def sub(a, b): return tuple(a[i]-b[i] for i in range(3))
def scale(s, a): return tuple(s*x for x in a)
def dot(a, b): return sum(a[i]*b[i] for i in range(3))
def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])
def det(a, b, c): return dot(a, cross(b, c))

def exact_polygon(I, ids, N):
    k = max(range(3), key=lambda j: abs(N[j]))
    axes = [j for j in range(3) if j != k]
    ids = sorted(ids, key=lambda i: (I[i][axes[0]], I[i][axes[1]]))
    def turn(a, b, c):
        x, y, z = I[a], I[b], I[c]
        return ((y[axes[0]]-x[axes[0]])*(z[axes[1]]-x[axes[1]])
                -(y[axes[1]]-x[axes[1]])*(z[axes[0]]-x[axes[0]]))
    lo, hi = [], []
    for seq, out in ((ids, lo), (ids[::-1], hi)):
        for i in seq:
            while len(out) >= 2 and turn(out[-2], out[-1], i) <= 0:
                out.pop()
            out.append(i)
    cy = lo[:-1]+hi[:-1]
    assert len(cy) >= 3
    a, b, c = [I[i] for i in cy[:3]]
    if dot(N, cross(sub(b, a), sub(c, a))) < 0:
        cy.reverse()
    j = cy.index(min(cy))
    return cy[j:]+cy[:j]

def exact_audit(I, D):
    I = [tuple(map(int, p)) for p in I]
    assert D > 0 and len(set(I)) == len(I)
    planes = set()
    for ia, ib, ic in combinations(range(len(I)), 3):
        a, b, c = I[ia], I[ib], I[ic]
        N = cross(sub(b, a), sub(c, a))
        if N == Z:
            continue
        h = dot(N, a)
        vals = [h-dot(N, p) for p in I]
        if max(vals) <= 0:
            N, h = scale(-1, N), -h
            vals = [-v for v in vals]
        if min(vals) < 0:
            continue
        assert max(vals) > 0, 'not full dimensional'
        divisor = math.gcd(*N, h)
        planes.add(tuple(v//divisor for v in N)+(h//divisor,))
    assert len(planes) >= 4
    planes = sorted(planes)
    F = []
    for N0 in planes:
        N, h = N0[:3], N0[3]
        ids = [i for i, p in enumerate(I) if dot(N, p) == h]
        F.append(exact_polygon(I, ids, N))
    active = sorted({i for cy in F for i in cy})
    E, T = {}, []
    for fi, cy in enumerate(F):
        N = planes[fi][:3]
        for j, b in enumerate(cy):
            a, c = cy[j-1], cy[(j+1) % len(cy)]
            assert dot(N, cross(sub(I[b], I[a]), sub(I[c], I[b]))) > 0
        for a, b in zip(cy, cy[1:]+cy[:1]):
            E.setdefault(tuple(sorted((a, b))), []).append((fi, a, b))
        T.extend((cy[0], cy[j], cy[j+1])
                 for j in range(1, len(cy)-1))
    assert len(active)-len(E)+len(F) == 2
    assert all(len(v) == 2 and v[0][1:] == v[1][1:][::-1]
               for v in E.values())
    adjacency = {i: set() for i in active}
    for a, b in E:
        adjacency[a].add(b)
        adjacency[b].add(a)
    seen, todo = set(), [active[0]]
    while todo:
        i = todo.pop()
        if i not in seen:
            seen.add(i)
            todo.extend(adjacency[i]-seen)
    assert seen == set(active)
    W, M = 0, Z
    for a, b, c in T:
        d = det(I[a], I[b], I[c])
        W += d
        M = add(M, scale(d, add(add(I[a], I[b]), I[c])))
    assert W > 0
    K = 4*W
    Y = [sub(scale(K, p), M) for p in I]
    Wc, Mc = 0, Z
    for a, b, c in T:
        d = det(Y[a], Y[b], Y[c])
        assert d > 0
        Wc += d
        Mc = add(Mc, scale(d, add(add(Y[a], Y[b]), Y[c])))
    assert Wc == K**3*W and Mc == Z
    S, Sd, U, Ud, H, Hd = [], [], [], [], [], []
    primitive_zeros = 0
    for fi, cy in enumerate(F):
        N = planes[fi][:3]
        vals = [dot(N, cross(Y[a], sub(I[b], I[a])))
                for a, b in zip(cy, cy[1:]+cy[:1])]
        if min(vals) > 0:
            S.append(fi)
        elif min(vals) >= 0:
            Sd.append(fi)
    for i in active:
        vals = [dot(Y[i], sub(I[j], I[i]))
                for j in active if j != i]
        if max(vals) < 0:
            U.append(i)
        elif max(vals) <= 0:
            Ud.append(i)
    for (a, b), es in sorted(E.items()):
        e = sub(I[b], I[a])
        L = dot(e, e)
        pa, pb = dot(Y[a], e), -dot(Y[b], e)
        (f, i, j), (g, k, l) = es
        N, NN = planes[f][:3], planes[g][:3]
        s0 = dot(N, cross(Y[i], sub(I[j], I[i])))
        s1 = dot(NN, cross(Y[k], sub(I[l], I[k])))
        primitive_zeros += sum(v == 0 for v in (pa, pb, s0, s1))
        nn, mm, nm = dot(N, N), dot(NN, NN), dot(N, NN)
        assert nn*mm-nm*nm > 0
        A, B = -pa, K*L+pa
        z = add(scale(L, Y[a]), scale(A, e))
        alpha = dot(z, sub(scale(mm, N), scale(nm, NN)))
        beta = dot(z, sub(scale(nn, NN), scale(nm, N)))
        vals = (A, B, alpha, beta)
        strict = min(vals) > 0
        assert strict == (pa < 0 and pb < 0 and s0 > 0 and s1 > 0)
        if strict:
            H.append([a, b])
        elif min(vals) >= 0:
            Hd.append([a, b])
    return dict(
        input_vertex_count=len(I), V=len(active), E=len(E), F=len(F),
        active_input_indices=active, maximal_faces=F,
        true_edges=[list(e) for e in sorted(E)],
        primitive_support_planes=[list(p) for p in planes],
        counts=[len(S), len(U), len(H)],
        weak=[len(Sd), len(Ud), len(Hd)],
        stable_faces=[F[i] for i in S], unstable_vertices=U,
        saddle_edges=H, weak_faces=Sd, weak_vertices=Ud,
        weak_edges=Hd, true_edge_primitive_zeros=primitive_zeros,
        volume=str(Q(W, 6*D**3)),
        raw_first_moments=[str(Q(v, 24*D**4)) for v in M],
        raw_centroid=[str(Q(v, 4*W*D)) for v in M],
        centred_first_moments=['0', '0', '0'],
        centred_denominator=K*D,
        centred_integer_coordinates=[list(p) for p in Y],
        integration_triangles=[list(t) for t in T])


if __name__ == '__main__':
    p=json.loads(Path(sys.argv[1]).read_text())
    r=exact_audit(p['I'],p['D'])
    raw=json.dumps(r,sort_keys=True,separators=(',',':')).encode()
    out=sys.argv[2] if len(sys.argv)>2 else 'audit_A.json'
    Path(out).write_bytes(raw)
    print(out,len(raw),hashlib.sha256(raw).hexdigest())
    print('EXACT_A',r['V'],r['E'],r['F'],r['counts'],r['weak'],r['true_edge_primitive_zeros'])
