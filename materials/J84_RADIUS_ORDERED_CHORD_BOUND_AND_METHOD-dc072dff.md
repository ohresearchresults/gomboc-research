# material-dc072dfffa56

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# J84 radius-ordered chord witnesses: quantitative control of radial persistence

This is a coordinator derivation motivated by the finite-basin/near-zero-witness-loss contradiction actually observed in the preceding J84 material experiments. It is not a claim of priority in the literature and not a construction of110. The lemma is mathematical; the numerical controls below illustrate it rather than prove it.

## Lemma and proof
Let K be a full-dimensional compact convex polytope with the chosen reference origin in its interior. Write r_i=||x_i|| for its vertices. Order the vertices by increasing r_i, resolving equal radii by a fixed strict elder priority. Except for the final, oldest/farthest vertex r, choose for each i a vertex j(i) later in this order. Define
c_i = x_i dot (x_j-x_i) / (r_i ||x_j-x_i||),
d_i = max(0,-c_i)^2.

Every finite zero-dimensional radial SUPERLEVEL persistence bar born at vertex i has relative squared-radius depth at most d_i. Consequently max depth<=max_i d_i, sum depths<=sum_i d_i, and sum sqrt(depth)<=sum_i sqrt(d_i). Only actual finite-bar birth vertices need be summed, so summing over all i except r remains valid. This applies to either physical K or its centred polar, giving P or Q bounds respectively. As usual the radial persistence here is the full boundary persistence; the adopted true-edge graph computes the same component merges, not a triangulation with unmerged false facets.

Proof: for the chord from x_i to x_j, put l=||x_j-x_i|| and t in[0,1]. Its squared radius is r_i^2+2t r_i l c_i+t^2 l^2. If c_i>=0 its minimum is r_i^2. If c_i<0, the later vertex has r_j>=r_i, so l>=-2r_i c_i; the minimum occurs at t=-r_i c_i/l<=1/2, and equals r_i^2(1-c_i^2). Thus the entire chord has radius at least r_i sqrt(1-d_i). The chord lies in K. Radially projecting its nonzero points outward to the boundary only increases radius and gives a boundary path with the same endpoints. For d_i=1 the lower bound is zero and the conclusion is trivial even if the chord passes through the origin. This path connects i to a vertex with greater birth radius or equal radius and older tie priority by the claimed level. Therefore a component born at i cannot survive below that level while remaining younger than the component containing j. Its bar depth is <=d_i. Sum and maximum inequalities follow. No compatibility assumption about separately nominated centres is used: these chords all live in ONE fixed actual K at ONE actual centre.

Why unrestricted cosine guards fail: nearly coincident points can choose each other or form cycles. All their local negative cosines can be tiny while the entire finite basin remains deep. Restricting the witness target to later radius order removes that defect. Positive unrestricted guards already strictly increase radius, so this correction matters in the negative/relaxed-loss regime; it does not invalidate legitimate positive chord certificates. A zero ordered deficit excludes finite positive bars, but may still leave weak/degenerate equilibria: strict110/weak000 still requires positive margins and exact final census. The bounds may be very loose, so a large upper bound is NOT an obstruction or lower bound.

## Completed numerical controls
Sources/dependencies: union84.py and exact N40 inputs from [internal-source-reference], J82 input/exact geometry from [internal-source-reference], the complete material methods from [internal-source-reference], and exact numerical checkpoint seeds from [internal-source-reference]. To regenerate constrained84_{0,1}.json for the diagnostic, run the two constrained84_portable.py commands in the method material first; those are complete producing sources, not missing input files. Nominations use CPython3.13.5,NumPy2.3.5,SciPy1.17.0,Torch2.10.0+cpu and one thread. Near-coplanar hulls and numerical bar floors remain limitations of the illustration, not of the geometric proof.

