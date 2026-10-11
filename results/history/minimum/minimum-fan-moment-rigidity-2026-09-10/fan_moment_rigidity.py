"""FAN_MOMENT_RIGIDITY_AND_FULL_TENSOR_COUNTERCONTROL_V2.
CPython 3.13.5, standard library; exact integer arithmetic, no random input.
Run: python -S fan_moment_rigidity.py
This finite audit illustrates the analytic theorem; it is not a C32 exclusion.
Coordinates are uncentred. The theorem is affine invariant and has no metric input.
"""
from itertools import combinations
from pathlib import Path
from math import comb, gcd, lcm
from fractions import Fraction as F
import hashlib
import json
assert __debug__
PRIME = 1000000007
FIXTURES = {
    'MP9_45': [[5,2,-6],[5,5,-6],[2,5,-6],[0,0,0],[12,0,0],
               [0,12,0],[2,5,6],[5,2,6],[5,5,6]],
    'C32_nonsimplicial': [[192,0,0],[0,192,0],[0,0,192],[48,48,-192],
                        [3,0,0],[0,3,0],[0,0,12],[3,3,-12],[80,80,-67]],
    'octahedron': [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]],
    'cube': [[x,y,z] for x in (-1,1) for y in (-1,1) for z in (-1,1)]
}
MP45 = {frozenset(map(int,s)) for s in
        '014 021 032 043 125 154 235 347 365 376 458 487 568 678'.split()}

def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])

def volume6(p,t):
    a,b,c,d = (p[i] for i in t)
    return dot(sub(b,a),cross(sub(c,a),sub(d,a)))

def hull(p):
    n = len(p)
    facets = set()
    for i,j,k in combinations(range(n),3):
        normal = cross(sub(p[j],p[i]),sub(p[k],p[i]))
        if not any(normal):
            continue
        slacks = [dot(normal,sub(v,p[i])) for v in p]
        if min(slacks)<0<max(slacks) or not any(slacks):
            continue
        facets.add(tuple(a for a in range(n) if slacks[a]==0))
    facets = sorted(facets)
    edges = set()
    for f,g in combinations(facets,2):
        e = set(f)&set(g)
        assert len(e)<=2
        if len(e)==2:
            edges.add(tuple(sorted(e)))
    assert n-len(edges)+len(facets)==2
    assert set().union(*map(set,facets))==set(range(n))
    centre_n = [sum(v[k] for v in p) for k in range(3)]
    cycles = []
    for f in facets:
        adj = {i:sorted(j for j in f if tuple(sorted((i,j))) in edges) for i in f}
        assert all(len(a)==2 for a in adj.values())
        q = [min(f),adj[min(f)][0]]
        while True:
            j = next(j for j in adj[q[-1]] if j!=q[-2])
            if j==q[0]:
                break
            assert j not in q
            q.append(j)
        assert set(q)==set(f)
        normal = cross(sub(p[q[1]],p[q[0]]),sub(p[q[2]],p[q[0]]))
        inward = dot(normal,sub(centre_n,[n*a for a in p[q[0]]]))
        assert inward!=0
        if inward>0:
            q = [q[0]]+q[:0:-1]
        cycles.append(q)
    return cycles,sorted(edges)

def fans(p,facets):
    triangles = [(f[0],f[j],f[j+1]) for f in facets for j in range(1,len(f)-1)]
    result = []
    zero_occurrences = 0
    for a in range(len(p)):
        fan = set()
        for tri in triangles:
            if a in tri:
                continue
            z = volume6(p,(a,)+tri)
            assert z>=0
            if z==0:
                zero_occurrences += 1
            else:
                fan.add(tuple(sorted((a,)+tri)))
        result.append(sorted(fan))
    cells = sorted(set().union(*(set(f) for f in result)))
    sizes = [sum(abs(volume6(p,t)) for t in f) for f in result]
    assert sizes[0]>0 and len(set(sizes))==1
    return result,cells,zero_occurrences,sizes[0]

def complement_polynomial(p,t):
    # product_(j not in t) (1 - p_j . z), total degree <= n-4.
    out = {(0,0,0):1}
    for j,x in enumerate(p):
        if j in t:
            continue
        new = dict(out)
        for e,c in out.items():
            for k in range(3):
                if x[k]:
                    f = list(e)
                    f[k] += 1
                    f = tuple(f)
                    new[f] = new.get(f,0)-c*x[k]
        out = {e:c for e,c in new.items() if c}
    return out

