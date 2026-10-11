# material-5d7e4b91009d

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# J131 Recovery capsule part 2 of 3

Mandatory exact dependency: part1, material [internal-source-reference]. Its one explicitly labelled textual correction in parallel131.py must be applied to reproduce the original source identity. The complete UNPACK131.py below performs that exact correction and checks all six original source/data identities. Part3 is optional for exact reconstruction and contains the complete numerical producer methods. The three frozen rational bodies are NOT own110.

Save UNPACK131.py from its block below, then run it on the readable material files (their local names may differ):
```sh
python UNPACK131.py PART1.md PART2.md PART3.md
# PART3.md may be omitted for exact reconstruction.
OPENBLAS_NUM_THREADS=1 python cert131.py
OPENBLAS_NUM_THREADS=1 python atlas131.py
```

The generator below reconstructs the complete original FROZEN131.json, 4448B/SHA256 26df06fb91835f2d8ee16413550065f4721791be02e2609e2ee9ee2967237bed. Each44-entry list is the recorded free-height checkpoint at denominator10^12, not a shortened coordinate array. The pivot heights are determined by exact RREF of the full parent mass coefficients. Therefore optimizer replay is not needed to reproduce the objects. The numerical producer's rule was ties-even round(binary64 t_i*10^12), followed by exact projection and exact retraction. Do not independently reround the recovered rational vertices.

Original source identities:
- cert131.py 7182B / 57be5f88b3620dec2d5edb8f86f885fc3c9d946eb6574b90712acb1089a068bc
- atlas131.py 2814B / ef08841bdfd43daa42c53d14480a7a57d48b7fd33004e403530a4f4467e1ba70
- FROZEN131.json 4448B / 26df06fb91835f2d8ee16413550065f4721791be02e2609e2ee9ee2967237bed

Observed terminal markers and complete reproduced-output identities:
- J131_PARALLEL_EXACT_PASS: J131_EXACT_REPORT.json 11391B / 51cc99d6087b04ea6a523068b1ac5e36c472b9d21ce189843f459e3955b3b803
- J131_FOUR_CHART_LOCAL_RANK_137_PASS: J131_ATLAS_RANK.json 2724B / 2a7a3903ab58d7ad90333f9fea8ec43bb39d096afd6d2a33deb5fdd019b5a8f4
- J131_PARALLEL_100.json 526451B / e0c55b4f9823fed173fd59d71e73c60a925c94cc2475ad9bda2868e8e4ef43dd
- J131_PARALLEL_010.json 538796B / fd82b52fbffd18a9bbfeb1bb5285f35007b2662374aab431f46c669911ed4339
- J131_PARALLEL_001.json 44577B / 436c37180957dfb5ddb321043f76061eac2ad53b93a1f6bf7206d8471629664c

Every body is47/135/90,C270,exact own211/additionalweak000/endpointprimitive000,P[],oneQ,with EXACT original V,M,g and the same strict triangular lattice. Q intervals, divided by10^15, are (446793221594605,446793221594606), (438150109628924,438150109628925), and (440780104846534,440780104846535). Point numerator/denominator maxima are324/325,338/339,334/335bits. The first two ENTIRE quadratic point paths are certified own211/weak000 by3960 affine support comparisons and146 cubic S/U guard families with exact finite witness-union Bernstein covers, maximum subdivision depth2. No all-parameter primitive000 claim.

The third path is NOT own211 throughout: its exact midpoint is own222/weak000/primitive000,U=[4,6],with oneP in (43280723978,43280723979)/10^18 and oneQ in (451832280373303670,451832280373303671)/10^18,still identical V,M,g/lattice. This retained counterexample rules out inferring path safety from exact mass and safe endpoints.

