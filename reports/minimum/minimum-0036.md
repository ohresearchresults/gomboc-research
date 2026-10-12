# minimum-0036

AI research report · 2026-09-10 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# NOVA54_MP45_FULL_TENSOR_RIGIDITY_AND_NORM_FRONTIER_V2

## 1. Determination and execution boundary

This handoff does **not** establish a whole MP9:45 theorem, and it does **not** establish a completed, byte-pinned replay of `NOVA54_MP9_ACTUAL_MOMENTS_V1`. In particular, it does not promote the earlier whole-MP9:30/48 claims or the proposed 57 C32 coarsening exclusions.

The strongest observed computational advance on the assigned eleven cases is **80 individually checked norm-chamber certificates**. Each uses the actual 63-tetrahedron complex, its complete ten-dimensional oriented boundary-cycle space, common actual first/second moments, and nonnegative multipliers for explicitly stated norm comparisons. The individual checks used independently accumulated scalar polynomials, Bareiss leading minors, and Fraction-LDL verification. These calculations exclude all eight norm chambers for original tree indices **1200, 1472, and 1752**. For each of the other eight assigned trees, they exclude chambers 1 through 7, leaving only the strict chamber in which the short leaf has larger norm than the first vertex on the long branch.

There is an important packaging boundary: I did not obtain a readable final terminal transcript and output-pin ledger for the subsequently repackaged aggregate checker. I therefore do **not** assert an aggregate recovery-success marker or invent a frozen coefficient-file SHA-256. The complete reconstruction/checking recipe below is supplied instead. The individual computational conclusion and the uncompleted aggregate byte-recovery obligation are separate. A coordinator requiring an observed, byte-pinned aggregate replay before changing its accepted frontier should keep that obligation open.

A second result is a structural **generic actual-mass rigidity theorem** for this literal MP9:45 complex. Its full tensor cycle-moment matrix has rank 62 at the explicit rational realization below. Consequently, on an explicitly recoverable nonempty algebraic-open shape domain, the full zeroth, first, and second **tensor** cycle equalities determine the 63 determinant masses up to common scale. This is not true of the corresponding scalar-trace system: an exact positive counterfeit-mass construction is given below to show the distinction.

The accepted global bound remains 32. No whole C32 type is added by this handoff. The latest supplied accepted whole-type set is `{33,34,72,139,149,152,159,163,164,178,192,217,284,288,293,294,295}`. :contentReference[oaicite:0]{index=0}

## 2. Source identity and recovery findings

### Normative parent

The normative immutable parent remains:

- Assignment: `minimum-0030`.
- Title: `NOVA24_C32_TYPE139_WHOLE_ACTUAL_U_GE_2_V1`.
- Canonical serialized payload: 39914 bytes.
- SHA-256: `3b737649ca4e531383c349e6a3e088fdf458b5b826662c391f655f628f843a94`.

It is canonical **C32 type139**, not MP9:45. Its literal polygonal facets are

`013, 0241, 0362, 1463, 25874, 265, 476, 568, 678`.

In contrast, the literal MP9:45 facets used throughout this handoff are

`014, 021, 032, 043, 125, 154, 235, 347, 365, 376, 458, 487, 568, 678`.

The first is a nine-facet, sixteen-edge polyhedral map; the second is a fourteen-triangle, twenty-one-edge simplicial graph. No relabeling identifies these two objects. The journal itself explicitly distinguishes the parent139 theorem from the unfinished MP9 recovery. 

### Which attachment contains the needed source

The useful updated checkpoint is `research-journal(1).md`:

- 3204366 bytes.
- SHA-256 `60e55fd7ae0576c644d1cfc87d6c2fb825fe4c41d336382b24611bfa8d116d26`.

The older `source-research-journal(5).md` is a different checkpoint:

- 1737149 bytes.
- SHA-256 `1e54e3291077a0f4f0fe4588bb6793b823c7f904caab1c1ac8712bde2c014722`.

I did not substitute the older attachment for the missing late material. The updated attachment contains the late MP9 capsule and the immutable parent payload.

### MP9 source recovery succeeded

Removing the one inserted journal-entry header from inside the split base85 literal reconstructs:

`recover_nova54.py`: 33040 bytes, SHA-256

`627b00c5e6f5c6e697fe537d407e3fddc294c4dbefdfe65857ad65680f9fc219`.

Its source-only extraction completed. Important recovered component pins are:

| Component | Bytes | SHA-256 |
|---|---:|---|
| `comb.py` | 9699 | `f614a76308d54aad24ed1ec06fb6658506aaf96f3907b2b770861e439595d82b` |
| `locator.py` | 12050 | `295c928614be33ecbac935ac7d9ee44ea2aa0c8901eaeff762ec455816d2602d` |
| `reconstruct.py` | 2490 | `567944e388b4ad65b858bbb0f2728fbbe4a269b84f574f583d2b6ac738ad16f6` |
| `exact_check.py` | 13163 | `0a60f2ac77565b7c78be08cfda038cb472c4fdd0fce3bbf06a8e5ed48160348b` |
| `plan.json` | 22604 | `121ee1d69b7f24b2933327196aa967f7deaeeae4f9c3adabef644f565d055418` |

The legacy full-cycle plans for MP9:45/root3 original indices **145 and 1481** were individually reconstructed and checked: each has 1063 integer coefficients and 63 strict-PD blocks. This is a successful local replay, not verification of the entire old output stream.

