# figure-0353

AI research report · 2026-09-09 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Original-proof and applicability dossier — Sharp Lynx 90

## 1. Verdict

**The two nine/nine claims remain unverified, not refuted.** No original theorem or literal parallel-run certificate establishing either `V>=9` or `F>=9` for uniform filled polyhedra at their own volume centroid was recovered. The supplied journal itself records this exact evidence gap and makes the prohibition on below-32 construction independent of its resolution. That prohibition remains in force. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

**The published homogeneous exclusion has now been independently checked:** I reconstructed its entire `V<=6` case family, generated replacement rational certificates, and verified every one of its **5,943** cases, plus **16 tetrahedron cases**, using integer/rational arithmetic. The complete certificate and executable recovery capsule are below. They establish **V>=7**, not V>=9.

For the specified strict target, the strongest unconditional conclusion established by the material actually recovered and the replay here is

\[
V\ge7,\qquad F\ge6,\qquad C\ge22.
\]

The face statement in this line is a combinatorial consequence of the vertex statement, **not an independently established monostability face theorem**. It does not change the user's construction search boundary `C>=32`.

| Proposition | Evidence and justified scope |
|---|---|
| Filled homogeneous, mono-unstable: `V>=7` | Original Theorem 1 of Bozóki–Domokos–Papp–Regős; independently replayed here. |
| Filled homogeneous, monostable: `V,F>=5` | Homogeneous tetrahedron exclusion; also follows from the tetrahedron portion of this replay and the special simplex polarity argument below. |
| Filled homogeneous, mono-monostatic: `V>=7,F>=6` | Inherits the mono-unstable exclusion and Euler/degree inequalities. |
| Filled homogeneous, mono-monostatic: `V>=9` | Original proof/certificate not recovered. |
| Filled homogeneous, mono-monostatic: `F>=9` | Original proof/certificate not recovered; no justified general polarity transfer. |
| Equal unit masses at vertices, mono-unstable: `V>=11,F>=8` | A different, precisely identified theorem. Its centroid equation is inapplicable to general filled solids. |

The primary references supporting the source-derived entries are identified immediately below; the exact replay and elementary deductions are proved in Sections 3–5.

## 2. Source and provenance audit

### A. The actual homogeneous lower-bound paper

S. Bozóki, G. Domokos, D. Papp and K. Regős, **The smallest mono-unstable, homogeneous convex polyhedron has at least 7 vertices**, arXiv:2401.17906v2, 5 June 2024.

Primary URLs:
- https://arxiv.org/html/2401.17906v2
- https://arxiv.org/pdf/2401.17906v2

**Theorem 1, printed p. 2, says seven, not nine.** The relevant proof locations are Theorem 7, p. 5; Theorem 8, pp. 6–7; Section 4.1, p. 8; Algorithm 2, p. 10; and Section 5/Table 1, pp. 11–12. Section 6, p. 12, explicitly leaves some seven-vertex systems unresolved: about 99% are excluded, while the others have an inconclusive SDP result. Thus this source does not establish even `V>=8`, let alone nine/nine. :contentReference[oaicite:2]{index=2}

### B. The original public computational supplement

Primary URLs:
- https://github.com/dpapp-github/mono-unstable/tree/main/homogeneous
- https://raw.githubusercontent.com/dpapp-github/mono-unstable/main/homogeneous/mono-unstable_homogeneous_56.nb
- https://github.com/dpapp-github/mono-unstable/blob/main/homogeneous/cases56.csv.zip

I read the original notebook, including its case generator, SDP construction, `Rationalize[...,10^-8]`, and exact verification cells. Its public case archive concerns **five and six vertices**. The notebook's cached large solution output is explicitly shortened with `Missing["NotStored"]`; it is not a complete printed multiplier table. I did **not** execute Mathematica or claim to recover those missing cached rows. Instead, the capsule below supplies new, complete small rational multipliers for the same case family. It needs neither Mathematica nor the external CSV. :contentReference[oaicite:3]{index=3}

