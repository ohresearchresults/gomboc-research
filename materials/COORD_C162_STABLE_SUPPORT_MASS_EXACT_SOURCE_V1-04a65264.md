# material-04a6526457ad

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# COORD_C162_STABLE_SUPPORT_MASS_V1

## Evidence status and exact dependency
Coordinator-derived exact scoped obstruction and reusable method, NOT a new own110 body and NOT an exclusion of either entire shape family. The accepted C622 record is unchanged.

This is a complete one-file addition to immutable parent result figure-0395, first/full SHA256 9fc14dd9e08f3f635aaab511cc93ca8219cc1b84ded8926c38cbabee87da3f86,42825bytes. That result was read from cursor0 through eof:true before this derivation. It contains the entire standalone RL04_C162_CENTER_AND_MASS_V1 recovery source. No originating sandbox or Library item is needed. Recover the parent's literal RECOVER_RL04.py,21536bytes,SHA4ee2e1affe6b26674edb33d204d059b3627026faaa77895e781a8870abc52487, and execute `python -B -S RECOVER_RL04.py PARENT_DIRECTORY`. Parent replay reproduces REPORT.json427251bytes,SHA27622f77d27f2b1e929e201c324912d3c0ad087db00c4f5696a077bc65c62437. This addition needs exactly PARENT_DIRECTORY/RL04_CENTER.py,22965bytes,SHAa0af63a1d7de9c872cb35b2c134da0eb788e1f0287fb4ddc33534d6fd83d7ef7; its hash is checked before import. All exact29-vertex inputs, fixed-reference centers, witness-chamber rule, walks and feature maps remain the literal parent's objects. These are cyclic_D1000/cyclic_D10000, not D717 or DROP29.

## General support-retention theorem, elementary proof
Let K be any full-dimensional uniformly FILLED convex polyhedron in R^3, with its actual volume centroid c. Let r be ANY point retained in K, not necessarily exposed. If the halfspace n.x<=h contains K, then

`4 n.c <= n.r+3h`, equivalently `n.r >= 4 n.c-3h`.

Triangulate the boundary facets and join their triangles to r. The resulting tetrahedra have nonnegative volumes and partition K up to boundaries; zero-volume pieces may be discarded. Each positive tetrahedron with vertices r,a,b,d has centroid(r+a+b+d)/4. Its three non-r vertices are in K, hence have n-coordinate at mosth. Averaging tetrahedral centroids with positive volume weights proves the displayed inequality. The same averaging shows(4c-r)/3 belongs toK, giving the full necessary inclusion c-(K-c)/3 subset K. With multiple retained global halfspaces and target c, EVERY retained point must lie in all lower halfspaces n.r>=4n.c-3h. For K contained in a specified parentP this gives K subset P intersect(4c-3P).

The general centroid asymmetry inclusion is classical, not a new theorem. External primary context checked: Lin Cheng, Two new proofs of partial Godbersen's Conjecture, arXiv:2406.00278v1, section4 and introduction, https://arxiv.org/html/2406.00278v1. The present polyhedral proof and all specialized numerical certificates below are self-contained and do not depend on that paper or its other claims.

## New exact specialization
For each cyclic parent and each initial/final A/B witness chamber of the literal RL04 walk, minimize n.c over the CLOSED chamber, where n.x<=h is its unique stable parent support. The code below stores exact three-row optimal bases. It reconstructs strictly positive rational dual weights w with sum(w_i a_i)=n and lower bound L=-sum(w_i b_i), verifies an exact primal point satisfying EVERY chamber row, and checks n.x=L. Thus c in that entire chamber closure implies n.c>=L, with no solver approximation in the conclusion.

For all four A chambers (two parents, initial/final), each retained old rawlex point0..22 separately violates n.r>=4L-3h. For all four B chambers, each old point0..21 separately violates it. Therefore no full-dimensional uniform convex K, however many vertices it gains or however it extends in other directions, can have centroid in one of these chambers while retaining its stated stable halfspace AND even one of the corresponding offending parent points. K need NOT be contained in the parent; changed incidence is allowed. The support need not remain a maximal facet; merely being a valid global halfspace suffices.

