# material-b23c2c251066

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J139 recovery capsule, part 2/4

Proofs and scope: part1 [internal-source-reference]. Required unchanged exact dependencies are J137 [internal-source-reference]/exact137.py and [internal-source-reference]/LOW43.json, fully specified in part1. Supply BOTH literal materials to a fresh computational successor. No optimizer rerun is needed to recover these exact bodies, their own census or their global model U lower bounds.

Extract fenced file units with regex `r'### File: ([^\n]+)\n```[^\n]*\n(.*?)```'` and re.S; write group2 verbatim, UTF-8, including its final newline. Do not strip whitespace.

Commands, CPython3.13.5 standard library:
```
python -B -S certcycle139.py HIGH139_R12_CYCLE.json
python -B -S certcycle139.py ROOT139_R12_CYCLE.json
```
Expected terminal markers:
```
CYCLE139_EXACT_PASS HIGH139_R12 [41, 117, 78] [25, 9, 32] [0, 0, 0] GLOBAL_U_AT_LEAST 8
CYCLE139_EXACT_PASS ROOT139_R12 [43, 123, 82] [27, 10, 35] [0, 0, 0] GLOBAL_U_AT_LEAST 9
```
Input/source receipts: certcycle139.py6148B,SHA486dab45a94a462c2ce08a83d6f7c2865276677948b9027a049981f0a283e958; HIGH139_R12_CYCLE.json4146B,SHA32c4cde6f2e278fc42b47b651424bcf2adde88539f77385f08e4dc78608b4d52; ROOT139_R12_CYCLE.json3471B,SHAe8fee7094e1ec74afe4394102d1aa88c472947c414e2a1ceb8c89cacf936a160.
Outputs: HIGH139_R12_CYCLE_CERT.json475447B,SHA34e9d88f542e2f75ab45b0a9e8b2a7a3cee5f3048015065d3df55d34f5178dc7; ROOT139_R12_CYCLE_CERT.json529886B,SHA4ba6c4460acd73d01e9ffab7b392256e43caa8aa29db826a007c886fce35f110.

The two rational input objects are identical to the earlier fan-format HIGH139_R12/ROOT139_R12 bodies/models. Exact aggregation drops zero mixture terms but no positive term. The cycle orientation/degree certificate directly proves the globally valid density bound. Frozen own classes differ from the ideal global minimizers' only-partially-certified census; retain that distinction.

