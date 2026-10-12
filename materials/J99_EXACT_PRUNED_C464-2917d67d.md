# material-2917d67d1757

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J99 exact rational vertex-subset construction — useful own211, NOT the target

Identity J99_R82_PRUNED25_C464. Starting from the literal KH93_C434_R82_G6 body in parent figure-0581, delete exactly the 25 vertices omitted by the complete retained support-triple list below. This is a new homogeneous body, not a new name for R82. The complete exact audit executed under CPython3.13.5 standard library only: V135/E232/F99, C464; strict(S,U,H)=(2,1,1), additionalweak000, zero directed primal/polar chord equalities. P is empty; the only Q depth lies strictly between115971537954088/10^15 and115971537954089/10^15. Stable facet indices57 and69 in THIS supplied face list are a quadrilateral on original support7 and a20-gon on original support18. U is localvertex15, H is localedge4--75. Do not confuse these local vertex labels with the parent's canonical auditor ordering. Exact own volume lies in(1712489400170296,1712489400170297)/10^15. Own centroid coordinates lie in(24961603351134,24961603351135), (3206153552545,3206153552546), (-6772303543692,-6772303543691), all divided by10^15. Maximum centroid denominator bit length13679. Degrees:93 degree3,31 degree4,6 degree5,4 degree6,1 degree7. Compared with R82 this frees8 true edges and reduces vertices by25, with almost unchanged shallow Q; it increases F82 to99 and therefore does NOT inherit the universal three-extra-H guarantee.

The exact audit reconstructs rational vertices from the integer planes; verifies every old input support and every complete new maximal supporting face, strict polygon convexity, oriented manifold edges and connectedness; integrates positive tetrahedra; recomputes the own-centred polar; counts all strict and additional weak face/vertex/edge equilibria; and computes every positive primal/polar zero-dimensional radial bar without a cutoff. A second tetrahedral sum based at the computed centroid gives the same volume and exactly zero first moments. This is the coordinator's exact computation, not an independent replay of a worker claim. The new object is not own110 and does not replace canonical accepted C622.

## Recovery and verification
Save this material unchanged as J99_EXACT_PRUNED_C464.md. Extract the three complete FILE fences with the following standard-library command, then run the audit:

```sh
python -c 'import pathlib,re; s=pathlib.Path("J99_EXACT_PRUNED_C464.md").read_text(); fs=re.findall(r"^## FILE ([^\n]+)\n```[^\n]*\n(.*?)^```",s,re.M|re.S); assert len(fs)==3; [(pathlib.Path(n).write_text(t)) for n,t in fs]'
python -B -S exact99.py J99_PRUNED25_INPUT.json
```

Expected terminal marker: J99_EXACT_VERTEX_SUBSET_AUDIT_PASS J99_R82_PRUNED25_C464 135 232 99 [2, 1, 1] [0, 0, 0] [0, 0].
Input manifest: KH93_C434_R82_G6.txt1888B SHA9765712b5ffaa464ed4d677974256294c6d867b77fe77b930d166853f66a92a7; J99_PRUNED25_INPUT.json3684B SHAd67d882bfee515e445afdccda95668c259b83b1ae2d14af1f760899a56b4f36c; exact99.py6606B SHA62590494bd5c9e01368ce20336f2eb8c93b9dac8f0e7a9c0ea5f7da300e7d135. Output J99_PRUNED25_INPUT_EXACT.json79729B SHA837ab88566e63c06f2729a5470c463da3b9a8ab663a5a79bd57f0de1e06ebe19. The output contains all exact fractions and all positive bars. Hashes identify these complete sources and regenerated outputs; they are not substitutes for the literal inputs below.