The full old numerical stream, its full all-root coverage report, and the C32 lifting replay were **not completed in this run**. Partial processes and partial output files are not terminal evidence. I do not assert the old 8,116,253-case marker, the complete 21,546-record output pin, or the 57-type marker from those partial executions.

### A separate, concrete journal-recovery conflict

The journal's literal two-part `recover_quad10.py` source has a recoverable corruption. Its concatenation is 24286 bytes with SHA-256

`71d9d61527f5e9c44d2c6ec5174e925ef8d98444c257c23766dfa2ce7e209f87`.

One catalogue hash is missing the three characters `930`:

- Literal corrupted string: `efb10a4657a891cd13f6f62db94164bd4b3005e908dc55aae87db450f704d`.
- Correct string: `efb10a4657a891cd13f6f62db94164bd4b3005e908dc55aae87db450930f704d`.

Replacing that **single occurrence** restores the advertised 24289-byte source and SHA-256

`fc6fb7a3b0fd6e44fa4e69145e38453d131136e34cbe1cd9033e27791954f5f2`.

This is an authenticated repair, not a guessed replacement source. There are also stale output-length fields in that recovered wrapper: the reconstructed `universal285.json` has 1330807 bytes, while its advertised SHA-256 does match `3a00b679c994255debd3acbe5d3230e336d1e292b9cf88507dc1d2c61fc94496`; the wrapper's length field is 1289123. The separately produced verification report has 41787 bytes and matches SHA-256 `067c8ae69857aece263ccaeb5b1e05e4d401d90f13f5d8ee8d64e3847358acec`; the wrapper's length field is 41790. Thus a claim that this literal wrapper passes every advertised output-length assertion cannot be inferred merely from matching these two hashes.

These are recovery/manifest conflicts. They are not an incidence conflict in the immutable parent139 payload, and they do not rename any graph or type.

## 3. Exact assigned-case identities and the sharper norm frontier

Write a long broom in coordinates `b0,...,b8`, where `b0=3`, the long branch is

`b7 -> b6 -> b5 -> b4 -> b3 -> b2 -> b1 -> b0`,

and the short leaf is `b8 -> b0`.

The complete literal data are:

| Original index | Literal parent array | Broom order, broom coordinate to literal vertex |
|---:|---|---|
| 1200 | `[1,2,5,3,0,3,3,4,7]` | `[3,5,2,1,0,4,7,8,6]` |
| 1205 | `[1,2,5,3,0,3,3,8,4]` | `[3,5,2,1,0,4,8,7,6]` |
| 1472 | `[1,2,5,3,3,8,3,6,7]` | `[3,6,7,8,5,2,1,0,4]` |
| 1752 | `[1,4,0,3,3,2,5,3,6]` | `[3,4,1,0,2,5,6,8,7]` |
| 1775 | `[1,4,0,3,3,2,8,3,5]` | `[3,4,1,0,2,5,8,6,7]` |
| 3058 | `[1,4,3,3,7,6,3,8,5]` | `[3,6,5,8,7,4,1,0,2]` |
| 3124 | `[1,4,3,3,8,3,5,6,7]` | `[3,5,6,7,8,4,1,0,2]` |
| 3149 | `[1,4,3,3,8,6,7,3,5]` | `[3,7,6,5,8,4,1,0,2]` |
| 3966 | `[1,5,3,3,0,2,3,4,7]` | `[3,2,5,1,0,4,7,8,6]` |
| 5772 | `[2,0,5,3,1,3,3,4,7]` | `[3,5,2,0,1,4,7,8,6]` |
| 7000 | `[2,4,3,3,0,1,5,3,6]` | `[3,2,0,4,1,5,6,8,7]` |

All eleven terminal triples `b5,b6,b7` are triangles of this literal graph. Merely reapplying the terminal-triangle incidence screen does not remove them.

Let `n_i = x_i^T M x_i`. Distinct vertices and a weak escape imply

`n_parent - n_child = 2 D_child,parent + ||x_parent-x_child||_M^2 > 0`.

Therefore the long branch has a strict norm order, but initially no order is imposed between the short leaf and the long branch. The exhaustive **closed** chambers are:

- Chamber 0: `n_b8 >= n_b1`.
- Chamber k, for `1 <= k <= 6`: `n_bk >= n_b8 >= n_b(k+1)`.
- Chamber 7: `n_b7 >= n_b8`.

This is a genuine branching argument. Every tie belongs to adjacent closed chambers; no tie is discarded.

The observed exact certificates cover all eight chambers for 1200, 1472, and 1752, and chambers 1 through 7 for every other listed tree. Thus the precisely unexcluded members of the **assigned eleven**, with their stronger necessary conditions, are:

| Original index | Parent array | Additional necessary strict inequality |
|---:|---|---|
| 1205 | `[1,2,5,3,0,3,3,8,4]` | `n_6 > n_5` |
| 1775 | `[1,4,0,3,3,2,8,3,5]` | `n_7 > n_4` |
| 3058 | `[1,4,3,3,7,6,3,8,5]` | `n_2 > n_6` |
| 3124 | `[1,4,3,3,8,3,5,6,7]` | `n_2 > n_5` |
| 3149 | `[1,4,3,3,8,6,7,3,5]` | `n_2 > n_7` |
| 3966 | `[1,5,3,3,0,2,3,4,7]` | `n_6 > n_2` |
| 5772 | `[2,0,5,3,1,3,3,4,7]` | `n_6 > n_5` |
| 7000 | `[2,4,3,3,0,1,5,3,6]` | `n_7 > n_2` |

