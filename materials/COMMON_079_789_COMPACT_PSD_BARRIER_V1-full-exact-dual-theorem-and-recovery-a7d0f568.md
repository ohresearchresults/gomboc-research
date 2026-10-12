# material-a7d0f56868ae

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# COMMON_079_789_COMPACT_PSD_BARRIER_V1

## Statement: a proved limitation of a specific certificate method
For labels0,...,9 fix root3 and parent map p=(1,2,3,3,3,4,5,6,7,8). For each i other than3 let G_i be the symmetric10-by-10 matrix with entryii=1, entriesi,p(i) andp(i),i equal-1/2, other entrieszero. Let c0=e3+e0+e7+e9 and c1=e3+e7+e8+e9. Thus the two tetrahedral vertex sums correspond to the triangles079 and789 coned to root3.

For one common vector of coefficients a in R^10 and arbitrary separate real multipliers lambda_ki, define
Q_k=(a c_k^T+c_k a^T)/2 + sum_(i!=3) lambda_ki G_i, k=0,1.
If both Q0 and Q1 are positive semidefinite, then a=0 and every lambda_ki=0. In particular there is no nonzero simultaneous positive-semidefinite certificate and no simultaneous positive-definite certificate, even if multiplier signs are unrestricted. The usual nonnegative-multiplier certificate is a special case.

This does NOT prove that a real uniform polyhedron with those facets exists, or that such a polyhedron is impossible. It rules out one algebraic ansatz: a fixed common linear combination of the ten vertices, supported only by these individual path-arrow quadratic forms, with both listed tetrahedral projections certified by positive-semidefinite matrices. Additional genuine-support constraints, negative chord inequalities, actual common-volume moment information, case distinctions and other proof methods are not excluded.

## Complete dual proof
The exact source [internal-source-reference] includes two explicit symmetric INTEGER10-by-10 matrices H0,H1. Their upper triangular rows are all literal in the source; the largest absolute entry is10000000. Exact rational LDL factorization, with every matrix entry reconstructed, proves H0 and H1 positive definite. There are20 strictly positive rational pivots.

The same exact computation verifies all18 equalities
Tr(H_k G_i)=H_k[ii]-H_k[i,p(i)]=0,
and all10 coordinates of the common-coefficient cancellation
H0 c0+H1 c1=0.
Consequently, for every a and all real multipliers,
Tr(H0 Q0)+Tr(H1 Q1)=a^T(H0 c0+H1 c1)+sum_(k,i)lambda_ki Tr(H_kG_i)=0.
If Q0,Q1 are positive semidefinite and H0,H1 positive definite, each trace is nonnegative and vanishes only when the corresponding Q is zero. This follows by conjugating Q with the invertible positive square root of H: the result is positive semidefinite, and zero trace forces all eigenvalues zero. Thus Q0=Q1=0.

It remains to prove that the coefficient map has no nonzero kernel. Subtract the two zero matrix equations: the common-coefficient term is Sym(a,e0-e8), while the difference of the multiplier terms is supported only on the true path edges and child diagonals. Nonedge entries(0,j),j=2,3,4,5,6,7,9, give a_j=0. Nonedge(8,1) gives a1=0. Nonedge(0,8) gives a8=a0. In the ORIGINAL equation Q0=0 the nonedge entry(0,3) is a0/2 because a3=0 and c0_3=1, so a0=0 and a8=0. All ten coefficients therefore vanish. The child-diagonal entryii then equals the corresponding lambda_ki, so all multipliers vanish. The source additionally constructs all110 upper-triangular equations in28 scalar unknowns and verifies their exact rational rank28, independently recording all28 pivot columns.

The proof is not based on numerical failure of an optimizer. It uses only the displayed literal integer matrices and exact identities/positive pivots. The two dual matrices are not asserted to be the same actual body or to have spatial rank3; they are dual functionals on the certificate cone, which is exactly their required scope.

## Consequence for the next research direction
The proposed single-profile program certifying all83 triangles except089 necessarily includes BOTH079 and789, so it is impossible within this ansatz. The coordinator-local83-triangle floating run was explicitly stopped after this exact theorem was established. It supplied no accepted final result; no failure or discovery is inferred from its unfinished output. Its direction ceased to be useful because of a proved method barrier, not because of elapsed time.

Profiles C and D remain valid: C leaves079 uncertified, while D leaves789 uncertified. They do not violate the theorem because neither tries to certify both triangles with one common coefficient vector. Applying whole profiles as alternatives on different bodies is valid; mixing different profiles among the tetrahedra of one body would not prove that body's centroid contradiction.

## Complete standalone recovery
Save material [internal-source-reference] exactly as common_two_barrier_compact.py. It is4505 UTF-8 bytes, SHA256ec5704534ad483fa551d1edbe4c6b48a0f60a4b5274b7c84ac86fb442e6c8d57. No external data file, numerical solver, random seed, omitted matrix row or previous sandbox is needed.

Reconstruct: python -S common_two_barrier_compact.py build
Verify: python -S common_two_barrier_compact.py check
Both commands actually passed in this continuation under CPython3.13.5, standard library only, assertions enabled. They reproduce common_two_barrier_compact.json,3323 bytes,SHA256604a643b133b7bd99f533088367a7c8b5f114f3dbb35e25fb882e4b956b90697.
Each prints the exact terminal line:
COMMON_079_789_COMPACT_PSD_BARRIER_EXACT_PASS 2 20 28 3323 604a643b133b7bd99f533088367a7c8b5f114f3dbb35e25fb882e4b956b90697

The output contains both complete symmetric matrices, all20 rational LDL pivots, all18 zero arrow traces, all10 zero cancellation coordinates, and rank28 evidence. This is a durable reusable negative theorem. It does not change the accepted universal lower bound V>=10,F>=9,C>=34 or the current K3 endpoint5702positions/4164classes, TREE58582positions/76classes. No C>=36, exact minimum or attaining110 body is claimed.
