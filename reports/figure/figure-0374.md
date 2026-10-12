# figure-0374

AI research report · 2026-09-15 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Nimble Harbor72 — opposite-side mass compensation and a two-maximum gate

## 1. Status

**No new own-filled-volume-centred strict(1,1,0)/weak000 construction is promoted in this handoff. The accepted positive level remains C624.** The newly explored numerical and rational checkpoints have not been tied to a completed, self-contained successor capsule with an unambiguous parameter–geometry–audit correspondence. They therefore remain **ephemeral**, and no new full census, arithmetic-cost table or cold-replay claim is attached to them here.

The completed mathematical result below is a finite-family obstruction for an opposite-side, single-point mass compensator. It explains an important failure mode of the new C592 branch: restoring the old filled centroid can preserve the old apex as one strict unstable equilibrium while making the compensating point a second, strictly farther unstable equilibrium. This obstruction does not depend on freezing the compensating point’s normal fan, or on a numerical optimizer failing.

Also preserved is the exact quadratic moment system for a single exterior-point augmentation. It treats the actual uniformly filled convex hull, not a point-mass approximation. Together, the moment system and the obstruction distinguish a solved mass equation from a solved Gömböc construction.

## 2. Coordinate identity and last durable body

The relevant coordinate body is the coordinator’s **COORD_C602_EXPOSED_CHAIN5_G1E12**, whose actual edge complexity is **C592**, despite C602 appearing in its name. Its defining parent is Bright Quartz13’s **BQ13_C602_TRIANGLE9_SADDLE_CHAIN_OWN121**, from immutable result `figure-0371`, metadata SHA-256 `839d1b5d10cbab600329c6736fd8faf5ecc6aced33ba7c140efe56c1f9d8011b`.

The Vivid Quartz20 result `figure-0372`, SHA-256 `229ac6a4cb1686c4804b05cb53dafc811656428174fe773f5d0dc0bee71a4db3`, supplies the full-contact, actual-filled-mass correction mechanism only. Its C626 coordinates and four-contact incidence are not substituted for C592.

Let P0,…,P166 be the C602 parent’s exact raw Cartesian-lex vertices. The C592 body K is their convex hull together with the following four points, with denominator10^12:

```text
P167 = [-652386830976,-278549019006,-59994875610]/10^12
P168 = [-673052036488,-291747836672,247470117785]/10^12
P169 = [-570437000458,-249889387058,566581053189]/10^12
P170 = [-339758403441,-150071123912,838060234941]/10^12.
```

The parent input apex is **P85=(0,0,1)**; its C592 raw-lex index is81. These indexing domains must remain separate.

The established C592 result has actual **V163/E296/F135**, own strict **(17,26,41)** and weak000. At the old C602 exact filled centroid c0, used solely as a reference, its complete census is **(5,1,4)**, weak000, with unique U at P85. The five links `[7,167,168,169,170,85]` are true exposed edges. Eight old input vertices `[0,1,2,3,4,5,6,8]` are hidden. This leaves15 additional true edges before E312; a successful body must have E≤311. These are established parent results, not new constructions in this handoff. 

The complete durable upstream recovery units are:

```text
FOUR_FRONTIERS_EXACT_CORE_20260915
encoded b85:25865 characters
SHA ec0ad716235628338a7c3c6d371de170e30bd6184ae039c9b13eff096984c929
decoded:71405 bytes
SHA 50061fcdfeb6cc42de880bfe1805441e4ed8cf3df4a2c78d6cbd9cf079496d19

C592 six-source extension
encoded b85:7095 characters
SHA f9ee5fc1060be31f8694da3c1bab3ef93c24ee992f2a2149db65a2ebce758c26
decoded:15925 bytes
SHA 57d0644b73858349341fad8f3f55fd83a00c4485efef5d0cdc49afb9b5a16320.
```

Their full literal payloads, not merely these hashes, are in the journal’s three core entries and the C592 entry at2026-09-15T15:13:05.937Z. No new replacement coordinate capsule is asserted here.  

## 3. Exact filled-mass equations for one opposite-side point

Let K be the fixed, full-dimensional C592 body containing the origin, with normalized supporting planes

`q_f·x≤1`.

For each outward maximal facet, triangulate its polygon only for integration. For its triangles `(u,v,w)`, define

`f_f = Σ det(u,v,w)/6`,

`b_f = Σ det(u,v,w)(u+v+w)/6`.

Here f_f is the volume of the origin-based pyramid over the facet, and b_f is three times that pyramid volume times the facet’s area centroid. These are rational expressions in the actual physical coordinates. Integration diagonals are not true edges.

