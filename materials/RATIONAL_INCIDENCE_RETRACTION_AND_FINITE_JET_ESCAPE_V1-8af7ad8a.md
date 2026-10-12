# material-8af7ad8a6e76

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# RATIONAL_INCIDENCE_RETRACTION_AND_FINITE_JET_ESCAPE_V1

## Status and scientific contribution

Coordinator analytic derivation, with a separately preserved complete exact-arithmetic chart compiler/control. This strengthens the known smoothness of genuine convex three-polytope realization spaces to explicit rational local coordinates and a rational incidence retraction. It then gives a finite, uniform, necessary-and-sufficient jet criterion for same-lattice proper110 regularization of an actual weak-inclusive S1U1 E17 body. Neither feasibility of this criterion nor the existence of such an input body is asserted. The global interval remains 34 <= C_min <= 622; exclusion and an attaining construction remain separate obligations.

There are three main results:

1. Every genuine convex three-polytope realization has a rational local incidence chart, with E+6 free scalar coordinates, obtained by degree-at-most-three elimination in the radial incidence graph. This is not the private-whole-facet hypothesis and does not require simple vertices or triangular facets throughout.
2. Approximate incidence jets can be corrected by an explicit rational retraction without changing their prescribed order. Any successful finite escape jet produces an exact same-lattice rational deformation in the vertex/metric representation, with the actual moving uniform centroid and the same inverse metric.
3. For the genuine 23-variable E17 chart and degree-at-most-12 physical rows, one finite jet order L_* suffices whenever local regularization is possible at all. An explicit safe order is L_*=576*(3230)^2*(30*29^22)^4, with 2^479 <= L_* < 2^480. This is an enormous existence/decision bound, not a computation at that order and not a useful numerical cutoff currently executed.

## Exact inputs and primary external theorem

The complete source [internal-source-reference] was read through EOF, unchanged SHA256 dcf2cf5c0aa9fdcc106b5375502e4fe198b43833ae0b70405698f082e6bf770a. It supplies the actual 23-variable E17 chart, seven full-rank planarity equations, actual moment formulas and polynomial physical rows of degrees at most12. Its previously accepted weak-inclusive V/F exclusions are premises, not replayed here.

The complete immutable worker result minimum-0230 was read through EOF, unchanged SHA256 daa0643fe164f5e11709744cc9493058547276f9356231fc732b06ef31aef86e. It supplies exact VF complementary pairing and the boundary on right-corner second-order compression. Its accepted reduced physical-packet/radial-index input is used with its stated scope. No contrary parent incidence or renamed control is used.

External quantitative input: Saugata Basu and Marie-Francoise Roy, Quantitative Curve Selection Lemma, arXiv:1803.00505v3, 19 July2021, Theorems2 and4, https://arxiv.org/pdf/1803.00505. The statements and relevant proof were inspected, including rendered pages3 and11. In n ambient variables and polynomial degree d, put N=(2d+6)(2d+5)^(n-1), N'=5(n(2d+4)+2)N. Their Theorem4 supplies an entering semialgebraic curve whose Zariski closure has degree at most B=4dN^2(N')^2. The proof below derives the jet consequence; that consequence is not quoted as a theorem of Basu-Roy.

## 1. Rational charts from radial-graph elimination

Fix a genuine convex three-polytope P and a fixed interior point o. Write w_i=y_i-o for its vertex vectors and p_F for its facet poles normalized by p_F.w_i=1 on incidences. The vectors of two types have three coordinates each. The incidence equations are

    p_F.w_i=1, for i incident to F.

Their graph is the simple planar bipartite radial graph, with V+F nodes and I=2E edges. Every nonempty induced subgraph has a node of degree at most three: for at least three nodes this follows from e<=2v-4, and smaller graphs are immediate. Repeatedly delete such a node and record its surviving neighbors. Reverse this order to reconstruct the incidence configuration.

When a node x is reconstructed, it has d<=3 already reconstructed opposite-type neighbors a_1,...,a_d. Solve

    a_j.x=1, 1<=j<=d.

At the given genuine realization those d neighbor vectors are linearly independent. For neighbors that are vertices, they belong to one true supporting face whose plane does not contain o; any three are noncollinear and hence their position vectors are independent. For pole neighbors, apply the same argument to the corresponding true face of the polar. Smaller subsets are independent as well.

Choose one nonsingular d-by-d coordinate minor at the base realization, retain the other 3-d coordinates of x as free parameters, and solve by Cramer's rule. The chosen minor remains nonzero in a neighborhood. All solved coordinates are rational functions of parameters already introduced and the new free coordinates. Every graph edge is imposed once, at its later-built endpoint.

