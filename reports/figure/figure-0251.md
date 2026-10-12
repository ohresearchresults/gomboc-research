# figure-0251

AI research report · 2026-09-03 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Vivid Quartz 58 — `E23-CY3` source-integrity determination

## Literal disposition

**`BLOCKED_SOURCE_COLLISION`; no winner or nonwinner determination for `E23-CY3`.** The acceptance gate is a materialized finite uniform-density polyhedron at its own exact ordinary-volume centroid, with strict `(S,U,H)=(1,1,0)`, complete irredundant V/H incidence, maximal faces, true edges, all full-cone margins, an independent verifier, and matching OBJ/STL.

The current journal identifies the source as an exact dyadic body named `E23T78`, with `(V,E,F)=(23,63,42)`, class `(3,4,5)`, intended stable face `[D,1,11]`, intended unstable vertex `8`, residual stable faces `[I,J,K]` and `[J,M,N]`, residual saddles `[J,M]`, `[J,N]`, `[U,W]`, `[U,Y]`, `[W,Y]`, and a certified positive cycle `W→Y→U→W`; it names `E23-CY3` as the next topology.

Those exact source bytes are not present. The only mounted and library-visible exact object named `E23T78` is a different endpoint with the same f-vector but strict class `(2,2,2)`, stable faces `[8,A,B]`, `[10,H,R]`, unstable vertices `8,O0`, and saddles `(A,O0),(R,S)`. Its own result explicitly identifies it as the two-support whole-packet endpoint, not the journal’s `(3,4,5)` source.

This is a material oriented-matroid and label-namespace collision, not a cosmetic mismatch. Without the missing exact source, the boundary disk, trihedral incidence, cycle-star genealogy, circuit equations, dependent moment system, and full normal-cone ledger are undefined. Any literal `E23-CY3` coordinates or exclusion theorem built from the available body would refer to the wrong polyhedron.

## Immutable provenance audit

- Portable audit archive (`vivid_quartz_58_e23cy3_source_integrity.zip`)
- Archive SHA-256 (`vivid_quartz_58_e23cy3_source_integrity.zip.sha256`): `1100a2768fe7435ac1f338d69f4a1b99a2c87a1ac7a1481288a283a48c761939`
- Complete source-consistency report (`SOURCE_CONSISTENCY_REPORT.md`)
- Deterministic verifier (`verify_source_collision.py`)
- Verifier transcript (`VERIFY.log`)
- Machine-readable local scan (`local_source_scan_result.json`)
- Journal-claimed signature (`expected_source_signature.json`)
- Mounted exact signature (`available_E23T78_signature.json`)
- Required source manifest (`REQUESTED_SOURCE_MANIFEST.md`)
- Checksummed manifest (`SHA256SUMS`)

Running

```bash
python verify_source_collision.py
```

terminates with `E23CY3_SOURCE_COLLISION_VERIFIED`. Every entry in `SHA256SUMS` passes, and the ZIP passes a complete compressed-data integrity test.

## Exact mismatch

| datum | journal source required by this assignment | exact object actually available |
|---|---|---|
| alias | `E23T78` | `E23T78` |
| f-vector | `(23,63,42)` | `(23,63,42)` |
| strict class | `(3,4,5)` | `(2,2,2)` |
| intended stable | `[D,1,11]` | `[8,A,B]` in the available branch |
| intended unstable | `8` | `8` |
| residual stable faces | `[I,J,K]`, `[J,M,N]` | `[10,H,R]` |
| residual unstable structure | at least two of `{W,U,Y}` | `O0` in addition to `8` |
| residual saddles | `(J,M),(J,N),(U,W),(U,Y),(W,Y)` | `(A,O0),(R,S)` |
| required cycle edges | `W-Y`, `Y-U`, `U-W` | only `W-Y` is true; `Y-U` and `U-W` are absent |
| coordinate denominator | not supplied in the journal summary | `512` |

The available exact label set is

```text
8,10,11,A,B,C,F,L,P,T,W,X,Y,U,V,G,H,K,J,R,S,O0,O1.
```

It lacks `1,D,I,M,N`. Therefore `[D,1,11]`, `[I,J,K]`, and `[J,M,N]` cannot even be expressed in that body. The exact hashes establishing the collision are

```text
current journal  969a8056057e9272b82e4d3086aeba0935ce031f42487908816a3d3b4f918f84
mounted report   a8199a02167f90b539aa622c3d73e3597f977db75c3ea372c9c85992f69adc27
mounted archive  5510fd038588df2902d8ee17731435c8dacd1ddaf875bdbd1f8be598d66e2a6b
```

Reference bytes: available exact report (`E23T78_exact_report.json`), available archive (`vivid_quartz_58_nonflippable_core_nonwinner.zip`).

## Recovery work actually performed

### Local exact-artifact scan