## File: MAKE_FROZEN131.py
```python
#!/usr/bin/env python3
from pathlib import Path
import hashlib,json
ROWS=[
[-2090257687,10162417814,-6656765558,-4511251688,233606973,-3391590434,363142886,-539067128,-870915852,-223366727,-347602927,-15884296,-135165244,-69547428,136589924,2875541774,242860987,67223051,29165763,102709042,169755502,206494318,391211892,309212427,251920763,-2445856107,11090144394,-34100598186,23798377744,-29573195589,35156978398,-12731288834,-10754847178,21150442156,12909959972,-7225795829,-17289057553,876548368,18063020452,17597881651,17629732829,-10726027539,-9740672570,-14609043414],
[-2687101791,-4434086811,-22574987,2469205123,9104478038,9050455306,-26752604338,-27088284043,-26043834191,-22454966003,-22805418593,-12472749978,-10156122355,-7521111335,9100302415,-12048940522,-16075222792,7395948068,-8794489679,8685439039,9248683709,9425937823,9293464558,9287950824,9335828863,8566291293,-6212554182,13099486878,23495946226,14797377927,-33318690436,8945620933,-23702005521,44760009169,-21285015367,31846760960,5803847721,9627334284,13353828128,-5243669384,15611582835,4696195288,16355524610,3780680952],
[34582673925,14863083996,11993135595,18112259399,-7588008121,-7605415720,287543227,416748322,345122826,620293462,507234368,-540676162,-541303765,-539260989,-2120913070,200818867,240999843,-579435974,-549562346,-665931479,-176852299,-328760034,-453343458,-430087074,-392427034,-422739105,9481383762,-4395916922,-15586194348,-5689337814,-21888625611,-51213874336,-5659954038,-827478363,-8383475703,2743993222,-1790659560,-1552247622,-10401020464,6771468736,17328689168,-1330830526,15218421668,17555225476]
]
DIRECTIONS=[[1,0,0],[0,1,0],[0,0,1]]
assert len(ROWS)==3 and all(len(row)==44 for row in ROWS)
data=[dict(name='J131_PARALLEL_'+''.join(map(str,v)),v=v,pivot_columns=[0,1,2],free_columns=list(range(3,47)),denominator=10**12,free_numerators=row)for v,row in zip(DIRECTIONS,ROWS)]
b=(json.dumps(data,indent=2)+'\n').encode()
assert len(b)==4448 and hashlib.sha256(b).hexdigest()=='26df06fb91835f2d8ee16413550065f4721791be02e2609e2ee9ee2967237bed'
Path(__file__).with_name('FROZEN131.json').write_bytes(b)
print('J131_LITERAL_FROZEN_HEIGHTS_PASS',len(b),hashlib.sha256(b).hexdigest())
```