### File: certcycle139.py
```python
"""Rational all-fan global minimum bracket and directional mass certificate.
Standard library only. Reuses unchanged exact137.py for maximal hull and census.
No optimizer result, float sign, or unvalidated triangulation is accepted.
"""
import sys,json,math,itertools,hashlib
from pathlib import Path
from fractions import Fraction as Q
from exact137 import dot,sub,mul,add,cross,det,lattice,mass,classify,clean
sys.set_int_max_str_digits(0)

def common(points):
 D=math.lcm(*(x.denominator for p in points for x in p));W=[tuple(int(x*D) for x in p) for p in points]
 gg=math.gcd(D,*(v for p in W for v in p));return [tuple(x//gg for x in p) for p in W],D//gg

def solve3cols(a,b,c,y):
 d=det(a,b,c);assert d
 return (det(y,b,c)/d,det(a,y,c)/d,det(a,b,y)/d)

def root4floor(q,L):
 assert q>=0
 n=math.isqrt(math.isqrt(q.numerator*L**4//q.denominator))
 assert Q(n,L)**4<=q<Q(n+1,L)**4
 return Q(n,L)

def sqrtfloor(q,L=10**24):
 assert q>=0
 n=math.isqrt(q.numerator*L**2//q.denominator)
 assert Q(n,L)**2<=q<Q(n+1,L)**2
 return Q(n,L)

def localization(R,t,w,d,vs,tri,UB,LB):
 """Global minimizer localization via nonnegative AM-GM dual slack.
 If F(s)<=UB, every square-root radius lies in the returned rational box.
 """
 L=10**24;blo=[Q(0)]*len(t);bhi=[Q(0)]*len(t)
 for v,(i,j,k) in zip(vs,tri):
  if v==0:continue
  rr=w[i]*w[j]*w[k]/(d[i]*d[j]*d[k]);lo=root4floor(rr,L);gglo=v*lo;gghi=v*(lo+Q(1,L))
  for z in (i,j,k):
   alpha=v/t[z]*w[z]/d[z]
   blo[z]+=sqrtfloor(alpha*gglo,L)
   bhi[z]+=sqrtfloor(alpha*gghi,L)+Q(1,L)
 gap=UB-LB;intervals=[]
 for i,wi in enumerate(w):
  err=sqrtfloor(gap/wi,L)+Q(1,L)
  yl=max(Q(0),blo[i]/wi-err);yu=bhi[i]/wi+err
  intervals.append((yl*yl,yu*yu))
 roots=[];maximum_upper=[]
 for i,ri in enumerate(R):
  rr=dot(ri,ri);bounds=[]
  for j,rj in enumerate(R):
   if i==j:continue
   pp=dot(ri,rj);bd=pp*intervals[i][1 if pp>=0 else 0]-rr*intervals[j][0]
   bounds.append((bd,j))
  bd,j=max(bounds);maximum_upper.append(bd)
  if bd<0:roots.append({'vertex':i,'worst_target':j,'maximum_arrow_upper':bd})
 return {'t_intervals':intervals,'certified_U_at_global_balanced_minimizer':roots,'all_vertex_maximum_arrow_upper':maximum_upper,'scope':'The exact positive balanced-weight minimizer is centered at zero and lies in this box. These strict all-chord inequalities certify actual U vertices there; they do NOT exclude other weights or all fixed-ray centered bodies.'}

def cycle_certificate(RI,rows,den):
 faces=[];edges={};total=Q(0)
 for i,j,k,c in rows:
  assert c>0 and len({i,j,k})==3
  if det(RI[i],RI[j],RI[k])<0:j,k=k,j
  assert det(RI[i],RI[j],RI[k])>0
  faces.append((i,j,k,c))
  for a,b in ((i,j),(j,k),(k,i)):edges[(a,b)]=edges.get((a,b),0)+c
 assert all(c==edges.get((b,a),0) for (a,b),c in edges.items())
 for k in range(1,1001):
  probe=(1,k,k*k)
  if all(det(RI[a],RI[b],probe)!=0 for a,b in edges):break
 else:raise AssertionError('no generic probe found')
 cover=sum(c for i,j,k,c in faces if det(probe,RI[j],RI[k])>0 and det(RI[i],probe,RI[k])>0 and det(RI[i],RI[j],probe)>0)
 assert cover==den
 return {'triangles':len(rows),'probe':list(probe),'weighted_coverage_numerator':cover,'denominator':den,'weighted_closed_edges':len(edges)//2}

def verify(path):
 src=json.loads(Path('LOW43.json').read_text());W,F,N,HH,E,EF,active=lattice(src['rows']);Vp,gp=mass(W,F,src['denominator'])
 R=[sub(tuple(Q(x,src['denominator']) for x in row),gp) for row in W];RI,RD=common(R)
 p=json.loads(Path(path).read_text());T=p['grid'];t=[Q(x,T) for x in p['t_int']];w=[Q(x,T) for x in p['w_int']]
 assert min(t)>0 and min(w)>0 and p['cycle_denominator']>0
 triple=max(itertools.combinations(range(len(R)),3),key=lambda q:abs(det(*(RI[i] for i in q))))
 defect=tuple(sum(wi*ri[k] for wi,ri in zip(w,R)) for k in range(3));corr=solve3cols(*(R[i] for i in triple),mul(-1,defect))
 for i,c in zip(triple,corr):w[i]+=c
 assert min(w)>0 and all(sum(wi*ri[k] for wi,ri in zip(w,R))==0 for k in range(3))
 cycle=cycle_certificate(RI,p['weighted_triangles'],p['cycle_denominator'])
 X=[mul(1/ti,ri) for ti,ri in zip(t,R)];WX,DX=common(X)
 WX,FX,NX,HX,EX,EFX,AX=lattice(WX);V,g=mass(WX,FX,DX);assert min(HX)>0
 vs=[];tri=[];d=[Q(0)]*len(R);M=[Q(0)]*3
 for i,j,k,cc in p['weighted_triangles']:
  c=Q(cc,p['cycle_denominator']);v=c*abs(det(R[i],R[j],R[k]))/(6*t[i]*t[j]*t[k]);vs.append(v);tri.append((i,j,k))
  for a in (i,j,k):d[a]+=v/t[a]
  for a in range(3):M[a]+=v*(X[i][a]+X[j][a]+X[k][a])/4
 assert min(d)>0
 vb=sum(vs);delta=V-vb;assert delta>=0
 assert all(sum(R[i][k]*d[i] for i in range(len(R)))==4*M[k] for k in range(3))
 intervals=[]
 for k in range(3):
  lo=(M[k]+delta*min(x[k] for x in X))/V;hi=(M[k]+delta*max(x[k] for x in X))/V
  assert lo<=g[k]<=hi;intervals.append((lo,hi))
 UB=V+sum(wi*ti for wi,ti in zip(w,t));LB=Q(0)
 for v,(i,j,k) in zip(vs,tri):LB+=4*v*root4floor(w[i]*w[j]*w[k]/(d[i]*d[j]*d[k]),10**24)
 assert 0<LB<=UB
 loc=localization(R,t,w,d,vs,tri,UB,LB);own=classify(WX,FX,NX,HX,EX,EFX,AX,DX,g)
 out={'name':p['name'],'input_sha256':hashlib.sha256(Path(path).read_bytes()).hexdigest(),'parent_sha256':hashlib.sha256(Path('LOW43.json').read_bytes()).hexdigest(),'true_VEF':[len(AX),len(EX),len(FX)],'C':2*len(EX),'facets':FX,'active_vertices':AX,'balanced_correction_indices':triple,'balanced_correction':corr,'balanced_weights':w,'cycle':cycle,'V':V,'mixture_volume':vb,'volume_defect':delta,'relative_volume_defect':delta/V,'mixture_moment':M,'mass_intervals':intervals,'actual_centroid':g,'centroid_is_zero':all(x==0 for x in g),'centroid_linf_bound':max(abs(x) for pair in intervals for x in pair),'objective_lower_bound':LB,'objective_upper_bound':UB,'relative_objective_gap_bound':(UB-LB)/UB,'localization':loc,'coordinate_bits':max(abs(v).bit_length() for row in WX for v in row),'coordinate_denominator_bits':DX.bit_length(),'own':own}
 out=clean(out);dest=Path(path).with_name(Path(path).stem+'_CERT.json');dest.write_text(json.dumps(out,indent=2)+'\n')
 print('CYCLE139_EXACT_PASS',p['name'],out['true_VEF'],own['strict'],own['weak'],'GLOBAL_U_AT_LEAST',len(loc['certified_U_at_global_balanced_minimizer']),flush=True)
 return out
if __name__=='__main__':verify(sys.argv[1])
```

