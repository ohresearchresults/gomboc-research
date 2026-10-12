# material-7897300ca205

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# SHARP_FIVE_ARROW_COPLANAR_SUPPORT_V2

Coordinator analytic theorem and exact rational controls. The local obstruction-support bound is exactly FIVE, for weak as well as strict SPD feasibility. The lower example is a five-edge boundary path of a strictly convex hexagon. This sharpness statement concerns local coplanar arrow systems, NOT the mechanical minimum Cmin. The global interval34<=Cmin<=622 is unchanged.

This material supersedes the previously OPEN four-versus-five sharpness question in [internal-source-reference]. Its complete source also reconstructs the previous minimal-four pentagon without that older material's superseded malformed short fence. This is the clean canonical recovery unit for BOTH explicit local controls. The complete tangent reduction antecedent is [internal-source-reference], SHAe1c694aba308253401e7e57173bce684930ad008b3d037816e1bc1c556cf50ed; its analytical facts are restated as needed below. No arbitrary plane polygon is asserted here to be an actual own-centred E17 polar face.

## 1. The setting and exact tangent elimination

For points q_i=A p_i+b in an affine plane not through0, withA rank2 and[A b] invertible, select finitely many arrowsi->j. Put e_i=p_j-p_i. One physical SPD N yields H=A^T N A>0 and free k=A^T N b, with
D_i=p_i^T H e_i+k^T e_i.
Conversely anyH>0 and arbitraryk extend toN>0 by choosing the remaining normal coefficientc>k^T H^-1 k. This uses ONE common metric, not separate local metrics.

LetK={lambda>=0:sumlambda_i e_i=0}, and S(lambda)=sumlambda_i sym(p_i e_i^T). Elementary finite Farkas elimination ofk says weak arrows are feasible iff someH>0 contracts nonnegatively with everyS(lambda), lambda inK. The coneS(K) is finitely generated and closed. Separation of this cone from the openSPD cone shows weak infeasibility iff there existslambda>=0 withS(lambda) nonzero NSD. For strict arrows the alternative includesS=0 withlambda nontrivial: normalize the finitely many extreme rays ofK and separate their compact convex hull from the closed NSD cone. Equivalently, strict infeasibility has a nontriviallambda>=0 withsumlambda_i e_i=0 andS(lambda) NSD, now INCLUDINGzero. Full separation proof is in the antecedent; zero is NEVER by itself a weak obstruction.

## 2. Every coplanar infeasible system has an infeasible subset of at mostfive arrows

Encode each selected arrow by
v_i=(e_i,sym(p_i e_i^T)) in R² direct-sum Sym2,
a five-dimensional real vector space.

Weak case: an infeasibility certificate gives(0,S),S!=0 NSD, in the positive cone ofv_i. If more thanfive coefficients arepositive, take a linear dependence on theirv_i, choose its sign so some coefficient ispositive, and subtract the largest multiple retaining all coefficientsnonnegative. At leastone term disappears, while(0,S) is unchanged. Repeat to support<=5. This is a direct finite conic reduction and preserves the exact nonzeroNSD obstruction.

Strict case: ifweakfeasibility alreadyfails useabove. Otherwise a strictinfeasibilitycertificate must haveS=0, because nonzeroNSD wouldcontradictweakfeasibility. Choose an inclusion-minimal nontrivialpositiverelation sumlambda_i v_i=0. Its support hasatmostsix: otherwise its nullspace hasdimension>=2, allowing a nonproportional perturbation oflambda until a coefficient vanishes while retaining nonnegativity and a nonzero relation. If it hadsix terms, minimalityforcesrankfive. Those vectors spanR5 and theirstrictlypositivezero relation implies theirpositivecone equalsR5: shift any real coefficientrepresentation by asufficientlylarge multiple ofthepositiverelation. Inparticular theircone contains(0,-I), contradictingweakfeasibility. Hence thezerorelation alsohas<=5terms. Onthat subset allD_i cannot bestrictlypositive.

