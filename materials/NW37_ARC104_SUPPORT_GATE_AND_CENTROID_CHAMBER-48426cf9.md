# material-48426cf91b86

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# NW37 ARC104 support gate and directional all-point centroid chamber

## Evidence and limits
Lead-derived scalar consequence and constructive lemma, NOT a new own110 body or independent mechanics audit. Immutable NW37 parent figure-0445 was read completely cursor0 through EOF in consecutive pages with constant SHA256 f57c846c102989063465ec50d170bd6210969dcc31d1f0c6b68655dd3dce51b7. Its exact object NW37_ARC104_G6 remains V104/E306/F204,C612,own211/additionalweak000/primitivezero000. Do not alias it to PRUNE94_G6, RETRACT20 or an own110 record. The parent contains a complete22-file recovery capsule. The three literal scalar inputs below come from its ARC104_G6 complete polar elder event and actual uniform volume. The new calculation does not reconstruct the hull; its geometric conclusion inherits the parent's certified elder-bar meaning.

## Remaining support-scale barrier
For inherited same-physical-centre polar elder birth/death squared radii b>d>0, put Delta=1/sqrt(d)-1/sqrt(b), eta=Delta/2. The complete elder component determines two separated physical support-function sublevel basins. Under uniform support perturbation at most epsilon<eta, each retains a point of height at most1/sqrt(b)+epsilon while its boundary has height at least1/sqrt(d)-epsilon. Both retain interior local minima. For a polyhedron and interior reference point, such a local minimum is a strict stable facet equilibrium: a projection on a face boundary admits a tangent direction with zero first derivative and negative second derivative, hence cannot be a local minimum. Consequently centred Hausdorff distance<eta excludes S1. This is local, not a complexity bound or global obstruction.

Executed exact ARC104_G6 result: eta in(57147727848,57147727849]/10^12. The CLOSED centred Hausdorff radius2857/50000=0.05714 therefore excludes S1. Delta/Vol^(1/3) lies strictly between
38098485232000000000000000000/461685521348166494600459753553 and
57147727849000000000000000000/692528282022249741900689630329,
approximately0.08252042455381474 to0.08252042455525872. The remaining support gap is substantially smaller than RETRACT20's, but positive. No matched-vertex distance, optimized similarity alignment or crossing of an older protected ball was computed. Every S1 targetL must satisfy d_H(K,aRL)>=eta(K) for every positive scalea and rotationR, because similarity preserves own counts.

For x>=0, x<eta iff h=1/d-1/b-4*x*x>0 and h*h>16*x*x/b. The complete program bisects using rational arithmetic and brackets the cube root of exact volume by rational powers. Floating JSON numbers are descriptive only.

## Directional centroid chambers: escape witnesses need not be true edges
For the complete physical vertex set x_i in a fixed frame, select any other vertexp(i) for every nonrooti. Define e_i=x_p(i)-x_i and g_i=x_i dot e_i. At centrec the escape inequality is exactly e_i dot c<g_i. Their intersection is an open rational convex centroid chamber. When allg_i>0, min_i g_i/|e_i| is merely its origin-centred inball radius; directional inequalities can allow much larger finite centroid shifts. A witness chord need NOT be a true hull edge.

Proof: a positive witness gives |x_j-c|^2-|x_i-c|^2=2*(x_i-c) dot (x_j-x_i)+|x_j-x_i|^2>0. One positive witness for EVERY nonroot makes an acyclic graph whose only possible sink is the root. The root is strictly farther fromc than every other vertex. For everyj!=r,
(x_r-c) dot (x_r-x_j)=(|x_r-c|^2-|x_j-c|^2+|x_r-x_j|^2)/2>0,
so the root is strictly unstable. Every other vertex has a positive witness in the body and its radial vector is outside its normal cone, even weakly. Thus U1 and no additional weakU follow. This says nothing by itself aboutS,H or other primitive zeros.

At a specified actual centre, the exact test can therefore use max_j (x_i-c) dot (x_j-x_i)>0 for every nonroot, without forcing selected witnesses to stay on the one-skeleton. A positive chord also implies a positive incident edge via the tangent cone, but a prescribed positive cosine margin on selected edges is a stronger numerical restriction. Permit witness switches and useful root switches rather than freezing one tree. This is relevant to NW37's newly enlarged escape reserve; it is NOT a claim that prior optimizers necessarily omitted all-pairs witnesses.

