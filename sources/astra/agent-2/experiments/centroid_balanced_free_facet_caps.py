"""Actual free-facet deletion plus a centroid-restoring physical point cap.

For each active non-apex plane, delete that plane. The resulting homogeneous
body has a new moment. Solve for an external point whose added visible-facet
pyramids restore the ORIGINAL actual volume centroid. Reconstruct the full
convex hull independently and check its mass and complete S/U census. A
restored center is never simply substituted into an unchanged mass integral.
"""
import sys,json,hashlib,time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from scipy.spatial import QhullError
from apex_polygon_supports import ApexFamily
from physical_point_cap_family import PointCapFamily
from mass_balanced_cap_retirement import cone_mass_map

def run(src,out,m=4):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=src.read_bytes();(out/'source_q.npy').write_bytes(raw);qold=np.load(out/'source_q.npy');old=ApexFamily(m,True,249).state(qold);target=old['g'];rows=[];best=None;start=time.time()
    (out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(raw).hexdigest(),m=m,target_centroid=target.tolist(),method=__doc__,source_counts={k:old[k] for k in ['V','E','F','S','U','Pmax','Qmax']}),indent=2)+'\n')
    for removed in old['A']:
        removed=int(removed)
        if removed<m:continue
        H=np.delete(old['H'],removed,axis=0);bf=ApexFamily(m,True,249);q=bf.pack(H)
        try:b=bf.state(q)
        except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError) as e:rows.append(dict(removed=removed,error=repr(e)));continue
        massfun=cone_mass_map(b);delta=target-b['g'];distance=np.linalg.norm(delta)
        if distance<1e-14:raise ValueError('active facet deletion unexpectedly changed no centroid; handle separately')
        direction=delta/distance;den=b['H'][b['A']]@direction;ray=np.min((1-b['H'][b['A']]@b['g'])[den>0]/den[den>0]);diam=np.linalg.norm(np.ptp(b['X'],axis=0));fam=PointCapFamily(m,500);seeds=[b['g']+(1+a)*ray*direction for a in [.002,.05,.5,2.]]
        for k,seed in enumerate(seeds):
            fit=least_squares(lambda p:(massfun(p)[0]-target)/distance,seed,jac=lambda p:massfun(p)[1]/distance,max_nfev=240,xtol=1e-12,ftol=1e-12,gtol=1e-12,bounds=(b['g']-diam*8,b['g']+diam*8));p=fit.x;res=float(np.max(abs(massfun(p)[0]-target)));label=f'drop{removed:03d}_seed{k}';row=dict(label=label,removed=removed,mass_error=res,solver_message=str(fit.message),solver_evaluations=int(fit.nfev))
            if res>2e-12:rows.append(row);continue
            z=np.r_[q,p]
            try:s=fam.state(z)
            except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError) as e:row['error']=repr(e);rows.append(row);continue
            actual_error=float(np.max(abs(s['g']-target)));volume_error=float(abs(s['volume']-massfun(p)[2]))
            if actual_error>2e-12 or volume_error>1e-10:raise ValueError('independent cap-cone and complete hull integrals disagree')
            row.update({j:s[j] for j in ['V','E','F','S','U','Pmax','Qmax','minimum_noncontact','visible_facets']});row.update(actual_centroid_error=actual_error,independent_volume_error=volume_error,cap_point=p.tolist());np.save(out/(label+'_z.npy'),z);np.save(out/(label+'_base_H.npy'),H);np.save(out/(label+'_cap_point.npy'),p);rows.append(row)
            key=(s['E']>249,s['U']!=1,s['S']+s['U'],s['Pmax']+s['Qmax'])
            if best is None or key<best[0]:best=(key,row);np.save(out/'best_z.npy',z);(out/'best.json').write_text(json.dumps(row,indent=2)+'\n');print('CENTROID_BALANCED_FACET_CAP',row,flush=True)
            if s['S']==s['U']==1 and s['E']<=249:
                np.save(out/'NUMERICAL_NOMINATION_z.npy',z);np.save(out/'NUMERICAL_NOMINATION_base_H.npy',H);np.save(out/'NUMERICAL_NOMINATION_cap_point.npy',p);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');(out/'screen.json').write_text(json.dumps(rows,indent=2)+'\n');return row
            break
        (out/'screen.json').write_text(json.dumps(rows,indent=2)+'\n')
    (out/'FINITE_SCREEN_END.json').write_text(json.dumps(dict(seconds=time.time()-start,rows=len(rows),goal_complete=False),indent=2)+'\n');return None if best is None else best[1]

if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 4)
