# material-6e7e96d6cac7

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# MUTUAL_ALL_AGGREGATE_COFACTOR_BLIND_CONE_AND_RECIPROCAL_GAP_V1

## Scope and evidence
New coordinator mathematics: an exact limitation of mutual scalar/cofactor relaxations for one physical metric and its inverse, with a mixed-metric alternative. The rational control is a system of genuine rank-two arrow FORMS, NOT a realized convex polytope, NOT an equilibrium census, NOT an E17 body. Bounds remain 34 <= Cmin <= 622. Infinite-family conclusions are proved analytically, not sampled. This is Recovery capsule part 2/2. Part 1/2 is the complete runnable source [internal-source-reference], reciprocal_gap.py.txt, 7736 bytes, SHA256 b7092044e73448f35b53f36f404c7e57c352bef9de904dea84a811a466ffd2d1. Both parts together preserve the full result without an originating sandbox.

Scientific starting point: fully read material [internal-source-reference], actual current title RECIPROCAL_SCALAR_EXACT_ALTERNATIVE_AND_ACTUAL_BEVEL_FOUR_ARROW_CLOSURE_V1, 11874 UTF-8 bytes, SHA256 5910a8a846fc9dbab9251a0eca8b9e623d439983167c946259ebeb51fae1adce6. It proves, for symmetric A of inertia (+,--), that A:M>=0 for SPD M implies adj(A):M^-1<0. Its scalar alternative and actual bevel four-arrow box do not solve simultaneous arbitrary arrow systems. Older descriptions of that material as 9933 bytes with a different title are not the literal object read. The present proof needs only the stated cofactor implication, also immediate below at N=M^-1.

Notation: X:Y=tr(XY) for real symmetric matrices. All metrics M,N are strictly positive definite unless closure is expressly discussed. adj is the ordinary 3-by-3 adjugate. An arrow x->x+e has matrix sym(x e^T), with value x^T M e. Physical reciprocity up to a sign-irrelevant positive scale is N=alpha M^-1, alpha>0.

## 1. Exact universal blind cone
For SPD M0,N0 define S=M0^(1/2) N0 M0^(1/2), t=tr(S)=tr(M0N0), u=tr(S^2)=tr(M0N0M0N0), Delta=t^2-2u.

THEOREM. Delta>=0 iff adj(A):N0<=0 for EVERY symmetric A of inertia (+,--) with A:M0>=0. All these inequalities are strict iff Delta>0. Thus Delta>0 is an open region of independent metric pairs invisible to every such reciprocal cofactor aggregate.

Proof for M0=I. The eigenvalues of A are a,-b,-c with a,b,c>0 and a>=b+c. Let Y=-adj(A), whose eigenvalues are -bc,ac,ab. Its trace p=a(b+c)-bc is positive, and direct expansion gives

    p^2-tr(Y^2)=2abc(a-b-c)>=0.

Consequently ||Y-(p/3)I||_F<=sqrt(2/3)p. For q=tr(N)>0, subtracting scalar parts and applying Cauchy--Schwarz yields the uniform estimate

    Y:N >= (p/3)[q-sqrt(6tr(N^2)-2q^2)].                 (1)

The radical is real by tr(N^2)>=q^2/3. Delta>=0 makes the bracket nonnegative; Delta>0 makes it positive.

For sharpness order the eigenvalues of N as lambda1>=lambda2>=lambda3>0. Then

    Delta=4lambda2lambda3-(lambda1-lambda2-lambda3)^2.

In this order Delta<0 iff lambda1>(sqrt(lambda2)+sqrt(lambda3))^2. In N's eigenbasis choose b=sqrt(lambda2), c=sqrt(lambda3), a=b+c and A=diag(a,-b,-c). It has trace zero and

    adj(A):N=sqrt(lambda2lambda3)
                [lambda1-lambda2-lambda3-2sqrt(lambda2lambda3)].

This is positive outside the cone and zero on its full-rank boundary. Strict witnesses outside can also be approximated rationally. A boundary point does NOT satisfy every strict cofactor inequality.

For general M0 use Abar=M0^(1/2) A M0^(1/2), Nbar=M0^(1/2) N0 M0^(1/2). Then tr(Abar)=A:M0, inertia is preserved, and

    adj(Abar)=det(M0)M0^(-1/2)adj(A)M0^(-1/2),
    adj(Abar):Nbar=det(M0)adj(A):N0.