The verifier recursively inspected mounted JSON and text artifacts, excluding its own output. It found **zero** non-journal JSON objects simultaneously carrying f-vector `[23,63,42]` and class `[3,4,5]`. Twelve local filenames contain `E23T78`; all belong to the older `(2,2,2)` package. The only local text containing `E23-CY3`, `W→Y→U→W`, or both residual stable faces is the current research journal itself.

### Connected-library retrieval

Searches covered the alias, successor name, assignment id `figure-0244`, `1,429-sign`, intended face `[D,1,11]`, both residual stable faces, all five residual saddle edges, and the cycle `W→Y→U→W`. Retrieval surfaced coordinator journal summaries of the `(3,4,5)` result and the complete older `(2,2,2)` package, but no V table, H table, face/edge list, centroid ledger, chamber certificate, verifier, mesh, archive, or first SHA-256 for the `(3,4,5)` source.

### Attempts to reject an easy substitute

These tests are empirical diagnostics only and are not used as a theorem about `E23-CY3`.

1. I sampled `1,228,800` determinant-one SPD images of the available exact `(2,2,2)` `E23T78`. `35,957` images had count class `(3,4,5)`, but **none** had the assignment’s required packet pattern: an unstable triangle whose three edges are saddles together with the two `J`-centred stable/saddle faces. Receipt (`available_E23T78_SPD_pattern_scan.json`) and log (`available_E23T78_SPD_pattern_scan.log`).
2. I reversed the target on the exact ten-vertex `E10R`, which does contain `[D,1,11]` and unstable `8`. None of its `288` first-order separator branches was feasible. Receipt (`e10r_reverse_target_search.json`). This does not identify the missing 23-vertex source and does not exclude nonlinear or topology-changing continuations.

These checks make a simple relabelling or affine-image explanation unlikely, but the decisive issue is still byte-level provenance: the exact source required to define the task was not transferred.

## Why the requested exact evidence cannot be reconstructed from the paragraph

A simplicial 23-vertex sphere is not determined by `(23,63,42)` or by five equilibrium labels. In particular:

- the cycle `W-U-Y` does not specify the incident face stars or the boundary of the disk to replace;
- `[I,J,K]`, `[J,M,N]`, `(J,M)`, and `(J,N)` do not determine the remaining adjacency or orientation signs;
- the 1,429 inequalities are not recoverable from their count;
- exact mass polynomials depend on the complete oriented boundary triangulation and coordinates;
- negative escape arrows depend on the exact own centroid and actual neighbor vectors;
- a positive-volume trihedral surgery needs a common boundary complex and an embedded source realization;
- an independent verifier and matching mesh cannot be compared against a source that has no transferred V/H representation.

Accordingly, no coordinates, event chronology, perturbation radius, residual forcing component, OBJ, or STL for `E23-CY3` are claimed here.

## Minimum immutable continuation input

The source-recovery boundary is finite and explicit. The following bytes are required before the geometric continuation is well posed:

1. the first-published SHA-256 and archive/result identifier for the `(3,4,5)` `E23T78`;
2. the exact active label list and dyadic/rational coordinates, including `D,1,11,I,J,K,M,N,W,U,Y,8`;
3. all 42 maximal-face cycles and 63 true edges, including `W-Y`, `Y-U`, `U-W` and `[D,1,11]`;
4. exact ordinary volume, three first moments, centroid, and identities `M=VC`;
5. exhaustive face, vertex, and four-component true-edge-cone ledgers proving `(3,4,5)`;
6. the complete 1,429-sign chamber certificate with variable domains;
7. its perturbation or implicit-root proof, independent verifier, and OBJ/STL;
8. enough source lineage to distinguish this namespace from the older object with the same alias.

## Exact continuation once the source is restored

The smallest reusable program is then:

1. reconstruct and hash-check the source independently;
2. extract the union of the `W-U-Y` triangle star and the two `J`-centred stable/saddle stars, including its true boundary cycles;
3. enumerate connected three-page and minimal stronger 3-ball replacements that remove at least one of `W-Y`, `Y-U`, `U-W` and couple both `J` saddle channels in the same incidence event;
4. reject candidate cells before moment solving unless every surviving nonprotected internal carrier has a certified negative external arrow;
5. reserve at least three physical shape variables after eliminating the three ordinary moments through the dependent exact centroid;
6. isolate every actual circuit/support/mechanical root, audit all strict cells and walls, and exactify the first `(1,1,0)` cell; otherwise prove the minimal surviving component on the chamber actually covered.

## Reusable conclusion

The new fact relative to the supplied journal is a **proven source alias collision**. The journal’s exact `(3,4,5)` `E23T78` is not represented by the exact `E23T78` bytes available to this copy. The available body has the same f-vector but a different label set, edge graph, equilibrium packet, and class. Therefore the requested `E23-CY3` construction cannot be defined, verified, or honestly excluded from the supplied materials.

**Final status: real source-provenance blocker; no fabricated winner, no fabricated nonwinner, and no topology exclusion for `E23-CY3`.**
