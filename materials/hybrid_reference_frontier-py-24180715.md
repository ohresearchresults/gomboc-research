# material-241807152d60

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Canonical top-triangle references and exact template-blind H5 control.
Requires the two preserved hybrid_exact_*.py source files; standard library only.
"""
from fractions import Fraction as F
from itertools import combinations
import json,hashlib,sys
from pathlib import Path
import hybrid_exact_region as h
from hybrid_exact_control import dot,sub,add,mul,cross,mv,det,inv,quad,const,conv,strings
D2=[[F(2),F(-1)],[F(-1),F(2)]]
DI=[[F(2,3),F(1,3)],[F(1,3),F(2,3)]]

def body(theta):
    _,zz,dd,kk,planar,nn,hh,HH,_=h.build([(x,x) for x in theta])
    z=[conv(v) for v in zz];D=const(dd);K=conv(kk);g=mul(1/D,K)
    v=[sub(a,g) for a in z];ns=[conv(n) for n in nn];hs=[const(a) for a in hh]
    poles=[mul(D/const(a),n) for a,n in zip(HH,ns)]
    assert D>0 and all(const(a)>0 for a in HH)
    found=set()
    for i,j,k in combinations(range(10),3):
        no=cross(sub(z[j],z[i]),sub(z[k],z[i]))
        if not any(no):continue
        off=dot(no,z[i]);sl=[off-dot(no,a) for a in z]
        if min(sl)<0<max(sl):continue
        found.add(tuple(t for t,s in enumerate(sl) if not s))
    assert found=={tuple(sorted(f)) for f in h.FACES}
    edge={}
    for f,face in enumerate(h.FACES):
        for j,i in enumerate(face):
            a,b=sorted((i,face[(j+1)%len(face)]));edge.setdefault((a,b),[]).append(f)
    assert len(edge)==17 and all(len(fs)==2 for fs in edge.values())
    # Same true body, independent positive apex-7 moment integral.
    apex=z[7];D2_=F(0);K2=[F(0)]*3
    for face in h.FACES:
        if 7 in face:continue
        a=z[face[0]]
        for j in range(1,len(face)-1):
            b,c=z[face[j]],z[face[j+1]]
            d=dot(sub(a,apex),cross(sub(b,apex),sub(c,apex)))
            assert d>0
            D2_+=d;K2=add(K2,mul(d/4,add(add(apex,a),add(b,c))))
    assert D2_==D and K2==K
    return z,v,poles,D,g,edge,planar

def guards(z,poles,g,planar,alpha):
    gamma=g[2];upper=[];lower=[F(0)];rguards=[];aguards=[]
    for n0,h0,t0,f in planar:
        n=conv(n0);hh=const(h0)
        for i in range(7):
            for j in range(7,10):
                intercept=(1-gamma)*hh-dot(n,g[:2])+gamma*dot(n,z[j][:2])
                slope=-dot(n,g[:2])+(1-gamma)*dot(n,z[i][:2])+gamma*dot(n,z[j][:2])
                rguards.append(intercept+alpha*slope)
                if slope<0:upper.append((-intercept/slope,[f,i,j]))
                elif slope>0:lower.append(-intercept/slope)
                else:assert intercept>0
    for f in range(1,9):
        for j in range(7,10):aguards.append(1+dot(poles[f],sub(z[j],g)))
    assert min(rguards)>0 and min(aguards)>0
    cap,witness=min(upper);floor=max(lower)
    assert floor<alpha<cap and 0<alpha<1
    beta=gamma*(1+alpha)/(1-gamma);r=beta/alpha
    assert F(1,4)<gamma<F(4,9) and alpha>=1-2*gamma and alpha**2<gamma and r<2
    assert cap**2<gamma
    return dict(alpha=alpha,alpha_max=cap,alpha_max_witness=witness,alpha_lower=floor,
                R_min=min(rguards),A_min=min(aguards),turn_r=r,
                maximal_required_product=gamma/(gamma-cap**2))

def physical(v,poles,edges):
    M=[[F(a) for a in row] for row in [[5,1,2],[1,3,-1],[2,-1,4]]];N=inv(M)
    assert M[0][0]>0 and M[0][0]*M[1][1]-M[0][1]**2>0 and det(M)>0
    assert [[dot(M[i],[N[k][j] for k in range(3)]) for j in range(3)] for i in range(3)]==[[int(i==j) for j in range(3)] for i in range(3)]
    U=[True]*10;S=[True]*9;H=[];rows=[]
    for (i,j),(f,k) in sorted(edges.items()):
        a=dot(v[i],mv(M,sub(v[j],v[i])));b=dot(v[j],mv(M,sub(v[i],v[j])))
        c=dot(poles[f],mv(N,sub(poles[k],poles[f])));d=dot(poles[k],mv(N,sub(poles[f],poles[k])))
        assert all((a,b,c,d))
        U[i]&=a<0;U[j]&=b<0;S[f]&=c<0;S[k]&=d<0
        if max(a,b,c,d)<0:H.append([i,j])
        rows.append(dict(edge=[i,j],facets=[f,k],primitives=[a,b,c,d]))
    U=[i for i,t in enumerate(U) if t];S=[i for i,t in enumerate(S) if t]
    assert len(S)+len(U)-len(H)==2
    return dict(M=M,N=N,S=S,U=U,H=H,physical_weak=0,primitives=rows)

def canonical(theta,v,poles,g):
    lam=theta[4];H=1-g[2];m=sub([lam/3]*2,g[:2]);e=2*lam**2/9;s2=(g[2]/H)**2
    rs=[];aa=[]
    for vi in v:
        w=sub(vi[:2],mul(vi[2]/H,m));rs.append(quad(w,DI));aa.append((vi[2]/H)**2)
    assert rs[7:]==[e]*3 and aa[:7]==[s2]*7 and aa[7:]==[F(1)]*3
    ell=[quad(q[:2],D2) for q in poles]
    b=[(dot(m,q[:2])+H*q[2])**2 for q in poles]
    assert all(x>=0 for x in ell+b+rs) and ell[0]==0 and b[0]==(H/g[2])**2
    # Exact polynomial matrix inverse and norm identities for all k>0.
    k=h.P({(1,0,0,0,0):F(1)})
    C=[[k*D2[i][j]+m[i]*m[j] for j in range(2)]+[h.P(H*m[i])] for i in range(2)]
    C.append([h.P(H*m[0]),h.P(H*m[1]),h.P(H*H)])
    dm=mv(DI,m)
    E=[[h.P(H*H*DI[i][j]) for j in range(2)]+[h.P(-H*dm[i])] for i in range(2)]
    E.append([h.P(-H*dm[0]),h.P(-H*dm[1]),k+dot(m,dm)])
    for i in range(3):
        for j in range(3):
            assert (sum((C[i][r]*E[r][j] for r in range(3)),h.P(0))-int(i==j)*k*H*H).zero()
    for i,vi in enumerate(v):assert (h.quad(vi,E)-H*H*(rs[i]+aa[i]*k)).zero()
    for f,q in enumerate(poles):assert (h.quad(q,C)-(ell[f]*k+b[f])).zero()
    R=max(rs[:7]);Rindex=rs[:7].index(R)
    # All possible breakpoints for the two primal pieces and nine polar lines.
    points={F(0)}
    if R>e:points.add((R-e)/(1-s2))
    for f,j in combinations(range(9),2):
        if ell[f]!=ell[j]:
            t=(b[j]-b[f])/(ell[f]-ell[j])
            if t>0:points.add(t)
    points=sorted(points);intervals=[]
    for j,l in enumerate(points):
        r=points[j+1] if j+1<len(points) else None
        sample=(l+r)/2 if r is not None else l+1
        pi=max(range(2),key=lambda i:([F(1),s2][i]+[e,R][i]/sample))
        f=max(range(9),key=lambda f:ell[f]*sample+b[f])
        a=[F(1),s2][pi];rv=[e,R][pi]
        A=a*b[f]+rv*ell[f];B=a*ell[f];D=rv*b[f]
        # Exact quintic coefficient list in ascending powers.
        # 4(k+e)(B k^2-D)^2-e(B k^2+A k+D)^2.
        coef=[3*e*D*D,4*D*D-2*e*A*D,-10*e*B*D-e*A*A,
              -8*B*D-2*e*A*B,3*e*B*B,4*B*B]
        polynomial=4*(k+e)*(B*k**2-D)**2-e*(B*k**2+A*k+D)**2
        assert (polynomial-sum((c*k**j for j,c in enumerate(coef)),h.P(0))).zero()
        intervals.append(dict(left=l,right=r,primal=pi,polar=f,A=A,B=B,D=D,stationary_quintic=coef))
    # A derivative sign test avoiding square roots, valid on active intervals.
    def sign_der(k0,rec):
        A,B,D=rec['A'],rec['B'],rec['D'];num=2*(B*k0*k0-D);den=B*k0*k0+A*k0+D
        if num<=0:return -1
        compare=num*num*(k0+e)-e*den*den
        return (compare>0)-(compare<0)
    exact_min=None
    for j,t in enumerate(points[1:],1):
        left=intervals[j-1];right=intervals[j]
        sl=sign_der(t,left);sr=sign_der(t,right)
        if sl<=0<=sr:
            assert exact_min is None
            Gamma=max(1+e/t,s2+R/t)*max(ell[f]*t+b[f] for f in range(9))
            exact_min=dict(k=t,left_derivative_sign=sl,right_derivative_sign=sr,Gamma=Gamma,chi=e/t,
                           left_active=[left['primal'],left['polar']],right_active=[right['primal'],right['polar']])
    isolated=None
    if exact_min is None:
        for rec in intervals:
            lo=rec['left'];hi=rec['right']
            if sign_der(lo,rec)>=0:continue
            if hi is None:
                hi=lo+1
                while sign_der(hi,rec)<=0:hi=2*hi
            if sign_der(hi,rec)<=0:continue
            original=[lo,hi]
            for iteration in range(80):
                mid=(lo+hi)/2
                if sign_der(mid,rec)<0:lo=mid
                else:hi=mid
            assert sign_der(lo,rec)<0 and sign_der(hi,rec)>=0
            assert isolated is None
            isolated=dict(bracket=[lo,hi],iterations=80,active=[rec['primal'],rec['polar']],
                          source_interval=original,quintic=rec['stationary_quintic'])
    assert (exact_min is None)!=(isolated is None)
    return dict(height=H,shift=m,e=e,base_a=s2,base_R=R,base_R_vertex=Rindex,
                r=rs,a=aa,ell=ell,b=b,intervals=intervals,rational_global_minimum=exact_min,
                isolated_global_minimum=isolated)

def main():
    pi_lower=16*sum(((-1)**j*F(1,5)**(2*j+1)/F(2*j+1) for j in range(6)),F(0))-4*F(1,239)
    pi_upper=16*sum(((-1)**j*F(1,5)**(2*j+1)/F(2*j+1) for j in range(5)),F(0))-4*(F(1,239)-F(1,3*239**3))
    assert pi_lower>F(333,106) and pi_upper<F(22,7)
    fl=(1-(F(22,7)/20)**2/2)**20*(1-(F(22,7)/18)**2/2)**18
    assert fl>F(9,16)
    assert F(901,1000)**7<F(1,2)
    out=dict(version=1,finite_height_product_lower=F(9,16),exact_trigonometric_lower=fl,controls=[])
    for lam,alpha in [(F(87,1000),F(251,500)),(F(3,25),F(47,100))]:
        theta=[F(3,20)]*3+[F(9,20),lam]
        z,v,poles,D,g,edges,planar=body(theta)
        gd=guards(z,poles,g,planar,alpha)
        c=(1-g[2])/g[2];klo=F(9,16)*c**4
        assert klo>1
        lower=(klo+1)**2/(4*klo)
        blind_margin=lower-gd['maximal_required_product']
        if lam==F(3,25):
            assert blind_margin>F(5,4) and lower>F(109,20)
            assert gd['maximal_required_product']<F(421,100)
        ca=canonical(theta,v,poles,g)
        op=ca['rational_global_minimum']
        if op:
            ck=F(16,27)*op['Gamma']**2;chi=op['chi'];ceiling=F(21,2)
            load=4*ck*ceiling-(ck+1)**2*(1+chi)-(ck-1)**2*chi
            disc=load**2-4*(ck+1)**2*(ck-1)**2*chi*(1+chi)
            assert load>0 and disc>0
            assert ceiling<g[2]/(g[2]-alpha**2)
            op.update(product_ceiling=ceiling,ceiling_load=load,ceiling_discriminant=disc)
        rec=dict(theta=theta,volume=D/6,centroid=g,facet_cycles=h.FACES,vertices=z,poles=poles,
                 guards=gd,physical=physical(v,poles,edges),canonical=ca,
                 all_reference_template_floor=lower,all_reference_template_blind_margin=blind_margin)
        out['controls'].append(rec)
    path=Path(sys.argv[1] if len(sys.argv)>1 else 'HYBRID_REFERENCE_FRONTIER.json')
    data=(json.dumps(strings(out),sort_keys=True,indent=2)+'\n').encode();path.write_bytes(data)
    for rec in out['controls']:
        p=rec['physical'];op=rec['canonical']['rational_global_minimum']
        print('CONTROL',rec['theta'],'S U H',len(p['S']),len(p['U']),len(p['H']),'weak',p['physical_weak'])
        if op:print('EXACT_GLOBAL_CANONICAL_SCALE',op['k'],'BRANCHES',op['left_active'],op['right_active'])
        else:print('UNIQUE_ALGEBRAIC_CANONICAL_SCALE',rec['canonical']['isolated_global_minimum'])
        print('ALL_REFERENCE_TEMPLATE_BLIND',rec['all_reference_template_blind_margin']>0)
    print(path.name,len(data),hashlib.sha256(data).hexdigest())
    print('H5_CANONICAL_REFERENCE_IDENTITIES_AND_ALL_REFERENCE_TEMPLATE_BLIND_CONTROL_PASS')
if __name__=='__main__':main()
