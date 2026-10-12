# figure-0307

AI research report · 2026-09-04 UTC

---

# Steady Lynx 98 — a materialized quadratic-algebraic homogeneous polyhedral Gömböc

## Verdict and exact object

**A finite object passed the requested strict own-centroid `(S,U,H)=(1,1,0)` gate.** Its name here is `L98_RH222935_Q`. It has

\[
(V,E,F)=(222935,668674,445741),\qquad C=1337348.
\]

This is a large, fully expanded polyhedron, not a low-complexity construction, an unexpanded approximation prescription, or a smooth-body claim. There are 445,740 triangular maximal faces and one 128-gonal maximal face. Its display triangulation has 445,866 triangles and 125 additional, nonphysical cap diagonals.

The exact coefficient/triangulation file is `L98_exact.txt`, SHA-256

`c1865ec183618e2d35ef7cb3ecaf91ba84390dfea569f2555f92ce6b60d6d54b`.

Its first line is `222935 445866 281474976710656`. The next 222,935 rows are integer quadruples `(Nx_i,Ny_i,Nz_i,B_i)`; the remaining 445,866 rows are outward-oriented, zero-based vertex triples. Put `D=2^48=281474976710656`. The **exact physical coordinates** are

\[
p_i(\lambda)=D^{-1}(Nx_i-\lambda B_i,Ny_i,Nz_i).
\]

No subsequent translation, point masses, surface-centroid substitution, or change of density is involved.

Define the primitive integer polynomial `P(lambda)=a0+a1*lambda+a2*lambda^2` by

```text
a0 = 32197784347459092787648934050106531825927025214512867
a1 = -111500276126685181863588709076092098786828548533367252185042
a2 = -5623297103141422125921343398227599504408859436091215068
```

Use its unique root in the following **rational isolating interval**:

```text
L = 383839375497491445993980015631
H = 383839375497491445993980015632
Q = 1329227995784915872903807060280344576 = 2^120
L/Q < lambda < H/Q
```

The endpoint polynomial signs are opposite, the derivative is strictly negative there, and the discriminant is not a perfect square. Thus this is a genuine isolated quadratic-algebraic parameter, not a rounded transcendental root. Numerically,

`lambda = 0.000000288768651213091812785511677271486762587830803475664...`.

The exact ordinary volume and first moments, independently recomputed from the actual oriented boundary, are

\[
V(\lambda)=\frac{560289597993512939716335986465207112914777530
+20203290451698989453873510380554226560694\lambda}{6D^3}>4,
\]

\[
M_x(\lambda)=\frac{P(\lambda)}{12D^4},\qquad M_y(\lambda)=M_z(\lambda)=0.
\]

Both coefficients of each transverse moment polynomial are literally zero integers. Consequently the root makes the body's **own uniform-volume centroid exactly `(0,0,0)`**. Its volume is approximately `4.1873757506861550588053581841777278116`.

The unique stable maximal face has exported face ID **445740** and the oriented cycle

`[0,2,4,...,126,127,125,123,...,1]`.

It lies on `x=-275789182181101/D`; its stable foot is `(-275789182181101/D,0,0)`. The unique unstable vertex is **222934**, exactly `(287160771240211/D,0,0)`. There are no saddle true edges. In verifier output, `S_TRI_REP 1` denotes a triangle representing the entire merged 128-gon, not a separate triangular stable face.

## Construction and the consequential repair

The starting analytic geometry was the journal's new circular-section phase with `epsilon=1/50`, `eta=(3*pi/2)*(z-z^3/3)`, and `P=eta-(41/100)sin(2eta)-(9/200)sin(4eta)`. The journal separates that smooth result from a finite polyhedron and supplies the radial-height identity and the one-axis quadratic moment mechanism. I used those as construction guidance, not as a substitute for a finite hull or equilibrium certificate. I did not independently rerun its 4096-cell smooth-curvature certificate; **the finite proof below does not depend on that certificate being correct**.

An initial radial-level mesh and a globally integrated gradient-trajectory mesh were not adequate. The `1600 x 256` radial-level experiment retained numerical class `(4941,6613,11552)` after centring. The global trajectory experiment suffered severe trajectory bunching and was rejected as a reliable discretization. These were exploratory floating-point experiments, not exact nonexistence results.

The successful replacement is a **non-layered, radial/Gauss-map, whole-feature adaptive mesh**. Start with 20,000 C2-paired circular-seed samples, add a 128-point stable cut at numerical `x=-.9798`, and add the apex at numerical `(1.0202,0,0)`. At each actual rebuilt hull, insert radial points opposite unwanted stable facets, Gauss-support points opposite unwanted unstable vertices, and both kinds of points at unwanted edge projection directions. Re-solve the actual fixed-cell quadratic moment equation while rebuilding the hull. This handles phase shear through the actual support map rather than assuming that untwisted level-ring diagonals are correct.

The supplied builder specifies every sample, bisection, insertion, symmetry operation and rounding decision. The floating-point input counts along the successful part were

```text
196129 -> 210541 -> 217711 -> 220819 -> 222235 -> 222619
       -> 222781 -> 222871 -> 222895 -> 222919 -> 222931 -> 222937
classes:
(2579,2227,4804) -> (1287,1105,2390) -> (537,501,1036)
-> (253,221,472) -> (65,65,128) -> (31,25,54)
-> (17,15,30) -> (7,3,8) -> (5,5,8) -> (3,3,4)
-> (1,3,2) -> (1,1,0).
```

