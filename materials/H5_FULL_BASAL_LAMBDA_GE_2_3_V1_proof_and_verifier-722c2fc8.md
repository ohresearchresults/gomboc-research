# material-722c2fc8cf34

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# H5_FULL_BASAL_LAMBDA_GE_2_3_V1

## Theorem and boundary
Every genuine homogeneous polyhedron in the literal H5 heptagon/triangle family, with 0<=x,r<=1, p,q>=0, p+q<=1 and 2/3<=lambda<1, has at least two strict unstable vertices under every common SPD affine metric. This exclusion allows additional weak contacts. More strongly, every complete weak rooted true-edge cone is excluded for every nonzero PSD metric. Degenerate endpoints concern indexed polynomial matrices only, not a claimed true ten-vertex lattice.

This extends the accepted full-basal lambda>=3/4, 4/5 and 511/512 collars. It is not an E17-wide exclusion and does not give attainment. Global accepted 34<=C_min<=622 is unchanged.

## Complete exact recovery pack: all three required
1. [internal-source-reference]: extract the entire Python block as h5_collar_weighted.py, 9389 bytes, SHA256 18d63fc0ed4267051d54e63e780554d042d92d44a38bd445b14effe066c4ac7d. This is the complete geometry, actual moments, sparse polynomial algebra, true graph and Bernstein kernel. No other earlier atlas is required.
2. [internal-source-reference]: save the complete literal text as h5_two_thirds_atlas.json, 18398 bytes, SHA256 780abadad78c31b42b2f133a00eafd07c892f43c62e4f447fb32f3634a1c9b03.
3. This material: extract the complete Python block as verify_h5_atlas.py, 3524 bytes, SHA256 467ff4d1b5e3afdf23afd3fa748c9995b8da6dd4c8eca206c24fb75b9c1da32b.

Verification/reconstruction command:
OPENBLAS_NUM_THREADS=1 python verify_h5_atlas.py --atlas h5_two_thirds_atlas.json --output h5_two_thirds_report.json

Coordinator executed with Python3.13.5 and NumPy2.3.5. No optimizer is used by the proof kernel. Report h5_two_thirds_report.json:1166 bytes,SHA256 bd207fe37f7ea7477b0ef7ad1fa941dcfd8c1f90f95189973341fe7c3b2d4b19. Expected verdict PASS, failed_certificates=0, uncovered_rooted_trees=0.

## Literal geometry and true center
Set s=1-lambda. The seven basal coordinates before multiplication by s are (1/4,0),(1-3x/4,0),(1-p,p),(q,1-q),(0,1-3r/4),(0,1/4),(1/16,1/16); append height zero. The top vertices7,8,9 are (0,0,1),(lambda,0,1),(0,lambda,1). The outward true facets are (6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),(9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9). Their edge set has17 edges.
The source derives D=6V and K=6J directly from every oriented boundary triangle, and asserts all four multivariate identities. Thus g=K/D is the actual homogeneous volume centroid, never a vertex average or free mass assignment. D=1-s+2As^2 with A=(31-24xp-24rq)/64>=7/64, so D>0 on 0<=s<=1/3.

## Exact stress proof
For an original arrow i->j put B_ij=sym((D z_i-K)(z_i-z_j)^T). Every atlas certificate is a positive integer sum P=sum w_ij B_ij. Its entries have degree at most3 in x,3 in r,total3 in(p,q),4 in s. On [0,1]^2 times the full p/q triangle times s in[0,1/3], expand in the product Bernstein basis of those degrees: 800 coefficient matrices. All Bernstein basis functions are nonnegative and sum to one.
The 461 literal certificates have sizes3,4,5,6,7,8 in counts140,36,155,97,31,2; maximum weight60 and maximum weight sum128. Exact integer Sylvester tests check every one of368800 coefficient matrices, hence1106400 positive leading minors. Common matrix scale L=1719926784. The three minimum leading minors are20010240,1563187910618880,642167641403354850656256; maximum trace61057400832. Thus P>=delta I, where delta=113814715213/284103505285742592>0, by lambda_min(M)>=4det(M)/trace(M)^2 and convexity. Checked integer accumulation prevents overflow; determinants are Python arbitrary integers.
Enumerate all connected9-edge subsets of the17 true edges, then each of10 roots:4879 unrooted and48790 rooted trees. Literal bitmask containment verifies every rooted tree contains a complete certificate. There is no quotient-only feasibility assumption in this covering step.
If a nonzero PSD metric H makes every arrow of a tree weakly increasing, then (z_i-g)^T H(z_j-z_i)>=0, so trace(H P)<=0 for its contained certificate. But P>=delta I gives trace(H P)>=delta trace(H)>0. This contradiction excludes every complete rooted cone.
For a genuine SPD body, any vertex that is not a strict unstable vertex has an adjacent arrow with nonnegative radial derivative. Such an arrow strictly increases squared H-distance, since the difference is twice this derivative plus a positive squared edge length. Hence choosing one such arrow per non-sink yields an acyclic graph. With one strict unstable sink it would contain an already excluded rooted tree. Therefore U>=2, even when some contacts are weak.

