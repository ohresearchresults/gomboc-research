# material-03b93a1aba81

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# H5_FULL_BASAL_LAMBDA_GE_3_4_V1

## Theorem
Every genuine homogeneous H5 heptagon–triangle body on the full domain 0<=x,r<=1, p,q>=0, p+q<=1, and 3/4<=lambda<1 has at least two strict unstable vertices under every positive definite affine metric. Weak contacts are allowed in this exclusion. The corresponding weak rooted cones are excluded for every common nonzero PSD metric. Degenerate shape endpoints and lambda=1 assert polynomial matrix limits only, not proper ten-vertex bodies.

This is the same literal geometry as H5_FULL_BASAL_LAMBDA_GE_4_5_V1, not a larger unnamed combinatorial class. The new interval strictly extends the old full-basal lambda>=4/5 and lambda>=511/512 collars. Global accepted 34<=C_min<=622 is unchanged; this does not exclude all H5 parameters, all E17 types, or supply an attaining example.

## Exact recovery dependencies
Supply ALL THREE complete materials for a computational continuation:
1. `[internal-source-reference]`: complete geometry, true moments, rational polynomial algebra, Bernstein conversion and graph code. Extract its complete Python block as `h5_collar_weighted.py`, 9389 bytes, SHA-256 18d63fc0ed4267051d54e63e780554d042d92d44a38bd445b14effe066c4ac7d.
2. `[internal-source-reference]`: the entire literal JSON atlas, 10743 bytes, SHA-256 937c60eccc01a8d6496c35b7808bc12031248fd7f54c3e1abb8d8239521a959c. Save its text verbatim as `h5_three_quarters_atlas.json`, or pass its original .json.txt name through --atlas. The material receipt hash and byte count match the exact executed input.
3. This complete verifier/proof material. Extract its Python block as `verify_h5_three_quarters.py`, 4246 bytes, SHA-256 6542edc33b841b903a592dad32d038eacef2be20bb352be36adca130d68c1db7.

Run:
`OPENBLAS_NUM_THREADS=1 python verify_h5_three_quarters.py --atlas h5_three_quarters_atlas.json --output h5_three_quarters_report.json`

Author-executed environment: Python3.13.5, NumPy2.3.5. Output h5_three_quarters_report.json:1290 bytes, SHA-256 496284bdd09d16cab23d02b8a9748a20c6e597992a59d75693a3816c47799f8b. Expected verdict PASS; failed_certificate_count=0; uncovered_rooted_trees=0. The numerical proposal optimizer is not used in reconstruction or verification.

## What changed scientifically
Keeping just the 260 fixed quotient-lift supports gives 208 exact positive three-arrow supports on the whole lambda>=3/4 domain, initially covering46581 of48790 rooted trees. Adding one internal basal arrow gives120 certified four-arrow supports, covering1654 more by that initial assignment rule. Testing all literal certificate containments, not just the originally selected quotient support, leaves479 trees; retaining further original arrows supplies exact positive stresses for all of them. Greedy compression leaves332 certificates of sizes3/4/5/6/7 in counts208/54/32/22/16. These are the complete literal atlas, not a summary of omitted data. Maximum integer weight147; maximum sum192.

The exact control in [internal-source-reference] explains why the added arrows are essential: at x=r=p=q=1/10,lambda=3/4, one selected three-arrow support has a genuine compatible SPD metric, but the body has unstable vertices4 and8. The extra original arrows forbid this second sink. That control is not a counterexample to the present complete atlas.

## Proof
Use s=1-lambda, D=6V, K=6J and g=K/D from the literal oriented boundary. The geometry module verifies the four exact volume/moment identities, so the center is the actual volume centroid. D=1-s+2As^2 is positive throughout 0<=s<=1/4, because A=(31-24xp-24rq)/64>=7/64.

For every atlas row (i,j,w), form w*sym((D zi-K)(zi-zj)^T). Sum these matrices over a certificate. Its entries are polynomials of degree at most3 in x,3 in r,total3 in(p,q), and4 in s. Expand in the nonnegative partition-of-unity product Bernstein basis on x,r in[0,1], the full p,q triangle, and u=4s in[0,1]. There are800 coefficient matrices per certificate. Exact integer Sylvester tests prove all332*800=265600 matrices PD, using796800 strictly positive leading minors. No sampling or floating-point eigenvalue threshold enters the proof.

The common integer coefficient scale is L=5435817984. Across every certified matrix the three least leading minors are46361160,12912362128502784,19348361922325031021445120, and the largest trace is941755465728. Hence every stress polynomial is at least delta I with delta=1085023774385/67589038045157916672>0, by lambda_min(M)>=4det(M)/trace(M)^2 and Bernstein convexity. Integer accumulators are checked before NumPy operations; all determinants are Python arbitrary integers.

Enumerate all connected9-edge subsets of the17 true edges and orient each toward each of10 roots. This is4879 unrooted and48790 rooted trees. Literal bit-mask inclusion shows that each tree contains at least one complete positive-weight certificate from the332-row atlas. Coverage does not assume that this certificate is the particular quotient lift originally chosen during discovery.

