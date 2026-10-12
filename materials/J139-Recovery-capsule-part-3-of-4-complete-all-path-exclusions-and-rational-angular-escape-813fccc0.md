# material-813fccc03b12

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J139 recovery capsule, part 3/4

Proofs, interpretation and scope: part1 [internal-source-reference]. The complete code below additionally needs ONLY unchanged J137 exact137.py from [internal-source-reference] and LOW43.json from [internal-source-reference]. Both full exact materials must be supplied to a fresh computational successor. Part2's optimizer models are NOT required by these exclusions. All rational ray directions use LOW43's EXACT original uniform centroid as origin.

This is an exact finite-ray obstruction and an outer-envelope escape witness, NOT an own110 or even an ownU1 construction. Ten initial roots are excluded by exact outer supporting planes; a ninth-round reflection propagation excludes root5, so eleven roots are excluded in total. The other32 roots are not asserted feasible. Adding one rational ray makes root0's reflected point strictly interior to the new path envelope; it does not prove actual homogeneous mass closure. Arbitrary radial changes followed by recentering elsewhere change the relative rays and lie outside the fixed-origin exclusion.

Extract each file unit with regex `r'### File: ([^\n]+)\n```[^\n]*\n(.*?)```'`, re.S; write group2 verbatim UTF-8 including its terminal newline.

CPython3.13.5 standard-library commands:
```
python -B -S envelope139_exact.py
python -B -S reflection139_exact.py
python -B -S rayinsert139_exact.py
python -B -S robust139.py
```
Expected final markers:
```
J139_TEN_EXACT_FINITE_RAY_ROOT_EXCLUSIONS 10 [0, 1, 2, 3, 4, 6, 7, 8, 12, 14]
J139_ELEVENTH_EXACT_ROOT_EXCLUSION 5 rounds 9 root_bound 988248205631/1000000000000
J139_ONE_RATIONAL_RAY_OPENS_ROOT0_GATE [4, 6, 16, 20]
J139_ROOT0_OPEN_ANGULAR_EXCLUSION 1/20000 remaining_gap_gt 7/30000
```
The ray-insertion marker additionally prints four floating displays of exact positive weights; acceptance uses exact fractions and an exact nonzero determinant, not those displays.

Input/source byte/SHA-256 receipts:
- envelope139_exact.py3815B,67ad4365e83488ec7e70b97c0f05f426efa45e772173ef0c02f9323dfbf396e1
- reflection139_exact.py2953B,21714c3c6b91c3393dd8334ac0236a01b8c437aaceeaa85c71ba771c035343c0
- rayinsert139_exact.py1827B,fe0c3875839d01ae7cce795eef4ef8288825deae8b10b9e0e690e1a706efdf18
- robust139.py923B,a7604e26489fe38c982d0c3ffed862100a47c5e5e2fe89c4fa0dabf1724038cf
- ENVELOPE139_NOMINATIONS.json304B,72456df4aadc2eb4a5f78b5fb67f6e2bc4436bb65c37399bc909d54408b05f84
- RAYINSERT139_GATE_NOMINATION.json104B,a5124918cfc02b5a361ba12d10529dbba54ffff80b8e67bf49687c1bca9eebc6

Reproduced outputs:
- ENVELOPE139_EXACT_CERT.json2791020B,a9e29a9588bb6b1869a2336cc63b8fbeeeb67051adf542fa43c6ae69f4f005fe
- REFLECTION139_EXACT_CERT.json89668B,00c9c7125226043ac42cee015a9aff89f6dd0ea4069735162b8bfa984f6421e3
- RAYINSERT139_EXACT_CERT.json87813B,9c5ff7268276e67e73b50d141a7237326b483fd5a05d3c6008da74e6477e73f4
- ROBUST139_EXACT_CERT.json7152B,e21a9822aba33e65bdfbff7af97b8c772a0acf2207af1c5b250f433bfae603e2

The large first certificate is generated exact fractions, not essential hidden input. These complete compact sources reconstruct it with no originating sandbox or numerical scout.