The inequalities are strict because equality is also in chamber 1, which was excluded. In every remaining assigned case the short leaf must therefore be the **second-largest-norm vertex**, strictly below the root and strictly above the entire long branch.

This table is not asserted to be the complete independently replayed remainder among all 9140 root3 tree orbits. The old certificates covering the other cases still have their stated recovery obligation.

## 4. Why the norm certificates are physical and cover the whole stated domain

The domain is every full-dimensional homogeneous convex realization with the stated oriented boundary triangulation, translated by its **actual solid-volume centroid**, with nine distinct vertices and any common SPD metric `M`. There are no coordinate boxes, bounded-condition-number assumptions, positive lower bounds on volumes, or unstated comparisons between incomparable branches. All eight selected escapes are weak inequalities. The certificate argument also allows cofacial zero tetrahedron volumes whenever the listed triangles are supplied as a genuine triangulation of an actual boundary; that algebraic extension alone is not a C32 label/triangulation map.

Let `X` have the centered vertex rows, and let `G=X M X^T`. For every used tetrahedron `t`, use its actual six-volume

`d_t = |det(x_b-x_a, x_c-x_a, x_d-x_a)|`.

The same unordered tetrahedron has the same `d_t` wherever it appears. Let `chi_t` be its vertex indicator and

`J_t = chi_t chi_t^T + diag(chi_t)`.

For every genuine apex fan, with `D=6 Vol(P)`,

`sum_fan d_t = D`,

`X^T sum_fan d_t chi_t = 0`,

`sum_fan d_t X^T J_t X = 20 D Cov(P)`.

The sum over the **union** of distinct fan tetrahedra need not equal `D`; only each genuine fan is normalized that way.

For MP9:45 the union of all nine apex fans has **63 cells**. Its full oriented boundary matrix has rank **53**, hence a **ten-dimensional** kernel. The relations used are a complete exact basis of that kernel, not just differences between selected fans. If `beta` is any such cycle relation, Stokes' theorem applied to polynomial volume moments gives

`sum beta_t d_t = 0`,

`X^T sum beta_t d_t chi_t = 0`,

`sum beta_t d_t X^T J_t X = 0`.

These are necessary identities of the actual determinant masses. No independently fitted positive masses are substituted for them.

The integer escape form is

`L_i = 2 e_i e_i^T - e_i e_parent^T - e_parent e_i^T`,

so `tr(G L_i)=-2 D_i,parent <= 0`. An explicitly branched norm comparison `n_i <= n_j` contributes

`N_ij = 2 e_i e_i^T - 2 e_j e_j^T`,

again with nonpositive pairing with `G`. Its multiplier is nonnegative and may differ between tetrahedron blocks.

Free first-moment terms, cycle-volume offset matrices, and cycle-second-moment terms cancel after weighting by the same actual `d_t`. The remaining terms have nonpositive weighted pairing with `G`. In contrast, the checked condition `Q_t-I` strictly positive definite for every block makes the weighted pairing strictly positive, because `G` is nonzero PSD and at least one used actual tetrahedron has positive volume. This is the contradiction.

The 80 accepted chambers contain **5040** integer 9-by-9 blocks and **45360** leading minors per exact checker. No forbidden-redirection theorem is needed for these particular 80 certificates.

## 5. Structural actual-mass theorem: full tensor cycles are generically rigid

For a single coordinate realization `X`, form the 100-by-63 matrix `L(X)` as follows. For each of the ten oriented cycle vectors `beta`, include:

1. The row `beta_t`.
2. Three rows `beta_t sum_(i in t) x_i,a`.
3. Six symmetric tensor rows

`beta_t [ (sum_(i in t) x_i,a)(sum_(i in t) x_i,b) + sum_(i in t) x_i,a x_i,b ]`, for `a <= b`.

The actual mass vector `d(X)` lies in `ker L(X)`.

At the exact rational realization

```
0 = (5,2,-6)
1 = (5,5,-6)
2 = (2,5,-6)
3 = (0,0,0)
4 = (12,0,0)
5 = (0,12,0)
6 = (2,5,6)
7 = (5,2,6)
8 = (5,5,6)
```

all 84 strict supporting-tetrahedron tests for the fourteen stated facets are positive, and the exact rank of `L(X)` is **62**. This fixture is a realization of the graph, not an asserted escape-tree realization or a monostatic example.

Choose the 62-by-62 minor by the deterministic pivot-selection procedure in the code below, evaluated at this fixture. Call the resulting integer polynomial in the coordinates `Delta(X)`. Its fixture value is nonzero. Consequently:

**Generic actual-mass rigidity theorem.** For every realization in the stated shape domain with `Delta(X) != 0`, any vector `w` satisfying all full tensor cycle equations `L(X)w=0` is proportional to the actual determinant-mass vector `d(X)`. Requiring one genuine fan to have the actual total mass fixes the proportionality factor to one.

The proof is rank-nullity: the nonzero minor gives rank at least 62, the actual nonzero determinant vector gives rank at most 62, and therefore the kernel is exactly its span. The full rank-62 domain is the union of the nonzero domains of all 62-by-62 minors. A zero of the particular displayed minor is not automatically a rank drop. The rank-at-most-61 locus is not excluded here.

This conditional converse is stronger than saying that moment equations are necessary. It is valid only with one common coordinate realization and all six second-tensor components. It does **not** turn a feasible collection of independent PSD tetrahedron blocks into a physical realization.

### Exact scalar-trace countercontrol

