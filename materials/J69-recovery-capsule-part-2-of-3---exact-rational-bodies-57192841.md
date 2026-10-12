# material-571928413b05

AI research material

---

# Recovery capsule part 2/3 — J69 exact nonrecord bodies

These are new, distinct rational bodies derived by cap-preserving rounding of the protected floating checkpoint, NOT aliases of JOINT56 L18 or F18. Both are homogeneous, use their own exact volume centroid, have V75/E204/F131/C408, strict(S,U,H)=(2,2,2), and weak=(0,0,0). They are useful nonrecords, not target110. This part alone suffices for their exact reconstruction and census; no NumPy, Qhull, earlier sandbox or external geometry is required for exact69.py.

Names: J69_PROTECTED_R7_D10 has common denominator10^10, with non-cap coordinate parameter denominator10^7. J69_PROTECTED_R12_D15 has common denominator10^15 and parameter denominator10^12. Coordinates are the complete integer rows below divided by the named denominator. The18 cap points retain y=-.272x-.409z-.68526367 exactly. For R7_D10 the floating complete-bar values are P=.09695055264111185,Q=.06272866732853433; for the original protected floating checkpoint P=.09695054888878352,Q=.06272864076835438. P/Q are normalized squared-radius depths, not radius differences. Their numerical precision is not part of the exact census claim.

Compared with literal L18 (P=.10018756794854829,Q=.06712194454711812), both bars decrease without extra critical points. This does not dominate every historical candidate: F18 has P=.09747142366897970 and Q=.06236768950811229, so the new R7_D10 improves P but worsens Q against F18. No global-best or canonical promotion is made. The larger exact D15 body is retained separately rather than discarded because a simpler D10 body also works.

The complete exact auditor enumerates all triples to obtain every supporting plane, verifies every point is a true vertex with rank-three incident normals, verifies facet boundary cycles and Euler incidence, then computes exact oriented-tetrahedron volume and first moments. It tests stable feet against all supporting half-spaces, unstable vertices against every other vertex, and edge projections against the cone of the two adjacent normals. Closed-boundary equalities are recorded as weak incidences; both endpoints have none. It does not rely on the floating search or an Euler-count shortcut for the equilibrium classification.

## Reconstruction and proof commands
Extract the literal file sections as described in part1. Run:

```sh
python exact69.py protected1/simple_D10000000000.txt 10000000000 protected1/simple_exact_census.json
python exact69.py protected1/exact_D1e15.txt 1000000000000000 protected1/exact_census.json
```

Expected terminal line for EACH command:

```text
EXACT_AUDIT 75 204 131 408 [2, 2, 2] [0, 0, 0]
```

Both have stable facets cap18 and {14,16,24}, unstable vertices6,62, and saddle edges13–22 and6–63. These labels refer to the rows in this capsule only. Expected generated output identities:

protected1/simple_exact_census.json: 6468bytes, SHA-256 6faa634000564a56dff906b403e4d1f45fb4c01540f8e0ba378a2b9bbe797829

protected1/exact_census.json: 6619bytes, SHA-256 e2efba76b39a9fc6fc8b1085a5b2cb7c74d43301f49c799ea2eb17c4fcd71915

For R7_D10 the exact volume is309032051639300617184939/240000000000000000000000 and exact centroid is(-60423884133454651723814759027023/309032051639300617184939000000000, -41230169635082149488164128655694847/309032051639300617184939000000000000, -44410076844301799984913036896203/309032051639300617184939000000000).

## Recovery input manifest
exact69.py: 4803bytes, SHA-256 2831269dee71e61e2616eab92191e2ed4babf6760b46a5f702eebaa080394603

protected1/simple_D10000000000.txt: 2569bytes, SHA-256 db2317beb0153668da0f973365db8f95e2f804f1759384ad25c494b815f10c42

protected1/exact_D1e15.txt: 3694bytes, SHA-256 d596fc44636fde444bd4f805c7cb35dcddf22266056788949a4ee25ddeb3e73d