### File: envelope139_exact.py
```python
"""Exact finite-ray all-path envelope and centroid-reflection obstruction.
No floating arithmetic or SciPy is used in the certificate. LOW43.json is the
complete literal input. A failure excludes ONLY own-centred radial bodies on
these rays with the indicated sole unstable root, not changed angular rays.
"""
from fractions import Fraction as Q
from pathlib import Path
import json,sys,hashlib
from exact137 import dot,sub,mul,cross,lattice,mass,clean
sys.set_int_max_str_digits(0)

# Candidate supporting triples came from a numerical hull. They are checked
# against EVERY exact outer point here; no numerical hull sign is accepted.
NOMINATIONS = None

def potentials(R,r):
 n=len(R);G=[[dot(a,b) for b in R] for a in R]
 p=[Q(0)]*n;p[r]=Q(1);parent=[None]*n;todo=set(range(n));order=[]
 while todo:
  j=max(todo,key=lambda i:(p[i]*p[i]*G[i][i],-i))
  assert p[j]>0,'the positive-dot graph does not reach this root'
  todo.remove(j);order.append(j)
  for i in sorted(todo):
   if G[i][j]>0:
    x=G[i][j]*p[j]/G[i][i]
    if x>p[i]:p[i]=x;parent[i]=j
 assert p[r]==1 and min(p)>0
 # These inequalities alone certify a simultaneous bound on ALL root paths.
 slacks=[]
 for i in range(n):
  for j in range(n):
   if i!=j and G[i][j]>0:
    s=G[i][i]*p[i]-G[i][j]*p[j]
    assert s>=0
    slacks.append(s)
 paths=[]
 for i in range(n):
  path=[i];z=i;prod=Q(1)
  while z!=r:
   j=parent[z];assert j is not None and j not in path
   prod*=G[z][j]/G[z][z];path.append(j);z=j
  assert prod==p[i];paths.append(path)
 return p,parent,paths,len(slacks)

def certificate(R,r,triple):
 p,parent,paths,comparisons=potentials(R,r)
 H=[mul(a,b) for a,b in zip(p,R)]
 i,j,k=triple;normal=cross(sub(H[j],H[i]),sub(H[k],H[i]));h=dot(normal,H[i])
 assert any(normal)
 side=[dot(normal,v)-h for v in H]
 if min(side)>=0:normal=mul(-1,normal);h=-h;side=[-s for s in side]
 assert max(side)<=0,('not a supporting plane',r,triple)
 reflected=mul(-Q(1,3),R[r]);separation=dot(normal,reflected)-h
 assert separation>0,('root not excluded',r,triple)
 # h must be positive because the rays positively span and p_i>0.
 assert h>0
 return {'root':r,'supporting_triple':triple,'paths':paths,'potentials':p,
  'bellman_comparisons':comparisons,'normal':normal,'offset':h,
  'all_support_slacks':[-s for s in side], 'reflected_root':reflected,
  'strict_separation':separation,
  'dimensionless_squared_separation':separation**2/(dot(normal,normal)*dot(R[r],R[r]))}

def main():
 srcpath=Path('LOW43.json');src=json.loads(srcpath.read_text())
 W,F,N,HH,E,EF,A=lattice(src['rows']);V,g=mass(W,F,src['denominator'])
 R=[sub(tuple(Q(x,src['denominator']) for x in row),g) for row in W]
 assert min(Q(h,src['denominator'])-dot(n,g) for n,h in zip(N,HH))>0
 nominations=json.loads(Path('ENVELOPE139_NOMINATIONS.json').read_text())
 certs=[]
 for row in nominations:
  c=certificate(R,row['root'],row['facet']);certs.append(c)
  print('EXACT_ROOT_ENVELOPE_EXCLUDED',row['root'],row['facet'],
   float(c['dimensionless_squared_separation']),flush=True)
 out={'name':'J139_LOW43_FINITE_RAY_ROOT_ENVELOPES',
  'input_sha256':hashlib.sha256(srcpath.read_bytes()).hexdigest(),
  'parent_VEF':[len(A),len(E),len(F)],'origin_is_parent_actual_centroid':g,
  'excluded_roots':[c['root'] for c in certs],'certificates':certs,
  'scope':'Every full-dimensional convex hull of positive radial scalings of these 43 rays, with its OWN uniform centroid at this ray origin, cannot have strict U1 without weak vertices at any listed root. No claim excludes another root, a body centered elsewhere, changed/added angular rays, or all own110 polyhedra.'}
 Path('ENVELOPE139_EXACT_CERT.json').write_text(json.dumps(clean(out),indent=2)+'\n')
 print('J139_TEN_EXACT_FINITE_RAY_ROOT_EXCLUSIONS',len(certs),out['excluded_roots'],flush=True)
if __name__=='__main__':main()
```

