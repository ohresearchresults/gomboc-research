# material-af2d97753294

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

#!/usr/bin/env python3
"""Closed support-patch chart negative control; exact arithmetic, no optimization."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, importlib.util, json, sys

SOURCE='lower_stability_exact.py'
EXPECTED_BYTES=14296
EXPECTED_SHA='5991d683097726af3677b2f331c12d23f1aa831528a5ee3f130bf3aa69658b90'
b=Path(SOURCE).read_bytes()
assert len(b)==EXPECTED_BYTES and hashlib.sha256(b).hexdigest()==EXPECTED_SHA
spec=importlib.util.spec_from_file_location('lower_stability_exact',SOURCE)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

def build():
    # Exactly the triangular r=2 frustum from the parent's equality controls.
    B=[(-1,-1),(2,-1),(-1,2)]
    pts=[(*p,0) for p in B]+[(2*p[0],2*p[1],1) for p in B]
    body=m.hull(pts); root=m.with_vertices(body,range(3)); top=m.with_vertices(body,range(3,6))
    L,d,H=m.root_stats(body,root)
    assert body['f_vector']==[6,9,5]
    assert body['volume']==F(21,2) and body['centroid']==(0,0,F(17,28))
    assert (L,d,H)==(F(28,17),F(51,196),F(1736,1445))
    assert d==3/(L*7)  # D(L), since r=2 and 1+r+r^2=7.
    w=body['Lambda'][root][top]; assert w==F(132,119)
    twice=2*w; gap=twice-F(51,25); assert gap==F(531,2975)>0
    # Ordinary weak separation falsely allows two identical copies of the top facet.
    n=(F(0),F(0),F(1)); t=F(1); verts=body['vertices'][3:]
    assert all(m.dot(n,v)<=t and m.dot(n,v)>=t for v in verts)
    wrong_orthogonality=m.dot(n,m.add(n,n)); assert wrong_orthogonality==2
    # A tangential separator of identical positive-area triangles would vanish:
    # its dot products with both triangle differences and n would all be zero.
    independent=m.det(m.sub(verts[1],verts[0]),m.sub(verts[2],verts[0]),n)
    assert independent==36
    # Genuine distinct bottom/top facets do have the required unit witness.
    nf=(F(0),F(0),F(-1)); ng=n; witness=n; cut=F(1,2)
    assert m.dot(witness,witness)==1 and m.dot(witness,m.add(nf,ng))==0
    assert all(m.dot(witness,v)<=cut for v in body['vertices'][:3])
    assert all(m.dot(witness,v)>=cut for v in verts)
    return {'identity':'CLOSED_TWO_SUPPORT_PATCH_SEPARATOR_V1','body':body,'root':root,'top':top,
            'L':L,'d_equals_D':d,'H_equals_M2':H,'single_top_trace':w,
            'invalid_duplicate_trace':twice,'invalid_duplicate_gap_over_51_25':gap,
            'invalid_normal_witness_orthogonality':wrong_orthogonality,
            'no_tangential_unit_witness_determinant':independent,
            'genuine_distinct_pair_witness':{'nF':nf,'nG':ng,'w':witness,'cut':cut},
            'status':'The actual body is valid; duplicating its top facet is an invalid formal patch pair.'}

def main():
    assert len(sys.argv)==2 and sys.argv[1] in ('build','check')
    obj=m.encode(build()); data=(json.dumps(obj,sort_keys=True,indent=2)+'\n').encode()
    p=Path('patch_separation_controls.json')
    if sys.argv[1]=='build': p.write_bytes(data)
    else: assert p.read_bytes()==data
    print('SUPPORT_PATCH_NAIVE_CLOSURE_COUNTEREXAMPLE_PASS 264/119 531/2975')
    print('SUPPORT_PATCH_TANGENTIAL_WITNESS_REPAIR_PASS 36')
    print('SUPPORT_PATCH_GENUINE_PAIR_PRESERVED_PASS')
    print('SUPPORT_PATCH_RECOVERY_PASS',len(data),hashlib.sha256(data).hexdigest())
if __name__=='__main__': main()
