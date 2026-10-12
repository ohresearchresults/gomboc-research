# material-bd58b3857129

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# H5_FULL_BASAL_LAMBDA_GE_3_5_DYADIC_V1
Recovery capsule part 3/3: proof, exact reconstruction and complete verification source.

## Theorem
Every genuine homogeneous body of the literal H5 heptagon/triangle family, with full x,r in [0,1], p,q>=0, p+q<=1, and 3/5<=lambda<1, has at least two strict unstable vertices for every common SPD affine metric, even permitting additional weak contacts. All complete weak rooted true-edge cones are excluded for every nonzero PSD metric. Collapsed shape endpoints assert indexed polynomial matrices, not a true ten-vertex face lattice.

This extends the accepted full-basal lambda>=2/3, 3/4, 4/5 and 511/512 collars. It does not exclude all H5 realizations, all E17 types, or provide an attaining proper110 body. The accepted global interval 34<=C_min<=622 remains unchanged.

## Complete exact recovery dependencies
All three parts of this capsule AND the original geometry module are required. The two data parts contain literal decimal triples, not an optimizer seed, summary, encoded archive or omitted arrays. Each non-PATH line is one certificate, with each triple (source label,target label,positive integer weight). PATH lines describe exact parameter subdivisions. Part 1 is the root node; part 2 supplies every other node, including empty intermediate nodes needed to prove a complete partition.

- Geometry: [internal-source-reference]. Extract its complete Python block as h5_collar_weighted.py, 9389 bytes, SHA256 18d63fc0ed4267051d54e63e780554d042d92d44a38bd445b14effe066c4ac7d.
- Part 1: [internal-source-reference]. Save verbatim as h5_three_fifths_root_rows.txt, 16844 bytes, SHA256 4a2eb99c3df47cf4e34eb74694d4a6b5f33340d894f81000cc309acb41dcdeb0.
- Part 2: [internal-source-reference]. Save verbatim as h5_three_fifths_cell_rows.txt, 6431 bytes, SHA256 efd1b9732d6c6046222bb34d22cb1b486a92b13252136c12f0a67c6d9841e7b7.
- Part 3: this complete material. First Python block is recover_h5_three_fifths.py, 1631 bytes, SHA256 d4aa7f107b706add31141546a9250bb5403173278d593e60cbfadf1af8258c60. Second block is verify_h5_subdivision.py, 5973 bytes, SHA256 ec89a59a9815e809d371cb9d6ce1022f9b70c0cecc11c9a34174f18d64a26cd7.

Commands:
python recover_h5_three_fifths.py --root h5_three_fifths_root_rows.txt --cells h5_three_fifths_cell_rows.txt --output h5_three_fifths_atlas.json
OPENBLAS_NUM_THREADS=1 python verify_h5_subdivision.py --atlas h5_three_fifths_atlas.json --output h5_three_fifths_report.json

Reproduced literal atlas: 34289 bytes, SHA256 967640b387993a9297e0fae367b4e817e34b9c090530288adb4d842b138957c8. Recovery terminal RECOVERY_PASS.
Report: 1041 bytes, SHA256 b01cd22973e4bbf4ca655766f1817601980c4aa5e2a6db4757ab6b25be540705. Expected verdict PASS, uncovered_rooted_cones=0. Coordinator executed exact reconstruction and verification with Python3.13.5 and NumPy2.3.5. No optimizer or floating point enters these proof programs.

## Literal body and actual moments
Set s=1-lambda. The basal seven vertices are s times (1/4,0),(1-3x/4,0),(1-p,p),(q,1-q),(0,1-3r/4),(0,1/4),(1/16,1/16), at height zero. Top labels7,8,9 are (0,0,1),(lambda,0,1),(0,lambda,1). True outward facets are (6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),(9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9).

The geometry module computes D=6V and K=6J from all oriented boundary triangles and checks all four full polynomial identities. Thus g=K/D is the actual uniform volume centroid. With A=(31-24xp-24rq)/64>=7/64, D=1-s+2As^2>=3/5 on 0<=s<=2/5. There is no freely chosen center or vertex mass.

