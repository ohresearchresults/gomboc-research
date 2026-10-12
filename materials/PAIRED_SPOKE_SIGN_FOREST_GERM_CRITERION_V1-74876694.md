# material-748766944a6e

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# PAIRED_SPOKE_SIGN_FOREST_GERM_CRITERION_V1

## Scope, exact sources, and evidence
This is a coordinator analytic continuation, not a numerical computation or a new physical example. It gives an exact finite sign criterion for simultaneous analytic top-fixed radial escape of all spoke EFs and their basal VE partners, including arbitrarily many coupled quadratic resonances. It also handles a stated sufficient positive-quadrant selector for basal VF partners. A successful criterion, with two available actual-centroid triangle actuators, gives a genuine complete-packet regularization. Its failure is not an obstruction to general same-lattice shape changes.

The complete immutable parent minimum-0239 was read through EOF, SHA256 02d2c6a3a9b0e54366f01c86b298d2055aea3037c342d8389b23e4b4dd465a38. The two complete analytic sources were also read: [internal-source-reference], NONPARALLEL_TWO_TRIANGLE_ACTUATOR_AND_PAIRED_BLIND_ESCAPE_V1, SHA256 2c914bd63d8483930ed596e79f628c464417de6ca62b250afe09cfb822544b39; and [internal-source-reference], SPOKE_EF_BASAL_PARTNER_EXACT_RADIAL_ESCAPE_V1, SHA256 ce9f3503f2111b0c739ba2a18d21337bcb02390c81dbbca5dc19062b83c0fc70. Their literal geometry and actual-COM conclusions are used without an independent computational replay.

No code materially produced this result. This file is the complete new proof unit. Bounds 34<=C_min<=622, whole-E17 exclusion, universal regularization, and attainment are unchanged. No actual weakS1U1 input is presumed.

## 1. Physical input and exact scalar functions
Use the sources' normalization M=N=I, F:z=h, T:z=k, h>0>k, q=q_T=e_z/k. The body is a genuine uniformly filled parallel heptagon-triangle 10/17/9 polytope at its own volume centroid. There are seven lateral poles. Each physical interior-spoke EF gives an arrow i->j, with bearing pole r_i, adjacent pole r_j, r_i.(r_j-r_i)=0, and its foot in the relative interior of that spoke. The physical arrow graph D is an acyclic outdegree-at-most-one forest, because each bearing facet has a unique foot and |r_j|^2-|r_i|^2=|r_j-r_i|^2>0.

Prescribe actual lateral poles by
 r_i(f_i)=q+(r_i-q)/(1-f_i),   f_i(0)=0.
For each arrow i->j set
 A_i=|r_i|^2-q.r_i>0,
 L_i=q.(r_i-q),
 D_i=q.(r_j-r_i),
 B_i=A_i+D_i,
 T_i(u)=[B_i u-(L_i+D_i)u^2]/(A_i-L_i u).
All denominators 1-f_i and A_i-L_i f_i are positive in a sufficiently small common neighborhood. The exact physical EF row has the sign of
 (A_i-L_i f_i)[f_j-T_i(f_i)].
In particular its successful inequality is f_j>T_i(f_i). Always
 A_i-L_i=|r_i-q|^2>0.
The latter strictness follows because a true lateral pole is distinct from q.

At the basal endpoint of a spoke EF, every possible weak unstable partner is a source-side basal VE, a target-side basal VE, or F-VF, as proved in [internal-source-reference]. Distinct EF spokes have distinct basal endpoints, so these partner groups are not duplicated.

Classify each D arrow as follows.
E: no basal weak partner is being explicitly opened; only the EF inequality is imposed.
S: a source-side VE partner. Then D_i=0, B_i=A_i, T_i(u)=u exactly, and BOTH exits have sign f_j-f_i.
T: a target-side VE partner. The actual geometry gives d_z<0, D_i=d_z/k>0, hence B_i>A_i>0. Its primal exit has sign f_i-gamma_i f_j, where gamma_i<1. Thus the two exact inequalities are
 T_i(f_i)<f_j,  gamma_i f_j<f_i.
