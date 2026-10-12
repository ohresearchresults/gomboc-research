# minimum-0247

AI research report · 2026-09-26 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# H5_PATH_ENERGY_FIVE_ARROW_CAP_AND_CLOSED_REFLECTION_SEPARATION_V1

## Result and exact scope

The path-energy mechanism gives a genuine H5 exclusion that is not a renamed closed-reflection obstruction. On the five-dimensional box

    Ω = [123/128,125/128] × [47/128,49/128]
        × [79/128,81/128] × [31/128,33/128] × [3/128,5/128]

in the order (x,r,p,q,lambda), a fixed rational path-cone fit satisfies **G−rrᵀ>I/256**. Its residual is explicitly nonzero at the centre. Meanwhile **every one of the nine selected edges of the full T56 tree fails closed reflected-hull inclusion throughout Ω**. This remains true even allowing arbitrary real reflection parameter t whenever beta=1−t+theta_b>=0. Thus the comparison is against actual mixed-layer closed hulls, not just against the earlier finite chord certificate.

The resulting five-arrow stress has the small integer weights

    196 D01 + 90 D12 + 109 D56 + 113 D60 + 79 D70.

The same stress is uniformly negative on the much larger cap

    0<=x,r<=1, 0<=lambda<=1/16,
    p>=9/16, q>=0, p+q<=1,

with all actual moments recomputed. It excludes **208 complete labelled rooted trees** containing its support, under every nonzero PSD common metric. The reflected stress gives 208 on the different cap q>=9/16. Neither statement is all-root coverage, a whole-H5/E17 exclusion, or a new complexity bound.

A retained negative result identifies a useful limitation: the fixed-fit sufficient test G−rrᵀ>0 fails at another genuine point of that larger cap, although its derived five-arrow stress remains positive definite. One should therefore retain and test the complete stress, not discard it when its initial Schur-complement sufficient test stops working.

The global accepted interval remains 34<=C_min<=622, and attainment is separate. These calculations do not supply an actual complete weak-arrow PSD/SPD survivor. fileciteturn13file2L9-L11

## 1. Inputs, source authority, and research route

The complete new 965-line journal was read through EOF, together with both new analytic sources. The unchanged local H5 proof/code and the literal parent minimum-0245, SHA256 3a4889dd902249e2904ddfa747f00575a10c16646d44cf15224164893c8056be, remain fully supplied in this chat. No required exact dependency was unavailable.

There is one source-identity discrepancy: the new branch memory associates the path-energy source with SHA256 777d3b2e307553b77a92f077911d7040e94b73f764ad8b68b6c96baaf66e3633e. The manifested and actually verified attached file is **9224 bytes, SHA256 6dc7106cabaa16510d7f067ac60cff45a53c08dd55482a97025aa011b8ad4866**. Only the attached, manifest-matching version is used below. fileciteturn19file0L123-L128

I used the rational, unit-path-weight identity, not the optional sharper trigonometric constants. A nonnegative least-squares fit located three useful source/path columns. Exact three-by-three elimination reconstructs that fit, and upward rounding to quarters gives the fixed rational certificate. I then proved a full residual box and explicit separation from every closed reflected-edge test. Finally I tested the resulting original stress directly on the larger cap. All accepted statements below use exact rational/integer arithmetic; numerical fitting only located the coefficients.

## 2. The unchanged uniformly filled H5 body

Let s=1−lambda and use the basal polygon

    B0=(1/4,0), B1=(1−3x/4,0), B2=(1−p,p), B3=(q,1−q),
    B4=(0,1−3r/4), B5=(0,1/4), B6=(1/16,1/16).

Set z_i=(s B_i,0) for i=0,...,6, followed by

    z7=(0,0,1), z8=(lambda,0,1), z9=(0,lambda,1).

The exact maximal-face cycles are

    (6,5,4,3,2,1,0), (8,7,0,1), (7,6,0), (1,2,8),
    (9,8,2,3), (9,3,4), (4,5,7,9), (6,7,5), (7,8,9).

For 0<x,r<1, p,q>0, p+q<1 and 0<lambda<1, this is the genuine 10/17/9 body. The original positive-volume indexed boundary convention is retained; a collapsed boundary is not called a genuine E17 body. fileciteturn13file6L18-L36

The actual volume and first moments are

    A=(31−24xp−24rq)/64,
    bx=509/3072−3xp/8+3x²p/32+xp²/8−rq²/8,
    by=509/3072−3rq/8+3r²q/32+rq²/8−xp²/8,
    V=A s²/3+lambda/6,
    Jx=s³bx/4+s²lambda(1−3xp/4)/24+lambda²/24,
    Jy=s³by/4+s²lambda(1−3rq/4)/24+lambda²/24,
    Jz=A s²/12+lambda/12+lambda²/24.

Throughout, **g=J/V** and u_i=z_i−g. The verifier proves these four moment formulas against the eight-tetrahedron oriented fan as full five-variable polynomial identities, and proves all 34 parameter/physical reflection identities. The inherited bounds 7/192<=V<=1/6 are also immediate from 7/64<=A<=31/64 and the displayed volume polynomial. No surrogate physical masses, frozen centroid, or independently recentered polar enters. fileciteturn13file6L41-L52

## 3. Explicit path-energy certificate

### Tree, component, and rational fit

Use the literal T56 tree rooted at 2:

    T=((0,1),(1,2),(3,2),(4,3),(5,6),(6,0),(7,0),(8,2),(9,3)).

Cut **1->2**. Its source component is D={0,1,5,6,7}; the reverse paths from source 1 are

    to 0: 1,0;        to 1: 1;
    to 5: 1,0,6,5;    to 6: 1,0,6;    to 7: 1,0,7.

