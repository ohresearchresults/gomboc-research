"""Simultaneous radial caps with an explicit old-shadow growth certificate.

Each new cap lies beyond one unwanted stable basin's saddle level. A selected
old point is grown enough to shadow it; all ancestors are grown to preserve
strict positive paths to the old unique unstable root. The four base inputs
share one common growth factor. Entire new hull and uniform mass are recomputed.
Only <=85 retained inputs enter mass-corrected refinement and exact goal audit.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
from vertex_geometry import geometry
from support_geometry import escape
from direct_face_polish import face_scores
from full_shadow_family import Family
from shadow_mass_retracted_goal import restore,bars,census,run as refine
from goal_nomination import preserve

def run(source,out,width):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(source);g=geometry(X,False);g['height_gap']=X[4:,2]-X[0,2];values,_,features=bars(g,False);vf,_,_=face_scores(g,False);root=len(X)-1;h=X[0,2];r=np.linalg.norm(X,axis=1);scores=X@X.T/np.sum(X*X,axis=1)[:,None]-1;np.fill_diagonal(scores,-np.inf);parent=scores.argmax(1);assert np.all(scores[np.arange(root),parent[:root]]>0);ratio=np.array([(X[i]@X[i])/(X[i]@X[parent[i]])for i in range(root)]);factor=ratio*(1+np.minimum(1e-8,(1/ratio-1)/4));assert max(factor)<1
    order=np.argsort(r);features=sorted(zip(values,features),reverse=True);unique={}
    for value,(u,i,j)in features:
        if np.all(g['T'][u]<4)or vf[u]>=0:continue
        a,b=g['H'][i],g['H'][j];e=b-a;t=np.clip(-(a@e)/(e@e)if e@e else 0,0,1);saddle=1/np.linalg.norm(a+t*e);n=g['H'][u]/np.linalg.norm(g['H'][u]);unique.setdefault(u,(saddle,n,float(value)))
    features=list(unique.items());history=[];pool=[];serial=0;start=time.time()
    for count in [len(features),min(20,len(features)),min(10,len(features))]:
        for lift in [.0001,.001,.005,.02,.06,.12]:
            for root_budget in [1.,1.08,1.25,1.6,2.]:
                serial+=1;caps=np.array([(1+lift)*data[0]*data[1]for _,data in features[:count]]);s=np.ones(len(X));s[root]=root_budget;witness=[]
                for w in caps:
                    prod=X@w;need=np.where(prod>0,(w@w)/np.maximum(prod,1e-300),np.inf)
                    if need[root]<=root_budget:j=root
                    else:
                        mx=max(prod);eligible=np.flatnonzero(prod>=mx*(1-1e-12));j=int(eligible[np.argmax(r[eligible])])
                    s[j]=max(s[j],need[j]*(1+1e-7));witness.append(j)
                converged=False
                for iteration in range(2*len(X)):
                    old=s.copy();a=max(1.,max(s[:4]));negative=s[4:]*X[4:,2]/h;a=max(a,float(max(negative,default=1.))*(1+1e-7));a=max(a,float(max(caps[:,2]/h,default=1.))*(1+1e-7));s[:4]=a
                    for i in order:
                        if i==root:continue
                        s[parent[i]]=max(s[parent[i]],s[i]*factor[i])
                    if max(abs(s-old))<1e-13*max(s):converged=True;break
                row=dict(case=serial,caps=count,lift=lift,root_budget=root_budget,scales=s.tolist(),cap_witnesses=witness,converged=converged)
                if not converged:history.append(row);continue
                Y=np.vstack((s[:-1,None]*X[:-1],caps,s[root]*X[root]));Y[:4,2]=s[0]*h
                try:
                    hh=ConvexHull(Y);ids=hh.vertices;last=len(Y)-1
                    if last not in ids:raise ValueError('certified root is not a hull vertex')
                    Z=np.vstack((Y[:4],Y[[i for i in ids if i>=4 and i!=last]],Y[last]));row.update(inputs=len(Z),numeric_hull_vertices=len(ids))
                    if len(Z)>85:history.append(row);continue
                    vg,_=escape(Z,angular=True)
                    if sum(vg<0)!=1:raise ValueError('reference shadow certificate failed numeric readback')
                    d=out/f'case{serial:04d}';d.mkdir();np.save(d/'raw_physical.npy',Z);F=Family(Z,cost_floor=1e-12);q=F.freeze_tree(F.q);q,gg,corr=restore(F,q,limit=100);row['mass_correction']=corr
                    if q is None:raise ValueError('actual mass and raw base equations did not close')
                    cc=census(gg);row.update(census=cc)
                    if cc['U']!=1 or not cc['base_valid']:raise ValueError('actual closed body failed U1/base')
                    vv,_,_=bars(gg,False);value=float(max(vv,default=0.));row['Qmax']=value;np.save(d/'physical.npy',gg['X']);np.save(d/'parameters.npy',q);(d/'construction.json').write_text(json.dumps(row,indent=2));pool.append((value,d,row))
                    if cc['S']==1:preserve(gg['X'],d/'exact_goal','simultaneous saddle-level radial caps with inherited positive-shadow paths and actual uniform mass closure, numerical own110')
                except(ValueError,np.linalg.LinAlgError)as err:row['rejected']=repr(err)
                history.append(row)
                if serial%20==0:print('BULK_BASIN_CAP_GOAL',serial,'admitted',len(pool),'best',min([p[0]for p in pool],default=None),'seconds',time.time()-start,flush=True)
    (out/'history.json').write_text(json.dumps(history,indent=2));pool.sort(key=lambda p:p[0])
    for _,d,row in pool[:width]:refine(d/'physical.npy',None,d/'goal_refinement',1600,full_shadow=True,fixed_tree=True,tree_seed=891512+row['case'],cost_floor=1e-12)
    print('BULK_BASIN_CAP_FINITE_STOP',serial,len(pool),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--width',type=int,default=8);a=p.parse_args();run(a.source,a.out,a.width)
