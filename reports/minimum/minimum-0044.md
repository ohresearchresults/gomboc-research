# minimum-0044

AI research report · 2026-09-11 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

Resolved affirmatively for all six assigned literal canonical types286,287,289,290,291,292. Each has one fixed combinatorial boundary triangulation, chosen independently of the realization and before introducing auxiliary weights, on which full formal cycle moments of total degree at most2 force the common moments to be the genuine homogeneous volume moments. The proof includes the exceptional coplanarity strata. No counterexample or unresolved realization stratum remains for these six types.

The same argument also proves this statement for canonical284. Combining these seven results with the journaled288 positive types from C32_COFACIAL_L6_Q2_METHOD_V1 gives quadratic moment physicality for every canonical type0 through294. Canonical295 is not settled by this handoff, but it is already independently excluded whole. Consequently all180 types in the accepted whole-exclusion complement now admit a sufficient quadratic formulation. This does not add a C32 exclusion, increase the lower bound, or establish rigidity of every auxiliary cell mass.

I authenticated the immutable parent minimum-0043: restoring the Markdown's final LF and its compact version2 JSON envelope gives54473 bytes and SHA-256486ba862561f660c9592ca19853855a9fec58d59486048e4a62d863a84bc3882. Its catalogue reconstruction reproduced240929 bytes and SHA-256efb10a4657a891cd13f6f62db94164bd4b3005e908dc55aae87db450930f704d. All seven literal facet lists and true-edge lists below were checked against that catalogue. No parent, label, incidence, or alias conflict was found. The triangulations below are explicitly defined templates; they are not identifications with Q4 sphere IDs or the parent's MP9:45 sphere.

The useful change of approach was to examine four-apex equality classes instead of requiring three cofacial apices. Four noncoplanar apices immediately prevent a common fan density from jumping. The remaining difficulty was to handle four coplanar apices without a genericity assumption. The new geometric argument uses a connected path through the other boundary vertices to rule out the sole possible jump plane. Thus the journal's cofacial-method negatives retain their original meaning, while their full quadratic physicality question is resolved by additional geometry.

The precise moment statement is as follows. Let P=conv(x_0,...,x_8) be any real, full-dimensional convex realization of one of the seven literal maximal-face lattices in DATA in the source below, with all nine points actual vertices and exactly16 true edges. Use its specified triangulation Sigma, oriented outward. Let K be the set of distinct unordered four-sets containing a triangle of Sigma. Retain every column of the formal boundary matrix B=boundary_3, including geometrically flat cells. Assign one common real mass w_T to each T in K, with w_T=0 for flat T. For sorted T=(i_0,i_1,i_2,i_3), put Delta_T=det(x_i1-x_i0,x_i2-x_i0,x_i3-x_i0) and z_T=sign(Delta_T)w_T, with z_T=0 when Delta_T=0. Let mu_T be uniform probability measure on the tetrahedron; its moment formulas have the usual barycentric polynomial continuation on flat cells.

Write s_T=sum_{i in T}x_i and R_T=sum_{i in T}x_i x_i^T. The COMPLETE degree-at-most2 assumptions are, for every beta in the full formal ker B,

```
sum_T beta_T z_T = 0,
sum_T beta_T z_T s_T = 0,
sum_T beta_T z_T (s_T s_T^T + R_T) = 0.
```

The vector equation retains all three components and the symmetric tensor equation all six components. These are exactly all ten polynomial moment identities, since mu_T(x)=s_T/4 and mu_T(xx^T)=(s_T s_T^T+R_T)/20. The same T has the same w_T in every fan and cycle occurrence. These assumptions are stronger than degree2 fanagreement alone, and the proof uses that stronger hypothesis.

For every vertex a, let nu_a be its fan measure, the sum of w_T mu_T over its nonflat fan cells. If M=nu_a(1), then M is independent of a and

