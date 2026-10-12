# material-a67376189f33

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J137 balanced-weight exact coalescences

These are useful method nonwinners, NOT own110 and NOT a new canonical record. Literal identities: J137_WEIGHT_HIGH_M01 and J137_WEIGHT_HIGH_M4. HIGH_M01 is the same rational geometry as the earlier sandbox label J137_WEIGHT_SNAP_2_G1000000000000_T1e-07; HIGH_M4 is the rational geometry of FAST_SNAP137_CONVEX_MASS137_HIGH_6. These equivalences were checked by identical exact t and unchanged rational LOW43 rays, not inferred from filenames.

Required complete dependencies: [internal-source-reference] supplies exact137.py; [internal-source-reference] supplies LOW43.json. This material supplies ALL additional inputs and the full standard-library recovery unit. No floating optimizer, SciPy, omitted coordinate row or sandbox file is needed for recovery.

Executed Python3.13.5 command:
```
python replay_weights137.py J137_WEIGHT_HIGH_M01_SEED.json J137_WEIGHT_HIGH_M4_SEED.json
```
Expected markers:
```
J137_WEIGHT_REPLAY_PASS J137_WEIGHT_HIGH_M01 40 105 67 [23, 7, 28] [0, 0, 0] 874aca23e91239de54a652e16f2ae22dda1f5c52383e6999901beb8b274f71d5
J137_WEIGHT_REPLAY_PASS J137_WEIGHT_HIGH_M4 32 66 36 [12, 5, 15] [0, 0, 0] 62fc04149d950898e1c5f9c4cb6beafd4deb469a7dc76dad7f791e0cdf770159
```

Exact true incidence and own-centroid classes:
- HIGH_M01: V40/E105/F67,C210,strict(23,7,28),weak000,primitive000. Six positive P and22 positive Q intervals. Earlier exact137.classify also enumerated all28 exact bar heights. The compact replay records counts, not heights; the preserved exact engine and reconstructed coordinates suffice to regenerate the full bars. Rank12 hinge equations,31 exact free reciprocal radii.
- HIGH_M4: V32/E66/F36,C132,strict(12,5,15),weak000,primitive000. Four positive P and11 positive Q intervals. Heights were NOT computed; no interval was thresholded out of the count. Rank35 hinge equations,eight exact free reciprocal radii.

Neither rational snapped body has exact g=0. Displays: HIGH_M01 g~(-1.0568309774838796e-8,-1.360606533823128e-8,3.836382620009765e-9),V~.35362156909052955; HIGH_M4 g~(-4.253841616463312e-8,-6.082571845496983e-9,1.71482357718934e-8),V~.33074795858451483. The census uses the full exact actual g, never zero or these approximations.

Recovery proof: the supplied fan is compared exactly with ALL maximal triangular facets of LOW43 and every oriented ray determinant is positive. For shared hinge f=(i,j,k), opposite l, coplanarity after x_i=R_i/t_i is
 t_l det(R_i,R_j,R_k)-t_i det(R_l,R_j,R_k)-t_j det(R_i,R_l,R_k)-t_k det(R_i,R_j,R_l)=0.
Rational RREF plus the COMPLETE supplied free values determines every t. Positive t preserves the complete radial fan. Every source triangle is checked as a supporting plane against every point; equal planes merge, full planar convex boundaries are rebuilt, and all true edges have two owners with Euler2. These supporting maximal faces form the complete hull boundary. The original radial fan supplies exact volume and moment even when its artificial diagonals cease to be true edges.

Fast exact census: every true edge has two directed physical affine-in-centre arrow numerators and two directed polar numerators. A vertex/face is strict unstable/stable when all outgoing arrows are negative; zero maxima are weak. An edge is a strict saddle exactly when all four arrows are negative: the physical pair places the foot inside the segment and the polar pair puts its radial vector inside the two-normal cone. All-nonpositive with a zero is weak. All facet offsets at exact g are positive. Small row denominators are cleared before multiplication by the large centroid numerator. There is no floating sign or weak tolerance; Euler equilibrium identity is a check, not the source of H.

Provenance: numerical convex-weight HIGH scouts at strengths-.1 and-4. Normalized hinge residuals below1e-7 were selected, free t values rounded at denominator10^12, and pivots solved exactly. This makes a new rational geometry, not an alias for a binary64 endpoint. HIGH is a26-node numerical graph superlevel component, NOT the author's36-node entire P complement. Neither path canceled the remaining basin.