## File: exact69.py
```python
"""Exact complete-facet and equilibrium audit for rational 3D input.
Enumerates supporting planes from all triples; no numerical hull oracle is used.
Weak flags include boundary incidences (possibly repeated across strata).
This audit assumes all supplied points are distinct and all boundary edge
intersections contain exactly two supplied vertices; it checks these assumptions.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import gcd
from functools import reduce
import json,sys,time

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def scale(s,a):return tuple(s*x for x in a)
def add(a,b):return tuple(x+y for x,y in zip(a,b))

def audit(points,D):
    I=[tuple(map(int,p)) for p in points];N=len(I)
    assert D>0 and len(set(I))==N
    F={}
    for i,j,k in combinations(range(N),3):
        a=I[i];n=cross(sub(I[j],a),sub(I[k],a))
        if n==(0,0,0):continue
        h=dot(n,a);sgn=0;support=True
        for p in I:
            v=dot(n,p)-h
            if not v:continue
            s=1 if v>0 else -1
            if sgn and s!=sgn:support=False;break
            sgn=s
        if not support or sgn==0:continue
        if sgn>0:n=scale(-1,n);h=-h
        d=reduce(gcd,n+(h,));key=tuple(x//d for x in n+(h,))
        if key not in F:F[key]={v for v,p in enumerate(I) if dot(key[:3],p)==key[3]}
    faces=list(F.values());planes=list(F);nf=len(F);edges={}
    for f,g in combinations(range(nf),2):
        e=faces[f]&faces[g]
        assert len(e)<=2,'collinear edge points require preprocessing'
        if len(e)==2:edges[tuple(sorted(e))]=(f,g)
    used=set().union(*faces)
    assert used==set(range(N)), 'this recovery endpoint expects every input point to be extreme'
    for v in range(N):
        normals=[planes[f][:3] for f in range(nf) if v in faces[f]]
        assert any(dot(a,cross(b,c)) for a,b,c in combinations(normals,3))
    assert N-len(edges)+nf==2
    W=0;T=[0,0,0]
    for f,vs in enumerate(faces):
        adj={v:[] for v in vs}
        for (a,b),fg in edges.items():
            if f in fg:adj[a].append(b);adj[b].append(a)
        assert all(len(z)==2 for z in adj.values())
        first=min(vs);cycle=[first];prev=None;cur=first
        while True:
            nxt=next(v for v in sorted(adj[cur]) if v!=prev)
            if nxt==first:break
            assert nxt not in cycle
            cycle.append(nxt);prev,cur=cur,nxt
        assert set(cycle)==vs
        a,b,c=(I[v] for v in cycle[:3]);n=planes[f][:3]
        if dot(cross(sub(b,a),sub(c,a)),n)<0:cycle.reverse()
        a=I[cycle[0]]
        for j in range(1,len(cycle)-1):
            b=I[cycle[j]];c=I[cycle[j+1]]
            assert dot(cross(sub(b,a),sub(c,a)),n)>0
            w=dot(a,cross(b,c));W+=w
            for q in range(3):T[q]+=w*(a[q]+b[q]+c[q])
    assert W>0
    centroid=tuple(Q(t,4*W) for t in T)
    Z=[sub(p,centroid) for p in I]
    ns=[p[:3] for p in planes]
    hs=[Q(p[3])-dot(p[:3],centroid) for p in planes]
    assert all(h>0 for h in hs)
    S=[];U=[];H=[];weakS=[];weakU=[];weakH=[]
    for f,n in enumerate(ns):
        foot=scale(hs[f]/dot(n,n),n)
        sl=[hs[g]-dot(ns[g],foot) for g in range(nf) if g!=f]
        if min(sl)>0:S.append(sorted(faces[f]))
        elif min(sl)==0:weakS.append(sorted(faces[f]))
    for v,p in enumerate(Z):
        sl=[dot(p,sub(I[w],I[v])) for w in range(N) if w!=v]
        if max(sl)<0:U.append(v)
        elif max(sl)==0:weakU.append(v)
    for (a,b),(f,g) in edges.items():
        d=sub(I[b],I[a]);t=-dot(Z[a],d)/dot(d,d)
        if not 0<=t<=1:continue
        p=add(Z[a],scale(t,d));n,m=ns[f],ns[g]
        A=dot(n,n);B=dot(n,m);C=dot(m,m);det=A*C-B*B
        assert det>0
        al=(dot(n,p)*C-dot(m,p)*B)/det
        be=(dot(m,p)*A-dot(n,p)*B)/det
        assert p==add(scale(al,n),scale(be,m))
        if al>0 and be>0 and 0<t<1:H.append([a,b])
        elif al>=0 and be>=0:weakH.append([a,b])
    out={'D':D,'V':N,'E':len(edges),'F':nf,'C':2*len(edges),
         'own_strict':[len(S),len(U),len(H)],'weak':[len(weakS),len(weakU),len(weakH)],
         'S':S,'U':U,'H':H,'weak_S':weakS,'weak_U':weakU,'weak_H':weakH,
         'centroid':[str(c/D) for c in centroid], 'volume':str(Q(W,6*D**3)),
         'facets':[sorted(v) for v in faces]}
    assert len(S)+len(U)-len(H)==2 if not any(out['weak']) else True
    return out

if __name__=='__main__':
    fn=sys.argv[1];D=int(sys.argv[2]);out=sys.argv[3]
    points=[list(map(int,l.split())) for l in open(fn) if l.strip()]
    r=audit(points,D)
    text=json.dumps(r,sort_keys=True,indent=2)+'\n';open(out,'w').write(text)
    print('EXACT_AUDIT',r['V'],r['E'],r['F'],r['C'],r['own_strict'],r['weak'])
```

