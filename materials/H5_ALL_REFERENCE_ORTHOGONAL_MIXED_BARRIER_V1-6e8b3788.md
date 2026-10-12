# material-6e8b37885e0f

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# H5 all-reference orthogonal mixed-template barrier

## Precise result
For the literal homogeneous H5 body at theta=(x,r,p,q,lambda)=(3/20,3/20,3/20,9/20,13/100), centered at its actual uniform volume centroid, let a be centered top vertex9 and q0 the basal polar vertex. For every auxiliary positive definite reference C,
Upsilon_C(P) exp(asinh sqrt(chi_9(C))) > 14/3,
where chi_9=(a^T C^-1 a)(q0^T C q0)/(a.q0)^2-1. This is an all-reference lower bound, not a failed local reference search.

With F=f(10)f(9), f(m)=cos(pi/(2m))^(2m), the unchanged sharp condition-number reflection-product ceiling, using K=max(1,F Upsilon_C^2), consequently exceeds
2427364/650475 > 37/10.
But the largest top9-specific geometric target gamma/(gamma-alpha9^2) obtainable from the existing R homothety is
184189845528335946123113480625/51914865174695118759383445901 < 18/5.
The maximal R parameter is exactly alpha9=71341806413/154940815225, with limiting basal edge index0, basal vertex4, top9. Thus optimizing every C and every allowed top9 R parameter cannot make this unchanged sufficient template exclude this body. This is stronger than the earlier Gamma-template limitation, because Upsilon is the improved orthogonality-constrained factor. It does not prove S1U1 feasibility, does not refute the seven-turn theorem, and does not exclude the actual body mechanically. Whole H5/E17 and 34<=Cmin<=622 are unchanged.

## Actual body and exact origin
Set s=1-lambda. Basal planar points in order0..6 are
(1/4,0), (1-3x/4,0), (1-p,p), (q,1-q), (0,1-3r/4), (0,1/4), (1/16,1/16).
The seven raw spatial basal vertices are (s*b_x,s*b_y,0). The three raw top vertices7,8,9 are (0,0,1),(lambda,0,1),(0,lambda,1).
The nine oriented maximal facet cycles are
(6,5,4,3,2,1,0), (8,7,0,1), (7,6,0), (1,2,8), (9,8,2,3), (9,3,4), (4,5,7,9), (6,7,5), (7,8,9).
The core verifies all supporting vertex triples, all strict nonincidences, rank3 of each vertex normal family, and exactly17 genuine edges; no triangulation diagonals enter the equilibrium census.

At the stated theta, actual Vol=6497249/48000000 and
g=(92526062243/415823936000,87300500333/415823936000,7672449/25988996).
The exact oriented boundary integration agrees with the closed actual volume-moment expressions in the core. Every v_i=raw_i-g and every polar q_f is normalized using this same g. No independent formal moments or polar centroid are introduced.

## Four-pair certificate
Write a=(b0,h), h=1-g_z. Use the aligned auxiliary reference
C=[W+b0*b0^T,h*b0;h*b0^T,h^2],
W=[[223142,-130077],[-130077,219126]]/1000000.
Then chi_9(C)=0. The four actual pairs are:
1. w1=v1; n1 is the unique point of the true polar edge(q5,q6) perpendicular to w1.
2. w2 is the unique point of the true edge(v3,v4) with first coordinate0; n2=(-1/g_x,0,0).
3. w3 is the unique point of the true edge(v5,v6) with second coordinate0; n3=(0,-1/g_y,0).
4. w4=v1+(v2-v1)/16; n4 is the unique point of the true polar edge(q5,q6) perpendicular to w4.
The core/verifier proves all indicated edge parameters lie strictly between0 and1 and all eight vectors lie in their respective bodies. It checks every p_i=(w_i^T C^-1 w_i)(n_i^T C n_i)>14/3.

The three derivatives of log p_i with respect to the independent W entries, plus the weight-sum row, form a literal rational4-by-4 system. Solve it with right side(0,0,0,1) to define the four weights exactly. No rounded weights are inputs. The verifier proves every weight positive and each W-gradient sum exactly zero. If d is the weighted b-gradient, it proves d^T W d<2/5<1.