File integrity:
replay_weights137.py:5216B,SHA9184c0f26b6a782e44f123f8e3ba66896ed64a12ee9719a29ed408d032062951.
J137_WEIGHT_HIGH_M01_SEED.json:2234B,SHAf81919dafcc88e6c21ed6d80970117320936c853d0f48bf3da056e8d45b32e91.
J137_WEIGHT_HIGH_M4_SEED.json:1771B,SHA6fa81508769b4863d33627ab83c630e3c554ff55cfa7e539ff65ce8b8a9be92f.
J137_WEIGHT_HIGH_M01_REPLAY.json:29473B,SHA874aca23e91239de54a652e16f2ae22dda1f5c52383e6999901beb8b274f71d5.
J137_WEIGHT_HIGH_M4_REPLAY.json:152996B,SHA62fc04149d950898e1c5f9c4cb6beafd4deb469a7dc76dad7f791e0cdf770159.

Extract each fenced file verbatim, including its final newline. A suitable re.S pattern is r'### File: ([^\n]+)\n```[^\n]*\n(.*?)```'.

### File: replay_weights137.py
```python
"""Exact compact recovery of J137 balanced-weight ray coalescences.
Standard library only. Requires exact137.py and unchanged LOW43.json.
Descriptor free values and selected hinge edges define the object exactly;
SciPy, its facet order and all floating optimizers are absent from replay.
"""
import json,sys,math,hashlib
from pathlib import Path
from fractions import Fraction as Q
from exact137 import dot,sub,mul,cross,det,hull2,mass,lattice,clean
sys.set_int_max_str_digits(0)
def rref(A,n):
 A=[[Q(x) for x in row] for row in A];piv=[];r=0
 for j in range(n):
  p=next((i for i in range(r,len(A)) if A[i][j]),None)
  if p is None:continue
  A[r],A[p]=A[p],A[r];z=A[r][j];A[r]=[v/z for v in A[r]]
  for i in range(len(A)):
   if i!=r and A[i][j]:
    z=A[i][j];A[i]=[x-z*y for x,y in zip(A[i],A[r])]
  piv.append(j);r+=1
  if r==len(A):break
 return A[:r],piv

def affine_sign(a,b,G,Gden):
 co=(*a,b);D=math.lcm(*(v.denominator if isinstance(v,Q) else 1 for v in co));z=[int(v*D) for v in co];s=dot(z[:3],G)+z[3]*Gden
 return (s>0)-(s<0)

def exact_body(R,tt,F):
 X=[mul(1/t,Ri) for Ri,t in zip(R,tt)];planes={}
 for i,j,k in F:
  dd=det(R[i],R[j],R[k]);nn=mul(1/dd,tuple(tt[i]*a+tt[j]*b+tt[k]*c for a,b,c in zip(cross(R[j],R[k]),cross(R[k],R[i]),cross(R[i],R[j]))))
  vals=[dot(nn,x) for x in X];assert max(vals)<=1,'nonconvex snap';ids=tuple(i for i,v in enumerate(vals) if v==1);planes[nn]=ids
 ordered=sorted(planes.items(),key=lambda item:item[1]);N=[n for n,ids in ordered];faces=[hull2(ids,X,n) for n,ids in ordered];EF={}
 for f,cy in enumerate(faces):
  for i,j in zip(cy,cy[1:]+cy[:1]):EF.setdefault(tuple(sorted((i,j))),[]).append(f)
 E=sorted(EF);active=sorted({i for cy in faces for i in cy});assert len(active)-len(E)+len(faces)==2 and all(len(q)==2 for q in EF.values())
 V=Q(0);M=[Q(0)]*3
 for i,j,k in F:
  d=det(R[i],R[j],R[k])/(6*tt[i]*tt[j]*tt[k]);V+=d
  for a in range(3):M[a]+=d*(X[i][a]+X[j][a]+X[k][a])/4
 g=[m/V for m in M];Gden=math.lcm(*(q.denominator for q in g));G=[int(q*Gden) for q in g]
 assert all(affine_sign(mul(-1,n),Q(1),G,Gden)>0 for n in N)
 ps={};qs={};vadj={i:[] for i in active};fadj={f:[] for f in range(len(faces))}
 for i,j in E:
  for u,v in [(i,j),(j,i)]:
   d=sub(X[v],X[u]);ps[u,v]=affine_sign(mul(-1,d),dot(X[u],d),G,Gden);vadj[u].append(v)
 for f,k in EF.values():
  for u,v in [(f,k),(k,f)]:
   a,b=N[u],N[v];aa,ab=dot(a,a),dot(a,b);row=sub(mul(aa,b),mul(ab,a));qs[u,v]=affine_sign(row,ab-aa,G,Gden);fadj[u].append(v)
 U=[i for i in active if max(ps[i,j] for j in vadj[i])<0];WU=[i for i in active if max(ps[i,j] for j in vadj[i])==0]
 S=[i for i in fadj if max(qs[i,j] for j in fadj[i])<0];WS=[i for i in fadj if max(qs[i,j] for j in fadj[i])==0]
 H=[];WH=[]
 for e in E:
  i,j=e;f,k=EF[e];s=[ps[i,j],ps[j,i],qs[f,k],qs[k,f]]
  if max(s)<0:H.append(list(e))
  elif max(s)==0:WH.append(list(e))
 if not WU and not WS and not WH:assert len(S)+len(U)-len(H)==2
 return {'V':len(active),'E':len(E),'F':len(faces),'C':2*len(E),'facets':faces,'active_vertices':active,'strict':[len(S),len(U),len(H)],'weak':[len(WS),len(WU),len(WH)],'S_carriers':[faces[f] for f in S],'U_vertices':U,'H_edges':H,'primitive_zero_physical':[list(e) for e,s in ps.items() if s==0],'primitive_zero_polar':[list(e) for e,s in qs.items() if s==0],'positive_P_count':len(U)-1,'positive_Q_count':len(S)-1,'bar_heights':'not computed; no positive count threshold','g':g,'volume':V},X


def replay(descriptor):
 seed=json.loads(Path(descriptor).read_text()); raw=Path('LOW43.json').read_bytes()
 assert hashlib.sha256(raw).hexdigest()==seed['low43_sha256']
 old=json.loads(raw);W,F0,N,H,E,EF,A=lattice(old['rows']);D=old['denominator'];vol,g=mass(W,F0,D)
 R=[sub(tuple(Q(x,D) for x in w),g) for w in W];F=seed['source_triangles']
 assert {tuple(sorted(f)) for f in F}=={tuple(sorted(f)) for f in F0}
 assert all(det(R[i],R[j],R[k])>0 for i,j,k in F)
 K=math.lcm(*(q.denominator for v in R for q in v));RI=[tuple(int(q*K) for q in v) for v in R];ef={}
 for f,cy in enumerate(F):
  for i,j in zip(cy,cy[1:]+cy[:1]):ef.setdefault(tuple(sorted((i,j))),[]).append(f)
 rows=[]
 for e in seed['selected_edges']:
  fs=ef[tuple(e)];assert len(fs)==2;f,ff=fs;i,j,k=F[f];l=next(v for v in F[ff] if v not in F[f]);a=[0]*len(R)
  a[l]=det(RI[i],RI[j],RI[k]);a[i]-=det(RI[l],RI[j],RI[k]);a[j]-=det(RI[i],RI[l],RI[k]);a[k]-=det(RI[i],RI[j],RI[l]);gg=math.gcd(*a);rows.append([v//gg for v in a])
 B,piv=rref(rows,len(R));free=[i for i in range(len(R)) if i not in piv];tt=[Q(0)]*len(R)
 assert set(map(int,seed['free_values']))==set(free)
 for i in free:tt[i]=Q(seed['free_values'][str(i)])
 for row,p in zip(B,piv):tt[p]=-sum(row[j]*tt[j] for j in free)
 assert min(tt)>0 and len(piv)==seed['rank']
 out,X=exact_body(R,tt,F);out.update({'name':seed['name'],'rank':len(piv),'t_exact':[str(q) for q in tt]})
 for k,v in seed['expected'].items():assert out[k]==v,(k,out[k],v)
 text=json.dumps(clean(out),indent=2)+'\n';target=Path(seed['name']+'_REPLAY.json');target.write_text(text)
 print('J137_WEIGHT_REPLAY_PASS',seed['name'],out['V'],out['E'],out['F'],out['strict'],out['weak'],hashlib.sha256(text.encode()).hexdigest(),flush=True)
 return out,X
if __name__=='__main__':
 for fn in sys.argv[1:]:replay(fn)
```

