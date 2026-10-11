# material-4bdc0b4e413d

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

# WEAK_RADIAL_INDEX_TETRA_CONTROL_V1

Exact supplementary actual-body controls; not a computational proof of the general index theorem. Uniform tetrahedron vertices (1,0,0),(1,1,0),(1,0,1),(-3,-1,-1), M=I, actual volume centroid 0. There is ONE physical VF point at vertex0/face012, represented also on two weak edges. Strict counts are (3,3,4). Active tangent polar polygon at that point is conv{(0,0),(0,-4),(-4,0)}, so the descending directional link is the complement of the closed first-quadrant arc: one connected arc, index0. Four homogeneous rational perturbations have strict counts (4,4,6),(4,4,6),(3,3,4),(3,3,4), no weak contacts. They demonstrate both creation of S+U+2H and complete removal of the single VF; alternating contribution is zero.

Save the exact block as weak_index_control.py, UTF-8 LF with terminal newline. Python3.13.5 observed, standard library only, no input files or seeds; compatible Python3.11+.
Commands: python -B weak_index_control.py build ; python -B weak_index_control.py check
Expected marker: WEAK_RADIAL_INDEX_TETRA_CONTROL_PASS.
Source:4328 bytes SHA256 ddff549663bfef4e75649e06e66a91035065c22dec50eca410b82da8aaf1b946.
Output weak_index_control_report.json:16005 bytes SHA256 9f1a2bfd9f68be23b58b204276371c42921a279381215ece60aa5aa6ca976890.
Coordinator observed build PASS; separate check recorded after storage. The general theorem is analytic and does not rest on these examples.

```python
"""WEAK_RADIAL_INDEX_TETRA_CONTROL_V1. Python 3.11+, standard library only.
Run: python -B weak_index_control.py build ; python -B weak_index_control.py check
Exact geometric controls only; the general index theorem is proved separately.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib, json, sys

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(t,a): return tuple(t*x for x in a)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))

def census(raw):
    assert len(raw)==4
    v=[tuple(map(F,x)) for x in raw]
    g=mul(F(1,4),tuple(sum(x[k] for x in v) for k in range(3)))
    x=[sub(y,g) for y in v]
    vol=abs(det(sub(x[1],x[0]),sub(x[2],x[0]),sub(x[3],x[0])))/6
    assert vol>0 and all(t==0 for t in g)
    faces=list(combinations(range(4),3)); q=[]
    for face in faces:
        a,b,c=[x[i] for i in face]
        n=cross(sub(b,a),sub(c,a)); h=dot(n,a)
        assert h!=0
        p=mul(1/h,n)
        assert all(dot(p,z)<=1 for z in x)
        assert [i for i,z in enumerate(x) if dot(p,z)==1]==list(face)
        q.append(p)
    pp=[[dot(a,sub(b,a)) for b in x] for a in x]
    qq=[[dot(a,sub(b,a)) for b in q] for a in q]
    unstable=[i for i in range(4) if all(pp[i][j]<0 for j in range(4) if i!=j)]
    stable=[f for f in range(4) if all(qq[f][h]<0 for h in range(4) if f!=h)]
    weak_v=[i for i in range(4) if max(pp[i][j] for j in range(4) if i!=j)==0]
    weak_f=[f for f in range(4) if max(qq[f][h] for h in range(4) if f!=h)==0]
    saddles=[]; weak_edges=[]; edge_rows=[]
    for i,j in combinations(range(4),2):
        f,h=[f for f,face in enumerate(faces) if i in face and j in face]
        rows=[pp[i][j],pp[j][i],qq[f][h],qq[h][f]]
        edge_rows.append([[i,j],[f,h],[str(t) for t in rows]])
        if max(rows)<0: saddles.append([i,j])
        elif max(rows)==0: weak_edges.append([i,j])
    assert len(stable)+len(unstable)-len(saddles)==2
    return dict(vertices=[[str(t) for t in z] for z in x],faces=faces,
                volume=str(vol),centroid=[str(t) for t in g],poles=[[str(t) for t in z] for z in q],
                stable=stable,unstable=unstable,saddles=saddles,weak_vertices=weak_v,
                weak_facets=weak_f,weak_edges=weak_edges,edge_rows=edge_rows,
                counts=[len(stable),len(unstable),len(saddles)])

def main():
    if len(sys.argv)!=2 or sys.argv[1] not in ('build','check'):
        raise SystemExit('usage: python -B weak_index_control.py build|check')
    # At vertex 0 the supporting plane x=1 is the true face 012.
    # Thus this is a genuine own-volume-centred VF, not two physical points.
    vf=[(1,0,0),(1,1,0),(1,0,1),(-3,-1,-1)]
    controls={'VF':census(vf)}
    assert controls['VF']['weak_vertices']==[0]
    assert controls['VF']['weak_facets']==[0]
    assert controls['VF']['weak_edges']==[[0,1],[0,2]]
    poles=[tuple(map(F,row)) for row in controls['VF']['poles']]
    active=[poles[f] for f,face in enumerate(controls['VF']['faces']) if 0 in face]
    A=[(p[1],p[2]) for p in active]
    assert A==[(F(0),F(0)),(F(0),F(-4)),(F(-4),F(0))]
    # h_A(theta)=max(0,-4 theta_y,-4 theta_z). Its zero normal cone
    # is the first quadrant; the strict lower directional link is one arc.
    controls['VF']['active_tangent_polygon']=[[str(t) for t in a] for a in A]
    controls['VF']['weak_physical_count']=1
    controls['VF']['local_lower_link_components']=1
    controls['VF']['weak_index']=0
    for n in (-17,-3,3,17):
        e=F(n,1000)
        a=(F(1),e,2*e);b=(F(1),F(1),e);c=(F(1)+e,-e,F(1))
        d=mul(-1,add(add(a,b),c))
        controls['perturb_'+str(n)]=census([a,b,c,d])
    out=(json.dumps(controls,sort_keys=True,indent=2)+'\n').encode()
    p=Path('weak_index_control_report.json')
    if sys.argv[1]=='build':p.write_bytes(out)
    else:assert p.read_bytes()==out
    print('WEAK_RADIAL_INDEX_TETRA_CONTROL_PASS')
    for key,c in controls.items(): print(key,c['counts'],c['weak_vertices'],c['weak_facets'])
    for path in (Path(__file__),p):
        b=path.read_bytes();print(path.name,len(b),hashlib.sha256(b).hexdigest())
if __name__=='__main__':main()
```