## FILE KH93_C434_R82_G6.txt
```text
82 1000000
-725174 1362065 699290
-876644 1271151 690615
-1099310 1231174 294886
-817964 1365431 563226
-1081003 1264128 151488
-621649 1353152 816931
-910427 1348627 429305
-518139 1328018 931336
-1150535 1200456 6778
-1020626 1165129 671462
-1000361 1313225 295844
-1194316 1138885 290932
-1092629 1226455 -152925
-1154723 1038071 651530
-1018232 1244394 -303529
-826413 1255634 -573231
-413284 1274995 1033847
-712036 1248759 -690383
-565903 -2054257 -854847
-307427 1210004 1127958
-587643 1233564 -794247
-200527 1134456 1212109
-455233 1210233 -883762
-928979 1254154 -443961
-92885 1049729 1285004
-316806 1179053 -958168
-193819 -1291659 -912554
18238 952579 1348058
-174313 1140389 -1016977
-5177 -1016438 -923390
126983 847597 1397922
-11369 1085575 -1065309
231228 735671 1434828
330275 -1762331 162369
151779 1022336 -1093263
30004 1300793 -698627
219511 -659625 -911359
322219 610162 1464118
1094885 47914 75899
412797 485892 1476567
312873 951248 -1101019
394488 -437948 -877153
372181 573535 -1047196
751040 -363347 1338736
494318 358585 1477376
482341 -441422 -830169
502322 597143 -1020344
986434 79237 -460427
565401 225769 1467982
1050351 419486 112141
1083749 -76462 20200
570962 315730 -946952
315382 1317869 -337108
631111 96499 1445527
618364 -68927 -830846
685954 -34720 1413641
769199 -342229 -602838
779840 -1029259 1003128
816852 -402173 -515337
803000 -801799 1145327
813560 70446 -729507
796119 -578783 1253080
873889 -555249 -338841
940788 -543762 -95731
905170 -119352 -513537
748587 944500 20227
956411 -355836 -265735
889363 454940 -604392
917283 703683 114724
1033644 -185828 -146671
1044375 -230785 26003
1003015 537275 125496
1077079 104258 162986
1081632 235703 135814
1081426 316201 94169
570808 -432037 -763436
714032 -374886 -651118
654625 -473702 -663065
648347 -407882 -703531
589983 -1511107 549377
727139 -1270183 798804
579789 -1442685 583018
```

