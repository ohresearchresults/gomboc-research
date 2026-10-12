# material-331b7473f484

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

"""Every whole facet for EVERY concave three-affine-piece homothetic profile.
CPython3.13.5/SymPy1.14.0; assertions on; no external input or helper.
The two complete five-parameter charts include all nonnegative end heights.
All rational Bernstein controls are regenerated, checked and written exactly.
Analytical planar input: [internal-source-reference]. Actual facet mergers
use the accepted whole-two-piece theorem, never summed fragment estimates.
"""
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
import math,json,hashlib,itertools
import sympy as S
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
Q=S.Rational

def clean(v):return S.factor(S.cancel(v))
def matzero(v):assert v.applyfunc(clean)==S.zeros(*v.shape),v

def positive_semidefinite(matrix):
    matrix=matrix.applyfunc(clean)
    minors={str(ids):clean(matrix.extract(ids,ids).det())
            for k in range(1,matrix.rows+1) for ids in itertools.combinations(range(matrix.rows),k)}
    assert all(v>=0 for v in minors.values()),minors
    return minors

R,a,b,x,l,y=ring('a,b,x,l,y',QQ)

def F(n,j,H0,H1):
    return sum(QQ(math.comb(n,k)*math.factorial(k+j)*math.factorial(n-k),math.factorial(n+j+1))*H0**(n-k)*H1**k for k in range(n+1))

def setup(chart):
    B=b+1;Q=b+x;L=B*l if chart=='bulged' else B+a*(1-x)*l;T=B*x*y
    intervals=[]
    for k in range(3):
        row={}
        for n,j in [(2,0),(2,1),(2,2),(4,0),(3,0),(1,0),(1,1),(1,2)]:
            if k==0:val=(-1)**j*a**(j+1)*F(n,j,B,L)
            elif k==1:val=F(n,j,B,Q)
            else:val=b*sum(math.comb(j,i)*b**i*F(n,i,Q,T) for i in range(j+1))
            row[n,j]=val
        intervals.append(row)
    V=sum(p[2,0] for p in intervals);M=sum(p[2,1] for p in intervals);E=sum(p[2,2] for p in intervals);N=sum(p[4,0] for p in intervals)
    dn=[a*B*V+(B-L)*M,B*V+(x-1)*M,((b+1)*Q-T)*V+(T-Q)*M]
    return intervals,V,M,E,N,dn,L,T

def gate(chart,idx,name):
    rows,V,M,E,N,dn,L,T=setup(chart)
    if idx=='cap':
        Z=(M+a*V) if name.startswith('L') else (1+b)*V-M
        h=L if name.startswith('L') else T
        return QQ(3,2)*V*N-Z*h**4 if name.endswith('t') else QQ(3,2)*V**2*(V*E-M*M)-Z**3*h**2
    idx=int(idx);p=rows[idx];D=dn[idx];length=[a,R.one,b][idx]
    H=length*V*N-D*p[3,0]
    if name=='H':return H
    Z1=V*p[2,1]-M*p[2,0]
    Z2=V*V*p[1,2]-2*V*M*p[1,1]+M*M*p[1,0]
    RR=QQ(9,4)*length*V**2*(V*E-M*M)-D*Z2
    if name=='R':return RR
    if name=='D':return H*RR-D*D*Z1*Z1
    raise ValueError(name)

