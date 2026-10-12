"""Steiner fibre centering of exact uniform-centred physical polyhedra.

For upper/lower planes qi.x<=1, qj.x<=1 and fibre direction v, write
di=qi.v>0,dj=qj.v<0. The centred-fibre body's two support normals are
 (qi*dj-qj*di)/(dj-di) +/- 2*di*dj*v/((dj-di)*(v.v)).
Every pair is included; planes parallel to v are retained. This is rational
for rational input/direction. Equal fibre lengths preserve uniform volume and
transverse moments, while reflection cancels the axial moment. Hence an own
zero centroid remains zero. Full actual hull and mass are still read back.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time,hashlib
import numpy as np,gmpy2
from scipy.optimize import differential_evolution,minimize
from scipy.spatial import QhullError
from geometry import halfspace_mesh,census
from persistence_search import pairs
from cyclic_flower_mass_goal import Found

def steiner(Q,v):
    vv=float(v@v)
    if vv<=0:raise ValueError('Zero fibre direction')
    d=Q@v;up=np.flatnonzero(d>0);down=np.flatnonzero(d<0);parallel=np.flatnonzero(d==0)
    if not len(up) or not len(down):raise ValueError('Unbounded fibre directions')
    i=np.repeat(up,len(down));j=np.tile(down,len(up));den=d[j]-d[i]
    base=(Q[i]*d[j,None]-Q[j]*d[i,None])/den[:,None];offset=(2*d[i]*d[j]/(den*vv))[:,None]*v
    return np.r_[base+offset,base-offset,Q[parallel]]

def run(source,out,scouts=700,iterations=160,seed=931518):
    source=pathlib.Path(source);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);data=source.read_bytes();a=json.loads(data);g=list(map(gmpy2.mpq,a['centroid']));H=a['raw_halfspaces'];Q=[]
    for i in a['active']:
        row=list(map(gmpy2.mpq,H[i]));den=row[3]-sum(row[k]*g[k] for k in range(3))
        if den<=0:raise ValueError('Exact own centroid outside input support')
        Q.append([float(row[k]/den) for k in range(3)])
    Q=np.array(Q);m=halfspace_mesh(Q);initial=census(m,0);volume=m['volume']
    if max(abs(m['g']))>1e-8:raise ValueError('Exact-centroid source fails numerical integration')
    np.savez(out/'centred_source.npz',Q=Q,X=m['X']);(out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes());(out/'definition.json').write_text(json.dumps(dict(source=str(source.resolve()),sha256=hashlib.sha256(data).hexdigest(),scouts=scouts,iterations=iterations,seed=seed,initial=initial,
        scope='Literal convex fibre-centred uniform body, all upper/lower support pairs, actual mass and true hull census; only own110 qualifies'),indent=2))
    rng=np.random.default_rng(seed);calls=0;best=float('inf');bestz=None;hist=[];bad={};pool=[];start=time.time()
    def evaluate(z):
        nonlocal calls,best,bestz
        calls+=1;t,p=z;v=np.array([np.sin(t)*np.cos(p),np.sin(t)*np.sin(p),np.cos(t)])
        try:
            Hs=steiner(Q,v);mm=halfspace_mesh(Hs);row=census(mm,0)
            if abs(mm['volume']/volume-1)>2e-7 or max(abs(mm['g']))>2e-8:raise ValueError('Independent fibre volume/centroid identity failed')
            HH=Hs[mm['active']];P=mm['X']-mm['g'];R=HH/(1-HH@mm['g'])[:,None]
            if 17<=row['E']<=249 and row['S']==row['U']==1:
                np.savez(out/'POTENTIAL_OWN110.npz',Q=HH,X=mm['X'],direction=v,parameters=z,all_pair_halfspaces=Hs);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(calls=calls,direction=v.tolist(),**row),indent=2));raise Found()
            if row['E']<17:return 100.
            if row['E']>249:score=20+(row['E']-249)/40+.0001*(row['S']+row['U'])
            else:
                edgefaces={tuple(e):[] for e in mm['edges']}
                for f,cy in enumerate(mm['faces']):
                    for x,y in zip(cy,cy[1:]+cy[:1]):edgefaces[tuple(sorted((x,y)))].append(f)
                if any(len(fs)!=2 for fs in edgefaces.values()):raise ValueError('Fibre body boundary is not closed')
                bars=[]
                for A,ed in [(P,mm['edges']),(R,np.array(list(edgefaces.values())))]:
                    pp,h=pairs(A,ed);bars.extend((1-h[pp[:,1]]/np.sum(A[pp[:,0]]**2,axis=1)).tolist())
                score=float(row['S']+row['U']-2+.45*max(bars,default=0)+.04*(np.mean(bars) if bars else 0))
            if score<best:
                best=score;bestz=np.array(z);record=dict(calls=calls,score=score,direction=v.tolist(),seconds=time.time()-start,**row);hist.append(record);np.savez(out/'best.npz',Q=HH,X=mm['X'],direction=v,parameters=z);(out/'history.json').write_text(json.dumps(hist,indent=2));print('STEINER_OWN_CENTROID_GOAL',json.dumps({k:v for k,v in record.items() if k not in ['S_ids','U_ids']}),flush=True)
            if calls<=scouts:pool.append((score,np.array(z)))
            return score
        except (ValueError,RuntimeError,AssertionError,QhullError,np.linalg.LinAlgError) as err:
            key=str(err).split('\n')[0];bad[key]=bad.get(key,0)+1;return 1000.
    try:
        for _ in range(scouts):evaluate(np.array([np.arccos(rng.uniform(-1,1)),rng.uniform(-np.pi,np.pi)]))
        pop=[z for _,z in sorted(pool,key=lambda t:t[0])[:30]]
        while len(pop)<50:pop.append(np.array([np.arccos(rng.uniform(-1,1)),rng.uniform(-np.pi,np.pi)]))
        bounds=[(1e-7,np.pi-1e-7),(-np.pi,np.pi)]
        differential_evolution(evaluate,bounds,init=np.array(pop),seed=seed,maxiter=iterations,workers=1,updating='immediate',tol=1e-8,atol=1e-9,polish=False)
        if bestz is not None:minimize(evaluate,bestz,method='Nelder-Mead',bounds=bounds,options={'maxiter':900,'xatol':1e-8,'fatol':1e-9})
    except Found:return
    (out/'FINITE_END.json').write_text(json.dumps(dict(calls=calls,best=best,failures=bad,seconds=time.time()-start,scope='Finite literal Steiner-centred search ended without a qualifying body'),indent=2))

if __name__=='__main__':
    import sys
    run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 700,int(sys.argv[4]) if len(sys.argv)>4 else 160)
