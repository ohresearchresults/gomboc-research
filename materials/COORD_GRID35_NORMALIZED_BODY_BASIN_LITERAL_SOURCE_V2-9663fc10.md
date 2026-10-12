# material-9663fc1046ca

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# COORD_GRID35_NORMALIZED_BODY_BASIN_LITERAL_SOURCE_V2

## Correction and exact source status

**Do not use [internal-source-reference] as a recovery source.** Its manually transferred encoded block was corrupted (including a non-base64 question mark); the advertised payload digest does not validate. Its material hash proves only storage, not correct recovery. This complete literal-source material replaces that failed encoded transfer. No body or method is to be parented through the invalid material.

The exact selected body is COORD_GRID35_NORMALIZED_W001_D100000, actual35/99/66, C198, own ordinary-filled-volume-centroid strict211, weak000, all primitive-zero counters0. It is NOT a winner. Sfaces3,57,Urawlex15,H11--17. Raw coordinate maximum17bits; common centred denominator67bits. Exact volume53928718583353/1500000000000000 and centroid(-4188897247624520623,3367172185439624937,476412288260694757)/86285949733364800000.

Only unchanged dependency: **[internal-source-reference]**,39762B SHA7b9d113b63af0c9a7e9dda973cddaa2b0adf27dcebe107d615db90323b602d45. Recover that complete18-source unit's LEAD_GATE_SOURCE. Its five files used here are freeze_variants.py1522B SHA3cf9e0fb42a645ca0a70613c93f05ffd126a4ffdd1e6077c3c490532198f3124; CF7_SOURCE/grid7.py3138B SHAfdbfb8cb6783fdc3b4511d03d543b072c5eab51323043aafbdadf41855f4e292; CF7_SOURCE/core/check_A.py5483B SHAad72cc198140249c1e52a615513354036c04f4c718333a7beed64fba4b43d7f3; check_B.py6351B SHAb0cb62d5486b32d020b60f717f3dfe9d07c6c9a978492928f54c3a38f396fc24; centred_mass.py1398B SHA5f1afafa0432436bfe953a94d94ca1027c12549504f9452491f0287c2a29d1a8. The last two are in the same core directory. No separate normalized optimizer checkpoint is necessary for this exact object and certificate.

Save the JSON block as INPUT.json **without its terminal newline**, and the Python block as BASIN_GATES.py **with its terminal LF newline**. INPUT.json is822B SHA11af2bb2d0e96073ed84499aa34bd15a88dff1209e167b8fc9a109165a8fc217. BASIN_GATES.py is8681B SHA4c852560bbe8ac80bfdd1135beed1b8e3eed401ebf114b96e93116ce6514cf22. Python3.13.5 standard library only, assertions enabled, no stochastic/nondefault numerical parameters.

Commands:

`python3 -B -S LEAD_GATE_SOURCE/freeze_variants.py INPUT.json NEW_PROOF`

`python3 -B -S BASIN_GATES.py NEW_PROOF/A.json NEW_PROOF/BASIN_GATES.json`

The first command reconstructs the true convex hull, executes two independently implemented full exact geometry/filled-mass/all-feature audits and a third centred integration. The second reproduces the new exact graph and perturbation certificates. Both commands actually completed in a fresh source-only directory before storage. Expected terminal markers are EXACT_VARIANT_TWO_AUDITS_AND_MASS_PASS; EXACT_INPUT_HULL_EQUALITY_PASS COORD_GRID35_NORMALIZED_W001_D100000 [2,1,1] [0,0,0]; EXACT_OWN_CENTRED_PRIMAL_TREE_AND_POLAR_BASIN_CUTS_PASS.

Expected outputs: A.json=B.json10280B SHA904861a5b7097b235266d033d55004cd5da3c11717c2ac0da44b7e6e336526d3; RAW.json3748B SHAf042ac1663e5dcb5f689e6ed17032517a46626a7ac3be04d934fa1e62205f189; MASS.json216B SHA634789f284417937eec9d5219ef852f98c187303483e14b648c3a70c3aea6cb6; BASIN_GATES.json7604B SHAe578d6eb25c6a279885f306eead3181b3058ed434e332af559526bc096adba1b.

## Mathematical meaning and limits

