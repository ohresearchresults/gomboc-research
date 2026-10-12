# minimum-0299

AI research report · 2026-09-28 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# ADAPTIVE_OUTER_TETRAHEDRON_FULL_LEFT_TAILS_77_AND_100_AND_SEVEN_CORE_V1

## 1. New mechanical determination

The new argument excludes a substantial part of the previously unresolved early positive interval while retaining every independent left coefficient and the entire closed stack-weight triangle. It also removes the right-to-stack smallness requirement from the sufficient condition.

### Theorem A: unrestricted left coefficients, starting at a s = 77

Assume

```text
0 < beta < 1,  s > 0,
0 < p_j < s,
0 < q_j <= 1/1024,
u_j >= 0,  u_0+u_1+u_2 = 1,
Q = max(q_0,q_1,q_2).
```

For every admissible parameter

```text
a s >= 77,     a < 1 + 1/Q,
```

the actual uniformly refilled cut-stack body, at its own volume centroid, has **U >= 2 under every SPD metric**. Every complete true weak rooted tree is impossible under every nonzero PSD matrix.

There is no restriction on the three independent ratios p_j/s beyond membership in (0,1). In particular, this is not another small-left-coefficient theorem. The bound on q_j is absolute in the literal chart: the additional condition q_j <= s/1024 is not needed.

On the assignment's entire right-coefficient range `q_j <= min(1,s)/1024`, the newly excluded interval

```text
77/s <= a < 256/s
```

occupies exactly 179/256 of the previously unresolved interval `[0,256/s)`. The resulting complete tail occupies **strictly more than 947/1024 of the whole positive pencil**, approximately 92.48%. The endpoint at a s = 77 is included.

### Theorem B: twice the right allowance, starting at a s = 100

With the same beta, s, p and full closed weight triangle, replace the right hypothesis by

```text
0 < q_j <= 1/512.
```

The same conclusions hold whenever

```text
a s >= 100,     a < 1 + 1/Q.
```

Under `q_j <= min(1,s)/512`, this covers strictly more than 103/128 of the whole positive pencil. It doubles the right allowance of the parent's unrestricted-left theorem and starts substantially earlier than its a s = 256 threshold.

Theorems A and B have their literal admissibility conditions: when the absolute right bound is used without a q_j/s bound, the stated tail is not asserted to be nonempty for every s. No such qualification is needed for the stated positive-pencil fractions, where the corresponding `min(1,s)` hypothesis is imposed.

For example, there is a common full-dimensional continuous region

```text
1/4 < s < 1/2,
0 < p_j < s,
0 < q_j <= 1/512,
400 <= a < 513,
0 < beta < 1,
u_j >= 0, sum u_j = 1.
```

Every body in it is excluded. Here q_j/s can approach 1/128, eight times the assignment's relative right-side allowance, while all left ratios and both independent weights remain free. This example is a parameter region, not a claimed newly executed equilibrium control.

The mechanism is an **adaptively enclosing tetrahedron**. After its affine normalization, the actual body is inside a regular tetrahedron and contains an explicit inner tetrahedron with a contracted base and one inward-moved apex. The actual missing-volume moments give the centre bound. This is different from applying a larger homothetic-shell constant to conv(R0,R1,R2,S).

A second, independent finding is the exact seven-vertex-core enclosure in Section 8. It gives a proved shape-uniform, whole-pencil collar with an unevaluated width. That companion does not claim to close the entire remaining interval at right scale 1/1024.

## 2. Input and evidence audit

The supplied journal was read through EOF, including the complete literal parent. Its manifest identity is:

```text
research-journal.md
357316 bytes
SHA-256 c4ae383bc76885c7e5950506d94f04093b4902daf7f550806cc35c897b6ae814
```

The authoritative parent is

```text
minimum-0296
SHA-256 b183ff5f2131be1248b0965c365dd5a18a4122b5c2b4e5628457bb6338dd0fdb
```

I use its accepted four-central-section alternative with gap 7/32. Its complete finite multiplier data are reproduced in the checker below, so the explicit 77 and 100 theorems need no older numerical pencil package, numerical shape certificate or nine-vertex theorem. No parent identity or incidence conflict was found.