At N40_V47, actual numerical Q sum=.33674610559645446, ordered square sum=.7870404046597842, unrestricted square sum=.005208705662708027.
At constrained84_0 best, Q=.3947268113339911 but unrestricted square sum=1.4092283417201127e-14; ordered square sum=.7988186292198038. At constrained84_1, Q=.39818792423144855, unrestricted square sum=4.872274163755621e-12, ordered square sum=.7996862752046062. The radius-order restriction therefore exposes rather than hides the finite remaining basin.
At the two literal barconstrained SEEDS (not their final solver iterates), Q sums are .2627696214001677/.26179630177072044, maxima .2319485622523184/.23008578095192256. Their saved optimization losses .2628133015839675/.26183893277907 include the positive1e-3 witness regularizer; do not call those losses the exact Q sum. Ordered square sums are .8029712284853234/.8073459165103959. The interrupted repair seed has Q sum .2800000000190108, maximum .2742610219631548, ordered square sum .7854488830085546. Its tiny nominal-budget excess is within its save tolerance, NOT exact compliance with Q<=.28.
All six controls passed the numerical max/sum/square-root-sum inequalities. The complete mathematical proof above, not six tests, supports the lemma.

An actual bounded radius-ordered L1 search was then performed from N40_V47: fixed U carrier6, same hard primal margin1e-8 and coordinate bounds as constrained84, tau1e-5, SLSQP requested80 iterations. It completed362 calls,55 iterations,status0, loss.887074472416405, min constraint8.688681331317183e-6, numericalS2/U1 and Q=.33678178222366273, no P. This did NOT improve the input or reach110. Only run0 was performed; no ordered-search run1 is claimed. It supplies a usable corrected objective, not proof that this local chart is optimal or a prescribed only next route.

## Reconstruction and hashes
Save sources below with final LF. Run python recover_ordered_search84.py; python ordered84.py; then OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python ordered_search84.py --run 0 --iters 80. The exact source patch is anchored to the complete constrained84_portable.py in the named material; it changes only the polar relaxed objective and output names, not true S/U census or primal constraints.
ordered84.py2264B/SHAec42b4763ecc827f4f034716a85fe320c2ab8de5063a286fb0ccd62c7d13b91b
recover_ordered_search84.py1350B/SHA2368cf31f35d816bb16761822476347d41d6519ebf19448ffb6c44f9d69b3037
reproduced ordered_search84.py4584B/SHA377127ccd3b4869afcff4bf9262fa834e1ea21c4514243878e36dd66f6596c6d
observed J84_ORDERED_BOUND_CHECKS.json2488B/SHA797800bfbd846485e9e33eba77fb30f7f68e87cef8a226f8c164ae27595676cb
Observed markers: J84_ORDERED_SEARCH_SOURCE_RECOVERED; J84_RADIUS_ORDERED_BOUND_NUMERICAL_CONTROLS_PASS; J84_ORDERED_SEARCH_NOMINATION_DONE0 362 0 55. Floating trajectories/report bytes can depend on solver versions; the source/seed hashes are exact, and no floating output becomes a certified class by reproduction alone.

