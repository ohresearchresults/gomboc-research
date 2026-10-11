# Exact directed certificate for the two grouped nullspace bypasses

## Result

`RUN_ALL.sh` rebuilds the frozen proof object and finishes with the literal line

```text
EXACT_DIRECTED_GROUPED_NULLSPACE_BYPASS_PASS
```

The theorem is exact for the explicitly serialized rational cells and the
explicit plane-preserving polynomial paths in `certificate.json`.  It proves:

1. the shared `U263/H(10,263)` wall and its four quadrant cells;
2. an exact two-leg actual-cell L-bypass of that wall;
3. the shared `U1/H(1,54)` wall and its four quadrant cells;
4. an exact two-leg actual-cell L-bypass retaining both earlier nonbirth guards;
5. the first hard wall on the explicit exact `round3_C -> round4` planar morph.

It does **not** claim a global theorem about every interpolation in the original
nonlinear 27-dimensional binary64 chart.  That chart is used only to choose
nearby snapshots.  Each snapshot is frozen with 17-digit decimal rounding and
then projected onto the enlarged base plane with exact rational arithmetic.
All predicates after that freeze are exact.

## Common-numerator identities

Write

```text
X_i = 4 D6 P_i - M24
```

for the denominator-cleared centroid vector used by the verifier.

For round 2, let `d = P263-P10`.  Then the vertex endpoint numerator is

```text
V(263;10) = -X263·(P10-P263) = X263·d,
```

while the `1-tau` numerator of edge `(10,263)` is

```text
E(10,263;1-tau) = 4 D6 ||d||^2 + X10·d = X263·d.
```

The last equality is the polynomial identity
`X263-X10 = 4 D6 (P263-P10)`.  The verifier compares the complete degree-9
coefficient vectors, not sampled values.

For round 3, let `d = P54-P1`.  Both defining numerators are literally

```text
V(1;54) = E(1,54;tau) = -X1·d.
```

The exact event roots on the local rational event paths are:

| Event | Local root | Exact bracket width | Numerator digest |
|---|---:|---:|---|
| `U263/H(10,263)` | `0.50103070270122407` | `1/1844674407370955161600000` | `21a28aebd3b377472a549fab1c9748ff49c80e92aa01d1bb7a8d4c3419b74448` |
| `U1/H(1,54)` | `0.50069152697075392` | `1/1844674407370955161600000` | `8fbe55fef5f3d53a5f1d6e35188a5bf155ef438d40ca99fbeaa3da75de0c5435` |

In each case the degree-8 derivative has one strict Bernstein sign on the
whole event interval, so the isolated root is unique.  Apart from the two
names attached to the same numerator, all 7,902 other support, incidence and
mechanics polynomials are strictly signed throughout the event path.

## Four fresh quadrant cells at each wall

Every frozen quadrant has exact support vector `[61,162,103]`, Euler value 2,
the common enlarged base face, and every edge of both forced rails.  The two
tangent signs give the same class; the transverse sign selects the side:

| Round | Quadrant | Exact class | Coordinate hash |
|---|---|---|---|
| 2 | `u-1_v-1` | `[2,3,3]` | `d21488ac9e923ff48c4922e326ce259be26f1b65f4461133f7ac042be66277fb` |
| 2 | `u+1_v-1` | `[2,3,3]` | `829ed627a9cc2bf87972fcb689c164c4b2f77f1681ce5407006a613ea5e4a5f1` |
| 2 | `u-1_v+1` | `[2,2,2]` | `65b17c87b8594968a423c0d31701322e290114e2080b5affb737b2906ef18db4` |
| 2 | `u+1_v+1` | `[2,2,2]` | `5bd0e018b20831ce25ec6c311454c16ec2d574cc3b7ae8499b80b57f0f3d5630` |
| 3 | `u-1_v-1` | `[2,3,3]` | `4e1e24504bad48c00cf7349446fa7a704c7e961ff92eb7d9bee4661b0c5d96ac` |
| 3 | `u+1_v-1` | `[2,3,3]` | `7a2a09c6af17f72b7ddf4a952788c6fb6a3f2cb3ca41dfef182c59cd4ebab1a6` |
| 3 | `u-1_v+1` | `[2,2,2]` | `3d3b4aad6884adc59bdd11bf3f092fb7b582fd60537e3923158849420e6b3cf3` |
| 3 | `u+1_v+1` | `[2,2,2]` | `b635c93da5ad860be4750f4ba52d8d7d99182fdcc6d2e66725465f46ed6620f3` |

