# minimum-0019

AI research report · 2026-09-08 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# HEPTAGON_SOLE_CHILD_REFLECTION_SECTORS_V2

## Determination

**This is a partial global theorem, not a whole-type or whole-root closure and not a C30 attainer.** It replaces the former local cylinders, for the two smallest joint roots, by metric-independent exclusions of full-dimensional, unbounded shape sectors. All six admissible cap coordinates and every positive-definite physical metric are covered, without bounding the height anisotropy.

Writing the inherited core parameters as beta, tau, s, the new exclusions are:

* **graph3, parent S1/U7:** every strict realization with `(2-tau)s >= 1` is excluded for every physical metric. Independently, the entire `tau=1` slice of this joint root is excluded, including the part outside that sector.
* **graph29, parent S1/U8:** every strict realization with `tau>=1`, `beta+tau<=2`, and `(2-tau)s>=1` is excluded for every physical metric.

The proof also gives a stronger exact reflected-ray obstruction on the complete, unbounded nine-shape domain. Its complement, together with the remaining shared-height inequalities, is explicitly specified below. Two exact interior-sector controls satisfy the old height-interval obstruction's complementary inequalities, so the advance is not merely another certification of the old forbidden cylinders.

The finite prerequisites were completed: the parent's cylinder checker, original catalogue reconstruction, all 367 matrix checks, both original frontier sweeps, and the literal five-record/facet-binding audit actually ran successfully. In particular, graph29's facet map is now derived from the pinned catalogue, rather than assumed. The preceding parent explicitly withheld these execution and binding claims.

**No records are deleted globally.** The heptagonal remainder stays 3,042 records / 78 joint-root orbits. The current global journal frontier stays 178,103 / 4,366 / 74 after the unrelated patches; the reproduced original parent remains the distinct 178,131-record checkpoint. The inherited bound remains `30 <= C_min <= 1374`.

## 1. Literal dependencies, labels, and the decisive finite observation

Immutable parents, unchanged:

```text
minimum-0017
43ee13ee6deecc6dc457943f669ac92903f27e22972427a95af6bc3ca897105c
minimum-0009
6f905a98d5d84d11e1369aebb34643ad59248a2485b95270c59bb52c48b92326
```

Canonical-to-parent maps, now checked against complete ordered parent facets and ordered dual edges:

```text
              vertex map                  facet map
graph3   (0,6,4,1,5,2,3,7,8)       (0,1,2,6,3,4,5,7)
graph29  (6,0,1,3,2,5,4,8,7)       (0,1,2,7,3,6,4,5)
```

Thus canonical S1/U7 means parent `g3_s1_u7` and parent `g29_s1_u8`, respectively. The canonical maximal-facet cycles are:

```text
graph3:
(0,4,5,6,2,3,1), (0,1,8,7), (2,7,8,3),
(0,7,4), (4,7,5), (5,7,6), (6,7,2), (3,8,1)

graph29:
(0,4,5,2,3,6,1), (0,1,8,7), (2,7,8,3),
(0,7,4), (4,7,5), (5,7,2), (3,8,6), (6,8,1)
```

The complete five-record root input, with canonical parent arrays, is:

```text
record (3,1,7,29889)
primal (7,8,6,2,0,4,5,-1,3)
dual   (1,-1,1,4,5,6,2,0)

record (3,1,7,30337)
primal (7,3,6,2,0,4,5,-1,3)
dual   (1,-1,1,4,5,6,2,1)

record (3,1,7,31873)
primal (7,3,6,2,0,4,5,-1,1)
dual   (1,-1,1,4,5,6,2,2)

record (29,1,8,27304)
primal (4,0,3,8,5,7,1,-1,1)
dual   (5,-1,1,1,3,2,0,6)

record (29,1,8,27312)
primal (4,0,3,8,5,7,3,-1,1)
dual   (5,-1,1,1,3,2,7,0)
```

The last record field retains the original `<BBBH` dual-edge-mask convention. The capsule contains both literal parent facet/edge arrays and reconstructs every displayed array; it does not hard-code a presumed graph29 facet binding.

**The new structural observation is that the primal root 7 has exactly one child in every one of these records: child 0 in graph3 and child 5 in graph29.** Consequently that child must be strictly farther from the body's actual centroid than every other nonroot vertex. This is stronger than merely choosing an unspecified maximum-radius base vertex. Coverage of candidates by the parent's complementary records is inherited, not reproved by selecting these five convenient trees.

## 2. Complete shape chart and actual mass

Use the inherited chart, with nine independent shape parameters:

```text
p0=(0,0,0), p1=(1,0,0), p2=(0,1,0),
p3=(beta*s,1+(tau-1)*s,0),
p4=(x4,y4,0), p5=(x5,y5,0), p6=(x6,y6,0),
a=p7=(0,0,1), b=p8=(beta,0,tau).
```

Put `delta=beta+tau-1`, `h=1+(tau-1)s`, `k=beta*s`. The domain Phi consists of positive beta, tau, s, delta, h, the 35 strict clockwise base convexity inequalities, and all 42 strict noncontact facet inequalities. The first three outward planes are `(0,0,-1).x<=0`, `(0,-1,0).x<=0`, and `(1-tau,beta,beta).x<=beta`; the other normals are the oriented triangular cross products. This is the complete inherited realization chart, including tau=1.

For the clockwise base cycle C define

```text
S = -sum_C cross2(pi,pj),
M = -sum_C cross2(pi,pj)*(pi+pj).
```

For each b-side triangle `(i,8,j)`, define its positive actual apex-cone determinant

```text
dij = det(pi-a,b-a,pj-a).
```

There is one such triangle in graph3 and two in graph29. Exactly:

```text
D = S + sum dij,
N = S*a + M + sum dij*(a+b+pi+pj),
Vol = D/6,
g = N/(4D).
```

These are actual tetrahedral volumes and moments, not independently adjustable masses. An invertible physical map T gives volume `abs(det T)D/6` and centroid `Tg`. The body used for mechanics is `T(P-g)` throughout. This mass formula is inherited, and the new replay checks it against oriented boundary integration symbolically and against all nine apex-cone integrations at the exact controls.

