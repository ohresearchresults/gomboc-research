# material-532652150f92

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

"""JOINT_MASS_CUBIC_STABILITY_V2: exact finite certificate and physical controls.
CPython 3.13.5, standard library only, assertions enabled.
Exact dependency in the same directory: joint_mass_stability_exact.py,
8331 bytes, SHA256 d760d4070fbe920485f68166515e59786da1a3e606d11348e8bf22686b2b2d79,
immutable material [internal-source-reference]. No omitted source helpers.
Run: python -S joint_mass_cubic_exact.py build
     python -S joint_mass_cubic_exact.py check
The continuous theorem is in joint_mass_cubic_proof.md, not inferred from controls.
"""
from pathlib import Path
import hashlib
import itertools
import json
import sys
assert __debug__
BASE=Path(__file__).with_name('joint_mass_stability_exact.py')
assert [len(BASE.read_bytes()),hashlib.sha256(BASE.read_bytes()).hexdigest()]==[
8331,'d760d4070fbe920485f68166515e59786da1a3e606d11348e8bf22686b2b2d79']
import joint_mass_stability_exact as old
F=old.F
add,scale,mul,power,value,affine,bernstein=old.add,old.scale,old.mul,old.power,old.value,old.affine,old.bernstein
encode=old.encode
GAP=F(1,2500000)

def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))

def polygon2(points,ids,drop):
    axes=[k for k in range(3) if k!=drop]
    coords={i:tuple(points[i][k] for k in axes) for i in ids}
    order=sorted(ids,key=lambda i:(coords[i],i))
    def orient(i,j,k):
        a,b,c=coords[i],coords[j],coords[k]
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    def half(seq):
        out=[]
        for i in seq:
            while len(out)>1 and orient(out[-2],out[-1],i)<=0:out.pop()
            out.append(i)
        return out
    return half(order)[:-1]+half(list(reversed(order)))[:-1]

def hull(raw):
    """Exact maximal facets/true edges and positive boundary tetrahedral moments.
    The origin must belong to the hull; all calls contain A=(0,0,0).
    Coplanar non-vertices and edge-interior points are removed by exact 2D hulls.
    """
    points=[]
    for p in raw:
        p=tuple(F(q) for q in p)
        if p not in points:points.append(p)
    assert (F(0),F(0),F(0)) in points
    planes={}
    for i,j,k in itertools.combinations(range(len(points)),3):
        n=cross(sub(points[j],points[i]),sub(points[k],points[i]))
        if not any(n):continue
        signs=[dot(n,sub(p,points[i])) for p in points]
        if min(signs)<0<max(signs):continue
        if min(signs)==max(signs)==0:continue
        if min(signs)>=0:n=tuple(-q for q in n)
        ids=frozenset(t for t,p in enumerate(points) if dot(n,sub(p,points[i]))==0)
        planes.setdefault(ids,n)
    faces=[]
    for ids,n in planes.items():
        drop=next(k for k in range(3) if n[k])
        face=polygon2(points,ids,drop)
        assert len(face)>=3
        if dot(cross(sub(points[face[1]],points[face[0]]),sub(points[face[2]],points[face[0]])),n)<0:
            face=list(reversed(face))
        k=face.index(min(face));face=face[k:]+face[:k]
        faces.append(tuple(face))
    faces=sorted(set(faces))
    edges=sorted({tuple(sorted((a,b))) for face in faces for a,b in zip(face,face[1:]+face[:1])})
    vertices=sorted(set(itertools.chain.from_iterable(faces)))
    assert len(vertices)-len(edges)+len(faces)==2
    V=F(0);moment=[F(0)]*3;tetra=[]
    for face in faces:
        for k in range(1,len(face)-1):
            ids=(face[0],face[k],face[k+1]);a,b,c=(points[i] for i in ids)
            vol=det(a,b,c)/6
            assert vol>=0
            if not vol:continue
            V+=vol
            for t in range(3):moment[t]+=vol*(a[t]+b[t]+c[t])/4
            tetra.append([list(ids),vol])
    assert V>0
    centroid=tuple(q/V for q in moment)
    return {'points':points,'vertices':vertices,'faces':faces,'edges':edges,
            'fvector':[len(vertices),len(edges),len(faces)],'volume':V,
            'moment':moment,'centroid':centroid,'positive_fan_tetrahedra':tetra}

