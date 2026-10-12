# material-370224784bcb

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

"""Exact endcap moment theorem and actual controls for concave homothetic profiles.
CPython 3.11+; SymPy 1.13+; assertions enabled. No data files or random input.
The analytical proof is in the companion recovery capsule. The universal normal
3/2 inequality is an explicitly named accepted predecessor, not replayed here.
"""
from pathlib import Path
from itertools import combinations
from math import comb, factorial
import hashlib, json, platform
import sympy as S
Q=S.Rational
z,s,t=S.symbols('z s t', real=True)

def clean(x): return S.factor(S.cancel(x))
def zero(x): assert clean(x)==0,clean(x)
def integral(x,a,b): return clean(S.integrate(S.expand(x),(z,a,b)))
def serialize(x):
    if isinstance(x,S.MatrixBase): return [[serialize(x[i,j]) for j in range(x.cols)] for i in range(x.rows)]
    if isinstance(x,S.Basic): return str(x)
    if isinstance(x,dict): return {str(k):serialize(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [serialize(v) for v in x]
    return x

def kernels():
    k=1-z
    w1=2*k*(Q(10,3)*k*k+1-4*z)
    w2=11-24*z+10*z*z
    A=lambda x:x*x/2-x**3/3
    C=lambda x:x*x/2-x**3+3*x**4/4-x**5/5
    W=lambda x:11*x**3/3-6*x**4+2*x**5
    L=s*s*(1-s)**2*(13-4*s)/3
    zero(integral(z*w1,0,s)-L)
    zero(integral(z*z*w2,0,s)-W(s))
    zero(integral(z*(1-z),0,s)-A(s))
    zero(integral(z*(1-z)**3,0,s)-C(s))
    K=W(s)+20*(A(s)*C(t)+A(t)*C(s)) # valid s<=t
    P=11+23*s-51*s*s+34*s**3-8*s**4
    zero(K.subs(t,s)-s**3*(1-s)*P/3)
    zero(S.diff(K,t)-20*(A(s)*t*(1-t)**3+C(s)*t*(1-t)))
    controls=[clean(sum(S.expand(P).coeff(s,j)*Q(comb(i,j),comb(4,j)) for j in range(i+1))) for i in range(5)]
    assert controls==[11,Q(67,4),14,Q(Q(45,4)),9]
    assert all(x>0 for x in controls)
    v,a,b,c,d,e,f,gg,j=S.symbols('v a b c d e f g j')
    # a=int k g,b=int g²,c=int k³g,d=int k²g²,e=int kg³,
    # f=int zkg,gg=int g⁴,j=int zg². v scales the perturbation g.
    V=Q(1,3)+2*v*a+v*v*b
    N=Q(1,5)+4*v*c+6*v*v*d+4*v**3*e+v**4*gg
    M=Q(1,12)+2*v*f+v*v*j
    coeff=[clean(S.expand(5*V*N-4*M).coeff(v,i)) for i in range(7)]
    expected=[0,2*a+Q(20,3)*c-8*f,b+10*d+40*a*c-4*j,
              Q(20,3)*e+60*a*d+20*b*c,Q(5,3)*gg+40*a*e+30*b*d,
              10*a*gg+20*b*e,5*b*gg]
    for observed,target in zip(coeff,expected): zero(observed-target)
    return dict(linear_kernel=L,quadratic_kernel_ordered=K,
                diagonal_kernel=s**3*(1-s)*P/3,
                positive_Bernstein_controls=controls,perturbation_coefficients=coeff)

def simplex_moment(points,exponents):
    """Average of product coordinate powers on simplex; dimensions 2 or 3."""
    dim=len(points)-1
    slots=[]
    for i,p in enumerate(exponents): slots.extend([i]*p)
    def walk(j,counts,factor):
        if j==len(slots):
            return factor*Q(factorial(dim)*__import__('math').prod(factorial(k) for k in counts),factorial(dim+len(slots)))
        out=0
        for k,v in enumerate(points):
            cc=counts.copy();cc[k]+=1
            out+=walk(j+1,cc,factor*v[slots[j]])
        return out
    return clean(walk(0,[0]*len(points),S.Integer(1)))

def base_data():
    raw=[S.Matrix(v) for v in [(0,0),(3,0),(4,1),(2,3),(-1,2)]]
    A=0;J=S.zeros(2,1);R=S.zeros(2)
    for i in range(1,len(raw)-1):
        p=[raw[0],raw[i],raw[i+1]]
        area=S.det(S.Matrix.hstack(p[1]-p[0],p[2]-p[0]))/2
        A+=area
        for a in range(2):
            exp=[0,0];exp[a]=1;J[a]+=area*simplex_moment(p,exp)
            for b in range(2):
                exp=[0,0];exp[a]+=1;exp[b]+=1;R[a,b]+=area*simplex_moment(p,exp)
    g=J/A;cov=(R/A-g*g.T).applyfunc(clean)
    assert cov.det()>0 and cov[0,0]>0
    return [(p-g).applyfunc(clean) for p in raw],A,cov,g

def profile_moments(pieces):
    V=M=E=N4=0
    for lo,hi,h in pieces:
        V+=integral(h*h,lo,hi);M+=integral(z*h*h,lo,hi)
        E+=integral(z*z*h*h,lo,hi);N4+=integral(h**4,lo,hi)
    mu=clean(M/V);SS=clean(E-M*M/V)
    return tuple(map(clean,(V,M,E,N4,mu,SS)))

def cap_records(pieces,area,base_cov):
    V,M,E,N4,mu,SS=profile_moments(pieces)
    cov=S.diag(1,1,1)
    cov[:2,:2]=N4/V*base_cov;cov[2,2]=SS/V
    records=[]
    for lohi,idx in [(0,0),(1,-1)]:
        a,b,h=pieces[idx];end=a if lohi==0 else b;he=clean(h.subs(z,end))
        if he==0:continue
        dist=abs(end-mu);alpha=clean(dist*he*he/V)
        T=S.zeros(3);T[:2,:2]=he*he*base_cov;T[2,2]=dist*dist
        tang=clean(dist*he**4/N4);norm=clean(dist**3*he**2/SS)
        assert tang<=Q(5,4) and norm<=Q(3,2),(tang,norm)
        G=(Q(3,2)*cov-alpha*T).applyfunc(clean)
        for k in (1,2,3):
            for inds in combinations(range(3),k):assert G.extract(inds,inds).det()>=0
        pole=S.Matrix([0,0,1/(end-mu)])
        cf=S.Matrix([0,0,end-mu]);assert (T*pole-cf).applyfunc(clean)==S.zeros(3,1)
        records.append(dict(end=end,height=he,alpha=alpha,T=T,pole=pole,
                            tangent_ratio=tang,normal_ratio=norm,full_gap=G))
    return dict(volume=area*V,centroid=(0,0,mu),covariance=cov,
                axial_moments=dict(V=V,M=M,E=E,N4=N4,variance_numerator=SS),caps=records)

def physical_polytope(base,knots,heights):
    """Full true incidence and Euclidean census for one strict five-piece control."""
    n=len(base);levels=len(knots)
    vertices=[S.Matrix([h*p[0],h*p[1],t]) for t,h in zip(knots,heights) for p in base]
    faces=[list(reversed(range(n))),list(range((levels-1)*n,levels*n))]
    for l in range(levels-1):
        for i in range(n):
            j=(i+1)%n;faces.append([l*n+i,l*n+j,(l+1)*n+j,(l+1)*n+i])
    refs=sum(vertices,S.zeros(3,1))/len(vertices)
    planes=[];edges={}
    for ids in faces:
        p=[vertices[i] for i in ids];nn=(p[1]-p[0]).cross(p[2]-p[0]);hh=nn.dot(p[0])
        if nn.dot(refs)>hh:ids.reverse();nn=-nn;hh=-hh
        assert all(nn.dot(vertices[i])==hh for i in ids)
        assert all(nn.dot(vertices[i])<hh for i in range(len(vertices)) if i not in ids)
        planes.append((nn,hh))
        for i,j in zip(ids,ids[1:]+ids[:1]):edges.setdefault(tuple(sorted((i,j))),[]).append(len(planes)-1)
    assert all(len(ff)==2 for ff in edges.values())
    V=0;J=S.zeros(3,1);R=S.zeros(3)
    for ids in faces:
        for i in range(1,len(ids)-1):
            p=[S.zeros(3,1),vertices[ids[0]],vertices[ids[i]],vertices[ids[i+1]]]
            vol=S.det(S.Matrix.hstack(*p[1:]))/6;V+=vol
            for a in range(3):
                exp=[0]*3;exp[a]=1;J[a]+=vol*simplex_moment(p,exp)
                for b in range(3):
                    exp=[0]*3;exp[a]+=1;exp[b]+=1;R[a,b]+=vol*simplex_moment(p,exp)
    g=(J/V).applyfunc(clean);cov=(R/V-g*g.T).applyfunc(clean);x=[v-g for v in vertices]
    nbr={i:[] for i in range(len(x))}
    for i,j in edges:nbr[i].append(j);nbr[j].append(i)
    U=[i for i in nbr if all(x[i].dot(x[j]-x[i])<0 for j in nbr[i])]
    stable=[]
    for f,(nn,hh) in enumerate(planes):
        d=hh-nn.dot(g);foot=d*nn/nn.dot(nn)
        if all(mm.dot(foot)<kk-mm.dot(g) for j,(mm,kk) in enumerate(planes) if j!=f):stable.append(f)
    saddle=[];weak=set();edge_packets=[]
    for (i,j),ff in edges.items():
        a=x[i];u=x[j]-a;L=u.dot(u);AA=-a.dot(u);rr=L*a+AA*u;BB=[]
        for f in ff:
            k=next(k for k in faces[f] if k not in (i,j));BB.append(clean(rr.dot(x[k]-a)))
        packet=[AA,L-AA,-BB[0],-BB[1]]
        if all(v>=0 for v in packet):
            if all(v>0 for v in packet):saddle.append((i,j))
            else:weak.add(tuple(clean(v/L) for v in rr))
        edge_packets.append(dict(edge=(i,j),closed_packet=packet))
    assert len(stable)+len(U)-len(saddle)==2
    return dict(vertices=vertices,facets=faces,edges=list(edges),V_E_F=(len(x),len(edges),len(faces)),
                volume=V,centroid=g,covariance=cov,strict_stable=stable,strict_unstable=U,
                strict_saddle=saddle,physical_weak_points=sorted(weak),edge_packets=edge_packets)

def main():
    assert __debug__
    cert=kernels();base,area,covD,baseg=base_data()
    examples={
      'pyramid_sharp_tangent':[(S.Integer(0),S.Integer(1),1-z)],
      'prism_sharp_normal':[(S.Integer(0),S.Integer(1),S.Integer(1))],
      'curved_positive_caps':[(S.Integer(0),S.Integer(1),S.sqrt(1+2*z-z*z))]}
    knots=[Q(i,5) for i in range(6)];hh=list(map(S.sympify,[1,Q(7,5),Q(17,10),Q(9,5),Q(8,5),1]))
    slopes=[(hh[i+1]-hh[i])/(knots[i+1]-knots[i]) for i in range(5)]
    assert all(slopes[i]>slopes[i+1] for i in range(4))
    pieces=[(knots[i],knots[i+1],hh[i]+slopes[i]*(z-knots[i])) for i in range(5)]
    examples['five_piece_actual_polytope']=pieces
    controls={name:cap_records(p,area,covD) for name,p in examples.items()}
    assert controls['pyramid_sharp_tangent']['caps'][0]['tangent_ratio']==Q(5,4)
    assert controls['prism_sharp_normal']['caps'][0]['normal_ratio']==Q(3,2)
    poly=physical_polytope(base,knots,hh);m=controls['five_piece_actual_polytope']
    zero(poly['volume']-m['volume']);assert poly['centroid']==S.Matrix(m['centroid'])
    assert (poly['covariance']-m['covariance']).applyfunc(clean)==S.zeros(3)
    assert tuple(poly['V_E_F'])==(30,55,27)
    assert (len(poly['strict_stable']),len(poly['strict_unstable']),len(poly['strict_saddle']))!=(1,1,0)
    # An actual nonorthogonal affine image: covariances and cap gap by congruence.
    A=S.Matrix([[1,Q(1,5),Q(1,7)],[0,1,Q(1,6)],[0,0,1]])
    shift=S.Matrix([2,-3,1]);aff=dict(vertices=[A*x+shift for x in poly['vertices']],
        centroid=A*poly['centroid']+shift,covariance=A*poly['covariance']*A.T,caps=[])
    for c in m['caps']:
        cc=dict(alpha=c['alpha'],T=A*c['T']*A.T,pole=A.T.inv()*c['pole'])
        gap=(Q(3,2)*aff['covariance']-cc['alpha']*cc['T']).applyfunc(clean)
        for k in (1,2,3):
            for inds in combinations(range(3),k):assert gap.extract(inds,inds).det()>=0
        cc['gap']=gap;aff['caps'].append(cc)
    # Exact kernel controls with non-affine concave h, including an unbounded g(t)/t at0.
    perturb_controls=[]
    for h in [1-z+z*(1-z),1-z+S.sqrt(z),1-z+z*(2-z),S.sqrt(1+2*z-z*z)]:
        V=integral(h*h,0,1);M=integral(z*h*h,0,1);N=integral(h**4,0,1)
        gap=clean(5*V*N-4*M);assert gap>0
        perturb_controls.append(dict(h=h,V=V,M=M,N4=N,gap=gap))
    report=dict(identity='ARBITRARY_CONCAVE_HOMOTHETIC_ENDCAPS_SHARP_TANGENT_5_4_V1',
        kernels=cert,base_area=area,raw_base_centroid=baseg,base=base,base_covariance=covD,
        controls=controls,five_piece_full_actual_polytope=poly,affine_image=aff,
        non_affine_kernel_controls=perturb_controls,
        scope='Every whole END CAP of any concave homothetic profile: tangent5/4, full3/2 using the named accepted universal normal theorem. No arbitrary sloping-facet theorem, no E17 exclusion, no own110 attainer.',
        analytical_normal_predecessor='[internal-source-reference]',
        environment=dict(python=platform.python_version(),sympy=S.__version__))
    data=(json.dumps(serialize(report),sort_keys=True,indent=2)+'\n').encode()
    Path('concave_profile_endcaps_report.json').write_bytes(data)
    print('ONE_SIDED_CONCAVITY_LINEAR_AND_QUADRATIC_KERNELS_EXACT_PASS')
    print('ALL_ARBITRARY_CONCAVE_PROFILE_ENDCAPS_SHARP_TANGENT_5_4_PASS')
    print('ACTUAL_FIVE_PIECE',poly['V_E_F'],len(poly['strict_stable']),len(poly['strict_unstable']),len(poly['strict_saddle']),'weak',len(poly['physical_weak_points']))
    print('REPORT',len(data),hashlib.sha256(data).hexdigest())
    print('ARBITRARY_CONCAVE_PROFILE_ENDCAPS_EXACT_RECOVERY_PASS')
if __name__=='__main__':main()
