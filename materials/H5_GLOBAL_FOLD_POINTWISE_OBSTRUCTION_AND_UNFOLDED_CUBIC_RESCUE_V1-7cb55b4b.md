# material-7cb55b4bddd4

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# H5_GLOBAL_FOLD_POINTWISE_OBSTRUCTION_AND_UNFOLDED_CUBIC_RESCUE_V1

## Scientific status and exact source

New coordinator result, actually executed in normal and clean source-only cold runs. It strengthens the completely read immutable parent minimum-0242, SHA256 2a595fe188fb14834839829730d1b03c7b31f836418523faf1a3552e5db63ba1. That parent found a macroscopic degree-two Bernstein-coefficient obstruction but deliberately left degree elevation open and reported its new checker as unexecuted. No independent execution of that parent is claimed here.

The new theorem separates two effects on the SAME complete rooted tree and actual H5 carrier section. The global quadratic LOWERED matrix has no positive common stress even at three genuine interior parameter points, hence no degree elevation or more accurate positivity test can certify that same fixed lowering with one stress over the whole triangle. In contrast, the original UNFOLDED cubic has a single explicit constant stress whose ten degree-three triangle Bernstein matrices are uniformly positive definite over the ENTIRE triangle.

This is a limitation and repair of a certificate mechanism, not a physical feasible tree and not an enlargement of the accepted all-root domain. The fixed section r=1/3 was already excluded by the accepted all-root theorem. Bounds remain 34<=C_min<=622. There is no new weakS1U1 body, complete E17 exclusion or attaining construction.

Complete independent recovery code: [internal-source-reference], h5_global_fold_loss.py.txt, 8350 bytes, SHA256 54cef57d721ee9167377de3fcaca380d67ec75cd5cf44f0df6f31f59fd2e7ccf. The source embeds every coordinate rule, actual fan, moment polynomial, directed edge, rational test vector and stress weight. No parent file or originating sandbox is needed for reconstruction. The parent is the intellectual predecessor, not a hidden computational dependency.

## 1. Actual uniformly filled geometry

Fix x=63/64, r=1/3, lambda=1/256 and s=1-lambda. Let Delta be the closed triangle p>=0,q>=0,p+q<=1. Basal vertices are

B0=(1/4,0), B1=(1-3x/4,0), B2=(1-p,p), B3=(q,1-q),
B4=(0,1-3r/4), B5=(0,1/4), B6=(1/16,1/16).

The ten labelled vertices are z_i=(s B_i,0), i=0,...,6, and z7=(0,0,1),z8=(lambda,0,1),z9=(0,lambda,1). True outward facets, in the parent's exact labels, are

(6,5,4,3,2,1,0), (8,7,0,1), (7,6,0), (1,2,8),
(9,8,2,3), (9,3,4), (4,5,7,9), (6,7,5), (7,8,9).

Every interior point of Delta is a genuine 10/17/9 body. Boundary labels have the parent's genuine lower-vertex limiting meanings; no boundary point is claimed to be a ten-vertex body.

Write
A=(31-24xp-24rq)/64,
Bx=509/3072-3xp/8+3x^2p/32+xp^2/8-rq^2/8,
By=509/3072-3rq/8+3r^2q/32+rq^2/8-xp^2/8.

The actual volume and unnormalised first moment are

V=A s^2/3+lambda/6,
Jx=s^3 Bx/4+s^2 lambda(1-3xp/4)/24+lambda^2/24,
Jy=s^3 By/4+s^2 lambda(1-3rq/4)/24+lambda^2/24,
Jz=A s^2/12+lambda/12+lambda^2/24.

The executable verifies these as polynomial identities against the actual eight-tetrahedron apex-0 fan. The actual centroid is g=J/V, never a basal, frozen or transported centroid. Throughout Delta, 0<V<=1/6.

Use the complete true-edge tree rooted at 2, in this order:

T56=(0->1,1->2,3->2,4->3,5->6,6->0,7->0,8->2,9->3).

For any nonnegative weights w_e supported on this tree, define
G=-sum_e w_e sym[(Vz_i-J)(z_j-z_i)^T].
Then sum_e w_e D_e(M)=-tr(MG)/V, where D_e(M)=(z_i-g)^T M(z_j-z_i).

## 2. The global quadratic lowering and its pointwise obstruction

Put f=(-1,1,0), b=w32, Ia=w12+w82 and Ib=w43+w93. On this particular tree Oa=Ob=w23=0. The four cubic coefficients of G are

A=x(Ia+b), D=r(Ib+3b),
E=x(5b-Ib), F=r(3b-Ia)+4xb.

Thus the full degree-three part is
-s^4/32 [A p^3+E p^2q+F pq^2+D q^3] ff^T.

The parent's strongest aggregate global envelope is
L=x Lx+r Lr,
Lx=max(5b-Ib,4b), Lr=max(0,3b-Ia).

It replaces the cubic by -s^4/32 [A p^2+D q^2+Lpq] ff^T, giving G_low<=G in the PSD order. Equivalently,
G_low=sum_e w_e H_e+Lx Hx+Lr Hr,
where H_e is the original unit-arrow matrix with its cubic removed and -s^4(A_e p^2+D_e q^2)ff^T/32 inserted, and
Hx=-s^4 x p q ff^T/32, Hr=-s^4 r p q ff^T/32.
All 136 cubic identities on all 34 directed true edges are checked exactly by the new executable.

Let epsilon=1/65536 and choose THREE strictly interior points
P0=(1/2,epsilon), P1=(1/2-epsilon,1/2-epsilon), P2=(1-2epsilon,epsilon).
The executable verifies every true facet incidence, every strictly inward nonincidence and positive fan volume on all three bodies, and recomputes each actual centroid.

