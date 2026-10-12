"""C2-symmetric seeds sampled from a twisted height function on the sphere.

h(x,y,z)=x*cos(k*z)-y*sin(k*z) is height after the smooth spherical
diffeomorphism rotating longitude by k*z. Thus h has exactly two critical
points. The radial surface r=1+eps*h is a motivation, not the accepted body.
For its continuous uniform first moment, symmetry kills y,z; the x equation
is I1(k)+(3 eps^2/4) I2(k)=0, Ij=integral (1-z^2)^j cos(kz) dz.
Every actual sampled polyhedron is independently hulled and re-integrated.
"""
import sys,json
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq,minimize
from c2_twisted_ladder import Search,NumericalGoal,ROOT,state

def initial(n,seed):
    eps=[.02,.035,.043,.055,.08,.12][seed%6]
    def moment(k):return quad(lambda z:(1-z*z)*np.cos(k*z)*(1+.75*eps*eps*(1-z*z)),-1,1,epsabs=1e-13)[0]
    k=brentq(moment,4.,5.3,xtol=1e-13);delta=[.003,.01,.025][(seed//2)%3]
    xb=-(1-eps)/(1+eps)+delta
    def radial(u):
        x,y,z=u;return 1+eps*(x*np.cos(k*z)-y*np.sin(k*z))
    def section(alpha,axis):
        u=np.array([-np.cos(alpha),np.sin(alpha) if axis==1 else 0.,np.sin(alpha) if axis==2 else 0.]);return radial(u)*u/(1+eps)
    # First crossing of the declared base plane in each meridian, retained as
    # a literal diamond. Convexity of the smooth motivation is not assumed.
    radii=[]
    for axis in [1,2]:
        grid=np.linspace(0,np.pi/2,300);vals=[section(t,axis)[0]-xb for t in grid];j=next(j for j in range(1,len(grid)) if vals[j]>=0 and vals[j-1]<0);alpha=brentq(lambda a:section(a,axis)[0]-xb,grid[j-1],grid[j]);radii.append(abs(section(alpha,axis)[axis]))
    phi0=.37*(seed//6);gold=np.pi*(3-np.sqrt(5));pts=[]
    for i in range(n):
        xx=-1+2*(i+.6)/(n+.2);phi=(gold*i+phi0)%np.pi;rr=np.sqrt(1-xx*xx);u=np.array([xx,rr*np.cos(phi),rr*np.sin(phi)]);p=radial(u)*u/(1+eps)
        if p[0]<=xb:p[0]=xb+.005*(1-xb)
        if p[0]>=1:p[0]=.999
        pts.append(p)
    pts=np.array(pts);t=(pts[:,0]-xb)/(1-xb);q=np.r_[np.log(-xb),np.log(radii),np.c_[np.log(t/(1-t)),pts[:,1:]].ravel()]
    return q,dict(eps=eps,k=k,continuous_x_moment_equation_residual=moment(k),base_plane=xb,base_radii=radii,base_depth=delta,phase=phi0,scope='smooth motivation only; sampled hull independently integrated')

def run(out,n=40,seeds=12):
    out=Path(out);out.mkdir(parents=True,exist_ok=False)
    bounds=[(-4,1),(-4,1),(-4,1)]+[b for _ in range(n) for b in [(-8,8),(-3,3),(-3,3)]]
    for seed in range(seeds):
        q,definition=initial(n,seed);(out/f'seed{seed:02d}_smooth_motivation.json').write_text(json.dumps(definition,indent=2)+'\n')
        for stage,tau in enumerate([-1.,.03,.003,.0003]):
            s=Search(out/f'seed{seed:02d}_stage{stage}',n,tau)
            try:opt=minimize(s.eval,q,jac=True,method='L-BFGS-B',bounds=bounds,options=dict(maxiter=700,maxls=40,maxcor=15,ftol=1e-13,gtol=1e-10))
            except NumericalGoal:
                (out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(dict(folder=str(s.out)),indent=2)+'\n');print('C2_MORSE_NUMERICAL_GOAL_REQUIRES_EXACT',str(s.out),flush=True);return
            q=np.load(s.out/'best_q.npy');(s.out/'history.json').write_text(json.dumps(s.hist,indent=2)+'\n');print('C2_MORSE_STAGE_DONE',seed,stage,s.fewest,opt.message,flush=True)
    (out/'FINITE_SEARCH_END.json').write_text(json.dumps(dict(seeds=seeds,pairs=n,goal_complete=False),indent=2)+'\n')

if __name__=='__main__':run(ROOT/sys.argv[1],int(sys.argv[2]) if len(sys.argv)>2 else 40,int(sys.argv[3]) if len(sys.argv)>3 else 12)
