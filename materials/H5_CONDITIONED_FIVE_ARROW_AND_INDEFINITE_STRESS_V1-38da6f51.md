# material-38da6f51cf9c

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# H5_CONDITIONED_FIVE_ARROW_AND_INDEFINITE_STRESS_V1

## Contribution and boundaries
This coordinator theorem connects the accepted common-metric five-arrow reduction with the covariance-conditioned metric cone necessary for joint S1/U1. The five-arrow bound survives this additional convex constraint. Its dual allows genuinely indefinite stresses, not only the PSD stresses of unrestricted metric infeasibility.

An exact actual-centroid H5 four-arrow packet is strictly feasible for an unrestricted SPD metric, but is impossible for every metric whose ACTUAL covariance-weighted condition number is at most 63. Thus the extension can reject packets which no unrestricted PSD-stress certificate can reject. It is not merely a new search box. The packet occurs in 255 raw labelled rooted trees at one fixed shape; this is not whole-shape coverage, a nonoverlap claim, a canonical-registry subtraction, or a global bound improvement. Whole H5 and E17 remain open; 34<=C_min<=622.

The supplied premises are the finite-height joint covariance bound and the literal actual H5 geometry. The main parent minimum-0251 was read completely, SHA256 c6740ff1f093f61efe88b3be1e4fbc19f4163ffa98e8ce686fb621ac0237d252. Its unrestricted five-arrow theorem, exact shape A and four-arrow deletion metric are used without changing identity. Companion minimum-0252 was also read completely, SHA256 c166ef43daf3b0236b4e6c5360246aaf15fec13adfb79c3a1f22541c4d49bce9. Its accepted actual covariance-weighted adjacent ratios p0=7024915/1000000 and q0=6832329/1000000 have product<48. This is a necessary JOINT S1/U1 condition, including incidental weak rests, not a constraint on arbitrary U1 metrics.

## 1. A projection theorem for any open convex physical metric cone
Let z_i=(x_i,h_i), x_i in R2, h_i in {0,1}, with a fixed interior reference g=(c,gamma), 0<gamma<1. Let D be a nonempty open convex cone of SPD 3x3 matrices. For H5 the reference is always its actual uniform volume centroid. A selected true-edge arrow e=(i,j) requires the weak exit derivative

    D_e(M)=(z_i-g)^T M(z_j-z_i)>=0.

Normalize by tr G=1, writing M=[[G,b],[b^T,m]]. Set a_i=x_i-c, k_i=h_i-gamma, delta_e=x_j-x_i and sigma_e=h_j-h_i. Then

    ell_e(G,b)=a_i^T G delta_e+(sigma_e a_i+k_i delta_e)^T b,
    D_e(M)=ell_e(G,b)+k_i sigma_e m.

For a same-layer arrow sigma_e=0, its constraint is independent of m. For every cross-layer arrow c_e=-k_i sigma_e>0, and its constraint is the UPPER bound m<=L_e(G,b), where L_e=ell_e/c_e. Both cross orientations have this same monotonicity.

Project the normalized D onto the four variables (G,b): the trace-one symmetric G has two free coordinates and b has two. For each arrow let S_e be the projection of {M in D, tr G=1, D_e(M)>=0}. Each S_e is convex, since it is a linear projection of an intersection of convex sets.

Crucially, for every finite packet J,

    intersection_{e in J} S_e
      = projection{M in D, tr G=1, D_e(M)>=0 for all e in J}.       (1)

Indeed, at fixed (G,b) the nonempty normal fibre of D is an OPEN interval I. All same-layer constraints are already fixed. If each cross constraint can separately be satisfied in I, its upper threshold L_e is strictly above inf I. The finite minimum of these thresholds remains strictly above inf I, so one m in I satisfies ALL of them. No contraction outside D is used. This is precisely the point that permits the joint cone and forbids blindly sending eta to zero.

Consequently a finite weak-arrow packet is feasible in D iff every subpacket of at most FIVE arrows is feasible in D. To justify the finite Helly step without any closure assumption: if a minimal empty family of convex subsets of R4 had at least six members, choose for each of six members a point in all the other members of the full family. The six augmented vectors (x_i,1) in R5 are linearly dependent. Separating the positive and negative coefficients gives a point in the convex hulls of two disjoint nonempty groups. For every family member one of those groups avoids its omitted point; their common point is therefore in every member, a contradiction. This argument applies to open, closed and mixed projected sets.