### C. The 11-vertex/8-face result is a 0-skeleton theorem

D. Papp, K. Regős, G. Domokos and S. Bozóki, **The smallest mono-unstable convex polyhedron with point masses has 8 faces and 11 vertices**, arXiv:2302.04252v2; European Journal of Operational Research 310(2), 511–517, DOI 10.1016/j.ejor.2023.04.028.

Primary URLs:
- https://arxiv.org/html/2302.04252v2
- https://arxiv.org/pdf/2302.04252v2
- https://github.com/dpapp-github/mono-unstable/tree/main/0-skeletons

Theorem 3, printed p. 4, and Theorem 4, p. 5, concern **mono-unstable 0-skeletons**. Theorem 7, p. 7, starts with the essential equation `sum_i r_i=0`; p. 4 defines the model as one unit mass per vertex. The `F>=8` statement on p. 5 follows from `V>=11` and polyhedral combinatorics, not from a separate homogeneous face exclusion. The earlier `V>=8` result is explicitly restated as Theorem 5 for the same 0-skeleton model. :contentReference[oaicite:4]{index=4}

The concrete applicability failure is the substitution `r_V=-sum_{i<V}r_i` in that proof. A filled body's centroid is a **volume-weighted average of tetrahedron centroids**, not generally the average of its vertices. Changing to the filled centroid changes the equilibrium inequalities themselves. No part of this dossier imports the 0-skeleton certificates into the filled-density problem.

### D. The precise polarity result

G. Domokos, F. Kovács, Z. Lángi, K. Regős and P. T. Varga, **Balancing polyhedra**, arXiv:1810.05382v3; Ars Mathematica Contemporanea 19 (2020), 95–124.

Primary URLs:
- https://arxiv.org/html/1810.05382v3
- https://arxiv.org/pdf/1810.05382v3

Theorem 4, printed p. 5, excludes homogeneous monostatic tetrahedra. **Lemma 3, p. 10, preserves the zero homogeneous centroid under polarity for a simplex. Lemma 4, pp. 10–11, exchanges equilibrium features at the specified origin for a general polytope.** These are different assertions: Lemma 4 does not say that the polar's ordinary-volume centroid is that origin. A nine-vertex bound cannot therefore be converted into a nine-face filled-density bound by invoking that lemma alone. :contentReference[oaicite:5]{index=5}

### E. The September 2026 preprint is an upper-bound construction

T. Schettini Gherardini, **An explicit mono-monostatic polyhedron**, arXiv:2609.07827v1.

Primary URL: https://arxiv.org/html/2609.07827v1

Theorem 1.1 reports a particular homogeneous own-centroid example with `V=113888,E=170832,F=56946`. It is not a nine/nine exclusion. Its introduction expressly separates unit-vertex-mass results from the homogeneous problem. I checked this theorem's stated scope, not its large construction certificate; no new audit or priority claim about that object is made here. Note its signature order `(S,H,U)`, unlike the journal's `(S,U,H)`. :contentReference[oaicite:6]{index=6}

### F. What the available private sources did and did not contain

Independent Library searches for the literal nine/nine claims, the parallel minimum investigation, and the historical counts returned copies of the supplied construction journal, not the original minimum proof. The subsequent complete metadata listing exposed eight journal files and two images, with `has_more=false`; it exposed no separate certificate archive. This is an access finding, not a claim that the user's parallel investigation never produced a proof. :contentReference[oaicite:7]{index=7} :contentReference[oaicite:8]{index=8} :contentReference[oaicite:9]{index=9}

The historical digest mentions `139636 -> 1714/869 -> 5341` and a `V8` investigation with `3237069 / 24835 / 17253 / 207036` counts, but explicitly labels them unverified historical claims. No literal matrix collection or exhaustive terminal certificate for those claims was recovered. The later **139,636** seven-vertex enumeration is expressly a case count, not an exclusion certificate. These numbers cannot be promoted to `V>=9`. :contentReference[oaicite:10]{index=10} :contentReference[oaicite:11]{index=11}

