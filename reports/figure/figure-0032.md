# figure-0032

AI research report · 2026-08-22 UTC

---

# Exact nonsimple-boundary classification of the Reshetov obstruction

**Artifacts:** complete package (`nonsimple_reshetov_package.zip`), full report with both complete face lattices (`REPORT.md`), exact verifier (`verify_nonsimple_reshetov.py`).

Reshetov's appendix supplies the exact 14 face cycles, 24 incident-facet triples, and 14 integer normals, and verifies the unistable seed in rational arithmetic. The paper explains why rational verification is essential when margins can be below floating-point epsilon. The inherited transcript identified this seed as `(F,V,E)=(14,24,36)` with `(S,U,H)=(1,2,1)`, stable facet `11`, unstable vertices `(1,11,13)` and `(3,9,11)`, and saddle pair `(9,13)`.

## Correct equilibrium predicates

The verifier computes the exact uniform-volume centroid. A polygonal face is stable exactly when the centroid projection is in the strict relative interior of its **complete** boundary cycle. A vertex of any valence is unstable exactly when `v-c` is in the strict interior of its **full** normal cone; dually, every true outgoing edge `v→w` must satisfy `-(w-v)·(v-c)>0`. An edge is a saddle exactly when the centroid projection lies strictly between its endpoints and the projected radial vector is a strictly positive combination of its two incident facet normals. Every face, vertex, and edge is checked.

## Five-plane concurrence is impossible

For the five relevant normals, the exact primitive four-ray circuits are

```text
2929163 n1 + 3555472 n3 - 1362525 n9 + 5868633 n11 = 0
11137102 n1 + 9822248 n3 - 8576658 n9 - 5868633 n13 = 0
1695088 n1 + 2915672 n3 + 8576658 n11 + 1362525 n13 = 0
230605 n1 - 364459 n9 - 1227781 n11 - 444434 n13 = 0
1844840 n3 + 1695088 n9 + 11137102 n11 + 2929163 n13 = 0
```

Five-plane concurrence requires, for example,

```text
2929163 h1 + 3555472 h3 - 1362525 h9 + 5868633 h11 = 0
11137102 h1 + 9822248 h3 - 8576658 h9 - 5868633 h13 = 0.
```

The third and fifth circuits are all-positive. Hence `{1,3,9,11,13}` generates a nonpointed cone and cannot be the incident physical facets of one vertex. In centroid coordinates all physical supports are positive, giving the same contradiction by dotting either positive circuit with the common vertex. Adding one or arbitrarily many new rays cannot cure a positive dependent subset that remains present.

## Complete edge-contraction classification

The path is `(1,11,13)--(1,9,13)--(3,9,13)--(3,9,11)`.

- **Left contraction:** `230605h1-364459h9-1227781h11-444434h13=0`. It forces
  `n1=(364459 n9+1227781 n11+444434 n13)/230605`, so facet `1` is not an extreme physical incident facet.
- **Middle contraction:** `11137102h1+9822248h3-8576658h9-5868633h13=0`. This is the only genuine pointed four-ray contraction with all rays extreme. Its opposite pairs are `{1,3}` and `{9,13}`, so `(9,13)` becomes a diagonal/non-edge and the old saddle is eliminated.
- **Right contraction:** the all-positive equation `1844840h3+1695088h9+11137102h11+2929163h13=0` makes a physical contraction impossible.

An exact all-14-facet middle-contraction witness is obtained by retaining `h_i=||n_i||²` except

```text
h1 = 640398771027 / 5568551.
```

Its complete exact lattice is in MID_exact_certificate.json: `(V,E,F)=(23,35,14)`, unique nonsimple incidence `(1,3,9,13)`, and `(S,U,H)=(6,2,6)`. The pair `(9,13)` is not an edge, but the two original forced unstable vertices remain. Centered OBJ (`MID_contraction_witness.obj`).

## Complete one-facet deletion classification

The two positive circuits are `{1,3,11,13}` and `{3,9,11,13}`.

- Delete `1`: remaining `{3,9,11,13}` is impossible.
- Delete `9`: remaining `{1,3,11,13}` is impossible.
- Delete `3`: in `{1,9,11,13}`, `n1` is interior to `cone(n9,n11,n13)`, so facet `1` also disappears physically.
- Delete `13`: in `{1,3,9,11}`, `n9=(2929163 n1+3555472 n3+5868633 n11)/1362525`, so facet `9` also disappears physically.
- Delete `11`: `{1,3,9,13}` is the only genuine four-valent one-deletion cone.
- Delete `{1,9}`: only the simple cone `{3,11,13}` remains.