def rank_mod(rows,ncols):
    basis = {}
    selected = []
    for ordinal,row in enumerate(rows):
        r = [v%PRIME for v in row]
        for j in sorted(basis):
            v = r[j]
            if v:
                q = basis[j]
                for k in range(j,ncols):
                    r[k] = (r[k]-v*q[k])%PRIME
        j = next((j for j,v in enumerate(r) if v),None)
        if j is None:
            continue
        c = pow(r[j],-1,PRIME)
        basis[j] = [v*c%PRIME for v in r]
        selected.append(ordinal)
    return len(basis),selected,sorted(basis)

def audit(name,p):
    f,e = hull(p)
    if name=='MP9_45':
        assert set(map(frozenset,f))==MP45 and len(e)==21
    if name=='C32_nonsimplicial':
        assert len(f)==9 and len(e)==16
    fs,cells,zeros,total = fans(p,f)
    d = [abs(volume6(p,t)) for t in cells]
    assert min(d)>0
    polys = [complement_polynomial(p,t) for t in cells]
    degree = len(p)-4
    monomials = sorted({(a,b,c) for a in range(degree+1)
                        for b in range(degree+1-a) for c in range(degree+1-a-b)},
                       key=lambda q:(sum(q),q))
    assert len(monomials)==comb(degree+3,3)
    fan_sets = list(map(set,fs))
    rows = []
    row_labels = []
    for a in range(1,len(p)):
        beta = [int(t in fan_sets[a])-int(t in fan_sets[0]) for t in cells]
        for m in monomials:
            row = [beta[j]*polys[j].get(m,0) for j in range(len(cells))]
            assert dot(row,d)==0
            rows.append(row)
            row_labels.append([a,list(m)])
    ranks = []
    for k in range(degree+1):
        subset = [r for r,lab in zip(rows,row_labels) if sum(lab[1])<=k]
        rank,_,_ = rank_mod(subset,len(cells))
        ranks.append(rank)
    rank,pivot_rows,pivot_columns = rank_mod(rows,len(cells))
    assert rank==len(cells)-1
    # A nonzero modular minor proves this exact integer rank lower bound.
    assert len(pivot_rows)==len(pivot_columns)==rank
    # Actual nonzero d in the kernel proves the matching exact upper bound.
    numerator = {}
    for a in range(len(p)):
        poly = {}
        for j,t in enumerate(cells):
            if t not in fan_sets[a]:
                continue
            for m,v in polys[j].items():
                poly[m] = poly.get(m,0)+d[j]*v
        poly = {m:v for m,v in poly.items() if v}
        if a:
            assert poly==numerator
        else:
            numerator = poly
    return dict(name=name,vertices=p,facets=f,edges=e,cells=cells,apex_fans=fs,
                cofacial_zero_occurrences_omitted=zeros,actual_six_volumes=d,
                six_volume_of_body=total,degree=degree,
                monomials=len(monomials),matrix_rows=len(rows),
                rank_lower_bounds_by_degree=ranks,exact_full_rank=rank,
                modular_prime=PRIME,pivot_rows=pivot_rows,pivot_columns=pivot_columns,
                numerator=[[list(m),v] for m,v in sorted(numerator.items())],
                mass_rigidity_only_no_equilibrium_exclusion=True)

