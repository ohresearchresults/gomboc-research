# Post-C17 exact linked death and first support flip

## Result

The rational 19-control hard-moment path starts from the immutable exact
post-C17 endpoint and preserves the base plane, shell plane, all 61 active
rows, protected `U8`, and all 37 forced rails.

Its first genuine event is the common degree-five algebraic root of
`U254_via_255` and `H254_255_via_t`, isolated in
`[2192928817/2500000000, 8771715269/10000000000]`.  The exact class changes
from `(2,5,5)` to `(2,4,4)` with no compensating birth.

The continuation then reaches the first complete support/in-face event family.
Exactly two support rows share the unique quadratic root in
`[9535026893/10000000000, 4767513447/5000000000]`; the circuit is
`(255,256,257,258)`, removing true edge `(255,257)` and adding `(256,258)`.
The new diagonal has its expected barycentric pole exactly at that algebraic
wall.  A one-sided exact cone cover proves that every selected numerator is
root-free and every selected denominator root is the same unique support
root; hence no hidden mechanics event occurs on entry.  The strict far cell
and the endpoint retain class `(2,4,4)` and all 37 rails.

This is **NONWINNER**.  It is a new exact cell and a certified handoff for the
remaining packet `S[228,264,246], U228, U231, U246, H(8,246), H(228,254),
H(231,247), H(236,237)`.

## Verification

```bash
/usr/local/bin/python3 tracks/piecewise_transfer/post_c17_attack/verify_certificate.py
```

Expected terminal marker:

```text
INDEPENDENT_EXACT_POST_C17_LINKED_DEATH_AND_SUPPORT_FLIP_PASS
```