This is an analytical successor. I do not claim a newly observed full-hull/census execution, a reconstructed numerical survivor, or an output hash for an unobserved run. The new finite algebra, constants, maps and recovery inputs are literal in this handoff. The thirteen parent controls retain their previously accepted status; they are not relabelled as new controls for this result.

The qualitative seven-core companion invokes the accepted nonzero-PSD contained-refinement theorem recorded in the journal, identified precisely in Section 8. Its separate full source was not supplied or replayed. That dependency is not needed by Theorems A and B.

## 3. Actual chart, centre and true boundary

Use the unchanged labels

```text
0,1,2 = B0,B1,B2
3,4,5 = L0,L1,L2
6,7,8 = R0,R1,R2
9     = S.
```

The literal coordinates are

```text
B0=(0,-beta,0), B1=(0,1-beta,0), B2=(0,0,1),
d_j=1+a p_j,
e_j=1+(1-a)q_j,
d_s=1+a s,
L_j=(-p_j,(B_j)_y,(B_j)_z)/d_j,
R_j=( q_j,(B_j)_y,(B_j)_z)/e_j,
S=(-s,sum_j u_j(B_j)_y,sum_j u_j(B_j)_z)/d_s,
Delta=s-sum_j u_j p_j.
```

All denominators must be positive. For p_j<s, Delta is positive on the entire closed weight triangle and the maximal pencil is

```text
-1/s < a < 1+1/Q.
```

The actual body P_a is the convex hull of these points. Its interior-weight maximal facet cycles and genuine edges remain

```text
F0=(0,3,4,1,7,6)  F1=(0,2,5,3)  F2=(0,6,8,2)
F3=(1,4,5,2)      F4=(1,2,8,7)  F5=(3,9,4)
F6=(3,5,9)        F7=(4,9,5)    F8=(6,7,8)

02,03,06,12,14,17,25,28,34,35,39,45,49,59,67,68,78.
```

Every projective member is refilled uniformly. The seven actual positive tetrahedra and their six-volumes are

```text
(0,1,2,5): p2/d2
(0,1,4,5): p1/(d1 d2)
(0,3,4,5): p0/(d0 d1 d2)
(3,4,5,9): Delta/(d_s d0 d1 d2)
(0,1,2,8): q2/e2
(0,1,7,8): q1/(e1 e2)
(0,6,7,8): q0/(e0 e1 e2).
```

Writing their weights as w_t, their vertex sums as C_t and their sums of outer products as J_t, the one physical centre and covariance are

```text
D=sum_t w_t,
Vol(P_a)=D/6,
g_a=sum_t w_t C_t/(4D),
E[XX^T]=sum_t w_t(C_t C_t^T+J_t)/(20D),
Sigma_a=E[XX^T]-g_a g_a^T.
```

No old centroid or vertex average replaces these moments. An affine normalization in the proof transports this actual uniform measure because its Jacobian is constant; changing a does not transport the measure.

The true weight-boundary changes are unchanged:

```text
u0=0: merge F3/F7 and delete L1--L2;
u1=0: merge F1/F6 and delete L0--L2;
u2=0: merge F0/F5 and delete L0--L1.
```

Exactly one zero weight gives **10/16/8**, with the first two mergers pentagonal and the third heptagonal. At u_j=1, two mergers occur and L_j is strictly between B_j and S; deleting that redundant label gives **9/14/7**. All claimed mechanical arguments apply to the resulting true vertices and edges. No nine-vertex shortcut is applied to a weight edge.

## 4. A new trimmed-tetrahedron theorem

Let

```text
z0=(1,1,1), z1=(1,-1,-1),
z2=(-1,1,-1), z3=(-1,-1,1),
T=conv(z0,z1,z2,z3).
```

Choose any one corner as apex A; the other three form the base. Let O and W be arbitrary points of the closed base triangle. For parameters 0<=b<=d<1/4, define the inner tetrahedron T_in by replacing its base corners B_i and apex by

```text
B_i'=(1-b)B_i+b O,
A'=(1-d)A+d W.
```

Let K be any actual uniformly filled convex polytope satisfying

```text
T_in subset K subset T.
```

Put

```text
v=(1-b)^2(1-d),
C(b,d)=sqrt((d+2b)(d+6b))/v,
G(b,d)=7/32-9d-(51/10)C(b,d).
```

**Trimmed-tetrahedron theorem.** If G(b,d)>0, then K at its actual uniform centroid has U>=2 under every SPD metric, and no complete weak rooted tree under any nonzero PSD metric. There is no vertex-count bound for these qualitative conclusions.