The corresponding rational path constants sigma_d=(d−1)/(d+1), with sigma_0=−1, are respectively 0,−1,1/2,1/3,1/3. Choose

    eta=9/2,
    v5=21/4, v7=15/4, v0=v1=v6=0,
    mu_i=1/5 for every i in D.

These mu are certificate weights on actual centred vectors, not a replacement for the body's uniform volume distribution.

Define

    r=u1+(9/2)(u2−u1)+(21/4)(u5+u1/2)+(15/4)(u7+u1/3)
     =(3/8)u1+(9/2)u2+(21/4)u5+(15/4)u7,
    G=(u0u0ᵀ+u1u1ᵀ+u5u5ᵀ+u6u6ᵀ+u7u7ᵀ)/5.

At the central parameters

    (x,r,p,q,lambda)=(31/32,3/8,5/8,1/4,1/32),
    V=470023/6291456,
    g=(963259811/7700856832,
       138572147/481303552,
       503815/1880092),

the residual is exactly

    r=(−89371305/61606854656,
        5164611/3850428416,
        479295/15040736) != 0.

The deterministic coefficient recipe is useful independently of the numerical locator. Solve the three-column equation

    eta0*(u2−u1)+v50*(u5+u1/2)+v70*(u7+u1/3)=−u1

at that central body. Its exact positive solution is

    (7580047354/1703991721,
     189423046/36255143,
     6278542530/1703991721).

Rounding each coefficient upward to the next multiple of 1/4 gives eta,v5,v7 above. The rounded residual is never silently set to zero.

### Identity and the five actual arrows

Write H_ij=sym(u_i,u_j−u_i), so D_ij=tr(M H_ij). For each descendant i of depth d>=1, the rational path identity supplies the PSD remainder

    S_i=(1/2) sum_j (Delta_j−(u1−u_i)/d)(same)ᵀ
        +(d+1)/(2d)*(u_i+sigma_d u1)(same)ᵀ,

where Delta_j is the actual parent-minus-child increment along that path; S_1=0. The exact identity is

    sym(u1,u_i)+sigma_d u1u1ᵀ=sum_path H_e+S_i.

The source's complete cut identity then gives

    C_path=−eta H12−sum_i(v_i+mu_i)sum_path(i->1) H_e
          =(G−rrᵀ)/2+(u1−r)(u1−r)ᵀ/2
            +sum_i v_i S_i+(1/2)sum_i mu_i sum_path Delta_e Delta_eᵀ.

Every term after (G−rrᵀ)/2 is PSD, and all coefficients of the negative arrows are nonnegative. The complete runnable unit checks the four nonzero-depth path identities and all six symmetric entries of this cut identity symbolically on the moving family. This is precisely the rational path-energy mechanism of the supplied source. fileciteturn13file0L24-L55

Multiplying by 20 gives the claimed small-integer stress

    C=20 C_path=−196 H01−90 H12−109 H56−113 H60−79 H70.

For an independent exact check, at the central body its matrix is

    C = 1/15771354791936 *
        ((43911763855663, 29738255648176, −102933329280000),
         (29738255648176,208623857468544, −120504298094592),
         (−102933329280000,−120504298094592,912058811940864)).

The leading principal minors of this integer numerator are

    43911763855663,
    8276677714819928070286637696,
    5438476621518360603425157321026461564403712,

all strictly positive.

### Uniform residual box

The verifier expands

    V²*(G−rrᵀ−I/256)

on Ω in the rectangular Bernstein basis of degrees (4,4,4,4,6). All **4375 coefficient matrices** are strictly positive definite, by **13125 positive exact leading minors**. Therefore G−rrᵀ>I/256 at every point of Ω, with its own g=J/V. This is a full closed parameter box, not a sampled neighbourhood or an unspecified continuity radius.

Since C=20 C_path>10(G−rrᵀ), on Ω we have C>5I/128. Consequently

    (196D01+90D12+109D56+113D60+79D70)/587
        < −5 tr(M)/75136

for every nonzero PSD M. No rank or conditioning qualification is needed because the certified matrix is PD.

## 4. All nine closed reflected-edge tests really fail

The supplied closed-reflection theorem tests, for an edge a->b with source component D_a and S=D_a union {b},

    2g=(1−t)z_b+t z_a+sum_{i in S} theta_i z_i,
    theta_i>=0, sum theta_i=1, 0<=t<1.

Its kernel conclusion includes mixed layers. The path-energy source also identifies the extended admissible beta=1−t+theta_b>=0 qualification. fileciteturn13file1L8-L23 fileciteturn13file0L59-L79

There is a simple exact certificate of failure even in that larger class. Every such representation, for arbitrary real t and beta>=0, can be rewritten

    2g=z_a+sum_{i in D_a} theta'_i z_i+beta(z_b−z_a),
    theta'_i>=0, sum theta'_i=1,
    theta'_a=theta_a+theta_b.

Thus it is impossible if a vector n obeys

    n·(z_a+z_i−2g)>0 for every i in D_a,
    n·(z_b−z_a)>=0.                                      (F)

For every point of Ω, the following explicit normals satisfy (F):

| Edge | Complete source component D_a | n |
|---|---|---|
| 0->1 | {0,5,6,7} | (0,−1,0) |
| 1->2 | {0,1,5,6,7} | (1,0,0) |
| 3->2 | {3,4,9} | (1,1,0) |
| 4->3 | {4} | (0,1,0) |
| 5->6 | {5} | (0,−1,0) |
| 6->0 | {5,6} | (0,−1,0) |
| 7->0 | {7} | (1,0,(1−lambda)/4) |
| 8->2 | {8} | (1,1,1−2lambda) |
| 9->3 | {9} | (1,1,1−2lambda) |

