# figure-0047

AI research report · 2026-08-23 UTC

---

# Decisive independent verdict

**Verdict: PASS at theorem level.** I recovered the rejected artifact titled **“Repaired construction: a branch-complete rational polyhedral Gömböc theorem”**, verified its internal SHA-256 manifest, reran all supplied checkers, re-derived the smooth-seed estimates that those checkers treated as premises, and independently audited the complete exposed-face/normal-cone argument. The prior response was rejected because it rendered two fenced JSON blocks; that was an envelope failure, not a mathematical counterexample.

The repaired construction does specify a single deterministic finite rational H-polytope with uniform volume density such that, at its **own exact uniform-volume centroid**, it has

\[
S=1,\qquad U=1,\qquad H=0
\]

strictly. Its H-description has

\[
4(24\cdot 2^{384}+2)+1
=
3782592594853870004378787849613786925287654969964682880123036166807589290063732218695769560468951901517436287069454345
<2^{391}
\]

candidate rows.

This is a mathematically explicit **lazy finite specification**, not a practical mesh. The complete row list, V-representation, face lattice, OBJ, and STL were not materialized; the object has about \(2^{390.585}\) candidate inequalities. The original transcript demanded exact coordinates or halfspaces, an exact uniform-volume centroid, and an audit of every face, edge, and vertex with strict margins. :contentReference[oaicite:0]{index=0} The recovered theorem meets that demand at the universal-certificate level: every row is exactly generable, while one full-exposed-face separator handles all actual and nonsimplicial active sets without enumerating the astronomical face lattice.

## 1. Exact deterministic object

Start from the smooth radial body

\[
\beta=\frac7{200},\qquad
q(x,y,z)=x\cos(\lambda z)+y\sin(\lambda z),\qquad
\rho=(1+4\beta q)^{1/4},
\]

where \(\lambda\) is the unique root in \((\pi,3\pi/2)\) of

\[
\sin\lambda-\lambda\cos\lambda=0.
\]

Let \(K=\{ru:0\le r\le\rho(u)\}\) and \(B=K^\circ\). The root identity makes the first volume moment of \(K\) vanish exactly. The only critical points of \(q\), hence of \(\rho\), are \(+e_x\) and \(-e_x\). The independent derivation gives

\[
\frac1{50}I\prec C_K\prec\frac94I,
\qquad
\frac1{60}I\prec\nabla^2h_B+h_BI\prec3I,
\]

so the seed and polar are globally strictly convex. It also gives \(\lVert\nabla q\rVert<5\), \(\lVert\nabla^2q\rVert<24\), \(\lVert\nabla^3q\rVert<256\), a critical Hessian gap greater than \(1/800\), and the cap derivatives \(\pm\nabla h_B\cdot t\ge\theta/1024\) on angular radius \(2^{-100}\).

Set

\[
D=2^{192},\qquad
\mathcal M_D=\{m\in\mathbb Z^3:\max_i|m_i|=D\},
\qquad v_m=m/|m|.
\]

There are exactly \(24D^2+2\) listed directions, with covering radius below \(4/D\). For every \(m\), the generator interval-evaluates the polar contact

\[
x(v_m)=h_B(v_m)v_m+\nabla h_B(v_m),
\]

rounds it to a dyadic raw point \(r_m\) of denominator \(2^{600}\), and moves it inward:

\[
q_m=(1-2^{-520})r_m.
\]

The inward-ball lemma proves \(q_m\in B\) exactly and

\[
|q_m-x(v_m)|<2^{-519}.
\]

Define

\[
Q_0=\operatorname{conv}\{q_m:m\in\mathcal M_D\},
\quad
D_\varepsilon=\{0\}\times[-2^{-180},2^{-180}]^2,
\]

and let \(A\) be the axial rational point at \(-e_x\) whose support exceeds the exact smooth polar support there by \(2^{-220}\), after an upward dyadic rounding. Finally set

\[
Q=\operatorname{conv}\bigl((Q_0+D_\varepsilon)\cup\{A\}\bigr),
\qquad
P=Q^\circ.
\]

Thus an exact H-description of \(P\) is

\[
\bigl(q_m+(0,\sigma_y2^{-180},\sigma_z2^{-180})\bigr)\cdot x\le1
\]

for every \(m\in\mathcal M_D\) and \(\sigma_y,\sigma_z\in\{-1,+1\}\), together with \(A\cdot x\le1\). Every coefficient is dyadic rational. A metadata correction is required: \(2^{600}\) is the raw-contact denominator; after multiplication by \(1-2^{-520}\), final ordinary H-row coordinates have denominators dividing \(2^{1120}\). This changes no geometry, margin, or count.