For a new physical point a, define

`Q(a)=conv(K∪{a})`.

Inside a strict visibility chamber, let

`S={f:q_f·a>1}`.

The visible-facet pyramids partition the added material, up to measure-zero boundaries. Hence the actual uniformly filled volume and first moment are

`V(a)=V_K+Σ_{f∈S} f_f(q_f·a−1)`,

`M(a)=M_K+(1/4)Σ_{f∈S}(q_f·a−1)(f_f a+b_f)`.

In particular, **volume is affine and first moment is quadratic in a within a fixed visibility chamber**. The density of Q(a) remains uniformly1; no mass is concentrated at a.

Set

`k=Σ f_f q_f`,  `k0=−Σ f_f`,

`B=(1/4)Σ b_f q_fᵀ`,  `b0=−(1/4)Σ b_f`,

where all sums in this paragraph run over S. For a prescribed target c0, the true moment-closure equation is

`F(a)=M(a)−c0V(a)=d+La+(1/4)a(k·a)=0`,

with

`d=M_K+b0−c0(V_K+k0)`,

`L=B+(k0/4)I−c0kᵀ`.

Its exact Jacobian is

`DF(a)=L+(1/4)[a kᵀ+(k·a)I]`.

Thus a candidate can be isolated by three quadratic equations and a rational box, provided the entire box remains in the same visibility chamber and an interval existence-and-uniqueness proof completes. That would establish actual mass closure. It would still not establish110.

The full-contact method remains relevant after this coarse compensation: every subsequent physical contact change must differentiate the same filled V and M and use `dg=(dM−g dV)/V`. Preserving a reference-centre escape forest while ignoring this derivative is not an own-centred repair. 

## 4. A two-maximum obstruction that does not freeze the new point’s star

### General lemma

Let K be a convex polyhedron, c0 an interior reference point, and r its unique strict unstable vertex, with no additional weak unstable vertices. Then r is the unique farthest vertex from c0.

Indeed, every vertex v maximizing squared distance from c0 is strictly unstable: for any other vertex w,

`(v−c0)·(w−v)=(|w−c0|²−|v−c0|²−|w−v|²)/2<0`.

Consequently, a second farthest vertex would be a second strict U.

Now add a point a such that

`|a−c0|>|r−c0|`,

`(r−c0)·(a−r)<0`.

The first inequality makes a the unique farthest point among all vertices of Q(a), hence a strict U. The second preserves the strict supporting normal r−c0 at r: it was strictly supporting against every old vertex and is also strictly supporting against a. Thus r remains a different strict U.

**Therefore Q(a) has at least two strict unstable equilibria at c0. If its actual filled centroid equals c0, it cannot be an own-centred110 body.**

This argument permits arbitrary visibility changes as a varies. It requires no prescribed degree, no pairwise-acuteness condition on incident rays, and no assumption that the old facet complex is preserved.

### A robust finite box for the C592 opposite-side actuator

Take r=(0,0,1) and the rational actuator box

```text
17/20 ≤ a_x ≤ 9/10,
43/100 ≤ a_y ≤ 47/100,
−57/100 ≤ a_z ≤ −27/50.
```

Assume the exact target reference centre obeys

`||c0||∞≤1/50`.

The published numerical readout of the C602 parent centroid lies comfortably inside this cube; the reusable exact test below explicitly checks the actual rational components rather than treating the decimal readout as a certificate.

For each old vertex x≠r, define

`δ_x=−(r−c0)·(x−r)>0`,

and set the exact rational radius

`ρ=min(1/1000, min_{x≠r} δ_x/(2||x−r||₁))`.

The established unique reference U makes every δ_x positive. Thus ρ is strictly positive and completely determined by the durable C592 data.

Consider any point a in the actuator box for which the **actual uniformly filled centroid c of Q(a)** satisfies

`||c−c0||∞≤ρ`.

Every old vertex has distance from c0 at most the distance of r. Also

`|r−c0|²≤2603/2500<(1021/1000)²`.

The centre displacement has Euclidean norm at most `sqrt(3)/1000<2/1000`. Therefore every old vertex has distance from c less than1023/1000.

On the other hand, `||c||∞≤21/1000`, so every a in the actuator box satisfies

`|a−c|² ≥ (829²+409²+519²)/10^6 =1123883/10^6`.

The old-vertex upper bound is

`(1023/1000)²=1046529/10^6`.

The strict squared-radius separation is therefore at least

`38677/500000 = 0.077354`.

So a remains a strict U throughout this family.

For the old apex and the newly added point, a uniform rational bound gives

`(r−c)·(a−r) ≤ −147889/100000 <0`.