## Discovery, not proof
The initial four small weight choices certified140 three-arrow supports and covered43464 trees. For each uncovered tree, semidefinite cutting-plane linear programming proposed weights on its actual nine arrows. Rounding was accepted only after exact coefficient Sylvester tests.400 additional certified rows closed all48790 trees; deterministic greedy containment compression retained461 of540 proposals. This history explains the mechanism: retained original basal paths compensate for information discarded by quotient supports. The optimizer is dispensable once the literal atlas is preserved.
A separate bounded attempt on s<=1/2 found certificates covering46758 trees after1500 proposals, but did not close that larger domain. A failed Bernstein relaxation is not a physical metric witness or a proved method impossibility. This partial observation is not promoted as a global theorem.

## Complete verifier
```python
"""Exact original-arrow H5 atlas verifier; no optimizer used.
Requires the complete h5_collar_weighted.py and a literal JSON atlas.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,itertools,json,math,sys
import numpy as np
from h5_collar_weighted import exact_geometry,EDGES,orient,matrix_polynomials,bernstein_coefficients,BASIS,minors

def verify(atlas_path,output):
    raw=Path(atlas_path).read_bytes();atlas=json.loads(raw);S=F(atlas['s_max'])
    assert 0<S<1;certs=atlas['certificates'];assert certs
    z,D,K=exact_geometry()
    arrows=sorted((i,j) for a,b in EDGES for i,j in ((a,b),(b,a)));idx={a:k for k,a in enumerate(arrows)}
    for c in certs:
        assert c and len(set((i,j) for i,j,w in c))==len(c)
        assert all((i,j) in idx and type(w) is int and w>0 for i,j,w in c)
    polys={a:matrix_polynomials(z,D,K,*a) for a in arrows}
    pd=math.lcm(*(v.denominator for pp in polys.values() for p in pp for v in p.values()))
    L=pd*648*S.denominator**4;ws=max(sum(w for i,j,w in c) for c in certs);T={}
    for ar,pp in polys.items():
        cols=[bernstein_coefficients(p,S,L) for p in pp]
        assert max(abs(v) for col in cols for v in col)*ws<2**63
        T[ar]=np.array(cols,dtype=np.int64).T
    mask=lambda ar:sum(1<<idx[tuple(e)] for e in ar)
    cm=[];small=[None]*3;largest_trace=0;size_counts={}
    for k,c in enumerate(certs):
        P=sum((w*T[i,j] for i,j,w in c),np.zeros((len(BASIS),6),dtype=np.int64))
        for row in P:
            mm=minors(row);assert min(mm)>0,('nonpositive coefficient',k,mm)
            small=[m if v is None else min(v,m) for v,m in zip(small,mm)]
            largest_trace=max(largest_trace,int(row[0])+int(row[3])+int(row[5]))
        cm.append(mask((i,j) for i,j,w in c));size_counts[len(c)]=size_counts.get(len(c),0)+1
    rooted=0;unrooted=0
    for es in itertools.combinations(EDGES,9):
        if orient(es,0) is None:continue
        unrooted+=1
        for root in range(10):
            tm=mask(orient(es,root));rooted+=1
            assert any(tm&m==m for m in cm),('uncovered tree',root,es)
    assert (unrooted,rooted)==(4879,48790)
    gap=F(4*small[2],largest_trace**2*L)
    report={'identity':atlas['identity'],'verdict':'PASS','s_max':str(S),'lambda_min':str(1-S),
      'domain':'0<=x,r<=1; p,q>=0; p+q<=1; 0<=s<=s_max',
      'actual_moments':'four complete oriented-boundary polynomial identities, D=6V,K=6J',
      'atlas_sha256':hashlib.sha256(raw).hexdigest(),'certificate_count':len(certs),'size_counts':size_counts,
      'max_weight':max(w for c in certs for i,j,w in c),'max_weight_sum':ws,
      'coefficient_matrices':len(certs)*len(BASIS),'sylvester_minors':3*len(certs)*len(BASIS),
      'integer_matrix_scale':L,'minimum_leading_minors':small,'maximum_trace':largest_trace,
      'uniform_scaled_stress_gap':str(gap),'unrooted_trees':unrooted,'rooted_trees':rooted,
      'failed_certificates':0,'uncovered_rooted_trees':0,
      'scope':'Every genuine H5 body in this domain has U>=2 for every SPD metric, including weak contacts. Every nonzero PSD weak rooted cone is excluded. Collapsed endpoints concern indexed matrices only; no whole-E17 or attaining claim.'}
    Path(output).write_text(json.dumps(report,sort_keys=True,indent=2)+'\n');print(json.dumps(report,indent=2))
    return report
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--atlas',required=True);p.add_argument('--output',required=True);a=p.parse_args();verify(a.atlas,a.output)
```