If a common nonzero PSD metric H made every tree arrow weakly increasing, trace(H*P)<=0 for its contained certificate. Positive definiteness instead gives trace(H*P)>=delta*trace(H)>0, contradiction. If a genuine SPD-metric body had just one strict unstable vertex, every other vertex would have an adjacent nonnegative radial derivative. Such an arrow strictly increases squared metric distance because the edge has positive metric length, even when the derivative is zero. These arrows therefore generate an acyclic rooted tree to the unique sink, already excluded. Thus U>=2, independently of weak contacts elsewhere.

## Complete verifier
```python
"""Exact continuous-domain H5 certificate atlas and all-root tree coverage.
Requires h5_collar_weighted.py and the literal h5_three_quarters_atlas.json.
The numerical search that proposed the atlas is not part of this proof kernel.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,itertools,json,math
import numpy as np
from h5_collar_weighted import (exact_geometry,EDGES,orient,matrix_polynomials,
                               bernstein_coefficients,BASIS,minors)

def verify(atlas_path,s_max,output):
    raw=Path(atlas_path).read_bytes();atlas=json.loads(raw)
    S=F(s_max or atlas['s_max']);assert 0<S<1
    certs=atlas['certificates']
    for c in certs:
        assert len({(i,j) for i,j,w in c})==len(c)
        assert all(type(w) is int and w>0 for i,j,w in c)
    z,D,K=exact_geometry()
    arrows=sorted((i,j) for a,b in EDGES for i,j in ((a,b),(b,a)))
    idx={a:k for k,a in enumerate(arrows)}
    mask=lambda es:sum(1<<idx[tuple(e)] for e in es)
    polys={a:matrix_polynomials(z,D,K,*a) for a in arrows}
    pd=math.lcm(*(v.denominator for pp in polys.values() for p in pp for v in p.values()))
    L=pd*648*S.denominator**4;max_weight_sum=max(sum(w for i,j,w in c) for c in certs)
    T={}
    for ar,pp in polys.items():
        cols=[bernstein_coefficients(p,S,L) for p in pp]
        bound=max(abs(v) for col in cols for v in col)
        assert bound*max_weight_sum<2**63,'Signed integer accumulator could overflow'
        T[ar]=np.array(cols,dtype=np.int64).T
    small=[None]*3;large_trace=0;failed=[];cm=[];valid_sizes={}
    for k,c in enumerate(certs):
        P=sum((w*T[i,j] for i,j,w in c),np.zeros((len(BASIS),6),dtype=np.int64))
        leading=[minors(row) for row in P]
        if not all(min(mm)>0 for mm in leading):failed.append(k);continue
        cm.append(mask((i,j) for i,j,w in c))
        valid_sizes[len(c)]=valid_sizes.get(len(c),0)+1
        for row,mm in zip(P,leading):
            for j,t in enumerate(mm):small[j]=t if small[j] is None else min(small[j],t)
            large_trace=max(large_trace,int(row[0])+int(row[3])+int(row[5]))
    unrooted=0;rooted=0;uncovered=[]
    for es in itertools.combinations(EDGES,9):
        if orient(es,0) is None:continue
        unrooted+=1
        for root in range(10):
            ar=orient(es,root);tm=mask(ar);rooted+=1
            if not any(tm&m==m for m in cm):uncovered.append((root,ar))
    assert (unrooted,rooted)==(4879,48790)
    gap=F(4*small[2],large_trace**2*L) if cm else None
    result={'identity':'H5_FULL_BASAL_LAMBDA_GE_3_4_V1','s_max':str(S),'lambda_min':str(1-S),
            'actual_moments':'D=6V and K=6J checked against the complete boundary',
            'domain':'0<=x,r<=1; p,q>=0; p+q<=1; 0<=s<=s_max',
            'atlas_sha256':hashlib.sha256(raw).hexdigest(),'atlas_certificates':len(certs),
            'valid_certificate_size_counts':valid_sizes,'failed_certificate_count':len(failed),
            'first_failed_certificate_indices':failed[:10],
            'coefficient_matrices_per_certificate':len(BASIS),
            'validated_coefficient_matrices':len(cm)*len(BASIS),'validated_sylvester_minors':3*len(cm)*len(BASIS),
            'integer_matrix_scale':L,'max_weight_sum':max_weight_sum,
            'minimum_integer_leading_minors':small,'maximum_integer_trace':large_trace,
            'uniform_scaled_stress_gap':str(gap),'unrooted_trees':unrooted,'rooted_trees':rooted,
            'uncovered_rooted_trees':len(uncovered),'first_uncovered_rooted_trees':uncovered[:2],
            'verdict':'PASS' if not uncovered else 'INCOMPLETE_ATLAS',
            'scope':'All genuine H5 bodies in the stated domain have U>=2 under every SPD metric, even allowing weak contacts, when verdict is PASS. Collapsed endpoints assert matrices only. No E17-wide or attaining claim.'}
    Path(output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--atlas',default='h5_three_quarters_atlas.json');p.add_argument('--s-max');p.add_argument('--output',default='h5_three_quarters_report.json');a=p.parse_args()
    verify(a.atlas,a.s_max,a.output)
```