Apply the normalized proof. QED.

For fixed M0, the weak cone is a trace/traceless Lorentz cone, with PSD retained in closure. Its spectral description is sqrt(lambda1)<=sqrt(lambda2)+sqrt(lambda3). The strict interior Delta>0 is what is used below.

## 2. Why arbitrary mutual cofactor iterations remain incomplete
Take an independently feasible pair M0,N0 for any linear homogeneous primal and dual inequalities, with Delta(M0,N0)>0. Allow nonnegative aggregation, addition of positive-semidefinite trivial inequalities, valid semidefinite domination consequences, and the transfer in either direction

    A:M>=0, inertia(A)=(+,--)  ==>  (-adj(A)):N>0,

or the reversed rule from dual B to primal -adj(B).

The SAME pair M0,N0 satisfies every generated inequality, for every finite number of such operations, and all valid weak limits. Every aggregate A remains nonnegative at M0; Theorem 1 gives strict positivity of its transferred cut at N0. In the reverse direction N0^(1/2)M0N0^(1/2) has the same eigenvalues as S and the same Delta, so the argument repeats. Aggregation and valid domination preserve feasibility. A zero limiting form cannot legitimately be required strictly positive.

This proves a limitation of this precise inference hierarchy, including ALL its aggregates in BOTH directions, not of arbitrary mixed M,N equations, actual primal-dual incidence, actual facet moments, or direct MN=alpha I. Such genuinely mixed conditions can escape the blind cone.

## 3. Exact strict rank-two arrow-form control
Let epsilon=1/20 and ei be the standard basis. For each i<j impose FOUR weak primal arrows, twelve total:

    source ei, displacement epsilon ei + ej;
    source ei, displacement epsilon ei - ej;
    source ei+ej, displacement epsilon(ei+ej)+(ei-ej);
    source ei+ej, displacement epsilon(ei+ej)-(ei-ej).

Each corresponding symmetric form has rank two and inertia (+,-,0). M0=I satisfies all strictly with values epsilon or 2epsilon. Equivalently,

    |Mij|<=epsilon Mii,
    |Mii-Mjj|<=epsilon(Mii+Mjj+2Mij).

Normalize tr(M)=3, allowed by homogeneity. Then |Mij|<=3epsilon, every diagonal difference is <=3epsilon(1+2epsilon), and |Mii-1|<=2epsilon(1+2epsilon). Gershgorin therefore gives for EVERY feasible SPD M

    1-8epsilon-4epsilon^2 <= lambda(M) <= 1+8epsilon+4epsilon^2,
    namely 59/100 <= lambda(M) <= 141/100.                 (2)

The dual arrow q=(1,0,2)->r=(2,0,0) has matrix

    B=sym(q(r-q)^T)=diag(1,0,-4).

By (2), every reciprocal candidate satisfies

    B:M^-1=(M^-1)11-4(M^-1)33
       <=100/59-400/141=-9500/8319<0.                     (3)

Thus no N=alpha M^-1, alpha>0, can satisfy the weak dual arrow together with the twelve weak primal arrows.

But the independent SPD N0=diag(1,1,1/10) strictly satisfies B:N0=3/5. At I,N0 the exact quantities are

    t=21/10, u=201/100, Delta=39/100>0,
    R=3u-t^2=81/50, rho=R/t^2=18/49.

Theorem 2 therefore says ALL aggregates and mutual cofactor iterations retain this nonreciprocal pair. In (1) the radical is 9/5, giving the stronger uniform bound

    (-adj(A)):N0 >= (1/10)tr(-adj(A))>0

for every eligible aggregate. This controls an infinite continuum, not a finite numerical list.

These are literal rational arrow FORMS, but their sources and targets are NOT claimed to form true edges of one actual convex body and its polar. There is no volume, own COM, actual facet lattice or mechanical census for this formal control. It is a countercontrol to a relaxation, not a counterexample to any lower bound.

## 4. Mixed reciprocal defect and a usable quantitative alternative
For SPD M,N put

    R(M,N)=3tr(MNMN)-(tr(MN))^2.

S=M^(1/2)NM^(1/2) is symmetric positive definite and similar to MN. For its eigenvalues mui,

    R=sum_{i<j}(mui-muj)^2
     =3||S-(tr(S)/3)I||_F^2>=0.                          (4)

