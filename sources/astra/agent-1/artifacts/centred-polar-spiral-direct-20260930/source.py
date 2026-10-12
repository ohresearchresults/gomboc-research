"""Direct homogeneous S1 family from rotated positive-escape polar chains.

Every support point has a strict geometric arrow to a previous orbit and
ultimately to -e_z. A half-turn gives axial mass symmetry. A real four-plane
top vertex is added inside the last orbit's escape disks. The bottom support
is then solved against the same body's uniform centroid, within the exact
reference-S1 root-height inequality. Only the unstable count remains to find;
the final numerical complete census is always checked independently.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time
import numpy as np
from scipy.spatial import QhullError
from rotated_monostable_intersections import centered_body
from geometry import arrows
from persistence_search import pairs


def construct(parameters,m=39):
    power,endgap,omega,b1,b2,b3,damp,alpha,beta=parameters
    theta=(np.arange(1,m+1)/m)**power*(np.pi-endgap)
    phi=omega*theta+b1*np.sin(theta)+b2*np.sin(2*theta)+b3*np.sin(3*theta)
    directions=np.c_[np.sin(theta)*np.cos(phi),np.sin(theta)*np.sin(phi),-np.cos(theta)]
    last=np.array([0.,0.,-1.]);points=[];witnesses=[]
    for j,d in enumerate(directions):
        mirror=last*np.array([-1.,-1.,1.]);parent=last if d@last>=d@mirror else mirror
        product=float(d@parent)
        if product<=1e-8:raise ValueError('Orbit step has no positive parent projection')
        q=np.exp(-damp)*product*d
        margin=float(q@(parent-q))
        if margin<=1e-12:raise ValueError('Finite polar escape margin too small')
        points.extend([q,q*np.array([-1.,-1.,1.])]);witnesses.append(dict(orbit=j,margin=margin));last=q
    xy=last[:2];length=np.linalg.norm(xy);perp=np.array([-xy[1],xy[0]])
    # beta<1 puts this second pair strictly inside the last pair's diameter
    # disk at the same z, while spanning a genuine axial top normal cone.
    v=alpha*xy+beta*np.sqrt(alpha*(1-alpha))*perp
    top=np.r_[v,last[2]]
    if top@(last-top)<=1e-12:raise ValueError('Top completion has no strict escape')
    points.extend([top,top*np.array([-1.,-1.,1.])])
    return np.array(points),witnesses


def run(out,trials=6000,seed=294971):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);rng=np.random.default_rng(seed);history=[];bestU=999;bestP=np.inf;start=time.time()
    (out/'definition.json').write_text(json.dumps(dict(trials=trials,seed=seed,orbit_pairs=40,supports=81,
        edge_bound=237,scope='Actual uniform-centred monostable construction; only complete own110 is a candidate for exact verification'),indent=2))
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes())
    for i in range(trials):
        z=np.array([rng.uniform(.6,1.6),rng.uniform(.04,.75),rng.uniform(-2.4,2.4),rng.uniform(-1.2,1.2),
                    rng.uniform(-.8,.8),rng.uniform(-.5,.5),10**rng.uniform(-5,-2.5),rng.uniform(.2,.8),rng.uniform(.2,.98)])
        try:
            other,w=construct(z);Q,m,row=centered_body(other)
            if not 17<=row['E']<250:raise ValueError('Numerical edge budget violated')
            P=m['X']-m['g'];pp,h=pairs(P,m['edges']);bars=(1-h[pp[:,1]]/(P[pp[:,0]]**2).sum(1)).tolist();value=max(bars,default=0)
            row.update(sample=i,parameters=z.tolist(),P=bars,Pmax=value,seconds=time.time()-start)
            if row['U']<bestU or value<bestP:
                p=out/f'sample{i:05d}';p.mkdir();np.savez(p/'body.npz',Q=Q,X=m['X'],parameters=z);row['folder']=str(p.resolve())
                (p/'summary.json').write_text(json.dumps(row,indent=2));(p/'witnesses.json').write_text(json.dumps(w,indent=2));bestU=min(bestU,row['U']);bestP=min(bestP,value)
                print('CENTERED_POLAR_SPIRAL',json.dumps({k:v for k,v in row.items() if k not in ['S_ids','U_ids','P']}),flush=True)
            if row['S']==row['U']==1:
                np.savez(out/'POTENTIAL_OWN110.npz',Q=Q,X=m['X'],parameters=z);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(row,indent=2));return
        except (ValueError,RuntimeError,AssertionError,QhullError,np.linalg.LinAlgError) as error:
            row=dict(sample=i,parameters=z.tolist(),error=repr(error))
        history.append(row)
        if i%25==0:(out/'history.json').write_text(json.dumps(history,indent=2))
    (out/'history.json').write_text(json.dumps(history,indent=2))