This is a universal upper bound of five; no claim that it is sharp for a prescribed conditioned cone is made. The unrestricted sharpness result of the parent remains intact.

## 2. The exact joint covariance-conditioned cone
Fix any SPD Sigma and K>1. Define

    D_(Sigma,K)={M>0: condition(Sigma^(1/2) M Sigma^(1/2))<K}.

This is an open convex cone. Equivalently it consists of matrices admitting tau>0 such that

    tau Sigma^-1 < M < K tau Sigma^-1.                            (2)

Convexity follows directly by adding these two strict LMIs with the same positive convex weights, including the tau variables. Scaling is harmless. Thus Section 1 applies to the full conditioned cone, not just a fixed-G slice, a fixed shear, an entry box or one value of tau. For actual proper110 H5 metrics use K=48 from the supplied finite-height premise.

Every nonroot vertex of a body with exactly one strict U has a nonnegative true-edge exit. Such an exit strictly increases squared M-norm because the edge has positive length. Selecting one exit per nonroot gives a rooted tree. Conversely, a complete rooted tree of nonnegative exits makes its root the unique global norm maximum and a strict U, while every nonroot has an escape. The conditioned five-arrow theorem therefore applies to each complete true-edge tree as a necessary joint110 test. It does not provide S1 on a surviving tree.

## 3. Complete real dual and exact rational certificate format
For each arrow put A_e=sym((z_i-g)(z_j-z_i)^T). For nonnegative weights, not all zero, put

    Q=-sum_e w_e A_e.

A sufficient rejection certificate is

    Q=P-N !=0,    P>=0, N>=0,
    tr(Sigma^-1 (P-K N))>=0.                                    (3)

All quantities may be exact rational matrices when available. If M satisfies (2), put H=Sigma^(1/2) M Sigma^(1/2), P'=Sigma^-1/2 P Sigma^-1/2 and N' similarly. Then

    tr(MQ)=tr(H(P'-N'))
           > tau tr(P'-K N')>=0,

where strictness follows because at least one of P',N' is nonzero. But selected nonnegative arrows imply tr(MQ)=-sum w_e D_e(M)<=0, a contradiction. If the trace gap in (3) is strictly positive, the same certificate also excludes the CLOSED condition bound <=K.

This is a complete real certificate system. Separation of the open cone D_(Sigma,K) from the polyhedral cone {M:A_e:M>=0} gives a nonzero member of its dual in the negative conical hull of the arrow tensors. To characterize that dual, put T=Sigma^-1/2 Q Sigma^-1/2. Its exact spectral test is

    tr T+(K-1) sum_{lambda_i(T)<0} lambda_i(T)>=0.                 (4)

Necessity follows by testing the closure matrix I+(K-1)Pi_minus. Sufficiency follows by splitting T into its positive and negative spectral parts. Transporting those parts back gives (3). Applied after the five-arrow theorem, an infeasible packet has a certificate with at most five arrow weights. Degenerate rational data need not be asserted to admit rational weights or a positive gap; the completeness statement is over the reals. The concrete control below has rational weights, PD P and N, and a strictly positive gap.

A shape-cell implementation can avoid all square roots: verify P,N PSD and the sign of tr(adj(Sigma)(P-KN)), since det Sigma>0. If Q, Sigma and a chosen N depend rationally on the actual shape, clearing their known positive moment denominators yields polynomial certificate guards. A uniform cell certificate need not inherit the fixed-shape five-row sparsity. Failure to find one is not feasibility.

## 4. A genuinely new exact four-arrow control
Use the parent's literal shape A:

    (x,r,p,q,lambda)=(13/20,3/4,4/5,1/10,3/10),
    Volume=22241/240000,
    g=(18537583/142342400,13363403/71171200,37841/88964).

The seven basal vertices, three upper vertices, nine maximal facet cycles and seventeen true edges are reconstructed independently by the complete source. Sigma is its actual uniform-volume covariance, not a vertex covariance.