Write `Z=N_z`. An important strict identity is

```text
Z-D = tau*sum dij > 0,
therefore g_z > 1/4.
```

A second actual-mass consequence, valid for every vertex c of any convex three-polytope, is

```text
(4g-pc)/3 belongs to P.
```

Indeed, cone a genuine triangulation of every nonincident maximal facet from pc. The actual positive normalized tetrahedral volumes express `4g-pc` as a convex average of sums of three vertices; division by three proves the containment. This is an actual-volume identity, not a free-weight surrogate.

## 3. Sole-child reflected-ray theorem

**Lemma.** Suppose an actual centered physical body admits a true-edge escape tree with root r and sole child c. Then the closed ray

```text
q(lambda)=2g-pc-lambda*(pr-pc), lambda>=0,
```

cannot meet `Q=conv{pj:j!=r}`.

**Proof.** Let `vi=T(pi-g)`. Every escape increases squared radius strictly, since

```text
||vparent||^2-||vi||^2
 = 2 vi.(vparent-vi)+||vparent-vi||^2 > 0.
```

Thus `||vj||<||vc||` for every j other than r,c. Every point x of the physical nonroot convex hull satisfies `vc.x > -||vc||^2`, by Cauchy-Schwarz, including the vertex c itself. But a point of the displayed ray has

```text
vc.T(q(lambda)-g)
 = -||vc||^2-lambda*vc.(vr-vc)
 <= -||vc||^2.
```

This is a contradiction. The proof allows equality in the escape shadow and allows boundary contact with Q. It uses one actual Euclidean metric after one T, not independent primal and dual metrics. Convex containment is affine invariant; mechanical classification is not assumed affine invariant.

### Exact global elimination of the ray parameter

For these roots, Q is the actual heptagonal pyramid with base C and apex 8. Its eight halfspaces can be reconstructed from C and the triangles `(i,8,j)` on every base edge; these are Q facets, not new escape edges in P.

For a Q halfspace `n.x<=h_f`, ray membership is

```text
a_f*lambda+b_f >= 0,
a_f=n.(p7-pc),
b_f=h_f-n.(2g-pc).
```

Append `(a,b)=(1,0)` for lambda>=0. Existence is equivalent to: every zero-slope row has b>=0, and every pair with `a_i>0>a_j` satisfies

```text
a_i*b_j-a_j*b_i >= 0.
```

This covers every zero-slope stratum, all contacts, and the whole positive unbounded axis. Thus ray intersection is an explicit nine-shape semialgebraic forbidden region for both complete root disjunctions, uniformly over every physical metric.

### The base-intersection reduction

At `lambda=2g_z`, the ray meets the base plane at

```text
w_c = 2g_xy+(2g_z-1)xc
    = [N_xy+(Z-2D)xc]/(2D).
```

**All base halfplanes whose three-dimensional facets contain a are automatically strict at w_c.** To prove this, write such a facet as `(m,h_f).(x,z)<=h_f` and set `sigma=h_f-m.xc>=0`. The actual-centroid containment gives `4 n.g-n.pc<=3h_f`, hence

```text
h_f-m.w_c >= (2g_z-1/2)*sigma.
```

For sigma>0 this is strictly positive. For sigma=0 the exact expression is `2(h_f-n.g)>0`, since g is interior. Therefore only the b-side base halfplanes can obstruct w_c's membership in the base.

For a clockwise base edge i->j put `m_ij=(-(yj-yi),xj-xi)`, `h_ij=m_ij.xi`, and

```text
Phi_ij(c)=2D*h_ij-m_ij.[N_xy+(Z-2D)xc].
```

A candidate must consequently satisfy

```text
graph3:  Phi_31(0)<0;
graph29: Phi_36(5)<0 OR Phi_61(5)<0.
```

Equality is excluded when the other b-side inequalities are nonnegative. These are global actual-mass restrictions on all nine shape variables; no metric remains.

## 4. Graph3: an unbounded whole-root sector

Let the six-vertex core have base `(0,2,3,1)`. Its six-volume and b-tetrahedron determinant are

```text
D0=beta+tau+tau*delta*s,
d0=delta*h.
```

Let the actual a-side planar cap `(0,4,5,6,2)` have twice-area L and moment numerator `M_A=3L*c_A`. Set `m=(h,1-k)` and

```text
T_A=2hL-m.M_A,
K0=beta*(1+tau*s)*delta*[(2-tau)s-1].
```

The exact polynomial identity is

```text
Phi_31(0)=K0+T_A.
```

Moreover **T_A>0 on the entire strict shape domain**. Triangulate the actual planar cap from vertex 0. Each positive triangle contributes its area weight times `(h-m.pi)+(h-m.pj)` to T_A; every cap vertex is strictly inside the opposite base-edge 3->1 halfplane. Hence every contribution is positive.

It follows that `(2-tau)s>=1` forces `Phi_31(0)>0`, contradicting the sole-child theorem. This proves the stated graph3 sector for all cap shapes and all physical metrics, including its equality boundary.

### Separate complete equal-height exclusion

Every graph3 record also has dual arrows 0->1 and 2->1. At tau=1 the three outward normals obey

```text
n0+n1+n2/beta=0.
```

For the actual centered physical poles `q_f`, the corresponding relation has strictly positive coefficients: `L0*q0+L1*q1+(L2/beta)*q2=0`, with `L_f=4D h_f-n_f.N>0`. Both arrows imply `q1.q0>0` and `q1.q2>0`. Taking the dot product with q1 contradicts the positive relation. Thus the entire tau=1 slice is excluded, not only s>=1.

The surviving graph3 domain must therefore obey all of

```text
tau != 1,
(2-tau)s < 1,
0 < T_A < beta*(1+tau*s)*delta*[1-(2-tau)s],
and the complete reflected ray misses Q.
```

## 5. Graph29: all caps closed over a second unbounded core sector