One exact recovery pointer in the digest is the host-local archive
`/REDACTED_HOME/.pro-research-minimum/backups/20260907-journal-prefix-compaction-LcSYUS/research-journal.full.md`.
It is not an available sandbox file, and the pointer does not establish that its contents include the later nine/nine proof. No missing assignment ID or immutable payload has been invented. :contentReference[oaicite:12]{index=12}

## 3. Reconstructed necessary system and its density/degeneracy scope

The source's proof-critical ingredients are adjacent shadow inequalities and one tetrahedron-centroid inequality. The following gives an explicit reconstruction, including a combinatorial triangulation argument that avoids relying on a perturbation preserving equilibrium counts. :contentReference[oaicite:13]{index=13}

Translate the **actual filled-volume centroid** to zero and normalize the unique unstable vertex to `r_0=(1,0,0)` by a rotation and positive uniform scaling. For each other vertex choose an adjacent parent `p(i)` satisfying

\[
q_i=\lVert r_i\rVert^2-r_i\cdot r_{p(i)}\le0. \tag{1}
\]

This is necessary: if every edge direction at `r_i` had strictly negative dot product with `r_i`, the entire tangent cone would lie strictly behind the vertex orthoplane, making `r_i` unstable. Moreover,

\[
0<\lVert r_i-r_{p(i)}\rVert^2
\le\lVert r_{p(i)}\rVert^2-\lVert r_i\rVert^2.
\]

Thus chosen arrows cannot cycle. With only the root lacking an outgoing arrow, they form a rooted spanning tree.

**Nonsimplicial coverage without moving any point.** Triangulate each maximal polygonal face with diagonals and no new vertices. This produces a maximal planar graph containing every original true edge. The selected shadow tree therefore remains available. Cone the root to every boundary triangle not containing it. The positive-volume tetrahedra partition the body's volume; triangles in a root-incident original face may give zero-volume tetrahedra and can be ignored for integration. Since the volume centroid is zero, at least one positive-volume tetrahedron `T={0,a,b,c}` has nonpositive first-coordinate centroid. Consequently

\[
L=1+x_a+x_b+x_c\le0. \tag{2}
\]

The generator includes every possible choice of that triangle. Artificial face diagonals are used only for case enumeration and integration, never reclassified as true mechanical edges.

This proves coverage of **all full-dimensional convex realizations** in the enumerated vertex range, including coplanar polygonal faces and nonsimple vertices. Weak shadow inequalities include equality. No lower bound on shape thickness, no rational-coordinate restriction, and no positive geometric margin are assumed. The user's strict no-degeneracy target is consequently covered. Collapsed lower-dimensional sets and repeated/nonextreme purported vertices are not alternative polyhedra under this model.

This argument is **not** a face-count-preserving perturbation and is **not** a claim that triangulation preserves monostability as a new physical polyhedron. It cannot silently justify a fixed-`F` exclusion.

### A smaller exact certificate matrix

For a tree and its three marked nonroot vertices, choose positive weights `w_i` and give (2) weight one. Let

\[
H_{ii}=w_i,\qquad H_{i,p(i)}=H_{p(i),i}=-w_i/2\quad(p(i)\ne0),
\]

with other off-diagonal entries zero, and

\[
b_i=\mathbf1_{i\in\{a,b,c\}}-w_i\mathbf1_{p(i)=0},\qquad
K=\begin{pmatrix}1&b^T/2\\ b/2&H\end{pmatrix}.
\]

Writing the nonroot coordinate columns as `x,y,z`, direct expansion gives

\[
\sum_i w_iq_i+L
=(1,x)^TK(1,x)+y^THy+z^THz.
\]

Therefore **`K` positive definite is a complete, exact infeasibility certificate** for (1)–(2). It uses an `n x n` matrix instead of a `3(n-1)+1` augmented matrix. The reduction is independently checked below by separately expanding the full three-coordinate matrix and applying rational Schur elimination.

