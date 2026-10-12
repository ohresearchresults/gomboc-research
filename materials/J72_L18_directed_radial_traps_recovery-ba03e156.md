# material-ba03e1568818

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J72 — finite interior-block radial traps in exact L18

This complete runnable source extends the J71 recovery capsule, not a new own110 body. Required exact dependencies are BOTH J71 parts: [internal-source-reference] (l18_exact_points.json) and [internal-source-reference] (rootpair_exact.py). This material supplies the complete additional source trap_exact.py. All three materials together reconstruct the exact computation without the originating sandbox. No SciPy or other external dependency; observed Python3.13.5 standard library.

## Theorem and physical scope
For any nonempty proper vertex set B of a convex polyhedron with actual homogeneous centroid g, suppose every actual edge from B to its complement satisfies q(v,w;g)=(v-g).(w-v)<0 in the outward direction. A vertex of maximum squared radius in B is strictly unstable: for an internal neighbor w its score is at most -|v-w|^2/2<0, while external neighbors are covered by hypothesis. A separate retained strict unstable vertex6 gives U>=2.

Frozen cross-edge endpoints satisfy q(v,w;g)<=q(v,w;g0)+epsilon*|w-v|_1 whenever |g-g0|_infinity<=epsilon. Thus these certificates permit arbitrary finite motion or retriangulation of every listed interior vertex, not merely one-ray motion, a fixed interior star, or infinitesimal perturbations. Retain the fixed cross-edge endpoints, with no new cross-edge outside the certified list, and the original6-star with its endpoints fixed. The resulting body must remain convex and its ACTUAL homogeneous centroid must remain in the stated cube. Other changes are allowed only if these same conditions hold. Boundary motion, new crossing edges, or leaving the cube are NOT excluded, and absence of a matching certificate is not proof of success or feasibility.

P20 is the original positive-P component, with20 vertices,10 boundary and10 interior. P21 adjoins65, giving21 vertices,10 boundary and11 interior. Both certify U>=2 for actual-centre drift<=1/20. P21 interior=[34,37,41,44,48,50,52,54,55,58,62]; freeing BOTH58 and62 does not escape this retained-cut family. The limiting cross edge is22->13, with exact threshold23978704849772661895190984552183/432698373667668648338310640000000, approximately.05541667431407857.

ATTRACTOR53 consists of the53 vertices that cannot reach6 by a path of positive q edges in the original exact L18 graph. Its35 boundary vertices leave18 interior vertices [26,30,34,37,38,41,44,47,48,49,50,51,52,54,55,58,62,65]. It certifies U>=2 for drift<=3/100. Hence additionally freeing49/65 still leaves this larger cut obstruction. Limiting port42->6 has exact threshold1221845821996372785089217995201143/35271019534162365633872116560000000, approximately.03464163605514529. All original cross-edge scores and actual homogeneous reference-centre fractions are reconstructed exactly. In particular the53-set is NOT a paraphrased alias of a different old component.

These are new conditional finite-block exclusions. They are not a global impossibility claim about L18 descendants, changed cuts, or C<500, and do not establish any new construction. Together with J71 they distinguish changing a local peak from changing the basin interface. A coordinated root-neighborhood/interface deformation remains scientifically open.

## Recovery and observed output
Extract the complete Python unit below, including one terminal LF, as trap_exact.py beside the two J71 source files. Run:

    python -B -S trap_exact.py --input l18_exact_points.json --out trap_exact.json

Expected terminal markers:

    L18_DIRECTED_TRAP_EXACT_PASS P20 B 20 boundary 10 interior 10 eps 1/20 threshold 0.05541667431407857
    L18_DIRECTED_TRAP_EXACT_PASS P21 B 21 boundary 10 interior 11 eps 1/20 threshold 0.05541667431407857
    L18_DIRECTED_TRAP_EXACT_PASS ATTRACTOR53 B 53 boundary 35 interior 18 eps 3/100 threshold 0.03464163605514529

Exact UTF-8/LF identities:
- l18_exact_points.json:2357B SHA90d0a3e009fe9a0ff5bef092a8ad6ac9071fa7d1242bb3cdc82b43531aa1f0f6 (J71 part1).
- rootpair_exact.py:12447B SHA6db7a6739614e3a9318f9e12700874e1f05415fd718008edfe06c8aca3f44887 (J71 part2).
- trap_exact.py:4274B SHA16c72934d09c9fa26acbf50d2739c6211e8d6be0ce69f336c9b74061d46576f8 (below).
- trap_exact.json:21637B SHA81ae7b30fc677f2fddd9370eb757b03f1e27c883090f2351b60d8c72f4b7ded5 (generated exact fractions, cuts, sets, scopes).
The coordinator actually ran the source and reran it with --out trap_replay.json, reproducing the same21637B/hash. This is replay of the same exact engine, not independent physical verification. Earlier transient context-summary numbers4344B/30042B and boundary34/interior19 were erroneous: the literal runnable source and these observed outputs govern.