For at most ten true vertices, any gamma>0 with 18 gamma<G(b,d) gives a selected-arrow margin

```text
some D_ij < -gamma tr(M)
```

in this enclosing-tetrahedron normalization, for every rooted tree and every nonzero PSD M.

### 4.1 Exact actual-centroid estimate

The regular tetrahedron has centroid zero, covariance I/5, volume denoted V_T, and |x|^2<=3 throughout T. Its inner tetrahedron has volume v V_T.

First replace only the apex, obtaining

```text
T_1=conv(B0,B1,B2,A').
```

Write w=|W|^2. Since A.W=-1, the exact simplex second-moment formula gives

```text
(1/V_T) integral_(T minus T_1) |x|^2 dx
 = d-(9+w)d^2/10+(5+w)d^3/10
 <= d.
```

The inequality follows directly from

```text
d-[the displayed expression]
 = d^2[4+(5+w)(1-d)]/10 >= 0.
```

Contracting the base next removes volume

```text
(1-d)(2b-b^2)V_T <= 2b V_T.
```

Its second moment is at most 6b V_T. Consequently,

```text
Vol(T minus T_in) <= (d+2b)V_T,
integral_(T minus T_in) |x|^2 dx <= (d+6b)V_T.
```

Let g be the actual uniform centroid of K. Because the integral of x over T vanishes,

```text
g = - integral_(T minus K) x dx / Vol(K).
```

Cauchy-Schwarz, the two preceding bounds and Vol(K)>=v V_T give

```text
|g| <= C(b,d).
```

This estimate uses actual missing volume and its actual first and second moments. It is not an independently chosen mixture or a frozen tetrahedral centre.

The actual covariance also satisfies

```text
Sigma_K <= E_K[XX^T] <= I/(5v).
```

### 4.2 The inherited complete four-section alternative

Normalize a nonzero PSD M by tr(M)=1. Permute the corners by an orthogonal symmetry so that

```text
n0>=n1>=n2>=n3,   n_i=z_i^T M z_i,   sum n_i=4.
```

The four alternatives are

```text
A: plane x1=0, section vertices +/-e2,+/-e3,
   opposite witnesses z0,z2, m_A=n2;
B: plane x2=0, section vertices +/-e1,+/-e3,
   opposite witnesses z0,z1, m_B=n1;
C: plane x3=0, section vertices +/-e1,+/-e2,
   opposite witnesses z0,z1, m_C=n1;
D: plane z0.x=0, section vertices (z0+3z_j)/4, j=1,2,3,
   opposite witnesses z0,z1, m_D=n1.
```

At least one satisfies

```text
m_H-max_(y in T intersect H) y^T M y > 7/32.
```

This is exactly the parent's 7/32 lemma, including nonzero singular matrices and all norm-order ties. Its finite 24-case certificate is reproduced below. No stronger 1/4 assertion is being made.

### 4.3 Moving the witnesses, not enlarging the section

Each chosen corner has a corresponding point of T_in moved a fraction at most d towards a convex combination of other corners. For distinct regular corners z_i,z_j, the symmetric matrix

```text
z_i(z_j-z_i)^T+(z_j-z_i)z_i^T
```

has least eigenvalue `-4-sqrt(24)>-9`. It follows that every such moved witness z_i' obeys

```text
(z_i')^T M z_i' >= n_i-9d.
```

The nonnegative quadratic term in the displacement is retained in deriving this lower bound.

The moved witnesses remain in opposite open halfspaces of H. Indeed, for the two-against-two cuts the original corner values are +/-1; for the fourth cut they are 3 and -1. Moving a fraction less than 1/4 towards T cannot cross the relevant plane.

Every point y of any one of these four sections has squared distance at most 13/2 from every point of T. To check this it suffices, by convexity, to use a tetrahedral corner and a displayed section vertex. Hence

```text
2|z_i'-y| <= sqrt(26) < 51/10.
```

For the actual squared distance f(x)=(x-g)^T M(x-g), the common g^T M g cancels. The selected section therefore satisfies

```text
f(z_i')-f(y)
 > 7/32-9d-(51/10)|g|
 >= G(b,d)>0
```

for both opposite witnesses and every y in K intersect H.

