"""Independent exact verification of the universal 285-rooted-shape lemma.
CPython 3.13.5, standard library only. No numerical engine import.
Run python -S verify_universal.py universal285.json
"""
import itertools,json,hashlib,collections,sys,math
from fractions import Fraction as F
from pathlib import Path
assert __debug__
PH='3b737649ca4e531383c349e6a3e088fdf458b5b826662c391f655f628f843a94'
T=(0,0,1,2,3,4,5,6,0)
def encoded(o):return (json.dumps(o,sort_keys=True,separators=(',',':'))+'\n').encode()
def parse(code):
 p=[]
 def visit(k,pa):
  assert code[k]=='(';v=len(p);p.append(pa if v else 0);k+=1
  while code[k]=='(':k=visit(k,v)
  assert code[k]==')';return k+1
 assert visit(0,0)==len(code)
 return tuple(p)
def root_code(p):
 children=[[]for _ in p]
 for i in range(1,len(p)):children[p[i]].append(i)
 def rec(i):return '('+''.join(sorted(rec(j)for j in children[i]))+')'
 return rec(0)
def rooted_trees():
 codes={1:['()']}
 for n in range(2,10):
  pool=sorted((s,k)for k in range(1,n)for s in codes[k]);out=[]
  def forest(start,left,parts):
   if left==0:out.append('('+''.join(parts)+')');return
   for j in range(start,len(pool)):
    s,k=pool[j]
    if k<=left:forest(j,left-k,parts+[s])
  forest(0,n-1,[]);codes[n]=sorted(out)
  assert len(out)==len(set(out))
 counts=[len(codes[n])for n in range(1,10)]
 assert counts==[1,1,2,4,9,20,48,115,286]
 ps=sorted(parse(s)for s in codes[9]);assert len(set(ps))==286 and ps[278]==T
 return ps,counts

def all_cells(apex):
 return [tuple(sorted((apex,)+t))for t in itertools.combinations([i for i in range(9)if i!=apex],3)]
def scalar_matrices(rec,extra=()):
 aa=rec['apices'];A=len(aa);cv=rec['covariance'];z=rec['z'];p=rec['parent']
 assert len(aa)==len(set(aa)) and all(type(a)is int and 0<=a<9 for a in aa)
 assert type(cv)is bool and all(type(x)is int for x in z)
 constraints=[(i,p[i],1)for i in range(1,9)]+list(extra)
 m=len(constraints);k=56*A;end=9*A+m*k
 assert len(z)==end+(45+int(cv))*(A-1) and min(z[9*A:end])>=0
 for a,ap in enumerate(aa):
  for j,t in enumerate(all_cells(ap)):
   block=a*56+j;P=collections.defaultdict(int)
   def add(i,j,x):P[min(i,j),max(i,j)]+=x
   for i in range(9):
    for j in t:add(i,j,2*z[9*a+i])
   ll=z[9*A+m*block:9*A+m*(block+1)]
   for l,(i,j,sg)in zip(ll,constraints):add(i,i,2*sg*l);add(i,j,-2*sg*l)
   for b in range(A-1):
    sg=int(a==b)-int(a==A-1);at=end+45*b
    for i in range(9):
     for j in range(i,9):add(i,j,2*sg*z[at]);at+=1
   if cv:
    eta=sum((int(a==b)-int(a==A-1))*z[end+45*(A-1)+b]for b in range(A-1))
    for i in t:
     for j in t:add(i,j,2*eta)
     add(i,i,2*eta)
   Q=[[0]*9 for _ in range(9)]
   for (i,j),v in P.items():
    if i==j:Q[i][i]=v
    else:assert v%2==0;Q[i][j]=Q[j][i]=v//2
   yield a,t,Q,ll,constraints

def bareiss(Q):
 M=[r[:]for r in Q];old=1;out=[]
 assert all(M[i][j]==M[j][i]for i in range(9)for j in range(9))
 for i in range(9):M[i][i]-=1
 for k in range(9):
  d=M[k][k];assert d>0,('NONPOSITIVE_LEADING_MINOR',k,d);out.append(d)
  for i in range(k+1,9):
   for j in range(i,9):
    num=d*M[i][j]-M[i][k]*M[k][j];assert num%old==0
    M[i][j]=M[j][i]=num//old
  old=d
 return out

