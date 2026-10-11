"""Finite root extension plus radial cap proposals for the qualifying Figure.

Extending the existing unstable root preserves every old reference escape path.
A new radial point above a stable face is shadowed by that extended root when
t > |w|^2/(w.root). The source and new body are distinct; their actual uniform
mass is recomputed, then six physical mass/base equations are restored while
holding the new cap's direction fixed. No nonwinner can complete the goal.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
from vertex_geometry import geometry
from direct_face_polish import face_scores
from support_geometry import escape
from full_shadow_family import Family
from shadow_mass_retracted_goal import restore,bars,run as refine
from goal_nomination import preserve

def classify(g):
    f,_,_=face_scores(g,False);mask=~np.all(g['T']<4,axis=1);b=ConvexHull(g['X'][:4,:2]);bs=float(max(b.equations[:,:2]@g['g'][:2]+b.equations[:,2]))<0;u,_=escape(g['Z'][g['vertices']],angular=True)
    return dict(S=int(sum(f[mask]<0))+int(bs),U=int(sum(u<0)),base_stable=bool(bs),V=len(g['vertices']))

def run(source,out,maxcases,width):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(source);assert len(X)<85;g=geometry(X,False);f,_,_=face_scores(g,False);stable=[int(i)for i in np.flatnonzero(f<0)if not np.all(g['T'][i]<4)];H=np.linalg.solve(X[g['T']],np.ones((len(g['T']),3,1)))[:,:,0];root=X[-1];pool=[];history=[];serial=0;start=time.time()
    stable.sort(key=lambda i:-np.linalg.norm(H[i]));targets=stable[:8]
    for face in targets:
        n=H[face]/np.linalg.norm(H[face]);h=1/np.linalg.norm(H[face]);nr=float(n@root)
        if nr<=0:continue
        for height_fraction in [.0003,.001,.003,.01,.03,.08,.15]:
            w=(h+height_fraction*np.linalg.norm(root))*n
            if w[2]<=X[0,2]+1e-6:continue
            required=float((w@w)/(w@root))
            for extra in [.0001,.003,.015,.06]:
                t=max(1.,required)*(1+extra)
                if t>2 or t*root[2]<=X[0,2]+1e-6:continue
                serial+=1
                if serial>maxcases:break
                Y=np.vstack((X[:-1],w,t*root));row=dict(case=serial,face=face,height_fraction=height_fraction,root_extension=t,required_extension=required,cap=w.tolist());d=out/f'case{serial:04d}';d.mkdir();np.save(d/'raw_physical.npy',Y)
                try:
                    gg=geometry(Y,False);cc=classify(gg);row['raw_census']=cc
                    if cc['S']==cc['U']==1:preserve(Y,d/'exact_raw_goal','new root-extended radial cap, complete numerical actual own110')
                    F=Family(Y);q=F.freeze_tree(F.q);F.restore_free=np.arange(2*(F.n-1));q,gg,corr=restore(F,q,limit=70);row['mass_correction']=corr
                    if q is None:raise ValueError('six physical constraints did not close')
                    cc=classify(gg)
                    if cc['U']!=1:raise ValueError('closed body lost unique unstable equilibrium')
                    vv,_,_=bars(gg,False);value=float(max(vv,default=0.));row.update(Qmax=value,closed_census=cc);np.save(d/'physical.npy',gg['X']);np.save(d/'parameters.npy',q);(d/'fixed_tree.json').write_text(json.dumps(dict(parent=F.fixed_parent.tolist(),order=F.fixed_order),indent=2));pool.append((value,d,row))
                    if cc['S']==cc['U']==1:preserve(gg['X'],d/'exact_closed_goal','root-extended radial cap with actual uniform mass closure and numerical own110')
                except(ValueError,np.linalg.LinAlgError)as err:row['rejected']=repr(err)
                (d/'construction.json').write_text(json.dumps(row,indent=2));history.append(row)
                if serial%10==0:print('ROOT_EXTENDED_CAP_GOAL',serial,'closed',len(pool),'best',min([v for v,_,_ in pool],default=None),'seconds',time.time()-start,flush=True)
            if serial>maxcases:break
        if serial>maxcases:break
    (out/'history.json').write_text(json.dumps(history,indent=2));pool.sort(key=lambda x:x[0])
    for value,d,row in pool[:width]:refine(d/'physical.npy',None,d/'goal_refinement',1400,full_shadow=True,fixed_tree=True,tree_seed=892730+row['case'])
    print('ROOT_EXTENDED_CAP_FINITE_STOP',serial,len(pool),min([v for v,_,_ in pool],default=None),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--cases',type=int,default=160);p.add_argument('--width',type=int,default=6);a=p.parse_args();run(a.source,a.out,a.cases,a.width)