def rational_kernel(A):
    a = [list(map(F,row)) for row in A]
    n = len(a[0])
    rank = 0
    pivots = []
    for j in range(n):
        k = next((i for i in range(rank,len(a)) if a[i][j]),None)
        if k is None:
            continue
        a[k],a[rank] = a[rank],a[k]
        q = a[rank][j]
        a[rank] = [v/q for v in a[rank]]
        for i in range(len(a)):
            if i!=rank and a[i][j]:
                q = a[i][j]
                a[i] = [v-q*w for v,w in zip(a[i],a[rank])]
        pivots.append(j)
        rank += 1
        if rank==len(a):
            break
    out = []
    for j in range(n):
        if j in pivots:
            continue
        v = [F(0)]*n
        v[j] = F(1)
        for i,k in enumerate(pivots):
            v[k] = -a[i][j]
        den = lcm(*(x.denominator for x in v))
        w = [int(x*den) for x in v]
        g = gcd(*w)
        w = [x//g for x in w]
        if next(x for x in w if x)<0:
            w = [-x for x in w]
        assert all(dot(row,w)==0 for row in A)
        out.append(w)
    return out

def cube_countercontrol():
    p = FIXTURES['cube']
    facets,edges = hull(p)
    triangles = [(f[0],f[j],f[j+1]) for f in facets for j in range(1,len(f)-1)]
    # Keep formal cofacial tetrahedra in the chain complex, imposing their mass=0.
    cells = sorted({tuple(sorted((a,)+tri)) for a in range(8)
                    for tri in triangles if a not in tri})
    triples = list(combinations(range(8),3))
    index = {t:i for i,t in enumerate(triples)}
    boundary = [[0]*len(cells) for t in triples]
    for j,t in enumerate(cells):
        for k in range(4):
            boundary[index[t[:k]+t[k+1:]]][j] = (-1)**k
    cycles = rational_kernel(boundary)
    assert len(cells)==42 and len(cycles)==9
    d = [volume6(p,t) for t in cells]  # Signed for canonical tuple orientation.
    zeros = [j for j,v in enumerate(d) if v==0]
    assert len(zeros)==6
    polys = [complement_polynomial(p,t) for t in cells]
    monomials = sorted({(a,b,c) for a in range(5) for b in range(5-a)
                       for c in range(5-a-b)},key=lambda q:(sum(q),q))
    zero_rows = [[int(i==j) for i in range(len(cells))] for j in zeros]
    cycle_rows = {}
    for degree in (2,3,4):
        rows = [[beta[j]*polys[j].get(m,0) for j in range(len(cells))]
                for beta in cycles for m in monomials if sum(m)<=degree]
        assert all(dot(row,d)==0 for row in rows)
        cycle_rows[degree] = rows
    L2 = cycle_rows[2]+zero_rows
    assert len(rational_kernel(L2))==2
    # Pin actual volume, first moments AND all six second tensor components of fan0.
    fs,nonflat,_,total = fans(p,facets)
    selected = set(fs[0])
    fan0 = [int(t in selected)*(1 if d[j]>0 else -1) for j,t in enumerate(cells)]
    reference_rows = [[fan0[j]*polys[j].get(m,0) for j in range(len(cells))]
                      for m in monomials if sum(m)<=2]
    kernel = rational_kernel(L2+reference_rows)
    assert len(kernel)==1
    h = kernel[0]
    assert all(h[j]==0 for j in zeros)
    epsilon = min(F(abs(d[j]),2*abs(h[j])) for j in range(len(cells)) if h[j])
    fake = [F(v)+epsilon*h[j] for j,v in enumerate(d)]
    assert fake!=list(map(F,d))
    assert all(fake[j]==0 for j in zeros)
    assert all(fake[j]*d[j]>0 for j in range(len(cells)) if d[j])
    assert all(dot(row,h)==0 for row in L2+reference_rows)
    assert dot(fan0,fake)==dot(fan0,d)==total
    violations = [[i,dot(row,h)] for i,row in enumerate(cycle_rows[3]) if dot(row,h)]
    assert violations
    for fan in fs:
        selected = set(fan)
        sign = [int(t in selected)*(1 if d[j]>0 else -1) for j,t in enumerate(cells)]
        for m in monomials:
            if sum(m)<=2:
                assert sum(sign[j]*h[j]*polys[j].get(m,0) for j in range(len(cells)))==0
    ranks = {k:rank_mod(cycle_rows[k]+zero_rows,len(cells))[0] for k in (2,3,4)}
    assert ranks=={2:40,3:41,4:41}
    return dict(vertices=p,facets=facets,cells=cells,boundary_cycles=cycles,
                formal_cells=42,nonflat_cells=36,zero_cells=zeros,
                boundary_rank=33,cycle_dimension=9,
                signed_actual_six_volumes=d,perturbation=h,epsilon=str(epsilon),
                signed_counterfeit_six_volumes=[str(x) for x in fake],
                full_tensor_cycle_ranks_including_zero_constraints=ranks,
                nonzero_third_degree_cycle_responses=violations,
                all_fan_volume_centroid_full_covariance_preserved=True,
                homogeneous_realization_of_counterfeit_masses=False)

def main():
    reports = [audit(name,p) for name,p in FIXTURES.items()]
    for r in reports:
        print(r['name'],len(r['cells']),r['cofacial_zero_occurrences_omitted'],
              r['rank_lower_bounds_by_degree'],r['exact_full_rank'])
    raw = (json.dumps(dict(identity='FAN_MOMENT_RIGIDITY_AND_FULL_TENSOR_COUNTERCONTROL_V2',
                          fixtures=reports,cube_full_tensor_countercontrol=cube_countercontrol()),sort_keys=True,separators=(',',':'))+'\n').encode()
    Path('fan_moment_rigidity.json').write_bytes(raw)
    print('ALL_INTEGER_FAN_NUMERATOR_IDENTITIES_AND_RANK_CHECKS_PASS')
    print('CUBE_FULL_CYCLE_DEGREE_TWO_POSITIVE_COUNTERFEIT_ACTUAL_ALL_FAN_COVARIANCE_PASS')
    print('CUBE_THIRD_DEGREE_DETECTS_COUNTERFEIT_PASS')
    print('DEGREE_N_MINUS_4_MASS_RIGIDITY_ILLUSTRATIONS_NOT_C32_EXCLUSIONS')
    print('fan_moment_rigidity.json',len(raw),hashlib.sha256(raw).hexdigest())
if __name__=='__main__':
    main()
