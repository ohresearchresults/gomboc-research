# material-e125db06319b

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# W_ONLY_RESIDUAL_FULL_COVARIANCE_CHORD_ATLAS_V1
## Recovery capsule part 3/3: theorem, complete exact checker and observed report

Required complete capsule: part1 [internal-source-reference]; part2 [internal-source-reference], including its explicit one-line byte repair; this part3; and exact lift_core.py from [internal-source-reference]. These preserve all actual coordinates, moments, non-default parameters and runnable code without the originating sandbox. The generator reconstructs the exact compact certificate. The checker does not use a numerical solver.

## A. The mathematical result and its relationship to stronger accepted work

For the literal actual homogeneous H5 W_ONLY_RESIDUAL body with theta=(1/10,9/10,3/25,3/5,3/20), there is NO SPD metric with both S=1 and U=1, even allowing additional physical weak contacts. This concerns its whole affine orbit: every shear, tangential SPD block and positive Schur height. It is not a proof of whole H5 or whole E17 exclusion. The global bracket34<=C_min<=622 and canonical C622 are unchanged.

The stronger accepted minimum-0267 already proves unconditional U>=2 on a full five-dimensional radius1/100 box about this body. The independent ordinary-PSD point cover in minimum-0266 also proves U>=2. Thus the present construction is preserved as a NON-RECORD method demonstrating the use of the full physical covariance matrix with true chord geometry; it is not promoted as the best exclusion or as a reason to re-solve this calibration point. These worker findings were accepted as author evidence, not independently replayed by the coordinator.

The coordinator developed and ran the present atlas directly. The canonical recovery object is the1232-leaf atlas below, not an earlier exploratory1452-leaf atlas. All23 closed cases were checked exactly after source reconstruction. A single full clean source reconstruction and partitioned complete exact verification were observed; no second full clean-generation replay is claimed.

## B. Exact body and analytic inputs

The complete core constructs raw vertices, true maximal facets and actual uniform moments. V10,E17,F9; true base is a heptagon and top is a triangle, not two pentagons. Its volume is881291/9600000 and actual centroid

    g=(7368835529/28201312000,3427883561/28201312000,50317/153268)=(c,gamma).

The true top-to-base spokes are7->0,7->5,7->6,8->1,8->2,9->3,9->4. The checker verifies strict W and A guards and0<gamma<1/3. It never substitutes triangulation diagonals for those edges.

Analytic parent1, read completely: minimum-0262,SHA256 9d6d4bb7467bce10452f7713b241cc60dbd441bea84f7100c4bc37c967d53825. Under actual W/A,gamma<=1/3 and joint S1/U1, the basal foot beta=c+gamma v is not in relint B. Every upper-layer norm maximizer a has a true nonnegative spoke a->b. Put H=1-gamma,k=1-2gamma and

    Y_i=(z_i-g)_H+(z_i,z-gamma)v,
    p=2c-a_H-kv.

Then p is in relint B, and with the TRUE basal chord

    tau=max{t>=0: beta-tY_a belongs to B},

one has tau>1 and the strict necessary lens

    |kY_b+2gamma Y_a|_G^2 < tau^2 |Y_a|_G^2.

The parent's analytic result is used. Its originally unobserved optional probe executions are not rewritten as observed by this independent atlas.

Analytic parent2, read completely: minimum-0264,SHA256 bfcc1a56683308cd9ba36d337656a9bbebb9065375f6d531d489c9f28c03c4b5. In the ACTUAL covariance frame the orthogonal bound83/10 and finite escape heights give gaps

    p_gap=116613589/18000000,
    q_gap=189027769/30000000,
    ell=1/(p_gap*q_gap+q_gap+1)
       =540000000000000/25985706405752941.

Thus a joint candidate satisfies M>=ell tr(M Sigma) Sigma^-1. This concerns the same physical metric and actual covariance, not an arbitrary reference or a uniformly recentered polar.

## C. Full matrix floor instead of scalar amplification alone

Write the single actual SPD metric as

    M=[[G,Gv],[v^T G,v^T Gv+eta]],       G>0,eta>0.