```
nu_a(p) = (M/Vol(P)) integral_P p(x) dx
```

for every a and every polynomial p of total degree at most2. In particular, at common mass1 the common first and second moments are the true probability moments of P. A common first moment0 then means that0 is the ordinary homogeneous volume centroid of P; the common second moment is its actual covariance tensor. There is no assertion here about all higher moments of every fan or uniqueness of all auxiliary masses.

A general physical theorem underlying the result is worth preserving. For a fixed boundary triangulation of any convex three-polytope, let L_{q+4} be the span of formal cycles supported on at most q+4 vertices. Suppose an apex class A with at least three vertices satisfies f_a-f_b in L_{q+4} for all a,b in A, where f_a is the formal apex fan. Suppose also that, for every vertex set S containing A and meeting every actual maximal facet in at most two vertices, deleting S leaves the graph of the boundary triangulation connected. Then full formal cycle moments through degree q force common homogeneous moments through degree q. Cofacial classes are included: when A contains a cofacial triple there is no such S. The seven certificates below use a particularly simple instance: incidence forces the only possible S to equal A, and a displayed path connects its complement.

Here is the complete analytic proof, including the coplanar branch.

1. For a tetrahedron, its normalized Dirichlet transform is

   `integral (1-u·x)^(-4) dmu_T(x) = product_{i in T}(1-u·x_i)^(-1)`.

   This follows by integrating the monomial expansion in barycentric coordinates. For a cycle supported on a vertex set W with at most6 elements, multiply the transform of its signed measure by `product_{i in W}(1-u·x_i)`. The resulting numerator has degree at most |W|-4, hence at most2. Its Taylor coefficients through degree2 vanish by the full moment assumptions; the denominator has constant term1. The numerator is therefore identically zero. All moments of the compactly supported signed measure vanish, so polynomial density implies that the measure itself is zero. The same argument uses degree q for at most q+4 vertices. Flat columns stay formal throughout; their assigned zero masses simply contribute zero measure.

2. The exact certificate proves f_a-f_b lies in L6 for the selected four apices A. Thus those four fans have one identical signed measure nu and one common piecewise constant density rho on P. This conclusion is equality as actual measures in all degrees for these selected fans, not merely their quadratic fanagreement.

3. Any interior jump plane of rho must contain every apex in A. Choose a generic point in an open jump patch, avoiding the intersections of the finitely many cell-face planes. That patch must be an internal boundary of every selected fan. Every internal face plane of an apex fan contains its apex: the opposite triangle of a cone lies on the actual boundary of P. If A is noncoplanar, no common jump plane exists, so rho is constant.

4. If A is coplanar, its plane H is unique because three distinct extreme vertices of a convex polytope cannot be collinear. Each certificate has at most two members of A on any actual facet. Hence H cannot be supporting. For each v outside A the certificate gives an actual facet containing v and two members of A. If v also lay in H, those three noncollinear points would identify that supporting facet plane with H, forcing every member of A onto that facet, contrary to the literal maximal-face lattice. Consequently H contains exactly the four vertices A, and the other five vertices lie strictly on its two sides, with both signs present.

5. The certified complement path contains an edge uv with endpoints on opposite sides of H. Choose a boundary triangle tau containing uv and let F be its actual supporting facet. Choose a in A outside F; this is possible because F contains at most two members of A. The cone conv(x_a,tau) is a nonflat tetrahedron of the selected apex fan, and its interior meets both open sides of H. It is essential here to choose a outside the ACTUAL FACET, not just outside tau.

6. H is the only possible jump plane, so rho has one constant value on each connected open half P-interior intersect H-positive and P-interior intersect H-negative. Yet the interior of the one tetrahedron from step5 crosses both halves and has one constant cell density. The two constants must agree. Thus rho is constant throughout the interior of P, including the coplanar branch. In the general criterion, let S be all vertices in H; an internal H meets each supporting facet in at most two vertices, and the same connected-complement argument applies.