Define five PSD rank-one tests a_k v_k v_k^T. In the following table a is the displayed integer divided by 10^9; v is the displayed integer triple divided by 10^6:

point | a numerator | v numerator
P0 | 39366201 | (-512838,840056,176924)
P1 | 46942882 | (845464,-528447,-77035)
P0 | 53699272 | (-513477,839727,176637)
P1 | 178511241 | (845954,-527715,-76671)
P2 | 681480403 | (804746,563857,185606)

All five a are strictly positive and all five v are nonzero. Let c_e=sum_k a_k v_k^T H_e(P_k)v_k, Cx=-sum_k a_k v_k^T Hx(P_k)v_k, and Cr analogously. The exact calculation gives Cx>0, Cr>0 and r Cx=x Cr. Define

lo=max(0,(c32-4Cx)/3),
hi=min(Cr,-c12,-c82), mu=(lo+hi)/2.

Exactly lo<hi and 0<mu<Cr. Since Lx>=4b, Lr>=0 and Lr>=3b-Ia,

sum_k a_k v_k^T G_low(P_k)v_k
=sum_e c_e w_e-Cx Lx-Cr Lr
<=sum_e K_e w_e,

where K32=c32-4Cx-3mu, K12=c12+mu, K82=c82+mu, and the other K_e equal c_e. Every one of the NINE exact rational coefficients satisfies K_e<-1/10^6. More precisely

-min_e(-K_e)=max_e K_e
=-418293000409778886366007276395593589401/
 290142196707511001929482240000000000000000000.

Consequently for every nonzero nonnegative stress, W=sum w_e>0,

sum_k a_k v_k^T G_low(P_k)v_k < -W/10^6 <0.

If G_low were positive definite at all three points, the left side would be positive. Contradiction. This obstruction uses evaluations at genuine interior bodies, NOT a Bernstein coefficient functional. It therefore survives arbitrary degree elevation, exact pointwise checking, or subdividing the same globally lowered polynomial while insisting on ONE common stress across these three points. Enlarging the global envelopes cannot help. Additional PSD subtractions cannot help.

Important limit: changing the stress between triangle cells CAN evade the common-stress obstruction; a local refold also changes the polynomial and is not excluded. Subdivision only in x,r,lambda, with each cell retaining the whole physical triangle, cannot repair this at the stated fixed parameter point. No macroscopic free-r obstruction box is asserted by this new theorem.

## 3. The original cubic repairs the SAME tree on the WHOLE triangle

Take weights, in the stated order of T56,

w=(0,8324309,18456120,9753139,12482147,29902002,21082282,0,0)/10^8.

Their total W=99999999/10^8. They are nonnegative and supported on the complete tree. Zero weights merely omit unnecessary inequalities from its separating stress; they do not change the tree.

Do NOT perform the global triangle lowering. Expand the actual G in the ten degree-three triangle Bernstein basis functions
B_ij=3!/[i!j!(3-i-j)!] p^i q^j(1-p-q)^(3-i-j), i,j>=0,i+j<=3.

For a monomial p^a q^b, its coefficient is
binom(i,a)binom(j,b)/[binom(3,a+b)binom(a+b,a)].
The complete executable generates every coefficient matrix C_ij exactly and verifies all three leading minors of C_ij-(W/100000)I as strictly positive. Thirty exact positive minors certify ten SPD matrices, with no numerical eigenvalue acceptance.

Since B_ij>=0 and sum B_ij=1,
G(p,q)>(W/100000)I throughout the entire CLOSED physical triangle.

For every nonzero PSD metric M this yields
sum_e w_e D_e(M)/W < -tr(M)/(100000 V) <= -3 tr(M)/50000.

Thus the original cubic excludes this complete rooted tree uniformly with one constant stress, while its global quadratic lowering cannot have any common positive stress even on the three displayed interior points. The obstruction is genuinely introduced by the lowering; it is not merely an inability to find a common stress for the original actual geometry.

This is one-tree coverage, not 48,790-tree coverage and not a new actual carrier domain. The practical next mechanism is the unfurled degree-three 150/450-block system or genuinely local triangle refolding, not unlimited degree elevation of a fixed global quadratic envelope.

## 4. Reconstruction and observed execution

Save the exact source [internal-source-reference] as h5_global_fold_loss.py. Reconstruction and verification are the same exact standard-library command:

python -B -S h5_global_fold_loss.py output

Expected and actually observed terminal marker:
H5_GLOBAL_FOLD_POINTWISE_OBSTRUCTION_AND_UNFOLDED_CUBIC_RESCUE_PASS 136 9 10 30

Output h5_global_fold_loss.json: 19235 bytes, SHA256 ffe937cc29cab35105156753b5cd48490b168fb7a1ef5d43074ede1fc9d2215c.
The report contains all three exact bodies and actual centroids, all five tests, every negative dual coefficient, all ten unmodified coefficient matrices and every shifted leading minor. Normal and clean source-only cold runs on CPython3.13.5 reproduced this output byte-for-byte. Python>=3.11, standard library, assertions enabled is the recovery contract.

Exploratory numerical location used CPython3.13.5, NumPy2.3.5, SciPy1.17.0 and SymPy1.14.0. Those floating-point optimizers are NOT needed by the preserved deterministic reconstruction and are not the acceptance criterion. The literal rational tests and weights are the fixed exact recovery inputs. No origin-sandbox file, unobserved census value, parent execution receipt or new global complexity claim is hidden in the source.