Set z=Sigma_zz,m=Sigma_Hz/z,D=(Sigma^-1)_HH,w=v+m and t=z w^T D w. The sheared covariance and its inverse are

    C_v=D^-1+z w w^T,
    Sigma_v=[[C_v,z w],[z w^T,z]],
    Sigma_v^-1=[[D,-D w],[-w^T D,(1+t)/z]].

Put T=tr(G C_v)+z eta. Congruence transports the complete physical floor to

    F=diag(G,eta)-ell T Sigma_v^-1 >=0.                  (F)

The earlier amplified normal inequality is only the final diagonal test in(F). This atlas keeps additional rational quadratic tests q^T F q>=0, with mixed horizontal-normal terms. It does not assert a finite direction net is equivalent to PSD; using any finite subset is a necessary relaxation and suffices for a certified contradiction.

At fixed p, the following rows are all linear in (G11,G12,G22,eta): the true spoke

    Y_a^T G(Y_b-Y_a)-H eta>=0;

two top-maximum comparisons |Y_a|_G^2-|Y_j|_G^2>=0; quadratic tests of(F); and valid true-chord upper bounds below. They use ONE common G,v,eta throughout. No dropped determinant relation or independently chosen polar normal height appears.

## D. Complete shear coverage and chord rows

For a basal support n_e.x<=h_e, beta not in relint B means at least one e has n_e.beta>=h_e. In the p chart this is exactly

    n_e.p <= [n_e.c-gamma n_e.a_H-k h_e]/gamma.

Intersect that closed halfplane with the closed true heptagon. Enumerating all7 true spokes and all7 outside-foot supports gives49 initial choices;26 have no possible relative-interior p, and23 closed polygons remain. The exact checker reconstructs every polygon, including empty cases, so no shear is omitted. Each polygon is triangulated by a full first-vertex fan and each fan triangle is covered by a complete binary longest-edge subdivision.

For any other basal support n_j.x<=h_j with d=-n_j.Y_a>0 throughout a leaf, put s=h_j-n_j.p>=0. Since beta=p+Y_a, its chord upper endpoint is(d+s)/d. The actual tau is no larger. The strict lens therefore implies the relaxed necessary polynomial row

    (d+s)^2 |Y_a|_G^2-d^2 |kY_b+2gamma Y_a|_G^2 >=0.     (C)

No claim that this chosen j always attains the chord minimum is needed. Its positive d is verified at all three vertices of the leaf; d is affine, so this verifies the whole closed leaf. All physical contacts have been over-covered by closed necessary inequalities, not discarded as generic zeros.

## E. Exact certificate on each leaf

The compact table records the leaf path, a certified ancestral anchor path and four physical row labels. Exact rational linear algebra at the ANCHOR triangle barycentre reconstructs four constant weights. The deterministic Fraction.limit_denominator(100000000) operation then reduces their denominators; nonnegativity and the entire resulting certificate are checked AFTER this rounding. Locator floating weights are not used by the final checker.

For the four rows L_i and weights w_i>=0, form

    -sum_i w_i L_i = R11 G11+2R12 G12+R22 G22+r_eta eta.

The checker proves R11>0,det(R)>0,r_eta>0 on the entire closed leaf by exact triangular Bernstein coefficients. Hence R is positive definite and the right side is strictly positive for every G>0,eta>0. But each necessary L_i>=0 makes the left side nonpositive. This is a whole-domain contradiction, not a point test of the metric.

The binary prefix check covers every root triangle exactly, with no missing child, duplicate leaf or hidden pending cell. The exact core reconstructs the actual centroid/covariance and all rows independently of the numerical solver. Complete observed verification:23 cases,1232 leaves,59858 strictly positive Bernstein coefficients,552 chord guard vertex tests,max subdivision depth11. The fixed145 primitive integer direction net plus explicit solver cuts is a locator; rational proofs decide acceptance.

The finite strict certificates also imply some unspecified open actual-shape neighborhood remains jointly excluded: the body guards and each closed-leaf coefficient have positive margins and moving clipped polygons can be transported locally. No explicit neighborhood size is claimed from this argument; the accepted stronger U2 macro theorem already supplies an explicit five-box.

