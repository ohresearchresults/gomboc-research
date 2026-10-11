# material-ebbf64fe9441

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# J98 exact geometry core — single effective cover obstruction and finite witness depth

This is a complete recovery core, not an own110 construction. The literal source body is KH93_C434_R82_G6 from fully read immutable result figure-0581, SHA f4d4df1390c5e9bd18047aad823f3cd12e8c85751a66dbfc62ae50f67c779461. The standalone H input below is identical to that parent's 1888-byte input. No originating sandbox or decoded 47-file parent workspace is required by these computations. The parent's exact own211/weak000 audits are trusted author evidence; the coordinator independently computed the new conditional result below, not the parent's full census.

## Reconstruction and verification

Each FILE block is a complete UTF-8/LF file, with its final newline included before the closing fence. Extract all four FILE blocks into one directory. A complete extractor for this and other J98 materials is:

```python
from pathlib import Path
import re,sys
out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True)
for bundle in sys.argv[2:]:
    text=Path(bundle).read_text()
    for name,data in re.findall(r'(?ms)^### FILE ([^\n]+)\n```[^\n]*\n(.*?)^```\n',text):
        p=out/name
        assert not Path(name).is_absolute() and '..' not in Path(name).parts
        p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data.encode())
```

Run `python -B -S exact98.py`. Expected terminal marker: `J98_EXACT_SINGLE_COVER_OBSTRUCTION_PASS_NOT_110`. Expected EXACT98_CERTIFICATE.json: 3278 bytes, SHA 3db4268b560949d3b3921ab7a57092df00cf71b0b55b3c4d01806b2c72d2c4bc. It is deterministically generated, not a missing recovery input. Run `python gmpq98.py` for `GMPQ98_EXACT_ADAPTER_TEST_PASS`; this optional adapter accelerates later capacity certificates. Observed environment: Python 3.13.5, Linux GMP shared library. The exact geometry verifier itself uses only the standard library and no numerical tolerance.

Input/source manifest:
KH93_C434_R82_G6.txt: 1888 bytes, SHA 9765712b5ffaa464ed4d677974256294c6d867b77fe77b930d166853f66a92a7.
R82_LATTICE98.json: 3494 bytes, SHA 651ea1111c9e2ed093261133fc1f32f8c1459f2b36e66c6b472ae5676e83610c.
exact98.py: 7752 bytes, SHA 7f0d54f3e65abbf6478615d3cd1426793ec2642290685dbc1d92785fbb8b5e6f.
gmpq98.py: 4537 bytes, SHA 3e72f475aa26e26526e2ecb4f752e17c090daa294c2da9498502ca6793e2b3f8.

## Exact result and scope

Let c be the exact uniform-volume centroid of literal R82. At support level r=6339/10000, the two unit directions proportional to d=(447257,-71910,891510) and e=(-712036,1248759,-690383) belong to the same old junior sublevel component; the elder component containing old H18 is distinct. The verifier reconstructs every original vertex, proves the closed convex maximal-facet boundary, computes exact volume and first moments, and verifies both component paths and the entire connecting polar segment. The normalized dot product is strictly less than -6419/10000. Any single point a that lifts BOTH directions to r must therefore satisfy |a-c|^2 > 40182921/17905000. The old U squared radius is below (14969/10000)^2. The strict squared separation is greater than 1260308659/358100000000. Thus a single effective covering vertex cannot perform this whole-component lift while retaining the old U as unique unstable.

This remains true for actual centre displacement of Euclidean norm at most 1/20000, provided the elder remains below r minus that displacement bound and every other added point stays below the tested level in both selected directions. The shifted required radius squared is greater than 160706329/71620000, with squared separation greater than 4319715099/1432400000000 against the old-U radius upper bound enlarged by the displacement. The source proves the necessary height buffers exactly. This excludes only one effective covering vertex under these conditions. It does NOT exclude multiple effective points, larger centre motion, old-U or elder retirement, inner cuts, changed old geometry, or the research goal.

The support inclusion used is: if K is contained in L and |delta|<=epsilon, then {n:h_(L-delta)(n)<s} is contained in {n:h_K(n)<s+epsilon}. When the elder survives, a nondegenerate S1 endpoint cannot leave a second compact low-support component. Counting old facet normals alone is insufficient: the obstruction direction d is in the interior of an old polar facet.

## Finite whole-component certificate lemma

