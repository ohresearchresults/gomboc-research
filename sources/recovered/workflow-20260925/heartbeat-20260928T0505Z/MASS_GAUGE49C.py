# MASS_GAUGE49C.py -- Python standard library only
from fractions import Fraction as Q
from itertools import combinations


def vec(a):
    return tuple(Q(x) for x in a)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def mul(s, a):
    return tuple(s * x for x in a)


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), Q(0))


def cross(a, b):
    return (a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0])


def det(a, b, c):
    return dot(a, cross(b, c))


def tetra_faces(x):
    assert len(x) == 4
    faces = []
    for i, j, k in combinations(range(4), 3):
        other = next(t for t in range(4) if t not in (i, j, k))
        n = cross(sub(x[j], x[i]), sub(x[k], x[i]))
        side = dot(n, sub(x[other], x[i]))
        assert side != 0
        if side > 0:
            j, k = k, j
        faces.append((i, j, k))
    return faces


def mass_and_derivative(x, dx, faces):
    zero = (Q(0), Q(0), Q(0))
    V = Q(0)
    M = zero
    dV = Q(0)
    dM = zero
    for i, j, k in faces:
        a, b, c = x[i], x[j], x[k]
        da, db, dc = dx[i], dx[j], dx[k]
        D = det(a, b, c)
        dD = det(da, b, c) + det(a, db, c) + det(a, b, dc)
        abc = add(add(a, b), c)
        dabc = add(add(da, db), dc)
        V += D / 6
        M = add(M, mul(D / 24, abc))
        dV += dD / 6
        dM = add(dM, mul(Q(1, 24),
                         add(mul(dD, abc), mul(D, dabc))))
    assert V > 0
    g = mul(1 / V, M)
    dg = mul(1 / V, sub(dM, mul(dV, g)))
    B = sub(mul(3 * V, dg), mul(dV, g))
    BM = sub(mul(3 * V, dM), mul(4 * dV, M))
    assert BM == mul(V, B)
    return V, M, g, dV, dM, dg, B


def scale_free_merit_cube(V, g):
    return dot(g, g) ** 3 / V ** 2


def main():
    x = list(map(vec, [(-1, -1, -1), (3, 0, 0),
                       (0, 2, 0), (0, 0, 4)]))
    faces = tetra_faces(x)
    zero = [(Q(0), Q(0), Q(0)) for _ in x]
    V, M, g, *_ = mass_and_derivative(x, zero, faces)
    assert V == Q(25, 3)
    assert g == (Q(1, 2), Q(1, 4), Q(3, 4))
    merit = scale_free_merit_cube(V, g)
    assert merit == Q(3087, 320000)

    # Uniform physical dilation is a null direction of normalized centring.
    _, _, _, dV, dM, dg, B = mass_and_derivative(x, x, faces)
    assert dV == 3 * V
    assert dM == mul(4, M)
    assert dg == g
    assert B == (0, 0, 0)

    # An arbitrary rational direction and its exact volume-gauge projection.
    dx = list(map(vec, [(Q(1, 7), 0, 0),
                        (0, Q(-2, 7), Q(1, 5)),
                        (Q(1, 3), 0, Q(-1, 9)),
                        (0, Q(2, 11), 0)]))
    out = mass_and_derivative(x, dx, faces)
    alpha = out[3] / (3 * V)
    dx0 = [sub(d, mul(alpha, p)) for d, p in zip(dx, x)]
    out0 = mass_and_derivative(x, dx0, faces)
    assert out0[3] == 0
    assert out0[6] == out[6]

    # Finite rational dilations can make raw centroid residual arbitrarily
    # small while leaving the dimensionless physical residual unchanged.
    for lam in (Q(1, 2), Q(1, 10), Q(1, 1000)):
        y = [mul(lam, p) for p in x]
        Vy, My, gy, *_ = mass_and_derivative(y, zero, faces)
        assert Vy == lam**3 * V
        assert My == mul(lam**4, M)
        assert gy == mul(lam, g)
        assert scale_free_merit_cube(Vy, gy) == merit

    print('QW49_SCALE_FREE_MASS_NEWTON_IDENTITY_PASS')
    print('V =', V, '; g =', g, '; rational merit =', merit)


if __name__ == '__main__':
    main()
