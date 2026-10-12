"""Joint stable-carrier cap and lower mass countercap on a physical C2 hull.

New vertices lie strictly inside diameter balls of existing physical vertices.
After explicit orbit removals, all radial sinks are recomputed, a sufficient
axial-root height is imposed, and the actual uniform centroid is solved.
The numerical hull is independently rebuilt; only own110 nominates a figure.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time,hashlib,itertools
import numpy as np
from scipy.spatial import QhullError
from cyclic_flower_mass_goal import close_mass,Found
from free_primal_goal import mesh_points
from geometry import arrows
from persistence_search import pairs

def run(source,out,rounds=16,samples=2200,seed=931792):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);data=pathlib.Path(source).read_bytes();(out/'source_body.npz').write_bytes(data)
    X=np.load(out/'source_body.npz')['X'];m=mesh_points(X);X=X[m['active']]
    rng=np.random.default_rng(seed);hist=[];start=time.time()
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes())
    (out/'definition.json').write_text(json.dumps(dict(source=str(pathlib.Path(source).resolve()),sha256=hashlib.sha256(data).hexdigest(),rounds=rounds,samples=samples,seed=seed,
        scope='Joint literal cap pairs with actual mass closure; alternative orbit deletions explicit; only own110 qualifies'),indent=2))
    def inspect(Y,label):
        mm=mesh_points(Y);row=mm['row']
        if 17<=row['E']<=249 and row['S']==row['U']==1:
            np.savez(out/'POTENTIAL_OWN110.npz',X=Y,Q=mm['Q']);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(**label,**row),indent=2));raise Found()
        return mm
    try:
        for k in range(rounds):
            m=inspect(X,dict(round=k,stage='entrance'));st=m['row']
            if st['U']!=1 or max(abs(m['g']))>2e-9:raise ValueError('Actual centred U1 entrance required')
            pp,h=pairs(m['R'],m['eq']);bb=1-h[pp[:,1]]/np.sum(m['R'][pp[:,0]]**2,axis=1);base=(st['S'],float(max(bb,default=0)));bestscore=base;best=None
            stable=np.flatnonzero(arrows(m['R']).max(1)<0);targets=[int(j) for j in stable if np.linalg.norm(m['R'][j,:2])>1e-8]
            bottom=float(X[:,2].min());mate=np.linalg.norm(X[:,None]-X[None,:]*np.array([-1,-1,1]),axis=2).argmin(1)
            if np.max(np.linalg.norm(X[mate]-X*np.array([-1,-1,1]),axis=1))>1e-9 or mate[0]!=0:raise ValueError('Literal C2 pairing failed')
            orbits=[(i,int(mate[i])) for i in range(1,len(X)) if i<mate[i] and X[i,2]>bottom+1e-8]
            lowerparents=np.flatnonzero(X[:,2]<0);p=out/f'round{k:02d}';p.mkdir();np.savez(p/'parent.npz',X=X);tested=0;failed={}
            for j in range(samples):
                target=int(rng.choice(targets));R=m['R'][target];n=R/np.linalg.norm(R);bound=(X@R+np.linalg.norm(X,axis=1)*np.linalg.norm(R))/2;parents=np.flatnonzero(bound>1+1e-7)
                if not len(parents):continue
                parent=int(rng.choice(parents));v=X[parent];d=n+rng.choice([.01,.04,.12,.3])*rng.normal(size=3);d/=np.linalg.norm(d)
                q=v/2+(1-10**rng.uniform(-6,-.5))*np.linalg.norm(v)/2*d
                if q@R<=1+1e-7 or q[2]<=bottom+1e-9 or q@(v-q)<=1e-11:continue
                parent2=int(rng.choice(lowerparents));v2=X[parent2]
                # Bias outward below the equator; this is a free physical
                # countercap, not an imposed point mass or density change.
                d2=v2/np.linalg.norm(v2)+rng.choice([.15,.5,1.])*rng.normal(size=3);d2[2]=-abs(d2[2]);d2/=np.linalg.norm(d2)
                r=v2/2+(1-10**rng.uniform(-6,-.5))*np.linalg.norm(v2)/2*d2
                if not bottom+1e-9<r[2]<0 or r@(v2-r)<=1e-11 or np.max(m['Q']@r)<=1+1e-7:continue
                raw=np.r_[X,[q,q*np.array([-1,-1,1]),r,r*np.array([-1,-1,1])]]
                alternatives=[()]
                # Include varied explicit replacements even when minimum
                # root-height ties would otherwise select the same orbit.
                if st['E']>235:
                    chosen=rng.choice(len(orbits),size=min(7,len(orbits)),replace=False)
                    alternatives.extend(orbits[t] for t in chosen)
                    alternatives.extend(tuple(sorted(orbits[a]+orbits[b])) for a,b in itertools.combinations(chosen[:4],2))
                label=dict(round=k,sample=j,target=target,parents=[parent,parent2],new_points=[q.tolist(),r.tolist()])
                ranked=[]
                for removed in alternatives:
                    Y=np.delete(raw,removed,axis=0);other=Y[1:];W=arrows(other);sinks=np.flatnonzero(W.max(1)<=1e-12)
                    if not len(sinks) or np.any(other[sinks,2]<=0):continue
                    rmin=float(np.max(np.sum(other[sinks]**2,axis=1)/other[sinks,2]));ranked.append((rmin,removed,Y))
                # Both low required height and distinct retirements are
                # represented; the actual hull count remains the admission.
                for _,removed,Y in sorted(ranked,key=lambda a:a[0])[:8]:
                    try:
                        Y,closed=close_mass(Y);attempt=dict(**label,explicitly_removed_old_vertices=list(removed));mm=inspect(Y,attempt);tested+=1;row=mm['row']
                        if not closed or not 17<=row['E']<=249:continue
                        if row['U']!=1 or max(abs(mm['g']))>2e-9:raise ValueError('Independent own U1/mass readback failed')
                        pp,h=pairs(mm['R'],mm['eq']);bb=1-h[pp[:,1]]/np.sum(mm['R'][pp[:,0]]**2,axis=1);qmax=float(max(bb,default=0));score=(row['S'],qmax)
                        if score<bestscore:
                            if mm['active'][0]!=0:raise ValueError('Axial root lost')
                            bestscore=score;best=(Y[mm['active']],dict(**attempt,**row,Qmax=qmax));np.savez(p/'best.npz',X=best[0]);(p/'best.json').write_text(json.dumps(best[1],indent=2))
                            print('PAIRED_PHYSICAL_CAP',json.dumps({a:b for a,b in best[1].items() if a!='new_points'}),flush=True)
                    except (ValueError,RuntimeError,AssertionError,QhullError,np.linalg.LinAlgError) as err:
                        key=str(err).split('\n')[0];failed[key]=failed.get(key,0)+1
            rec=dict(round=k,parent=st,parentQmax=base[1],tested=tested,failures=failed,adopted=best is not None,seconds=time.time()-start)
            if best is not None:X,rec['result']=best;np.savez(out/'latest.npz',X=X)
            hist.append(rec);(out/'history.json').write_text(json.dumps(hist,indent=2))
            if best is None:break
    except Found:return
    (out/'FINITE_END.json').write_text(json.dumps(dict(rounds=len(hist),seconds=time.time()-start,scope='Finite joint physical cap search ended without a qualifying body'),indent=2))

if __name__=='__main__':
    import sys
    run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 16,int(sys.argv[4]) if len(sys.argv)>4 else 2200)
