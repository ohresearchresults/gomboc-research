# material-4daaf444955b

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Radius-ordered escape bound, exact implementation, and numerical errata

This is a coordinator mathematical result and reusable exact method, NOT an own110 construction. It continues branch [internal-source-reference]-. The three W51_STACK424 recovery units [internal-source-reference], [internal-source-reference], [internal-source-reference] remain the complete exact construction input and interval program. Their source code and advertised source/output hashes are unchanged. This material corrects several numbers in coordinator prose and adds a general bound which does not have the counterfamily's local-loss pathology.

## Corrections: literal regenerated files take precedence over compacted prose
The literal 32-row W51_ROBUST_G3 input in capsule part2 has exact volume10865185711/1500000000, approximately7.243457140666667, NOT534976657/120000000. Its exact centroid is[-386613615871/10865185711000,-3857015486057/21730371422000,57133873364297/173842971376000]. It remains V31/E87/F58,C174, strict211, weak000, primitive000, Q=.7827432115794241. No coordinate row was changed to obtain this correction.

The actual T6.audit.json (15274bytes, SHAe328282214d70936e141e0463811de1e4aaed5f8809e50469be8af6d6bab7c87) has P=[8.52350600103285e-14], Q=[.7827427941285544,2.5404807769576437e-11,4.677777063671518e-18]. The different T6 figures in earlier capsule prose/branch memory were compacted-summary errors and are superseded. The exact generator and its actual hashed output were correct. All five grids remain V32/E90/F60, strict424, weak000, primitive000. Their actual main bars, in increasing k=2,3,4,5,6, are:
P=[8.501803533872741e-6,8.521322484720498e-8,8.523289463756342e-10,8.52348631443525e-12,8.52350600103285e-14].
Q main=[.7793110752136112,.7823330734373575,.7827015388348808,.7827390377282688,.7827427941285544].
At T6, raw P loss=8.312562499665334e-13, raw Q loss=1.853935177180864e-21; cosine P loss=8.52350600103285e-14, cosine Q loss=5.977222383775926e-11. These converge to zero while the interval theorem still proves Q>43/56. Its correct certificate remains2973 sign records, degree<=8, delta=92097297554728442267067614728413760140823011800502046681/620699302727971710640470954959122086455729813942160229729936.

## Ordered-escape theorem
Let L be any bounded full-dimensional convex polytope with origin strictly inside, and let z_i be its distinct genuine vertices. Sort them by increasing pair(||z_i||^2,i), so ties have an explicit acyclic order; let r be the last vertex. For every i other than r define
m_i=max over j later in this order of z_i.(z_j-z_i)/||z_i||^2,
d_i=max(0,-m_i), epsilon=max_i d_i.
Every nonessential squared-radius superlevel persistence bar on the boundary of L has relative depth at most min(1,epsilon/2). Consequently it is also bounded by min(1,sqrt(sum_i d_i^2)/2).

Proof. Choose for each i a maximizing later vertex j. Write R=||z_i||^2, D=||z_j-z_i||^2>0, g=z_i.(z_j-z_i). The radius ordering gives D+2g=||z_j||^2-R>=0. If g>=0 the whole segment has squared radius at least R. Otherwise its minimum occurs at t=-g/D<=1/2 and equals R-g^2/D. Thus its relative radial drop is g^2/(DR)<=(-g)/(2R)=d_i/2. Iterating the strictly later indices reaches r, with nondecreasing vertex radii. From any starting peak of squared radius B, the entire polygonal chain therefore stays outside the open ball of squared radius (1-epsilon/2)B. If this threshold is positive, radial projection of the chain onto the boundary of L is continuous and can only increase radii, since the original segments lie in L. Hence the starting component joins the retained root before a larger relative drop. For epsilon>=2 the capped bound1 is trivial. Equivalently, the usual edge-superlevel model has the same connected components: on each convex polygonal facet the squared-radius upper set can connect its boundary arcs exactly as in the polygon outside a centred disk. Thus the bound applies to the exact P/Q bar calculation used in this research. The argument does not assume general position or absence of weak equilibria.

