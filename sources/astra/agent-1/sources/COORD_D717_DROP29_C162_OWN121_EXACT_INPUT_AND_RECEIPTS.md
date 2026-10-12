# Recovery capsule part 1/1 — COORD_D717_DROP29_C162_OWN121

## Identity and result
New informative NONWINNER: remove original input row29 from the literal D717 hull, retaining all other input coordinates including original interior rows5,6. This is a different exact body from D717 and from both COORD_NONAFFINE_cyclic_D1000 and cyclic_D10000; C162 alone is not an alias.

The uniformly FILLED body has true V29/E81/F54,C162, own-centroid strict(S,U,H)=(1,2,1), weak000. All reported face,vertex-max and edge primitive zero counters are0. A supplementary exact all-distinct-vertex-pair escape check also found no zero. Full independent A/B audits and third positive centered-tetrahedron mass integration were executed to completion.54 positive tetrahedra, exact centered first moments0, volumes agree. It is NOT an own110 construction and does not change canonical accepted C622.

Ordinary volume93367248745/2211610878. Exact own filled centroid is
(13172649867893,-9149149779648,-9664147072343)/267777269400660.
The minimal common denominator of reduced centered vertex coordinates is267777269400660,48bits; maximum centered integer coordinate51bits. Raw coordinate maximum reduced denominator10bits,numerator12bits.

Rawlex-to-original-input labels:
[0,4,1,2,8,7,9,3,10,12,15,11,14,17,13,16,30,19,18,20,21,22,25,31,24,26,23,28,27].
S raw support50, raw face polygon[25,28,27], original input labels[26,27,28]. U raw25/26=original inputs26/23. H raw0--2=original inputs0--1. These labels are local to this exact body.

Scientific parent: fully read asg_tBnseXYKfUe8912fe5d0SOFM, SHA2562ee8abc72403f981770152547d685735c7cc724a253f7ac7b354dff4fc7e19f1. The exact finite family exclusion in att_98271e77193cc9c99046_01 contains this case and independently proves at least2U; this material adds its full mechanical census and independent acceptance pipeline.

## Complete dependency and commands
The only source dependency is the already immutable complete six-file audit capsule **att_572f9bc48c511c01950e_01**, COORD_D100_STANDALONE6_EXACT_OWN121_SOURCE_V1.md,14044bytes,SHA256572f9bc48c511c01950ed7f8435ea46aded86eec9f05a9a67c54319308aaf85c. It contains the full generic audit_rational.py, independent core/check_B.py and core/centred_mass.py. Its D100 geometry is merely an upstream regression, not substituted for this DROP29 input.

From that dependency save its Python fence as RESTORE.py and text fence as SOURCE6.b64; run `python -B -S RESTORE.py SOURCE6.b64 D100_CORE D100_CONTROL`. The decoded dictionary19753bytes SHA9793ea2121a3149cada862af94f18fa13e9192a7014dcba1ccb92366162a5949 is complete. All output directories must initially be absent. Save the JSON fence below as DROP29.json with NO final newline, then run:

`python -B -S D100_CORE/audit_rational.py DROP29.json D100_CORE/core DROP29_PROOF`

CPython3.13.5 standard library only, assertions enabled, no random seed or precision setting. The input JSON's triangle proposals were generated once with SciPy1.17.0 but are preserved literally; reconstruction and certification use NO SciPy. Audit A proves their exact supporting planes and maximal hull; B independently reconstructs the full halfspace intersection, incidence and ordinary mass; the third separately integrates positive tetrahedra at the exact centered integer coordinates.

The exact command was executed and printed:
`EXACT_RATIONAL_HULL_TWO_AUDITS_AND_CENTRED_MASS_PASS COORD_D717_DROP29_C162_OWN121 29 81 54 [1, 2, 1] [0, 0, 0]`
(the runtime seconds suffix is not part of the deterministic record).

## Input/output byte identities
DROP29.json1757bytes SHA256bba7fc65e3dee174f821da817182c0ca69d62913be0a9ae2171671de2ac55538.
A.json12350bytes SHA256b9b5a565c4f9fe0b0630ef627c91d6f8075ae490faff73e0fb8bd550712210a1.
B.json7330bytes SHA256f1218fbf6c51e1486e26f820fdd0ad5862804ab37c12f92b9050d1ce74897abc.
H.json2256bytes SHA2565c3b35b66a5913713716a8fdd83aac17a2e4e2f5a0d76c1616e699ac7070656c.
MASS.json216bytes SHA25694d2a74ec13ced79f5f6a0fdcc1917e17107468f0cadcc7cdc3254923333f256.
SUMMARY.json1146bytes SHA256d289bdb7dc2226a93f4698ad243018ec0c04352b7cf37eb613319cd8d975295c.
The complete source dependency verifies its own original regression hashes. This input plus that full immutable dependency is sufficient to reconstruct all outputs without the originating sandbox.

## File DROP29.json
```json
{"labels":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31],"name":"COORD_D717_DROP29_C162_OWN121","points":[["-1513/717","11/717","-73/239"],["-1477/717","17/717","494/717"],["-467/239","170/717","-806/717"],["-1132/717","451/717","133/239"],["-1477/717","-104/717","-179/239"],["-967/717","102/239","301/717"],["-860/717","296/717","185/717"],["-1366/717","-514/717","-149/717"],["-1369/717","-81/239","830/717"],["-1144/717","178/239","-397/239"],["-336/239","-649/717","1324/717"],["-108/239","1060/717","643/717"],["-418/717","-983/717","-854/717"],["0","508/239","443/717"],["-91/239","119/239","-1439/717"],["-389/717","-1400/717","657/239"],["62/239","1064/717","677/717"],["-16/717","-565/239","-631/717"],["421/717","-1700/717","647/239"],["208/717","278/239","-1594/717"],["445/717","1739/717","226/717"],["503/717","-784/239","-71/239"],["587/717","1751/717","-1733/717"],["917/717","-635/239","1672/717"],["883/717","-769/239","125/717"],["200/239","2569/717","-394/717"],["884/717","3415/717","-1871/717"],["1046/717","-652/239","508/239"],["1034/717","-2222/717","194/239"],["188/717","-2248/717","1078/717"],["764/717","2962/717","-989/717"]],"triangles":[[28,26,27],[28,27,29],[7,21,29],[15,7,29],[22,9,26],[30,27,26],[30,25,27],[30,26,25],[20,25,13],[18,15,29],[8,7,15],[2,0,26],[2,26,9],[19,22,21],[19,14,9],[19,9,22],[24,21,22],[24,29,21],[24,28,29],[24,26,28],[24,22,26],[23,20,18],[23,27,25],[23,25,20],[23,29,27],[23,18,29],[16,20,13],[16,18,20],[16,13,15],[16,15,18],[10,8,15],[1,26,0],[1,0,7],[1,7,8],[4,7,0],[4,0,2],[17,19,21],[17,14,19],[17,21,7],[17,7,4],[11,15,13],[11,10,15],[11,8,10],[11,1,8],[3,25,26],[3,26,1],[3,13,25],[3,11,13],[3,1,11],[12,2,9],[12,9,14],[12,14,17],[12,4,2],[12,17,4]]}
```
