"""Active-hull analytic derivatives of true COM and cap persistence.

These derivatives are local to the current incidence and MST cells. Every finite
step still reconstructs the hull and is checked independently by the caller.
"""
import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from geometry import census,escape_table


def persistence_gradient(y):
    delta=y[None,:,:]-y[:,None,:]
    ee=np.einsum('ijk,ijk->ij',delta,delta)
    ze=np.einsum('ik,ijk->ij',y,delta)
    t=np.clip(-ze/np.maximum(ee,1e-300),0.,1.)
    z=y[:,None,:]+t[:,:,None]*delta
    zz=np.einsum('ijk,ijk->ij',z,z)
    weights=1/np.maximum(zz,1e-300);np.fill_diagonal(weights,0.)
    rr=np.einsum('ij,ij->i',y,y);birth=1/rr
    tree=minimum_spanning_tree(weights).tocoo()
    grad=2*y/(rr*rr)[:,None]
    grad[np.argmin(birth)]=0.
    for i,j in zip(tree.row,tree.col):
        v=-2*z[i,j]/zz[i,j]**2
        grad[i]+=(1-t[i,j])*v;grad[j]+=t[i,j]*v
    return float(tree.data.sum()-birth.sum()+min(birth)),grad


def mass_gradient(p,r):
    c=np.array(r['centroid']);h=r['hull'];volume=r['volume']
    jc=np.zeros((3,len(p),3));dv=np.zeros_like(p)
    for triangle,normal in zip(h.simplices,h.equations[:,:3]):
        i,j,k=map(int,triangle)
        if np.dot(np.cross(p[j]-p[i],p[k]-p[i]),normal)<0:
            j,k=k,j
        pts=p[[i,j,k]]
        det=np.dot(pts[0],np.cross(pts[1],pts[2]))
        moment_direction=pts.sum(axis=0)-4*c
        for local,index in enumerate([i,j,k]):
            ddet=np.cross(pts[(local+1)%3],pts[(local+2)%3])
            dv[index]+=ddet/6
            jc[:,index,:]+=(np.outer(moment_direction,ddet)+det*np.eye(3))/(24*volume)
    return jc,dv


def derivatives(p,protect,witness,volume0,margin,roundness=0.,roundness_weight=10.):
    r=census(p,True);c=np.array(r['centroid']);x=p-c
    rr=np.einsum('ij,ij->i',x,x);root=int(np.argmax(rr));scale=rr[root]
    jc,dv=mass_gradient(p,r)
    b,gq=persistence_gradient(r['q'])
    gb=np.zeros_like(p);mass_coefficient=np.zeros(3)
    for f,triangles in enumerate(r['groups']):
        ids=r['hull'].simplices[triangles[0]]
        inverse=np.linalg.inv(x[ids])
        coefficient=-(gq[f]@inverse)[:,None]*r['q'][f]
        for index,coeff in zip(ids,coefficient):
            gb[index]+=coeff
        mass_coefficient-=coefficient.sum(axis=0)
    gb+=np.einsum('a,akb->kb',mass_coefficient,jc)
    gradius=-np.einsum('a,akb->kb',2*x[root],jc)
    gradius[root]+=2*x[root]
    gradient=gb/scale-b*gradius/scale**2
    objective=b/scale
    if roundness:
        f=int(np.argmax(np.einsum('ij,ij->i',r['q'],r['q'])))
        q=r['q'][f];qscale=q@q
        ids=r['hull'].simplices[r['groups'][f][0]]
        inv=np.linalg.inv(x[ids]);coeff=-(2*q@inv)[:,None]*q
        gqs=np.zeros_like(p)
        for index,co in zip(ids,coeff):
            gqs[index]+=co
        gqs-=np.einsum('a,akb->kb',coeff.sum(axis=0),jc)
        ratio=1/np.sqrt(scale*qscale)
        if ratio<roundness:
            dratio=-.5*ratio*(gradius/scale+gqs/qscale)
            objective+=roundness_weight*(roundness-ratio)**2
            gradient+=2*roundness_weight*(ratio-roundness)*dratio
    jac=[];constraints=[]
    for i in protect:
        j=witness[i];z=x[i];e=p[j]-p[i]
        rz=np.linalg.norm(z);re=np.linalg.norm(e);cos=(z@e)/(rz*re)
        gz=e/(rz*re)-cos*z/rz**2
        ge=z/(rz*re)-cos*e/re**2
        derivative=-np.einsum('a,akb->kb',gz,jc)
        derivative[i]+=gz-ge;derivative[j]+=ge
        jac.append(derivative.ravel());constraints.append(cos-margin)
    jac.append((dv/volume0).ravel());constraints.append(r['volume']/volume0-.5)
    return objective,np.array(constraints),gradient.ravel(),np.array(jac),r


