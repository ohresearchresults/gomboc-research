# figure-0401

AI research report · 2026-09-17 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Bright Willow 35 — C260 actual-mass core restrictions

Assignment: `figure-0401`.

## Closing outcome

**No new polyhedron, exact nonwinner, or own110 endpoint is claimed.** The retained construction is the inherited `C260_COARSEN_COUNT`: V74/E130/F58, C260, own211/weak000, with180 true edges of headroom under E<=310. Its stable carriers are original C384 planes31/77; its own labels are S14/37, U65, and saddle edge66--72. The unstable vertex is a genuinely new intersection, not an inherited C384 vertex. The accepted own110 C622 endpoint is unchanged by this assignment. These parent identities agree with the attached immutable payload.

The new result is **`BW35_C260_OWN_MASS_CORE_RESTRICTIONS_V1`**, an exact C260-specific disk/slab certificate and three infinite-family restrictions that incorporate the successor's actual uniform mass. In particular, a contained disk-preserving cut cannot produce own110 while retaining at least92% of C260's volume. Two homothetic sandwich families also cannot produce own110, without imposing the successor's centroid externally.

I completed source recovery, the exact reconstruction needed for these certificates, their mathematical derivation, and a fresh source-only cold replay. I did **not** complete a nonlocal optimization campaign or obtain a new candidate. The constructive objective remains unresolved; the restrictions below leave nonlocal surgery outside their hypotheses unexcluded.

## Evidence and reading boundary

The exact parent is `figure-0398`, SHA-256 `b6c84be62ea56d1c11575d4d6309563f525d734f79b0ad2a299f0b7abd2ccdd3`. Its embedded37-file dictionary decoded to146068bytes, SHA-256 `8f6e206a6c8e7163b76623200840b024bd13643ed66b435d8e6358a48da4dacf`. All36 listed source/input hashes matched; the manifest is the37th unit. Relevant complete sources and exact inputs were read before use. The smaller standalone capsule below contains every dependency actually used, including the literal original coordinates and C260 support selection.

Read-only library work included the first catalog page, the first C260 search batch, the complete current brief at revision1930, SHA-256 `6fa52a875b6d63345927f5a7df7afa3fe65bf353410f6d1bbb75f8d821fd8e81`, and the complete newly available CA95 result `figure-0399`, SHA-256 `c30ee459df73233920d909ab76375f089eae0cb264d9520a9db9ac700549c7da`, through EOF. The entire472-source archive was not exhaustively searched. CA95's disk/slab proof informed the mechanism; its other34 nonliteral constructions and external recovery parts were not inputs here. No scheduler or journal mutation was made.

## Exact C260 geometry used by the new certificate

Let P be the exact C260 body and **P0=P-centroid(P)**. Every inclusion and dilation below uses this fixed actual-centroid origin, not the original C384 origin and not an independently recentered successor.

With `a=(-4,5,8)` and `|a|²=105`, exact rational checks establish:

- The unit disk `D={x:a·x=0, |x|<=1}` is contained in P0.
- P0 lies in the slab `|a·x|<36/5`.
- P0 lies in the ball `|x|<23/10`.

For each original-frame maximal support `n·x<=h`, write `h0=h-n·centroid(P)`. Disk inclusion is checked on all58 supports using

`h0>0` and `105*h0² > 105*|n|²-(a·n)²`.

The slab and ball bounds are checked on all74 extreme vertices. These are exact inequalities, not toleranced hull screens.

## Disk/slab lemma with orthogonal centroid components

Let a full-dimensional convex polyhedron K contain the radius-r disk in the plane perpendicular to a through zero, and lie in `|a·x|<=b`. Write its actual uniform centroid as `z=t+s*u`, where `u=a/sqrt(105)` and `t·u=0`. If

`r > b/sqrt(105)+|t|+|s|`,

then K has **at least two strict stable maximal facets about z**.

Proof. Put `Q=(K-z)^polar`. An equatorial q in Q, with `q·u=0`, satisfies `r*|q|-q·t<=1`, hence `|q|<=1/(r-|t|)`. The slab makes both

`u/(b/sqrt(105)-s)` and `-u/(b/sqrt(105)+s)`

feasible points of Q. Their denominators are positive because z is interior. Each has norm at least `1/(b/sqrt(105)+|s|)`, strictly greater than the equatorial bound. Therefore a greatest-norm point of each closed half `Q∩{±q·u>=0}` lies in its open half.

For such a maximizer q, any distinct w in Q with `q·(w-q)>=0` would strictly increase squared norm along a sufficiently short segment from q toward w that remains in the same half. This includes equality in the linear term because the quadratic term is positive. Consequently q strictly exposes itself radially against every other point of Q. The two maximizers are distinct polar vertices. Their physical dual feet `q/|q|²` satisfy their respective facet equalities and every other maximal support inequality strictly, giving two strict stable facets. No centroid of Q is used.

Since `|t|+|s|<=sqrt(2)*|z|`, a sufficient condition for `|z|<=eta` is

`r-sqrt(2)*eta-b/sqrt(105)>0`.

The executable uses the stronger, entirely rational sufficient check

`gap = r-(10/7)*eta-(5/51)*b >0`,

because `sqrt(2)<10/7` and `sqrt(105)>51/5`. For `r=1`, `b=36/5`, and `eta=1/5`, this gap is **1/119**. This specializes the CA95 mechanism and sharpens its sufficient estimate through orthogonal centroid components; it is not presented as a new general convexity theorem.

## Restriction1: contained disk-preserving cuts with actual mass

Suppose `D⊂K⊂P0` and `Vol(K)>=23/25*Vol(P0)`. Put `tau=Vol(P0\K)/Vol(P0)<=2/25`. Since P0 has zero first moment and every removed point has norm at most23/10,

`|centroid(K)| <= (23/10)*tau/(1-tau) <= 1/5`.

K inherits the slab and retains D. The lemma therefore supplies at least two strict stable maximal facets.

**Any contained, disk-preserving own110 successor must remove strictly more than8% of P0's filled volume.** This is a necessary condition, not sufficient. It does not apply to cuts that break D or to geometry added outside P0. It allows arbitrary new faces, vertices and equilibrium-carrier turnover.

## Restrictions2–3: homothetic sandwiches without a prescribed centroid

Suppose `lambda*P0⊂K⊂mu*P0`, with `0<lambda<=1<=mu`. Then K contains the radius-lambda disk and lies in the slab with `b=mu*36/5`.

Relative to P0, the added and removed volumes are at most `(mu³-1)*Vol(P0)` and `(1-lambda³)*Vol(P0)`. Points in these regions have norms at most `mu*23/10` and `23/10`, respectively. Zero first moment of P0 and `Vol(K)>=lambda³*Vol(P0)` give the bound on the **actual** centroid:

`eta=(23/10)*[mu*(mu³-1)+(1-lambda³)]/lambda³`.

