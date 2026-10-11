# material-ab0afd7c1617

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# J85 low stable carrier: general finite lemma and executed C276 own121 example

## Scientific distinction
This is coordinator-derived geometry and an executed exact construction, not own110 and not a claim that stable-carrier detachment is historically new. It removes a direct geometric coupling while preserving, rather than cancelling, the remaining P basin. The accepted own110 remains C622, outside the requested C<500 target.

### General three-stellar low-carrier lemma
Suppose a homogeneous convex 3D polyhedron has OWN strict121, no additional weak equilibria, and a triangular maximal stable facet. Let D be the squared radius at its unique strict saddle, equivalently the death level of its single finite P bar in our radial-tree convention. There is a homogeneous rational successor when the input is rational, with the SAME strict121/weak000, at most9 additional true edges, and a stable triangle all of whose points have squared radius STRICTLY BELOW its remaining P death. Its stable carrier can be made to use only newly added vertices. Thus E<=240 suffices to keep the successor at E<=249. This does not produce110.

Proof of the radial gap: center at the actual centroid g. The radius d of the largest centered ball contained in the polyhedron is the least normalized support distance. A minimizing plane touches that ball at its orthogonal foot, which lies in the relative interior of that maximal facet: for any different outward unit normal m, m.(d*n)<d unless m=n; coincident planes are one maximal facet. Therefore every minimizing support gives a strict stable facet. Since S=1, the minimum is attained at exactly one facet and its foot f is the unique boundary point of minimum squared radius d^2. The strict saddle is a different boundary point, so d^2<D.
Choose a rational L strictly between d^2 and D, avoiding the finitely many existing vertex squared radii. At any stage let f be the current stable foot and choose a corner c to replace. Write delta=L-|f-g|^2>0 and r=|c-f|^2>0. The explicit rational choice lambda=delta/[2(r+delta)] belongs to(0,1), and t=(1-lambda)f+lambda*c satisfies
|t-g|^2=|f-g|^2+lambda^2*r <= |f-g|^2+delta/16 < L.
The inequality uses r*delta/(r+delta)^2<=1/4. Apply the stable-triangle splitting lemma in [internal-source-reference], with a sufficiently small positive rational protrusion beta. It preserves the complete OWN strict/weak census, replaces corner c in the stable triangle by the new apex, and adds exactly3 true edges. Because the TRUE homogeneous centroid and surviving saddle vary continuously, beta can be chosen small enough that every previously installed low corner remains below L, the new corner remains below L, the new stable foot stays below L, and the current saddle level stays above L. All these inequalities are open. Replace each of the three original stable corners in at most three steps. If only high corners are to be removed, fewer steps can suffice, but three steps also remove every original stable corner. The resulting triangle is entirely below the saddle level: squared norm is convex, so its maximum over the triangle is bounded by the maximum at its vertices. Each step uses genuine homogeneous mass, not a freely selected reference center.
For rational input, all feet, lambda values, rational apex coordinates and uniform-volume moments are rational. A deterministic constructive version chooses beta=2^-m and increases m until the exact visibility, strict/weak census and displayed radial inequalities hold; termination follows from the small-interval lemma. This proof is not a uniform lower bound on beta or on the achieved robustness. Centroid motion, other nonstable-facet guards and useful finite deformation capacity remain coupled. Merely detaching labels never proves cancellation.

## Executed exact instance
Starting from the literal J85_DOUBLE_STELLAR_L1D4_G12, third_stellar85.py below removes the old elder vertex0 from the stable carrier by a third protrusion. The result J85_THIRD_STELLAR_LOW_S_G18 has V48/E138/F92,C276, OWN strict121, additionalweak000, exactly one P depth .45529621853755375, and no Q. U remains material0/40; the sole stable triangle is{45,46,47}, all new relative to the original45-row J85_DYNAMIC_A_G8. Its three squared vertex radii at its NEW actual centroid are approximately .513447917438454,.23815561562887316,.2872614337969408, while the single finite P death is .7360975669027151. The complete triangle is therefore strictly below the death level, independent of which superlevel component is considered. Its sufficient unchanged-surface S1 cube rho is3.1617028314840814e-7. No primitivezero000 claim is made.
The first execution had an overly strong test asking the two previously added vertices to lie below the NEW apex's construction target L=(old minimum+old death)/2. One older apex has squared radius .51345, above that target~.48512 but still strictly below the actual death~.73610. The corrected certificate checks the desired strict separation below the actual death and records an exact separator halfway between the maximal stable-vertex radius and that death. No input coordinate was changed by this test correction; input hash remained identical. This is not evidence against the three-step lemma or a discarded equilibrium.

