# figure-0132

AI research report · 2026-08-28 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Determination

**No winner.** I materialized a genuine finite-width, four-sector two-cell/Y-zipper beyond the M42 terminal relay and exactified its strongest endpoint. The new body deletes the inherited true edge `(47,53)`, deactivates both relay endpoints 47 and 52, gives the terminal sector three independent outgoing true-edge routes, and replaces the inherited stable and saddle stars in one global hull rebuild. After exact closure of all three ordinary moments and a complete own-centroid audit, the endpoint is a strict open `(S,U,H)=(2,2,2)` nonwinner. A new cell-wide external-positive obstruction occurs on true edge `(64,68)`.

The supplied journal explicitly materializes the original 42 M42-SLP rows, but it records the later `(35,85,52,170)` relay only by its f-vector, class, deleted rows, and obstruction `(47,53)`, without listing the relay coordinates. Consequently, I rebuilt an exact terminating-decimal representative of that same reported terminal cell. It exactly matches `(V,E,F,C)=(35,85,52,170)`, strict `(3,3,4)`, the row labels, independent unstable vertex 8, and the external-positive true edge `(47,53)`. I do **not** claim byte identity with the unavailable worker-local relay object.

# What was constructed

The rebuilt predecessor uses rows `0..59`. I then inserted 22 exact 12-decimal bridge rows `60..81`, each placed outward from a selected predecessor face. Their selected-face adjacency contains a 12-cycle

`65-66-67-68-69-70-71-72-73-74-75-76-65`,

a right arm `60-61-62-63-64-65`, and northern cells through `77,78,79,80,81`. Thus this is a finite-width two-dimensional support complex with transverse incidence, not another serial terminal relay.

Every added row `60..81` is extreme after the event. The post-event active source rows are

`0..16, 43,49,50,53,54,57,58,59, 60..81`.

The predecessor-active rows

`33,42,44,45,46,47,48,51,52,56`

deactivate together. In particular, vertices 47 and 52 are inactive and edge `(47,53)` is absent.

Terminal row 68 has three internally disjoint outgoing true-edge routes:

```text
right: 68-63-62-60
left:  68-70-71-72-73
north: 68-67-66-75-79-81
```

The inherited stable faces `[44,57,58]` and `[56,58,57]`, terminal saddle `(47,52)`, and northern saddle `(57,58)` disappear. The old right/left saddles `(4,50)` and `(13,49)` become nonsaddles and are replaced by `(4,60)` and `(49,73)`.

# Exact endpoint

The postbridge has

```text
(V,E,F,C) = (47,121,76,242).
```

Its exact unshifted volume is

`11770270552119553611368543610015744943 / 3000000000000000000000000000000000000`

`≈ 3.9234235173731844`.

Its exact unshifted centroid is

```text
Cx =  28434543344050535101575199923132460589320843340517
      / 94162164416956428890948348880125959544000000000000

Cy = -2673681543014130762349991868410783730149958978417
      / 3362934443462729603248155317147355698000000000000

Cz = -27250830448833544599798131696161393364056322115219
      / 94162164416956428890948348880125959544000000000000
```

or approximately

`(0.30197419016560045, -0.79504420557812228, -0.28940318669996823)`.

For each oriented boundary triangle, volume and first moments were accumulated exactly as

```text
V = Σ det(a,b,c)/6,
M = Σ det(a,b,c)(a+b+c)/24.
```

The three translation coordinates were then eliminated as the hard dependent equations `τ=-M/V`. Only after substituting those exact values was mechanics evaluated. The centered coordinate file therefore has exactly `Mx=My=Mz=0`; no auxiliary mechanical center or soft moment objective is used.

# Complete mechanics and margins

The exhaustive own-centroid class is

```text
(S,U,H) = (2,2,2).
```

Stable maximal faces:

```text
[0,1,2,...,16]    protected 17-gon
[57,79,78]        residual stable triangle
```

Unstable vertices:

```text
8                  protected target
68                 residual maximum
```

Saddle true edges:

```text
(4,60)             right sector
(49,73)            left sector
```

Normalized endpoint margins are:

```text
target stable 17-gon                  +0.05217722070108715
target unstable vertex 8              +0.37281835418604264
residual stable face [57,79,78]        +0.04837948511028132
residual unstable vertex 68            +0.27207798411980120
saddle (4,60)                          +0.21464462864948220
saddle (49,73)                         +0.14386756843690962
minimum absolute face decision          0.022780814286547244
minimum absolute vertex decision        0.07539794516691552
minimum absolute edge-cone component    0.0008901319046306089
```

Every one of the 121 true edges has a complete four-component audit: segment parameters `t,1-t` and both incident-normal coefficients, in exact rational and normalized form. The full ledger is in the archive.

# New rigorous obstruction

The transferred obstruction is the true edge `(64,68)`, incident to faces `[63,68,64]` and `[64,68,67]`. For centered vertices define

`σ(i→j)=-X_i·(X_j-X_i)`.

Every support from either endpoint to a neighbor outside `{64,68}` is strictly positive:

```text
64→63  +0.13832926816061394
64→65  +0.19131459485589633
64→67  +0.027865758470135733

68→43  +0.84097951661388337
68→53  +0.25923931984281456
68→63  +0.45950617096470897
68→67  +0.13055185021904139
68→69  +0.28004584143703470
68→70  +0.37697533980565223
```

The two mutual supports are

```text
σ(64→68) = -0.074874655557203559
σ(68→64) = +0.27998287019680157
```

and satisfy the exact identity

