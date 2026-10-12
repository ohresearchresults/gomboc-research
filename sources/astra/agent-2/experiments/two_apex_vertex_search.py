"""Global physical relocation of the second high-valence vertex.
The support-ring coordinates stay fixed and their common physical point moves;
the entire resulting support intersection and its own filled-volume mass are
reconstructed. No reference-center or inherited equilibrium claim is used.
"""
import sys,json,hashlib,time
from pathlib import Path
import numpy as np
from scipy.optimize import differential_evolution,minimize
from scipy.spatial import QhullError
from flexible_two_apex_supports import FlexibleTwoApexFamily

def run(src,out,m=44,n=20,generations=250):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=src.read_bytes();(out/'source_q.npy').write_bytes(raw);q=np.load(out/'source_q.npy');fam=FlexibleTwoApexFamily(m,n);s=fam.state(q);best=np.inf;calls=0;admitted=0;history=[];start=time.time()
    (out/'source.json').write_text(json.dumps(dict(path=str(src),sha256=hashlib.sha256(raw).hexdigest(),m=m,n=n,method=__doc__),indent=2)+'\n')
    class Found(Exception):pass
    def fun(v):
        nonlocal best,calls,admitted
        qq=q.copy();qq[-3:]=v;calls+=1
        try:t=fam.state(qq)
        except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError):return np.inf
        admitted+=1;score=float(max(t['Pmax'],t['Qmax'])+.1*(t['P'].mean()+t['Q'].mean()))
        if score<best:
            best=score;row={k:t[k] for k in ['V','E','F','S','U','Pmax','Qmax','minimum_noncontact','active_anchors']};row.update(calls=calls,admitted=admitted,seconds=time.time()-start,score=score,physical_vertex=list(map(float,v)))
            history.append(row);np.save(out/'best_q.npy',qq);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n');print('PHYSICAL_SECOND_VERTEX_SEARCH',row,flush=True)
        if t['S']==t['U']==1:
            np.save(out/'NUMERICAL_NOMINATION_q.npy',qq);np.save(out/'NUMERICAL_NOMINATION_H.npy',t['H']);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(dict(V=t['V'],E=t['E'],F=t['F'],S=t['S'],U=t['U'],m=m,n=n,actual_centroid=t['g'].tolist()),indent=2)+'\n');raise Found()
        return score
    try:
        fun(q[-3:]);p=s['pp'][np.argmax(s['P'])];a,b=s['X'][p[1:]];d=b-a;t=np.clip(-(a-s['g'])@d/(d@d),0,1);death=a+t*d
        for destination in [s['g'],death,(s['g']+death)/2]:
            for alpha in np.linspace(.02,1.4,65):fun((1-alpha)*q[-3:]+alpha*destination)
        v=q[-3:];bounds=[(v[0]-.65,v[0]+.65),(v[1]-.65,v[1]+.65),(min(v[2]-.35,-.03),-.015)]
        result=differential_evolution(fun,bounds,x0=v,popsize=10,maxiter=generations,seed=98471,polish=False,tol=1e-9)
        minimize(fun,result.x,method='Nelder-Mead',options=dict(maxiter=900,xatol=1e-12,fatol=1e-13))
    except Found:return
    (out/'FINITE_BRANCH_END.json').write_text(json.dumps(dict(calls=calls,admitted=admitted,score=best,goal_complete=False),indent=2)+'\n')

if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 44,int(sys.argv[4]) if len(sys.argv)>4 else 20,int(sys.argv[5]) if len(sys.argv)>5 else 250)
