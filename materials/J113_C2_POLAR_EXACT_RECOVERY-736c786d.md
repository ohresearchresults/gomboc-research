# material-736c786d3038

AI research material

---

# J113 — four new own132 homogeneous C2 polar-tree bodies, exact recovery

These are FOUR NEW exact nonwinning bodies, not descendants or aliases of R82, CH95, KF27D or the accepted C622. All have own strict(S,U,H)=(1,3,2), additional weak000 and zero tested primitive equalities. None is own110. The construction began with two twisted polar paths and their C2 partners, followed by literal rational freezing; their actual filled homogeneous centroid, not the reference origin, is used in every reported census.

- C2POLAR_M0_D14_G4: V101/E152/F53,C304. Input integer scale10000; actual centroid(0,0,.03021996951027496 approximately). P depths .9974037743212082 and .0008186513382412203; Q empty.
- C2POLAR_M0_D14_G6: V101/E152/F53,C304. Scale1000000; centroid z approximately .030339648132438644. P depths .9974016153218734 and .0008196087280215534; Q empty.
- C2POLAR_M0_D20_G6: V141/E212/F73,C424. Centroid z approximately .08383436480913958. P depths .9972842821909345 and .0005104616805335512; Q empty.
- C2POLAR_M1_D20_G6: V157/E236/F81,C472. Centroid z approximately .12254769436643397. P depths .9803872428407502 and .00035305289582448455; Q empty.

G4 and G6 are distinct exact objects, not arithmetic aliases. For the two D14 bodies the true U indices are raw-lex0,50,100; the sole S is input0. The dominant P bar is100 to0, its component has27 vertices and cut25 edges; the other bar is the axial degree-four U50 alone, cut4. In D20/M0, U indices0,70,140, dominant component39/cut33. In D20/M1, U indices9,78,147, dominant component37/cut39. The full exact output contains all carrier indices, face lattice, both bars with components/cuts and exact rational depths, not just largest-bar proxies.

The scientific gain is a small-arithmetic alternate S1 architecture beyond the shallow-root capacity barrier, not improved target proximity: its extra physical basin is much deeper than KF27D's. Fixed transverse-affine, joint shape/transverse-affine and symmetry-breaking full-affine numerical scouts did not achieve110; they are not exclusion proofs. Do not prioritize this merely because it is new. Existing whole-basin continuations on the stronger own121/211 frontiers remain active.

## Complete standalone reconstruction
Extract the two FILE blocks verbatim, preserving final LF, into one directory. Run `python -B -S recover113.py OUTPUT_DIRECTORY`. Only CPython standard library is used; executed with CPython3.13.5. No numerical optimizer, old workspace, parent result, compressed data, third-party package or originating sandbox is required. The code reconstructs all six literal inputs (four nonwinners and two controls), executes the exact auditor, checks all twelve input/output hashes and explicitly rejects them as target110.

Observed cold reconstruction ended:
`J113_FOUR_OWN132_NONWINNERS_TWO_CONTROLS_TWELVE_HASHES_PASS`.
Each exact census also ends `EXACT113_HOMOGENEOUS_FULL_CENSUS_PASS` followed by the input identity.

Source manifest:
- exact113.py8656B SHA4f69ceb7be3fd57639a70d7d355505673f922e3f0bdc570659d7c2625d20c315.
- recover113.py6962B SHA05675eee3f0365665b86b3c34a27af196e241b5bec7ae8c252cb128d4a6c6994.
All six input filenames, byte counts and hashes and all six generated exact JSON byte counts/hashes are literal in MANIFEST below. Hashes identify outputs, while the complete integer CASES plus full auditor regenerate them. No coordinate row, incidence or non-default parameter is omitted.