Assume

```text
tau>=1, beta+tau<=2, (2-tau)s>=1.
```

Put `d=tau-1>=0`, `q=2-tau>0`. Reparameterize the six cap coordinates, without restricting them, by

```text
p4=(-u,y,0), p5=(-v,z,0),
p6=(1+t*(k-1)+r,t*h,0).
```

Here y and z are planar ordinates, not heights. Strict shape incidence and convexity imply

```text
u,v,r,t>0, 0<y<z<1,
e=u*z-v*y>0,
a0=1-z-d*v/beta>0,
t<1+d*r/delta.
```

For example, the middle and last a-side noncontacts are `beta(z-y)-d e>0` and `beta(1-z)-d v>0`; the b-side determinants are `h[delta(1-t)+d r]>0` and `t*delta*h>0`. This is why t>1 cannot be omitted.

Delete vertex 6 temporarily and use bars for the **actual** mass of the remaining eight-vertex polytope. Its a-cap has

```text
L=e+v,
M_A=(-u*e-v*L, (y+z)*e+v*(z+1), 0).
```

Let `N0` be the core numerator from the mass formula, and define

```text
Dbar=D0+L,
Nbar=N0+L*a+M_A,
Wbar=Nbar_xy+(Zbar-2Dbar)*(-v,z),
Fbar=2hDbar-(h,1-k).Wbar,
V_y=Wbar_y,
B_v=2hDbar-V_y,
Astar=h*(beta+1+q*v)+q*(k-1)*z.
```

The full b-cap has twice-area `R=h*r`, numerator `M_B=R*(p3+p6+p1)`, and actual contribution

```text
D=Dbar+tau*R,
N=Nbar+tau*R*b+tau*M_B.
```

The following exact identities provide a positive-factor proof. Set

```text
K0=beta*(1+tau*s)*delta*(q*s-1),
K2=(beta+tau)*(2-beta-tau)*h,
H_A=h*(u+2)+(k-1)*y,
C0=beta*[tau*q*s*(d*s+2)-d],
B0=beta*d*(tau*s+1)*(q*s-1),
B1=2h*(tau*q-beta*d).
```

Then

```text
Fbar = K0*a0+z*K2+e*H_A > 0,
V_y-tau*h*Astar = C0*a0+y*e > 0,
B_v-tau*h*Astar = B0*a0+z*B1+(2h-y)*e > 0,
Astar = q*[h*(v+1)+(k-1)*z]+h*delta > 0.
```

The signs are not numerical assumptions: K0,K2,B0 are nonnegative in the sector; `H_A>h>0` by the core chord halfplane at p4; `C0>0` because q*s>=1; `B1>=2h*q>0` because beta<=q; `2h-y>0`; and the bracket in Astar is the strict chord slack at p5. Also `h-q*z>0`.

The two full b-side cuts are exactly

```text
Phi_36(5)=(1-t)*Fbar
          +r*[B_v-(1-t)*tau*h*Astar]
          +r^2*tau*h*q*z,

Phi_61(5)=t*Fbar
          +r*[V_y-t*tau*h*Astar]
          +r^2*tau*h*(h-q*z).
```

For `0<t<=1`, both are strictly positive from the preceding identities.

For **t>1**, necessarily d>0. Put `theta=delta*(t-1)/(d*r)`, so `0<theta<1`. Two further identities are

```text
E=B_v-d*Fbar/delta
 =(h/delta)*(2*beta*Dbar+d*Wbar_x-beta*Wbar_y)>0,

delta*(h-q*z)-d*Astar=beta*q*h*a0>0.
```

The positivity of E follows from the automatic a-facet lemma applied to the actual deleted-6 polytope and its facet 2; no independent reference center is introduced. Substitution gives

```text
Phi_36(5)=r*[E+(d/delta)*(1-theta)*Fbar]
          +r^2*tau*h*[q*z+(d*theta/delta)*Astar] > 0,

Phi_61(5)=Fbar
          +r*[V_y-tau*h*Astar+(d*theta/delta)*Fbar]
          +r^2*tau*h*[beta*q*h*a0/delta
                      +(d/delta)*(1-theta)*Astar] > 0.
```

This closes **all admissible cap geometry**, including the unbounded r direction and the t>1 branch. The sole-child theorem now excludes both graph29 records throughout the claimed sector, for every physical metric.

## 6. The remaining shared-height problem is still exact and global

For continuation retain the parent's single physical metric

```text
A=((a,c),(c,2-a)) positive definite,
G=((A,A*ell),(ell^T*A,ell^T*A*ell+kappa)), kappa>0,
H=G^(-1), not an independently chosen matrix.
```

With `B=4D`, `W_i=B*pi-N`, `R_i=W_i,xy+W_i,z*ell`, `d=det A`, `L_f=B h_f-n_f.N`, and `k_f=n_f,z-m_f.ell`, the original arrow rows are

```text
primal i->j:
a_ij=W_i,z*(zj-zi),
b_ij=R_i^T A [(xj-xi)+(zj-zi)*ell];

dual f->h:
a_fh=m_f^T adj(A)(L_f*m_h-L_h*m_f),
b_fh=d*k_f*(L_f*k_h-L_h*k_f).
```

Every row means `a*kappa+b>0`. The new source also generates all seven child-versus-other-nonroot radius comparisons, eight root-radius comparisons, and seven prescribed-stable-pole norm comparisons. These 22 added rows are necessary consequences, not a relaxation with independent metrics. There are **37 affine rows per record**, plus kappa>0. Their direct expressions in the same G and H were checked by 185 exact rational identities across the five records.

The complete strict Fourier-Motzkin elimination is, after appending `(1,0)`:

```text
for every i: ai != 0 OR bi > 0;
for every ordered i,j:
    ai <= 0 OR aj >= 0 OR ai*bj-aj*bi > 0.
```

