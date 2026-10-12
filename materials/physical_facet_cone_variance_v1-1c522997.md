# material-1c5229975025

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# PHYSICAL_FACET_CONE_VARIANCE_DECOMPOSITION_V1

## Status and exact dependencies
This is a coordinator-derived continuation of PHYSICAL_FACET_CONE_MARKOV_OBLIQUITY_V1, not a new complexity bound or a class110 construction. The accepted physical lower/upper bounds are unchanged. Necessary parent sources are the complete proof [internal-source-reference] and the complete executable [internal-source-reference]. Both were read through eof in this turn. This material contains the new analytic argument and the entire additional executable. It must be supplied together with that parent executable for computational reproduction. The numerical example remains a strict S5/U5/H8, weak0 quadrilateral pyramid.

## Actual second-moment identity
Let P be a full-dimensional bounded polytope in R^d, d>=2, with its true homogeneous solid centroid at the origin. Use the physical definitions from the parent: actual facet poles q_i, area centroids c_i, and centroid-based cone-volume probabilities w_i. Let Q,C have corresponding row vectors, D=diag(w), B=Q^T D Q, G=(dB)^(-1), Z=C-QG. Thus Q^T D C=I/d, Q^T D Z=0, and G is positive definite. Let Sigma_P=E_P[xx^T] be the true homogeneous solid covariance and let Sigma_i=E_{F_i}[(x-c_i)(x-c_i)^T] be the actual area covariance of facet i. Set S=sum_i w_i Sigma_i and T=Z^T D Z.

The exact identity is
(d+2)/d * Sigma_P = G/d + T + S.                         (1)
To prove it, decompose the solid into its actual facet cones. A uniform point in the i-th cone can be written tY, where Y is uniform in F_i, t is independent with density d*t^(d-1) on [0,1], and E[t^2]=d/(d+2). Hence
Sigma_P=d/(d+2) sum_i w_i(c_i c_i^T+Sigma_i).
Using C=QG+Z and Q^T D Z=0 gives
C^T D C=G B G+Z^T D Z=G/d+T,
which proves (1).

Moreover S is positive definite, not just semidefinite. If a nonzero vector a had a^T S a=0, then a dot x would be constant on every actual facet. Since each facet has full relative dimension d-1, a would be parallel to every facet normal. A bounded full-dimensional polytope in dimension d>=2 cannot have all facet normals parallel. Therefore
(d+2)Sigma_P-G=d(T+S) is positive definite.              (2)
The restriction d>=2 matters: intervals in dimension one have zero facet covariance and equality instead.

## Exact obliquity energy
The parent's weighted oblique operator is K=d Z Q^T D. Its nonzero squared singular values in the D inner product have sum
E_obl=tr(D^(-1)K^T D K)=d^2 tr(BT)=d tr(G^(-1)T).
Consequently (1) gives the exact affine-invariant budget
E_obl=(d+2)tr(G^(-1)Sigma_P)-d-d tr(G^(-1)S).             (3)
No inequality treating the last term as zero is an equality unless the physical within-facet variances vanish, which they do not in d>=2. In particular the geometric residual cannot be silently deleted from this identity.

One valid symmetric object is the actual joint Gram matrix
Gamma=[Q C]^T D [Q C]
     =[[B,I/d],[I/d,G/d+T]].                             (4)
It is positive semidefinite, has rank d+rank Z, and its Schur complement with respect to B is exactly T. Thus symmetric reasoning can retain the mixed pole/centroid coupling through a larger block instead of falsely identifying C with QG. This is a reformulation and potential route for a physical certificate, not by itself a target-class exclusion.

## Exact executed countercontrol and recovery
For the parent's five-vertex pyramid, the complete executable below verifies (1)-(4) using exact tetrahedral solid integration and exact triangular facet integration. It reports
(d+2)tr(G^(-1)Sigma_P)=85421/11339,
d tr(G^(-1)S)=149980/34017,
E_obl=184/1479,
rank Gamma=4.
The three quantities obey 85421/11339-3-149980/34017=184/1479. Actual solid and facet covariances are emitted in the deterministic JSON output. This example is not proper110; no new complexity exclusion follows.

Reconstruct the parent executable from [internal-source-reference] as physical_slack_obliquity_v1.py, exactly 7809 bytes, SHA256 e543dc7cf55208bba16982e2ccad4bcb190eee8825b5e9903c4a1da21da4d6f0. Save the sole Python code block below, including its final LF, as physical_slack_variance_v1.py, exactly 3918 bytes, SHA256 14e83ac6b9421bd77e8aa42a0154ae01c8acfd86bcc8188b7bce429f4e2f474f. Use CPython>=3.10, sympy==1.14.0, assertions enabled. Run both files from the same directory with `python physical_slack_variance_v1.py`. It reconstructs the parent's output as well and writes physical_slack_variance_v1.json, 1231 bytes, SHA256 0e608d9f559f8c591fb4ba7aa7dc32256e3c2bb285d896b64f0ca09d8d36a04a. Expected terminal marker ALL_PHYSICAL_VARIANCE_CHECKS_PASS; intermediate markers ACTUAL_SOLID_AND_FACET_MOMENT_DECOMPOSITION_PASS, STRICT_COVARIANCE_GAP_PASS, and JOINT_GRAM_RANK 4. No search seed or non-default numerical tolerance is used.

