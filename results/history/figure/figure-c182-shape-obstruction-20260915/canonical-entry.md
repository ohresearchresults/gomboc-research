
## 2026-09-15T20:43:37.741Z

### C182 exact double shape obstruction — complete recovery capsule and constructive consequence

A new coordinator-owned geometric result applies to the literal Finch C182_TWO_PLANE222, not the different C476. At its exact own filled-volume centroid it contains the central disk of radius **31/400** perpendicular to **n=(8,3,0)**, and lies strictly inside the slab of halfwidth **7/400** in that direction. It also contains a centred segment of half-length **363/1000** parallel to **m=(-7,12,100)** and lies strictly inside the coaxial cylinder of radius **121/1000**. All 136 supplied inequalities and all 54 exact vertices were checked by rational squared comparisons. These facts imply **at least two strict stable facets and at least two strict unstable vertices**, independently of its existing exhaustive own222 census. This explains why local contact correction remains in that class and gives quantitative shape changes a successor must escape.

More strongly, every nonsingular affine image A(P)+b with singular-value condition number kappa(A)<31/7 still has S>=2 about its own filled-volume centroid. Every such image with kappa(A)<3 has U>=2. These are proved exclusions of specified affine regions, NOT an exclusion of the full affine orbit, arbitrary non-affine redesign, or all C182 polyhedra. They motivate deliberately anisotropic or non-affine reconstruction rather than another near-identity local optimization.

**Proof.** Translate the own centroid to 0. For the disk/slab assertion let e=n/|n| and rho(u) be the radial function on the unit sphere. On the equator e.u=0, rho>=R; at both poles rho<=h<R. Thus rho attains a local minimum inside each open hemisphere. To see this is a strict stable maximal facet, write rho(u)=1/f(u), f(u)=max_i q_i.u for distinct normalized facet vectors q_i=a_i/b_i, b_i>0. At an interior local maximum u of f, every active linear function q_i.u has a local maximum on the sphere, hence each active q_i is the same positive multiple of u. There is therefore a single distinct active maximal facet and the radial point is its interior perpendicular foot. The two hemispheres yield distinct facets. For the segment/cylinder assertion, rho<=r on the equator perpendicular to m, while rho>=L>r at both poles. It attains a local maximum inside each hemisphere. The corresponding boundary point must be a vertex: any point inside an edge or face admits a two-sided segment along which strictly convex squared norm cannot have a local maximum. At a vertex p, a neighbor difference d with p.d>=0 would give |p+td|^2>|p|^2 for small t>0, also impossible. Hence every adjacent escape dot product is strictly negative, giving a strict unstable vertex in each hemisphere. No generic-position assumption is needed for these existence arguments.

Under A, the central disk becomes an ellipse containing a disk of radius at least sigma_min(A)R in its image plane; the slab's transformed halfwidth is h/|A^{-T}e|<=sigma_max(A)h. Similarly, the axial segment has half-length at least sigma_min(A)L and the image lies inside a cylinder about its image axis of radius at most sigma_max(A)r. The two ratio conditions follow. A uniform filled-volume centroid transforms affinely because the volume Jacobian is constant.

**Exact evidence and dependencies.** The complete Finch source capsule in immutable parent asg_9_3jUNaB9fDmUrfQOxs-5B7l (SHA243b10b026bbadf9b085000d4490d02db4f2273c1836e07188b407ad662a66ee), already fully read and durably journaled in six parts ending20:31:06, is the sole geometric input. Library supplementary FINCH3_RESULT.json and FINCH3_SOURCE.zip were materialized. Their embedded59545-character capsule matched SHA776bd3a4fa0abe64ede23fde3078f938a7df8d58117e320df8504ce428c6bccc; its210036-byte decompression matched SHA0ba9975c3b9c374c8b2b51f6cba4c2ec0328752136a1e93813fb6dd20eb26ad6. Every one of the44 extracted source files matched the literal capsule's expected map. This is byte identity for programmatic reuse, not an independent research audit. The exact clip auditor was run to obtain the new section geometry; its entire normalized report matched the parent's audit hash.

