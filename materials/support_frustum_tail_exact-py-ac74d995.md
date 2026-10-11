# material-ac74d9955bd1

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""SUPPORT_FRUSTUM_CONVEX_ORDER_AND_ROOT_MASS_V1.
Exact rational algebra, continuous polynomial certificates, true-body controls.
CPython >=3.11; standard library only; assertions must remain enabled.
  python -S support_frustum_tail_exact.py build
  python -S support_frustum_tail_exact.py check
No external inputs. The accompanying proof supplies the continuous theorem.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb
from pathlib import Path
import hashlib
import json
import sys
assert __debug__
IDENTITY='SUPPORT_FRUSTUM_CONVEX_ORDER_AND_ROOT_MASS_V1'
OUTPUT='support_frustum_tail_exact.json'
Z=(F(0),F(0),F(0))

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def addp(a,b):
    c=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=x
    return trim(c)

def scale(a,s):return trim([s*x for x in a])
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)

def power(a,n):
    b=[F(1)]
    for _ in range(n):b=mul(b,a)
    return b

def ev(a,x):
    z=F(0)
    for v in reversed(a):z=z*x+v
    return z

def compose(a,l,r):
    out=[F(0)]
    for i,v in enumerate(a):out=addp(out,scale(power([l,r-l],i),v))
    return out

def derivative(a):return trim([i*a[i] for i in range(1,len(a))] or [F(0)])
def integral(a,l,r):return sum((v*(r**(i+1)-l**(i+1))/(i+1) for i,v in enumerate(a)),F(0))

def bernstein(a,l,r):
    p=compose(a,l,r);n=len(p)-1
    b=[sum((p[i]*F(comb(j,i),comb(n,i)) for i in range(j+1)),F(0)) for j in range(n+1)]
    out=[F(0)]
    for j,x in enumerate(b):
        out=addp(out,scale(mul([F(0)]*j+[F(1)],power([F(1),F(-1)],n-j)),x*comb(n,j)))
    assert out==p
    return b

def certify(a,l,r,depth=0):
    """Exact exhaustive subdivision, not a numerical positivity test."""
    b=bernstein(a,l,r)
    if min(b)>=0:
        return [{'interval':[l,r],'degree':len(b)-1,'coefficients':b}]
    assert depth<20,('uncertified',l,r,b)
    mid=(l+r)/2
    return certify(a,l,mid,depth+1)+certify(a,mid,r,depth+1)

def hinge_poly(values,mid):
    """Polynomial in t on an interval with no affine knot in its interior."""
    v=sorted(values);p=len(v)
    d=[power([x,F(-1)],p) if x>mid else [F(0)] for x in v]
    for k in range(1,p):
        nd=[]
        for i in range(len(d)-1):
            if v[i+k]==v[i]:
                nd.append(scale(power([v[i],F(-1)],p-k),F(comb(p,k))) if v[i]>mid else [F(0)])
            else:nd.append(scale(addp(d[i+1],scale(d[i],-1)),1/(v[i+k]-v[i])))
        d=nd
    return scale(d[0],F(1,p))

def hinge(values,t):
    v=sorted(values);p=len(v)
    d=[max(x-t,F(0))**p for x in v]
    for k in range(1,p):
        d=[F(comb(p,k))*max(v[i]-t,F(0))**(p-k) if v[i+k]==v[i]
           else (d[i+1]-d[i])/(v[i+k]-v[i]) for i in range(len(d)-1)]
    return d[0]/p

def frustum_parameters(r):
    a=1+r+r*r;b=1+2*r+3*r*r
    L=4*a/b;D=3*b/(4*a*a)
    second=L*L*(1+3*r+6*r*r)/(10*a)
    return L,D,second

def density_poly(r):
    L,D,_=frustum_parameters(r)
    return scale(power([F(1),(r-1)/L],2),D)