## Exact source dependency and recovery
Required complete materials: [internal-source-reference] for exact84.py and its base input; [internal-source-reference] for freeze85.py; [internal-source-reference] for freeze_dynamic85.py, stellar_exact85.py and double_stellar85.py; [internal-source-reference] for literal J85_DYNAMIC_A_G8_INPUT.json. Only G8 is used here, so the separate G10 serialization correction is not a computational dependency for this body. Extract these files, run python stellar_exact85.py, then python double_stellar85.py, then python third_stellar85.py below. The generators use only exact rational arithmetic after their literal integer input; no optimizer, FULL76 or former sandbox is needed.
The required double-stellar input is2071B/SHAf9d5198d166df9893f9bc93e94689b618ab62d2721f546c44af131bdb94f0a54. The additional row on D=10^18 is exactly[-215600882895910855,-740999561581714304,-271106200596555378]; every previous row is scaled by10^6 without geometric change. The complete formula below independently regenerates this row with rational ties-to-even rounding.
Save the source block with its final LF. Executed CPython3.13.5 standard library. third_stellar85.py2791B/SHA7a8dc1e7d3ff144ffd2b64af6f60eac8e57c905f91c7234bd6ad5e2b7f772e4e.
Expected outputs:
J85_THIRD_STELLAR_LOW_S_G18_INPUT.json2985B/32cba83de40271ce4bf02ba6ff22d38a839879b64da33c6637089e72876e757b
J85_THIRD_STELLAR_LOW_S_G18_EXACT.json8107B/6be7e0521fe41380bb2a19b7559de46c74c58edf764e78c35001a71de2ca702a
J85_THIRD_STELLAR_LOW_S_G18_CUBE.json133812B/a111878dacb23682a813c283e1ffd725bc4c55471e15036c1a2ca1a8d0324108
Expected markers: J85_THIRD_STELLAR_LOW_STABLE_TRIANGLE_EXACT_PASS and J85_THIRD_STELLAR_OWN121_NO_110.

## third_stellar85.py
```python
"""Exact third stellar addition: stable triangle below the remaining P death.
Dependencies: exact84.py, freeze85.py, freeze_dynamic85.py and the complete exact
J85_DOUBLE_STELLAR_L1D4_G12 input generated by double_stellar85.py. No optimizer.
"""
import json
from fractions import Fraction as R
from exact84 import ROOT,audit,sub,cross,dot,add,scale
from freeze85 import dump,cube
from freeze_dynamic85 import exact_hull

def main():
    base=json.loads((ROOT/'J85_DOUBLE_STELLAR_L1D4_G12_INPUT.json').read_text())
    P,F,ids=exact_hull(base['points'],base['denominator']);assert ids==list(range(47))
    parent=audit(P,F);assert parent['strict']==[1,2,1] and parent['weak']==[0,0,0]
    g=tuple(map(R,parent['own_centroid']));sf=F[parent['S'][0]];a,b,c=[P[i] for i in sf]
    n=cross(sub(b,a),sub(c,a));nn=dot(n,n);h=dot(n,sub(a,g));foot=add(g,scale(n,h/nn))
    rmin=dot(sub(foot,g),sub(foot,g));death=R(parent['P'][0]['death2']);L=(rmin+death)/2
    assert rmin<L<death
    dist=dot(sub(P[0],foot),sub(P[0],foot));delta=L-rmin;lam=delta/(2*(dist+delta))
    assert 0<lam<1
    t=add(scale(foot,1-lam),scale(P[0],lam));assert dot(sub(t,g),sub(t,g))<L
    beta=R(1,10**12);D=10**18
    w=add(t,scale(n,beta*h/nn));row=[round(v*D) for v in w]
    rows=[[z*(D//base['denominator']) for z in p] for p in base['points']]+[row]
    name='J85_THIRD_STELLAR_LOW_S_G18'
    dump(name+'_INPUT.json',{'denominator':D,'name':name,'points':rows})
    Q,G,qids=exact_hull(rows,D);r=audit(Q,G);r['name']=name;r['material_rows']=qids
    assert (r['V'],r['E'],r['F'])==(48,138,92) and r['strict']==[1,2,1] and r['weak']==[0,0,0]
    assert [qids[i] for i in r['U']]==[0,40] and len(r['P'])==1 and not r['Q']
    sf2=G[r['S'][0]];assert {qids[i] for i in sf2}=={45,46,47}
    own=tuple(map(R,r['own_centroid']));newdeath=R(r['P'][0]['death2'])
    norms=[dot(sub(Q[i],own),sub(Q[i],own)) for i in sf2]
    assert all(s<newdeath for s in norms)
    certificate_level=(max(norms)+newdeath)/2
    r['stable_facet_material_rows']=sorted(qids[i] for i in sf2)
    r['stable_vertex_squared_radii']=[str(s) for s in norms]
    r['separating_squared_radius']=str(certificate_level);r['construction_target_squared_radius']=str(L)
    r['lambda']=str(lam);r['beta']=str(beta)
    r['scope']='All three stable-facet vertices lie strictly below the sole finite P death at the new own centroid. The remaining P basin is not cancelled.'
    dump(name+'_EXACT.json',r);cc=cube(Q,G);dump(name+'_CUBE.json',cc)
    print('J85_THIRD_STELLAR_LOW_STABLE_TRIANGLE_EXACT_PASS',row,float(lam),
          float(R(r['P'][0]['depth'])),[float(s) for s in norms],float(newdeath),
          cc['certificates']['adjacent']['rho_float'],flush=True)
    print('J85_THIRD_STELLAR_OWN121_NO_110',flush=True)
if __name__=='__main__':main()
```
