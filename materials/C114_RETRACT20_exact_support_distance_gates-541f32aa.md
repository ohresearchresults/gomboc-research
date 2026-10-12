# material-541f32aaa6cf

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# C114_RETRACT20: exact support-persistence radii and actual centred displacement

This is a new scoped obstruction calculation, not an own110 body or a global family exclusion. It applies the whole-support-bar mechanism from the fully read Sharp Finch90 result figure-0444, SHA caa76e093d11dd6a4a2e3b6b9c2172fac9b3cbe768a3faedb549b3f22f00c66b, to the distinct lead TURNOVER/RETRACT20 rootinput20 family. None of SF90's body labels, centroids or incidences are inherited.

## Geometric argument and scope
For a convex body K centred at its own uniform-volume centroid, form Q=K-polar without independently filling or recentering Q. A finite positive polar squared-radius elder bar has birth b and death d, with b>d>0. Under the radial correspondence between the sphere and Q's boundary, rho_Q(u)=1/h_K(u); the support minimum associated with the younger component has height alpha=1/sqrt(b), and its merger height is beta=1/sqrt(d). An older component has a minimum no higher than alpha. Define Delta=beta-alpha and eta=Delta/2.

Suppose another centred convex polyhedron L satisfies h_K-a <= h_L <= h_K+b0 on every unit direction, where a,b0>=0 and a+b0<Delta. Choose a level strictly between alpha+b0 and beta-a. The younger basin and an older basin both contain points below this level, while the original separating boundary remains above it. Minimizing h_L inside the younger basin and in its exterior gives two distinct local minima, both away from this boundary. These are strict facet equilibria: for a positive polyhedral support h=max(v_i dot u), at a local minimum the tangential projections of the active vertices must contain zero in their two-dimensional interior. Otherwise a separating tangent direction has all active first derivatives nonpositive; if the maximal derivative is zero, the negative second derivative -h along the great circle makes the support decrease for sufficiently small positive parameter. Inactive vertices have a strict gap and cannot prevent that decrease. Interior containment of zero instead means the support foot lies in the relative interior of a maximal facet, and gives strictly positive directional growth. Thus S(L)>=2, even without assuming weak-free L.

The exact graph bar paths/cuts used here are those of the already reconstructed maximal polar boundary. Its squared-radius superlevel components have the same connectivity as the true-edge superlevel graph: on each planar convex facet, the sublevel region is a disk intersection, and every superlevel component meets the facet boundary; interior connectivity adds no connection absent along its superlevel boundary. Consequently the complete edge cut certifies the separating support basin, not merely a local edge-score defect.

In particular, Euclidean Hausdorff distance d_H(K,L)<eta excludes S1. The distance is taken in the same physical coordinates at the respective actual centroids, with no extra rotation or rescaling. This is a local necessary-displacement bound, not the optimal exclusion radius or evidence that feasibility holds outside the ball. For a retained-parent addition K subset Lraw, let delta=d_H(K,Lraw) and g be Lraw's actual volume centroid in K's centred frame. Then h_K-|g| <= h_(Lraw-g) <= h_K+delta+|g|, so delta+2|g|<2eta excludes own S1 regardless of the number of additions or incidence changes. The mass, not a free choice, determines g.

For rational b,d and epsilon>=0, epsilon<eta iff q=1/d-1/b-4epsilon^2>0 and q^2>16epsilon^2/b. This supplies exact rational comparisons and integer bisection; the resulting interval is (lower,upper], not [lower,upper).

## Executed exact results
TURNOVER_G4 eta is in (252190560401,252190560402]/10^12. Its closed own-centred Hausdorff ball of radius 25219/100000=0.25219 excludes S1.

RETRACT20 G6/G5/G4 eta intervals respectively are (247462330265,247462330266], (247463284454,247463284455], (247471264095,247471264096], all divided by10^12. Each therefore excludes S1 throughout the closed centred Hausdorff ball of radius1237/5000=0.2474. Their exact own census remains211/weak000, not110.