### File: reflection139_exact.py
```python
"""Exact all-ray bound propagation excludes one further LOW43 U root.
Every round uses the full exact hull of OUTER radial bounds, centroid reflection
-K/3 subset K, and a nonnegative outgoing chord from every non-root point.
Upward rounding enlarges the bounds and therefore never causes false exclusion.
"""
import json,math,sys,hashlib
from fractions import Fraction as Q
from pathlib import Path
from exact137 import dot,sub,mul,lattice,mass,clean
from envelope139_exact import potentials
sys.set_int_max_str_digits(0)

def ceilq(x,D):return Q(-((-x.numerator*D)//x.denominator),D)
def common(X):
 D=math.lcm(*(x.denominator for row in X for x in row));W=[tuple(int(x*D) for x in row) for row in X]
 return W,D

def main(root=5,grid=10**12,maxiter=30):
 srcpath=Path('LOW43.json');src=json.loads(srcpath.read_text());W,F,N,HH,E,EF,A=lattice(src['rows']);V,g=mass(W,F,src['denominator'])
 R=[sub(tuple(Q(x,src['denominator']) for x in row),g) for row in W];G=[[dot(a,b) for b in R] for a in R]
 p,*_=potentials(R,root);b=[ceilq(x,grid) for x in p];b[root]=Q(1);history=[];excluded=False
 for k in range(maxiter):
  H=[mul(x,r) for x,r in zip(b,R)];WI,D=common(H);WI,FI,NI,HI,EI,EFI,AI=lattice(WI)
  assert min(HI)>0
  bounds=b.copy();certs=[]
  for i in range(len(R)):
   cap=b[i];witness=None
   for f,(n,h) in enumerate(zip(NI,HI)):
    nr=-dot(n,R[i])
    if nr>0:
     value=3*Q(h,D)/nr
     if value<cap:cap=value;witness={'kind':'centroid_reflection','facet':FI[f],'normal':n,'offset':Q(h,D),'raw_cap':value}
   if i!=root:
    values=[(G[i][j]*b[j]/G[i][i],j) for j in range(len(R)) if i!=j and G[i][j]>0]
    outgoing,j=max(values)
    if outgoing<cap:cap=outgoing;witness={'kind':'all_outgoing_chords','largest_target':j,'raw_cap':cap}
   bounds[i]=min(b[i],ceilq(cap,grid))
   if bounds[i]<b[i]:certs.append({'vertex':i,'old_bound':b[i],'new_bound':bounds[i],'witness':witness})
  history.append({'iteration':k,'outer_VEF':[len(AI),len(EI),len(FI)],'changes':certs,'new_bounds':bounds})
  print('EXACT_REFLECTION_ROUND',root,k,len(certs),'root_bound',str(bounds[root]),flush=True)
  if bounds[root]<1:excluded=True;break
  if bounds==b:break
  b=bounds
 assert excluded,'This finite exact policy did not exclude the requested root'
 out={'name':'J139_LOW43_ITERATED_REFLECTION_ROOT5','root':root,'grid':grid,'maxiter':maxiter,'input_sha256':hashlib.sha256(srcpath.read_bytes()).hexdigest(),'initial_paths':potentials(R,root)[2],'history':history,'strict_terminal_root_upper':bounds[root], 'scope':'Own centroid at the original ray origin, only the original 43 ray directions, one strict unstable root at label 5 and no weak unstable vertices. This does not exclude any remaining root or moved/added rays.'}
 Path('REFLECTION139_EXACT_CERT.json').write_text(json.dumps(clean(out),indent=2)+'\n')
 print('J139_ELEVENTH_EXACT_ROOT_EXCLUSION',root,'rounds',len(history),'root_bound',str(bounds[root]),flush=True)
if __name__=='__main__':main()
```

