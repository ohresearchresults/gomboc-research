# material-96c76b074bac

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# FULL_CUT_STACK_COMPLETE_PENCIL_AND_ELEVEN_PARAMETER_TUBE_V1

## Status, object and exact source identity

This is a new coordinator theorem on the actual uniformly filled cut-stack nine-cycle incidence. It proves U>=2 for every positive definite metric on ONE ENTIRE maximal projective pencil and on an explicit eleven-dimensional parameter tube around that pencil. It does not cover the whole eleven-parameter incidence, does not subtract an E17 incidence and supplies no own110 attainer. The accepted bracket remains34<=C_min<=622.

The exact all-tree proof uses5791 nonnegative independent-edge integer stresses,104238 positive rational Bernstein coefficient matrices and all46410 rooted spanning trees. The numerical optimization only discovers integer coefficients; the reported continuum conclusion is checked by exact integer/rational inequalities, not by a finite sample or a solver success flag. The complete standalone generator and separate exact verifier were executed by the coordinator. These are observed executions, not a proof-assistant formalization.

This TWO-PART recovery capsule is complete. Part2 is immutable material [internal-source-reference], named Recovery capsule part 2 of 2 - pencil_certificate.py.txt,16434bytes,SHA b36cdea35fb1834d680e4459c3c8163c69a9ca27d96ae422cfe14b18ec7eed1b. Its archived transport text has one shortened variable name relative to the executed source. The exact one-line recovery patch in Section8 is REQUIRED before executing it. That patch reconstructs the executed16437-byte source with SHA b1e887ff04f59652ee400a9988d813ea63a5cc71859755d38086c0f6ca74f7b1. No mathematical or algorithmic change is being inferred from a hash: the complete source and complete literal patch are both supplied. Do not run the unpatched transport input or describe it as the tested source.

The geometric chart used below was proved in fully read [internal-source-reference], SHA dd480d2ba12bf5900f39203067889155843b1fef24f168c4bb1e023a62c142ae. Its two complete sources, also fully read, are [internal-source-reference] (9133bytes,SHA249a774019a71dadb0777992cf831a4173992f429df622f13c1ea3dd15a8f107) and [internal-source-reference] (4179bytes,SHA15a94febb513c71c46cb5d61b7459b173077a517d494fb610bd93af72a364f4f). The present computation has no code or checkpoint dependency on those sources: every vertex, true edge, positive tetrahedron, coefficient and parameter needed for its reconstruction is literal here and in the standalone generator. The earlier whole-chart geometric theorem, not a dimension count, supplies the stated true-incidence domain.

## 1. Actual body, all true cycles and positive volume moments

Use labels0..9=B0,B1,B2,L0,L1,L2,R0,R1,R2,S. For beta in(0,1), positive p_i,q_i,u_i with sum u_i=1, and s>sum u_i p_i, put

    B0=(0,-beta,0), B1=(0,1-beta,0), B2=(0,0,1),
    d_i=1+a p_i, e_i=1+(1-a)q_i, d_s=1+a s,
    L_i=(-p_i,B_i,y,B_i,z)/d_i,
    R_i=(q_i,B_i,y,B_i,z)/e_i,
    S=(-s, sum u_i B_i,y, u_2)/d_s.

In the preceding two expressions, (-p_i,B_i,y,B_i,z) and (q_i,B_i,y,B_i,z) each denote three coordinates: the first coordinate followed by the y and z coordinates of B_i. Let P be their convex hull. The full chart theorem gives exactly the following nine outward maximal cycles whenever all denominators are positive:

    (0,3,4,1,7,6), (0,2,5,3), (0,6,8,2),
    (1,4,5,2), (1,2,8,7),
    (3,9,4), (3,5,9), (4,9,5), (6,7,8).

The true17 edges, in the exact certificate order, are

    (0,2),(0,3),(0,6),(1,2),(1,4),(1,7),(2,5),(2,8),
    (3,4),(3,5),(3,9),(4,5),(4,9),(5,9),(6,7),(6,8),(7,8).

