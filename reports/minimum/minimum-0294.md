# minimum-0294

Historical AI scientific report · saved 2026-09-28 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# FULL_CUT_STACK_POSITIVE_PENCIL_SHELL_AND_LARGE_LEFT_TAIL_V1

## 1. Main findings and exact scope

There is a new all-metric mechanical exclusion of an **entire maximal projective pencil**, with the entire independent closed stack-weight triangle. A second theorem removes the small-left-coefficient restriction on a region occupying **more than the last three quarters of the positive pencil**.

Both results concern the actual uniformly refilled convex hull at its own volume centroid. They prove U ≥ 2 for every SPD metric, without assumptions about S, conditioning, selected root, or weak-contact freedom. They also exclude every complete true weak rooted tree for every nonzero PSD matrix.

Write Q = max(q0,q1,q2).

**Theorem A — whole maximal pencil.** Suppose

```text
0 < beta < 1,  s > 0,
u_j >= 0,  u_0+u_1+u_2 = 1,
0 < p_j <= s/131072,
0 < q_j <= min(1,s)/131072.
```

Then the conclusion holds for every

```text
-1/s < a < 1 + 1/Q.
```

In particular this includes the entire previously untreated positive-a sector, the regular a=1 section, and every allowed a>1. Neither true endpoint has an omitted collar. The endpoints themselves, where a denominator vanishes, are not included as ten-vertex bodies.

**Theorem B — large-left, majority positive tail.** Suppose instead

```text
0 < beta < 1,  s > 0,
u_j >= 0,  sum u_j = 1,
0 < p_j < s,
0 < q_j <= min(1,s)/262144.
```

Then the conclusion holds throughout

```text
65536/s <= a < 1 + 1/Q.
```

This interval is nonempty and has length strictly greater than three quarters of the full positive interval `(0,1+1/Q)`. The three ratios p_j/s are now independently free over `(0,1)`, not bounded by 1/1024 or by a small neighborhood of a fixed tuple.

Theorem A tightens the parent's lateral bound from 1/1024 to 1/131072; it is therefore **not** a whole-positive-pencil theorem on the parent's entire lateral region. Theorem B makes a different tradeoff: much broader left coefficients, smaller right coefficients, and a specified majority positive tail. Both parameter regions are full dimensional in the actual eleven-parameter chart, with the full weight triangle retained.

The new mechanism is not the old assignment of every point to a nearby tetrahedral corner. It is a **tetrahedral-shell theorem allowing vertices near the interiors of edges or faces**, combined with an exact monotonicity of negative barycentric coordinates under the positive projective motion.

## 2. Input audit and dependency boundary

I read the supplied journal in full through line 1561, including the complete literal parent. The attachment is 325472 bytes, SHA-256 `661a7c4c56f52d0de324460e7c47425c52ad867ce710f6d777e36b89e63c6701`.

The parent is `minimum-0291`, advertised SHA-256 `ca9358c9ea98d493542b01d93f39422425c00ef0fe0be2a4cdf9548fec180eef`. I verified that hash by reconstituting its compact UTF-8 JSON envelope `{"version":2,"result_markdown":...}` with `ensure_ascii=False` and separators `(',',':')`: 23781 bytes. The extracted Markdown alone is 22857 bytes, SHA-256 `246f143968be33cf03cc0ced0d1ca0e77a92d2d3c2e3c90234983ba0ae5413c9`. Thus there is no parent-identity conflict. The parent's stated negative-sector scope and its historical source-reading limitation remain distinct. fileciteturn0file0L1033-L1047

No older numerical pencil/beta package, archived nine-vertex certificate, moment-extremum source, or construction package was supplied or replayed. None is a dependency of the new proof. The four small corner-tree matrices used below are reproduced and independently checked here. The qualitative homogeneous-tetrahedron exclusion is older background, not a priority claim for this handoff. citeturn158680search1

## 3. Actual hull, one uniform centre, and true boundary changes

Use exactly the parent's label order

```text
0,1,2 = B0,B1,B2
3,4,5 = L0,L1,L2
6,7,8 = R0,R1,R2
9     = S.
```

The literal vertices are

```text
B0 = (0,-beta,0)
B1 = (0,1-beta,0)
B2 = (0,0,1)
d_j = 1+a p_j
e_j = 1+(1-a)q_j
d_s = 1+a s
L_j = (-p_j, (B_j)_y, (B_j)_z)/d_j
R_j = ( q_j, (B_j)_y, (B_j)_z)/e_j
S   = (-s, sum u_j(B_j)_y, sum u_j(B_j)_z)/d_s.
```