Matching all21 input-labelled centred vertices gives a convex-combination witness in BOTH Hausdorff directions. The square root of the maximum matched squared displacement lies respectively in [21061110523,21061110524), [21058014111,21058014112), [21080069437,21080069438), all divided by10^12. These are enclosures of an upper certificate, NOT exact Hausdorff distances. All three distances are strictly below211/10000=0.0211, far inside TURNOVER's two-stable neighbourhood. Maximum matching displacement occurs at input1. Thus the previously established >7.169% full TQ decrease does not approach cancellation in this physical support-distance sense. The raw support exclusion radius falls by only about1.875%, and it remains substantial. No scalar percentage is a completion score.

The distinct G3 rounding control has own277/weak000, eta in (247743823689,247743823690]/10^12 and matching-upper interval [20890150500,20890150501)/10^12; its six extra unstable/saddle pairs are not ignored. These coarse values must not be transferred to a211 endpoint.

## Recovery and exact verification
Mandatory exact source dependencies: [internal-source-reference] supplies exact_turnover.py (11252bytes SHA c9ef4681d976faa810ea3e27631a5ad686ac904fb18ba2bd8a38e5435ad36f1d); [internal-source-reference] supplies replay_retract20.py (4056bytes SHA15352ca7e883895bdae04b58ac77319464aa32302e7fa745156a8c0feb6dc117). This material contains the complete new source and literal parent input. [internal-source-reference] is the numerical producer provenance, not needed for this standard-library exact calculation. No old sandbox or optimizer run is required.

Save the block below exactly with final newline as support_retract20.py:5350bytes SHA a5d484bd4c0f667834fbbdf29cbb566a0d6fbb3422ff6b30a421601e4dd1c99d. Run python -B -S support_retract20.py. It reconstructs/checks the eight existing endpoint files, audits the literal TURNOVER seed with the same exact implementation, computes all rational bar comparisons and all21 squared displacement witnesses per endpoint, and writes RETRACT20_SUPPORT_GATES.json:19317bytes SHA91d1f8fe1c3de7a7737fe223cac2a1661e295e1f2b80ede942e14492f0545377. Actual execution passed the input/output hashes and terminal marker RETRACT20_SUPPORT_RADII_AND_MATCHED_HAUSDORFF_PASS. Also observed were TURNOVER_EXACT_TETRA446_PRISM446_WEAK123_CONTROLS_PASS and RETRACT20_INDEPENDENT_GRIDS_AUDIT_PASS. Execution environment Python3.13.5 standard library. This reuses one complete mechanical auditor with independent mass, not a second complete mechanical implementation or proof-assistant formalization of the support argument.