### File: HIGH139_R12_CYCLE.json
```json
{"name":"HIGH139_R12","grid":1000000000000,"t_int":[1027433945121,1056928622194,979020512905,1063270084976,1050625654945,999766840687,978949058337,991744163743,1004070108339,999796249802,990058160260,997931509963,1012318891876,1008472139454,1047678018394,1029588696541,1017529194048,1027437311871,970158094091,1031842218655,1024355661600,1016282594200,1016291002396,1032784738711,982419968118,1005622241974,1026836485788,1026731971751,1013819364692,1033331286053,1020470638429,1021808763667,1020118049508,1025737113217,1021491164108,1023206232280,1013218627333,1017913468539,1015082507703,1013930967280,1009403777508,1012181174591,993071917535],"w_int":[175582226503,9531858450,31464094710,60201525764,11693356386,15475718048,47835770590,12264120470,16060560071,13188623848,11163129692,9783530590,5693042060,16149286979,48597183121,12212346348,17923192233,35285840689,49828647674,6979967989,15360503808,15984657821,14094918178,10804658338,15559930690,29371024650,11942466346,8469303739,36996207278,58766237341,15982424635,9609558209,9421467712,28269430118,11210318374,7895730150,14190870891,10546800838,12184784279,19499321742,3198032001,7482327668,13313195057],"cycle_denominator":1000000000001,"weighted_triangles":[[0,1,3,5202883249],[0,1,18,5202883249],[0,2,3,1000000000001],[0,2,7,915238927721],[0,2,8,84761072280],[0,3,18,994797116752],[0,5,8,1000000000001],[0,5,9,1000000000001],[0,7,8,915238927721],[0,9,10,2592159544],[0,9,11,997407840457],[0,10,11,997407840457],[0,10,13,5853763110],[0,10,15,986357192236],[0,10,17,7789044655],[0,13,15,238119804779],[0,13,17,756026432112],[0,13,26,990911271554],[0,13,27,9088728447],[0,15,17,748237387457],[0,16,32,1000000000001],[0,16,37,1000000000001],[0,18,24,17874050417],[0,18,25,449641545849],[0,18,40,136625360407],[0,18,41,339954696732],[0,18,42,55904346596],[0,21,22,1000000000001],[0,21,37,1000000000001],[0,22,38,1000000000001],[0,24,33,1000000000001],[0,24,40,997485],[0,24,42,982124952099],[0,25,41,346560198439],[0,25,42,103081347410],[0,26,27,990911271554],[0,27,30,1000000000001],[0,30,31,1000000000001],[0,31,32,1000000000001],[0,33,36,1000000000001],[0,36,39,1000000000001],[0,38,39,1000000000001],[0,40,42,136624362922],[0,41,42,686514895171],[1,3,6,1000000000001],[1,3,18,994797116752],[1,4,6,1000000000001],[1,4,18,1000000000001],[2,3,7,1000000000001],[2,7,8,84761072280],[3,6,7,1000000000001],[4,6,14,1000000000001],[4,14,18,1000000000001],[5,8,17,1000000000001],[5,9,17,1000000000001],[6,7,8,842453515401],[6,7,12,157546484600],[6,8,12,842453515401],[6,12,17,1000000000001],[6,14,29,1000000000001],[6,17,29,1000000000001],[7,8,12,157546484600],[8,12,17,1000000000001],[9,10,11,2592159544],[9,11,17,1000000000001],[10,11,17,1000000000001],[10,13,17,5853763110],[10,15,17,986357192236],[13,15,17,238119804779],[13,17,23,1000000000001],[13,23,26,1000000000001],[13,26,27,9088728447],[14,18,19,158845915],[14,18,25,999841154086],[14,19,25,999841154086],[14,19,28,1000000000001],[14,28,29,1000000000001],[16,20,21,1000000000001],[16,20,29,1000000000001],[16,21,37,1000000000001],[16,29,30,1000000000001],[16,30,31,1000000000001],[16,31,32,1000000000001],[17,23,29,1000000000001],[18,19,25,158845915],[18,24,25,25249255811],[18,24,40,997485],[18,24,42,7374207909],[18,25,40,136621562072],[18,25,41,276768971165],[18,25,42,111718665104],[18,40,42,2800850],[18,41,42,63185725567],[19,25,28,1000000000001],[20,21,35,1000000000001],[20,28,29,1000000000001],[20,28,34,1000000000001],[20,34,35,1000000000001],[21,22,35,1000000000001],[22,35,39,1000000000001],[22,38,39,1000000000001],[23,26,30,1000000000001],[23,29,30,1000000000001],[24,25,33,1000000000001],[24,25,40,142965104],[24,25,42,974607779086],[24,40,42,142965104],[25,28,33,1000000000001],[25,40,41,346560198439],[25,40,42,483038795407],[25,41,42,276768971165],[26,27,30,1000000000001],[28,33,34,1000000000001],[33,34,36,14311250419],[33,34,39,985688749582],[33,36,39,985688749582],[34,35,39,1000000000001],[34,36,39,14311250419],[40,41,42,346560198439]],"representation":"Exact aggregation of positive fan mixture; weighted oriented closed cone cycle of degree one. Same t and balanced-w models as the original fan checkpoint."}
```