Take arrows (4->3,5->7,6->5,9->4), with weights (1,2,3,2). This is exactly the old five-packet with 0->6 deleted; it is not a renamed incidence. Define Q by these weighted actual centred tensors and put

    N = [[229,-360,208],[-360,654,-439],[208,-439,330]]/100000
        + Sigma/1000,
    P = Q+N.

Both P and N are positive definite by exact positive leading minors. Q is genuinely indefinite: Q_xx=-254456167/113873920000<0 and Q_zz=2>0. The exact closed-cap63 dual gap is

    tr(Sigma^-1(P-63N))
      =99947766888859436456480715043/373725596997921228932542371620>0.

The cap48 gap is

    6934640723718068653729983230291/747451193995842457865084743240>0.

The certificate remains valid up to the exact ratio

    tr(Sigma^-1 P)/tr(Sigma^-1 N)
      =28485825331527187952344452990947/448983012662689985387801453347,

approximately 63.4452. Only the simple cap63 is promoted.

Nevertheless the parent's rational unrestricted metric

    M=[[808,65,-2],[65,190,-17],[-2,-17,2]]/1000

is SPD and makes all four selected derivatives strictly positive. Its complete actual-inverse census is (S,U,H)=(2,3,3), physical weak000, and all 68 true-edge primitives are nonzero. The source independently reconstructs the literal control because it is the input to the new comparison, not as a generic audit of its author. The exact stress pairing is

    tr(QM)=-104711199703/56936960000000<0.

Thus no nonzero PSD negative weighted stress of these four rows can certify unrestricted infeasibility, since the displayed SPD metric satisfies them. The conditioned indefinite certificate genuinely rejects something that the unrestricted PSD method cannot reject.

The packet occurs in 255 raw rooted trees, by root {0:18,1:33,2:54,3:102,7:21,8:27}, out of 48790 orientations of 4879 spanning trees. This is a literal containment count. It does not establish that all 255 are new relative to any historical atlas, and it does not exclude the whole fixed shape. By continuity the strict rational guards persist locally, but no explicit parameter-box radius or full coverage is claimed.

## 5. Exact recovery and evidence level
The entire source is immutable material [internal-source-reference], named h5_conditioned_packet.py.txt. Save its exact bytes as h5_conditioned_packet.py. It has 7819 bytes and SHA256 e4a124f9605d1af7d05e74a4c12bf5044fb9ac20b2d18b42d50bffd89484bad0. It needs only CPython3.13.5 and SymPy1.14.0. It has no input data, parent imports, solver, random seed or omitted helper.

Reconstruction and verification command, with assertions enabled:

    python -B h5_conditioned_packet.py

Expected output h5_conditioned_packet_report.json: 16233 bytes, SHA256 8bf49db203aac4274a87839494c1e3e45b216d07bf744e82c5fed588642ab7de. Expected stdout:253 bytes, SHA256844303adca8b5746045260e304c62fbd1f3669a2055e5c808ec17dd3031aee4a. Last marker H5_CONDITIONED_FIVE_ARROW_EXTENSION_V1_PASS. Other lines include CONDITION_CAP 63 TRACE_GAP_POSITIVE True; UNRESTRICTED_CONTROL (2,3,3) WEAK 0; RAW_CONTAINING_TREES 255, with Python tuple spacing as emitted by the source.

The coordinator executed the source normally and in a fresh directory containing only that source; exact JSON reports were byte-identical. The general convex/projection/dual theorem is an analytic proof, not proof-assistant formalization. Supplied finite-height bounds are accepted research premises, not independently reproved here. Numerical discovery found useful weights and a negative-part decomposition; all promoted control facts depend only on the exact source and rational guards above. The optional discovery source is preserved separately and is not a reconstruction dependency.

## 6. Next scientific question
Use this stronger cone to seek substantial common-metric rejection on the residual H5 domain, rather than demanding U>=2 for every unrestricted metric. A whole-shape or regional result requires coverage of every rooted tree under the SAME actual covariance and the supplied joint cap, with exact guards throughout its stated parameter domain. A surviving cone is not a proper110 example; it still requires actual SPD reconstruction and complete same-inverse equilibrium audit. Nonparallel realizations and other E17 incidences remain outside this literal H5 result.
