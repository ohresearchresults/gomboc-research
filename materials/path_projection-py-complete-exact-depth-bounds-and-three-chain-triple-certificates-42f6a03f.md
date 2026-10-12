# material-42f6a03f6756

AI research material

---

"""Exact path projection bounds for ten vertices. Python 3.8+, standard library.
Run with assertions enabled: python -S path_projection.py build|check.
The pinned central_root.py supplies the original three pair certificates.
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
PIN=(6759,'c0fa7d4662c6863efb88ac356e3518a82cbac40bea2fda838be416797868ccaf')
def pin(b):return (len(b),hashlib.sha256(b).hexdigest())
def enc(a):return (json.dumps(a,sort_keys=True,separators=(',',':'))+'\n').encode()
assert pin((HERE/'central_root.py').read_bytes())==PIN
import central_root as R

DEPTH={1:F(0),2:F(1,8),3:F(1,4),4:F(7,20),5:F(27,64),
       6:F(49,100),7:F(17,32),8:F(23,40),9:F(61,100)}
SPECS=(
 ((3,4,6),F(19,20),(1562474,2587775,4285883,4063368,2302766,2416557)),
 ((3,5,6),F(999,1000),(1582616,2508946,3977473,3665265,4170128,2271006)),
 ((2,5,6),F(3,4),(1529122,3127519,3513362,4004822,4565028,2489135)),
)
DENOMINATOR=1000000

def exact_certificates():
    # Polynomial root isolation and rational power bounds used in the proof.
    t=F(901,500)
    assert t>F(5,3) and t**3-t*t-2*t+1==F(32201,125000000)>0
    assert F(49,100)-F(901,1000)**7>0
    assert F(99,70)**2>2 and F(17,32)-(17+12*F(99,70))/64==F(1,2240)>0
    c=F(47,50)
    assert c*c>F(3,4) and 8*c**3-6*c-1==F(73,15625)>0
    assert F(23,40)-c**9>0
    assert F(161,72)**2>5 and F(61,100)-((5+F(161,72))/8)**5>0
    pair=R.verify_pairs()
    bounds={tuple(map(int,k)):v for k,v in pair.items()}
    records=[]
    for terms,B,ints in SPECS:
        q=[[F(0) for _ in range(7)] for _ in range(7)];q[0][0]=B
        for j in terms:q[0][j]+=F(1,2);q[j][0]+=F(1,2)
        for j,a in enumerate(ints,1):
            a=F(a,DENOMINATOR);assert a>0
            q[j][j]+=a;q[j][j-1]-=a/2;q[j-1][j]-=a/2
        order=tuple(range(1,7))+(0,)
        pivots=R.ldl([[q[i][j] for j in order] for i in order])
        assert all(v>0 for v in pivots)
        # We deliberately keep the simpler rational B, not B minus the final pivot.
        bounds[terms]=B
        records.append({'depths':terms,'B':str(B),'lambda_numerators':ints,
                        'denominator':DENOMINATOR,'pivots':list(map(str,pivots))})
    assert len(bounds)==6
    return bounds,records

BOUNDS,CERTIFICATES=exact_certificates()

@lru_cache(None)
def triangle_bound(root,triangle,strong=True):
    assert 0<=root<10 and len(triangle)==3 and len(set(triangle))==3
    assert root not in triangle and all(0<=v<10 for v in triangle)
    best=sum((DEPTH[abs(v-root)] for v in triangle),F(0));reason=('depth',)
    for terms,b in BOUNDS.items():
        if len(terms)==3 and not strong:continue
        for side in(-1,1):
            vertices=tuple(root+side*j for j in terms)
            if set(vertices)<=set(triangle):
                other=set(triangle)-set(vertices)
                value=b+sum((DEPTH[abs(v-root)] for v in other),F(0))
                if value<best:best=value;reason=('chain',side,terms)
    return best,reason

def positive_triangulation(face,root,strong=True):
    face=tuple(face);assert len(face)>=3 and root not in face
    @lru_cache(None)
    def solve(i,j):
        if j-i<2:return ()
        for k in range(i+1,j):
            tri=(face[i],face[k],face[j])
            if triangle_bound(root,tuple(sorted(tri)),strong)[0]>=1:continue
            left,right=solve(i,k),solve(k,j)
            if left is not None and right is not None:return left+right+(tri,)
        return None
    return solve(0,len(face)-1)

def verify_triangulation(face,triangles):
    assert len(triangles)==len(face)-2
    positions={v:i for i,v in enumerate(face)}
    assert len(positions)==len(face)
    counts=Counter()
    for tri in triangles:
        assert len(set(tri))==3 and set(tri)<=set(face)
        for j,a in enumerate(tri):counts[tuple(sorted((a,tri[(j+1)%3])))]+=1
    boundary={tuple(sorted((v,face[(i+1)%len(face)]))) for i,v in enumerate(face)}
    assert {e for e,n in counts.items() if n==1}==boundary
    assert all(n==(1 if e in boundary else 2) for e,n in counts.items())
    diagonals=[tuple(sorted((positions[a],positions[b]))) for (a,b),n in counts.items() if n==2]
    for (a,b),(c,d) in combinations(diagonals,2):
        assert not(a<c<b<d or c<a<d<b)

def build():
    roots=[]
    for root in range(10):
        triples=list(combinations([v for v in range(10) if v!=root],3))
        bad=[t for t in triples if triangle_bound(root,t)[0]>=1]
        good=[t for t in triples if t not in bad]
        roots.append({'root':root,'uncertified_triangles':bad,
                      'certified_count':len(good),
                      'minimum_gap':str(min(1-triangle_bound(root,t)[0] for t in good))})
    assert roots[3]['uncertified_triangles']==[(0,7,9),(0,8,9),(1,8,9),(7,8,9)]
    assert roots[6]['uncertified_triangles']==[(0,1,2),(0,1,8),(0,1,9),(0,2,9)]
    assert roots[4]['uncertified_triangles']==[(0,8,9)]
    assert roots[5]['uncertified_triangles']==[(0,1,9)]
    for root in range(10):
        reflected={tuple(sorted(9-v for v in t)) for t in roots[root]['uncertified_triangles']}
        assert reflected==set(roots[9-root]['uncertified_triangles'])
    return enc({'identity':'MINIMUM_PATH_PROJECTION_TRIANGLES_V1','central_source_pin':PIN,
                'depth_bounds':{k:str(v) for k,v in DEPTH.items()},
                'new_certificates':CERTIFICATES,'root_screens':roots,
                'scope':'Weak path arrows at the actual uniform-volume centroid, one SPD metric. Triangle screen is sufficient only; no numerical failure proves impossibility.'})

def main():
    assert sys.argv[1:] in (['build'],['check'])
    b=build();p=HERE/'path_projection.json'
    if sys.argv[1]=='check' or p.exists():assert p.read_bytes()==b
    else:p.write_bytes(b)
    print('PATH_PROJECTION_EXACT_THREE_TRIPLE_CERTIFICATES_PASS',3,21)
    print('PATH_PROJECTION_TEN_ROOT_TRIANGLE_SCREENS_PASS',10,840)
    print('PATH_PROJECTION_RECOVERY_PIN',*pin(b))
if __name__=='__main__':main()