The exact optimal parent-normal depth fractions(h-L)/(h-min_parent n.p) are all strictly between0 and3/100, whereas retaining the farthest opposite parent point would require at least1/4. Approximate fractions: D1000 initialA .0283551830,finalA .0295951968,initial/finalB .0282014425; D10000 initialA .0287416428,finalA .0295201289,initial/finalB .0281405912. These fractions use the parent normal width and are NOT manufacturing tolerances. Every offending point's necessary L-infinity movement lower bound is reconstructed exactly as(4L-3h-n.p)/||n||1.

Additionally all twelve exact closed reference110 boxes from the parent are checked against the support-retention inequality. At least25 old points are incompatible throughout each A box;26 throughout every B,C,D,E,F box. At the exact D1000A center26 are incompatible; D10000A25; all B,C,D,E,F exact centers26. The full labels and exact fractions are in the reproduced report.

Stable primitive planes retain original exact ordering: D1000 A51=(6854348000,196540000,209653000,3921340067); B44=(1089960000,-23374000,-115041000,641359851). D10000 A48=(2735406768000,79651245000,84201053000,1564917405047); B43=(875359741000,-17549410000,-89969564000,514748557339).

Combined with the parent's contained-body mass obstruction, this rules out both naive contained clipping retainingp25 and arbitrary pure exterior extension preserving the demonstrated stable plane/old scaffold as ways to close mass in these particular cells. A useful successor must genuinely move/remove the blocked scaffold or stable plane, or reach another cell/component. This does NOT exclude such successors, all reference110 centers, the entire projective/affine orbit, or C162 own110 in general.

## Reconstruction, verification and receipts
Save the complete code fence below with its final newline as SUPPORT_MASS.py,6624bytes,SHA2560060d3e10f0686e6f7596fec12d413a6d62c294fc2fda0dd040ca93c7f36c51e.

Exact command, CPython3.13.5 standard library, assertions enabled:
`python -B -S SUPPORT_MASS.py PARENT_DIRECTORY NEW_OUTPUT_DIRECTORY`

It reproduces SUPPORT_MASS_REPORT.json,32310bytes,SHA2568a96d351367d3b1df54ffcaf795e4925e22f7562d1d06a511fe305e5734ae36c and terminal
`COORD_C162_STABLE_SUPPORT_RETAINED_MASS_EIGHT_CELLS_AND_TWELVE_BOXES_PASS`.

Observed both the exact source replay and optional discovery replay; their report bytes/hashes are identical. Optional complete LP-discovery method is also included in this same source; run without-S and append--discover. Versions NumPy2.3.5,SciPy1.17.0,threadpoolctl3.6.0,binary64,one BLAS/OMP thread. It uses HiGHS on L1-normalized rows, chooses the fourteen closest tight rows, searches exact3row bases, and accepts only exact positive primal/dual agreement. It reproduced all eight literal bases. Discovery is NOT needed to reconstruct or verify the proofs. Tetrahedron equality, an interior but false tetrahedral centroid, and cube controls validate the inequality's orientation; these are software controls, not sub-floor construction searches.