Unlike the previous shell argument, the section is not enlarged: K is inside the enclosing regular tetrahedron. Only the contained witnesses and the actual centroid are moved.

### 4.4 Every true root and every weak alternative

Maximize f over K clipped by each closed halfspace of H. The two witnesses lie strictly above the entire section, so each half has a maximizer at a true vertex of K off H; a new clipping vertex on H cannot maximize.

For SPD M, a neighbor in the same half has no larger f, and

```text
2D_ij=f(v_j)-f(v_i)-|v_j-v_i|_M^2<0.
```

An edge leaving the half first crosses the strictly lower section, which also makes its initial primitive negative. Thus the two half-maximizers are two strict unstable equilibria.

For PSD M, a weak arrow D_ij>=0 makes f nondecreasing along the entire edge segment. A complete root path from a half-maximizer cannot cross the lower section. One root cannot belong to both open halves. This excludes every complete weak rooted tree, including all zero primitives and projection coincidences.

For the quantitative version, if all selected arrows were at least -gamma after tr(M)=1, the energy drop on a whole edge or a traversed fraction would be at most 2 gamma. A simple root path on at most ten vertices has at most nine edges. The inequality 18 gamma<G again forbids the first section crossing.

By separation, each fixed actual tree then has nonnegative weights summing to one with

```text
Q_tree=-sum_e w_e sym[(v_i-g)(v_j-v_i)^T] > gamma I.
```

These weights may depend on the actual body and tree, but not on M. Their existence is proved analytically; no computed actual-tree coefficient library is claimed.

## 5. The new adaptive outer tetrahedron

Begin with the parent's contained tetrahedron

```text
T_a^R=conv(R0,R1,R2,S).
```

It remains distinct from both the older base-and-stack tetrahedron and the new enclosing tetrahedron constructed below.

Use the exact inherited barycentric data

```text
o=(1-beta,beta,0),
v_i=u_i+s o_i,
H=s+sum_i q_i v_i,
A_j=p_j(1+sum_i o_i q_i)+q_j.
```

In ordered (R0,R1,R2,S), the other coordinates are

```text
lambda_S(B_j)=d_s q_j/H,
lambda_Ri(B_j)=e_i[delta_ij-v_i q_j/H],

lambda_S(L_j)=d_s A_j/(H d_j),
lambda_Ri(L_j)=(e_i/d_j)[delta_ij+p_j o_i-v_i A_j/H].
```

The R and S rows are unit rows. They sum to one and reconstruct the literal vertices. Also

```text
6 Vol(T_a^R)=H/(d_s e0 e1 e2)>0.
```

For positive a, define

```text
alpha=(1+Q)/(1+a s),
epsilon=Q(1+Q).
```

Suppose alpha<1. Write h=lambda_S. Every actual vertex satisfies the stronger coupled inequalities

```text
h>=0,
lambda_Ri + alpha h u_i + epsilon o_i >=0,  i=0,1,2.
```

### Proof of the coupled inequalities

Put

```text
C_j=(s q_j-p_j sum_i u_i q_i)/H.
```

The left-vertex bracket is exactly

```text
delta_ij-u_i A_j/H-o_i C_j.
```

Since a>=0, d_j>=1, e_i<=1+Q, H>=s and C_j<=q_j. Therefore

```text
lambda_Ri(L_j)
 = (e_i/d_j)delta_ij-(e_i/d_s)h u_i-(e_i/d_j)C_j o_i
 >= -alpha h u_i-epsilon o_i.
```

For a base vertex,

```text
lambda_Ri(B_j)
 = e_i delta_ij-(e_i/d_s)h u_i-(e_i s q_j/H)o_i
 >= -alpha h u_i-epsilon o_i.
```

The reference R and S vertices satisfy the inequalities directly. Notice the cancellation: **no factor Q/s occurs in this enclosure, and no upper bound on p_j/s is used here**.

### Explicit outer vertices and normalization

Let

```text
U_u=sum_i u_i R_i,
U_o=sum_i o_i R_i,
r0=1+epsilon.
```

The four inequalities define the actual enclosing tetrahedron Q_a with vertices

```text
W_i=r0 R_i-epsilon U_o,  i=0,1,2,
A_out=[r0/(1-alpha)](S-alpha U_u)-epsilon U_o.
```

Their affine barycentric coordinates are

