# material-87fc898e0703

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J132 — a global reference-centre gap on the exact QW49G compact body

## Scientific statement and scope
Let K be the literal QW49G_APEX_MASS_RELAY_G10_COMPACT body, not a new alias or rounded variant, from immutable result figure-0613 (SHA-256 e15bba43b67e32afee950dda82e82b8eb9cbac6f806a3b4aec735938144e139f, 118656 bytes). That complete parent was read through EOF. Let V be its actual uniform volume, g its actual centroid, and R the union of ALL interior reference centres where this same unchanged body has strict110 and additionalweak000. Then

44291912451/10^12 <= inf_{c in R} |c-g|/V^(1/3) <= 44291947130/10^12.

The old author's reference gap is approximately .044291982863602655. The infimum is strictly greater than (1249998/1250000) times that old gap. Thus changing the reference centre alone can improve the old normalized gap by LESS THAN 0.00016 percent. The interval is an exact rational outward enclosure, not a floating optimizer's bound. The lower projection need not itself be reference110 or weak-free and the infimum need not be attained. The upper point is exactly reference110/weak000/primitive000. This result does not exclude physical changes, projective changes, changed metric, changed density, other bodies or an own110 construction. K itself is own(21,28,47), with 27 physical and 20 polar positive persistence bars, V119/E209/F92; the canonical accepted own110 remains C622.

## Affine guards
For a true physical edge i--j and vertex coordinates x_i,x_j, i has a radial escape along that edge exactly when
L_P(i,j;c)=(x_i-c).(x_j-x_i)>0.
Thus a=-(x_j-x_i), b=x_i.(x_j-x_i) give L=a.c+b. For two adjacent maximal supporting faces (n,h),(m,k), with n.x<=h and m.x<=k, positivity of the corresponding polar escape has affine numerator
L_Q(f,k;c)=(n.m)h-|n|^2 k + (|n|^2 m-(n.m)n).c.
All support heights h-n.c are positive at an interior centre, so this clearing of denominators preserves sign. Interior guards are h-n.c>0.
A non-root with no additional weak equilibrium must have a strictly positive true-edge escape. A positive escape strictly increases the corresponding squared physical or polar radial norm, so positive directed cycles are impossible. A choice of one positive escape for every non-root, together with strict negative root guards and positive interior heights, establishes unique U and S. The direct exact census separately checks H and additional weak cases.

## Exact upper certificate, one policy only
For each non-root at the author's reference centre choose the true-edge escape maximizing L/max(abs(a)). Roots are physical40 and polar24. There are118 physical and91 polar chosen escape rows plus92 interior rows, total301. Intersect their closed positive-margin versions L/max(abs(a))>=eta, eta=1/10^9. The old centre satisfies all with smallest normalized guard approximately2.6184252744658542e-8.
Project g onto this convex polyhedron. The three active rows are P51->37, Q89->63 and Q90->35. The exact positive KKT multipliers are computed by a rational3x3 solve; their decimal values are approximately .00127624253996405, .00936721474446029, .01206054078786604. The exact projected centre is approximately (.08119757873845448,.05603820293026759,-.10863373611051315). Its displacement from the author's centre is only about4.013e-8. All301 inequalities and the KKT normal identity are checked exactly. Its normalized distance is approximately .04429194712985737. The full exact physical/polar/edge census at this point is strict110, weak000 and primitive000. It supplies a genuine upper bound on the infimum over ALL policies.

