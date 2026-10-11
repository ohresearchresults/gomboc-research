# material-ec5704534ad4

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Exact common-projection PSD barrier for root3 triangles079 and789.
python -S common_two_barrier_compact.py build|check; standard library only.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys
if not __debug__:raise RuntimeError('Assertions must be enabled')
HERE=Path(__file__).resolve().parent
PARENT=(1,2,3,3,3,4,5,6,7,8)
TETS=((3,0,7,9),(3,7,8,9))
UPPER=(
((1967771,1967771,576375,-2270087,-3295638,-2842815,-1581201,-190029,446236,912560),
(3308086,3308086,868770,-2126758,-3358301,-3031954,-1756662,-982428,-270261),
(5738496,5738496,1418175,-1885702,-3423192,-3251712,-2784007,-2146659),
(10000000,6548380,2064025,-1584940,-3461707,-3870038,-3833754),
(6548380,4315410,1384101,-1048741,-1994027,-2564557),
(4315410,2851552,884169,-89962,-861537),
(2851552,1856883,1194687,551092),
(1856883,1633411,1299292),(1633411,1474656),(1474656,)),
((992431,992431,766997,302391,-370619,-688846,-669597,-405817,-228798,-87991),
(1656589,1656589,1028687,-316060,-1086921,-1223553,-876998,-603139,-358168),
(2645463,2645463,888617,-566767,-1325870,-1367511,-1210350,-984102),
(3971075,2600113,808311,-638768,-1370951,-1528684,-1505892),
(2600113,1701989,533151,-422990,-800411,-1016156),
(1701989,1118436,342763,-48702,-346214),
(1118436,726467,459704,210763),
(726467,635149,504896),(635149,574121),(574121,)))

def enc(x):return(json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def pin(b):return(len(b),hashlib.sha256(b).hexdigest())

def ldl(a):
    n=len(a);lower=[[F(i==j) for j in range(n)] for i in range(n)];d=[]
    assert all(a[i][j]==a[j][i] for i in range(n) for j in range(n))
    for j in range(n):
        pivot=a[j][j]-sum((lower[j][k]**2*d[k] for k in range(j)),F(0));assert pivot>0;d.append(pivot)
        for i in range(j+1,n):lower[i][j]=(a[i][j]-sum((lower[i][k]*lower[j][k]*d[k] for k in range(j)),F(0)))/pivot
    assert all(a[i][j]==sum((lower[i][k]*d[k]*lower[j][k] for k in range(n)),F(0)) for i in range(n) for j in range(n))
    return d

def rank(a):
    a=[[F(x) for x in row] for row in a];r=0;pivots=[]
    for j in range(len(a[0])):
        k=next((k for k in range(r,len(a)) if a[k][j]),None)
        if k is None:continue
        a[k],a[r]=a[r],a[k];v=a[r][j];a[r]=[x/v for x in a[r]]
        for i in range(r+1,len(a)):
            if a[i][j]:v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[r])]
        pivots.append(j);r+=1
    return r,pivots

def build():
    h=[];tails=[i for i in range(10) if i!=3]
    for block in UPPER:
        assert len(block)==10 and all(len(row)==10-i for i,row in enumerate(block))
        h.append([[block[min(i,j)][abs(i-j)] for j in range(10)] for i in range(10)])
    pivots=[list(map(str,ldl(a))) for a in h]
    arrows=[[a[i][i]-a[i][PARENT[i]] for i in tails] for a in h];assert arrows==[[0]*9]*2
    cancellation=[sum(h[k][i][j] for k in range(2) for j in TETS[k]) for i in range(10)];assert cancellation==[0]*10
    # Full coefficient map of 2Q_k=2Sym(a,c_k)+2sum(lambda_ki G_i).
    # The same ten coefficients a occur in both blocks; the multipliers are separate.
    equations=[]
    for k,tet in enumerate(TETS):
        c=[int(i in tet) for i in range(10)]
        for i in range(10):
            for j in range(i,10):
                row=[0]*28;row[i]+=c[j];row[j]+=c[i]
                for z,tail in enumerate(tails):
                    if i==j==tail:row[10+9*k+z]+=2
                    elif {i,j}=={tail,PARENT[tail]}:row[10+9*k+z]-=1
                equations.append(row)
    r,cols=rank(equations);assert r==28 and cols==list(range(28))
    return enc({'identity':'COMMON_079_789_COMPACT_PSD_BARRIER_V1','parent':PARENT,'tets':TETS,
                'positive_definite_dual_matrices':h,'positive_ldl_pivots':pivots,
                'arrow_traces':arrows,'common_coefficient_cancellation':cancellation,
                'coefficient_map_rank':r,'coefficient_map_pivot_columns':cols,
                'scope':'Any two PSD matrices of this common-a quadratic path-arrow ansatz must be zero, hence a and all multipliers are zero. No restriction on multiplier signs is needed. This is a method barrier, not an actual-body realization or geometric exclusion.'})
def main():
    assert sys.argv[1:] in (['build'],['check'])
    b=build();p=HERE/'common_two_barrier_compact.json'
    if sys.argv[1]=='check' or p.exists():assert p.read_bytes()==b
    else:p.write_bytes(b)
    print('COMMON_079_789_COMPACT_PSD_BARRIER_EXACT_PASS',2,20,28,*pin(b))
if __name__=='__main__':main()
