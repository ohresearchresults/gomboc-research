# Material findings

- The apparent `4.75e-14` separation between the numerical
  `S(8,245,246)` and `H(8,245)` births is not two walls.  Their active
  components share one exact beta numerator; the face/beta identity is a
  literal zero polynomial.
- A five-control cofactor construction gives an exact keep-tangent with a
  strictly negative linked-birth pairing.  No finite-difference Jacobian is
  used in the certificate.
- The complete two-segment L bypass has 13,936 exact constant-sign polynomial
  checks and retains the full class `(2,2,2)` continuously.
- The first hard adaptive wall is the ordered circuit `(8,9,10,263)`; only its
  two proportional support slacks vanish before row `9` becomes base-interior.
- The later stage-6 failure is a clean `2<->2` tetrahedral flip on
  `(7,8,245,246)`, not a class-increasing birth: the stable face and diagonal
  transfer, while `(S,U,H)=(2,2,2)` and all 37 rails persist.
- All theorem statements are deliberately limited to the frozen nearby
  rational charts.  The exact base repair shifts the stage-6 root by
  `5.4366637494e-10` from its binary64 locator; this is recorded rather than
  hidden.

