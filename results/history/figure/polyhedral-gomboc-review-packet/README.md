# Exact polyhedral Gömböc candidate

This packet contains one explicitly materialized finite convex polyhedron of uniform volume density and an independent exact verifier.

The asserted equilibrium class, relative to the polyhedron's own volume centroid, is

```text
(stable faces, unstable vertices, saddle edges) = (1, 1, 0).
```

## Object

```text
vertices                                      134131
true edges                                    402134
maximal faces                                 268005
oriented triangulation faces                  268258
triangulation edges                           402387
coplanar internal triangulation diagonals        253
Euler characteristic                              2
```

The unique stable maximal face is a 256-gon in the plane

```text
x = -100327/102400.
```

The unique unstable vertex has index `134130`, degree `152`, and coordinate

```text
(104473/102400, 0, 0).
```

`exact_polyhedron.npz` contains these arrays:

```text
I : (134131,3) int64
B : (134131,)  int64
F : (268258,3) int64, outward-oriented triangle indices
D : scalar int64 = 109951162777600
```

For the algebraic parameter `t`, vertex `i` is

```text
v_i(t) = ((I[i,0] - t*B[i])/D, I[i,1]/D, I[i,2]/D).
```

`t` is the unique root in the rational interval recorded in `root.json` of

```text
C0 + C1*t + C2*t^2 = 0,
```

where the coefficients are also recorded in `root.json`. Numerically,

```text
t ~= -3.50637336622894879374850470801155491523743452402042643327945115173306042721.
```

## Exact verification

Run from the extracted directory:

```text
python3 verify.py
```

The only Python dependency is NumPy. The verifier does not use stored equilibrium labels or import construction code. From the coordinate and face arrays it independently recomputes:

- the volume and all three first moments, proving that the centroid is the origin;
- isolation and simplicity of the algebraic root;
- triangle and oriented-edge incidences;
- connectedness, closedness, orientation, Euler characteristic, and every vertex link;
- positive radial orientation and degree one of the radial map;
- all exact adjacent-hinge signs and the global convexity certificate;
- coplanar components, true edges, and maximal-face boundary cycles;
- a rank-three supporting-normal cone at every vertex;
- every face, vertex, and true-edge equilibrium predicate.

A successful run ends with

```text
"status": "INDEPENDENT_EXACT_AUDIT_PASS"
"vertices": 134131
"triangles": 268258
"maximal_faces": 268005
"true_edges": 402134
"independently_recomputed_exact_equilibrium_class": [1, 1, 0]
```

Some hinge margins are too small for reliable floating-point classification. The verifier therefore evaluates the relevant signs with exact integer arithmetic in the quadratic number field defined by `root.json`.
