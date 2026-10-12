# material-c20501687f00

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# COORD_D100_MONOSTABLE_AFFINE_COMPONENT_EXACT_SOURCE5_V1

## Scientific object and scope

This is an exact obstruction for the actual COORD_RELEASED8_DUAL_PRUNE32_D100 body, V32/E90/F60,C180, own strict121/weak000. It is NOT a new own110 construction. The accepted C622 record is unchanged. The body and its complete independent full A/B geometry, incidence, ordinary-filled-volume-centroid, strict/weak all-feature audits and separate centered integration are in required immutable material **[internal-source-reference]**, SHA572f9bc48c511c01950ed7f8435ea46aded86eec9f05a9a67c54319308aaf85c,14044bytes. This addition needs that complete material, but no historical worker result or other source. All source files below are complete.

**Theorem.** Let D_S consist of positive-definite symmetric polar metrics H, trace(H)=1, for which an affine image of this uniformly filled physical body has exactly one strict stable face and no weak stable face, with other equilibrium counts unrestricted. The entire connected component of D_S containing H=I/3 is the open convex region given by the 17 core inequalities specified below. Throughout its closure the two physical raw-lex vertices26 and27 are separately strictly unstable. Therefore no own110/weak000 body lies in that component. Other connected components, the whole affine orbit, projective images and non-affine changes remain OPEN. A path allowed to leave D_S is not excluded. No theorem about the distinct C198 body is used.

The physical Gram metric is a positive scalar times H^{-1}, equivalently adj(H) for signs. H is the metric on the physical OWN-CENTERED polar, not the Gram metric on physical vertices and not a metric about the filled centroid of the polar.

## Proof and all finite coverage obligations

Read X_i=v_i-c and Q_f=n_f/(h_f-n_f dot c) from the exact reconstructed A.json of the required seed. Vertex and face indices are that A output's raw-lex vertex and maximal supporting-plane order. The physical centroid c is the actual ordinary-filled-volume centroid. In an affine image it transforms affinely, so inverse primal/polar Gram coupling is exact.

For every directed adjacent polar pair define r_ij(H)=Q_i^T H(Q_j-Q_i). The code divides each six-coefficient row by its positive rational maximum absolute coefficient; no irrational normalization is used. H has coefficient order (a,b,c,d,e,f), meaning [[a,d,e],[d,b,f],[e,f,c]], and trace row (1,1,1,0,0,0). At H=I/3 root47 is a strict local radial maximum and the other59 polar vertices have the positive witness arrows W stored completely in metric_component.py. The checker proves all59 arrows are adjacent and strictly positive at I/3, have exactly the59 nonroot sources, and follow finite paths to47.

Among these59 rows, core indices are [0,3,9,13,15,17,20,22,27,33,35,37,39,41,48,53,54]. Their arrows are [(0,1),(3,8),(9,6),(13,9),(15,7),(17,26),(20,41),(22,14),(27,12),(33,23),(35,16),(37,11),(39,45),(41,36),(49,46),(54,56),(55,51)]. This is a complete defining17-inequality description; irredundancy of every listed inequality is not needed or claimed.

There are88 exact Farkas certificates:12 coordinate bounds,42 strictly positive lower bounds for the other witness rows, and34 strictly negative alternative-escape upper bounds on the17 possible core zero walls. Every certificate uses ONLY those17 core rows. The checker reconstructs each entire rational vector identity from its frozen sparse basis, checks nonnegative inequality multipliers, and checks every residual exactly. Explicitly objective=sum lambda_k*C_k+mu0*TRACE+mu1*C_wall, where lambda_k>=0; mu1 and its equality are present only for a wall. On C_k>=0,trace=1,wall=0 the certified lower bound is mu0. Every absent-row lower bound and every negated alternative's lower bound is strictly positive. All alternatives are enumerated from independently audited actual incidence, two per nonroot polar vertex because every physical facet is triangular.

