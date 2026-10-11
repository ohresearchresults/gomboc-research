"""C2 flower additions with actual uniform mass closure by the axial apex.

A new point inside an old vertex's diameter ball has a strict positive radial
escape to that vertex. Adding its exact half-turn retains referenceU1. Raising
the positive axial root preserves all old positive arrows into that root.
The resulting actual centroid is solved again, and inactive vertices are
retired only after the complete physical hull and census have been computed.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time
import numpy as np
from scipy.optimize import brentq
from scipy.spatial import QhullError
from geometry import arrows
from free_primal_goal import mesh_points
from primal_chain_mass_goal import quick_mass
from persistence_search import pairs

class Found(Exception):pass

def close_mass(raw):
    other=raw[1:];W=arrows(other);sinks=np.flatnonzero(W.max(1)<=1e-12)
    if not len(sinks) or np.any(other[sinks,2]<=0):raise ValueError('Axial-root strict sink bound unavailable')
    rmin=float(np.max(np.sum(other[sinks]**2,axis=1)/other[sinks,2]))*(1+1e-9)
    Y=raw.copy();Y[0,2]=rmin;V,g=quick_mass(Y)
    if g[2]>=0:return Y,False
    def f(r):
        Z=Y.copy();Z[0,2]=r;return float(quick_mass(Z)[1][2])
    high=max(raw[0,2],rmin*1.1)
    for _ in range(18):
        if f(high)>0:break
        high*=1.5
    if f(high)<=0:raise ValueError('No finite moving-apex mass bracket')
    Y[0,2]=brentq(f,rmin,high,xtol=1e-12);return Y,True

def run(source,out,rounds=18,samples=1800,seed=939916,exchanges=False):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);data=pathlib.Path(source).read_bytes();(out/'source_body.npz').write_bytes(data)
    X=np.load(out/'source_body.npz')['X'];rng=np.random.default_rng(seed);history=[];start=time.time()
    if np.linalg.norm(X[0,:2])>1e-12 or X[0,2]<=0:raise ValueError('Literal positive axial root absent')
    mirror=X*np.array([-1,-1,1]);dist=np.linalg.norm(X[:,None,:]-mirror[None,:,:],axis=2)
    if dist.min(1).max()>1e-10:raise ValueError('Input lacks literal C2 mass symmetry')
    m=mesh_points(X)
    if m['row']['U']!=1 or abs(m['g']).max()>1e-9:raise ValueError('Input is not an actual centred U1 body')
    (out/'definition.json').write_text(json.dumps(dict(source=str(pathlib.Path(source).resolve()),rounds=rounds,samples=samples,seed=seed,exchanges=exchanges,
        scope='Literal new physical caps, actual moving-apex mass closure, true hull vertex retirement; only own110 qualifies'),indent=2))
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes())
    def inspect(Y,label):
        mm=mesh_points(Y);row=mm['row']
        if 17<=row['E']<=249 and row['S']==row['U']==1:
            np.savez(out/'POTENTIAL_OWN110.npz',X=Y,Q=mm['Q']);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(label=label,**row),indent=2));raise Found()
        return mm
    try:
        for k in range(rounds):
            m=inspect(X,dict(round=k,stage='entrance'));st=m['row'];R=m['R'];Wq=arrows(R);stable=np.flatnonzero(Wq.max(1)<0)
            # The horizontal bottom facet is the desired stable carrier.
            eligible_stable=[int(j) for j in stable if np.linalg.norm(R[j,:2])>1e-8]
            if not eligible_stable:raise ValueError('No unwanted stable carrier to target')
            pairsQ,h=pairs(R,m['eq']);bars=1-h[pairsQ[:,1]]/np.sum(R[pairsQ[:,0]]**2,axis=1);basebar=float(max(bars,default=0));best_score=(st['S'],basebar);winner=None;failures={};tested=0
            bottom=float(X[:,2].min());orbits=[]
            if exchanges:
                for i in range(1,len(X)):
                    mate=int(np.argmin(np.linalg.norm(X-X[i]*np.array([-1,-1,1]),axis=1)))
                    if i<mate and X[i,2]>bottom+1e-8:orbits.append((i,mate))
            p=out/f'round{k:02d}';p.mkdir();np.savez(p/'parent.npz',X=X,Q=m['Q'])
            for j in range(samples):
                target=int(rng.choice(eligible_stable));normal=R[target]/np.linalg.norm(R[target]);bound=(X@R[target]+np.linalg.norm(X,axis=1)*np.linalg.norm(R[target]))/2
                choices=np.flatnonzero(bound>1+1e-7)
                if not len(choices):continue
                parent=int(rng.choice(choices));v=X[parent];sigma=rng.choice([.015,.07,.2,.5,1.])
                direction=normal+sigma*rng.normal(size=3);direction/=np.linalg.norm(direction)
                radius=np.linalg.norm(v)/2;factor=1-10**rng.uniform(-6,-.3);q=v/2+factor*radius*direction
                margin=float(q@(v-q))
                if margin<=1e-11 or q@R[target]<=1+1e-8 or q[2]<=bottom+1e-10:continue
                raw=np.r_[X,[q,q*np.array([-1,-1,1])]]
                label=dict(round=k,sample=j,target=target,parent=parent,point=q.tolist(),escape=margin)
                proposals=[([],raw)]
                if exchanges:
                    W=arrows(raw[1:]);ranked=[]
                    for orbit in orbits:
                        ids=np.array([a for a in range(len(raw)-1) if a+1 not in orbit],int);ww=W[np.ix_(ids,ids)]
                        sinks=ids[np.flatnonzero(ww.max(1)<=1e-12)];pts=raw[1:][sinks]
                        if not len(sinks) or np.any(pts[:,2]<=0):continue
                        minimum=float(np.max(np.sum(pts*pts,1)/pts[:,2]));ranked.append((minimum,orbit))
                    # Root-height feasibility orders the explicit alternatives;
                    # no deletion is silently treated as keeping old witnesses.
                    for _,orbit in sorted(ranked)[:5]:proposals.append((list(orbit),np.delete(raw,orbit,axis=0)))
                for removed,raw_proposal in proposals:
                    attempt=dict(**label,explicitly_removed_old_vertices=removed)
                    try:
                        Y,closed=close_mass(raw_proposal);mm=inspect(Y,attempt);tested+=1;row=mm['row']
                        if not closed or not 17<=row['E']<=249:continue
                        if abs(mm['g']).max()>2e-9 or row['U']!=1:raise ValueError('Independent actual mass/unique-U readback failed')
                        pp,h=pairs(mm['R'],mm['eq']);bb=1-h[pp[:,1]]/np.sum(mm['R'][pp[:,0]]**2,axis=1);value=float(max(bb,default=0));score=(row['S'],value)
                        if score<best_score:
                            best_score=score;active=mm['active']
                            if active[0]!=0:raise ValueError('The designated root was retired from its own U1 hull')
                            winner=(Y[active],dict(**attempt,**row,Qmax=value,retired_input_vertices=sorted(set(range(len(Y)))-set(map(int,active)))))
                            np.savez(p/'best.npz',X=Y[active],Q=mm['Q']);(p/'best.json').write_text(json.dumps(winner[1],indent=2));print('CYCLIC_MASS_FLOWER_IMPROVEMENT',json.dumps({key:val for key,val in winner[1].items() if key not in ['point','retired_input_vertices']}),flush=True)
                    except (ValueError,RuntimeError,AssertionError,QhullError,np.linalg.LinAlgError) as error:
                        key=str(error).split('\n')[0];failures[key]=failures.get(key,0)+1
            record=dict(round=k,parentS=st['S'],parentU=st['U'],parentE=st['E'],parentQmax=basebar,tested=tested,failures=failures,seconds=time.time()-start)
            if winner is None:
                record['adopted']=False;history.append(record);(out/'history.json').write_text(json.dumps(history,indent=2));break
            X,row=winner;record.update(adopted=True,result=row);history.append(record);np.savez(out/'latest.npz',X=X);(out/'history.json').write_text(json.dumps(history,indent=2))
    except Found:return
    (out/'FINITE_END.json').write_text(json.dumps(dict(rounds=len(history),seconds=time.time()-start,scope='Finite mass-closed positive-escape cap search ended without a qualifying body'),indent=2))

if __name__=='__main__':
    import sys
    run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 18,int(sys.argv[4]) if len(sys.argv)>4 else 1800)
