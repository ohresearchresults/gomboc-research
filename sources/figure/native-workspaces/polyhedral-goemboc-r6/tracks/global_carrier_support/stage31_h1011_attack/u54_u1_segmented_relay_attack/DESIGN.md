# Exact segmented carrier relay U54 -> U1

## Scope and bindings

This sidecar attacks only the literal rational checkpoint
`continuation2_row230_bypass/step15_transfer_far.csv`.  It does not mutate the
continuation ledger or any previous certificate.

Frozen external inputs:

- source SHA-256: `7f16c070aeba30199758815215774877bf759554d5dca1c6d875b85f27c8b94d`
- maximal-face ledger SHA-256: `c1d74d638df21a0492645aa39e4d3943b8401ed0732393505c838ec2f1c0ed77`
- `exact_core.py`, selected-component owner, chart owner, and hull owner: hashed
  fresh by every executable receipt rather than copied into this document.

The exact source contract is `(V,E,F)=(61,162,103)`, all 61 labels active,
stable faces equal to the enlarged base and `(7,8,245)`, unstable vertices
`{8,54}`, saddles `{(5,6),(10,11)}`, all 37 forced rails present, all 18
enlarged-base turns strict, both row-230 danger supports strict, and H910
strictly dead.

## Ordered event identity

Let

`B = vertex:1:54 = edge:(1,54):t`

and

`D = vertex:54:1 = edge:(1,54):one_minus_t`.

For the exact own-centroid scaling used by `exact_core.py`,

`B + D = 4*d6*||p54-p1||^2 > 0`.

At the source, `B<0<D`.  Therefore a retained-ledger relay must cross `B`
first.  That crossing simultaneously births U1 and saddle H(1,54), producing
class `(2,3,3)`.  Only after a rational post-birth checkpoint is materialized
may a new chart target `D`; its crossing simultaneously kills U54 and
H(1,54), leaving U1 as carrier and restoring class `(2,2,2)`.

## Executable phases

1. `propose_epoch.py --phase birth` constructs a deterministic 165-mode
   numerical full-support direction, exactifies it to a rational affine path,
   performs a fresh hull readback, and writes `post_birth_checkpoint.csv` plus
   `birth_proposal.json` only if the endpoint has exact class `(2,3,3)` and the
   literal face ledger, labels, base, rails, row-230 supports, and H910 survive.
2. `locate_epoch.py --phase birth` scans all 7,922 volume/support/base-turn/
   four-cone primitives with exact Bernstein subdivision.  It accepts only the
   two B aliases as the overlapping first event.
3. `certify_birth.py` proves the aliases have a common exact polynomial,
   isolates its simple (hence odd) root, proves every other primitive strict,
   proves both open classes, and binds the rational checkpoint.
   `verify_birth.py` independently reconstructs the 7,922-row proof and all
   source/pre/post/endpoint state invariants without importing the certifier.
4. `propose_epoch.py --phase death` must start from that literal checkpoint;
   this is a fresh 165-mode chart, never an extrapolation of the birth ray.
   Mechanics use a fresh central chart while all 5,959 support guards use
   sparse exact-rational unnormalized first jets.  It targets only the two D
   aliases and writes `far_u1.csv` only if the fresh endpoint has the required
   `(2,2,2)` U1-carrier feature set.
5. `locate_epoch.py --phase death`, `certify_death.py`, and
   `verify_death.py` repeat the exhaustive exact checks, including a strictly
   positive birth/death gap.  The verifier does not import the certifier.

No certificate may report acceptance from floating roots, aggregate minima,
tolerances, a 60-vertex endpoint, a changed face ledger, or an unverified
checkpoint.  A failed phase writes a fail-closed receipt and names the first
exact or fresh-hull blocker.

## Materialized direct birth

The rejected endpoint `2ab419da49a2831cc29acb75bbaa739b71ca4a8996f666e872740d177fc11e01`
had an exact preceding zero family at `t ~= 0.800336403711988`:
`edge:(249,250):beta1` and
`face_raw:(228,249,250):(249,250)`.  Its two intended B aliases crossed only
at `t ~= 0.9900994101040146`.  `birth_ordering_diagnosis.json` preserves the
exact Bernstein/Sturm diagnosis and is bound to that rejected endpoint; the
old failure receipt is likewise historical, not current.

The proposer now performs an exact 1,943-row non-target raw-mechanics endpoint
sign gate after rationalization.  This rejected the old branch and selected
bounded branch `b10` (`post=33/32`, guard floor `1/4`, row230 inward factor
`1`).  The resulting literal checkpoint has SHA-256
`301ee45fecc7166d76fa8abadd53bf92d0c63224853cee191c4237493f84f11a`.
On this repaired ray the unchanged exhaustive locator proves all 7,920 other
primitives strict and isolates only
`edge:(1,54):t == vertex:1:54` at `t ~= 0.9696952724425052`.

`birth_certificate.json` has verdict `EXACT_U1_BIRTH_EPOCH_PASS`,
`post_birth_class233_checkpoint.json` has verdict
`EXACT_POST_BIRTH_CLASS_233_CHECKPOINT_PASS`, and
`birth_verification.json` has verdict
`INDEPENDENT_EXACT_U1_BIRTH_VERIFICATION_PASS`.  No preceding transfer was
needed.

## Materialized direct death and completed relay

The first bounded death grid exposed cancellation in the inherited normalized
double finite-difference support Jacobian: all rational candidates crossed a
frozen support wall.  The repaired death chart forms every support source value
and sparse first jet exactly over the rational source.  The exact endpoint gate
then selected branch `b01` (`post=101/100`, guard floor `1/20`, row230 factor
`1`) with zero changed support or non-target raw-mechanics signs.

Both row230 squared margins decrease on this branch, but remain exactly strict.
Monotonic margin growth is recorded only as a diagnostic; it is not part of the
stated preservation contract.  The two actual row230 support polynomials are
among the 5,959 rows proved strict by the unchanged exhaustive locator over the
whole epoch.

The literal FAR endpoint has SHA-256
`9f6c84382c05502766a17feb0cb9346bd44ec9f889e566e3e102d3d63a29ed77`.
The locator proves all 7,920 non-target primitives strict and isolates only
`edge:(1,54):one_minus_t == vertex:54:1` at
`t ~= 0.990119618496397`, with negative derivative.  The exact class changes
from `(2,3,3)` to `(2,2,2)`, removes unstable vertex `54` and saddle `(1,54)`,
and leaves unstable vertices `{1,8}` with saddles `{(5,6),(10,11)}`.

`death_ordering_diagnosis.json` independently enumerates exactly two root
candidates, both D aliases, with no preceding non-target event.  For each
alias its exact Sturm counts are zero roots before the isolated interval, one
inside it, and one on the complete unit epoch.  The diagnosis binds its own
implementation and the unchanged locator and is a mandatory input to both the
primary death certificate and independent death verifier.

`death_certificate.json` has verdict `EXACT_U54_DEATH_EPOCH_PASS`,
`far_u1_class222_checkpoint.json` has verdict
`EXACT_FAR_U1_CLASS_222_CHECKPOINT_PASS`, and `death_verification.json` has
verdict `INDEPENDENT_EXACT_U54_DEATH_VERIFICATION_PASS`.  No intermediate
transfer was needed; the segmented U54-to-U1 carrier relay is complete.
