# material-f4a14462a347

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# OPTIMAL_COVARIANCE_TRACE_FLOOR_MAP_AND_CAP73_V1

## Scope, exact sources and evidence
New coordinator analytic continuation of the completely read immutable result minimum-0254, SHA256 54910bbef02f3039f114fe487568a3710a65cbf08331a42511807f836c39c2d0, H5_ACTUAL_COVARIANCE_CAP48_ALLROOT_MACRO_EXCLUSION_V1. This is not an independent replay of its atlas. Its actual moving-covariance Taylor lower bounds and exhaustive 48790-tree cover are accepted author-executed premises. The complete finite-height source [internal-source-reference] was read to EOF at SHA256 e7daf31f7dddffac638b3bb0d7005af5613e4b2473b0979daff4357ebf5894db. It proves the rational strict adjacent-ratio bounds p=7024915/1000000 and q=6832329/1000000 for joint S1/U1 first-layer candidates. Do not apply these joint caps to arbitrary U1 metrics.

This continuation strengthens the metric class and quantitative margin of an already excluded actual H5 region, supplies the optimal scalar trace-floor map for the sharper finite-height spectral cone, and gives an exact new nonattaining actual control. Whole H5 and E17 remain open, 34<=C_min<=622 unchanged. The new control is not the parent's lambda=3/10 body and not a class110 example. Its complete source is a companion immutable material, not a sandbox-only construction.

## 1. General trace-floor certificate
Let Sigma>0 be the ACTUAL uniform covariance, M>0 the physical metric, H=Sigma^(1/2) M Sigma^(1/2), Q=-sum_e w_e A_e with w_e>=0 and A_e=sym((Z_i-g)(Z_j-Z_i)^T). Put t=tr(Sigma^-1 Q). For alpha>0 set

P=Q+alpha*t*Sigma,       ell=alpha/(1+3alpha).

In whitened coordinates T=Sigma^-1/2 Q Sigma^-1/2 and P0=Sigma^-1/2 P Sigma^-1/2, exact inversion gives

T=P0-ell*tr(P0) I.

Normalize tr(H)=tr(Sigma M)=1. Then

tr(MQ)=tr((H-ell I) P0).                                      (1)

Consequently if H>=ell I and P is positive definite, tr(MQ)>0: the first factor is PSD with positive trace 1-3ell, and the second is PD. More generally P>=0, P!=0 suffices whenever H>ell I. Both conclusions contradict all selected weak original arrows A_e:M>=0. No physical inverse is replaced by a certificate matrix.

If in the same physical/congruence coordinates P/W>=delta I and Sigma<=R I, W=sum w>0, then P0/W>=delta/R I. Formula (1) yields the normalized negative-arrow mean

-sum w_e D_e/W = tr(MQ)/W >= (delta/R)(1-3ell).                 (2)

The argument uses the full matrix H and all its orientations. It does not freeze G, shear, normal height, centroid or covariance.

## 2. The already accepted atlas proves CAP73, not merely CAP48
The literal parent's map uses alpha=1/144, hence ell=1/147. For any SPD H with condition(H)<=73 and tr(H)=1,

lambda_min(H)>=1/(2*73+1)=1/147.

Therefore EVERY positive packet matrix P certified by that atlas rejects all its selected weak arrows throughout the CLOSED covariance-weighted cap73. No new tree enumeration, numerical solve or source replay is needed: its same 501 closed cells, 1728 certificates, 152170 uses and true moving-covariance bounds are sufficient.

The parent's cellwise normalized margin was 3delta/(49*97*R). Formula (2) gives 48delta/(49R), exactly 1552 times that bound. Since its exact global lower guard is 2^-33, the new global guard is at least 1552*2^-33>2^-23.

Thus on the literal basal box
3/5<=x<=7/10, 7/10<=r<=4/5, 3/4<=p_shape<=17/20, 1/20<=q_shape<=3/20, p_shape+q_shape<1,
for every 0<lambda<=3/5 and EVERY M with condition(Sigma^(1/2)M Sigma^(1/2))<=73, every rooted tree has an original escape derivative <=-2^-23 after tr(Sigma M)=1 normalization. Hence U>=2 including incidental weak contacts. Together with the accepted all-metric lambda>=3/5 result, the whole genuine taper is excluded at cap73 on this box and its coordinate reflection. This is a stronger conditional-U theorem on the SAME shape region, not a new canonical registry subtraction.