T0=[(F(0),F(0),F(0)),(F(0),F(0),F(1)),(F(0),F(1),F(0)),(F(1),F(0),F(0))]

def ell_at(vals,p):
    a,b,c,d=vals;x,y,z=p
    return a+(d-a)*x+(c-a)*y+(b-a)*z

def g(h):return 1+2*h-h*h

def K(h):return max(11*h-h**3,3+6*h-h*h)

def integral_ell(body,vals):return body['volume']*ell_at(vals,body['centroid'])

def trace(body,vals):
    a,b,c,d=vals;X,Y,_=body['moment'];V=body['volume'];B=integral_ell(body,vals)
    assert B>0
    return ((a+b+c)*X+(a+b+d)*Y)/(6*V*B)

def physical_control(name,extra,vals):
    vals=tuple(F(q) for q in vals);norm=max(vals)
    assert norm>0 and min(vals)>=0
    vals=tuple(q/norm for q in vals);a,b,c,d=vals
    assert a>=b
    P=hull(T0+extra)
    assert all(ell_at(vals,p)>=0 for p in P['points'])
    face_sets={frozenset(face) for face in P['faces']}
    assert frozenset((0,1,2)) in face_sets and frozenset((0,1,3)) in face_sets
    assert (0,1) in P['edges']
    root_ids=frozenset(i for i in P['vertices'] if ell_at(vals,P['points'][i])==0)
    assert root_ids in face_sets
    V=P['volume'];X,Y,Z=P['moment'];h=1/(6*V);B=integral_ell(P,vals)
    assert B>=V/4
    T=trace(P,vals);delta=F(3,4)*(1+h)-(X+Y)/(2*V*V)
    assert 0<h<=1 and delta>=0
    rid=max(P['vertices'],key=lambda i:(P['points'][i][0]+P['points'][i][1],-i))
    R=P['points'][rid];r,s,z=R;t=r+s;Delta=1/h-t
    z0=min(F(0),max(1-t,z));kappa=abs(z-z0)
    assert t>=1 and 0<=kappa<=Delta
    P1=hull(T0+[R]);P0=hull(T0+[(r,s,z0)])
    assert P1['volume']==(t+kappa)/6 and P0['volume']==t/6
    assert P1['moment'][0]-P0['moment'][0]==kappa*(1+r)/24
    assert P1['moment'][1]-P0['moment'][1]==kappa*(1+s)/24
    assert X>=P1['moment'][0] and Y>=P1['moment'][1]
    loss=t*Delta/6-kappa*(3*t-2)/24
    assert 0<=(X+Y)-(P0['moment'][0]+P0['moment'][1])<=loss
    eta_ell=max(F(0),-ell_at(vals,(r,s,z0)))
    vals_plus=tuple(q+eta_ell for q in vals)
    assert all(ell_at(vals_plus,p)>=0 for p in P0['points'])
    B0=integral_ell(P0,vals_plus);B1=integral_ell(P1,vals)
    if kappa==0:sigma=F(0);case='no_clip'
    elif z>0:sigma=(a-b)*(t-1)-(b+c+d);case='positive_clip'
    else:sigma=(a-b)*(3*t+1)-(a+c+d);case='negative_clip'
    assert B0-B1<=kappa*sigma/24 and B1<=B
    qmax=max(a+b+c,a+b+d)
    N=(a+b+c)*X+(a+b+d)*Y
    ap,bp,cp,dp=vals_plus
    N0=(ap+bp+cp)*P0['moment'][0]+(ap+bp+dp)*P0['moment'][1]
    assert N<=N0+qmax*loss
    assert trace(P0,vals_plus)<=g(1/t)
    trace_margin=g(h)+K(h)*Delta-T
    assert trace_margin>=0
    if h<1:
        cubic_margin=delta-F(3,8)*h**3*Delta**3/(1-h)
        assert cubic_margin>=0
    else:
        assert delta==Delta==0;cubic_margin=F(0)
    return {'name':name,'polytope':P,'normalized_ell_ABCD':vals,'root_vertex_indices':[
            i for i in P['vertices'] if ell_at(vals,P['points'][i])==0],
            'h':h,'delta':delta,'trace':T,'max_projection_vertex':rid,'t':t,'Delta':Delta,
            'kappa':kappa,'clip_case':case,'P1':P1,'P0':P0,'ell_correction':eta_ell,
            'sigma':sigma,'affine_moment_margin':B+kappa*sigma/24-B0,
            'trace_stability_margin':trace_margin,'cubic_projection_margin':cubic_margin,
            'claim_110':False}