Consequently the59-row closed cone equals the17-row closed cone. The remaining42 inequalities are uniformly strict throughout the latter. The coordinate certificates, rounded outward to denominator10^6, bound
(a,b,c,d,e,f) in
[319353,347175]/10^6 x [320982,356166]/10^6 x [317533,350840]/10^6 x [-11507,11881]/10^6 x [-9331,6357]/10^6 x [-13482,37526]/10^6.
The three strict diagonal-dominance lower bounds are298141/1000000,10863/40000,67669/250000. Thus the entire closed polytope is SPD, without relying on a floating semidefinite relaxation.

In the open core cone every nonroot has a positive radial escape. A global farthest polar vertex under an SPD norm is always a STRICT radial maximum: for distinct neighboring q', q^T H(q'-q)=(||q'||_H^2-||q||_H^2-||q'-q||_H^2)/2<0 when q is farthest. Since no nonroot can be a closed radial maximum, that global maximum must be47. Therefore root47 is strict and every other face is neither strict nor weak stable, so the open cone lies in D_S. It is convex and nonempty, hence connected. At every boundary point at least one core row is zero; for that source both other adjacent escapes are strictly negative by the exact wall certificates. It is therefore a weak stable face and the boundary is disjoint from D_S. The open cone is both relatively open and relatively closed in D_S and contains I/3, proving that it is exactly the stated connected component.

Finally the checker interval-bounds all six entries of adj(H): (bc-f^2,ac-e^2,ab-d^2,ef-cd,df-be,de-af), using the exact coordinate box. It checks every physical adjacent escape X_i^T adj(H)(X_j-X_i) for i26 and27. The complete neighbor lists are26->[22,24,28,29,31],27->[23,25,30,31]. All nine interval upper bounds are strictly negative. The largest upper bound is -200621717938935706497551/5332021480000000000000000. Thus both vertices are strictly unstable on the entire CLOSED cone, completing the exclusion.

## Observed execution, recovery and dependency rules

This coordinator reconstructed the required seed in a fresh container from its complete literal six-source capsule and completed its independent A/B and third-mass replay. It then ran the complete numerical basis proposer and exact checker. A second absent-directory source-only restoration of BOTH seed6 and this addition5 completed again, with all8 terminal output byte/hash receipts identical. This is a completed exact certificate computation, not a numerical conjecture and not an unsolved formula export.

Proof replay uses CPython3.13.5 standard library only, assertions on, no seed or stochastic input. Numerical discovery additionally used NumPy2.3.5 and SciPy1.17.0 with OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1. The complete proposer source contains every LP bound, objective, normalization, HiGHS option, tolerance and sparse-basis fallback. Floating optimization proposes bases only; all accepted certificates are reconstructed and checked with fractions.Fraction. Proof replay consumes the literal frozen COMPONENT_BASES.json, not an optimizer's future choice.

Save the required seed material's base64 payload, stripping whitespace, as SOURCE6.b64. Save the text payload below as COMPONENT5.b64. Save the following complete decoder as RESTORE_COMPONENT.py. Run with a new absent destination:

`python -B -S RESTORE_COMPONENT.py SOURCE6.b64 COMPONENT5.b64 absent-root`

The decoder creates seed/ and component/ then runs component/REPLAY.py, which executes both independent full seed audits, the separate centered mass integration and the88 exact certificates, and verifies all8 receipts. Direct verification, after restoring sources but before proof directories exist, is `python -B -S absent-root/component/REPLAY.py`.

