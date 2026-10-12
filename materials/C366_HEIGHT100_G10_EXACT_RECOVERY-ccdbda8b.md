# material-ccdbda8b3940

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# C366_HEIGHT100_G10 — exact homogeneous monostable, bistable-in-U nonwinner

This exact rational uniformly filled body has V122/E183/F63, C366, own strict[1,2,1], weak000 and primitive-zero000. The name records its100-input height-deformation origin; its ACTUAL maximal support count is63. It is NOT own110 and does not replace C622. No reference-centroid substitution is used for the accepted class: both complete auditors recompute the ordinary filled centroid from this literal rational body.

The body was produced by protected polar refinement of C378_GLOBAL65_G9 followed by mass closure in the linear height cone. The floating precursor had centroid residual about2e-10, but this is not used as an exact lock. The accepted own121 conclusion comes from full rational hull/mechanics/mass reconstruction after freezing the63 active support vectors at grid10^10. Its two unstable vertices are genuinely strict, not weak. A vanishing local escape residual near an edge of length3.19e-8 had misleadingly suggested near-cancellation; the numerical whole physical bottleneck is about-.826, a large obstruction. That decimal is a numerical diagnostic, not a new exact cut exclusion.

## Complete recovery

Only the complete independent auditor source material [internal-source-reference] and this material are needed to reconstruct the exact geometry and mechanics. Save the JSON line below without a terminal newline as POLAR_POINTS.json and the complete source below as RECONSTRUCT_C366_HEIGHT100.py beside exact_source/. Run `python -B -S RECONSTRUCT_C366_HEIGHT100.py OUT` with OUT absent. Expected terminal marker C366_HEIGHT100_G10_EXACT_OWN121_AB_MASS_NONWINNER_PASS. CPython3.13.5 standard library, assertions enabled. No floating optimizer, originating sandbox, source ZIP or old output file is needed.

Independent A/B and third centered integration have already executed for the exact body and matched every expected output identity below. The newly assembled wrapper is not called cold-replayed merely because it was stored. Its240 positive centered tetrahedra have exactly zero first moments; common centered denominator22026bits and maximum centered integer coordinate22027bits. This arithmetic is much worse than C330's72-bit V-description and is retained for its different monostable height architecture, not simplicity.

## POLAR_POINTS.json
2365bytes, SHA256207426c620eacfcaba4a3d60d9fc13fdaed16d41236ddd458ac3829ac5ea0973. The physical body is the intersection of row dot x<=10000000000, NOT the convex hull of these rows.
```json
{"grid":10000000000,"points":[[-19069246691,-10431901805,4531017550],[-16678004971,-9874833314,3144843203],[-7749441786,-1267257945,4978466577],[-4716842017,-6086504703,-2853674584],[-1479314952,-5698020271,-4191108833],[1857037837,504975161,5833145586],[513627685,9085221336,-7045333784],[1496759762,-1659616619,6156610708],[10978351650,-10431709829,5341784630],[1670086289,16579794326,-3031349186],[1925400206,16578760495,-1685790122],[1067764142,5610870305,-7439138981],[5765086385,-6339613928,-6165521811],[1469415186,4310297569,-7467512075],[4692051455,-3300502037,-7211218968],[10338150531,2569257866,-11096325944],[13153534331,-7045271050,2555754328],[13078693213,5503694530,1454950642],[10097391617,6781658845,-9677095377],[12751299837,5027548842,-7095516798],[14605873217,-3864743043,106724843],[14234107852,1916393050,-5305243919],[15024464223,-553943083,-2278338118],[7011802200,-13709982419,6959092137],[-2456849508,17096463790,-2479278479],[-6686280218,16595733882,-1741190768],[-10764962710,15045898942,-850962858],[-14433367779,12477685190,146114193],[-17452858645,8992188621,1196212291],[-19589216755,4735239238,2238705136],[-20642538193,-79753168,3206972578],[-20493758971,-5185340662,4037863449],[-363461842,-11674955270,6875329613],[10771931872,3004087901,5606782782],[10359072511,3648128015,-10827053745],[10325941761,4713565509,-10499764543],[10238657058,5759932372,-10115874760],[10451502683,-11462785105,4427284342],[5997712275,-14954574777,5963572682],[153096583,-16923026781,6911546827],[-6483684834,-16918560080,7072784303],[-13142033588,-14682762280,6322756009],[14511997380,2661889879,-364343352],[9031106071,9388596294,-8962772208],[7611931760,11758527203,-7910249216],[5877133458,13800343035,-6544490648],[3876308861,15431218185,-4902280315],[12289692643,5408818705,-7654924498],[11792145627,5775918358,-8194333395],[11259961792,6127774043,-8712168003],[10694543401,6463351138,-9206908071],[14754530678,-3329910234,-292936736],[14869547758,-2786158405,-692856485],[14954124001,-2235535685,-1092172405],[15008248163,-1679205787,-1490070275],[15031730428,-1118294631,-1885730574],[13947977463,2708906336,-5786695404],[13604656775,3493720043,-6246831417],[13205304308,4267651717,-6683721257],[14948455400,-60203726,-2899640811],[14831149777,435058398,-3514681409],[14672755732,930486148,-4121752030],[14473597431,1424718345,-4719162645]]}
```