Input C182 raw.json:11449 bytes SHA3a3d80e75979c004f995115dd4bfb491560af0f661af0840c6868f3b5f046d86. Parent B.json:51790 bytes SHAcaf78ccee9abec82174d346227b2da7d99a13b823c88a4ef405e3e8cb9d1967d. Preferred generator and every dependency are in the existing capsule, so no old sandbox is needed.

**Reconstruction/verification.** Decode the already journaled FINCH3 capsule to a directory named finch3-source. Save the following entire source as check_shape.py (UTF-8, LF, final newline); run `python -B -S check_shape.py finch3-source --out shape-exact`, where the output directory must not already exist. CPython3.13.5; exact standard library and existing parent radial.py/check_B.py, assertions enabled. Observed marker `C182_EXACT_DISK_SLAB_AND_SEGMENT_CYLINDER_PASS`. check_shape.py is3640 bytes SHA27463970240605c6afbdbb739b8fb62e090d2f1beb98b2a60c5e9ed6c9f90c50. Reproduced SHAPE.json is1163 bytes SHA2b42ab3272257aa104fbb33619e7dd90b7321755a18b019610a7e42d5c10da83. Its strict minimum relative squared slacks floored after multiplying by10^12 are: disk4383572120, slab3857440131, segment894804655, cylinder12266356184. All positive.

```python
"""Exact section/slab and segment/cylinder certificates for Finch C182.
Requires the complete FINCH3 source capsule; source_root is its directory.
Uses only the Python standard library and the parent's exact clip auditor.
"""
import argparse, hashlib, json, sys
from fractions import Fraction as F
from pathlib import Path
sys.set_int_max_str_digits(0)
SCALE=10**12

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def encoded(x): return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def bind(b,spec):
    assert len(b)==spec['bytes'] and hashlib.sha256(b).hexdigest()==spec['sha256']
def floor12(x): return (x.numerator*SCALE)//x.denominator

def main():
    p=argparse.ArgumentParser();p.add_argument('source_root');p.add_argument('--out',required=True);a=p.parse_args()
    assert __debug__
    root=Path(a.source_root).resolve();sys.path[:0]=[str(root),str(root/'core')]
    import radial,check_B
    case=json.loads((root/'CASES.json').read_bytes())['C182_TWO_PLANE222']
    gb=(root/case['generator']).read_bytes();bind(gb,case['generator_info'])
    raw,_=radial.reconstruct(json.loads(gb))
    for i,row in case['replace'].items():raw['H'][int(i)]=row
    bind(encoded(raw),case['raw']);A=check_B.run(raw);bind(encoded(A),case['audit'])
    assert [A['V'],A['E'],A['F'],*A['counts'],*A['weak']]==[54,91,39,2,2,2,0,0,0]
    g=tuple(map(F,A['raw_centroid']));X=[tuple(F(t)-c for t,c in zip(v,g)) for v in A['raw_vertices']]
    H=[tuple(map(F,row[:3])) for row in raw['H']]
    d=[F(row[3])-dot(n,g) for n,row in zip(H,raw['H'])]
    assert all(t>0 for t in d)
    # Disk radius 31/400 in n-perp, slab halfwidth 7/400.
    n=(8,3,0);nn=dot(n,n);R=F(31,400);h=F(7,400)
    ds=[]
    for u,b in zip(H,d):
        projected=dot(u,u)-F(dot(u,n)**2,nn)
        assert projected>=0 and b*b>R*R*projected
        if projected:ds.append(b*b/(R*R*projected)-1)
    ss=[1-dot(n,x)**2/(h*h*nn) for x in X];assert min(ss)>0
    # Segment of half-length 363/1000 along m, cylinder radius 121/1000.
    m=(-7,12,100);mm=dot(m,m);L=F(363,1000);r=F(121,1000)
    ls=[]
    for u,b in zip(H,d):
        um=dot(u,m)
        assert b*b*mm>L*L*um*um
        if um:ls.append(b*b*mm/(L*L*um*um)-1)
    cs=[1-(dot(x,x)-dot(m,x)**2/F(mm))/(r*r) for x in X];assert min(cs)>0
    report={'object':'FINCH_C182_TWO_PLANE222_SECTION_CERTIFICATE','parent_case':'C182_TWO_PLANE222','parent_raw':case['raw'],'parent_audit':case['audit'],'centroid':'own exact uniform filled-volume centroid from parent clip audit','all_supplied_rows':len(H),'all_vertices':len(X),'census':[A['V'],A['E'],A['F'],*A['counts'],*A['weak']],
        'disk_slab':{'normal':n,'disk_radius':str(R),'slab_halfwidth':str(h),'radius_to_halfwidth':str(R/h),'minimum_disk_relative_squared_slack_floor_1e12':floor12(min(ds)),'minimum_slab_relative_squared_slack_floor_1e12':floor12(min(ss))},
        'segment_cylinder':{'axis':m,'segment_halflength':str(L),'cylinder_radius':str(r),'halflength_to_radius':str(L/r),'minimum_segment_relative_squared_slack_floor_1e12':floor12(min(ls)),'minimum_cylinder_relative_squared_slack_floor_1e12':floor12(min(cs))},
        'consequences':{'stable_facets_at_least':2,'unstable_vertices_at_least':2,'all_affine_images_with_condition_number_less_than_31_over_7_have_S_at_least':2,'all_affine_images_with_condition_number_less_than_3_have_U_at_least':2}}
    b=encoded(report);out=Path(a.out);out.mkdir(parents=True,exist_ok=False);(out/'SHAPE.json').write_bytes(b)
    print('C182_EXACT_DISK_SLAB_AND_SEGMENT_CYLINDER_PASS')
    print(b.decode());print('REPORT_BYTES_SHA256',len(b),hashlib.sha256(b).hexdigest())
if __name__=='__main__':main()
```

