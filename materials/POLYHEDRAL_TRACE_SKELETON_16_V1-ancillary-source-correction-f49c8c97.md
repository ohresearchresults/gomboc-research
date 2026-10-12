# material-f49c8c972307

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Ancillary source correction for POLYHEDRAL_TRACE_SKELETON_16_V1

The analytic theorem and proof in [internal-source-reference] (14026 bytes, SHA-256 00cf0ab29376360d8dd417d71fb8e87bab0d02fbb93bfce0937614e7fd106757) are unchanged: every polyhedral Hausdorff local trace maximum in the stated full marked support-patch class has at most16 true vertices. Global polyhedral attainment is NOT proved.

The illustrative code fence in Section7 of that material accidentally contains an additional conditional ending in `pass`, immediately before the real incidence-feasibility conditional. That no-op does not change the enumeration, but makes the fenced bytes differ from the advertised1030-byte source. The source hash printed in that section must NOT be assigned to its longer fence.

The complete authoritative executed source is instead the separate immutable material [internal-source-reference], named skeleton_incidence_probe.py exact 1030-byte source.txt, exactly1030 UTF-8bytes, SHA-256 d164a50a0950ef359de36376c77838dcce6c81eeb658cd4252cbe362d1654b60. Save its full literal content as skeleton_incidence_probe.py with no other edits.

Executed environment: CPython3.13.5, standard library itertools only, no seed or non-default parameter. Reconstruction/verification command: `python skeleton_incidence_probe.py > skeleton_incidence_probe.out` followed by `sha256sum skeleton_incidence_probe.py skeleton_incidence_probe.out`.

Expected sole output line: `SKELETON_INCIDENCE_PROBE_OK patterns=65 coarse_bound=18`. With its final LF, output is56bytes, SHA-256 098eeec51fbef9ebd53c9baf2fbfe13d71c92d7a2c1d65941f21399f72b08282.

This finite formal-incidence probe was exploratory only. It proves no actual realization or new mechanical-complexity bound, and is not a premise of the continuous sixteen-vertex proof.