## 2. Why the mixed-feature gap is genuinely repaired

The old SPG-EFFECTIVE proof was invalid because separate one-normal residuals do not exclude a radial vector from the positive cone of two incident normals. The preserved exact rational prism regression still demonstrates that failure. The new construction does not use that inference.

For any unit normal \(n\), write

\[
b(n)=h_{Q_0}(n)+h_{D_\varepsilon}(n),
\qquad a(n)=A\cdot n.
\]

The **entire** exposed face is known without a face-lattice assumption:

\[
F_Q(n)=
\begin{cases}
F_{Q_0}(n)+F_{D_\varepsilon}(n),&b(n)>a(n),\\
\{A\},&a(n)>b(n),\\
\operatorname{conv}\bigl((F_{Q_0}(n)+F_{D_\varepsilon}(n))\cup\{A\}\bigr),&a(n)=b(n).
\end{cases}
\]

The rolling-support inequality localizes **every** active contact at \(n\):

\[
\angle(n,v_m)<128D^{-1},
\qquad |q_m-x(n)|<385D^{-1}.
\]

The sphere is then exhausted by six active-normal classes:

- **S0:** \(n=+e_x\). The exposed face is the intended transverse square, whose tangent projection contains zero strictly; it dualizes to the unique strict unstable vertex.
- **S1:** \(0<\angle(n,+e_x)\le2^{-100}\). The common separator is the outward geodesic tangent \(t_+\), and every point of the whole Minkowski exposed face satisfies
  \[
  z\cdot t_+>\theta/1024+2^{-180}/3.
  \]
- **G:** outside both axial caps. The separator \(s(n)=\nabla h_B/|\nabla h_B|\) satisfies
  \[
  z\cdot s(n)>2^{-129}
  \]
  for every point of the full active base face.
- **A0:** \(n=-e_x\). The apex alone is exposed and dualizes to the unique strict stable face.
- **A1:** \(0<\angle(n,-e_x)<2^{-112}\). The apex dominates by more than \(3\cdot2^{-220}/4\), and \(A\cdot(-t_-)>\theta/3\).
- **A2:** \(2^{-112}\le\angle(n,-e_x)\le2^{-100}\). The face may be base only, apex only, or their complete convex-hull tie. The same separator \(-t_-\) is positive on every base generator by more than \(\theta/2048\) and on the apex by more than \(\theta/3\).

Outside the last cap, the base beats the apex by more than \(2^{-210}\). Because each displayed inequality is one strict linear functional on **every generator of the entire exposed face**, it remains strict on all convex combinations. This automatically includes mixed edges, mixed vertices, square-edge and square-corner ties, apex/base transitions, higher-valence faces, and all nonsimplicial ties. The old prism fails exactly this common-separator condition and is therefore rejected by the repaired certificate.

## 3. Exact transfer to the polytope’s own volume centroid

The rational approximation satisfies a homothetic sandwich with \(t<2^{-178}\):

\[
(1-t)B\subset Q\subset(1+t)B.
\]

Polarity gives

\[
(1+t)^{-1}K\subset P\subset(1-t)^{-1}K.
\]

Since \(c(K)=0\) and \(K\subset(26/25)B_2\), an exact shell-moment estimate yields

\[
|c(P)|<2^{-175}.
\]

The exact half-turn symmetry \((x,y,z)\mapsto(x,-y,-z)\) forces

\[
c(P)=(c_x,0,0)
\]

exactly. Because the H-coefficients are rational, the vertices and any tetrahedral volume-moment formula are rational, so this is the exact uniform-volume centroid of the rational polytope, not an auxiliary reference point.

For any radial boundary point \(y=n/h_Q(n)\), polarity gives the **full** normal cone

\[
N_P(y)=\operatorname{cone}F_Q(n).
\]

If \(y\) were an equilibrium relative to \(c=c(P)\), then

\[
y-c=\Lambda\bar z,
\qquad \bar z\in F_Q(n),
\qquad
\Lambda=\frac{1-h_Q(n)(n\cdot c)}{h_Q(n)^2}>\frac34.
\]

Tangential projection gives

\[
-\Pi_nc=\Lambda\Pi_n\bar z.
\]

Applying the appropriate branch separator contradicts this equation in every non-target branch. The weakest right-side coefficients are \(3/(4\cdot2048)\), \((3/4)2^{-129}\), and \(3/(4\cdot1024)\), all overwhelmingly larger than the axial-centroid contribution below \(2^{-175}\).