Thus FIVE is a universal upper bound for both versions. The next exact example proves it SHARP even for consecutive boundary arrows of a strictly convex polygon.

## 3. Exact minimal-five convex hexagon

Counterclockwise vertices:
p0=(0,0),p1=(1,0),p2=(1,3),p3=(-1,5),p4=(-4,2),p5=(-4,1).
Letq_i=(p_i,1), and select0->1->2->3->4->5. The closing5->0 edge is a true polygon edge but is NOT selected. Every nonincidentvertex lies strictlyleft of every oriented boundaryedge; all24determinants are checked by the source.

Write H=[[a,b],[b,c]],k=(kx,ky). The five arrowforms are
D0=kx,
D1=3b+3ky,
D2=-2a-4b+6c-2kx+2ky,
D3=3a-12b-15c-3kx-3ky,
D4=4b-2c-ky.

The strictlypositive integerweightslambda=(75,4,27,7,45) satisfy
sumlambda_i e_i=0,
S(lambda)=-33I,
and consequently the exact identity
75D0+4D1+27D2+7D3+45D4=-33(a+c)<0
for everyH>0. All five WEAK arrows are therefore impossible for everycommonSPD, including every finite weak-arrow boundary.

## 4. Every proper subsystem is strictly feasible

For each omittedarrow use the following SEPARATE common physicalN on the same originalq_i coordinates. Each3x3matrix is SPD byits three displayedleadingminors; everyretainedD is strictlypositive.

OmitD0:
N0=[[6,2,-22],[2,4,-1],[-22,-1,94]],
leadingminors(6,20,26),D=(-22,3,46,3,1).

OmitD1:
N1=[[8,-16,2],[-16,44,-153],[2,-153,1852]],
leadingminors(8,96,136),D=(2,-507,2,9,1).

OmitD2:
N2=[[36,4,1],[4,4,-2],[1,-2,2]],
leadingminors(36,128,92),D=(1,6,-70,3,10).

OmitD3:
N3=[[12,4,1],[4,8,-1],[1,-1,1]],
leadingminors(12,80,52),D=(1,9,4,-132,1).

OmitD4:
N4=[[32,-4,2],[-4,8,5],[2,5,5]],
leadingminors(32,240,288),D=(2,3,6,3,-37).

Every proper subset is contained in oneofthese4-arrow systems. Hence everyproper subset isstrictlyfeasible butthefull5arrow system isweaklyinfeasible. This proves the universal boundfive issharp for BOTH weak andstrictinfeasibility, evenforconvexboundarypaths. All4-arrow gates, evennonconsecutiveones, are incomplete for this hexagon.

## 5. The minimal-five phenomenon occupies an open chamber

Use the featurecolumns
v_i=(e_x,e_y,p_x e_x,p_x e_y+p_y e_x,p_y e_y).
For the displayedhexagon their5x5matrixV has exactdeterminant-396, and
V*(75,4,27,7,45)^T=(0,0,-33,0,-33)^T.
For all sufficientlysmall vertexperturbations, V remainsinvertible and the unique solutionlambda(p)=V(p)^-1(0,0,-33,0,-33) remainsstrictlypositive. It gives thesame fixednegative-definitetangentstress-33I. The fivefixedwitnessmetrics retain theirstrict retained-arrow inequalities, and strictconvexity persists. Thus minimal-five infeasibility isnot a fragile parallel-edge artifact or isolatedrationalpoint. No numericalneighborhoodradiusisclaimed.

## 6. The preceding minimal-four pentagon is preserved, not renamed

Its distinctliteralpoints remain((0,0),(2,0),(2,4),(-2,5),(-3,3)),with4boundaryarrows andweights(11,2,4,6). Stress=-[[20,23],[23,44]],det351. Separate proper-subsystem metrics are thefourliteralmatrices in the source. This control answered the consecutivequad-completeness question negatively; the hexagon now answers the stronger four-versus-five question. They aredifferentobjects and neither is renamed into anactualE17body. The complete source below reconstructsboth.