```python
#!/usr/bin/env python3
"""Exact retained-point/support-plane centroid obstructions; assertions required.
Dependency: RL04_CENTER.py from immutable RL04_C162_CENTER_AND_MASS_V1.
Usage: python -B -S SUPPORT_MASS.py PARENT_DIRECTORY NEW_OUTPUT_DIRECTORY
Optional discovery: omit -S and append --discover (NumPy/SciPy/threadpoolctl).
"""
import sys, hashlib, importlib.util
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
assert __debug__ and len(sys.argv) in (3,4)
parent=Path(sys.argv[1]);out=Path(sys.argv[2]);assert not out.exists()
p=parent/'RL04_CENTER.py';b=p.read_bytes()
assert len(b)==22965 and hashlib.sha256(b).hexdigest()=='a0af63a1d7de9c872cb35b2c134da0eb788e1f0287fb4ddc33534d6fd83d7ef7'
spec=importlib.util.spec_from_file_location('rl04_exact_dependency',p)
r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
BASES={
 (1000,'A','initial'):[87,54,98],(1000,'A','final'):[84,231,126],
 (1000,'B','initial'):[84,230,97],(1000,'B','final'):[84,230,97],
 (10000,'A','initial'):[54,90,97],(10000,'A','final'):[55,90,126],
 (10000,'B','initial'):[55,90,104],(10000,'B','final'):[55,90,104]}
RADII={'A':Q(1,200),'B':Q(1,1000),'C':Q(1,10000),'D':Q(1,10000),'E':Q(1,10000),'F':Q(9,10000)}

def exact_basis(rows,n,ids):
    rr=[rows[i] for i in ids];a,b,c=[z[:3] for z in rr];dd=r.det(a,b,c)
    assert dd
    w=[Q(r.det(n,b,c),dd),Q(r.det(a,n,c),dd),Q(r.det(a,b,n),dd)]
    assert min(w)>0
    assert tuple(sum(v*z[k] for v,z in zip(w,rr)) for k in range(3))==tuple(n)
    x=r.mul(r.add(r.add(r.mul(r.cross(b,c),-rr[0][3]),r.mul(r.cross(c,a),-rr[1][3])),r.mul(r.cross(a,b),-rr[2][3])),Q(1,dd))
    L=-sum(v*z[3] for v,z in zip(w,rr))
    assert all(r.value(z,x)>=0 for z in rows)
    assert r.dot(n,x)==L and all(r.value(z,x)==0 for z in rr)
    return w,x,L

def discover(rows,n):
    import numpy as np
    from scipy.optimize import linprog
    from threadpoolctl import threadpool_limits
    threadpool_limits(limits=1)
    norms=[sum(map(abs,z[:3])) for z in rows]
    A=np.array([[float(Q(v,m)) for v in z[:3]] for z,m in zip(rows,norms)])
    bb=np.array([float(Q(z[3],m)) for z,m in zip(rows,norms)])
    nf=np.array([float(Q(v,sum(map(abs,n)))) for v in n])
    sol=linprog(nf,A_ub=-A,b_ub=bb,bounds=[(None,None)]*3,method='highs')
    assert sol.success,sol.message
    candidates=list(map(int,np.argsort(abs(A@sol.x+bb))[:14]))
    for ids in combinations(candidates,3):
        try:exact_basis(rows,n,ids)
        except (AssertionError,ZeroDivisionError):continue
        return list(ids)
    raise AssertionError('No verified optimal basis among fourteen closest rows')

def controls():
    tetra=[(0,0,0),(1,0,0),(0,1,0),(0,0,1)]
    planes=[(-1,0,0,0),(0,-1,0,0),(0,0,-1,0),(1,1,1,1)]
    g=(Q(1,4),)*3
    slacks=[r.dot(h[:3],v)+3*h[3]-4*r.dot(h[:3],g) for h in planes for v in tetra]
    assert min(slacks)==0 and max(slacks)>0
    false_center=(Q(9,10),Q(3,100),Q(3,100))
    assert all(r.dot(h[:3],false_center)<h[3] for h in planes)
    assert any(r.dot(h[:3],v)+3*h[3]-4*r.dot(h[:3],false_center)<0 for h in planes for v in tetra)
    cube=[(x,y,z) for x in (-1,1) for y in (-1,1) for z in (-1,1)]
    for k in range(3):
        for sg in (-1,1):assert all(sg*v[k]+3>0 for v in cube)
    return {'tetra_equalities':slacks.count(0),'false_interior_centroid_rejected':True,'cube_pass':True}

report={'identity':'COORD_C162_STABLE_SUPPORT_MASS_V1','dependency_result':'figure-0395','dependency_sha256':'9fc14dd9e08f3f635aaab511cc93ca8219cc1b84ded8926c38cbabee87da3f86','controls':controls(),'cells':[],'center_boxes':[]}
for D,(den,points) in r.DATA.items():
    d=r.auditA(*r.hull(points,den));P=d['P'];H=d['H']
    assert (len(P),len(d['edges']),len(H))==(29,81,54)
    own=r.census(d,d['centroid'],'B');assert own['counts']==[1,2,1] and own['weak']==[0,0,0]
    centers={'A':r.CA,'B':r.CB,**r.EXTRA_CENTERS}
    for name,c in centers.items():
        cc=r.census(d,c,'B');assert cc['counts']==[1,1,0] and cc['weak']==[0,0,0]
        f=cc['S'][0];n=H[f][:3];h=H[f][3];rho=RADII[name]
        ch=r.chamber(d,c);assert ch['open_box_radius']>rho
        L=r.dot(n,c)-rho*sum(map(abs,n));cut=4*L-3*h
        bad=[i for i,p in enumerate(P) if r.dot(n,p)<cut]
        exact_bad=[i for i,p in enumerate(P) if r.dot(n,p)<4*r.dot(n,c)-3*h]
        assert bad and 0 in bad
        report['center_boxes'].append(dict(parent=D,center_name=name,center=c,radius=rho,stable_facet=f,stable_plane=H[f],bad_for_entire_closed_box=bad,bad_at_exact_center=exact_bad,necessary_retained_n_dot_lower=cut,parent_depth_fraction=(h-r.dot(n,c))/(h-min(r.dot(n,p) for p in P))))
    for name,start in [('A',r.CA),('B',r.CB)]:
        cf=r.census(d,start,'B')['S'][0];n=H[cf][:3];h=H[cf][3]
        final=start
        for ids in r.WALK_BASES[D,name]:final=r.basis_point(r.chamber(d,final),ids,Q(1,10**6))
        for phase,c in [('initial',start),('final',final)]:
            cc=r.census(d,c,'B');assert cc['counts']==[1,1,0] and cc['weak']==[0,0,0] and cc['S']==[cf]
            ch=r.chamber(d,c);rows=ch['rows'];ids=BASES[D,name,phase]
            if len(sys.argv)==4:
                assert sys.argv[3]=='--discover';found=discover(rows,n)
                print('DISCOVERED',D,name,phase,found)
                assert exact_basis(rows,n,found)[2]==exact_basis(rows,n,ids)[2]
            w,x,L=exact_basis(rows,n,ids);cut=4*L-3*h
            bad=[i for i,p in enumerate(P) if r.dot(n,p)<cut]
            assert bad==list(range(23 if name=='A' else 22))
            width=h-min(r.dot(n,p) for p in P);depth=(h-L)/width
            assert 0<depth<Q(3,100)<Q(1,4)
            moves={i:Q(cut-r.dot(n,P[i]),sum(map(abs,n))) for i in bad}
            assert min(moves.values())>0
            report['cells'].append(dict(parent=D,root_cell=name,phase=phase,reference_center=c,stable_facet=cf,stable_plane=H[cf],rows_sha256=hashlib.sha256(r.pack(rows)).hexdigest(),row_count=len(rows),optimal_basis=ids,basis_rows=[rows[i] for i in ids],basis_labels=[ch['labels'][i] for i in ids],positive_dual_weights=w,attained_primal_closure_point=x,exact_lower_n_dot_center=L,necessary_retained_n_dot_lower=cut,incompatible_retained_parent_points=bad,necessary_Linf_point_displacements=moves,parent_normal_width=width,maximum_parent_depth_fraction=depth))
assert len(report['cells'])==8 and len(report['center_boxes'])==12
out.mkdir(parents=True);b=r.pack(report);(out/'SUPPORT_MASS_REPORT.json').write_bytes(b)
print('SUPPORT_MASS_REPORT.json',len(b),hashlib.sha256(b).hexdigest())
print('COORD_C162_STABLE_SUPPORT_RETAINED_MASS_EIGHT_CELLS_AND_TWELVE_BOXES_PASS')
```