## File: cert131.py
```python
#!/usr/bin/env python3
"""Exact reconstruction and entire polynomial-path certificate for J131.
Every input height is a literal rational in FROZEN131.json. Exact projection
fixes V and transverse moments; a common quadratic translation restores the
remaining actual centroid component. No optimizer is needed for this replay.
"""
from fractions import Fraction as F
from math import comb
import json
import engine131 as e,parallel131 as p
O=F(0)
def coefficients(v):
 c0=v[0];c3=F(9,2)*(v[3]-3*v[2]+3*v[1]-v[0]);c2=F(9,2)*(v[2]-2*v[1]+v[0])-c3;c1=3*(v[1]-v[0])-c2/3-c3/9
 return [c0,c1,c2,c3]
def bernstein(c):return [sum((c[j]*F(comb(k,j),comb(3,j))for j in range(k+1)),O)for k in range(4)]
def positive(b,depth=0):
 if min(b)>0:return (depth,min(b))
 assert b[0]>0 and b[-1]>0,('Path guard fails at subdivision endpoint',depth)
 assert depth<40,('Unresolved path guard',b)
 rows=[b]
 while len(rows[-1])>1:rows.append([(a+c)/2 for a,c in zip(rows[-1],rows[-1][1:])])
 left=[r[0]for r in rows];right=[r[-1]for r in rows[::-1]]
 l=positive(left,depth+1);r=positive(right,depth+1);return max(l[0],r[0]),min(l[1],r[1])
def path_certificate(X,fs,v,t,g):
 A,ell,B,vr,L=p.exact_coefficients(X,fs,v);V,M,_=e.mass(X,fs)
 assert all(e.dot(a,t)==0 for a in A)
 q1=e.dot(ell,t)/V;q2=sum((t[i]*e.dot(B[i],t)for i in range(len(t))),O)/V
 points=[]
 for s in [O,F(1,3),F(2,3),F(1)]:
  Y=[e.sub(e.add(x,e.mul(s*z-s*q1-s*s*q2,v)),g)for x,z in zip(X,t)];points.append(Y)
  vv,mm,gg=e.mass(Y,fs);assert vv==V and mm==(O,O,O)and gg==(O,O,O)
 # R(s*t) is a quadratic point path. Its hull gaps are affine, since the
 # quadratic point term is a COMMON translation and all other motions parallel.
 hull_min=None;hull_count=0
 for face in fs:
  for j in range(len(X)):
   if j in face:continue
   ends=[]
   for Y in [points[0],points[-1]]:
    a,b,c=[Y[i]for i in face];gap=-e.dot(e.cross(e.sub(b,a),e.sub(c,a)),e.sub(Y[j],a));assert gap>0;ends.append(gap)
   margin=min(ends);hull_min=margin if hull_min is None else min(hull_min,margin);hull_count+=1
 edges=sorted({tuple(sorted((f[k],f[(k+1)%3])))for f in fs for k in range(3)})
 nb=[[]for _ in X]
 for i,j in edges:nb[i].append(j);nb[j].append(i)
 certs=[];roots=[];stable=[]
 def check(kind,identity,vals):
  cc=coefficients(vals);bb=bernstein(cc);depth,margin=positive(bb)
  certs.append(dict(kind=kind,identity=identity,power=cc,bernstein=bb,max_subdivision=depth,positive_lower_bound=margin))
 def cover(kind,identity,rows):
  # The union of positive witnesses need not have one globally valid member.
  # Cover the full parameter interval by exact dyadic Bernstein tests.
  bs=[bernstein(coefficients(row))for row in rows]
  leaves=[]
  def split(bb):
   levels=[bb]
   while len(levels[-1])>1:levels.append([(a+b)/2 for a,b in zip(levels[-1],levels[-1][1:])])
   return [r[0]for r in levels],[r[-1]for r in levels[::-1]]
  def rec(arr,a,b,depth):
   valid=[(min(bb),j)for j,bb in enumerate(arr)if min(bb)>0]
   if valid:
    margin,j=max(valid);leaves.append(dict(interval=(a,b),witness=j,lower=margin));return
   assert max(bb[0]for bb in arr)>0 and max(bb[-1]for bb in arr)>0,('No strict escape at a dyadic endpoint',kind,identity,a,b)
   assert depth<40,('Unresolved union of witnesses',kind,identity)
   halves=[split(bb)for bb in arr];m=(a+b)/2
   rec([h[0]for h in halves],a,m,depth+1);rec([h[1]for h in halves],m,b,depth+1)
  rec(bs,O,F(1),0)
  certs.append(dict(kind=kind,identity=identity,witness_powers=[coefficients(row)for row in rows],cover=leaves,max_subdivision=max((x['interval'][1]-x['interval'][0]).denominator.bit_length()-1 for x in leaves)))
 for i in range(len(X)):
  vals={j:[e.dot(Y[i],e.sub(Y[j],Y[i]))for Y in points]for j in nb[i]}
  best=max(nb[i],key=lambda j:vals[j][0])
  if vals[best][0]<0:
   roots.append(i)
   for j in nb[i]:check('U_root',(i,j),[-a for a in vals[j]])
  else:cover('U_escape',(i,nb[i]),[vals[j]for j in nb[i]])
 for fi,face in enumerate(fs):
  vals=[]
  for k in range(3):
   row=[]
   for Y in points:
    a,b,c=[Y[i]for i in face];n=e.cross(e.sub(b,a),e.sub(c,a));row.append(e.dot(n,e.cross(Y[face[k]],Y[face[(k+1)%3]])))
   vals.append(row)
  edge=min(range(3),key=lambda k:vals[k][0])
  if vals[edge][0]>0:
   stable.append(face)
   for k in range(3):check('S_root',(fi,k),vals[k])
  else:cover('S_escape',fi,[[-a for a in row]for row in vals])
 assert len(roots)==1 and len(stable)==2
 return dict(path='p_i(s)=p_i+[s*t_i-s*q1-s^2*q2]*v, 0<=s<=1',q1=q1,q2=q2,hull_comparisons=hull_count,hull_min_raw_margin=hull_min,strict=[2,1,1],additionalweak=[0,0,0],U=roots,S=stable,guard_count=len(certs),max_subdivision=max(c['max_subdivision']for c in certs),guards=certs,scope='Fixed strict triangular lattice; exact V,M,g and cubic equilibrium guards on the ENTIRE path. No claim of primitive-zero-free every intermediate point.')

def main():
 X=e.load();base,fs=e.audit(X);data=json.loads((e.R/'FROZEN131.json').read_text());outputs=[];reports=[]
 for item in data:
  v=tuple(F(z)for z in item['v']);A,ell,B,vr,L=p.exact_coefficients(X,fs,v);rr,piv=e.rref(A);free=[j for j in range(len(X))if j not in piv]
  assert len(piv)==3 and piv==item['pivot_columns'] and free==item['free_columns']
  t=e.lift_free(rr,piv,free,[F(n,item['denominator'])for n in item['free_numerators']])
  # Structural exact identities: every common translation lies in the slice;
  # B*1 = V_gradient/2 and ell.1=V make the retraction global, not local.
  ones=[F(1)]*len(X);assert all(e.dot(a,ones)==0 for a in A);assert e.dot(ell,ones)==base['volume']
  assert all(e.dot(r,ones)==vr[i]/2 for i,r in enumerate(B))
  Y,shift,tt=p.retract(X,fs,v,t);audit,ys=e.audit(Y)
  assert ys==fs and audit['strict']==[2,1,1]and audit['weak']==[0,0,0]and audit['primitive_zero']==[0,0,0]
  assert all(audit[k]==base[k]for k in ['volume','moment','centroid'])
  if item['v']==[0,0,1]:
   midpoint,_,_=p.retract(X,fs,v,[a/2 for a in t]);mid,ms=e.audit(midpoint)
   assert ms==fs and mid['strict']==[2,2,2]and mid['weak']==[0,0,0]and mid['primitive_zero']==[0,0,0]
   assert mid['U']==[4,6]and len(mid['P'])==len(mid['Q'])==1
   cert=dict(scope='No whole-path211 claim: exact midpoint is own222.',midpoint_vertices=midpoint,midpoint_audit=mid,guard_count=0,max_subdivision=0)
  else:cert=path_certificate(X,fs,v,t,base['centroid'])
  bits=[max(a.numerator.bit_length()for y in Y for a in y),max(a.denominator.bit_length()for y in Y for a in y)]
  rec=e.write(item['name']+'.json',dict(vertices=Y,audit=audit,t=t,corrected_heights=tt,translation=shift,coefficient_rank=3,point_fraction_bits=bits,path_certificate=cert));outputs.append(rec)
  reports.append(dict(name=item['name'],audit=audit,point_fraction_bits=bits,guard_count=cert['guard_count'],max_subdivision=cert['max_subdivision'],output=rec))
  print('J131_EXACT_BODY',item['name'],audit['strict'],[float(q['depth'])for q in audit['Q']],bits,'PATH',cert['guard_count'],cert['max_subdivision'],flush=True)
 rec=e.write('J131_EXACT_REPORT.json',dict(parent=base,bodies=reports,outputs=outputs,evidence='One exact Fraction implementation; Qhull only nominates triangles. No target110 obtained.'))
 print('J131_PARALLEL_EXACT_PASS',rec,flush=True)
if __name__=='__main__':main()
```

