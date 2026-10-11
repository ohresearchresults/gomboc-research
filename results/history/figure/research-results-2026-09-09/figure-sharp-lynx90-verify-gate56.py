# Python 3.13.5, standard library only.  Exact exclusion, not a body search.
from itertools import product, combinations, permutations
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
import json

# Labels 1..n; candidate roots modulo automorphisms; all triangular faces.
DATA = [
 (4,(1,),((1,2,3),(1,4,2),(1,3,4),(2,4,3))),
 (5,(1,3),((4,3,1),(1,3,5),(5,4,1),(2,3,4),(5,3,2),(2,4,5))),
 (6,(1,),((1,2,3),(4,2,1),(1,3,5),(5,4,1),(6,3,2),(2,4,6),(6,5,3),(4,5,6))),
 (6,(1,2,5),((1,3,5),(6,3,1),(5,4,1),(1,4,6),(2,4,5),(6,4,2),(2,5,6),(6,5,3)))
]
# For lexicographically sorted rooted marked-tree keys: first base-36
# character is denominator d, the remaining characters are positive
# numerators a_i of shadow weights a_i/d in canonical preorder.
TOKENS = """111111 111125 111233 111254 111111 111125 212332 112222 112233 213552 112433 112453
11111 111111 111212 111223 11124 111241 111124 112122 112143 112232 112433 112343
11233 112331 112514 112444 11254 112541 111111 111125 111233 111254 111111 111125
111111 121111 121123 121231 121322 121343 111111 111125 121211 121211 121223 122221
122221 123222 123232 122321 122321 235944 8DLZXJ 111111 212233 212355 11111 111111
111212 111223 11124 111241 11111 111111 12222 122221 121211 121313 121333 12233
122331 111111 111124 122133 123121 124122 124143 122221 124232 123422 123443 12231
122311 12433 124231 123311 124513 124433 12443 124531 1111 11121 111211 111221
111111 112111 112122 11211 112121 112211 112211 112222 11222 112321 1122 11221
113311 113321 111212 111222 12123 111231 121124 121111 131133 131222 121322 121343
12122 131221 131312 131333 12133 131331 122124 122111 132133 133122 134122 123133
123222 123222 123422 123342 132222 12222 132221 12322 134231 133312 124413 123433
12343 124431 1222 13231 132311 132321 132121 134112 134133 13413 134131 134212
134413 134433 13433 134431 1243 13441 135411 135421""".split()

def require(ok, msg):
    if not ok:
        raise ValueError(msg)

def check_graphs():
    for n,roots,faces in DATA:
        fs={tuple(sorted(f)) for f in faces}
        incidence=Counter(e for f in fs for e in combinations(f,2))
        edges=set(incidence)
        require(len(fs)==2*n-4 and len(edges)==3*n-6,'wrong triangulation')
        require(set(incidence.values())=={2},'nonmanifold edge')
        require({v for f in fs for v in f}==set(range(1,n+1)),'missing vertex')
        covered=set()
        for p in permutations(range(1,n+1)):
            image={tuple(sorted(p[v-1] for v in f)) for f in fs}
            if image==fs: covered.update(p[r-1] for r in roots)
        require(covered==set(range(1,n+1)),'root orbits not covered')

def code_and_order(parent, marks):
    def visit(v):
        cs = sorted((visit(i) for i in range(1,len(parent)) if parent[i]==v),
                    key=lambda pair:(pair[0],pair[1]))
        return (str(int(v in marks))+'('+''.join(c for c,o in cs)+')',
                [v]+[i for c,o in cs for i in o])
    return visit(0)

def cases():
    for graph,(n,roots,faces) in enumerate(DATA):
        adj={i:set() for i in range(1,n+1)}
        for a,b,c in faces:
            for i,j in ((a,b),(b,c),(c,a)):
                adj[i].add(j); adj[j].add(i)
        for root in roots:
            rest=[v for v in range(1,n+1) if v!=root]
            rename={v:i for i,v in enumerate([root]+rest)}
            for choice in product(*(sorted(adj[v]) for v in rest)):
                parent=[-1]+[rename[v] for v in choice]
                good=True
                for start in range(1,n):
                    v=start; seen=set()
                    while v!=0:
                        if v in seen:
                            good=False; break
                        seen.add(v); v=parent[v]
                    if not good: break
                if not good: continue
                for face in faces:
                    if root not in face:
                        marks={rename[v] for v in face}
                        key,order=code_and_order(parent,marks)
                        yield graph,root,parent,marks,key,order

