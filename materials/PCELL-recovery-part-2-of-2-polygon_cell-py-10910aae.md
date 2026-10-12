# material-10910aae6d82

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

#!/usr/bin/env python3
"""Exact polygonal-facet design cells and a local planarity obstruction.
Requires the canonical centroid_cell.py from the CCELL recovery package.
Python 3.10+, standard library only. This is NOT a class-110 construction.
Run: python polygon_cell.py --output polygon_cell.json
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import itertools
import json
from pathlib import Path
import centroid_cell as c


def validate_incidence(vertices, polygons, references, triangles):
    """Check a closed oriented polygon mesh and its specified triangulation."""
    if len(polygons) != len(references):
        raise ValueError('Every polygon requires one reference triangle')
    if any(len(face) < 3 or len(set(face)) != len(face) for face in polygons):
        raise ValueError('A polygon has fewer than three distinct vertices')
    if set().union(*(set(f) for f in polygons)) != set(range(len(vertices))):
        raise ValueError('Vertex list and face incidence disagree')
    edges = c.edge_map(polygons)
    if len(vertices)-len(edges)+len(polygons) != 2:
        raise ValueError('Polygonal Euler characteristic is not two')
    for edge, uses in edges.items():
        if len(uses) != 2 or uses[0][1:] != uses[1][1:][::-1]:
            raise ValueError('Inconsistent or nonmanifold geometric edge: '+str(edge))
    for i,face in enumerate(polygons):
        if not set(references[i]).issubset(face) or len(set(references[i])) != 3:
            raise ValueError('Invalid reference triangle')
        for other in polygons[i+1:]:
            common = set(face).intersection(other)
            if len(common) > 2:
                raise ValueError('Two geometric faces share more than an edge')
            if len(common) == 2:
                a,b = common
                for cycle in (face,other):
                    k=cycle.index(a)
                    if cycle[(k-1)%len(cycle)]!=b and cycle[(k+1)%len(cycle)]!=b:
                        raise ValueError('Face intersection is not a boundary edge')
    # Vertex links must be single cycles, not pinched surfaces.
    for vertex in range(len(vertices)):
        link={}
        for face in polygons:
            if vertex in face:
                k=face.index(vertex); a=face[k-1]; b=face[(k+1)%len(face)]
                link.setdefault(a,[]).append(b); link.setdefault(b,[]).append(a)
        if not link or any(len(x)!=2 for x in link.values()):
            raise ValueError('Non-circular vertex link')
        seen=set(); todo=[next(iter(link))]
        while todo:
            x=todo.pop()
            if x not in seen:
                seen.add(x); todo.extend(link[x])
        if len(seen)!=len(link): raise ValueError('Disconnected vertex link')
    c.check_topology(vertices,triangles)
    # Every triangle belongs to exactly one polygon, with matching outer boundary.
    grouped=[[] for _ in polygons]
    for tri in triangles:
        owners=[i for i,f in enumerate(polygons) if set(tri).issubset(f)]
        if len(owners)!=1: raise ValueError('Ambiguous triangulation owner')
        grouped[owners[0]].append(tri)
    for face,patch in zip(polygons,grouped):
        if len(patch)!=len(face)-2: raise ValueError('Wrong triangle count in polygon')
        outer=[]
        for edge,uses in c.edge_map(patch).items():
            if len(uses)==1: outer.append(uses[0][1:])
            elif len(uses)!=2 or uses[0][1:]!=uses[1][1:][::-1]:
                raise ValueError('Bad internal diagonal incidence')
        if set(outer)!=set(zip(face,face[1:]+face[:1])):
            raise ValueError('Triangulation boundary differs from geometric face')
    return edges


def polygon_values(vertices, polygons, references):
    """Equality and inequality polynomials, without counting auxiliary diagonals."""
    equalities={}; inequalities={}
    for fi,(face,ref) in enumerate(zip(polygons,references)):
        a,b,d=(vertices[i] for i in ref)
        n=c.cross(c.sub(b,a),c.sub(d,a))
        inequalities[f'normal:{fi}']=c.dot(n,n)
        inequalities[f'interior:{fi}']=c.dot(n,a)
        for j,p in enumerate(vertices):
            side=c.dot(n,c.sub(p,a))
            if j in face and j not in ref: equalities[f'plane:{fi}:{j}']=side
            elif j not in face: inequalities[f'support:{fi}:{j}']=-side
        for i,j in zip(face,face[1:]+face[:1]):
            inequalities[f'faceedge:{fi}:{i}:{j}']=c.dot(n,c.cross(vertices[i],vertices[j]))
    for i,j in c.edge_map(polygons):
        inequalities[f'radial:{i}:{j}']=c.dot(vertices[i],c.sub(vertices[i],vertices[j]))
        inequalities[f'radial:{j}:{i}']=c.dot(vertices[j],c.sub(vertices[j],vertices[i]))
    return equalities,inequalities


def check_polygon_body(vertices, polygons, references, triangles):
    edges=validate_incidence(vertices,polygons,references,triangles)
    eq,ineq=polygon_values(vertices,polygons,references)
    if any(eq.values()): raise ValueError('A geometric face is not planar')
    geom=[v for k,v in ineq.items() if not k.startswith(('radial:','faceedge:'))]
    if not geom or min(geom)<=0: raise ValueError('Non-strict polygonal supporting geometry')
    volume,moment=c.mass(vertices,triangles)
    if volume<=0 or moment!=c.ZERO: raise ValueError('Not a positive-volume own-centred body')
    stable=[];unstable=[];saddle=[];weak=[]
    def classify(name,values,out):
        if min(values)>0:out.append(name)
        elif min(values)==0:weak.append(name)
    for fi,face in enumerate(polygons):
        vals=[ineq[f'faceedge:{fi}:{a}:{b}'] for a,b in zip(face,face[1:]+face[:1])]
        classify(f'face:{fi}',vals,stable)
    for a in range(len(vertices)):
        vals=[ineq[f'radial:{a}:{b if a==i else i}'] for i,b in edges if a in (i,b)]
        classify(f'vertex:{a}',vals,unstable)
    for (a,b),uses in edges.items():
        vals=[ineq[f'radial:{a}:{b}'],ineq[f'radial:{b}:{a}']]
        vals += [ineq[f'faceedge:{fi}:{i}:{j}'] for fi,i,j in uses]
        classify(f'edge:{a}:{b}',vals,saddle)
    return {'V':len(vertices),'E':len(edges),'F':len(polygons),
            'volume':volume,'moment':moment,'S':len(stable),'U':len(unstable),'H':len(saddle),
            'stable':stable,'unstable':unstable,'saddle':saddle,'weak_features':weak,
            'minimum_geometric_margin':min(geom),
            'zero_equilibrium_margins':[k for k,v in ineq.items()
                                       if k.startswith(('radial:','faceedge:')) and not v]}


def cube_fixture():
    core=[c.vec(x) for x in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]
    vertices=core+[c.mul(-1,p) for p in core]
    polygons=[]; references=[]; triangles=[]
    for axis in range(3):
        for sign in [-1,1]:
            ids=[i for i,p in enumerate(vertices) if p[axis]==sign]
            a,b=[i for i in ids if i>=4]
            p,q=[i for i in ids if i<4]
            patch=[(a,p,b),(a,b,q)]
            for j,tri in enumerate(patch):
                x,y,z=(vertices[i] for i in tri)
                if c.dot(c.cross(c.sub(y,x),c.sub(z,x)),x)<0:
                    patch[j]=(tri[0],tri[2],tri[1])
            boundary={use[0][1]:use[0][2] for use in c.edge_map(patch).values() if len(use)==1}
            cycle=[min(ids)]
            for _ in range(3):cycle.append(boundary[cycle[-1]])
            if boundary[cycle[-1]]!=cycle[0]:raise AssertionError('Cube face is not a cycle')
            polygons.append(tuple(cycle));references.append(patch[0]);triangles.extend(patch)
    return vertices,polygons,references,triangles


def rank(matrix):
    rows=[list(r) for r in matrix]; height=len(rows); width=len(rows[0]); pivot=0
    for j in range(width):
        found=next((i for i in range(pivot,height) if rows[i][j]),None)
        if found is None:continue
        rows[pivot],rows[found]=rows[found],rows[pivot]
        q=rows[pivot][j];rows[pivot]=[v/q for v in rows[pivot]]
        for i in range(height):
            if i!=pivot:
                q=rows[i][j];rows[i]=[a-q*b for a,b in zip(rows[i],rows[pivot])]
        pivot+=1
        if pivot==height:break
    return pivot


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',default='polygon_cell.json')
    args=parser.parse_args()
    vertices,polygons,refs,triangles=cube_fixture()
    fixture=check_polygon_body(vertices,polygons,refs,triangles)
    assert (fixture['S'],fixture['U'],fixture['H'])==(6,8,12)
    assert not fixture['weak_features'] and not fixture['zero_equilibrium_margins']
    handles=[(i,d) for i in range(4) for d in c.tangent_basis(c.volume_normal(vertices,triangles,i))]
    instantiate,particular,nullspace,response_rank=c.design_family(vertices,triangles,handles)
    expected=[(1,-1,-1,1,0,0,0,0),(0,0,-1,0,1,0,0,0),
              (0,-1,0,0,0,1,0,0),(-1,0,0,0,0,0,1,0),(1,-1,-1,0,0,0,0,1)]
    assert nullspace==expected and particular==(F(0),)*8 and response_rank==3
    def evaluate(z):
        eq,ineq=polygon_values(instantiate(z),polygons,refs)
        return dict(eq,**ineq)
    tables=c.quadratic_tables(evaluate,5)
    plane_keys=[next(k for k in tables if k.startswith(f'plane:{i}:')) for i in range(6)]
    jacobian=[tables[k]['linear'] for k in plane_keys]
    jacobian_rank=rank(jacobian)
    assert jacobian_rank==2
    kernel=[(-1,1,1,0,0),(0,1,0,1,0),(0,-1,0,0,1)]
    assert all(not sum(a*b for a,b in zip(row,vec)) for row in jacobian for vec in kernel)
    # Exact coefficient identities prove the reduced quadratic obstruction.
    # Transformed parameters are (a,b,u,v,w); z=(a-u,u+v-w-b,u,v,w).
    def transform(t):
        a,b,u,v,w=t
        return (a-u,u+v-w-b,u,v,w)
    def actual_forms(t):
        values=evaluate(transform(t))
        return {'F0':values[plane_keys[0]]/4,'F4':values[plane_keys[4]]/4,
                'Q':sum(values[plane_keys[i]] for i in (0,2,4))/4}
    def claimed_forms(t):
        a,b,u,v,w=t
        return {'F0':b*(1-v+w)+(v-w)**2,
                'F4':-a*(1+u)+u*u,
                'Q':u*u+v*v+(v-w)**2+a*(v-u)+b*(w-2*v)}
    assert c.quadratic_tables(actual_forms,5)==c.quadratic_tables(claimed_forms,5)
    checks=0
    for grid in itertools.product([-1,0,2],repeat=5):
        z=tuple(F(x,7) for x in grid)
        values=evaluate(z)
        for key,value in values.items():
            assert value==c.eval_quadratic(tables[key],z),key
            checks+=1
        assert c.mass(instantiate(z),triangles)==(F(8),c.ZERO)
    r=F(1,10)
    coeff_u=1-2*r/(1-r);coeff_diff=1-3*r/(1-2*r)
    assert (coeff_u,coeff_diff)==(F(7,9),F(5,8))
    # From F0=F4=0 in |u|,|v|,|w|<=r we obtain
    # a=u^2/(1+u), b=-(v-w)^2/(1-v+w), hence
    # Q >= (7/9)u^2+v^2+(5/8)(v-w)^2.  Q=0 forces z=0.
    output={'claim':'Method and local obstruction only; not a class-110 candidate search.',
            'vertices':vertices,'geometric_faces':polygons,'reference_triangles':refs,
            'integration_triangles':triangles,'fixture':fixture,'handles':handles,
            'response_rank':response_rank,'particular':particular,'nullspace':nullspace,
            'coplanarity_jacobian':jacobian,'coplanarity_rank':jacobian_rank,
            'tangent_kernel':kernel,'quadratic_tables':tables,'identity_checks':checks,
            'isolation_parameter_bound':r,'positive_lower_coefficients':[coeff_u,F(1),coeff_diff]}
    Path(args.output).write_text(json.dumps(c.serialise(output),sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print('POLYGON_GEOMETRIC_EDGES',fixture['E'],'NOT_INTEGRATION_EDGES',len(c.edge_map(triangles)))
    print('POLYGON_FIXTURE_S_U_H',fixture['S'],fixture['U'],fixture['H'])
    print('EXACT_CENTROID_RESPONSE_RANK',response_rank,'FREE_DIMENSION',len(nullspace))
    print('COPLANARITY_JACOBIAN_RANK',jacobian_rank,'TANGENT_DIMENSION',5-jacobian_rank)
    print('QUADRATIC_IDENTITY_CHECKS',checks)
    print('EXACT_LOCAL_ISOLATION_BOUND',r,'LOWER_COEFFICIENTS',coeff_u,F(1),coeff_diff)
    print('POLYGON_CELL_PLANARITY_OBSTRUCTION_PASS')

if __name__=='__main__':main()
