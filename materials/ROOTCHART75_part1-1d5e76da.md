# material-1d5e76da9cd3

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# ROOTCHART75 recovery part 1

## Scientific identity
This is the newly computed combined physical root-chart transfer from literal JOINT75 primary75. It is not FULL76 and not target110. Exact input: swap_P58_Q64_G12, rational denominator10^12, V75/E219/F146,C438. At its actual uniform-volume centroid: strict S2/U2/H2; additional weak0/0/0; primitive zero0/0/0. The unstable junior moves from old input62 to58; the stable junior moves from the old triangle(14,16,24) to(16,31,24). Old dominant U6 and stable triangle(0,59,4) remain; H edges(6,63),(13,22). There is one positive primal and one positive polar bar. Exact rational values are generated below; numerical depths .09617230078016685 and .06405962701817887. The original JOINT75 depths were .10155678447201545 and .06771400169970322. This is finite simultaneous improvement and release of both old root carriers, not simultaneous cancellation.

## Evidence and ancestry
The coordinator executed the command below under CPython3.13.5. The auditor enumerates all supporting triples, rejects nonsimplicial maximal facets, constructs all true edges, computes actual volume and centroid and confirms them from a second interior origin, evaluates all strict and closed-weak vertex/facet/edge predicates, and computes every positive exact primal/polar bar without a cutoff. This is one exact hull/equilibrium implementation with a second-origin mass check, not two independent hull verifiers.
The complete literal parent figure-0552 was read through EOF at SHA ad8dc7c434c78f9d6a7bbd334969fdbfdab83f3a56202484b2698ad9bf1c95d4. Its full75 rows and the exact audit method also appear in the fully read [internal-source-reference]. This new body uses those75 input vertices and no bridge points. The producing SLSQP experiment used physical coordinates, actual own mass, root exchanges P58/Q64, trust .06, maxiter240. It hit its iteration limit; numerical success=false and scaled residual approximately -1.74e-9. Its exact rational endpoint independently passes the checks recorded here; optimizer termination is not the certificate. The complete producing units are separate ROOTCHART75 method recovery material; this part alone exactly reconstructs and audits this endpoint. Coordinates were rounded from saved decimal float output using Decimal nearest ties-even at D10^12; the integers below, not an unpreserved float checkpoint, are authoritative.

## Reconstruct and verify
Save both complete blocks with their displayed filenames and terminal LF.
```
python -B -S exact_endpoint.py swap_P58_Q64_G12.json
```
Expected terminal markers: EXACT_ENDPOINT_PASS and NO_OWN110_CLAIM. Expected census: S face IDs[3,64], cycles[(0,59,4),(16,31,24)], U input IDs[6,58], H[(6,63),(13,22)], weak_counts[0,0,0]. Primitive sign counts: S[156,0,282],U[5390,0,160],H[242,0,634]. Output includes the full input, all maximal faces and true edges, exact volume and centroid, every equilibrium carrier and all exact rational bar values.
Manifest (UTF-8 bytes, terminal LF):
- exact_endpoint.py:6424 bytes,SHA25617c834f792de79598126a77c1596e212821171e397ad3bde2c94179b5e91e0e1.
- swap_P58_Q64_G12.json:3195 bytes,SHA256e38a17555aa0a8d8a86d79278b3a053d097747f8e789835169f12486a5adb870.
- reproduced swap_P58_Q64_G12_audit.json:9192 bytes,SHA256521b5e1c891d97e27441b18264dd523c836220b883201e42daca5c3ac8f151bc.

