# Global carrier support

This track asks whether the exact locally preconditioned carrier event can be
realized as a globally supporting convex sphere with its own volume centroid.

The principal reconstructed checkpoint is `shell63_exact.csv`, built by
`build_shell63_exact.py` and rerun by `verify_shell63_exact.py`.  It is an
exact globally supporting `(63,169,108)` sphere of strict class `(2,1,1)`.
See `RESULT.md` for the construction and the finite actuator obstruction.

`projective_support_obstruction.py` closes the smallest synthesis template
exactly.  It audits prescribed faces by exact homogeneous determinants.  A
face with witnesses on both sides of its plane cannot be made supporting by a
single affine transformation, or by an invertible projective transformation
that leaves all points in one affine chart.  The reason is the identity

```text
orient(Tp_a,Tp_b,Tp_c,Tp_x)
  = det(T) orient(p_a,p_b,p_c,p_x)/(w_a w_b w_c w_x),
```

where all dehomogenizing factors `w_i` have one sign.  Thus a mixed sign pair
stays mixed.  Any successful global carrier construction must therefore move
rows relative to one another or solve a new supporting realization; a common
projective rechart is not enough.

Run after placing the recovered carrier files under
`../carrier_preconditioning/`:

```bash
python projective_support_obstruction.py \
  ../carrier_preconditioning/preconditioned_event_exact.csv \
  intended_faces.json \
  --output projective_support_obstruction.json
```

The intended-face list is deliberately a separate explicit input so the
certificate never silently treats the accidental Qhull faces of the raw local
event as the target sphere.
