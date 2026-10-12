# figure-0464

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Steady Finch 43 — exact closure of the anchor-91 one-anchor E310 chart

## Disposition

No strict110/additionalweak000 body is promoted. The authoritative entrance remains `QC52_SURVIVING_ROOT124_G9_F8B57E0F`, not the unrecovered historical 8adb object. The attached branch update identifies the prior C618 changed-interface checkpoint and the intended one-anchor E310 continuation. :contentReference[oaicite:0]{index=0}

This turn materially advances that continuation in two ways:

1. I produced and cold-replayed a source-complete **genuine one-anchor C620 exact checkpoint**, `QC52_C620_ONEANCHOR_A1E6_B1E2_OWN121`.
2. I proved an exact obstruction for the **entire two-parameter anchor-old91 chart**, not merely a finite search: every real `0<a<1, 0<b<1` member fails strict110. Thus this particular E310 chart is now closed.

The theorem does **not** cover the analogous charts that pin old109, old117, or old134, nor retained-support motion, multiple cuts, or changing the old pair being removed.

## Exact one-anchor C620 checkpoint

Let

- `a = 1/1000000`,
- `b = 1/100`,
- `P=(1-a)x120+a x117` on old edge120–117,
- `Q=(1-b)x124+b x134` on old edge124–134,
- and add the halfspace whose boundary plane passes through old91, `P`, and `Q`.

Exact signs show that the new halfspace removes exactly old vertices120 and124 and retains every other old vertex. Besides the pinned old91 crossing, it creates three genuine new crossings on old edges117–120,109–124,124–134. Rebuilding the actual maximal H-poly gives

`V=175, E=310, F=137, C=620`.

This is the intended final-edge one-anchor topology, not an inferred count.

### Complete mechanics and mass

Two independently implemented exact maximal-H/mechanics auditors agree byte-for-byte:

- strict `(S,U,H)=(1,2,1)`;
- additional weak `000`;
- primitive face/vertex/mixed-edge zero counts `000`;
- stable input face `3`;
- unstable raw-lex vertices `94,124`;
- saddle raw edge `125–135`;
- all137 supplied supports active.

The new cut facet is child face136 with cycle `[91,125,124,120]`. Stable face3 is now the 19-gon

`[62,100,153,155,158,161,164,166,168,170,165,163,151,150,149,135,125,91,66]`.

The degree histogram is `132×3, 34×4, 4×5, 4×6, 1×44`; the maximal-facet histogram is `50×3,35×4,24×5,13×6,7×7,3×8,2×9,1×10,1×12,1×19`. The minimum squared true-edge length lies in `[218568,218569]/10^12`, so the construction contains a short but exactly positive edge; no zero-length collapse is being counted.

Independent centered tetrahedral mass uses346 positive tetrahedra, agrees exactly with both auditors, has zero centered first moments, and has common centered-coordinate denominator42334 bits. Exact `/10^12` intervals are:

- volume `[488593193617,488593193618]`;
- raw centroid x `[-13246698662,-13246698661]`;
- raw centroid y `[5376686876,5376686877]`;
- raw centroid z `[-8754361232,-8754361231]`.

### Complete physical and polar landscapes

There is exactly one positive physical elder bar. It is no longer the singleton C618 packet: the strict-upper dying component is `[124,125]`. The peak is124, elder/global root94, death edge125–135, and the complete crossing cut is

`[91–125, 109–124, 120–124, 125–135]`.

A checked attaining true-edge path is

`[124,125,135,145,146,148,149,150,151,152,154,156,162,163,165,170,168,166,164,161,158,155,153,100,94]`.

Its exact normalized drop is `[418537428,418537429]/10^12` in units `delta/Vol^(2/3)`. This is only microscopically below the surviving C616 parent's `[418537478,418537479]/10^12`; the scientific value is the genuine E310 interface and two-vertex packet, not scalar bar improvement.

At the **same physical filled centroid**, the complete polar true-dual graph has137 vertices and310 edges, exactly one strict polar root (face3), no weak polar root, and every other polar vertex has a certified strict positive escape in a rootward forest of maximum depth74. Therefore `Qbars=[]` exactly.

Observed exact receipts:

