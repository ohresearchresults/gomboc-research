"""Cyclic intersections and dual escape-ball apex completion.

If all polar support points escape to the SAME unique polar maximum, their
union retains that property. Intersecting rotated parent copies therefore
preserves reference S1. New top-plane polar points have explicit old escape
witnesses. Half-turn symmetry reduces uniform mass closure to one scalar.
All final actual-centroid S/U counts and genuine numerical hull counts are
computed again; exact verification is reserved for a qualifying candidate.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time
import numpy as np
from scipy.optimize import brentq
from scipy.spatial import QhullError
from geometry import halfspace_mesh,census,arrows


def centered_body(other):
    # With the root removed, every positive-arrow path ends at a sink. For
    # q*= -r e_z all such sinks escape iff r> |q|^2/(-q_z).
    W=arrows(other);sinks=np.flatnonzero(W.max(1)<=1e-12)
    if not len(sinks) or np.any(other[sinks,2]>=0):raise ValueError('No strict axial stable-root bound')
    hmax=float(np.min(-other[sinks,2]/np.sum(other[sinks]**2,axis=1)))*(1-1e-8)
    def body(h):
        Q=np.r_[[[0.,0.,-1/h]],other];return Q,halfspace_mesh(Q)
    Q,m=body(hmax)
    if m['g'][2]>=0:raise ValueError('Uniform centroid cannot close inside this certified S1 height interval')
    height=float(brentq(lambda h:float(body(h)[1]['g'][2]),hmax*1e-7,hmax,xtol=1e-12))
    Q,m=body(height)
    if abs(m['g']).max()>2e-9:raise ValueError('Actual uniform mass closure or axial symmetry failed')
    st=census(m,0)
    if st['S']!=1:raise ValueError('Independent actual stable census contradicts the strict reference construction')
    return Q,m,dict(height=height,maximum_S1_height=hmax,**st)


def run(parent,out,trials=2500,seed=912551):
    parent=pathlib.Path(parent);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False)
    d=np.load(parent);H=d['Q'];root=int(d['stable']);q=np.delete(H,root,axis=0);other=np.r_[q,q*np.array([-1.,-1.,1.])]
    top=float(other[:,2].max());eligible=[]
    for j,p in enumerate(other):
        radius2=float(p@p/4-(top-p[2]/2)**2)
        if radius2>1e-12:eligible.append((j,p[:2]/2,np.sqrt(radius2)))
    if not eligible:raise ValueError('No finite top-plane escape disks')
    rng=np.random.default_rng(seed);rows=[];start=time.time();best=999;best_merit=np.inf
    np.savez(out/'base_supports.npz',Q=np.r_[[[0,0,-1]],other],top=top)
    (out/'definition.json').write_text(json.dumps(dict(parent=str(parent.resolve()),trials=trials,seed=seed,
        eligible_old_witnesses=[x[0] for x in eligible],scope='Direct physical own110 family with proven referenceS1 device and separately integrated uniform mass'),indent=2))
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes())
    for it in range(trials):
        pairs=int(rng.choice([1,2,3,4,6,9,13,20,27]));added=[];witnesses=[]
        for j in range(pairs):
            index,centre,radius=eligible[int(rng.integers(len(eligible)))];angle=rng.uniform(0,2*np.pi)
            rad=radius*np.sqrt(rng.uniform(.02,.999))
            xy=centre+rad*np.array([np.cos(angle),np.sin(angle)]);p=np.r_[xy,top]
            margin=float(p@(other[index]-p))
            if margin<=1e-10:raise ValueError('Explicit top-plane escape witness is not strict')
            added.extend([p,p*np.array([-1.,-1.,1.])]);witnesses.append(dict(old=index,point=p.tolist(),margin=margin))
        allq=np.r_[other,added]
        try:
            Q,m,row=centered_body(allq);row.update(trial=it,pairs=pairs,witnesses=witnesses,seconds=time.time()-start)
            if not 17<=row['E']<250:raise ValueError('Candidate exceeds genuine numerical complexity limit')
            merit=max(0,-row['min_primal_nonroot'])
            if row['U']<best or merit<best_merit:
                p=out/f'trial{it:05d}';p.mkdir();np.savez(p/'body.npz',Q=Q,X=m['X']);row['folder']=str(p.resolve());(p/'summary.json').write_text(json.dumps(row,indent=2));best=min(best,row['U']);best_merit=min(best_merit,merit)
                print('MONOSTABLE_INTERSECTION',json.dumps({k:v for k,v in row.items() if k not in ['S_ids','U_ids','witnesses']}),flush=True)
            if row['S']==row['U']==1:
                np.savez(out/'POTENTIAL_OWN110.npz',Q=Q,X=m['X']);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(row,indent=2));return
        except (ValueError,RuntimeError,AssertionError,QhullError,np.linalg.LinAlgError) as error:
            row=dict(trial=it,pairs=pairs,witnesses=witnesses,error=repr(error))
        rows.append(row)
        if it%25==0:(out/'history.json').write_text(json.dumps(rows,indent=2))
    (out/'history.json').write_text(json.dumps(rows,indent=2))
