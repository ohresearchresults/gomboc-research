"""Broad physical cuts plus thickness change; every score uses fresh solid mass."""
import argparse,json,time
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.optimize import differential_evolution
from scipy.spatial import ConvexHull,QhullError
from geometry import census,persistence,mass,write_json


def clip(points,normal,fraction):
    z=points@normal;level=min(z)+fraction*(max(z)-min(z));keep=points[z<=level]
    hull=ConvexHull(points);pairs=set()
    for triangle in hull.simplices:
        for i,j in zip(triangle,np.roll(triangle,1)):pairs.add(tuple(sorted((int(i),int(j)))))
    extra=[]
    for i,j in pairs:
        if (z[i]-level)*(z[j]-level)<0:
            t=(level-z[i])/(z[j]-z[i]);extra.append(points[i]+t*(points[j]-points[i]))
    assert len(extra)>0
    result=np.r_[keep,extra];hull=ConvexHull(result)
    return result[hull.vertices]


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',default='work/pyramid-101-exact/POINTS.json')
    ap.add_argument('--out',required=True);ap.add_argument('--cuts',type=int,default=1)
    ap.add_argument('--restarts',type=int,default=4);ap.add_argument('--iterations',type=int,default=150)
    args=ap.parse_args();out=Path(args.out);out.mkdir(exist_ok=False)
    p=np.array(json.loads(Path(args.input).read_text())['points'],float);p-=mass(p)[1];p/=max(np.linalg.norm(p,axis=1))
    bounds=[(-1.,3.5),(-.7,.7)]+[(0.,np.pi),(-np.pi,np.pi),(.05,.995)]*args.cuts
    best=[np.inf];evals=[0];history=[];start=time.time();winner=[False]
    def build(z):
        q=p*np.exp([z[1],z[0],-z[1]])
        for k in range(args.cuts):
            theta,phi,fraction=z[2+3*k:5+3*k]
            n=np.array([np.sin(theta)*np.cos(phi),np.sin(theta)*np.sin(phi),np.cos(theta)])
            q=clip(q,n,fraction)
        return q
    def objective(z,weight):
        evals[0]+=1
        try:
            q=build(z);r=census(q,True);xx=max(np.einsum('ij,ij->i',r['x'],r['x']));qq=max(np.einsum('ij,ij->i',r['q'],r['q']))
            sb=persistence(r['q'])/xx;ub=persistence(r['x'])/qq;ratio=1/np.sqrt(xx*qq)
            score=sb+weight*ub+10*max(0.,.03-ratio)**2
            if score<best[0]:
                best[0]=score;rec=dict(score=float(score),stable_bar=float(sb),unstable_bar=float(ub),ratio=float(ratio),
                                     weight=weight,parameters=z.tolist(),points=q.tolist(),census=census(q),nfev=evals[0])
                write_json(out/'BEST.json',rec)
            if r['S']==r['U']==1 and r['S_uncertain']==r['U_uncertain']==0:
                winner[0]=True;write_json(out/'PROPOSAL110.json',dict(points=q.tolist(),parameters=z.tolist(),census=census(q)))
            return score
        except(QhullError,AssertionError,ValueError,np.linalg.LinAlgError):return 1e6
    for restart in range(args.restarts):
        weight=[1.,10.,100.,1000.][restart%4];best[0]=np.inf
        result=differential_evolution(lambda z:objective(z,weight),bounds,popsize=9,maxiter=args.iterations,
                                     seed=96100+restart,polish=False,workers=1,callback=lambda x,convergence:winner[0])
        q=build(result.x);record=dict(restart=restart,weight=weight,score=float(result.fun),parameters=result.x.tolist(),
                                     points=q.tolist(),census=census(q),nfev=evals[0])
        write_json(out/f'RESTART{restart}.json',record);history.append({k:v for k,v in record.items()if k!='points'})
        write_json(out/'SEARCH.json',dict(config=vars(args),history=history,nfev=evals[0],elapsed=time.time()-start))
        print('CUT_RESTART',restart,result.fun,record['census']['S'],record['census']['U'],record['census']['E_proposal'],evals[0],flush=True)
        if winner[0]:break


if __name__=='__main__':main()