def fraction_ldl(Q):
 L=[[F(int(i==j))for j in range(9)]for i in range(9)];dd=[];prod=F(1);out=[]
 for i in range(9):
  d=F(Q[i][i]-1)-sum(L[i][k]**2*dd[k]for k in range(i));assert d>0
  dd.append(d);prod*=d;assert prod.denominator==1;out.append(int(prod))
  for j in range(i+1,9):L[j][i]=(Q[j][i]-sum(L[j][k]*L[i][k]*dd[k]for k in range(i)))/d
 return out

def determinant(a,b,c):
 return sum(a[i]*(b[(i+1)%3]*c[(i+2)%3]-b[(i+2)%3]*c[(i+1)%3])for i in range(3))
def cross(a,b):return [a[(i+1)%3]*b[(i+2)%3]-a[(i+2)%3]*b[(i+1)%3]for i in range(3)]
def sub(a,b):return [x-y for x,y in zip(a,b)]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def physical_fixture():
 X=[[28*(2*((i>>0)&1)-1),28*(2*((i>>1)&1)-1),28*(2*((i>>2)&1)-1)-5]for i in range(8)]+[[0,0,51]]
 facets={}
 for a,b,c in itertools.combinations(range(9),3):
  n=cross(sub(X[b],X[a]),sub(X[c],X[a]));val=[dot(n,sub(v,X[a]))for v in X]
  if not any(val) or (min(val)<0<max(val)):continue
  if min(val)==0:n=[-v for v in n];val=[-v for v in val]
  assert max(val)==0 and min(val)<0
  f=tuple(i for i,v in enumerate(val)if v==0)
  if f in facets:continue
  cycles=[]
  for perm in itertools.permutations(f[1:]):
   q=(f[0],)+perm
   if all(dot(cross(sub(X[j],X[i]),sub(X[k],X[i])),n)>0
          for i,j in zip(q,q[1:]+q[:1])for k in q if k not in(i,j)):cycles.append(q)
  assert len(cycles)==1;facets[f]=cycles[0]
 FS=sorted(facets.values());assert sorted(map(len,FS))==[3]*4+[4]*5
 d={}
 for t in itertools.combinations(range(9),4):
  a,b,c,z=t;d[t]=abs(determinant(sub(X[b],X[a]),sub(X[c],X[a]),sub(X[z],X[a])))
 fans=[];mom=[]
 for a in range(9):
  ff=[]
  for f in FS:
   if a in f:continue
   ff += [tuple(sorted((a,f[0],f[k],f[k+1])))for k in range(1,len(f)-1)]
  assert len(ff)==len(set(ff)) and all(d[t]>0 for t in ff);fans.append(set(ff))
  D=sum(d[t]for t in ff)
  first=[sum(d[t]*sum(X[i][j]for i in t)for t in ff)for j in range(3)]
  second=[[sum(d[t]*(sum(X[i][j]for i in t)*sum(X[i][k]for i in t)+sum(X[i][j]*X[i][k]for i in t))for t in ff)for k in range(3)]for j in range(3)]
  assert D==56*28**3 and first==[0,0,0];mom.append(second)
 assert all(q==mom[0]for q in mom)
 M=[[5,1,2],[1,4,1],[2,1,6]];assert determinant(*M)==97
 G=[[sum(X[i][a]*M[a][b]*X[j][b]for a in range(3)for b in range(3))for j in range(9)]for i in range(9)]
 U=[i for i in range(9)if all(G[i][j]<G[i][i]for j in range(9)if i!=j)]
 assert len(U)>=2
 return X,FS,d,fans,G,dict(vertices=X,facets=FS,six_volume=56*28**3,second_moment_numerator=mom[0],metric=M,unstable_vertices=U)