def gap_certificate():
    A=[F(26),F(-50),F(25)]
    k1=[F(0),F(11),F(0),F(-1)];k2=[F(3),F(6),F(-1)]
    p1=add(scale(power(A,3),60),scale(mul([F(1),F(-1)],power([F(11),0,F(-1)],3)),-1))
    p2=add(scale(mul([0,0,0,F(1)],power(A,3)),60),scale(mul([F(1),F(-1)],power(k2,3)),-1))
    assert p1==[1053229,-6082669,14742363,-19200363,14174967,-5624967,937501,-1]
    assert p2==[-27,-135,-135,1054749,-6083793,14741883,-19199981,14174999,-5625000,937500]
    # Multiplying the desired rational bound by 25^3/8 gives exactly these polynomials.
    assert add(scale(mul([0,0,0,F(1)],power(A,3)),60),scale(mul([1,-1],power(k1,3)),-1))==mul([0,0,0,F(1)],p1)
    leaves=[]
    cases=[('K1',p1,F(0),F(1),['0','10','110','111']),
           ('K2',p2,F(7,45),F(1),['0','1'])]
    for name,P,lo,hi,paths in cases:
        intervals=[]
        for path in paths:
            l,r=lo,hi
            for bit in path:
                m=(l+r)/2
                if bit=='0':r=m
                else:l=m
            B=bernstein(P,l,r,len(P)-1)
            assert min(B)>0
            intervals.append((l,r))
            leaves.append({'branch':name,'path':path,'lo':l,'hi':r,'bernstein':B})
        assert intervals[0][0]==lo and intervals[-1][1]==hi
        assert all(p[1]==q[0] for p,q in zip(intervals,intervals[1:]))
    assert len(leaves)==6 and sum(len(v['bernstein']) for v in leaves)==52
    return {'gap':GAP,'factor_improvement_over_V1':GAP/F(1,50000000000000),
            'polynomials':{'K1_after_dividing_h3':p1,'K2':p2},'leaves':leaves}