## Positive original-arrow stresses on a complete subdivision
For each actual arrow i->j, let B_ij=sym((D z_i-K)(z_i-z_j)^T). Each stored certificate P=sum w_ij B_ij has positive integer weights. Entry degrees are at most 3 in x, 3 in r, total3 in (p,q), and4 in s. The product Bernstein basis therefore has 4*4*10*5=800 nonnegative functions summing to one on each product parameter cell.

The atlas has83 nodes,48 leaves, maximum path depth5. A path step uses axis0=x, axis1=r, axis2=(p,q) triangle, or axis3=s. Interval axes split at the midpoint into side0 and side1. The triangle splits into its four midpoint subtriangles, with barycentric vertices exactly as listed in VERTS in the verifier. Its denominator2 integer coordinates are explicit. All cell transforms are exact de Casteljau/blossom matrices with nonnegative entries and row sums equal to their common denominator. The triangle degree3 transform sums over all27 blossom choices; no enclosing square replaces the actual triangle.

At each node every stored matrix coefficient is proved positive definite by its three exact leading Sylvester minors. There are686 certificates:532 at the root and154 at other nodes. Sizes3/4/5/6/7/8 occur163/78/140/182/107/16 times. Maximum integer weight7037, maximum sum16385. The proof checks548800 coefficient matrices and1646400 positive leading minors. NumPy is used only for checked integer linear combinations; all determinant operations are arbitrary Python integers. Each coefficient table has an explicit positive integer scale; normalization divides the table and scale by their exact common gcd.

For each certificate the least determinant and greatest trace across its800 coefficient matrices give a positive bound via lambda_min(M)>=4det(M)/trace(M)^2. Taking the minimum over all certificates yields the exact uniform scaled-stress gap
P >= (178029/44800000000) I
on the relevant certificate cell. The certificate may differ between cells and between trees, but this one positive bound applies throughout the finite atlas.

The graph has4879 unrooted spanning trees and48790 rooted orientations. Literal arrow-mask containment computes which complete trees contain each certificate. Coverage is inherited from ancestors. For every branching node the verifier requires every side of exactly one split axis, and every node must have a parent. Every leaf must cover all48790 rooted trees. Consequently every point of the entire domain and every complete rooted true-edge tree has a contained PD certificate. There are no discarded residual cells or trees.

For a common nonzero PSD metric H making every tree arrow weakly increasing, each contained B_ij has trace(H B_ij)<=0. The positive sum would satisfy trace(H P)<=0, contradicting trace(H P)>0. Thus all such rooted cones are excluded.

For a genuine SPD body, any vertex which is not a strict unstable vertex has a neighboring arrow with nonnegative radial derivative. Such an arrow strictly increases squared metric distance, since its distance difference equals twice that derivative plus the positive squared edge length. A graph choosing one such arrow per nonsink is acyclic. With only one strict unstable vertex it supplies a rooted spanning tree, already excluded. Hence U>=2 even when some contacts are weak.

## What changed and what failed
A global constant-weight original-arrow search on s<=2/5 gave661 certificates covering48616 trees, leaving174. The first x/r-only refinement still had132 tree-cell failures. Adding the physical triangle and taper midpoint subdivisions closed the remainder; greedy containment compression gives the present686-certificate atlas. These failed relaxations did not establish feasible physical metrics. This subdivision acts on exact original-arrow polynomials, not on the earlier globally lowered quadratic relaxation whose failure cannot be repaired by subdividing that lowering.

