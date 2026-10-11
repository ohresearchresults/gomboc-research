"""Literal support retirement, compensated by one actual point cap.
For a fixed base B, visible facet pyramids partition conv(B,p) minus B.
For each facet, deltaV=max(c_i.p-d_i,0) and its centroid is (p+3C_i)/4.
This gives the exact-form uniform mass map and its analytic 3x3 Jacobian.
Solve for the point that restores the old capped body's centroid, then
reconstruct and audit its actual hull, mass and equilibrium census.
Only numerical110 with E<=249 goes to the complete rational A/B freeze.
"""
import sys,json,hashlib,time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from scipy.spatial import QhullError
from apex_polygon_supports import ApexFamily
from physical_point_cap_family import PointCapFamily
from support_persistence import ROOT

def cone_mass_map(s):
    X=s['X'];coeff=[];offset=[];centers=[]
    for f in s['faces']:
        P=X[f];area_vector=np.sum(np.cross(P,np.roll(P,-1,axis=0)),axis=0)/2;area=np.linalg.norm(area_vector);n=area_vector/area;a=P[0];areas=[];cent=[]
        for i in range(1,len(P)-1):areas.append(np.cross(P[i]-a,P[i+1]-a)@n/2);cent.append((a+P[i]+P[i+1])/3)
        C=np.average(cent,axis=0,weights=areas);ci=area_vector/3;coeff.append(ci);offset.append(ci@C);centers.append(C)
    C=np.array(coeff);D=np.array(offset);F=np.array(centers);V=s['volume'];M=V*s['g']
    def fun(p):
        dv=np.maximum(C@p-D,0);active=dv>0;vol=V+dv.sum();moment=M+np.sum(dv[:,None]*(p+3*F),axis=0)/4;g=moment/vol;vg=C[active].sum(0);mg=(np.einsum('ni,nj->ij',(p+3*F)[active],C[active])+dv.sum()*np.eye(3))/4;J=(mg-np.outer(g,vg))/vol;return g,J,vol
    return fun

def run(src,out,m=42):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=src.read_bytes();(out/'source_z.npy').write_bytes(raw);z=np.load(out/'source_z.npy');oldfam=PointCapFamily(m,500);old=oldfam.state(z);base=oldfam.base.state(z[:-3]);target=old['g'];pold=z[-3:];check=cone_mass_map(base)(pold)
    if np.max(abs(check[0]-target))>1e-10 or abs(check[2]-old['volume'])>1e-10:raise ValueError('independent facet-cone mass disagrees with hull tetrahedra')
    (out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(raw).hexdigest(),apex_candidates=m,target_centroid=target.tolist(),independent_mass_discrepancy=float(np.max(abs(check[0]-target))),method=__doc__),indent=2)+'\n');star=[int(base['A'][i]) for i,f in enumerate(base['faces']) if 0 in f];other=[int(i) for i in base['A'] if int(i) not in star];rows=[];best=None;start=time.time()
    for removed in star:
        order=[i for i in star if i!=removed]+other;mm=len(star)-1;H=base['H'][order].copy();H[:mm,2]=1.;bf=ApexFamily(mm,allow_top_retirement=True,edge_limit=249);q=bf.pack(H)
        try:b=bf.state(q)
        except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError) as e:rows.append(dict(removed=removed,error=repr(e)));continue
        massfun=cone_mass_map(b);scale=max(np.linalg.norm(target-b['g']),1e-9);diam=np.linalg.norm(b['X'].max(0)-b['X'].min(0));delta=target-b['g'];dn=np.linalg.norm(delta);seeds=[pold]
        if dn>0:
            direction=delta/dn;den=b['H'][b['A']]@direction;distance=np.min((1-b['H'][b['A']]@b['g'])[den>0]/den[den>0]);seeds.extend(b['g']+distance*(1+a)*direction for a in [.001,.02,.2,1.])
        fam=PointCapFamily(mm,500);bestlocal=None
        for k,seed in enumerate(seeds):
            fit=least_squares(lambda p:(massfun(p)[0]-target)/scale,seed,jac=lambda p:massfun(p)[1]/scale,max_nfev=240,xtol=1e-12,ftol=1e-12,gtol=1e-12,bounds=(b['g']-diam*6,b['g']+diam*6));point=fit.x;zz=np.r_[q,point];res=float(np.max(abs(massfun(point)[0]-target)));label=f'drop{removed:03d}_seed{k}';np.save(out/(label+'_z.npy'),zz)
            if res>1e-10:rows.append(dict(label=label,removed=removed,new_apex_candidates=mm,mass_error=res,solver_message=str(fit.message)));continue
            try:
                s=fam.state(zz);actual_error=float(np.max(abs(s['g']-target)))
                if actual_error>1e-10:raise ValueError('cap-hull mass does not match the solved cone mass')
                row={t:s[t] for t in ['V','E','F','S','U','Pmax','Qmax','minimum_noncontact']};row.update(label=label,removed=removed,new_apex_candidates=mm,mass_error=actual_error,visible_facets=s['visible_facets'],solver_evaluations=int(fit.nfev));np.save(out/(label+'_base_H.npy'),s['baseH']);np.save(out/(label+'_cap_point.npy'),point)
                key=(s['E']>249,s['S']+s['U'],max(s['Pmax'],s['Qmax']))
                if best is None or key<best[0]:best=(key,row);np.save(out/'best_z.npy',zz);(out/'best.json').write_text(json.dumps(row,indent=2)+'\n');print('MASS_BALANCED_ACTUAL_BODY',row,flush=True)
                if s['S']==s['U']==1 and s['E']<=249:
                    (out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');from freeze_triangle_cap_goal import run as freeze;verified=freeze(out/(label+'_base_H.npy'),out/(label+'_cap_point.npy'),out/'exact_nomination_g16');(out/'verification_result.json').write_text(json.dumps(verified,indent=2)+'\n');return row
                bestlocal=row
            except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError) as e:row=dict(label=label,removed=removed,new_apex_candidates=mm,mass_error=res,error=repr(e))
            rows.append(row)
            if bestlocal is not None:break
        (out/'screen.json').write_text(json.dumps(dict(rows=rows,seconds=time.time()-start,goal_complete=False),indent=2)+'\n')
    return None if best is None else best[1]

if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 42)