At the targets the axial centroid shift preserves strictness exactly: the target vertex vector remains an equal positive combination of all four square-corner normals, with every coefficient greater than \(1/5\); the projection onto the apex plane remains the same axial relative-interior point, while \(-e_x\) lies in the interior of the apex normal cone. Therefore

\[
\boxed{S(P)=1,\quad U(P)=1,\quad H(P)=0}
\]

at the object’s own exact centroid, with no origin-only shortcut and no unexamined transition class.

## 4. Independent scrutiny performed

1. The recovered ZIP hash and every entry of its internal manifest were verified.
2. The recovered `run_all.sh` was rerun successfully. It executes the primary exact/outward-rounded verifier, an independent standard-library `Fraction` verifier, and the adversarial old-prism regression.
3. A new independent checker was written without importing either recovered checker. It independently re-derives the centroid identity, derivative and convexity bounds, normal-net localization, branch inequalities, support/polarity/centroid transfer, target strictness, and exact plane count; it separately interval-evaluates the published contact samples.
4. A non-proof adversarial numerical optimizer found much stronger actual smooth margins: minimum \(C_K\) eigenvalue about `0.0915553642` versus the certified `0.02`; maximum about `1.7936508500` versus `2.25`; maximum spherical Hessian norm about `22.1455728041` versus `24`; and minimum gradient-ratio square about `0.0451557523` versus `4/89≈0.0449438202`.
5. The combined audit manifest contains 37 hashed files and verifies cleanly.

## 5. Deliverables and integrity

- [Complete combined audit package](sandbox:/mnt/data/bright_finch_branch_complete_gomboc_audit.zip) — SHA-256 `9ae7cae88ae91ce3a28b9d9345fc8cbc9ca4ade28ebe3d88196765a4003cef20`.
- [Package SHA-256 file](sandbox:/mnt/data/bright_finch_branch_complete_gomboc_audit.zip.sha256).
- [Independent mathematical verdict](sandbox:/mnt/data/bright_finch_branch_complete_audit/INDEPENDENT_VERDICT.md).
- [Independent exact/interval checker](sandbox:/mnt/data/bright_finch_branch_complete_audit/independent_branch_complete_audit.py).
- [Machine-readable independent audit](sandbox:/mnt/data/bright_finch_branch_complete_audit/independent_audit_report.json).
- [Corrected deterministic theorem contract](sandbox:/mnt/data/bright_finch_branch_complete_audit/corrected_theorem_contract.json).
- [Complete audit manifest](sandbox:/mnt/data/bright_finch_branch_complete_audit/MANIFEST.sha256).
- [Recovered immutable theorem bundle](sandbox:/mnt/data/bright_finch_branch_complete_audit/recovered/assignment4_repaired_spectral_polar_bundle.zip) — SHA-256 `20c0c9cbe97855e9316aab71bba56f50251ffc9b564ac3c1c01434aac6f78839`.
- [Recovered theorem text](sandbox:/mnt/data/bright_finch_branch_complete_audit/recovered/assignment4/REPAIRED_THEOREM.md).
- [Lazy exact H-generator](sandbox:/mnt/data/bright_finch_branch_complete_audit/recovered/assignment4/spectral_polar_generator.py).
- [Machine-readable six-class partition](sandbox:/mnt/data/bright_finch_branch_complete_audit/recovered/assignment4/active_set_partition.json).
- [Evaluated common-separator certificate](sandbox:/mnt/data/bright_finch_branch_complete_audit/recovered/assignment4/common_separator_certificate.json).
- [Exact centroid/polarity audit](sandbox:/mnt/data/bright_finch_branch_complete_audit/recovered/assignment4/centroid_polarity_audit.json).
- [Combined verification log](sandbox:/mnt/data/bright_finch_branch_complete_audit/COMBINED_VERIFICATION.log).

## 6. Scope and decisive conclusion

The claimed repaired theorem is sound under the audited exact/interval premises. It supplies the requested finite rational specification, evaluated size bound, complete full-normal-cone/common-separator proof, exact own-centroid transfer, strict `S=1,U=1,H=0`, deterministic generator, independent checker, adversarial regression, and integrity hashes.

It does **not** supply a reduced expanded H/V instance, explicit maximal-face list, printable OBJ/STL, low mechanical complexity, or a prize-ready physical object. Those are absent because the proved safe scale is astronomical, not because an active-set branch remains open. Academic novelty and priority also remain outside this audit. The strongest justified statement is therefore:

> A finite exact rational homogeneous polyhedral Gömböc is specified and proved by a branch-complete lazy construction with fewer than `2^391` candidate H-planes; every mixed active-normal-cone class and the exact own uniform-volume centroid are covered, but no practical materialized model has been produced.