def certify(poly,chart,idx,name,output):
    blocks=defaultdict(dict)
    for key,v in poly.items():
        blocks[key[:2]][key[2:]]=Fraction(int(v.numerator),int(v.denominator))
    count=zeros=0;minimum=None;metadata=[]
    for ab,power_data in sorted(blocks.items()):
        deg=tuple(max(key[i] for key in power_data) for i in range(3))
        data=power_data
        # Degrees are fixed for the ENTIRE (a,b)-coefficient before conversion.
        # Each axis conversion uses the exact power-to-Bernstein identity.
        for axis in range(3):
            groups=defaultdict(dict)
            for key,v in data.items():groups[key[:axis]+key[axis+1:]][key[axis]]=v
            new={};n=deg[axis]
            weights=[[Fraction(math.comb(k,j),math.comb(n,j)) for j in range(k+1)] for k in range(n+1)]
            for other,vals in groups.items():
                for k in range(n+1):
                    value=sum(v*weights[k][j] for j,v in vals.items() if j<=k)
                    new[other[:axis]+(k,)+other[axis:]]=value
            data=new
        order=list(itertools.product(*(range(n+1) for n in deg)))
        assert set(data)==set(order)
        controls=[data[key] for key in order]
        assert all(v>=0 for v in controls),(chart,idx,name,ab,min(controls))
        count+=len(controls);zz=sum(v==0 for v in controls);zeros+=zz
        mm=min(controls);minimum=mm if minimum is None else min(minimum,mm)
        # Compact JSONL still contains EVERY literal regenerated coefficient.
        line=dict(chart=chart,piece=idx,gate=name,a_power=ab[0],b_power=ab[1],
                  unit_variables=['x','l','y'],degrees=deg,
                  order='lexicographic x,l,y (y fastest)',controls=list(map(str,controls)))
        output.write((json.dumps(line,sort_keys=True,separators=(',',':'))+'\n').encode())
        metadata.append(dict(a_power=ab[0],b_power=ab[1],degrees=deg,controls=len(controls),zeros=zz))
    return dict(chart=chart,piece=idx,gate=name,original_monomials=len(poly),blocks=metadata,
                controls=count,zeros=zeros,negative=0,minimum=str(minimum))

def polygon_moments(points):
    area=S.S.Zero;first=S.zeros(2,1);second=S.zeros(2)
    for aa,bb in zip(points,points[1:]+points[:1]):
        det=S.det(S.Matrix.hstack(aa,bb));area+=det/2;first+=det*(aa+bb)/6
        ss=aa+bb;second+=det*(ss*ss.T+aa*aa.T+bb*bb.T)/24
    assert area>0
    g=(first/area).applyfunc(clean);cov=(second/area-g*g.T).applyfunc(clean)
    assert cov.det()>0
    return area,g,cov

def positive_definite(matrix):
    matrix=matrix.applyfunc(clean)
    minors={str(ids):clean(matrix.extract(ids,ids).det())
            for k in range(1,matrix.rows+1) for ids in itertools.combinations(range(matrix.rows),k)}
    assert all(v>0 for v in minors.values()),minors
    return minors