def convexity_derivatives(p,r):
    values=[];jac=[]
    for triangle,normal in zip(r['hull'].simplices,r['hull'].equations[:,:3]):
        i,j,k=map(int,triangle)
        n=np.cross(p[j]-p[i],p[k]-p[i])
        if n@normal<0:
            j,k=k,j;n=-n
        scale=np.linalg.norm(n)
        for l in range(len(p)):
            if l in (i,j,k):
                continue
            u,v,w=p[[i,j,k]]-p[l]
            value=(u@np.cross(v,w))/scale
            grad=np.zeros_like(p)
            gi=np.cross(v,w)/scale;gj=np.cross(w,u)/scale;gk=np.cross(u,v)/scale
            grad[i]=gi;grad[j]=gj;grad[k]=gk;grad[l]=-gi-gj-gk
            values.append(max(0.,value));jac.append(grad.ravel())
    return np.array(values),np.array(jac)


def stable_escape_derivatives(p,r,margin=1e-5):
    c=np.array(r['centroid']);x=p-c;q=r['q'];jc,_=mass_gradient(p,r)
    jq=[]
    for f,triangles in enumerate(r['groups']):
        ids=r['hull'].simplices[triangles[0]]
        inv=np.linalg.inv(x[ids]);a=inv@np.ones(3)
        derivative=a[:,None,None]*np.einsum('a,akb->kb',q[f],jc)[None,:,:]
        for k,index in enumerate(ids):
            derivative[:,index,:]-=np.outer(inv[:,k],q[f])
        jq.append(derivative)
    table=escape_table(q);best=table.argmax(axis=1);values=[];jac=[]
    for i,j in enumerate(best):
        cos=table[i,j]
        if cos<=1e-9:
            continue
        z=q[i];e=q[j]-q[i];rz=np.linalg.norm(z);re=np.linalg.norm(e)
        gz=e/(rz*re)-cos*z/rz**2;ge=z/(rz*re)-cos*e/re**2
        derivative=np.einsum('a,akb->kb',gz-ge,jq[i])+np.einsum('a,akb->kb',ge,jq[j])
        values.append(cos-min(margin,.2*cos));jac.append(derivative.ravel())
    return np.array(values),np.array(jac)


def roundness_derivative(p,r):
    c=np.array(r['centroid']);x=p-c;jc,_=mass_gradient(p,r)
    rr=np.einsum('ij,ij->i',x,x);v=int(np.argmax(rr));rs=rr[v]
    gr=-np.einsum('a,akb->kb',2*x[v],jc);gr[v]+=2*x[v]
    f=int(np.argmax(np.einsum('ij,ij->i',r['q'],r['q'])))
    q=r['q'][f];qs=q@q;ids=r['hull'].simplices[r['groups'][f][0]]
    inv=np.linalg.inv(x[ids]);coeff=-(2*q@inv)[:,None]*q;gq=np.zeros_like(p)
    for index,co in zip(ids,coeff):
        gq[index]+=co
    gq-=np.einsum('a,akb->kb',coeff.sum(axis=0),jc)
    ratio=1/np.sqrt(rs*qs)
    return float(ratio),(-.5*ratio*(gr/rs+gq/qs)).ravel()


if __name__=='__main__':
    import json,sys
    from pathlib import Path
    from geometry import write_json
    p=np.array(json.loads(Path(sys.argv[1]).read_text())['points'])
    r=census(p,True);x=p-np.array(r['centroid']);w=escape_table(x).argmax(axis=1)
    protect=np.array([i for i in range(len(p)) if i!=14]);vol=r['volume']
    f,con,df,jac,_=derivatives(p,protect,w,vol,.0002)
    rng=np.random.default_rng(991);rows=[]
    for k in range(12):
        direction=rng.normal(size=p.shape);direction/=np.linalg.norm(direction)
        eps=1e-9
        plus=derivatives(p+eps*direction,protect,w,vol,.0002)
        minus=derivatives(p-eps*direction,protect,w,vol,.0002)
        observed=(np.r_[plus[0],plus[1]]-np.r_[minus[0],minus[1]])/(2*eps)
        expected=np.r_[df@direction.ravel(),jac@direction.ravel()]
        rows.append(dict(maximum_absolute_error=float(max(abs(observed-expected))),
                         barrier_predicted=float(expected[0]),barrier_observed=float(observed[0])))
    report=dict(input=sys.argv[1],directions=rows,max_error=max(r['maximum_absolute_error']for r in rows))
    if len(sys.argv)>2:
        write_json(sys.argv[2],report)
    print(json.dumps(report,indent=2))
