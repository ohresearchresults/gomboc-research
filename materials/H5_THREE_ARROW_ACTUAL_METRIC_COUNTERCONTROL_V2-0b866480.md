# material-0b8664800305

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# H5_THREE_ARROW_ACTUAL_METRIC_COUNTERCONTROL_V2 — corrected complete recovery

This replaces the source code in `[internal-source-reference]`. That first transport mistakenly repeated F(1,10) five times in POINT instead of four, so its code did not match the stated source hash and must not be executed or supplied as the canonical recovery. Its mathematical statement and literal metric were correct. This complete replacement uses POINT=(F(1,10),)*4+(F(1,4),), has been executed, and reproduces the same exact report. The object itself has not changed.

## Exact result
For the literal H5 body with x=r=p=q=1/10 and s=1/4 (lambda=3/4), let
M=((248,-34,22),(-34,5,-3),(22,-3,2)).
Its leading principal minors are (248,84,4)>0. All ten vertices are distinct; exactly the nine specified facets are supporting, with all nonincident inequalities strict. The true uniform centroid is (2556781/13264640,2556781/13264640,27163/41452); 6V=10363/12800.

For T=((1,8),(7,0),(9,4)), the original-arrow derivatives (zi-g)^T M(zj-zi) are respectively 209823287/212234240, 18438549/21223424, 1940447493/2122342400, all strictly positive. Thus no nonnegative weighting of these three arrows can be a positive definite reverse-arrow stress at this point. This is a genuine actual-centred support obstruction, not a failed coefficient test.

Exactly vertices 4 and 8 are strict unstable vertices. This is NOT a complete rooted-cone survivor and NOT a class110 object. A rooted tree toward 8 would need an outgoing arrow from 4, forbidden by this metric. The quotient discarded that basal information; extension to lambda=3/4 may need additional original arrows or different supports.

## Recovery
The complete geometry module `h5_collar_weighted.py` is preserved in `[internal-source-reference]`: 9389 bytes, SHA-256 18d63fc0ed4267051d54e63e780554d042d92d44a38bd445b14effe066c4ac7d. Supply that material together with this one for computational descendants.

Save this complete block as `verify_h5_three_arrow_control.py` beside the geometry module. Run `python verify_h5_three_arrow_control.py`. Source: 2383 bytes, SHA-256 79fe6cabefbfed07b7876f1658d0da5079c7136f3d83ce29cf874e55060b5441. Output `h5_three_arrow_control_report.json`: 954 bytes, SHA-256 15be0b9cf1d598143faa64461dcd5a4123df099bd4161bf1c709253cfb6033d9. Expected PASS and strict_unstable_vertices [4,8]. Executed with Python 3.13.5; NumPy 2.3.5 is imported by the geometry module but all witness verification uses exact integers/Fractions. The numerical proposal is not needed to reconstruct or verify the complete literal metric.

```python
"""Exact genuine-H5 obstruction to extending one three-arrow stress support."""
from fractions import Fraction as F
from math import prod
from pathlib import Path
import json
from h5_collar_weighted import exact_geometry, FACETS, EDGES, minors

POINT=(F(1,10),)*4+(F(1,4),)
M=((248,-34,22),(-34,5,-3),(22,-3,2))
SUPPORT=((1,8),(7,0),(9,4))

def evaluate(p):
    return sum((c*prod(t**k for t,k in zip(POINT,e)) for e,c in p.items()),F(0))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def metric(a,b):return sum(a[i]*M[i][j]*b[j] for i in range(3) for j in range(3))

def main():
    zp,dp,kp=exact_geometry();z=[tuple(evaluate(t) for t in v) for v in zp]
    D=evaluate(dp);K=tuple(evaluate(t) for t in kp);g=tuple(t/D for t in K)
    assert D>0 and len(set(z))==10
    # Verify the entire stated face incidence and strict supporting inequalities.
    for f in FACETS:
        a,b,c=[z[i] for i in f[:3]];normal=cross(sub(b,a),sub(c,a))
        assert normal!=(0,0,0)
        for i in range(10):
            h=dot(normal,sub(z[i],a))
            assert h==0 if i in f else h<0
    leading=minors((M[0][0],M[0][1],M[0][2],M[1][1],M[1][2],M[2][2]))
    assert leading==(248,84,4)
    arrow=lambda i,j:metric(sub(z[i],g),sub(z[j],z[i]))
    vals=[arrow(i,j) for i,j in SUPPORT]
    assert min(vals)>0
    assert vals==[F(209823287,212234240),F(18438549,21223424),F(1940447493,2122342400)]
    unstable=[i for i in range(10) if all(arrow(i,a+b-i)<0 for a,b in EDGES if i in (a,b))]
    assert unstable==[4,8]
    report={'identity':'H5_THREE_ARROW_ACTUAL_METRIC_COUNTERCONTROL_V1','verdict':'PASS',
            'point_x_r_p_q_s':[str(t) for t in POINT],'D_equals_6V':str(D),'own_centroid':[str(t) for t in g],
            'metric':M,'metric_leading_minors':leading,'support':SUPPORT,
            'positive_original_arrow_values':[str(t) for t in vals],'strict_unstable_vertices':unstable,
            'scope':'No nonnegative weights on these three arrows can form a PD stress at this genuine actual-centred H5 point. Not a full rooted-cone survivor or a class110 body.'}
    Path('h5_three_arrow_control_report.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
```