def exact_polytope(vertices,cycles):
    interior=sum(vertices,S.zeros(3,1))/len(vertices) # orientation ONLY, never the mass centre
    faces=[]
    for old in cycles:
        f=list(old);aa,bb,cc=[vertices[i] for i in f[:3]];n=(bb-aa).cross(cc-aa)
        assert n.dot(n)>0
        if n.dot(aa-interior)<0:f.reverse()
        aa,bb,cc=[vertices[i] for i in f[:3]];n=(bb-aa).cross(cc-aa)
        assert n.dot(aa-interior)>0
        for j,v in enumerate(vertices):
            value=clean(n.dot(v-aa));assert value==0 if j in f else value<0
        faces.append(tuple(f))
    edges=sorted({tuple(sorted(e)) for f in faces for e in zip(f,f[1:]+f[:1])})
    assert len(vertices)-len(edges)+len(faces)==2
    incidence={e:[j for j,f in enumerate(faces) if e in [tuple(sorted(ab)) for ab in zip(f,f[1:]+f[:1])]] for e in edges}
    assert all(len(v)==2 for v in incidence.values())
    V=S.S.Zero;first=S.zeros(3,1);second=S.zeros(3)
    for f in faces:
        aa=vertices[f[0]]
        for k in range(1,len(f)-1):
            bb,cc=vertices[f[k]],vertices[f[k+1]];det=S.det(S.Matrix.hstack(aa,bb,cc));v=aa+bb+cc
            V+=det/6;first+=det*v/24
            second+=det*(v*v.T+aa*aa.T+bb*bb.T+cc*cc.T)/120
    V=clean(V);assert V>0
    g=(first/V).applyfunc(clean);cov=(second/V-g*g.T).applyfunc(clean);positive_definite(cov)
    data=[]
    for f in faces:
        aa,bb,cc=[vertices[i] for i in f[:3]];n=(bb-aa).cross(cc-aa)
        support=clean(n.dot(aa-g));assert support>0
        mass=S.S.Zero;moment1=S.zeros(3,1);moment2=S.zeros(3)
        for k in range(1,len(f)-1):
            bb,cc=vertices[f[k]],vertices[f[k+1]];w=clean(n.dot((bb-aa).cross(cc-aa)));assert w>0
            v=aa+bb+cc;mass+=w;moment1+=w*v/3
            moment2+=w*(v*v.T+aa*aa.T+bb*bb.T+cc*cc.T)/12
        cf=(moment1/mass-g).applyfunc(clean)
        T=(moment2/mass-(moment1/mass)*g.T-g*(moment1/mass).T+g*g.T).applyfunc(clean)
        alpha=clean(support*mass/(2*n.dot(n)*V));pole=(n/support).applyfunc(clean)
        matzero(T*pole-cf)
        gap=(Q(3,2)*cov-alpha*T).applyfunc(clean)
        data.append(dict(vertices=f,alpha=alpha,c=cf,T=T,pole=pole,gap=gap,
                         nonnegative_principal_minors=positive_semidefinite(gap)))
    centered=[v-g for v in vertices];poles=[f['pole'] for f in data]
    stable=[i for i,v in enumerate(poles) if all(v.dot(w)-v.dot(v)<0 for j,w in enumerate(poles) if j!=i)]
    unstable=[i for i,v in enumerate(centered) if all(v.dot(centered[j]-v)<0 for e in edges if i in e for j in e if j!=i)]
    saddles=[];weak=[];primitives=[]
    for e in edges:
        i,j=e;k,l=incidence[e];aa,bb=centered[i],centered[j];cc,dd=poles[k],poles[l]
        values=[clean(aa.dot(bb)-aa.dot(aa)),clean(aa.dot(bb)-bb.dot(bb)),clean(cc.dot(dd)-cc.dot(cc)),clean(cc.dot(dd)-dd.dot(dd))]
        if all(t<0 for t in values):saddles.append(e)
        if all(t<=0 for t in values) and any(t==0 for t in values):weak.append(e)
        primitives.append(dict(edge=e,facets=(k,l),values=values))
    if not weak:assert len(stable)+len(unstable)-len(saddles)==2
    return dict(vertices=vertices,faces=faces,edges=edges,volume=V,centroid=g,Sigma=cov,facet_moments=data,
                own_euclidean=dict(S=stable,U=unstable,H=saddles,physical_weak_edge_packets=weak),all_edge_primitives=primitives)

def profile_polytope(base,aa,bb,ll,qq,tt):
    assert aa>0 and bb>0 and ll>=0 and qq>0 and tt>=0
    assert (1-ll)/aa>=qq-1>=(tt-qq)/bb
    levels=[(-aa,ll),(S.S.Zero,S.S.One),(S.S.One,qq),(1+bb,tt)]
    removed=[]
    while len(levels)>2:
        for k in range(1,len(levels)-1):
            za,ha=levels[k-1];zz,hh=levels[k];zb,hb=levels[k+1]
            if (hh-ha)*(zb-zz)==(hb-hh)*(zz-za):
                removed.append(levels.pop(k));break
        else:break
    vertices=[];rings=[]
    for zz,hh in levels:
        if hh==0:rings.append([len(vertices)]);vertices.append(S.Matrix((0,0,zz)))
        else:
            rr=[]
            for v in base:rr.append(len(vertices));vertices.append(S.Matrix((hh*v[0],hh*v[1],zz)))
            rings.append(rr)
    faces=[];n=len(base)
    for rr in (rings[0],rings[-1]):
        if len(rr)>1:faces.append(tuple(rr))
    for low,high in zip(rings,rings[1:]):
        for j in range(n):
            jj=(j+1)%n
            if len(low)==1:ff=(low[0],high[j],high[jj])
            elif len(high)==1:ff=(low[j],low[jj],high[0])
            else:ff=(low[j],low[jj],high[jj],high[j])
            faces.append(ff)
    return exact_polytope(vertices,faces),removed