## ordered84.py
```python
"""Radius-ordered chord witnesses: a numerical check of a proved bar upper bound.
No exact class or feasibility claim is made by this floating diagnostic.
"""
import json
import numpy as np
from scipy.spatial import ConvexHull
from union84 import ROOT,inputs,properties,radial_bars

def check(P):
    H=ConvexHull(P);s=properties(P);g=np.array(s['centroid']);q=H.equations[:,:3]/(-H.equations[:,3]-H.equations[:,:3]@g)[:,None]
    out={}
    for name,x,depths in [('P',P[H.vertices]-g,s['P']),('Q',q,s['Q'])]:
        rr=np.einsum('ij,ij->i',x,x);delta=x[None,:,:]-x[:,None,:]
        denom=np.sqrt(rr[:,None])*np.linalg.norm(delta,axis=2);np.fill_diagonal(denom,1.)
        cosine=np.einsum('ik,ijk->ij',x,delta)/denom;np.fill_diagonal(cosine,-np.inf)
        order=np.lexsort((np.arange(len(x)),rr));rank=np.empty(len(x),int);rank[order]=np.arange(len(x));root=order[-1]
        admissible=rank[None,:]>rank[:,None]
        guards=np.where(admissible,cosine,-np.inf).max(axis=1);deficit=np.maximum(-guards,0);deficit[root]=0
        unord=np.maximum(-cosine.max(axis=1),0);unord[root]=0
        total=float(np.sum(deficit**2));maximum=float(np.max(deficit**2))
        assert sum(depths)<=total+1e-9 and max(depths,default=0)<=maximum+1e-9
        out[name]={'bar_sum':sum(depths),'bar_max':max(depths,default=0),'ordered_square_sum':total,'ordered_square_max':maximum,'unordered_square_sum':float(unord@unord),'sqrt_bar_sum':sum(np.sqrt(depths)),'ordered_L1':float(deficit.sum())}
        assert out[name]['sqrt_bar_sum']<=out[name]['ordered_L1']+1e-8
    return out

if __name__=='__main__':
    _,B,*_=inputs(47);cases={'N40_V47':B}
    for key in ['constrained84_0','constrained84_1']:
        d=json.loads((ROOT/(key+'.json')).read_text());cases[key]=np.array(d['best']['points'])
    for key in ['barconstrained84_0','barconstrained84_1','repair84_0']:
        d=json.loads((ROOT/(key+'_SEED.json')).read_text());cases[key]=np.array(d['points'])
    result={key:check(p) for key,p in cases.items()}
    (ROOT/'J84_ORDERED_BOUND_CHECKS.json').write_text(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n')
    for key,value in result.items():print(key,value['Q'],flush=True)
    print('J84_RADIUS_ORDERED_BOUND_NUMERICAL_CONTROLS_PASS',flush=True)
```

## recover_ordered_search84.py
```python
"""Recover the exact radius-ordered L1 witness search from its full durable parent."""
from pathlib import Path
import hashlib
p=Path(__file__).resolve().parent
s=(p/'constrained84_portable.py').read_text()
assert hashlib.sha256(s.encode()).hexdigest()=='1bb3f634f57677b0292ae552dc40545f6bc705b664ae9a61eb9c0311bed95e46'
old='    loss=(torch.relu(tau-qg)**2*mask).sum();cons=pg[torch.as_tensor(idx)]-margin'
new='''    # Acyclic, radius-ordered chords cannot hide a finite basin in a near-coincident cycle.
    delta=q[None,:,:]-q[:,None,:];eye=torch.eye(len(q),dtype=torch.bool)
    denom=torch.sqrt(qr[:,None]*((delta*delta).sum(dim=2)+eye.to(torch.float64)))
    cosine=(q[:,None,:]*delta).sum(dim=2)/denom
    admissible=(qr[None,:]>qr[:,None]).detach()
    ordered=cosine.masked_fill(~admissible,-1e4).max(dim=1).values
    loss=(torch.relu(tau-ordered)*mask).sum();cons=pg[torch.as_tensor(idx)]-margin'''
assert s.count(old)==1
s=s.replace(old,new).replace('constrained84_', 'ordered_search84_').replace('CONSTRAINED84_', 'ORDERED_SEARCH84_').replace('J84_CONSTRAINED_NOMINATION_DONE','J84_ORDERED_SEARCH_NOMINATION_DONE')
b=s.encode();assert len(b)==4584 and hashlib.sha256(b).hexdigest()=='377127ccd3b4869afcff4bf9262fa834e1ea21c4514243878e36dd66f6596c6d'
(p/'ordered_search84.py').write_bytes(b)
print('J84_ORDERED_SEARCH_SOURCE_RECOVERED')
```