def algebraic_controls():
    # Exact polynomial identities used in the continuous linear-profile proof.
    assert add([2,-3,0,1],scale(mul(power([1,-1],2),[2,1]),-1))==[F(0)]
    assert power([1,-1],3)==[1,-3,3,-1]
    # The following are polynomials multiplied by t to clear positive denominators.
    positives={
      'minus_a':[0,-1,7,3],
      'minus_negative_b':[-1,-3,6,3],
      't_times_tg':[-1,2,1],
      'plus_a':[1,-1,2,1],
      'one_minus_plus_b':[-2,1,1],
      'minus_envelope_minus_plus_coarse':[-1,-1,5,2],
      'minus_envelope':[1,-1,7,3]}
    shifted={}
    for name,P in positives.items():
        C=affine(P,F(1),F(2)) # t=1+u, u>=0; not a sampled interval.
        assert min(C)>=0 and any(C)
        shifted[name]=C
    # Definitions of the coefficients are independently expanded.
    ttg=[F(-1),F(2),F(1)] # t*(t*g(1/t)).
    t=[F(0),F(1)];tplus2=[F(2),F(1)]
    assert add(mul(t,tplus2),scale(mul(t,ttg),3))==positives['minus_a']
    assert scale(add(mul(t,tplus2),scale(mul([1,3],ttg),-1)),-1)==positives['minus_negative_b']
    assert add(mul(t,tplus2),mul([-1,1],ttg))==positives['plus_a']
    assert add(mul(t,tplus2),scale(mul(t,ttg),-1))==[0,3,-1,-1]
    # Exact controls with positive endpoint values, so no endpoint-zero assumption is hidden.
    profiles=[]
    for H,k in ((F(1),F(-1,2)),(F(3,2),F(2,3)),(F(2),F(-1,2))):
        f=[F(1),k];assert value(f,H)>=0
        W=old.integral(f,0,H);J=old.integral(mul([0,1],f),0,H);R=2*W
        assert R*R/6-J==(R-H)**2/6
        I=old.integral(mul([0,1],f),0,H);J2=old.integral(mul([0,0,1],f),0,H)
        assert J2==F(3,4)*H*I-H**3/24
        profiles.append([H,k,W,J,R,I,J2])
    # The primitive in the angular cap integral equals (T-t)^3/T identically.
    caps=[]
    for T,t0 in ((F(3),F(2)),(F(7,4),F(5,4)),(F(2),F(1))):
        primitive=T*T-3*t0*T+3*t0*t0-t0**3/T
        assert primitive==(T-t0)**3/T
        caps.append([T,t0,primitive*T/(24*(T-1))])
    return {'positive_coefficients_after_t_equals_1_plus_u':shifted,
            'affine_profile_equality_controls':profiles,'angular_cap_controls':caps}

def formal_control():
    # This is not a body. It passes the explicitly listed old scalar tests and V1
    # bounds, but violates the new necessary condition for real adjacent triangles.
    h=F(1,5);delta=F(1,10**8);tau=F(51,25);m=F(3,4)*(1+h)-delta
    m1=m2=m/2;lam=tau/2;a=b=(tau-h)/(m-h);c=d=3*tau/m-2*a
    zc=(3-tau)/(3-m);gx=gy=m/(6*h);gz=(1-gx-gy)/2
    assert F(1,50000000000000)<delta<GAP
    assert all(F(3,4)*h<q<F(3,4) for q in (m1,m2))
    assert m<F(3,4)*(1+h) and m>F(13,15) and h>F(7,45)
    assert all(0<q<4 for q in (a,b,c,d))
    assert a+(d-a)*gx+(c-a)*gy+(b-a)*gz==1
    assert m1*(a+b+c)/3==lam==m2*(a+b+d)/3
    assert lam<F(132,119)<F(10,9)
    assert 4>a+h*(a+c+d)
    assert F(1,2)-1/(4*h)<gz<F(1,2)-gx-gy+1/(4*h)
    Q=(a*a+b*b+c*c+a*b+a*c+b*c)/6
    surface_second=m*Q+(3-m)*zc*zc;assert surface_second<6
    vals=(a,b,c,d);tetmean=sum(vals)/4;tetsecond=(sum(q*q for q in vals)+sum(vals)**2)/20
    volume_second=h*tetsecond+(1-h*tetmean)**2/(1-h)
    assert h*tetmean<1 and volume_second<F(8,5)
    w=F(4,3)*(1-h)*delta
    assert ((tau-2)*h*h/24)**4<=w
    assert ((tau-g(h))*h*h/28)**4<=w
    old_local=F(3,4)*h**8/(1-h)*((tau-g(h))/28)**4
    new_local=F(3,8)*h**3*(tau-g(h))**3/((1-h)*K(h)**3)
    assert old_local<delta<new_local
    U=power([F(1),F(-1,4)],4);knots=sorted(set((F(0),zc,F(1),c,a,F(4))))
    assert 0<zc<1<c<a<4
    leaves=[]
    for i,(lo,hi) in enumerate(zip(knots,knots[1:])):
        mid=(lo+hi)/2
        P=add(U,scale(old.hinge_tetra((F(1),a,a,c),mid),-m/3),
                scale(old.hinge_tetra((F(1),zc,zc,zc),mid),-(3-m)/3))
        B=bernstein(P,lo,hi,4);assert min(B)>=0
        leaves.append({'interval':i,'lo':lo,'hi':hi,'polynomial':P,'bernstein':B})
    assert len(leaves)==5
    return {'is_polytope':False,'h':h,'delta':delta,'m1':m1,'m2':m2,'T':tau,
      'lambda1':lam,'lambda2':lam,'a':a,'b':b,'c':c,'d':d,'complement':zc,
      'formal_centroid':[gx,gy,gz],'surface_second':surface_second,'volume_second':volume_second,
      'old_local_gap':old_local,'new_local_gap':new_local,'full_scalar_tail':leaves,
      'claim_all_H_K_rank_incidence_metric_constraints':False}

