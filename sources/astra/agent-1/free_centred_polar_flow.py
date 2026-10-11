"""Free C2 support-plane descent at the body's own uniform centroid.

The bottom plane is eliminated by exact-form slab integration followed by a
fresh boundary mass check. Its implicit derivative is used in every search
row. Other support planes are free, with one literal four-plane axial star.
The hull is rebuilt after every proposal, so hull adjacency may change.
Numerical search only: a saved own110 requires the complete rational audit.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time
import numpy as np
import torch
from scipy.optimize import linprog
from scipy.spatial import QhullError
from geometry import arrows,census
from persistence_search import pairs
from rotated_monostable_intersections import centered_body

torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

def pack(Q):
    q=Q[1::2].copy()
    if len(Q)!=1+2*len(q) or np.max(abs(Q[2::2]-q*np.array([-1,-1,1])))>1e-9:
        raise ValueError('Input is not the literal C2 support arrangement')
    if abs(q[-1,2]-q[-2,2])>1e-10:raise ValueError('Input lacks the specified axial star')
    return q.ravel()[:-1]

def unpack(z):
    q=np.r_[z,z[-3]].reshape(-1,3)
    other=np.empty((2*len(q),3));other[::2]=q;other[1::2]=q*np.array([-1,-1,1])
    return other

def evaluate(z,jacobian=False):
    Q,m,st=centered_body(unpack(z),True)
    if not 17<=st['E']<=249:raise ValueError('Genuine numerical edge budget violated')
    P=m['X']-m['g'];pp,h=pairs(P,m['edges']);bars=1-h[pp[:,1]]/(P[pp[:,0]]**2).sum(1)
    W=arrows(Q);jj=W.argmax(1);ii=np.arange(len(Q));sg=np.ones(len(Q));sg[0]=-1
    v=sg*W[ii,jj]
    if v.min()<=0:raise ValueError('Strict selected polar escape constraints failed')
    row=dict(**st,Pmax=float(max(bars,default=0)),P=bars.tolist(),score=float(max(bars,default=0)+.02*bars.sum()),min_polar=float(v.min()))
    out=dict(Q=Q,m=m,row=row,bars=bars,v=v)
    if not jacobian:return out
    t=torch.tensor(m['triples']);tri=torch.tensor(m['triangles']);ee=torch.tensor(m['edges'][pp[:,1]]);bi=torch.tensor(pp[:,0]);jt=torch.tensor(jj);sgt=torch.tensor(sg)
    def mechanics(w):
        q=torch.cat([w[1:],w[-3:-2]]).reshape(-1,3)
        other=torch.stack([q,q*torch.tensor([-1.,-1.,1.])],dim=1).reshape(-1,3)
        qt=torch.cat([torch.stack([w[0]*0,w[0]*0,w[0]])[None],other])
        x=torch.linalg.solve(qt[t],torch.ones((len(t),3,1)))[:,:,0]
        a=x[tri];six=(a[:,0]*torch.linalg.cross(a[:,1],a[:,2])).sum(1)
        g=(six[:,None]*a.sum(1)).sum(0)/(4*six.sum());p=x-g
        a=p[ee[:,0]];d=p[ee[:,1]]-a
        frac=(-(a*d).sum(1)/(d*d).sum(1)).clamp(0,1)
        hb=((a+frac[:,None]*d)**2).sum(1);rb=(p[bi]**2).sum(1);bb=1-hb/rb
        # The implicit mass derivative below makes Dg=0, but retaining g here
        # also verifies the correct physical dual before elimination.
        polar=qt/(1-qt@g)[:,None];delta=polar[jt]-polar
        vv=sgt*(polar*delta).sum(1)/(polar.norm(dim=1)*delta.norm(dim=1))
        return torch.cat([g[2:3],bb,vv])
    w=torch.tensor(np.r_[Q[0,2],z]);values=mechanics(w).detach().numpy()
    J=torch.func.jacrev(mechanics)(w).detach().numpy()
    if abs(J[0,0])<1e-10:raise ValueError('Uniform-mass bottom plane has singular implicit derivative')
    implicit=J[1:,1:]-J[1:,0,None]*J[0,1:][None,:]/J[0,0]
    if np.max(abs(values[1:1+len(bars)]-bars),initial=0)>1e-8 or np.max(abs(values[1+len(bars):]-v))>1e-8:
        raise ValueError('Differentiated mechanics disagree with the fresh physical hull')
    out.update(Jbars=implicit[:len(bars)],Jv=implicit[len(bars):])
    return out

def run(source,out,steps=1400,trust=.02,seed=97281):
    source=pathlib.Path(source);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False)
    Q=np.load(source)['Q'];z=pack(Q);np.savez(out/'entrance.npz',Q=Q,z=z)
    (out/'definition.json').write_text(json.dumps(dict(source=str(source.resolve()),steps=steps,initial_trust=trust,seed=seed,
        scope='Free literal physical C2 support planes; actual implicit uniform mass; numerical candidate only'),indent=2))
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes())
    e=evaluate(z,True);rng=np.random.default_rng(seed);direction=rng.normal(size=len(z));direction/=np.linalg.norm(direction)
    eta=1e-7;ep=evaluate(z+eta*direction);em=evaluate(z-eta*direction)
    # At generic points the sorted persistence bar values and selected arrows
    # retain their carriers. The objective directional check also detects an
    # omitted derivative of the moving mass-closing plane.
    predicted=float(e['Jbars'][np.argmax(e['bars'])]@direction+.02*e['Jbars'].sum(0)@direction)
    measured=(ep['row']['score']-em['row']['score'])/(2*eta)
    check=dict(predicted=predicted,measured=measured,absolute_error=abs(predicted-measured))
    (out/'directional_check.json').write_text(json.dumps(check,indent=2));print('IMPLICIT_MASS_DERIVATIVE',json.dumps(check),flush=True)
    if abs(predicted-measured)>2e-4:raise ValueError('Implicit same-body derivative failed its independent check')
    start=time.time();history=[];failures=[];best=e['row']['score'];minU=e['row']['U']
    for it in range(steps):
        e=evaluate(z,True);row=dict(it=it,trust=trust,seconds=time.time()-start,**e['row']);history.append(row)
        np.savez(out/'latest.npz',Q=e['Q'],X=e['m']['X'],z=z);(out/'history.json').write_text(json.dumps(history,indent=2))
        if it%10==0:print('FREE_CENTRED_POLAR',json.dumps({k:v for k,v in row.items() if k not in ['S_ids','U_ids','P']}),flush=True)
        if row['S']==row['U']==1:
            np.savez(out/'POTENTIAL_OWN110.npz',Q=e['Q'],X=e['m']['X'],z=z)
            (out/'POTENTIAL_OWN110.json').write_text(json.dumps(row,indent=2));return
        if row['score']<best or row['U']<minU:
            best=min(best,row['score']);minU=min(minU,row['U'])
            np.savez(out/'best.npz',Q=e['Q'],X=e['m']['X'],z=z);(out/'best.json').write_text(json.dumps(row,indent=2))
        # Coordinate scale is fixed from current support radii. The explicit
        # trust box is a search restriction, not an equilibrium tolerance.
        qr=np.linalg.norm(e['Q'][1::2],axis=1);scale=np.repeat(qr,3)[:-1]
        jb=e['Jbars']*scale[None,:];jv=e['Jv']*scale[None,:]
        eps=min(1e-7,float(e['v'].min())*.2);n=len(z)
        A=np.r_[np.c_[jb,-np.ones(len(jb))],np.c_[-jv,np.zeros(len(jv))]]
        b=np.r_[-e['bars'],e['v']-eps]
        costs=np.r_[.02*jb.sum(0),1.]
        lp=linprog(costs,A_ub=A,b_ub=b,bounds=[(-trust,trust)]*n+[(0,None)],method='highs',
                   options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        accepted=False
        if lp.success:
            dz=scale*lp.x[:n]
            for level in range(17):
                zz=z+dz*2**-level
                try:
                    ee=evaluate(zz)
                    if ee['row']['S']==ee['row']['U']==1:
                        np.savez(out/'POTENTIAL_OWN110.npz',Q=ee['Q'],X=ee['m']['X'],z=zz)
                        (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(it=it,stage='proposal',**ee['row']),indent=2));return
                    if ee['v'].min()<eps*.1:continue
                    if ee['row']['score']<row['score']-1e-10:
                        z=zz;accepted=True;break
                except (ValueError,RuntimeError,QhullError,np.linalg.LinAlgError,AssertionError) as error:
                    if len(failures)<40:failures.append(dict(it=it,level=level,error=repr(error)))
        if accepted:trust=min(.08,trust*1.25) if level==0 else max(1e-7,trust*.9)
        else:trust*=.35
        if trust<1e-9:break
    (out/'failed_proposals.json').write_text(json.dumps(failures,indent=2))
    (out/'FINITE_END.json').write_text(json.dumps(dict(iterations=len(history),best=best,minU=minU,seconds=time.time()-start,
        scope='Finite numerical direct search; no qualifying body found'),indent=2))

if __name__=='__main__':
    import sys
    run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 1400)