Every listed edge has its two directed arrows, forward then reverse. There are34 arrows, not triangulation diagonals. The body is triangulated by these seven positive actual tetrahedra:

    (0,1,2,5), (0,1,4,5), (0,3,4,5), (3,4,5,9),
    (0,1,2,8), (0,1,7,8), (0,6,7,8).

Their respective positive six-volumes are

    p2/d2, p1/(d1 d2), p0/(d0 d1 d2),
    (s-sum u_i p_i)/(d_s d0 d1 d2),
    q2/e2, q1/(e1 e2), q0/(e0 e1 e2).

Consequently the uniform volume is one sixth of their sum, and the actual centroid is their volume-weighted tetrahedral centroid. No vertex masses, polar centroid or prescribed centre are substituted.

For the central pencil fix the exact rational data

    beta=2/5,
    p=(1/5,2/5,3/5), q=(1/4,1/3,1/2),
    u=(1/5,2/5,2/5), s=4/5.

The stack excess is9/25. The FULL maximal admissible interval is -5/4<a<3. It includes both regular ghost-infinity sections a=0,1 and the valid non-operation sectors a<0 and a>1. The claim is not confined to0<a<1 or to endpoint collars.

## 2. One affine compactification with nonvanishing actual volume

Set q=q2, y_s=u1-beta(1-u2), K=s+q u2. Define the actual affine-linear normalization

    T_a(x,y,z)=(d_s(qz-x)/K, e2(sz+u2 x)/K,
                y-y_s(qz-x)/K).

It is invertible on the whole open pencil and sends S to(1,0,0), R2 to(0,1,0). It has determinant d_s e2/K>0. On the fixed data, K=1 and y_s=4/25. The normalized labelled vertices Z_i=T_a V_i extend continuously to both closed endpoints:

    Z0=(0,0,-2/5), Z1=(0,0,3/5),
    Z2=(2a/5+1/2,6/5-2a/5,-2/25),
    Z3=((4a+5)/(5a+25),(a-3)/(5a+25),-54/(25a+125)),
    Z4=((8a+10)/(10a+25),(2a-6)/(10a+25),67/(50a+125)),
    Z5=((44a+55)/(30a+50),(21-7a)/(15a+25),-22/(75a+125)),
    Z6=((4a+5)/(5a-25),(a-3)/(5a-25),36/(25a-125)),
    Z7=((4a+5)/(5a-20),(a-3)/(5a-20),-49/(25a-100)),
    Z8=(0,1,0), Z9=(1,0,0).

For each vertex its three coordinates have a common denominator, linear and nonzero throughout[-5/4,3]. Thus the whole vector traces the straight segment between its endpoint values, with a possibly nonuniform monotone parameter. Exact endpoint norms give ||Z_i||<5 throughout the closed interval. Merely bounding each scalar coordinate would not suffice for this particular radius claim; the common-denominator segment property is used.

Write

    N(a)=12a^5-7a^4-80a^3+1975a^2+22400a+40500.

The normalized six-volume is exactly

    D(a)=N(a)/[5(a-5)(a-4)(a+5)(2a+5)(3a+5)].

The degree17 Bernstein coefficients of N after a=-5/4+(17/4)t,0<=t<=1, have minimum2008125/128 and maximum125664. The positive denominator is at most202125. Hence D>1/16 even at the closed normalized endpoints. The limiting centroid remains the actual uniform volume centroid. The original physical bodies at a=-5/4 and3 are not claimed to be finite10/17/9 members; their normalized limits are only used for the uniform estimates.

## 3. Rooted-tree alternative and exact continuum separation

Let g be the ACTUAL normalized centroid and define

    H_ij=sym[(Z_i-g)(Z_j-Z_i)^T].

A weak forward escape at vertex i under a physical positive definite metric M is tr(M H_ij)>=0. Along such an edge the squared M-distance to g strictly increases, because

    ||Z_j-g||_M^2-||Z_i-g||_M^2
       =2 tr(M H_ij)+||Z_j-Z_i||_M^2>0.

