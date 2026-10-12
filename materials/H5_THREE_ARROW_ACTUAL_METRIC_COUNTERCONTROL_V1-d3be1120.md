# material-d3be1120e707

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# H5_THREE_ARROW_ACTUAL_METRIC_COUNTERCONTROL_V1

## Exact finding and scope
For the literal H5 body with x=r=p=q=1/10 and s=1/4 (lambda=3/4), the positive definite integer metric
M=((248,-34,22),(-34,5,-3),(22,-3,2))
has leading principal minors (248,84,4). The body has ten distinct vertices and exactly the nine stated supporting facets, all other vertex/plane incidences strict. Its actual uniform centroid is
(2556781/13264640,2556781/13264640,27163/41452), with 6V=10363/12800.

For the three literal original arrows T=((1,8),(7,0),(9,4)), the quantities (zi-g)^T M(zj-zi) are respectively
209823287/212234240,
18438549/21223424,
1940447493/2122342400,
all strictly positive. Consequently no nonnegative weighting of these three arrows can yield a positive definite reverse-arrow stress at this point. This is a genuine actual-centred support obstruction, not a failed Bernstein coefficient or floating-point near miss.

The same metric has exactly two strict unstable vertices, labels 4 and 8. Therefore this is NOT a full rooted-tree survivor and NOT a class110 attaining body. In particular, a full rooted tree toward vertex 8 would need an outgoing arrow from vertex 4, which this metric forbids. The selected quotient support erased this basal obstruction. Extending the large-taper method to lambda=3/4 may require retaining additional original arrows or choosing different supports, not merely refining the same three-arrow weight search.

## Recovery inputs and commands
The geometry/moment module is the complete runnable source `h5_collar_weighted.py` preserved in material `[internal-source-reference]` (source 9389 bytes, SHA-256 18d63fc0ed4267051d54e63e780554d042d92d44a38bd445b14effe066c4ac7d). Supply that complete material with this one for descendants requiring computation.

Save the complete block below as `verify_h5_three_arrow_control.py`. No other data files are needed. Run `python verify_h5_three_arrow_control.py` in the same directory as `h5_collar_weighted.py`. Source 2401 bytes, SHA-256 21fa6ee21ebb7c1d9a75b0214dc0a695de94e7fb1a6eb3cfd31188ec50500a7d. Output `h5_three_arrow_control_report.json`: 954 bytes, SHA-256 15be0b9cf1d598143faa64461dcd5a4123df099bd4161bf1c709253cfb6033d9. Expected verdict PASS, strict_unstable_vertices [4,8]. Executed by coordinator with Python 3.13.5, NumPy 2.3.5 imported through the geometry module. The verifier uses only exact integers/Fractions. The literal metric was obtained from a numerical SDP outer-approximation proposal and then rounded and certified; neither the numerical optimizer nor its workspace is needed to recover or prove this exact object.

```python
"""Exact genuine-H5 obstruction to extending one three-arrow stress support."""
from fractions import Fraction as F
from math import prod
from pathlib import Path
import json
from h5_collar_weighted import exact_geometry, FACETS, EDGES, minors

POINT=(F(1,10),F(1,10),F(1,10),F(1,10),F(1,10),F(1,4))
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