Two supplied points are interior and are discarded, leaving exactly 222,935 actual vertices. This trace is numerical discovery evidence only. Acceptance came afterwards.

The remote weights are the exact dyadic `B_i/D` stored in the file, generated from the journal's even bump `b=0` for `|z|<=1/4`, and otherwise `b=16t^2(1-t)^2`, `t=(|z|-1/4)/(3/4)`. They are rational approximations to that smooth bump, not silently identified with an unevaluated analytic integral. Their exact C2 pairing and bounds `0<=B_i<=D` are checked. The resulting finite moment polynomial is computed from these actual weights.

**The first rounded Qhull proposal was not an exact hull.** Ten near-coplanar diagonals had the wrong strict orientation. Its purported transverse moments were small but nonzero exact integers; symmetry of the point cloud alone did not make that erroneous triangulated boundary valid. Ten explicit exact diagonal repairs, included in the reconstruction code, fix this. No vertices are removed by the repair. After it, both transverse moment polynomials become identically zero and every actual hull predicate passes. Treating the pre-repair numerical `(1,1,0)` audit as a completion would have been incorrect.

The finite centring motion genuinely leaves both critical patches alone. The complete vertex-star union of the stable 128-gon has 640 vertices; that of the unstable apex has 317. These are disjoint, giving **957 frozen critical-star vertices**, all with `B_i=0`. Their largest `|z|` values are approximately `.02040595` and `.02032288`, far inside the protected slab. This includes the transition stars, not only the stable face and apex themselves. The final root also satisfies `0<lambda<1/20000` exactly, although no inheritance from the smooth no-birth bound is needed for the finite audit.

## Exhaustive hull, centroid and equilibrium evidence

Four checks agree on the exact object.

**Integer-only verifier.** The complete standard-library Python verifier reproduced the moment coefficients and root interval, validated the actual incidence sphere and convexity, and audited every stable-face, unstable-vertex and four-component true-edge condition. It uses no floating-point geometry, Qhull, numerical centroid, or interval package. Its clean run ended in `PYTHON_INTEGER_ONLY_ALL_CHECKS_PASS`.

**GMP verifier.** A separate C++/GMP implementation evaluates exact polynomial signs on the same rational root interval. It agrees with Python on all **2,674,696 strict true-edge primitives**, including both directed vertex supports and both incident-face/cone numerators per edge. The complete 668,674-row sign ledger has SHA-256

`82a7067af1031a5aadceecd24e60b69aa2a9b0030e33d75ceefffc96d44fbf66`.

**Outward-interval geometric verifier.** A different implementation uses outward-rounded long-double interval cross products, in-face inequalities and full projected edge cones. It returns `(1,1,0)` with zero undecided face, vertex or edge primitives. It does not infer the edge result from Euler's identity.

**Independent global H/V incidence audit.** The global checker covers all **99,371,269,835 maximal-face/vertex pairs**. Directed bounding boxes certify 98,868,526,309 strict nonincidences; 502,743,526 remaining pairs are evaluated individually by exact integer affine predicates. The audit finds exactly 1,337,348 incidences and **zero failures or additional coplanar vertices**. There are 409,276,447 visited tree nodes. Its conservatively computed minimum normalized nonincidence lower bound is about `1.91499e-17`; an explicit `>2^-160` floor is also asserted. This is an exhaustive bound-tree proof, not sampling or a tolerance-based plane merger.

All maximal faces and true edges are materialized. The cap's 125 triangulation diagonals are merged by literal zero determinant identities and excluded from the edge ledger. Every other dihedral has a strict sign. Thus the reported counts concern maximal faces and true edges, not the arbitrary display triangulation.

The exact sign certificates assert, uniformly on the root interval, the following conservative physical-coordinate floors:

```text
|directed vertex support|                    > 2^-44
|face-foot / edge-cone numerator|            > 2^-154
positive origin-face determinant            > 2^-160
|nonflat adjacent-face determinant|          > 2^-160
|generic-ray cone determinant|               > 2^-160
|24*Mx at either root-bracket endpoint|      > 2^-160
ordinary volume                             > 4
```

The tiny raw cone floor reflects unnormalized normals of small triangles; it is not a claimed fabrication tolerance. Floating diagnostics, kept separate from the certificate, give stable-cap in-face margin about `1.96145e-5`, unstable-apex minimum directed support about `4.07947e-4`, closest excluded-vertex support about `-1.61171e-11`, and closest excluded-face margin about `-7.14965e-11` in the numerical audit's respective normalizations.

## Why the certificate proves the complete finite statement

For an outward face plane `n_f dot x=h_f`, let

`A(v,w)=p_v dot (p_v-p_w)`

and for adjacent maximal faces `f,g`, let

`B(f,g)=h_g*(n_f dot n_f)-h_f*(n_f dot n_g)`.

The orthogonal foot on face `f` obeys its edge inequality against `g` exactly when `B(f,g)>0`. Accordingly, face `f` is stable precisely when all its perimeter values are positive. A vertex is unstable precisely when all its outgoing true-edge values `A(v,w)` are positive.