For `lambda=39/40`, `mu=1`, the exact values are

`eta=107663/593190`,

`gap=2776799/282358440>0`.

For `lambda=79/80`, `mu=81/80`, the exact values are

`eta=71106823/394431200`,

`b=729/100`,

`gap=17901573/1173432820>0`.

Thus every full-dimensional convex polyhedron in either sandwich family has at least two strict stable maximal facets at its own filled-solid centroid. These restrictions concern literal geometric inclusions around the fixed C260 centroid. They are not labelled polar-coordinate bounds, Hausdorff-distance bounds, physical-vertex deletion thresholds, or limits on the number of permitted features.

## Verification actually executed

The recovered original C384 report matched50185bytes and SHA-256 `3761fcd1bcc014f71030378a0c3cdce69742e386536ad6c524954003adebdbc5`. The reconstructed C260 report matched113928bytes and SHA-256 `2894aaa74771ebd7e735eb42baec96f81208562970178b1ca9154cac1f25f973`.

The independent A/B implementations agreed on the maximal hull, oriented incidence, true edges, ordinary filled volume and centroid, and all strict/weak face, vertex and edge equilibrium tests. The third integer integration used144 positive centered tetrahedra with exactly zero first moments. Centered denominator/integer costs remain11569/11570bits: no coordinate simplification or new body is claimed.

A separate helper-independent all-support-triples program reconstructed the complete vertex set and every maximal-facet owner set. It tested30856 triples and recovered74 distinct feasible vertices. Its140byte output has SHA-256 `625d86117b0e832dca0eb48afd94ba1ec647ef344c94a13587c04903a0125fcc`.

The new certificate checks all58 maximal supports and74 vertices using rational arithmetic. Its1334byte JSON has SHA-256 `7881cada4cd616ea372a7172a31fc0ff303a03db712b9901c803ff611a15b388`. Every expected output hash matched a fresh decoder-based cold replay.

The rational gaps above are sufficient-condition slacks in the disk/slab inequalities, **not minimum all-feature equilibrium margins or optimizer escape margins**. No numerical near-coplanarity count, reference-center110 census, small zero-target loss or convergence flag is promoted. Execution verifies the exact geometric premises and arithmetic; the theorem is justified by the mathematical proof above, not by a formal-machine proof checker.

## Most useful continuation and scope

These are C260 own-mass restrictions, not an extension of the obsolete fixed128-generator C384 polar-chart obstruction. They impose no fixed roots, fixed incidence or edge-count assumption. They do not prove any global impossibility.

A constructive continuation should explicitly break the protected disk, leave the certified slab/core enclosure, or create enough actual moment change to leave the centroid regime. For a proposed cut `n·x<=h` in the P0 frame, preservation of D is exactly

`h>=sqrt(|n|²-(n·a)²/105)`.

The sign of h must be checked before squaring. A disk-breaking cut avoids the corresponding hypothesis but does not guarantee cancellation: its newly created stable faces and opposite-side moment-carrying region must be modified together. This handoff supplies no evidence that such coupled nonlocal surgery is impossible. Retain the E<=310 budget and recompute actual maximal features and filled mass at every proposed exact endpoint.

## Complete standalone recovery capsule

Save the complete program below as `BW35_RECOVER.py` and execute:

`python -B -S BW35_RECOVER.py BW35_FRESH`

Executed environment: CPython3.13.5, standard library only, assertions enabled. There are no random seeds, optimizer options, third-party packages, network requests, ancestor downloads or omitted helpers. The decoder reconstructs ten units: `PARENT_INPUT.json`, `PARENT_BUILD.py`, `C260_INPUT.json`, `EXACT.py`, `EXACT_SUPPORTS.py`, `INDEPENDENT_TRIPLES.py`, `BW35_CORE.py`, `REPLAY_CORE.py`, `PROOF.md`, and `MANIFEST.json`.

Dictionary:32694bytes, SHA-256 `7286890bb97d71d9adaa7b05276d492f4bd89eed991c8aebaa75d5f622c6e6bc`. XZ:12956bytes, SHA-256 `f4f5284fb2db87c8eda8d07efe3402feaea30f32d5d9d1a7e9446205aa5e50b6`. Whitespace-free base64:17276bytes, SHA-256 `be0ab5a6d258a34aca4c37a0d3bb79111de73ba3ed5f3fc0b3e21d4159dee55a`.

Expected terminal markers:

```text
BW35_STANDALONE_10_SOURCE_FILES_HASHES_PASS
BW35_C260_ACTUAL_MASS_CORE_RESTRICTIONS_ALL_PASS
BW35_C260_SOURCE_ONLY_AB_TRIPLES_MASS_AND_CORE_CERTIFICATES_PASS
NO_NEW_POLYHEDRON_OR_OWN110_CLAIM
```