For a finite bank v_i write f_ij=v_i dot(v_j-v_i). Positive escape arrows strictly increase squared norm. If all nonroots have a positive-arrow path to one root, the convex hull has exactly one strict radial maximum. A set A with f_ij<0 for every i inside and j outside contains a strict radial maximum: select a maximum-norm point inside A and apply Cauchy--Schwarz to every other distinct point inside too. Two disjoint such sets yield two distinct maxima. Duplicate points within a set represent one geometric point; strict outgoing signs forbid sharing a point between two sets.

For supporting poles q_f at the physical body's ACTUAL filled centroid, these radial maxima are physical stable faces. This uses mechanical polarity at a fixed origin, not preservation of the filled polar's own centroid. A new polyhedron must be represented by the complete corresponding pole bank or satisfy the asserted geometry separately.

Under per-vector coordinate bounds |e_ik|<=epsilon*a_i, a_i=max_k|v_ik|, expand f'_ij=f_ij+e_i dot(v_j-2v_i)+v_i dot e_j+e_i dot e_j-|e_i|^2. With L=a_i||v_j-2v_i||_1+a_j||v_i||_1, D=3(a_i*a_j+a_i^2), and U=3*a_j^2/4 when a_j<=2*a_i, otherwise U=3*a_i*(a_j-a_i), one has f-epsilon*L-epsilon^2*D<=f'<=f+epsilon*L+epsilon^2*U. U follows from maximizing uv-u^2 over |u|<=a_i,|v|<=a_j. All coefficients are rational.

Possible-escape arcs have upper bound>=0. A terminal strongly connected component has all outside bounds strictly negative. The polar graph has two disjoint30-pole sink sets at epsilon15412249/100000000; epsilon1/10 also works. Guaranteed-escape arcs have lower bound>0; in the primal graph all35 points reach root15 at epsilon5309/50000000. These bounds concern DIFFERENT coordinate spaces, not a shared raw-shape deformation radius. For applications recompute the new physical centroid and check the appropriate centred primal or centred supporting-pole bounds. Arbitrary whole-shape surgery or new unconstrained supporting poles are not excluded. A next-grid failure is only failure of this sufficient certificate.

The exact rational widest-path diagnostic uses weights f_ij/|v_i|^2. It exhibits a root-reaching tree and an outgoing cut with equal bottleneck, giving approximately-0.4546085456597566 for root3 and-0.4581910274442488 for root57. The full rational values, cut indices, tree edges and tight inequalities are reproduced. This is a global finite-basin diagnostic, not a global no-go theorem or an S-H cancellation.

## INPUT.json

```json
{"denominator":100000,"name":"COORD_GRID35_NORMALIZED_W001_D100000","vertices":[[-42115,37117,9130],[-41216,37251,12587],[-41057,37686,-988],[-41054,33929,23657],[-39371,35322,-11279],[-38194,31925,30998],[-38006,33382,-16999],[-36964,32367,-19905],[-36170,30593,-22796],[-33070,28354,-27792],[-30811,24189,46426],[-29938,25262,-32076],[-22412,17219,54629],[-14689,19848,-14906],[-5803,10770,-31306],[-2184,1119,67929],[-210,-7283,-33844],[2748,-2330,-45096],[11142,-9639,-43362],[15106,-13502,56075],[19134,-16743,-38659],[22825,-19948,-35263],[24287,-21571,45287],[26232,-22937,-31064],[28428,-25094,38802],[29281,-25580,-26359],[31499,-27620,32668],[31971,-27790,-20969],[34021,-29633,25819],[34122,-29503,-15161],[35807,-31040,18721],[35821,-30715,-8865],[36883,-31701,11617],[36813,-31677,-2278],[37142,-32029,4619]]}
```

## BASIN_GATES.py