The necessary system depends only on the rooted tree and the set of three marked vertices, not on the rest of the ambient graph. Canonicalizing these marked trees is an exact algebraic duplicate reduction, not a geometric symmetry assumption. For the original 5,943 cases there are **26 five-vertex and 134 six-vertex** marked-tree types. Four additional types cover the tetrahedron cases.

## 4. Complete finite coverage and executed results

There is one maximal planar graph on five vertices and two on six. Here is a short completeness proof, so the enumeration need not trust a graph database. A spherical triangulation has degree sum `6n-12`. For `n=5`, it has a degree-three vertex; deleting that vertex gives `K4`, and reinsertion into a triangular face gives the triangular bipyramid. For `n=6`, either a degree-three vertex can be deleted, giving the five-vertex bipyramid, whose faces form one automorphism orbit, or all degrees are four, giving `K6` minus a perfect matching. Thus the literal face lists below cover all cases. The program also verifies the root-orbit coverage using all label permutations.

| Graph/root representatives in the capsule's labels | Rooted trees per root | Root-to-boundary tetrahedra | Raw cases |
|---|---:|---:|---:|
| Tetrahedron, root 1 | 16 | 1 | 16 |
| Triangular bipyramid, roots 1 and 3 | 75 | 3, 2 | 375 |
| Regular octahedron, root 1 | 384 | 4 | 1,536 |
| Other six-vertex triangulation, roots 1, 2 and 5 | 336 | 4, 5, 3 | 4,032 |

The last three rows reproduce **5,943/5,943** original cases, not merely a sample. Every raw case is assigned its actual pulled-back rational certificate and checked by positive leading principal determinants. Separately, all **164** canonical cases receive a full-coordinate rational positive-definiteness check. The new multipliers have denominators only **1, 2 or 8** and numerators at most **35**. No numerical optimization status enters acceptance. Both arithmetic checks were written in this assignment; this is reproducible coefficient/linear-algebra cross-checking, not external peer review or proof-assistant formalization.

Executed terminal output:

```text
EXACT_FILLED_VOLUME_V_GE_7_REPLAY_PASS
raw_cases_V4 = 16
raw_cases_V5 = 375
raw_cases_V6 = 5568
canonical_certificates = 164
minimum_integer_leading_minor = 2
certificate_records_sha256 = 587a697822eb834ebeca3e3b2d8b023f797005fcda21c26544b33768f126289d
```

The integer-minor value refers to the deliberately scaled certificate matrices; it is not a physical robustness margin. Numerical proposals used Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0. **Exact recovery and verification require only the complete standard-library capsule below**, whose frozen multipliers remove any solver/version dependence from the proof.

### Independent monostability/tetrahedron deduction

The 16-case replay establishes that a homogeneous tetrahedron cannot be mono-unstable. For a tetrahedron with centroid zero, its four vertices satisfy `sum r_i=0`. Write its polar vertices as `q_i`, where `q_i dot r_j=1` for `j!=i`; then `q_i dot r_i=-3`. Consequently every `r_j` is orthogonal to `sum q_i`, so `sum q_i=0`: the polar tetrahedron also has its own filled centroid at zero.

For `P={x:q_f dot x<=1}`, the foot on face `f` is `q_f/||q_f||^2`. Its strict inclusion in that face is equivalent to `q_f dot q_g<||q_f||^2` for all other `g`, exactly the strict unstable-vertex condition for `q_f` in the polar. Hence a homogeneous monostable tetrahedron would yield a homogeneous mono-unstable tetrahedron, already excluded. This supplies the independent `S=1` tetrahedron obstruction; the special sum identity is why this argument does **not** generalize to arbitrary polyhedra.

## 5. The precise remaining nine/nine gap