```text
mu_S=(1-alpha)h/r0,
mu_i=(lambda_Ri+alpha h u_i+epsilon o_i)/r0.
```

They sum to one and are nonnegative on P_a. Thus

```text
T_a^R subset P_a subset Q_a.
```

Normalize Q_a affinely to the regular tetrahedron, with A_out as its designated apex. In that gauge the actual R_i and S become

```text
R_i'=(1-b)z_i+b O,
S'=(1-d)z_A+d W,
```

where O,W belong to the closed base triangle and

```text
b=epsilon/(1+epsilon),
d=(alpha+epsilon)/(1+epsilon),
O=sum_i o_i z_i,
W=sum_i [(alpha u_i+epsilon o_i)/(alpha+epsilon)] z_i.
```

This is precisely the trimmed-tetrahedron setting. All weights remain the actual independent u_i; they were not optimized or coupled to the cut coefficients.

The affine normalization changes with a and with the other parameters. The body is uniformly refilled first, and its one actual centroid is then transformed. This construction transports neither a density nor an old arrow certificate between projective members.

## 6. General rational sufficient gate and exact parameter bounds

The preceding proof gives a pointwise sufficient condition wider than either convenient theorem box.

For an actual chart member with a>0, Delta>0 and positive denominators, calculate alpha, epsilon, b and d as above. If

```text
alpha<1,
0<=b<=d<1/4,
A=7/32-9d>0,
100 A^2 (1-b)^4 (1-d)^2
  > 2601 (d+2b)(d+6b),
```

then U>=2 for every SPD and every complete nonzero-PSD weak rooted system is excluded. This test is rational and uses no square roots.

It does not require p_j<s at a fixed weight: only the actual stack condition Delta>0 is needed there. The full closed weight triangle in Theorems A and B is guaranteed separately by p_j<s. A fixed-weight test must not be promoted to a whole-weight statement when some p_j>=s.

A failed gate is only failure of this sufficient bound, not a feasible rooted system or a physical survivor.

### Regime A

At Q<=1/1024 and a s>=77,

```text
b <= 1025/1049601 < 1/1000,
d <= 1129550/81868878 < 1/72.
```

For b_bar=1/1000 and d_bar=1/72,

```text
v_bar=70858071/72000000,
(d_bar+2b_bar)(d_bar+6b_bar)=25597/81000000,
C(b_bar,d_bar)<1/55.
```

The last strict inequality is the exact positive integer comparison

```text
70858071^2 - 3025*25597*64000000
 = 65287025841041 >0.
```

Consequently

```text
G > 7/32-9/72-51/550 = 9/8800.
```

This proves Theorem A. For at most ten vertices, take gamma=1/32768, since

```text
9/8800-18/32768 = 2133/4505600 >0.
```

Also v_bar>4/5, so Sigma_K<I/4. Every complete actual tree therefore has a probability-weighted stress

```text
Q_tree > I/32768 > Sigma_K/8192.
```

The covariance inequality survives undoing the affine normalization by congruence.

### Regime B

At Q<=1/512 and a s>=100,

```text
b <= 513/262657 < 1/500,
d <= 314469/26528357 < 1/84.
```

For b_bar=1/500 and d_bar=1/84,

```text
v_bar=20667083/21000000,
(d_bar+2b_bar)(d_bar+6b_bar)=41917/110250000,
C(b_bar,d_bar)<1/50.
```

The exact integer comparison is

```text
20667083^2 - 41917*10000000000
 = 7958319728889 >0.
```

Hence

```text
G > 7/32-9/84-51/500 = 269/28000.
```

This proves Theorem B. Here gamma=1/4096 is permitted because 18/4096<269/28000. Again v_bar>4/5, giving

```text
Q_tree > I/4096 > Sigma_K/1024.
```

The universal proof covers the actual weight-edge and weight-corner graphs without maintaining deleted edges or artificial integration diagonals.

## 7. What the new mechanism changes

The earlier comparison bounded each negative barycentric coordinate separately and enclosed the whole body in a homothetic shell around T_a^R. That lost both the common u_i direction and the factor h=lambda_S.

The coupled inequalities retain both. Their enclosing object is a tetrahedron with an explicitly displaced apex and a commonly expanded base. After normalization, the actual body lies inside that tetrahedron, so the four central sections themselves do not move. Only the four contained witnesses and the actual missing-volume centre contribute to the error estimate.