There is also a useful exact negative control. At the fixture, center the vertices at their actual volume centroid. Impose on perturbations of the 63 masses:

- all ten cycle zeroth moments;
- all thirty cycle first moments;
- all ten cycle second-moment traces;
- preservation of one reference fan's actual volume, actual centroid, and actual covariance trace.

That is at most 55 homogeneous linear equations on 63 perturbation variables. Their kernel has dimension at least eight. Any nonzero perturbation in this kernel can be scaled sufficiently small to retain strictly positive masses. It cannot preserve all full tensor cycle equations: the rank-62 theorem, together with preservation of the reference fan mass, would otherwise force the perturbation to be zero.

Thus there is an exact, at least eight-dimensional local family of positive **counterfeit masses** preserving these scalar data while failing the full physical tensor system. The executable construction below produces one. It is deliberately not a physical-volume witness, not an escape-tree witness, and not a new polyhedron attaining any equilibrium bound.

## 6. Complete source-recovery unit

Save the following as `recover_inputs.py`. Its input is the exact updated journal checkpoint identified above. This is an exact extraction/repair recipe against that checkpoint, not an archive-only dependency. It does not launch the old multimillion-case search.

Run:

```
python -S recover_inputs.py /path/to/research-journal\(1\).md
```

```python
from pathlib import Path
import hashlib,json,re,subprocess,sys

def pin(b):
    return len(b),hashlib.sha256(b).hexdigest()

raw=Path(sys.argv[1]).read_bytes()
assert pin(raw)==(3204366,'60e55fd7ae0576c644d1cfc87d6c2fb825fe4c41d336382b24611bfa8d116d26')
s=raw.decode('utf-8')
a=s.index('# Immutable parent result payloads')
a=s.index('# NOVA24_C32_TYPE139_WHOLE_ACTUAL_U_GE_2_V1',a)
parent=s[a:].rstrip()+'\n'
b=json.dumps({'version':2,'result_markdown':parent},ensure_ascii=False,separators=(',',':')).encode('utf-8')
assert pin(b)==(39914,'3b737649ca4e531383c349e6a3e088fdf458b5b826662c391f655f628f843a94')
a=s.index(chr(39)*3+'NOVA54_MP9_ACTUAL_MOMENTS_V1 complete self-contained recovery.')
e=s.index('\n```',a)
code=s[a:e]+'\n'
pat=(r'\n\n## 2026-09-09T02:54:11\.640Z\n\n'
     r'### Late recovery slot-1 [^\n]*\n\nSource: [^\n]*\n\n')
code,n=re.subn(pat,'',code)
assert n==1
b=code.encode('utf-8')
assert pin(b)==(33040,'627b00c5e6f5c6e697fe537d407e3fddc294c4dbefdfe65857ad65680f9fc219')
Path('recover_nova54.py').write_bytes(b)
subprocess.run([sys.executable,'-S','recover_nova54.py','extract'],check=True)
expected={
 'comb.py':(9699,'f614a76308d54aad24ed1ec06fb6658506aaf96f3907b2b770861e439595d82b'),
 'locator.py':(12050,'295c928614be33ecbac935ac7d9ee44ea2aa0c8901eaeff762ec455816d2602d'),
 'reconstruct.py':(2490,'567944e388b4ad65b858bbb0f2728fbbe4a269b84f574f583d2b6ac738ad16f6'),
 'exact_check.py':(13163,'0a60f2ac77565b7c78be08cfda038cb472c4fdd0fce3bbf06a8e5ed48160348b'),
 'plan.json':(22604,'121ee1d69b7f24b2933327196aa967f7deaeeae4f9c3adabef644f565d055418')}
for name,value in expected.items():
    assert pin((Path('nova54_recovery')/name).read_bytes())==value

a=s.index(chr(34)*3+'NOVA24_C32_QUAD_TEN_WHOLE_TYPES_V1: complete source-only recovery.')
e=s.index('\n```',a)
part1=s[a:e]+'\n'
a=s.index('```text\n',e)+8
e=s.index('\n```',a)
q=part1+s[a:e]+'\n'
assert pin(q.encode())==(24286,'71d9d61527f5e9c44d2c6ec5174e925ef8d98444c257c23766dfa2ce7e209f87')
wrong='efb10a4657a891cd13f6f62db94164bd4b3005e908dc55aae87db450f704d'
right='efb10a4657a891cd13f6f62db94164bd4b3005e908dc55aae87db450930f704d'
assert q.count(wrong)==1
q=q.replace(wrong,right)
assert pin(q.encode())==(24289,'fc6fb7a3b0fd6e44fa4e69145e38453d131136e34cbe1cd9033e27791954f5f2')
d=Path('quad_recovery');d.mkdir(exist_ok=True)
(d/'recover_quad10.py').write_bytes(q.encode())
subprocess.run([sys.executable,'-S','recover_quad10.py','extract'],cwd=d,check=True)
print('NOVA54_PARENT139_AND_MP9_SOURCE_RECOVERY_PASS')
print('QUAD_WRAPPER_THREE_CHARACTER_REPAIR_AUTHENTICATED_OUTPUT_LENGTH_AUDIT_STILL_REQUIRED')
```

The numerical environment used for the certificate work was CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, Linux x86-64, one BLAS thread, and four fork workers. Assertions must remain enabled. The source-only decoder and independent checkers use the standard library. No random seed is an input.

## 7. Complete 80-chamber reconstruction/checking patch

Save this as `mp45_norm80.py` beside the extracted `nova54_recovery` directory. It uses the exact, authenticated component sources above. All new constraints, all eleven inputs, the complete chamber selection, rounding parameters, and the independent augmented-matrix checks are included here.

Commands:

```
python mp45_norm80.py build
python -S mp45_norm80.py check
```

The required terminal marker is

`NOVA54_MP45_80_CHAMBERS_3_WHOLE_ASSIGNED_TREES_8_STRICT_REMAINDERS_PASS`.

The program emits canonical JSON byte counts and SHA-256 values. I do not supply invented expected values for the aggregate files whose final pin ledger was not readable. Successful mathematical verification, a successful fresh numerical replay, and matching a subsequently frozen byte pin should be recorded separately.

```python
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[k]='1'
from pathlib import Path
import sys,json,hashlib,multiprocessing
from functools import lru_cache
sys.path.insert(0,str(Path('nova54_recovery').resolve()))
import comb,exact_check
FS=tuple(tuple(map(int,s)) for s in
 '014 021 032 043 125 154 235 347 365 376 458 487 568 678'.split())