For the first inequalities in (F), the 19 cleared polynomials

    V*n·(z_a+z_i)−2n·J

have degrees (2,2,2,2,3). All **6156 Bernstein coefficients** are strictly positive; their minimum is **408331249547/844424930131968**. Of the nine direction guards, five are identically zero, on 01,32,70,82,93. The other four have degrees (1,1,1,1,1); all **128 coefficients** are positive, with minimum **1107/65536**.

These strict scalar certificates prove failure of actual containment uniformly, not merely failure to find its barycentric coefficients. They include small components and mixed-layer source components. In particular, the selected 1->2 path-energy certificate is not secretly an exact closed reflected-hull certificate on another edge of T56.

All of Ω satisfies p+q in [55/64,57/64] and lambda in [3/128,5/128]. It lies in the requested p+q>1/2 residual and entirely above the old twenty-tree certificate's lambda<=1/64 range. The local reflection results extend to lambda<=1/16, but their actual containment condition is explicitly disproved here for this tree. The older half-triangle all-root result is also not being reused on the complementary triangle. fileciteturn13file3L14-L36 fileciteturn19file0L101-L105

## 5. The same five weights on a macroscopic full-x/r cap

Instead of requiring the fixed-fit residual test everywhere, retain the complete stress C. Its original moment polynomial is

    P=V C=−sum w_ij sym(V z_i−J,z_j−z_i).

Use p=9/16+7u/16, q=7v/16, u,v>=0,u+v<=1. On each of the eight closed intervals x in [k/8,(k+1)/8], k=0,...,7, keep the ENTIRE r in [0,1], physical cap triangle, and lambda in [0,1/16]. Expand P−I/1000 with degrees

    (3 in x, 2 in r, total 3 in (u,v), 4 in lambda).

There are 600 coefficient matrices per interval. All **4800 matrices /14400 leading minors** pass exactly. Hence P>I/1000 throughout this five-parameter cap, including indexed limits. No global quadratic lowering or discarded cubic term occurs: the lower r degree is an exact degree of this selected support's original polynomial.

Since V<=1/6,

    (196D01+90D12+109D56+113D60+79D70)/587
        < −tr(M)/(587000 V)
        <=−3 tr(M)/293500.

Every nonzero PSD metric therefore violates at least one of these five weak arrows. A genuine body's complete rooted tree containing them is impossible even when its other arrows are only weak.

Exact reconstruction of all complete extensions yields rootwise counts

    (0,0,88,45,23,0,0,0,28,24), total 208.

The source emits all 208 full nine-arrow trees, not only their count. Exactly 20 contain the old seven-arrow T56 support; this is a support-overlap count, not a claim of 188 new exclusions after every historical result. The old twenty-tree theorem has its own smaller x/r/lambda domain. The new cap is demonstrably nonredundant with the supplied closed-reflection tests because it contains the whole box Ω and T56 there fails all nine such tests. No closed-reflection census for the other 207 extensions is asserted. fileciteturn13file6L7-L12 fileciteturn13file6L102-L110

The unchanged reflection permutation (5,4,3,2,1,0,6,7,9,8) gives

    −109H06−90H43−196H54−113H65−79H75

on q>=9/16, the same complete x/r and lambda ranges. This is 208 on a different cap, not 416 at a single parameter point. The two cap conditions cannot hold simultaneously in the physical triangle.

## 6. Exact failure of the fixed-fit Schur test inside the successful stress domain

At the genuine parameters

    (x,r,p,q,lambda)=(31/32,3/8,3/4,1/8,1/32),
    V=207623/3145728,
    g=(342342085/3401695232,
       128481647/425211904,
       224519/830492),

retain exactly the same eta,v,mu. The residual becomes

    r=(−5638189671/27213561856,
        1185688383/3401695232,
       −6849/6643936).

The exact e1-direction of the sufficient matrix is

    e1ᵀ(G−rrᵀ)e1
      =−107935605748404377077/3702889744451690823680 <0.

Thus that fixed-fit sufficient test truly fails, not just its Bernstein coefficient representation. Nevertheless the SAME original five-arrow C is PD at this point and throughout the cap proved above. Its integer numerator matrix has leading minors

    21724189128353,
    2544567332342463791417999216,
    679122182309728437154735212311137266696192,

with common entry denominator 6966671835136. The report/source preserve the complete rational body, actual V,J,g, residual, G−rrᵀ, C, eight positive fan volumes and 56 strict nonincidences.

This is a negative control for **one fixed residual fit**, not a failure of all cone fits, not a complete surviving physical tree, and not an equilibrium-census claim. It explains why checking C directly can enlarge the useful domain of a path-energy discovery: the remaining PSD terms in the exact identity cannot be discarded when evaluating necessity of the Schur condition.

## 7. Execution, recovery, and most useful continuation

All accepted checks use the standalone source below, Python>=3.11 and the standard library with assertions enabled. Observed CPython was **3.13.5**. The optional discovery replay used **NumPy 2.3.5 / SciPy 1.17.0**, single-thread OpenBLAS, nonnegative least squares with maxiter=100 and the explicitly coded whitening/quarter-rounding rules. Its active columns [0,3,5] and rational rounded coefficients were reproduced; it then produced byte-identical exact outputs. Numerical success is not an acceptance test.

A normal exact run and a separate cold directory containing only the final source both passed. All three JSONs and the normal receipt were byte-identical. This is author-executed exact arithmetic plus the mathematical proofs above, not proof-assistant formalization. The unavailable historical auxiliary checker mentioned in the analytic source is not a dependency of this reconstruction.