Let P_a be their convex hull. In both main theorems s>max p_j, so the stack excess `Delta=s-sum u_j p_j` is positive throughout the closed weight triangle, and the displayed maximal pencil is precisely the positive-denominator interval.

For positive weights the outward true facet cycles and genuine edges are

```text
F0=(0,3,4,1,7,6)   F1=(0,2,5,3)   F2=(0,6,8,2)
F3=(1,4,5,2)       F4=(1,2,8,7)   F5=(3,9,4)
F6=(3,5,9)         F7=(4,9,5)     F8=(6,7,8)

02,03,06,12,14,17,25,28,34,35,39,45,49,59,67,68,78.
```

These are the parent's actual cycles, not an integration triangulation. fileciteturn0file0L1157-L1179 At a=0 the left part is the prismatoid over the transverse triangle with left graph `x=-sum p_j lambda_j`. The right part is the cut cone towards `(1,0,0)`. The stack point sees only the left triangular cut, with boundary coincidences exactly when a weight vanishes. The positive map `x -> x/(1-a x_1)` establishes the same actual geometry for every admissible a. It is used for geometry, **not** for transporting a uniform probability law.

Every P_a is refilled uniformly. Its seven actual positive tetrahedra and six-volumes are

```text
(0,1,2,5) : p2/d2
(0,1,4,5) : p1/(d1 d2)
(0,3,4,5) : p0/(d0 d1 d2)
(3,4,5,9) : Delta/(d_s d0 d1 d2)
(0,1,2,8) : q2/e2
(0,1,7,8) : q1/(e1 e2)
(0,6,7,8) : q0/(e0 e1 e2).
```

If their weights are w_t, let `D=sum w_t`, `C_t=sum_{v in t} v`, and `J_t=sum_{v in t} vv^T`. The actual moments used everywhere are

```text
Vol(P_a) = D/6
g_a      = sum w_t C_t/(4D)
E[XX^T]  = sum w_t(C_t C_t^T + J_t)/(20D)
Sigma_a  = E[XX^T] - g_a g_a^T.
```

The parent supplies the same positive-cell identities; the new audit verifies the determinants and checks all moments against a separately reconstructed true-hull surface fan. fileciteturn0file0L1217-L1254

The weight-edge changes are retained literally:

```text
u0=0: merge F3/F7; delete L1--L2.
u1=0: merge F1/F6; delete L0--L2.
u2=0: merge F0/F5; delete L0--L1.
```

With exactly one zero weight, the true body is 10/16/8: the first two mergers produce a pentagon and the third a heptagon. At `u_j=1`, two such mergers occur and L_j is strictly between B_j and S. The actual counts in the present strict parameter domains are **9/14/7**: remove that redundant label and replace its two collinear incident segments by their genuine combined edge. These counts follow directly from the two mergers and the redundancy; all three corners are also checked independently by the exact hull auditor. The parent's ten-vertex facet-merging warning is respected. fileciteturn0file0L1192-L1206

The proof below is on the resulting body's true vertices and edges. It never invokes a nine-vertex theorem on a weight edge.

## 4. New general lemma: an actual tetrahedral shell excludes U1 in every metric

Let

```text
z0=(1,1,1), z1=(1,-1,-1),
z2=(-1,1,-1), z3=(-1,-1,1),
T=conv(z0,z1,z2,z3), delta0=1/8192.
```

**Shell lemma.** If an actual uniformly filled convex polytope K satisfies

```text
T subset K subset (1+delta)T,   0 <= delta <= delta0,
```

then K, at its actual volume centroid g, has U≥2 under every SPD metric. Every complete weak rooted tree on its true vertices is impossible under every nonzero PSD metric. There is no bound on the number of vertices for these two statements.

If K has at most ten true vertices, a stronger uniform statement holds. For every rooted tree and every nonzero PSD M, at least one selected arrow satisfies

```text
(v_i-g)^T M(v_j-v_i) < -(1/65536) tr(M)
```

in this regular-tetrahedron normalization.

### 4.1 Four corner trees give two separated metric traps

For any directed tree on the four corners, put

```text
Q_tree = sum_{i->j} sym[z_i(z_i-z_j)^T].
```

Up to an orthogonal permutation of the tetrahedral corners, the four possibilities are

