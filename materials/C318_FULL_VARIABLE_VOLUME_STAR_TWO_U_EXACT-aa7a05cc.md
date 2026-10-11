# material-aa7a05cc53b0

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# C318 full variable-volume star17 replacement cell: exact two-U exclusion

Object identity: the V55/E159/F106 C318 input of [internal-source-reference], not the unrelated C318_PROTECTED15 body. This source is self-contained and does not use a worker result as an unstated dependency.

THEOREM. Keep the other 54 input vertices fixed and let input vertex 17 move in the complete closed convex-realization cell that retains the supplied oriented triangle fan and all other supplied supporting triangles. Volume is NOT held fixed. At the actual filled-volume centroid c(v), both input vertices 0 and 17 satisfy (p_i-c(v)).(p_j-p_i)<-1/100 for every other input point j. They therefore remain two distinct strict unstable vertices, even on cell-boundary limiting bodies. This excludes own110 throughout this entire one-vertex chamber, not arbitrary changed incidences or coupled moves.

The chamber has 498 distinct exact defining inequalities, six irredundant facets, eight rational vertices. The certificate reconstructs these eight vertices from six proposed planes, checks every original inequality at all vertices, independently enumerates every hull facet of the eight points and matches it to original inequalities. These two inclusions prove equality with the full chamber, not merely an inscribed sampled region. Original geometry is checked as an exact strictly simplicial closed oriented convex surface.

Let D(v)=6 volume=d0+g.v and N(v)=4D(v)c(v)=n0+Bv+(g.v)v, obtained by expanding the complete oriented boundary integrals. D is positive on the whole chamber by its exact vertex minimum. Polarize the quadratic numerator to obtain symmetric bilinear A(u,w) for 4D(v)v-N(v) and C(u,w) for 4D(v)p0-N(v). Each shifted U inequality is a cubic or quadratic polynomial after multiplying by positive 4D. All its Bernstein coefficients on the simplex of the eight chamber vertices are strictly negative. The source checks all 54 inequalities for each of the two U vertices, not a selected witness pool. Convex-combination weights over all eight vertices suffice; no tetrahedralization or floating optimization is used by the final proof.

Reconstruction: write the two file blocks below exactly. input.json has no final newline; full_star_exact.py has one final newline. Check input/source hashes. Run `python full_star_exact.py` using Python 3.11.8 standard library only. Run `sha256sum input.json full_star_exact.py full_cell_proof.json` to verify the exact recovered input and output. The construction/proof uses no random seed and no omitted parameters.

Expected terminal marker: `C318_VARIABLE_VOLUME_FULL_STAR_TWO_U_PASS 8 6 54 54`.
Expected reported largest shifted numerator coefficients (display floats only; exact fractions in output): -0.23614915444819784 and -0.31204088427191473.
Input input.json: 1958 bytes, SHA256 5cd9cf50c8574da530c02d1b13d24840c0a9d15562fc8c3fe92e32b2eaebf90b.
Source full_star_exact.py: SHA256 33e8175d2a468ddb6254d7c4a82e730b38cc7678812fae3bafc48c6af1815879.
Output full_cell_proof.json: 19923 bytes, SHA256 d30678ad689ba64e372ca57fc231ac0536bb7342f2cbec75da8e6f675d2a1bc8.
The exact D range in output is [23966329665576347862806251/2368041867034199000000000,8069446958486899/794186500000000].

## File input.json
```json
{"P1000":[[-681,-206,-1391],[-679,-107,-1396],[-629,-369,-1329],[-617,53,-1375],[-609,92,-1348],[-555,142,-1297],[-428,-626,-982],[-342,333,-1068],[-321,338,1121],[-315,217,1142],[-304,375,-893],[-294,463,1098],[-271,-686,-813],[-239,349,-994],[-218,601,1066],[-188,-34,1135],[-186,-86,1099],[-114,734,1026],[-91,-280,847],[-79,418,-737],[-61,755,986],[-36,517,-404],[-24,657,238],[35,620,-19],[84,-732,-513],[106,708,953],[149,586,-141],[152,-212,955],[146,-111,1077],[234,-715,-454],[267,564,-130],[273,276,-551],[305,-15,1032],[320,-521,5],[438,248,-394],[459,590,333],[459,-379,178],[487,-524,-407],[476,172,-398],[479,338,-279],[499,377,-222],[515,541,29],[519,75,-403],[527,412,-155],[540,-23,-412],[560,-140,-388],[561,463,-57],[609,306,-71],[612,271,-81],[614,92,-155],[618,154,-121],[636,123,260],[642,-336,-135],[660,-55,333],[671,-212,37]],"T":[[0,1,3],[0,8,1],[0,3,2],[0,2,9],[0,9,8],[1,4,3],[1,11,4],[1,8,11],[2,3,37],[2,6,16],[2,29,6],[2,16,9],[2,37,29],[3,4,5],[3,5,13],[3,13,44],[3,45,37],[3,44,45],[4,17,5],[4,11,14],[4,14,17],[5,7,13],[5,17,7],[6,12,18],[6,29,12],[6,18,16],[7,20,10],[7,10,22],[7,19,13],[7,17,20],[7,26,19],[7,23,21],[7,21,26],[7,22,23],[8,9,11],[9,14,11],[9,17,14],[9,16,15],[9,15,28],[9,32,17],[9,28,32],[10,20,22],[12,24,18],[12,29,24],[13,19,46],[13,40,31],[13,31,42],[13,43,40],[13,42,44],[13,46,43],[15,16,28],[16,18,27],[16,27,28],[17,25,20],[17,32,25],[18,24,29],[18,29,27],[19,26,30],[19,30,41],[19,41,46],[20,23,22],[20,35,23],[20,25,35],[21,23,26],[23,35,26],[25,32,35],[26,41,30],[26,35,41],[27,32,28],[27,29,33],[27,36,32],[27,33,36],[29,36,33],[29,37,36],[31,34,38],[31,39,34],[31,38,42],[31,40,39],[32,53,35],[32,36,53],[34,39,38],[35,46,41],[35,51,46],[35,53,51],[36,37,52],[36,52,54],[36,54,53],[37,45,52],[38,39,42],[39,40,42],[40,43,42],[42,43,46],[42,47,44],[42,46,47],[44,49,45],[44,47,48],[44,48,50],[44,50,49],[45,49,52],[46,51,47],[47,54,48],[47,51,53],[47,53,54],[48,54,50],[49,50,52],[50,54,52]]}
```

