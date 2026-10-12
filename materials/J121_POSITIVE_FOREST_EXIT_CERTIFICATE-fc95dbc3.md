# material-fc95dbc358a6

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J121: a root's best outgoing target belongs to its own positive forest

This is a scoped mechanism for the exact proxy counterexample in [internal-source-reference], not a new110 construction or an obstruction to all moving geometry. A new exact integer computation proves, at both C270 own222 endpoints and on both primal/polar landscapes, that the deficient root's best angular outgoing target has precisely one positive outgoing chord: back to that same root.

## Complete exact evidence
The inputs are J121_PAIRED_RELAYQ_G8, fully recoverable from [internal-source-reference], and J121_ROOTGUARD_RELAYQ_G10, fully recoverable from [internal-source-reference]. Each exact115 audit uses the actual homogeneous centroid and true hull. That exact hull/mass engine is the source in [internal-source-reference]. The complete proxyseparation121.py in [internal-source-reference] identifies the exact maximal angular outgoing target of each junior U root; physical S facets give the polar U roots. New source below then checks ALL exact outgoing signs from that target, not only its edge neighbours.

Actual exact results:
- Parent P: deficient root62, best target53; the only positive outgoing chord from53 is to62; no zero chord to any other point.
- Parent Q: deficient root31, best target32; the only positive outgoing chord from32 is to31; no zero chord.
- Child P: deficient root56, best target52; the only positive outgoing chord from52 is to56; no zero chord.
- Child Q: deficient root31, best target32; the only positive outgoing chord from32 is to31; no zero chord.
Labels belong to each exact auditor ordering. They are not assertions of material-point identity across deformations. These are scalar sign comparisons on existing exact geometry/mass, not an independent second physics reconstruction.

## Why this particular root objective cannot close its fixed policy
For distinct points u,v relative to the same centre,

u dot(v-u)+v dot(u-v)=-|u-v|^2.

Therefore preserving v dot(u-v)>0 forces u dot(v-u)<-|u-v|^2<0. The attempted new root arrow u->v cannot become even weakly nonnegative while the positive return arrow v->u is retained. In angular normalization the current root score is strictly less than -|u-v|/|u|. A collision u=v is a geometric/incidence event, not a strict positive-arrow completion in the same distinct-point policy.

More generally, a directed cycle x_0->x_1->...->x_m=x_0 satisfies

2 sum_i x_i dot(x_(i+1)-x_i)=-sum_i |x_(i+1)-x_i|^2<0

when at least one consecutive pair is distinct. Thus a directed cycle of strictly positive outgoing chords is impossible. Every positive chord also strictly increases squared radius, so a finite positive-witness graph with one outgoing edge at each nonroot is a forest flowing to its roots.

If an unwanted root u is given a new outgoing target in its OWN existing forest component, while all old forest arrows on the target-to-u path are retained, the proposed arrow closes a forbidden cycle. A usable root escape must instead enter another root's forest component, or first change an outgoing witness along that return path. With exactly two roots on one landscape, a positive root arrow into the other component completes a one-root forest on that landscape, provided every other required arrow remains positive. When both current primal and actual-centred polar forests are so completed, and the exact hull/census has no weak degeneracy, this is the desired structural direction toward110. No feasible simultaneous geometry or edge-budget theorem for such rewiring is asserted here.

## Interpretation of the executed J121 rootguard trials
Their linear models chose each nonroot's maximal positive angular witness and each deficient root's maximal, still negative, angular target. At the two exact endpoints above, the target's unique positive arrow returns to the deficient root. Consequently the currently preferred root objective asks to close a cycle in the very policy it protects. The optimization may still improve the negative angular score, as the exact scalar comparison already demonstrated, without eliminating a basin; both persistence depths actually increased in that comparison.

This is NOT a global exclusion of dynamic-witness continuation. A full finite deformation can change the target's outgoing policy, change forest ownership, change the stable carrier or the elder, or pass through a legitimate incidence replacement. Nor do endpoint sign checks establish that the same return pair held through every floating trial. They identify a concrete local obstacle and a next useful event: select cross-component root witnesses, or explicitly release/reorient the return branch, rather than ranking all negative outgoing scores without their forest ownership. This proposed forest-exit continuation has not yet been implemented or executed.

## Complete source cyclecertificate121.py
1928 bytes; SHAd61ec8bfb1eb494fc54b5e4becd61783c617b024fb6ebbed45569d8a70a4cdcb. Save including its final newline. Required complete code dependency proxyseparation121.py3296 bytes,SHA0756e8f5711e52eb814c2bad9c7580f95c39c98be281c9b7da7ad3a8ebaef95b, is in [internal-source-reference]. Python3.13.5 standard library only.
```python
"""Exact return-witness check for the J121 proxy counterexample.
Needs complete proxyseparation121.py, the two H inputs and their exact115 audits.
This scalar check does not independently reconstruct hulls or uniform mass.
Python3.13.5 standard library only. All signs below are integer signs.
"""
import json
from pathlib import Path
from proxyseparation121 import vector,dot,score

records=[]
for stem in ['J121_PAIRED_RELAYQ_G8','J121_ROOTGUARD_RELAYQ_G10']:
    data=json.loads(Path(stem+'.audit.json').read_text());sc=score(stem)
    gn,gd=vector(data['centroid']);raw=[vector(v) for v in data['vertices']]
    lines=Path(stem+'.txt').read_text().splitlines();_,D=map(int,lines[0].split())
    nn=[list(map(int,s.split())) for s in lines[1:] if s.strip()]
    qn=[nn[k] for k in data['active_input_planes']]
    qh=[D*gd-dot(n,gn) for n in qn];assert min(qh)>0
    for side in ['P','Q']:
        root,target=sc[side]['root'],sc[side]['witness']
        positive=[];zeros=[]
        points=raw if side=='P' else qn
        for k in range(len(points)):
            if k==target:continue
            if side=='P':
                nj,dj=raw[target];nk,dk=raw[k]
                v=[nj[t]*gd-gn[t]*dj for t in range(3)]
                direction=[nk[t]*dj-nj[t]*dk for t in range(3)]
            else:
                v=qn[target]
                direction=[qh[target]*qn[k][t]-qh[k]*qn[target][t] for t in range(3)]
            s=dot(v,direction)
            if s>0:positive.append(k)
            elif s==0:zeros.append(k)
        assert positive==[root] and not zeros
        records.append(dict(body=stem,side=side,deficient_root=root,best_outgoing_target=target,targets_positive_from_that_target=positive,zero_targets=zeros))
out={'records':records,'marker':'J121_EXACT_BEST_BAD_WITNESS_HAS_ONLY_RETURN_ARROW_NO_110'}
Path('cyclecertificate121.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
```

Executed command: python cyclecertificate121.py, after reconstructing the two exact inputs and audits and extracting proxyseparation121.py. Every assertion passed. Output cyclecertificate121.json994 bytes,SHA0b2724764696dff7ac328fd63aa81b830ae390cc461d295385d9bcd0b2a7e085. Observed marker: J121_EXACT_BEST_BAD_WITNESS_HAS_ONLY_RETURN_ARROW_NO_110. All evidence is recoverable from these explicit materials without the originating sandbox.