## File: protected1/simple_D10000000000.txt
```text
-11460387000 -3857916343 299523000
-11470512000 -2899224230 -2037734000
-11026063000 -2254861043 -3908769000
-10230644000 -1796831680 -5557628000
-9510445000 -6928532491 6510359000
-9400019000 -1541285244 -6734832000
-8468521000 -8207174333 8943705000
-8419307000 -1396211900 -7741744000
-7643561000 -1347148481 -8377603000
-6445073000 -1385339868 -9081264000
-6107888000 2653709000 -1537258000
-6252684000 2353981000 33982000
-5614553000 2389456000 850031000
-5230979000 -1516744630 -9567398000
-5131977000 2361292000 1409188000
-5288348000 3437582000 -1971679000
-4269447000 2172177000 2317685000
-4292456000 268128000 4263928000
-4140111000 1847464000 2775654000
-4137873000 1249068000 3402551000
-4150730000 4403557000 -2272310000
-3992109000 4169498000 -809449000
-3465436000 -1811109638 -10021830000
-3351040000 510316000 4171974000
-3404358000 4164688000 314875000
-3291158000 4693357000 -3160677000
-2728918000 -1961861509 -10143055000
-2598967000 625894000 4065303000
-2962803000 -348854000 4692291000
-2399766000 4849633000 -3649875000
-1989936000 -2141282092 -10195824000
-2243067000 4441045000 714278000
-1997500000 3857049000 1478358000
-1555779000 3662522000 1799252000
-1242032000 -2351402402 -10179466000
-1191451000 4682884000 -4358740000
-990653000 3660375000 1894721000
-502791000 -2588408240 -10091612000
-407355000 4553841000 -4419610000
-58227000 3893946000 1763960000
-30020000 771551000 3535302000
258459000 -2765491000 -9938221000
166131000 556402000 3547340000
755065000 722314000 3303509000
1009309000 -2931109000 -9714852000
886559000 1617542000 2968865000
1270620000 4202904000 1545354000
2443009000 4436944000 -3174557000
1746798000 -3086791000 -9420723000
3110309000 -1657691000 -8729344000
2459014000 -3227406000 -9059629000
3901251000 3995200000 -950557000
3139884000 -3354000000 -8633918000
2957473000 4713829000 1029882000
3242078000 -4404395736 -8142020000
3763178000 -3505110000 -8150261000
3693219000 4021824000 1262033000
4174250000 3468524000 1353393000
4344628000 -3635920000 -7612699000
4136479000 -5177667687 -6846189000
4462556000 3126907000 1308119000
4734972000 2773746000 1245220000
4880613000 -3749058000 -7023891000
4988477000 2413014000 1165451000
5253751000 -4751584000 -5529282000
5365776000 -828760000 -5894998000
5498948000 1697741000 833437000
5932577000 941705000 419481000
5841306000 -4230720000 -4538684000
6278016000 152540000 -80632000
6254986000 -3616235000 -3628646000
6508863000 -621657000 -633103000
6634282000 -1400183000 -1263239000
6520856000 -2917480000 -2763638000
6642749000 -2170404000 -1972574000
```