For edge `(v,w)` with incident faces `f,g`, the two segment-parameter numerators are `A(v,w)` and `A(w,v)`. Their sum is the positive squared edge length. The two normal-cone coefficient numerators are `B(f,g)` and `B(g,f)`, with positive Gram determinant denominator. **A saddle exists on that edge if and only if all four are positive.** The check evaluates all four on every true edge. None is zero and no edge has all four positive.

Coordinates are affine in lambda. The vertex predicates have degree at most two and the `B` predicates degree at most three. For an integer polynomial `q(t)=sum(c_k*t^k)`, the integer-only verifier evaluates

`E = Q^3*q(L/Q)`

and bounds its possible change on `[L/Q,H/Q]` by

`R = (H-L)*(|c1|*Q^2 + 2*|c2|*H*Q + 3*|c3|*H^2)`.

It asserts `|E|>R` and the stated margin floor. Therefore every reported sign is valid at the exact quadratic root, without evaluating a floating approximation to that root.

For completeness, the integer-only local hull certificate has a global argument; it is not an unsupported local-to-global mechanics inference. The checked triangles form a connected, oriented, closed triangulated sphere, with a single cyclic link at every vertex. Every origin determinant is positive. Radial projection therefore maps each triangle orientation-preservingly onto its spherical cone triangle and has no fold across an edge. At each vertex the link winds a positive integral number of times. An exhaustive exact cone-membership count gives exactly one preimage of the generic ray `(1,2,3)`, and no zero ray predicate. Hence the radial map has degree one, all local winding numbers equal one, and its cones form a genuine complete fan.

On each cone define the homogeneous linear function `g(x)=n_f dot x/h_f`. The functions agree on shared cone boundaries. The checked nonpositive opposite-vertex determinant says that the derivative of `g` cannot decrease on crossing such a boundary. Along every generic line, `g` is consequently convex; continuity extends this to all lines. Thus `{g<=1}` is a bounded convex polyhedron with the asserted boundary. Exact coplanarity components are its maximal faces, and the check that every listed vertex belongs to at least three distinct maximal faces excludes redundant edge/face points. The separate all-pairs audit additionally verifies the global supporting inequalities directly, so the result does not depend solely on this fan argument.

Finally, the exact signed-tetrahedron formulas are `V=sum det(a,b,c)/6` and `M=sum det(a,b,c)*(a+b+c)/24`. The proven convex boundary surrounds the origin, so these are the ordinary three-dimensional volume and first moments of the actual homogeneous solid. The isolated root and zero transverse polynomials give its own centroid, not a selected reference centre.

## A nonzero preserving neighbourhood

An explicit conservative open family is available. Freeze the 957 critical-star vertices, keep every `B_i/D` fixed, and perturb the remaining source coordinates in exact C2 pairs by at most **`delta=2^-200` per coordinate**. Re-solve the quadratic first-moment equation. The new root remains inside the same rational interval, the actual lattice remains fixed, and the strict class remains `(1,1,0)`.

Here is a reproducible bound rather than an unverified numerical box claim. All original coordinates have absolute value below two. A source-coordinate change of size delta changes an adjacent-face determinant by less than `2^11*delta`, and a directed vertex support by less than `2^5*delta`. Using edge components bounded by four, normal components by 32 and support values by 192, the two products defining `B` change by less than `2^25*delta`; allowing an extra factor two is still far below `2^-154`. The origin and ray signs retain their `2^-160` floors. The flat cap and critical patches are frozen identically.

For the moment equation, each summand `det(a,b,c)*(a_x+b_x+c_x)` changes by less than `1602*delta`. There are fewer than `2^19` summands, so the complete `24*Mx` change is below `2^30*delta`, smaller than either certified endpoint magnitude. The original derivative of `24*Mx` on `[0,1]` is less than `-1`; a conservative coefficient-derivative perturbation bound `2^40*delta` preserves strict monotonicity. Opposite endpoint signs therefore isolate one perturbed root in the same bracket. C2 symmetry still makes the other two ordinary moments vanish. This establishes a positive-dimensional open incidence/mechanics stratum with exact centring, not a wall point.

## Reproduction, files and limits

The reconstruction script below is complete: it does not read a hidden seed, a prior worker archive or the journal. Its proposal stage is deliberately numerical and **bit-reproducibility-sensitive**. Production environment: Linux x86-64 / glibc 2.41, Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, `longdouble` with 63 fraction bits, and one OpenBLAS thread. It asserts an intermediate point-table SHA and the final exact-source SHA. Do not silently accept a mismatching hash as this object. A clean end-to-end run reproduced the final bytes; a separate point-generator replay was also bit-identical. Verification of the supplied exact data uses only portable Python integer arithmetic and is independent of that proposal environment.

The archive includes the literal V coefficients, complete affine H rows, every maximal face cycle, every true edge and its four signs, feature-exclusion witnesses, the Python/GMP/interval/global verifiers, their transcripts, and the matching meshes. The OBJ uses actual maximal faces; ASCII STL uses the full triangulation. Every OBJ coordinate and every STL occurrence was checked against the exact root interval with integer arithmetic: their coordinatewise approximation error is strictly below `2^-120`. A separate mesh audit verifies consistent winding, watertightness and Euler characteristic two. The HTML contains the full mesh, not a decimation, with a tested offline software-rendering fallback; its float32 coordinates are explicitly display-only.