The auditor exhausts all integer H triples; verifies oriented strictly convex maximal facets, closure, Euler, connectivity and boundedness; integrates homogeneous volume/moments at two origins; counts face-foot and polar-vertex S independently inside the same program, physical U, and mixed true-edge saddle cones, including additional weak cases; and computes both complete positive persistence lists with simultaneous processing of equal death levels. This is ONE auditor with internal crosschecks, not two independently authored verifiers. Controls returned tetrahedron446/weak000 and cube6,8,12/weak000. The rational input itself is the construction and requires no reliance on floating nomination predicates.

### FILE recover113.py
```python
"""Exact reconstruction of four new own132 bodies and two non-target controls.
CPython3.13.5 standard library. No numerical optimizer, old sandbox or third-party
package is needed. exact113.py must be supplied beside this complete source.
"""
from pathlib import Path
import hashlib,json,subprocess,sys
CASES = {'C2POLAR_M0_D14_G4': [10000, 14, [[631, -19, 9661], [1323, -79, 9564], [2131, -184, 9377], [3091, -335, 9043], [4203, -526, 8478], [5422, -735, 7586], [6635, -923, 6275], [7661, -1039, 4499], [8272, -1036, 2304], [8244, -895, -141], [7440, -643, -2550], [5874, -353, -4579], [3741, -115, -5929], [1367, 0, -6433]], [[-618, 149, 9657], [-1305, 273, 9559], [-2116, 381, 9370], [-3085, 481, 9033], [-4210, 581, 8466], [-5440, 690, 7571], [-6658, 819, 6257], [-7674, 973, 4481], [-8258, 1139, 2287], [-8190, 1277, -154], [-7343, 1322, -2558], [-5754, 1203, -4583], [-3634, 879, -5930], [-1318, 365, -6433]]], 'C2POLAR_M0_D14_G6': [1000000, 14, [[63092, -1942, 966123], [132312, -7946, 956400], [213126, -18417, 937728], [309055, -33537, 904280], [420322, -52629, 847827], [542191, -73526, 758582], [663457, -92314, 627460], [766063, -103885, 449898], [827152, -103568, 230424], [824428, -89462, -14066], [743972, -64289, -254950], [587376, -35277, -457927], [374077, -11512, -592885], [136731, 0, -643267]], [[-61761, 14944, 965728], [-130532, 27295, 955887], [-211634, 38093, 937032], [-308456, 48093, 903337], [-420980, 58058, 846593], [-544029, 68972, 757059], [-665754, 81897, 625720], [-767416, 97294, 448090], [-825795, 113887, 228749], [-818968, 127688, -15402], [-734323, 132175, -255815], [-575405, 120319, -458322], [-363433, 87935, -592961], [-131766, 36511, -643267]]], 'C2POLAR_M0_D20_G6': [1000000, 20, [[46100, 1191, 936760], [94168, 4811, 931789], [146139, 10979, 923396], [203651, 19834, 910240], [267879, 31430, 890411], [339324, 45615, 861417], [417566, 61901, 820253], [500988, 79354, 763597], [586519, 96543, 688169], [669462, 111594, 591280], [743516, 122385, 471548], [801094, 126889, 329666], [834041, 123641, 169085], [834741, 112214, -3633], [797486, 93569, -178989], [719848, 70108, -345380], [603661, 45352, -490529], [455298, 23259, -603260], [285074, 7368, -675221], [105834, 0, -702165]], [[44282, 12569, 936760], [91136, 23537, 931806], [142455, 33369, 923439], [199856, 42430, 910319], [264485, 51019, 890536], [336785, 59421, 861596], [416214, 67951, 820493], [500958, 76969, 763900], [587663, 86852, 688531], [671288, 97892, 591692], [745190, 110133, 471992], [801526, 123149, 330119], [832083, 135845, 169520], [829469, 146348, -3244], [788523, 152104, -178671], [707628, 150231, -345151], [589555, 138100, -490392], [441527, 114030, -603200], [274395, 77887, -675210], [101076, 31378, -702165]]], 'C2POLAR_M1_D20_G6': [1000000, 20, [[199600, -9601, 909305], [378371, -34689, 826290], [528424, -66847, 711755], [645881, -96247, 574693], [730261, -114510, 424405], [783144, -116701, 269555], [807050, -102094, 117592], [805009, -73803, -25597], [780653, -37551, -155890], [738340, 0, -270962], [682972, 32852, -370065], [619494, 56795, -453626], [552256, 69862, -522795], [484516, 72201, -579082], [418213, 65579, -624116], [354059, 52761, -659497], [291866, 36922, -686701], [230965, 21175, -706990], [170585, 8205, -721341], [110088, 0, -730384]], [[-196569, 40160, 909559], [-376600, 59922, 825937], [-530268, 65596, 710636], [-651358, 65874, 572767], [-737363, 68856, 421738], [-788658, 79760, 266297], [-807579, 99900, 113943], [-797906, 126958, -29416], [-764647, 156221, -159665], [-713740, 182261, -274512], [-651476, 200458, -373254], [-583722, 207960, -456366], [-515200, 203962, -525046], [-449022, 189444, -580841], [-386614, 166622, -625409], [-327953, 138364, -660377], [-272040, 107698, -687234], [-217429, 77462, -707257], [-162682, 50057, -721427], [-106665, 27238, -730384]]]}
MANIFEST = {'C2POLAR_M0_D14_G4.txt': [874, '53d2d66e568161904ed2b66a44190459d70409f96b552a76c1f6316fc210e4b4'], 'C2POLAR_M0_D14_G4.audit.json': [47310, '6c8a912b47b1a5b85724f2c8bcb074b151391a58040fad05bc69fa5320665a26'], 'C2POLAR_M0_D14_G6.txt': [1210, 'df87058bf5be35f667b338c6a835e1e3b00371d62990a171ad0bb9e7c3fe2f91'], 'C2POLAR_M0_D14_G6.audit.json': [64031, 'c52452a727c9d54e9efb491401b351a55af53b627804faffdfa2698dee458e98'], 'C2POLAR_M0_D20_G6.txt': [1726, 'd92ff295840845d14afc3b80ea90568c840f16d9718cbcb2e3ee66a462a475be'], 'C2POLAR_M0_D20_G6.audit.json': [86483, 'de9e20ccd1b1b2dc3693dceaeb0215ea8940e84cb1a01e227b758b65bac6cbcf'], 'C2POLAR_M1_D20_G6.txt': [1755, 'd02591e194ca0f83ebeb8c93979aba1069a7cc6885b46e512537d0fb35befebd'], 'C2POLAR_M1_D20_G6.audit.json': [100639, 'b9aaa00d81b6ac992c4d2de8609e6bb439369b79b41b8829b61cedd62cd9ae03'], 'CONTROL_TETRA.txt': [34, 'cf2999b83c5e867a44e45d99c83d7c39270fa4d082424b5eb79f4d6b0d73c9a0'], 'CONTROL_TETRA.audit.json': [4276, '957a405de0f40cfd82a7b2910c4c86c07ff64dfe3c42e3a011f80c4790592121'], 'CONTROL_CUBE.txt': [43, 'beefbc39c21af35eded2d7a9112c908e6a7812f91b80ccda3dc4f90adb48abe8'], 'CONTROL_CUBE.audit.json': [7595, 'a6946aa5a3b60e93ca3f6a4a092962db6b2d4dd76517e9d78cf45959f17a2248']}

def check(path):
    data=path.read_bytes();assert [len(data),hashlib.sha256(data).hexdigest()]==MANIFEST[path.name],path.name

def main():
    target=Path(sys.argv[1]);target.mkdir(parents=True,exist_ok=True)
    source=Path(__file__).with_name('exact113.py').read_bytes()
    assert len(source)==8656 and hashlib.sha256(source).hexdigest()=='4f69ceb7be3fd57639a70d7d355505673f922e3f0bdc570659d7c2625d20c315'
    (target/'exact113.py').write_bytes(source)
    inputs={}
    for name,(D,m,a,b) in CASES.items():
        assert len(a)==len(b)==m
        N=[[0,0,D]]
        for block in (a,b):
            N.extend(block);N.extend([[-x,-y,z] for x,y,z in block])
        inputs[name]=(D,N)
    inputs['CONTROL_TETRA']=(1,[[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]])
    inputs['CONTROL_CUBE']=(1,[[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]])
    checked=0
    for name,(D,N) in inputs.items():
        path=target/(name+'.txt')
        path.write_text(str(len(N))+' '+str(D)+'\n'+'\n'.join(' '.join(map(str,row)) for row in N)+'\n')
        check(path);checked+=1
        result=subprocess.run([sys.executable,'-B','-S',str(target/'exact113.py'),str(path)],text=True,capture_output=True,check=True)
        assert 'EXACT113_HOMOGENEOUS_FULL_CENSUS_PASS '+name in result.stdout
        output=path.with_suffix('.audit.json');check(output);checked+=1
        a=json.loads(output.read_text());expected=[4,4,6] if name=='CONTROL_TETRA' else [6,8,12] if name=='CONTROL_CUBE' else [1,3,2]
        assert a['strict']==expected and a['additional_weak']==[0,0,0]
        assert all(x==0 for x in a['primitive_zero_counts'].values())
        assert a['strict']!=[1,1,0]
        print(name,a['V'],a['E'],a['F'],a['strict'],a['additional_weak'],flush=True)
    assert checked==12
    print('J113_FOUR_OWN132_NONWINNERS_TWO_CONTROLS_TWELVE_HASHES_PASS')
if __name__=='__main__':main()
```
### FILE exact113.py
```python
"""Standalone exact homogeneous H-polyhedron auditor.
Integer exhaustive triples; Fraction geometry, mass, strict/weak mixed mechanics,
complete simultaneous-level positive primal/polar bars. atan2 only nominates
facet order; exact all-corner inequalities subsequently certify it.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import combinations,groupby
from collections import Counter
from pathlib import Path
import json,math,sys,hashlib
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(t,a):return tuple(t*x for x in a)
def bars(v,edges):
    rr=[dot(x,x) for x in v];items=[]
    for i,j in edges:
        d=sub(v[j],v[i]);t=max(F(0),min(F(1),-dot(v[i],d)/dot(d,d)))
        x=add(v[i],mul(t,d));items.append((dot(x,x),i,j))
    items.sort(reverse=True);par=list(range(len(v)));members=[{i} for i in par];out=[]
    def root(i):
        while par[i]!=i:par[i]=par[par[i]];i=par[i]
        return i
    for level,records in groupby(items,key=lambda x:x[0]):
        adj={}
        for _,i,j in records:
            a,b=root(i),root(j)
            if a!=b:adj.setdefault(a,set()).add(b);adj.setdefault(b,set()).add(a)
        seen=set()
        for start in sorted(adj):
            if start in seen:continue
            seen.add(start);comp=[start]
            for a in comp:
                for b in sorted(adj[a]):
                    if b not in seen:seen.add(b);comp.append(b)
            elder=max(comp,key=lambda i:(rr[i],-i))
            for r in sorted(comp):
                if r==elder:continue
                assert rr[r]>=level
                if rr[r]>level:
                    m=members[r];cut=[list(e) for e in edges if (e[0] in m)!=(e[1] in m)]
                    dep=(rr[r]-level)/rr[r]
                    out.append(dict(root=r,elder=elder,birth=str(rr[r]),death=str(level),depth=str(dep),depth_float=float(dep),component=sorted(m),cut=cut))
            for r in comp:
                if r!=elder:par[r]=elder;members[elder].update(members[r]);members[r]=set()
    assert len({root(i) for i in range(len(v))})==1
    return sorted(out,key=lambda x:(-F(x['depth']),x['root']))

def audit(A,D,name):
    A=[tuple(map(int,a)) for a in A];assert D>0 and len(set(A))==len(A) and all(dot(a,a)>0 for a in A)
    n=len(A);verts={};cr={(i,j):cross(A[i],A[j]) for i,j in combinations(range(n),2)}
    for i,j,k in combinations(range(n),3):
        w=dot(A[i],cr[j,k])
        if not w:continue
        u=tuple(D*(cr[j,k][t]-cr[i,k][t]+cr[i,j][t]) for t in range(3))
        if w<0:w=-w;u=tuple(-x for x in u)
        if all(dot(a,u)<=D*w for a in A):verts.setdefault(tuple(F(x,w) for x in u),None)
    v=sorted(verts);assert len(v)>=4
    inc=[tuple(i for i,a in enumerate(A) if dot(a,x)==D) for x in v]
    faces=[];active=[];avectors=[];edge={};volume=F(0);moment=(F(0),)*3
    for j,norm in enumerate(A):
        ids=[i for i,t in enumerate(inc) if j in t]
        if len(ids)<3:continue
        c=tuple(sum(v[i][k] for i in ids)/len(ids) for k in range(3))
        axis=min(range(3),key=lambda k:abs(norm[k]));unit=tuple(int(k==axis) for k in range(3))
        e=cross(norm,unit);f=cross(norm,e)
        ids.sort(key=lambda i:math.atan2(float(dot(sub(v[i],c),f)),float(dot(sub(v[i],c),e))))
        area=(F(0),)*3;fid=len(faces)
        for a,b in zip(ids,ids[1:]+ids[:1]):
            assert all(dot(cross(sub(v[b],v[a]),sub(v[k],v[a])),norm)>0 for k in ids if k not in(a,b))
            area=add(area,mul(F(1,2),cross(v[a],v[b])))
            edge.setdefault(tuple(sorted((a,b))),[]).append((a,b,fid))
        assert cross(area,norm)==(0,0,0) and dot(area,norm)>0
        for b,cidx in zip(ids[1:-1],ids[2:]):
            a=ids[0];w=dot(v[a],cross(v[b],v[cidx]));assert w>0
            volume+=w/6;moment=add(moment,mul(w/24,add(add(v[a],v[b]),v[cidx])))
        faces.append(ids);active.append(j);avectors.append(area)
    assert len(v)-len(edge)+len(faces)==2
    assert all(len(z)==2 and z[0][:2]==tuple(reversed(z[1][:2])) for z in edge.values())
    assert tuple(sum(a[k] for a in avectors) for k in range(3))==(0,0,0)
    assert any(dot(A[i],cross(A[j],A[k]))!=0 for i,j,k in combinations(active,3))
    # Positive multiples of spanning normals sum to zero: no recession direction.
    neighbours=[set() for _ in v]
    for a,b in edge:neighbours[a].add(b);neighbours[b].add(a)
    seen={0};todo=[0]
    for a in todo:
        for b in neighbours[a]:
            if b not in seen:seen.add(b);todo.append(b)
    assert len(seen)==len(v)
    g=mul(1/volume,moment);p=[sub(x,g) for x in v]
    assert all(dot(a,g)<D for a in A)
    # Independent origin shift in the tetrahedral integration confirms its mass.
    vol2=F(0);m2=(F(0),)*3
    for ids in faces:
        for b,c in zip(ids[1:-1],ids[2:]):
            a=ids[0];w=dot(p[a],cross(p[b],p[c]));assert w>0
            vol2+=w/6;m2=add(m2,mul(w/24,add(add(p[a],p[b]),p[c])))
    assert vol2==volume and m2==(0,0,0)
    strict=[[],[],[]];weak=[[],[],[]];primitive=Counter()
    for i,x in enumerate(p):
        scores=[dot(x,sub(p[j],x)) for j in neighbours[i]]
        primitive['physical_arrow_zeros']+=sum(y==0 for y in scores)
        if max(scores)<0:strict[1].append(i)
        elif max(scores)==0:weak[1].append(i)
    q=[]
    for fid,j in enumerate(active):
        norm=A[j];h=D-dot(norm,g);foot=add(g,mul(h/dot(norm,norm),norm));scores=[]
        for a,b in zip(faces[fid],faces[fid][1:]+faces[fid][:1]):
            scores.append(dot(cross(sub(v[b],v[a]),sub(foot,v[a])),norm))
        if min(scores)>0:strict[0].append(j)
        elif min(scores)==0:weak[0].append(j)
        primitive['face_foot_zeros']+=sum(x==0 for x in scores)
        q.append(mul(1/h,norm))
    qedges=[]
    for (a,b),data in sorted(edge.items()):
        f1,f2=data[0][2],data[1][2];qedges.append(tuple(sorted((f1,f2))))
        d=sub(p[b],p[a]);t=-dot(p[a],d)/dot(d,d);x=add(p[a],mul(t,d))
        n1,n2=A[active[f1]],A[active[f2]];aa,bb,cc=dot(n1,n1),dot(n1,n2),dot(n2,n2);det=aa*cc-bb*bb;assert det>0
        u,w=dot(x,n1),dot(x,n2);lam=(cc*u-bb*w)/det;mu=(aa*w-bb*u)/det
        assert x==add(mul(lam,n1),mul(mu,n2))
        vals=[t,1-t,lam,mu];primitive['edge_mechanical_zeros']+=sum(z==0 for z in vals)
        if min(vals)>0:strict[2].append([a,b])
        elif min(vals)==0:weak[2].append([a,b])
    qadj=[set() for _ in q]
    for a,b in qedges:qadj[a].add(b);qadj[b].add(a)
    polarS=[];polarWeak=[]
    for i,x in enumerate(q):
        scores=[dot(x,sub(q[j],x)) for j in qadj[i]]
        if max(scores)<0:polarS.append(active[i])
        elif max(scores)==0:polarWeak.append(active[i])
    assert polarS==strict[0] and polarWeak==weak[0]
    if not any(weak):assert len(strict[0])+len(strict[1])-len(strict[2])==2
    P=bars(p,sorted(edge));Q=bars(q,sorted(qedges))
    if not any(weak):assert len(P)==len(strict[1])-1 and len(Q)==len(strict[0])-1
    return dict(identity=name,V=len(v),E=len(edge),F=len(faces),C=2*len(edge),strict=[len(x) for x in strict],additional_weak=[len(x) for x in weak],
        strict_carriers=strict,weak_carriers=weak,primitive_zero_counts=dict(primitive),volume=str(volume),centroid=list(map(str,g)),centroid_float=list(map(float,g)),
        input_N=A,input_D=D,raw_vertices=[list(map(str,x)) for x in v],active_input_faces=active,facets=faces,edges=[list(x) for x in sorted(edge)],
        polar_edges=[list(x) for x in sorted(qedges)],P=P,Q=Q,verification='Exhaustive exact H triples; boundedness/closed oriented facets; two-origin exact uniform mass; face feet and polar S agree; physical U and mixed edge cone mechanics; simultaneous-level full P/Q bars. One auditor with internal crosschecks, not two independent auditors.')

def main():
    source=Path(sys.argv[1]);lines=source.read_text().splitlines();n,D=map(int,lines[0].split());A=[tuple(map(int,l.split())) for l in lines[1:]];assert len(A)==n
    result=audit(A,D,source.stem);data=(json.dumps(result,indent=2)+'\n').encode();out=source.with_suffix('.audit.json');out.write_bytes(data)
    print(json.dumps(dict(identity=result['identity'],VEF=[result[x] for x in ['V','E','F']],strict=result['strict'],weak=result['additional_weak'],P=[x['depth_float'] for x in result['P']],Q=[x['depth_float'] for x in result['Q']],centroid=result['centroid_float'],bytes=len(data),sha256=hashlib.sha256(data).hexdigest()),indent=2))
    print('EXACT113_HOMOGENEOUS_FULL_CENSUS_PASS',source.stem)
if __name__=='__main__':main()
```