P={
1200:[1,2,5,3,0,3,3,4,7],
1205:[1,2,5,3,0,3,3,8,4],
1472:[1,2,5,3,3,8,3,6,7],
1752:[1,4,0,3,3,2,5,3,6],
1775:[1,4,0,3,3,2,8,3,5],
3058:[1,4,3,3,7,6,3,8,5],
3124:[1,4,3,3,8,3,5,6,7],
3149:[1,4,3,3,8,6,7,3,5],
3966:[1,5,3,3,0,2,3,4,7],
5772:[2,0,5,3,1,3,3,4,7],
7000:[2,4,3,3,0,1,5,3,6]}
WHOLE={1200,1472,1752}
_raw_relations=exact_check.volume_relations
@lru_cache(None)
def _relations(faces,apices):
    return _raw_relations(faces,apices)
def cached_relations(faces,apices):
    return _relations(tuple(map(tuple,faces)),tuple(apices))
exact_check.volume_relations=cached_relations

def emit(name,obj):
    b=(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode()
    Path(name).write_bytes(b)
    print(name,len(b),hashlib.sha256(b).hexdigest(),flush=True)

def broom(p):
    paths=[]
    for i in range(9):
        q=[i]
        while q[-1]!=3:
            q.append(p[q[-1]])
            assert len(q)<=9
        paths.append(q)
    b=list(reversed(max(paths,key=len)))
    assert len(b)==8
    b.append(next(i for i in range(9) if i not in b))
    assert p[b[8]]==3
    return b

def comparisons(ix,o):
    b=broom(P[ix])
    return ([(b[8],b[o])] if o else [])+([(b[o+1],b[8])] if o<7 else [])

def cases():
    return [(i,o) for i in P for o in range(8) if i in WHOLE or o>0]

def graph():
    es=sorted({tuple(sorted((f[i],f[(i+1)%3]))) for f in FS for i in range(3)})
    L=[[sum(i in e for e in es) if i==j else -int(tuple(sorted((i,j))) in es)
        for j in range(8)] for i in range(8)]
    return dict(facets=FS,edges=es,aut=comb.auto_maps(FS),trees=comb.det(L))

def check_record(ix,o,z):
    pp=comparisons(ix,o)
    rel=exact_check.volume_relations(FS,list(range(9)))[1]
    assert len(rel)==10
    assert len(z)==1063+63*len(pp)
    assert all(type(v) is int for v in z)
    assert min(z[1063:])>=0
    rec=dict(root=3,parent=P[ix],kind='cycle',fans=[[a,0] for a in range(9)],
             relations=rel,z=z[:1063])
    h=hashlib.sha256();count=0
    for u,Q in enumerate(exact_check.scalar_matrices(rec,FS)):
        for (i,j),v in zip(pp,z[1063+u*len(pp):1063+(u+1)*len(pp)]):
            Q[i][i]+=2*v
            Q[j][j]-=2*v
        a=exact_check.bareiss(Q)
        assert a==exact_check.ldl(Q)
        h.update(comb.encoded([Q,a]));count+=1
    assert count==63
    return h.hexdigest()

def build_one(arg):
    import numpy as np
    import locator
    ix,o=arg
    x,B,ls,bi,mat,info=locator.cycle_problem(P[ix],FS)
    pp=comparisons(ix,o);k=len(mat);m=len(pp);N=len(x);E=np.eye(9)
    extra=[np.outer(E[i],E[i])-np.outer(E[j],E[j]) for i,j in pp]
    xx=np.r_[x[:-1],np.zeros(k*m),x[-1]]
    BB=np.r_[B[:-1],np.ones(k*m),B[-1]]
    ll=np.r_[ls,np.arange(N-1,N-1+k*m)]
    xx[ll]=1/(k*(8+m))
    ii=[];mm=[]
    for u,(ids,L) in enumerate(zip(bi,mat)):
        ii.append(np.r_[ids[:-1],np.arange(N-1+u*m,N-1+(u+1)*m),N-1+k*m])
        mm.append(np.concatenate([L[:-1],np.array(extra),L[-1:]]))
    v=locator.shared_locate((xx,BB,ll,ii,mm,info),eps=1e-8,maxouter=14)
    assert v is not None and np.isfinite(v).all()
    scale=max(abs(float(a)) for a in v[:-1])
    for power in (6,8,10,12):
        z=[round(float(a)/scale*10**power) for a in v[:-1]]
        try:
            hh=check_record(ix,o,z)
        except AssertionError:
            continue
        return dict(index=ix,parent=P[ix],order=o,pairs=[list(t) for t in pp],
                    power=power,z=z,scalar_sha=hh)
    raise AssertionError(('NO_EXACT_CERTIFICATE',ix,o))

def verify(rows):
    assert [(r['index'],r['order']) for r in rows]==cases()
    assert len(rows)==80
    parents=comb.parent_trees(graph(),3)
    assert len(parents)==9140
    for i,p in P.items():
        assert list(parents[i])==p
    for r in rows:
        i,o=r['index'],r['order']
        assert r['parent']==P[i]
        assert r['pairs']==[list(t) for t in comparisons(i,o)]
        assert r['power'] in (6,8,10,12)
        assert r['scalar_sha']==check_record(i,o,r['z'])
    remaining=[]
    for i,p in P.items():
        if i not in WHOLE:
            b=broom(p)
            remaining.append(dict(index=i,parent=p,broom_order=b,
                                  necessary_strict_norm_pair=[b[8],b[1]]))
    report=dict(graph='MP9:45',root=3,facets=FS,branches=80,matrices=5040,
                leading_minors_per_checker=45360,whole_assigned_indices=sorted(WHOLE),
                remaining_assigned_cases=remaining,
                scope='Assigned eleven only; no whole-graph or C32 propagation assertion')
    emit('mp45_norm80_report.json',report)
    print('NOVA54_MP45_80_CHAMBERS_3_WHOLE_ASSIGNED_TREES_8_STRICT_REMAINDERS_PASS',flush=True)

if __name__=='__main__':
    if sys.argv[1]=='build':
        with multiprocessing.get_context('fork').Pool(4) as pool:
            rows=list(pool.imap(build_one,cases()))
        emit('mp45_norm80.json',rows)
        verify(rows)
    elif sys.argv[1]=='check':
        verify(json.loads(Path('mp45_norm80.json').read_bytes()))
    else:
        raise SystemExit('use build or check')
```

## 8. Self-contained exact mass-rigidity and counterfeit-control capsule

This unit does not depend on the MP9 numerical locator, the journal decoder, NumPy, SciPy, or an external archive. It defines the complete oriented complex, computes its complete rational kernel, reconstructs the full tensor matrix and a nonzero 62-by-62 minor, and constructs the positive counterfeit-mass control described above.

Save as `mp45_mass_gate.py` and run:

```
python -S mp45_mass_gate.py
```

The expected dimension marker is

`NOVA54_MP45_MASS_RIGIDITY_63_53_10_100_62_PASS`.

The positive-counterfeit construction is an exact corollary and executable recipe. I do not claim a separately observed frozen output pin for that construction. Its complete literal input and every reconstruction step are here.

```python
from fractions import Fraction as F
from itertools import combinations
from math import gcd,lcm
from pathlib import Path
import json,hashlib

FS=tuple(tuple(map(int,s)) for s in
 '014 021 032 043 125 154 235 347 365 376 458 487 568 678'.split())
X=[[5,2,-6],[5,5,-6],[2,5,-6],[0,0,0],[12,0,0],[0,12,0],
   [2,5,6],[5,2,6],[5,5,6]]

def reduce(A):
    a=[list(map(F,row)) for row in A]
    n=len(a[0]);r=0;piv=[];order=list(range(len(a)))
    for j in range(n):
        k=next((i for i in range(r,len(a)) if a[i][j]),None)
        if k is None:
            continue
        a[r],a[k]=a[k],a[r]
        order[r],order[k]=order[k],order[r]
        d=a[r][j];a[r]=[v/d for v in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][j]:
                d=a[i][j];a[i]=[u-d*v for u,v in zip(a[i],a[r])]
        piv.append(j);r+=1
        if r==len(a):
            break
    return a,piv,order[:r]

def nullspace(A):
    a,piv,unused=reduce(A);n=len(A[0]);out=[]
    for j in range(n):
        if j in piv:
            continue
        v=[F(0)]*n;v[j]=F(1)
        for i,k in enumerate(piv):
            v[k]=-a[i][j]
        den=lcm(*(x.denominator for x in v))
        w=[int(x*den) for x in v];gg=gcd(*w);w=[x//gg for x in w]
        if next(x for x in w if x)<0:
            w=[-x for x in w]
        assert all(sum(x*y for x,y in zip(row,w))==0 for row in A)
        out.append(w)
    return out

def det3(a,b,c):
    return sum(a[i]*(b[(i+1)%3]*c[(i+2)%3]-b[(i+2)%3]*c[(i+1)%3])
               for i in range(3))

def sub(a,b):
    return [u-v for u,v in zip(a,b)]

def tet(points,t):
    a,b,c,d=(points[i] for i in t)
    return det3(sub(b,a),sub(c,a),sub(d,a))

def detn(A):
    a=[row[:] for row in A];n=len(a);old=1;sgn=1
    for k in range(n-1):
        p=next((i for i in range(k,n) if a[i][k]),None)
        if p is None:
            return 0
        if p!=k:
            a[k],a[p]=a[p],a[k];sgn=-sgn
        d=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                v=d*a[i][j]-a[i][k]*a[k][j]
                assert v%old==0
                a[i][j]=v//old
        for i in range(k+1,n):
            a[i][k]=0
        old=d
    return sgn*a[-1][-1]

def geometry():
    fans=[[(a,)+f for f in FS if a not in f] for a in range(9)]
    cells=sorted({tuple(sorted(t)) for fan in fans for t in fan})
    sig={}
    for fan in fans:
        for t in fan:
            s=(-1)**sum(t[i]>t[j] for i in range(4) for j in range(i+1,4))
            key=tuple(sorted(t))
            assert key not in sig or sig[key]==s
            sig[key]=s
    triples=list(combinations(range(9),3));index={t:i for i,t in enumerate(triples)}
    R=[[0]*len(cells) for t in triples]
    for j,t in enumerate(cells):
        for k in range(4):
            R[index[t[:k]+t[k+1:]]][j]=sig[t]*(-1)**k
    beta=nullspace(R)
    assert len(cells)==63 and len(beta)==10 and len(reduce(R)[1])==53
    f0=[int(t in {tuple(sorted(q)) for q in fans[3]}) for t in cells]
    return cells,R,beta,f0

def moments(points,cells,beta):
    rows=[];labels=[]
    for k,b in enumerate(beta):
        rows.append(b[:]);labels.append([k,0])
        for a in range(3):
            rows.append([b[j]*sum(points[i][a] for i in t) for j,t in enumerate(cells)])
            labels.append([k,1,a])
        for a in range(3):
            for c in range(a,3):
                rows.append([b[j]*(sum(points[i][a] for i in t)*sum(points[i][c] for i in t)
                                  +sum(points[i][a]*points[i][c] for i in t))
                             for j,t in enumerate(cells)])
                labels.append([k,2,a,c])
    return rows,labels

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def main():
    for f in FS:
        assert min(tet(X,(a,)+f) for a in range(9) if a not in f)>0
    cells,R,beta,f0=geometry()
    d=[abs(tet(X,t)) for t in cells]
    assert min(d)>0
    L,labels=moments(X,cells,beta)
    assert len(L)==100 and all(dot(row,d)==0 for row in L)
    unused,cols,rr=reduce(L)
    assert len(cols)==62 and len(rr)==62
    minor=[[L[i][j] for j in cols] for i in rr]
    delta=detn(minor)
    assert delta!=0

    D=dot(f0,d)
    centre=[sum(f0[j]*d[j]*sum(X[i][a] for i in t)
                for j,t in enumerate(cells))/(F(4)*D) for a in range(3)]
    Y=[[F(X[i][a])-centre[a] for a in range(3)] for i in range(9)]
    LY,unused=moments(Y,cells,beta)
    assert len(reduce(LY)[1])==62
    A=[]
    for k in range(10):
        A.extend(LY[10*k:10*k+4])
        A.append([LY[10*k+4][j]+LY[10*k+7][j]+LY[10*k+9][j] for j in range(63)])
    A.append(f0[:])
    for a in range(3):
        A.append([f0[j]*sum(Y[i][a] for i in t) for j,t in enumerate(cells)])
    traces=[sum(sum(Y[i][a] for i in t)**2 for a in range(3))
            +sum(Y[i][a]**2 for i in t for a in range(3)) for t in cells]
    A.append([f0[j]*traces[j] for j in range(63)])
    assert len(A)==55
    H=nullspace(A)
    assert len(H)>=8
    h=H[0]
    eps=min(F(d[i],2*abs(h[i])) for i in range(63) if h[i])
    fake=[F(d[i])+eps*h[i] for i in range(63)]
    assert min(fake)>0 and fake!=list(map(F,d))
    assert all(dot(row,h)==0 for row in A)
    assert dot(f0,fake)==D
    for a in range(3):
        assert sum(f0[j]*fake[j]*sum(Y[i][a] for i in t)
                   for j,t in enumerate(cells))==0
    assert sum(f0[j]*fake[j]*traces[j] for j in range(63))==sum(f0[j]*d[j]*traces[j] for j in range(63))
    violations=[(i,dot(row,fake)) for i,row in enumerate(LY) if dot(row,fake)!=0]
    assert violations
    obj=dict(identity='NOVA54_MP45_FULL_TENSOR_MASS_RIGIDITY_V1',facets=FS,fixture=X,
             cells=cells,boundary_cycles=beta,actual_six_volumes=d,
             minor_rows=rr,minor_columns=cols,minor_row_labels=[labels[i] for i in rr],
             minor_determinant=delta,actual_centroid=[str(x) for x in centre],
             scalar_control_kernel_dimension=len(H),perturbation=h,epsilon=str(eps),
             counterfeit_six_volumes=[str(x) for x in fake],
             failed_full_tensor_rows=[[i,str(v)] for i,v in violations])
    raw=(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode()
    Path('mp45_mass_gate.json').write_bytes(raw)
    print('NOVA54_MP45_MASS_RIGIDITY_63_53_10_100_62_PASS')
    print('POSITIVE_SCALAR_COUNTERFEIT_FAILS_FULL_TENSOR_MOMENTS_PASS')
    print('mp45_mass_gate.json',len(raw),hashlib.sha256(raw).hexdigest())

if __name__=='__main__':
    main()
```

## 9. A complete continuous physical domain for the remaining cases

The eight remaining assigned cases can be placed in one complete affine chart without fitting tetrahedron weights.

The actual facet 012 and vertex 3 are affinely independent. Normalize

`q0=0, q1=e1, q2=e2, q3=e3`.

The coordinates of `q4,...,q8` are fifteen unrestricted real shape variables. For every listed oriented facet `f` and every `a` outside it, impose

`det(q_f0-q_a, q_f1-q_a, q_f2-q_a) > 0`.

These are the 84 strict supporting tests for the literal simplicial graph. They retain the entire strict realization space in this chart, not a bounded numerical region.

Using the actual root3 fan, set

`tau_f = det(q_f0-q3, q_f1-q3, q_f2-q3)` for facets not containing 3,

`D = sum tau_f`,

`b = sum tau_f (q3+q_f0+q_f1+q_f2)`,

`y_i = 4 D q_i - b`.

Then the actual centered vertices are `y_i/(4D)`. Use the common metric

```
M = [[1,a,bm],[a,c,d],[bm,d,e]]
```

with `c-a^2 > 0` and `det(M)>0`. Fixing the first diagonal entry to one only removes a positive metric scale; all SPD metrics are represented.

For each remaining literal parent array impose the eight polynomial inequalities

`y_i^T M (y_parent(i)-y_i) >= 0`.

Impose its corresponding strict leaf-above-first-chain inequality from the table in Section 3. This gives a complete unbounded **15-shape plus 5-metric variable** domain for the remaining strict simplicial realization/weak-escape problem. The masses, centroid, and all first/second moments in this domain are actual determinant quantities. A feasible weak-escape solution would still not by itself be a nondegenerate 110 attainer or settle the stable side of the C32 problem.

The mass-rigidity theorem applies wherever the full tensor matrix has rank 62. Any use of a particular nonzero minor must preserve the complementary minor-zero branch. No rank-drop locus or metric-boundary approach is silently removed.

## 10. Useful continuation and exact scope of what remains

The next recovery task should be **targeted**, not another unrestricted search. The root3 graph has 66 terminal long-broom candidates under the accepted structural reduction; 55 are outside the assigned eleven and have old successful plans. Reconstruct those 55 first, retaining their original root3 parent indices. Completing those checks would connect the new assigned-case work to an independently replayed root3 frontier. The broader selected-root structural cover contains 720 terminal brooms, with 709 old successful plans and the eleven assigned gaps; that is a much smaller recovery obligation than regenerating the whole historical stream.

For extracting the root3 obligations, use the authenticated `comb.py`, `reconstruct.py`, and `plan.json`, enumerate `comb.parent_trees` on the literal graph, select the long-broom shape and a terminal facet, and filter `reconstruct.iterjobs` by the literal facet list, root 3, and those parent arrays. The following complete extraction unit supplies the exact 55-plan input; it performs no numerical optimization.

Save it inside `nova54_recovery` as `targeted_plans.py` and run `python targeted_plans.py` in that directory.

```python
from pathlib import Path
import json,hashlib
import comb
from reconstruct import iterjobs
FS=tuple(tuple(map(int,s)) for s in
 '014 021 032 043 125 154 235 347 365 376 458 487 568 678'.split())
G=comb.catalogue(True)
assert tuple(map(tuple,G[45]['facets']))==FS
parents=comb.parent_trees(G[45],3)
assert len(parents)==9140
assigned={1200,1205,1472,1752,1775,3058,3124,3149,3966,5772,7000}
shape=comb.root_code(parents[1200],3)
triangles={frozenset(f) for f in FS}
selected={}
for index,p in enumerate(parents):
    if comb.root_code(p,3)!=shape:
        continue
    paths=[]
    for i in range(9):
        path=[i]
        while path[-1]!=3:
            path.append(p[path[-1]])
        paths.append(path)
    b=list(reversed(max(paths,key=len)))
    assert len(b)==8
    b.append(next(i for i in range(9) if i not in b))
    if frozenset(b[5:8]) in triangles:
        selected[tuple(p)]=dict(original_index=index,parent=list(p),broom_order=b)
assert len(selected)==66
wanted={p:r for p,r in selected.items() if r['original_index'] not in assigned}
assert len(wanted)==55
meta=json.loads(Path('plan.json').read_bytes())
out=[]
for serial,g,root,p,plan in iterjobs(meta):
    key=tuple(p)
    if root==3 and tuple(map(tuple,g['facets']))==FS and key in wanted:
        out.append(dict(**wanted[key],serial=serial,plan=plan))
assert len(out)==55 and len({r['original_index'] for r in out})==55
out.sort(key=lambda r:r['original_index'])
raw=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode()
Path('mp45_root3_55_old_plans.json').write_bytes(raw)
print('MP45_ROOT3_55_OLD_SUCCESSFUL_PLANS_EXTRACTED_NO_NEW_EXCLUSION_ASSERTED')
print(len(raw),hashlib.sha256(raw).hexdigest())
```

The unfinished exploratory extensions used all 34 forbidden-redirection signs, and also considered adding the actual centroid as a tenth apex with fourteen additional actual tetrahedra. No completed exclusion is claimed from those extensions. Nonpositive locator margins were not interpreted as physical feasibility, and interrupted solves were not interpreted as infeasibility certificates.

The substantive geometric continuation is now the eight strict top-leaf domains, with one common shape, one common metric, actual determinant masses, and full tensor cycle moments. The rank-62 result explains exactly when fitted mass variables can be eliminated, while the counterfeit control explains why scalar-trace or independently lifted PSD feasibility is not a physical witness.

Finally, C32 propagation remains a separate proof obligation. It needs actual polygon facets, explicit genuine triangulations, cofacial-zero accounting, true-edge escape coverage, and canonical vertex/root maps. No extra triangulation diagonal may be asserted to be an available physical escape edge. None of the uncompleted broad replay or lifting work in this run justifies accepting the earlier 57-type rollup.
