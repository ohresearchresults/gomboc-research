# material-4b5d903d00a5

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# CF82 exact connected-affine-component obstruction: complete compact recovery

## Source and dependency
Scientific source is fully read immutable result figure-0446, SHAe33ef3c141a5dee5658263bb371547437a7d1740f14fd649c3c5d9410a59c4e4. Its complete recovered39-file dictionary was authenticated at209355bytes SHA778d9a6a51765315295fa67b8f9bf6abc0c2b9a1f061ab2e3e5f8edc79f50d42. This material preserves the COMPLETE exact affine proof without the unrelated numerical campaign.

Dependency [internal-source-reference],CF82_PRIMARY_RECOVERY.md provides complete exact_addition.py6947bytes SHA130800bb8fd045a0399a04663cb193d728fbc7ed4379a6d5328ea5d4972cc079. Extract that dependency first. Place the three literal files below in the same recovered directory. AFFINE_CONE_COMPACT.py is a dependency-reduced copy of CF82's4989byte AFFINE_CONE.py: its sole change inlines the complete four-line rational support_test instead of importing the larger SF90_EXTRA module. No certificate, scalar, basis or proof logic changed. The original and compact programs were both executed and reproduced the SAME150191byte AFFINE_CONE_REPORT.json SHA5be46de8b7ced1bf53d72ec46ae6a167c83f09945d6227eb7d5e11a3f12c1671. This is source recovery,not another independent mathematical proof.

File receipts: AFFINE_CONE_COMPACT.py5032bytes SHA716c523095c57f14e7b6204f556838d4fcdc5c4c0aa3ecf52a21590d13edc6d5; exact_landscape.py4720bytes SHAe65997173e5eb13d05d15f5a6989b4337be15aec6cc733c1a04468545ae1a964; SF90_CANCEL14_G5.json519bytes SHA8608f8fc284b4b262a510ca205812ae7a1c9c02215fffac46d42cc92733fd57d. The JSON has NO trailing newline; both Python files do. Standard-library-only command, executed CPython3.13.5:
python -B -S AFFINE_CONE_COMPACT.py

Expected markers: CF82_THIRTEEN_CORE_ARROWS_TWELVE_EXACT_DUAL_BOUNDS_PASS; CF82_AFFINE_ALIGNED_HAUSDORFF_LT_1_OVER_40_TWO_S_PASS; CF82_AFFINE_U1_WEAK000_COMPONENT_NO_ESCAPE_PASS98; final AFFINE_REPORT150191 with the hash above.

## Mathematical meaning and limits
At the ACTUAL uniformly filled centroid of literal SF90_CANCEL14_G5, impose13closed core arrow inequalities x_i^T G(x_(i+1)-x_i)>=0, i2..14, on a real symmetric trace3 Gram matrixG. Twelve exact Farkas certificates,each five core rows+trace, bound all six entries. The largest absolute row-sum displacement rho is<13/1000,soG is automaticallySPD. Its canonical positive square root lies within rho ofI; parentcircumradius<47/25 gives centred Hausdorffdistance<611/25000<1/40. The fully reconstructed polar elder bar proves1/40 lies inside the parent's two-stable protection radius. Every affine image in this closed cone therefore hasS>=2 at its actual transformed uniform centroid.

Exact interval evaluation excludes98of99 non-tree directed true-edge arrows everywhere in the cone; only21→8 remains unexcluded. Every alternative at corevertices2..14 is strictly negative,as is every outgoingroot0arrow. A continuous invertible affine path from the parent retaining strictU1/additionalweak000 cannot leave: at the first core-arrow zero it creates an additional weak unstable vertex while root0 stays strictly unstable. Thus this CONNECTED affine U1/weak000 component contains noS1. This is not merely a fixed-tree assumption. It does NOT exclude disconnected affine components,finite jumps,paths with extraU/weak,nonlinear changes,added/removedsupports,or the new CF82_RESERVE42/83 families. No new110 body or global lower complexity bound is claimed.

The protection step uses the entire polar strict-upper basin and its complete boundary cut,not one chosen tree arrow. For an interior-centred polyhedron, a spherical local minimum of its support function is a strict stable facet equilibrium; a facet-boundary foot has a decreasing tangent direction and is not a local minimum. Uniform support perturbation less than half the basin's support-height gap preserves two separated local minima. Similarity normalisation does not change own counts; actual uniform centroids transform affinely. These are the geometric premises of the certificate.