```python
#!/usr/bin/env python3
"""Exact physical second-moment decomposition extending the obliquity control.
Requires CPython >=3.10, sympy==1.14.0, and the exact adjacent dependency
physical_slack_obliquity_v1.py (SHA256 stated below). Assertions must be enabled.
Run: python physical_slack_variance_v1.py
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import sympy as s

base = Path(__file__).resolve().parent
source = base / 'physical_slack_obliquity_v1.py'
expected_source_sha = 'e543dc7cf55208bba16982e2ccad4bcb190eee8825b5e9903c4a1da21da4d6f0'
assert hashlib.sha256(source.read_bytes()).hexdigest() == expected_source_sha
spec = importlib.util.spec_from_file_location('physical_obliquity_control', source)
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)
assert s.__version__ == '1.14.0'

# Tetrahedra (0,a,b,c) partition the solid. Dirichlet(1,1,1,1)
# integration gives E[xx^T]=(ss^T+aa^T+bb^T+cc^T)/20, s=a+b+c.
solid_cov = s.zeros(3,3)
facet_covariances = []
for face in p.faces:
    triples = [(face[0],face[k],face[k+1]) for k in range(1,len(face)-1)]
    determinants = []
    face_first = s.zeros(3,1)
    face_second = s.zeros(3,3)
    for ids in triples:
        a,b,c = [p.x[j] for j in ids]
        determinant = s.det(s.Matrix.hstack(a,b,c))
        assert determinant > 0
        total = a+b+c
        numerator = total*total.T + a*a.T+b*b.T+c*c.T
        solid_cov += determinant*numerator/(120*p.volume)
        # Dirichlet(1,1,1) integration on a triangle uses divisor 12.
        determinants.append(determinant)
        face_first += determinant*total/3
        face_second += determinant*numerator/12
    area_centroid = face_first/sum(determinants)
    facet_covariances.append(s.simplify(face_second/sum(determinants)
                                       -area_centroid*area_centroid.T))

boundary_variance = sum((wi*si for wi,si in zip(p.weights,facet_covariances)),s.zeros(3,3))
residual_cov = p.Z.T*p.D*p.Z
assert p.C.T*p.D*p.C == p.G/3+residual_cov
assert s.simplify(s.Rational(5,3)*solid_cov-p.G/3-residual_cov-boundary_variance) == s.zeros(3,3)
assert all(boundary_variance[:k,:k].det() > 0 for k in (1,2,3))
strict_gap = s.simplify(5*solid_cov-p.G)
assert all(strict_gap[:k,:k].det() > 0 for k in (1,2,3))
assert p.sigma_squared == s.simplify(3*s.trace(p.G.inv()*residual_cov))
solid_energy = s.factor(5*s.trace(p.G.inv()*solid_cov))
boundary_energy = s.factor(3*s.trace(p.G.inv()*boundary_variance))
assert s.factor(solid_energy-3-boundary_energy-p.sigma_squared) == 0
# Joint first-moment Gram. Its Schur complement is exactly residual_cov.
joint_gram = (p.Q.row_join(p.C)).T*p.D*(p.Q.row_join(p.C))
assert joint_gram.rank() == 3+p.Z.rank() == 4

def matrix(a):
    return [[str(a[i,j]) for j in range(a.cols)] for i in range(a.rows)]

report = {
    'object':'PHYSICAL_FACET_CONE_VARIANCE_DECOMPOSITION_V1',
    'dependency_sha256':expected_source_sha,
    'solid_covariance':matrix(solid_cov),
    'weighted_within_facet_covariance':matrix(boundary_variance),
    'residual_covariance':matrix(residual_cov),
    'strict_gap_5_Sigma_minus_G':matrix(strict_gap),
    'normalized_solid_energy':str(solid_energy),
    'normalized_within_facet_energy':str(boundary_energy),
    'obliquity_energy':str(p.sigma_squared),
    'joint_gram_rank':joint_gram.rank(),
    'scope':'Exact actual-volume identity and countercontrol, NOT a new complexity bound.'
}
blob=(json.dumps(report,sort_keys=True,indent=2,ensure_ascii=True)+'\n').encode('utf-8')
output=base/'physical_slack_variance_v1.json'
output.write_bytes(blob)
print('ACTUAL_SOLID_AND_FACET_MOMENT_DECOMPOSITION_PASS')
print('STRICT_COVARIANCE_GAP_PASS')
print('NORMALIZED_ENERGIES',solid_energy,boundary_energy,p.sigma_squared)
print('JOINT_GRAM_RANK',joint_gram.rank())
print('OUTPUT',output.name,len(blob),hashlib.sha256(blob).hexdigest())
print('ALL_PHYSICAL_VARIANCE_CHECKS_PASS')
```

## Remaining scientific obstacle
Equations (1)-(4) apply to actual homogeneous polytopes and avoid the false polar-centroid and false diagonal-symmetry shortcuts. They do not yet turn S=U=1 or the V10/E17/F9 incidence conditions into a bound on T or into a PSD killer stress. The next useful bridge is a genuinely mechanical or incidence-dependent restriction on this joint moment system, or a continuation of the distinct H5 arbitrary-ratio certificate mechanism. Neither the exact spectrum nor these covariance identities alone close E17.