## RECONSTRUCT_C366_HEIGHT100.py
```python
import sys,json,hashlib,math
from pathlib import Path
sys.set_int_max_str_digits(0)
sys.path.insert(0,str(Path(__file__).resolve().parent/'exact_source'))
import check_A as A,check_B as B,centred_mass as M
J=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
assert __debug__ and len(sys.argv)==2
p=Path('POLAR_POINTS.json').read_bytes();assert (len(p),hashlib.sha256(p).hexdigest())==(2365,'207426c620eacfcaba4a3d60d9fc13fdaed16d41236ddd458ac3829ac5ea0973');cfg=json.loads(p);H=[]
for v in cfg['points']:
 r=v+[cfg['grid']];d=math.gcd(*r);H.append([x//d for x in r])
raw={'H':sorted(H)};a=A.run(raw);b=B.run(raw);assert J(a)==J(b);m=M.run(a)
assert [a['V'],a['E'],a['F']]==[122,183,63] and a['counts']==[1,2,1] and a['weak']==[0,0,0]
assert [a['face_primitive_zero_count'],a['vertex_max_zero_count'],a['edge_primitive_zero_count']]==[0,0,0]
assert a['stable_face_ids']==[3] and a['unstable_vertices']==[2,38] and a['saddle_edges']==[[90,118]]
assert m['tetrahedra']==240 and m['filled_first_moments']==[0,0,0] and m['common_centred_denominator_bits']==22026
expected={'RAW.json':(3084,'2a803e23c50ef6c92e2281e57b6b83eea7e79c5c9c61c98889f7490a8caad699'),'A.json':(120665,'2d646e02deaed82244ff7cc00870b341dca148ce86b553acbc29cb4ef8aaca4b'),'B.json':(120665,'2d646e02deaed82244ff7cc00870b341dca148ce86b553acbc29cb4ef8aaca4b'),'MASS.json':(223,'483df377a3860e3c848346695c7767f24dcde7300444122455ad609ac7c8a231')}
out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False)
for name,value in [('RAW.json',raw),('A.json',a),('B.json',b),('MASS.json',m)]:
 bb=J(value);assert (len(bb),hashlib.sha256(bb).hexdigest())==expected[name],name;(out/name).write_bytes(bb)
print('C366_HEIGHT100_G10_EXACT_OWN121_AB_MASS_NONWINNER_PASS',flush=True)
```

## Direction and evidence status

Full producing methods, exact upstream input recipes and finite options are in [internal-source-reference]. The parent exact C378_GLOBAL65_G9 is [internal-source-reference]. Those methods prove no universal fixed-normal exclusion. The final63-row body can now be deformed in a much smaller H-chart, with E<=183 for bounded full-dimensional intersections, leaving42 additional input halfspaces before the unconditional F<=105/E<=309 limit. However, adding physical supporting halfspaces naturally addresses S, already solved here; the remaining U basin may require outward physical additions or changing normal directions, not merely retaining this height cone.

C366's floating protected-root radius ratio to the unwanted U is only about1.009; shortening a physical escape route requires substantially changing that radial geometry or following a different route, not interpreting near-coincident endpoint dot products as a cheap link. This is a continuation suggestion, not a proved necessary bound for all deformations. C288 own211, C402 own514 and C378 own[17,1,16] retain different advantages and must not be conflated with this own121 body.
