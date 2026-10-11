"""Gradual physical centroid closure of strict reference-monounstable bodies.

Each LP chooses a fraction of the remaining centroid displacement.  A finite
step is accepted only after rebuilding its actual filled hull, checking the
strict radial domain and interior carrier, and observing smaller mass offset.
This is distinct from a full Newton correction that can be infeasible in one
bounded step.  Reference U1 is never asserted to be own-centroid U1.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
from primal_log_thales import Chart,evaluate,metric
from constrained_mass_projection import project
from vertex_geometry import geometry
from support_geometry import escape
from exact_audit_vertices import audit
from exact_barcode_report import report

OPT={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10}
def volume(e):
    X=e['X'];DX=e['DX'];T=geometry(X,False)['T'];a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]]
    vv=np.einsum('ic,ic->i',a,np.cross(b,c));DV=(np.einsum('ic,icp->ip',np.cross(b,c),DX[T[:,0]])+np.einsum('ic,icp->ip',np.cross(c,a),DX[T[:,1]])+np.einsum('ic,icp->ip',np.cross(a,b),DX[T[:,2]])).sum(0)/6
    return vv.sum()/6,DV

def run(source,out,steps,floor):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(source);assert len(X)<=84;c=Chart(X);z=c.z0.copy();e=evaluate(c,z,.03);V0=volume(e)[0];trust=.2;hist=[];start=time.time()
    (out/'method.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),initial_volume=V0,volume_floor_fraction=floor,radial_log_floor=1e-8),indent=2));np.save(out/'initial.npy',X)
    for it in range(steps):
        e=evaluate(c,z,.03);norm=np.linalg.norm(e['g']);V,DV=volume(e);refU=int(np.sum(escape(e['X'])[0]<0));assert refU==1
        row=dict(it=it,mass_norm=float(norm),S=e['S'],U=e['U'],reference_U=refU,Q=max(e['Q'],default=0.),volume=float(V),V=len(e['vertices']),trust=trust,seconds=time.time()-start);hist.append(row);np.save(out/'latest.npy',e['X']);np.save(out/'latest_params.npy',z);(out/'history.json').write_text(json.dumps(hist,indent=2))
        if it%10==0:print('THALES_MASS_CLOSE',out,row,flush=True)
        if e['S']==e['U']==1:
            aa=audit(out/'latest.npy',out/f'exact_nomination_it{it}',10**12);report(out/f'exact_nomination_it{it}')
            if aa['counts']==[1,1,0]and aa['weak']==[0,0,0]:return
        if norm<1e-11:
            zz,ee=project(c,z,.03);np.save(out/'closed.npy',ee['X']);(out/'closure.json').write_text(json.dumps(dict(mass_norm=float(np.linalg.norm(ee['g'])),S=ee['S'],U=ee['U'],Q=max(ee['Q'],default=0.)),indent=2));print('THALES_MASS_CLOSED',out,ee['S'],ee['U'],max(ee['Q'],default=0.),flush=True);return
        W,sx=metric(e);d=c.d;rad=np.arange(2,d,3);R=np.vstack((-e['DI']@W,W[rad],-W[rad],-(DV@W)[None,:]/V0));bR=np.r_[e['inside']*.95,-1e-8-z[rad],z[rad]+25,(V-floor*V0)/V0];m=len(bR);I=eye(d)
        A=vstack([hstack([csr_matrix(R),csr_matrix((m,1+d))]),hstack([I,csr_matrix((d,1)),-I]),hstack([-I,csr_matrix((d,1)),-I])],format='csr');b=np.r_[bR,np.zeros(2*d)];ms=1e5;AE=hstack([csr_matrix(ms*e['Dg']@W/sx),csr_matrix((ms*e['g']/sx)[:,None]),csr_matrix((3,d))],format='csr');bound=trust/np.sqrt(d)
        sol=linprog(np.r_[np.zeros(d),-1.,np.full(d,1e-5)],A_ub=A,b_ub=b,A_eq=AE,b_eq=np.zeros(3),bounds=[(-bound,bound)]*d+[(0.,1.)]+[(0,None)]*d,method='highs',options=OPT)
        if not sol.success:row['error']=sol.message;trust*=.4
        else:
            dz=W@sol.x[:d];fraction=float(sol.x[d]);row['predicted_mass_fraction']=fraction;ok=False
            for k in range(18):
                try:zz=z+2.**-k*dz;ee=evaluate(c,zz,.03);VV,_=volume(ee)
                except (ValueError,np.linalg.LinAlgError):continue
                nn=np.linalg.norm(ee['g'])
                if VV>=floor*V0 and max(zz[2::3])<-0.8e-8 and nn<norm-max(1e-14,norm*fraction*2.**-k*1e-4):
                    z=zz;ok=True;row['alpha']=2.**-k
                    if k==0:trust=min(.8,trust*1.25)
                    break
            if not ok:trust*=.4
            if ok and it%20==19:
                c=Chart(ee['X']);z=c.z0.copy();np.savez(out/f'rechart{it}.npz',X=c.X0,parent=c.parent,tetra=c.tetra,z0=z)
        if trust<1e-9:break
    print('THALES_MASS_CLOSE_FINITE_END',out,hist[-1],flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--steps',type=int,default=500);p.add_argument('--volume-floor',type=float,default=.65);a=p.parse_args();run(a.source,a.out,a.steps,a.volume_floor)