## FILE J99_PRUNED25_INPUT.json
```json
{"identity":"J99_R82_PRUNED25_C464","retained_incident_supports":[[40,65,67],[11,13,18],[13,43,59],[13,57,59],[43,53,55],[8,11,18],[8,12,18],[18,28,31],[49,53,55],[50,57,70],[38,50,59],[50,57,59],[57,79,80],[57,70,80],[13,18,33],[13,33,79],[18,33,62],[33,62,79],[13,57,81],[43,59,61],[38,59,61],[38,61,72],[15,17,18],[15,18,23],[12,14,18],[14,18,23],[18,34,40],[18,31,34],[17,18,20],[18,20,22],[18,25,28],[18,22,25],[18,26,40],[26,29,40],[29,40,42],[18,29,45],[46,60,67],[46,51,60],[40,46,67],[36,46,51],[29,36,46],[29,42,46],[49,67,74],[49,55,74],[65,67,68],[47,60,67],[38,47,50],[38,47,74],[47,67,74],[47,50,69],[63,70,80],[63,69,70],[62,63,79],[63,79,80],[18,62,77],[58,62,77],[9,11,13],[13,21,24],[24,27,65],[27,30,65],[13,24,27],[13,27,30],[30,32,65],[30,32,37],[32,65,68],[32,37,68],[1,7,9],[7,9,13],[45,54,60],[45,51,54],[36,41,51],[41,45,51],[60,75,78],[45,60,75],[18,75,77],[43,55,73],[55,73,74],[43,61,73],[61,72,73],[38,73,74],[49,67,71],[67,68,71],[49,53,71],[44,68,71],[62,63,66],[63,66,69],[47,62,66],[47,66,69],[60,76,78],[58,76,77],[47,62,64],[58,62,64],[47,60,64],[58,60,64],[13,19,21],[13,16,19],[37,39,68],[39,44,68],[13,37,39],[48,53,71],[44,48,71],[43,48,53],[43,44,48],[56,58,60],[56,60,76],[56,58,76],[0,1,3],[1,3,6],[0,1,5],[4,8,11],[2,4,11],[4,8,12],[0,5,52],[0,3,52],[5,7,52],[7,16,52],[40,52,65],[16,19,52],[19,21,52],[24,52,65],[2,6,10],[2,4,10],[4,10,14],[6,10,23],[3,35,52],[15,17,35],[17,20,35],[6,15,35],[20,22,35],[22,25,35],[25,28,35],[28,31,35],[31,34,35],[34,35,40],[35,40,52]],"retained_original_indices":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,20,21,22,23,25,26,27,28,29,30,31,32,33,34,35,37,38,40,41,42,43,45,46,47,48,49,50,51,52,53,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,78,79,80,82,83,84,87,88,89,90,91,93,94,95,96,97,99,100,101,102,103,105,106,107,108,109,110,111,112,113,114,116,117,118,119,120,121,122,123,125,129,130,131,132,134,135,136,137,138,139,140,141,143,144,145,147,148,149,150,151,153,154,155,156,157,158,159],"faces":[[66,56,67],[107,56,66],[120,56,107],[123,23,25],[123,25,122],[25,24,122],[112,108,114],[108,66,114],[98,2,102],[63,61,98],[97,96,98],[102,97,98],[118,57,119],[94,57,118],[121,110,120],[110,56,120],[24,6,111],[122,24,111],[127,23,123],[127,107,124],[41,34,38],[69,37,68],[74,35,73],[115,67,95],[115,95,117],[78,21,79],[35,32,33],[15,12,18],[49,9,51],[73,72,74],[71,35,70],[40,39,70],[70,35,40],[104,103,105],[74,72,88],[89,74,88],[122,121,120,123],[132,133,26,27],[27,7,131,132],[130,131,7,30],[17,15,14,16],[117,95,94,118],[96,65,63,98],[62,59,61,63],[4,101,102,2,19,77,75],[78,77,19,20,21],[107,106,113,124],[107,66,108,106],[112,113,106,108],[5,1,56,110,109],[122,111,109,110,121],[6,5,109,111],[127,125,22,23],[123,120,107,127],[61,60,57,94,95,67,56,1,14,15,18,3,2,98],[20,19,2,3,11,10],[116,134,124,113,112,114,115,117,118,119],[114,66,67,115],[97,83,81,44,64,65,96],[65,64,62,63],[62,64,44,0,116,119,58,59],[58,119,57,60],[59,58,60,61],[102,100,83,97],[101,99,100,102],[99,101,4,8,82],[99,82,80,81,83,100],[79,21,20,10,46,47],[80,82,8,43,42],[35,74,54,16,14,1,5,6,24,25,23,22,28,29,31,30,7,27,26,32],[28,22,125,126],[29,28,126,128],[131,130,129,128,126,125,127,124,134,133,132],[129,130,30,31],[31,29,128,129],[26,133,134,116,0,38,34,33,32],[50,13,12,53],[13,9,11,3,18,12],[51,9,13,50],[10,11,9,49,46],[43,8,4,75,76],[79,76,75,77,78],[79,47,48,42,43,76],[45,36,38,0,44,81,80,42,48],[68,73,35,71,69],[41,38,36,37,39,40],[35,33,34,41,40],[52,53,12,15,17],[87,86,90,92,45,48,47,46,49],[92,90,91,93],[84,52,17,16,54,55,91,90,86],[70,39,37,69,71],[84,85,51,50,53,52],[87,49,51,85],[87,85,84,86],[88,72,73,68,37,36,45,92,93,103,104],[93,91,55,89,105,103],[89,88,104,105],[89,55,54,74]]}
```