### File: rayinsert139_exact.py
```python
"""One rational new ray opens the LOW43 root-0 reflection gate.
This is an outer-envelope capacity witness, NOT a centered U1 polyhedron.
"""
import json,sys,hashlib
from pathlib import Path
from fractions import Fraction as Q
from exact137 import dot,sub,mul,add,det,lattice,mass,clean
from envelope139_exact import potentials
sys.set_int_max_str_digits(0)

def main():
 src=json.loads(Path('LOW43.json').read_text());W,F,N,HH,E,EF,A=lattice(src['rows']);V,g=mass(W,F,src['denominator'])
 R=[sub(tuple(Q(x,src['denominator']) for x in row),g) for row in W]
 nom=json.loads(Path('RAYINSERT139_GATE_NOMINATION.json').read_text());R.append(tuple(Q(x,nom['new_ray_denominator']) for x in nom['new_ray_numerator']))
 p,par,paths,count=potentials(R,nom['root']);H=[mul(a,r) for a,r in zip(p,R)];q=mul(-Q(1,3),R[nom['root']]);i,j,k,l=nom['witness_vertices']
 aa,bb,cc,yy=sub(H[i],H[l]),sub(H[j],H[l]),sub(H[k],H[l]),sub(q,H[l]);D=det(aa,bb,cc);assert D
 z=[det(yy,bb,cc)/D,det(aa,yy,cc)/D,det(aa,bb,yy)/D];z.append(1-sum(z));assert min(z)>0
 assert tuple(sum(w*H[i][a] for w,i in zip(z,(i,j,k,l))) for a in range(3))==q
 # Therefore q lies strictly in this full-dimensional tetrahedron in H.
 out={'name':'J139_ROOT0_ONE_NEW_RAY_GATE_OPEN','nomination':nom,'potentials':p,'paths':paths,'bellman_comparisons':count,'simplex_weights':z,'simplex_determinant':D,'strict_interior':True,'scope':'The all-path outer envelope passes centroid reflection after one new rational ray. Neither the envelope nor a centered strict-U1/S1 construction is asserted to exist as a completion. No sufficient mass-capacity claim.'}
 Path('RAYINSERT139_EXACT_CERT.json').write_text(json.dumps(clean(out),indent=2)+'\n');print('J139_ONE_RATIONAL_RAY_OPENS_ROOT0_GATE',nom['witness_vertices'],[float(x) for x in z],flush=True)
if __name__=='__main__':main()
```

### File: robust139.py
```python
"""Exact constants for the LOW43 root-0 angular exclusion.
The path-product Lipschitz proof is in J139 recovery part 1.
"""
import json
from fractions import Fraction as Q
from pathlib import Path
p=json.loads(Path('ENVELOPE139_EXACT_CERT.json').read_text())
c=next(x for x in p['certificates'] if x['root']==0)
sq=Q(c['dimensionless_squared_separation']['q'])
lower=Q(9,2000);epsilon=Q(1,20000);loss=Q(256,3)*epsilon
assert sq>lower**2
assert lower-loss==Q(7,30000)>0
out={'normalized_gap_strict_lower':str(lower),'squared_gap':str(sq),'maximum_direction_displacement':str(epsilon),'gap_strict_lower_after_perturbation':str(lower-loss),'scope':'The same43 labeled normalized rays, root0; no added rays, actual centroid at the perturbed ray origin.'}
Path('ROBUST139_EXACT_CERT.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
print('J139_ROOT0_OPEN_ANGULAR_EXCLUSION',epsilon,'remaining_gap_gt',lower-loss)
```

### File: ENVELOPE139_NOMINATIONS.json
```json
[{"root":0,"facet":[29,12,28]},{"root":1,"facet":[37,42,13]},{"root":2,"facet":[42,13,22]},{"root":3,"facet":[37,42,13]},{"root":4,"facet":[37,42,13]},{"root":6,"facet":[22,42,13]},{"root":7,"facet":[42,13,22]},{"root":8,"facet":[42,13,22]},{"root":12,"facet":[42,13,22]},{"root":14,"facet":[37,42,13]}]
```

### File: RAYINSERT139_GATE_NOMINATION.json
```json
{"new_ray_numerator":[-639,68,-766],"new_ray_denominator":1000,"root":0,"witness_vertices":[4,6,16,20]}
```
