# material-569337ddefb6

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

#!/usr/bin/env python3
"""Exact volume-preserving centroid repair and quadratic design cells.
Python 3.10+; standard library only. The built-in example is NOT class 110.
Run: python centroid_cell.py --output centroid_cell.json
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import itertools
import json
from pathlib import Path

ZERO = (F(0), F(0), F(0))

def vec(x):
    if len(x) != 3:
        raise ValueError('A vector must have three coordinates')
    return tuple(F(t) for t in x)

def add(a, b): return tuple(x+y for x,y in zip(a,b))
def sub(a, b): return tuple(x-y for x,y in zip(a,b))
def mul(t, a): return tuple(t*x for x in a)
def dot(a, b): return sum((x*y for x,y in zip(a,b)), F(0))
def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def det(a, b, c): return dot(a, cross(b,c))

def mass(vertices, faces):
    """Signed volume and unnormalised first moment of a closed oriented mesh."""
    volume, moment = F(0), ZERO
    for ia, ib, ic in faces:
        a,b,c = vertices[ia],vertices[ib],vertices[ic]
        sixv = det(a,b,c)
        volume += sixv/6
        moment = add(moment, mul(sixv/24, add(add(a,b),c)))
    return volume, moment

def edge_map(faces):
    edges = {}
    for fi, face in enumerate(faces):
        for a,b in zip(face, face[1:]+face[:1]):
            edges.setdefault(tuple(sorted((a,b))), []).append((fi,a,b))
    return edges

def check_topology(vertices, faces):
    if len(set(vertices)) != len(vertices):
        raise ValueError('Repeated vertex')
    if len(set(tuple(sorted(f)) for f in faces)) != len(faces):
        raise ValueError('Repeated face')
    edges = edge_map(faces)
    for edge, uses in edges.items():
        if len(uses) != 2 or uses[0][1:] != uses[1][1:][::-1]:
            raise ValueError(f'Nonmanifold or inconsistent oriented edge {edge}')
    if len(vertices)-len(edges)+len(faces) != 2:
        raise ValueError('Euler characteristic differs from two')
    seen, todo = set(), [0]
    adj = {i:set() for i in range(len(vertices))}
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    while todo:
        a = todo.pop()
        if a not in seen:
            seen.add(a); todo.extend(adj[a]-seen)
    if len(seen) != len(vertices):
        raise ValueError('Disconnected mesh')
    return edges

def support_values(vertices, faces):
    result = {}
    for fi, (ia,ib,ic) in enumerate(faces):
        a,b,c = vertices[ia],vertices[ib],vertices[ic]
        n = cross(sub(b,a),sub(c,a))
        for j,p in enumerate(vertices):
            if j not in (ia,ib,ic):
                result[f'support:{fi}:{j}'] = -dot(n,sub(p,a))
    return result

def elementary_values(vertices, faces):
    """Support margins, directed radial margins, and face-edge margins."""
    result = support_values(vertices, faces)
    for a,b in edge_map(faces):
        result[f'radial:{a}:{b}'] = dot(vertices[a],sub(vertices[a],vertices[b]))
        result[f'radial:{b}:{a}'] = dot(vertices[b],sub(vertices[b],vertices[a]))
    for fi, face in enumerate(faces):
        a,b,c = (vertices[i] for i in face)
        n = cross(sub(b,a),sub(c,a))
        for i,j in zip(face,face[1:]+face[:1]):
            result[f'faceedge:{fi}:{i}:{j}'] = dot(n,cross(vertices[i],vertices[j]))
    return result

def check_strict_hull(vertices, faces):
    edges = check_topology(vertices, faces)
    margins = support_values(vertices, faces)
    if not margins or min(margins.values()) <= 0:
        raise ValueError('The specified triangles are not all strict supporting facets')
    for ia,ib,ic in faces:
        a,b,c = vertices[ia],vertices[ib],vertices[ic]
        if dot(cross(sub(b,a),sub(c,a)),a) <= 0:
            raise ValueError('The origin is not strictly inside')
    return len(vertices),len(edges),len(faces),min(margins.values())

def equilibria(vertices, faces):
    """Requires a strictly convex triangular mesh and volume centroid at zero."""
    check_strict_hull(vertices,faces)
    if mass(vertices,faces)[1] != ZERO:
        raise ValueError('Equilibria must be relative to the actual volume centroid')
    edges = edge_map(faces)
    values = elementary_values(vertices,faces)
    stable, unstable, saddle, weak_features = [],[],[],[]
    def classify(name, data, yes):
        if min(data) > 0: yes.append(name)
        elif min(data) == 0: weak_features.append(name)
    for fi, face in enumerate(faces):
        data = [values[f'faceedge:{fi}:{a}:{b}'] for a,b in zip(face,face[1:]+face[:1])]
        classify(f'face:{fi}',data,stable)
    for a in range(len(vertices)):
        data = [values[f'radial:{a}:{b if a==c else c}'] for c,b in edges if a in (c,b)]
        classify(f'vertex:{a}',data,unstable)
    for (a,b), uses in edges.items():
        data = [values[f'radial:{a}:{b}'],values[f'radial:{b}:{a}']]
        data += [values[f'faceedge:{fi}:{i}:{j}'] for fi,i,j in uses]
        classify(f'edge:{a}:{b}',data,saddle)
    return {'S':len(stable),'U':len(unstable),'H':len(saddle),
            'stable':stable,'unstable':unstable,'saddle':saddle,
            'weak_features':weak_features,
            'zero_elementary_margins':[k for k,v in values.items() if v==0]}

def star_pairs(vertex, faces):
    result = []
    for face in faces:
        if vertex in face:
            i = face.index(vertex)
            rotated = face[i:]+face[:i]
            result.append(rotated[1:])
    if not result:
        raise ValueError('Handle has an empty star')
    return result

def volume_normal(vertices, faces, vertex):
    out = ZERO
    for u,v in star_pairs(vertex,faces,):
        out = add(out,cross(vertices[u],vertices[v]))
    return out

def tangent_basis(a):
    if a == ZERO:
        raise ValueError('A nonzero volume gradient is required')
    pivot = next(i for i,x in enumerate(a) if x != 0)
    basis = []
    for j in range(3):
        if j != pivot:
            d = [F(0)]*3; d[j] = F(1); d[pivot] = -a[j]/a[pivot]
            basis.append(tuple(d))
    return basis

def moment_column(vertices, faces, vertex, direction):
    a = volume_normal(vertices,faces,vertex)
    if dot(a,direction) != 0:
        raise ValueError('Motion does not preserve volume exactly')
    p = vertices[vertex]
    out = ZERO
    for u,v in star_pairs(vertex,faces):
        q,r = vertices[u],vertices[v]
        b = cross(q,r)
        term = add(mul(dot(direction,b),add(add(p,q),r)),mul(dot(p,b),direction))
        out = add(out,mul(F(1,24),term))
    return out

def check_handles(vertices, faces, handles):
    ids = {i for i,d in handles}
    if any(len(ids.intersection(face)) > 1 for face in faces):
        raise ValueError('Two distinct movable vertices share a triangle')
    for i,d in handles:
        if dot(volume_normal(vertices,faces,i),d) != 0:
            raise ValueError('A direction is not volume-tangent')

def apply_handles(vertices, handles, parameters):
    if len(handles) != len(parameters):
        raise ValueError('Wrong parameter count')
    out = list(vertices)
    for (i,d),t in zip(handles,parameters):
        out[i] = add(out[i],mul(t,d))
    return out

def affine_solve(columns, rhs):
    """Return an exact particular solution and nullspace basis, with free variables zero."""
    n = len(columns)
    rows = [[columns[j][i] for j in range(n)]+[rhs[i]] for i in range(3)]
    pivots, r = [],0
    for c in range(n):
        found = next((k for k in range(r,3) if rows[k][c]),None)
        if found is None: continue
        rows[r],rows[found] = rows[found],rows[r]
        q = rows[r][c]; rows[r] = [x/q for x in rows[r]]
        for k in range(3):
            if k != r:
                q = rows[k][c]
                rows[k] = [x-q*y for x,y in zip(rows[k],rows[r])]
        pivots.append(c); r += 1
        if r==3: break
    if any(not any(row[:n]) and row[n] for row in rows):
        raise ValueError('Centroid residual is outside the handle response span')
    particular = [F(0)]*n
    for i,c in enumerate(pivots): particular[c] = rows[i][n]
    nullspace = []
    for free in (j for j in range(n) if j not in pivots):
        z = [F(0)]*n; z[free] = F(1)
        for i,c in enumerate(pivots): z[c] = -rows[i][free]
        nullspace.append(tuple(z))
    return tuple(particular),nullspace,len(pivots)

def design_family(vertices, faces, handles):
    check_handles(vertices,faces,handles)
    columns = [moment_column(vertices,faces,i,d) for i,d in handles]
    particular,nullspace,rank = affine_solve(columns,mul(-1,mass(vertices,faces)[1]))
    def instantiate(z):
        if len(z) != len(nullspace): raise ValueError('Wrong free dimension')
        x = list(particular)
        for t,basis in zip(z,nullspace): x = [a+t*b for a,b in zip(x,basis)]
        return apply_handles(vertices,handles,x)
    return instantiate,particular,nullspace,rank

def quadratic_tables(evaluate, dimension):
    """Exact polarization for maps whose entries have degree at most two."""
    zero = [F(0)]*dimension
    c = evaluate(zero)
    plus,minus = [],[]
    for i in range(dimension):
        x = zero.copy(); x[i]=F(1); plus.append(evaluate(x))
        x[i]=F(-1); minus.append(evaluate(x))
    tables = {}
    for key,value in c.items():
        tables[key] = {'constant':value,
                      'linear':[(plus[i][key]-minus[i][key])/2 for i in range(dimension)],
                      'quadratic':[[F(0)]*dimension for _ in range(dimension)]}
        for i in range(dimension):
            tables[key]['quadratic'][i][i]=(plus[i][key]+minus[i][key])/2-value
    for i in range(dimension):
        for j in range(i+1,dimension):
            x=zero.copy();x[i]=x[j]=F(1);v=evaluate(x)
            for key in c:
                tables[key]['quadratic'][i][j]=v[key]-plus[i][key]-plus[j][key]+c[key]
    return tables

def eval_quadratic(table, z):
    return (table['constant']+sum((a*b for a,b in zip(table['linear'],z)),F(0))
            +sum((table['quadratic'][i][j]*z[i]*z[j] for i in range(len(z)) for j in range(i,len(z))),F(0)))

def safe_box_margin(tables, center, radius):
    """Certify all elementary signs on center+[-radius,radius]^dimension.
    A positive result is sufficient; a nonpositive result is inconclusive.
    """
    if radius < 0: raise ValueError('Radius must be nonnegative')
    dimension = len(center)
    bounds = []
    for key,table in tables.items():
        value = eval_quadratic(table,center)
        q = table['quadratic']
        gradient = [table['linear'][j]+2*q[j][j]*center[j]
                    +sum((q[i][j]*center[i] for i in range(j)),F(0))
                    +sum((q[j][i]*center[i] for i in range(j+1,dimension)),F(0))
                    for j in range(dimension)]
        lower = (abs(value)-radius*sum(map(abs,gradient))
                 -radius**2*sum(abs(q[i][j]) for i in range(dimension) for j in range(i,dimension)))
        bounds.append((lower,key))
    if not bounds: raise ValueError('No polynomial constraints supplied')
    return min(bounds)

def make_example():
    core = [vec(x) for x in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]
    vertices = core+[mul(F(-1,2),p) for p in core]
    faces = []
    for omitted in range(4):
        tri = [i for i in range(4) if i != omitted]
        a,b,c = (core[i] for i in tri)
        if dot(cross(sub(b,a),sub(c,a)),a) < 0: tri[1],tri[2] = tri[2],tri[1]
        for a,b in zip(tri,tri[1:]+tri[:1]): faces.append((a,b,4+omitted))
    vertices[4] = add(vertices[4],vec([F(1,100),F(2,100),F(-3,100)]))
    return vertices,faces

def serialise(value):
    if isinstance(value,F): return str(value)
    if isinstance(value,dict): return {str(k):serialise(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)): return [serialise(v) for v in value]
    return value

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',default='centroid_cell.json')
    args=parser.parse_args()
    vertices,faces = make_example()
    check_strict_hull(vertices,faces)
    initial_volume,initial_moment = mass(vertices,faces)
    handles = [(i,d) for i in (5,6,7) for d in tangent_basis(volume_normal(vertices,faces,i))]
    instantiate,particular,nullspace,rank = design_family(vertices,faces,handles)
    d=len(nullspace)
    if rank != 3 or d != 3: raise AssertionError('Unexpected response rank/free dimension')
    # Pick a small nonsymmetric rational point in the exact centroid-zero affine family.
    free = [F(1,1000),F(-2,1000),F(3,1000)]
    corrected = instantiate(free)
    counts = check_strict_hull(corrected,faces)
    volume,moment = mass(corrected,faces)
    if volume != initial_volume or moment != ZERO:
        raise AssertionError('Exact mass identities failed')
    eq = equilibria(corrected,faces)
    if eq['weak_features']: raise AssertionError('Example has a weak equilibrium')
    if eq['S']+eq['U']-eq['H'] != 2: raise AssertionError('Equilibrium Euler relation failed')
    tables = quadratic_tables(lambda z:elementary_values(instantiate(z),faces),d)
    # Exact polynomial identity checks at a deterministic rational grid, including
    # points outside the hull chamber: the polynomial identity does not need convexity.
    checks = 0
    for grid in itertools.product([-2,0,1,3],repeat=d):
        z=[F(x,7) for x in grid]
        actual=elementary_values(instantiate(z),faces)
        for key,value in actual.items():
            if value != eval_quadratic(tables[key],z):
                raise AssertionError('Quadratic identity failed: '+key)
            checks += 1
        if mass(instantiate(z),faces) != (initial_volume,ZERO):
            raise AssertionError('Affine mass identity failed off chamber')
    box_radius = F(1,32)
    box_margin,box_limiting_key = safe_box_margin(tables,free,box_radius)
    if box_margin <= 0: raise AssertionError('Strict-sign box certificate failed')
    output={'claim':'Method demonstration only; not a class-110 construction.',
            'vertices_input':vertices,'faces_outward':faces,'handles':handles,
            'initial_volume':initial_volume,'initial_moment':initial_moment,
            'response_rank':rank,'particular_parameters':particular,'nullspace_basis':nullspace,
            'selected_free_parameters':free,'vertices_centroid_zero':corrected,
            'verified_volume':volume,'verified_first_moment':moment,
            'V':counts[0],'E':counts[1],'F':counts[2],'C':2*counts[1],
            'minimum_support_margin':counts[3],'equilibria':eq,
            'quadratic_identity_checks':checks,'quadratic_tables':tables,
            'certified_box_radius':box_radius,'certified_box_margin':box_margin,
            'certified_box_limiting_key':box_limiting_key}
    Path(args.output).write_text(json.dumps(serialise(output),sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print('EXACT_VOLUME_PRESERVED',volume)
    print('EXACT_FIRST_MOMENT_ZERO',moment)
    print('STRICT_CONVEX_HULL',counts[:3])
    print('EQUILIBRIA_S_U_H',eq['S'],eq['U'],eq['H'])
    print('WEAK_FEATURES',len(eq['weak_features']))
    print('QUADRATIC_IDENTITY_CHECKS',checks)
    print('STRICT_SIGN_BOX_RADIUS',box_radius,'MARGIN',box_margin)
    print('CENTROID_CELL_SELFTEST_PASS')

if __name__=='__main__': main()