## Complete trap_exact.py
```python
"""J72: exact directed radial-trap certificates for finite L18 patch motion.
Requires complete J71 rootpair_exact.py and l18_exact_points.json.
python -B -S trap_exact.py --input l18_exact_points.json --out trap_exact.json
The geometric lemma and scope are in the output; all original signs are exact.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
from fractions import Fraction as F
import rootpair_exact as r

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',default='l18_exact_points.json');ap.add_argument('--out',default='trap_exact.json');args=ap.parse_args()
    data=json.loads(Path(args.input).read_text());p,D,P,faces,edges,nb,c=r.exact_hull(data)
    audit=r.census(P,faces,edges,c);assert audit['strict']==[2,2,2] and audit['primitive_zero']==[0,0,0]
    x=[r.sub(v,c) for v in P]
    def q(i,j):return r.dot(x[i],r.sub(x[j],x[i]))
    out={i:[j for j in nb[i] if q(i,j)>0] for i in nb}
    can={6}
    while True:
        nxt=can|{i for i in nb if any(j in can for j in out[i])}
        if nxt==can:break
        can=nxt
    B53=set(nb)-can
    B20=set(r.full_bars(x,edges)[0]['component']);B21=B20|{65}
    assert len(B20)==20 and len(B21)==21 and len(B53)==53
    six=[(-q(6,j)/sum(map(abs,r.sub(x[j],x[6]))),j) for j in nb[6]]
    assert all(t>0 for t,j in six)
    results=[]
    for name,B,eps in [('P20',B20,F(1,20)),('P21',B21,F(1,20)),('ATTRACTOR53',B53,F(3,100))]:
        assert 6 not in B and 62 in B
        cut=sorted((i,j) if i in B else(j,i) for i,j in edges if (i in B)!=(j in B))
        boundary={i for i,j in cut};interior=B-boundary
        # No interior point is a neighbor of6. Thus if only interior points move,
        # retaining the old6-star fixes all its endpoint coordinates as required.
        assert not (interior&set(nb[6]))
        cert=[]
        for i,j in cut:
            qi=q(i,j);l1=sum(map(abs,r.sub(x[j],x[i])));assert qi<0 and qi+eps*l1<0
            cert.append({'edge':[i,j],'score':qi,'l1':l1,'drift_threshold':-qi/l1})
        assert all(eps<t for t,j in six)
        lower=min(cert,key=lambda d:d['drift_threshold'])
        item={'name':name,'vertices':sorted(B),'boundary':sorted(boundary),'interior':sorted(interior),'cross_edge_certificate':cert,'centroid_cube_halfwidth':eps,'limiting_cross_edge':lower['edge'],'limiting_drift_threshold':lower['drift_threshold'],'vertex6_drift_threshold':min(six)[0]}
        results.append(item)
        print('L18_DIRECTED_TRAP_EXACT_PASS',name,'B',len(B),'boundary',len(boundary),'interior',len(interior),'eps',str(eps),'threshold',float(lower['drift_threshold']))
    # A moving block wholly inside any certified interior cannot remove all U
    # while retaining the specified cross edges/6-star and centroid cube.
    controls={}
    for name,M in [('root_pair',[58,62]),('root_pair_plus49_65',[49,58,62,65]),('root62_and_saddle',[13,22,62]),('root62_saddle_and49',[13,22,49,62])]:
        controls[name]={'moving':M,'traps_whose_interior_contains_block':[d['name'] for d in results if set(M)<=set(d['interior'])]}
    answer={'centroid':list(map(str,c)),'traps':results,'blocks':controls,'lemma':'For any nonempty proper vertex set B, if every edge from B to its complement has q(v,w;g)<0 in the outward direction, a maximum-radius vertex of B is strictly U: internal-neighbor scores are <=-|v-w|^2/2<0. If a separate vertex6 is strictly U, then U>=2. Frozen cross-edge endpoints give q(v,w;g)<=q(v,w;g0)+epsilon*|w-v|_1. No fixed interior triangulation or local support cell is required.','scope':'Allow arbitrary finite motion or retriangulation of the named interior, with the original cross-edge endpoints fixed and no new cross-edge outside the certified list. Retain the original6-star with its endpoints fixed. The homogeneous centroid of the actual resulting convex polyhedron must lie in the specified closed cube about g0. Changes elsewhere are permitted only if these same conditions hold. New edges crossing the cut, moving boundary anchors, or leaving the cube are not excluded. Absence of a matching trap certificate does not prove success or feasibility.'}
    Path(args.out).write_text(json.dumps(answer,sort_keys=True,separators=(',',':'),default=str)+'\n')
if __name__=='__main__':main()
```
