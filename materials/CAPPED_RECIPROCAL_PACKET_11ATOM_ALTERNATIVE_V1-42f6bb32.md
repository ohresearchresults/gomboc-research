# material-42f6bb32e1c3

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# CAPPED_RECIPROCAL_PACKET_11ATOM_ALTERNATIVE_V1

Coordinator analytic companion to MIXED_5P5Q_PACKET_COVER_COMPLETENESS_V1, material [internal-source-reference], SHA256 4263f2c0cdd5dd328ce3ef77f242f8978b0eb3cab49f3796bc54a623026d30cf. No numerical solver result, new body or excluded E17 cell is asserted. The application context is the fully read actual-cylinder result minimum-0229, SHA256 325b2943769ef476fd483b07ac9289dcfd2b090aef1847f44a0df8e59eabd187.

## 1. An exact primal alternative to small mixed separators

Fix a genuine centred body and its actual covariance C>0. For a physical metric M>0 define the square-root-free normalized pair

 P(M)=M/tr(CM),
 Q(M)=M^-1/tr(C^-1 M^-1).

Thus tr(CP)=tr(C^-1 Q)=1 and P Q is a positive scalar multiple of I. Impose fixed closed adjacent eigenvalue caps p>=q>1 on C^(1/2) M C^(1/2). Metrics are identified up to positive scaling. Their normalized pair set R is compact: after tr(CM)=1 the spectral caps bound all eigenvalues above and away from zero. Let K=conv(R).

For any finite complete selected primal/polar arrow packet there is the following exhaustive alternative:

(A) Its closed nonnegative row system is infeasible in K. Then the companion theorem gives a positive-gap separator on at most six one-sided rows, or at most five primal plus five polar rows.

(B) It is feasible in K. Then there are m<=11 genuine capped physical metrics M_l and weights w_l>=0, sum w_l=1, for which the pair

 Pbar=sum_l w_l P(M_l), Qbar=sum_l w_l Q(M_l)

satisfies EVERY row of the selected complete packet.

Case B is an exact certificate of failure of this convex relaxation on this body/packet. It is NOT one physical metric and does NOT establish S1, U1, H0 or an attainer.

### Proof of the eleven-atom bound

The affine product specified by tr(CP)=tr(C^-1 Q)=1 has dimension 5+5=10. Caratheodory's elementary reduction therefore bounds a convex representation by eleven points of R. To see the reduction directly, any representation with more than eleven positive weights has an affine dependence among its pair atoms. Vary the weights along that dependence, maintaining their sum and represented pair, until at least one weight first becomes zero. All remaining weights stay nonnegative. Repeat. Compactness also makes conv(R) compact in this finite-dimensional setting. No orbit-extremality theorem, optimality, or uniqueness of the atoms is assumed.

The eleven atoms may be interior capped reciprocal pairs. Requiring all atoms to be a single spectral corner would be an unjustified restriction. The accepted exact one-curve hull can be used to locate a witness, but it is not needed to state or prove this finite representation.

## 2. Rational witnesses whenever the complete relaxed packet is strictly feasible

Assume the actual body has rational vertex coordinates, and therefore rational exact volume centroid, rational true poles and rational covariance C. Assume a pair in K gives STRICTLY POSITIVE values to every row of the selected complete packet. Then Case B can be realized with at most eleven rational positive-definite matrices M_l, strictly inside both spectral caps, and rational nonnegative weights. Consequently P(M_l), Q(M_l), all arrow values and the resulting positive margins are rational.

Proof. Start with an at-most-eleven-atom representation and discard any zero weights. Its finite set of row values has a positive minimum. For each atom replace M by

 M(epsilon)=(1-epsilon) M + epsilon C^-1,  0<epsilon<1,

using any initial positive scaling for M. Its whitened matrix is (1-epsilon) H+epsilon I, with the SAME eigenvectors as H. Every adjacent ratio greater than one strictly decreases, since

 ((1-epsilon) h_i+epsilon)/((1-epsilon) h_j+epsilon) < h_i/h_j

for h_i>h_j>0. An equal ratio remains one, already strictly below p and q. Thus every atom moves into the strict capped domain for any epsilon>0. For sufficiently small epsilon the represented pair changes so little that all packet row values remain positive.

Positive definiteness and strict cap inequalities are open. Approximate each of the finitely many moved symmetric matrices by a rational symmetric matrix inside those open conditions. Approximate the positive weight vector by a rational positive vector in the simplex, for example approximate all but one weight sufficiently closely and use the final weight to enforce the sum. Continuity of inversion, trace normalization and all row evaluations preserves the positive packet margins. The number of atoms remains at most eleven. Rational M and C make both normalization denominators and every normalized atom rational.

This proof does NOT imply a rational witness when feasibility exists only on a zero-margin boundary. It does not bound rational denominators or cap-verification complexity.

## 3. Fully physical and checkable data for a relaxation witness

A useful exact witness should include:

1. The actual body coordinates or their complete deterministic generator, maximal facets and true edges; the actual integrated g,C and the same-origin true poles.
2. One COMPLETE necessary selected packet, with all labels and its root(s), not just the three arrows of a smaller independently feasible control.
3. At most eleven rational SPD matrices M_l and rational simplex weights.
4. Exact actual-gauge spectral-cap checks for every M_l; these can use the characteristic polynomial of C M_l and rational isolating intervals, avoiding any numerical matrix square root.
5. The normalized pairs P(M_l),Q(M_l) or exact reconstruction rules, and the rational values of ALL complete-packet arrows at their convex combination.

The original physical inverse in each atom is mandatory. Independently capped matrices Pbar,Qbar do not by themselves prove membership in K. Conversely, a verified convex combination of actual capped atoms proves K-membership even when Pbar Qbar is not scalar.

If every complete-packet row is positive, this exact witness persists on a sufficiently small genuine same-lattice shape neighborhood with uniform refilling and recomputed covariance: retain the finitely many M_l and weights, recompute their two normalizations, and use the strict cap and arrow margins. A rigorously quantified cylinder still requires exact interval or polynomial bounds. Mere continuity gives existence of a neighborhood, not its radius.

## 4. Research consequence

The actual heptagon-triangle programme now has finite exact certificate formats on both sides of the capped-hull question: a small mixed separator, or an at-most-eleven-atom complete relaxed packet. This is not a decision algorithm with a claimed running time, and it is not a physical attainment/exclusion alternative: a hull-feasible packet can still be impossible for every single physical inverse pair.

The H5 separately capped independent three-row example is not yet the Case B witness required here, because neither complete-tree feasibility nor coupled-hull membership was claimed for that example. A successful Case B continuation would identify a genuine limitation of adding further joint-linear packet certificates on that actual geometry. A successful Case A cover for every necessary packet over the full stated cylinder would exclude the cylinder, not the whole incidence class.

Global bounds remain 34<=C_min<=622. No stronger lower bound or smaller attaining example is obtained by these abstract alternatives alone.