## 7. Scientific scope and next consequence

The theorem gives a finite exact local motif bound: any coplanar path failure alreadyoccurs on<=5selectedtruearrows, andfivecanreallybenecessary. At anactualdegree-sixvertex, the6incidentfacetpoles arecoplanar andthis criterionapplies, but onlyafter substituting q_i=n_i/(b_i-n_i.g_actual) fromtheSAME uniformbody and itsgenuinevolumeCOM. An algebraic segment isnotautomaticallyatrueedge. A realizedlocalcountercontrolwouldstillnotitselfproveallFULLgraphorientationsimpossible, a wholecanonicaltypeexclusion or anewCminimum.

The pendingactualgeometrybranch presentlyaims atdegree-fivepentagonrealization; its eventualmethodmaygeneralize todegree-sixhexagons. A possiblepyramid-plus-small-cutsroute isstillresearch, notanacceptedconstructionhere. This material containsnoactualhomogeneousE17realizationor110attainer.

## 8. Self-contained exact recovery

Save the followingcomplete source as coplanar_sharp5.py,UTF-8 LFwithfinalnewline. Python>=3.10standardlibrary only; no inputfile, randomness, optimizerornetwork. Assertionsmustbeenabled. Run `python coplanar_sharp5.py` inanydirectory. The sourcealone deterministicallyreconstructs coplanar_sharp5_report.json; runninginthefreshdirectoryistherecoveryverificationcommand.

Observed onCPython3.13.5 bythecoordinator:
source4101bytes SHA256b51d1d8d73e79d699a5c8b2ead7c161ea6620af23c5671a4d6fb0a002550b4f3;
report6834bytes SHA25674949efb23974ce6843cae456bf7e7ff6e9e5fae859b512c480a3faa7e33b981.
Terminalmarkers:
PENTAGON_MINIMAL4_AND_HEXAGON_MINIMAL5_EXACT_PASS
ALL_PROPER_SUBSETS_STRICT_SPD_AND_FULL_PATH_WEAK_IMPOSSIBLE_PASS
HEXAGON_OPEN_CHAMBER_FEATURE_DETERMINANT_MINUS396_PASS

Evidence: exactrationalcontrolverification andfullanalyticalsupport/opennessproof. No proofassistantformalizationorindependentworkerreplayclaimed. Exploratoryfloatingsearch merelysuggestedacandidate; noneofitsdecisionsareproofinputs.