```text
[[4,0,0],[0,4,0],[0,0,4]]
[[4,0,2],[0,4,2],[2,2,4]]
[[2,-2,1],[-2,6,1],[1,1,4]]
[[2,0,1],[0,6,-1],[1,-1,4]].
```

After subtracting `(5/8)I`, their leading principal minors are respectively

```text
(27/8,729/64,19683/512)
(27/8,729/64, 5859/512)
(11/8,217/64,  355/512)
(11/8,473/64, 9315/512).
```

Thus every corner-tree matrix is strictly greater than `(5/8)I`. These exact matrices are in the parent, and the new program independently enumerates and verifies all 64 labelled rooted corner trees. fileciteturn0file0L1425-L1464

Normalize a nonzero PSD M by `tr(M)=1`, and set

```text
D_ij = z_i^T M(z_j-z_i),  c=5/24.
```

Form the complete directed threshold graph containing `i->j` when `D_ij>=-c`. It cannot contain an in-arborescence: the sum of its three selected arrows would be at least `-3c=-5/8`, contradicting the matrix inequality. Consequently this graph has at least two disjoint sink strongly connected components I and J. For every i in a sink component I and j outside I,

```text
D_ij < -c.
```

This covers every metric and every possible rooted alternative; it is not a selection of a favorable root fan.

Let lambda_i be the affine barycentric coordinates of T and put

```text
t=c/8=5/192,  b=c^2/8=25/4608,
m_I=max_{i in I} z_i^T M z_i.
```

The section `sum_{i in I} lambda_i(y)=1-t` has vertices `(1-t)z_i+t z_j`, with i in I and j outside. On each such vertex,

```text
y^T M y
 = z_i^T M z_i + 2t D_ij + t^2 |z_j-z_i|_M^2
 < m_I - 2tc + 8t^2
 = m_I - b.
```

Here `|z_j-z_i|_M^2<=8` because `tr(M)=1`. Convexity extends the bound to the whole section.

### 4.2 The centre is the actual uniform centroid

Let q be the actual volume fraction of K outside T. Since T has centroid zero,

```text
q <= 1-(1+delta)^(-3)
|g| <= sqrt(3)(1+delta)q <= 3 sqrt(3) delta.
```

The last inequality follows from

```text
(1+delta)-(1+delta)^(-2) <= 3delta.
```

No tetrahedral surrogate mean replaces g.

Define the cap of K associated with I by

```text
sum_{i in I} lambda_i(x/(1+delta)) >= 1-t.
```

Every z_i with i in I is strictly inside this cap. The caps associated with disjoint I and J are disjoint because `1-t>1/2`.

Write `f(x)=(x-g)^T M(x-g)`. At a maximizing corner of I,

```text
f(z_i) >= m_I - 18delta.
```

On the artificial boundary of the cap, write `x=(1+delta)y` and use the preceding section bound. Since `|y|<=sqrt(3)` and `|g|<=3sqrt(3)delta`,

```text
f(x) <= m_I-b + 24delta + 48delta^2.
```

Thus each cap contains a witness separated from its entire artificial boundary by at least

```text
G(delta)=25/4608 - 42delta - 48delta^2.
G(delta0)=11237/37748736 > 1/4096.
```

Maximize f over the clipped cap. A maximizer exists at a true vertex of K: newly created clipping vertices lie on the strictly lower artificial boundary. For SPD M, this maximizing vertex has strictly negative primitive along every incident true edge. A neighbor inside the cap has no larger f and strict edge energy; an edge leaving the cap first crosses a point of strictly smaller f. Therefore each of the two disjoint caps supplies a strict U.

For nonzero PSD M, a path of weak arrows makes f nondecreasing along every complete edge segment. Starting at either cap maximum, such a path cannot cross its lower artificial boundary. A complete rooted tree would require both starting points to reach one root, impossible because the caps are disjoint. This handles all actual weak rooted alternatives, including incidental zero primitives.

### 4.3 Quantitative tree margin and covariance stress

For a tree on at most ten vertices, suppose instead that all selected primitives were at least `-gamma`, where `gamma=1/65536` and `tr(M)=1`. Along a path of k edges, endpoint energy drops by at most `2k gamma`. At a point inside the next edge it drops by at most an additional `2gamma`. A root path has at most nine edges, so its first crossing of a cap boundary would have energy at least the starting witness minus `18gamma`. But

```text
G(delta0)-18/65536 = 869/37748736 > 0.
```

Choose a cap not containing the root. The crossing is impossible, proving the asserted negative-arrow margin.

