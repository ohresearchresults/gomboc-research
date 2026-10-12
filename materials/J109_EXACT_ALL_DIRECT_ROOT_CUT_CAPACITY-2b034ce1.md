# material-2b034ce1e956

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J109 — exact uniform-mass obstruction for every direct new root and any number of one-step polar cut controls

This is a complete standalone recovery unit and an EXECUTED scoped negative result, not an own110 construction and not a global impossibility claim. Literal K is KH93_C434_R82_G6, copied unchanged from completely read native material [internal-source-reference] (J98_EXACT_GEOMETRY_CORE.md, SHA ebbf64fe9441d3a320e8f673941436f186af46f8f5b25464c1ebc78a9c5e42fa). That material identifies author result figure-0581, SHA f4d4df1390c5e9bd18047aad823f3cd12e8c85751a66dbfc62ae50f67c779461. The author's own211/weak000 census is a working premise; the NEW obstruction below was derived and executed by the coordinator. No originating sandbox, encoded parent workspace, or C622 package is needed for this computation.

## Exact statement
Write O=(0.02496294,0.00321635,-0.00678274) rationally and delta=1/2048. For EVERY proposed centre c with ||c-O||_infinity<=delta, put q_i=N_i/(1000000-N_i.c). Let r=n/h, |n|=1,h>0, receive nonnegative radial arrows from BOTH old polar points 7 and18: q_i.(r-q_i)>=0. Intersect K with r.(x-c)<=1 and ANY family of additional cuts w.(x-c)<=1 satisfying w.(r-w)>=0. No such full-dimensional homogeneous intersection has centroid c. Its axial first moment satisfies the uniform strict bound

integral_L n.(x-c) dx < -h/25 < 0.

The number of controls is unrestricted, all directions and depths are covered, and arbitrary old-facet retirement is allowed. The use of nonnegative arrows includes strict arrows. This is NOT an exclusion of multi-step witnesses, controls outside the closed diameter ball of r, changed old K, outer additions, or centres outside this specified cube. No requirement about retention of the old U was used.

## Proof
1. The allowed cutting vectors form the closed diameter ball D(r)={w:w.(r-w)>=0}. For z=x-c, its support is (r.z+|r||z|)/2. Consequently every allowed intersection must retain K intersect {|z|+n.z<=2h}, and the new root bounds it above by K intersect {n.z<=h}.
2. Exact old halfspaces prove B(c,R) subset K throughout the centre cube, with R=441/1000. The two old feet a_i(c)=q_i/|q_i|^2 satisfy h<=min(n.a_7(c),n.a_18(c)). At O an exact convex mixture m of those feet has |m|<3/20. Each foot changes by an orthogonal projection of -(c-O), so its Euclidean error is <2delta. Therefore h<3/20+2delta<151/1000=HMAX<R/2.
3. The positive first moment in the slab 0<n.z<=h is at most A_projection(n)h^2/2. The compulsory negative ball-paraboloid core has axial first-moment magnitude pi I(R,h), where I=2h(2R^3-3R^2h+2h^3)/3. To derive it, write t=n.z<0: the cross-sectional disk area divided by pi is min(R^2-t^2,4h(h-t)), switching at t=2h-R. Integrate (-t) times this expression from -R to0.
4. Using pi>3 yields J/h < A_projection(n)h/2-4R^3+6R^2h-4h^3. This expression increases with h<=HMAX. Cauchy's projection formula is A_projection(n)=one-half the sum of absolute dot products with all exact outward facet area vectors. The verifier rounds those vectors and the two feet outward with retained rational errors, and covers the entire unit sphere by exact dyadic boxes. Every feasible box gives an upper coefficient strictly below -1/25.
5. Thus even any measurable set sandwiched between the compulsory negative core and the old-root-cut upper body has negative first moment. In particular a homogeneous allowed intersection cannot have centre c.

The exact geometry routine enumerates ALL 88560 H triples using integer signs, verifies every resulting facet and all supporting corners, closed opposite edge orientations, Euler and connectivity. Positive facet-area multiples of all normals sum to zero, and the normals span R^3, proving boundedness. atan2 only nominates facet cyclic order; the order is checked by exact all-corner inequalities. There are no floating acceptance predicates or optimizer calls.