The number 73 is sharp for a universal conclusion from P=Q+t*Sigma/144>0 alone: Section 4 gives counterexamples to any larger cap. Those sharpness examples are matrices, not asserted actual polyhedra.

## 3. Optimal scalar map for the actual finite-height bounds
Set

p=7024915/1000000, q=6832329/1000000,
D=pq+q+1, l=1/D, u=pq/D, alpha_star=1/(D-3).

If h1>=h2>=h3>0, h1/h2<=p, h2/h3<=q and sum h_i=1, then h3>=l and h1<=u. The same inequalities are strict when both ratio bounds are strict. Thus

P_star=Q+[tr(Sigma^-1 Q)/(pq+q-2)] Sigma >=0, P_star!=0          (3)

rejects the weak packet under the strict finite-height bounds. PD suffices on their closed boundary, and its robust normalized guard is delta*(D-3)/(R*D).

The old alpha=1/144 and the optimal condition48-only alpha=1/94 are both smaller than alpha_star. Whenever an old packet P_old is PD its t is positive; hence P_star=P_old+(alpha_star-alpha_old)t Sigma is PD too. This is a mathematical monotonicity of exact packet matrices. A newly constructed interval enclosure may still be too conservative; a failed enclosure is not a loss of the exact old certificate or a physical survivor.

For a general dimension n and a known normalized eigenvalue floor l in (0,1/n), the corresponding optimal scalar coefficient is alpha=l/(1-nl). In dimension three, a mere condition cap K gives floor 1/(2K+1), hence alpha=1/[2(K-1)]. The parent's 1/(3K) choice was a sufficient split certificate, not this sharp scalar boundary.

## 4. Optimality, including strict matrix boundaries
Consider only universal tests of the form P=T+alpha tr(T) I>=0 (or >0). Their inverse is T=P-ell tr(P)I. If alpha>alpha_star, then ell>l. Take H=diag(l,q/D,pq/D) and P=diag(1,epsilon,epsilon). For sufficiently small rational epsilon>0,

tr(HT)=l-ell+epsilon[(1-l)-2ell]<0,

while P>0. Thus such a test would falsely exclude an admissible closed ratio-capped metric. Because the pairing is strictly negative, contracting H slightly toward I/3 retains the contradiction while putting both adjacent ratios strictly inside their bounds. The code gives three exact positive-definite examples. These are algebraic optimality controls, not actual arrow packets or realizable S1U1 bodies.

The same proof with floor 1/(2K+1) makes the condition-only coefficient sharp. In particular alpha=1/144 cannot universally certify beyond K=73, whereas it certifies K=73 itself with PD P.

## 5. Exact one-sided spectral hull and a richer linear dual
This section concerns ONE physical metric, not the joint reciprocal-pair hull. The convex hull of orthogonal orbits of trace-one H with adjacent bounds <=p,<=q is exactly

K={H: tr H=1, l I<=H<=u I}, l=1/D,u=pq/D.

Proof: every such H has the two displayed extreme-eigenvalue bounds. Conversely, for sorted eigenvalues those bounds say that the vector is majorized by (pq,q,1)/D. The standard finite-dimensional doubly-stochastic decomposition proves it is a convex combination of permutations of this corner spectrum; conjugating by its eigenbasis gives a convex combination of orthogonal conjugates. The corner itself satisfies both ratio bounds, so both containments hold. One can prove the needed three-dimensional majorization assertion directly: the ordered trace-one polygon is cut out by the largest-eigenvalue and smallest-eigenvalue inequalities, and averaging permutations gives exactly those partial-sum bounds.

For sorted eigenvalues tau1<=tau2<=tau3 of T=Sigma^-1/2 Q Sigma^-1/2, its exact support minimum is

min_{H in K} tr(HT) = (pq*tau1+q*tau2+tau3)/D.                (4)

A square-root-free linear dual format is

Q=P-N+c Sigma, P,N>=0,
c+[tr(Sigma^-1 P)-pq tr(Sigma^-1 N)]/D >=0.                  (5)

A strict final scalar gives a positive uniform gap; a zero gap needs the appropriate strict-metric/nonconstant qualification. At a fixed Q equality in the exact optimum is achieved by c=tau2, P the positive spectral part of Q-cSigma and N the negative spectral part, transformed back. The two parts have rank at most one each; the proof is spectral, not a rationality promise at degenerate input.