**For `V>=9`:** the missing proof must exclude the seven- and eight-vertex cases for the **joint** homogeneous condition `S=U=1`, unless it proves the stronger mono-unstable assertion. Those are different objectives. A proof using `S=1` may be perfectly valid even where a mono-unstable-only relaxation survives. The located 2024 proof and its 5,943 cases stop before these exclusions; the 139,636 seven-vertex case count does not supply their missing terminal certificates.

**For `F>=9`:** the missing proof must be genuinely applicable to a filled body's own centroid. A bound on vertices alone does not supply it. Using `V<=2F-4`, the still-unexcluded face ranges under the replayed `V>=7` are `F=6` with `V=7..8`, `F=7` with `V=7..10`, and `F=8` with `V=7..12`. Even if the parallel `V>=9` proof is supplied, `F=7,V=9..10` and `F=8,V=9..12` still need coverage. An eight-vertex enumeration is therefore not an independent eight-face exclusion.

A fixed-face proof also must cover maximal polygonal faces and non-simple contacts, or have a reduction that demonstrably preserves its face bound and the required mass condition. The vertex-preserving triangulation argument in Section 3 does not do that. Neither unit-vertex-mass certificates nor equilibrium duality at a freely specified origin fills this gap.

For any full-dimensional convex 3-polytope, Euler and minimum vertex degree give

\[
V-E+F=2,\qquad 3V\le2E,\qquad V\le2F-4.
\]

For the requested `(S,U,H)=(1,1,0)` target,

\[
C=V+E+F-2=2E=2(V+F-2).
\]

Thus **if both original nine/nine propositions are validated**, then

\[
\boxed{C\ge2(9+9-2)=32.}
\]

Equality would require `V=F=9,E=16`; it is not supplied by that inequality. **No exact-minimum or attainment claim follows.** With only the results actually proved here, `V>=7` instead yields `F>=6` and `C>=22`.

The next useful continuation is **source recovery of the literal parallel minimum proof/certificate**, specifically its seven/eight-vertex terminal exclusions and its independent at-most-eight-face coverage. Until that evidence is supplied, label nine/nine as *user-accepted, original-proof verification pending*. Do not reopen below-32 construction, rerun the superseded small-construction direction, or identify this seven-vertex-bound replay as a nine/nine proof.

## 6. Deterministic recovery capsule

Exact parent/checkpoint: the attached `research-journal(6).md`, 2,768,037 bytes, SHA-256 `806f1ed0fb05c8fd8b202c394ab874652cd2eff68eb0494656905cc86ff94ae3`; the mathematical case family is fixed by the literal graph/face/root data in this capsule. The certificate is new work in this assignment, not an invented parent-assignment payload.

Save the following complete source as `verify_gate56.py` and run:

```bash
python3 -S verify_gate56.py
```

Tested with Python 3.13.5. No downloads, graph library, floating arithmetic, optimization package, omitted helper or external certificate file is required. The source SHA-256 with exactly the displayed LF-terminated bytes is `9aff6f42a6df666185d227c02a681605e574fae663b086b53f0bc26e21a50a90`; the canonical mathematical certificate hash printed by the program is the more portable identity check if text formatting changes.