No positive floor, finite ceiling, or nonzero-slope assumption is used. The resulting variables remain the nine shapes, two A entries, and two ell entries. Retain all inherited physical leaf/core constraints as well. The reflected-ray test is an additional shape-only obstruction, not a replacement for the actual mechanical system. The parent already supplied the underlying exact affine-height reduction.

## 7. Exact controls: progress beyond the old obstruction, and genuine remaining complement

The following controls are in the strict interiors of the new core sectors. All 77 geometry guards, the entire supporting-triple hull, boundary mass, and all nine actual-apex mass integrations are checked exactly.

```text
graph3 shape:
(1,1/2,1,-3/5,1/5,-4/5,1/2,-3/5,4/5)
minimum geometry guard=3/25
D=283/100
N=(859/500,699/200,591/200)
Phi_31(0)=1971/1000
A=I, ell=(-3/10,-6/5), kappa=1/100
old L_height=-39899/970225
old max Ui=U0=251/3940

graph29 shape:
(1/4,3/2,3,-1/10,1/5,-1/10,3/5,15/8,5/4)
minimum geometry guard=1/25
D=1803/200
N=(92803/4000,27817/1000,5481/400)
Phi_36(5)=155161/16000
Phi_61(5)=241017/16000
A=I, ell=(-4/5,-21/10), kappa=1/10
old L_height=-867672377/3004136100
old max Ui=U0=311147/548100
```

Both satisfy `L_height<0<kappa<max Ui`: the parent's old necessary height interval is nonempty. Nevertheless the new proof excludes every metric at these shapes, not only the displayed metric. These controls do not claim feasibility of any complete escape record.

The full ray test also strictly strengthens the base-plane test. At graph29 shape

```text
(2,1,1/4,-1/100,1/5,-1/100,7/10,19/25,1/2)
```

both base cuts are negative, `(-316053/200000,-318277/200000)`, but the entire closed interval

```text
599/3290 <= lambda <= 207169/467415
```

belongs to the reflected ray's intersection with the nonroot pyramid. The base-plane value is `lambda=221/282`, outside that interval. Thus this shape is excluded for all physical metrics even though the one/two base-cut test alone does not exclude it.

Conversely, the shape-domain complement of the **new** obstruction is not empty. Exact controls are

```text
graph3:
(3/4,1/2,1/4,-1/100,1/5,-1/50,1/2,-1/100,4/5)
Phi_31(0)=-383187/3200000
ray lower=168633/260650 > upper=11301/20852

graph29:
(3/4,1/2,1/4,-1/100,1/500,-1/50,1/50,4751/8000,7/16)
(Phi_36(5),Phi_61(5))=
(-730306597637/12800000000000,-1459547946601/25600000000000)
ray lower=9382760361091/14618217957480 > upper=3009733/5552916
```

They are actual strict hulls, but **are not claimed to satisfy the leaf systems, any full record, or 110 mechanics**. They delimit the reach of this obstruction; they are not attainers or feasibility certificates.

## 8. Exact remaining scope and continuation

For graph3 the remaining shape domain is restricted by the strict cap-moment budget in section 4, tau!=1, and ray nonintersection. For graph29 it must satisfy

```text
tau<1 OR beta+tau>2 OR (2-tau)s<1,
Phi_36(5)<0 OR Phi_61(5)<0,
and the complete reflected ray misses Q.
```

These conditions are necessary, not sufficient. All the remaining facet comparisons, base-radius order, full true-edge arrows, and actual-mass leaf conditions still have to hold with one G and its reciprocal H. No unbounded branch of that final system was solved here, and no new whole-root/type exclusion or C30 attainer is asserted.

The most useful continuation is to attack these explicit complementary sectors with the displayed exact mass factorizations and the 37-row shared-kappa system. In particular, graph29's tau<1 branch reverses some factor signs and changes the cap-height inequalities; it was not silently included in the positive-factor proof. The returned ray-miss controls provide exact nonempty shape test points for that work. Another box around the old controls would not address this remainder.

## 9. Recovery capsule, dependencies, and execution provenance

The entire new source is one self-contained Python unit. Its default run needs **no parent files**: literal parent facets, ordered edges, five records, maps, all exact controls, every helper, the actual-mass integrations, symbolic identity checks, ray elimination, and the enriched common-height row generator are included. An optional two-argument run authenticates those literals against the complete original catalogue and remainder.

Reference environment actually used: **CPython 3.13.5, SymPy 1.14.0**, assertions enabled. All proof calculations are rational or symbolic; no numerical optimization, random test, external SMT solver, floating eigenvalue test, or tolerance is a proof dependency. The twenty symbolic identities supplement the analytic sign proof above; the terminal marker is not a claim that an unbounded CAD solver closed a whole root.

```text
hept_global_v2.py
16022 bytes
5094f40c058a6ffc148b0f361df5dcd4aac8e0c259a0edb17750d7644c9e3aff

hept_global_v2.json
9915 bytes
0150d7003b77ec6de9aae5d7ec6794cdbe268fdc39087713575d70b2eebcbb8b

hept_global_v2_execution.txt, pinned-parent run
672 bytes
26badb25a877126ae560cc45b2d4c54dc4cf783136eb46f639a022179e2a1392

clean base85 stream
7705 bytes
cb534e1a2cfcdb0ec2ac38e8ff4ef12af5649f13015373529259d92c35935602
```

Encoding is `base85(lzma.compress(source,preset=6))`. Save the complete stream below as `hept_global_v2.b85`; ASCII whitespace is discarded. Save this complete decoder as `unpack_hept_global_v2.py`:

```python
from pathlib import Path
import base64, hashlib, lzma
b = b''.join(Path('hept_global_v2.b85').read_bytes().split())
assert len(b) == 7705
assert hashlib.sha256(b).hexdigest() == 'cb534e1a2cfcdb0ec2ac38e8ff4ef12af5649f13015373529259d92c35935602'
s = lzma.decompress(base64.b85decode(b))
assert len(s) == 16022
assert hashlib.sha256(s).hexdigest() == '5094f40c058a6ffc148b0f361df5dcd4aac8e0c259a0edb17750d7644c9e3aff'
Path('hept_global_v2.py').write_bytes(s)
print('HEPT_GLOBAL_V2_CAPSULE_DECODE_PASS')
```