For actual homogeneous volumeV>0 and first momentM, c=M/V, the directional constraint becomes e_i dot M<V*g_i, linear in mass and moment for the fixed geometry. For a retained parent of volumeV0 at centroid0 and genuinely disjoint added geometric cells of volumesv_k and centroidsc_k, it is
V0*g_i+sum_k v_k*(g_i-e_i dot c_k)>0.
All quantities must come from the ACTUAL convex uniformly filled final geometry. This does not license independent density weights or arbitrary realization of a moment-space linear program. Its prospective use is coupled interface/mass compensation with exact finite hull checks. The union over witness/root choices is larger and need not be convex. No new finite110 deformation is claimed.

## Complete executed scalar source
Save code as support_gate.py:2619UTF-8bytes SHA2567bfcf05994968d2448f6afac9d152215e2e3baa907bca4e837fbdff36c483d93. Standard library only, executed CPython3.13.5. Run python -B -S support_gate.py. Marker NW37_ARC104_EXACT_SUPPORT_GATE_PASS. Reproduced NW37_ARC104_SUPPORT_GATE.json:1082bytes SHA2563b3cad1ec4f46eff437fbd3ec5af19cecd3a663c78b40c619b14c904a85acd03. The literal inputs are embedded; no old sandbox or optimizer needed.

```python
"""Exact inherited ARC104 polar-bar support gap; standard library only.
The quoted birth/death/volume come from immutable NW37 result, not a new hull audit.
"""
from fractions import Fraction as Q
import hashlib, json
from pathlib import Path

SOURCE_ID = 'figure-0445'
SOURCE_SHA256 = 'f57c846c102989063465ec50d170bd6210969dcc31d1f0c6b68655dd3dce51b7'
B = Q(8907144718796459433110608243085063783821257036338825169049056000000000000,3934866812342999123389035701250186801436931149755870203977402793741367289)
D = Q(2399095352389492696843113308351417785052850090102368000000000000,1455681313764653708119907379751364956987308762256717267585377127)
VOL = Q(15942402875921080133,6000000000000000000)
SCALE = 10**12

def less_than_eta(x):
    """Equivalent exact comparison x < (D**(-1/2)-B**(-1/2))/2 for x>=0."""
    assert x >= 0 and B>D>0
    h=1/D-1/B-4*x*x
    return h>0 and h*h>16*x*x/B

def floor_eta():
    lo,hi=0,1
    while less_than_eta(Q(hi,SCALE)):
        hi*=2
    while hi-lo>1:
        mid=(lo+hi)//2
        if less_than_eta(Q(mid,SCALE)): lo=mid
        else: hi=mid
    assert less_than_eta(Q(lo,SCALE)) and not less_than_eta(Q(hi,SCALE))
    return lo,hi

def root_bracket(q,n,scale):
    assert q>0 and n>=1 and scale>0
    lo,hi=0,1
    while Q(hi,scale)**n<q: hi*=2
    while hi-lo>1:
        mid=(lo+hi)//2
        if Q(mid,scale)**n<q: lo=mid
        else: hi=mid
    return Q(lo,scale),Q(hi,scale)

def main():
    lo,hi=floor_eta()
    vlow,vhigh=root_bracket(VOL,3,10**30)
    lower,upper=2*Q(lo,SCALE)/vhigh,2*Q(hi,SCALE)/vlow
    protected=Q(5714,100000)
    assert less_than_eta(protected)
    report={
        'object':'NW37_ARC104_G6', 'source_assignment':SOURCE_ID,
        'source_result_sha256':SOURCE_SHA256,
        'birth':str(B),'death':str(D),'volume':str(VOL),
        'eta_interval_left_open_right_closed': [lo,hi], 'interval_denominator':SCALE,
        'normalized_support_gap_rational_lower':str(lower),
        'normalized_support_gap_rational_upper':str(upper),
        'normalized_support_gap_approx_interval':[float(lower),float(upper)],
        'closed_centred_Hausdorff_radius_excludes_S1':str(protected),
        'scope':'Exact scalar consequence of quoted complete polar elder bar; not new mechanics or reconstruction audit.'}
    output=json.dumps(report,sort_keys=True,separators=(',',':'))+'\n'
    Path('NW37_ARC104_SUPPORT_GATE.json').write_bytes(output.encode())
    print(output,end='')
    print('NW37_ARC104_EXACT_SUPPORT_GATE_PASS')
    print(len(output.encode()),hashlib.sha256(output.encode()).hexdigest())

if __name__=='__main__':main()
```