The number of free scalar coordinates is

    sum_nodes(3-d_node)=3(V+F)-2E=E+6.

The inverse on actual nearby incidence configurations simply reads the designated free coordinates. Thus this is a rational local chart, not merely a full-rank Jacobian or a rational domination with an unidentified inverse. A finite set of pivot choices covers the genuine realizations for any fixed deletion order. All true nonincidence slacks and nonzero pivot minors persist locally, so the true face lattice is preserved. Nothing asserts convexity on all parameter space outside that neighborhood.

The construction is over Q whenever o is rational. For the affine E17 chart fixing 0,e1,e2,e3, the single fixed point o=(1/4,1/4,1/4) lies in the interior of every genuine body in that chart; it is NOT a substitute for the volume centroid. Its role is only to avoid infinite raw facet poles.

A crude common-denominator degree bound is also explicit. If previously reconstructed coordinates have common numerator/denominator degree at most D, Cramer's rule at a d<=3 node gives, after taking a common denominator with the preceding nodes, degree at most (d+1)D+1 <= 4D+1. Starting at D=0, after m=V+F nodes the bound is (4^m-1)/3. This concerns the raw incidence rational functions, not a claim that the later centroid or affine-normalization expressions have this same degree.

### Corollary 1.1: rational proper realizations suffice for attainment

Rational parameter vectors are dense in each rational chart. The actual filled-volume centroid depends continuously and rationally on true vertices in a fixed oriented boundary fan. A proper110 body has a neighborhood with the same strict equilibrium labels and no additional weak points: retain the strict negative rows at the two roots and one existing positive exit at every other vertex/facet. The reduced physical-packet criterion excludes weak edge points too. Therefore every proper110 real body can be approximated by rational-coordinate homogeneous proper110 bodies with the SAME lattice and E, keeping physical Euclidean metric I throughout.

Consequently there cannot be an irrational-only minimal-complexity attainer. This does not provide a numerical minimum or an attainer at34. The assertion is stronger than approximating vertices independently, which can split polygonal faces and change E.

### Corollary 1.2: local sixteen-parameter Euclidean families in E17

The raw E17 incidence chart has23 parameters. The seven-dimensional similarity group (three translations, three rotations, one positive scale) acts freely infinitesimally on a labelled full-dimensional realization. Its tangent action on the23 free coordinates has rank7. Select seven coordinate rows with a nonsingular minor on this action and hold those seven free coordinates at their base values. The remaining16 parameters give a rational family transverse to similarities. By the implicit function theorem, every sufficiently close physical shape is similar to one in this family. This is a local statement with base-dependent fixed values, not a precomputed global16-variable polynomial atlas or a rational inverse for the similarity normalization. Mechanical counts and actual-centroid status are similarity-invariant.

## 2. Explicit rational retraction and high-order error control

Let pi extract the chart's designated free coordinates from an arbitrary nearby mixed vertex/pole configuration, and let R reconstruct by the ordered linear solves. Then pi R=id and R pi is a rational retraction onto the incidence manifold in its pivot domain.

It also has the error estimate needed for jets. Suppose an arbitrary analytic mixed configuration Z(t) has all incidence residuals p_F(t).w_i(t)-1=O(t^(L+1)). Compare it to R(pi Z(t)) node by node in reconstruction order. Free coordinates at each node agree exactly. Its solved coordinates satisfy a uniformly invertible linear system; the discrepancy in the right-hand side is a sum of original incidence residuals and discrepancies of already reconstructed neighbors, with bounded coefficients. Induction gives

    R(pi Z(t))-Z(t)=O(t^(L+1)).

This is an explicit triangular proof, not an assertion that an approximate solution automatically extends on a singular variety.

Apply it to an approximate jet in the23-variable, four-vertex affine gauge. For each facet compute its raw pole about fixed o from its first three vertices. Those three incidence equations hold exactly; residuals at the other incident vertices are the seven planarity polynomials divided by nonvanishing support denominators. Thus planarity residual O(t^(L+1)) gives the same mixed-incidence residual order. Retract as above. If the four affine anchors moved at order L+1, affinely renormalize them to 0,e1,e2,e3; this is another rational transformation differing from the identity at order L+1. Transport the metric by inverse congruence and divide by its positive trace. Never reset a transported metric to I. The resulting point of the genuine23-variable carrier differs from the original jet by O(t^(L+1)).

Every polynomial physical row therefore changes by O(t^(L+1)). Any positive leading coefficient appearing by order L survives. The recovered vertices satisfy the exact face equations at all orders. Compute the ACTUAL centroid afterward by the fixed true boundary fan, g=J/(4D), and use the actual inverse of this same SPD metric in the polar rows. This is not an independent motion of the reference point. The rational metric/vertex representation describes a genuine homogeneous Euclidean body after the corresponding linear realization of the SPD form.