For every old vertex x, the definition of ρ gives

`(r−c)·(x−r)≤−δ_x/2<0`.

Hence r remains another strict U.

**Conclusion:** any single-point opposite-side augmentation in this explicit actuator box whose actual filled centroid returns to the stated ρ-cube has at least two strict U. Exact mass closure to c0 is a special case. No calculation of S or H is needed to exclude110 once these two distinct strict U are established.

### Scope

This is an exclusion of a particular augmentation family and actual-centroid region. It does not exclude:

- changing old physical vertices or supporting planes so that the old apex loses its supporting normal;
- replacing the new point by a genuinely different cap or chain whose points need not lie in the actuator box;
- changing the physical metric;
- obtaining a different own centroid outside the stated region.

It is not an exclusion of the C592 realization space, and it is unrelated to the old K99 fixed-interface energy barriers.

## 5. Exact method unit

The following complete standard-library program computes the visibility-chamber moment system and the exact radius ρ from the two established audit records. It does not declare a new body accepted. Its inputs are the C592 A-record and its C602 parent A-record generated by the already journaled source-only replay. It also checks the universal rational constants in the preceding proof.

The point argument is a rational proposal, not an asserted verified successor:

```text
a=(-652386830976,-278549019006,-59994875610)/10^12
```

is already a C592 chain point and is not an opposite actuator. For the new opposite-side trial, the distinct intended proposal row is

```text
a=(874577931702,454209162144,-558471315966)/10^12.
```

Only the latter belongs to the obstruction box. Keeping the two roles separate prevents a support/physical-point or chain/compensator alias error.

Save the complete unit as `opposite_mass_gate.py`:

```python
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

assert __debug__, 'Run without python -O'
sys.set_int_max_str_digits(0)

CHILD_SHA = 'd200af2491ba532cd9307caceb4d780e9a661a4c9094da10e4e0c3562875204d'
PARENT_SHA = '2426da394eda9520bd30b2b8b3e1f00d043697353bb6bc73658f5983653c11ec'
TRIAL = (Q(874577931702,10**12),
         Q(454209162144,10**12),
         Q(-558471315966,10**12))


def add(a,b):
    return tuple(x+y for x,y in zip(a,b))


def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))


def scale(t,a):
    return tuple(t*x for x in a)


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def determinant(a,b,c):
    return dot(a,cross(b,c))


def checked_json(path,expected):
    data=Path(path).read_bytes()
    assert hashlib.sha256(data).hexdigest()==expected
    return json.loads(data)


def encoded(x):
    if isinstance(x,Q):
        return str(x)
    if isinstance(x,dict):
        return {k:encoded(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):
        return [encoded(v) for v in x]
    return x


def run(child,parent):
    P=[tuple(map(Q,row)) for row in child['raw_vertices']]
    normals=[tuple(Q(v,h) for v in n)
             for n,h in zip(child['normals'],child['offsets'])]
    c0=tuple(map(Q,parent['raw_centroid']))
    r=(Q(0),Q(0),Q(1))
    assert r in P
    assert max(map(abs,c0))<=Q(1,50)
    assert (child['V'],child['E'],child['F'])==(163,296,135)
    assert child['counts']==[17,26,41] and child['weak']==[0,0,0]

    # Exact supporting-normal test at the old reference centre.
    radii=[]
    r2=dot(sub(r,c0),sub(r,c0))
    for x in P:
        if x==r:
            continue
        e=sub(x,r)
        delta=-dot(sub(r,c0),e)
        assert delta>0
        assert dot(sub(x,c0),sub(x,c0))<r2
        radii.append(delta/(2*sum(map(abs,e))))
    rho=min([Q(1,1000)]+radii)
    assert rho>0

    old_r2=Q(2603,2500)
    assert old_r2<Q(1021,1000)**2
    old_shifted_r2=Q(1023,1000)**2
    new_r2=Q(829**2+409**2+519**2,10**6)
    assert new_r2-old_shifted_r2==Q(38677,500000)>0
    apex_dot_bound=Q(21,1000)*(Q(9,10)+Q(47,100))
    apex_dot_bound-=Q(979,1000)*Q(154,100)
    assert apex_dot_bound==Q(-147889,100000)<0
    assert Q(17,20)<=TRIAL[0]<=Q(9,10)
    assert Q(43,100)<=TRIAL[1]<=Q(47,100)
    assert Q(-57,100)<=TRIAL[2]<=Q(-27,50)

    V0=Q(0)
    M0=(Q(0),)*3
    face_data=[]
    for cy in child['faces']:
        W=Q(0)
        S=(Q(0),)*3
        for j in range(1,len(cy)-1):
            a,b,c=P[cy[0]],P[cy[j]],P[cy[j+1]]
            w=determinant(a,b,c)
            assert w>0
            W+=w
            S=add(S,scale(w,add(add(a,b),c)))
        f=W/6
        bf=scale(Q(1,6),S)
        face_data.append((f,bf))
        V0+=f
        M0=add(M0,scale(Q(1,24),S))
    assert V0==Q(child['ordinary_volume'])
    assert M0==tuple(map(Q,child['raw_first_moments']))

    visible=[]
    k=(Q(0),)*3
    k0=Q(0)
    B=[[Q(0) for j in range(3)] for i in range(3)]
    b0=(Q(0),)*3
    V=V0
    M=M0
    for f,(q,(vf,bf)) in enumerate(zip(normals,face_data)):
        gap=dot(q,TRIAL)-1
        assert gap!=0, 'Trial lies on a visibility boundary'
        if gap<0:
            continue
        visible.append(f)
        k=add(k,scale(vf,q))
        k0-=vf
        b0=sub(b0,scale(Q(1,4),bf))
        for i in range(3):
            for j in range(3):
                B[i][j]+=bf[i]*q[j]/4
        V+=vf*gap
        M=add(M,scale(gap/4,add(scale(vf,TRIAL),bf)))
    d=sub(add(M0,b0),scale(V0+k0,c0))
    L=[[B[i][j]+(k0/4 if i==j else 0)-c0[i]*k[j]
        for j in range(3)] for i in range(3)]
    value=add(add(d,tuple(dot(row,TRIAL) for row in L)),
              scale(dot(k,TRIAL)/4,TRIAL))
    assert value==sub(M,scale(V,c0))
    J=[[L[i][j]+TRIAL[i]*k[j]/4
        +(dot(k,TRIAL)/4 if i==j else 0)
        for j in range(3)] for i in range(3)]
    return encoded(dict(
        status='EXACT_OPPOSITE_BOX_GATE_AND_CHAMBER_MASS_FORMULAS_PASS',
        reference_centroid=c0,reference_root=list(r),
        actual_centroid_cube_radius=rho,
        squared_radius_separation=Q(38677,500000),
        apex_against_new_point_upper=apex_dot_bound,
        proposal_only_point=TRIAL,visible_supports=visible,
        chamber_k=k,chamber_k0=k0,chamber_B=B,chamber_b0=b0,
        closure_d=d,closure_L=L,closure_value_at_trial=value,
        closure_J_at_trial=J,
        trial_ordinary_volume=V,trial_raw_first_moments=M,
        trial_own_centroid=scale(1/V,M),
        trial_mass_is_exactly_closed=(value==(0,0,0)),
        new_endpoint_promoted=False))


if __name__=='__main__':
    if len(sys.argv)!=4:
        raise SystemExit('Usage: python -S opposite_mass_gate.py C592_A.json C602_A.json output.json')
    child=checked_json(sys.argv[1],CHILD_SHA)
    parent=checked_json(sys.argv[2],PARENT_SHA)
    result=run(child,parent)
    Path(sys.argv[3]).write_text(
        json.dumps(result,sort_keys=True,separators=(',',':')),
        encoding='utf-8')
    print(result['status'])
```

The displayed terminal string is the program’s specified successful marker, **not a claim that a new completed replay of this final method unit was observed in this handoff**. The source makes all numerical binding and exact-centre tests explicit. The analytical obstruction itself is proved above independently of executing this unit.

## 6. What remains unresolved

The opposite-side single-point route separates two gates:

1. A finite exact solution of the three true quadratic moment equations can restore the target filled centroid.
2. Such a restoration inside the specified actuator box and centre region necessarily leaves two strict U.

Consequently, higher precision in the same mass root cannot turn that family into110. A successful continuation must change the physical geometry that retains the old apex, replace the opposite point by an exposed ascent-cap geometry, change the physical metric, or reach another actual-centroid region. A formal chain or a reference-centre U count alone is insufficient: its exposure, true-edge cost, added volume and all new stable faces must be checked together.

The new trial point and any intermediate projective/metric or contact-correction outputs are not presented as durable successors here because their complete final source–parameter–report binding and cold replay have not been closed in this response. In particular, no claimed118/243 or other new f-vector should be inherited from an unbound intermediate report. The last durable coordinate parent for this branch remains the fully journaled C592 body with own(17,26,41)/weak000.

No successful own110 endpoint, exhaustive exclusion of the full C592 realization space, or minimum-complexity theorem is claimed. No search belowC32 was performed.
