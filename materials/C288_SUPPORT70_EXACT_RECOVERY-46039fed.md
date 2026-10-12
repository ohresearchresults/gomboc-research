# material-46039fed037c

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# C288_SUPPORT70: exact support-deletion nonwinner

A new uniformly filled rational convex body, V76/E144/F70, C288, own strict211, weak000 and primitive-zero000. Not the requested own110 construction. Canonical own110 record remains C622. This exact nonwinner is derived from C330_ROOTFREE_G5 by deleting precisely the omitted physical supports from its canonically sorted exact H-description; it is not a vertex deletion or an affine image.

## Complete recovery dependencies

Read and supply both C330 recovery materials: [internal-source-reference] (C330_ROOTFREE_G5_LITERAL_GEOMETRY.md, SHA66acbe5c6104c66f7b6d19ee683fc4281787435772b5bd3cf3e98d549615da18) and [internal-source-reference] (C330_ROOTFREE_G5_COMPLETE_AUDIT_SOURCE.md, SHA9a9df583f7de4e822792c875bc35043156693591d06b14c924c488995a2ff4b2). Together with this material they supply every exact coordinate, support nomination, helper, and audit source. Extract the two-part parent as instructed there and execute its audit once to PARENT. Save the following complete source as RECONSTRUCT_C288.py. Run `python -B -S RECONSTRUCT_C288.py PARENT/RAW.json C288`. The target C288 directory must be fresh. No numerical search, old sandbox, external library, or unstated parameter is needed.

```python
import sys,json,hashlib
from pathlib import Path
sys.set_int_max_str_digits(0)
sys.path.insert(0,str(Path(__file__).resolve().parent/'exact_source'))
import check_A as A,check_B as B,centred_mass as M
J=lambda v:json.dumps(v,sort_keys=True,separators=(',',':')).encode()
assert __debug__ and len(sys.argv)==3
p=Path(sys.argv[1]);data=p.read_bytes();assert len(data)==6701 and hashlib.sha256(data).hexdigest()=='9391eef0f0d760dbedbc7fc48accfdfc4014bb0dc00f232d4af3ba6729540c2f'
keep=[0,2,3,4,5,7,8,9,10,11,15,17,20,21,22,23,25,27,28,29,31,32,33,34,36,38,40,42,43,48,50,51,54,55,56,58,59,60,63,64,65,67,68,69,73,74,75,76,78,80,82,85,86,87,88,90,91,92,93,94,95,96,99,101,102,103,105,107,108,109]
raw={'H':[json.loads(data)['H'][i] for i in keep]}
a=A.run(raw);b=B.run(raw);assert J(a)==J(b);m=M.run(a)
assert [a['V'],a['E'],a['F']]==[76,144,70] and a['counts']==[2,1,1] and a['weak']==[0,0,0]
assert [a['face_primitive_zero_count'],a['vertex_max_zero_count'],a['edge_primitive_zero_count']]==[0,0,0]
assert a['stable_face_ids']==[0,54] and a['unstable_vertices']==[16] and a['saddle_edges']==[[57,59]]
assert m['tetrahedra']==148 and m['filled_first_moments']==[0,0,0]
expected={'RAW.json':(4288,'ff6315752d61fa1a04c065f1b311db6d28e621c5a0f09bea706b297aaf1b264f'),'A.json':(39507,'93a142eefdf1fb53b4b5a080089c6243f670c66a6e15c8a38be8c428b4971a7d'),'B.json':(39507,'93a142eefdf1fb53b4b5a080089c6243f670c66a6e15c8a38be8c428b4971a7d'),'MASS.json':(221,'c766982bb5596007a73095abb35e95262f396b225ccc16bfc404ae67efa8e7f0')}
out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=False)
for name,value in [('RAW.json',raw),('A.json',a),('B.json',b),('MASS.json',m)]:
 bb=J(value);assert (len(bb),hashlib.sha256(bb).hexdigest())==expected[name];(out/name).write_bytes(bb)
print('C288_SUPPORT70_EXACT_AB_MASS_NONWINNER_PASS',a['counts'],a['weak'],flush=True)
```

The exact computation producing all four expected outputs completed in this coordinator context: independent A/B reports matched byte-for-byte and a third integration over148 positive centered integer tetrahedra matched the volume and had exactly zero first moments. The literal reconstruction wrapper above adds the pinned-output assertions; its terminal marker will be called cold-replayed only after execution from a fresh extracted source. Common centered integer denominator5173bits: this is much worse arithmetic than the original C330's72bits, despite fewer true edges.

## Consequential geometry and scope

With F<=70 under arbitrary bounded full-dimensional deformations of these70 inequalities, Euler and minimum vertex degree give E<=3F-6<=204. Adding at most35 further physical supporting planes gives F<=105 and E<=309, still C<=618. This is a topology-independent complexity resource, not a mechanical existence theorem. The retained own211 state has only one surplus S-H pair, but no small global polar-basin barrier is claimed. The finite scout's all-pair local escape diagnostic is not a true-edge bottleneck certificate.

## Production method boundary

Produced by a complete40-level width6 support-deletion beam from exact C330 RAW, numerical edge ceiling310,20,822 attempted distinct subsets. Selected level39 attempt20,479, not the last arbitrary output. Each trial reconstructed the polar hull, physical vertices, ordinary filled centroid, physical/polar escape signs and estimated true E via Euler; floating deduplication used9 decimal places and was only a scout. The complete chosen rational H-subset, not the scout's tolerance or topology, defines the object; the independent exact audits establish all accepted counts above. The full runnable producer and finite report are separate method evidence. No continuous-family exclusion and no own110 endpoint was obtained by the finite beam.