For completeness, this implies a metric-independent stress for each fixed actual tree. There are nonnegative weights w_e summing to one such that

```text
Q = -sum_e w_e sym[(v_i-g)(v_j-v_i)^T] > (1/65536)I.
```

Indeed, otherwise separation of the convex hull of these arrow matrices from `(1/65536)I+PD` supplies a nonzero PSD M making every selected forward arrow at least `-(1/65536)tr(M)`, contrary to the preceding proof. This is an analytic existence statement, not a computed coefficient library.

The actual covariance also obeys

```text
Sigma_K <= E_K[xx^T]
        <= [1/5 + 9delta(1+delta)^2]I < I/4.
```

Here the contained regular tetrahedron has covariance I/5 and the genuine complement has squared radius at most `3(1+delta)^2`. Hence the stress satisfies

```text
Q > (1/16384) Sigma_K,
sum_e w_e D_e < -(1/16384) tr(M Sigma_K).
```

Undoing the affine normalization preserves these two inequalities by congruence. For rational input geometry, an exact stress can, in principle, be recovered by enumerating dyadic probability vectors on the selected tree edges and checking the three leading minors of `Q-(1/65536)I`; strict separation guarantees termination. No such whole-tree coefficient catalogue was computed or claimed here.

## 5. The different comparison tetrahedron and exact barycentric attenuation

Use the **actual contained tetrahedron**

```text
T_a^R = conv(R0,R1,R2,S),
```

not the parent's `conv(B0,B1,B2,S)`.

Define

```text
o=(1-beta,beta,0)
v_i=u_i+s o_i
H=s+sum_i q_i v_i
A_j=p_j(1+sum_i o_i q_i)+q_j.
```

H is strictly positive throughout the closed weight triangle. In the ordered tetrahedron `(R0,R1,R2,S)`, the exact barycentric coordinates of the other labels are

```text
lambda_S(B_j)   = d_s q_j/H
lambda_Ri(B_j)  = e_i [delta_ij-v_i q_j/H]

lambda_S(L_j)   = d_s A_j/(H d_j)
lambda_Ri(L_j)  = (e_i/d_j)[delta_ij+p_j o_i-v_i A_j/H].
```

The R and S rows are unit coordinate rows. Direct substitution verifies that every row sums to one and reconstructs the displayed raw vertex. Moreover,

```text
6 Vol(T_a^R) = H/(d_s e0 e1 e2) > 0.
```

In particular every non-tetrahedral label has nonnegative S-coordinate. Only its R-coordinates can be negative.

Let eta(a) be the largest negative part of any displayed barycentric coordinate. It is a completely explicit rational maximum, not a fitted mass parameter. It is nonincreasing over the entire admissible a interval. The signs of the bracketed terms above do not change with a, while

```text
d(e_i)/da = -q_i < 0,
d(e_i/d_j)/da = -(q_i+p_j+p_j q_i)/d_j^2 < 0.
```

Thus **passing a shell test at one a certifies every later admissible a**, but with the uniform centroid freshly recomputed for each resulting body. What is transported is a convex inclusion, not a centroid, density, equilibrium census, or arrow stress.

If `eta(a)<=1/32768`, send `(R0,R1,R2,S)` affinely to `(z0,z1,z2,z3)`. Every barycentric coordinate is at least `-eta`. Because `sum z_i=0`, the whole actual image K obeys

```text
T subset K subset (1+4eta)T subset (1+1/8192)T.
```

The shell lemma therefore applies. This gives an exact pointwise sufficient condition on the general actual chart, beyond the convenient parameter boxes below. For that general pointwise application, require `Delta>0` and all displayed denominators positive; when `max p_j>s`, the left endpoint is `-1/max(s,p0,p1,p2)`, not `-1/s`. A condition checked at one fixed weight does not assert feasibility of the whole weight triangle. Theorems A and B separately retain the whole triangle through `s>max p_j`.

The new inclusion allows actual vertices near the middle of a tetrahedral edge. This is precisely what the old four-corner assignment failed to retain as a became positive.

## 6. Uniform estimates proving both parameter theorems

### 6.1 Entire pencil, all weights

Put

```text
p_* = max_j p_j,  Q=max_j q_j,
r=p_*/s,  ell=Q/s+Q.
```

Assume r<1. On the entire maximal pencil,

```text
d_j >= 1-r,
e_i <= 1+ell.
```

Write

```text
C_j=(s q_j-p_j sum_i u_i q_i)/H.
```

Then