def cap_poly(r):
    L,_,_=frustum_parameters(r);dens=density_poly(r)
    # Integral_t^L (s-t) dens(s) ds, as a polynomial in t.
    out=[F(0)]
    for j,c in enumerate(dens):
        term=[L**(j+2)/F(j+2),-L**(j+1)/F(j+1)]+[F(0)]*j+[F(1,(j+1)*(j+2))]
        out=addp(out,scale(term,c))
    assert ev(out,L)==0 and ev(derivative(out),L)==0
    assert ev(out,F(0))==1 and ev(derivative(out),F(0))==-1
    return out

def cap(r,t):
    L,_,_=frustum_parameters(r)
    if t<=0:return 1-t
    if t>=L:return F(0)
    return ev(cap_poly(r),t)

def pair_lower_poly(m,T,a,c,mid):
    z=(3-T)/(3-m)
    return addp(scale(hinge_poly([F(1),a,a,c],mid),m/3),
                scale(hinge_poly([F(1),z,z,z],mid),(3-m)/3))

def all_piecewise(bounds,polynomial):
    bounds=sorted(set(bounds));out=[]
    for l,r in zip(bounds,bounds[1:]):
        p=polynomial((l+r)/2)
        cells=certify(p,l,r)
        for t in [l,(l+r)/2,r]:assert ev(p,t)>=0
        out.append({'knots':[l,r],'power_coefficients':p,'cells':cells})
    return out

def scalar_control():
    r=F(2,5);A,D,second=frustum_parameters(r);h=F(1,4);T=F(51,25)
    m=h+(T-h)/A;c=A+3*h/m*(1-A);mi=m/2;z=(3-T)/(3-m)
    assert A==F(52,19) and m==F(4701,5200) and c==F(38584,29773)
    assert 0<c<A<4 and F(4,3)<A and 3*h/4<mi<F(3,4)
    delta=3*(1+h)/4-m
    assert delta==F(87,2600)>0 and m>F(13,15) and h>F(7,45)
    gx=gy=m/(6*h);gz=F(1,4)
    assert A+(c-A)*(gx+gy)==1
    assert m*(2*A+c)/3==T and T/2<F(132,119)
    assert A>=4*T-8 and c>=0
    Q=lambda a,b,c:(a*a+b*b+c*c+a*b+a*c+b*c)/6
    surface=m*Q(A,A,c)+(3-T)**2/(3-m)
    radial_second=F(2,5)+surface/5
    assert radial_second<second<F(8,5) and surface<6
    tetmean=(A+c)/2
    tetsecond=(2*A*A+2*c*c+(2*A+2*c)**2)/20
    ztet=(1-h*tetmean)/(1-h)
    tet_second_lower=h*tetsecond+(1-h)*ztet*ztet
    assert 0<ztet<1 and tet_second_lower<second
    old_cap=power([F(1),F(-1,4)],4)
    old_tail=all_piecewise([F(0),z,F(1),c,A,F(4)],
        lambda mid:addp(old_cap,scale(pair_lower_poly(m,T,A,c,mid),-1)))
    for region in old_tail:
        l,u=region['knots']
        for t in [l,(l+u)/2,u]:
            actual=m*hinge([F(1),A,A,c],t)/3+(3-m)*hinge([F(1),z,z,z],t)/3
            assert ev(region['power_coefficients'],t)==max(1-t/4,F(0))**4-actual
    # The tetrahedron plus its Jensen remainder passes even the new full cap.
    fcap=cap_poly(r)
    def tet_gap(mid):
        rest=[ztet,F(-1)] if mid<ztet else [F(0)]
        lower=addp(scale(hinge_poly([A,A,c,c],mid),h),scale(rest,1-h))
        return addp(fcap,scale(lower,-1))
    tet_tail=all_piecewise([F(0),ztet,c,A],tet_gap)
    # Complete earlier family of partial facet-merge cuts, 0<k<=1.
    k=[F(0),F(1)];one=[F(1)];t=addp(one,scale(k,-3*h/m));q=2*A
    f=[F(0),F(0),F(3),F(-2)];I=[F(0),F(0),F(0),F(2),F(-3,2)]
    ZZ=addp(f,scale(I,-3*h/m))
    J=addp(scale([F(0),F(0),F(3,2),F(-2),F(3,4)],q),
           scale([F(0),F(0),F(0),F(1),F(-3,4)],2*c))
    omk=addp(one,scale(k,-1));AA=addp(addp(mul(t,t),mul(t,omk)),mul(omk,omk))
    BB=mul(k,addp(t,scale(omk,2)))
    brace=addp(addp(scale(AA,m*q),scale(BB,3*T-m*q)),
              scale(mul(addp(one,scale(t,-1)),addp(scale(t,2),omk)),m))
    U=addp(one,scale(f,-h));W=addp(one,scale(J,-h));den=mul(U,W)
    num=scale(mul(mul(k,brace),addp(mul(t,U),scale(ZZ,h))),F(1,3))
    cut_cert={name:{'power_coefficients':p,'cells':certify(p,F(0),F(1))}
              for name,p in [('t',t),('U',U),('W',W),('den_minus_num',addp(den,scale(num,-1)))]}
    assert ev(t,F(1))>0
    assert all(all(min(cel['coefficients'])>0 for cel in d['cells']) for d in cut_cert.values())
    threshold=F(7,5)
    lower=m*hinge([F(1),A,A,c],threshold)/3+(3-m)*hinge([F(1),z,z,z],threshold)/3
    upper=cap(r,threshold);newgap=lower-upper
    assert newgap>0
    return {'status':'FORMAL_SCALAR_CONTROL_NOT_A_BODY_NOT_A_FULL_LAMBDA_METRIC_SYSTEM',
            'r':r,'L':A,'h':h,'m':m,'m1':mi,'m2':mi,'T':T,'facet_values':[A,A,c,c],
            'formal_own_centroid':[gx,gy,gz],'joint_mass_deficit':delta,
            'root_function':'ell(x,y,z)=A+(c-A)*(x+y); on x,y>=0 its maximum is A, attained at AB',
            'conditional_root_mass_cap':D,'conditional_second_upper':second,
            'radial_second_lower':radial_second,'tetrahedron_second_lower':tet_second_lower,
            'old_full_radial_tail_certificates':old_tail,
            'new_full_tetrahedron_tail_certificates':tet_tail,
            'all_partial_cut_certificates':cut_cert,'cut_numerator':num,'cut_denominator':den,
            'new_rejection_threshold':threshold,'new_radial_lower':lower,'new_upper':upper,'new_gap':newgap,
            'not_claimed_to_pass_other_constraints':True}