## FILE exact99.py
```python
"""Exact source-only audit of rational R82 vertex-subset bodies.
Input is a complete retained support-triple list and a closed oriented face lattice.
No floating point or bar floor is used. All geometry and mass are reconstructed.
"""
from fractions import Fraction as F
from pathlib import Path
from collections import deque
import json,hashlib,sys
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(t,a):return tuple(t*x for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def meet(a,b,c,D):
    den=det(a,b,c);assert den
    return mul(F(D,den),add(add(cross(b,c),cross(c,a)),cross(a,b)))
def segment(a,b):
    d=sub(b,a);dd=dot(d,d);assert dd>0
    t=max(F(0),min(F(1),-dot(a,d)/dd));f=add(a,mul(t,d));return dot(f,f)
def bars(p,edges):
    r=[dot(x,x)for x in p];ev=[(x,0,i)for i,x in enumerate(r)]
    for i,(a,b)in enumerate(edges):ev.append((segment(p[a],p[b]),1,i))
    ev.sort(key=lambda z:(-z[0],z[1],z[2]));par=list(range(len(p)));root=par[:];out=[]
    def find(i):
        while par[i]!=i:par[i]=par[par[i]];i=par[i]
        return i
    for value,typ,k in ev:
        if typ==0:continue
        a,b=map(find,edges[k])
        if a==b:continue
        if r[root[a]]<r[root[b]]:a,b=b,a
        dep=1-value/r[root[b]];assert dep>=0
        if dep>0:out.append(dict(root=root[b],edge=list(edges[k]),birth2=r[root[b]],death2=value,depth=dep))
        par[b]=a
    return sorted(out,key=lambda z:-z['depth'])
def interval(x,d=10**15):
    k=x.numerator*d//x.denominator
    return dict(lower=k,upper=k+1,denominator=d,strict_lower=x>F(k,d),strict_upper=x<F(k+1,d))
def main(specpath):
    folder=Path(__file__).parent;raw=(folder/'KH93_C434_R82_G6.txt').read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='9765712b5ffaa464ed4d677974256294c6d867b77fe77b930d166853f66a92a7'
    lines=raw.decode().splitlines();N,D=map(int,lines[0].split());old=[tuple(map(int,l.split()))for l in lines[1:]];assert N==len(old)==82
    specraw=specpath.read_bytes();spec=json.loads(specraw);triples=spec['retained_incident_supports'];faces=spec['faces']
    v=[meet(*(old[i]for i in tt),D)for tt in triples];assert len(set(v))==len(v)
    for p,tt in zip(v,triples):assert all(dot(n,p)<=D for n in old)and set(tt)=={i for i,n in enumerate(old)if dot(n,p)==D}
    W=F(0);T=(F(0),)*3;ef={};planes=[]
    for k,f in enumerate(faces):
        assert len(set(f))==len(f)>=3
        a,b,c=[v[i]for i in f[:3]];n=cross(sub(b,a),sub(c,a));h=dot(n,a);assert h>0
        assert {i for i,x in enumerate(v)if dot(n,x)==h}==set(f)
        assert all(dot(n,x)<=h for x in v)
        # Every listed polygon is the entire strictly convex supporting facet.
        for j,i in enumerate(f):
            nxt=f[(j+1)%len(f)];d=sub(v[nxt],v[i])
            for z in f:
                if z not in(i,nxt):assert dot(cross(d,sub(v[z],v[i])),n)>0
            ef.setdefault(tuple(sorted((i,nxt))),[]).append((k,i,nxt))
        planes.append((n,h))
        for j in range(1,len(f)-1):
            a,b,c=[v[i]for i in(f[0],f[j],f[j+1])];w=det(a,b,c);assert w>0
            W+=w;T=add(T,mul(w,add(add(a,b),c)))
    E=sorted(ef);assert len(v)-len(E)+len(faces)==2
    for e,ff in ef.items():assert len(ff)==2 and ff[0][1:]==tuple(reversed(ff[1][1:]))
    adj=[[]for _ in v]
    for a,b in E:adj[a].append(b);adj[b].append(a)
    seen={0};todo=deque([0])
    while todo:
        for j in adj[todo.popleft()]:
            if j not in seen:seen.add(j);todo.append(j)
    assert len(seen)==len(v)
    V=W/6;g=mul(1/(4*W),T);p=[sub(x,g)for x in v]
    q=[]
    for n,h in planes:
        off=h-dot(n,g);assert off>0;q.append(mul(1/off,n))
    QE=[(ff[0][0],ff[1][0])for ff in ef.values()]
    def census(x,e):
        vals=[[]for _ in x];zeros=0
        for a,b in e:
            d=sub(x[b],x[a]);aa=dot(x[a],d);bb=-dot(x[b],d)
            vals[a].append(aa);vals[b].append(bb);zeros+=(aa==0)+(bb==0)
        strict=[i for i,t in enumerate(vals)if max(t)<0]
        weak=[i for i,t in enumerate(vals)if max(t)==0]
        return strict,weak,zeros,vals
    U,wU,zP,pvals=census(p,E);S,wS,zQ,qvals=census(q,QE);H=[];wH=[]
    for a,b in E:
        d=sub(p[b],p[a]);t=-dot(p[a],d)/dot(d,d)
        if not 0<=t<=1:continue
        foot=add(p[a],mul(t,d));i,j=[f[0]for f in ef[a,b]];n,m=q[i],q[j]
        A=dot(n,n);B=dot(n,m);C=dot(m,m);D2=A*C-B*B;assert D2>0
        alpha=(dot(foot,n)*C-dot(foot,m)*B)/D2
        beta=(dot(foot,m)*A-dot(foot,n)*B)/D2
        assert add(mul(alpha,n),mul(beta,m))==foot
        if alpha>=0 and beta>=0:
            if 0<t<1 and alpha>0 and beta>0:H.append([a,b])
            else:wH.append([a,b])
    assert len(S)+len(U)-len(H)==2
    P=bars(p,E);Q=bars(q,QE)
    assert len(P)==len(U)-1 and len(Q)==len(S)-1
    # Independent positive tetrahedra based at the computed interior centroid.
    WW=F(0);TT=(F(0),)*3
    for f in faces:
        for j in range(1,len(f)-1):
            a,b,c=[p[i]for i in(f[0],f[j],f[j+1])];w=det(a,b,c);assert w>0
            WW+=w;TT=add(TT,mul(w,add(add(a,b),c)))
    assert WW==W and TT==(0,0,0)
    out=dict(identity=spec['identity'],source_sha256=hashlib.sha256(specraw).hexdigest(),V=len(v),E=len(E),F=len(faces),C=2*len(E),
             strict=[len(S),len(U),len(H)],additional_weak=[len(wS),len(wU),len(wH)],primitive_chord_zeros=[zP,zQ],
             S=S,U=U,H=H,weakS=wS,weakU=wU,weakH=wH,volume=str(V),centroid=[str(x)for x in g],
             volume_interval=interval(V),centroid_intervals=[interval(x)for x in g],
             P=[{**z,**{k:str(z[k])for k in ['birth2','death2','depth']},'depth_interval':interval(z['depth'])}for z in P],
             Q=[{**z,**{k:str(z[k])for k in ['birth2','death2','depth']},'depth_interval':interval(z['depth'])}for z in Q],
             maximum_centroid_denominator_bits=max(x.denominator.bit_length()for x in g),evidence='EXACT_OWN_MASS_AND_FULL_STRICT_WEAK_CENSUS_NOT_110')
    dest=specpath.with_name(specpath.stem+'_EXACT.json');text=json.dumps(out,indent=2)+'\n';dest.write_text(text)
    print('J99_EXACT_VERTEX_SUBSET_AUDIT_PASS',out['identity'],out['V'],out['E'],out['F'],out['strict'],out['additional_weak'],out['primitive_chord_zeros'],flush=True)
    print('P_DEPTHS',[float(z['depth'])for z in P],'Q_DEPTHS',[float(z['depth'])for z in Q],flush=True)
    print('OUTPUT',dest.name,len(text.encode()),hashlib.sha256(text.encode()).hexdigest(),flush=True)
if __name__=='__main__':main(Path(sys.argv[1]))
```