Thus R=0 iff N=alpha M^-1, alpha=tr(MN)/3>0. The single homogeneous quartic inequality R<=0 plus SPD enforces reciprocity up to sign-irrelevant scale; imposing tr(MN)=3 gives the literal inverse. This is jointly nonconvex, though convex quadratic in either matrix block with the other fixed. No claim that it is computationally easier than MN=I is made. SPD matters: singular M=diag(1,0,0),N=diag(0,1,0) gives R=0,MN=0 without an inverse.

The blind cone Delta>0 is equivalent to rho=R/(tr(MN))^2<1/2. True reciprocity is rho=0; the strict control has rho=18/49>0 inside the same blind cone. Cofactor feasibility does not therefore imply even asymptotic reciprocity.

Let alpha=tr(MN)/3. Then

    ||N-alpha M^-1||_F <=sqrt(R/3)/lambda_min(M).

For a symmetric arrow form B set C=M^(-1/2)BM^(-1/2). Pairing the two traceless parts gives the sharper directional estimate

    |B:N-alpha tr(C)|
      <=sqrt((R/3)[tr(C^2)-(tr(C))^2/3]).                 (5)

This can turn a rigorously small mixed defect into sign preservation once actual geometry, actual centering and strict margins have separately been supplied. It does not supply those missing physical facts.

For fixed M, if tr(C)<0 while B:N>=0, (5) implies

    rho >= (tr(C))^2/[3tr(C^2)-(tr(C))^2].                (6)

If the denominator is zero, C is a negative scalar and no SPD N satisfies that halfspace. A positive uniform version of (6) over an ACTUAL primal feasible region would exclude its reciprocal metrics through genuine mixed coupling rather than another scalar cofactor cut.

Sharpness at fixed M: for M=I,B=diag(1,0,-4), tr(B)=-3, tr(B^2)=17. Formula (6) yields rho>=3/14. The SPD matrix

    Nstar=diag(10/7,17/14,5/14)=I+(3/14)(B+I)

has trace three, B:Nstar=0, rho=3/14 and Delta=12/7>0. Hence the weak-halfspace minimum is attained strictly inside the cofactor blind cone. N0 instead gives a strictly positive dual arrow. No complete E17 realization class has yet been closed by applying this defect method.

## 5. Source-only reconstruction and exact observed pins
Both capsule parts are required for the full mathematical result. For computation alone save part 1 [internal-source-reference] verbatim as reciprocal_gap.py, retaining its final newline. It contains every input and parameter and needs no other file, RNG or package.

Executed environment: CPython 3.13.5 standard library, assertions enabled.

    python -B -S reciprocal_gap.py build > build.stdout
    python -B -S reciprocal_gap.py check > check.stdout
    cmp build.stdout check.stdout

Observed inputs/outputs:
- reciprocal_gap.py: 7736 bytes, SHA256 b7092044e73448f35b53f36f404c7e57c352bef9de904dea84a811a466ffd2d1.
- reciprocal_gap.json: 7766 bytes, SHA256 7dd6c0bda600482c6ac92c536b11e4bbbe67df2235097e13d9547bd5aafe1a72.
- build.stdout and identical check.stdout: 389 bytes, SHA256 4271c3883c86e7414ceb9428ea0ead6d9173f672f99d919bd7386851c0295141.

Exact terminal output:

    ALL_THREE_POLYNOMIAL_IDENTITIES_PASS

[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]

    reciprocal_gap.json 7766 7dd6c0bda600482c6ac92c536b11e4bbbe67df2235097e13d9547bd5aafe1a72

The exact source checks three polynomial identities, all thirteen rank-two rational arrow matrices, spectral bounds, reciprocal-gap constants, strict independent feasibility and the sharp fixed-M floor. It does not pretend to enumerate the continuum or the infinite hierarchy; those are addressed by the complete proofs above. Transient scratch pins claiming source8377B/output11321B were not the actually executed files and are superseded by this complete literal capsule and the observed pins. No uncertainty about a scratch filename is promoted into a mathematical discrepancy.

## Next useful mathematical frontier
Use true mixed reciprocity, actual volume/facet moments and true incidence to leave the blind cone. A promising target is a positive uniform reciprocal-defect floor on a genuine E17 shape sector after actual S1/U1 constraints, or a direct mixed identity strengthening facet-energy bounds. Merely generating more scalar cofactor cuts cannot by itself defeat the explicit strict control. A geometric realization of a comparable obstruction remains a distinct, unproved task.
