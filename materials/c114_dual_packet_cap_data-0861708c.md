# material-0861708cde29

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

C114 dual-polar whole-basin separator and one-cap exact patch.
Status: exact coordinator nonwinner; not own110.
Dependency: immutable parent result figure-0438, exact body VL12_DUAL_CANCEL21_G4.

Parent exact physical body: V21/E57/F38,C114, strict211/weak000. All 38 physical facets are triangles, so the same-physical-centre polar is simple V38/E57/F21. Sole positive polar strict-upper packet:
[0,2,4,9,11,13,14,17,19,20,26,30,32]
with 15 boundary cut edges, hence simple-packet cycle rank r=(13-15+2)/2=0.

Exact separator in the parent's actual-centred coordinate frame:
a=(3/5,-1,-1), cut h=2.
Every retained polar vertex satisfies a.q<2; every packet polar vertex satisfies a.q>2.
Minimum packet value is at polar vertex 32:
6104561850604438971752000/2717758194599235640710191.
Maximum retained value is at polar vertex 34:
5377780345688294868040000/3290438764026334302719257.
Exact positive margins:
minpacket-2 =
669045461405967690331618/2717758194599235640710191.
2-maxretained =
1203097182364373737398514/3290438764026334302719257.

By polarity, intersecting the old same-centre polar with a.q<=2 is exactly dual to adding one physical point
p=a/2=(3/10,-1/2,-1/2)
to the parent's actual-centred physical hull.

Exact child after adding p and rebuilding its own uniform filled-volume centroid:
V22/E60/F40,C120.
Volume =
38659275694658640364928149/24581892172315200000000000.
New centroid in the parent-centred frame =
(-15035788158214841071491554054370232952823773/158386357764317416249624482114762496760800000,
 -929345067836311679624744516241928988956891/9899147360269838515601530132172656047550000,
 -8755089546222648656398928333185105168246479/158386357764317416249624482114762496760800000).

Exact child mechanics:
strict S/U/H = 5/17/20.
weak S/U/H = 0/0/0.
primitive mechanical zero counts = 0/0/0.
Stable face indices [0,5,6,7,35].
Unstable vertex indices [2,3,4,5,6,7,8,9,10,11,12,14,16,18,19,20,21].
Strict H true edges:
[[1,3],[2,13],[2,15],[2,21],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10],[10,11],[11,12],[12,14],[13,21],[14,16],[16,18],[16,21],[18,20],[19,20]].

Coordinator exact verifier terminal marker:
C114_DUAL_PACKET_CAP_EXACT_PASS 1400 ee707a499fa6358a8c34ec1904fed7fc821699a5604185a7f927d68949fa7606
Local verifier source used CPython standard library only; source SHA-256 2a6b773b68e0a9dec877779576e9dab4ccf0db3d422429f2412679013e78a363.

Scientific interpretation: the complete old extra stable/polar basin is strongly one-cap-separable at only +3 true-edge cost, but the arbitrary cut h=2 shifts actual mass/mechanics catastrophically. The next exact problem is the full cap-offset/orientation chart, not repeating this one representative.