def det(A):
    # Fraction-free Bareiss, with row pivoting; also checks exact divisions.
    A=[row[:] for row in A]; n=len(A); old=1; sign=1
    for k in range(n-1):
        p=next((p for p in range(k,n) if A[p][k]),None)
        if p is None: return 0
        if p!=k:
            A[p],A[k]=A[k],A[p]; sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                q,r=divmod(pivot*A[i][j]-A[i][k]*A[k][j],old)
                require(r==0,'nonexact Bareiss division')
                A[i][j]=q
            A[i][k]=0
        old=pivot
    return sign*A[-1][-1]

def reduced_matrix(parent,marks,d,nums):
    # This is 2*d times K, whose variables are (1,x_1,...,x_(n-1)).
    n=len(parent); M=[[0]*n for _ in range(n)]; M[0][0]=2*d
    for i in range(1,n):
        a=nums[i-1]; p=parent[i]
        M[i][i]+=2*a
        M[0][i]+=d*int(i in marks); M[i][0]+=d*int(i in marks)
        M[i][p]-=a; M[p][i]-=a
    return M

def full_matrix(parent,marks,d,nums):
    # Independent expansion of 2*d*[sum_i (a_i/d) q_i + L].
    n=len(parent); m=1+3*(n-1); M=[[0]*m for _ in range(m)]
    M[0][0]=2*d
    def idx(i,k): return 1+3*(i-1)+k
    for i in range(1,n):
        a=nums[i-1]; p=parent[i]
        for k in range(3):
            ii=idx(i,k); M[ii][ii]+=2*a
            if p==0:
                if k==0:
                    M[0][ii]-=a; M[ii][0]-=a
            else:
                jj=idx(p,k); M[ii][jj]-=a; M[jj][ii]-=a
        if i in marks:
            ii=idx(i,0); M[0][ii]+=d; M[ii][0]+=d
    return M

def ldl_positive(A):
    # Rational Schur elimination, separate from the Bareiss test.
    A=[[Q(v) for v in row] for row in A]
    for k in range(len(A)):
        require(A[k][k]>0,'nonpositive full-matrix pivot')
        for i in range(k+1,len(A)):
            for j in range(i,len(A)):
                A[i][j]-=A[i][k]*A[j][k]/A[k][k]
                A[j][i]=A[i][j]

check_graphs()
rows=list(cases()); keys=sorted({r[4] for r in rows})
require(len(keys)==len(TOKENS)==164,'canonical coverage changed')
cert={k:[int(c,36) for c in word] for k,word in zip(keys,TOKENS)}
counts=Counter(); unique_by_n=Counter(); checked=set(); records=[]
min_minor=None
for graph,root,parent,marks,key,order in rows:
    d,*a=cert[key]; n=len(parent)
    require(d>0 and len(a)==n-1 and min(a)>0,'bad multiplier')
    # Pull the canonical multipliers back onto every ORIGINAL raw case.
    nums=[0]*(n-1)
    for v,value in zip(order[1:],a): nums[v-1]=value
    M=reduced_matrix(parent,marks,d,nums)
    for size in range(1,n+1):
        value=det([r[:size] for r in M[:size]])
        require(value>0,'nonpositive principal minor')
        min_minor=value if min_minor is None else min(min_minor,value)
    counts[(graph,root)]+=1
    if key not in checked:
        ldl_positive(full_matrix(parent,marks,d,nums))
        checked.add(key); unique_by_n[n]+=1
        records.append([key,d,a])
require(dict(counts)=={(0,1):16,(1,1):225,(1,3):150,(2,1):1536,
                      (3,1):1344,(3,2):1680,(3,5):1008},'raw coverage changed')
require(dict(unique_by_n)=={4:4,5:26,6:134},'wrong orbit count')
payload=json.dumps(sorted(records),separators=(',',':')).encode()
print(json.dumps({'status':'EXACT_FILLED_VOLUME_V_GE_7_REPLAY_PASS',
 'raw_cases_V4':16,'raw_cases_V5':375,'raw_cases_V6':5568,
 'canonical_certificates':len(checked),'minimum_integer_leading_minor':min_minor,
 'certificate_records_sha256':sha256(payload).hexdigest()},sort_keys=True))