Apply the finite weighted-log theorem in [internal-source-reference] (GEODESIC_MIXED_REFERENCE_OPTIMIZATION_V1.md, SHA498098f99b56efd67efeb3fcba25aa80ba63f837dd9b281d676434ab5107b72c). The convex function sum lambda_i log p_i + delta has nonnegative derivative in every tangent direction at this aligned reference: the W part is zero and d.db+sqrt(db^T W^-1 db)>=0. Geodesic convexity makes this a global minimum. Since every selected p_i exceeds14/3, the all-reference strict lower bound follows. The pairs need not be active at the true optimum, and the argument does not need an all-edge upper estimate or an exact algebraic optimizer.

The elementary exact trigonometric bound F>59/100 is certified with Machin's identity, alternating rational arctangent bounds giving pi<22/7, and cos(t)>1-t^2/2. Therefore F(14/3)^2>1 and the full ceiling is strictly greater than the displayed rational value. The strict rational gap above the maximal geometric target is
6205385019864317697819797466488089/33769321924509807375009946972452975.

## Physical and geometric countercontrols
The actual body satisfies A strictly and the seven-turn geometric conditions with separate alpha7=alpha8=1/2, alpha9=23/50. All147 R guards are positive, alpha_j>=1-2gamma, and beta_j/alpha_j<2. A rational Taylor bound using pi>333/106 proves cos(pi/7)^7<1/2. The barrier therefore does not merely exploit failure of those geometric hypotheses.

For physical M=[[5,1,2],[1,3,-1],[2,-1,4]], the actual census is S=[0,1,5,6], U=[1,2,4,8], H=[(0,1),(1,2),(1,8),(2,3),(4,9),(6,7)]: own446, no weak edges and no zero primitive.
For physical M9=[[3,1,-1],[1,5,2],[-1,2,4]], top9 has strictly larger M9 norm than both other top vertices, yet the actual census is S=[0,1,4,6], U=[1,4,9], H=[(1,8),(3,4),(4,5),(4,9),(6,7)]: own435, again no weak edge or zero primitive. This shows the top9 maximum is a genuine possible physical top choice, not a removable labeling artifact. Neither control is a110 attainer.

## Complete recovery capsule
The exact proof uses only Python standard-library rational arithmetic. Tested CPython3.13.5, also written for Python>=3.11. Assertions must be enabled. Place these two exact stored UTF-8 sources in one directory, removing only the final .txt from each filename:

- [internal-source-reference]: h5_reference_core.py,9461bytes,SHA54374c6e67c89467a37f68dca0c076ee20a8581acc2791d228f0c8e8f6d9aad8.
- [internal-source-reference]: h5_mixed_reference_exact.py,6460bytes,SHA1c8dff377cfe601bf2d7b42e249720f65c2b8a90c9b6f46eb39d2a0b4e5ff764.

Reconstruction and verification command, no external inputs:
python -B -S h5_mixed_reference_exact.py

Expected output file H5_MIXED_REFERENCE_EXACT.json:11373bytes,SHA b37d991642f376c911cf1f463df4e96fd5397833f45c6fc3bf2a70e2fbbc5de1.
Expected terminal marker: H5_ALL_REFERENCE_ORTHOGONAL_MIXED_TEMPLATE_BARRIER_PASS.
The output includes every exact pair, weight, derivative, matrix, target, comparison and census. All constants and parameters affecting it are in the two source units. The coordinator ran this exact source successfully; the rational identities and analytic geodesic proof are the mathematical evidence, while hashes identify reconstruction bytes. This is not a proof-assistant formalization.

Floating discovery was separate: aligned semidefinite sampling with a complete floating edge-curve oracle located the obstruction, and a finite linear program located the four rational pairs. The final verifier reads no locator output. Failed numerical searches are not mathematical exclusions. Full optional locator sources are preserved separately when their methods are supplied to a computational successor; they are not dependencies of this exact capsule.