def vector_add(a,b):return tuple(x+y for x,y in zip(a,b))
def vector_sub(a,b):return tuple(x-y for x,y in zip(a,b))
def vector_scale(a,s):return tuple(s*x for x in a)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))

def cycle(raw,ids,n):
    drop=next(i for i in range(3) if n[i]);keep=[i for i in range(3) if i!=drop]
    pts=sorted((raw[k][keep[0]],raw[k][keep[1]],k) for k in ids)
    def turn(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lo=[];hi=[]
    for p in pts:
        while len(lo)>1 and turn(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(hi)>1 and turn(hi[-2],hi[-1],p)<=0:hi.pop()
        hi.append(p)
    out=[p[2] for p in lo[:-1]+hi[:-1]]
    assert len(out)>=3
    if dot(cross(vector_sub(raw[out[1]],raw[out[0]]),vector_sub(raw[out[2]],raw[out[0]])),n)<0:out.reverse()
    j=out.index(min(out));return tuple(out[j:]+out[:j])

def hull(raw):
    planes={}
    for i,j,k in combinations(range(len(raw)),3):
        n=cross(vector_sub(raw[j],raw[i]),vector_sub(raw[k],raw[i]))
        if n==Z:continue
        b=dot(n,raw[i]);sgn=[dot(n,x)-b for x in raw]
        if all(x==0 for x in sgn):continue
        if all(x<=0 for x in sgn):pass
        elif all(x>=0 for x in sgn):n=vector_scale(n,-1);b=-b
        else:continue
        ids=tuple(k for k,x in enumerate(raw) if dot(n,x)==b)
        planes.setdefault(ids,(n,b))
    faces=sorted((cycle(raw,ids,n),n,b) for ids,(n,b) in planes.items())
    V=F(0);mom=Z
    for cyc,n,b in faces:
        a=raw[cyc[0]]
        for j in range(1,len(cyc)-1):
            c=raw[cyc[j]];d=raw[cyc[j+1]];w=det(a,c,d)/6
            V+=w;mom=vector_add(mom,vector_scale(vector_add(vector_add(a,c),d),w/4))
    assert V>0
    g=vector_scale(mom,1/V)
    assert all(dot(n,g)<b for cyc,n,b in faces)
    edges=sorted({tuple(sorted((cyc[j],cyc[(j+1)%len(cyc)]))) for cyc,n,b in faces for j in range(len(cyc))})
    vertices=sorted({i for cyc,n,b in faces for i in cyc})
    assert len(vertices)-len(edges)+len(faces)==2
    return V,g,faces,edges,vertices

def body_control(name,raw,ell,r,equality):
    raw=[tuple(map(F,p)) for p in raw];ell=tuple(map(F,ell))
    V,g,faces,edges,vertices=hull(raw);mu=ell[0]+dot(ell[1:],g)
    assert mu>0
    vals=[(ell[0]+dot(ell[1:],p))/mu for p in raw]
    L,D,second=frustum_parameters(r)
    assert min(vals)==0 and max(vals)==L
    cones=[];rootmass=F(0);facet_data=[]
    for cyc,n,b in faces:
        mass=F(0);trace=F(0)
        for j in range(1,len(cyc)-1):
            ids=(cyc[0],cyc[j],cyc[j+1])
            w=det(*(vector_sub(raw[i],g) for i in ids))/(6*V)
            assert w>0
            cones.append((w,[F(1)]+[vals[i] for i in ids]));mass+=3*w
            trace+=w*sum((vals[i] for i in ids),F(0))
        if all(vals[i]==0 for i in cyc):rootmass+=mass
        facet_data.append({'cycle':cyc,'mass':mass,'trace':trace})
    assert sum((w for w,vs in cones),F(0))==1
    actualmean=sum((w*sum(vs,F(0))/4 for w,vs in cones),F(0));assert actualmean==1
    actualsecond=sum((w*(sum((v*v for v in vs),F(0))+sum(vs,F(0))**2)/20 for w,vs in cones),F(0))
    assert actualsecond<=second and rootmass<=D
    thresholds=sorted(set([F(0),F(1),L]+[L*j/8 for j in range(1,8)]))
    checks=[]
    for t in thresholds:
        actual=sum((w*hinge(vs,t) for w,vs in cones),F(0));upper=cap(r,t)
        assert actual<=upper<=max(1-t/4,F(0))**4
        if equality:assert actual==upper
        elif 0<t<L:assert actual<upper
        checks.append({'threshold':t,'actual_tail':actual,'conditional_cap':upper})
    if equality:assert actualsecond==second and rootmass==D
    else:assert actualsecond<second and rootmass<D
    return {'name':name,'status':'ACTUAL_GEOMETRIC_CONTROL_NOT_A_110_WITNESS',
            'raw_points':raw,'raw_ell':ell,'volume':V,'own_centroid':g,
            'true_facets':[x[0] for x in faces],'true_edges':edges,
            'f_vector':[len(vertices),len(edges),len(faces)],'normalized_vertex_values':vals,
            'r':r,'L':L,'root_mass':rootmass,'root_mass_cap':D,
            'second_moment':actualsecond,'conditional_second_cap':second,
            'facet_data':facet_data,'tail_checks':checks,'is_frustum_equality':equality}

def identities():
    # All-r exact polynomial proof of d <= 3/4 - (4-L)^3/64.
    a=[F(1),F(1),F(1)];b=[F(1),F(2),F(3)]
    lhs=addp(scale(mul([F(2),F(1)],power(b,3)),3),
             scale(mul(power(a,2),power([F(1),F(2)],3)),-4))
    expect=list(map(F,[2,7,36,119,250,297,212,49]));assert lhs==expect
    assert all(x>0 for x in lhs)
    # r-polynomial identities for L' and D'.
    dl=scale(addp(mul(derivative(a),b),scale(mul(a,derivative(b)),-1)),4)
    assert dl==list(map(F,[-4,-16,-4]))
    dd=scale(addp(mul(derivative(b),a),scale(mul(b,derivative(a)),-2)),F(3,4))
    assert dd==[F(0),F(0),F(-9,2),F(-9,2)]
    controls=[]
    for r in [F(0),F(1,10),F(2,5),F(1),F(3),F(100)]:
        L,D,second=frustum_parameters(r);p=density_poly(r)
        assert integral(p,F(0),L)==1
        assert integral(mul(p,[F(0),F(1)]),F(0),L)==1
        assert integral(mul(p,[F(0),F(0),F(1)]),F(0),L)==second
        assert F(3,4)-D==F(3,4)*r**3*(r+2)/(1+r+r*r)**2
        assert D<=F(3,4)-(4-L)**3/64
        assert integral(cap_poly(r),F(0),L)*2==second
        controls.append({'r':r,'L':L,'D':D,'second':second})
    return {'density_deficit_positive_polynomial':expect,'L_derivative_numerator':dl,
            'D_derivative_numerator':dd,'normalization_controls':controls}

def report():
    controls=[]
    for r in [F(0),F(2,5),F(1),F(3)]:
        raw=[(x,y,0) for x,y in product([-1,1],repeat=2)]
        raw+=([(0,0,1)] if r==0 else [(r*x,r*y,1) for x,y in product([-1,1],repeat=2)])
        controls.append(body_control('square_frustum_r='+str(r),raw,(0,0,0,1),r,True))
    octa=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    controls.append(body_control('octahedron_genuine_root_triangle',octa,(1,1,1,1),F(1),False))
    return {'identity':IDENTITY,'identities':identities(),'scalar_control':scalar_control(),
            'actual_controls':controls,'universal_C_lower_bound_unchanged':34,
            'complete_E17_exclusion':False,'exact_minimum_found':False}

def serial(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:serial(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [serial(v) for v in x]
    return x

def main():
    assert len(sys.argv)==2 and sys.argv[1] in ('build','check')
    obj=report();data=(json.dumps(serial(obj),sort_keys=True,indent=2)+'\n').encode()
    path=Path(OUTPUT)
    if sys.argv[1]=='build':path.write_bytes(data)
    else:assert path.read_bytes()==data
    sc=obj['scalar_control'];groups=[sc['old_full_radial_tail_certificates'],sc['new_full_tetrahedron_tail_certificates']]
    counts=[sum(len(x['cells']) for x in group) for group in groups]
    cuts=sum(len(x['cells']) for x in sc['all_partial_cut_certificates'].values())
    print('SUPPORT_FRUSTUM_ALGEBRA_EXACT_PASS')
    print('OLD_ALL_RADIAL_TAILS_AND_NEW_TETRAHEDRON_TAILS_PASS',*counts)
    print('ALL_PARTIAL_CUTS_AND_CONDITIONAL_SECOND_MOMENTS_PASS',cuts)
    print('NEW_SUPPORT_RADIAL_TAIL_REJECTS_SCALAR_CONTROL_PASS',sc['new_gap'])
    print('ACTUAL_FRUSTUM_EQUALITY_AND_OCTAHEDRON_STRICT_CONTROLS_PASS',len(obj['actual_controls']))
    print('SUPPORT_FRUSTUM_RECOVERY_PASS',len(data),hashlib.sha256(data).hexdigest())
if __name__=='__main__':main()
