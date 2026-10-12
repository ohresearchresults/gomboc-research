# material-9353f233334e

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J142 complete exact recovery

Save all three FILE blocks below, including their final newlines, in one directory. Run `python -B -S exact142.py` with assertions enabled. Standard-library CPython3.13.5 was used; no numerical library or inherited mechanics engine is required. The exact input is the unchanged LOW62 raw body from fully read parent figure-0622. This capsule proves the scoped finite mass exclusions, not a new own110 body or a complete mechanics audit of every rounded envelope.

Input manifest:
QW49J_LOW62_G9_INPUT.json:2182B/SHA25690cc88f1a89396ed5cbe20e84cb4fc8265ae1b4170cc2d5bf245c024d4c4662e.
RECIPE142.json:506B/SHA2564522da08fce645bdf50dd63a44e2198a1d476aeb1e5c516fc1daa94a9d34e20c.
exact142.py:7386B/SHA2564db4b57869d417d2f8b9045e0fbb76c93e439bafbf746194c6201d3e17e06dd1.
Executed output EXACT142.json:196328B/SHA256178abeb7f0a404c1db0021fe7f1c4ec580b0eb9970a6279e890f7c7955b6fd6f.
Terminal markers: J142_HOMOTHETIC_SHELL_EXACT_RADIAL_BOX_EXCLUDED for9 and45, then J142_TWO_FINITE_MASS_GAPS_EXACT_PASS_NO_110.
The accompanying proof is [internal-source-reference]. The source is self-contained without that explanatory text.

## FILE QW49J_LOW62_G9_INPUT.json
```json
{"denominator":1000000000,"kind":"V","name":"QW49J_LOW62_G9","rounding":"rational ties-to-even","rows":[[-653160200,-396049270,-281044390],[-635901120,-348735520,-114703370],[-573485370,-312096030,59433110],[-403851850,-274801310,333222890],[-628942740,-465851940,-479051720],[-298369900,-270988410,445608910],[-294004040,145261700,-277025530],[-227641470,174563440,-397890660],[-205616870,175558830,52613520],[-166419230,-864228870,-1684987750],[-159639480,-279904570,546701640],[-127070280,274153810,-149434510],[-121431580,232514050,-433105560],[-64253580,188186610,-573157110],[-61840320,48778390,-768887040],[-41547760,287804810,5312940],[-29845790,163437240,-627608200],[99900,-45390120,-874628490],[5559340,-304900310,621173960],[8318690,-777643830,-875588880],[21079870,317858320,-407617870],[32249280,209952060,183953630],[35691350,401777180,-198295560],[143526670,299058790,155509180],[167157090,336773360,123310730],[189220990,-314610540,663403040],[214862400,-113330470,-923187470],[281708130,-144015970,-906872580],[292611180,361490930,-462968400],[298261210,78683760,-725758550],[316173700,495336860,-305926610],[330358080,-672965550,-524978670],[380482910,-290962420,671095610],[386072830,-647953450,-486309890],[419532220,375270360,-409491510],[884356620,279779640,-154148160],[453499290,-113904820,-752292560],[911839560,76557340,-160274860],[474798190,-564668400,-560385730],[957240240,-75942940,-56852760],[524292760,-463132620,-621603750],[568515370,-264590000,639235000],[663024440,-544756110,473622630],[670107650,446931130,-241056530],[691422270,462164000,-26560520],[742534800,-242797950,570713920],[742815290,197050420,387780860],[754773010,333161360,219979510],[773316910,405326120,-199527750],[838672450,-157875350,483863520],[874122860,-21297470,412343550],[878258330,193058660,-187178160],[886599130,-414301780,340615460],[963831750,31793390,253159880],[967688420,-9467480,-64248670],[973362910,208028950,-67041890],[990960090,-260302030,206973360],[1018719710,94253200,-4759060],[1042461050,-76072250,102176640],[100843014,-554476498,-80803471],[54576523,-557100114,-132222383],[147109506,-596760201,-171977242]],"source":"QW49J_LOW62_B20_AUDIT.json"}
```

## FILE RECIPE142.json
```json
{"roots":{"45":{"alpha":"631803/1000000","n":[-69210,724445,685850],"parent":[1,2,3,5,0,10,7,12,3,17,18,22,20,20,16,22,13,14,25,9,28,23,30,24,47,32,17,26,34,28,34,33,41,38,43,55,29,54,40,58,36,45,45,48,47,-1,50,46,35,45,49,55,45,50,39,57,49,53,53,18,59,59]},"9":{"alpha":"332119/500000","n":[-242532,101335,-964837],"parent":[4,0,1,2,19,3,7,12,11,-1,5,12,13,16,17,11,14,9,10,9,13,15,20,15,15,18,9,26,20,26,20,19,41,31,28,48,27,51,33,54,38,45,52,34,43,49,47,44,43,50,53,35,56,57,57,35,58,55,39,61,61,31]}}}
```