Equivalently the dual cone is generated by the two positive-map cones
Q=P-l tr(Sigma^-1 P)Sigma + u tr(Sigma^-1 N)Sigma-N, P,N>=0,
with an optional nonnegative multiple of Sigma. The simpler test (3) uses only its first cone. The upper-map-only test is -Q+[pq/(2pq-q-1)]tr(Sigma^-1 Q)Sigma>=0. The full dual can be useful when the scalar-floor class stalls.

The conditioned five-arrow theorem already preserved in this branch applies because the strict cone l tr(Sigma M)Sigma^-1<M<u tr(Sigma M)Sigma^-1 is open and convex. Pointwise sparse certificates do not imply sparse uniform box certificates. This is not a new five-arrow theorem or a claim that the one-sided hull imposes actual reciprocity.

## 6. Exact actual control demonstrating the stronger scalar map
Use the literal H5 geometry from the parent but the NEW rational parameters

(x,r,p_shape,q_shape,lambda)=(13/20,3/4,4/5,1/10,273/1000).

This differs from the parent's lambda=3/10 body. It has actual
V=219662561/2400000000,
g=(18287876803423/140584039040000,13513141506443/70292019520000,358674161/878650244).

For the three original arrows 7->0,8->7,9->4 and fixed weights 31,24,45, the exact leading-minor signs of Q+alpha*t*Sigma are
alpha=1/144: (+,-,-);
alpha=1/94: (+,-,-);
alpha=alpha_star: (+,+,+).

Thus the stronger finite-height scalar map accepts this exact weighted packet, while both older scalar maps reject this same weighted certificate. This is not proof that all other old weights or old dual packets fail.

The rational physical metric M=[[4,17,1],[17,9993,26],[1,26,4]]/10000 makes all three selected derivatives positive. Its full actual-inverse census on the NEW body is (S,U,H)=(3,2,3), physicalweak000, all68 primitives nonzero; S=(0,3,6), U=(0,3), H=((1,2),(4,5),(8,9)). It therefore lies outside the strict finite-height spectral cone, as the certificate itself proves. The new body lies in an already excluded shape box: it illustrates methodological gain, not new whole-shape coverage or an attainer.

## 7. Recovery and execution
The complete standalone source companion is spectral_floor.py, 7694 bytes, SHA256 bdb5fe86802c7d4da89389630a04b17917aca21f890f7b65e7825e9a72388b51. It reconstructs both actual controls, original moments/covariances/supports, all68 primitives and the actual common inverse, exact map matrices/minors, sharpness examples and every rational constant. No parent import, saved output or numerical library is required.
Command: python -B -S spectral_floor.py
CPython3.13.5 standard library. Expected spectral_floor_report.json 38964 bytes SHA256 5c68e2402065c530385535da7bbe74a9b3911a39faab229426fef82f376c37a9. Terminal OPTIMAL_COVARIANCE_TRACE_FLOOR_MAP_AND_CAP73_V1_PASS. Coordinator normal and source-only cold runs gave identical reports. These computations do not independently rerun the large parent atlas or formally verify the analytic proof.

The materially used optional locator is spectral_floor_locator.py, 1580 bytes SHA256 102a63fc514e4cbb84388299d6196eacebfd1e1509f6d3907c3de6829bf2ca97. It uses NumPy2.3.5, deterministic lambda grid i/1000, i=1..599, and the fixed three weights. Command OPENBLAS_NUM_THREADS=1 python -B spectral_floor_locator.py. Expected proposal431 bytes SHA256 e46f3da93f713bcbda2550805e36a15fd8780def67e925ab42284608a00258ab. Its floating proposal is not the acceptance test; exact acceptance is in the main source.

## Next research question
Use the stronger floor map or the exact one-sided-window dual to expand complete-tree coverage in residual actual H5 shape space. Do not spend another copy on replaying these accepted parents. A conservative certificate failure is not a full-tree witness. The independent paired-end reflection result minimum-0253 closes the full-basal small taper through1/300, not merely1/400000. The substantial unresolved taper is1/300<lambda<3/5 outside its larger regional boxes and the other complete-tree regions. No exact minimum follows yet.