## File exact_endpoint.py
```python
"""Exact simplicial endpoint audit, adapted from immutable exact_bridge.py.
Primary method source: [internal-source-reference], fully read; all-triple
support enumeration, homogeneous-integer signs, actual uniform volume mass,
all strict/closed-weak equilibria, and all positive primal/polar bars.
Run: python -B -S exact_endpoint.py <integer-input.json>
Input has D positive integer and I complete integer triples. No third-party
libraries. A nontriangular maximal facet is rejected explicitly.
"""
from fractions import Fraction as F
from itertools import combinations
from functools import reduce
from math import gcd,lcm
from pathlib import Path
import json,sys,hashlib
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(t,a):return tuple(t*x for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def primitive(a):
    g=reduce(gcd,a);return tuple(x//g for x in a) if g else tuple(a)
def hull(I,D):
    assert D>0 and len(set(I))==len(I)
    faces={};done=set()
    for i,j,k in combinations(range(len(I)),3):
        if (i,j,k) in done:continue
        n=cross(sub(I[j],I[i]),sub(I[k],I[i]))
        if not any(n):continue
        h=dot(n,I[i]);sg=0;zero=[];good=True
        for l,p in enumerate(I):
            v=dot(n,p)-h
            if v:
                s=1 if v>0 else -1
                if sg and sg!=s:good=False;break
                sg=s
            else:zero.append(l)
        if not good or not sg:continue
        if sg>0:n=mul(-1,n);h=-h
        key=tuple(zero);faces[key]=primitive(tuple(n)+(-h,));done.update(combinations(key,3))
    if not faces:raise ValueError('not full dimensional')
    X=[tuple(F(v,D) for v in p) for p in I];tri=[];planes=[]
    for ids,pl in sorted(faces.items()):
        if len(ids)!=3:raise ValueError('nontriangular maximal facet '+repr(ids))
        a,b,c=ids
        if dot(cross(sub(I[b],I[a]),sub(I[c],I[a])),pl[:3])<0:b,c=c,b
        tri.append((a,b,c));planes.append(pl[:3])
    edges={}
    for f,t in enumerate(tri):
        for j in range(3):edges.setdefault(tuple(sorted((t[j],t[(j+1)%3]))),[]).append(f)
    assert all(len(v)==2 for v in edges.values())
    active=sorted(set(sum((list(t) for t in tri),[])))
    assert len(active)-len(edges)+len(tri)==2
    return X,tri,planes,edges,active

def mass(X,tri):
    W=F(0);M=[F(0)]*3
    for i,j,k in tri:
        a,b,c=X[i],X[j],X[k];d=det(a,b,c);W+=d
        for t in range(3):M[t]+=d*(a[t]+b[t]+c[t])
    V=W/6;g=tuple(t/(4*W) for t in M);assert V>0
    o=mul(F(1,len(X)),tuple(sum(p[t] for p in X) for t in range(3)));w=F(0);m=[F(0)]*3
    for i,j,k in tri:
        a,b,c=(sub(X[t],o) for t in (i,j,k));d=det(a,b,c);assert d>0;w+=d
        for t in range(3):m[t]+=d*(a[t]+b[t]+c[t])
    assert w==W and add(o,tuple(t/(4*w) for t in m))==g
    return V,g

def sgns(a):return [sum(v<0 for v in a),sum(v==0 for v in a),sum(v>0 for v in a)]
def census(I,D,tri,planes,edges,active,c):
    cd=lcm(*(v.denominator for v in c));cn=tuple(int(v*cd) for v in c)
    R=[tuple(p[k]*cd-cn[k]*D for k in range(3)) for p in I]
    S=[];U=[];H=[];weak=[[],[],[]];alls=[];allu=[];allh=[]
    for f,(ids,n) in enumerate(zip(tri,planes)):
        assert dot(n,R[ids[0]])>0
        vals=[dot(n,cross(R[ids[i]],R[ids[(i+1)%3]])) for i in range(3)];alls.extend(vals)
        if min(vals)>0:S.append(f)
        elif min(vals)==0:weak[0].append(f)
    for i in active:
        vals=[dot(R[i],sub(R[j],R[i])) for j in active if j!=i];allu.extend(vals)
        if max(vals)<0:U.append(i)
        elif max(vals)==0:weak[1].append(i)
    for (i,j),own in sorted(edges.items()):
        a=R[i];d=sub(R[j],a);dd=dot(d,d);ad=dot(a,d);p=sub(mul(dd,a),mul(ad,d))
        n1=planes[own[0]];n2=planes[own[1]];aa=dot(n1,n1);bb=dot(n1,n2);ee=dot(n2,n2);assert aa*ee-bb*bb>0
        vals=[-ad,dd+ad,ee*dot(p,n1)-bb*dot(p,n2),aa*dot(p,n2)-bb*dot(p,n1)];allh.extend(vals)
        if min(vals)>0:H.append([i,j])
        elif min(vals)==0:weak[2].append([i,j])
    counts=[len(S),len(U),len(H)];assert counts[0]+counts[1]-counts[2]==2 or any(weak)
    return dict(SUH=counts,weak_counts=list(map(len,weak)),S_face_ids=S,S_cycles=[tri[i] for i in S],U_input_ids=U,H_edges=H,weak_carriers=weak,primitive_sign_counts=[sgns(alls),sgns(allu),sgns(allh)])

def bars(P,edges):
    r=[dot(p,p) for p in P];gates=[]
    for i,j in edges:
        a=P[i];d=sub(P[j],a);dd=dot(d,d);ad=dot(a,d);t=max(F(0),min(F(1),-ad/dd));p=add(a,mul(t,d));gates.append(dot(p,p))
    par=list(range(len(P)));root=list(range(len(P)));out=[]
    def find(i):
        while par[i]!=i:par[i]=par[par[i]];i=par[i]
        return i
    for e in sorted(range(len(edges)),key=lambda k:(-gates[k],k)):
        i,j=map(find,edges[e])
        if i==j:continue
        if (r[root[i]],root[i])<(r[root[j]],root[j]):i,j=j,i
        birth=r[root[j]];death=gates[e];assert death<=birth
        if death<birth:out.append(dict(root=root[j],elder=root[i],edge=edges[e],birth=birth,death=death,depth=1-death/birth))
        par[j]=i
    return sorted(out,key=lambda z:(-z['depth'],z['root']))
def encode(v):
    if isinstance(v,F):return str(v)
    raise TypeError(type(v))
def run(path):
    raw=path.read_bytes();a=json.loads(raw);D=a['D'];I=list(map(tuple,a['I']));X,tri,n,ed,ids=hull(I,D);V,g=mass(X,tri)
    P=[sub(x,g) for x in X];Q=[mul(1/dot(nn,P[t[0]]),nn) for t,nn in zip(tri,n)]
    bp=bars(P,list(ed));bq=bars(Q,[tuple(o) for o in ed.values()]);own=census(I,D,tri,n,ed,ids,g)
    out=dict(input_sha256=hashlib.sha256(raw).hexdigest(),D=D,I=I,VEF=[len(ids),len(ed),len(tri)],faces=tri,edges=list(ed),active_input_ids=ids,volume=V,centroid=g,own=own,Pbars=bp,Qbars=bq,bar_summary=dict(counts=[len(bp),len(bq)],largest_depths=[float(z[0]['depth']) if z else 0 for z in (bp,bq)]))
    text=json.dumps(out,default=encode,sort_keys=True,separators=(',',':'))+'\n';dst=path.with_name(path.stem+'_audit.json');dst.write_text(text)
    print('EXACT_ENDPOINT_PASS',path.name,out['VEF'],own,out['bar_summary'],len(text.encode()),hashlib.sha256(text.encode()).hexdigest(),flush=True)
    print('OWN110' if own['SUH']==[1,1,0] and own['weak_counts']==[0,0,0] else 'NO_OWN110_CLAIM',flush=True)
if __name__=='__main__':run(Path(sys.argv[1]))
```

