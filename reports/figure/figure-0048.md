# figure-0048

AI research report · 2026-08-23 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

## Outcome

The required deliverable has **not** been obtained. I did not reinterpret a near-witness, a degenerate bifurcation, or an equilibrium count relative to an artificial reference point as a solution. This preserves the acceptance criterion stated explicitly in the earlier transcript: a valid result needs the actual uniform-volume centroid, strict positive margins, explicit coordinates, and an independent certificate.

## Strongest object produced in this direction

I reconstructed the equilibrium-aware smooth-cap construction using the exactly centered spectral-phase seed with beta = 0.035, removed the regions q > 0.96 and q < -0.96, installed a single intended stable truncation at the minimum, and installed an apex cone at the maximum. I then replaced the nonconvex sampled cone-normal curve by a convexly bulged polygon in the dual slope plane, rebuilt the complete active H-polytope, removed redundant supports through the dual hull, grouped coplanar triangles into maximal faces, reconstructed true edges, recomputed the body's own uniform centroid, and audited faces, vertices, and edges.

For the reproducible parameter set

```text
nsamp = 2000
beta = 0.035
qcut = 0.96
delta = 0.035
ring samples = 256
bulge fill = 12
bulge epsilon = 0.00001
```

the actual active polyhedron has

```text
V = 1121
E = 1698
F = 579
own centroid = (-0.21956145559400628,
                -0.000000509223482,
                 0.000000688877436)
(S,U,H) = (3,1,2)
```

The equilibrium margins, normalized by RMS distance from the centroid, are:

```text
intended stable face:       +0.2687568600719556
unique intended apex:       +0.1538244273089303
false stable transition 1:  +0.3205041519327874
false stable transition 2:  +0.3205058025573526
associated saddle 1:        +0.1644615172263536
associated saddle 2:        +0.1545713605514268
```

Thus this is an open, robust (3,1,2) object rather than numerical dust. Its two false stable faces are maximal transition faces, not hidden triangulation diagonals. They correspond to cone support rows 1919 and 1937, with outward normals approximately

```text
(0.25448417,  0.93380630,  0.25148280)
(0.25448417, -0.93380630, -0.25148280)
```

Each spans nearly the entire cone-to-middle transition, with diameter about 1.966 in the construction's scale. The two positive saddle margins occur on their boundary edges. This gives the branch-complete Morse relation 3 - 2 + 1 = 2.

## What was disproved computationally

### Uniform tangent or uniformly inward-shifted nets

Uniform tangent-plane approximations with 200 to 10,000 support samples produced hundreds or thousands of stable faces, unstable vertices, and saddle edges. Applying one common inward support shift reduced their counts only gradually; it did not implement the common-separator condition required by Lángi's construction. This confirms that increasing global resolution is not the missing operation.

### Feasible convex cone-normal polygon

I computed the complete two-dimensional feasible slope polygon for planes through the intended apex that contain all retained middle-surface samples. Using its boundary as the apex normal polygon kept the centroid close to the smooth body's center, but it retained too much of the near-equilibrium middle surface. At 1,000–2,000 middle samples this produced roughly 500–800 stable faces and comparable numbers of other equilibria.

### Convex bulging of the original dual ring

The original q = 0.96 normal curve is highly nonconvex in the dual slope plane. Convex-hull analysis found only about twenty extreme samples from a 512-point ring, including two long skipped arcs. I inserted outward convex bulges across those arcs so that additional cone supports became active. This substantially reduced the two transition-face margins—from approximately 0.77 in the unmodified construction to approximately 0.32—but it did not change their signs. Larger bulges eventually created additional unstable vertices before eliminating the stable pair.

These experiments break the hypothesis that the failure is merely inadequate sampling of the cone boundary. The two stable faces are enforced by the joint placement of the cone contour, the retained middle supports, and the displaced uniform centroid.

## Reproducible code

The principal scripts produced in this direction are:

- Smooth-cap reconstruction and baseline scan (`qcap_rebuild.py`)
- Feasible apex-slope polygon experiment (`qcap_feasible.py`)
- Convex dual-ring bulging experiment (`qcap_bulge.py`)
- Complete active-face and equilibrium classifier (`geomlib.py`)
- Uniform tangent-net diagnostic (`test_tangent_net.py`)
- Uniform inward-shift diagnostic (`test_inward_net.py`)

The strongest branch above is reconstructed by:

```python
import sys
sys.path.insert(0, "/mnt/data")
from qcap_bulge import build

obj = build(
    nsamp=2000,
    beta=0.035,
    qcut=0.96,
    delta=0.035,
    rn=256,
    nfill=12,
    eps=1e-5,
)
r = obj["r"]
print(len(r["hull"].vertices), len(r["edges"]), len(r["faces"]))
print(r["c"])
print(len(r["stable"]), len(r["unstable"]), len(r["saddle"]))
```

## Exact remaining mathematical obstruction

The unresolved operation is now finite and local but still coupled to the global centroid. The two transition support rows and their neighboring middle supports must be varied jointly so that each complete maximal transition face has a common separating edge excluding its own centroid projection. Simultaneously, the two associated edge normal cones must lose the centroid ray, while the apex displacement remains in the interior of its entire 36-generator normal cone.

Optimizing individual support residuals is insufficient: moving one transition face alone transfers stability to its neighbor, and checking only simplicial pieces misses the maximal-face condition. The next valid formulation must optimize the whole active cone-face block together with at least three independent remote volume controls, recomputing the uniform centroid after every step. This is the constructive content suggested by Lángi's separate equilibrium patches, common-separator middle truncation, and remote centroid controls.

No rationalization or printable model was performed because the numerical object fails the primary equilibrium criterion. Producing OBJ/STL files for it under the Gömböc label would be misleading.