### FILE SF90_CANCEL14_G5.json
```json
{"grid":100000,"points":[[-128702,111000,-81448],[75454,8233,-44869],[88555,30801,-26906],[96197,34302,-1099],[102483,17928,19180],[104196,-4245,29526],[102344,-27902,30809],[94465,-48113,38103],[82466,-64625,47068],[68073,-73028,61732],[50165,-79867,74146],[29330,-84384,84017],[6282,-86581,90380],[-18196,-85926,93159],[-43393,-82400,91865],[-68527,-75886,86133],[-92679,-66207,75654],[-115265,-51560,60999],[-134788,-31191,41506],[-149173,-3231,16029],[-153688,35949,-18400],[3128,-12816,-12288],[-558,11161,10728]]}
```

### FILE AFFINE_CONE_COMPACT.py
```python
"""Exact trace-normalized affine-component obstruction for SF90_CANCEL14_G5.
Python standard library; no optimizer or numerical eigensolver in verification.
The thirteen inequalities indexed 1..13 below are physical arrows 2->3,...,14->15.
Each bound is a Farkas certificate, reconstructed from six exact basis rows.
"""
import json,sys,hashlib
from fractions import Fraction as F
from pathlib import Path
from exact_addition import audit,dot,sub,encode
from exact_landscape import run as landscape
def support_test(e,b,d):
 B=1/b;D=1/d;q=D-B-4*e*e
 return q>0 and q*q>16*e*e*B
ROOT=Path(__file__).resolve().parent
PARENT='SF90_CANCEL14_G5.json'
BASES=[[1,3,4,11,13],[1,2,6,11,12],[1,2,6,12,13],[1,2,3,9,11],
 [2,5,6,11,12],[1,4,6,12,13],[1,2,6,10,11],[2,3,5,12,13],
 [1,2,6,8,9],[2,3,5,12,13],[1,2,6,12,13],[1,3,4,7,11]]

def solve(A,b):
 A=[list(map(F,r))+[F(v)] for r,v in zip(A,b)];n=len(b)
 for k in range(n):
  r=next(i for i in range(k,n) if A[i][k]);A[k],A[r]=A[r],A[k]
  z=A[k][k];A[k]=[x/z for x in A[k]]
  for i in range(n):
   if i!=k:
    z=A[i][k];A[i]=[x-z*y for x,y in zip(A[i],A[k])]
 return [r[-1] for r in A]

def coeff(x,d):return [x[0]*d[0],x[1]*d[1],x[2]*d[2],x[0]*d[1]+x[1]*d[0],x[0]*d[2]+x[2]*d[0],x[1]*d[2]+x[2]*d[1]]

def run():
 raw=(ROOT/PARENT).read_bytes();assert len(raw)==519 and hashlib.sha256(raw).hexdigest()=='8608f8fc284b4b262a510ca205812ae7a1c9c02215fffac46d42cc92733fd57d'
 d=json.loads(raw);A=audit(d['points'],d['grid']);L=landscape(d)
 assert A['strict']==[2,1,1] and A['weak']==A['primitive_zeros']==[0,0,0]
 X=[sub(tuple(F(x,d['grid']) for x in p),A['centroid']) for p in d['points']]
 tree=[(i,i+1) for i in range(1,20)]+[(20,0),(21,1)]
 C=[coeff(X[i],sub(X[j],X[i])) for i,j in tree];tr=[F(1)]*3+[F(0)]*3
 cert=[];bounds=[]
 for k in range(6):
  values=[]
  for sign in [1,-1]:
   ids=BASES[2*k+(sign==-1)];assert all(1<=i<=13 for i in ids)
   B=[C[i] for i in ids]+[tr];c=[F(0)]*6;c[k]=F(sign)
   v=solve(B,[0]*5+[3]);y=solve(list(map(list,zip(*B))),c)
   assert min(y[:5])>=0
   assert all(sum(y[j]*B[j][i] for j in range(6))==c[i] for i in range(6))
   assert all(dot(row,v)>=0 for row in C[1:14]) and dot(tr,v)==3
   assert dot(c,v)==3*y[-1]
   values.append(v[k]);cert.append(dict(coordinate=k,minimization_sign=sign,core_basis=ids,dual=y,attaining_vertex=v,bound=v[k]))
  bounds.append(values)
 delta=[max(abs(lo-(k<3)),abs(hi-(k<3))) for k,(lo,hi) in enumerate(bounds)]
 rho=max(delta[0]+delta[3]+delta[4],delta[1]+delta[3]+delta[5],delta[2]+delta[4]+delta[5])
 R2=max(dot(X[i],X[i]) for i in A['active_inputs'])
 assert rho<F(13,1000) and R2<F(47,25)**2
 # Symmetric G: ||G-I||_2 <= ||G-I||_infinity <= rho < 1.
 # Hence G is SPD and ||sqrt(G)-I||_2 <= rho/(1+sqrt(1-rho)) < rho.
 # Matching each convex-combination point to its linear image proves the upper bound.
 Dupper=F(13,1000)*F(47,25);assert Dupper<F(1,40)
 assert len(L['Q']['bars'])==1
 bar=L['Q']['bars'][0];assert support_test(F(1,40),bar['birth'],bar['death'])
 neg=[];unexcluded=[]
 for e in A['edges']:
  for i,j in [e,e[::-1]]:
   if (i,j) in tree:continue
   c=coeff(X[i],sub(X[j],X[i]));upper=sum(t*b[int(t>=0)] for t,b in zip(c,bounds))
   (neg if upper<0 else unexcluded).append(dict(arrow=[i,j],box_upper=upper))
 assert len(neg)==98 and [v['arrow'] for v in unexcluded]==[[21,8]]
 # In particular all alternatives to each core arrow and every root-0 arrow
 # remain strictly negative throughout the closed core cone, including its boundary.
 for i in list(range(2,15))+[0]:
  for e in A['edges']:
   if i not in e:continue
   j=e[0] if e[1]==i else e[1]
   if i and j==i+1:continue
   assert any(v['arrow']==[i,j] for v in neg)
 result=dict(parent_sha256=hashlib.sha256(raw).hexdigest(),core_arrows=tree[1:14],trace=3,
  certificates=cert,coordinate_bounds=bounds,rho=rho,R2=R2,Hausdorff_strict_upper=Dupper,
  support_exclusion_radius=F(1,40),excluded_other_directed_edges=neg,unexcluded_other_edges=unexcluded,
  conclusions=['Every real symmetric trace-three G satisfying the thirteen closed core escape inequalities is SPD and lies in the certified entry box.',
   'Every affine image whose normalized Gram matrix is in this cone has at least two strict stable equilibria at its actual uniform-volume centroid.',
   'A continuous affine path from the parent retaining own U1 and additionalweak000 cannot leave this cone: first exit makes a core vertex weak-unstable while input0 remains strictly unstable.',
   'No assertion about disconnected affine U1 components, nonlinear deformations, support changes, or finite jumps outside the cone.'])
 payload=(json.dumps(encode(result),sort_keys=True,separators=(',',':'))+'\n').encode();(ROOT/'AFFINE_CONE_REPORT.json').write_bytes(payload)
 print('CF82_THIRTEEN_CORE_ARROWS_TWELVE_EXACT_DUAL_BOUNDS_PASS')
 print('CF82_AFFINE_ALIGNED_HAUSDORFF_LT_1_OVER_40_TWO_S_PASS')
 print('CF82_AFFINE_U1_WEAK000_COMPONENT_NO_ESCAPE_PASS',len(neg))
 print('AFFINE_REPORT',len(payload),hashlib.sha256(payload).hexdigest())
 return result
if __name__=='__main__':run()
```