```text
σ(64→68)+σ(68→64)
 = ||X68-X64||²
 = 51277053659899503536843 / 250000000000000000000000
 > 0.
```

Therefore at least one mutual support is positive. Because every external support at both endpoints is positive, at least one endpoint is necessarily unstable throughout this realized incidence/external-sign cell. At the exact endpoint it is vertex 68. Vertex 8 is independently unstable, so the whole certified cell has `U≥2`. This is a proof of nonwinning status for the realized cell, not merely a search failure.

# Directed perturbation box

Rows `0..16` are fixed to preserve the single maximal 17-gon. Every scalar coordinate of every other active row—90 independent coordinates—is allowed to vary by `±1e-10`.

Outward interval arithmetic certifies throughout the complete box:

```text
incidence                     (47,121,76)
class                         (2,2,2)
all bridge rows 60..81        extreme
old edge (47,53)              absent
new edge (64,68)              true and external-positive
target vertex 8               independently unstable
```

The centroid enclosure is

```text
Cx ∈ [ 0.30197418747485927,  0.30197419285634153]
Cy ∈ [-0.7950442124189351,  -0.7950441987373095]
Cz ∈ [-0.2894031886033941,  -0.28940318479654226]
```

Certified lower clearances are:

```text
inactive-incidence/topology     6.060970377915988e-6
volume                           3.923423506286902
face decisions                   0.002757365283479645
vertex decisions                 0.07487461895912019
edge four-component decisions    0.0008899665041945405
edge Gram determinant            2.134258696238745e-12
external-positive obstruction    0.02786572214506636
```

# Independent reconstruction and mesh

`verify_exact.py` is standard-library-only. It independently performs:

1. exhaustive **V→H** supporting-plane enumeration from all input rows, including inactive rows;
2. exhaustive **H→V** triple-plane intersection followed by every halfspace test;
3. exact volume, centroid, and moment integration;
4. complete maximal-face, vertex, and true-edge reconstruction;
5. the full two-normal/four-component cone solution on every true edge;
6. exact obstruction identities for predecessor `(47,53)` and postbridge `(64,68)`.

Its reproduced output is:

```text
PASS predecessor: V/E/F/C=(35, 85, 52, 170), class=(3,3,4), min external support=0.10856803745177947
PASS postbridge: V/E/F/C=(47, 121, 76, 242), class=(2,2,2), min external support=0.027865758470135733
PASS exact V->H, H->V, centroid, moments, complete mechanics, and obstruction audits
```

The interval verifier independently passes the full 90-dimensional box. Both OBJ and STL are watertight after STL vertex merging, have 47 vertices, 90 triangles, Euler number 2, consistent winding, volume `3.9234235173731853`, and mesh center of mass below `5.4×10^-17` in every coordinate.

# Attempts to break the conclusion

I numerically scanned one-row caps above each incident face of `(64,68)`, a bisector row, and symmetric two-row caps over depths `0.001..1.2`. These additions can delete the edge, but the extra maximum remains at 68 or transfers to a cap vertex. No tested local cap improved below `(2,2,2)`. This is supporting evidence only; it is not claimed as an exclusion theorem for arbitrary caps.

# Smallest next topology

The residual Euler-neutral block is:

```text
extra stable      [57,79,78]
extra unstable    68
right saddle      (4,60)
left saddle       (49,73)
structural edge   (64,68)
```

Moving from `(2,2,2)` to `(1,1,0)` requires one stable–saddle and one unstable–saddle cancellation. The smallest face-disjoint pairing found has 13 face cells and attains the independent dual-distance lower bounds.

Terminal-to-right strip, 6 dual edges / 7 faces:

```text
[63,68,64]
[43,68,63]
[43,53,68]
[43,61,53]
[50,53,61]
[50,61,60]
[4,50,60]
```

Northern-stable-to-left strip, 5 dual edges / 6 faces:

```text
[57,79,78]
[57,75,79]
[74,79,75]
[49,74,75]
[13,74,49]
[13,49,73]
```

These paths are face-disjoint and realize the shortest individual distances `6+5`; hence 13 face cells are graph-theoretically minimal for this pairing. The symmetric terminal→left / north→right pairing also requires 13 cells.

The smallest honest continuation is therefore a **13-row two-rail zipper, or genuinely three-dimensional two-cell equivalent**, on those two strips. It should keep the three moments as dependent exact equations in every rebuilt cell and permit at least rows

`43,49,50,53,57,60,61,63,64,68,73,74,75,78,79`

to deactivate while both Morse cancellations cross together.

# Materialized artifacts

- Complete exact archive (`M42_2cell_postbridge_exact.zip`) — SHA-256 `5c0eabcf0ab96bf9e75b8672460f81b77d4cb198d7d8bda70421b7f99e107ddc`
- Full research handoff (`research_handoff.md`)
- Exact independent V/H verifier (`verify_exact.py`)
- Outward interval verifier (`verify_interval.py`)
- Exact centered V-representation (`coordinates_postbridge_active_centered.csv`)
- Exact centered H-representation (`halfspaces_postbridge_centered.csv`)
- Complete 121-edge four-component audit (`edges_postbridge_four_component_audit.csv`)
- Complete actual face incidence (`faces_postbridge.json`)
- Next-topology certificate (`next_topology.json`)
- OBJ (`body.obj`)
- STL (`body.stl`)

The archive was extracted into a clean directory; `sha256sum -c SHA256SUMS`, `python3 verify_exact.py`, and `python3 verify_interval.py` all passed there.