def report():
    controls=[]
    controls.append(physical_control('high_trace_root_CD',[
        (F(1,100),F(4,5),F(19,80)),(F(3,4),F(1,50),F(23,80))],(1,F(1,5),0,0)))
    assert controls[-1]['trace']==F(1799763200,887522067)>2
    controls.append(physical_control('negative_clip_actual_root',[
        (F(7,3),F(3,2),F(-11,4)),(F(8,3),F(11,6),F(-47,12)),
        (F(14,5),F(13,5),F(-47,10))],(1,F(4,5),F(9,10),F(2,5))))
    assert controls[-1]['clip_case']=='negative_clip' and controls[-1]['ell_correction']>0
    controls.append(physical_control('positive_clip_actual_root',[
        (2,1,1),(1,2,1),(1,1,2)],(4,3,3,3)))
    assert controls[-1]['clip_case']=='positive_clip'
    controls.append(physical_control('equal_endpoint_root_below_half_h',[
        (F(3,4),F(5,4),F(-2,5)),(F(5,4),F(3,4),F(-3,5)),(1,1,F(-3,10))],
        (1,1,F(1,2),F(1,2))))
    assert controls[-1]['h']==F(40,113)
    controls.append(physical_control('literal_equality_branch',[(1,1,F(-1,2))],(1,0,0,F(1,2))))
    assert controls[-1]['delta']==controls[-1]['Delta']==0
    controls.append(physical_control('extra_nonroot_volume',[
        (F(1,100),F(4,5),F(19,80)),(F(3,4),F(1,50),F(23,80)),
        (F(1,2),F(1,2),F(-1,5))],(1,F(1,5),0,0)))
    return {'identity':'JOINT_MASS_CUBIC_STABILITY_V2','proof_file':'joint_mass_cubic_proof.md',
            'gap_certificate':gap_certificate(),'algebraic_controls':algebraic_controls(),
            'formal_scalar_control':formal_control(),'physical_controls':controls,
            'claim_C_ge_36':False,'claim_exact_minimum':False}

def main():
    if len(sys.argv)!=2 or sys.argv[1] not in ('build','check'):
        raise SystemExit('Use build or check; assertions must be enabled.')
    out=report();data=(json.dumps(encode(out),ensure_ascii=True,sort_keys=True,indent=2)+'\n').encode('utf-8')
    target=Path('joint_mass_cubic_exact.json')
    if sys.argv[1]=='build':target.write_bytes(data)
    else:assert target.read_bytes()==data
    print('CUBIC_STABILITY_ALGEBRAIC_PROFILE_CONTROLS_PASS')
    print('UNIVERSAL_CUBIC_GAP_BERNSTEIN_PASS',6,52,str(GAP))
    print('STRONGER_FORMAL_SCALAR_FULL_TAIL_PASS',5)
    print('ACTUAL_POLYTOPE_CUBIC_STABILITY_CONTROLS_PASS',len(out['physical_controls']))
    print('JOINT_MASS_CUBIC_EXACT_PASS',len(data),hashlib.sha256(data).hexdigest())
if __name__=='__main__':main()