## FILE exact142.py
```python
"""Exact finite homogeneous-moment exclusions for two LOW62 radial envelopes.
Standard-library only. Coordinates are unchanged from the immutable source.
Recipes nominate equality paths and a separator, not an answer: every required
path inequality, hull facet, integration and final gap is checked exactly.
"""
from fractions import Fraction as Q
from itertools import combinations
from collections import Counter
from pathlib import Path
from math import gcd,lcm
import json,hashlib,sys
sys.set_int_max_str_digits(0)

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return [x-y for x,y in zip(a,b)]
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def det(a,b,c):return dot(a,cross(b,c))
def primitive(n,h):
    d=0
    for v in [*n,h]:d=gcd(d,abs(v))
    return tuple(v//d for v in [*n,h])

def hull(Y):
    """Exhaust all supporting triples; integer coordinates, no geometry oracle."""
    out={};N=len(Y)
    for i,j,k in combinations(range(N),3):
        n=cross(sub(Y[j],Y[i]),sub(Y[k],Y[i]))
        if n==[0,0,0]:continue
        h=dot(n,Y[i]);pos=neg=False;ids=[]
        for t,x in enumerate(Y):
            z=dot(n,x)-h
            if z>0:pos=True
            elif z<0:neg=True
            else:ids.append(t)
            if pos and neg:break
        if pos and neg:continue
        assert pos or neg,'not full dimensional'
        if pos:n=[-v for v in n];h=-h
        key=primitive(n,h)
        if key not in out:out[key]=ids
    assert len(out)>=4
    faces=[]
    for key,ids in sorted(out.items()):
        n=key[:3];axis=max(range(3),key=lambda a:abs(n[a]));axes=[a for a in range(3)if a!=axis]
        pts=sorted((Y[i][axes[0]],Y[i][axes[1]],i)for i in ids)
        def turn(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
        lo=[];hi=[]
        for p in pts:
            while len(lo)>1 and turn(lo[-2],lo[-1],p)<=0:lo.pop()
            lo.append(p)
        for p in reversed(pts):
            while len(hi)>1 and turn(hi[-2],hi[-1],p)<=0:hi.pop()
            hi.append(p)
        cyc=[p[2]for p in lo[:-1]+hi[:-1]]
        assert len(cyc)>=3
        if dot(cross(sub(Y[cyc[1]],Y[cyc[0]]),sub(Y[cyc[2]],Y[cyc[0]])),n)<0:cyc.reverse()
        faces.append(cyc)
    edges=Counter();oriented=Counter();vertices=set();area=[0,0,0]
    for f in faces:
        vertices.update(f)
        for i,j in zip(f,f[1:]+f[:1]):edges[tuple(sorted((i,j)))]+=1;oriented[i,j]+=1
        for j in range(1,len(f)-1):
            n=cross(sub(Y[f[j]],Y[f[0]]),sub(Y[f[j+1]],Y[f[0]]))
            area=[a+b for a,b in zip(area,n)]
    assert all(v==2 for v in edges.values())
    assert all(oriented[j,i]==v==1 for (i,j),v in oriented.items())
    assert len(vertices)-len(edges)+len(faces)==2
    assert area==[0,0,0]
    return faces,dict(V=len(vertices),E=len(edges),F=len(faces))

def tetrahedra(F):
    return [(f[0],f[j],f[j+1])for f in F for j in range(1,len(f)-1)]

def mass(Y,D,F):
    sixV=0;twentyfourM=[0,0,0]
    for i,j,k in tetrahedra(F):
        v=det(Y[i],Y[j],Y[k]);sixV+=v
        for a in range(3):twentyfourM[a]+=v*(Y[i][a]+Y[j][a]+Y[k][a])
    V=Q(sixV,6*D**3);M=[Q(v,24*D**4)for v in twentyfourM]
    assert V>0
    return V,M

def positive_moment(Y,D,F,n,ND=10**6):
    """Integrate max(n.x/ND,0) via exact positive origin tetrahedra.
    In each tetrahedron the heights are 0,a,b,c. Equal-height cases are
    handled algebraically, with denominators only across opposite signs.
    """
    ans=Q(0)
    for i,j,k in tetrahedra(F):
        v=det(Y[i],Y[j],Y[k]);assert v>0
        h=sorted([dot(n,Y[t])for t in (i,j,k)])
        a,b,c=h
        if c<=0:q=Q(0)
        elif a>=0:q=Q(a+b+c)
        elif b<=0:q=Q(c**3,(c-a)*(c-b))
        else:q=Q(b*c*(b+c)-a*(b*b+b*c+c*c),(b-a)*(c-a))
        assert q>=0
        ans+=v*q
    return ans/(24*D**4*ND)

def interval(x,D=10**12):
    b=x.numerator*D//x.denominator
    return [b,b+1,D]

def exactpaths(R,parent,root):
    N=len(R);p=[None]*N;p[root]=Q(1);active=set()
    def build(i):
        if p[i] is not None:return p[i]
        assert i not in active
        active.add(i);j=parent[i];assert 0<=j<N and j!=i
        c=Q(dot(R[i],R[j]),dot(R[i],R[i]));assert c>0
        p[i]=c*build(j);active.remove(i);return p[i]
    for i in range(N):build(i)
    for i in range(N):
        for j in range(N):assert p[i]*dot(R[i],R[i])>=p[j]*dot(R[i],R[j]),('Bellman',root,i,j)
    return p

def main():
    raw=Path('QW49J_LOW62_G9_INPUT.json').read_bytes()
    assert len(raw)==2182 and hashlib.sha256(raw).hexdigest()=='90cc88f1a89396ed5cbe20e84cb4fc8265ae1b4170cc2d5bf245c024d4c4662e'
    o=json.loads(raw);Y=o['rows'];D=o['denominator'];F,vef=hull(Y)
    assert vef==dict(V=62,E=180,F=120) and all(len(f)==3 for f in F)
    V,M=mass(Y,D,F);g=[v/V for v in M]
    assert V==Q(1602464968338538832616823393,1200000000000000000000000000)
    assert g==[Q(1351925154762799228156273608880460239,6409859873354155330467293572000000000),Q(-1244558017473100755622810530258629593,6409859873354155330467293572000000000),Q(-790091171830583829920224489049169863,3204929936677077665233646786000000000)]
    RD=lcm(D,*[v.denominator for v in g]);R=[[v*(RD//D)-int(g[a]*RD)for a,v in enumerate(x)]for x in Y]
    rF,rvef=hull(R);v0,m0=mass(R,RD,rF);assert v0==V and m0==[0,0,0]
    recipe=json.loads(Path('RECIPE142.json').read_text());PD=10**12
    result=dict(parent_volume=str(V),parent_centroid=list(map(str,g)),parent_counts=vef,roots={})
    for root in [9,45]:
        r=recipe['roots'][str(root)];p=exactpaths(R,r['parent'],root)
        low=[(v.numerator*PD)//v.denominator for v in p]
        high=[-((-v.numerator*PD)//v.denominator)for v in p]
        assert all(Q(a,PD)<=v<=Q(b,PD)for a,v,b in zip(low,p,high))
        n=r['n'];records=[]
        for label,pnum in [('inner',low),('outer',high)]:
            Z=[[s*x for x in point]for s,point in zip(pnum,R)];ZD=RD*PD
            faces,counts=hull(Z)
            for f in faces:
                nn=cross(sub(Z[f[1]],Z[f[0]]),sub(Z[f[2]],Z[f[0]]))
                assert dot(nn,Z[f[0]])>0
            vv,mm=mass(Z,ZD,faces);jp=positive_moment(Z,ZD,faces,n);jt=dot(n,mm)/10**6;jm=jp-jt
            assert jp>0 and jm>0
            records.append(dict(name=label,counts=counts,volume=vv,moment=mm,Jplus=jp,Jminus=jm,faces=faces,p_grid=pnum))
        jp=records[0]['Jplus'];jm=records[1]['Jminus'];alpha=Q(r['alpha'])
        gap=alpha**4*jp-jm;assert gap>0
        scale=10**12;lo=0;hi=scale
        while hi-lo>1:
            mid=(lo+hi)//2
            if Q(mid,scale)**4*jp>jm:hi=mid
            else:lo=mid
        q=dict(root=root,separator=n,separator_denominator=10**6,alpha=str(alpha),epsilon=str(1-alpha),
            gap=str(gap),gap_interval=interval(gap),critical_alpha_interval=[lo,hi,scale],
            p=list(map(str,p)),bodies=records)
        result['roots'][str(root)]=q
        print('J142_HOMOTHETIC_SHELL_EXACT_RADIAL_BOX_EXCLUDED',root,'epsilon',str(1-alpha),'gap',float(gap),'critical',lo/scale,hi/scale,flush=True)
    def encode(v):
        if isinstance(v,Q):return str(v)
        raise TypeError(type(v).__name__)
    b=(json.dumps(result,default=encode,sort_keys=True,separators=(',',':'))+'\n').encode()
    Path('EXACT142.json').write_bytes(b)
    print('J142_TWO_FINITE_MASS_GAPS_EXACT_PASS_NO_110',len(b),hashlib.sha256(b).hexdigest(),flush=True)
if __name__=='__main__':main()
```