For K contained in B with the same interior origin, B polar is contained in K polar. Let C be a component of K polar outside a closed sphere. If B polar has any point x in C, choose a vertex z of B polar maximizing x dot z. Then x dot z>=|x|^2, and the segment x--z remains outside the sphere and inside K polar. Consequently at least one vertex of B polar lies in C. Testing ALL new polar vertices, with exact membership in the old outside-sphere components, is therefore a finite whole-component test. An outside point can be classified by radial extension to the old boundary followed by a norm-nondecreasing segment to a maximizing corner of that old facet. The old component graph uses only edges whose entire segments remain outside the sphere; convex-face radial retraction to the perimeter preserves its H0 components. Later J98 capacity material applies this test to an actual four-point hull, which removes the whole old component but still has nine reference S at higher levels.

## Finite-depth witness envelope (derived here, not a construction)

For centered old vertices p_v and m>=1, consider points a0 that can reach an old vertex through m strictly positive radial escape chords ai dot (a(i+1)-ai)>0. For unit direction n, their closed support supremum is
H_m(n)=max_v |p_v| cos(arccos(n dot p_v/|p_v|)/(m+1))^(m+1).
For m=1 this is max_v (n dot p_v+|p_v|)/2, the convex hull of old diameter witness balls. Proof: each chord bounds a radius ratio by the cosine of its angular increment. Include the support-projection cosine. Their m+1 angular increments have sum at least the endpoint angle, and concavity of log cos bounds their product by equal increments. Equally spaced great-circle directions with geometric radius ratios attain the closed bound; slight inward perturbations give strict chords. This is a pointwise supremum, not a finite covering, mass, edge-budget, or S1 certificate. Adding all points of such strict chains preserves reference U1 because each new nonroot has a later point as a witness, while the old strict radial maximum still dominates their radii. Own-centroid U1 requires separate physical mass analysis.