## File: atlas131.py
```python
#!/usr/bin/env python3
"""Exact local completeness test for four mass-preserving parallel charts.
At DETACHED47 the mass fibre has dimension 3*47-4=137. Three coordinate
parallel kernels contribute 3*(47-4)=129 directions. Eight (1,1,1)-parallel
kernel directions supply the missing quotient. This is local rank, NOT
finite equilibrium cancellation or proof of global reachability.
"""
from fractions import Fraction as F
import engine131 as e,parallel131 as p
O=F(0)
def determinant(A):
 a=[r[:]for r in A];out=F(1)
 for j in range(len(a)):
  k=next((k for k in range(j,len(a))if a[k][j]),None)
  if k is None:return O
  if k!=j:a[k],a[j]=a[j],a[k];out=-out
  pivot=a[j][j];out*=pivot
  for k in range(j+1,len(a)):
   z=a[k][j]/pivot
   for h in range(j+1,len(a)):a[k][h]-=z*a[j][h]
 return out

def main():
 X=e.load();fs=e.hull(X)[0];N=len(X);G=[];axis=[]
 for v in [(1,0,0),(0,1,0),(0,0,1)]:
  _,_,_,vr,L=p.exact_coefficients(X,fs,tuple(map(F,v)));mat=[vr]+L;rr,piv=e.rref(mat);assert len(piv)==4
  axis.append(dict(direction=v,rank=4,pivot_columns=piv,nonzero_minor=determinant([[row[j]for j in piv]for row in mat])))
  G.append(mat)
 C=[[G[a][k][i]for a in range(3)for k in range(4)]for i in range(N)]
 rr,piv=e.rref(C);assert len(piv)==12
 rr,rowids=e.rref([list(a)for a in zip(*C)]);minor=determinant([C[i]for i in rowids]);assert minor
 diag=[[sum(G[a][k][i]for a in range(3))for i in range(N)]for k in range(4)]
 rr,piv=e.rref(diag);assert len(piv)==4;free=[i for i in range(N)if i not in piv]
 K=[e.lift_free(rr,piv,free,[F(int(j==k))for j in range(len(free))])for k in range(len(free))]
 H=[[e.dot(G[a][k],col)for col in K]for a in range(2)for k in range(4)]
 rr,eight=e.rref(H);assert len(eight)==8
 minor8=determinant([[row[j]for j in eight]for row in H]);assert minor8
 # Gz*K = -Gx*K-Gy*K since K lies in the diagonal's mass kernel.
 assert all(sum(e.dot(G[a][k],col)for a in range(3))==0 for col in K for k in range(4))
 out=dict(N=N,global_mass_rank=4,mass_fibre_dimension=3*N-4,axes=axis,axis_sum_dimension=3*(N-4),axis_coefficient_matrix_rank=12,rank12_rows=rowids,rank12_minor=minor,diagonal_direction=[1,1,1],diagonal_kernel_pivots=piv,diagonal_quotient_rank=8,diagonal_selected_kernel_columns=eight,diagonal_selected_free_height_indices=[free[j]for j in eight],rank8_minor=minor8,combined_rank=3*(N-4)+8,local_claim='A composition of four exact parallel mass charts contains a neighbourhood in the fixed-lattice V,M fibre by the inverse function theorem. Retain all 43 coordinates on each axis and the listed eight diagonal coordinates. No global capacity or equilibrium-class claim.')
 rec=e.write('J131_ATLAS_RANK.json',out);print('J131_FOUR_CHART_LOCAL_RANK_137_PASS',rec,flush=True)
 print('Eight diagonal free heights',[free[j]for j in eight],flush=True)
if __name__=='__main__':main()
```