This accounts for the wider result without modifying the parent's 7/32 section lemma. In particular, it does not challenge the parent's exact countermetric to a fixed-four-section 1/4 claim:

```text
M=(1/800)[[410,190,190],[190,221,190],[190,190,169]].
```

That obstruction remains valid and is not used as evidence of a physical survivor.

## 8. A different exact seven-vertex core, and a uniform whole-pencil companion

There is an exact geometric reduction that is independent of the outer-tetrahedron tail argument.

Define

```text
C_a=conv(L0,L1,L2,R0,R1,R2,S),
h_j=p_j q_j/(p_j+q_j),
h=max_j h_j.
```

The core has at most seven true vertices and is full dimensional because it contains T_a^R.

For each j the intersection of the chord [L_j,R_j] with x=0 is

```text
B_j'=[q_j d_j L_j+p_j e_j R_j]/[p_j e_j+q_j d_j]
    = B_j/(1+h_j).
```

The key cancellation is exact:

```text
p_j e_j+q_j d_j=p_j+q_j+p_j q_j.
```

Thus the coefficients are positive throughout the entire admissible pencil. The raw origin O lies on [B0',B1'], so O belongs to C_a. Consequently,

```text
C_a subset P_a subset O+(1+h)(C_a-O).
```

The harmonic width h is independent of a. This is not a limiting statement about q_j tending to zero, and it does not replace the actual centroid of P_a by the centroid of the seven-vertex core.

### A proved uniformity statement, with an unevaluated width

For this companion use the accepted background theorem

```text
NINE_VERTEX_NONZERO_PSD_REFINEMENT_COLLAR_V1
[internal-source-reference]
SHA-256 3052074db1f19530ac423145576607e4c86366b7e45a96cf9f17f880f0aee65b.
```

Its relevant statement is that a full-dimensional uniformly centred body with at most nine true vertices admits no nonzero-PSD complete weak rooted system even after adding arbitrary finite contained refinement labels. This is an accepted journal premise, not a source replay in this result.

Define Gamma_7,10 by the following exact compact minimization. Take

```text
c0=0, c1=e1, c2=e2, c3=e3,
c4,c5,c6 in [-1,1]^3,
C=conv(c0,...,c6),
z_i=c_i for i=0,...,6,
z7,z8,z9 in C,
M PSD, tr M=1,
T_root any rooted tree on the ten labels.
```

Use the actual uniform centroid g_C, and minimize

```text
max_(i->j in T_root) [-(z_i-g_C)^T M(z_j-z_i)]
```

over all these choices. The domain is compact, Vol(C)>=1/6, and its actual centroid is continuous. The accepted contained-refinement theorem makes the displayed maximum strictly positive at every point. Therefore

```text
Gamma_7,10 >0.
```

This is a fixed, precisely defined mathematical constant; no numerical value is asserted here.

Set

```text
epsilon_7=min(1,Gamma_7,10/384).
```

Then every actual cut-stack body with

```text
max_j p_j q_j/(p_j+q_j) <= epsilon_7
```

is excluded over its **entire maximal pencil**, subject to its actual positive-denominator and stack conditions. In particular, with s>max p_j the conclusion retains the entire closed weight triangle.

Here is the quantitative stability argument, rather than an assumed collar. Normalize a maximum-volume tetrahedron of C_a to the standard tetrahedron. Every core point then belongs to [-1,1]^3 and the core volume is at least 1/6. Write C and P for the normalized bodies and retain the normalized O in C. Since

```text
C subset P subset O+(1+h)(C-O),   h<=1,
```

their actual centroids obey

```text
|g_P-g_C| <= 12 sqrt(3) h.
```

This follows from the actual exterior-volume fraction, at most `1-(1+h)^(-3)<=3h`, and diameter at most 4 sqrt(3).

Keep the seven core labels fixed. Move each of the other labels from y to `O+(y-O)/(1+h)`, which lies in C. Each matched displacement is at most 2 sqrt(3)h; every centred displacement is at most 14 sqrt(3)h. For tr M=1, each corresponding arrow changes by at most

```text
(14 sqrt(3)h)(4 sqrt(3))+(2 sqrt(3))(4 sqrt(3)h)
 =192h.
```