### File: J137_WEIGHT_HIGH_M01_SEED.json
```json
{"name":"J137_WEIGHT_HIGH_M01","low43_sha256":"c9cfe9c62a5835f6aecbbb77513ab9727a6a2a08f34429d22e0873d76f9dc6f6","source_triangles":[[29,17,6],[29,16,30],[21,22,0],[32,16,0],[13,0,17],[13,26,0],[27,30,0],[27,0,26],[27,26,30],[23,30,26],[23,17,29],[23,29,30],[23,13,17],[23,26,13],[38,0,22],[38,39,0],[38,22,39],[36,33,0],[36,0,39],[36,39,33],[18,0,25],[18,3,0],[24,0,33],[24,33,25],[28,25,33],[28,19,25],[15,17,0],[15,0,10],[15,10,17],[11,9,17],[11,17,10],[11,0,9],[11,10,0],[1,6,3],[1,4,6],[1,3,18],[1,18,4],[5,17,9],[5,8,17],[5,9,0],[5,0,8],[12,6,17],[12,17,8],[12,8,6],[2,0,3],[7,3,6],[7,6,8],[7,2,3],[7,8,0],[7,0,2],[37,0,16],[37,21,0],[37,16,21],[34,33,39],[34,28,33],[31,30,16],[31,16,32],[31,0,30],[31,32,0],[14,4,18],[14,6,4],[14,25,19],[14,18,25],[14,29,6],[14,19,28],[14,28,29],[20,16,29],[20,21,16],[20,29,28],[20,28,34],[35,39,22],[35,34,39],[35,20,34],[35,22,21],[35,21,20],[41,25,0],[41,40,25],[42,24,25],[42,25,40],[42,0,24],[42,41,0],[42,40,41]],"selected_edges":[[0,17],[0,26],[33,39],[0,25],[3,18],[0,11],[6,8],[0,7],[14,25],[25,41],[0,41],[40,41],[25,40],[24,42],[25,42],[40,42],[0,42],[41,42]],"free_values":{"3":"523848879523/500000000000","4":"514468526051/500000000000","5":"983962172177/1000000000000","7":"244157097237/250000000000","8":"24705881697/25000000000","10":"9784541181/10000000000","11":"985433119839/1000000000000","12":"98784313987/100000000000","16":"1001138502809/1000000000000","17":"1013961883253/1000000000000","19":"253551356191/250000000000","20":"10035474629/10000000000","21":"1000669629813/1000000000000","22":"125057399519/125000000000","23":"505440055771/500000000000","26":"1011566010763/1000000000000","27":"201432342131/200000000000","28":"495931513913/500000000000","29":"505210670141/500000000000","30":"1003291463331/1000000000000","31":"1004730528447/1000000000000","32":"501854668113/500000000000","34":"250224018923/250000000000","35":"250249902943/250000000000","36":"15579823341/15625000000","37":"200400115163/200000000000","38":"199952835101/200000000000","39":"998988745653/1000000000000","40":"497060479729/500000000000","41":"996211491791/1000000000000","42":"490097417357/500000000000"},"rank":12,"expected":{"V":40,"E":105,"F":67,"strict":[23,7,28],"weak":[0,0,0]}}
```