If the input jet has rational coefficients and base data are rational, the recovered vertex/metric family is rational in t with rational coefficients. More generally it is rational over the field generated by the input coefficients. The existence theorem below permits arbitrary real coefficients; an exact executable decision procedure requires exact algebraic input or an appropriate coefficient-field oracle.

## 3. Exact finite-jet formulation, including right VF corners

Let z0 be an ACTUAL weak-inclusive S1U1 E17 realization. Use the23-variable local carrier C(z)=0 with seven planarity equations. Maximum-simplex bounds and their tie walls are gauge choices, not physical infinitesimal constraints; remove these artificial inequalities for the local question. Work in a sufficiently small true-lattice, SPD neighborhood of z0 and protect all originally nonzero physical row signs.

Use the polynomial row extensions from [internal-source-reference]:

    P_ij=(4D y_i-J)^T M(y_j-y_i),
    R_FG=n_F^T adj(M)(H_F n_G-H_G n_F),
    H_F=4D h_F-n_F.J.

Their signs on the carrier are the genuine primal and same-inverse polar signs; all divided factors are positive near z0. Degrees are at most12. They have well-defined ambient polynomial extensions even when a trial jet is temporarily off the planarity manifold.

Form the reduced physical selector list. At VE use its forced primal row, at EF its forced polar row. At each VF choose one of the TWO exact complementary pairs (P1,R2) or (P2,R1) from minimum-0230. There are at most2^q<=256 choices and at most k+q<=17 selected rows for any one choice. At a right corner retain the paired original rows for this all-orders test; do not replace them at higher order by one first-order normalized row and discard the changing Gram coefficient.

For integer L>=1, define Jet_L(z0) to mean that some selector and some real vectors z1,...,zL exist for

    Z(t)=z0+z1 t+...+zL t^L

such that:

(a) every coefficient of t^ell in C_j(Z(t)) is zero for 0<=ell<=L;
(b) for each selected row f, its first nonzero coefficient among orders1,...,L is positive.

Since the selected f(z0)=0, there is no order0 exception. No condition is imposed on harmless unselected zero rows. This is a finite existential semialgebraic formula: choose the leading order of each selected row, impose earlier zero coefficients, and make that coefficient positive. Each coefficient is a polynomial of degree at most12 in z0,z1,...,zL. The coefficient count is huge, but finite.

### Theorem 3.1: finite-jet sufficiency at every order

Jet_L(z0) gives a genuine same-lattice analytic proper110 arc for all sufficiently small t>0. In fact the vertex/metric arc can be chosen rational in t by Section2. Correct the incidence equations at order L+1, preserving every selected positive leading term. The actual COM and reciprocal metric are built into the physical rows. Continuity protects every original nonzero sign. The accepted physical selector equivalence then retains S=U=1 and removes every weak point; the radial-index theorem gives H=0.

A truncated polynomial Z(t) itself need NOT be a polyhedral realization. The rational correction is part of the certificate-to-body construction. The method does not replace equality to all orders by an unproved small-residual heuristic.

## 4. A uniform order sufficient for necessity

Here is the algebraic observation converting curve degree into jet order.

Let gamma be a nonconstant semialgebraic arc entering a prescribed strict sign set, with Zariski closure of degree at most B. Choose the irreducible curve component and real local branch used near its endpoint, and take the complex projective normalization. A local real uniformizing parameter s gives an analytic parametrization gamma_tilde(s) of the branch. This is a primitive local parameter; arbitrary time slowdowns such as s=t^m are not used to estimate orders.

If a polynomial f of degree at most d is strictly positive on the branch, it does not vanish identically on that component. Its homogenization restricts to a nonzero section of the degree-d hyperplane bundle on the normalized projective curve, whose degree is d*deg(C). Its zero divisor is effective and has that total degree. The order at the chosen normalized point is consequently at most dB. The affine homogenizing coordinate is nonzero at this finite point, so this is precisely ord_s f(gamma_tilde(s)). This argument is the curve/hypersurface intersection bound with local multiplicity; it remains valid at a singular point of the image because orders are taken on its normalization.

