# VQ20_RL07_C626_Z87_127_G1E9

This package defines a new homogeneous convex polyhedron by `candidate/GENERATOR.json` and exact translation to its own filled-volume centroid. It has V178/E313/F137, C626, strict(S,U,H)=(1,1,0), additional weak=(0,0,0). The unique stable input is3; the unique unstable raw001 is lex96 with degree44.

## Exact definition

The generator has181 mixed coordinate nodes on grid10^9:137 support vectors and44 designated nonsimple physical vertices. Node137 is fixed exactly001. At every `(i,deps,axes)` plan step, solve `Y_i dot Y_j=1` for the listed coordinates of node i, retaining its other literal rational controls. The bipartite contact equations, reconstruction order and free coordinates are finite data in the generator. The first137 vectors q_i define `P_raw={x:q_i dot x<=1}`. They are converted to primitive integer halfspaces by `parent/RECONSTRUCT.py`.

Reconstruct the maximal facets of P_raw and outward boundary triangles `(a,b,c)`. Define exact finite sums `V=sum det(a,b,c)/6`, `M=sum det(a,b,c)(a+b+c)/24`, `g=M/V`. The final body is `P=P_raw-g`, density1. Thus its three first moments and centroid are exactly zero. These sums, not a floating centre, define the large volume/moment fractions generated independently in A.json and B.json.

## Incidence

The parent is literal RL07_GRID7_Z18_94_C628_G1E9, not the older C628 own121 objects. Its four-contact {16,18,71,94} is preserved. Parent physical owner triples {87,108,127} and {87,122,127} are replaced by {87,108,122,127}. Parent maximal polar edge242=(87,127) is the new zero stress. All137 inequalities remain active. The new contact plan replaces the old free127 step with `[180,[87,108,122],[0,1,2]]`, `[127,[180],[2]]`; all previous contact groups remain.

## Commands

Run with Python3 and assertions enabled, never -O:

```
python -B -S REPLAY.py --out fresh-proof
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B DISCOVER.py --proof fresh-proof --out checkpoint-replay
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B DISCOVER.py --proof fresh-proof --out correction-replay --refine
python -B -S PREPARE_NEXT.py --out next-chart
```

The first command is entirely standard-library and recomputes two complete independent exact audits, third centred mass integration, all maximal incidence and strict/weak equilibrium signs, both zero-stress refinement diagonals, faithful contact and Maxwell/inverse maps, 9454 three-connectivity cases, and nonvacuous controls. It also independently audits both retained exact nonwinners. `RECEIPT.json` is emitted only after every required assertion has completed.

The next two commands require NumPy2.3.5 and SciPy1.17.0; observed Python3.13.5. They replay the literal final checkpoint and the12-step analytic mass-correction path, respectively. Both were observed to produce the exact same generator. `--optimize` additionally reruns the exploratory2000-evaluation hinge least-squares phase. Changed floating proposals are not certified; the literal finite candidate is authoritative.

PREPARE_NEXT prepares the accepted C626 maximal chart for continuation with all existing contacts preserved. It does not claim any further edge loss. Copying that new directory's baseline/chart into a discovery workspace and using GeneralAtlas with a listed eligible edge provides the same full contact/mass mechanism. A degree-three polar endpoint loss requires genuine suppression and new maximal incidence; the triangle-union atlas deliberately excludes that case.

## Recorded nonwinners

`nonwinner_warm`: C626, strict(95,97,190), weak000. This is the grid10^9 rationalization of the full-contact least-squares checkpoint before successful mass-aware correction, not a winner.

`nonwinner_pentagon`: C626, strict(1,2,1), weak000. It has exact five-contact {16,18,55,71,94}. The extra unstable point is that five-contact rawlex88; the saddle is rawlex edge90--95. All137 facets, including the very small triangular support16, remain maximal. A tolerance-based numerical suppression would miscount this body; only exact incidence is authoritative. Both complete exact audits and centred mass integration completed for both nonwinners. Neither is an impossibility certificate.

## Source authority

Original operator-preserved RL07 raw result:52764 UTF-8 bytes, SHA256 adde3e920f2cdf7f5bfcbd4d6ed4c99f2b7484be5d969ebf42ba9fd49cfb8214. It was recovered from the journal's literal three-part raw answer, not a fabricated immutable scheduler result. Original15-file map SHA256 bf845a6aad83816c0238c1b301b69dd4a7d49a74a2cb13de1a2dd65dedb245f8. Literal C628 parent generator SHA256 94b1784349c731f5b19e99444c6eb14507b42a954ea2824f9a4eda6470bbf4ed is included in full here.

No claim of global minimality, independent human peer review, formal proof-assistant verification, manufacturing tolerance or an exact no-birth homotopy is made. C<32 remains outside the assigned search scope, not an established lower bound.