## File: UNPACK131.py
```python
#!/usr/bin/env python3
"""Extract the readable J131 source blocks; refuse identity mismatches."""
import hashlib,re,runpy,sys
from pathlib import Path
root=Path(__file__).resolve().parent
expected={
'DETACHED_G6.txt':(1034,'a5b7cb7cd10de4a8ba08a997945ee3a932385cf03a5e259946be867954772a50'),
'engine131.py':(5318,'57c193dfbdc155935de187e4c6b01f0115bd1dba1c65d89b383076abd0c7f63a'),
'parallel131.py':(5151,'c57594109a3b9a91cc4f90f2404bf4b7b59b65893c01e923abedd1310d4e4057'),
'cert131.py':(7182,'57be5f88b3620dec2d5edb8f86f885fc3c9d946eb6574b90712acb1089a068bc'),
'atlas131.py':(2814,'ef08841bdfd43daa42c53d14480a7a57d48b7fd33004e403530a4f4467e1ba70'),
'FROZEN131.json':(4448,'26df06fb91835f2d8ee16413550065f4721791be02e2609e2ee9ee2967237bed')}
assert len(sys.argv)>=3,'Supply the part1 and part2 Markdown filenames; part3 is optional.'
for source in sys.argv[1:]:
 text=Path(source).read_text(encoding='utf-8')
 for name,code in re.findall(r'^## File: ([A-Za-z0-9_.]+)\n```[^\n]*\n(.*?)^```\s*$',text,re.M|re.S):
  assert Path(name).name==name and name not in ('.','..')
  if name=='parallel131.py':
   code=code.replace('  U=np.zeros((N,N));dU=np.zeros((N,N,N,self.d)) if False else np.zeros((N,N,self.d))\n','  U=np.zeros((N,N));dU=np.zeros((N,N,self.d))\n')
  b=code.encode('utf-8')
  if name in expected:assert (len(b),hashlib.sha256(b).hexdigest())==expected[name],name
  dest=root/name
  if dest.exists()and dest.read_bytes()!=b:raise FileExistsError(str(dest))
  dest.write_bytes(b)
runpy.run_path(str(root/'MAKE_FROZEN131.py'),run_name='__main__')
for name,identity in expected.items():
 b=(root/name).read_bytes();assert (len(b),hashlib.sha256(b).hexdigest())==identity,name
print('J131_SIX_EXACT_SOURCE_IDENTITIES_PASS')
```
