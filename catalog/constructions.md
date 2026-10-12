# Constructions and exact checks

The size measure is C = V + E + F − 2 = 2E, counted after merging coplanar faces. Equilibrium counts are (stable, unstable, saddle) about each solid’s own centre of mass at uniform density; “strict” counts hold with a margin and “weak” counts are borderline cases. [Notation](README.md#notation) lists the other terms.

| Construction | V / E / F | Evidence in this release | Scientific package |
| --- | --- | --- | --- |
| C622, VQ20 routed endpoint | 176 / 311 / 137 | Exact verification rerun; strict 1/1/0, weak 0/0/0 | [C622](../C622/README.md) |
| C632, BQ13 winner | 180 / 316 / 138 | Historical local exact replay; distinct from the C632 nonwinner | [BQ13 source](../results/history/figure/gomboc-C632-BQ13-2026-09-10/BQ13/) |
| C634, SOC construction | 182 / 317 / 137 | Historical exact verification of the SOC construction | [Source](../results/history/figure/gomboc-C634-2026-09-10/source-only/) |
| C648, rebuilt R7/R12 | 189 / 324 / 137 | AI-reported exact results; source integrity checked, mathematics not rerun locally | [Rebuilt family](../results/history/figure/gomboc-C648-REBUILT-2026-09-09/) |
| C746 | 235 / 373 / 140 | Historical local supplied exact replay, strict 1/1/0 and weak 0/0/0 | [C746](../results/history/figure/gomboc-C746-2026-09-09/) |
| C752 | 237 / 376 / 141 | Historical local supplied exact replay, strict 1/1/0 and weak 0/0/0 | [C752](../results/history/figure/gomboc-C752-2026-09-09/) |
| C1370 | 258 / 685 / 429 | Historical supplied exact construction and viewing-mesh diagnostic | [C1370](../results/history/figure/domokos-C1370-diagnostic-2026-09-08/gomboc-1370/) |
| C1374 | 258 / 687 / 431 | Historical local two-implementation exact replay | [C1374](../results/history/figure/domokos-C1374-2026-09-07/) |
| C5368 | 897 / 2684 / 1789 | Historical exact rational specimen and direct verifier | [897-vertex source](../results/history/figure/langi-review-2026-09-05/shortcut897-source/) |

The [historical-constructions download](downloads.md) adds the large geometry and audit files to their corresponding source directories. A Git-only checkout is sufficient for C622; some historical packages require that data download. Use a working copy for historical replays, since several original drivers write beside their inputs.

## Views of earlier specimens

![Historical C1374, equal-scale orthographic views](images/C1374.png)

C1374 has 258 vertices and 431 maximal facets.

![Historical C5368, equal-scale orthographic views](images/C5368.png)

C5368 is the 897-vertex specimen. The separate 1,213-vertex body in the same historical collection is a different construction.

## A documented local construction chain

The dated records and C622 source document this sequence. The separate S8 C624 benchmark is not its parent. The [construction history](construction-history.md) lists 136 identified bodies, their methods and source excerpts.

```mermaid
flowchart LR
    P[C630 GRID7] -->|edge contraction| Q[RL07 C628]
    Q -->|edge contraction| A[VQ20 C626 parent]
    A[VQ20 C626 parent] -->|merge physical contact nodes 155 and 156| B[C624 nonsimple]
    B -->|contract polar edge 88 to 118| C[C622 warm state: strict 8/1/7]
    C -->|rooted primal/polar routing and eight mass corrections| D[C622 routed: strict 1/1/0]
```

The finite generators and [protocols](../C622/source/PROTOCOLS.json) document the final steps. Whether new equilibria appear during the continuous numerical interpolation remains unproved. The [chronology](chronology.md) lists other constructions and verification dates.