Suppose z0 lies in the closure of the nearby proper110 set. Finite selectors and sign conditions imply that z0 is in the closure of one selected strict sign set on the genuine carrier. Its defining polynomials, including a small ball and open geometry guards, have degree at most d=12 in n=23 ambient variables. Basu-Roy supplies an entering curve with degree bound B=4dN^2(N')^2. Along its normalized branch every selected positive row has a positive leading coefficient by order dB. Taylor truncation of the genuine analytic arc to order L_*=dB makes the planarity coefficients vanish through that order and preserves these leading coefficients. Hence Jet_L*(z0) holds.

Combining with Theorem3.1 proves

    z0 is a limit of same-lattice proper110 bodies
      iff Jet_L*(z0),
    L_*=4d^2 N^2(N')^2, n=23,d=12.

In this case N=30*29^22, N'=3230N and

    L_*=576*(3230)^2*(30*29^22)^4,
    2^479 <= L_* < 2^480.

One may use the simpler larger integer2^480 as the jet cutoff. The count of signs/selectors affects computation size, not this degree bound. Using n=16 and d=12 without an explicit polynomial16-variable chart would be unjustified; the bound deliberately uses the actual23-variable polynomial ambient chart.

This proves that arbitrarily long reparameterizations do not force an unbounded MINIMAL witness order. It does not prove that the minimal witness order is small, that first/second order suffice, or that a witness exists at every weak-inclusive S1U1 point.

### Consequences and boundaries

A fixed actual algebraic input admits an exact finite algebraic regularizability test; no such target input has been supplied or tested here. A universal density claim could be phrased as a finite first-order sentence quantifying z0 over the faithful closed atlas and then these jet variables. That sentence has not been decided. A negative answer at some z0 would establish a genuine local regularization obstruction, not automatic global E17 nonexistence. Conversely, an actual proper110 point is an attainer at34 and needs its own complete construction/census.

The original right-VF example explains why the paired test matters. With u1=A t^2+B t^3, u2=-t and corner coefficient c=2t, the first primal exit is (A-2)t^2+B t^3 while the complementary normalized polar exit is u1. A=2,B=0 leaves a zero row; A=2,B=1 first resolves at order3. The finite test retains this distinction automatically. This recalls the literal parent's actual controls; it is not a new S1U1 example.

## 5. Complete compiler/control capsule and observed execution

The companion immutable material [internal-source-reference] contains the complete raw UTF-8 Python source. Save it exactly as rational_incidence.py, with LF and final newline. It is self-contained: Python3.13.5 was used, only the standard library, assertions enabled, no random seed, optimizer, input files or network.

Reconstruction: python -B rational_incidence.py build
Verification: python -B rational_incidence.py check
Expected marker: RATIONAL_INCIDENCE_RETRACTION_E17_PASS
Expected summary: FREE_PARAMETERS23 V_E_F10 17 9 DEFORMATIONS3
Expected strict counts at base and all three controls: [5,6,9].
Source:8966 bytes, SHA256747db8f521e4769245c5c44053b237982deb6a5f3a4a7e79d2e303799fe0f203.
Generated rational_incidence_report.json:170782 bytes, SHA2560d0ceac31e39e9ac01c0bee5a3e31a6fc38b3a6b80cb0adc0b84ae56510ed1f3.

The source constructs a rational six-vertex perturbed triangular prism with E11/F7, truncates two specified simple vertices at1/16, and obtains a true10/17/9 body. It regenerates all maximal faces, genuine edges, outward cycles, actual volume centroid, chart pivot choices and23 free coordinates. Three deterministic rational parameter changes reconstruct with all34 incidences exact and every true nonincidence slack strictly positive. Each reconstructed body is checked against its exact convex hull, and its poles are moved to its OWN actual volume centroid before the same-metric census. The chart inverse and retraction idempotence are checked exactly.

Normal build/check and a fresh source-only build/check all passed with identical pins. These finite controls check the implementation at their exact rational endpoints, not an interval certificate for an entire parameter box. The general chart/retraction and finite-jet theorems are analytic proofs above, not inferred from the endpoints. The strict569 controls are not target S1U1 bodies and do not improve either complexity bound.

A practical negative result is retained: perturbing all23 free rational parameters in this deliberately naive Cramer implementation produces some integers exceeding4300 decimal digits. The final source explicitly disables Python's trusted-integer string limit; arithmetic and all checks remain exact. Thus rationality is not a claim of small bit complexity. Better elimination orders, denominator sharing, modular methods or local numerical evaluation followed by exact recovery may matter for a useful search implementation.

## Next scientifically useful move

Use the explicit rational chart/retraction to turn a genuinely positive mixed contact jet into an exact same-lattice family or to attack a residual actual positive-stress core. The sixteen-dimensional Euclidean slice also permits equality-free local search without separately optimizing fake centroids or independent dual metrics. Sharpening the huge universal jet bound is secondary to proving one real escape mechanism or an actual first-layer exclusion/attainer. No new global exclusion, proper110 density theorem or canonical record is claimed.