Commands:

```sh
python -S unpack_hept_global_v2.py
python hept_global_v2.py
# Optional complete-parent authentication, with the parent's reconstructed inputs:
python hept_global_v2.py e15_frontier.json raven_remaining.bin
```

The default run was repeated in a fresh directory containing only this encoded stream and decoder. It reproduced the source and report hashes above. The optional input pins are:

```text
e15_frontier.json 106553
9b7354d49fa9fb07ede494140fc0cde9a06f994f0359cb0a26b6ee3e8debe833
raven_remaining.bin 890655
5d3329d312adf3db48d9e22314d6cec046f4ec9b00b29fe248fa96f699bb3f1f
heptagonal order-preserving filter 15210 / 3042 records
c02fe56b8c0aaecd0c0cd13098723327c81ead01ea2a103c13df8d43a1aa71bd
```

Observed markers, also the expected markers for replay:

```text
HEPT_GLOBAL_V2_CAPSULE_DECODE_PASS
PINNED_3042_RECORDS_AND_FIVE_ROOT_RECORDS_PASS  [optional parent run only]
BOTH_LITERAL_FACET_MAPS_AND_SOLE_CHILDREN_PASS
SYMBOLIC_MASS_AND_SECTOR_IDENTITIES_PASS 20
STRICT_AND_CLOSED_FM_ZERO_SLOPE_UNBOUNDED_CASES_PASS
EXACT_INTERIOR_SECTOR_CONTROL_AND_OLD_HEIGHT_COMPLEMENT_PASS 3
EXACT_INTERIOR_SECTOR_CONTROL_AND_OLD_HEIGHT_COMPLEMENT_PASS 29
SAME_G_INVERSE_185_ENRICHED_HEIGHT_IDENTITIES_PASS
RAY_STRICTLY_STRENGTHENS_BASE_CUT_AND_BOTH_COMPLEMENTS_NONEMPTY_PASS
REPORT_BYTES_SHA256 9915 0150d7003b77ec6de9aae5d7ec6794cdbe268fdc39087713575d70b2eebcbb8b
SOURCE_BYTES_SHA256 16022 5094f40c058a6ffc148b0f361df5dcd4aac8e0c259a0edb17750d7644c9e3aff
HEPT_GLOBAL_V2_EXACT_REPLAY_PASS_NO_WHOLE_ROOT_CLAIM
```

The earlier parent prerequisites were separately observed, not merely expected: `CYLINDER_ALL_POSITIVE_KAPPA_PASS 3`, the analogous graph29 marker, `COMMON_G_INVERSE_AND_120_SHADOW_IDENTITIES_PASS`, both actual-mass/cylinder markers, `ALL_367_SHIFTED_PD_IDENTITIES_AND_TWO_FOUR_DEEP_MATRICES_PASS`, sweep counts 97,118 and 81,013, the 178,131-record recovery marker, and both original parent-binding audit markers. The exact extracted checker hashes are:

```text
verify_height.py 6818
097883867beefcc0bb8b3fff9fd969aa7084c1bbd3040cbb8b8c9e6e909d4fca
audit_parent.py 4162
79df690e1b792dda8a6d801891e5dbc4f8e3f9c71611e4add6f5d632516c0f38
binding_execution.txt 1225
603a36b00f05b7e0953d84d030904c6c964ad130bd15b359f6007f144bee2641
```

Source-file provenance: the supplied 2,037,143-byte journal has SHA-256 `bf80a0a493e910b5d483656dc811684a27394abe587d45cfa0055dcbb76e3095`. The rendered height-parent extraction is 32,446 bytes / `4e43bdc228ec1c93934378a66c9ce963dfe90b9e3f9b4236c4df3b2f69f2bc3d`; the rendered frontier-parent extraction is 43,477 bytes / `b073e42c222c9c578aaae909d64c18b1abd1a1385cc5fb2b52f733713db34e44`. These rendered-byte hashes do not reproduce the immutable envelope hashes, and are not substituted for them. No mathematical facet, vertex, incidence, or root alias conflict was found.

Convenience copies: complete recovery archive (`HEPT_GLOBAL_V2_recovery.zip`), decoded source (`hept_global_v2.py`), exact report (`hept_global_v2.json`). The archive is 25,535 bytes, SHA-256 `78b435bea7b422a4282269836f5c641491a0725bdb05dc308e9dfd88e88186fa`; these links are supplementary to the complete capsule below.

### Complete encoded source