**Preserved discovery method.** The following complete bounded numerical program chose useful directions; it proves nothing by itself. NumPy2.3.5, SciPy1.17.0, CPython3.13.5, OPENBLAS_NUM_THREADS=1. Its inputs are exactly the parent's raw.json and B.json above, placed at /mnt/data/c182. Run `OPENBLAS_NUM_THREADS=1 python c182_section_search.py`. Disk optimum in chart(1,a,b) was approximately a=.375244971,b=-.0000965029968, R/h4.4493099157; rational direction(8,3,0) gives numerical R/h4.4468523160. Rod chart(a,b,1) gave approximately(-.07309344,.12249114), ratio3.0674257841. The rational direction and radius bounds in check_shape.py were then deliberately simplified and independently evaluated exactly; these approximate optima are not global proof claims.

```python
import json,numpy as np
from fractions import Fraction as F
from scipy.optimize import differential_evolution,minimize
A=json.load(open('/mnt/data/c182/B.json'));H=np.array(json.load(open('/mnt/data/c182/raw.json'))['H'],float);H=H[:,:3]/H[:,3:]
g=np.array([float(F(x)) for x in A['raw_centroid']]);P=np.array([[float(F(x)) for x in p] for p in A['raw_vertices']]);X=P-g;b=1-H@g

def metrics(n):
 n=n/np.linalg.norm(n);h=np.max(np.abs(X@n));r=np.min(b/np.linalg.norm(np.cross(H,n),axis=1));return h,r,r/h

def obj(t):return -metrics(np.r_[1.,t])[2]
r=differential_evolution(obj,[(.05,.65),(-.05,.05)],seed=182,maxiter=150,popsize=12,tol=1e-10,polish=True)
print('disk opt',r.x,metrics(np.r_[1,r.x]))
for n in [[94,34,1],[100,30,1],[1000,*np.rint(r.x*1000).astype(int)],[100,*np.rint(r.x*100).astype(int)]]:print('disk simple',n,metrics(np.array(n,float)))

def cylinder(n):
 n=n/np.linalg.norm(n);c=np.max(np.linalg.norm(np.cross(X,n),axis=1));L=np.min(b/np.abs(H@n));return c,L,L/c
r=differential_evolution(lambda t:-cylinder(np.r_[t,1.])[2],[(-.1,.1),(-.2,.2)],seed=183,maxiter=150,popsize=12,tol=1e-10,polish=True)
print('rod opt',r.x,cylinder(np.r_[r.x,1.]))
for n in [[0,0,1],[-4,8,100],[*np.rint(r.x*1000).astype(int),1000],[*np.rint(r.x*100).astype(int),100]]:print('rod simple',n,cylinder(np.array(n,float)))
```

The current record remains C622. No new own110 body is claimed by this shape certificate.