Meaningful prior limitations: coarse13-direction locators generated ill-conditioned dual candidates and unclosed slivers; these were not physical survivors. The first shear p9=(.15,.15) passed a local floor but already had beta in relint B and was excluded by the basal-foot condition. The final49-to23 coverage explicitly includes that gate. Scalar amplified-normal and two separate tangential conic tests are not equivalent to(F).

## F. Complete exact verifier

Save as atlas_verify.py,7627B,SHA256 259cf805d4b74c385a5d8717c5411a50445e27f100f50bb47ad9d59ccf1ef684. The introductory phrase 'barycentre' refers to the explicit ancestral anchor in the code; the old inline comment 'All21' is a prose counting typo only: the loops actually enumerate49 choices and check23 surviving cases. These comments are retained to preserve the actually executed bytes.

```python
"""Independent exact verifier for the actual W-only full-affine-orbit atlas.

Usage: python -B atlas_verify.py [--case A B E]
Requires only Python >=3.10 and SymPy; no NumPy, SciPy, optimizer, sampled
metric, or original locator weights. The exact compact table chooses four
valid inequality rows on each closed triangle. Constant nonnegative weights
are reconstructed by a rational linear solve at its exact barycentre.
"""
from fractions import Fraction
import argparse
import hashlib
import json
from pathlib import Path
import sympy as S
import atlas_common as A

IDENTITY='W_ONLY_RESIDUAL_FULL_COVARIANCE_CHORD_ATLAS_V1'
EXPECTED_THETA=['1/10','9/10','3/25','3/5','3/20']
EXPECTED_PORTS={(7,0),(7,5),(7,6),(8,1),(8,2),(9,3),(9,4)}


def assumptions():
    assert list(A.THETA)==EXPECTED_THETA
    body=A.BODY
    assert len(body['raw'])==10 and len(body['edges'])==17 and len(body['poles'])==9
    assert body['volume']==A.R(881291,9600000)
    assert body['g']==S.Matrix([A.R(7368835529,28201312000),
                               A.R(3427883561,28201312000),A.R(50317,153268)])
    assert 0<A.GAMMA<S.Rational(1,3) and A.K>0
    assert set(A.PORTS)==EXPECTED_PORTS
    w_slacks=[]
    for a in (7,8,9):
        for b in range(7):
            reflected=2*A.C-A.K*A.RAW[b][:2,0]-2*A.GAMMA*A.RAW[a][:2,0]
            w_slacks.extend(h-n.dot(reflected) for n,h in A.SUPPORTS)
    assert min(w_slacks)==A.R(110813102889,11280524800000)>0
    a_slacks=[1+q.dot(body['v'][a]) for q in body['poles'][1:] for a in (7,8,9)]
    assert min(a_slacks)==A.R(2625570322,3427883561)>0
    p=A.R(116613589,18000000);q=A.R(189027769,30000000)
    assert A.ELL==1/(p*q+q+1)==A.R(540000000000000,25985706405752941)
    # All 21 clipped polygons are reconstructed, including empty cases.
    cases=[]
    for a,b in A.PORTS:
        for e,(n,h) in enumerate(A.SUPPORTS):
            bound=(n.dot(A.C)-A.GAMMA*n.dot(A.RAW[a][:2,0])-A.K*h)/A.GAMMA
            poly=A.polygon(a,e)
            if len(poly)<3 or A.area2(poly)==0:
                # No point of relint B can then satisfy the outside-foot row.
                assert bound<=min(n.dot(v) for v in A.BASE)
                continue
            assert A.area2(poly)>0
            assert all(n.dot(v)<=bound for v in poly)
            assert all(hh-nn.dot(v)>=0 for v in poly for nn,hh in A.SUPPORTS)
            cases.append((a,b,e))
    assert len(cases)==23
    return cases


def decode(a,b,symbol):
    if symbol==['S']:return {'kind':'spoke'}
    if symbol[0]=='T':
        assert len(symbol)==2 and symbol[1] in (7,8,9) and symbol[1]!=a
        return {'kind':'top','data':[symbol[1]]}
    if symbol[0]=='C':
        assert len(symbol)==2 and isinstance(symbol[1],int) and 0<=symbol[1]<7
        return {'kind':'chord','data':[symbol[1]]}
    if symbol[0]=='F':
        assert len(symbol)==4
        q=tuple(A.R(x) for x in symbol[1:]);assert any(q)
        return {'kind':'floor','data':list(map(str,q))}
    raise ValueError('Unrecognized physical row')


def complete_cover(paths,root_count):
    assert len(paths)==len(set(paths)) and paths
    seen=set(paths)
    for path in paths:
        assert path and path[0] in set(map(str,range(root_count)))
        assert set(path[1:])<=set('01')
    prefixes={path[:i] for path in paths for i in range(1,len(path)+1)}
    def check(prefix):
        if prefix in seen:
            assert prefix+'0' not in prefixes and prefix+'1' not in prefixes
            return 1
        assert prefix+'0' in prefixes and prefix+'1' in prefixes
        return check(prefix+'0')+check(prefix+'1')
    assert sum(check(str(i)) for i in range(root_count))==len(paths)


def case_verify(case):
    a,b=case['port'];e=case['outside_edge']
    assert (a,b) in EXPECTED_PORTS
    poly=A.polygon(a,e)
    roots=[(poly[0],poly[j],poly[j+1]) for j in range(1,len(poly)-1)]
    leaves=case['leaves']
    complete_cover([x[0] for x in leaves],len(roots))
    coeffs=0;guards=0;maxdepth=0;used=set()
    for leaf in leaves:
        assert len(leaf)==6
        path=leaf[0];tri=roots[int(path[0])]
        for digit in path[1:]:tri=A.split_triangle(tri)[int(digit)]
        assert S.det(S.Matrix.hstack(tri[1]-tri[0],tri[2]-tri[0]))!=0
        maxdepth=max(maxdepth,len(path)-1)
        anchor=leaf[1];assert path.startswith(anchor)
        anchor_tri=roots[int(anchor[0])]
        for digit in anchor[1:]:anchor_tri=A.split_triangle(anchor_tri)[int(digit)]
        terms=[decode(a,b,t) for t in leaf[2:]]
        pt=sum(anchor_tri,S.zeros(2,1))/3
        at={A.X:pt[0],A.Y:pt[1]}
        rows=[A.constraint(a,b,t['kind'],tuple(t.get('data',()))) for t in terms]
        mat=S.Matrix([[f.eval(at) for f in row] for row in rows]).T
        rhs=-S.Matrix([f.eval(at) for f in A.chart(a)[4]])
        assert mat.det()!=0
        exact_weights=mat.inv()*rhs
        # Exact continued-fraction rounding reduces coefficient sizes. It is
        # only a deterministic reconstruction step; all resulting signs and
        # the complete-domain strict certificate are verified below.
        weights=[A.R(Fraction(int(w.p),int(w.q)).limit_denominator(100000000))
                 for w in exact_weights]
        assert all(w>=0 for w in weights) and any(w>0 for w in weights),(a,b,e,path,anchor,'weight sign')
        for term,weight in zip(terms,weights):
            term['weight']=str(weight)
            used.add(term['kind'])
            if term['kind']=='chord':
                n,h=A.SUPPORTS[term['data'][0]]
                d=-n.dot(A.chart(a)[1][a])
                assert all(d.subs({A.X:p[0],A.Y:p[1]})>0 for p in tri)
                guards+=3
        rr=A.certificate_polys(a,b,terms)
        # -sum weights*rows is R:G+r_eta*eta with R positive definite.
        # Strict positivity of R11, detR, r_eta on each CLOSED triangle
        # is established by their exact triangular Bernstein coefficients.
        for f in rr:
            bb=A.bernstein(f,tri)
            assert bb and min(bb)>0,(a,b,e,path,'Bernstein sign')
            coeffs+=len(bb)
    return {'port':[a,b],'outside_edge':e,'leaves':len(leaves),
            'coefficients':coeffs,'chord_guard_vertices':guards,
            'max_depth':maxdepth,'row_types':sorted(used)}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--case',nargs=3,type=int)
    parser.add_argument('--range',nargs=2,type=int)
    args=parser.parse_args()
    raw=Path(__file__).with_name('atlas_exact_bases.json').read_bytes()
    data=json.loads(raw)
    assert data['version']==1 and data['identity']==IDENTITY
    assert data['theta']==EXPECTED_THETA and A.R(data['ell'])==A.ELL
    expected=assumptions()
    actual=[(*c['port'],c['outside_edge']) for c in data['cases']]
    assert actual==expected and len(actual)==len(set(actual))
    cases=data['cases']
    if args.case:
        assert tuple(args.case) in actual
        cases=[c for c in cases if (*c['port'],c['outside_edge'])==tuple(args.case)]
    if args.range:
        lo,hi=args.range;assert 0<=lo<hi<=len(cases)
        cases=cases[lo:hi]
    reports=[]
    for case in cases:
        report=case_verify(case);reports.append(report)
        print(json.dumps(report,sort_keys=True,separators=(',',':')),flush=True)
    print('ATLAS_DATA_SHA256',hashlib.sha256(raw).hexdigest())
    print('EXACT_CASES',len(reports),'LEAVES',sum(r['leaves'] for r in reports),
          'BERNSTEIN_COEFFICIENTS',sum(r['coefficients'] for r in reports),
          'CHORD_GUARD_VERTICES',sum(r['chord_guard_vertices'] for r in reports))
    print(IDENTITY, 'PART_PASS' if args.case or args.range else 'PASS')

if __name__=='__main__':main()
```

