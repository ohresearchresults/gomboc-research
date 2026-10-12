"""Replace almost-flat profile turns by exact linear interpolation.
This explicitly changes the physical body and recomputes its OWN mass. The
removed knots make true coplanar facets merge and collinear vertices retire.
No old triangulation is counted, and no old equilibrium census is inherited.
"""
import sys,json,hashlib
from pathlib import Path
import numpy as np
import jax
import jax.numpy as jnp
from scipy.optimize import linprog
from concave_profile_family import ProfileFamily

def run(src,normal_src,out,L):
    src=Path(src);normal_src=Path(normal_src);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=src.read_bytes();nraw=normal_src.read_bytes();(out/'source_q.npy').write_bytes(raw);(out/'source_normals.npy').write_bytes(nraw);q=np.load(out/'source_q.npy');normals=np.load(out/'source_normals.npy');m=len(normals);h=np.r_[q[:m*L].reshape(L,m),np.zeros((1,m))];z=np.r_[q[m*L:m*L+L],1.];theta=q[-m:] if len(q)>m*L+L else np.unwrap(np.arctan2(normals[:,1],normals[:,0]));rows=[]
    (out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(raw).hexdigest(),normal_source=str(normal_src),normal_sha256=hashlib.sha256(nraw).hexdigest(),m=m,L=L,method=__doc__),indent=2)+'\n')
    for threshold in [1e-6,1e-5,1e-4,.001,.003,.01,.03]:
        breaks=[]
        for i in range(m):
            keep=list(range(L+1))
            while len(keep)>2:
                curv=[]
                for j in range(1,len(keep)-1):
                    a,b,c=keep[j-1:j+2];s1=(h[b,i]-h[a,i])/(z[b]-z[a]);s2=(h[c,i]-h[b,i])/(z[c]-z[b]);curv.append(np.arctan(s1)-np.arctan(s2))
                j=int(np.argmin(curv))
                if curv[j]>=threshold:break
                keep.pop(j+1)
            breaks.append(keep[:-1])
        label=f'turn_{threshold:g}';controls=np.r_[*[h[b,i] for i,b in enumerate(breaks)],z[:-1],theta]
        try:
            fam=ProfileFamily(m,L,breaks);non=np.argwhere(~fam.contact)
            @jax.jit
            def gaps(p):
                X,Z,Y,g,v,N,d=fam.physical(p)
                return d[non[:,0]]-jnp.sum(N[non[:,0]]*X[non[:,1]],axis=1)
            oldgap=np.asarray(gaps(controls));C=np.asarray(jax.jacfwd(gaps)(controls))[:,:fam.K];initial=fam.independent_physical(controls);floor=1e-8*np.linalg.norm(initial[5],axis=1)[non[:,0]];rhs=oldgap-floor;A=np.r_[np.c_[-C,np.zeros(len(C))],np.c_[np.eye(fam.K),-np.ones(fam.K)],np.c_[-np.eye(fam.K),-np.ones(fam.K)]];b=np.r_[rhs,np.zeros(2*fam.K)];projection=linprog(np.r_[np.zeros(fam.K),1.],A_ub=A*1000,b_ub=b*1000,bounds=[(None,None)]*fam.K+[(0,None)],method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-10))
            if not projection.success:raise ValueError('explicit merged-profile convexity projection failed: '+projection.message)
            before=controls.copy();controls[:fam.K]+=projection.x[:fam.K];discrepancy=float(np.max(abs(np.asarray(gaps(controls))-(oldgap+C@projection.x[:fam.K]))))
            if discrepancy>1e-8 or np.min(np.asarray(gaps(controls))/floor)<.99:raise ValueError('linear support projection fails actual geometry readback')
            np.save(out/(label+'_unprojected_q.npy'),before);s=fam.state(controls)
        except (ValueError,AssertionError,np.linalg.LinAlgError) as e:rows.append(dict(label=label,error=repr(e)));continue
        row={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax','minimum_noncontact']};row.update(label=label,threshold=threshold,m=m,L=L,breaks=breaks,support_projection_Linf=float(projection.x[-1]),linear_geometry_discrepancy=discrepancy);np.save(out/(label+'_q.npy'),controls);(out/(label+'.json')).write_text(json.dumps(row,indent=2)+'\n');rows.append(row);print('GENUINE_PROFILE_CONTRACTION',row,flush=True)
        if s['S']==s['U']==1:
            np.save(out/'NUMERICAL_NOMINATION_q.npy',controls);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n')
    (out/'screen.json').write_text(json.dumps(rows,indent=2)+'\n')

if __name__=='__main__':run(sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4]))