## The all-policy lower certificate
Use the squared distance R2 of the preceding upper point from g. Centres outside that closed Euclidean ball already have distance at least the upper bound. For every affine escape L=a.c+b let l=L(g). If l<0 and l^2>|a|^2 R2, L is strictly negative throughout the ball. Such an edge cannot be the positive escape of its node anywhere in the ball. The exact implementation discards518 directed forms.
For physical40 and polar24 every outgoing form is so excluded, hence those two nodes remain strict roots throughout the ball. Every other physical or polar node must have a positive outgoing true-edge escape at ANY weak-free reference110 centre in the ball. Where only one possible outgoing form remains, its positivity is mandatory independently of policy choices or root selection elsewhere.
This forces132 guards:97 physical and35 polar. Counts of remaining possible escapes for the209 non-root nodes are {1:132,2:72,4:1,7:2,11:1,13:1}. Intersect the closed versions of the132 mandatory guards and all92 closed interior guards. Project g exactly onto that necessary polyhedron with eta=0. The three active rows are P57->98, P63->59 and P46->64. Exact positive multipliers have approximate values .009372686307730705,.0023547545789576805,.01668258888165741. Full exact feasibility and the normal identity certify that this projection is nearest in the relaxed polyhedron. Since every reference110 centre inside the upper ball lies in it, its distance is a lower bound for all such centres; points outside the ball are farther. This proves the global bound without enumerating all policies.
For A x<=b and positive multipliers with g-x=A_active^T lambda, the identity |y-g|^2=|x-g|^2+|y-x|^2+2(x-g).(y-x) shows |y-g|>=|x-g| for every feasible y. All distances are certified without square roots: the sixth power of |c-g|/V^(1/3) equals |c-g|^6/V^2, rational. The decimal enclosing endpoints and comparison with the old gap are checked by exact sixth-power inequalities.

## Constructive consequence and limitation
The all-policy bottleneck is on three ordinary host edges, not just on the added apex-relay faces. P57--98 has adjacent H4/25; P63--59 has H26/28; P46--64 has H7/19. Incident triples are vertex57:{4,18,25},98:{4,24,25},63:{14,26,28},59:{26,27,28},46:{6,7,19},64:{7,17,19}. All six are current own-U vertices. Changing the reference alone is exhausted to the stated precision. Physical host/normal-fan changes, actual mass transport, or other genuine geometry must address these ordinary interfaces. This does not say that three edges suffice to solve the full actual P/Q landscape.

## Recovery dependencies and commands
This material contains the ENTIRE new exact certificate source. The exact body, full exact115.cpp and its reference49g adapter are already literal in the named immutable parent; they are not supplied by merely naming a sandbox. A computational successor must receive that completed parent as parent_assignment_ids along with this material. No C622 source is used here.
Recover the parent's literal RECOVER_QW49G.py (93639 bytes, SHA-256 2d019d1ce94cb86b31e51db0d81e1a9d8305a59a6bc241d239e19d8f174d09b8) and execute it. It reconstructs57 exact units from its dictionary (265678 bytes, SHA-256 cf8db0ab6e17a2e9eb426e89096ed4e32d623d568e78b07d04298208987233d8). Enter recovered/ and run:

python RECOVER_QW49G.py  # run in the directory above recovered/, before entering it
cd recovered
g++ -O2 -std=c++17 exact115.cpp -lgmpxx -lgmp -o exact115
python apexexact49g.py compile
python apexexact49g.py replay QW49G_APEX_MASS_RELAY_G10_COMPACT
python certificate132.py

Save the fenced source below as certificate132.py in recovered/ with a final newline. New source6321 bytes, SHA-256 19c28699ed0966502848ae5687f6943b1b50cdf1c648a0305c186781489783ea. Required exact input QW49G_APEX_MASS_RELAY_G10_COMPACT_INPUT.json is7791 bytes/SHA-256 e7566f52d438560e5ec42b5b265a1612e10e4dadadcb5c6d5270ab1cf7171e36. Parent exact115.cpp is11038 bytes/SHA-256 d7fd1244c086a0c5354844cca3453c42b26ed31a55b89720aa9e3987f0a06736. Python3.13.5 was used; this new certificate uses only the standard library and the parent's GMP-backed exact census executable, no SciPy or floating optimizer.
Expected terminal marker:
J132_ALL_POLICY_REFERENCE_GAP_EXACT_PASS 44291912451 44291947130 1000000000000 summary 2640 eb3d0c4de6e496d5e354ad4770cf8e8413e0ebdf6c27ae67f685470fd80b6dfc
The reproduced compact J132_GLOBAL_CERTIFICATE_SUMMARY.json is2640 bytes with that SHA-256; it contains the full rational upper and lower points, counts, scope and census. Large raw rational row ledgers are reproducible, not necessary recovery inputs. This certificate was executed and passed by the coordinator; it is one exact implementation, not a claim of independent dual verification.