```text
delta_ij+p_j o_i-v_i A_j/H
 = delta_ij-u_i A_j/H-o_i C_j,
A_j/H <= p_j/s+q_j/s,
max(C_j,0) <= q_j.
```

Because u_i and o_i belong to `[0,1]`, every negative coordinate is bounded by

```text
eta(a) <= eta_- := (1+ell)(r+ell)/(1-r).
```

This is uniform in beta, both independent stack weights, and a, including arbitrarily close approaches to either true horizon. Consequently the more general sufficient full-pencil domain is

```text
r<1,   (1+ell)(r+ell)/(1-r) <= 1/32768.
```

The simple box in Theorem A follows by setting `epsilon=1/131072`: there `r<=epsilon`, `ell<=2epsilon`, and

```text
eta_- <= 3epsilon(1+2epsilon)/(1-epsilon)
       < 4epsilon = 1/32768.
```

This proves Theorem A without invoking any old numerical pencil certificate or a vertex-count theorem.

For positive a alone one may use the slightly wider sufficient bound

```text
eta(a) <= (1+Q)(r+ell),
```

since then `d_j>=1` and `e_i<=1+Q`. The exact eta(a) criterion can be substantially less conservative than either maximum-coefficient bound.

### 6.2 Majority positive tail with unrestricted relative left coefficients

For every positive a,

```text
p_j/[s(1+a p_j)] <= 1/(a s).
```

The same barycentric formulas therefore give, without a smallness assumption on p_j/s,

```text
eta(a) <= (1+Q)[1/(a s)+Q/s+Q].
```

Thus a general explicit tail is certified whenever

```text
(1+Q)[1/(a s)+Q/s+Q] <= 1/32768.
```

Under Theorem B's hypotheses, `Q<=2^-18` and `Q/s<=2^-18`; at `a s>=2^16`,

```text
eta(a) <= (1+2^-18)(2^-16+2^-17) < 2^-15.
```

All later a are covered as well. Finally

```text
s(1+1/Q) = s+s/Q > 262144,
(65536/s)/(1+1/Q) < 1/4.
```

This proves both the asserted tail and its strict three-quarter length claim. The condition `p_j<s` guarantees the actual stack geometry for every weight, not merely for one favorable barycentric stack point.

## 7. Exact nonwinning controls and actual verification

No numerical optimizer was used. The continuous theorems are analytic. A standard-library exact audit independently checks all 64 corner trees, the rational constants, the barycentric identities, and 13 actual uniformly refilled bodies.

For the first eleven controls use

```text
epsilon=1/131072, beta=2/5, s=1,
p=epsilon(1/2,2/3,3/4), q=epsilon(1,3/4,1/2).
```

Five have `u=(1/5,2/5,2/5)` and respectively

```text
a=-1/2, 0, 1, 65536, 131072.
```

Six more have `a=65536` and respectively

```text
u=(0,2/5,3/5), (2/5,0,3/5), (2/5,3/5,0),
  (1,0,0), (0,1,0), (0,0,1).
```

The twelfth control demonstrates genuine near-edge refinement:

```text
beta=1/2, s=1, p=q=(1/131072,1/131072,1/131072),
u=(1/3,1/3,1/3), a=131073/2.
```

After regularizing the NEW comparison tetrahedron, each B_j has squared distance greater than 1 from every tetrahedral corner. Nevertheless its largest negative barycentric coordinate is only

```text
eta=218455/68720525312.
```

For example B2 has the complete barycentric row

```text
(-218455/68720525312,
 -218455/68720525312,
  17180218711/34360262656,
  131075/262148).
```

Thus a genuinely ten-vertex body in the new full-pencil region is not covered by pretending that all its vertices stay close to four corners.

The thirteenth control belongs to the expanded left-coefficient tail:

```text
beta=2/5, s=1,
p=(1/2,2/3,3/4),
q=(1/262144,1/524288,3/1048576),
u=(1/5,2/5,2/5), a=65536.
```

Every control is first affinely normalized by `(R0,R1,R2,S)->(z0,z1,z2,z3)`, is centered at its actual transformed uniform centroid, and uses the single exact physical pair

```text
M=[[7,1,2],[1,5,-1],[2,-1,6]],  N=M^(-1).
```

All thirteen have strict `(S,U,H)=(4,4,6)`, physical weak count zero, and no zero primitive. There are **836** exact true-edge primitive checks in total. The seven interior-weight examples are 10/17/9, the three weight-edge examples 10/16/8, and the three weight corners 9/14/7. They are nonattainers, not C34 examples of class110.

