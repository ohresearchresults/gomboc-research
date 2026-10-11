# material-4331e803cca0

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

"""DEPTH_INCIDENCE_AND_DEG6_CAP300_V1: complete deterministic exact recovery.
CPython 3.13.5; standard library; assertions enabled; no external input.
python -S depth_incidence_cap300.py build
python -S depth_incidence_cap300.py check
Not a whole E17 exclusion or an attaining class110 polyhedron.
The companion proof supplies the continuous geometric arguments.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb
from pathlib import Path
from collections import Counter
import hashlib
import json
import sys
assert __debug__
IDENTITY='DEPTH_INCIDENCE_AND_DEG6_CAP300_V1'
PARENTS=[
 ['minimum-0086','8123315ee22b6a0fc370e8f672f299bc19997f89ad023530404946c77f994f10'],
 ['minimum-0087','b77264d597b32a5f97ac011c57d4c95e7581fb2d81d202e2bc477b0e6fc867f5']]
MATERIAL_DEPENDENCIES=[
 ['[internal-source-reference]','af169f4ded154478fff382b79d1beaa91071ef51b625dec2db222b0e470c48ab'],
 ['[internal-source-reference]','0ef4abceed94299c2ffd0501d0b1c5c39607955f59bcfb6f9747caf66ab69572']]

def trim(a):
    a=list(map(Q,a))
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def add(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])

def mul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)

def scale(a,t):return trim([Q(t)*x for x in a])

def power(a,n):
    c=[Q(1)]
    for k in range(n):c=mul(c,a)
    return c

def value(p,x):
    ans=Q(0)
    for c in reversed(p):ans=ans*x+c
    return ans

def bernstein(p,l,r):
    n=len(p)-1
    aa=[(r-l)**k*sum((p[j]*comb(j,k)*l**(j-k) for j in range(k,n+1)),Q(0)) for k in range(n+1)]
    return [sum((aa[k]*Q(comb(i,k),comb(n,k)) for k in range(i+1)),Q(0)) for i in range(n+1)]

def cover_positive(p,l,r,depth=0):
    bb=bernstein(p,l,r)
    if min(bb)>0:return [{'left':l,'right':r,'bernstein':bb}]
    assert depth<20,'No positivity certificate at permitted depth'
    mid=(l+r)/2
    return cover_positive(p,l,mid,depth+1)+cover_positive(p,mid,r,depth+1)

def determinant(a):
    a=[list(map(Q,row)) for row in a];n=len(a);out=Q(1)
    for k in range(n):
        i=next((i for i in range(k,n) if a[i][k]),None)
        if i is None:return Q(0)
        if i!=k:a[i],a[k]=a[k],a[i];out=-out
        p=a[k][k];out*=p
        for j in range(k+1,n):
            f=a[j][k]/p
            for t in range(k+1,n):a[j][t]-=f*a[k][t]
    return out

def rank_cap_identity():
    k=[[8692,-9579,-2375,-575,1459],[-9579,11888,0,1066,-2404],[-2375,0,7220,-866,1459],[-575,1066,-866,200,-391],[1459,-2404,1459,-391,782]]
    mat=[[Q(0)]*5 for _ in range(5)]
    def term(i,j,c):
        if i==j:mat[i][j]+=c
        else:mat[i][j]+=c/2;mat[j][i]+=c/2
    def expr(terms,c):
        for i,j,f in terms:term(i,j,Q(f)*c)
    eq=[[(0,0,1)],[(0,3,1)],[(2,3,1)],[(1,4,1)]]
    ine=[[(0,4,1),(2,4,1)],[(4,4,1),(3,4,-1)],[(1,3,1)],[(1,1,1),(0,1,-1)],[(2,2,1),(0,2,-1)],[(2,2,1),(1,1,-1)]]
    yy=[Q(-2173,50),Q(23,4),Q(433,50),Q(601,25)]
    mm=[Q(1459,100),Q(391,100),Q(533,50),Q(9579,100),Q(95,4),Q(727,20)]
    term(3,3,Q(1));term(2,2,Q(-24))
    for e,y in zip(eq,yy):expr(e,-y)
    for e,m in zip(ine,mm):expr(e,m)
    assert mat==[[Q(v,200) for v in row] for row in k]
    minors=[determinant([row[:i] for row in k[:i]]) for i in range(1,6)]
    assert minors==[8692,11573255,16503151100,8831025280,5962527728]
    rhs=sum(yy)+2*mm[0]-mm[2]
    assert rhs==Q(1351,100)
    return {'order':['x','b','z','q0','B'],'K':k,'leading_minors':minors,'Y':yy,'mu':mm,'q0_minus_24z2_lower':rhs,'u_minus_24z2_lower':rhs-1}

def trig_and_depth():
    # Machin: tan(4 atan(1/5))=120/119; subtract atan(1/239).
    t=Q(1,5);t2=2*t/(1-t*t);t4=2*t2/(1-t2*t2)
    assert (t4-Q(1,239))/(1+t4/Q(239))==1
    pi_lower=16*sum((Q((-1)**j,(2*j+1)*5**(2*j+1)) for j in range(4)),Q(0))-Q(4,239)
    p=Q(333,106);assert pi_lower>p
    def f(n):
        assert n>=2
        t=p/(2*n);c=1-t*t/2+t**4/24
        assert 0<c<1
        return c**(2*n)
    kk=81*f(10)*f(9);assert kk<48
    sqrt8_hi=Q(99,35);assert sqrt8_hi**2>8
    def incidence(k):return (3*(k+1)+sqrt8_hi*(k-1))**2/(4*k)
    r=incidence(Q(48));assert r==Q(8000067,19600)<Q(40817,100)<409
    table=[]
    for hp in range(1,10):
        for hq in range(1,9):
            k=81*f(hp+1)*f(hq+1);assert k>1
            all_bound=9*k;contact_bound=incidence(k)
            ceil=lambda a:(a.numerator*1000000+a.denominator-1)//a.denominator
            table.append({'primal_height':hp,'dual_height':hq,'condition_upper_millionths':ceil(k),'all_pair_upper_millionths':ceil(all_bound),'incident_upper_millionths':ceil(contact_bound),'incident_less_than_301':contact_bound<301})
    assert all(row['incident_less_than_301'] for row in table if row['primal_height']<=3 or (row['primal_height']<=4 and row['dual_height']<=6))
    return {'pi_lower_from_machin':pi_lower,'chosen_pi_lower':p,'condition_E17_upper':kk,'all_pair_E17_upper':9*kk,'incident_E17_simplified_upper':r,'depth_table_rounding_scale':1000000,'depth_table':table}

def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def dot(a,b):return sum((x*y for x,y in zip(a,b)),Q(0))
def sub(a,b):return [x-y for x,y in zip(a,b)]

def angular_certificate():
    w=[0,1]
    d=[1,1,1,-9,31]
    c5=[5,-20,16]
    sinefactor=[1,-12,16]
    n=mul(power(w,5),power(sinefactor,2))
    rawden=add(add([1],power(w,5)),scale(mul(power(w,3),c5),-2))
    assert rawden==mul([1,-1],d)
    assert add([1],scale(mul(w,power(c5,2)),-1))==mul([1,-1],power(sinefactor,2))
    # P = 100*((12.51-300 w^5)*(D+300N)+24D).
    pp=add(mul(add([1251],scale(power(w,5),-30000)),add(d,scale(n,300))),scale(d,2400))
    end=Q(131,200)
    assert Q(56,25)**2>5 and (3+Q(56,25))/8==end
    pieces=cover_positive(pp,Q(0),end)
    assert pieces[0]['left']==0 and pieces[-1]['right']==end
    assert all(a['right']==b['left'] for a,b in zip(pieces,pieces[1:]))
    assert all(min(cell['bernstein'])>0 for cell in pieces)
    # Exact convex six-pole local cone: NOT a bounded own-COM body.
    tt=[[Q(1),Q(0)]]
    for i in range(5):
        a,b=tt[-1];tt.append([a-Q(4,3)*b,Q(4,3)*a+b])
    assert all(dot(tt[i],sub(tt[i+1],tt[i]))==0 for i in range(5))
    assert all(cross(tt[i],tt[(i+1)%6])>0 for i in range(6))
    for i in range(6):
        edge=sub(tt[(i+1)%6],tt[i])
        assert all(cross(edge,sub(tt[j],tt[i]))>0 for j in range(6) if j not in (i,(i+1)%6))
    uu=dot(tt[0],tt[0]);aa=dot(tt[-1],tt[-1]);hh=cross(tt[0],tt[-1])**2/dot(sub(tt[0],tt[-1]),sub(tt[0],tt[-1]))
    ww=Q(9,25);assert ww**5==uu/aa and hh/aa==value(n,ww)/value(d,ww)
    assert Q(1251,30000)>Q(1,32)
    return {'F5_numerator':n,'F5_denominator':d,'positive_polynomial_100scaled':pp,'certified_interval':[0,end],'positive_bernstein_cover':pieces,'local_cone_control':{'scope':'LOCAL_CONVEX_SIX_POLE_CONE_NOT_A_BOUNDED_BODY','tangents':tt,'u':uu,'a':aa,'h':hh,'w':ww}}

def rooted(n,ee,root):
    adj=[[] for i in range(n)]
    for a,b in ee:adj[a].append(b);adj[b].append(a)
    par=[None]*n;par[root]=root;dist=[0]*n;todo=[root]
    while todo:
        a=todo.pop()
        for b in adj[a]:
            if par[b] is None:par[b]=a;dist[b]=dist[a]+1;todo.append(b)
    return (par,max(dist)) if all(a is not None for a in par) else None

def native_census():
    facets=[(0,1,2,3,4,5,6,7),(0,1,8),(1,2,8),(3,4,9),(4,5,9),(5,6,9),(6,7,9),(2,3,9,8),(7,0,8,9)]
    ef={}
    for i,ff in enumerate(facets):
        for a,b in zip(ff,ff[1:]+ff[:1]):ef.setdefault(tuple(sorted((a,b))),[]).append(i)
    ee=sorted(ef);assert len(ee)==17 and all(len(a)==2 for a in ef.values())
    cycles=[(7,3,4,5,6,8),(8,6,5,4,3,7)]
    for cy in cycles:
        for a,b in zip(cy,cy[1:]+cy[:1]):
            common=set(facets[a])&set(facets[b]);assert len(common)==2 and 9 in common
    selected=[];trees=0
    for kk in combinations(range(17),9):
        ss=set(kk);pp=rooted(10,[ee[k] for k in kk],9)
        if pp is None:continue
        trees+=1
        for sr in range(9):
            dd=rooted(9,[tuple(ef[ee[k]]) for k in range(17) if k not in ss],sr);assert dd is not None
            pv,hp=pp;pq,hq=dd
            for cy in cycles:
                if pq[0]==cy[0] and all(pq[cy[k]]==cy[k+1] for k in range(5)):
                    assert pv[8]==9
                    selected.append({'mask':sum(1<<k for k in kk),'U':9,'S':sr,'primal_parent':pv,'dual_parent':pq,'primal_height':hp,'dual_height':hq,'incident_chain':cy})
    hist=Counter((r['primal_height'],r['dual_height']) for r in selected)
    assert trees==4053 and len(selected)==24
    assert sorted(hist.items())==[((7,7),6),((7,8),4),((8,6),2),((8,7),4),((8,8),2),((9,6),2),((9,7),2),((9,8),2)]
    selected_new=[r for r in selected if r['primal_height']<=3 or (r['primal_height']<=4 and r['dual_height']<=6)]
    assert selected_new==[]
    return {'scope':'LITERAL_ROOF8_3_5_COMPLEX_WITH_U9_DEGREE6_NOT_BALANCED_ROOF','facets':facets,'lex_edges':ee,'all_primal_trees':trees,'selected_xz_chains':selected,'depth_histogram':[[a,b,c] for (a,b),c in sorted(hist.items())],'new_exclusions_from_shallow_depth_corollary':0}

def encode(obj):
    if isinstance(obj,Q):return str(obj)
    if isinstance(obj,(tuple,list)):return [encode(x) for x in obj]
    if isinstance(obj,dict):return {k:encode(v) for k,v in obj.items()}
    return obj

def build():
    result={'identity':IDENTITY,'scope':'NEW_CONTINUOUS_BOUNDS_AND_EXACT_NEGATIVE_CENSUS_NOT_MINIMUM_PROOF','literal_parents':PARENTS,'mathematical_material_dependencies':MATERIAL_DEPENDENCIES,'rank_cap_identity':rank_cap_identity(),'metric_depth':trig_and_depth(),'degree6_cap300':angular_certificate(),'native_degree6_census':native_census()}
    return (json.dumps(encode(result),sort_keys=True,separators=(',',':'))+'\n').encode()

if __name__=='__main__':
    if sys.argv[1:] not in (['build'],['check']):raise SystemExit('Usage: python -S depth_incidence_cap300.py build|check')
    bb=build();path=Path('depth_incidence_cap300.json')
    if sys.argv[1]=='build':
        if path.exists():assert path.read_bytes()==bb,'Refuse to overwrite changed exact report'
        path.write_bytes(bb)
    else:assert path.read_bytes()==bb,'Exact report mismatch'
    print('CENTROID_TREE_DEPTH_CONDITION_48_AND_INCIDENT_PRODUCT_409_PASS')
    print('DEG6_XZ_FIVE_ARROW_CHORD_AND_CAP300_EXACT_PASS')
    print('ROOF8_DEG6_24_SELECTED_CHAINS_SHALLOW_DEPTH_COVERAGE_ZERO_PASS')
    print(path.name,len(bb),hashlib.sha256(bb).hexdigest())
    print('DEPTH_INCIDENCE_AND_DEG6_CAP300_RECOVERY_PASS')