### File: ROOT139_R12_CYCLE.json
```json
{"name":"ROOT139_R12","grid":1000000000000,"t_int":[1001411008922,1000415905552,1000145936333,1000217928947,1000343006486,1000275258732,1000623815956,1000399422869,1000339501015,1000263278917,1000248529022,1000256095062,1000493203939,1000055361403,1000000775084,999881890145,1000590516996,999988355868,998857512689,999973618946,991032304170,996059044864,999952368197,1000325618236,1000632773283,999979307065,999516881184,999441394172,998874301018,1000246626578,999296017312,999309782175,998688352525,995185591276,1035001876774,1019199344358,1000921640436,999253966199,999931250599,992948454217,999521892703,999521351970,999057224920],"w_int":[191317812486,10803036206,32298087236,68154591244,13226313131,15896366183,49340274010,12643957457,16547276842,13500262009,11339108098,9971666758,5849566777,16141313752,54565841107,12367346587,19498059305,39560713794,49514347887,7735842117,16829791619,17284879382,15207762961,12041723892,15242247212,32123716997,13220279384,9344266707,40500167920,65042311445,17573728681,10525392170,10283403343,30463986543,11027451657,8588311232,15270281852,11437196087,13124458902,20979914837,3158539464,7393876569,13069809507],"cycle_denominator":999999999999,"weighted_triangles":[[0,2,3,999999999999],[0,2,7,999999999999],[0,3,18,999999999999],[0,5,8,999999999999],[0,5,9,999999999999],[0,7,8,999999999999],[0,9,11,999999999999],[0,10,11,999999999999],[0,10,15,999999999999],[0,13,17,999999999999],[0,13,26,999999999999],[0,15,17,999999999999],[0,16,32,999999999999],[0,16,37,999999999999],[0,18,25,999999999999],[0,21,22,999999999999],[0,21,37,999999999999],[0,22,38,999999999999],[0,24,33,999999999999],[0,24,42,999999999999],[0,25,41,999999999999],[0,26,27,999999999999],[0,27,30,999999999999],[0,30,31,999999999999],[0,31,32,999999999999],[0,33,36,999999999999],[0,36,39,999999999999],[0,38,39,999999999999],[0,41,42,999999999999],[1,3,4,310054903],[1,3,6,999999999999],[1,3,18,999689945096],[1,4,6,999999999999],[1,4,18,999689945096],[2,3,7,999999999999],[3,4,18,310054903],[3,6,7,999999999999],[4,6,14,999999999999],[4,14,18,999999999999],[5,8,17,999999999999],[5,9,17,999999999999],[6,7,8,999999999999],[6,8,12,999999999999],[6,12,17,999999999999],[6,14,29,999999999999],[6,17,29,999999999999],[8,12,17,999999999999],[9,11,17,999999999999],[10,11,17,999999999999],[10,15,17,999999999999],[13,17,23,999999999999],[13,23,26,999999999999],[14,18,19,83029695],[14,18,25,999916970304],[14,19,25,999916970304],[14,19,28,999999999999],[14,28,29,999999999999],[16,20,21,999999999999],[16,20,29,999999999999],[16,21,37,999999999999],[16,29,30,999999999999],[16,30,31,999999999999],[16,31,32,999999999999],[17,23,29,999999999999],[18,19,25,83029695],[19,25,28,999999999999],[20,21,22,26099755002],[20,21,35,973900244997],[20,22,35,26099755002],[20,28,29,999999999999],[20,28,34,882145806469],[20,28,35,117854193530],[20,34,35,882145806469],[21,22,35,973900244997],[22,35,39,999999999999],[22,38,39,999999999999],[23,26,30,999999999999],[23,29,30,999999999999],[24,25,33,999999999999],[24,25,42,999999999999],[25,28,33,999999999999],[25,40,41,999124282094],[25,40,42,999124282094],[25,41,42,875717905],[26,27,30,999999999999],[28,33,34,999999999999],[28,34,35,117854193530],[33,34,39,999999999999],[33,36,39,999999999999],[34,35,39,999999999999],[40,41,42,999124282094]],"representation":"Exact aggregation of positive fan mixture; weighted oriented closed cone cycle of degree one. Same t and balanced-w models as the original fan checkpoint."}
```