Thus preserving the original stable facet `11` requires at least two effective old-facet deletions plus a new ray.

The exact delete-11 witness uses

```text
(h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h12,h13,h14)
=(0,54,0,35,4,15,7,24,0,47,65,0,35).
```

All 13 inequalities are physical facets. Its complete exact vertex coordinates, vertex-facet incidences, 32 edges, and all polygon cycles are in D_exact_certificate.json and D_exact_summary.md. It has `(V,E,F)=(21,32,13)`, unique four-valent vertex `(1,3,9,13)`, exact rational centroid approximately `(-0.2248277056600262,0.13921652216042335,0.08257870737226365)`, and `(S,U,H)=(5,2,5)`. The common four-valent vertex is not unstable. Centered OBJ (`D_concurrence_witness.obj`).

## Complete minimal two-deletion/one-new-ray classification

Let `(a,b,c)` be independent, with `b=n11`, and set `r=a-b+c`. In this basis `r=(1,-1,1)`. The cone is pointed with all four rays extreme; opposite pairs are `{a,c}` and `{b,r}`. More generally, for `r=αa+βb+γc`, all four rays are extreme in a pointed cone exactly when two coefficients have one sign and the third the opposite sign. To make `{a,c}` the diagonal, take `α,γ>0>β`.

Exactly four minimal patterns preserve `n11` and one nonshared ray from each forced cone:

| pattern | deleted | survivor basis | new ray | support equation | old diagonal/non-edge |
|---|---|---|---|---|---|
| A | `{1,3}` | `(n9,n11,n13)` | `(5,-660,-680)` | `h9-h11+h13-hr=0` | `(9,13)` |
| B | `{9,13}` | `(n1,n11,n3)` | `(-7,-500,-515)` | `h1-h11+h3-hr=0` | `(1,3)` |
| C | `{1,9}` | `(n3,n11,n13)` | `(6,-964,-239)` | `h3-h11+h13-hr=0` | `(3,13)` |
| E | `{3,13}` | `(n1,n11,n9)` | `(-8,-196,-956)` | `h1-h11+h9-hr=0` | `(1,9)` |

For each pattern, setting the four common supports to `1` gives an exact rational common vertex, and adding the rational box `|x|,|y|,|z|≤10` gives a bounded exact realization while remaining strict at that vertex. The complete certificates and face lattices are in minimal_one_new_ray_patterns.json and the four `pattern_*_local_exact_certificate.json` files. These certify cone realizability, not Gömböc equilibrium.

## Exact centroid polynomial system

For the delete-11 lattice, gauge the common vertex to zero by `h1=h3=h9=h13=0`. The shape variables are `(h2,h4,h5,h6,h7,h8,h10,h12,h14)`. With the fixed exact triangulation,

```text
Volume = D/6,
centroid = (Mx,My,Mz)/(4D).
```

The fully expanded exact system has 34 monomials in the cubic `D` and 51, 50, and 50 monomials in the quartics `Mx,My,Mz`. Introducing translation `t=(tx,ty,tz)`, exact centering is

```text
Mx + 4D tx = 0,
My + 4D ty = 0,
Mz + 4D tz = 0,
h_i(centered) = h_i + n_i·t.
```

Full expansions: JSON (`D_centroid_polynomial_system.json`), text (`D_centroid_polynomial_system.txt`).

## Verification and final status

Run `python verify_nonsimple_reshetov.py`. It uses Python and SymPy only and regenerates every exact object. The recorded output is VERIFICATION_OUTPUT.txt. The package SHA-256 is `5436050ed048511ff3851a795f8186695779e990726f8d783f48f32a48ecc848`; individual hashes are in manifest_sha256.json.

No homogeneous polyhedral Gömböc is claimed. The exact contribution is a complete closure of the requested smallest nonsimple route: the five-plane merge is impossible; the only genuine old-edge contraction removes the saddle but leaves `U=2`; the only genuine one-facet merge deletes the stable facet and yields `(5,2,5)`; and the remaining minimal stable-facet-preserving fronts are exactly A, B, C, and E.
