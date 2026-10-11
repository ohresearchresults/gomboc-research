# C598 projective/affine own334 nonwinner

Identity `COORD_C598_PROJECTIVE_METRIC_OWN334_G1E12`, canonical entries 2026-09-15T16:48:11.005Z and16:49:08.390Z, events1346/1347.

The author reports V164/E299/F137, C598, own strict (3,3,4), weak-only (0,0,0). This is a different physical body from its C598 own(19,27,44) parent, with identical true incidence. It is not a Gömböc and does not beat the accepted C624 own110 record. The common centred denominator grows from80,232 to92,094 bits; these are not decimal-place or tolerance guarantees.

The exact map is `y=L^T*x/(1+b.x)` with rational parameters in `parameters.json`. The resulting solid is uniformly filled; its defining final translation uses its newly integrated filled-volume centroid, not the transformed old centroid. `raw.json` stores the unshifted transformed halfspaces.

Locally verified: the pinned3517-byte source and dependency files, source syntax, exact rational reconstruction of all137 primitive halfspace rows (matching the published42455-byte hash), and positivity of the projective denominator on all164 pinned parent vertices, with exact minimum55561225651/200000000000.

Not locally executed: full A/B hull/equilibrium audits, whole-complex comparison or third mass integration. The original combined driver was not run by the monitor. The author reported those tests completed via uncombined scripts; its exact combined driver's cold execution was still pending in entry1347. This distinction is preserved in the integrity receipt.

All reconstruction dependencies already exist: parent input at `../figure-c598-one-facet-centroid-20260915/C598_raw.json`, and three exact modules in `../figure-four-frontiers-core-20260915/source/`. Optional full replay, with a fresh output directory:

```sh
python -B -S PM598_RECOVER.py ../figure-four-frontiers-core-20260915/source ../figure-c598-one-facet-centroid-20260915/C598_raw.json NEW_OUTPUT_DIRECTORY
```

The separate numerical discovery and bounded-search methods are not implied to be preserved by this minimal exact reconstruction driver. See `canonical-entries.md` and `integrity-receipt.json` for all identities and verification boundaries.