### FILE exact98.py
```python
"""Exact finite-direction single-cover-vertex obstruction on literal R82.
The target parent is the homogeneous body given by the supplied 82 integer H rows.
This verifies a conditional obstruction, NOT impossibility of multi-vertex extension,
changed-centre continuation, elder retirement, or the original C<500 problem.
Standard library; exact face lattice nomination is supplied as literal JSON.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
from collections import deque
import json,hashlib,sys

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(t,a):return tuple(t*x for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def meet(a,b,c,D):
    w=det(a,b,c);assert w
    return mul(F(D,w),add(add(cross(b,c),cross(c,a)),cross(a,b)))
def edge_min(a,b):
    d=sub(b,a);dd=dot(d,d);assert dd>0
    t=max(F(0),min(F(1),-dot(a,d)/dd));z=add(a,mul(t,d));return dot(z,z)
def interval(x,den=10**12):
    k=x.numerator*den//x.denominator
    return {'lower_numerator':k,'upper_numerator':k+1,'denominator':den,'strict_lower':x>F(k,den),'strict_upper':x<F(k+1,den)}
def main(root:Path):
    raw=(root/'KH93_C434_R82_G6.txt').read_bytes()
    assert len(raw)==1888 and hashlib.sha256(raw).hexdigest()=='9765712b5ffaa464ed4d677974256294c6d867b77fe77b930d166853f66a92a7'
    lines=raw.decode().splitlines();N,D=map(int,lines[0].split());A=[tuple(map(int,x.split())) for x in lines[1:]];assert len(A)==N==82
    spec=json.loads((root/'R82_LATTICE98.json').read_text());I=spec['incident_supports'];faces=spec['faces']
    assert len(I)==160 and len(faces)==82 and all(len(i)==3 for i in I)
    v=[meet(*(A[k] for k in i),D)for i in I]
    assert len(set(v))==160
    # Every listed vertex is a feasible intersection; incidence is exact, with no
    # unlisted tight H row. Every supplied facet is its entire supporting polygon.
    for x,ii in zip(v,I):
        tight=[]
        for k,a in enumerate(A):
            z=dot(a,x);assert z<=D
            if z==D:tight.append(k)
        assert tight==ii
    edgefaces={};W=F(0);T=(F(0),)*3
    for k,f in enumerate(faces):
        assert len(set(f))==len(f)>=3
        assert set(f)=={j for j,ii in enumerate(I)if k in ii}
        for j,a in enumerate(f):
            bb=f[(j+1)%len(f)];cc=f[(j+2)%len(f)]
            assert dot(cross(sub(v[bb],v[a]),sub(v[cc],v[bb])),A[k])>0
            for jj in f:
                if jj not in (a,bb):assert dot(cross(sub(v[bb],v[a]),sub(v[jj],v[a])),A[k])>0
            edgefaces.setdefault(tuple(sorted((a,bb))),[]).append((k,a,bb))
        for j in range(1,len(f)-1):
            a,b,c=(v[z]for z in (f[0],f[j],f[j+1]));w=det(a,b,c);assert w>0
            W+=w;T=add(T,mul(w,add(add(a,b),c)))
    assert len(edgefaces)==240 and len(v)-len(edgefaces)+len(faces)==2
    for ee,ff in edgefaces.items():
        assert len(ff)==2 and ff[0][1:]==tuple(reversed(ff[1][1:]))
    seen={0};todo=deque([0]);vedges=[set()for _ in v]
    for a,b in edgefaces:vedges[a].add(b);vedges[b].add(a)
    while todo:
        a=todo.popleft()
        for b in vedges[a]:
            if b not in seen:seen.add(b);todo.append(b)
    assert len(seen)==len(v)
    # The closed, outward, convex supporting-facet sphere is the boundary of conv(v).
    # Its exactly 82 facet halfspaces are exactly the supplied H system.
    V=W/6;g=mul(1/(4*W),T);p=[sub(x,g)for x in v]
    y=[mul(F(1,D),a)for a in A]
    off=[1-dot(a,g)for a in y];assert min(off)>0
    q=[mul(1/h,a)for a,h in zip(y,off)]
    qe=[(ff[0][0],ff[1][0])for ff in edgefaces.values()]
    r=F(6339,10000);cut=1/r**2
    adj=[[]for _ in q]
    for i,j in qe:
        if edge_min(q[i],q[j])>cut:adj[i].append(j);adj[j].append(i)
    pred={7:None};todo=deque([7])
    while todo:
        u=todo.popleft()
        for z in adj[u]:
            if z not in pred:pred[z]=u;todo.append(z)
    expected=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,21,23,24,27,30,32,37,39,44,48,53,55]
    assert sorted(pred)==expected and 18 not in pred
    assert dot(q[7],q[7])>cut and dot(q[18],q[18])>cut
    paths={}
    for z in [17,55]:
        pp=[z]
        while pred[pp[-1]]is not None:pp.append(pred[pp[-1]])
        paths[str(z)]=pp[::-1]
    d=(447257,-71910,891510);e=A[17]
    hh=[dot(d,x)for x in p];h=max(hh);ind=hh.index(h)
    assert I[ind]==[43,53,55]
    assert h>0 and h*h<r*r*dot(d,d)
    qa=mul(1/h,d)
    # qa lies in the polar facet at the physical vertex {43,53,55}.
    # The entire segment to corner55 stays outside the chosen sphere.
    assert edge_min(qa,q[55])>cut
    he=off[17]*D;assert he>0 and he*he<r*r*dot(e,e)
    # The two normalized directions have inner product strictly less than -0.6419.
    c=F(-6419,10000);de=dot(d,e);dd=dot(d,d);ee=dot(e,e)
    assert de<0 and de*de>c*c*dd*ee
    u=I.index([13,33,79]);R2=dot(p[u],p[u]);Rbar=F(14969,10000)
    assert R2<Rbar**2
    # The old unique U remains the strict radial maximum; verify directly too.
    assert all(dot(x,x)<R2 for j,x in enumerate(p)if j!=u)
    required2=2*r*r/(1+c)
    assert required2>Rbar**2
    eps=F(1,20000)
    assert h*h<(r-2*eps)**2*dot(d,d)
    assert he*he<(r-2*eps)**2*dot(e,e)
    assert off[18]**2<(r-2*eps)**2*dot(y[18],y[18])
    shifted_required2=2*(r-eps)**2/(1+c)
    assert shifted_required2>(Rbar+eps)**2
    # Every direction covered by a single point must satisfy
    # 2r <= a.(n_d+n_e) <= |a| sqrt(2+2 n_d.n_e).
    # Thus |a|^2 > required2 > Rbar^2 > |oldU|^2.
    out={'identity':'J98_R82_SINGLE_EFFECTIVE_COVER_VERTEX_OBSTRUCTION','kind':'exact_conditional_negative_result_not_body',
        'V':len(v),'E':len(edgefaces),'F':len(faces),'support_level':str(r),
        'direction_a':list(d),'direction_b':list(e),'angle_dot_strict_upper':str(c),
        'old_U_incident_supports':[13,33,79],'local_U_index':u,'actual_volume_interval':interval(V),
        'actual_centroid_intervals':[interval(x)for x in g],'old_U_radius_squared_interval':interval(R2),
        'old_U_radius_strict_upper':str(Rbar),'single_point_required_radius_squared_strict_lower':str(required2),
        'squared_radius_separation_strict_lower':str(required2-Rbar**2),
        'moving_centre_euclidean_epsilon':str(eps),'moving_centre_required_radius_squared_strict_lower':str(shifted_required2),
        'moving_centre_squared_radius_separation_strict_lower':str(shifted_required2-(Rbar+eps)**2),
        'junior_component':expected,'junior_paths':paths,'polar_segment_qa_q55_min_squared_interval':interval(edge_min(qa,q[55])),
        'polar_level_squared':str(cut),'max_input_coordinate_bits':max(max(z.numerator.bit_length(),z.denominator.bit_length())for x in v for z in x),
        'centroid_denominator_bits':max(z.denominator.bit_length()for z in g),
        'scope':'At the unchanged actual parent centroid, or with actual centre displacement of Euclidean norm at most 1/20000, any outer extension retaining the old U as unique unstable and retaining an elder low-support direction below 6339/10000 minus the displacement bound cannot reach nondegenerate S1 with only ONE effective added vertex lifting the two specified old-junior directions. All other added points are assumed below that new level in both directions. Multiple effective cover vertices, larger centre motion, elder retirement, or deleting/moving old material are not excluded.'}
    text=json.dumps(out,indent=2)+'\n';(root/'EXACT98_CERTIFICATE.json').write_text(text);print(text);print('J98_EXACT_SINGLE_COVER_OBSTRUCTION_PASS_NOT_110')
if __name__=='__main__':main(Path(sys.argv[1])if len(sys.argv)>1 else Path(__file__).parent)
```
### FILE gmpq98.py
```python
"""Small exact GMP rational adapter used to accelerate the capacity certificate.
No third-party Python package is needed. Uses GMP's public mpq interface via ctypes.
Fraction fallback is selected in capexact98 with --fraction.
"""
from __future__ import annotations
import ctypes as C
import ctypes.util
import sys
from fractions import Fraction
sys.set_int_max_str_digits(0)

class Z(C.Structure):
    _fields_=[('_mp_alloc',C.c_int),('_mp_size',C.c_int),('_mp_d',C.c_void_p)]
class RawQ(C.Structure):
    _fields_=[('_mp_num',Z),('_mp_den',Z)]
lib=C.CDLL(ctypes.util.find_library('gmp')or'libgmp.so.10')
P=C.POINTER(RawQ)
def bind(name,args,result=None):
    fn=getattr(lib,'__gmpq_'+name);fn.argtypes=args;fn.restype=result;return fn
_init=bind('init',[P]);_clear=bind('clear',[P]);_set=bind('set',[P,P]);_setstr=bind('set_str',[P,C.c_char_p,C.c_int],C.c_int)
_canon=bind('canonicalize',[P]);_add=bind('add',[P,P,P]);_sub=bind('sub',[P,P,P]);_mul=bind('mul',[P,P,P]);_div=bind('div',[P,P,P]);_neg=bind('neg',[P,P]);_cmp=bind('cmp',[P,P],C.c_int)
_double=bind('get_d',[P],C.c_double);_string=bind('get_str',[C.c_char_p,C.c_int,P],C.c_void_p)
_size=getattr(lib,'__gmpz_sizeinbase');_size.argtypes=[C.POINTER(Z),C.c_int];_size.restype=C.c_size_t

class Q:
    __slots__=('raw',)
    def __init__(self,a=0,b=None):
        self.raw=RawQ();_init(C.byref(self.raw))
        if isinstance(a,Q)and b is None:_set(C.byref(self.raw),C.byref(a.raw));return
        if b is not None:
            if b==0:raise ZeroDivisionError
            aa=a if isinstance(a,Q)else Q(a);bb=b if isinstance(b,Q)else Q(b)
            _div(C.byref(self.raw),C.byref(aa.raw),C.byref(bb.raw));return
        if isinstance(a,Fraction):s=f'{a.numerator}/{a.denominator}'
        elif isinstance(a,int):s=str(a)
        elif isinstance(a,str):s=a
        else:raise TypeError(f'non-exact Q input: {type(a)}')
        if _setstr(C.byref(self.raw),s.encode(),10)!=0:raise ValueError(s)
        _canon(C.byref(self.raw))
    def __del__(self):
        if hasattr(self,'raw'):_clear(C.byref(self.raw))
    def __str__(self):
        n=int(_size(C.byref(self.raw._mp_num),10)+_size(C.byref(self.raw._mp_den),10)+6)
        buf=C.create_string_buffer(n);_string(buf,10,C.byref(self.raw));return buf.value.decode()
    def __repr__(self):return 'Q('+repr(str(self))+')'
    @property
    def numerator(self):return int(str(self).split('/')[0])
    @property
    def denominator(self):
        ss=str(self).split('/');return int(ss[1])if len(ss)>1 else 1
    def __float__(self):return _double(C.byref(self.raw))
    def __bool__(self):return self.raw._mp_num._mp_size!=0
    def __hash__(self):return hash(Fraction(self.numerator,self.denominator))
    def _binary(self,b,fn):
        bb=b if isinstance(b,Q)else Q(b);z=Q();fn(C.byref(z.raw),C.byref(self.raw),C.byref(bb.raw));return z
    def __add__(self,b):return self._binary(b,_add)
    __radd__=__add__
    def __sub__(self,b):return self._binary(b,_sub)
    def __rsub__(self,b):return Q(b)._binary(self,_sub)
    def __mul__(self,b):return self._binary(b,_mul)
    __rmul__=__mul__
    def __truediv__(self,b):
        if b==0:raise ZeroDivisionError
        return self._binary(b,_div)
    def __rtruediv__(self,b):
        if not self:raise ZeroDivisionError
        return Q(b)._binary(self,_div)
    def __neg__(self):z=Q();_neg(C.byref(z.raw),C.byref(self.raw));return z
    def __abs__(self):return -self if self.raw._mp_num._mp_size<0 else Q(self)
    def __pow__(self,n):
        if not isinstance(n,int):raise TypeError('integer exponents only')
        if n<0:return (1/self)**(-n)
        z=Q(1);a=Q(self)
        while n:
            if n&1:z=z*a
            a=a*a;n//=2
        return z
    def compare(self,b):
        bb=b if isinstance(b,Q)else Q(b);return _cmp(C.byref(self.raw),C.byref(bb.raw))
    def __eq__(self,b):
        try:return self.compare(b)==0
        except (TypeError,ValueError):return False
    def __lt__(self,b):return self.compare(b)<0
    def __le__(self,b):return self.compare(b)<=0
    def __gt__(self,b):return self.compare(b)>0
    def __ge__(self,b):return self.compare(b)>=0

if __name__=='__main__':
    import random
    r=random.Random(981)
    for _ in range(100):
        a,b,c,d=[r.randrange(1,10**30)for _ in range(4)];x=Fraction(a,b);y=Fraction(c,d);X=Q(a,b);Y=Q(c,d)
        for u,v in [(x+y,X+Y),(x-y,X-Y),(x*y,X*Y),(x/y,X/Y),(-x,-X),(x**2,X**2)]:assert str(u)==str(v)
        assert (x<y)==(X<Y) and hash(x)==hash(X)
    print('GMPQ98_EXACT_ADAPTER_TEST_PASS')
```
### FILE KH93_C434_R82_G6.txt
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
### FILE R82_LATTICE98.json
```json
{"incident_supports":[[40,65,67],[11,13,18],[13,43,59],[13,57,59],[43,53,55],[8,11,18],[8,12,18],[18,28,31],[49,53,55],[50,57,70],[38,50,59],[50,57,59],[57,79,80],[57,70,80],[13,18,33],[13,33,79],[18,33,62],[33,62,79],[57,79,81],[13,79,81],[13,57,81],[43,59,61],[38,59,61],[38,61,72],[13,30,37],[15,17,18],[15,18,23],[12,14,18],[14,18,23],[18,34,40],[18,31,34],[17,18,20],[18,20,22],[18,25,28],[18,22,25],[18,26,40],[18,26,29],[26,29,40],[29,40,42],[29,36,45],[18,29,45],[46,60,67],[46,51,60],[40,46,67],[40,42,46],[36,46,51],[29,36,46],[29,42,46],[49,67,74],[49,55,74],[65,67,68],[47,60,67],[38,47,50],[38,47,74],[47,67,74],[50,69,70],[47,50,69],[63,70,80],[63,69,70],[62,63,79],[63,79,80],[18,62,77],[58,62,77],[9,11,13],[13,21,24],[24,27,65],[27,30,65],[13,24,27],[13,27,30],[30,32,65],[30,32,37],[32,65,68],[32,37,68],[1,7,9],[7,9,13],[7,13,16],[2,9,11],[51,54,60],[45,54,60],[45,51,54],[36,41,51],[36,41,45],[41,45,51],[60,75,78],[45,60,75],[75,77,78],[18,45,75],[18,75,77],[43,55,73],[55,73,74],[43,61,73],[61,72,73],[38,72,73],[38,73,74],[49,67,71],[67,68,71],[49,53,71],[44,68,71],[13,43,44],[62,63,66],[63,66,69],[47,62,66],[47,66,69],[60,76,78],[76,77,78],[58,76,77],[47,62,64],[58,62,64],[47,60,64],[58,60,64],[13,19,21],[13,16,19],[37,39,68],[39,44,68],[13,37,39],[13,39,44],[48,53,71],[44,48,71],[43,48,53],[43,44,48],[56,58,60],[56,60,76],[56,58,76],[0,1,3],[1,6,9],[1,3,6],[2,6,9],[6,15,23],[1,5,7],[0,1,5],[4,8,11],[2,4,11],[4,8,12],[4,12,14],[0,5,52],[0,3,52],[5,7,52],[7,16,52],[40,52,65],[16,19,52],[19,21,52],[24,52,65],[21,24,52],[2,6,10],[2,4,10],[4,10,14],[10,14,23],[6,10,23],[3,35,52],[15,17,35],[17,20,35],[6,15,35],[3,6,35],[20,22,35],[22,25,35],[25,28,35],[28,31,35],[31,34,35],[34,35,40],[35,40,52]],"faces":[[134,135,123,129],[125,124,73,128,129,123],[144,131,76,126,143],[152,125,123,135,148],[145,133,132,130,131,144],[134,129,128,136],[147,143,126,124,125,152,151,127],[137,136,128,73,74,75],[6,5,130,132],[124,126,76,63,74,73],[145,144,143,147,146],[130,5,1,63,76,131],[27,6,132,133],[24,68,67,64,110,111,75,74,63,1,14,15,19,20,3,2,98,115,114],[28,27,133,145,146],[127,151,149,25,26],[137,75,111,139],[31,25,149,150],[36,40,86,87,61,16,14,1,5,6,27,28,26,25,31,32,34,33,7,30,29,35],[139,111,110,140],[32,31,150,153],[140,110,64,142],[34,32,153,154],[146,147,127,26,28],[141,142,64,67,65],[154,155,33,34],[36,35,37],[66,65,67,68],[155,156,7,33],[39,40,36,37,38,47,46],[66,68,24,70,69],[30,7,156,157],[72,71,69,70],[17,15,14,16],[157,158,29,30],[155,154,153,150,149,151,152,148,159,158,157,156],[80,81,39,46,45],[112,72,70,24,114],[93,92,23,22,10,52,53],[113,112,114,115],[29,158,159,138,0,43,44,38,37,35],[81,80,82],[47,38,44],[4,118,119,98,2,21,90,88],[115,98,119,117,97,113],[84,86,40,39,81,82,79,78],[44,43,41,42,45,46,47],[102,101,106,108,51,54,53,52,56],[118,116,117,119],[94,96,8,49,48],[52,10,11,9,55,56],[80,45,42,77,79,82],[138,159,148,135,134,136,137,139,140,142,141],[116,118,4,8,96],[79,77,78],[49,8,4,88,89],[121,120,122],[13,9,11,3,20,18,12],[109,107,62,105,122,120],[22,21,2,3,11,10],[103,83,84,78,77,42,41,51,108,109,120,121],[91,90,21,22,23],[99,59,17,16,61,62,107,106,101],[99,100,58,57,60,59],[108,106,107,109],[69,71,50,0,138,141,65,66],[102,100,99,101],[51,41,43,0,50,95,94,48,54],[113,97,95,50,71,72,112],[56,55,58,100,102],[58,55,9,13,57],[116,96,94,95,97,117],[91,23,92],[93,89,88,90,91,92],[93,53,54,48,49,89],[86,84,83,85,87],[105,104,103,121,122],[104,105,62,61,87,85],[85,83,103,104],[17,59,60,12,18,19,15],[57,13,12,60],[19,18,20]]}
```