## Exact L-path certificates

For each saved `A -> B -> C` chain, rows 0,1,2 move affinely; every other base
row is reconstructed from linearly interpolated exact barycentric coordinates;
all nonbase rows move affinely.  Thus the base is polynomially coplanar for the
entire path, not only at its endpoints.

Each segment certifies every defining primitive: volume, all support
determinants, every face-reference orientation, all edge norm and Gram factors,
every directed face component, every vertex component, and all four components
of every edge decision.  No one-witness reduction is used.

| Round / segment | Polynomials | Primitive digest | Smallest Bernstein coefficient, log10 abs |
|---|---:|---|---:|
| 2 `A->B` | 7,904 | `c46612cbcee3c1254b1e0a5139003a6814d0059024425d8dedc8778965bece75` | -44.1342202719 |
| 2 `B->C` | 7,904 | `a415ee04978fc016f389f5e675e09453108f8b511e252610885075b8f87ebd3f` | -44.1312015073 |
| 3 `A->B` | 7,904 | `b7825a3f8df8015565f674fde88d600e0d96f5f1697a0a76e50e06f831770cf4` | -44.1754193008 |
| 3 `B->C` | 7,904 | `6c37de2569d180304b52ca6bdc76d75a4d631341e549bb7e1016a42203a24f11` | -44.1754107160 |

All four segments stay in the exact class `[2,2,2]`.  On the round-2 bypass,
the common `U263/H(10,263)` numerator is strictly negative throughout, which
is a positive nonbirth guard.  On both round-3 segments, both that previous
common numerator and the new `U1/H(1,54)` numerator are strictly negative
throughout.

## First hard event in round 4+

The endpoint-to-endpoint exact planar morph from `round3_C` to the round-4
endpoint is not event-free.  Its first wall is again the common
`U263/H(10,263)` numerator:

```text
t = 0.0018369232861480654
exact bracket width = 1/1844674407370955161600000
common numerator digest = 7de67eab3769ebe5c24be993124df1155500511eed00fa591565672baa3fbb84
```

The shared numerator is strictly negative on the complete certified prefix,
has positive derivative on its isolating interval, and all 7,902 other
primitives retain strict signs through the root.  An exact rational sample
`10^-8` after the bracket has class `[2,3,3]`; the retained round-3
`U1/H(1,54)` nonbirth numerator is still strictly negative.  Therefore this is
the first hard event of this explicit replacement morph.  The round-4 saved
endpoint itself is again `[2,2,2]`, so the morph later exits the temporary
birth cell; this report intentionally certifies only the first event ordering.

## Hashes and reproducibility

The two face files are byte-identical:

```text
source file SHA256: 277c9f8373b886d3dda47b03183c9d9a49575100b1339576cfed8af004a218fc
canonical face-ledger SHA256: 4f50f9ffb003c32a424a64132ad9244f2e76dff12f149bbf9e2f7d7052986381
```

Principal coordinate sources:

```text
row54_combined_hard_slp_best.csv
  701b91e91e1ee4c54a03a92f6f463a222034470be014186b9b9121cdc057b293
row54_round2_null_bypass_C_buffered_post.csv
  62029acb73bfcbfea8a36bd7122fb1cc5862aad481d565ca0f9253f3fb4fde4c
row54_round3_null_bypass_C_buffered_post.csv
  87794d3be2206da26c498272fe9c9f4ad48625991f26f2914487b8d433cd3d23
row54_combined_hard_slp_round4_best.csv
  3d41a362f36e9b3911384ad5475a921a3beb549ee585e48f4b3bb418b749722e
```

The generated certificate SHA256 from the clean pass is
`571f739f7c2189b0b089b468696c001863f562d9722c29156a80676a14f4c780`.
The exact arithmetic core SHA256 is
`d2d69ce6e4ddefd2ab7171b7e61bd09ae12846eaf509f61dd25be6d9bbb235dd`.
All 31 input hashes, all frozen coordinate hashes, complete rational root
brackets, and all degree-9 common-numerator coefficient vectors are embedded
in `certificate.json` and `verification_summary.json`.

Run from this directory:

```bash
./RUN_ALL.sh
```

