"""Adaptive positive-shadow caps, actual mass correction, then goal minimax.

Unused interior inputs are removed to define a NEW literal body. New cap points
are inside an existing vertex's open Thales ball at reference0. Every retained
candidate is restored to its actual uniform centroid before refinement. All
positive bars remain in the audit and every own110 triggers an exact freeze.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from vertex_geometry import geometry
from bounded_cap_beam_goal import points
from shadow_centroid_goal import Family
from shadow_mass_retracted_goal import restore,model,bars,census,run as refine
from goal_nomination import preserve

def compress(X):
    g=geometry(X,False);ids=g['vertices'];root=len(X)-1;assert root in ids
    return np.vstack((X[:4],X[[i for i in ids if i>=4 and i!=root]],X[root]))

def run(source,out,rounds,width,full_shadow=False):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);X=compress(np.load(source));rng=np.random.default_rng(702951);history=[];serial=0;start=time.time()
    for level in range(rounds):
        if len(X)>=85:print('SHADOW_CAP_INPUT_BOUND',level,len(X),flush=True);break
        ld=out/f'level{level:02d}';ld.mkdir();np.save(ld/'source.npy',X);g=geometry(X,False);g['height_gap']=X[4:-1,2]-X[0,2];v,_,features=bars(g,False);old=max(v,default=0.);birth=features[int(np.argmax(v))][0];rootface=int(np.argmax(np.sum(g['H']**2,axis=1)));targets=[f for f in dict.fromkeys([birth,rootface])if not np.all(g['T'][f]<4)]
        ref=dict(g,Z=X,g=np.zeros(3),H=np.linalg.solve(X[g['T']],np.ones((len(g['T']),3,1)))[:,:,0]);pool=[]
        with (ld/'trials.jsonl').open('w')as log:
            for p,info in points(ref,targets,rng):
                serial+=1
                if p[2]<=X[0,2]+1e-6:continue
                Y=np.vstack((X[:-1],p,X[-1]));gg=geometry(Y,False)
                if len(Y)-2 not in gg['vertices']:continue
                gg['height_gap']=Y[4:-1,2]-Y[0,2];vals,_,_=bars(gg,False);cc=census(gg);row=dict(serial=serial,Qmax=float(max(vals,default=0.)),centroid_norm=float(np.linalg.norm(gg['g'])),point=p.tolist(),**info,**cc);log.write(json.dumps(row)+'\n')
                if cc['S']==cc['U']==1 and cc['base_valid']:preserve(Y,ld/f'exact_raw_goal_{serial}','underbound positive-shadow cap, actual centroid numerical110')
                pool.append((row['Qmax']+2*row['centroid_norm'],Y,row))
        pool.sort(key=lambda x:x[0]);restored=[];seen=set()
        for _,Y,row in pool:
            key=(row['facet'],row['witness'],row['fraction'])
            if key in seen:continue
            seen.add(key)
            if len(seen)>40:break
            try:
                if full_shadow:
                    from full_shadow_family import Family as FullFamily
                    FF=FullFamily(Y)
                else:FF=Family(Y)
                q,gg,correction=restore(FF,FF.q)
                if q is None:continue
                vv,_,_=bars(gg,False);cc=census(gg)
                if cc['U']!=1 or not cc['base_valid']:continue
                row.update(restored_Q=float(max(vv,default=0.)),restored_counts=cc,correction=correction);restored.append((row['restored_Q'],gg['X'],q,row))
            except(ValueError,np.linalg.LinAlgError):continue
        restored.sort(key=lambda x:x[0]);candidates=[]
        for k,(value,Y,q,row)in enumerate(restored[:width]):
            d=ld/f'candidate{k:02d}';d.mkdir();np.save(d/'physical.npy',Y);np.save(d/'parameters.npy',q);(d/'construction.json').write_text(json.dumps(row,indent=2))
            refine(d/'physical.npy',None,d/'refinement',600,full_shadow=full_shadow);Z=np.load(d/'refinement/endpoint.npy');ZZ=compress(Z);gg=geometry(ZZ,False);gg['height_gap']=ZZ[4:-1,2]-ZZ[0,2];vv,_,_=bars(gg,False);score=float(max(vv,default=0.));candidates.append((score,ZZ,str(d)));np.save(d/'compressed_endpoint.npy',ZZ)
        if not candidates:print('SHADOW_CAP_NO_ADMITTED_REFINEMENT',level,len(pool),flush=True);break
        value,Y,path=min(candidates,key=lambda x:x[0]);row=dict(level=level,raw_trials=len(pool),mass_closed=len(restored),old_Q=float(old),best_Q=value,inputs=len(Y),selected=path,seconds=time.time()-start);history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('SHADOW_CAP_ADAPT',row,flush=True)
        if value>=old-1e-8:break
        X=Y;np.save(out/'latest.npy',X)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--rounds',type=int,default=8);p.add_argument('--width',type=int,default=4);p.add_argument('--full-shadow',action='store_true');a=p.parse_args();run(a.source,a.out,a.rounds,a.width,a.full_shadow)