def raw_profile_moments(aa,bb,ll,qq,tt):
    zz=S.symbols('z',real=True)
    pieces=[(-aa,0,1+(1-ll)*zz/aa),(0,1,1+(qq-1)*zz),
            (1,1+bb,qq+(tt-qq)*(zz-1)/bb)]
    def integral(n,j):
        result=0
        for lo,hi,hh in pieces:
            poly=S.Poly(S.expand(hh**n*zz**j),zz)
            result+=sum(c*(hi**(k+1)-lo**(k+1))/S.Integer(k+1) for (k,),c in poly.terms())
        return clean(result)
    return dict(V=integral(2,0),M=integral(2,1),E=integral(2,2),N4=integral(4,0))

def actual_controls():
    square=[S.Matrix(p) for p in [(-1,-1),(1,-1),(1,1),(-1,1)]]
    pentagon=[S.Matrix(p) for p in [(0,0),(3,0),(4,1),(2,3),(-1,2)]]
    triangle=[S.Matrix(p) for p in [(0,0),(3,0),(1,2)]]
    cases=[('square_bulged_positive_caps',square,(2,3,Q(1,3),Q(4,5),Q(1,10))),
           ('pentagon_monotone_left',pentagon,(2,1,Q(5,4),Q(3,4),Q(1,4))),
           ('triangle_rising_middle',triangle,(1,2,Q(1,4),Q(3,2),2)),
           ('triangle_left_apex',triangle,(2,1,0,Q(2,3),Q(1,6))),
           ('square_two_apices',square,(2,3,0,1,0)),
           ('square_left_merge',square,(2,1,Q(3,2),Q(3,4),Q(1,4))),
           ('square_right_merge',square,(2,1,Q(1,3),Q(3,4),Q(1,2))),
           ('square_double_merge',square,(2,1,Q(3,2),Q(3,4),Q(1,2))),
           ('square_prism_merge',square,(2,3,1,1,1))]
    records=[]
    for name,raw,parameters in cases:
        pars=tuple(map(Q,parameters));area,bg,bc=polygon_moments(raw);base=[v-bg for v in raw]
        body,removed=profile_polytope(base,*pars);mm=raw_profile_moments(*pars)
        V,M,E,N=map(mm.get,('V','M','E','N4'));mu=clean(M/V)
        cv=S.zeros(3);cv[:2,:2]=N/V*bc;cv[2,2]=clean(E/V-mu*mu)
        assert body['volume']==area*V
        matzero(body['centroid']-S.Matrix((0,0,mu)));matzero(body['Sigma']-cv)
        records.append(dict(name=name,raw_base=raw,base_centroid=bg,parameters=pars,
                            removed_redundant_levels=removed,profile_moments=mm,body=body))
    # A genuine nonorthogonal affine image: recompute volume, whole facets,
    # covariance and native metric census rather than transferring a census.
    old=records[1]['body']
    A=S.Matrix([[1,Q(1,5),Q(1,7)],[0,1,Q(1,6)],[0,0,1]])
    shift=S.Matrix((2,-3,1))
    image=exact_polytope([A*v+shift for v in old['vertices']],old['faces'])
    assert image['volume']==A.det()*old['volume']
    matzero(image['centroid']-A*old['centroid']-shift)
    matzero(image['Sigma']-A*old['Sigma']*A.T)
    records.append(dict(name='pentagon_actual_affine_image',affine_matrix=A,shift=shift,body=image))
    return records