## File swap_P58_Q64_G12.json
```json
{"D":1000000000000,"I":[[-1144023837938,-387612893781,83266099999],[-1152222641705,-288351460881,-172496868721],[-1111567471271,-226963007845,-364950401926],[-1033964089827,-184500585864,-535162890972],[-957904546177,-630890166773,585655500002],[-950941215435,-161775522240,-657359347027],[-836753158533,-783328661098,897060241862],[-886423766001,-144541963255,-732582750295],[-794800584422,-138630560816,-813668176798],[-684450910895,-144556927612,-885372204136],[-657504598235,224042280548,-125170324201],[-626801992310,239400551703,-1425325951],[-597478226819,226320112919,73596130077],[-565552152400,-164523301725,-939000015167],[-553232675548,222332943725,134452823522],[-537036519548,338463926423,-201943319117],[-474607992502,191043792745,243356130293],[-443343986727,-7568481755,464886599998],[-458359397913,158723417392,293144491078],[-440188733219,92501184555,371243912884],[-419537409537,437119868324,-239327143754],[-426103800000,398159946565,-83136180383],[-387806462858,-185898686246,-993228222561],[-291811286196,80651635790,399970910874],[-375560900000,397985734939,16785768490],[-342007140043,455806971174,-320565973123],[-312390427610,-208896042962,-1008368051351],[-255848457252,57357953573,411512939078],[-312251533397,-47780100000,483315218388],[-262223537628,463565132887,-376466687829],[-234427868054,-229184750508,-1016599354750],[-159771334498,461391781043,58384078803],[-221931782420,345739834813,169348699999],[-142209012029,367819074082,167120586760],[-154233875317,-246594564110,-1017700959746],[-163683362983,464549128515,-421873787082],[-69318275489,382075929665,162843147236],[-76410058672,-276719929740,-1009625584906],[-75581010756,465193316119,-426946100000],[41211871315,393681099913,152580558636],[15692266206,65450287592,345674361169],[4863440153,-294345068309,-994946131477],[36411291185,42557185712,345721563602],[91002886606,50241435554,323021566433],[85047687459,-310541499015,-972414309815],[142701188560,156836947654,273436057450],[185754100000,395094786829,142263249073],[200072000000,466268767567,-301039886924],[163373020459,-325122507643,-942174049829],[284886928381,-171724300000,-882042900001],[239064999648,-337978845599,-904447738604],[317573854288,465425443483,-51042506492],[301020431734,-360713101539,-862459604689],[352748228759,411548760736,101031550578],[340446773380,-483269300742,-777108468416],[363162674556,-372759956939,-815153450527],[400823638354,355566459148,117395968157],[439952971570,306198785102,120096338358],[421225864428,-383465656536,-762450413366],[394832554323,-545363779842,-654035468535],[466589390698,270953689866,114441475023],[491352433287,234942756678,107169772942],[491713018883,-399832758674,-659075659188],[514159113087,198351936039,98346126611],[522319564674,-491546144159,-509206375430],[544135788371,-123963912333,-555214376213],[562175994973,122284374311,61611415057],[592721643622,58405991825,28560470895],[578900483478,-431966121707,-408482894066],[618814413479,-11229235993,-12834674190],[618905430622,-357938476136,-307578781273],[637148008040,-81827895915,-59944765090],[647102867045,-152705080196,-112873518898],[638876979917,-291880862521,-236622288320],[647958043406,-223053615355,-171734317394]]}
```