The reference refined-core tree has an arrow at most -Gamma_7,10. Its actual arrow is therefore at most -Gamma_7,10/2. A true tree on fewer than ten labels can be padded by directing each redundant contained label to a true vertex with a nonnegative arrow; convexity guarantees such a vertex. This does not retain a deleted mechanical edge.

The width is uniform over the core geometry, stack weights and projective parameter. What remains unevaluated is its magnitude. In particular, this companion **does not assert epsilon_7>=1/1024**, and it cannot be used to declare the entire early target interval solved.

The domain is nevertheless structurally different from an all-right-small condition. Each pair can use its own small side, since h_j<=min(p_j,q_j). It permits arbitrarily large max p_j and max q_j on different pairs. Also, for s<epsilon_7 and arbitrary p_j/s in (0,1), all positive right coefficients are permitted. These are whole-pencil statements with an unevaluated universal width, not executed numerical coverage at a specified right scale.

## 9. Complete finite recovery data and supplementary exact checker

No newly computed numerical hull or coefficient file is required by the explicit theorems. The following complete standard-library source reproduces the inherited 24 positive-definite section alternatives and every new rational guard used above. Its inputs are literal; it needs no parent import, encoded patch, numerical optimizer, seed, cache or connector.

Use Python 3 with Fraction arithmetic and assertions enabled. For consistency with the parent environment, CPython 3.13.5 is suitable. Save as `adaptive_outer_tet.py` and run

```text
python -B -S adaptive_outer_tet.py
```

The expected terminal markers are

```text
FOUR_SECTION_24_EXACT_PD_ALTERNATIVES_PASS
ADAPTIVE_OUTER_TETRAHEDRON_77_100_RATIONAL_GUARDS_PASS
```

These are reconstruction instructions, not a claim of a newly observed execution or of a new output hash. The continuous geometric proof is given above rather than inferred from these finite checks.