```python
# Python 3.13.5, standard library only.  Exact exclusion, not a body search.
from itertools import product, combinations, permutations
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
import json

# Labels 1..n; candidate roots modulo automorphisms; all triangular faces.
DATA = [
 (4,(1,),((1,2,3),(1,4,2),(1,3,4),(2,4,3))),
 (5,(1,3),((4,3,1),(1,3,5),(5,4,1),(2,3,4),(5,3,2),(2,4,5))),
 (6,(1,),((1,2,3),(4,2,1),(1,3,5),(5,4,1),(6,3,2),(2,4,6),(6,5,3),(4,5,6))),
 (6,(1,2,5),((1,3,5),(6,3,1),(5,4,1),(1,4,6),(2,4,5),(6,4,2),(2,5,6),(6,5,3)))
]
# For lexicographically sorted rooted marked-tree keys: first base-36
# character is denominator d, the remaining characters are positive
# numerators a_i of shadow weights a_i/d in canonical preorder.
TOKENS = """111111 111125 111233 111254 111111 111125 212332 112222 112233 213552 112433 112453
11111 111111 111212 111223 11124 111241 111124 112122 112143 112232 112433 112343
11233 112331 112514 112444 11254 112541 111111 111125 111233 111254 111111 111125
111111 121111 121123 121231 121322 121343 111111 111125 121211 121211 121223 122221
122221 123222 123232 122321 122321 235944 8DLZXJ 111111 212233 212355 11111 111111
111212 111223 11124 111241 11111 111111 12222 122221 121211 121313 121333 12233
122331 111111 111124 122133 123121 124122 124143 122221 124232 123422 123443 12231
122311 12433 124231 123311 124513 124433 12443 124531 1111 11121 111211 111221
111111 112111 112122 11211 112121 112211 112211 112222 11222 112321 1122 11221
113311 113321 111212 111222 12123 111231 121124 121111 131133 131222 121322 121343
12122 131221 131312 131333 12133 131331 122124 122111 132133 133122 134122 123133
123222 123222 123422 123342 132222 12222 132221 12322 134231 133312 124413 123433
12343 124431 1222 13231 132311 132321 132121 134112 134133 13413 134131 134212
134413 134433 13433 134431 1243 13441 135411 135421""".split()

def require(ok, msg):
    if not ok:
        raise ValueError(msg)

def check_graphs():
    for n,roots,faces in DATA:
        fs={tuple(sorted(f)) for f in faces}
        incidence=Counter(e for f in fs for e in combinations(f,2))
        edges=set(incidence)
        require(len(fs)==2*n-4 and len(edges)==3*n-6,'wrong triangulation')
        require(set(incidence.values())=={2},'nonmanifold edge')
        require({v for f in fs for v in f}==set(range(1,n+1)),'missing vertex')
        covered=set()
        for p in permutations(range(1,n+1)):
            image={tuple(sorted(p[v-1] for v in f)) for f in fs}
            if image==fs: covered.update(p[r-1] for r in roots)
        require(covered==set(range(1,n+1)),'root orbits not covered')

def code_and_order(parent, marks):
    def visit(v):
        cs = sorted((visit(i) for i in range(1,len(parent)) if parent[i]==v),
                    key=lambda pair:(pair[0],pair[1]))
        return (str(int(v in marks))+'('+''.join(c for c,o in cs)+')',
                [v]+[i for c,o in cs for i in o])
    return visit(0)

def cases():
    for graph,(n,roots,faces) in enumerate(DATA):
        adj={i:set() for i in range(1,n+1)}
        for a,b,c in faces:
            for i,j in ((a,b),(b,c),(c,a)):
                adj[i].add(j); adj[j].add(i)
        for root in roots:
            rest=[v for v in range(1,n+1) if v!=root]
            rename={v:i for i,v in enumerate([root]+rest)}
            for choice in product(*(sorted(adj[v]) for v in rest)):
                parent=[-1]+[rename[v] for v in choice]
                good=True
                for start in range(1,n):
                    v=start; seen=set()
                    while v!=0:
                        if v in seen:
                            good=False; break
                        seen.add(v); v=parent[v]
                    if not good: break
                if not good: continue
                for face in faces:
                    if root not in face:
                        marks={rename[v] for v in face}
                        key,order=code_and_order(parent,marks)
                        yield graph,root,parent,marks,key,order

def det(A):
    # Fraction-free Bareiss, with row pivoting; also checks exact divisions.
    A=[row[:] for row in A]; n=len(A); old=1; sign=1
    for k in range(n-1):
        p=next((p for p in range(k,n) if A[p][k]),None)
        if p is None: return 0
        if p!=k:
            A[p],A[k]=A[k],A[p]; sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                q,r=divmod(pivot*A[i][j]-A[i][k]*A[k][j],old)
                require(r==0,'nonexact Bareiss division')
                A[i][j]=q
            A[i][k]=0
        old=pivot
    return sign*A[-1][-1]

def reduced_matrix(parent,marks,d,nums):
    # This is 2*d times K, whose variables are (1,x_1,...,x_(n-1)).
    n=len(parent); M=[[0]*n for _ in range(n)]; M[0][0]=2*d
    for i in range(1,n):
        a=nums[i-1]; p=parent[i]
        M[i][i]+=2*a
        M[0][i]+=d*int(i in marks); M[i][0]+=d*int(i in marks)
        M[i][p]-=a; M[p][i]-=a
    return M

def full_matrix(parent,marks,d,nums):
    # Independent expansion of 2*d*[sum_i (a_i/d) q_i + L].
    n=len(parent); m=1+3*(n-1); M=[[0]*m for _ in range(m)]
    M[0][0]=2*d
    def idx(i,k): return 1+3*(i-1)+k
    for i in range(1,n):
        a=nums[i-1]; p=parent[i]
        for k in range(3):
            ii=idx(i,k); M[ii][ii]+=2*a
            if p==0:
                if k==0:
                    M[0][ii]-=a; M[ii][0]-=a
            else:
                jj=idx(p,k); M[ii][jj]-=a; M[jj][ii]-=a
        if i in marks:
            ii=idx(i,0); M[0][ii]+=d; M[ii][0]+=d
    return M

def ldl_positive(A):
    # Rational Schur elimination, separate from the Bareiss test.
    A=[[Q(v) for v in row] for row in A]
    for k in range(len(A)):
        require(A[k][k]>0,'nonpositive full-matrix pivot')
        for i in range(k+1,len(A)):
            for j in range(i,len(A)):
                A[i][j]-=A[i][k]*A[j][k]/A[k][k]
                A[j][i]=A[i][j]

check_graphs()
rows=list(cases()); keys=sorted({r[4] for r in rows})
require(len(keys)==len(TOKENS)==164,'canonical coverage changed')
cert={k:[int(c,36) for c in word] for k,word in zip(keys,TOKENS)}
counts=Counter(); unique_by_n=Counter(); checked=set(); records=[]
min_minor=None
for graph,root,parent,marks,key,order in rows:
    d,*a=cert[key]; n=len(parent)
    require(d>0 and len(a)==n-1 and min(a)>0,'bad multiplier')
    # Pull the canonical multipliers back onto every ORIGINAL raw case.
    nums=[0]*(n-1)
    for v,value in zip(order[1:],a): nums[v-1]=value
    M=reduced_matrix(parent,marks,d,nums)
    for size in range(1,n+1):
        value=det([r[:size] for r in M[:size]])
        require(value>0,'nonpositive principal minor')
        min_minor=value if min_minor is None else min(min_minor,value)
    counts[(graph,root)]+=1
    if key not in checked:
        ldl_positive(full_matrix(parent,marks,d,nums))
        checked.add(key); unique_by_n[n]+=1
        records.append([key,d,a])
require(dict(counts)=={(0,1):16,(1,1):225,(1,3):150,(2,1):1536,
                      (3,1):1344,(3,2):1680,(3,5):1008},'raw coverage changed')
require(dict(unique_by_n)=={4:4,5:26,6:134},'wrong orbit count')
payload=json.dumps(sorted(records),separators=(',',':')).encode()
print(json.dumps({'status':'EXACT_FILLED_VOLUME_V_GE_7_REPLAY_PASS',
 'raw_cases_V4':16,'raw_cases_V5':375,'raw_cases_V6':5568,
 'canonical_certificates':len(checked),'minimum_integer_leading_minor':min_minor,
 'certificate_records_sha256':sha256(payload).hexdigest()},sort_keys=True))
```

Supplemental executable copy: [verify_gate56.py](sandbox:/mnt/data/proof_gate/verify_gate56.py). All proof-critical data are already embedded above.
