"""Physical roof caps to supply free fibre-height controls within84vertices."""
import pathlib,json,time
import numpy as np
from scipy.spatial import QhullError
from free_primal_goal import mesh_points

def run(source,out,target=78):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);data=pathlib.Path(source).read_bytes();(out/'source_body.npz').write_bytes(data);d=np.load(out/'source_body.npz');X=d['X'];v=d['direction'];v=v/np.linalg.norm(v);hist=[];start=time.time()
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes());(out/'definition.json').write_text(json.dumps(dict(source=str(pathlib.Path(source).resolve()),target=target,scope='Literal small roof caps preserving numerical own1/2 as a direct figure-search seed; not an accepted body'),indent=2))
    for step in range(100):
        m=mesh_points(X);X=X[m['active']]-m['g'];m=mesh_points(X)
        if m['row']['S']!=1 or m['row']['U']!=2:raise ValueError('Literal height seed lost its stated own1/2 entrance')
        if len(X)>=target:break
        choices=[]
        for f,cy in enumerate(m['faces']):
            q=m['Q'][f]
            if abs(q@v)<1e-8:continue
            pts=X[cy];center=pts.mean(0);area=sum(np.linalg.norm(np.cross(pts[i]-pts[0],pts[i+1]-pts[0])) for i in range(1,len(pts)-1))/2;choices.append((area,f,center))
        accepted=False;attempts=[]
        for area,f,center in sorted(choices,reverse=True)[:25]:
            for relative_height in [1e-4,1e-5,1e-6]:
                delta=relative_height*np.sqrt(area);p=center+np.sign(m['Q'][f]@v)*delta*v;Y=np.r_[X,[p]]
                try:
                    mm=mesh_points(Y);r=mm['row'];attempts.append(dict(face=f,relative_height=relative_height,**r))
                    if r['S']==1 and r['U']==2 and len(X)<r['V']<=84 and r['E']<=249:
                        X=Y[mm['active']]-mm['g'];accepted=True;rec=dict(step=step,face=f,relative_height=relative_height,**r,seconds=time.time()-start);hist.append(rec);np.savez(out/'latest.npz',X=X,direction=v,matrix=np.eye(3),parameters=np.zeros(6));(out/'history.json').write_text(json.dumps(hist,indent=2));print('FIBRE_HEIGHT_SEED_REFINEMENT',json.dumps(rec),flush=True);break
                except (ValueError,QhullError,np.linalg.LinAlgError) as e:attempts.append(dict(face=f,relative_height=relative_height,error=str(e)))
            if accepted:break
        if not accepted:
            (out/'unadmitted_caps.json').write_text(json.dumps(attempts,indent=2));break
    (out/'FINITE_SEED.json').write_text(json.dumps(dict(vertices=len(X),seconds=time.time()-start,scope='Refined actual-centroid1/2 seed only; complete own110 remains the goal'),indent=2))

if __name__=='__main__':
    import sys
    run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 78)
