"""Literal C2 planar quadrilateral replacements to release true edge budget.

Every proposal moves physical points, closes uniform mass by its axial apex,
and rebuilds all maximal facets. Coplanar faces are numerical nominations only;
any own110 result requires exact rational incidence and weak-contact audit.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time,hashlib
import numpy as np
from scipy.spatial import QhullError
from free_primal_goal import mesh_points
from cyclic_flower_mass_goal import close_mass
from persistence_search import pairs

def run(source,out,rounds=12,patches=90):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False)
    data=pathlib.Path(source).read_bytes();(out/'source_body.npz').write_bytes(data)
    X=np.load(out/'source_body.npz')['X'];start=time.time();hist=[]
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes())
    (out/'definition.json').write_text(json.dumps(dict(source=str(pathlib.Path(source).resolve()),
        sha256=hashlib.sha256(data).hexdigest(),rounds=rounds,patches=patches,
        scope='Actual physical planar patches; U1 and own mass retained, strict edge decrease; only complete own110 qualifies'),indent=2))
    def inspect(Y,label):
        m=mesh_points(Y)
        if 17<=m['row']['E']<=249 and m['row']['S']==m['row']['U']==1:
            np.savez(out/'POTENTIAL_OWN110.npz',X=Y,Q=m['Q'])
            (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(**label,**m['row']),indent=2))
            return m,True
        return m,False
    for k in range(rounds):
        m,found=inspect(X,dict(round=k,stage='entrance'))
        if found:return
        if m['row']['U']!=1 or max(abs(m['g']))>2e-9:raise ValueError('Entrance is not actual own U1')
        mirror=X*np.array([-1,-1,1]);dist=np.linalg.norm(X[:,None,:]-mirror[None,:,:],axis=2)
        mate=dist.argmin(1)
        if dist.min(1).max()>1e-10 or mate[0]!=0:raise ValueError('Literal C2 apex symmetry missing')
        floor=set(np.flatnonzero(X[:,2]<X[:,2].min()+1e-9));edgefaces={}
        for f,cy in enumerate(m['faces']):
            for a,b in zip(cy,cy[1:]+cy[:1]):edgefaces.setdefault(tuple(sorted((a,b))),[]).append(f)
        candidates=[];seen=set()
        for e,fs in edgefaces.items():
            if len(fs)!=2 or any(len(m['faces'][f])!=3 for f in fs):continue
            nodes=sorted(set(m['faces'][fs[0]])|set(m['faces'][fs[1]]));mir=sorted(map(int,mate[nodes]));key=min(tuple(nodes),tuple(mir))
            if len(nodes)!=4 or 0 in nodes or floor.intersection(nodes) or set(nodes).intersection(mir) or key in seen:continue
            seen.add(key);a,b=m['Q'][fs];a=a/np.linalg.norm(a);b=b/np.linalg.norm(b)
            candidates.append((float(np.linalg.norm(a-b)),e,fs,nodes))
        candidates.sort();best=None;bestscore=(m['row']['S'],m['row']['E'],float('inf'));failures={};tested=0
        p=out/f'round{k:02d}';p.mkdir();np.savez(p/'parent.npz',X=X)
        for rank,(angle,e,fs,nodes) in enumerate(candidates[:patches]):
            for theta in [0.,.25,.5,.75,1.]:
                n=(1-theta)*m['Q'][fs[0]]+theta*m['Q'][fs[1]];dots=X[nodes]@n
                for mode,d in [('min',dots.min()),('mean',dots.mean()),('max',dots.max())]:
                    Y=X.copy();Y[nodes]+=((d-dots)/(n@n))[:,None]*n
                    Y[mate[nodes]]=Y[nodes]*np.array([-1,-1,1])
                    label=dict(round=k,rank=rank,edge=list(e),faces=fs,nodes=nodes,theta=theta,plane_offset_mode=mode,angle=angle)
                    try:
                        Y,closed=close_mass(Y)
                        mm,found=inspect(Y,label);tested+=1
                        if found:return
                        row=mm['row']
                        if not closed or row['U']!=1 or max(abs(mm['g']))>2e-9 or row['E']>=m['row']['E'] or row['S']>m['row']['S']:continue
                        pp,h=pairs(mm['R'],mm['eq']);bars=1-h[pp[:,1]]/np.sum(mm['R'][pp[:,0]]**2,axis=1);qmax=float(max(bars,default=0))
                        score=(row['S'],row['E'],qmax)
                        if score<bestscore:
                            act=mm['active']
                            if act[0]!=0:raise ValueError('Axial root disappeared')
                            bestscore=score;best=(Y[act],dict(**label,**row,Qmax=qmax))
                            np.savez(p/'best.npz',X=best[0]);(p/'best.json').write_text(json.dumps(best[1],indent=2))
                            print('C2_PLANAR_COARSENING',json.dumps(best[1]),flush=True)
                    except (ValueError,RuntimeError,AssertionError,QhullError,np.linalg.LinAlgError) as err:
                        key=str(err).split('\n')[0];failures[key]=failures.get(key,0)+1
        rec=dict(round=k,parent=m['row'],tested=tested,patches=len(candidates),failures=failures,seconds=time.time()-start,adopted=best is not None)
        if best is not None:X,rec['result']=best;np.savez(out/'latest.npz',X=X)
        hist.append(rec);(out/'history.json').write_text(json.dumps(hist,indent=2))
        if best is None:break
    (out/'FINITE_END.json').write_text(json.dumps(dict(rounds=len(hist),seconds=time.time()-start,scope='Numerical edge-budget coarsening completed; no qualifying body'),indent=2))

if __name__=='__main__':
    import sys
    run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 12,int(sys.argv[4]) if len(sys.argv)>4 else 90)