```text
{Wp48S^xk9=GL@E0stWa761SMbT8$j;69ZX(_H{F9Eu`ut-S81YrLGNKhJ0vJ7ZPg1?c7<C`w1o8NH~g75W(s5ijukA*|~@FhN2)
Ks+U_TEo>(mDZN*{R^;eP9ae0^c9wfu$+mdoy)~|cqQ|v#P%+qqCfv^{V0ky<l`P0N!z3x3*SGVe^x}b?VqF;_S-sU^?2ic<i*r`
3<_V^)fMXjSS<~2DyL2n;xWzUIobB?4pf$%b>dLkIW-W2TWUAkN#g3?uZqhj$M(ZbiW%%gohv|{F>CRVgT1>dCcrAAP3GGOHy0}7
T$DNt*$V`xP`8MDI2@K}?t?_CQPfuyYts$khDrs!5`5Z)%gS(LABrk)*aM#^Arvv6E!3)8e@>L8Ky3|tDN{HFC$s@;<HB%mg{!|4
Vcf4XC)p&A!sasLLGMKtt8w;K-EsTBBQXiwep57A8`9B6&LU}uKOOEyjO=s~D+&#7e8I>)uCjCZo`w<e6?2%LMzDku%uA$<B>E0v
DBlSRT#tvWoG7gGHmfs*rU_)1Y8I?1v0LCWT?y@bggKYon|a<Z_KBI_%v2Qrpl*J_p%6EQl1lRFLhXQ+2N4Qia2VFQBi2xA36a>r
BMr&m9dD@LTz~tjW||Y>)c*4zngXV5%1;BR=FAt9!}-YgZs4m!DUGWa?{(7&nngXcP+^a~1B%&>Uy>1A&*{hLyD7X85uQC3J5m^Q
&)5}1?sqJh8xZA%E<h*0Kr9ouuD0_DC)brQO%glLlz#O6isv7bA{+vU$k^N<6Oxvl4X46g)@}_8CirawPhH;{_sX&M4V!azZOE&2
xq~^tvDnR-=Mr{8jE$e-+9l6Cb3`x~kL(%bhU*M3X{cru8leeb3>ye&enGc|3TQcd(eM$O2FkYBa*cG2j5O2+bQCJGukjLYxmI>I
5N&_2EQM+Nxrp_94Dq6QWO^p04rm+Qxl{bSOVFg~$B&>2)g!_o*c=Ut@@N*<3jAP>AtF6Ykt-{gbcDasvgTWX3vLn^6|q9OhXbaM
1U?#12myBxoRn&V!Wm!EaH)#7+rSsQPD|r-@2u+=_LKiP&1Od{v0|+@BVvsu6oz3keCWq*;Kh3#kvXGq0fu{#Fp)=@0XGo(*X0&T
nCAdK70{`EOi2i6@h(A`#Vwo`AlLK7D<eMe)(n5Zux>hEKl;%j6?~ifFO5a^p~r&vM-!o$M(t>wEJIx9jBF6k#e=Z(k6<V&FYrQD
XvhlvD_Z^KJ_*<|LKV*4xoP*i6XyHah%WuZn?VWb5J)4@eQ@XAJ(Q<nx(R++4dc}=jqyVQ$O}4xHAWfVqu5|^HEjDaVdn-G%SWwC
Tks0<(@5z%Io7nnB3b<zSgqTcvRB;e`_j5Vr0KC(A<u_)y2uB<Z#F6wcg={d?(wdhO8o0#xC1-a$lHVU$zXRiNHbX;@5Im5eP#U~
$6^c8#XO9BOaqM`!N?^%zA8JS^`4SUm#+tA5FlUBP+QG(6t7huJfzqqTc|14U7%w4P0_&EfF9ZYK@xtVBE$b1av8dqulVqhoT3R+
RYBs_lOjiy2sw!_Je26uZ=TVT5*qknKL=-qCvH#vQgo4WSuK67xu>9*KDh6lMvEX5F&D;DwPsElz5|MxbM=Z~PxAS}I+lg#!0-Vf
{Z`4}snxOBY0_~tJ;)SBOtdsav;s~R)A*Hg5~`WFM$vrTKP<tWd(eFncwz4l1v*p7H$E=RNt$*}*#+XBldzuVOS|lxjvwv-^U^Fv
knw4AC)WPn=zDvtR~RcK9F@hONX1A#9cAj7nyJCzc33u{ic2%$_>dynVjcNW2hJV==c){FEX$$aYW#*9mpC?RLD)vs;h7(LY`7eF
IqcC9FreQN3V1X(s}Xvcq~!&$=FDpuAwv~9$m$6u_opII(S4{Q`UJi73`iu_JqotrNX*;Vd2be-xszrY!h$?U9R>SM`(BsH!>#~<
sp3z>&4}3QGq^#xK!w_6{X=gZ$^Z(cm;bZq9dZ&-jwG*KY~~xpEwgp-9r`^qz<p+}lczleGp^i=ZW=Sqbt!%!LlrQt2q|T#Y~V^4
*pNYlc@2=Ht3DBOvuaQFr0^5)KZVm8U_H1Y=+VL`UjIS-;tkEN0JL3PBra5k4Z#@fogWmvsR;X)U~UN7&o^TfxJXg*EVdA=1}TSD
{S#+Ito-{|`Y%p-$cDuhj0{AUP*!KOZkt9bKd^s^0a)<5I1G`dx7AP8bOPTRT{;v02(x3AB_Th+J%U*SSddDQ0U^mhjl*LCf4IrX
bn6!0aHT9hw;;xp?N1CZ@s<)^Q_1`lhkKwZYCFe`rt^A6JugYomhR)!Op$vqs0_jQs7Edd;qz~p21{|-Z+KSRctQm9>3JMb?#|>R
q#uK}3#)!ErQAoLvqP10g`wlH>gIHie@x$=Ia;gj6ZG=DmdgfceBC!C7p<Nqz!C4(yS5}^NZ@Q99u&fxAL}+;cAs_Fce$~?Mq831
1c<v#tyzwthQe|&AW=S#7}HJKFPTk`m;Uojk5t+@dz7>asVtt|T;@K9(<B#8t5)2qTHi861Y+@QqCbV)*T>a%4c!t~daIVPsFFf*
euZ2MRG?gW+r5W`<N;5-zcVh`9q<=_6(+(pU3*Lg|AROtg6brj<`Vum3jp?WCa(uSu^LyOh%H|7sexe2cnOcVz=l0V)huv^rzxe<
cRzvHe2aw6tD8jqZQ7`gT{Q2%#lM>$@Z*sTjV`}&6F3W9h^GLsi@kV43Z`5~N)SFr5>XEGJuo8z5y*W9y*a4vSU#U7@&y(62}<-) 
Y4F&L>9m|R;{dcSF*a042J>Y<iv*%(11`!{A?hZijCvHH2?Q8QH^pZ@zP5_>{Ca?A!k+A;;B_d$8&IVIZhZWF>=Oo*%<e<V<{Hfa
j)<BMeAjU9*ZQHz&~?p)h~!6$TB^@9z9wsRxvt=4YdjcV6Ff`ANGeFs*3u%oEPh4=`oAJz)d68$^mjaE&dE$jxkLR-jRyA3hKv;q
$YP+F9Meu6w*X>y(0^qGKKPyE%!?3~qHKim`hUpy*^pN4`@%owBn2Sxcqu<(c0Q6vBF{b4YptJ=-Y>7=I73^i`I$lwobB!)bD<mB
VUo?S<LbaN!P**UjO*#D$xSd&j!FRvV$7#o|CQzZJ!I;0E7P4`d4?Q3?y9HZxFUfv?ZEazPoTf8lD|0MQ{}@3L1OP#)C>RtNa1X4
fl99&V|owAS;5rdDRKYC>CuQqIQCczAv@~}#IYekQ2a_@#I6NV4X@adPw~r0?_f1H**3qC2x^YJwF?c)sYEF-oU<GmJqwf{aPb}}
2WBMHPfWZ^s82(2(sKLoxl+Z@kAZt++T1EzkhC-%fv7!#LiE?9dth9%@u>XBq=DA3<z8x48~&&Ozx^uip~M}a#)Ai{;6JVfopJwZ
0}Y<znK&YRob@QQ#&usg(@nvSFd35!E7Ns80%&lQR1*fCQ9%K0rSlR?m)KT+7c6>LBU>Io(d~+7cnIkSI%~}yOMsjkt{Jnv`lOFY
T}10J0B+5lwA1Sst1VI&;`xrP$Zg3XP_|~$jNI@*er>nS7BvxSd8LJ7q9u3tFh6-+{?;2~xu3A#_$v!{3|2KCP3f#GZIhmWB;t8m
!>howTBF3fne1kYN3uY!rI<pW*;uLJ<XUrdf-;1mv~{gVV;my;3W)@{)$Y#3`-Rv_2;vlx=yrW(ggY*%R`M*V7V0eqv3|Ai3^1r|
cvtqo5n}LpYY6d#ChnZazXAJ)U{waP%gX)VVn_RZ7GnAkMJUaw{;IMosY#Y(B%b(VLpf*}mxX#^#iBmEWTsHI!!DmMgZOZE8Zr+E
5}AU=?VaV6WX&)xPCi27iNeoyWg9{A0GP-8!5)=&8pb|Eei}K0Wh1-=$GA3cLjWy7hrZ+}q@xIsA#x=08bVyirY1Gca>^&$_PD`5
EU8ofLfNE9?Ix=|kAl1ND)b^(oNS35>;uurfQp3O*TL?;8s8Bkg*;bSkS++^xUM6>6otR*sbFGQvkV1JTciz&!fp|6MaE4yEHfa(
w%%C(F$i=XkLv5^(d`8bhilX@I%AOXpR73d=<|Ed0JUNif?2+~@sd6dicZmq3AxX%jI<6wsb{k&y~8#)bxgNrn4q4a6Lvlo%i!N2
yp_p}M|F`wgV!H2?YIpf%y_2F<u>3ucY&asg#zWR3YcFr;rV(i$K&ml!4XHFbq--zJD&VB?N*<vU@&q0AmeNgNMZEDr5xX3ihvfr
OhZGiuqW5@ecwA`QvCvN3z>b;+SYk)o#ckho`Q6;uUbnVEpf(y&2Vj9yiL5?#sG|fMt{txjI3H*Gkp*jm-Urujhi&6U%>v#VWHzG
IfqV$zWDwx$9#F2pNIDCplpdx;5y2?s0%IQeKRjuyR>y_6EGC=4@+S%FNEN8gF5Xx&Ut!;8WuAEsGlCyTnmQvb?S@biRrnM@hC!n
<-`XdHskGta1c>65$8|mDrS&(Y^6!ppVbW0o!qZ)dz*@a`5GG3?wrfk7`;)TodqzV3lxQVxfP&5ke{CSyyszH&0$H^6hR~`)}vs<
KdBm^9^;aB!h;d}6HXzk#F9TC)=16|XyPttOJsgZ-$v5;u7^JL-C!Z!Sys`I`x!e35FLv6u)6;DOT!re=O05SXKXRqS*v!2F77Lc
6f3;?;r@%Kr9*BGG=>r>61pFLy0@lQmp9V2S>*x%0keAl@^`Mja#&|gArUA*=*ZVn-bv84*w1+xyPoOsmP>0;G`B0%)oC^s%cxJ7
X=9nd4=;RNj(DZoO0`|qow}ew2`E!mV=QnE7#eS7{Qn)f@G5Y2kx3)akDq4ZPwfD7R9cDU!k8;kE<4mSl=?fccNwNUg%JL?*<RAh
u^*M!f@qFI=_@}8q1<*uxD0EHPGy)Id;<hBWjw9m%S<2B>)n`CnJR4&Z(pwDodeKkF}7WxSB#Zk2*rsbh1Tk!I<I{~lKe2YZL-v}
ltd*+rXYRPh_!Fm17|=~xnB-=Iq<YZw}JPK_Kj3~rf{|*>Yg-pa22A}-Lu5Hl|r1KbFJtXTTTbOsL@rzLCg5nT{w%MDEi3Xk|81!
kpN&kva*6_A;!WeB0}?_uMBDLFY(k<vjWd&FjuUW=K94YBZO3)qrE~3_xP;ggrJ8)m$wGR1nL6u#qh~n?`e-Bts)7X9GBvJSll7h
e_zmJW9WO9n%mo%>$%`2(e4aS@m56nAvsEScy~W#7Lw~-hOLRR4-cf8;R(wHES(>e&?6%d&Wa4%32OJ_kviA{Qcyz(ayXXyTm9&k
=D<#C^1Rj}J7(7_7JaeA=4*dG#*{d#ua-c%Hiw?TVz|KA9aK)zEqYrHkOjKR#s0>=)22sFr7EHo+-z!y&rExw;j`kmhOYbNs3AC_
FKLPvU?w*8;YpLF99WT@NxsY-?^{|T3rSXRPrn!EuaB2t3s)R3&P`J7k5kV1WP!cPc%nH$s|}ffzC*Pt$j;}{ABVOQX+3iHczq~?
^!}OhDZ^(vCP9c*s~gH+f9x^z<uVEQy6sY1#SiszbS4%0m`&Ryj=#A@?%CArWnm-iHQ1LdtrE!Bj?*Rb7OI)|aW<6uILepMcrpS#
X9nREDe=3oSgJ4D@Wngf2kK@#Hy%s+i6OZXmmii7&6EZ8Q5_}=`@>Z;^|HzOf0T;yP349#4{A{K-rJ<LS!4W|$EOJO7}&Q-Io_Oe
2qqQvISaar{^v0%cuJl{UA9}~L0v;)ll<SW<QVCu`LWWm_W~9qI*V?xS>R0eIf2Qwpb^DSq)%c|eqgJ8<UsTX6SVYI#$q;;?TF{|
0!NqyK{FAN_1Wqx5*2C@EOj~B(T(5vvx;#Tzg$4&L)-;N*kd<>>|jr%Izu_>3QuLLj0a!r+v=NJ({xwu6s2mAjI^RO@g-jVo)TAW
QXL17W<#>)%0~oJpYGv-b+Z4FB-M+xO+tdTCeP4Ic>L7xk2N@{`su{(FnB`a0{k{||8Medb)DJSy8K1C<%{C}zQDs^_djwREqU7(
xCSq({)lpL)M7fkNTwTMWH5kG#X=5>9rYPVKGH)z$Zm$`3J!6TGgg;5dyKS%Uem6by%BlOw>?A+SNtGcj)_PAb2XDZSh-b=tfS0Y
QXS8H+pRbWx|_kvo{}hO!!rQ|IyzaiQhJC^l}3aLD=tcmQ4Q!8d^4{>{5=e7cwc(zz+?JHeq`;=jWY_pNRs2@u%N*~>WvxxFzNib
g|oFq+pH-q^DVWW+jR!fIO0LNg3bfqF%~CBjHYBoEsT>$N`53eJ<a<4V;IN(-L<LWE$ADB;De$``FgS5fDXK+?bT338S+Ch@Gx=%
c4nhZCH*<F<Qt@yU+~}pDt;a1(}Zj`f6@d@_S9M&onNePN8V&H^Iv>_Xa)MW1L4aE;TG#B*I9_e(*?0n$f-F1nbmFwn9I@9>&%wL
llSQ6mdfrOK+piN-4r5Ce;nG*G4Ji~izLzMJ#y%M8-!3+@ispwmQc|FKeBIXK#8p+VX8wsKiOg7KTB)2cbIPYXAy_egO0;f4rTiH
i7Axi7l3wHn6lyTC^!%dLv>36RxIIku@hT05JF6r8DJjE?22a7=O8IDr0&~pLGE*y-XTB9K|j)xXox3?A}7vcmYT&U;f5L1SbSf~
`2E6ig}%2BdXo_R8|%-Z(#6_fYZ%w#4H;FxAI}eVL8Th0Le>MR=d_$Qg9#P0oPxPOp5_0d?Byl6tL;`#UE@Y5s`gKDnY*%mG#|EB
nBtA&SkJM&5Mh5?b&aM-DxJTDl}BvM+c5V)H?sJAATuHW{(3o$RIE6wS=&}e9PnOU?Z)1JQxfMnX<kB1`tI^*=PO%UH#bI_KGE%;
oraKQ1@Xj3zi~v7VkNC1$BgNb{9Ed_u^UEtVNCws;fdQddr0nX<p$(77)oWdue;@k;uC&yFCdp(NSA3Em}-?lW~DAp^t}Z@gD_Zs
FE5-Ha2BELO<>I0bK}F1lxlE5%U=bnK&GG^@Gb%*TEBUFp$`U+f(a?7xQNa9AgW>55#`IuV|#6d-pkn<uFC5j^c}?eGVU;8q>xJO
?yUSLx$~cq&H8r3dkMW%ed-s%A>_|e+cH<tseHt^=9Rxmi{?KK=n+*34FoB5v+K)Gv>-!7x>Pw&6w5<1B)U4&BvSd~fBk|{j;<`}
iv0KJC<KD<zqA~9KcMo!CeKrrm1sA|q!QAx0O%s+bT^9zgAd{PR+y!rj)P87HQT6JNX7pa;)%gVT)#TA9rTvro8JiJjalth^)4|S
pXaep5w)y3$%M`L(pa!9TI1*E$`b`yS^^U*pHGx|zNvpJAx0+<$xJ%RkU(MdZS|mvCfFivML$G%fS;EqoY)8^A{eB)p?E_9Y~l9h
LU7qGP0QgfYbPrO0%@3p2JJ0c$eYIy3xX}v|0~|Hhr}Y|R7>3W7%NOeyjWOpz0AUSV8m~UdQAuERZ~BqlHAT(>Srq}0Exq@(YOA&
c6$*{Y>Q&hmAUE0+t1P6p_-?1Ixc6muzt5xd)Epz%ruIZ4M9~S3V=B~PY;nf=8)qYYMr+Do&c?eq4W|T3}nosokDkz=o@UhO~lQ!
TFPWA0VJTKa4Uku+6o5>T?<7b3h{rL@u>~L&XT#sYN1c*M5(Ihp<_msm|#SDsk|p?-nTA>7{c9h*~N$4A_cT`lkyw(AR@`Nb~I!Y
SO#gz^E%5RCxY0Vu6Y*?qQ+=JorIh9o}N?~&}-=3S%pm~Nps99yh$6uqq8t6Ii~c*#JIJrvNj=c7bAIeHZOn~W$-?U|8Zt*q=DO5
^$4GmQ6V<fh*_ZVyg?e-cik>|U0H#bjp_mZtkSW*#sw<AoJF$m_;n_CP>bY5H>%Mnu4{*jyZrZ}^XNgqaPNvUV*G1tf=b;1>B7}8
syHII#m=2O9TaJ~Z`+n!#Wj{BW#rKnpk^aD0O=xHQ8E0o6j(vbvj;x*nI0mV9@_u_juw-o+!zxD00HkWmVE#KB!JYTvBYQl0ssI2
00dcD
```
