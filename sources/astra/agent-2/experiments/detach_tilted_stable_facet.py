"""Detach an apex-incident stable face by one genuine meridian slope break.
The new earlier plane remains fixed during compensation. All other meridian
controls are solved to restore the source's actual volume centroid while
satisfying every true support inequality. The final same-body census is
recomputed. This is a physical facet split, not an integration diagonal.
"""
import sys,json,hashlib
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
import jax
import jax.numpy as jnp
from tilting_profile_family import TiltingProfileFamily

def run(src,metadata,normal_src,out):
    src=Path(src);metadata=Path(metadata);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=src.read_bytes();mr=metadata.read_bytes();nr=Path(normal_src).read_bytes();(out/'source_q.npy').write_bytes(raw);(out/'source_metadata.json').write_bytes(mr);(out/'source_normals.npy').write_bytes(nr);oldq=np.load(out/'source_q.npy');meta=json.loads(mr);m,L=meta['m'],meta['L'];oldfam=TiltingProfileFamily(m,L,meta['breaks']);old=oldfam.state(oldq);sr=int(np.argmax(np.sum(old['Y']**2,1)));i,a,b=oldfam.segments[sr];target=old['g'];z=oldq[oldfam.K:oldfam.K+L];theta=oldq[-m:]
    if b!=L or a>=L-1:raise ValueError('the principal stable facet has no removable apex incidence in this profile')
    k=L-1;breaks=[bb.copy() for bb in oldfam.breaks];breaks[i].append(k);fam=TiltingProfileFamily(m,L,breaks);non=np.argwhere(~fam.contact);newface=next(j for j,t in enumerate(fam.segments) if t==(i,a,k));free=np.array([j for j in range(fam.K) if not fam.offset[i]<=j<fam.offset[i+1]],int);source_slope=float(old['N'][sr,2]);rows=[]
    (out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(raw).hexdigest(),metadata_source=str(metadata),metadata_sha256=hashlib.sha256(mr).hexdigest(),m=m,L=L,old_stable_face=sr,meridian=i,old_block=[a,b],new_break=k,new_earlier_facet=newface,target_centroid=target.tolist(),method=__doc__),indent=2)+'\n');(out/'producer.py').write_bytes(Path(__file__).read_bytes())
    for delta in [1e-6,1e-5,1e-4,.001,.003,.01,.03,.1]:
        control=[]
        for j in range(m):
            control.extend(oldq[oldfam.offset[j]:oldfam.offset[j+1]])
            if j==i:control.append(source_slope-delta)
        q=np.r_[control,oldq[oldfam.K:]];label=f'delta_{delta:g}';trace=[];np.save(out/(label+'_uncompensated_q.npy'),q)
        try:
            X,N,d,ns=fam.independent_construct(q);scale=np.linalg.norm(N,axis=1)[non[:,0]];floor=np.full(len(non),1e-8)
            @jax.jit
            def pieces(p):
                X,Z,Y,g,v,N,d=fam.physical(p);gap=(d[non[:,0]]-jnp.sum(N[non[:,0]]*X[non[:,1]],1))/jnp.asarray(scale);return jnp.r_[gap,g]
            jac=jax.jit(jax.jacfwd(pieces));converged=False
            for it in range(20):
                value=np.asarray(pieces(q));geo=value[:-3];g=value[-3:];error=float(abs(g-target).max());trace.append(dict(it=it,centroid_error=error,minimum_support_gap=float(geo.min())))
                if geo.min()>=.999e-8 and error<2e-13:converged=True;break
                J=np.asarray(jac(q))[:,free];C=J[:-3];G=J[-3:];D=len(free);A=np.r_[np.c_[-C,np.zeros(len(C))],np.c_[np.eye(D),-np.ones(D)],np.c_[-np.eye(D),-np.ones(D)]];rhs=np.r_[geo-floor,np.zeros(2*D)];r=linprog(np.r_[np.zeros(D),1.],A_ub=A*1000,b_ub=rhs*1000,A_eq=np.c_[G,np.zeros(3)]*1000,b_eq=(target-g)*1000,bounds=[(-.05,.05)]*D+[(0,.05)],method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-9))
                if not r.success:raise ValueError('fixed-detachment centroid compensation failed: '+r.message)
                q[free]+=r.x[:D]
            if not converged:raise ValueError('fixed-detachment true centroid correction did not converge')
            s=fam.state(q);centroid_error=float(abs(s['g']-target).max());apex_gap=float((s['d'][newface]-s['N'][newface]@s['X'][-1])/np.linalg.norm(s['N'][newface]));foot=s['g']+s['N'][newface]*(s['d'][newface]-s['N'][newface]@s['g'])/(s['N'][newface]@s['N'][newface]);others=np.delete(np.arange(s['F']),newface);foot_margin=float(np.min((s['d'][others]-s['N'][others]@foot)/np.linalg.norm(s['N'][others],axis=1)))
            if centroid_error>2e-13 or apex_gap<=0:raise ValueError('actual detached body fails centroid or apex separation')
        except (ValueError,AssertionError,np.linalg.LinAlgError) as e:rows.append(dict(label=label,error=repr(e),trace=trace));(out/'screen.json').write_text(json.dumps(rows,indent=2)+'\n');continue
        row={key:s[key] for key in ['V','E','F','S','U','Pmax','Qmax','minimum_noncontact']};row.update(label=label,delta=delta,m=m,L=L,breaks=breaks,centroid_error=centroid_error,detached_face=newface,actual_apex_separation=apex_gap,detached_face_foot_margin=foot_margin,global_stable_face=int(np.argmax(np.sum(s['Y']**2,1))));np.save(out/(label+'_q.npy'),q);(out/(label+'.json')).write_text(json.dumps(row,indent=2)+'\n');(out/(label+'_trace.json')).write_text(json.dumps(trace,indent=2)+'\n');rows.append(row);print('PHYSICAL_STABLE_FACET_DETACHMENT',row,flush=True)
        if s['S']==s['U']==1:np.save(out/'NUMERICAL_NOMINATION_q.npy',q);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n')
        (out/'screen.json').write_text(json.dumps(rows,indent=2)+'\n')

if __name__=='__main__':run(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
