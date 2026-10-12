# material-cfdc14d700d7

AI research material

---

#!/usr/bin/env python3
"""ROOT_FOOT_QUADRATIC_ELIMINATION_AND_ACTUAL_HULL_GAP_V1.

Deterministic exact verification. Requires Python 3.13 and SymPy 1.14.0.
No input files, random seeds, floating arithmetic, external solvers, or downloads.

Run: python -B root_fibre_exact.py --output-dir OUT
The bounded-polytope routine is exhaustive, including singular stationary slices.
The physical countercontrols are not class110 bodies. The exclusion below is one
closed mixed-sign packet at one actual stable foot, not a complete E17 exclusion.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from itertools import combinations
from pathlib import Path
import sympy as sp

R=sp.Rational
FACETS=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),
        (9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
PACKET=(('Q6_7',-1),('P9_4',-1),('P0_1',1),('Q1_2',-1),('P6_0',-1))
COARSE_BOUNDS=((R(1,20),sp.S(231)),(-sp.S(222),sp.S(222)),
               (R(1,25),sp.S(213)),(R(1,10000),sp.S(3172)))
QH=sp.Matrix([[0,0,1,0],[0,-2,0,0],[1,0,0,0],[0,0,0,0]])
QL=sp.Matrix([0,0,0,-1])

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def pd(matrix: sp.Matrix) -> bool:
    return matrix==matrix.T and all(matrix[:k,:k].det()>0 for k in range(1,matrix.rows+1))

def primitive_row(row):
    """Positive rescaling to primitive integers; no integer division via float."""
    row=[sp.Rational(x) for x in row]
    denominator=sp.ilcm(*[x.q for x in row])
    nums=[int(x*denominator) for x in row]
    divisor=sp.igcd(*nums)
    if divisor==0:
        return [sp.S.Zero]*len(row)
    return [sp.Integer(x//divisor) for x in nums]

def box_rows(bounds):
    n=len(bounds);rows=[]
    for k,(lo,hi) in enumerate(bounds):
        v=[sp.S.Zero]*(n+1);v[k]=sp.S.One;v[-1]=-lo;rows.append(v)
        v=[sp.S.Zero]*(n+1);v[k]=-sp.S.One;v[-1]=hi;rows.append(v)
    return rows

def quadratic_extrema(rows, hessian=QH, linear=QL, constant=sp.S.Zero):
    """Exact min/max on a BOUNDED rational polyhedron, rows*x+constant>=0.

    The caller must establish boundedness. This program uses explicit boxes.
    Enumerate independent active rows I of size <=n. On their affine hull,
    stationarity is the rational linear system A_I*x=b_I,
    Z_I.T*(H*x+linear)=0. A nonempty bounded stationary slice has a vertex,
    obtained by adding n-rank(E_I) original active inequalities. Checking every
    such completion handles degeneracy without genericity or floating decisions.
    """
    if not rows:
        raise ValueError('Supply a bounded polyhedron with explicit rows.')
    n=len(rows[0])-1
    if any(len(r)!=n+1 for r in rows):
        raise ValueError('Inconsistent row dimensions.')
    H=sp.Matrix(hessian);ell=sp.Matrix(linear)
    if H.shape!=(n,n) or H!=H.T or ell.shape!=(n,1):
        raise ValueError('Invalid quadratic dimensions.')
    A=sp.Matrix([r[:n] for r in rows]);rhs=sp.Matrix([-r[n] for r in rows]);m=A.rows
    require(not (A.atoms(sp.Float)|rhs.atoms(sp.Float)|H.atoms(sp.Float)|ell.atoms(sp.Float)),
            'Exact inputs only.')
    points={}
    counts=dict(active_sets=0,stationary_affine_sets=0,point_tests=0,feasible_tests=0)
    def accept(x,I,J):
        counts['point_tests']+=1
        if any(z<0 for z in A*x-rhs):
            return
        counts['feasible_tests']+=1
        key=tuple(x)
        if key not in points:
            value=(x.T*H*x)[0]/2+(ell.T*x)[0]+constant
            points[key]=(value,tuple(I),tuple(J))
    def solve_affine(E,y):
        reduced,pivots=E.row_join(y).rref()
        if n in pivots:
            return None
        nr=len(pivots)
        return reduced[:nr,:n],reduced[:nr,n:n+1],nr
    for k in range(n+1):
        for I in combinations(range(m),k):
            counts['active_sets']+=1
            AI=A[list(I),:] if I else sp.zeros(0,n)
            if AI.rank()!=k:
                continue
            Z=sp.Matrix.hstack(*AI.nullspace()) if k<n else sp.zeros(n,0)
            E=AI.col_join(Z.T*H)
            y=rhs[list(I),:] if I else sp.zeros(0,1)
            y=y.col_join(-Z.T*ell)
            solution=solve_affine(E,y)
            if solution is None:
                continue
            ER,yr,rank=solution;counts['stationary_affine_sets']+=1
            if rank==n:
                accept(yr,I,())
                continue
            remaining=[j for j in range(m) if j not in I]
            for J in combinations(remaining,n-rank):
                EJ=ER.col_join(A[list(J),:]);yj=yr.col_join(rhs[list(J),:])
                completed=solve_affine(EJ,yj)
                if completed is not None and completed[2]==n:
                    accept(completed[1],I,J)
    counts['distinct_feasible_points']=len(points)
    if not points:
        return dict(empty=True,counts=counts)
    low=min(points.items(),key=lambda item:item[1][0])
    high=max(points.items(),key=lambda item:item[1][0])
    def pack(item):
        x,(value,I,J)=item
        return dict(value=value,point=x,active=I,completion=J)
    return dict(empty=False,minimum=pack(low),maximum=pack(high),counts=counts)

def build_geometry():
    # Unscaled H5 coordinates: x=1/10,r=9/10,p=3/25,q=3/5,rho=3/17.
    # They are NOT the compact lambda-scaled coordinates of another certificate.
    raw=[sp.Matrix(v) for v in [(R(1,4),0,0),(R(37,40),0,0),
        (R(22,25),R(3,25),0),(R(3,5),R(2,5),0),(0,R(13,40),0),
        (0,R(1,4),0),(R(1,16),R(1,16),0),(0,0,1),(R(3,17),0,1),(0,R(3,17),1)]]
    triangles=[(cyc[0],cyc[j],cyc[j+1]) for cyc in FACETS for j in range(1,len(cyc)-1)]
    require(len(triangles)==16,'Wrong boundary fan.')
    D=sp.S.Zero;J=sp.zeros(3,1);L=sp.zeros(3,3)
    for i,j,k in triangles:
        vs=[raw[i],raw[j],raw[k]];det=sp.Matrix.hstack(*vs).det()
        total=sum(vs,sp.zeros(3,1));D+=det;J+=det*total
        L+=det*(total*total.T+sum((v*v.T for v in vs),sp.zeros(3)))
    require(D>0,'Positive volume required.')
    centroid=J/(4*D);Sigma=L/(20*D)-centroid*centroid.T
    require(pd(Sigma),'Actual covariance must be positive definite.')
    xs=[v-centroid for v in raw];qs=[]
    for cyc in FACETS:
        q=sp.Matrix.vstack(*(xs[i].T for i in cyc[:3])).inv()*sp.ones(3,1)
        require(all(q.dot(xs[i])==1 for i in cyc),'Facet coplanarity failed.')
        require(all(q.dot(v)<1 for i,v in enumerate(xs) if i not in cyc),
                'True maximal facet support failed.')
        normal=(raw[cyc[1]]-raw[cyc[0]]).cross(raw[cyc[2]]-raw[cyc[1]])
        require(all(normal.dot((raw[cyc[(j+1)%len(cyc)]]-raw[cyc[j]]).cross(
            raw[cyc[(j+2)%len(cyc)]]-raw[cyc[(j+1)%len(cyc)]]))>0
            for j in range(len(cyc))),'Strict facet corner failed.')
        qs.append(q)
    edges=sorted(set(tuple(sorted((cyc[j],cyc[(j+1)%len(cyc)])))
                     for cyc in FACETS for j in range(len(cyc))))
    require(len(edges)==17 and len(raw)-len(edges)+len(FACETS)==2,'Wrong true lattice.')
    require(all(sum(i in cy and j in cy for cy in FACETS)==2 for i,j in edges),
            'Every true edge needs two maximal facets.')
    foot=sum((xs[i] for i in FACETS[2]),sp.zeros(3,1))/3
    H=sp.Matrix.hstack(xs[6]-xs[7],xs[0]-xs[7],foot)
    require(qs[2].T*H==sp.Matrix([[0,0,1]]),'Wrong root frame.')
    a,b,c,d=sp.symbols('a b c d');variables=(a,b,c,d);Hi=H.inv()
    M=Hi.T*sp.Matrix([[a,b,0],[b,c,0],[0,0,1]])*Hi
    Nlift=H*sp.Matrix([[c,-b,0],[-b,a,0],[0,0,d]])*H.T
    names=[];coeff=[]
    def add(name,expression):
        poly=sp.Poly(sp.expand(expression),variables)
        require(poly.total_degree()<=1,'A lifted mechanical row is not affine.')
        row=[poly.coeff_monomial(v) for v in variables]+[poly.coeff_monomial(1)]
        require(not any(v.has(sp.Float) for v in row),'Floating mechanical coefficient.')
        names.append(name);coeff.append(row)
    for i,j in edges:
        add(f'P{i}_{j}',(xs[i].T*M*(xs[j]-xs[i]))[0])
        add(f'P{j}_{i}',(xs[j].T*M*(xs[i]-xs[j]))[0])
        k,l=[f for f,cyc in enumerate(FACETS) if i in cyc and j in cyc]
        add(f'Q{k}_{l}',(qs[k].T*Nlift*(qs[l]-qs[k]))[0])
        add(f'Q{l}_{k}',(qs[l].T*Nlift*(qs[k]-qs[l]))[0])
    E=sp.Matrix(coeff);require(E.rows==68,'Missing true primitives.')
    Si=Sigma.inv();B=H.T*Si*H;S=B[:2,:2];K=sp.S(40)
    lower=1/(qs[2].dot(Sigma*qs[2]))
    upper=max(xs[i].dot(Si*xs[i]) for i in FACETS[2])
    amin=S[0,0]/(K*upper);amax=K*S[0,0]/lower
    cmin=S[1,1]/(K*upper);cmax=K*S[1,1]/lower;bmax=(amax+cmax)/2
    dmin=S.det()/(K*K*upper*upper);dmax=K*K*S.det()/(lower*lower)
    exact_bounds=((amin,amax),(-bmax,bmax),(cmin,cmax),(dmin,dmax))
    require(all(lo<elo and ehi<hi for (lo,hi),(elo,ehi) in zip(COARSE_BOUNDS,exact_bounds)),
            'Coarse box does not contain the proved facet-wide metric box.')
    return dict(raw=raw,xs=xs,qs=qs,edges=edges,centroid=centroid,Sigma=Sigma,
                volume=D/6,foot=foot,H=H,E=E,names=names,exact_bounds=exact_bounds,
                lower=lower,upper=upper)

def census(geo,M):
    require(pd(M),'Physical metric is not SPD.')
    xs=geo['xs'];qs=geo['qs'];N=M.inv();primal={};polar={};saddles=[];weak=[]
    for i,j in geo['edges']:
        primal[i,j]=(xs[i].T*M*(xs[j]-xs[i]))[0]
        primal[j,i]=(xs[j].T*M*(xs[i]-xs[j]))[0]
        k,l=[f for f,cyc in enumerate(FACETS) if i in cyc and j in cyc]
        polar[k,l]=(qs[k].T*N*(qs[l]-qs[k]))[0]
        polar[l,k]=(qs[l].T*N*(qs[k]-qs[l]))[0]
        values=(primal[i,j],primal[j,i],polar[k,l],polar[l,k])
        if all(v<0 for v in values):saddles.append((i,j))
        if all(v<=0 for v in values) and any(v==0 for v in values):weak.append((i,j))
    U=[i for i in range(10) if all(v<0 for (k,j),v in primal.items() if k==i)]
    S=[i for i in range(9) if all(v<0 for (k,j),v in polar.items() if k==i)]
    require(len(primal)==34 and len(polar)==34,'Incomplete census.')
    require(all(v!=0 for v in [*primal.values(),*polar.values()]),'Unexpected zero primitive.')
    require(len(S)+len(U)-len(saddles)==2,'Equilibrium Euler control failed.')
    return dict(stable=S,unstable=U,saddles=saddles,physical_weak=weak,
                primal={f'{i}_{j}':v for (i,j),v in primal.items()},
                polar={f'{i}_{j}':v for (i,j),v in polar.items()})

def regression_tests():
    standard=quadratic_extrema(box_rows(((1,2),(R(-1,2),R(1,2)),(1,2),(1,4))))
    require(standard['minimum']['value']==R(-13,4) and standard['maximum']['value']==3,
            'A stationary nonvertex extremum was missed.')
    # Lower-dimensional polytope: a=c=1, d=1/2, 0<=b<=1.
    algebraic=quadratic_extrema(box_rows(((1,1),(0,1),(1,1),(R(1,2),R(1,2)))))
    require(algebraic['minimum']['value']==R(-1,2) and algebraic['maximum']['value']==R(1,2),
            'Lower-dimensional extrema failed.')
    # Its physical point b=sqrt(2)/2 has determinant exactly d and degree two.
    require(sp.simplify(1-(sp.sqrt(2)/2)**2-R(1,2))==0,'Quadratic witness failed.')
    tangent=quadratic_extrema(box_rows(((1,1),(-1,1),(1,1),(1,1))))
    require(tangent['minimum']['value']==-1 and tangent['maximum']['value']==0,
            'An isolated tangent zero was missed.')
    flatH=sp.diag(0,2,0,0)
    flat=quadratic_extrema(box_rows(((1,2),(-1,1),(1,2),(1,2))),flatH,sp.zeros(4,1))
    require(flat['minimum']['value']==0 and flat['maximum']['value']==1,
            'A positive-dimensional stationary slice was missed.')
    bad=box_rows(((1,2),(-1,1),(1,2),(1,2)))+[[sp.S(-1),0,0,0,0]]
    empty=quadratic_extrema(bad)
    require(empty['empty'],'An empty bounded polyhedron was not detected.')
    return dict(standard=standard,algebraic=algebraic,tangent=tangent,flat=flat,empty=empty)

def verify():
    geo=build_geometry();H=geo['H'];Hi=H.inv();Sigma=geo['Sigma'];Si=Sigma.inv()
    E=geo['E'];names=geo['names']
    G=sp.Matrix([[R(513,100),R(533,100)],[R(533,100),R(156,25)]])
    independent_d=R(37,25);det=G.det();ratio=independent_d/det
    require(det==R(36023,10000) and ratio==R(14800,36023),'Wrong exact control.')
    M0=Hi.T*sp.diag(G,1)*Hi;M1=Hi.T*sp.diag(ratio*G,1)*Hi;N1=M1.inv()
    sample=sp.Matrix([G[0,0],G[0,1],G[1,1],independent_d,1])
    packet_rows=[];slacks={}
    for name,sign in PACKET:
        row=list(sign*E.row(names.index(name)));packet_rows.append(primitive_row(row))
        value=(sp.Matrix([row])*sample)[0];require(value>0,'Mixed packet is not strict.')
        slacks[name]=value
    require(all(lo<x<hi for x,(lo,hi) in zip(list(sample[:4]),COARSE_BOUNDS)),
            'Mixed point is outside the box.')
    require(M0*geo['foot']==geo['qs'][2] and N1*geo['qs'][2]==geo['foot'],
            'The two metrics do not share the exact physical root foot.')
    require(M0*N1!=sp.eye(3),'The mixed pair accidentally has a common inverse.')
    # Rational Loewner bounds certify both actual covariance condition numbers <5.
    for metric,t in ((M0,R(3,20)),(M1,R(3,40))):
        require(pd(metric-t*Si) and pd(5*t*Si-metric),'Condition<5 certificate failed.')
    A=M0/sp.trace(Sigma*M0);B=Si*N1*Si/sp.trace(Si*N1)
    reciprocal=(R(26,31)*Si-A-B,5*A+B-R(30,31)*Si,A+5*B-R(30,31)*Si)
    require(all(pd(matrix) for matrix in reciprocal),'Three-facet reciprocal hull test failed.')
    k=R(13,2);den=k*k+k+1
    outer_reciprocal=((k*k+1)/den*Si-A-B,k*A+B-k*(k+1)/den*Si,
                      A+k*B-k*(k+1)/den*Si)
    require(all(pd(matrix) for matrix in outer_reciprocal),'E17 outer reciprocal facets failed.')
    require(pd(A-Si/48) and pd(B-Si/48),'Normalized positive floors failed.')
    c0=census(geo,M0);c1=census(geo,M1)
    require((len(c0['stable']),len(c0['unstable']),len(c0['saddles']))==(6,6,10),
            'Wrong first physical class.')
    require((len(c1['stable']),len(c1['unstable']),len(c1['saddles']))==(7,7,12),
            'Wrong second physical class.')
    exact=quadratic_extrema(packet_rows+box_rows(COARSE_BOUNDS))
    require(not exact['empty'] and exact['minimum']['value']>R(1,2000),
            'The complete exact determinant exclusion failed.')
    require(exact['minimum']['active']==(0,1,2,3),'Unexpected minimizing vertex.')
    tests=regression_tests()
    return dict(identity='ROOT_FOOT_QUADRATIC_ELIMINATION_AND_ACTUAL_HULL_GAP_V1',
                geometry=dict(volume=geo['volume'],centroid=geo['centroid'],covariance=Sigma,
                    vertices=geo['raw'],facets=FACETS,edges=geo['edges'],foot=geo['foot'],frame=H),
                metric_box=dict(exact=geo['exact_bounds'],coarse=COARSE_BOUNDS,
                    minimum_foot_norm=geo['lower'],maximum_vertex_foot_norm=geo['upper']),
                control=dict(G=G,independent_d=independent_d,determinant=det,ratio=ratio,
                    metric0=M0,metric1=M1,packet_slacks=slacks,
                    reciprocal_leading_minors=[[X[:k,:k].det() for k in (1,2,3)] for X in reciprocal],
                    outer_reciprocal_leading_minors=[[X[:k,:k].det() for k in (1,2,3)]
                        for X in outer_reciprocal],
                    census0=c0,census1=c1),packet_rows=packet_rows,extrema=exact,tests=tests,
                limitations=['One closed mixed-sign packet at one actual root foot; no complete tree cover.',
                    'Exclusion uses a box guaranteed for hypothetical E17 jointS1U1 metrics by condition<40.',
                    'The two physical controls have classes (6,6,10) and (7,7,12), not110.',
                    'No full two-variable root-foot arrangement or whole E17 solve is claimed.'])

def encode(value):
    if isinstance(value,sp.MatrixBase):return value.tolist()
    if isinstance(value,sp.Basic):return str(value)
    raise TypeError(type(value).__name__)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir',type=Path,default=Path('.'))
    args=parser.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
    report=verify()
    data=(json.dumps(report,default=encode,sort_keys=True,indent=2)+'\n').encode()
    target=args.output_dir/'root_fibre_report.json';target.write_bytes(data)
    print('TRUE_LATTICE 10 17 9; ACTUAL_CENTROID_AND_COVARIANCE_PASS')
    print('COMMON_ROOT_FOOT; TWO_PHYSICAL_CONTROLS_6610_7712; ALL_68_PRIMITIVES_NONZERO')
    print('BOTH_ACTUAL_CONDITION_NUMBERS_LT_5; RECIPROCAL_FACETS_K5_AND_K13_2_STRICT; FLOORS_GT_1_48')
    print('EXACT_PACKET_QUADRATIC_MIN_GT_1_2000; ALL_1093_ACTIVE_SETS_CHECKED')
    print('LOWER_DIMENSIONAL_TANGENT_FLAT_AND_EMPTY_REGRESSIONS_PASS')
    print(f'root_fibre_report.json {len(data)} {hashlib.sha256(data).hexdigest()}')
    print('ROOT_FOOT_QUADRATIC_ELIMINATION_AND_ACTUAL_HULL_GAP_V1_PASS')

if __name__=='__main__':
    main()