```python
from fractions import Fraction as F
from itertools import product

Z=[(F(1),F(1),F(1)),(F(1),F(-1),F(-1)),
   (F(-1),F(1),F(-1)),(F(-1),F(-1),F(1))]
I=[[F(i==j) for j in range(3)] for i in range(3)]

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

def outer(x,y):
    return [[a*b for b in y] for a in x]

def add(A,B):
    return [[A[i][j]+B[i][j] for j in range(3)] for i in range(3)]

def scale(c,A):
    return [[c*x for x in row] for row in A]

def subtract(A,B):
    return add(A,scale(-1,B))

def minors(A):
    a,b,c=A[0]
    d,e=A[1][1:]
    f=A[2][2]
    return (a,a*d-b*b,a*d*f+2*b*c*e-a*e*e-d*c*c-f*b*b)

P=[outer(z,z) for z in Z]
E=[[[F(i==j==k) for j in range(3)] for i in range(3)]
   for k in range(3)]

def row(A,B):
    return subtract(scale(32,subtract(A,B)),scale(7,I))

Wsec=[tuple((Z[0][k]+3*Z[j][k])/4 for k in range(3))
      for j in (1,2,3)]
C=[[row(P[2],E[k]) for k in (1,2)],
   [row(P[1],E[k]) for k in (0,2)],
   [row(P[1],E[k]) for k in (0,1)],
   [row(P[1],outer(w,w)) for w in Wsec]]
O=[scale(32,subtract(P[j+1],P[j])) for j in range(3)]

# Complete exact parent multiplier data, compressed only by repeated rows.
V=[(15,0,0,45,0,22,18),
   (0,13,0,38,0,34,15),
   (14,0,0,42,0,23,21),
   (0,5,8,39,0,34,14),
   (0,132,0,395,0,341,132),
   (151,0,0,452,0,226,171),
   (152,0,0,455,0,241,152),
   (0,123,0,368,0,326,184),
   (0,5,7,37,0,32,19),
   (0,0,123,368,0,326,184)]
INDEX=(0,1,2,0,1,2,0,3,2,0,4,2,
       5,6,7,5,6,8,5,6,9,5,6,9)
choices=list(product(range(2),range(2),range(2),range(3)))
assert len(choices)==len(INDEX)==24
for choice,k in zip(choices,INDEX):
    rows=[C[j][choice[j]] for j in range(4)]+O
    Q=[[F(0) for j in range(3)] for i in range(3)]
    for weight,A in zip(V[k],rows):
        assert weight>=0
        Q=add(Q,scale(weight,A))
    assert min(minors(Q))>0

# Exact Euclidean constants used for moved witnesses and section distances.
assert 24<25                       # 4+sqrt(24)<9
assert F(26)<F(51,10)**2            # sqrt(26)<51/10
for S in ([tuple(F(i==k) for i in range(3)) for k in (1,2)],
          [tuple(F(i==k) for i in range(3)) for k in (0,2)],
          [tuple(F(i==k) for i in range(3)) for k in (0,1)]):
    for y in S:
        for sign in (-1,1):
            yy=tuple(sign*x for x in y)
            for z in Z:
                assert dot(tuple(z[i]-yy[i] for i in range(3)),
                           tuple(z[i]-yy[i] for i in range(3)))<=F(13,2)
for y in Wsec:
    for z in Z:
        e=tuple(z[i]-y[i] for i in range(3))
        assert dot(e,e)<=F(13,2)
print('FOUR_SECTION_24_EXACT_PD_ALTERNATIVES_PASS')

def gate_parameters(Q,t):
    alpha=(1+Q)/(1+t)
    epsilon=Q*(1+Q)
    b=epsilon/(1+epsilon)
    d=(alpha+epsilon)/(1+epsilon)
    return alpha,b,d

REGIMES=[
    ('RIGHT_1024_TAIL_77',F(1,1024),F(77),
     F(1,1000),F(1,72),F(1,55),F(9,8800),F(1,32768)),
    ('RIGHT_512_TAIL_100',F(1,512),F(100),
     F(1,500),F(1,84),F(1,50),F(269,28000),F(1,4096))]

for name,Q,t,bmax,dmax,gmax,expected_gap,gamma in REGIMES:
    alpha,b,d=gate_parameters(Q,t)
    assert alpha<1 and 0<b< bmax<dmax<F(1,4)
    assert b<d<dmax
    volume=(1-bmax)**2*(1-dmax)
    product_bound=(dmax+2*bmax)*(dmax+6*bmax)
    assert product_bound < (volume*gmax)**2
    assert volume>F(4,5)
    gap=F(7,32)-9*dmax-F(51,10)*gmax
    assert gap==expected_gap and gap>18*gamma
    A=F(7,32)-9*d
    assert A>0
    assert 100*A*A*(1-b)**4*(1-d)**2 > 2601*(d+2*b)*(d+6*b)
    print(name,'b_bound',b,'d_bound',d,'gap',gap,'gamma',gamma)

assert 70858071**2-3025*25597*64000000==65287025841041
assert 20667083**2-41917*10000000000==7958319728889
assert F(9,8800)-18*F(1,32768)==F(2133,4505600)
assert F(1)-F(77,1024)==F(947,1024)
assert F(1)-F(100,512)==F(103,128)
assert F(256-77,256)==F(179,256)
print('ADAPTIVE_OUTER_TETRAHEDRON_77_100_RATIONAL_GUARDS_PASS')
```

## 10. Remaining obstacle and continuation

The old full 1/1024 small-lateral positive-pencil residual remains closed by the parent's full 1/512 theorem. It is not reopened here.

For the assignment's unrestricted-left range with `q_j<=min(1,s)/1024`, the unresolved early interval is now confined to **0<=a s<77**, outside portions already covered by the parent or by the new rational gate. The whole interval is not excluded in this handoff. The new right-512 theorem and the removal of the Q/s requirement supply additional independent coverage rather than a claim about all remaining shapes.

The harmonic-core identity makes precise why the small-right limit has a seven-vertex comparison. Its shape-uniform collar is proved using the accepted contained-refinement premise, but its width has not been evaluated at 1/1024. Treating that unevaluated width as an already certified numerical radius would be incorrect.

The most useful continuation is to combine the explicit seven-core enclosure with actual core moment and true-edge information to evaluate a substantial collar, particularly for the remaining 0<=a s<77 region. That route can exploit the exact three chord relations rather than another worst-case homothetic tetrahedral shell. The alternative outer-tetrahedron gate is already rational and can be used directly to remove additional parameter points without any further source reconstruction.

No genuine complete U1 or joint110 survivor was obtained. No whole cut-stack incidence, E17 type or canonical registry count is subtracted. The accepted global bracket remains **34 <= C_min <= 622**.