7. Every other fan difference f_b-f_a belongs to the FULL formal ker B because all formal fans have boundary Sigma. The full degree2 cycle identities therefore transfer the uniform measure's moments through degree2 to all nine fans, proving the displayed conclusion.

8. The hypotheses are necessary for actual homogeneous masses. Taking `w_T=abs(Delta_T)/(6 Vol(P))` gives the body's actual normalized tetrahedron masses. Signed polynomial integrals over any formal cycle vanish by Stokes. For a homogeneous polynomial p of degree k, one may use the vector field x p(x)/(3+k), whose divergence is p. Cofacial tetrahedra contribute zero. Thus the fixed triangulation may be selected before any auxiliary weights; there is no flip or transfer of arbitrary weights in this argument.

All used flat cells are determined by the actual face lattice, not a generic-coordinate test. A used cell contains a genuine boundary triangle in an actual facet F. Its fourth vertex makes it flat exactly when that vertex belongs to F. No other zero-volume stratum for a used cell is possible. Incidental coplanarity of four-sets that are not used cells is allowed, and the argument above explicitly covers coplanarity of A. No chosen affine frame, coordinate minor, rational-coordinate restriction, mass positivity assumption, or conditioning bound is imposed.

The fixed triangulations and certificates are:

| Types | Template | Four apices A | Complement path |
|---|---|---|---|
|286,287,289,291|Sigma A|1246|0-3-7-8-5|
|290,292|Sigma B|0348|1-5-2-6-7|
|284, supplementary|Sigma C|2357|4-1-0-6-8|

```
Sigma A = 012 013 023 125 134 148 158 236 258 268 347 367 478 678
Sigma B = 012 013 026 036 125 134 148 158 256 347 367 467 468 568
Sigma C = 012 013 026 036 125 137 145 147 256 367 457 568 578 678
```

Every path edge for the six assigned types is a true edge. For supplementary284,06 is a boundary triangulation diagonal within actual facet0362. It is valid in the density argument because it belongs to a genuine boundary triangle. It is explicitly distinguished from the16 true edges and is not used as a mechanical escape.

The exact finite results are:

| Type | Formal tetrahedron columns | Boundary rows | Boundary rank | Full kernel dimension | L6 dimension | Flat columns |
|---|---:|---:|---:|---:|---:|---:|
|284|65|84|51|14|10|5|
|286|65|84|51|14|10|5|
|287|65|84|51|14|10|7|
|289|65|84|51|14|10|7|
|290|64|84|51|13|9|5|
|291|65|84|51|14|10|7|
|292|64|84|51|13|9|7|

These are exact formal chain-complex computations, not ranks sampled on geometric coordinates. The source checks each polygon triangulation by ear removal, unique actual-facet ownership of all14 triangles, all16 true edges, exactly5 added diagonals, consistent sphere orientation and every vertex link. It computes the full formal kernel and all84 kernels obtained by omitting three vertices, verifies their inclusion, verifies every fan boundary and all full-kernel fan differences, and verifies the three independent selected-apex differences lie in L6. Only afterward does it identify the flat columns. It also checks every outside-plane incidence blocker and the complete complement path.

The self-contained recovery capsule is C32_Q2_CONNECTED_COMPLEMENT_V1. Save the entire source below as c32_q2_connected_complement.py, UTF-8 with LF line endings and its final LF. The normative executed environment was CPython3.12.14, standard library only, assertions enabled. There are no external input files, numerical libraries, random choices, coordinate seeds, or hidden parameters. DATA contains every literal actual facet; consecutive pairs around those cycles reconstruct the complete true-edge sets. SIGMA, APICES and PATHS contain all chosen witnesses. The full formal cells, complete cycle kernels, zero-cell lists and facet ownership are reconstructed deterministically.

Run:

```
PYTHONHASHSEED=0 python -S c32_q2_connected_complement.py > run.log
```