A strict unstable vertex has every adjacent derivative negative. If there were only one such vertex, choose an outgoing weak escape at every other vertex. Strictly increasing distance forbids directed cycles, so the selected arrows form a spanning tree oriented toward that unique vertex. This implication includes other weak vertex contacts and uses only true edges.

The graph has4641 undirected spanning trees and46410 distinct rootings. The source exhaustively enumerates all9-edge subsets, tests connectivity/acyclicity, and roots each tree at all10 vertices. Its bit-mask coverage is exact.

Define the positive clearing factor

    Q(a)=20000(a-5)^2(a-4)^2(a+5)^2(2a+5)^2(3a+5)^2 N(a).

Every matrix R_ij=Q H_ij is a rational-coefficient polynomial of degree at most17. Their degree17 Bernstein coefficient matrices have the common integer scale1343519457280. The source derives these coefficients exactly from the actual tetrahedral centroid; it does not fit them to evaluations.

For each rooted tree and every parameter, the certificate supplies positive integer weights on a subset of its arrows such that

    -sum w_ij H_ij >= 2^(-26) (sum w_ij) I.       (A)

To prove this, all18 Bernstein coefficient matrices of -sum w_ij R_ij are checked positive definite after subtracting

    2^(-26) (sum w_ij) max_Bernstein(Q) I,
    max_Bernstein(Q)=506018631541267125/14.

The exact checks are the three Sylvester leading-minor inequalities of a symmetric3x3 rational matrix. Integer arithmetic clears the remaining denominators. The maximum Bernstein coefficient bounds Q from above, and Q is strictly positive, so the matrix polynomial checks imply(A) on the entire interval.

Coverage is a complete three-node exact de Casteljau tree:

    interval[0,1]:314 stresses cover4459 rooted trees,41951 remain;
    interval[0,1/2]:2067 further stresses cover every remaining tree;
    interval[1/2,1]:3410 further stresses cover every remaining tree.

There are5791 stresses and104238 coefficient-matrix checks. The two children inherit the already-covered parent trees. Each child array has an extra exact2^17 scaling, accounted for by the verifier. The numerical discovery made5792 stress requests; an unsuccessful parent request caused the single subdivision and is not evidence for a feasible rooted system.

Taking the trace of(A) against any nonzero positive semidefinite M contradicts simultaneous nonnegative values of every selected arrow. Thus no weak rooted system exists even for nonzero singular PSD matrices. For actual positive definite metrics the rooted-tree implication proves U>=2. The singular statement is an algebraic rooted-system exclusion, not a claim that a degenerate physical metric has ordinary strict unstable equilibria.

Since arbitrary positive definite M are included, the assertion holds after every nonsingular affine map of each actual body, with uniform refilling and the affine image of its own centroid. No independent inverse metric is chosen.

## 4. An explicit same-incidence actual-refill collar

Let eta=2^(-53). Suppose a convex ten-labelled-vertex body has the same literal cycles and the seven listed positive actual tetrahedra form its triangulation, and in the normalized coordinates

    max_i ||Ztilde_i-Z_i||<=eta.

Recompute its uniform centroid gtilde from its actual volume. Then every stress used above retains normalized margin at least2^(-27), so this body also has U>=2 for every positive definite metric.

Here is a uniform proof, including the own-centroid change. Old vertex radius R=5 gives edge-vector norm<=2R. A displacement at most eta changes each edge vector by at most2eta. By determinant multilinearity, a tetrahedron's six-volume changes in absolute value by at most

    24 R^2 eta+24 R eta^2+8 eta^3.

Summing seven and using eta<=1 gives at most5096eta. Since D>1/16, the new six-volume exceeds1/32. Each tetrahedral centroid changes by at most eta, and each old tetrahedral centroid differs from g by at most10. Therefore

    ||gtilde-g||<=eta+10*5096eta*32
                  =1630721eta<2^21 eta.

The centred vertex displacement is less than2^22eta; the edge displacement is at most2eta. Consequently

    ||Htilde_ij-H_ij||
      <=10*2^22eta+20eta+2^23eta^2
      <2^26eta=2^(-27).

