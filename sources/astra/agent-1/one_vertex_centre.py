"""Add one physical vertex and solve the enlarged body's true centroid equation.
All original material is retained. New convex hull, own mass and equilibria are
computed on the same complete body. A centroid residual is never a census.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,pathlib,time,argparse
from scipy.optimize import least_squares
from mass_homotopy import mesh
from geometry import arrows
from persistence_search import pairs

def info(X):
    m=mesh(X);a=X[m['active']]-m['g'];q=np.linalg.solve(X[m['polar_triangles']]-m['g'],np.ones((m['F'],3,1)))[:,:,0];pa=arrows(a).max(1);qa=arrows(q).max(1);h=__import__('scipy').spatial.ConvexHull(X);edge=np.unique(np.sort(np.vstack([h.simplices[:,[0,1]],h.simplices[:,[1,2]],h.simplices[:,[2,0]]]),axis=1),axis=0);aa=X-m['g'];pp,hh=pairs(aa,edge);rr=(aa*aa).sum(1);dep=(1-hh[pp[:,1]]/rr[pp[:,0]]).tolist() if len(pp) else []
    return dict(V=m['V'],E=m['E'],F=m['F'],C=2*m['E'],S=int(np.sum(qa<0)),U=int(np.sum(pa<0)),minP=float(np.sort(pa)[1]),minQ=float(np.sort(qa)[1]),centroid=m['g'].tolist(),mass_norm=float(np.linalg.norm(m['g'])),P=sorted(dep,reverse=True),volume=float(m['volume']))

def solve(X):
    m=mesh(X);X=X[m['active']];g=m['g'];r=np.max(np.linalg.norm(X,axis=1));direction=-g/np.linalg.norm(g);best=None
    for scale in [.8,1.2,2.,3.]:
        y=direction*r*scale
        def fun(y):return mesh(np.vstack([X,y]))['g']/r
        opt=least_squares(fun,y,jac='3-point',xtol=1e-13,ftol=1e-13,gtol=1e-13,max_nfev=150,x_scale=r)
        P=np.vstack([X,opt.x]);err=float(np.linalg.norm(mesh(P)['g']))
        if best is None or err<best[0]:best=(err,P,dict(success=bool(opt.success),message=opt.message,nfev=opt.nfev,start_radius=scale,y=opt.x.tolist()))
        if err<1e-11*r:break
    if best[0]>1e-9*r:raise ValueError('one-vertex physical centroid closure unresolved')
    return best[1],best[2]

def run(sources,out):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);rows=[];start=time.time()
    for i,source in enumerate(sources):
        folder=out/f'case{i:03d}';folder.mkdir(exist_ok=True);dat=np.load(source);X=dat['X'];m=mesh(X)
        if 'reference' in dat:c=dat['reference']
        elif 'lam' in dat:c=float(dat['lam'])*m['g']+(1-float(dat['lam']))*(dat['w']@X)
        else:c=np.zeros(3)
        X=X-c;np.savez(folder/'reference_base.npz',X=X,reference=np.zeros(3))
        try:Y,receipt=solve(X);np.savez(folder/'centred_body.npz',X=Y,reference=np.zeros(3));row=dict(case=i,source=str(pathlib.Path(source).resolve()),solver=receipt,seconds=time.time()-start,**info(Y));rows.append(row);(folder/'summary.json').write_text(json.dumps(row,indent=2));print('CENTRING_VERTEX',json.dumps(row),flush=True)
        except Exception as e:(folder/'error.txt').write_text(repr(e));print('CENTRING_VERTEX_REJECTED',i,repr(e),flush=True);continue
        (out/'history.json').write_text(json.dumps(rows,indent=2))
        if row['S']==row['U']==1 and row['minP']>1e-10 and row['minQ']>1e-10 and 17<=row['E']<250:
            np.savez(out/'NOMINATION_OWN110.npz',X=Y,reference=np.zeros(3));print('POTENTIAL_OWN110_REQUIRES_EXACT',flush=True);return

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--input',action='append',required=True);ap.add_argument('--out',required=True);a=ap.parse_args();run(a.input,a.out)
