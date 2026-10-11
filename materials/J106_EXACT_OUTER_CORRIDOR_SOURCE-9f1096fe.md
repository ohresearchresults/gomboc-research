# material-9f1096feb0d7

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Exact finite own-centroid obstruction for KF27D two-facet outer surgery.
Self-contained standard-library Python. No numerical predicates or optimizers.
Every convex B with K subset B subset L retains two strict U, for each of 43
explicit outer envelopes L. This is NOT exclusion of all physical deformations.
"""
import hashlib,itertools,json,sys
from fractions import Fraction as Q
from functools import cmp_to_key
from pathlib import Path
sys.set_int_max_str_digits(0)
RAW='''49 10000
-5079 13732 9267
-14396 11026 -3218
-12466 13017 -2373
-10223 14660 -1659
-12371 13207 485
-5511 15313 6055
-8438 14243 6102
-6944 14003 7847
-2416 17109 -242
-5135 16720 -706
-3100 13245 10467
-7743 15902 -1141
5950 3897 -9129
7859 14371 112
7631 1392 -8083
-7105 -20060 -8288
3029 16527 756
10270 12338 -490
5553 15635 147
13447 -12400 4798
10989 9339 -4734
8969 11100 5188
-1080 12497 11470
5972 13236 -6394
3314 -20677 -1248
2405 11856 11399
2827 16105 -3395
-1372 -21226 -4632
337 17042 309
6856 -18977 2259
8235 -11672 11211
-1912 9348 13526
3963 10154 12299
6264 11222 9621
-48 16910 -1981
9667 -16286 5360
13499 -8728 8488
-9829 14213 4254
-11155 13859 2378
-13471 12248 -1382
-15456 9243 -4601
-16262 7227 -5952
-16803 4959 -7230
-17054 2425 -8392
-16933 -367 -9448
-16470 -4196 -10134
-15277 -8346 -10358
-12715 -13423 -10051
2909 -2 -9206
'''
INPUT_SHA='52a71e8f9dbfe781d3a0aeafe053045e7cedb2fa588661f822d05990c5a86421'
assert hashlib.sha256(RAW.encode()).hexdigest()==INPUT_SHA
N=[tuple(map(int,r.split())) for r in RAW.splitlines()[1:]]
assert RAW.splitlines()[0]=='49 10000' and len(N)==49
D=10000

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(t,a):return tuple(t*x for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def serial(x):
    if isinstance(x,Q):return str(x)
    if isinstance(x,dict):return {str(k):serial(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [serial(v) for v in x]
    return x

def interval(x,digits=15):
    t=10**digits;lo=x.numerator*t//x.denominator
    assert Q(lo,t)<=x<Q(lo+1,t)
    return {'lower':lo,'upper':lo+1,'denominator':t,'strict':Q(lo,t)!=x}

def polygon_order(p,f,n):
    c=mul(Q(1,len(f)),tuple(sum(p[i][j] for i in f) for j in range(3)))
    k=next(j for j in range(3) if n[j]);a=(k+1)%3;b=(k+2)%3
    def h(i):
        x=p[i][a]-c[a];y=p[i][b]-c[b]
        return 0 if y>0 or (y==0 and x>=0) else 1
    def cmp(i,j):
        if h(i)!=h(j):return -1 if h(i)<h(j) else 1
        z=(p[i][a]-c[a])*(p[j][b]-c[b])-(p[i][b]-c[b])*(p[j][a]-c[a])
        assert z!=0 or i==j
        return -1 if z>0 else 1 if z<0 else 0
    f=sorted(f,key=cmp_to_key(cmp))
    if n[k]<0:f.reverse()
    s=f.index(min(f));return f[s:]+f[:s]

def geom(removed):
    rows=[i for i in range(len(N)) if i not in removed]
    vertices=set();bounded=[None]*6
    for i,j,k in itertools.combinations(rows,3):
        bc=cross(N[j],N[k]);ca=cross(N[k],N[i]);ab=cross(N[i],N[j]);det=dot(N[i],bc)
        if not det:continue
        # e_axis with either sign is a nonnegative combination of three normals.
        for axis in range(3):
            for sign in (-1,1):
                z=2*axis+(sign+1)//2
                if bounded[z] is None and all(v[axis]*sign*det>=0 for v in (bc,ca,ab)):
                    lam=[Q(v[axis]*sign,det) for v in (bc,ca,ab)]
                    assert all(t>=0 for t in lam)
                    assert tuple(sum(t*N[r][a] for t,r in zip(lam,(i,j,k))) for a in range(3))==tuple(sign if a==axis else 0 for a in range(3))
                    bounded[z]={'rows':[i,j,k],'lambda':lam}
        num=tuple(D*(bc[a]+ca[a]+ab[a]) for a in range(3))
        if det<0:det=-det;num=tuple(-x for x in num)
        if all(dot(N[r],num)<=D*det for r in rows):vertices.add(tuple(Q(x,det) for x in num))
    assert all(v is not None for v in bounded)
    p=sorted(vertices);assert len(p)>=4
    faces=[];labels=[];owners={};orient={}
    for r in rows:
        f=[i for i,v in enumerate(p) if dot(N[r],v)==D]
        if len(f)<3:continue
        f=polygon_order(p,f,N[r]);fi=len(faces)
        for a,b in zip(f,f[1:]+f[:1]):
            d=sub(p[b],p[a])
            assert all(dot(N[r],cross(d,sub(p[t],p[a])))>0 for t in f if t not in (a,b))
            e=tuple(sorted((a,b)));owners.setdefault(e,[]).append(fi);orient[e]=orient.get(e,0)+(1 if a<b else -1)
        faces.append(f);labels.append(r)
    es=sorted(owners)
    assert all(len(owners[e])==2 and orient[e]==0 for e in es)
    assert len(p)-len(es)+len(faces)==2
    nb=[set() for _ in p]
    for a,b in es:nb[a].add(b);nb[b].add(a)
    assert all(len(v)>=3 for v in nb)
    seen={0};todo=[0]
    for a in todo:
        for b in sorted(nb[a]):
            if b not in seen:seen.add(b);todo.append(b)
    assert len(seen)==len(p)
    W=Q(0);T=(Q(0),)*3
    for f in faces:
        for j in range(1,len(f)-1):
            a,b,c=(p[f[t]] for t in (0,j,j+1));w=dot(a,cross(b,c));assert w>0
            W+=w;T=add(T,mul(w,add(a,add(b,c))))
    vol=W/6;moment=mul(Q(1,24),T);g=mul(1/vol,moment)
    assert all(dot(N[r],g)<D for r in rows)
    return {'points':p,'faces':faces,'labels':labels,'edges':es,'neighbors':nb,'volume':vol,'moment':moment,'centroid':g,'bounded':bounded}

def find_carrier(K,rows):
    u=[p for p in K['points'] if all(dot(N[r],p)==D for r in rows)]
    assert len(u)==1;return u[0]

def main():
    K=geom(set());assert (len(K['points']),len(K['edges']),len(K['faces']))==(94,141,49)
    carriers=[(15,31,47),(12,46,47)];U=[find_carrier(K,r) for r in carriers]
    old_u=[]
    for u in U:
        i=K['points'].index(u);guards=[]
        for j in sorted(K['neighbors'][i]):
            d=sub(K['points'][j],u);v=dot(sub(u,K['centroid']),d)
            assert v<0;guards.append(v)
        old_u.append({'rows':carriers[len(old_u)],'point':u,'coordinate_lex_index':i,'guards':guards})
    assert len(set(U))==2
    # No root carrier is deleted in the certified union of envelopes.
    root_rows=set().union(*map(set,carriers))
    candidates=[None]+[j for j in range(49) if j not in root_rows|{32,36}]
    assert len(candidates)==43
    out=[];worst=None
    for extra in candidates:
        removed={32,36}|(set() if extra is None else {extra})
        L=geom(removed);DV=L['volume']-K['volume'];assert DV>0
        assert all(all(dot(N[r],p)<=D for r in L['labels']) for p in K['points'])
        checks=[]
        for u in U:
            i=L['points'].index(u)
            for j in sorted(L['neighbors'][i]):
                d=sub(L['points'][j],u)
                # For V_B*(u-g_B).d, any added measurable subset of L\K has
                # contribution at most DV*max(0,max_{x in L}(u-x).d).
                a=K['volume']*dot(sub(u,K['centroid']),d)
                z=max(Q(0),max(dot(sub(u,x),d) for x in L['points']))
                top=a+DV*z
                margin=top/(L['volume']*sum(abs(t) for t in d))
                # Since top<0 and V_B<=V_L, this also bounds the actual
                # (u-g_B).d/||d||_1 above, uniformly for all such B.
                assert margin<-Q(17,1000)
                if worst is None or margin>worst:worst=margin
                checks.append({'carrier':carriers[U.index(u)],'outer_edge_indices':[i,j],'direction':d,'base_moment_guard':a,'positive_shell_bound':DV*z,'upper_normalized_guard':margin,'upper_guard_interval':interval(margin)})
        assert len(checks)==6
        case={'removed':sorted(removed),'outer_counts':[len(L['points']),len(L['edges']),len(L['faces'])],'outer_volume':L['volume'],'outer_volume_interval':interval(L['volume']),'added_volume_bound':DV,'checks':checks,'boundedness_duals':L['bounded']}
        if extra is None:
            R=max(abs(x-g) for p in L['points'] for x,g in zip(p,K['centroid']))
            case['uniform_centroid_infinity_bound']=DV*R/K['volume']
            case['uniform_centroid_bound_interval']=interval(case['uniform_centroid_infinity_bound'])
            assert case['uniform_centroid_infinity_bound']<Q(14,1000)
        out.append(case)
        print('EXACT_OUTER_CORRIDOR_TWO_U',sorted(removed),max(float(v['upper_normalized_guard']) for v in checks),flush=True)
    report={'input_sha256':INPUT_SHA,'parent_volume':K['volume'],'parent_centroid':K['centroid'],'strict_old_U':old_u,'root_rows':sorted(root_rows),'case_count':len(out),'total_exact_edge_checks':sum(len(c['checks']) for c in out),'universal_guard':str(-Q(17,1000)),'worst_exact_upper_guard':worst,'worst_interval':interval(worst),'cases':out,'theorem':'Every homogeneous convex B with K subset B subset one of these L has at least these two strict U. No assumption on S, E or number of added vertices. Excludes neither inward retirement of K nor release of root-carrier rows nor two or more other released rows.'}
    dest=Path(__file__).resolve().parent
    (dest/'KF27D_QCANCEL_ROBUST_G4.txt').write_text(RAW)
    raw=(json.dumps(serial(report),indent=2)+'\n').encode();(dest/'J106_CORRIDOR_EXACT.json').write_bytes(raw)
    print('REPORT',len(raw),hashlib.sha256(raw).hexdigest())
    print('J106_43_FINITE_OUTER_CORRIDORS_TWO_STRICT_U_EXACT_PASS_NO_110')
if __name__=='__main__':main()