```python
"""Exact global radial-escape cut certificates, not a global exclusion.
Python 3.13.5 standard library only. Input is a complete exact audit A.json.
The q_i are supporting poles at the body's actual filled centroid. The
perturbation bounds concern these recentered poles, NOT raw vertex motions.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from math import isqrt
import json, sys

def dot(x,y): return sum(a*b for a,b in zip(x,y))
def sub(x,y): return tuple(a-b for a,b in zip(x,y))
def packed(x): return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def need(x,s):
    if not x: raise ValueError(s)

def coefficients(points):
    size=[max(map(abs,x)) for x in points]; out={}
    for i,x in enumerate(points):
        for j,y in enumerate(points):
            if i==j: continue
            a,b=size[i],size[j]
            f=dot(x,sub(y,x))
            linear=a*sum(abs(y[k]-2*x[k]) for k in range(3))+b*sum(map(abs,x))
            # max_{|u|<=a, |v|<=b} u*v-u*u, computed exactly.
            upper=3*(b*b/4 if b<=2*a else a*(b-a))
            lower=3*(a*b+a*a)
            out[i,j]=(f,linear,upper,lower)
    return out

def arcs(coef,n,epsilon,upper):
    ans=[[] for _ in range(n)]
    for (i,j),(f,l,u,d) in coef.items():
        v=f+epsilon*l+epsilon*epsilon*u if upper else f-epsilon*l-epsilon*epsilon*d
        if v>=0 if upper else v>0: ans[i].append(j)
    return ans

def scc(graph):
    n=len(graph); reach=[]
    for i in range(n):
        seen={i}; todo=[i]
        while todo:
            for j in graph[todo.pop()]:
                if j not in seen: seen.add(j);todo.append(j)
        reach.append(seen)
    unseen=set(range(n)); components=[]
    while unseen:
        i=min(unseen); c={j for j in reach[i] if i in reach[j]}
        components.append(sorted(c)); unseen-=c
    sinks=[c for c in components if all(j in c for i in c for j in graph[i])]
    return components,sinks,reach

def maximal_grid_true(test,denominator):
    need(test(Q(0)),'predicate false at zero')
    lo=0;hi=denominator
    need(not test(Q(hi,denominator)),'extend the search bound')
    while hi-lo>1:
        mid=(lo+hi)//2
        if test(Q(mid,denominator)):lo=mid
        else:hi=mid
    return Q(lo,denominator),Q(hi,denominator)

def root_paths(graph,root):
    parent={};distance={root:0};todo=[root]
    while todo:
        j=todo.pop(0)
        for i,row in enumerate(graph):
            if i not in distance and j in row:
                parent[i]=j;distance[i]=distance[j]+1;todo.append(i)
    need(len(distance)==len(graph),'not root reaching')
    return [[i,parent[i]] for i in sorted(parent)]

def widest_paths(points,root):
    """Exact widest-root paths for f(i,j)/|point_i|^2, a rational score."""
    n=len(points); weights={}
    for i,x in enumerate(points):
        for j,y in enumerate(points):
            if i!=j:weights[i,j]=dot(x,sub(y,x))/dot(x,x)
    # This finite value exceeds all edge scores and represents root infinity.
    infinity=max(weights.values())+1
    value=[None]*n;value[root]=infinity;parent={};done=set()
    for _ in range(n):
        j=max((i for i in range(n) if i not in done and value[i] is not None),
              key=lambda i:(value[i],-i))
        done.add(j)
        for i in range(n):
            if i in done:continue
            v=min(value[j],weights[i,j])
            if value[i] is None or v>value[i]:value[i]=v;parent[i]=j
    bottleneck=min(value[i] for i in range(n) if i!=root)
    cut=[i for i in range(n) if value[i]<=bottleneck]
    outside=[i for i in range(n) if i not in cut]
    cross=max(weights[i,j] for i in cut for j in outside)
    need(cross==bottleneck and root not in cut,'widest cut equality')
    paths=root_paths([[j] if i!=root else [] for i in range(n) for j in ([parent[i]] if i!=root else [root])],root)
    minimum=min(weights[i,j] for i,j in paths)
    need(minimum==bottleneck,'path/cut duality')
    return {'root':root,'bottleneck_relative_score':str(bottleneck),'cut':cut,
            'cut_complement':outside,'tree_edges':paths,
            'local_root_escape':str(max(weights[root,j] for j in range(n) if j!=root))}

def eta_certificate(X,root):
    records=[]
    for i,x in enumerate(X):
        if i==root:continue
        best=None
        for j,y in enumerate(X):
            if i==j:continue
            d=sub(y,x);a=dot(x,d)
            if a<=0:continue
            value=a*a/(dot(x,x)*dot(d,d))
            if best is None or (value,j)>best:best=value,j
        need(best is not None,'missing positive escape')
        value,j=best
        need(dot(X[j],X[j])>dot(x,x),'norm fails to increase')
        records.append([i,j,str(value)])
    owner={i:j for i,j,_ in records}
    for i in owner:
        seen=set()
        while i!=root:
            need(i not in seen,'cycle');seen.add(i);i=owner[i]
    eta2=min(Q(r[2]) for r in records);D=10**12
    lo=isqrt(eta2.numerator*D*D//eta2.denominator)
    need(Q(lo,D)**2<=eta2<Q(lo+1,D)**2,'square bracket')
    return {'eta_squared':str(eta2),'eta_bracket':[str(Q(lo,D)),str(Q(lo+1,D))],
            'arrows':records,'all_reach_root':True}

def analyse(audit_path,out):
    raw=Path(audit_path).read_bytes(); A=json.loads(raw)
    need(sha256(raw).hexdigest()=='904861a5b7097b235266d033d55004cd5da3c11717c2ac0da44b7e6e336526d3','selected audit identity')
    need([A[k]for k in ['V','E','F']]==[35,99,66] and A['counts']==[2,1,1] and A['weak']==[0,0,0],'selected class')
    g=tuple(map(Q,A['raw_centroid']))
    X=[sub(tuple(map(Q,x)),g)for x in A['raw_vertices']]
    P=[]
    for normal,h in zip(A['normals'],A['offsets']):
        d=Q(h)-dot(normal,g);need(d>0,'origin not strictly inside')
        P.append(tuple(Q(t)/d for t in normal))
    root,=A['unstable_vertices'];primal=coefficients(X);polar=coefficients(P)
    den=10**8
    def mono_u(e):return all(root in r for r in scc(arcs(primal,len(X),e,False))[2])
    ulo,uhi=maximal_grid_true(mono_u,den)
    ptree=root_paths(arcs(primal,len(X),ulo,False),root)
    pmin=min(primal[i,j][0]-ulo*primal[i,j][1]-ulo*ulo*primal[i,j][3]for i,j in ptree)
    def two_s(e):return len(scc(arcs(polar,len(P),e,True))[1])>=2
    slo,shi=maximal_grid_true(two_s,den)
    graph=arcs(polar,len(P),slo,True);parts,sinks,_=scc(graph)
    cuts=[]
    for c in sinks:
        outside=[j for j in range(len(P))if j not in c]
        bound=max((polar[i,j][0]+slo*polar[i,j][1]+slo*slo*polar[i,j][2],i,j)
                  for i in c for j in outside)
        need(bound[0]<0,'outgoing escape not strictly excluded')
        cuts.append({'indices':c,'max_outgoing_upper_bound':str(bound[0]),
                     'tight_pair':[bound[1],bound[2]]})
    need(len(cuts)>=2 and all(not(set(a['indices'])&set(b['indices']))for i,a in enumerate(cuts)for b in cuts[i+1:]),'sink disjointness')
    # A simple round bound is more convenient for subsequent exact audits.
    simple=Q(1,10)
    simple_components=scc(arcs(polar,len(P),simple,True))[1]
    obj={'status':'EXACT_OWN_CENTRED_PRIMAL_TREE_AND_POLAR_BASIN_CUTS_PASS',
         'input_A_sha256':sha256(raw).hexdigest(),'V_E_F':[35,99,66],
         'strict':[2,1,1],'weak':[0,0,0], 'eta':eta_certificate(X,root),
         'coordinate_bound_convention':'For each vector v_i, every coordinate of its perturbation is <= epsilon*max_k|v_ik| in absolute value. Primal and polar bounds are different spaces; no raw-vertex-to-polar-motion bound is claimed.',
         'primal_U1':{'root':root,'epsilon_certified':str(ulo),'next_grid_unproved':str(uhi),
                      'tree_edges':ptree,'minimum_lower_bound':str(pmin)},
         'polar_at_least_two_S':{'epsilon_certified':str(slo),'next_grid_unproved':str(shi),
                                'sink_cuts':cuts,'one_tenth_sink_count':len(simple_components)},
         'polar_widest_root_paths':[widest_paths(P,r)for r in A['stable_face_ids']],
         'scope':'Sufficient neighborhood certificates only; next grid failures are failures of these bounds, not witnesses. No restriction on a globally redesigned geometry is proved.'}
    b=packed(obj);Path(out).write_bytes(b)
    print(obj['status']);print('primal epsilon',ulo,'polar epsilon',slo,'sink sizes',[len(c['indices'])for c in cuts])
    print('output bytes',len(b),'sha256',sha256(b).hexdigest())
    for rec in obj['polar_widest_root_paths']:
        print('widest root',rec['root'],'bottleneck',float(Q(rec['bottleneck_relative_score'])),'cut size',len(rec['cut']))
if __name__=='__main__':
    if not __debug__:raise RuntimeError('Assertions must remain enabled')
    need(len(sys.argv)==3,'usage: BASIN_GATES.py A.json OUTPUT.json')
    analyse(sys.argv[1],sys.argv[2])
```