- `RAW.json`: 12600 bytes, SHA-256 `060cfe10f073c39ede69f4b3375ddaf9b5980e85bcdad157c37a7413d1968e1d`
- `A.json = B.json`: 239058 bytes, SHA-256 `96f605e6057bd00aa285db78766503863c76ae9236eb063271e21b5c571cc8ba`
- `MASS.json`: 224 bytes, SHA-256 `939682271de622d94c2d6d75d7b6989b5b69a4e1792b6123a6492ee52c2fcfe8`
- `PHYSICAL.json`: 1321 bytes, SHA-256 `5276d61a695396edaf4b79c3be64d0620a54744e623c30c8e51591bec7844f24`
- `POLAR.json`: 1082 bytes, SHA-256 `b14a5c9c333f29be893b2a197890082933907440be86b41537a8034d7e49d1fe`
- `MANIFEST.json`: 1966 bytes, SHA-256 `d5511e7baf738b5bb84f48cc79262da474e862001e8b4d85af356079730a717a`

Observed endpoint marker:

`QC52_C620_ONEANCHOR_SOURCE_ONLY_FULL_AUDIT_PASS 6`.

## Exact obstruction for the whole anchor-old91 two-parameter chart

Define `K_(a,b)` for `0<a<1,0<b<1` by the same construction with

`P_a=(1-a)x120+a x117`,

`Q_b=(1-b)x124+b x134`,

and the cutting plane through old91, `P_a`, `Q_b`.

### Fixed true topology

The unscaled plane signs are bilinear in `(a,b)`. Their four exact corner values prove by bilinear Bernstein/convex-combination signs that, throughout the open square, exactly old120 and old124 are outside, old91 is the sole old vertex pinned to the new plane, and every other old vertex is strictly retained. The parent crossing edges are exactly

`91–120, 109–124, 117–120, 124–134`.

Thus the strict crossings are `109–124,117–120,124–134`, together with the pinned old91 endpoint. Every old maximal facet remains two-dimensional and the new quadrilateral cut facet is maximal. Hence every member has true

`V=175, E=310, F=137, C=620`.

Write the three new strict crossing vertices as `P` on117–120, `R` on109–124, and `Q` on124–134. Their cut-facet chain is `old91–P–R–Q–old91`; their external true-edge exits are `P→old91`, `P→old117`, `R→old109`, `Q→old91`, with `Q→old134` as the remaining possible route toward the old geometry.

### Uniform actual-centroid control

Only ten boundary-integration triangles vary in this chart. If `L(a,b)` is the positive linear-intersection denominator on old109–124, then `(1/100000 - V_removed)L` is a bivariate polynomial of bidegree at most `(2,2)`. Exact reconstruction plus exact Bernstein coefficients on `[0,1]^2` proves

`V_removed < 1/100000`.

Every removed-cap vertex lies in the convex hull of old vertices `{120,124,91,117,109,134}`. Each of those six vertices is exactly inside the radius-`5/8` ball about the parent's filled centroid, so the entire removed material is inside that ball. The removed-mass identity then gives the changed body's **actual** filled-centroid displacement

`|g_(a,b)-g_parent| < 1/50000`.

This is not a reference-center substitution.

The parent apex94 has44 unaffected true edges. For every one, the exact old negative radial derivative has squared magnitude larger than `(1/50000)^2` times the squared edge length. Consequently apex94 remains a **strict unstable vertex for every member of the whole chart**.

### Low-a obstruction: a second strict U is unavoidable

For the closed rectangle `0<=a<=1/100, 0<=b<=1`, exact bivariate score polynomials certify all four external derivatives

`P→old91 < 0`, `P→old117 < 0`, `R→old109 < 0`, `Q→old91 < 0`.

The coefficient digest of these four exact polynomial certificates is

`ef4da6e40306699fa6bafde323cf1c5e24591fa1a32ee7bc4970ae7b35e242cf`.

Suppose none of `P,R,Q` were strict U. Since P's external exits strictly descend, P would need a nonnegative escape `P→R`. Then the reverse derivative `R→P` is strictly negative because opposite edge derivatives sum to `-|P-R|^2`; with `R→old109<0`, R would need `R→Q>=0`. This makes `Q→R<0`; with `Q→old91<0`, Q would need `Q→old134>=0`. Therefore avoiding a strict U among the new chain forces a nonnegative three-link radial path