### FILE exact_landscape.py
```python
"""Exact full primal/polar elder bars, attaining paths and complete cuts.
Q is the polar at P's physical volume centroid, never independently recentered.
Dependency: exact_addition.py. Python standard library only.
"""
from fractions import Fraction as F
from collections import deque
from pathlib import Path
import json,sys,hashlib
from exact_addition import audit,encode,dot,sub,add,mul
SCALE=10**12

def floor_cube_root(n):
    assert n>=0
    lo,hi=0,1<<((n.bit_length()+2)//3)
    while lo+1<hi:
        m=(lo+hi)//2
        if m**3<=n:lo=m
        else:hi=m
    return lo

def cube_bracket(r):
    """Enclose the positive cube root of an exact rational, no float."""
    assert r>=0
    z=floor_cube_root((r.numerator*SCALE**3)//r.denominator)
    assert F(z**3,SCALE**3)<=r<F((z+1)**3,SCALE**3)
    return [z,z+1]

def landscape(points,edges):
    radius={i:dot(p,p) for i,p in points.items()};adj={i:[] for i in points};events=[]
    for i,j in sorted(edges):
        d=sub(points[j],points[i]);dd=dot(d,d);assert dd>0
        t=min(F(1),max(F(0),-dot(points[i],d)/dd))
        p=add(points[i],mul(d,t));h=dot(p,p)
        assert h<=min(radius[i],radius[j])
        events.append((h,i,j));adj[i].append((j,h));adj[j].append((i,h))
    parent={i:i for i in points}
    def find(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    bars=[]
    for death,i,j in sorted(events,reverse=True):
        a,b=find(i),find(j)
        if a==b:continue
        if (radius[a],-a)<(radius[b],-b):a,b=b,a
        delta=radius[b]-death;assert delta>=0
        if delta>0:
            cut={b};todo=[b]
            while todo:
                k=todo.pop()
                for v,h in adj[k]:
                    if h>death and v not in cut:cut.add(v);todo.append(v)
            assert a not in cut
            boundary=sorted((u,v) for u in cut for v,h in adj[u] if v not in cut)
            assert boundary and all(h<=death for u in cut for v,h in adj[u] if v not in cut)
            pred={b:None};todo=deque([b])
            while todo and a not in pred:
                k=todo.popleft()
                for v,h in sorted(adj[k]):
                    if h>=death and v not in pred:pred[v]=k;todo.append(v)
            assert a in pred
            path=[a]
            while path[-1]!=b:path.append(pred[path[-1]])
            path.reverse()
            assert min(next(h for v,h in adj[u] if v==w) for u,w in zip(path,path[1:]))==death
            bars.append(dict(peak=b,elder=a,death_edge=[i,j],birth=radius[b],death=death,depth=delta,path=path,component=sorted(cut),boundary=boundary))
        parent[b]=a
    roots=sorted(i for i,p in points.items() if all(dot(p,sub(points[j],p))<0 for j,h in adj[i]))
    assert len(bars)==len(roots)-1
    global_root=max(points,key=lambda i:(radius[i],-i));hinge=F(0)
    for i,p in points.items():
        if i==global_root:continue
        terms=[(dot(p,sub(q,p)),dot(sub(q,p),sub(q,p))) for j,q in points.items() if j!=i]
        if all(v<0 for v,dd in terms):hinge+=min(v*v/(radius[i]*dd) for v,dd in terms)
    return dict(roots=roots,bars=bars,radius2=max(radius.values()),sum_depth=sum((b['depth'] for b in bars),F(0)),root_exempt_allpoint_cosine_hinge_sum=hinge)

def run(d):
    A=audit(d['points'],d['grid']);assert A['weak']==[0,0,0]
    P={i:sub(tuple(F(x,d['grid']) for x in d['points'][i]),A['centroid']) for i in A['active_inputs']}
    Q={i:mul(f['n'],1/(F(f['h'],d['grid'])-dot(f['n'],A['centroid']))) for i,f in enumerate(A['faces'])}
    owners={}
    for i,f in enumerate(A['faces']):
        c=f['cycle']
        for u,v in zip(c,c[1:]+c[:1]):owners.setdefault(tuple(sorted((u,v))),[]).append(i)
    assert all(len(v)==2 for v in owners.values())
    Lp=landscape(P,A['edges']);Lq=landscape(Q,list(map(tuple,owners.values())))
    assert Lp['roots']==A['U'] and Lq['roots']==A['S']
    V=A['volume'];pc=Lp['sum_depth']**3/V**2;qc=Lq['sum_depth']**3*V**2
    return dict(V=A['V'],E=A['E'],F=A['F'],strict=A['strict'],weak=A['weak'],volume=V,P=Lp,Q=Lq,
       TP_cube=pc,TQ_cube=qc,TP_bracket_1e12=cube_bracket(pc),TQ_bracket_1e12=cube_bracket(qc),
       relative_P_bracket_1e12=[int(Lp['sum_depth']/Lp['radius2']*SCALE),int(Lp['sum_depth']/Lp['radius2']*SCALE)+1],
       relative_Q_bracket_1e12=[int(Lq['sum_depth']/Lq['radius2']*SCALE),int(Lq['sum_depth']/Lq['radius2']*SCALE)+1])

if __name__=='__main__':
    d=json.loads(Path(sys.argv[1]).read_text());r=run(d)
    raw=(json.dumps(encode(r),sort_keys=True,indent=2)+'\n').encode()
    out=Path(sys.argv[2]);out.write_bytes(raw)
    print('C114_EXACT_FULL_ELDER_PATH_CUT_PASS',r['strict'],r['TP_bracket_1e12'],r['TQ_bracket_1e12'],len(raw),hashlib.sha256(raw).hexdigest())
```