### File: J137_WEIGHT_HIGH_M4_SEED.json
```json
{"name":"J137_WEIGHT_HIGH_M4","low43_sha256":"c9cfe9c62a5835f6aecbbb77513ab9727a6a2a08f34429d22e0873d76f9dc6f6","source_triangles":[[29,17,6],[29,16,30],[21,22,0],[32,16,0],[13,0,17],[13,26,0],[27,30,0],[27,0,26],[27,26,30],[23,30,26],[23,17,29],[23,29,30],[23,13,17],[23,26,13],[38,0,22],[38,39,0],[38,22,39],[36,33,0],[36,0,39],[36,39,33],[18,0,25],[18,3,0],[24,0,33],[24,33,25],[28,25,33],[28,19,25],[15,17,0],[15,0,10],[15,10,17],[11,9,17],[11,17,10],[11,0,9],[11,10,0],[1,6,3],[1,4,6],[1,3,18],[1,18,4],[5,17,9],[5,8,17],[5,9,0],[5,0,8],[12,6,17],[12,17,8],[12,8,6],[2,0,3],[7,3,6],[7,6,8],[7,2,3],[7,8,0],[7,0,2],[37,0,16],[37,21,0],[37,16,21],[34,33,39],[34,28,33],[31,30,16],[31,16,32],[31,0,30],[31,32,0],[14,4,18],[14,6,4],[14,25,19],[14,18,25],[14,29,6],[14,19,28],[14,28,29],[20,16,29],[20,21,16],[20,29,28],[20,28,34],[35,39,22],[35,34,39],[35,20,34],[35,22,21],[35,21,20],[41,25,0],[41,40,25],[42,24,25],[42,25,40],[42,0,24],[42,41,0],[42,40,41]],"selected_edges":[[0,21],[16,32],[0,32],[0,17],[0,26],[27,30],[0,30],[0,27],[26,27],[23,29],[22,39],[33,36],[0,33],[0,36],[36,39],[0,25],[3,18],[28,33],[19,28],[19,25],[15,17],[0,15],[10,15],[0,11],[3,6],[1,18],[4,18],[5,17],[8,17],[0,2],[2,3],[2,7],[0,7],[16,21],[34,39],[30,31],[16,31],[31,32],[0,31],[14,19],[14,29],[14,28],[20,28],[35,39],[22,35],[34,35],[20,35],[21,35],[25,41],[0,41],[40,41],[25,40],[24,42],[25,42],[40,42],[0,42],[41,42]],"free_values":{"12":"128018454237/125000000000","23":"1010032056201/1000000000000","32":"1233050610749/1000000000000","38":"116376964477/100000000000","39":"1137671080253/1000000000000","40":"34314322559/40000000000","41":"434454149203/500000000000","42":"866342513311/1000000000000"},"rank":35,"expected":{"V":32,"E":66,"F":36,"strict":[12,5,15],"weak":[0,0,0]}}
```