## G. Commands and exact expected outputs

Complete verification command after reconstruction:

    python -u -B atlas_verify.py > atlas_verify_report.txt

It must terminate W_ONLY_RESIDUAL_FULL_COVARIANCE_CHORD_ATLAS_V1 PASS, with EXACT_CASES23,LEAVES1232,BERNSTEIN_COEFFICIENTS59858,CHORD_GUARD_VERTICES552. This unpartitioned command is equivalent to the observed partitioned commands below, but its own output file was not separately run or hashed. Do not claim an unobserved unpartitioned file pin.

Observed complete partition, each command `python -u -B atlas_verify.py --range LO HI > NAME`, every file ends PART_PASS:

0 8, report_00_08.txt,1379B,SHA256 2ec6e9366ddbb7f90e44396744807b890fdbd88ea66b4bcddaa6ce8725e85162;
8 11, report_08_11.txt,658B,SHA256 5d952913c3bb12f618360570d8f175a67026c30ac77807d2ad5666a1d73a4b0c;
11 14, report_11_14.txt,642B,SHA256 0d33f18d0a37eee3779c87bf4d679ffdb3ae2573795cde1e3be5ea074910c7ba;
14 17, report_14_17.txt,646B,SHA256 5ef63f36210e554ed64515dd3a1219e70ca5fd06b0ff3ebee031cd05de2ad416;
17 20, report_17_20.txt,655B,SHA256 d6d46a2e119911d7e57eca2c1f9468ff5c91190919714bc75c0fbf83d11f4648;
20 22, report_20_22.txt,513B,SHA256 f7a67ea49570602bf96b5bd1d43d9b60ead73c9a61fd48adc4b57b73d3798e36;
22 23, report_22_23.txt,369B,SHA256 abd52c43bb685c7518ef75ba134c9e6ef56e10500f2a9253b792330a9dafe166.

Every part checks the same complete case catalog and atlas SHA b40f47caf65789a5725142ca203b0abbbdb02427f50b47467d4aed69c6197c05 before its exact subset. Their disjoint ranges exhaust0..22. A preliminary larger8..17 invocation timed out after six complete cases; it was replaced by the successful smaller runs above, not counted as complete verification.

The corresponding exact leaf counts in fixed case order are30,68,149,1,89,10,11,2,64,13,17,102,3,13,88,2,33,30,65,136,39,86,181. Numerical precision, hash identity and transport success alone are not the theorem: the strict whole-triangle algebra and complete geometric covering above are its computational acceptance criterion.
