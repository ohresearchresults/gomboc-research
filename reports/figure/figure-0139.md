# figure-0139

AI research report · 2026-08-28 UTC

---

# Steady Willow 49 — bounded trace-one SPD core continuation

## Literal disposition

**No strict own-centroid `(S,U,H)=(1,1,0)` metric was found, and no exact cover of the entire five-dimensional compact core was completed.** Global fixed-lattice nonexistence therefore remains unproved.

The result is nevertheless a machine-checkable, materially smaller frontier of the permitted partial kind. Two developments change the durable state:

1. The supposedly lost Sharp Quartz 52 result was recovered as an immutable artifact and independently rerun. It supplies a substantial exact atlas that was absent from the journal because the saved-conversation lifecycle had failed.
2. Beyond that recovered atlas, a new positive-volume dyadic box was isolated **inside its previously unresolved remainder**. The box is outside every earlier obstruction cell and has a complete strict all-wall class `(2,2,2)`. Thus the earlier remainder is now rigorously known to be nonempty, and this explicit open chamber is removed from it.

No sampling result is used as a certificate.

## Exact body and compact metric core

The fixed generator is

```text
q_i = Qint_i / 2^48,  i=0,...,4323.
```

The unique Santaló point is isolated in

```text
a_* in a_c + [-2^-90,2^-90]^3,
a_c = 2^-120 *
  (-39878490350125864373364388380978345,
    88581653811863381217051,
    819441514472273259270856).
```

For

```text
P_* = (conv{q_i}-a_*)^circ,
```

the uniform-volume centroid is exactly zero. Every invertible linear image remains exactly own-centred and preserves the actual lattice

```text
(H,V,E)=(4324,8644,12966).
```

Modulo rotation and positive scale, the inverse metric is normalized as

```text
K = [[k00,k01,k02],
     [k01,k11,k12],
     [k02,k12,1-k00-k11]] in SPD(3).
```

With ordered eigenvalues `lambda1>=lambda2>=lambda3>0`, the original unresolved compact core was

```text
trace(K)=1,
17179/16384 < lambda1/lambda3 < 2048/19,
lambda2/lambda1 > 1/32,
lambda3/lambda2 > 19/64,
lambda3 > 19/4115,
```

minus the parent 23-ball tube. Its boundedness is exact: multiplying the two ratio inequalities gives `lambda1/lambda3<2048/19`; trace one and `lambda2<=lambda1` imply `lambda3>19/4115`; positive semidefiniteness then places it inside

```text
k00,k11 in [19/4115,4077/4115],
k01,k02,k12 in [-2029/4115,2029/4115].
```

## Complete mechanical wall system

All fixed-lattice changes are represented by the exact directed walls

```text
S_ij(K) = (q_i-a_*)^T K(q_i-q_j),
W_fg(K) = d_g y_f^T adj(K)y_f - d_f y_f^T adj(K)y_g,
d_f = 1-a_*^T y_f.
```

The manifest contains

```text
25,932 directed face walls,
25,932 directed vertex walls,
12,966 actual true-edge cones.
```

A true edge with incident faces `(i,j)` and endpoints `(f,g)` is counted as a saddle only when all four actual components are strict:

```text
S_ij>0, S_ji>0, W_fg>0, W_gf>0.
```

No inference from feature representatives is used.

## Recovered Sharp Quartz 52 atlas

The recovered artifact was clean-rerun rather than trusted from stored labels. It contributes:

```text
direction-dependent stable leaves       9,024
direction-dependent unstable leaves     5,667
full-dimensional relative cells           256
  cells proving S>=2                        202
  cells proving U>=2                         54
directed boundary interval checks       102,742
minimum certified F lower       5.164757964010506e-8
strictly novel old-core boxes                141
```

The 141 boxes are pairwise disjoint and have exact total five-coordinate volume

```text
90202408465 / 576460752303423488.
```

For an exact centre `C` and rational `kappa>1`, a relative cell is

```text
B(C,kappa) = {trace-one K in SPD:
              exists mu>0 with mu C <= K <= kappa mu C}.
```

Every such cell stores two disjoint sink subsets and their complete outward boundaries. Positivity throughout the cell is certified by

```text
F=(1+kappa)c+(1-kappa)sqrt(pq)>0,
c=b^T C d, p=b^T C b, q=d^T C d,
```

with the dual `C^-1` construction for unstable subsets.

The direction-dependent thresholds strictly enlarge the original uniform collars and range over

```text
stable lambda2/lambda1:
  8796195645847/2^48 ... 25231810920545/2^48
unstable lambda3/lambda2:
  83563900502113/2^48 ... 103293901684931/2^48.
```

The recovered atlas left an exact remainder consisting of the old compact core outside the parent tube, above every applicable directional threshold, and outside all 256 new relative-condition cells.

## New exact open chamber in that remainder

A deterministic search located a candidate, after which every claim was exactified. The accepted inverse-metric centre has the literal form

```text
K_c = 2^-52 N,
trace(K_c)=1,
```

where all nine integers of `N` are recorded in `remainder_open_222_chamber.json`. In the independent coordinate order

```text
(K00,K11,K01,K02,K12),  K22=1-K00-K11,
```