```python
#!/usr/bin/env python3
# CPython 3.13.5 standard library; assertions must remain enabled.
from pathlib import Path
import base64,lzma,json,hashlib,subprocess,sys
assert __debug__
DATA = """
/Td6WFoAAATm1rRGAgAhARwAAAAQz1jM4H+1MlldAD2IhEVxpTfj8Reb7iCkPHa5Ix4jbSbbqAwNQOarrHjtK7q1RBTdcYcp/V9ghpO5ktIISjn8ZKoZ3+NT
uAYq5f8fRip8Zwr15asygDZWFx6+zj2FYFkOGBBM9OMQideYQ+p87Suj6J229kbSriLuYtzxr7hcLEWqf6kUA7IcDcnilKtd5HPfm7WYJEvP9ZXez2qJ0h5X
X+QWkZxwN2wrLqAhtXFv0mOuZgtTCHpmq8dxy5PoZrSDX4R5Rx0qwhdV7gms7TGnJPZjkPV+vzxu5TN5dDi0ENqe1weBOAK0R/gP5I73y7V43STmin7kC3SA
7aiXSP9vHu4t8vyJiikAfnADqKuS6WBw8mkh4ttl+/hyxfHXC+PwnfyvezsdCF/dpdEuvDqX8CLV9O/egkfprHV9MIr7rPSJ8jYHqwWn0dzqRVG9s/uzOUXG
3VKVMS/rKWpXx/8Fuj192qgU70zhdk0tl0Ps6+hIILpaGXI/B6KqIzxz4vGKskDfEPN5erdJzKvM0KNNEW07Icy4bjGHxlQXMkqXoenSJNpjKFYwu9nqGitK
eDpQtaBbqvXE2b7pvbPZ7BgFzW3lxw3NR33gUdV2Eyi7852dncjCwVHtoOz4V8L3Qb0uu0Ehk/r/fNlTTUmxYmEpSanWLBtssUqQZMhBXaer4iVrEww+dn8J
ptax+nh2JteuV+p+zyR8oiF5XJBueplukF6UF8SU1Vh03AIfIw/LsZo8Gb1JBLHlZKzUBvdkOl5pZS7rznQexBMVobQtdb8iFfVhkVaxvvaUNFR8qFC9M5GG
ek6iNE09Df1VhfVHU2B7vloiOmOOlpYWfEhuozG2XE7jMwOYTZsPtHHAUnQ9jKelm4UYMRsHcGlcA/a+mn0ge8gjRwxj7cfIrnE3mFExS+4zJEe5o7hC9NRW
KDqlICQO9xQfZUCjKQHgNijaRHQbLkd/+NcGGOPv36x3fV+n5fP7lgZGRqFh+hRbGW+s4hRiiBmH8UI3nW1t+VIxCKdsXOdqRQvvqHgvHvC3XCuHUUZcvxLk
u4zSJYPDCc6cHoTRL3K7O48ex36LH8DeGWUBsSThMBftXr5is7iT6BaErHFR2MWnTCbY4B6MhpQ8S0Coushsgo/AAWOS8Q83z66sJGoX+WJBBj9AL7k7pqZ/
8JEvu2e9uk51WKC/LO6FHgO0q+V4yqr+Jypu4n5IRXHpTZVgT7hx0ZoIn0a0KSjnoyanq84umpD24b8O+5gczmQVqC6FqwwtvHSZg5QpPWUJ+m1OFqqBhM97
m4D+CjkDkpOc+3xVl0Z5/lu7fk1ZiqlJKa1VOPoQYrw0EvB8Hg01IgT1EgF4YEt+KYO26OQSz82pWitcxcDgpDADUsIgtiYAE6kyb5BqxbE9LoH9xR1cTJBd
br1WQ0n+8Ox625A1EYzUMwfvlgjRJnOVAzoXP/ocjA1x/M721q2IJgnpPmDh/oKDau9NF+wUJCzkjUi0xQYuM5t+1rHxSGvvRj5zbvwEa+A0IgsdDiDTBDcW
zt4sJ0P2ozlxClrTxfUxHvprqxLfw+iqQMoHJrVvZD4BcxnLuUEStbZRL0p+2EK2JWMcBCmX67GA6TSc3dG6h7bXeV3UX4+Bmwr2yr7yk802MRWQlhVZBZFe
+PJE7N3Oj3tMM/zSS0Ee1Zca8T0935hEQKzkP7LL9aoJbf1QBqxPjiETnn7LqjWHClasvDork9kBGMvJzwaaTJL35FYICFKsXS7UUkYHqKJTA9ypVIbMrv7L
AiWCSCvT7MLn/JmWJreRFhtkOEd11hXW2TKGFnvZtGCOW+La8GdZgB2o6gMnkErFFcruFm2OTlICX2lxqMi7w1pWTh8Qtr/dLFI2rkb3PGyTHX9r+IuZMx2U
n5Bdz5tYH6BUAE8MrjhoS/i34oulw/ZywRunBLL1flTbQuYZNoNN1p/bI0l5aEgflrD/s75lzL8Mf7kFz/k3P6PRvCmUdWArpJHPa/ThXQVJoiLsm6WxWMBD
KpQGYfWCGlfgELFXXGt5RQ74wIjJCdvypFQ2uJH+Hd7VidigWI2x9f6nQvcy5rZc8kc/JXzBbuooNfqNnA+g7T9sNlRcz6TmDfvU+Bv7Syz3yGsoa3zF98Kh
+LMEh7Cie8drgVHSoZCxenCQV1aoxIb/zdZ8XlKHPkIFASKXjJOyM1wV/DTw4QzXfJcE9R6Mx+xSIPUhWss3rCDHn2Kf7NMiZWB5CMhSs/guKqtiOHvWsQ38
aIUYOQ4HCdCaS/ouUgUCL9G+pjBOjIAmUi2iXA+6wudknTQ1tTskWFfp7dVlKUJC+itRyNAaw0QM2EtD6cwMC4YMw+4df/Z3HgN67ZKHY6miuJbZ+6fRTtsF
5P2HTb32eBkk/Xior32mkbDshYApSgC/QZX9loI7xkZXOAC+UzCDJc4cQb7y8vlJqrEVabhy2F6jfWgxbIIrlDNqG9TY6m38lKxcEa/5E3ARrFq32VjjJHO9
SnifRY1Bs1jgXTZ7GUewim2Pa1lJJqwL5domZONGHCQFCqqdBqiH+bQ4LK8cKPMD+gu+saj/n8knC8kOHpUwCvDi7mIg7XAIfqNvVpGWpA1uxg28oLHjYAI9
0/olaO2xGgxZGwQNwQOgb5aFDY2BOUDuzjc0NNJbvi3Y3wdnjCtTnMv/bEpZ/3xx5lw49nMOoVNIKCYcMPmj86T2IVWmWHQZUEEfZGgb6zIyjIzVbo78uS7m
/01OlR2u3L259WtgK0c44CmDKg1t+b8iUbqvwDO6vy7MCcSEjMjgTR7DS0gQAU1wK3u+jMbxrN6GJlq1RXFHYjLn0HBTGMTxMIPfsFoVsodj6gKQmmOVRfn2
74aCwcmpP/EXWiN3QTievv7rFA0FZWW/95HrDupasNWuSKYtf3lux7GiW7/5gqjb8N4us4Iqe1SVr6v8EmmqvQVTPA/5eYRAbiEHwSowqt7+2TRQf1xBrMJZ
tNdth8Ndjl9KtxTVGCAsKPIkn4wTe29G/vIapsqYz4y423oHZQBTw9Spb33YKIGMpA316az0yIhowbeWcnaidrax+qJCbFO/YJb2P2Y8d4r0yLdyCZ8cio3Z
peJM1uYBYDZOVblu6lMQd1rtpjaDA32kTfJm8ODx1+ayE6AAkzNwfR+zMEWmHLXvssyinVclF+2cBEdB3WR3JcxXqtjNV1BrC27M/KcXBA3y0TYSN+fTVg7c
iWta5tJF9x8nKZKh+7dtxijjHcHeRR6kW2dR/5N9tCvpR1+Uv3/7s553sg6KHB74WBqrVEfA3RAfvykaFaKkNJ2xbC7NbUjofH0IYm2rC+6EY3x89NeS/SnI
nB9dWV+WmUDK7ADOQ3fvuId/5E9SSSmn84iBLfWhqOKbBeWUh1iZUUzVWSCflmFdPkmfkGwFlcOAGRUSAAlAmmAZSxTaLO3trggL3GH6bnzyN+xZr7ivmy32
GFSVUJXiS/3yhI5KdFqugChDTBvmdLmljYgUnD7KfHMz8vS13CuqRPd0+A2FZd1eBuNUpwO0b+RZ1pc2Fg3K6hFenPkkWnKqNK1nIVD03sj2SXxgCfbZSBcq
8+d+64CN4b1K2O6nXZbyjZMfTQEn0KuU7P618jrMRhfCnX1hKmWiPgi0L61DsWQ3vvNKd2zyCyDjR69dp7ESX4UXWT4Fm9ChzwpFlevsGIoWfaaPzrkXBTYp
YNvOmdi00+G/hBzbLCKGi1d9+3mZ4HyiEcNrX2cvg+szC76ZV8H40dZR0yzSHwxYn+IM/ctAlzHYmQEqnDWlY9nOQUODY6aXmqTJ5dufN+tSQybJhyodgzwl
tCl0ZvurFXJvZM8G88fusTJnxJxsG6ov5sdoz6BkAY0MGQ7LMh5t0RJnPGic9RztVC8NSeWAw9TFnGNg9nLHUnS9UGyDlZjCiFeQYmPr4+i74z31QQGeMNBI
GKeveodLGn+ZZ3zHClvSSZBtwpfFRYXaLRg5AjIr8tVQ3WgLck3+YjXPnHEkA92aGbvQpVD4RMKiYIHdKHEjV3oIrQqkcbpVNaQS8oca/GpAsrPBPO9Tbcdl
SwxPB16O/H59qrrdy2qNYpYXAKVf/wkjDNpLoR3jEW4Wc98QTSv2mRmFozvbHBxYY2NKKVuaOw2GYcuA6qNI6GRc1I289DTynclNDTIs/C+5FapvCRr42zaN
akt9z37ZzEmN/Bf+YkwCV21ryk8NUBwn4//DwupsLAdek2ZxJnpTew0K6ZV5LQxeipgbZsCnFRUa/u4OD+X3PGr2lIBjpm3mF2BwmGXFrqldb0owA3Cwt4nP
HZw3n83jrDmkyCHMPaoNhhAKPbn/pkzrAQTgKZwK7v1mtl7smgTjbseEL7ZBdzw7IXvJ5wfiUdWKQUpRc3kcTPGAnQKBSebU/ONR9XJbwiz7vseH3ZkKH883
h5H4jdqhGxop5j7/GrJbS2bJulFJdwfxOf1C8KSGnhbmxi7YpU2rp+ULA/1vuiY4fIKDcmxmqGeQ3G9sMbz1z6UXZURJUkd1dKbdUoRTRUwfm2UapeE+X5OO
HOZtGT5oP1j6ewVKO1ODCX+S+nKmfmjq756tXTrRIiOumqeV0EkKCu2CLPASKAc6CdNN4d4bKL5KXexYdDYTYQFxx1enBFiqi5zE71EZDtkOvIL/UHp4a7zm
1TkrTvPBc3oHywfL/vpy/5vFgilQOK5ixQ0L6srNuo0Gb+FN+cqn/dmTzCFeVvz1cn347U4gcJoQL7xfZBmt+g2skA1P3y8zoQw9CsqsFj62seIZxBIPMOqy
bdVzx1AOjkfiXUV8q2rhFwBn3U7HDsxXLVlv/ipp2zUzTl/dWOzm1Te52s65jj/FmGGedosHTa/wpfnXapHIgcqzcuZJ/lSTwBXOiw5AUCTiqMl4mMX7XWee
QV0LMNIEpRHpt6daQYua6vDkiICAoLiYwkGZG1Af2yS3gJZYQsnNuKIPwV1n5jAH/LmM/0K0CAvtNf2o/vlq3byT9m0GnkdnmiBjEP4kj5s7r2VjsibUNpUz
0p7oIkENBXnMqZDHRf+E0KMUb0Q5r8XCkclgCIaRX6i03XXcR++lDtn7sJowUn0KX+y3xvlkk2KoxKeSBQT1aB+9GdCgZhtYNBI8kX18INRANYgm5VJxQL1r
Fio5ij43yBMo6ogzdLD5N3Ig7dGwjt8jO+LXvG7Wn6hcFah10F3NrEsKE2x0hbdqXtdKmAn65NHTl92nEJ6Nqup09LRESMlc7AS6mq8rlp5NijZ4u1aIN057
CS5OcdKiqlVRkwpRUgm2v2MJRcak5GTsDsBb4pXWFLNkYymXc14qoM+ZSoeWpiSfTMrwYFqC6wrpY9uY2mmdA22XUec8aCF2AdFtqFsnTx+J48Qjap7f2cB5
HsuHRq1fAbOkt3fPHm0Q5YsuPcrEjm98hor+0AgEmbpntuErvSm6LQTvEZyIxYyl2loz9hsIvuHbFWtPjik8APFciNWuLN7y66kPihtombizfRiscIjJHwCx
laiP8SDeveHrqd4bi3s1ViRIdTsty44rZYR7x+a7EHgtnU8etVf/slns21IdrBkXkaJ5b6w0Zw+1QDcesYeWUAHU46zgmpKeNEtrS5gHg9sz/czw3Yb2Grsi
pYpdiVMDDWWLrECC3jG3UcDMje+JW0MFoNBeiVLcv7NgZhZRWI0IbkMugAnctauGYkJGmoMwQ7y3AsKEk1nRCVsC6V0TPBSoTOFKgYSyUfPaOlbGG/RTBPUj
DsUGVZiGC6zr5eJ1851LNAcMVLEKpaHKMrDy6s5CbCmENYIsLzcTVFm272aXxnzu0KbrXXrIX6hBbgdPSnIaODTZMZK/ps6zfCVs4FPY06vcaHfN50twIAFi
9JYhazL7rwfnUdLOJiLpozXHhSm4DRUZXVfg2xSiGlIRgvzRPgsFie+4DArFtqZyaydxNlup32ONw7DF2NcWdPRbcEKFgD0kygzGdnSZVWVYdkAYBTDFs/Ku
jrdH2AZszw8JjAOOUEvo6iq/+6TkhQi1lG+Z/Ixbuzvv/Apx29tZZ1QO/E4RExbdHjT7/4r1Lr6LV4ZsazNpldDu04zmhyibnmmXX932CusvKpa2tIwDnQG3
XM+OmKMF+Rn3KTwzEM0ZzLNfQlZS+QTQJPVDA10OApWLjd/peaNdpOojMjyaCIJ1sqOc7jHzJLNqCyxig6wdhsLjJA/a9FP0KnU1FandluKxvTegrXvPqasP
uS0LMhlOjJ6K5TPMoYxkSYBCxe5w+qo13ODoVTuRRA36h5IIMYCgp7XhKhuWE1WIynMHCQUY9JVoZqd3b8xCoKiSCghRwINM4MjvacCqCkHWFXyudq4PfEIC
5vOZRXINbVaRbYKdtDCUYua2xyXtSXEfNXe+621GghGzy2+hSsIHwKR6ZMrTXAnMYNMFXmCVtIftVyK8yEAFUZAsZm7tcFwjXg+PkEd3Q0hewFZG4t1UujMX
iekXMUWPOBb9Ng9walM3KL0vv+vuy9kMLHK4hIqbt6eVquQpWaXD7Gwnk9IRG4+r94tKGaP5N6LMQuzIuOboosILslxSuR3kmByKvM5TbW08PfnGeOt339Xr
4ZZbuib+aitWHokgXTvolr4WJyQY3hTFV+HQTrPz45+vix4/GTrhR5KXw9ILXg/X4Degmop+sB9XkRcpX2UTU1Xz53kasuANgAkzYmaDedgDmTXBF9zB7/g8
909For5FUlZ6zlEm0b70091iPNuIuHrF3GGajIRrywoIgGeqkaOq+FHVrjDwMzwHdAKN1PntSWQlGBey77zs7Uwy2YmnW6YlDbxBwqbRxqS6MUxiln1yyGKc
v3r22X4F56w5g7sP8rJBk34d8q0J1rxaHMAQkYttVpZjtqg4/BgoIstptyf5dam80fLqQRtzm3rTNJiQLiiE9TFjQzJ/3UbC+/B4fM6ViYR8Q6TQOqxs15WO
CPsRBOxlZ6kLtnvJQ3/qLtubF15lS/bNdC48dQpS7Rd2rEcldqLckxX0rIdTbCn0pesBW0/2w1NqQTCX7pI/Dhumx1NLNoJV48zVPWr9J95cRpItAYEYewas
febG4ZZB+NalVkj0M8LkXPaklc7Y24iG25//Mp+orQW2XKZYy38356B4wMTOejpW9pXWvXnhJib2aT7Klu0C8oB9Cam6dTMqbII0W5kMVzW/T5PiXaSPqT9O
36x34+RWZexeAs97zkXhgQ1VGuVarFO+2EJsk2ikjx1B0Xsfc+fAL0fT29s3r6DMQ8KMJNiBc8CVM/cCbj1qvNrWXTK/Yb/WmwFUVCMlQaPH2tSKnisE1wEi
XCo4eDclWrDsaioT1BeJ6mwbY+jUupKamM64Z33LJLfcw1LIPVEsavBsFYr/0cFpz7vq534OiG+1YyzNR6mWz/AhvuhIZnYJD1gxrXOvxcJE9Zl5MJEkf8o+
4wQm0mTkOKV+aw7jac9Wrh7q4LZy+iH9IbkVUi/YPbWCA4Sj5EnRejb20liUUyPXzzSv6fuBQvJhRGZDfjBXywA16hzwDolMlLR+e+SqG8XH+h/y4wpLzDZu
PkP4OUW/7DLUSxSNpleLCuL1xBNohxzuJfz9rnlH1boyPS8LzKFpUSfmWbxrVoF8gAalADYkCU2W4gLQ43Sd3Fauu+AY4i3c6+yIpCxzYC+NRcu+cgWhTWhq
ZdAvFgzxGz9pTxBw+Tkj+P9h8pe8EbwVenXxlQDLny6P7ABcPTn5LfmToGEapRhhscKrO8zoSQ7Zs1H/H0S11Utvlr9kdw1mdGexlzu5vNqSdyPqtrG+IHn9
fM8dQ07KBKuAy1VpsYKyh3o4wW/HOkgMgWEENp5qiPlRPp5DGA8eB3OjeBuByOvpwaX2SAbRDDzMgpixXmqFtaG6xyrmni5Hf6y93T11hgqEj//TU3NCaTV4
knWP9Sl8+m3fa4HYqcjSg9zLophK5tIfgCeIM+xUNGAapZo12bs0AbomGao/9K/kiMMPUF2biNvemyB3bUFECuSfyB5SUwp/zLUuz0hPZIG2q2ceZTN0XM/l
suLZOAzlxMetbS/MTUWvDHYqRrrgs3xS6uUE7Kb0yVdu4BHlvp/ybw4uiZMHsuzebq7rVmVRsflLV13U+se8qUIODqAFw/IumsjnmR+xq1nejL+8ksplivdA
j3U0ZTJMtDY9xc9AwNEfCfG2Q/EJaml4ShJMliSPltT2Rb8DsA/d8y8tDjRUGEYKNcr7qziuMQUD3au89vCyU55lY133z203vubsqwanH7yxLl0YdRIfKIF+
lx+eqXtIpkrGnsFQSFhcOT1Gp9eEie8B2EymVjbCststZ9tQaR6G41o9SV418RrOXo8OTExn7qMXq6p3fTZkghmyjPCNqfbwyrycMDylVlM/i1SYltDdzeU0
GYRbKPggmRalYtohwMKBlcvCh5MX98Y2jua0+E6WzGstxhWbOi5TooNoJ6ePBc/4x7tNMuBabTpm/+ib7hQSxGllJiKl0eVvfZ+cBe9NM195blNTSh+o753E
kRJ2dlbeo9PxPNH0JQt4veloIqIF+/MeNeIQeGJQfQSTBBGcZBRxjo4d/ljzywnGKLboCktP2NWBk8fb45O43Xp5Nw+AB9pnFwDkQke3B2UX1jPxomktEINE
jWRyGF4ZClYHU/K8pXwIFce9WOnl0EUJostzEza0Dga9q5kWgsNZ6TpuEBsFmNpwFpDU9IMaJgN49fRcRp6GXyXMWUmEe9CcpVrlHTjqRDvafpmmiQDro/+Z
dvsqIXiWmK+ZZJRe21MnhajC9Dfz9SCdII/s0PSdCic4MSH6Y8hMu3slc991iyD1+uHUFYmecsMLeJBEypvgSsgBG3E8a0MaN6qgrgOpvqqFrjWfm2WO8A4Q
LWY6vyJa4eR6UcxKitvg57eidkcafpoARX/N1uplLQjySSZPEoLTbMubOuUFODa+eUYmZDUrenpNoyFpGpNQ3kD7m9z1vWjA2zIXVhR9Dze6DuAux4YEwLSr
3wIY/5PpVPK3r/vYIjlC5ju8x1MnvQcfgKXRolgu+CQmwHs7KwquDgqVFlaVwvEjDc72Xbxowdpqo2Zmdb7grV8zgfqyjKBmqtY4KcBodErA76HYFCZ8FZfB
ktx9Ck8miEAs6XfzJTfb39BvKTluoZyGf1P9tzACeP7Ckf0cMmVmSkWbXXin8dP5jpt4Hg7+sFnggv4mgxWPHEc8OBh7tTrssqfFKAzMgUTgyzeaXCohmqvE
NWscUPwjerWZsZnpNfclibVSq+yDybKimMbOd8KlbVu2JT7qFiBYWN08iHALJc7atSaQ7OxqTFRcIavb5h00Cf2ZvxnIi5u5T/gPpppC+4vjORjWBTV+r1+t
4SVPvrIyTSHv35bt0ebOB1tPqC9jPceYwVrHyseMFjSOU/z4Cag/9eFMl7uv6maHAn4D0TYrpLKgKeP2J1yb7AaOBAHBCep9Bx1SLYdfnwsrX4n1EVFHULy7
oRN2YkLcUQcYWuyHXUc0GVvqMWWUgTpyYzAs5bkme4tD+w4K8fwj6YfvD+4EMc3M1wWMiRUO6+E+nl1W46BR2akwkoyXxQBAs6yEHLIFXRuC7ZJEKIb3Xqyi
Si6lh0jY27nrwYJ3Yfu+aWx4pu82l3lYlRAp3f8c3VzJ3iLpPOILi+7inUIfRDC0LzlVVRKkL6FSiIYW6R08hGxmk2HF2gf1uVulKPjZXrMwjFDttsUTs0g2
StBITqc7JPDMEBczltQUDHRVtx5NFYQ9Nd/hO/g2tKLeaR2FZPZjj+EqbwC8EhBEaS/HLLlizf6QeY+W6de6OefTnuzH0AxEiT+4dXLVkdRdqIOSCJu4jICg
LY4Ef8SQHcubVUnLX3t9CMTvV//wNuFjyt/yQ3GtKB2QchFMifMt3HDoaPjmSd7Hk+CyuTYpyxG+Rt7X6zzX6BRxawzLwQgyaKOfU3O/l4V5YnynhQUsbyoW
jPTsyt7ojR53740Mual+mGNjS1fIAer3F3gEIhnF/gPlzIrdZferLENGHrMuMaOOoKNnCpMzjvC1ZI0+o9Jhg10eedXIa/TX1iCNzYLjMQ0Bp1LO3aSlDRAR
D3v1hGtVDlFeP0iyUen2gEN9/QabtNaSsBI+84zxkSwZRGwALCEjx2k8aJA16ap9hAiQtLxqVLKCryKV0AMZnp7j2WbQbJX1MlUV3+c6espbOKBK73l9DchR
LH+AAEu/6ye5k9U4VPOVqwjBU1+a6JlN8uCO2cF0u89OlTVUcQshUmVgXbHdexJswWm6uvNUu3NEZTOkkh0MwBufpLiZHln55O3DADY0tG2t+OCOr7QGjTFz
QtLUCIFsLbAaTwOtDUbaQn2htK3XP1QGWcKAUEjySP34eixaZFc/w0ccAY0vikE8wu4ZUnzm/otSsXXvYwCU1VfFSmyrAuM2rjw+SLgwk2QJqKJLBw+mIpW4
bq/bA9aqg8viD2MxVpFLvBbN07Ulx8+GeDNkDf+D2wYMAb2tsQ9zLc8QL44ZQYqigSVc+3KS7lFo/zgs4GoD/mkevktlFRjSzIZW7Wc63cBOwMYhMjOtDl4F
MCyTPaEj18IcApfmvVrlYc4VQajg1I1Z6oYofFJ3v9pqGMbGiS6rhzZbzmf/xnEc8lkXQ5CtBBK7JIpss0dzBv2RCkevqcK/WDsDp/7jnCLHNfMKy7ZnOzP4
NUWxx0KtAzTTjNqG0IS3BMsBEhHGgLaPz0VXn77c3JDqIeLO6KLOOcKOc5WSjmoPj0VxIiGOWyXCPZsFI3n1OfHH1CaIkLpxR+Sb7JCRuc0FbuyJZXXuZaZJ
RQXJMq6p1LzKhB6QInvqRWLzYpW/W5vXti/jqYescRKWe/YIe55l2B1qBscW6jo9NnUgNxpYG/yp1lSmEb5wVlq1PY1sQPAHdJ0LwwX49bbjKNNAclwWDsuX
5cjWzytadJnO/bLiYLSxToaJSSK4Q7gpgXhvLl12BbQ2w2hZTAspU0xKp0wL8Gt665Qo/7cUXpUa4mopQFHi3vvYDlMqUOR8rCoGHzEwziyn+zBRJgtsQ+UB
kcRYCH+8duG0obJyIj1RHM5pOkM/vCPfrSZ+bhkBMd22MFza/DivIpudkAv6yzPcCv9v7pVr/vJI9oO28SwSvAa86vyBAVAXOhmsixHRxf9FmB69aROPpKGk
JuyL2as3IwtgPxkfhsxVr77EQPFBFA72v1OF/o1feiIBXZ6kXYn/Ru60ipIdmweNp6Af3VroGod6O2Cxl5YYjLjkFg3FrdJYbFmh4Vn4D9WVz8Oj03lD5Q3A
kmNMOtGwHhRD6/ld4NyhKyzvnXOZMy3Kz4dAtYbsRNckr3H2frOyR59Vl5b7n3wwLse6+bq7iFVQ0hAJEpS8N2VkZNE13KugDbRyZxn7n97CShTTleAx+Gjt
LsCZIA4VrdLMF9qfNkZxTH7ABModlgD+U+vzKHLGo3HvzT1YRefrsxXSMHtPd3xTM/osxDRLLSg7EKsEqSucWkNuK2stJn7CBTMXEXrUPdhT3Ll8a3qtMv/2
B4EbXhUjm83b1s6GF8ppf5eDLLZ8m8cD0tJbW12NIAlbNElRM6AWZKeEWcQZaEm1l3smsIfL3n2yqEK3tPm2bOBbZ1wMFwlBTvYEGUZNp4jWO9FYRjjaYybD
t3yUu9gCphCrEP7/IHAe/PQT9ctNgfUhjUzPkp5CGZ6Gwv5V1Sfi2INKTFffIi9rse7d1EoxYLn1SKDN/w17xv7KQKx2x1ftuEDTPOdrWXn7RmBhpuHBhDGR
EExmIfG0A4p8IK+cJFwE48RcW9GSdM2ZGwWS0zYNINMAzNTudqDCl/hXVANRgwZydtXwDIQUaUwoSpc9tvMIqPrQqDr7pXH5kOCeikY6EAR6XdR36WtFXPW6
yonHssr39R1i4HU2ryod1WQcOUxLBTbNY5kGpPYt/RcPCGfpQ3gM7D7kFApjh/VVSalKXhMsb58r5U9u+YtsM4BNR9T7XJgtyl5Avuk4zQzdDBER5NtAj4Rn
nBmF48c19X5AnZCaJX/qpktJWMZHu9eCMbhTrAWAcGE4b8ol1UXu6KgiqHLC5U8RF4uOtnWke5SFlYgWtFYtg6g5/efgJRXKxXhn5p5bZCFPzVBtBnu4amMb
TGfh1S6HY9Hgpb04Vd3+P9d3Bk7RT4N6LU4+HBXSHPcMqLAEpeDbnUaVesKQg7dJP4ZUu7FfXFW/xD/S8rzPy0+vPbdXPz49/QuBq6DEa/kzdeQYVnmzEJdD
JGkZ05By96nImtsdATFnbPpfIFtJER/HbuLvZh1aUAijz4K38WsLirtCrhrFY3eYx4xERpoqIzBcq48gcL/AglJUh2qCiOdNnyHzItW6JnNsNtUfCmtucefK
75Ebc1BQl4EYmSaqGOC3S3/A0tAJ0v6AS7NgeE50GAzUyFD3gTmvNJjuScpaUP3RfMjwAlZysiquRTCOVz3zw8LJ9dPpcdnU9pIl3u3LT3SReMNNK+FVJriP
vxtNUN1V8BTFDWjdoAeK8SFmUnaPqVzrPfO+ZjlFMa7CH7bDkm4pOumEdh5UIDB1+v5TJ4HH05LQQ7cCwq7HicMGr2tzm6WU/FX90FPvLv+K7MuDe2N4tMaA
lyqS4jFr8Ld0J6qYIOqrz/NoQYoTtENtV7nBFzjk8OYlg33Hw0asnV5L2BjcGM862cPUolEtL5B+EQRXOJMVaE/b2mHBcfHO07aW8Ff/lRvmb2hqPjxr1D1t
E1z4+EYMn9yuSS1cUdGCwTmEmW9cRD8tHBIOi9MKaUQH855ZHYMV2YXiCL3lqlR38Nw++WbBzlaKlnwqbkrjrgotrHwrZisDnuvJojRznIoH4qvGarHJxcck
zBQ8zXf2lbW437mDcThVPVexP+NlAUDPjIxMxs0BPyd4eKCO3G6W0a0AJhpTBdRt+QrMrLaN08t23YjZj0Xg0PpyTZkl7+rJMQYE7UiClz2UOf1NEeR8lGLX
1TmmD1JPolqypm2A17ifZl6xnxj9WqjsDCZU0k7P590yi59gHwjNXqsXKhvZPfysI4ioSNAqxPrYvPMNGAVnLCdEAh6VnHdUZ9BVJB+YDsutl4IMf8OZmw5X
QfHk4AgIUh8HjInUcMYdwbycbHT4be1dVPk0BiB15i7qYzT2kl8R4niFfkPqDeWQ6RpnMuq4/hnsg10CaEaeQANaoWIcO+o9rV5CeaEs6SeCKLP02LfeYC5w
aYiYsw9U5jw2J+xRzqB0tznFlbA7S03FV5MdpCB5MMRqp1J0P+zhkFQDb9s6/ggWt+D5pEzypnt0DWi/dGWBdvE9rHzV68qqPGZL4aBrB2pRuQxLsuH9VKCp
kS1N5VMC/nO5YGvru1pxEDUEI1IXpyLHCENVvD2X9WGjpZ8C3PPSDF96wx6grqc3fwffE6t5PJka5I44oblC8e/VDAPQ0CAh35kH9C0V+AH0bf9dx0m5wQy8
lmpxiwX35HAebDYJEM7Mvz9A/nnnk3ejh0C6RlFE6dmjhVYZn8GOirTK8wGIF0JdagLBrkJuh3rWPhG9fb67Y4g7BJPhJjhxWxKg8xRSntXmjc3tWvr1xbuz
X4JJsfS/kj4lqDUBHoofw+hAbPl4+aQ9c9CecQyB1PcGyfsm2JDYd1EO6BA4TqAvL9tJoWaWYedJFoaThm8ouAYKh/XfMyYNBSRfdj84dbwjJ8IyfBcDWEWI
6Q9P3rL4BSD6WIGKk9+w68XMSEyi8Ly9HYO3lHofR3udfu9IEDt1iTkJcojlUMWx0URp/E43r321pkaGZkcCcetRq3o//Neo6wkjgWkULsn1/YARvHITvX3y
h43Hdorj2EbioKAe8L00L6ev7qExjyYExjUOGsMBGBcg7Diz9qwTqmTWy/KTHLHYcVPTKHAgGo9MCuWGhXeLqyWquKDCCnkfFumyLchJI3zzgE9HjWHJXNUS
yV0Mzn79J4lv4Mpl0iSTmnoqurc0MbVadZwu9RkXt5AhCsrbpQOV0SpfwWS/HEuOisnBrib5KrmdF/03jYRBzTnto+QgwCUmzRC59pU21JXt+kc0leezsqIr
AL6uv6Hf8iuCUPn0cwdHc3AC9hJMmwJtE/Ib4Gqai1hYnAKlCJast/XVv+Sucp9MT1JKpRMA3t1+AjTWbNg4Y72dQsqHUwlMjUdzk37VBdkT5LACXKNrx8Hj
QG2p0Jbu58TxSpRz8SjkK5Av4d1OHIobp4FimW26XOSiTZIjZ6Kcfiz8aPsrAa14/hqweum1c/uaeCuW9UhCYRskXRaYobV9i85bQH8IU+IUgTx3R3Ux86sG
TqnEe73vB/ynO96qrCkrCsWOQlWfX/eqDYevHaqpJkhHZtFabNkcyaxt7N5PQFOi04JJx4E4np7ASz0GeP/H5kugamEg2aCdCwRke7Ro5WFTsAgbTowCOmPh
da9OyDnSoBs9gNVnAbWdY2CuVx6wQrD5LDpJ0G2baGIcE4kXIOM99snP6Hpk74rFtj+XqJXD7/Q45Fo2wftBCPoUt5S8gP3chRIoVNWJcFYmcX8JAe0cQRbZ
al25IyCa+bK67LR8UK8mkgZx6TxtXJXPEI4h8Yffu6vmmveo6xlOCw6byiAI89RghH85jIv4QqtSdAAWZz1Je/BkJuwtp9rEML8yIkd11cTTFJfBb67cIMaf
gAmFzWOSHfSd09T75rs66itgv2ttytJVDdK8Ie3fmcmvnIxrWmUJSQH/VUxnbKKu2ZRo8yquVxG3zVym/yX6Cj1QUDCJR+vTi3TRBrzQ1/kQjw1ntSwcO/S2
V1VClMBP9mC9Y+NfGwsXGMO+E6mghxNKI8J0ELy/Jgg5HlcV11XAQ09etN7vCWgMoU3NUY3GnGrOdEa9+Q1XxjNS+g/vSA3z+T0Xb9xgKsKDpOBmwMY+X4xV
HTk5q8iC6r6/aKZ1lc7/p9P4FQaxVQzWIGHT9funFg6YBjoK0oafh61KFRCJJKVNWTtgNHcLJf8BwoskQXVkT+1ECxHgevvG3YtJs0AgJGuPYHqhlRWC7mqs
oXuJ2CvLAARNw34cT391nK12Aq5fKahGnLxE9iE4qlOlemIoqbdfulfzs5NtnDffD4WMsU3MShYnlmFZUp1urjpHXkleUCnzkaGR1pA92N5R5eH3BGyjEMLU
qgNBbC+XdW4Ul5r5zm7AOeEKKuYKcMJ18EL0Aqq5n0wtgIreDn4ooA8wrc281/tpBVxiQPlUV8DW/naXuGwNX/j60jOhwxUfx1YNpRTFYxGN2xM4k4BECGSU
m033ZwqcnzA82+hBc13zBfvZ0uuBpHRacX6ikMNIJ67DTU78+4zGPz3CtFvFg2OULE/Pc8oQfMtHrkCEoZdhJ1RVI0gzgFy2wnazOx37/uMEtjxQ3QZxJLVp
FtQMleuMgLlbu2EYnogHcu5UrPnOvw0GYCNkZTqM72swvkrE0WJxqUd6B9w+4epV51lVL7rEKk9aBL7ITLzk+savKgUT1x3dFGG6T8wpxdSkBzhi7Xhz6d8M
R/+SkxIR72pd/v447xh+PswVu+IXxfFNJBaz8wqtvoh6HkvUv4rj2VR9szqwUEwOuHmkhK+VL+GXI3shQCsL4S4nx0QcdbuU9VlBzbqAcDVD9bcdUUwtQTx/
0eOevqgTHTxBqVeuAvn11UcNOezLIRSep1aYw6rydNfxrhd44eIbby0Y6qLJ3p8EQiQ42YTHKEgpT/kHQQ0bX/dRuVV3CaAOokH+tled5iOj7SXkXSvapC3j
675axfgR/3F6RZIs1h/IPcdxbTJQn7cJ0EXjtgnpX51wWFD7+dZHZ+yq9D5dxSfd4aa7TVuXQb5Q4DekzU3UBltqafhaPFCow5BcQEpokksqKEsgZLmvUT9X
PolBV80KJK2b9nr1Eb5my//cgIa+oZiCdp0HBtOzkzAE98vUgA48I97ZVZ/qPP8gRIqFgUR24ypIvOLuSnDhjdaUoCZYS0tMPOKs8v+DfMFkxEw+BzHp57dz
Bb6vJMFqwcEg8H4aUwkPocX28VE+MJPqzls0P9rFwqbSDkL6Bo15HwG4HVCgXyHxD/PVCYxa40IWrgvvO6NUWDRLP7SWH4WvI2Y+bzfm7FFYEuPkq4mg5n+x
B3kNMIwbhiEBSoKmYkRyc6D7fHFv0ZRWtaxXdaWjumjmE7NvKlhNhQW5EZWkqkTBZYrgElo7j2qArql6In5H3gKUHB//rACPamCLQfarDnrabvu95UlPGQay
H0Atrk21j7pk1wtbcxcfTMcQNQRn2oFX49MPnze0XOEyjc6t16GVgcR+rZIIHLWZ8rk3NCWoCtQ/MmORh7j/34D90HJbixWaSKLv7iBbru7dgn1cGAqgh+A2
igTf2PnbL9nuHnrN1Nl8XGOhElVDRh9ld5/0dZRhlRTpLHTBrPYPw77mrkMakukXhe+oV4v/c/15xkRiXhvAuFIBxMtAJiFqD/A1abulXEoqvr6xuLFxiyBT
uoNA87oV7cdtrGLe4hYOEOD4M6gZrDMJim1D7DTJnF3hLcKfyia9XKuVmJUQtuGedKTXxoYWWrTlGweIwZEqU733P+7bXIpWMXjIXoiKE6AyTYyiXrT3rKgF
XBPCtHQiFlI2we4w5UnBy2Q6Or9QYsCqQ6WcHVs08/J+vAWsnStsIqN82hiABeRMx0HFvnmq6F4yX46fXQ7ylCpiKKsHgxp5/zv+a1ppJ+PaILIWK5cBI0hk
HtR1hCUATepKN53NtEnRnLYfzd30I+8VkX4plJsKRwPtIgHgUHgKleNPk+PY1kKYOAmU3LjihzBIYg2JTqj6QufZuuaYRbefKiJuM0RXqaxgLQUrbgtJsvkB
zmOosMmTQyo3Q2wKYzFcqNKxzVl2ZBjWOOifql4YmSLqC6eCepvNkfx1h2W/k+sDwgFG480DsPX2rIwGxVRaiY8GHoa2/zx2nTxewv45TC1e74+gxvVoiEbG
vbvUrmwhRQxc2q1Y6KVJoC4cMNK/xgpjCl5uXnckogVnQ9aYI/N4o8gz7Nu8HFsbTS8ckYPFuXSbSpMigGB21YeGwJuOitdz5lKRGL51piTo5GxAuB6VGvmM
MHGU7yfmtrSFCALmc2bdAzimt5rd/p/hegN926bh+qKmkdRrUzzU1p6bYn7+TElKwfiymqg5UAGx99ZJhlSpmcQ4aUUy7Kd9yxIOPKvSqLUDNnYXKX26iNoa
p19VG38NvuFp8lsqU1Uq7+A1fGaBXbMptxZP/F7AAfIdo5WyFDsY8dICVxyjJt5IYrMAAAAAu6TbDgE3J3YAAfVktv8BABCZInWxxGf7AgAAAAAEWVo=
"""
def checked(b,n,h):
 assert len(b)==n and hashlib.sha256(b).hexdigest()==h
 return b

def main():
 out=Path(sys.argv[1]).resolve()
 enc=''.join(DATA.split()).encode('ascii')
 checked(enc,17276,'be0ab5a6d258a34aca4c37a0d3bb79111de73ba3ed5f3fc0b3e21d4159dee55a')
 z=checked(base64.b64decode(enc,validate=True),12956,'f4f5284fb2db87c8eda8d07efe3402feaea30f32d5d9d1a7e9446205aa5e50b6')
 raw=checked(lzma.decompress(z),32694,'7286890bb97d71d9adaa7b05276d492f4bd89eed991c8aebaa75d5f622c6e6bc')
 files=json.loads(raw);assert len(files)==10
 out.mkdir(parents=True,exist_ok=False)
 for name,text in files.items():
  p=Path(name);assert not p.is_absolute()and '..'not in p.parts
  q=out/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(text.encode('utf-8'))
 for name,r in json.loads(files['MANIFEST.json']).items():
  checked((out/name).read_bytes(),r['bytes'],r['sha256'])
 print('BW35_STANDALONE_10_SOURCE_FILES_HASHES_PASS',flush=True)
 subprocess.run([sys.executable,'-B','-S',str(out/'REPLAY_CORE.py'),str(out/'proof')],check=True)
if __name__=='__main__':main()
```

Supplementary active-runtime copies: standalone decoder (`BW35_RECOVER.py`), source and exact certificates (`BW35_C260_CORE_CAPSULE.zip`), and complete Markdown handoff (`BW35_RESULT.md`). None is required in addition to the inline recovery program.