For 0<gamma_i<1 put
 Delta_i=A_i/gamma_i-B_i,
 kappa_i=L_i(1-1/gamma_i)+D_i
         =d_z(k-h)/[k^2(1-h(r_i)_z)]>0.
Then
 f_i/gamma_i-T_i(f_i)=f_i(Delta_i+kappa_i f_i)/(A_i-L_i f_i).
V: a basal F-VF partner, using the sufficient selected quadrant f_i>0,f_j>0. Here D_i=0, so additionally f_j>f_i. Both F-source polar exits are then positive; the basal displacement is in the interior of its tangent cone, and one primal edge has a positive first term. Choose its complementary polar exit, as in the source. This selector includes right corners. Completeness for all possible VF escapes is NOT asserted.

Let H be any set of poles required to remain exactly fixed, for example the reduced protected footprint of all other non-spoke weak groups. Thus f_i=0 on H. Actual-centroid corrector planes will later be chosen outside H and all D endpoint poles.

## 2. Finite sign criterion
Use the ordered alphabet -<0<+, represented by -1,0,+1. State 0 means the function is identically zero; a nonzero analytic function has its eventual sign for t>0. Seek one label sigma_i at each D node, with sigma_i=0 on H. The allowed source/target label pairs for each edge are:

E with B_i>0: sigma_i<=sigma_j, except (0,0).
E with B_i<0: -sigma_i<=sigma_j, except (0,0).
E with B_i=0: sigma_j=+, with any sigma_i.
S: sigma_i<=sigma_j, except (0,0).
T with gamma_i<0: sigma_j=+, with any sigma_i.
T with gamma_i=0: (sigma_i,sigma_j)=(+,+).
T with 0<gamma_i<1: sigma_i=sigma_j in {-,+}; require + if Delta_i>0, - if Delta_i<0, and allow either if Delta_i=0.
V with the selected quadrant: (sigma_i,sigma_j)=(+,+).

### Theorem
There exists an analytic germ of all f_i satisfying the exact E/S/T inequalities, the selected V inequalities, and f_i=0 on H if and only if this finite sign-label system is feasible. Whenever feasible, a germ can be chosen so every nonzero f_i has a nonzero LINEAR leading term. Every selected EF and basal-partner exit then has positive leading order at most TWO. Only T edges with 0<gamma_i<1 and Delta_i=0 need order two.

Without V partners, this is an exact all-orders decision for the displayed actual radial physical exits, not merely a sufficient first-jet screen. With V partners it is exact for the explicitly selected positive quadrant, which is only a sufficient physical VF escape condition.

At most seven nodes occur. One may test at most 3^7=2187 assignments; no search over orders or formal coefficients is necessary. A linear-size tree dynamic program is preferable: let S_i be the allowed labels at node i. Process predecessors toward roots; retain a label at i precisely when, for every incoming edge a->i, at least one retained label at a forms an allowed pair with it. Each root must retain a label. Backtracking chooses compatible labels. This is exact because different incoming subtrees have no shared nodes. It is a finite mathematical algorithm, not an executed numerical experiment.

## 3. Necessity, including the zero-derivative case
For E with B_i nonzero, T_i has derivative B_i/A_i and therefore has, sufficiently close to zero, the sign of B_i f_i. The strict inequality f_j>T_i(f_i) gives exactly the listed sign restrictions. These sign restrictions remain necessary when one germ is identically zero. Both zero is impossible.

When B_i=0, D_i=-A_i, and the special physical identity gives
 T_i(u)=(A_i-L_i)u^2/(A_i-L_i u)>=0,
with strict positivity for u!=0 sufficiently small. Thus f_j must have positive sign; the source sign is unrestricted. A zero derivative therefore does not hide an arbitrary higher-order obstruction.

For S, the inequality is exactly f_j>f_i. The sign order and exclusion of (0,0) follow.

