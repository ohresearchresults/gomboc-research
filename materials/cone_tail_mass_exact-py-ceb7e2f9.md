# material-ceb7e2f9d01a

AI research material

---

"""CONE_TAIL_MASS_13_15_H_7_45_V1: exact algebra and actual-body controls.
CPython >=3.11, standard library only, assertions enabled. No external inputs.
  python -S cone_tail_mass_exact.py build
  python -S cone_tail_mass_exact.py check
The continuous Brunn--Minkowski and cone-disintegration proof is in the
accompanying immutable proof material; finite tests do not replace it.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb
from pathlib import Path
import hashlib
import json
import sys
assert __debug__
IDENTITY='CONE_TAIL_MASS_13_15_H_7_45_V1'
OUTPUT='cone_tail_mass_exact.json'
ZERO=(F(0),F(0),F(0))

def pa(a,b):
    c=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=x
    while len(c)>1 and c[-1]==0:c.pop()
    return c

def ps(a,s):return [s*x for x in a]
def pm(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    while len(c)>1 and c[-1]==0:c.pop()
    return c

def pp(a,n):
    b=[F(1)]
    for _ in range(n):b=pm(b,a)
    return b

def pe(a,x):
    y=F(0)
    for z in reversed(a):y=y*x+z
    return y

def affine(a,l,r):
    b=[F(0)]
    for i,x in enumerate(a):b=pa(b,ps(pp([l,r-l],i),x))
    return b

def bernstein(a,l=F(0),r=F(1)):
    p=affine(a,l,r);n=len(p)-1
    b=[sum((p[i]*F(comb(j,i),comb(n,i)) for i in range(j+1)),F(0)) for j in range(n+1)]
    rebuilt=[F(0)]
    for j,x in enumerate(b):
        rebuilt=pa(rebuilt,ps(pm([F(0)]*j+[F(1)],pp([F(1),F(-1)],n-j)),x*comb(n,j)))
    assert rebuilt==p and all(x>0 for x in b)
    return {'interval':[l,r],'degree':n,'coefficients':b,'back_expansion':p}

def hinge_simplex(values,t):
    """Exact mean of (ell-t)_+ on a simplex, via confluent divided differences.
    Repeated affine values use exact derivatives; no perturbation is introduced.
    """
    v=sorted(values);n=len(v)-1;p=n+1
    d=[max(x-t,F(0))**p for x in v]
    for k in range(1,n+1):
        d=[(F(comb(p,k))*max(v[i]-t,F(0))**(p-k) if v[i+k]==v[i]
            else (d[i+1]-d[i])/(v[i+k]-v[i])) for i in range(len(d)-1)]
    assert d[0]>=0
    return d[0]/p

def hinge_cone(z,t):
    return hinge_simplex([F(1),z,z,z],t)

def arithmetic():
    tau=F(51,25);M=F(13,15);t=F(11,8)
    z=tau/M;u=z-1;r=(t-1)/u
    lhs=M*hinge_cone(z,t)/3;rhs=(1-t/4)**4
    assert z==F(153,65) and u==F(88,65) and r==F(195,704)
    assert lhs==M*u*(3-4*r+r**4)/12
    assert lhs-rhs==F(29035697,279130931200)>0
    H=4*M/3-1
    assert H==F(7,45)
    assert H>F(2,31) and H*H==F(49,2025)
    # Exact integration of the cone formula: no quadrature or sampled proof.
    for s in [F(0),F(1,4),F(1),F(11,8),F(2),F(3),F(4)]:
        if 1<=s<=z:
            r0=(s-1)/(z-1)
            direct=3*((1-s)*(1-r0**3)/3+(z-1)*(1-r0**4)/4)
            assert direct==hinge_cone(z,s)
    return {'tau':tau,'mass_cutoff':M,'threshold':t,'boundary_mean':z,
            'radial_lower_endpoint':r,'cone_lower_tail':lhs,'universal_upper_tail':rhs,
            'strict_gap':lhs-rhs,'triangular_pair_h_cutoff':H,
            'pair_product_cutoff':H*H,'pair_sum_cutoff':2*H,
            'diagonal_sum_cutoff':4*M}

def scalar_control():
    """A formal scalar point, explicitly NOT a polytope or a full moment system."""
    h=F(1,5);m1=m2=F(2,5);m=m1+m2;T=F(51,25)
    a=b=F(46,15);c=d=F(91,60);q=a+b
    lam1=m1*(a+b+c)/3;lam2=m2*(a+b+d)/3
    assert lam1==lam2==F(51,50) and lam1+lam2==T
    assert all(3*h/4<=mi<=F(3,4) for mi in [m1,m2])
    assert m<=3*(1+h)/4 and m>F(37,50) and h>F(2,31)
    assert all(0<=v<=4 for v in [a,b,c,d]) and a>=4*T-8 and b>=4*T-8
    # c3 >= R(1/2)=132/119, hence each individual trace is below c3.
    assert lam1<F(132,119)
    gx=m1/(3*h);gy=m2/(3*h);gz=F(0)
    scalar_mean=a+(d-a)*gx+(c-a)*gy+(b-a)*gz
    assert scalar_mean==1
    def tri(x,y,z):return (x*x+y*y+z*z+x*y+x*z+y*z)/6
    surface=m1*tri(a,b,c)+m2*tri(a,b,d)+(3-T)**2/(3-m)
    assert surface==F(567041,99000)<6
    L=(a+b+c+d)/4;B2=(a*a+b*b+c*c+d*d+(a+b+c+d)**2)/20
    tet_lower=h*B2+(1-h*L)**2/(1-h)
    assert h*L<1 and tet_lower==F(2075221,1440000)<F(8,5)
    # Every partial cut 0<k<=1 is legal: t=1-3k/4 >=1/4.
    k=[F(0),F(1)];one=[F(1)];t=pa(one,ps(k,-3*h/m))
    f=[F(0),F(0),F(3),F(-2)];I=[F(0),F(0),F(0),F(2),F(-3,2)]
    Z=pa(f,ps(I,-3*h/m))
    J=pa(ps([F(0),F(0),F(3,2),F(-2),F(3,4)],q),
         ps([F(0),F(0),F(0),F(1),F(-3,4)],c+d))
    omk=pa(one,ps(k,-1))
    A=pa(pa(pm(t,t),pm(t,omk)),pm(omk,omk))
    B=pm(k,pa(t,ps(omk,2)))
    brace=pa(pa(ps(A,m*q),ps(B,3*T-m*q)),
             ps(pm(pa(one,ps(t,-1)),pa(ps(t,2),omk)),m))
    U=pa(one,ps(f,-h));W=pa(one,ps(J,-h));D=pm(U,W)
    N=ps(pm(pm(k,brace),pa(pm(t,U),ps(Z,h))),F(1,3))
    DN=pa(D,ps(N,-1))
    certificates=[bernstein(U),bernstein(W),
                  bernstein(DN,F(0),F(1,2)),bernstein(DN,F(1,2),F(1))]
    assert pe(t,F(1))==F(1,4)
    assert pe(N,F(1))/pe(D,F(1))==F(91,400)
    # All cuts are strictly below 1 <= c3, but the new cone test rejects the point.
    theta=F(11,8);weak_lower=m*hinge_cone(T/m,theta)/3
    exact_pair_lower=(m1*hinge_simplex([F(1),a,b,c],theta)
                      +m2*hinge_simplex([F(1),a,b,d],theta))/3
    upper=(1-theta/4)**4
    assert exact_pair_lower>=weak_lower>upper
    return {'status':'FORMAL_SCALAR_POINT_NOT_A_BODY_OR_FULL_PHYSICAL_MOMENT_SYSTEM',
            'h':h,'m1':m1,'m2':m2,'T':T,'facet_values':[a,b,c,d],
            'lambda1':lam1,'lambda2':lam2,'formal_centroid':[gx,gy,gz],
            'affine_centroid_identity':scalar_mean,'surface_second_lower':surface,
            'surface_margin':6-surface,'tetrahedron_second_lower':tet_lower,
            'tetrahedron_second_margin':F(8,5)-tet_lower,
            'cut_numerator':N,'cut_denominator':D,'all_cut_certificates':certificates,
            'cut_at_one':F(91,400),'new_weak_tail_gap':weak_lower-upper,
            'new_exact_triangular_tail_gap':exact_pair_lower-upper,
            'not_claimed_to_pass_all_previous_constraints':True}

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def scale(a,s):return tuple(x*s for x in a)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))

def polygon(points,ids,normal):
    drop=next(i for i in range(3) if normal[i]);keep=[i for i in range(3) if i!=drop]
    pts=sorted((points[k][keep[0]],points[k][keep[1]],k) for k in ids)
    def turn(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lo=[];hi=[]
    for z in pts:
        while len(lo)>=2 and turn(lo[-2],lo[-1],z)<=0:lo.pop()
        lo.append(z)
    for z in reversed(pts):
        while len(hi)>=2 and turn(hi[-2],hi[-1],z)<=0:hi.pop()
        hi.append(z)
    cyc=[z[2] for z in lo[:-1]+hi[:-1]]
    assert len(cyc)>=3
    if dot(cross(sub(points[cyc[1]],points[cyc[0]]),sub(points[cyc[2]],points[cyc[0]])),normal)<0:cyc.reverse()
    j=cyc.index(min(cyc));return tuple(cyc[j:]+cyc[:j])

def geometry(raw):
    planes={}
    for i,j,k in combinations(range(len(raw)),3):
        n=cross(sub(raw[j],raw[i]),sub(raw[k],raw[i]))
        if n==ZERO:continue
        b=dot(n,raw[i]);ss=[dot(n,x)-b for x in raw]
        if all(v==0 for v in ss):continue
        if all(v<=0 for v in ss):pass
        elif all(v>=0 for v in ss):n=scale(n,-1);b=-b
        else:continue
        ids=tuple(i for i,x in enumerate(raw) if dot(n,x)==b)
        planes.setdefault(ids,(n,b))
    facets=sorted((polygon(raw,ids,n),n,b) for ids,(n,b) in planes.items())
    V=F(0);moment=ZERO
    for cyc,n,b in facets:
        a=raw[cyc[0]]
        for j in range(1,len(cyc)-1):
            c=raw[cyc[j]];d=raw[cyc[j+1]];v=det(a,c,d)/6
            V+=v;moment=add(moment,scale(add(add(a,c),d),v/4))
    assert V>0
    g=scale(moment,1/V)
    assert all(dot(n,g)<b for cyc,n,b in facets)
    edges=sorted({tuple(sorted((cyc[j],cyc[(j+1)%len(cyc)]))) for cyc,n,b in facets for j in range(len(cyc))})
    vertices=sorted({v for cyc,n,b in facets for v in cyc})
    assert len(vertices)-len(edges)+len(facets)==2
    return V,g,facets,edges,vertices

def actual_control(name,raw,ell):
    raw=[tuple(map(F,p)) for p in raw];ell=tuple(map(F,ell))
    V,g,facets,edges,vertices=geometry(raw)
    mu=ell[0]+dot(ell[1:],g);assert mu>0
    vals=[(ell[0]+dot(ell[1:],x))/mu for x in raw]
    assert all(0<=x<=4 for x in vals)
    facet_data=[];all_cones=[]
    for cyc,n,b in facets:
        cones=[];mass=F(0);lam=F(0)
        for j in range(1,len(cyc)-1):
            ids=(cyc[0],cyc[j],cyc[j+1])
            w=det(*(sub(raw[i],g) for i in ids))/(6*V)
            assert w>0
            vs=[F(1)]+[vals[i] for i in ids]
            cones.append((w,vs));all_cones.append((w,vs));mass+=3*w
            lam+=w*sum((vals[i] for i in ids),F(0))
        facet_data.append({'cycle':cyc,'mass':mass,'trace':lam,'cones':cones})
    assert sum((f['mass'] for f in facet_data),F(0))==3
    assert sum((f['trace'] for f in facet_data),F(0))==3
    assert sum((w*sum(vs,F(0))/4 for w,vs in all_cones),F(0))==1
    thresholds=list(map(F,[0,1,2,3,4]))+[F(1,4),F(1,2),F(11,8),F(3,2)]
    thresholds=sorted(set(thresholds));checks=[];nf=len(facets)
    subsets=sorted({tuple(i for i in range(nf) if mask>>i&1) for mask in range(1,(1<<nf)-1)})
    for theta in thresholds:
        body_tail=sum((w*hinge_simplex(vs,theta) for w,vs in all_cones),F(0))
        universal=max(1-theta/4,F(0))**4
        assert body_tail<=universal
        for ids in subsets:
            m=sum((facet_data[i]['mass'] for i in ids),F(0))
            T=sum((facet_data[i]['trace'] for i in ids),F(0))
            selected=sum((w*hinge_simplex(vs,theta) for i in ids for w,vs in facet_data[i]['cones']),F(0))
            jensen=m*hinge_cone(T/m,theta)/3
            other=(3-m)*hinge_cone((3-T)/(3-m),theta)/3
            assert 0<=jensen<=selected<=body_tail<=universal
            assert jensen+other<=body_tail
            if T>=F(51,25):assert m>F(13,15)
        checks.append({'threshold':theta,'actual_body_tail':body_tail,'universal_upper':universal})
    triangles=[]
    for i,j in combinations(range(nf),2):
        ci=set(facets[i][0]);cj=set(facets[j][0])
        if len(ci)!=3 or len(cj)!=3 or len(ci&cj)!=2:continue
        ids=sorted(ci|cj);p=[raw[v] for v in ids]
        h=abs(det(sub(p[1],p[0]),sub(p[2],p[0]),sub(p[3],p[0])))/(6*V)
        m=facet_data[i]['mass']+facet_data[j]['mass'];T=facet_data[i]['trace']+facet_data[j]['trace']
        assert 0<h<=1 and m<=3*(1+h)/4
        if T>=F(51,25):assert h>F(7,45)
        triangles.append({'facets':[i,j],'h':h,'mass':m,'T':T})
    return {'name':name,'status':'TRUE_GEOMETRIC_CONTROL_NOT_A_110_WITNESS',
            'raw_points':raw,'raw_ell':ell,'own_center':g,'volume':V,
            'true_facets':[x[0] for x in facets],'true_edges':edges,
            'f_vector':[len(vertices),len(edges),nf],'normalized_values':vals,
            'masses':[x['mass'] for x in facet_data],'traces':[x['trace'] for x in facet_data],
            'tail_checks':checks,'subset_count':len(subsets),
            'all_subset_threshold_tests':len(subsets)*len(thresholds),
            'adjacent_triangular_pairs':triangles}

def serialize(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:serialize(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [serialize(v) for v in x]
    return x

def report():
    tet=[(0,0,0),(0,0,1),(0,1,0),(1,0,0)]
    cube=list(product([-1,1],repeat=3))
    octa=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    r=F(2);e=F(1,100);z=-(2*r-1)/2
    seven=tet+[(r-e,r+e,z),(r+e,r-e,z),(r,r,z+e)]
    controls=[actual_control('tetrahedron_root_CD',tet,(1,-1,-1,0)),
              actual_control('cube',cube,(1,1,0,0)),
              actual_control('octahedron',octa,(1,1,0,0)),
              actual_control('seven_vertex_genuine_root_triangle',seven,(4,-1,-1,0))]
    return {'identity':IDENTITY,'arithmetic':arithmetic(),'scalar_control':scalar_control(),
            'actual_controls':controls,'C_lower_bound_unchanged':34,
            'new_complete_incidence_exclusion':False,'exact_minimum_found':False,
            'analytic_inputs':'Brunn--Minkowski, layer-cake, cone disintegration and the preserved joint triangular mass theorem. See proof material.'}

def main():
    assert len(sys.argv)==2 and sys.argv[1] in ('build','check')
    obj=report();data=(json.dumps(serialize(obj),sort_keys=True,indent=2)+'\n').encode()
    path=Path(OUTPUT)
    if sys.argv[1]=='build':path.write_bytes(data)
    else:assert path.read_bytes()==data
    count=sum(x['all_subset_threshold_tests'] for x in obj['actual_controls'])
    coefficients=sum(len(x['coefficients']) for x in obj['scalar_control']['all_cut_certificates'])
    print('CONE_TAIL_MASS_13_15_H_7_45_EXACT_PASS 29035697/279130931200 7/45')
    print('OLD_SECOND_MOMENTS_ALL_PARTIAL_CUTS_SCALAR_CONTROL_PASS',coefficients)
    print('NEW_CONE_TAIL_STRICTLY_REJECTS_SCALAR_CONTROL_PASS')
    print('ACTUAL_BODY_ALL_FACET_SUBSET_TAIL_CONTROLS_PASS',len(obj['actual_controls']),count)
    print('CONE_TAIL_RECOVERY_PASS',len(data),hashlib.sha256(data).hexdigest())
if __name__=='__main__':main()