## File full_star_exact.py
```python
"""Exact Bernstein certificate over the FULL variable-volume star replacement cell.
No stochastic search, no fixed-centre approximation, no claim beyond this cell.
"""
import itertools,json,math,pathlib,sys
from fractions import Fraction as F
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def primitive(a):
 l=math.lcm(*(q.denominator for q in a));v=[int(q*l) for q in a];g=math.gcd(*v)
 return tuple(k//g for k in v) if g else None

def inequalities(P,T,k):
 rows=set()
 for tri in T:
  if k not in tri:
   a,b,c=[P[i] for i in tri];n=cross(sub(b,a),sub(c,a));row=primitive((*n,-dot(n,a)))
   if row:rows.add(row)
  else:
   t=list(tri);r=t.index(k);i,j=t[(r+1)%3],t[(r+2)%3];a,b=P[i],P[j]
   # det(a-v,b-v,p-v)=det(a,b,p)-v.(b x p+p x a+a x b) <=0
   for q,p in enumerate(P):
    if q in tri:continue
    n=tuple(-x-y-z for x,y,z in zip(cross(b,p),cross(p,a),cross(a,b)))
    row=primitive((*n,det(a,b,p)))
    if row:rows.add(row)
 return sorted(rows)

def filled(P,T):
 d=F(0);n=[F(0)]*3
 for i,j,k in T:
  s=det(P[i],P[j],P[k]);d+=s
  for q in range(3):n[q]+=s*(P[i][q]+P[j][q]+P[k][q])
 return d,tuple(x/(4*d) for x in n)



def scale(q,x):return tuple(q*t for t in x)
def mean(*vs):return tuple(sum(z)/len(vs) for z in zip(*vs))
def oriented_hull_rows(C):
 rows=set()
 for i,j,k in itertools.combinations(range(len(C)),3):
  n=cross(sub(C[j],C[i]),sub(C[k],C[i]))
  if not any(n):continue
  signs=[dot(n,sub(p,C[i])) for p in C]
  if all(x<=0 for x in signs):rows.add(primitive((*n,-dot(n,C[i]))))
  elif all(x>=0 for x in signs):rows.add(primitive((*scale(-1,n),dot(n,C[i]))))
 return rows

def main():
 z=json.load(open('input.json'));P=[tuple(F(x,1000) for x in p) for p in z['P1000']];T=z['T'];k=17
 candidate_H=[[-29936000,-18225000,-130292000,143318449],[-17471000,9798800,763700,-10511861],[-12418000,28877000,-4234000,-18384909],[90000,133600,789900,-902707],[25246000,91891000,-3115000,-64766309],[295676000,-373153000,36215000,264058761]]
 C=set()
 for rows in itertools.combinations(candidate_H,3):
  A=[r[:3] for r in rows];b=[-r[3] for r in rows];d=det(*A)
  if not d:continue
  v=tuple(F(det(*[tuple(b[r] if j==c else A[r][j] for j in range(3)) for r in range(3)]),d) for c in range(3))
  if all(dot(row[:3],v)+row[3]<=0 for row in candidate_H):C.add(v)
 C=sorted(C);assert len(C)==8
 raw={'corners':[[str(q) for q in p] for p in C]}
 # Validate exact source closed, oriented, strictly simplicial convex boundary.
 edges={}
 for tri in T:
  a,b,c=[P[i] for i in tri];n=cross(sub(b,a),sub(c,a));assert any(n)
  assert all(dot(n,sub(p,a))<0 for i,p in enumerate(P) if i not in tri)
  for i,j in zip(tri,tri[1:]+tri[:1]):edges.setdefault(tuple(sorted((i,j))),[]).append((i,j))
 assert len(P)==55 and len(T)==106 and len(edges)==159
 assert all(len(e)==2 and e[0]==e[1][::-1] for e in edges.values())
 assert len(P)-len(edges)+len(T)==2
 R=inequalities(P,T,k)
 assert all(dot(r[:3],p)+r[3]<=0 for r in R for p in C)
 H=oriented_hull_rows(C)
 assert H==set(tuple(r) for r in candidate_H) and H<=set(R)
 assert any(det(sub(a,C[0]),sub(b,C[0]),sub(c,C[0])) for a,b,c in itertools.combinations(C[1:],3))
 # All actual hull facets are defining constraints and all C vertices obey all
 # constraints. Thus conv(C) equals the entire closed intersection, bounded.
 d0=F(0);n0=(F(0),)*3;g=(F(0),)*3;B=[[F(0)]*3 for _ in range(3)]
 for t in T:
  if k not in t:
   a,b,c=[P[i] for i in t];d=det(a,b,c);d0+=d;n0=add(n0,scale(d,add(add(a,b),c)))
  else:
   r=t.index(k);a,b=P[t[(r+1)%3]],P[t[(r+2)%3]];n=cross(a,b);g=add(g,n)
   for i in range(3):
    for j in range(3):B[i][j]+=(a[i]+b[i])*n[j]
 def D(v):return d0+dot(g,v)
 def Nbar(u,v):
  w=mean(u,v);bv=tuple(dot(row,w) for row in B)
  quad=scale(F(1,2),add(scale(dot(g,u),v),scale(dot(g,v),u)))
  return add(add(n0,bv),quad)
 def Ab(u,v):
  return sub(scale(2,add(scale(D(u),v),scale(D(v),u))),Nbar(u,v))
 def Cb(u,v):return sub(scale(4*D(mean(u,v)),P[0]),Nbar(u,v))
 for v in [P[k]]+C+[mean(*C)]:
  PP=P.copy();PP[k]=v;dd,c=filled(PP,T)
  assert dd==D(v) and Nbar(v,v)==scale(4*dd,c)
 assert min(map(D,C))>0
 gap=F(1,100);u17=[];u0=[]
 for j in range(len(P)):
  if j==k:continue
  worst=None;wt=None
  for inds in itertools.combinations_with_replacement(range(len(C)),3):
   a,b,c=(C[i] for i in inds)
   coeff=(dot(Ab(a,b),sub(P[j],c))+dot(Ab(a,c),sub(P[j],b))+dot(Ab(b,c),sub(P[j],a)))/3
   upper=coeff+4*gap*D(mean(a,b,c))
   if worst is None or upper>worst:worst=upper;wt=inds
  assert worst<0,('U17 failed',j,str(worst),wt)
  u17.append(dict(other=j,max_shifted_bernstein=str(worst),indices=wt))
 for j in range(1,len(P)):
  degree=3 if j==k else 2;worst=None;wt=None
  for inds in itertools.combinations_with_replacement(range(len(C)),degree):
   vs=[C[i] for i in inds]
   if degree==2:coeff=dot(Cb(*vs),sub(P[j],P[0]))
   else:
    a,b,c=vs;coeff=(dot(Cb(a,b),sub(c,P[0]))+dot(Cb(a,c),sub(b,P[0]))+dot(Cb(b,c),sub(a,P[0])))/3
   upper=coeff+4*gap*D(mean(*vs))
   if worst is None or upper>worst:worst=upper;wt=inds
  assert worst<0,('U0 failed',j,str(worst),wt)
  u0.append(dict(other=j,max_shifted_bernstein=str(worst),indices=wt))
 ans=dict(theorem='For every v in the complete closed star17 convex replacement cell, actual filled-centroid dot products for vertices 0 and17 to all other input points are strictly less than -1/100.',vertices=raw['corners'],cell_halfspaces=len(R),cell_facets=len(H),cell_vertices=len(C),cell_facet_rows=[list(r) for r in sorted(H)],D_min=str(min(map(D,C))),D_max=str(max(map(D,C))),D_constant=str(d0),D_gradient=[str(q) for q in g],N_constant=[str(q) for q in n0],N_linear=[[str(q) for q in row] for row in B],gap=str(gap),U17=u17,U0=u0)
 pathlib.Path('full_cell_proof.json').write_text(json.dumps(ans,sort_keys=True,separators=(',',':')))
 print('C318_VARIABLE_VOLUME_FULL_STAR_TWO_U_PASS',len(C),len(H),len(u17),len(u0))
 print('worst adjusted numerator',max(float(F(x['max_shifted_bernstein'])) for x in u17),max(float(F(x['max_shifted_bernstein'])) for x in u0))
if __name__=='__main__':main()
```