For T, B_i>A_i>0, so T_i is strictly increasing near zero and has the sign of its argument. If gamma_i<=0 and f_j<=0, the primal inequality forces f_i>gamma_i f_j>=0, contradicting f_j>T_i(f_i)>=0. Thus f_j>0. Gamma_i=0 additionally forces f_i>0; gamma_i<0 has no further sign restriction.

For 0<gamma_i<1, the open interval
 T_i(f_i)<f_j<f_i/gamma_i
forces f_i and f_j to have the same nonzero sign. Its exact width is f_i(Delta_i+kappa_i f_i)/(A_i-L_i f_i). If Delta_i is nonzero, positivity requires sign(f_i)=sign(Delta_i) in a sufficiently small neighborhood. If Delta_i=0, kappa_i>0 allows either nonzero sign, but never f_i=0. The V row of the table is exactly the selected quadrant. These arguments establish necessity for any analytic germ, with no assumption on its leading order.

## 4. Explicit analytic construction from the labels
For each forest root j choose f_j(t)=sigma_j t, or zero if sigma_j=0. Then construct each predecessor i after its unique target j. Set y=f_j(t). The following recipes are analytic and give the requested sign with a linear leading term whenever the sign is nonzero.

### E edges with B_i>0
Let R_i=T_i^{-1} be the local analytic inverse at zero. The desired inequality is f_i<R_i(y). If the two labels are both + choose f_i=R_i(y)/2; if both - choose f_i=2R_i(y). For strictly ordered labels choose f_i=0 when the source label is 0, and f_i=-t when the source is - and the target is 0 or +. These are all permitted pairs.

### E edges with B_i<0
Again let R_i=T_i^{-1}; it is now decreasing. The desired inequality is f_i>R_i(y), whose sign is opposite that of y. For (sigma_i,sigma_j)=(+,-), take f_i=2R_i(y). For (-,+), take f_i=R_i(y)/2. In the remaining allowed cases take f_i=0 when its label is 0, or f_i=t when its label is + and the target is 0 or +.

### E edges with B_i=0
The target has a positive linear term. Put f_i=sigma_i t, or zero. Then T_i(f_i)=O(t^2), while y has a strictly positive order-one term. The EF opens at order one.

### S edges
Use the B>0 recipe with R_i(y)=y. Thus f_j-f_i is strictly positive at order one.

### T edges with gamma_i<=0
The target y is positive and R_i=T_i^{-1} is increasing with R_i(y)>0. If the source label is +, choose f_i=R_i(y)/2. If gamma_i<0 and the source label is -, choose f_i=gamma_i y/2. If gamma_i<0 and the source label is 0, choose f_i=0. These exhaust the allowed pairs, and both inequalities have strictly positive order-one terms.

### T edges with 0<gamma_i<1
Define the analytic increasing midpoint map
 H_i(u)=[T_i(u)+u/gamma_i]/2.
It has H_i(0)=0 and H_i'(0)=[B_i/A_i+1/gamma_i]/2>0. Set
 f_i=H_i^{-1}(y).
The permitted labels ensure the exact interval width is positive. The EF numerator and primal factor are respectively
 f_i(Delta_i+kappa_i f_i)/2,
 gamma_i f_i(Delta_i+kappa_i f_i)/[2(A_i-L_i f_i)].
They have positive order one if Delta_i!=0, and positive order two otherwise. Arbitrarily many adjacent resonances cause NO escalation of the order: each inverse has nonzero derivative, so every nonzero node retains a linear leading term.

### V edges
Both labels are +. Put f_i=y/2. The EF and both selected F-source polar factors are positive at order one. The actual basal displacement has a nonzero first term in its tangent-cone interior, so at least one primal edge row has a positive order-one term and can be paired with its complementary positive dual row.

All recipes keep an H node identically zero because its selected state is 0. There is no simultaneous implicit cycle: every node has at most one outgoing edge. Incoming subtrees can be constructed independently after the target. A finite common neighborhood makes every original denominator and strict geometric guard valid. This proves sufficiency and the order bound. The inverse functions are uniquely specified local analytic inverses at zero, not asserted globally rational.