Optional regeneration of the proposed sparse bases after recovery:
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B absent-root/component/discover_component.py absent-root/seed-proof NEW_BASES.json`
Then run `python -B -S absent-root/component/metric_component.py absent-root/seed-proof NEW_BASES.json new-absent-proof`. Numerical basis selection may differ with solver versions; every alternative still must pass the exact checker. The frozen literal checkpoint guarantees the byte-identical replay reported here.

Expected terminal markers:
COORD_D100_STANDALONE6_SOURCE_AB_MASS_COLD_PASS
D100_ALL_88_DISCOVERED_LP_BASES_EXACTLY_VALIDATED (optional numerical discovery)
D100_MONOSTABLE_COMPONENT_88_EXACT_FARKAS_AND_TWO_FORCED_UNSTABLE_PASS
D100_MONOSTABLE_COMPONENT_STANDALONE_SEED_AB_MASS_AND_88_CERTIFICATES_SOURCE_COLD_PASS 8

Addition encoded7816ASCII bytes SHA05f029da93df922623a7a6d4338ccc077640fa3a8edd9726ba121505b3baeb5b; decoded UTF-8 JSON dictionary16423bytes SHA80d9ffd06b42498acdc838cb9945955e87149fd570f4df2735be04387b27c236. Source filenames/bytes/SHA:
- metric_component.py8374,7a37b59660fb20a700a8e9d11832f0a6ceef52fb90089627d80cc5b53f7496fb
- discover_component.py2061,275f5d6d6045870a6c34b6ebbdcd3abf3753ec281ac4085aa900151f31433496
- COMPONENT_BASES.json3519,d86176b519ce7be1b535dcc1a9049dfd9c70e91897b28ee5579d95270342a9d3
- EXPECTED.json937,184651ad837c6cd7bca68d503c1469f13bfacc74cacc9ccf7e5ac45022629954
- REPLAY.py731,693cc3f672fb6542024ffdb0b3b4e3d7582d6795a4f770f846bac37f4b334856

Output filenames/bytes/SHA, all8 checked in the cold restoration:
- component-proof/CERTIFICATES.json132156,f872b73072fd82600771bb0a1f771f7274b2ce7b85b7ae9e66ffbe77e3a29412
- component-proof/SUMMARY.json1593,5d80531af05b670ab3ba205bc9b6386993c634e7df45ecb9a9455229a434750e
- component-proof/RECEIPT.json220,768ca405bbe385b354049cf8fed272bc938a833cadd3464e83378d53a5d74786
- seed-proof/A.json13409,449e2c663dd927a1edd48ebc0e56b89221be1cf45e20b782a429c807df758fb6
- seed-proof/B.json7081,af7509b5b9cbb9b174623fa9a3531e1512560e05213d2e1bf231874ddb8c3c1d
- seed-proof/H.json1760,535865b94a8f401d861c9ec60bda402121e7cad6d88fb57413eb8a3f549a0dc9
- seed-proof/MASS.json216,62bf93a59bb81cf1933c76918d377e95e786b194afbfdda72edabb17be8813d6
- seed-proof/SUMMARY.json1167,085adb5850959d53e97ac6e9656f6c1dd9be2f1ee0aeb1adee8bb6d5177ac8a4

```python
from pathlib import Path
import base64,hashlib,json,lzma,subprocess,sys
assert __debug__
checks=[(9368,'adb438e45e92f946524ccac9b804d2e7d2c9b7455faffe6ab820a174249ef466',19753,'9793ea2121a3149cada862af94f18fa13e9192a7014dcba1ccb92366162a5949',6,'seed'),(7816,'05f029da93df922623a7a6d4338ccc077640fa3a8edd9726ba121505b3baeb5b',16423,'80d9ffd06b42498acdc838cb9945955e87149fd570f4df2735be04387b27c236',5,'component')]
root=Path(sys.argv[3]);root.mkdir(parents=True,exist_ok=False)
for source,(n,h,dn,dh,count,subdir)in zip(sys.argv[1:3],checks):
 s=''.join(Path(source).read_text().split()).encode();assert len(s)==n and hashlib.sha256(s).hexdigest()==h
 raw=lzma.decompress(base64.b64decode(s,validate=True));assert len(raw)==dn and hashlib.sha256(raw).hexdigest()==dh
 data=json.loads(raw);assert len(data)==count
 for name,text in data.items():
  p=Path(name);assert not p.is_absolute()and '..'not in p.parts
  q=root/subdir/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(text.encode())
subprocess.run([sys.executable,'-B','-S',str(root/'component/REPLAY.py')],check=True)
```

## Complete literal addition5 payload

```text
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
```

## Consequence for continuation

Ordinary local affine fitting while retaining monostability cannot cancel the seed's last U/H pair: it stays in this exact component. Useful next directions are genuinely different monostable affine components (allowing intermediate S>1 or weak boundaries), projective changes with recomputed actual mass, and non-affine whole-basin/interface replacement. The finite LP proposal phase does not by itself exclude any of these. Preserve new rational nonwinners as well as any own110 winner.