the certificate provides a closed dyadic box

```text
|Delta K_j| <= 2^-r
```

with the exact integer `r`, exact coordinate volume `(2^(1-r))^5`, rational operator-norm perturbation bound, centre eigenvalue isolating intervals, and whole-box Weyl enclosures stored literally in the ledger. Its interior is an open full-dimensional trace-one SPD box.

The spectral enclosure proves throughout the box:

- strict SPD positivity and every old compact-core inequality;
- `lambda2/lambda1` above the global maximum of all 9,024 stable directional thresholds;
- `lambda3/lambda2` above the global maximum of all 5,667 unstable directional thresholds.

Consequently no projective eigendirection-boundary ambiguity is involved.

For each of the `23+256=279` earlier relative-condition balls, the ledger stores two integer generalized-Rayleigh witnesses. Exact interval arithmetic proves throughout the new box

```text
(h^T K h)(l^T C l)
  - kappa (l^T K l)(h^T C h) > 0.
```

Therefore the generalized condition of `K` relative to every old centre exceeds that ball's `kappa`. The entire box lies in the previously unresolved remainder.

## Exhaustive full-cone audit

The clean verifier reconstructs all 8,644 exact baseline polar vertices from their actual support triples, propagates both the full Santaló box and the full metric box, and evaluates every directed face and vertex wall by rational interval arithmetic. There are zero sign straddles.

It then rebuilds all actual maximal-face, vertex and four-component true-edge cones. The result throughout the open box is

```text
(S,U,H)=(2,2,2).
```

The exact stable-row indices, unstable-vertex indices, saddle-edge indices, minimum absolute wall separation, four decision-nearest wall indices, and their literal rational intervals are stored in `remainder_open_222_chamber.json`. The complete 51,864-entry directed-wall sign vector is independently regenerated and checked against its recorded SHA-256.

Thus this is a newly certified nonwinner chamber, not an unclassified sample. Since it lies inside the former remainder, that remainder is proved to contain positive five-dimensional volume; after adding the chamber, the new unresolved set is strictly smaller.

## Structural obstruction exposed

The open hole explains why the present 256-cell basis did not close the core. Relative-condition cells certify survival of two disjoint sink subsets under one multiplicative Löwner-radius model. Their radius terminates at the first SCC merger of the uncertain-edge graph. A strict all-sign `(2,2,2)` chamber can occupy an interstitial region between those balls even though its two stable and two unstable equilibria remain robust in an ordinary coordinate box.

A complete continuation therefore cannot rely on adding sample-derived relative balls alone. It must alternate three exact cell types:

1. first-SCC-merger relative-condition cells where a two-subset certificate has useful radius;
2. complete all-wall coordinate boxes for interstitial chambers such as the one isolated here;
3. wall-aligned subdivision at the first exact `S_ij=0` or `W_fg=0` straddle.

The four decision-nearest walls stored in the new ledger form the sharp next finite branch. Each child should first attempt an SCC cell, then a complete all-sign box, and otherwise split on its first exact wall. Any apparent `(1,1,0)` child must immediately undergo the complete 51,864-wall and 12,966-edge-cone audit.

## H/V reconstruction and watertight mesh

For any exact metric in the box choose the symmetric positive map `A=K^(-1/2)`. The transformed exact object is determined by

```text
h_i^A = A^-T(q_i-a_*),
v_f^A = A y_f/(1-a_*^T y_f),
```

with unchanged incidence.

The bundle includes deterministic midpoint H/V tables and matching OBJ/STL exports. Their verified mesh data are

```text
vertices                 8,644
boundary triangles      17,284
triangulated edges       25,926
triangle-edge incidence       2
true polyhedral edges    12,966.
```

The OBJ/STL coordinates use the exact dyadic metric centre and Santaló-box midpoint for decimal export; the exact object is the metric/root-box certificate plus the unchanged incidence ledger.

## Verification

After extracting the bundle, run

```bash
python verify_all.py
```

The command verifies the recovered Sharp Quartz 52 parent atlas, independently reconstructs the new spectral and ball-nonmembership certificates, evaluates every actual wall and full edge cone, and checks the midpoint OBJ/STL. The expected final line is

```text
PASS
```

## Artifacts

- Complete Markdown handoff (`RESULT.md`)
- Exact new chamber ledger (`remainder_open_222_chamber.json`)
- Independent exact verifier (`verify_remainder_exact.py`)
- Complete self-contained bundle (`Steady_Willow_49_core_extension.zip`)
- Bundle SHA-256 (`Steady_Willow_49_core_extension.zip.sha256`)
- Watertight OBJ (`metric_midpoint.obj`)
- Watertight STL (`metric_midpoint.stl`)

## Most useful continuation

The primary objective remains open: neither a homogeneous polyhedral Gömböc nor a complete impossibility cover has been certified. The exact frontier is now

```text
R_SW49 = R_SQ52 minus the newly certified dyadic (2,2,2) box.
```

The new chamber, its 279 nonmembership witness pairs and its complete wall-sign vector should be mandatory regression tests for every successor atlas. Branch first at its recorded nearest face and vertex walls; do not restart from an undelimited global sample cloud.