A sharper computable version minimizes the direct segment's relative drop over all later j for each i, obtaining b_i. Then every bar is <= beta=max_i b_i <= min(1,epsilon/2). The implementation below checks these inequalities exactly against the complete hull P/Q audits on each input.

Apply this theorem separately to K-c and its polar, where c is the actual uniform-volume centroid. Unlike unrestricted raw or cosine losses, the ordered loss cannot tend to zero while a P or Q basin remains bounded below. In the shallow-stack counterfamily, the highest member of the collapsing polar cluster cannot select a slightly lower nearby vertex as a counterfeit escape; it must choose a genuinely later vertex.

## Exact acceptance threshold, distinct from quantitative proximity
For rational tau>0, the sum across BOTH primal and polar nonroot vertices of max(0,tau-m_i)^2 being strictly less than tau^2 implies every m_i>0. Each nonroot then has a strictly positive radial escape witness, hence is not even a closed weak unstable equilibrium. The maximal-radius root is strictly unstable: by Cauchy-Schwarz every distinct point has strictly negative radial dot product from it. Apply the same observation to polar vertices, which represent primal facets, to obtain exactly one strict stable facet and no weak stable facet. A weak edge equilibrium at an endpoint would induce a weak vertex; one on the boundary of its normal cone would induce a weak facet. Both are excluded. The polyhedral equilibrium index identity S+U-H=2 then gives H=0. This is a sufficient own110/no-additional-weak test, not a claim that the current inputs pass it. It does not assert that every primitive expression at a non-equilibrium feature is nonzero; full primitive audits remain available and required for a promoted final construction. The positive-tau implication is also valid for unrestricted witnesses; ordering is what adds the uniform persistence bound at zero margin.

## Exact examples
Baseline W51: ordered Q maximum deficit1.9056146951019017; direct-chord bound .9350334585835974; actual Q .7827432115794241. T6: ordered Q maximum deficit1.905614787752659; direct-chord bound .9350333062713829; actual Q .7827427941285544. Thus the ordered deficit stays large on the previously deceptive family. Its P direct bound equals the actual P bar8.52350600103285e-14. A finite initial Adam run with ordered loss did not obtain110; it was a search experiment, not a theorem of exclusion.

## Complete exact source and reproduction
Requires exact_audit.py from recovery part1. Save the following as ordered_escape.py, LF with final newline:3244bytes, SHA7378c1241c2c9134d25ba1e876d96f0b38bddaf06c5796ffdfa171964412c5f8. Python3.13.5 standard library only. T6 input is reconstructed using the unchanged three-part capsule. Commands:

    python -B -S stack_family.py stack_exact --powers 2 3 4 5 6
    python -B -S ordered_escape.py stack_exact/T6.input.json T6.ordered.json

Expected terminal: ORDERED_ESCAPE_EXACT_PASS W51_SHALLOW_STACK_T_1_1000000 [4, 2, 4] P 8.52350600103285e-14 <= 8.52350600103285e-14 Q 0.7827427941285544 <= 0.9350333062713829.
T6.ordered.json:30612bytes,SHA67a48896b2851cb275b4cbb4adb6821081992d87463fdd234f5c4997f7deac39.
For baseline reproduction, construct W51_ROBUST_G3.json by json.dumps({'denominator':1000,'name':'W51_ROBUST_G3','points':POINTS},sort_keys=True,separators=(',',':'))+'\n', with POINTS imported from stack_family.py. It is565bytes,SHA6fc87990d1c2eff68da3297b39ad3ea51df64ceb78978bd69870fca14e86b414. Run python -B -S ordered_escape.py W51_ROBUST_G3.json W51.ordered.json. The latter is14743bytes,SHAdf7df67b11046325b43397bcbcf0273d69b4e38e1569adffcb9a6e3f3fcc06b2, terminal ORDERED_ESCAPE_EXACT_PASS W51_ROBUST_G3 [2, 1, 1] P 0.0 <= 0.0 Q 0.7827432115794241 <= 0.9350334585835974.