```python
"""Exact sharp five-arrow coplanar obstruction, with pentagon antecedent.
Python >=3.10 standard library only. No external inputs or solver.
Run with assertions enabled: python coplanar_sharp5.py
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys

CASES = (
    dict(name='PENTAGON_MINIMAL4',
         points=((0,0),(2,0),(2,4),(-2,5),(-3,3)),
         weights=(11,2,4,6), Q=((20,23),(23,44)),
         metrics=(
             ((1,0,-20),(0,1,1),(-20,1,402)),
             ((2,-2,2),(-2,4,-19),(2,-19,147)),
             ((12,0,1),(0,2,1),(1,1,1)),
             ((1,0,1),(0,1,9),(1,9,83)),
         ),
         arrows=((-40,4,77,10),(4,-92,1,2),(2,4,-91,1),(2,36,1,-27))),
    dict(name='HEXAGON_MINIMAL5',
         points=((0,0),(1,0),(1,3),(-1,5),(-4,2),(-4,1)),
         weights=(75,4,27,7,45), Q=((33,0),(0,33)),
         metrics=(
             ((6,2,-22),(2,4,-1),(-22,-1,94)),
             ((8,-16,2),(-16,44,-153),(2,-153,1852)),
             ((36,4,1),(4,4,-2),(1,-2,2)),
             ((12,4,1),(4,8,-1),(1,-1,1)),
             ((32,-4,2),(-4,8,5),(2,5,5)),
         ),
         arrows=((-22,3,46,3,1),(2,-507,2,9,1),(1,6,-70,3,10),
                 (1,9,4,-132,1),(2,3,6,3,-37))),
)

def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))

def cross(a,b):
    return a[0]*b[1]-a[1]*b[0]

def det(A):
    if not A:
        return 1
    return sum((-1)**j*A[0][j]*det(tuple(tuple(row[k] for k in range(len(A)) if k!=j) for row in A[1:])) for j in range(len(A)))

def form(A,a,b):
    return sum(a[i]*A[i][j]*b[j] for i in range(len(a)) for j in range(len(b)))

def verify(case):
    P=case['points']; n=len(P); m=n-1
    E=tuple(sub(P[i+1],P[i]) for i in range(m))
    q=tuple(p+(1,) for p in P)
    weights=case['weights']; Q=case['Q']
    slacks=tuple(cross(sub(P[(i+1)%n],P[i]),sub(P[j],P[i]))
                 for i in range(n) for j in range(n) if j not in (i,(i+1)%n))
    assert min(slacks)>0
    assert min(weights)>0
    assert tuple(sum(weights[i]*E[i][j] for i in range(m)) for j in range(2))==(0,0)
    S=tuple(tuple(sum(F(weights[k],2)*(P[k][i]*E[k][j]+E[k][i]*P[k][j]) for k in range(m)) for j in range(2)) for i in range(2))
    assert S==tuple(tuple(-x for x in row) for row in Q)
    assert Q[0][0]>0 and det(Q)>0
    controls=[]
    for omitted,N in enumerate(case['metrics']):
        assert all(N[i][j]==N[j][i] for i in range(3) for j in range(3))
        minors=tuple(det(tuple(tuple(row[j] for j in range(k)) for row in N[:k])) for k in (1,2,3))
        assert min(minors)>0
        D=tuple(form(N,q[i],sub(q[i+1],q[i])) for i in range(m))
        assert D==case['arrows'][omitted]
        assert all(D[i]>0 for i in range(m) if i!=omitted)
        assert sum(weights[i]*D[i] for i in range(m))==-sum(N[i][j]*Q[i][j] for i in range(2) for j in range(2))
        controls.append(dict(omitted=omitted,metric=N,leading_minors=minors,arrows=D))
    result=dict(name=case['name'],points=P,edges=E,weights=weights,Q=Q,
                convexity_slacks=slacks,controls=controls)
    if m==5:
        cols=tuple((e[0],e[1],p[0]*e[0],p[0]*e[1]+p[1]*e[0],p[1]*e[1]) for p,e in zip(P,E))
        V=tuple(tuple(col[j] for col in cols) for j in range(5))
        assert det(V)==-396
        assert tuple(sum(V[j][i]*weights[i] for i in range(5)) for j in range(5))==(0,0,-33,0,-33)
        result['arrow_feature_determinant']=det(V)
    return result

if __name__=='__main__':
    assert __debug__, 'Assertions must remain enabled'
    report=dict(identity='SHARP_FIVE_ARROW_COPLANAR_SUPPORT_V2',cases=[verify(c) for c in CASES])
    out=Path('coplanar_sharp5_report.json')
    out.write_bytes((json.dumps(report,sort_keys=True,indent=2)+'\n').encode('utf-8'))
    print('PENTAGON_MINIMAL4_AND_HEXAGON_MINIMAL5_EXACT_PASS')
    print('ALL_PROPER_SUBSETS_STRICT_SPD_AND_FULL_PATH_WEAK_IMPOSSIBLE_PASS')
    print('HEXAGON_OPEN_CHAMBER_FEATURE_DETERMINANT_MINUS396_PASS')
    for p in (Path(__file__),out):
        b=p.read_bytes()
        print(p.name,len(b),hashlib.sha256(b).hexdigest())
    print('Python',sys.version.split()[0])
```
