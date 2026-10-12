# figure-0283

AI research report · 2026-09-04 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Clear Willow 25 — immutable-parent source-collision determination

## Disposition

**EXACT SOURCE COLLISION; NO GEOMETRIC ENDPOINT PROMOTED.**

I did not construct `M42_WB25_BIHEX27`, add rows `6601,6602`, or claim a Gömböc. The assignment's named source and the runtime-owned literal parent payload are different exact polyhedra. The research-copy contract explicitly makes the literal payload authoritative and requires reporting a conflict rather than inventing missing data.

The journal integration summary identifies `figure-0281` as `M42_WB25_HX2_C8`, with 97 supplied rows, 71 active vertices, `(V,E,F)=(71,193,124)`, stable faces `[258,259,6503]` and `[6501,6502,6503]`, unstable vertex `248`, saddle `(248,6526)`, and proposed successor `M42_WB25_BIHEX27`.

Fourteen lines later, the immutable-payload section for the same result ID and the same declared SHA-256 begins `Clear Willow 25 — exact whole-basin annular cage`, not `M42_WB25_HX2_C8`. Its referenced archive is the whole-basin-cage object, not an HX2 archive.

## Exact collision matrix

| invariant | integration summary / assignment | literal payload and verified archive |
|---|---:|---:|
| endpoint | `M42_WB25_HX2_C8` | `EXACT_WHOLE_BASIN_ANNULAR_CAGE_NONWINNER` |
| supplied rows | 97 | 124 |
| active vertices | 71 | 97 |
| `(V,E,F)` | `(71,193,124)` | `(97,271,176)` |
| stable faces | `[258,259,6503]`, `[6501,6502,6503]` | `[0..16]`, `[900024,900005,900031]` |
| unstable vertex | `248` | `8` |
| saddle edge | `(248,6526)` | `(900017,900032)` |
| proposed new labels | `6601,6602` | no BIHEX27 data |

This cannot be a harmless relabeling: supplied-row count, active-vertex count, all three f-vector entries, critical-feature incidence, and unstable-vertex identity disagree.

## Independent finite audit

I materialized an independently replayable source-integrity certificate:

- Complete collision-audit archive (`M42_slot1_Clear_Willow_25_parent_source_collision_audit.zip`), SHA-256 `6191a2c56f594e41f7b9217f59faeddcb5b2af70b29c5f9bb591bbb72b72a168`.
- Machine-readable audit (`source_collision_audit.json`), SHA-256 `c8675556f433db99b259d87d43a51657c8d0439d63f6a14032bc96811ce41a88`.
- Independent verifier (`verify_source_collision.py`), SHA-256 `aa6b8f747f24fd1d0d47f9bd4a6b47011a5b467bd8a412fdbac88a6ca1c95fc9`.
- Clean replay transcript (`CLEAN_REPLAY.log`).
- Final manifest (`FINAL_MANIFEST.sha256`).

The verifier checks the following without relying on the summary interpretation:

```text
journal SHA-256
  ba9d43ff180a072ab3510960d704c508f3e30124ffc9a2f983adead6920f571f

integration-summary line
  6060

literal-payload start line
  6074

literal payload's referenced archive SHA-256
  8f390dae69ad2ea7fbb97f1cbe5c0616273b3b47654fed9e2315358c90d02cda

archive certificate
  supplied=124, active=97, f-vector=(97,271,176), class=(2,1,1)
  stable=[0..16], [900024,900005,900031]
  unstable=8
  saddle=(900017,900032)

label audit
  6501 absent
  6502 absent
  6503 absent
  6526 absent
  900005,900017,900024,900031,900032 present
```

A clean replay ends with

```text
EXACT_PARENT_SOURCE_COLLISION_CONFIRMED
```

and validates every checksum in the package.

## Why no BIHEX geometry is admissible from this input

The summary supplies only counts and feature names. It does not supply the 97 exact rows of `M42_WB25_HX2_C8`, its active/inactive ledger, maximal faces, true edges, exact ordinary centroid, 25-root path, seven-control atlas, or the proposed BIHEX27 incidence data. Those objects also do not occur in the authoritative literal payload or its verified archive.

Coordinates for `6601,6602` cannot be defined relative to faces `[258,259,6503]`, `[6501,6502,6503]`, and edge `(248,6526)` when rows `6501,6502,6503,6526` do not exist in the authoritative coordinate table. Any such construction would silently choose an unrecorded parent and fabricate the missing affine and oriented-matroid data. It could not satisfy the required all-supplied hull reconstruction, exact moment closure, chronology, perturbation certificate, verifier, or mesh.

I therefore did not substitute the whole-basin `900xxx` body and pretend it was HX2. That body has a different residual problem and a different evidence-forced successor.

## Exact continuation boundary

One of two source repairs is mathematically sufficient:

1. Supply the actual immutable `figure-0281` / `M42_WB25_HX2_C8` artifact whose certificate has 97 supplied rows, 71 active vertices, `(71,193,124)`, and labels `6501,6502,6503,6526`, including its exact coordinates, incidence, path atlas, and BIHEX27 design; or
2. reissue the assignment against the literal whole-basin-annular payload, whose certified residual packet is stable `[900024,900005,900031]`, unstable `8`, and saddle `(900017,900032)`.

Until one of those exact source identities is selected, there is no well-defined affine configuration on which to compute the requested shared quadrilateral, outgoing ports, ordinary-volume moments, death-before-birth order, or full normal-cone mechanics.

## Final conclusion

**SOURCE BLOCKER, EXACTLY CERTIFIED.** The named HX2 parent and the runtime-owned literal parent payload are not the same polyhedron. The discrepancy is combinatorial and metric-source-level, not cosmetic. No strict `(1,1,0)` winner or exact post-BIHEX nonwinner is claimed. The reusable output is the collision certificate and clean verifier above; the next valid research step begins only from a corrected immutable parent payload or a corrected assignment target.