## 5. Physical incidence sharpens the sign obstruction
Consider only arrows whose basal partner is a target-side VE. Two such arrows cannot enter the same lateral pole s. Its two possible incoming spoke arrows would meet the two opposite endpoints b,b' of the true basal edge F cap S. Their target-side partners would require simultaneously
 b.(b'-b)=0,   b'.(b-b')=0.
Adding gives -|b'-b|^2=0, contradicting a true edge. The same argument is coordinate-invariant with any SPD metric. Thus this target-partner subgraph has indegree and outdegree at most one and no cycles: its components are directed paths.

Along any component made of positive-gamma T edges, every radial germ must have one common nonzero sign. If two of its nonresonant edges have opposite signs of Delta, NO sufficiently small analytic radial escape germ exists for those paired exits. Individual positive quadratic curvatures do not remove this obstruction. This is a persistent obstruction only to the stated radial family, not to full shape deformation or proper110 density. No actual physical example realizing the conflicting signs is claimed.

Conversely, if no D endpoint is forced by H and every positive-gamma target partner has Delta>=0, assigning + to every D node passes the entire table, regardless of gamma signs at other target partners, B signs at unpaired EFs, source-side partners, or the chosen VF partners. Thus all these coupled packet types have a common germ with pair orders at most two. Another immediate class has only S/T partners, every T has positive gamma and Delta<=0: assigning - everywhere works. The full sign table covers mixtures not described by these convenient sufficient conditions.

## 6. Actual-centroid realization and complete-packet consequences
Assume two distinct lateral triangles lie outside H and outside all D endpoint poles. Prescribe the radial f_i(t) just constructed, keep both end planes and all top vertices fixed, and hold H fixed. Use the two triangles as actual uniform-centroid actuators, exactly as [internal-source-reference]. Their four fixed-apex pole coordinates have rank-three actual centroid derivative; a fixed nonsingular three-column minor defines the analytic correction. No independent masses or polar-volume centroid are introduced.

Because no corrector is an EF endpoint pole, every Q formula above is unchanged. Each basal partner source is an intersection of F and its two prescribed EF endpoint planes. Its other basal-edge endpoint may move under a corrector, but the edge retains its direction up to a positive length factor, exactly as [internal-source-reference]. Hence all successful pair signs and their leading orders survive the true uniformly refilled realization.

### Complete top-carrier class
If the entire weak packet consists of T-carried contacts and the EFs with their explicitly handled basal partners, take H empty. A successful sign table plus two unused triangles gives complete regularization with fixed physical M,N. All T-carried points stay exactly neutral during the pair motion: top vertices are fixed, quad T-source rows change only by positive radial factors, and triangle correctors do not share edges with T. Open T by the source's ordinary carrier motion at amplitude t^3. It is too small to spoil pair orders one or two. All selected physical exits have positive orders at most THREE, independently of the number of coupled resonances. This is a genuine extension of the one-EF/one-partner theorem, conditional only on the displayed sign and corrector hypotheses.

### Other protected weak groups
For arbitrary remaining weak groups, build H as the source's reduced complete protected footprint, omitting only the partners explicitly handled here and retaining both protections at every other VF. Use the parent's auxiliary non-spoke opening R(epsilon), with selected orders at most ten, and put epsilon=t^3. On this actual input apply the same originally constructed germs and correct the actual centroid by the two unused triangles. The nonparallel actuator theorem permits the auxiliary loss of end parallelism. Pair rows change by O(epsilon), which cannot spoil positive orders at most two. All other selected rows are exactly fixed or multiplied by the inherited positive factors. They retain positive orders at most THIRTY. Original nonzero primitive and true-incidence guards remain open.

A genuine weakS1U1 input in either successful class therefore regularizes to proper110 at the same incidence. No such input is supplied here. Failure of the sign table is an exact failure of these radial germ inequalities, but not of all deformations; exhaustion of the two triangle actuators is a separate genuine dependency of this construction. The next consequential question is whether actual weakS1U1 geometry rules out the remaining conflicting path signs, or whether transverse, nonradial shape freedoms can bypass them while repairing the actual centroid.
