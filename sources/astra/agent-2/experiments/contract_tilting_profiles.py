"""Actual coplanar facet contractions with explicit uniform-centroid restoration.
Sparse tilted-profile slope blocks merge genuine facets. A bounded Newton/LP
corrector changes their physical controls until complete support inequalities
hold and the actual filled centroid returns to the source centroid. No centroid
is substituted into an unchanged body; final mass and census are rebuilt.
"""
import sys,json,hashlib,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
import jax
import jax.numpy as jnp
from tilting_section_family import TiltingSectionFamily
from tilting_profile_family import TiltingProfileFamily

def run(src,normal_src,out,L):
    src=Path(src);normal_src=Path(normal_src);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=src.read_bytes();nr=normal_src.read_bytes();(out/'source_q.npy').write_bytes(raw);(out/'source_normals.npy').write_bytes(nr);oldq=np.load(out/'source_q.npy');normals=np.load(out/'source_normals.npy');m=len(normals);H=m*L;old=TiltingSectionFamily(normals,L).state(oldq);target=old['g'];z=oldq[H:H+L];tilts=oldq[H+L:H+3*L];theta=oldq[-m:];slopes=oldq[m:H].reshape(L-1,m);heights=np.r_[oldq[:m].reshape(1,m),oldq[:m]-np.cumsum(slopes*np.diff(z)[:,None],axis=0)];N=old['N'][:-1].reshape(L,m,3);unit=N/np.linalg.norm(N,axis=2)[:,:,None];turn=np.arccos(np.clip(np.sum(unit[:-1]*unit[1:],axis=2),-1,1));rows=[]
    (out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(raw).hexdigest(),normal_source=str(normal_src),normal_sha256=hashlib.sha256(nr).hexdigest(),m=m,L=L,target_centroid=target.tolist(),source_counts={k:old[k] for k in ['V','E','F','S','U','Pmax','Qmax']},method=__doc__),indent=2)+'\n')
    for name in ['tilting_profile_family.py','contract_tilting_profiles.py','concave_profile_family.py']:(out/name).write_bytes((Path(__file__).parent/name).read_bytes())
    for threshold in [1e-6,1e-5,1e-4,.001,.003,.01]:
        breaks=[[0]+[k for k in range(1,L) if turn[k-1,i]>=threshold] for i in range(m)];controls=[]
        for i,bb in enumerate(breaks):
            controls.append(oldq[i])
            for a,b in zip(bb[:-1],bb[1:]):controls.append((heights[a,i]-heights[b,i])/(z[b]-z[a]))
        q=np.r_[controls,z,tilts,theta];label=f'turn_{threshold:g}';np.save(out/(label+'_unprojected_q.npy'),q);trace=[]
        try:
            fam=TiltingProfileFamily(m,L,breaks);non=np.argwhere(~fam.contact);X,N0,d,ns=fam.independent_construct(q);scale=np.linalg.norm(N0,axis=1)[non[:,0]];floor=np.full(len(non),1e-8)
            @jax.jit
            def pieces(p):
                X,Z,Y,g,v,N,d=fam.physical(p);gap=(d[non[:,0]]-jnp.sum(N[non[:,0]]*X[non[:,1]],1))/jnp.asarray(scale);return jnp.r_[gap,g]
            jac=jax.jit(jax.jacfwd(pieces));converged=False
            for it in range(20):
                value=np.asarray(pieces(q));geo=value[:-3];g=value[-3:];error=float(abs(g-target).max());trace.append(dict(it=it,centroid_error=error,minimum_support_gap=float(geo.min())))
                if geo.min()>=.999e-8 and error<2e-13:converged=True;break
                J=np.asarray(jac(q))[:,:fam.K];C=J[:-3];G=J[-3:];A=np.r_[np.c_[-C,np.zeros(len(C))],np.c_[np.eye(fam.K),-np.ones(fam.K)],np.c_[-np.eye(fam.K),-np.ones(fam.K)]];b=np.r_[geo-floor,np.zeros(2*fam.K)];r=linprog(np.r_[np.zeros(fam.K),1.],A_ub=A*1000,b_ub=b*1000,A_eq=np.c_[G,np.zeros(3)]*1000,b_eq=(target-g)*1000,bounds=[(-.05,.05)]*fam.K+[(0,.05)],method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-9))
                if not r.success:raise ValueError('centroid and hull correction LP failed: '+r.message)
                q[:fam.K]+=r.x[:fam.K]
            if not converged:raise ValueError('explicit centroid/hull correction did not converge')
            s=fam.state(q)
            if np.max(abs(s['g']-target))>2e-13:raise ValueError('actual convex body centroid differs from solved target')
        except (ValueError,AssertionError,np.linalg.LinAlgError) as e:
            rows.append(dict(label=label,error=repr(e),trace=trace));(out/'screen.json').write_text(json.dumps(rows,indent=2)+'\n');continue
        row={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax','minimum_noncontact']};row.update(label=label,m=m,L=L,breaks=breaks,threshold=threshold,centroid_error=float(np.max(abs(s['g']-target))));np.save(out/(label+'_q.npy'),q);(out/(label+'.json')).write_text(json.dumps(row,indent=2)+'\n');(out/(label+'_trace.json')).write_text(json.dumps(trace,indent=2)+'\n');rows.append(row);print('MASS_BALANCED_TILTED_PROFILE_CONTRACTION',row,flush=True)
        if s['S']==s['U']==1:np.save(out/'NUMERICAL_NOMINATION_q.npy',q);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n')
        (out/'screen.json').write_text(json.dumps(rows,indent=2)+'\n')

if __name__=='__main__':run(sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4]))