The true hull is reconstructed from supporting planes, redundant labels are detected by active-normal rank, and maximal cycles and genuine edges are rebuilt. A separate origin-to-true-facet fan verifies volume, centroid and covariance against the seven-cell formulas. The full report retains every coordinate, barycentric row, true face, true edge and four-primitive packet.

Normal execution, a fresh-directory source-only execution, and the lossless recovery execution all completed. Both source-only reconstructions reproduced the report and stdout byte for byte. This is not a proof-assistant formalization and not a numerical sampling proof of the parameter continuum.

## 8. Self-contained recovery capsule

The readable audit is `positive_shell.py`, 11970 bytes, SHA-256 `1d21dd11a747bf1ef6a21558bc94e9c2edf55e7dfa7dccd0b3719d85ba8e0799`. The complete lossless executable capsule below reconstructs all its bytes and executes it. There are no downloaded inputs, omitted helpers, optimizer seeds, or parent-source dependencies.

Exact stack: **CPython 3.13.5, standard library only, assertions enabled**. Save the following block as `recover_positive_shell.py` with LF line endings and a final newline, then run:

```text
python -B -S recover_positive_shell.py fresh_shell
```

The capsule is 7931 bytes, SHA-256 `abcf5fb7c56256a9a130df8c2cb3d05c834de2454ff82dd7ece3aa0a84ebcb33`.

Expected reconstructed outputs:

```text
positive_shell_report.json
  bytes 211085
  SHA256 cb9a66165b4c1149a12bd1c5cd5af135a8d61f6662fc9f9e0db272875b5122fa
positive_shell_stdout.txt
  bytes 1022
  SHA256 cb5d95aa2117e5043d2ef963eb18ba5139d25cd115a1ccd77c12cca7fab3dad5
```

Expected terminal markers:

```text
ALL_64_CORNER_TREES_AND_SHELL_CONSTANTS_PASS
ALL_13_ACTUAL_REFILLS_HULLS_MOMENTS_AND_CENSUSES_PASS
FULL_CUT_STACK_POSITIVE_SHELL_ANALYTICAL_AUDIT_PASS
SOURCE_ONLY_RECOVERY_ALL_EXACT_PINS_PASS
```


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]


**Exact transport correction for the preceding encoded block:** before running it, replace the three damaged DATA substrings `cmu+1dZbnsDFV54` with `cmu+1dZsnsDFV54`, `pDsbjRsbjRDCnN1Z` with `pDsbjRDCnN1Z`, and `XEBE3jE3TV/gN1Z` with `XEBE3TV/gN1Z`. These replacements restore the byte-pinned capsule whose complete authoritative copy is embedded in the linked Markdown handoff and recovery script. The payload hash check prevents accepting any remaining transport error.

## 9. Remaining obstacle and continuation

The parent's full `1/1024` lateral region remains unresolved for general positive a. In particular, its permitted right-side quantity `Q/s+Q` can be much larger than the new shell threshold. Tightening the full-pencil lateral box is an explicit tradeoff, not an assertion that the old right-corner obstruction vanished at its original scale.

Theorem B nevertheless opens a genuinely different region: all three left fractions range through `(0,1)`, and more than three quarters of each positive pencil is excluded uniformly over the complete stack triangle. The exact monotone eta(a) criterion additionally certifies any rightward suffix whose starting shape passes, including shapes outside the convenient symmetric boxes.

A failed shell test is only failure of this sufficient bound. It is not a feasible weak rooted tree, a common-metric survivor, or evidence for class110. No actual survivor was obtained. The most useful continuation is to improve the tetrahedral-shell constant or adapt the contained comparison simplex when the unequal right coefficients make this particular barycentric shell too large; the exact negative-coordinate formulas preserve the actual geometry and provide a direct starting point.

No whole cut-stack incidence, E17 type, or canonical catalogue count is subtracted. The accepted global bracket remains **34 ≤ C_min ≤ 622**. fileciteturn0file0L887-L889

Convenience copies, not recovery dependencies: [readable exact audit](sandbox:/mnt/data/cut_stack_shell/positive_shell.py), [lossless recovery script](sandbox:/mnt/data/cut_stack_shell/recover_positive_shell.py), [complete exact report](sandbox:/mnt/data/cut_stack_shell/positive_shell_report.json), [complete Markdown handoff](sandbox:/mnt/data/cut_stack_shell/result_markdown.md).