## Executed certificate and recovery
Extract the two FILE blocks verbatim, including their final LF, to one directory. A generic extractor is:
```python
from pathlib import Path
import re,sys
out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True)
for name,data in re.findall(r'(?ms)^### FILE ([^\n]+)\n```[^\n]*\n(.*?)^```\n',Path(sys.argv[2]).read_text()):
    assert not Path(name).is_absolute() and '..' not in Path(name).parts
    (out/name).write_bytes(data.encode())
```
Run `python -B -S exact109.py`. Environment executed: CPython3.13.5, standard library only. Expected terminal marker:
`J109_ALL_DIRECT_ROOTS_ALL_ONE_STEP_CUT_CONTROLS_CENTRE_CUBE_MASS_EXCLUDED_EXACT_PASS_NO_110`.

Observed exact cover: visited609, subdivided76, certified235, off_sphere268, no_positive_root_height30, maximum_depth6. Largest certified upper coefficient lies between -40179366687/10^12 and -40179366686/10^12, both below -1/25. Old volume lies between 1712677687303/10^12 and 1712677687304/10^12. The actual old centroid differs from O by less than10^-8 in every coordinate.

Input/source/output manifest:
- R82.txt:1888 bytes, SHA9765712b5ffaa464ed4d677974256294c6d867b77fe77b930d166853f66a92a7.
- exact109.py:9721 bytes, SHAfbf651989a366a4243d4132bc4d5a9a75283c28b6c496a6f0c5ce43f1aba0c26.
- Generated J109_EXACT_CAPACITY.json:12224 bytes, SHA5a1d2f4f17234b1a2a62f4e4de6427fbc1937057bff447c1e8f96738f084ba70.
The JSON is regenerated deterministically, including its exact old volume, centroid intervals, mixture, all rounded area vectors/feet, and proof statistics. Timing in stdout is deliberately not a hashed output.