## File: protected1/exact_D1e15.txt
```text
-1146038684833000 -385791618979519 29952252455000
-1147051162179000 -289922444009247 -203773373785000
-1102606279526000 -225486122473081 -390876869183000
-1023064411475000 -179683149247229 -555762838219000
-951044452628000 -692853245340111 651035859303000
-940001906502000 -154128503437086 -673483246930000
-846852061396000 -820717457430622 894370533326000
-841930702978000 -139621189288962 -774174399758000
-764356103739000 -134714846751293 -837760300811000
-644507261100000 -138534013885586 -908126359646000
-610788842959000 265370853980000 -153725817190000
-625268400716000 235398075735000 3398152241000
-561455328814000 238945566948000 85003091845000
-523097867699000 -151674490836274 -956739753422000
-513197669220000 236129162147000 140918804491000
-528834793784000 343758216938000 -197167905197000
-426944651610000 217217733522000 231768490635000
-429245590740000 26812806632000 426392799299000
-414011095901000 184746354255000 277565416204000
-413787274360000 124906750671000 340255069378000
-415072991721000 440355675815000 -227230969199000
-399210853980000 416949814833000 -80944906350000
-346543591627000 -181110981417410 -1002182962494000
-335104043325000 51031595403000 417197417389000
-340435803269000 416468751246000 31487506472000
-329115812993000 469335745058000 -316067658481000
-272891838415000 -196186141019221 -1014305498611000
-259896706774000 62589367355000 406530278328000
-296280277909000 -34885437578000 469229107741000
-239976621964000 484963346249000 -364987465865000
-198993612452000 -214128223078173 -1019582357787000
-224306745204000 444104471909000 71427819343000
-199749993846000 385704941328000 147835794596000
-155577894699000 366252171558000 179925227383000
-124203194116000 -235140257110136 -1017946562568000
-119145057395000 468288393873000 -435874025779000
-99065308746000 366037491655000 189472125475000
-50279146020000 -258840827604522 -1009161160582000
-40735476691000 455384126226000 -441960992823000
-5822676529000 389394615373000 176396008580000
-3002044821000 77155125643000 353530181349000
25845853980000 -276549146020000 -993822126672000
16613113500000 55640160548000 354734011535000
75506470307000 72231434262000 330350919255000
100930853980000 -293110853980000 -971485228792000
88655853980000 161754180158000 296886488604000
127062045952000 420290414293000 154535351368000
244300853980000 443694446421000 -317455745664000
174679780151000 -308679146020000 -942072271440000
311030853980000 -165769146020000 -872934439595000
245901400451000 -322740603612000 -905962889474000
390125059179000 399519998206000 -95055698363000
313988359899000 -335400033303000 -863391784498000
295747312263000 471382858000000 102988187726000
324207795034000 -440439558757974 -814202032986000
376317806889000 -350511010475000 -815026105272000
369321873559000 402182358145000 126203347340000
417424972752000 346852365616000 135339254724000
434462833724000 -363592002630000 -761269858123000
413647916678000 -517766784685144 -684618872008000
446255593943000 312690694632000 130811898026000
473497201245000 277374579245000 124521991806000
488061300174000 -374905751594000 -702389055316000
498847685841000 241301359002000 116545059897000
525375053827000 -475158373354000 -552928229418000
536577597020000 -82876038893000 -589499796000000
549894817719000 169774063456000 83343720022000
593257672824000 94170531541000 41948132956000
584130646814000 -423071999852000 -453868435971000
627801569195000 15253950376000 -8063240287000
625498634154000 -361623538795000 -362864577771000
650886300029000 -62165671119000 -63310344925000
663428195892000 -140018254672000 -126323890677000
652085609237000 -291747951410000 -276363841659000
664274923762000 -217040401037000 -197257378128000
```