For a convex combination of the arrow matrices the same perturbation bound holds independently of the number or size of the positive integer weights. Subtract it from2^(-26) in(A). This explicitly controls the actual-refill centre rather than fixing a geometric origin by fiat.

## 5. A complete eleven-dimensional tube, with each entire maximal pencil

The transverse independent parameters are

    theta=(beta,p0,p1,p2,q0,q1,q2,u0,u1,s),
    u2=1-u0-u1.

Let theta0 be the fixed tuple in Section1 and delta=2^(-68). For EVERY theta satisfying ||theta-theta0||_infinity<=delta, and EVERY0<t<1, define

    a_theta(t)=-(1-t)/s+t(1+1/q2).

Then the corresponding true10/17/9 actual body satisfies U>=2 under EVERY positive definite metric. This covers the entire maximal admissible pencil of each theta, not a fixed truncated a interval. It is an eleven-dimensional positive-volume parameter domain. It is nevertheless a small transverse tube, not the whole chart.

Proof. Work first on the much larger guard box delta<=1/100. There s in[.79,.81],q2 in[.49,.51],u2 in[.38,.42],beta in[.39,.41]. All p,q,u remain positive; s remains the largest left coefficient and q2 the largest right coefficient. The stack excess9/25 changes by less than4delta, so remains positive. Thus the chart and all nine true facets persist throughout the open a pencil.

For the normalization T_theta,a of Section2, K=s+q2u2 is between9/10 and11/10, and0<y_s<1/5. On the closed t interval, |a|<4,|1-a|<3,d_s<7/2,e2<11/5. The vertices S,R2 are exactly fixed at(1,0,0),(0,1,0), including by cancellation at the endpoints.

Every other vertex has an uncancelled denominator h equal to1, a d_i, or an e_i with i=0,1. All such h satisfy1/5<h<4; therefore Kh>1/8. Compare theta to theta0 at the SAME t, using Delta for differences. Direct reciprocal bounds give

    |Delta a|<5delta, |Delta d_s|<8delta, |Delta e2|<8delta,
    |Delta K|<3delta, |Delta y_s|<3delta, |Delta h|<7delta.

For each remaining raw numerator(x0,y0,z0), write

    A=q2 z0-x0, B=s z0+u2 x0,
    Z=(d_s A,e2 B,K y0-y_s A)/(K h).

Here |A|,|B|<2, |Delta A|<=2delta and |Delta B|<4delta. The three numerator changes are respectively less than24delta,25delta,11delta, so their Euclidean norm is less than60delta. The numerator norm is less than16, and the denominator changes by less than20delta. Both old and new denominators exceed1/8. Hence

    ||Delta Z|| < (60*8+16*20*64)delta
                 =20960delta<2^15delta=eta.

The actual seven-positive-tetrahedron triangulation is inherited from the full chart theorem for every such theta. Apply the collar of Section4. All the displayed coarse rational guards are also checked in the executable; the comparison and centroid arguments are the analytical part of the proof.

## 6. What changed and what failed

The previous whole-chart geometry result provided only endpoint tails of arbitrary fixed pencils and regular ghost sections with retained incidence. The present calculation closes a specific full maximal pencil, with no missing middle, and derives a uniform physical margin and explicit all-pencil transverse tube. It does not turn the prior endpoint theorem into uniform coverage of all eleven parameters.

A restricted discovery attempt using only diagonally dominant common coefficient matrices failed to finish after a dyadic depth9 subdivision:1023 nodes and512 unclosed leaves. Those leaves were not feasible physical survivors. Allowing the actual3x3 positive definite cone through eigenvector cutting planes produced the complete three-node cover above. Increasing subdivisions in the smaller cone was not the decisive change. The durable source contains the complete successful DD-first/eigenvector-cut fallback mechanism with its exact acceptance check; the failed DD-only run contributes no mathematical exclusion or counterexample.

Uniformly stronger mixed whole-facet moment theorems were obtained independently in minimum-0287. They are not used to certify this pencil and are not being silently converted to an equilibrium census. The next concrete geometric opportunities are larger independent transverse parameter domains, or a structural proof controlling the entire cut-stack chart. Every result here leaves the global lower bound34 and canonical attainingC622 unchanged.