The mathematical acceptance gate is met by the reported certificates, but **external independent review is still outstanding**. There is no claim of priority, prize eligibility, physical printability or complexity below 1000. The next useful action is a clean external certificate replay, followed by C2-paired, moment-reisolated coarsening with a complete new hull and all-feature audit after each accepted deletion batch. Do not replace this object by a merely near-centred or numerically merged simplification.

Complete expanded construction, certificates and OBJ/STL bundle (`L98_exact_polyhedral_gomboc.zip`)

The ZIP is 100,325,136 bytes; its SHA-256 is `e51aa3201a800c6fd533e7048448f74292cd07472ff69fbb87ef395d506570c7`. A fresh extraction passed its 36-file manifest, the integer-only verifier, and the complete H/OBJ/STL export check.

Offline full-mesh viewer (`L98_view.html`) · Exact integer coefficient and triangulation file (`L98_exact.txt`) · Rendered preview (`L98_preview.png`)

## Complete deterministic builder — save as `build.py`

Run with the pinned NumPy/SciPy versions stated above. It writes `L98_exact.txt` and refuses an identity mismatch. The 10 listed diagonal repairs are part of this finite recipe, not an implicit invocation of an unknown mesh-correction procedure.

```python
#!/usr/bin/env python3
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np
import scipy
from scipy.spatial import ConvexHull
import hashlib
assert np.__version__=='2.3.5' and scipy.__version__=='1.17.0'
assert np.finfo(np.longdouble).nmant==63
EPS=.02
XMIN=-.9798
APEX=np.array([1.0202,0,0])

def phase(z):
    e=(1.5*np.pi)*(z-z*z*z/3)
    return e-.41*np.sin(2*e)-.045*np.sin(4*e)

def hull(P):
    h=ConvexHull(P)
    T=h.simplices.copy()
    n=np.cross(P[T[:,1]]-P[T[:,0]],P[T[:,2]]-P[T[:,0]])
    flip=np.einsum('ij,ij->i',n,h.equations[:,:3])<0
    T[flip]=T[flip][:,[0,2,1]]
    return T

def volume(P,T):
    PP=P.astype(np.longdouble);tt=PP[T]
    d=np.einsum('ij,ij->i',tt[:,0],np.cross(tt[:,1],tt[:,2]))
    V=np.sum(d)/6; M=np.sum(d[:,None]*np.sum(tt,axis=1),axis=0)/24
    return float(V),np.array(M/V,dtype=float)

def audit(P,T=None,c=None, merge_tol=1e-12):
    if T is None: T=hull(P)
    V,cen=volume(P,T)
    if c is None: c=cen
    P=P-c
    tt=P[T]
    n=np.cross(tt[:,1]-tt[:,0],tt[:,2]-tt[:,0]);
    ns=np.linalg.norm(n,axis=1);n=n/ns[:,None]
    h=np.einsum('ij,ij->i',n,tt[:,0])
    # all triangle-edge incidences then group twins
    E=np.sort(T[:,[0,1,1,2,2,0]].reshape(-1,2),axis=1)
    fi=np.repeat(np.arange(len(T)),3)
    order=np.lexsort((E[:,1],E[:,0]));E=E[order];fi=fi[order]
    assert np.all(E[::2]==E[1::2])
    E=E[::2];f=fi.reshape(-1,2)
    n1=n[f[:,0]];n2=n[f[:,1]];gg=np.cross(n1,n2)
    g2=np.einsum('ij,ij->i',gg,gg)
    actual=(g2>merge_tol**2)
    # union find for coplanar maximal faces
    parent=np.arange(len(T))
    def root(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]];i=parent[i]
        return i
    for a,b in f[~actual]:
        a=root(a);b=root(b)
        if a!=b: parent[b]=a
    roots=np.array([root(i) for i in range(len(T))]);_,groups=np.unique(roots,return_inverse=True)
    F=groups.max()+1
    # Triangle foot in-face inequalities only on actual perimeter edges, use orientation of triangle
    q=n*h[:,None]
    margins=np.einsum('ijk,ik->ij',np.cross(tt[:,[1,2,0]]-tt,q[:,None,:]-tt),n)
    # correspondence T edge triplets same ordering as E construction
    amask=np.repeat(actual,2)[np.argsort(order)].reshape(-1,3)
    margins[~amask]=np.inf
    fs=np.full(F,np.inf)
    np.minimum.at(fs,groups,np.min(margins,axis=1))
    E=E[actual]; f=f[actual];gg=gg[actual];g2=g2[actual];n1=n1[actual];n2=n2[actual]
    a=P[E[:,0]];b=P[E[:,1]];d=b-a
    l2=np.einsum('ij,ij->i',d,d)
    t=-np.einsum('ij,ij->i',a,d)/l2
    q=a+t[:,None]*d
    beta1=np.einsum('ij,ij->i',np.cross(q,n2),gg)/g2
    beta2=np.einsum('ij,ij->i',np.cross(n1,q),gg)/g2
    em=np.minimum.reduce((t,1-t,beta1,beta2))
    vu=np.full(len(P),np.inf)
    np.minimum.at(vu,E[:,0],-np.einsum('ij,ij->i',a,d))
    np.minimum.at(vu,E[:,1],np.einsum('ij,ij->i',b,d))
    vu[vu==np.inf]=-np.inf
    S=np.where(fs>0)[0];U=np.where(vu>0)[0];H=np.where(em>0)[0]
    sf=np.array([np.where(groups==i)[0][0] for i in S])
    return dict(counts=(len(S),len(U),len(H)),vef=(np.unique(T).size,len(E),F),V=V,c=cen,T=T,E=E,f=f,fs=fs,vu=vu,em=em,S=S,U=U,H=H,sf=sf,groups=groups,edgecomp=np.stack((t,1-t,beta1,beta2),1))

def bump(z):
    t=np.maximum((abs(z)-.25)/.75,0)
    return 16*t*t*(1-t)**2

def centre(P,T):
    b=bump(P[:,2]);v=np.zeros_like(P);v[:,0]=b
    a,c,d=P[T[:,0]],P[T[:,1]],P[T[:,2]]
    aa,cc,dd=v[T[:,0]],v[T[:,1]],v[T[:,2]]
    det=lambda a,b,c:np.einsum('ij,ij->i',a,np.cross(b,c))
    D0=det(a,c,d);D1=det(aa,c,d)+det(a,cc,d)+det(a,c,dd)
    X=np.sum(P[T,0],axis=1);B=np.sum(b[T],axis=1)
    coeff=np.array([np.sum(D0*X),-np.sum(D1*X+D0*B),np.sum(D1*B)])
    lam=np.polynomial.polynomial.polyroots(coeff);lam=float(lam[np.argmin(abs(lam))])
    Q=P-lam*v
    return Q,lam,coeff

def phase12(z):
    eta=1.5*np.pi*(z-z*z*z/3);d=1.5*np.pi*(1-z*z);dd=-3*np.pi*z
    q1=1-.82*np.cos(2*eta)-.18*np.cos(4*eta)
    q2=1.64*np.sin(2*eta)+.72*np.sin(4*eta)
    return eta-.41*np.sin(2*eta)-.045*np.sin(4*eta),d*q1,dd*q1+d*d*q2

def bump12(z):
    t=np.maximum((abs(z)-.25)/.75,0)
    b=16*t*t*(1-t)**2
    bp=32*t*(1-t)*(1-2*t)/.75*np.sign(z)
    bpp=32*(1-6*t+6*t*t)/(.75**2)*(abs(z)>.25)
    return b,bp,bpp

def gauss(n,lam=0):
    n=n/np.linalg.norm(n,axis=1)[:,None]
    nx,ny,nz=n.T;m=np.hypot(nx,ny)
    lo=np.full(len(n),-1.);hi=-lo
    for it in range(46):
        z=(lo+hi)/2;p,dp,ddp=phase12(z)
        b,bp,bpp=bump12(z)
        der=-m*z/np.sqrt(1-z*z)+EPS*dp*(-nx*np.sin(p)+ny*np.cos(p))+nz-lam*nx*bp
        lo=np.where(der>0,z,lo);hi=np.where(der<=0,z,hi)
    z=(lo+hi)/2;p=phase(z);r=np.sqrt(1-z*z)
    return np.stack((EPS*np.cos(p)+r*nx/np.maximum(m,1e-300),EPS*np.sin(p)+r*ny/np.maximum(m,1e-300),z),1)

def radial(n,lam=0):
    n=n/np.linalg.norm(n,axis=1)[:,None]
    lo=np.full(len(n),.978);hi=np.full(len(n),1.022)
    for i in range(40):
        r=(lo+hi)/2;z=r*n[:,2];p=phase(z)
        xx=r*n[:,0]-EPS*np.cos(p)+lam*bump(z); yy=r*n[:,1]-EPS*np.sin(p)
        val=xx*xx+yy*yy+z*z-1
        lo=np.where(val<0,r,lo);hi=np.where(val>=0,r,hi)
    q=(lo+hi)[:,None]/2*n;q[:,0]+=lam*bump(q[:,2]);return q

def cap(m=128):
    th=np.arange(m//2)*2*np.pi/m+.173
    lo=np.zeros(len(th));hi=lo+.03
    for i in range(46):
        r=(lo+hi)/2;y=r*np.cos(th);z=r*np.sin(th);p=phase(z)
        val=(XMIN-EPS*np.cos(p))**2+(y-EPS*np.sin(p))**2+z*z-1
        lo=np.where(val<0,r,lo);hi=np.where(val>=0,r,hi)
    r=(lo+hi)/2
    pp=np.stack((np.full(len(th),XMIN),r*np.cos(th),r*np.sin(th)),1)
    return np.concatenate((pp,pp*[1,-1,-1]))

def init(n=10000,m=128):
    j=np.arange(n);z=(j+.5)/n;th=j*(np.pi*(3-np.sqrt(5)))
    s=np.sqrt(1-z*z)*np.cos(th);v=np.sqrt(1-z*z)*np.sin(th);p=phase(z)
    Q=np.stack(((s+EPS)*np.cos(p)-v*np.sin(p),(s+EPS)*np.sin(p)+v*np.cos(p),z),1)
    Q=np.concatenate((Q,Q*[1,-1,-1]));Q=Q[Q[:,0]>XMIN]
    return np.concatenate((Q,cap(m),APEX[None]))

def fixcentre(P,lam=0):
    for j in range(6):
        Q=P.copy();Q[:,0]-=lam*bump(P[:,2]);T=hull(Q)
        Q,la,co=centre(P,T)
        if abs(la-lam)<1e-14:break
        lam=la
    return Q,la,co

def build():
    # Stage boundary deliberately re-audits checkpoint 6; this is part of the recipe.
    P=init(10000,128);lam=0.
    for stage,limit in ((0,7),(1,100)):
        for it in range(limit):
            Q,lam,_=fixcentre(P,lam);r=audit(Q,c=np.zeros(3))
            print(stage,it,len(P),r['counts'],flush=True)
            if r['counts']==(1,1,0):break
            if stage==0 and it==6:break
            tt=Q[r['T'][r['sf']]];ns=np.cross(tt[:,1]-tt[:,0],tt[:,2]-tt[:,0])[np.ptp(tt[:,:,0],axis=1)>1e-12]
            uu=Q[r['U']];uu=uu[np.linalg.norm(uu-APEX,axis=1)>1e-10]
            ee=r['E'][r['H']];a=Q[ee[:,0]];d=Q[ee[:,1]]-a;t=-np.sum(a*d,1)/np.sum(d*d,1);ep=a+t[:,None]*d
            add=np.concatenate((radial(ns,lam),gauss(uu,lam),radial(ep,lam),gauss(ep,lam)))
            add=add[add[:,0]>XMIN+1e-13];add=add[add[:,2]>=0];add=np.concatenate((add,add*[1,-1,-1]));P=np.concatenate((P,add))
            _,idx=np.unique(np.rint(P*1e12).astype(np.int64),axis=0,return_index=True);P=P[np.sort(idx)]
    assert r['counts']==(1,1,0) and len(P)==222937
    assert hashlib.sha256(P.tobytes()).hexdigest()=='d97d9f4239e609356b5de695c733b4541c0712b2e102630192cf2ba9226e0b5d'
    D=2**48;N=np.rint(P*D).astype(np.int64);B=np.rint(bump(N[:,2]/D)*D).astype(np.int64)
    P=N.astype(np.longdouble)/D;b=B.astype(np.longdouble)/D;T=hull(P.astype(float))
    det=lambda a,b,c:np.einsum('ij,ij->i',a,np.cross(b,c))
    for _ in range(4):
        a,c,d=P[T[:,0]],P[T[:,1]],P[T[:,2]];aa=np.zeros_like(a);cc=aa.copy();dd=aa.copy();aa[:,0]=b[T[:,0]];cc[:,0]=b[T[:,1]];dd[:,0]=b[T[:,2]]
        d0=det(a,c,d);d1=det(aa,c,d)+det(a,cc,d)+det(a,c,dd);xs=np.sum(P[T,0],axis=1);bs=np.sum(b[T],axis=1)
        coef=np.array([np.sum(d0*xs),-np.sum(d1*xs+d0*bs),np.sum(d1*bs)]);la=-coef[0]/coef[1]
        for _ in range(3):la-=np.polynomial.polynomial.polyval(la,coef)/(coef[1]+2*coef[2]*la)
        Q=P.copy();Q[:,0]-=la*b;T=hull(Q.astype(float))
    used=np.unique(T);mp=np.full(len(N),-1,dtype=int);mp[used]=np.arange(len(used));T=mp[T];N=N[used];B=B[used]
    flips=[(141244,145853,108883,134104),(129857,155311,159761,164845),(106368,154145,140943,165435),(108131,135748,140198,145282),(141264,141760,108087,135439),(142656,143803,94031,135026),(160807,165416,130609,153667),(162219,163366,115757,154589),(220503,221605,221781,221879),(193045,204125,206140,206809)]
    ll=383839375497491445993980015631;qq=2**120
    def cr(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
    def dt(a,b,c):return sum(x*y for x,y in zip(a,cr(b,c)))
    ni=[tuple(map(int,row)) for row in N];bi=list(map(int,B))
    def orient(t):
        a,b,c=(ni[i] for i in t);da,db,dc=((bi[i],0,0) for i in t)
        v=dt(a,b,c)*qq-ll*(dt(da,b,c)+dt(a,db,c)+dt(a,b,dc))
        assert v!=0
        return t if v>0 else (t[0],t[2],t[1])
    for a,b,c,d in flips:
        keep=~(np.any(T==a,axis=1)&np.any(T==b,axis=1));old=T[~keep]
        assert old.shape==(2,3) and set(old.ravel())=={a,b,c,d}
        T=np.vstack((T[keep],orient((c,d,a)),orient((d,c,b))))
    V=np.column_stack((N,B));order=np.lexsort((V[:,3],V[:,2],V[:,1],V[:,0]));inv=np.empty(len(V),dtype=int);inv[order]=np.arange(len(V));V=V[order];T=inv[T]
    cap=np.all(V[T,0]==V[0,0],axis=1);assert cap.sum()==126
    cycle=list(range(0,128,2))+list(range(127,0,-2));capT=[(0,cycle[i],cycle[i+1]) for i in range(1,127)];T=np.vstack((T[~cap],capT))
    for k in (1,2):
        mask=np.argmin(T,axis=1)==k;T[mask]=np.roll(T[mask],-k,axis=1)
    T=T[np.lexsort((T[:,2],T[:,1],T[:,0]))]
    with open('L98_exact.txt','w',newline='\n') as f:
        f.write(f'{len(V)} {len(T)} {D}\n')
        for v in V:f.write(' '.join(map(str,v))+'\n')
        for t in T:f.write(' '.join(map(str,t))+'\n')
    sha=hashlib.sha256(open('L98_exact.txt','rb').read()).hexdigest();assert sha=='c1865ec183618e2d35ef7cb3ecaf91ba84390dfea569f2555f92ce6b60d6d54b',sha
    print('EXACT_SOURCE_REBUILT',sha,flush=True)
if __name__=='__main__':build()
```