`P → R → Q → old134`.

That path is impossible at the actual centroid. Put

`A=|P-g|^2`, `B=|old134-g|^2`, `C=(P-g)·(old134-g)`.

For the whole parent edge120–117 about the parent filled centroid, one-variable exact Bernstein certificates prove

- `A > 9/25` and `A < 2/5`;
- `B-A > 1/600`;
- `1 < 4A-C < 7/6`;
- `(4A-C)^3 - 27 A^2 B > 1/600`.

The endpoint vectors to old134 differ by norm `<1/8`, and all involved endpoint radii are `<5/8`. Combining these exact margins with the actual-centroid displacement `<1/50000` preserves

`B>A`, `B<64A`, `4A-C>0`, and

`(4A-C)^3 > 27 A^2 B`.

For a three-link chain with nonnegative radial derivatives, multiplication of the three cosine inequalities and concavity of `log cos` gives the necessary three-link condition; in the branch used here its exact cleared form is

`B>A` and `[B>64A or (4A-C)^3 <= 27 A^2 B]`.

The strict reverse inequality above therefore excludes `P→R→Q→old134`. Hence at least one of `P,R,Q` is another **strict** U. Together with apex94, every `0<a<=1/100` member has at least two strict unstable equilibria.

The robustness calculation is explicit: with `eps=1/50000` and `E=(5/4)eps+eps^2`, the parent cubic margin stays positive because `1/600-36E>0`; throughout the centroid segment `A,B<2/5` and `0<4A-C<6/5`, which bounds the three partial derivatives of the cleared cubic by `26,5,5` respectively.

### High-a obstruction: two stable faces are unavoidable

For `1/100<=a<=1` and all `0<=b<=1`, two **fixed old maximal faces**, inputs2 and8, are simultaneously strict stable equilibria. Their complete true-dual neighbor sets in the clipped complex are

- face2: `[52,64,130]`;
- face8: `[5,9,20]`.

For fixed old supports i,j, the same-physical-centroid polar arrow sign is the sign of

`V[(n_i·n_j)h_i-|n_i|^2 h_j] + [|n_i|^2 n_j-(n_i·n_j)n_i]·M`.

After multiplication by the positive `L^2`, all six such signs are bivariate polynomials. Exact Bernstein coefficients on `[1/100,1]×[0,1]` are strictly negative, so faces2 and8 are both strict polar roots, equivalently strict stable primal faces. Their polynomial coefficient digest is

`75095c4775fd901e29a5606cd75774337fd53a3d53476628d7524bb8b2f13774`.

Thus every high-a member has `S>=2`.

### Whole-family conclusion and scope

The low and high regions overlap at `a=1/100`, so **every real member of the open anchor-old91 chart fails strict110**. This result is stronger than the prior finite search and is independent of whether additional weak equilibria happen elsewhere.

Observed theorem marker:

`QC52_ONEANCHOR_E310_WHOLE_CHART_EXCLUSION_PASS`.

`FAMILY_CERT.json` is1042 bytes, SHA-256 `c9141dabb9a9dbabcb2bd78c34f7578523a0dd6b291589dd9a36197166166f67`.

This theorem closes **all planes through old91** that remove exactly the pair `{120,124}` while their other three old crossing edges are met in their interiors. It does not close the corresponding one-anchor charts through old109, old117, or old134; those are genuinely different fixed-anchor families. It also does not cover moving retained supports/vertices, multiple cuts, or a different removed pair.

## What was tried numerically

A finite scan was used only to discover the structure: near the C618 boundary the genuine E310 interior is typically strict121 or strict132, while moderate parameters rapidly create many physical and polar roots. No numerical strict11 point was found. None of those finite observations is used as an exclusion; the exact theorem above supersedes them for the anchor91 chart.

## Most useful continuation

Do not spend more search on the anchor91 chart. The clean near-record options that remain outside the proved scope are:

- repeat the one-anchor construction with **old109, old117, or old134** as the pinned retained crossing endpoint and audit the complete two-parameter family;
- move retained supports/vertices together with the cut so that the external-descending chain used in the low-a theorem is broken;
- or use a genuinely multi-cut/contact change while compensating actual filled mass.