```python
#!/usr/bin/env python3
"""Exact all-policy reference-centre distance bracket, QW49G compact body.
Run in the decoded QW49G source directory after its compact own/reference replay.
Python 3 standard library only. Does not depend on SciPy or floating optimizers.
Input audit is produced by the complete exact115.cpp in the immutable parent.
"""
from pathlib import Path
from fractions import Fraction as Q
import sys,json,hashlib,subprocess
sys.set_int_max_str_digits(0)
TAG='QW49G_APEX_MASS_RELAY_G10_COMPACT'
O=Q(0)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(s,a):return tuple(s*x for x in a)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),O)
def solve(A,b):
 n=len(A);z=[list(a)+[t]for a,t in zip(A,b)]
 for j in range(n):
  k=next(k for k in range(j,n)if z[k][j]);z[j],z[k]=z[k],z[j];p=z[j][j];z[j]=[x/p for x in z[j]]
  for k in range(n):
   if k!=j:p=z[k][j];z[k]=[x-p*y for x,y in zip(z[k],z[j])]
 out=tuple(row[-1]for row in z);assert all(dot(a,out)==t for a,t in zip(A,b));return out

def forms(X,H,E):
 rows=[]
 for u,v in E:
  for i,j in [(u,v),(v,u)]:
   d=sub(X[j],X[i]);a=mul(-1,d);rows.append(('P',i,j,a,dot(X[i],d),max(map(abs,a))))
 for u,v in E.values():
  for i,j in [(u,v),(v,u)]:
   n,h=H[i];m,k=H[j];nn=dot(n,n);nm=dot(n,m);a=sub(mul(nn,m),mul(nm,n));rows.append(('Q',i,j,a,nm*h-nn*k,max(map(abs,a))))
 return rows

def projection(rows,g,eta,labels):
 lookup={r[:3]:j for j,r in enumerate(rows)};ids=[lookup[tuple(z)]for z in labels]
 A=[mul(-1/r[5],r[3])for r in rows];b=[r[4]/r[5]-eta for r in rows]
 G=[[dot(A[i],A[j])for j in ids]for i in ids];lam=solve(G,[dot(A[i],g)-b[i]for i in ids]);assert min(lam)>0
 x=g
 for i,l in zip(ids,lam):x=sub(x,mul(l,A[i]))
 assert all(dot(a,x)<=t for a,t in zip(A,b));assert all(dot(A[i],x)==b[i]for i in ids)
 d=sub(g,x);normal=(O,O,O)
 for i,l in zip(ids,lam):normal=add(normal,mul(l,A[i]))
 assert d==normal
 return x,dot(d,d)

def main():
 src=Path(TAG+'_INPUT.json');assert hashlib.sha256(src.read_bytes()).hexdigest()=='e7566f52d438560e5ec42b5b265a1612e10e4dadadcb5c6d5270ab1cf7171e36'
 raw=json.loads(src.read_text());a=json.loads(Path(TAG+'_AUDIT.json').read_text());ref=json.loads(Path(TAG+'_REFERENCE.json').read_text())
 assert a['vertices']==ref['vertices'] and a['faces']==ref['faces'] and a['volume']==ref['volume'] and a['centroid']==ref['centroid']
 assert [a[k]for k in ['V','E','F']]==[119,209,92] and a['strict']==[21,28,47] and a['weak']==[0,0,0]
 assert ref['strict']==[1,1,0] and ref['weak']==[0,0,0] and ref['primitive_zeros']==[0,0,0]
 assert a['active_input_planes']==list(range(92));X=[tuple(map(Q,x))for x in a['vertices']];H=[(tuple(map(Q,row[:3])),Q(row[3]))for row in raw['rows']]
 c=tuple(map(Q,raw['reference_center']));g=tuple(map(Q,a['centroid']));V=Q(a['volume']);E={}
 for f,cy in enumerate(a['faces']):
  for u,v in zip(cy,cy[1:]+cy[:1]):E.setdefault(tuple(sorted((u,v))),[]).append(f)
 assert len(E)==209 and all(len(v)==2 for v in E.values())
 rows=forms(X,H,E);roots={'P':ref['U'][0],'Q':ref['S'][0]};assert roots=={'P':40,'Q':24}
 policy=[]
 for kind,N in [('P',119),('Q',92)]:
  for i in range(N):
   rr=[r for r in rows if r[0]==kind and r[1]==i]
   if i==roots[kind]:assert max(dot(r[3],c)+r[4]for r in rr)<0;continue
   r=max(rr,key=lambda r:(dot(r[3],c)+r[4])/r[5]);assert dot(r[3],c)+r[4]>0;policy.append(r)
 interior=[('I',i,-1,mul(-1,n),h,max(map(abs,n)))for i,(n,h)in enumerate(H)]
 policy+=interior;eta=Q(1,10**9);assert len(policy)==301
 assert min((dot(r[3],c)+r[4])/r[5]for r in policy)>eta
 chosen=[('P',51,37),('Q',89,63),('Q',90,35)]
 upper_point,U2=projection(policy,g,eta,chosen)
 # All nonroots have a strictly positive actual true-edge escape at upper_point.
 for kind,N in [('P',119),('Q',92)]:
  for i in range(N):
   vv=[dot(r[3],upper_point)+r[4]for r in rows if r[0]==kind and r[1]==i]
   assert (max(vv)<0 if i==roots[kind] else max(vv)>0)
 forced=[];choices=[];hist={};discarded=0
 for kind,N in [('P',119),('Q',92)]:
  for i in range(N):
   rr=[r for r in rows if r[0]==kind and r[1]==i];possible=[]
   for r in rr:
    l=dot(r[3],g)+r[4];outside=l*l>dot(r[3],r[3])*U2
    if l>0 or not outside:possible.append(r)
    else:discarded+=1
   if i==roots[kind]:assert not possible;continue
   assert possible;hist[len(possible)]=hist.get(len(possible),0)+1
   if len(possible)==1:forced.append(possible[0]);choices.append(possible[0][:3])
 assert len(forced)==132 and sum(r[0]=='P'for r in forced)==97 and sum(r[0]=='Q'for r in forced)==35
 assert hist=={1:132,2:72,4:1,7:2,11:1,13:1}
 chosen_global=[('P',57,98),('P',63,59),('P',46,64)]
 lower_point,L2=projection(forced+interior,g,O,chosen_global);assert L2<=U2
 low6=L2**3/V**2;up6=U2**3/V**2;old6=dot(sub(c,g),sub(c,g))**3/V**2
 L,U,D=44291912451,44291947130,10**12
 assert Q(L,D)**6<=low6<=up6<=Q(U,D)**6
 assert low6>old6*Q(9999984,10000000)**6
 # Full direct census, including weak edge equilibria, at the strict upper point.
 with Path(TAG+'.txt').open('rb')as fi,Path('J132_UPPER_REFERENCE.json').open('wb')as fo,Path('J132_UPPER_REFERENCE.log').open('wb')as fe:
  subprocess.run(['./reference49g']+list(map(str,upper_point)),stdin=fi,stdout=fo,stderr=fe,check=True)
 rr=json.loads(Path('J132_UPPER_REFERENCE.json').read_text());assert rr['strict']==[1,1,0] and rr['weak']==[0,0,0] and rr['primitive_zeros']==[0,0,0]
 out=dict(body=TAG,own=[21,28,47],VEF=[119,209,92],mandatory_roots=roots,policy_rows=301,policy_active=chosen,global_active=chosen_global,forced_P=97,forced_Q=35,possible_histogram=hist,discarded_directed_forms=discarded,upper_point=list(map(str,upper_point)),lower_projection=list(map(str,lower_point)),normalized_distance_interval=[str(Q(L,D)),str(Q(U,D))],all_reference_centres_retain_more_than_old_gap_fraction='1249998/1250000',upper_census=[1,1,0],upper_weak=[0,0,0],upper_primitive=[0,0,0],scope='All strict110/weak000 reference centres of this exact unchanged body. Lower is a necessary-cell bound and need not be attained. No exclusion of physical shape changes.')
 data=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode();Path('J132_GLOBAL_CERTIFICATE_SUMMARY.json').write_bytes(data)
 print('J132_ALL_POLICY_REFERENCE_GAP_EXACT_PASS',L,U,D,'summary',len(data),hashlib.sha256(data).hexdigest())
if __name__=='__main__':main()
```