Save the complete source in section 8 as h5_path_energy_cap.py, UTF-8 with its final newline. Run

    python -B -S h5_path_energy_cap.py output

For the optional numerical rediscovery, without -S:

    OPENBLAS_NUM_THREADS=1 python -B h5_path_energy_cap.py output --locate

Final pins:

    h5_path_energy_cap.py — 19488 bytes
    SHA256 c594ce7bfcba34b06dc6bfe290d8939edc80dd6a11d3cbdb9b68509968ca8c09
    h5_path_energy_matrices.json — 2071642 bytes
    SHA256 c579e13f361f6de03320bd6fe6f4873582e41314df676788b629430f338b5042
    h5_closed_reflection_separators.json — 171130 bytes
    SHA256 8df4fb252525802aec05317820b3deb2e6c34e6fbbcd8edf5e94f21eb138504e
    h5_path_energy_report.json — 22101 bytes
    SHA256 014d51cd39bcdab54bf65d7cfbb963afbffa0f8235bd43d11ec2ae3fa8df07f7
    normal stdout — 754 bytes
    SHA256 65f5166f06e65a6bfdaf798c38d86e40a04290be8eed16e7b4a7cba6571ba046
    optional-rediscovery stdout — 832 bytes
    SHA256 e7b25e2fe962ca47f0c14d162a5ddee82131b4eb803902291ae561ddc3bd8166

Expected normal markers:

    H5_PATH_ENERGY_ACTUAL_IDENTITIES_PASS 4 34 4 6
    H5_NONZERO_RESIDUAL_CELL_PASS 4375 13125
    H5_ALL_BETA_NONNEGATIVE_CLOSED_REFLECTIONS_FAIL_PASS 9 19 6156 4 128 5
    H5_FIVE_ARROW_FULL_XR_CAP_PASS 8 4800 14400 208
    H5_FIXED_FIT_SCHUR_FAILURE_POSITIVE_STRESS_PASS
    H5_PATH_ENERGY_CAP_RECOVERY_PASS

The scientific continuation is now concrete: use quantitative path fits on other basal-route source components, preserving the complete resulting stresses when a particular residual floor weakens. The open issue is coverage of the other complete-tree supports and the omitted p/q region, not whether this mechanism can add anything beyond exact reflection—it now demonstrably can. The original stress cone is unchanged, as the supplied method explicitly warns; no all-root conclusion or complexity improvement follows merely from these 208 extensions. fileciteturn13file0L98-L104

## 8. Complete standalone source

This source reconstructs every coefficient matrix, scalar separating guard, complete tree extension and retained negative control from literal inputs. No parent code, earlier sandbox, saved certificate or download is required.

