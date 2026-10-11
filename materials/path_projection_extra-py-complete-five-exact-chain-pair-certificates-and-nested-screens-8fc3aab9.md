# material-8fc3aab988f7

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Five exact additional pair certificates. Standard library, assertions required.
Run: python -S path_projection_extra.py build|check.
"""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import hashlib,json,sys
if not __debug__:
    raise RuntimeError('Assertions must be enabled')
HERE=Path(__file__).resolve().parent

def pin(b):return (len(b),hashlib.sha256(b).hexdigest())
def enc(a):return (json.dumps(a,sort_keys=True,separators=(',',':'))+'\n').encode()
assert pin((HERE/'path_projection.py').read_bytes())==(6201,'42f6a03f6756de1f8266c4923c59e2991b9486e01c7884720a1dfab17d54c289')
import path_projection as P
R=P.R
SPECS=(
 ((1,6),F(1337,10000),(1255453,2498480,2767698,3065921,3396281,3762235)),
 ((1,7),F(1451,10000),(1229548,2406327,2597122,2803044,3025295,3265166,3524060)),
 ((2,6),F(4111,10000),(1008777,2476319,2184816,2361272,2551980,2758092)),
 ((2,7),F(4227,10000),(1009109,2410061,2137219,2259278,2388312,2524709,2668901)),
 ((6,7),F(4991,5000),(1206849,1459259,1764460,2133493,2579708,3119249,1767822)),
)

def certificates():
    records=[]
    for terms,B,nums in SPECS:
        m=len(nums);assert m==max(terms)
        q=[[F(0) for _ in range(m+1)] for _ in range(m+1)];q[0][0]=B
        for j in terms:q[0][j]+=F(1,2);q[j][0]+=F(1,2)
        for j,a in enumerate(nums,1):
            a=F(a,1000000);assert a>0
            q[j][j]+=a;q[j][j-1]-=a/2;q[j-1][j]-=a/2
        order=tuple(range(1,m+1))+(0,)
        pivots=R.ldl([[q[i][j] for j in order] for i in order])
        records.append({'depths':terms,'B':str(B),'lambda_numerators':nums,
                        'denominator':1000000,'pivots':list(map(str,pivots))})
    assert sum(len(r['pivots']) for r in records)==38
    return records
CERTIFICATES=certificates()
OLD_PAIRS=[(tuple(map(int,k)),b) for k,b in R.verify_pairs().items()]
TRIPLES=[(t,b) for t,b,nums in P.SPECS]
EXTRA=[(t,b) for t,b,nums in SPECS]

@lru_cache(None)
def triangle_bound(root,triangle,level=2):
    assert 0<=root<10 and len(triangle)==len(set(triangle))==3 and root not in triangle
    assert all(0<=v<10 for v in triangle) and level in(0,1,2)
    best=sum((P.DEPTH[abs(v-root)] for v in triangle),F(0));reason=('depth',)
    if best<1:return best,reason
    ordered=OLD_PAIRS+(TRIPLES if level>=1 else [])+(EXTRA if level>=2 else [])
    for terms,b in ordered:
        for side in(-1,1):
            selected={root+side*j for j in terms}
            if selected<=set(triangle):
                value=b+sum((P.DEPTH[abs(v-root)] for v in set(triangle)-selected),F(0))
                if value<best:best=value;reason=('chain',side,terms)
                if value<1:return best,reason
    return best,reason

def triangulate(face,root,level=2):
    face=tuple(face);assert len(face)>=3 and root not in face
    @lru_cache(None)
    def solve(i,j):
        if j-i<2:return ()
        for k in range(i+1,j):
            tri=(face[i],face[k],face[j])
            if triangle_bound(root,tuple(sorted(tri)),level)[0]>=1:continue
            left,right=solve(i,k),solve(k,j)
            if left is not None and right is not None:return left+right+(tri,)
        return None
    return solve(0,len(face)-1)

def build():
    rows=[]
    for level in range(3):
        for root in range(10):
            triangles=list(combinations([v for v in range(10) if v!=root],3))
            bad=[t for t in triangles if triangle_bound(root,t,level)[0]>=1]
            gaps=[1-triangle_bound(root,t,level)[0] for t in triangles if t not in bad]
            rows.append({'level':level,'root':root,'uncertified_triangles':bad,
                         'certified_count':len(gaps),'minimum_gap':str(min(gaps))})
    assert [len(rows[20+i]['uncertified_triangles']) for i in range(10)]==[41,21,11,4,1,1,4,11,21,41]
    for level in range(3):
        for r in range(10):
            reflected={tuple(sorted(9-v for v in t)) for t in rows[level*10+r]['uncertified_triangles']}
            assert reflected==set(rows[level*10+9-r]['uncertified_triangles'])
    assert min(F(r['minimum_gap']) for r in rows if r['level']==2)==F(1,1000)
    return enc({'identity':'MINIMUM_PATH_PROJECTION_EXTRA_PAIRS_V1','certificates':CERTIFICATES,
                'level_screens':rows,'scope':'Only sufficient triangle bounds. Uncertified does not assert existence or impossibility.'})

def main():
    assert sys.argv[1:] in (['build'],['check'])
    b=build();p=HERE/'path_projection_extra.json'
    if sys.argv[1]=='check' or p.exists():assert p.read_bytes()==b
    else:p.write_bytes(b)
    print('PATH_PROJECTION_FIVE_EXTRA_PAIR_CERTIFICATES_PASS',5,38)
    print('PATH_PROJECTION_LEVEL_SCREENS_PASS',3,10,2520,*pin(b))
if __name__=='__main__':main()