```python
"""Exact support-persistence radii and labelled Hausdorff upper certificates.
Requires complete exact_turnover.py and replay_retract20.py from durable capsules.
Run: python -B -S support_retract20.py. Standard library only; no optimizer.
An exact report is NOT an independent implementation of the general theorem.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
import exact_turnover as ex
import replay_retract20 as rr
SCALE=10**12
PARENT={'grid':10000,'points':[[-4900,9375,-4701],[6421,-82,-5296],[8443,2535,-3041],[9412,3109,-333],[10072,1807,1751],[10477,-562,2414],[10351,-2920,2709],[9618,-4801,3839],[8474,-6312,5048],[7021,-7226,6513],[5205,-7986,7728],[3072,-8650,8530],[723,-9005,9035],[-1739,-9104,9120],[-4279,-8878,8818],[-6795,-8218,8188],[-9218,-7095,7194],[-11421,-5456,5840],[-13241,-3217,4121],[-14541,-218,1839],[-14946,5442,-2355]]}

def verify_file(path,size,sha):
    b=Path(path).read_bytes()
    assert len(b)==size and hashlib.sha256(b).hexdigest()==sha,str(path)

def eta_greater_than(bar,epsilon):
    """Exact epsilon < (1/sqrt(death)-1/sqrt(birth))/2, epsilon >= 0."""
    b,d=F(bar['birth']),F(bar['death']);epsilon=F(epsilon)
    assert b>d>0 and epsilon>=0
    B,D=1/b,1/d;q=D-B-4*epsilon**2
    return q>0 and q*q>16*epsilon**2*B

def eta_interval(bar):
    lo,hi=0,1
    while eta_greater_than(bar,F(hi,SCALE)):hi*=2
    while hi-lo>1:
        m=(lo+hi)//2
        if eta_greater_than(bar,F(m,SCALE)):lo=m
        else:hi=m
    assert eta_greater_than(bar,F(lo,SCALE))
    assert not eta_greater_than(bar,F(hi,SCALE))
    return {'lower_open':lo,'upper_closed':hi,'scale':SCALE}

def identify(o):
    assert len(o['polar']['bars'])==1
    bar=o['polar']['bars'][0]
    return dict(V=o['V'],E=o['E'],F=o['F'],C=o['C'],
                strict=list(map(len,o['mechanics']['strict'])),
                weak=list(map(len,o['mechanics']['weak'])),
                primitive_zeros=o['mechanics']['primitive_zero_counts'],
                volume=o['volume'],centroid=o['centroid'],TQ=o['TQ'],
                physical_bar_count=len(o['physical']['bars']),
                polar_bar=bar,eta=eta_interval(bar))

def main():
    verify_file(ex.__file__,11252,'c9ef4681d976faa810ea3e27631a5ad686ac904fb18ba2bd8a38e5435ad36f1d')
    verify_file(rr.__file__,4056,'15352ca7e883895bdae04b58ac77319464aa32302e7fa745156a8c0feb6dc117')
    inp=json.dumps(PARENT,separators=(',',':')).encode()
    assert len(inp)==413 and hashlib.sha256(inp).hexdigest()=='f25bc23f5a3195f5769859866978326cb2ab58123a615c6a8263811ea0845619'
    rr.main()  # Reconstruct the four distinct grids and check all eight manifests.
    parent=ex.audit(PARENT);assert list(map(len,parent['mechanics']['strict']))==[2,1,1]
    pbar=parent['polar']['bars'][0]
    assert eta_greater_than(pbar,F(25219,100000))
    report={'definition':'eta=(1/sqrt(polar_death)-1/sqrt(polar_birth))/2',
            'metric':'Euclidean Hausdorff distance of bodies at respective own volume centroids; no rotation or rescaling',
            'theorem_scope':'Every own-centred convex polyhedron within distance strictly less than eta retains at least two strict stable facet equilibria.',
            'asymmetric_scope':'If hK-a <= hL <= hK+b and a+b < 2*eta, at least two strict stable equilibria remain. For K subset Lraw: a=norm(g), b=delta+norm(g).',
            'parent':identify(parent),'parent_closed_exclusion_radius':F(25219,100000),'bodies':{}}
    for k in (6,5,4,3):
        name='C114_RETRACT20_G%d'%k
        path=name+'_EXACT.json';verify_file(path,*rr.EXPECTED[path])
        o=json.loads(Path(path).read_text());entry=identify(o)
        old=parent['physical']['points'];new=[tuple(map(F,z)) for z in o['physical']['points']]
        assert len(old)==len(new)==21
        distances=[ex.norm2(ex.sub(a,b)) for a,b in zip(old,new)]
        eps2=max(distances);entry['labelled_vertex_squared_distances']=distances
        entry['matching_maximum_vertex']=distances.index(eps2)
        entry['hausdorff_squared_upper_bound']=eps2
        entry['sqrt_squared_upper_bound_interval']=ex.interval_power(eps2,2)
        entry['distance_interpretation']='Matched vertices give a convex-combination witness in both directions. This bounds the Hausdorff distance; it is not its exact value.'
        if k>3:
            assert list(map(len,o['mechanics']['strict']))==[2,1,1]
            assert eps2<F(211,10000)**2
            assert eta_greater_than(pbar,F(211,10000))
            assert eta_greater_than(o['polar']['bars'][0],F(1237,5000))
            entry['motion_strict_upper_bound']=F(211,10000)
            entry['new_closed_exclusion_radius']=F(1237,5000)
            entry['inside_parent_S2_neighbourhood']=True
        else:
            assert list(map(len,o['mechanics']['strict']))==[2,7,7]
            entry['control']='Rounding adds six unstable/saddle pairs; not a211 object.'
        report['bodies'][name]=entry
        print(name,'eta',entry['eta'],'distance_upper_interval',entry['sqrt_squared_upper_bound_interval'],flush=True)
    receipt=ex.write_json('RETRACT20_SUPPORT_GATES.json',report)
    assert receipt=={'bytes':19317,'sha256':'91d1f8fe1c3de7a7737fe223cac2a1661e295e1f2b80ede942e14492f0545377'}
    print('RETRACT20_SUPPORT_RADII_AND_MATCHED_HAUSDORFF_PASS',receipt,flush=True)
if __name__=='__main__':main()
```