```python
"""Exact radius-ordered escape bounds on primal/polar persistence.
Requires exact_audit.py. Standard library only, Python 3.13.5.
Run: python -B -S ordered_escape.py INPUT.json OUTPUT.json
Both bound tests are exact Fraction comparisons, never tolerance certificates.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json,sys,hashlib
from exact_audit import audit,dot,sub,mul

def landscape(z,actual_bars):
    r=[dot(v,v) for v in z]
    order=sorted(range(len(z)),key=lambda i:(r[i],i));rows=[]
    for k,i in enumerate(order[:-1]):
        candidates=[]
        for j in order[k+1:]:
            d=sub(z[j],z[i]);dd=dot(d,d);g=dot(z[i],d)
            assert dd>0 and r[j]>=r[i]>0
            w=g/r[i]
            # With nondecreasing endpoint radius, a negative derivative gives t<=1/2.
            t=max(F(0),-g/dd);assert t<=F(1,2)
            drop=(g*g/(dd*r[i])) if g<0 else F(0)
            candidates.append((j,w,drop))
        jw,w,bw=max(candidates,key=lambda row:(row[1],-row[0]))
        jb,wb,b=min(candidates,key=lambda row:(row[2],row[0]))
        defect=max(F(0),-w)
        assert b<=bw<=defect/2
        rows.append(dict(vertex=i,raw_witness=jw,margin=str(w),defect=str(defect),chord_witness=jb,chord_depth=str(b)))
    eps=max(F(row['defect']) for row in rows)
    loss=sum(F(row['defect'])**2 for row in rows)
    beta=max(F(row['chord_depth']) for row in rows)
    actual=max([F(bar['depth']) for bar in actual_bars]+[F(0)])
    assert actual<=beta<=min(F(1),eps/2)
    return dict(root=order[-1],actual_max_bar=str(actual),actual_max_bar_float=float(actual),ordered_max_deficit=str(eps),ordered_max_deficit_float=float(eps),zero_margin_loss=str(loss),zero_margin_loss_float=float(loss),raw_persistence_bound=str(min(F(1),eps/2)),direct_chord_bound=str(beta),direct_chord_bound_float=float(beta),strict_escape_test=all(F(row['margin'])>0 for row in rows),rows=rows)

def run(data):
    res=audit(data['points'],data['denominator']);D=data['denominator'];c=tuple(F(s) for s in res['centroid'])
    p=[tuple(F(v,D) for v in row) for row in data['points']];x=[sub(p[i],c) for i in res['vertices']]
    q=[]
    for f in res['facets']:
        n=tuple(f['normal']);h=F(f['offset'],D)-dot(n,c);q.append(mul(1/h,n))
    ans=dict(name=data.get('name','unnamed'),V=res['V'],E=res['E'],F=res['F'],strict=res['strict'],additional_weak=res['additional_weak'],primitive_zero=res['primitive_zero'],P=landscape(x,res['P']),Q=landscape(q,res['Q']))
    if ans['P']['strict_escape_test'] and ans['Q']['strict_escape_test']:
        assert res['strict']==[1,1,0] and res['additional_weak']==[0,0,0]
    return ans

if __name__=='__main__':
    if len(sys.argv)!=3:raise SystemExit('usage: ordered_escape.py INPUT.json OUTPUT.json')
    source=Path(sys.argv[1]).read_bytes();data=json.loads(source);res=run(data);res['input_sha256']=hashlib.sha256(source).hexdigest()
    Path(sys.argv[2]).write_text(json.dumps(res,sort_keys=True,separators=(',',':'))+'\n')
    print('ORDERED_ESCAPE_EXACT_PASS',res['name'],res['strict'],'P',res['P']['actual_max_bar_float'],'<=',res['P']['direct_chord_bound_float'],'Q',res['Q']['actual_max_bar_float'],'<=',res['Q']['direct_chord_bound_float'])
```