def encode(v):
    if isinstance(v,S.MatrixBase):return [[encode(t) for t in row] for row in v.tolist()]
    if isinstance(v,S.Basic):return str(v)
    if isinstance(v,Fraction):return str(v)
    if isinstance(v,dict):return {str(k):encode(t) for k,t in v.items()}
    if isinstance(v,(tuple,list)):return [encode(t) for t in v]
    return v

def file_identity(path):
    h=hashlib.sha256();size=0
    with open(path,'rb') as f:
        while block:=f.read(1024*1024):h.update(block);size+=len(block)
    return dict(filename=str(path),bytes=size,sha256=h.hexdigest())

def main():
    assert __debug__ and S.__version__=='1.14.0'
    coeff=Path('three_piece_all_bernstein_controls.jsonl');cert=[]
    with coeff.open('wb') as output:
        for chart in ('bulged','monotone'):
            for idx in ('0','1','2','cap'):
                for name in (('Lt','Ln','Rt','Rn') if idx=='cap' else ('H','R','D')):
                    cc=certify(gate(chart,idx,name),chart,idx,name,output);cert.append(cc)
                    print('GLOBAL',chart,idx,name,cc['controls'],cc['zeros'],flush=True)
    total=sum(c['controls'] for c in cert);zeros=sum(c['zeros'] for c in cert)
    assert (len(cert),total,zeros)==(26,1245442,199221)
    controls=actual_controls();identity=file_identity(coeff)
    report=dict(identity='ALL_CONCAVE_THREE_PIECE_HOMOTHETIC_PROFILES_EVERY_WHOLE_FACET_V1',
                coefficients_file=identity,certificates=cert,total_controls=total,zero_controls=zeros,negative_controls=0,
                actual_controls=controls,
                source_dependencies=dict(planar='[internal-source-reference]',merged_whole_facets='[internal-source-reference]'),
                scope='Every whole facet for every nonnegative concave profile with at most THREE affine pieces, arbitrary convex planar base and nonsingular affine images. Not arbitrary concave profiles, an equilibrium exclusion or a minimum theorem.',
                chart_conventions='Reflect/rescale middle heights to 1,q<=1. q=(b+x)/(b+1), right endpoint=x*y. Bulged left endpoint=l; monotone left endpoint=1+a*(1-q)*l. a,b>0; x,l,y in[0,1]. Code multiplies all heights by b+1.',
                exact_basis='For each positive a^i b^j, use tensor Bernstein in x,l,y at the blockwise maximum power degrees, fixed before any axis conversion. All basis functions and positive powers are nonnegative. No sampling.',
                degeneration='Remove coincident-slope rings. A merged WHOLE facet is covered by the accepted whole-two-piece theorem, never by summing fragment estimates.',
                sharpness='Rectangular prisms attain 3/2. Genuine three-piece square profiles with zero endpoint heights, a=b=1/n,q=1 have central-facet ratio 15*n/(10*n+4) tending to3/2; incidence changes at the prism limit.')
    data=(json.dumps(encode(report),sort_keys=True,indent=2)+'\n').encode()
    Path('three_piece_all_whole_facets_report.json').write_bytes(data)
    print('EXACT_ALL_THREE_PIECE_PROFILE_CHARTS_PASS',len(cert),total,zeros)
    for cc in controls:
        pp=cc['body'];own=pp['own_euclidean']
        print('ACTUAL',cc['name'],'VEF',len(pp['vertices']),len(pp['edges']),len(pp['faces']),
              'OWN',len(own['S']),len(own['U']),len(own['H']),'WEAK_PACKETS',len(own['physical_weak_edge_packets']))
    print('COEFFICIENTS',identity['bytes'],identity['sha256'])
    print('REPORT',len(data),hashlib.sha256(data).hexdigest())
    print('ALL_THREE_PIECE_HOMOTHETIC_PROFILES_WHOLE_FACET_EXACT_PASS')
if __name__=='__main__':main()