For a next fixed-anchor attempt, old109 or old117 is especially informative because it changes which nonsaddle/exit geometry is pinned rather than retaining the anchor91 stable-boundary geometry; this is a construction heuristic, not an exclusion or feasibility claim. Any promoted endpoint must again rebuild the maximal hull, actual uniform centroid, full strict/weak mixed-edge census and both same-center P/Q landscapes.

## Durable recovery capsule

Exact source parent: `figure-0434`, SHA-256 `037b2078e4f89986594472b0f6e0df78ecf3cb43bbfb82dee2eea017099c529f`, designation `QC52_SURVIVING_ROOT124_G9_F8B57E0F`. Its required parent `A.json` is230639 bytes SHA-256 `bf713a4201231250cfb98d45cc35f47f27afee73a7938f700ce51359ef3b19f5`, and parent `RAW.json` is11693 bytes SHA-256 `a2a309b2b8ed47fdeeeccc0b30a6eec38ee3e9bb030869fcbb221c0407eb4f2e`.

Save the literal decoder below as `RECOVER_QC52_ONEANCHOR_PACKAGE.py`. It is11573 bytes, SHA-256 `e1af476d0e0c6bd683861787fdc4ea7c827948e79aa841ef5ee6a14ab458013f`. It reconstructs, byte-for-byte:

- `RECOVER_QC52_ONEANCHOR_C620.py`: 9195 bytes, SHA-256 `c4f6f8f3e5225be2ee646541294dc002553275f512e7221ecac7af4eea463c15`;
- `QC52_ONEANCHOR_FAMILY_OBSTRUCTION.py`: 13426 bytes, SHA-256 `d62f53595119e3a83207d6eeacefc6e3e78a49d7908c88e3f3979e662de9e05e`.

Compressed package identities: decoded JSON23394 bytes SHA-256 `29d5fa2cd944fd42483c02e33f82932db2a64f18b4cfa032914e5a3adcc9f54c`; XZ8372 bytes SHA-256 `e42e292c5c5480ed311059ae4af86b6e104535e55d16c4d7a1b4a1fce95b53d0`; base85 10465 bytes SHA-256 `39d5523cc824a49a54648634fb82792d29628fda3e6f3867994ebf67a44bd95e`.

Reconstruction and verification commands:

```sh
python -B -S QC52_SURVIVING_RECOVER.py QC52_SURVIVING
python -B -S QC52_SURVIVING/RECONCILE_REPLAY.py --case ROOT124_G9 --out ROOT124_PROOF
python -B -S RECOVER_QC52_ONEANCHOR_PACKAGE.py ONEANCHOR_SRC
python -B -S ONEANCHOR_SRC/RECOVER_QC52_ONEANCHOR_C620.py QC52_SURVIVING ROOT124_PROOF ONEANCHOR_C620
python -B -S ONEANCHOR_SRC/QC52_ONEANCHOR_FAMILY_OBSTRUCTION.py ROOT124_PROOF/ROOT124_G9/A.json ONEANCHOR_C620/A.json FAMILY_CERT.json
```

Expected/observed terminal markers:

- `QC52_ONEANCHOR_PACKAGE_RECOVERY_PASS 3`
- `QC52_C620_ONEANCHOR_SOURCE_ONLY_FULL_AUDIT_PASS 6`
- `QC52_ONEANCHOR_E310_WHOLE_CHART_EXCLUSION_PASS`

The exact phase uses CPython3.13.5 standard library only with assertions enabled. The two whole-feature A/B auditors and centered-mass/basin implementations are inherited literal parent sources; the new family proof itself is standard-library Fraction arithmetic and exact Bernstein signs.


[Encoded source block omitted; the code in this passage is incomplete.]


## Acceptance boundary

No record changes. Canonical strict110/weak000 remains V176/E311/F137,C622. The new durable C620 endpoint is an exact own121/weak000 one-anchor checkpoint with `Qbars=[]`, while the **entire anchor-old91 two-parameter E310 chart containing it is now exactly excluded**. The next useful QC52 move must change the pinned anchor, retained geometry, or cut/contact architecture rather than refine this chart.
