# material-cad0b83d1b30

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Reconstruct the exact six-deletion body from the preserved25-deletion checkpoint."""
from pathlib import Path
import hashlib,json
root=Path(__file__).parent
raw=(root/'J99_PRUNED25_INPUT.json').read_bytes()
assert hashlib.sha256(raw).hexdigest()=='d67d882bfee515e445afdccda95668c259b83b1ae2d14af1f760899a56b4f36c'
p=json.loads(raw)
vertices=dict(zip(p['retained_original_indices'],p['retained_incident_supports']))
extra={24: [13, 30, 37], 39: [29, 36, 45], 55: [50, 69, 70], 75: [7, 13, 16], 76: [2, 9, 11], 77: [51, 54, 60], 85: [75, 77, 78], 86: [18, 45, 75], 98: [13, 43, 44], 104: [76, 77, 78], 115: [13, 39, 44], 124: [1, 6, 9], 126: [2, 6, 9], 127: [6, 15, 23], 128: [1, 5, 7], 133: [4, 12, 14], 142: [21, 24, 52], 146: [10, 14, 23], 152: [3, 6, 35]}
assert len(extra)==19 and not set(extra)&set(vertices)
vertices.update(extra)
ids=[i for i in range(160)if i not in [44,19,18,36,81,92]]
assert sorted(vertices)==ids
faces=[[43,35,40],[86,21,87],[37,33,34],[15,12,18],[77,36,76],[75,73,74],[115,114,116],[124,5,1,59,72,125],[128,123,122,130],[151,152,27,28],[28,7,150,151],[149,150,7,31],[17,15,14,16],[118,120,72,59,70,69],[133,105,104,134],[134,104,60,136],[86,85,19,20,21],[138,125,72,120,137],[139,138,137,141,140],[26,25,127,139,140],[140,141,121,24,26],[119,118,69,122,123,117],[128,129,117,123],[20,19,2,3,11,10],[93,55,17,16,57,58,101,100,95],[131,130,122,69,70,71],[131,71,105,133],[107,91,89,46,67,68,106],[87,21,20,10,48,49],[88,90,8,45,44],[62,61,63,64],[139,127,126,124,125,138],[6,5,124,126],[25,6,126,127],[121,145,143,23,24],[29,23,143,144],[30,29,144,147],[148,149,31,32],[32,30,147,148],[27,152,153,132,0,40,35,34,33],[55,56,12,15,17],[53,13,12,56],[13,9,11,3,18,12],[48,10,11,9,51,52],[54,51,9,13,53],[93,94,54,53,56,55],[52,51,54,94,96],[96,94,93,95],[64,63,60,104,105,71,70,59,1,14,15,18,3,2,92,109,108,22],[107,106,108,109],[62,64,22,66,65],[106,68,66,22,108],[68,67,65,66],[110,112,4,8,90],[110,90,88,89,91,111],[45,8,4,83,84],[87,84,83,85,86],[96,95,100,102,47,50,49,48,52],[87,49,50,44,45,84],[47,38,40,0,46,89,88,44,50],[132,153,142,129,128,130,131,133,134,136,135],[135,136,60,63,61],[65,67,46,0,132,135,61,62],[146,119,117,129,142],[149,148,147,144,143,145,146,142,153,152,151,150],[141,137,120,118,119,146,145,121],[36,37,34,35,43,42],[43,40,38,39,41,42],[102,100,101,103],[37,81,82,57,16,14,1,5,6,25,26,24,23,29,30,32,31,7,28,27,33],[4,112,113,92,2,19,85,83],[109,92,113,111,91,107],[112,110,111,113],[41,76,36,42],[76,41,39,73,75,77],[97,78,79,74,73,39,38,47,102,103,114,115],[79,81,37,36,77,75,74],[103,101,58,99,116,114],[99,98,97,115,116],[81,79,78,80,82],[98,99,58,57,82,80],[80,78,97,98]]
out=dict(identity='J99_R82_PRUNED6_C468',retained_incident_supports=[vertices[i]for i in ids],retained_original_indices=ids,faces=faces)
data=(json.dumps(out,separators=(',',':'))+'\n').encode()
assert len(data)==3959
assert hashlib.sha256(data).hexdigest()=='cb5150c5ace22ab9350b0cebc72f22088bcaa0533e3495d02f4cc954916b1939'
(root/'J99_PRUNED6_INPUT.json').write_bytes(data)
print('J101_EXACT_C468_INPUT_RECONSTRUCTION_PASS',len(data),hashlib.sha256(data).hexdigest())