## Complete reconstruction source
```python
"""Reconstruct the literal atlas from both complete, plain-text row parts."""
from pathlib import Path
import argparse,hashlib,json
EXPECTED=('4a2eb99c3df47cf4e34eb74694d4a6b5f33340d894f81000cc309acb41dcdeb0','efd1b9732d6c6046222bb34d22cb1b486a92b13252136c12f0a67c6d9841e7b7')
TARGET='967640b387993a9297e0fae367b4e817e34b9c090530288adb4d842b138957c8'
def recover(root,cells,output):
    data=[]
    for name,expected in zip((root,cells),EXPECTED):
        raw=Path(name).read_bytes();assert hashlib.sha256(raw).hexdigest()==expected
        data.append(raw.decode('utf-8'))
    nodes=[]
    for line in ''.join(data).splitlines():
        if line.startswith('PATH '):
            tail=line[5:];path=[] if tail=='ROOT' else [list(map(int,s.split(','))) for s in tail.split()]
            assert all(len(p)==2 for p in path)
            nodes.append({'path':path,'certificates':[]})
        else:
            cert=[list(map(int,s.split(','))) for s in line.split()]
            assert cert and all(len(t)==3 for t in cert)
            nodes[-1]['certificates'].append(cert)
    o={'identity':'H5_FULL_BASAL_LAMBDA_GE_3_5_DYADIC_V1','s_max':'2/5','nodes':nodes}
    raw=(json.dumps(o,separators=(',',':'))+'\n').encode()
    assert len(nodes)==83 and len(raw)==34289 and hashlib.sha256(raw).hexdigest()==TARGET
    Path(output).write_bytes(raw);print('RECOVERY_PASS',len(raw),TARGET)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',required=True);p.add_argument('--cells',required=True);p.add_argument('--output',default='h5_three_fifths_atlas.json');a=p.parse_args();recover(a.root,a.cells,a.output)
```

