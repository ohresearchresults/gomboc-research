# material-0f41ad93a9c9

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Exact common-normal-height sweep for an actual H5 body.
All 68 genuine primitive signs use the SAME metric and its inverse.
No solver or sampled eta grid is used. Dependency: complete lift_core.py.
"""
from lift_core import *
import json

KAPPA=R(924733153857541,21600000000000)
P_GAP=R(23884711,3600000)
Q_GAP=R(38716531,6000000)

def height_rows(B,v,G):
    v=S.Matrix(v);d=G.det();assert pd(G)
    y=[a[:2,0]+a[2]*v for a in B['v']]
    a=[q[:2,0] for q in B['poles']]
    l=[q[2]-v.dot(q[:2,0]) for q in B['poles']]
    adj=S.Matrix(((G[1,1],-G[0,1]),(-G[1,0],G[0,0])))
    rows={}
    for i,j in B['primal']:
        rows['P',i,j]=(B['v'][i][2]*(B['v'][j][2]-B['v'][i][2]),(y[i].T*G*(y[j]-y[i]))[0])
    for i,j in B['polar']:
        rows['Q',i,j]=((a[i].T*adj*(a[j]-a[i]))[0],d*l[i]*(l[j]-l[i]))
    return {k:tuple(map(S.factor,r)) for k,r in rows.items()}

def signs_census(B,rows,eta):
    val={k:A*eta+Z for k,(A,Z) in rows.items()}
    u=[i for i in range(10) if all(val['P',a,b]<0 for a,b in B['primal'] if a==i)]
    st=[i for i in range(9) if all(val['Q',a,b]<0 for a,b in B['polar'] if a==i)]
    hh=[];ww=[]
    for i,j in B['edges']:
        f,g=B['ef'][i,j];r=[val['P',i,j],val['P',j,i],val['Q',f,g],val['Q',g,f]]
        if max(r)<0:hh.append((i,j))
        elif max(r)==0:ww.append((i,j))
    assert len(u)+len(st)-len(hh)==2 or ww
    return dict(S=st,U=u,H=hh,weak=ww,counts=(len(st),len(u),len(hh)),zeros=[k for k,z in val.items() if z==0])

def local_control(B):
    c=B['g'][:2,0];gamma=B['g'][2];H=1-gamma;k=1-2*gamma
    v=(2*c-S.Matrix((0,B['theta'][4]))-S.Matrix((R(1,10),R(13,50))))/k
    yy=[a[:2,0]+a[2]*v for a in B['v']]
    J=S.Matrix.hstack(yy[9],yy[3]);Gram=S.Matrix(((1,R(11,10)),(R(11,10),R(73,50))))
    G0=(J.T.inv()*Gram*J.inv()).applyfunc(S.factor)
    eta0=1/(20*H)
    return v,G0/G0[0,0],eta0/G0[0,0]

def height_sweep(B,v,G):
    rows=height_rows(B,v,G)
    cuts=sorted(set(-Z/A for A,Z in rows.values() if A!=0 and -Z/A>0))
    cells=[]
    prev=S.S(0)
    for c in cuts:
        eta=(prev+c)/2
        cc=signs_census(B,rows,eta)
        cells.append(dict(kind='open',lo=prev,hi=c,sample=eta,census=cc))
        cells.append(dict(kind='point',eta=c,census=signs_census(B,rows,c)))
        prev=c
    eta=prev+1
    cells.append(dict(kind='open',lo=prev,hi='infinity',sample=eta,census=signs_census(B,rows,eta)))
    # Independently compare every cell representative against the direct M,N.
    for cell in cells:
        eta=cell['eta'] if cell['kind']=='point' else cell['sample']
        a=audit(B,v,G/eta);c=cell['census']
        assert all(a[k]==c[k] for k in ('S','U','H','weak','counts'))
    return dict(rows=rows,positive_cuts=cuts,cells=cells)

def symbolic_conic_degrees(B,v):
    b,c=S.symbols('b c');G=S.Matrix(((1,b),(b,c)));d=c-b*b
    yy=[a[:2,0]+a[2]*v for a in B['v']]
    aa=[q[:2,0] for q in B['poles']];ll=[q[2]-v.dot(q[:2,0]) for q in B['poles']]
    rows=[]
    for i,j in B['primal']:
        rows.append(('P',(B['v'][i][2]*(B['v'][j][2]-B['v'][i][2])),S.expand((yy[i].T*G*(yy[j]-yy[i]))[0])))
    adj=S.Matrix(((c,-b),(-b,1)))
    for i,j in B['polar']:
        rows.append(('Q',S.expand((aa[i].T*adj*(aa[j]-aa[i]))[0]),d*ll[i]*(ll[j]-ll[i])))
    maxima={'PP':0,'PQ':0,'QQ':0};counts=dict.fromkeys(maxima,0)
    for u,w in combinations(rows,2):
        kind=''.join(sorted((u[0],w[0])))
        if kind=='QQ':
            # Cancel only the strictly positive determinant factor.
            f=S.expand(S.cancel(u[2]/d)*w[1]-S.cancel(w[2]/d)*u[1])
        else:f=S.expand(u[2]*w[1]-w[2]*u[1])
        poly=S.Poly(f,b,c);degree=0 if poly.is_zero else int(poly.total_degree())
        assert degree<= (2 if kind=='PQ' else 1)
        maxima[kind]=max(maxima[kind],degree);counts[kind]+=1
    return dict(pair_counts=counts,max_degrees=maxima)

def spectral_data(B,v,G):
    sig=B['Sigma'];z=sig[2,2];D=sig.inv()[:2,:2];m=sig[:2,2]/z;w=v+m
    C=(sig[:2,:2]+sig[:2,2]*v.T+v*sig[2,:2]+z*v*v.T).applyfunc(S.factor)
    assert C==(D.inv()+z*w*w.T).applyfunc(S.factor)
    t=(z*w.T*D*w)[0];bound=(KAPPA-1)**2/(4*KAPPA)
    rho=KAPPA/(KAPPA+1)**2
    adj=S.Matrix(((G[1,1],-G[0,1]),(-G[1,0],G[0,0])))
    ellipse1=S.factor(C.det()*G.det()-rho*S.trace(C*G)**2)
    ellipse2=S.factor(D.det()*G.det()-rho*S.trace(D*adj)**2)
    return dict(shear_t=t,shear_bound=bound,shear_inside=t<bound,C=C,D=D,
                tangential_ellipse=ellipse1,inverse_tangential_ellipse=ellipse2)

def main():
    if not __debug__:raise RuntimeError('Assertions must be enabled')
    B=geometry((R(1,10),R(9,10),R(3,25),R(3,5),R(3,20)))
    v,G,eta0=local_control(B);ctrl=audit(B,v,G/eta0)
    assert ctrl['counts']==(2,2,2) and ctrl['U']==[3,6] and ctrl['S']==[1,5]
    assert not ctrl['weak'] and ctrl['zero_primitives']==0
    sweep=height_sweep(B,v,G)
    no110=all(z['census']['counts']!=(1,1,0) or z['census']['weak'] for z in sweep['cells'])
    assert no110
    # On a parallel two-end body every cross-layer primal slope is negative.
    assert all(A<0 for (kind,i,j),(A,Z) in sweep['rows'].items() if kind=='P' and B['v'][i][2]!=B['v'][j][2])
    out=dict(theta=B['theta'],volume=B['volume'],g=B['g'],v=v,G=G,eta_control=eta0,
             control=ctrl,all_positive_heights_exclude110=no110,spectral=spectral_data(B,v,G),
             conic_degree_check=symbolic_conic_degrees(B,v),height_sweep=sweep)
    print(json.dumps(encode(out),sort_keys=True,indent=2))
    print('FIXED_SHEAR_COMMON_HEIGHT_CONICS_V1_PASS')

if __name__=='__main__':main()