```python
#!/usr/bin/env python3
"""H5 path-energy cut beyond every closed reflected-edge test on one cell.
Python >=3.11, standard library, assertions enabled; no input files.
Optional --locate uses NumPy 2.3.5 / SciPy 1.17.0 for discovery only.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import comb, lcm
from pathlib import Path
import argparse, hashlib, json

TITLE='H5_PATH_ENERGY_FIVE_ARROW_CAP_AND_CLOSED_REFLECTION_SEPARATION_V1'
PARENT='3a4889dd902249e2904ddfa747f00575a10c16646d44cf15224164893c8056be'
METHOD='6dc7106cabaa16510d7f067ac60cff45a53c08dd55482a97025aa011b8ad4866'
CLOSED='d5e2797b9b8bbeba4458e339927569867ff855e828b975d6c0fbd82fc3492f71'
ZERO=(0,)*5
PAIRS=tuple((i,j)for i in range(3)for j in range(i,3))
FACES=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),
       (9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
FAN=((0,1,2,8),(0,9,8,2),(0,9,2,3),(0,9,3,4),
     (0,4,5,7),(0,4,7,9),(0,6,7,5),(0,7,8,9))
EDGES=tuple(sorted({tuple(sorted((a,b)))for f in FACES
                   for a,b in zip(f,f[1:]+f[:1])}))
TREE=((0,1),(1,2),(3,2),(4,3),(5,6),(6,0),(7,0),(8,2),(9,3))
A,B=1,2
D=(0,1,5,6,7)
POINT=tuple(map(F,('31/32','3/8','5/8','1/4','1/32')))
BOX=tuple((t-F(1,128),t+F(1,128))for t in POINT)
COUNTER=tuple(map(F,('31/32','3/8','3/4','1/8','1/32')))
def separators(l):
    return {0:(0,-1,0),1:(1,0,0),3:(1,1,0),4:(0,1,0),
            5:(0,-1,0),6:(0,-1,0),7:(1,0,(1-l)/4),
            8:(1,1,1-2*l),9:(1,1,1-2*l)}
PERM=(5,4,3,2,1,0,6,7,9,8)

class P:
    def __init__(self,x=0):
        if isinstance(x,P):self.d=x.d.copy()
        elif isinstance(x,dict):self.d={k:F(v)for k,v in x.items()if v}
        else:self.d={} if not x else {ZERO:F(x)}
    def __add__(self,b):
        d=self.d.copy()
        for k,v in P(b).d.items():d[k]=d.get(k,F(0))+v
        return P(d)
    __radd__=__add__
    def __neg__(self):return P({k:-v for k,v in self.d.items()})
    def __sub__(self,b):return self+-P(b)
    def __rsub__(self,b):return P(b)+-self
    def __mul__(self,b):
        d={}
        for k,v in self.d.items():
            for j,w in P(b).d.items():
                z=tuple(a+c for a,c in zip(k,j));d[z]=d.get(z,F(0))+v*w
        return P(d)
    __rmul__=__mul__
    def __truediv__(self,b):return self*(1/F(b))
    def __pow__(self,n):
        z=P(1)
        for _ in range(n):z=z*self
        return z
    def __eq__(self,b):return self.d==P(b).d

def var(i):
    k=[0]*5;k[i]=1
    return P({tuple(k):1})
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def add(*vs):return tuple(map(sum,zip(*vs)))
def mul(c,v):return tuple(c*x for x in v)
def sub(a,b):return add(a,mul(-1,b))
def outer(v):return tuple(v[i]*v[j]for i,j in PAIRS)
def sym(v,w):return tuple((v[i]*w[j]+v[j]*w[i])/2 for i,j in PAIRS)
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def minors(row):
    a,b,c,d,e,f=row
    return (a,a*d-b*b,a*d*f+2*b*c*e-a*e*e-d*c*c-f*b*b)
def solve(cols,y):
    mat=[[F(cols[j][i])for j in range(3)]+[F(y[i])]for i in range(3)]
    for k in range(3):
        j=next(j for j in range(k,3)if mat[j][k]);mat[k],mat[j]=mat[j],mat[k]
        t=mat[k][k];mat[k]=[v/t for v in mat[k]]
        for j in range(3):
            if j!=k:
                t=mat[j][k];mat[j]=[v-t*w for v,w in zip(mat[j],mat[k])]
    return tuple(row[-1]for row in mat)
def integer_matrix(row):
    den=lcm(*(F(v).denominator for v in row));n=[int(v*den)for v in row]
    return {'denominator':den,'upper_numerators':n,'leading_numerators':minors(n)}

def geometry(pt):
    x,r,p,q,l=pt;s=1-l
    base=((F(1,4),0),(1-3*x/4,0),(1-p,p),(q,1-q),
          (0,1-3*r/4),(0,F(1,4)),(F(1,16),F(1,16)))
    z=tuple((s*a,s*b,0)for a,b in base)+((0,0,1),(l,0,1),(0,l,1))
    area=(31-24*x*p-24*r*q)/64
    bx=F(509,3072)-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8
    by=F(509,3072)-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8
    V=area*s*s/3+l/6
    J=(s**3*bx/4+s*s*l*(1-3*x*p/4)/24+l*l/24,
       s**3*by/4+s*s*l*(1-3*r*q/4)/24+l*l/24,
       area*s*s/12+l/12+l*l/24)
    return z,V,J

def component(a):
    S={a};old=set()
    while S!=old:old=S.copy();S|={i for i,j in TREE if j in S}
    return tuple(sorted(S))
def path(i):
    p=dict(TREE);seq=[i]
    while seq[-1]!=A:seq.append(p[seq[-1]])
    return tuple(reversed(seq))
PATHS={i:path(i)for i in D}
SIGMA={i:F(len(PATHS[i])-2,len(PATHS[i]))for i in D}
assert component(A)==D and SIGMA[5]==F(1,2) and SIGMA[7]==F(1,3)


def inputs():
    z,V,J=geometry(POINT);g=mul(1/V,J);u=tuple(sub(v,g)for v in z)
    columns=(sub(u[B],u[A]),add(u[5],mul(SIGMA[5],u[A])),
             add(u[7],mul(SIGMA[7],u[A])))
    exact=solve(columns,mul(-1,u[A]));assert min(exact)>0
    assert add(u[A],*(mul(c,v)for c,v in zip(exact,columns)))==(0,0,0)
    rounded=tuple(F((4*q.numerator+q.denominator-1)//q.denominator,4)for q in exact)
    assert rounded==(F(9,2),F(21,4),F(15,4))
    eta,alpha,beta=rounded
    v={i:(alpha if i==5 else beta if i==7 else F(0))for i in D}
    mu={i:F(1,5)for i in D};w={(A,B):eta}
    for i in D:
        seq=PATHS[i]
        for a,b in zip(seq[1:],seq):w[(a,b)]=w.get((a,b),F(0))+v[i]+mu[i]
    weights={e:int(20*c)for e,c in sorted(w.items())}
    assert all(F(weights[e],20)==w[e]for e in w)
    assert weights=={(0,1):196,(1,2):90,(5,6):109,(6,0):113,(7,0):79}
    assert sum(weights.values())==587
    return z,V,J,g,u,exact,eta,v,mu,weights

def cut_terms(u,eta,v,mu):
    rr=add(u[A],mul(eta,sub(u[B],u[A])),
           *(mul(v[i],add(u[i],mul(SIGMA[i],u[A])))for i in D))
    G=add(*(mul(mu[i],outer(u[i]))for i in D))
    S={};energies={}
    for i in D:
        seq=PATHS[i];d=len(seq)-1
        if d==0:S[i]=(0,)*6;energies[i]=(0,)*6;continue
        deltas=[sub(u[j],u[k])for j,k in zip(seq,seq[1:])]
        mean=mul(F(1,d),sub(u[A],u[i]))
        S[i]=add(mul(F(1,2),add(*(outer(sub(t,mean))for t in deltas))),
                 mul(F(d+1,2*d),outer(add(u[i],mul(SIGMA[i],u[A])))))
        energies[i]=add(*(outer(t)for t in deltas))
        hh=add(*(sym(u[k],sub(u[j],u[k]))for j,k in zip(seq,seq[1:])))
        left=add(sym(u[A],u[i]),mul(SIGMA[i],outer(u[A])))
        assert all(x==y for x,y in zip(left,add(hh,S[i])))
    C=mul(-eta,sym(u[A],sub(u[B],u[A])))
    for i in D:
        seq=PATHS[i]
        for j,k in zip(seq,seq[1:]):C=add(C,mul(-v[i]-mu[i],sym(u[k],sub(u[j],u[k]))))
    R=add(mul(F(1,2),sub(G,outer(rr))),mul(F(1,2),outer(sub(u[A],rr))),
          *(mul(v[i],S[i])for i in D),*(mul(mu[i]/2,energies[i])for i in D))
    assert all(x==y for x,y in zip(C,R))
    return rr,G,C

def point_fidelity(z,V,J):
    vf=F(0);jf=(F(0),)*3;vols=[]
    for ids in FAN:
        a,b,c,d=(z[i]for i in ids);vv=dot(sub(b,a),cross(sub(c,a),sub(d,a)))/6
        assert vv>0;vols.append(vv);vf+=vv
        jf=add(jf,mul(vv/4,add(*(z[i]for i in ids))))
    assert vf==V and jf==J
    slacks=[];g=mul(1/V,J)
    for face in FACES:
        a,b,c=(z[i]for i in face[:3]);n=cross(sub(b,a),sub(c,a));hh=dot(n,a)
        if dot(n,g)>hh:n=mul(-1,n);hh=-hh
        assert hh-dot(n,g)>0
        for i in range(10):
            s=hh-dot(n,z[i]);assert (s==0)if i in face else (s>0)
            if i not in face:slacks.append(s)
    assert len(EDGES)==17 and len(slacks)==56
    return {'positive_fan_volumes':vols,'strict_nonincidences':len(slacks),
            'minimum_raw_support_slack':min(slacks)}

def interval(i,n,k,lo,hi):
    return sum(F(comb(k,j)*comb(i,j),comb(n,j))*lo**(k-j)*(hi-lo)**j
               for j in range(min(i,k)+1))

def rectangular(polys,box):
    keys={k for p in polys for k in P(p).d}
    deg=tuple(max(k[i]for k in keys)for i in range(5))
    ids=tuple(product(*(range(d+1)for d in deg)));loc={k:i for i,k in enumerate(ids)}
    den=lcm(*(c.denominator for p in polys for c in P(p).d.values()))
    data=[[int(P(p).d.get(k,F(0))*den)for p in polys]for k in ids]
    for ax,n in enumerate(deg):
        T=[[interval(i,n,k,*box[ax])for k in range(n+1)]for i in range(n+1)]
        dt=lcm(*(t.denominator for row in T for t in row));T=[[int(t*dt)for t in row]for row in T]
        new=[[0]*len(polys)for _ in ids]
        others=product(*(range(d+1)if a!=ax else (0,)for a,d in enumerate(deg)))
        for idx in others:
            pos=[loc[idx[:ax]+(k,)+idx[ax+1:]]for k in range(n+1)]
            for i in range(n+1):
                new[pos[i]]=[sum(T[i][k]*data[pos[k]][j]for k in range(n+1))for j in range(len(polys))]
        data=new;den*=dt
    return data,den,deg

def triangle(polys,xbox):
    keys=sorted({k for p in polys for k in p.d})
    nx=max(k[0]for k in keys);nr=max(k[1]for k in keys)
    nt=max(k[2]+k[3]for k in keys);nl=max(k[4]for k in keys)
    tri=tuple((i,j)for i in range(nt+1)for j in range(nt+1-i))
    ids=tuple(product(range(nx+1),range(nr+1),tri,range(nl+1)))
    coeff=[[p.d.get(k,F(0))for p in polys]for k in keys];trans=[]
    for i,j,(u,v),w in ids:
        row=[]
        for a,b,c,d,e in keys:
            if c>u or d>v or e>w:row.append(F(0));continue
            t=interval(i,nx,a,*xbox)*interval(j,nr,b,F(0),F(1))
            t*=F(comb(u,c)*comb(v,d),comb(nt,c+d)*comb(c+d,c))
            t*=F(comb(w,e),comb(nl,e))*F(1,16)**e;row.append(t)
        trans.append(row)
    dc=lcm(*(v.denominator for row in coeff for v in row))
    dt=lcm(*(v.denominator for row in trans for v in row))
    C=[[int(v*dc)for v in row]for row in coeff];rows=[]
    for row in trans:
        nz=[(k,int(v*dt))for k,v in enumerate(row)if v]
        rows.append([sum(t*C[k][j]for k,t in nz)for j in range(len(polys))])
    return rows,dc*dt,(nx,nr,nt,nl)

def audit(rows,den):
    mins=None
    for row in rows:
        m=minors(row);assert min(m)>0
        mins=m if mins is None else tuple(min(a,b)for a,b in zip(mins,m))
    return {'blocks':len(rows),'positive_leading_minors':3*len(rows),
            'minimum_leading_minors':[F(t,den**(i+1))for i,t in enumerate(mins)]}

def extensions(weights):
    adj={i:tuple(b if a==i else a for a,b in EDGES if i in(a,b))for i in range(10)}
    fixed={a:b for a,b in weights};answer=[]
    for root in range(10):
        if root in fixed:continue
        missing=[i for i in range(10)if i!=root and i not in fixed]
        for vals in product(*(adj[i]for i in missing)):
            parent=dict(fixed);parent.update(zip(missing,vals));ok=True
            for j in range(10):
                k=j;seen=set()
                while k!=root:
                    if k in seen:ok=False;break
                    seen.add(k);k=parent[k]
                if not ok:break
            if ok:answer.append((root,tuple(sorted(parent.items()))))
    counts=[sum(r==i for r,_ in answer)for i in range(10)]
    assert counts==[0,0,88,45,23,0,0,0,28,24]and len(answer)==208
    assert (2,TREE)in answer
    old={(0,1),(1,2),(3,2),(4,3),(5,6),(6,0),(7,0)}
    assert sum(old.issubset(t)for _,t in answer)==20
    return {'root_counts':counts,'complete_trees':answer,'total':208,'old_seven_support_overlap':20}

def clean(v):
    if isinstance(v,F):return str(v)
    if isinstance(v,dict):return {str(k):clean(w)for k,w in v.items()}
    if isinstance(v,(list,tuple)):return [clean(w)for w in v]
    return v

def save(p,v):
    data=(json.dumps(clean(v),sort_keys=True,separators=(',',':'))+'\n').encode()
    p.write_bytes(data)
    return {'filename':p.name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}

def locate():
    import numpy as np
    from scipy.optimize import nnls
    import scipy
    z,V,J,g,U,*_=inputs();u=np.array(U,float)
    G=u[list(D)].T@u[list(D)]/5;L=np.linalg.cholesky(np.linalg.inv(G)).T
    W=np.array([u[B]-u[A]]+[u[i]+float(SIGMA[i])*u[A]for i in D]).T
    c,res=nnls(L@W,-L@u[A],maxiter=100)
    assert res<1e-10
    active=[i for i,x in enumerate(c)if x>1e-8];assert active==[0,3,5]
    proposed=tuple(F(int(np.ceil(4*c[i])),4)for i in active)
    assert proposed==(F(9,2),F(21,4),F(15,4))
    print('H5_OPTIONAL_NNLS_ACTIVE_REDISCOVERY_PASS',np.__version__,scipy.__version__,clean(proposed))

def main(out):
    if not __debug__:raise RuntimeError('Assertions required; do not use -O.')
    out.mkdir(parents=True,exist_ok=True)
    z,V,J,g,u,exact,eta,v,mu,weights=inputs()
    fidelity=point_fidelity(z,V,J);rr,G,C=cut_terms(u,eta,v,mu)
    K=sub(G,outer(rr));assert any(rr)and min(minors(K))>0
    direct=add(*(mul(-w,sym(u[i],sub(z[j],z[i])))for (i,j),w in weights.items()))
    assert direct==mul(20,C)
    point={'parameters':POINT,'raw_vertices':z,'volume':V,'first_moment':J,'centroid':g,
           'source':A,'target':B,'source_component':D,'reverse_paths':PATHS,'sigma':SIGMA,
           'exact_zero_fit_eta_v5_v7':exact,'eta':eta,'v':v,'mu':mu,
           'nonzero_residual':rr,'G':integer_matrix(G),'G_minus_rrT':integer_matrix(K),
           'integer_weight_stress_C':integer_matrix(direct),'fidelity':fidelity}
    pt=tuple(var(i)for i in range(5));zz,VV,JJ=geometry(pt)
    vf=P(0);jf=(P(0),)*3
    for ids in FAN:
        a,b,c,d=(zz[i]for i in ids);dv=dot(sub(b,a),cross(sub(c,a),sub(d,a)))/6
        vf+=dv;jf=add(jf,mul(dv/4,add(*(zz[i]for i in ids))))
    assert vf==VV and all(a==b for a,b in zip(jf,JJ))
    def reflect(poly):return P({(k[1],k[0],k[3],k[2],k[4]):v for k,v in P(poly).d.items()})
    for i in range(10):
        for k in range(3):assert reflect(zz[PERM[i]][k])==zz[i][(1,0,2)[k]]
    assert reflect(VV)==VV and all(reflect(JJ[k])==JJ[(1,0,2)[k]]for k in range(3))
    U=tuple(sub(mul(VV,z),JJ)for z in zz)
    RR,GG,CC=cut_terms(U,eta,v,mu)
    residual=[GG[k]-outer(RR)[k]-(VV*VV/256 if a==b else 0)for k,(a,b)in enumerate(PAIRS)]
    rows,den,deg=rectangular(residual,BOX);ra=audit(rows,den)
    assert deg==(4,4,4,4,6)and len(rows)==4375
    matrices={'residual_box':BOX,'residual_degrees':deg,'residual_common_denominator':den,
              'residual_coefficient_upper_numerators':rows,'cap_cells':[]}
    sep=[];labs=[];point_separations=[];duals=[];dual_edges=[];zero_edges=[]
    pn=separators(POINT[4]);normals=separators(pt[4])
    for a,b in TREE:
        desc=component(a);n=normals[a];pv=[]
        for i in desc:
            sep.append(VV*dot(n,add(zz[i],zz[a]))-2*dot(n,JJ));labs.append((a,b,i))
            pv.append(dot(pn[a],sub(add(z[i],z[a]),mul(2,g))))
        assert min(pv)>0
        dual=dot(n,sub(zz[b],zz[a]))
        if dual==0:zero_edges.append((a,b))
        else:duals.append(P(dual));dual_edges.append((a,b))
        point_separations.append({'edge':(a,b),'D':desc,'normal':pn[a],
                                  'minimum_source_slack':min(pv),
                                  'edge_direction_slack':dot(pn[a],sub(z[b],z[a]))})
    sn,sd,sg=rectangular(sep,BOX);assert min(n for row in sn for n in row)>0
    dn,dd,dg=rectangular(duals,BOX);assert min(n for row in dn for n in row)>0
    assert len(sep)==19 and len(sn)==324 and sg==(2,2,2,2,3)
    assert len(duals)==4 and len(dn)==32 and dg==(1,1,1,1,1)
    assert zero_edges==[(0,1),(3,2),(7,0),(8,2),(9,3)]
    sep_pin=save(out/'h5_closed_reflection_separators.json',
                 {'box':BOX,'guard_order':labs,'degrees':sg,'common_denominator':sd,
                  'coefficient_numerators':sn,'point_normals':pn,
                  'edge_guard_order':dual_edges,'edge_degrees':dg,'edge_denominator':dd,
                  'edge_coefficient_numerators':dn,'identically_zero_edges':zero_edges})
    assert all(0<lo<hi<1 for lo,hi in BOX)and BOX[2][1]+BOX[3][1]<1
    assert BOX[2][0]+BOX[3][0]>F(1,2)and BOX[4][0]>F(1,64)
    cappt=list(pt);cappt[2]=F(9,16)+F(7,16)*pt[2];cappt[3]=F(7,16)*pt[3]
    cz,cv,cj=geometry(cappt)
    cp=add(*(mul(-w,sym(sub(mul(cv,cz[i]),cj),sub(cz[j],cz[i])))for(i,j),w in weights.items()))
    cp=[p-(F(1,1000)if a==b else 0)for p,(a,b)in zip(cp,PAIRS)]
    ca=[]
    for k in range(8):
        xbox=(F(k,8),F(k+1,8));cn,cd,cg=triangle(cp,xbox);cstats=audit(cn,cd)
        assert cg==(3,2,3,4)and len(cn)==600
        ca.append({'x_interval':xbox,**cstats})
        matrices['cap_cells'].append({'x_interval':xbox,'degrees':cg,'common_denominator':cd,
                                      'coefficient_upper_numerators':cn})
    matrix_pin=save(out/'h5_path_energy_matrices.json',matrices)
    qz,qv,qj=geometry(COUNTER);qg=mul(1/qv,qj);qu=tuple(sub(a,qg)for a in qz)
    qr,qG,qC=cut_terms(qu,eta,v,mu);qK=sub(qG,outer(qr))
    assert qK[0]<0 and min(minors(mul(20,qC)))>0
    counter={'parameters':COUNTER,'raw_vertices':qz,'volume':qv,'first_moment':qj,
             'centroid':qg,'residual':qr,'G_minus_rrT':integer_matrix(qK),
             'negative_direction':(1,0,0),'negative_value':qK[0],
             'integer_weight_stress_C':integer_matrix(mul(20,qC)),
             'fidelity':point_fidelity(qz,qv,qj),
             'scope':'Failure of this fixed-fit Schur sufficient test, NOT failure of all fits or a surviving tree.'}
    report={'title':TITLE,'parent_sha256':PARENT,'method_source_sha256':METHOD,'closed_source_sha256':CLOSED,
            'facets':FACES,'edges':EDGES,'fan':FAN,'tree':TREE,'fan_identities':4,
            'reflection_identities':34,'path_identities':4,'cut_matrix_identity_entries':6,
            'weights':[(a,b,w)for(a,b),w in weights.items()],'weight_sum':587,'point':point,
            'residual_cell':{'box':BOX,'gap_G_minus_rrT':F(1,256),'certificate':ra,
                             'mean_arrow_gap':F(5,75136)},
            'closed_reflection_failure':{'parameter_box':BOX,'point_separations':point_separations,
                                         'source_guards':19,'source_coefficients':6156,
                                         'edge_guards':4,'edge_coefficients':128,'edge_identities':5,
                                         'scope':'No exact reflected representation for ANY real t with beta=1-t+theta_b>=0.',
                                         'minimum_cleared_coefficient':F(min(n for row in sn for n in row),sd),
                                         'minimum_edge_coefficient':F(min(n for row in dn for n in row),dd)},
            'cap':{'x_r':[0,1],'lambda':[0,F(1,16)],'p_min':F(9,16),
                   'triangle_substitution':'p=9/16+7*u/16, q=7*v/16, u,v>=0,u+v<=1',
                   'polynomial_gap':F(1,1000),'mean_arrow_gap':F(3,293500),
                   'cells':ca,'blocks':4800,'positive_leading_minors':14400,
                   'boundary_scope':'Polynomial indexed limits; genuine geometry requires strict original shape conditions.'},
            'reflected_weights':sorted((PERM[a],PERM[b],w)for(a,b),w in weights.items()),
            'extension_census':extensions(weights),'matrices':matrix_pin,'separators':sep_pin,
            'fixed_fit_schur_failure_control':counter,
            'scope':'208 extensions per cap, NOT all roots; all closed reflected-edge tests fail for T56 throughout the residual cell.'}
    rp=save(out/'h5_path_energy_report.json',report)
    print('H5_PATH_ENERGY_ACTUAL_IDENTITIES_PASS 4 34 4 6')
    print('H5_NONZERO_RESIDUAL_CELL_PASS 4375 13125')
    print('H5_ALL_BETA_NONNEGATIVE_CLOSED_REFLECTIONS_FAIL_PASS 9 19 6156 4 128 5')
    print('H5_FIVE_ARROW_FULL_XR_CAP_PASS 8 4800 14400 208')
    print('H5_FIXED_FIT_SCHUR_FAILURE_POSITIVE_STRESS_PASS')
    print('H5_PATH_ENERGY_CAP_RECOVERY_PASS')
    print(json.dumps({'report':rp,'matrices':matrix_pin,'separators':sep_pin},sort_keys=True))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path,nargs='?',default=Path('h5-energy-output'))
    ap.add_argument('--locate',action='store_true');args=ap.parse_args()
    if args.locate:locate()
    main(args.out)
```

Supplementary copies: [standalone source](sandbox:/mnt/data/h5_path_energy_cap.py), [exact report](sandbox:/mnt/data/h5-energy-output/h5_path_energy_report.json), [matrix certificates](sandbox:/mnt/data/h5-energy-output/h5_path_energy_matrices.json), and [closed-reflection separating guards](sandbox:/mnt/data/h5-energy-output/h5_closed_reflection_separators.json). The complete executable recovery is already embedded above.