def redirects(ps):
 out=[];same=[];cyclic=[]
 for i in range(1,9):
  for j in range(9):
   if j in(i,T[i]):continue
   q=list(T);q[i]=j;valid=True
   for v in range(1,9):
    seen=set()
    while v!=0:
     if v in seen:valid=False;break
     seen.add(v);v=q[v]
    if not valid:break
   if not valid:cyclic.append((i,j));continue
   key=parse(root_code(q));ix=ps.index(key)
   if ix==278:same.append((i,j))
   else:out.append([i,j,ix])
 expected=[(i,j)for i in range(2,8)for j in range(i-1)]+[(i,8)for i in range(1,8)if i!=2]+[(8,j)for j in range(1,8)]
 assert len(out)==34 and {(i,j)for i,j,k in out}==set(expected) and same==[(2,8)] and len(cyclic)==21
 return out

def verify_record(r,d,fans,G,extra=()):
 nm=0;mh=hashlib.sha256();dh=hashlib.sha256();left=0;right=0
 for a,t,Q,ll,cc in scalar_matrices(r,extra):
  bb=bareiss(Q);assert bb==fraction_ldl(Q)
  mh.update(encoded([a,t,Q]));dh.update(encoded([a,t,bb]));nm+=1
  if t not in fans[r['apices'][a]]:continue
  left+=d[t]*sum(Q[i][j]*G[i][j]for i in range(9)for j in range(9))
  right+=d[t]*sum(2*l*sg*(G[i][i]-G[i][j])for l,(i,j,sg)in zip(ll,cc))
 assert left==right and left>0
 return nm,mh.hexdigest(),dh.hexdigest()

def main():
 path=Path(sys.argv[1]if len(sys.argv)>1 else'universal285.json');raw=path.read_bytes();o=json.loads(raw);assert encoded(o)==raw
 assert o['version']==1 and o['identity']=='NOVA24_UNIVERSAL_285_TREE_COVARIANCE_V1'
 assert o['parent_assignment']=='asg_VOkJgQeJI85JsScj0zkUI191' and o['parent_sha256']==PH
 ps,counts=rooted_trees();rs=o['records'];assert [r['index']for r in rs]==[i for i in range(286)if i!=278]
 X,FS,d,fans,G,fixture=physical_fixture();ledger=[];nmat=0
 for r in rs:
  ix=r['index'];assert tuple(r['parent'])==ps[ix]
  assert r['apices']in([0],[0,1],[0,2]) and r['covariance']==(len(r['apices'])>1)
  n,mh,dh=verify_record(r,d,fans,G);nmat+=n;ledger.append([ix,n,mh,dh])
 assert nmat==17416
 red=redirects(ps);assert all(i!=278 for a,b,i in red)
 report=dict(identity='NOVA24_UNIVERSAL_285_TREE_EXACT_AUDIT_V1',rooted_tree_counts=counts,
             certified_rooted_shapes=285,remaining_rooted_shape=T,matrix_count=nmat,
             leading_minor_count=9*nmat,record_hash_ledger=ledger,redirect_dependencies=red,
             physical_regression=fixture,certificate_sha256=hashlib.sha256(raw).hexdigest())
 b=encoded(report);Path('universal285_verification.json').write_bytes(b)
 print('INDEPENDENT_ROOTED_MULTISET_ENUMERATION_PASS',counts)
 print('SCALAR_POLYNOMIAL_INTEGER_BAREISS_AND_FRACTION_LDL_PASS',nmat,9*nmat)
 print('ACTUAL_NINE_FAN_VOLUME_FIRST_COVARIANCE_AND_WEIGHTED_IDENTITY_PASS',len(rs))
 print('BROOM_34_STRICT_REDIRECTIONS_AND_ONLY_ALTERNATE_2_TO_8_PASS')
 print('UNIVERSAL_285_EXCLUSION_PASS_ONE_BROOM_REMAINS_NO_V10_CLAIM')
 print('REPORT',len(b),hashlib.sha256(b).hexdigest())
if __name__=='__main__':main()