## Complete verification source
```python
"""Exact original-arrow Bernstein atlas with complete parameter partitions.
Proof dependencies: h5_collar_weighted.py and one literal subdivision JSON.
No optimization or floating point is used here.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,itertools,json,math
import numpy as np
from h5_collar_weighted import exact_geometry,EDGES,orient,matrix_polynomials,bernstein_coefficients,BASIS,minors

TRI=tuple((p,q) for p in range(4) for q in range(4-p))
TRI_IDX={a:i for i,a in enumerate(TRI)}
VERTS=(((2,0,0),(1,1,0),(1,0,1)),((1,1,0),(0,2,0),(0,1,1)),((1,0,1),(0,1,1),(0,0,2)),((1,1,0),(0,1,1),(1,0,1)))

def normalize(T,L):
    g=math.gcd(L,int(np.gcd.reduce(np.abs(T).ravel())))
    return T//g,L//g

def subdivide(T,L,axis,side):
    assert axis in range(4) and side in range(4 if axis==2 else 2)
    if axis==2:
        A=np.zeros((10,10),np.int64)
        for row,(p,q) in enumerate(TRI):
            vv=[VERTS[side][0]]*(3-p-q)+[VERTS[side][1]]*p+[VERTS[side][2]]*q
            for choices in itertools.product(range(3),repeat=3):
                A[row,TRI_IDX[choices.count(1),choices.count(2)]]+=math.prod(vv[k][j] for k,j in enumerate(choices))
        den=8;ax=3
    else:
        n=4 if axis==3 else 3;ax=4 if axis==3 else axis+1
        den=2**n;A=np.zeros((n+1,n+1),np.int64)
        for i in range(n+1):
            for j in range(n+1):
                if side==0 and j<=i:A[i,j]=math.comb(i,j)*2**(n-i)
                if side==1 and j>=i:A[i,j]=math.comb(n-i,j-i)*2**i
    assert np.all(A.sum(axis=1)==den)
    assert int(np.abs(T).max())*den<2**63
    out=np.tensordot(A,T.reshape(34,4,4,10,5,6),axes=(1,ax))
    return normalize(np.moveaxis(out,0,ax).reshape(T.shape),L*den)

def build(S):
    z,D,K=exact_geometry();arrows=sorted((i,j) for a,b in EDGES for i,j in ((a,b),(b,a)))
    pp=[matrix_polynomials(z,D,K,*a) for a in arrows]
    pd=math.lcm(*(v.denominator for ps in pp for p in ps for v in p.values()))
    L=pd*648*S.denominator**4
    cols=[[bernstein_coefficients(p,S,L) for p in ps] for ps in pp]
    assert max(abs(v) for a in cols for c in a for v in c)<2**63
    T=np.array(cols,dtype=np.int64).transpose(0,2,1)
    T,L=normalize(T,L);return arrows,T,L

def tree_masks(arrows):
    idx={a:k for k,a in enumerate(arrows)};masks=[];nt=0
    for es in itertools.combinations(EDGES,9):
        if orient(es,0) is None:continue
        nt+=1
        for root in range(10):masks.append(sum(1<<idx[a] for a in orient(es,root)))
    assert nt==4879 and len(masks)==48790
    return np.array(masks,dtype=np.uint64)

def verify(atlas_path,output):
    raw=Path(atlas_path).read_bytes();o=json.loads(raw);S=F(o['s_max']);assert 0<S<1
    ar,T,L=build(S);idx={a:i for i,a in enumerate(ar)};tm=tree_masks(ar)
    nodes={tuple(map(tuple,c['path'])):c['certificates'] for c in o['nodes']}
    assert len(nodes)==len(o['nodes']) and () in nodes
    children={p:[] for p in nodes}
    for p in nodes:
        if p:assert p[:-1] in nodes;children[p[:-1]].append(p[-1])
    visited=set();gaps=[];certificate_count=0;size_counts={};matrices=0;leaves=0;max_weight=0;max_sum=0;max_depth=0
    def visit(path,T,L,covered):
        nonlocal certificate_count,matrices,leaves,max_weight,max_sum,max_depth
        visited.add(path);max_depth=max(max_depth,len(path));cover=covered.copy()
        for cert in nodes[path]:
            assert cert and len(set((i,j) for i,j,w in cert))==len(cert)
            assert all((i,j) in idx and type(w) is int and w>0 for i,j,w in cert)
            ws=sum(w for i,j,w in cert);assert int(np.abs(T).max())*ws<2**63
            P=sum((w*T[idx[i,j]] for i,j,w in cert),np.zeros((len(BASIS),6),np.int64))
            md=None;mt=0
            for row in P:
                mm=minors(row);assert min(mm)>0,('non-PD',path,cert,mm)
                md=mm[2] if md is None else min(md,mm[2]);mt=max(mt,int(row[0])+int(row[3])+int(row[5]))
            gaps.append(F(4*md,mt*mt*L));certificate_count+=1;matrices+=len(BASIS)
            size_counts[len(cert)]=size_counts.get(len(cert),0)+1
            max_weight=max(max_weight,max(w for i,j,w in cert));max_sum=max(max_sum,ws)
            m=np.uint64(sum(1<<idx[i,j] for i,j,w in cert));cover|=(tm&m)==m
        cc=children[path]
        if not cc:
            leaves+=1;assert cover.all(),('uncovered leaf',path,int((~cover).sum()));return
        axes={a for a,s in cc};assert len(axes)==1;axis=axes.pop()
        assert sorted(s for a,s in cc)==list(range(4 if axis==2 else 2)),('incomplete partition',path,cc)
        for side in sorted(s for a,s in cc):
            U,LL=subdivide(T,L,axis,side);visit(path+((axis,side),),U,LL,cover)
    visit((),T,L,np.zeros(len(tm),bool));assert visited==set(nodes)
    report={'identity':o['identity'],'verdict':'PASS','s_max':str(S),'lambda_min':str(1-S),
      'atlas_sha256':hashlib.sha256(raw).hexdigest(),'domain':'full x,r unit square, full p/q triangle, 0<=s<=s_max',
      'actual_moments':'D=6V,K=6J; four full boundary polynomial identities',
      'nodes':len(nodes),'leaves':leaves,'max_partition_depth':max_depth,'certificate_count':certificate_count,
      'size_counts':size_counts,'max_weight':max_weight,'max_weight_sum':max_sum,
      'coefficient_matrices':matrices,'positive_sylvester_minors':3*matrices,'uniform_scaled_stress_gap':str(min(gaps)),
      'unrooted_trees':4879,'rooted_trees':len(tm),'uncovered_rooted_cones':0,
      'scope':'All genuine literal H5 bodies on the domain have U>=2 under every SPD metric, even with weak contacts. Nonzero PSD weak rooted cones excluded. Collapsed endpoints are indexed matrices only; not all H5 or E17 and not attainment.'}
    Path(output).write_text(json.dumps(report,sort_keys=True,indent=2)+'\n');print(json.dumps(report,indent=2));return report
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--atlas',required=True);p.add_argument('--output',required=True);a=p.parse_args();verify(a.atlas,a.output)
```