Observed pins:

| Artifact | Bytes | SHA-256 |
|---|---:|---|
|c32_q2_connected_complement.py|8511|1dc25bd4159aa613f6d279d0ae664ae5676a426848fc573c556eadc2de7f6b93|
|c32_q2_connected_complement.json|15497|483cb5bbc2694938954e66110513f1af21b9b9596afcf8cf42b00333b1a0f357|
|run.log|846|03cba2829f6cb18ac0068c115f69058b53ada0fbd6404b2a891cfe065c7e333b|

The terminal marker is `ALL_SEVEN_LITERAL_C32_Q2_CONNECTED_COMPLEMENT_PASS`. Clean-directory replays with different hash seeds produced byte-identical JSON and logs. The generated JSON is a convenience certificate; the following complete source, the analytic proof and literal inputs are sufficient without downloading it.

```python
"""C32_Q2_CONNECTED_COMPLEMENT_V1. CPython >=3.10, standard library only.
Run: python -S c32_q2_connected_complement.py
Literal labels: qvo minimum-0043,
SHA256 486ba862561f660c9592ca19853855a9fec58d59486048e4a62d863a84bc3882.
Formal flat columns are retained in every boundary/kernel computation.
"""
from fractions import Fraction as Q
from itertools import combinations
from collections import Counter, deque
from pathlib import Path
import hashlib, json
assert __debug__
PARENT = ['minimum-0043',
          '486ba862561f660c9592ca19853855a9fec58d59486048e4a62d863a84bc3882']
DATA = {
284:'013 0251 0362 1473 154 2685 376 4587 678',
286:'013 0251 0362 1473 1584 2685 376 487 678',
287:'013 0251 0362 143 15874 2685 347 376 678',
289:'013 0251 0362 143 1584 26785 347 376 487',
290:'013 0251 0362 143 1584 2685 347 376 4867',
291:'013 0251 03762 143 1584 2685 347 487 678',
292:'013 0251 03762 143 1584 265 347 4867 568'}
SIGMA = ['012 013 023 125 134 148 158 236 258 268 347 367 478 678',
         '012 013 026 036 125 134 148 158 256 347 367 467 468 568',
         '012 013 026 036 125 137 145 147 256 367 457 568 578 678']
APICES = [(1,2,4,6),(0,3,4,8),(2,3,5,7)]
PATHS = [(0,3,7,8,5),(1,5,2,6,7),(4,1,0,6,8)]

def parse(s): return tuple(tuple(map(int,t)) for t in s.split())
def parity(t):
    return (-1)**sum(t[i]>t[j] for i in range(len(t)) for j in range(i+1,len(t)))
def boundary(t):
    return {t[:i]+t[i+1:]:Q((-1)**i) for i in range(len(t))}
def plus(dst,src,c=Q(1)):
    for i,x in src.items():
        y=dst.get(i,Q(0))+c*x
        if y: dst[i]=y
        else: dst.pop(i,None)
def image(columns,v):
    out={}
    for j,x in v.items(): plus(out,columns[j],x)
    return out
class Basis:
    def __init__(self): self.pivots={}
    def reduce(self,v):
        v={i:Q(x) for i,x in v.items() if x}
        for p in sorted(self.pivots):
            if p in v: plus(v,self.pivots[p],-v[p])
        return v
    def add(self,v):
        v=self.reduce(v)
        if not v:return False
        p=min(v);a=v[p]
        self.pivots[p]={i:x/a for i,x in v.items()}
        return True

def kernel(columns):
    pivots={};out=[]
    for j,col in enumerate(columns):
        v=dict(col);rel={j:Q(1)}
        for p in sorted(pivots):
            if p in v:
                a=v[p];w,r=pivots[p]
                plus(v,w,-a);plus(rel,r,-a)
        if v:
            p=min(v);a=v[p]
            pivots[p]=({i:x/a for i,x in v.items()},
                       {i:x/a for i,x in rel.items()})
        else:out.append(rel)
    assert len(pivots)+len(out)==len(columns)
    assert all(not image(columns,z) for z in out)
    independent=Basis()
    assert all(independent.add(z) for z in out)
    return out,len(pivots)

def polygon_check(p,ts):
    """Exact ear-removal certificate of a straight convex-polygon triangulation."""
    assert len(ts)==len(p)-2 and len(set(ts))==len(ts)
    assert all(len(t)==3 and set(t)<=set(p) for t in ts)
    if len(p)==3:
        assert ts==(tuple(sorted(p)),);return
    ears=[(i,tuple(sorted((p[i-1],p[i],p[(i+1)%len(p)]))))
          for i in range(len(p))]
    ears=[(i,t) for i,t in ears if t in ts and sum(p[i] in q for q in ts)==1]
    assert ears
    i,t=ears[0]
    polygon_check(p[:i]+p[i+1:],tuple(q for q in ts if q!=t))

def surface_orientation(fs):
    ef={}
    for i,t in enumerate(fs):
        for e,s in boundary(t).items():ef.setdefault(e,[]).append((i,s))
    assert all(len(v)==2 for v in ef.values())
    signs={0:1};queue=deque([0])
    while queue:
        i=queue.popleft()
        for e,s in boundary(fs[i]).items():
            (a,sa),(b,sb)=ef[e]
            j,t=(b,sb) if a==i else (a,sa)
            want=-signs[i]*s/t
            if j in signs:assert signs[j]==want
            else:signs[j]=want;queue.append(j)
    assert len(signs)==len(fs)
    return [Q(signs[i]) for i in range(len(fs))],set(ef)

def certify(kind,facet_text):
    fac=parse(facet_text);k=2 if kind==284 else int(kind in (290,292))
    fs=parse(SIGMA[k]);A=APICES[k];path=PATHS[k]
    assert len(fac)==9 and len(fs)==14 and list(fs)==sorted(fs)
    true={tuple(sorted((f[i-1],f[i]))) for f in fac for i in range(len(f))}
    assert len(true)==16 and set().union(*map(set,fac))==set(range(9))
    incidence=Counter(tuple(sorted((f[i-1],f[i]))) for f in fac for i in range(len(f)))
    assert set(incidence.values())=={2}
    assignment=[]
    for t in fs:
        owners=[i for i,f in enumerate(fac) if set(t)<=set(f)]
        assert len(owners)==1;assignment.append(owners[0])
    for i,f in enumerate(fac):
        polygon_check(f,tuple(t for t,o in zip(fs,assignment) if o==i))
    orient,edges=surface_orientation(fs)
    assert true<=edges and len(edges)==21 and len(edges-true)==5
    for v in range(9):
        link=[tuple(x for x in t if x!=v) for t in fs if v in t]
        degrees=Counter(x for e in link for x in e)
        assert set(degrees.values())=={2}
        reached={min(degrees)}
        while True:
            new=reached|{x for e in link if set(e)&reached for x in e}
            if new==reached:break
            reached=new
        assert reached==set(degrees)
    # For four coplanar A vertices H cannot contain any additional vertex:
    # each outside v has a true facet containing v and two A vertices;
    # three distinct extreme vertices are noncollinear.
    assert len(A)==4 and all(len(set(f)&set(A))<=2 for f in fac)
    assert set(path)==set(range(9))-set(A) and len(path)==5
    assert all(tuple(sorted(e)) in edges for e in zip(path,path[1:]))
    blockers=[]
    for v in sorted(set(range(9))-set(A)):
        choices=[(i,tuple(sorted(set(f)&set(A)))) for i,f in enumerate(fac)
                 if v in f and len(set(f)&set(A))==2]
        assert choices
        i,pair=choices[0];blockers.append([v,i,list(pair)])
    cells=sorted({tuple(sorted((*t,a))) for t in fs for a in range(9) if a not in t})
    ci={t:i for i,t in enumerate(cells)}
    triples=list(combinations(range(9),3));ri={t:i for i,t in enumerate(triples)}
    columns=[{ri[t]:x for t,x in boundary(c).items()} for c in cells]
    full,rank=kernel(columns)
    short=Basis();omission=[]
    for omitted in combinations(range(9),3):
        ids=[i for i,t in enumerate(cells) if not set(t)&set(omitted)]
        kk,r=kernel([columns[i] for i in ids]);omission.append([list(omitted),len(ids),r,len(kk)])
        for z in kk:
            zz={ids[j]:x for j,x in z.items()}
            assert not image(columns,zz);short.add(zz)
    target={ri[t]:orient[i] for i,t in enumerate(fs)}
    fans=[]
    for a in range(9):
        fan={ci[tuple(sorted((a,*t)))]:orient[i]*parity((a,*t))
             for i,t in enumerate(fs) if a not in t}
        assert image(columns,fan)==target;fans.append(fan)
    for fan in fans:
        diff=dict(fan);plus(diff,fans[0],-1)
        assert not image(columns,diff)
    for a in A[1:]:
        diff=dict(fans[a]);plus(diff,fans[A[0]],-1)
        assert not short.reduce(diff)
    # Only now identify the geometrically forced zero masses; no column was deleted.
    flat=[list(t) for t in cells if any(set(t)<=set(f) for f in fac)]
    result=dict(id=kind,facets=fac,triangles=fs,triangle_facets=assignment,
                apices=A,complement_path=path,
                path_edge_is_true=[tuple(sorted(e)) in true for e in zip(path,path[1:])],
                outside_plane_blockers=blockers,
                true_edges=sorted(true),diagonals=sorted(edges-true),
                formal_cells=len(cells),boundary_rows=len(triples),boundary_rank=rank,
                full_kernel_dim=len(full),L6_dim=len(short.pivots),flat_cells=flat,
                omission_dimensions=omission)
    print('TYPE',kind,'CELLS',len(cells),'FULL_KERNEL',len(full),'L6',len(short.pivots),
          'FLAT',len(flat),'CONNECTED_COMPLEMENT_Q2_CERTIFICATE_PASS')
    return result

def main():
    result=dict(identity='C32_Q2_CONNECTED_COMPLEMENT_V1',parent=PARENT,
                scope='Quadratic common homogeneous moment physicality; no C32 exclusion.',
                records=[certify(i,s) for i,s in sorted(DATA.items())])
    b=(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n').encode('ascii')
    name='c32_q2_connected_complement.json';Path(name).write_bytes(b)
    print('OUTPUT',name,len(b),hashlib.sha256(b).hexdigest())
    b=Path(__file__).read_bytes()
    print('SOURCE',len(b),hashlib.sha256(b).hexdigest())
    print('ALL_SEVEN_LITERAL_C32_Q2_CONNECTED_COMPLEMENT_PASS')
if __name__=='__main__':main()
```

The remaining uncertainty is outside the assigned six-type question: this handoff does not determine quadratic physicality for295, degree1 sufficiency, or complete auxiliary-mass rigidity. It does not extend to a lower-dimensional hull, nonvertices, a changed maximal-face lattice, or a system using unrelated tetrahedron coordinates or separately fitted Gram matrices.

The useful continuation is to replace the six exceptional degree3 requirements in the current physical C32 pipeline with the fixed quadratic systems specified here, retaining one realized geometry, one shared tetrahedron mass family, all formal flat columns, zero flat masses and all ten cycle moment components. The accepted whole116 register remains unchanged. Further whole-type or root exclusions must still come from additional physical arguments; this theorem supplies the missing justification that the common normalized moments and imposed zero center in those quadratic systems are the body's actual homogeneous moments and own centroid.