## Complete integer-only verifier — save as `verify_exact.py`

Run `python verify_exact.py L98_exact.txt`, without `-O`. This code regenerates all exact predicates and moment coefficients; the stored sign ledger is not an input. Its digest agrees with the separate GMP ledger.

```python
#!/usr/bin/env python3
"""Independent integer-only verification. No NumPy, hull library or interval package."""
import sys,hashlib,math,time
if not __debug__: raise RuntimeError("Verification must not run with Python -O")

def cross(a,b):
 return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dot(a,b):return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
def sub(a,b):return tuple(a[i]-b[i] for i in range(len(a)))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def plane(a,b,c):
 u=sub(b,a);v=sub(c,a);n=cross(u,v);w=add(cross((u[3],0,0),v),cross(u,(v[3],0,0)))
 return n,w,dot(n,a),n[0]*a[3]+w[1]*a[1]+w[2]*a[2]
def detaff(a,b,c):
 n=cross(b,c);w=add(cross((b[3],0,0),c),cross(b,(c[3],0,0)))
 return dot(a,n),a[3]*n[0]+a[1]*w[1]+a[2]*w[2]

def main(path):
 start=time.time()
 assert hashlib.sha256(open(path,"rb").read()).hexdigest()=="c1865ec183618e2d35ef7cb3ecaf91ba84390dfea569f2555f92ce6b60d6d54b"
 with open(path) as f:
  nv,nt,D=map(int,f.readline().split());P=[tuple(map(int,f.readline().split())) for _ in range(nv)];T=[tuple(map(int,f.readline().split())) for _ in range(nt)];assert not f.read().strip()
 assert D==1<<48 and len(set(P))==nv
 ss=set(P)
 for x,y,z,b in P:assert (x,-y,-z,b) in ss and max(abs(x),abs(y),abs(z))<2*D and 0<=b<=D
 A0=A1=A2=V0=V1=Y0=Y1=Z0=Z1=0;planes=[];he=[]
 for fi,(a,b,c) in enumerate(T):
  assert len({a,b,c})==3 and min(a,b,c)>=0 and max(a,b,c)<nv
  n,w,d,e=plane(P[a],P[b],P[c]);planes.append((n,w,d,e))
  sx,sy,sz,sb=(P[a][j]+P[b][j]+P[c][j] for j in range(4))
  V0+=d;V1+=e;A0+=d*sx;A1-=e*sx+d*sb;A2+=e*sb;Y0+=d*sy;Y1-=e*sy;Z0+=d*sz;Z1-=e*sz
  for k,(v,u) in enumerate(((a,b),(b,c),(c,a))):he.append((min(v,u),max(v,u),3*fi+k))
 assert Y0==Y1==Z0==Z1==0
 assert A0>0 and A1<-(D**4) and A1+2*A2<-(D**4) and A0+A1+A2<0
 disc=A1*A1-4*A0*A2;assert math.isqrt(disc)**2!=disc
 Q=1<<120;L=0;H=Q
 def val(m):return A0*Q*Q+A1*m*Q+A2*m*m
 while H-L>1:
  mid=(L+H)//2
  if val(mid)>0:L=mid
  else:H=mid
 assert val(L)>0>val(H) and H*20000<Q
 for m in (L,H):
  assert abs(val(m))*(1<<160)>Q*Q*D**4
  assert V0*Q-V1*m>24*Q*D**3
 print('POLYNOMIAL',A0,A1,A2,flush=True);print('VOLUME',V0,V1,flush=True);print('ROOT',L,H,Q,flush=True)
 def affine(a,b,power=None):
  lo=a*Q-b*L;hi=a*Q-b*H
  if a==b==0:return 0
  assert lo*hi>0,'unisolated affine sign'
  if power is not None:assert min(abs(lo),abs(hi))*(1<<160)>Q*D**power
  return 1 if lo>0 else -1
 for n,w,d,e in planes:assert affine(d,e,3)>0
 he.sort();parent=list(range(nt));size=[1]*nt;connected=list(range(nt));twin=[-1]*(3*nt);degree=[0]*nv;out=[-1]*nv;E=[]
 def root(i):
  while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
  return i
 def join(a,b):
  a=root(a);b=root(b)
  if a!=b:
   if size[a]<size[b]:a,b=b,a
   parent[b]=a;size[a]+=size[b]
 def cr(i):
  while connected[i]!=i:connected[i]=connected[connected[i]];i=connected[i]
  return i
 flat=0
 for j in range(0,len(he),2):
  a,b,e=he[j];aa,bb,g=he[j+1];assert (a,b)==(aa,bb) and (j+2==len(he) or he[j+2][:2]!=(a,b))
  f,k=divmod(e,3);ff,kk=divmod(g,3)
  assert T[f][k]==T[ff][(kk+1)%3] and T[f][(k+1)%3]==T[ff][kk]
  twin[e]=g;twin[g]=e;connected[cr(f)]=cr(ff)
  n,w,d,h=planes[f];v=P[T[ff][(kk+2)%3]]
  z0=dot(n,v)-d;z1=n[0]*v[3]+w[1]*v[1]+w[2]*v[2]-h
  s=affine(z0,z1,3);assert s<=0,'nonconvex dihedral'
  if s==0:flat+=1;join(f,ff)
  else:E.append((a,b,f,ff))
 assert nv-len(he)//2+nt==2 and all(cr(f)==cr(0) for f in range(nt))
 for e in range(3*nt):v=T[e//3][e%3];degree[v]+=1;out[v]=e
 for v in range(nv):
  assert out[v]>=0;e=out[v];k=0
  while True:
   assert T[e//3][e%3]==v;e=twin[3*(e//3)+(e%3+2)%3];k+=1;assert k<=degree[v]
   if e==out[v]:break
  assert k==degree[v]
 ray=(1,2,3,0);cover=0
 for a,b,c in T:
  signs=[affine(*detaff(ray,P[b],P[c]),power=2),affine(*detaff(P[a],ray,P[c]),power=2),affine(*detaff(P[a],P[b],ray),power=2)]
  assert all(signs)
  cover+=all(s>0 for s in signs)
 assert cover==1
 roots=[root(i) for i in range(nt)];F=len(set(roots));assert nv-len(E)+F==2
 print('HULL',nv,len(E),F,'triangles',nt,'flat',flat,'degree',cover,flush=True)
 # Four edge predicates: two primal arrows and two plane-foot / cone numerators.
 q3=Q**3;lp=(q3,L*Q*Q,L*L*Q,L**3);hp=(Q*Q,H*Q,H*H);floors={2:q3*D**2,7:q3*D**7}
 def sign(c,power):
  c=tuple(c)+(0,)*(4-len(c));ev=sum(c[k]*lp[k] for k in range(4));bd=(abs(c[1])*hp[0]+2*abs(c[2])*hp[1]+3*abs(c[3])*hp[2])*(H-L);clear=abs(ev)-bd
  assert clear>0 and clear*(1<<(44 if power==2 else 154))>floors[power]
  return 1 if ev>0 else -1
 def arrow(a,b):
  x,y,z,u=a;xx,yy,zz,v=b
  return (x*(x-xx)+y*(y-yy)+z*(z-zz),-u*(x-xx)-x*(u-v),u*(u-v))
 sq=[(dot(n,n),-2*dot(n,w),dot(w,w)) for n,w,d,e in planes]
 def foot(hg,sf,hf,m):
  a,b=hg;c,d=hf
  return (a*sf[0]-c*m[0],a*sf[1]-b*sf[0]-c*m[1]+d*m[0],a*sf[2]-b*sf[1]-c*m[2]+d*m[1],-b*sf[2]+d*m[2])
 FP=[True]*nt;UP=[True]*nv;HS=[];digest=hashlib.sha256()
 for a,b,f,g in E:
  n,w,hf0,hf1=planes[f];nn,ww,hg0,hg1=planes[g]
  m=(dot(n,nn),-dot(n,ww)-dot(w,nn),dot(w,ww))
  sa=sign(arrow(P[a],P[b]),2);sb=sign(arrow(P[b],P[a]),2)
  sf=sign(foot((hg0,hg1),sq[f],(hf0,hf1),m),7);sg=sign(foot((hf0,hf1),sq[g],(hg0,hg1),m),7)
  if sa<0:UP[a]=False
  if sb<0:UP[b]=False
  if sf<0:FP[roots[f]]=False
  if sg<0:FP[roots[g]]=False
  if min(sa,sb,sf,sg)>0:HS.append((a,b))
  digest.update(f'{a} {b} {f} {g} {sa} {sb} {sf} {sg}\n'.encode())
 vf=[set() for _ in P]
 for f,t in enumerate(T):
  for v in t:vf[v].add(roots[f])
 assert all(len(s)>=3 for s in vf)
 SF=[f for f in set(roots) if FP[f]];UV=[i for i,u in enumerate(UP) if u]
 assert (len(SF),len(UV),len(HS))==(1,1,0)
 cap=set(v for f,t in enumerate(T) if roots[f]==SF[0] for v in t)
 assert cap==set(range(128)) and UV==[nv-1]
 frozen=set(v for t in T if any(i in cap or i==nv-1 for i in t) for v in t)
 assert len(frozen)==957 and all(P[i][3]==0 and 4*abs(P[i][2])<D for i in frozen)
 print('EXACT_CLASS',len(SF),len(UV),len(HS),'cap',len(cap),'apex',UV[0],flush=True)
 print('SIGN_LEDGER_SHA256',digest.hexdigest(),flush=True)
 print('MARGIN_FLOORS sigma>2^-44 B>2^-154 hull>2^-160 moment-endpoint>2^-160; V>4',flush=True)
 print('PYTHON_INTEGER_ONLY_ALL_CHECKS_PASS',time.time()-start,flush=True)
if __name__=='__main__':main(sys.argv[1])
```