### FILE exact109.py
```python
"""Exact finite mass-capacity exclusion for one-step polar cut repair.
Pure Python 3 standard library. No floating predicates or optimizer in proof.
The H input is the literal R82 integer body (hash checked).
This is a SCOPED exclusion, not a solution or global impossibility of own110.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
from collections import deque, Counter
import hashlib,json,math,sys,time
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent
DPROJ=10**8;DFOOT=10**10
O=tuple(map(F,('0.02496294','0.00321635','-0.00678274')))
DELTA=F(1,2048);R=F(441,1000);HMAX=F(151,1000)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(t,a):return tuple(t*x for x in a)
def floor(x):return x.numerator//x.denominator
def interval(x,den=10**12):
    k=floor(x*den);return [k,k+1,den]
def load_geometry():
    b=(ROOT/'R82.txt').read_bytes();assert len(b)==1888 and hashlib.sha256(b).hexdigest()=='9765712b5ffaa464ed4d677974256294c6d867b77fe77b930d166853f66a92a7'
    lines=b.decode().splitlines();N,D=map(int,lines[0].split());A=[tuple(map(int,s.split())) for s in lines[1:]];assert len(A)==N==82
    verts={}
    # Exact exhaustive H triples. Cross products are cached but no candidate is
    # dropped on a numerical sign. Feasible triples reconstruct the whole hull.
    cr={(i,j):cross(A[i],A[j]) for i,j in combinations(range(N),2)}
    for i,j,k in combinations(range(N),3):
        w=dot(A[i],cr[j,k])
        if not w:continue
        u=tuple(D*(cr[j,k][t]-cr[i,k][t]+cr[i,j][t]) for t in range(3))
        if w<0:w=-w;u=tuple(-z for z in u)
        rhs=D*w
        if all(dot(a,u)<=rhs for a in A):
            v=tuple(F(z,w) for z in u);verts.setdefault(v,set()).update((i,j,k))
    V=sorted(verts);inc=[tuple(i for i,a in enumerate(A) if dot(a,v)==D) for v in V]
    assert len(V)==160 and all(len(t)==3 for t in inc)
    faces=[];avec=[];edge={};vol=F(0);moment=(F(0),)*3
    for j,n in enumerate(A):
        ii=[i for i,t in enumerate(inc) if j in t];assert len(ii)>=3
        # Numerical angle only nominates a cyclic order, subsequently checked by
        # exact all-corner support inequalities. It is not an acceptance predicate.
        centre=tuple(sum(V[i][k] for i in ii)/len(ii) for k in range(3))
        axis=min(range(3),key=lambda k:abs(n[k]));axisv=tuple(int(k==axis) for k in range(3))
        e=cross(n,axisv);f=cross(n,e)
        ii.sort(key=lambda i:math.atan2(float(dot(sub(V[i],centre),f)),float(dot(sub(V[i],centre),e))))
        av=(F(0),)*3
        for a,b in zip(ii,ii[1:]+ii[:1]):
            for c in ii:
                if c not in(a,b):assert dot(cross(sub(V[b],V[a]),sub(V[c],V[a])),n)>0
            av=add(av,mul(F(1,2),cross(V[a],V[b])))
            edge.setdefault(tuple(sorted((a,b))),[]).append((a,b,j))
        assert dot(av,n)>0 and cross(av,n)==(0,0,0)
        for b,c in zip(ii[1:-1],ii[2:]):
            va,vb,vc=V[ii[0]],V[b],V[c];w=dot(va,cross(vb,vc));assert w>0
            vol+=w/6;moment=add(moment,mul(w/24,add(add(va,vb),vc)))
        faces.append(ii);avec.append(av)
    assert len(edge)==240 and len(V)-len(edge)+len(faces)==2
    assert all(len(x)==2 and x[0][:2]==tuple(reversed(x[1][:2])) for x in edge.values())
    assert tuple(sum(v[k] for v in avec) for k in range(3))==(0,0,0)
    assert any(dot(A[i],cross(A[j],A[k]))!=0 for i,j,k in combinations(range(N),3))
    # Positive facet-area multiples of all normals sum to zero and the normals
    # span R^3; hence their nonpositive recession cone is {0}.
    c=mul(1/vol,moment)
    assert max(abs(c[i]-O[i]) for i in range(3))<F(1,10**8)
    # A closed supporting, strictly convex facet sphere plus exhaustive H triples
    # identifies this bounded full-dimensional intersection; origin is strict.
    neighbours=[set() for _ in V]
    for a,b in edge:neighbours[a].add(b);neighbours[b].add(a)
    seen={0};todo=[0]
    for a in todo:
        for b in neighbours[a]:
            if b not in seen:seen.add(b);todo.append(b)
    assert len(seen)==160
    return A,D,V,faces,avec,vol,c

def cube_min_norm2(lo,hi):return sum((a*a if a>0 else b*b if b<0 else 0) for a,b in zip(lo,hi))
def cube_max_norm2(lo,hi):return sum(max(a*a,b*b) for a,b in zip(lo,hi))
def lin_upper(a,lo,hi):return sum(max(x*l,x*h) for x,l,h in zip(a,lo,hi))
def abs_lin_upper(a,lo,hi):return max(lin_upper(a,lo,hi),lin_upper(tuple(-x for x in a),lo,hi))
def proof():
    t0=time.time();A,D,V,faces,AV,vol,c=load_geometry();print('geometry',len(V),len(faces),'seconds',time.time()-t0,flush=True)
    # The same ball is contained in the old K around EVERY tested target centre.
    for a in A:
        h=D-dot(a,O)-DELTA*sum(map(abs,a));assert h>0 and h*h>R*R*dot(a,a)
    a,b=[mul((D-dot(A[i],O))/dot(A[i],A[i]),A[i]) for i in(7,18)]
    d=sub(a,b);lam=-dot(b,d)/dot(d,d);assert 0<lam<1
    m=add(b,mul(lam,d));assert dot(m,m)<F(3,20)**2
    # At c in the centre cube each foot is its old foot minus an orthogonal
    # projection of c-O. Its Euclidean error is <=sqrt(3)*DELTA<2*DELTA.
    # Thus h<=min(n.a(c),n.b(c))<=n.m+2*DELTA<.15+2*DELTA<HMAX.
    assert F(3,20)+2*DELTA<HMAX and HMAX<R/2
    # Outward-rounded area vectors and feet; errors are retained in all bounds.
    AA=[tuple(floor(x*DPROJ) for x in z) for z in AV]
    FF=[tuple(floor(x*DFOOT) for x in z) for z in (a,b)]
    assert all(0<=x-F(k,DPROJ)<F(1,DPROJ) for z,ks in zip(AV,AA) for x,k in zip(z,ks))
    assert all(0<=x-F(k,DFOOT)<F(1,DFOOT) for z,ks in zip((a,b),FF) for x,k in zip(z,ks))
    # On |n_i|<=1, A_projection(n)<=.5 sum|n.AA_i|/DPROJ +123/DPROJ.
    areaerr=F(3*len(AA),2*DPROJ);footerr=F(3,DFOOT)+2*DELTA
    target=F(-1,25)
    # A dyadic cube cover of the whole unit sphere. No sampled directions enter
    # this proof. Cubes whose closed interval cannot meet the sphere are dropped;
    # cubes with h_upper<=0 cannot contain a positive-depth feasible root.
    stack=[((-1,-1,-1),(1,1,1),1,0)];stats=Counter();worst=None;maxdepth=0;leaves=[]
    while stack:
        lo,hi,den,depth=stack.pop();stats['visited']+=1;maxdepth=max(maxdepth,depth)
        if cube_min_norm2(lo,hi)>den*den or cube_max_norm2(lo,hi)<den*den:stats['off_sphere']+=1;continue
        H=min(HMAX,*(F(lin_upper(z,lo,hi),den*DFOOT)+footerr for z in FF))
        if H<=0:stats['no_positive_root_height']+=1;continue
        AP=F(sum(abs_lin_upper(z,lo,hi) for z in AA),2*den*DPROJ)+areaerr
        # Upper moment coefficient for any 0<h<=H:
        # J/h <= A_projection*h/2 -4R^3+6R^2*h-4h^3.
        # Its derivative is positive for h<=HMAX<R/2, so evaluate H.
        C=AP*H/2-4*R**3+6*R**2*H-4*H**3
        if C<target:
            stats['certified']+=1;worst=C if worst is None else max(worst,C)
            leaves.append([list(lo),list(hi),den,depth]);continue
        if depth>=12:raise AssertionError(('uncertified_cube',lo,hi,den,str(C)))
        mid=tuple(l+h for l,h in zip(lo,hi));ll=tuple(2*x for x in lo);hh=tuple(2*x for x in hi)
        for bits in product((0,1),repeat=3):
            nl=tuple(mid[i] if bits[i] else ll[i] for i in range(3));nh=tuple(hh[i] if bits[i] else mid[i] for i in range(3))
            stack.append((nl,nh,2*den,depth+1))
        stats['subdivided']+=1
    assert worst is not None and worst<target
    out={'identity':'J109_R82_ONE_STEP_POLAR_CUT_MASS_CAPACITY_EXCLUSION','kind':'exact_scoped_family_exclusion_not_110',
         'V':160,'E':240,'F':82,'reference_rational_O':list(map(str,O)),'target_centre_infinity_cube_radius':str(DELTA),
         'exact_old_volume':str(vol),'old_volume_interval':interval(vol),'old_centroid_intervals':[interval(x) for x in c],
         'inscribed_radius_for_entire_cube':str(R),'root_support_height_strict_upper':str(HMAX),
         'direct_old_polar_roots':[7,18],'foot_mixture_lambda':str(lam),'squared_norm_mixture':str(dot(m,m)),
         'projection_rounding_denominator':DPROJ,'foot_rounding_denominator':DFOOT,'area_error':str(areaerr),
         'foot_error_including_centre_cube':str(footerr),'stats':dict(stats),'maximum_depth':maxdepth,
         'largest_certified_coefficient_interval':interval(worst),'uniform_axial_moment_upper':'-h/25 (strict)',
         'rounded_area_vectors':AA,'rounded_feet':FF,
         'scope':'For every c in the stated closed infinity cube, every unit n and h>0 whose r=n/h receives nonnegative radial arrows from BOTH old polar points7 and18 centred at c, and every family of additional normalized cutting normals w with w.(r-w)>=0, no full-dimensional homogeneous intersection of literal K with r.(x-c)<=1 and all w.(x-c)<=1 has centroid c. Any number of controls, all normal directions, all depths and arbitrary facet retirement are covered. Controls outside the closed diameter ball, multi-step witnesses, changed old K, outer additions and centres outside the cube are NOT excluded.',
         'stronger_measurable_sandwich':'Every measurable L between B(c,R) intersect {n.(x-c)<=0, |x-c|+n.(x-c)<=2h} and K intersect {n.(x-c)<=h} has axial first moment about c strictly below -h/25; the actual intersections additionally contain the full K-paraboloid core.'}
    text=json.dumps(out,indent=2)+'\n';(ROOT/'J109_EXACT_CAPACITY.json').write_text(text)
    print(json.dumps({k:out[k] for k in ['stats','maximum_depth','largest_certified_coefficient_interval','old_volume_interval']},indent=2),flush=True)
    print('J109_ALL_DIRECT_ROOTS_ALL_ONE_STEP_CUT_CONTROLS_CENTRE_CUBE_MASS_EXCLUDED_EXACT_PASS_NO_110')
if __name__=='__main__':proof()
```
### FILE R82.txt
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