## 7. Observed reproducibility and exact output pins

Executed environment: CPython3.13.5, SymPy1.14.0, NumPy2.3.5, SciPy1.17.0, OPENBLAS_NUM_THREADS=1, assertions enabled. The script itself forces this thread variable before importing NumPy. All actual coordinates and every nondefault search parameter are literal. There is no random seed because the algorithm uses no randomness. HiGHS is used only for coefficient discovery. The verify mode does not call a numerical optimizer; its matrix and combinatorial acceptance arithmetic is exact.

A source-only build reconstructed all coefficients, enumerated the trees, discovered all5791 integer stresses and passed the exact continuum verification. A separate verify invocation passed on the resulting certificate, including the explicit collar and tube arithmetic. The completed prototype and the standalone build produced the same stress-certificate bytes on this environment. Floating discovery can differ on a different numerical stack; byte identity there is not promised. Any accepted reconstruction must still pass the exact checker, and the pins below identify the observed object rather than replacing its generator.

    pencil_certificate.py:16437bytes
    b1e887ff04f59652ee400a9988d813ea63a5cc71859755d38086c0f6ca74f7b1

    pencil_stresses.json:466583bytes
    3028b4c589d08167a9c27d28158ca399b7a7cd745e2fb45eb7d607c6c1ae6de2

    pencil_verification.json:896bytes
    104cc2ba00822df5f133923b3c52b299075fef523e3a3c3706e97a3d0fab167a

The466583-byte integer certificate is deterministically regenerated from the complete16437-byte source and its literal inputs. It is not being claimed to be separately stored as a Pro material. No old sandbox file, hidden pickle, tree array or input checkpoint is required by the capsule.

## 8. Exact recovery patch, reconstruction and verification commands

Save the exact Part2 material bytes as pencil_source_input.txt. Save the following COMPLETE recovery program as recover_pencil.py. It applies the sole transport correction, checks the executed-source hash, and refuses to overwrite a different existing source.

```python
from pathlib import Path
import hashlib

raw = Path('pencil_source_input.txt').read_bytes()
assert len(raw) == 16434
assert hashlib.sha256(raw).hexdigest() == 'b36cdea35fb1834d680e4459c3c8163c69a9ca27d96ae422cfe14b18ec7eed1b'
old = b'            visit(right,mid,hi,pending,depth+1)'
new = b'            visit(right,middle,hi,pending,depth+1)'
assert raw.count(old) == 1
out = raw.replace(old, new)
assert len(out) == 16437
assert hashlib.sha256(out).hexdigest() == 'b1e887ff04f59652ee400a9988d813ea63a5cc71859755d38086c0f6ca74f7b1'
target = Path('pencil_certificate.py')
if target.exists() and target.read_bytes() != out:
    raise FileExistsError(str(target))
target.write_bytes(out)
print('FULL_CUT_STACK_PENCIL_SOURCE_RECOVERY_PASS')
```

Run:

```sh
python -B -S recover_pencil.py
OPENBLAS_NUM_THREADS=1 python -B pencil_certificate.py build
OPENBLAS_NUM_THREADS=1 python -B pencil_certificate.py verify
sha256sum pencil_certificate.py pencil_stresses.json pencil_verification.json
```

Expected recovery marker:

    FULL_CUT_STACK_PENCIL_SOURCE_RECOVERY_PASS

Expected discovery coverage markers:

    DISCOVERED_NODE 0 1 314 41951
    DISCOVERED_NODE 0 1/2 2067 0
    DISCOVERED_NODE 1/2 1 3410 0

Expected successful exact terminal marker from BOTH build and verify:

    FULL_CUT_STACK_PENCIL_ALLROOT_GAMMA_TUBE_EXACT_PASS

A missing marker, failed assertion, uncovered leaf or different unchecked output is not a proved cover. The complete source input plus this literal recovery patch supplies every byte required to reconstruct the executed computation.
