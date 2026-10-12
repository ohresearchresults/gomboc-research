"""Construct a physical point cap by erasing a polar escape basin.

At the SOURCE actual centroid, retain a polar set whose positive all-pair
escape graph reaches the farthest polar vertex. Remove the complementary
basin by one plane p.y=1. Along every crossing edge, compute the union of
intervals lying inside diameter balls of retained polar vertices. A cut past
the final unsafe interval makes each new polar vertex escape into the retained
set. These are linear inequalities in the added physical point p. A separate
diameter-ball check can ensure reference U1 too. Reference claims are never
substituted for the final filled-body centroid; own mass/census are recomputed.
"""
import sys,json,hashlib,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog,minimize,LinearConstraint
from apex_polygon_supports import ApexFamily
from physical_point_cap_family import PointCapFamily
from geometry import angular_scores

def run(src,out,m=44,margin=1e-8):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=src.read_bytes();(out/'source_q.npy').write_bytes(raw);q=np.load(out/'source_q.npy');s=ApexFamily(m,True,249).state(q);X,Y=s['Z'],s['Y'];root=int(np.argmax(np.sum(Y*Y,1)));dot=Y@Y.T-np.sum(Y*Y,1)[:,None];reach=np.zeros(len(Y),bool);reach[root]=True
    for _ in range(len(Y)):
        new=reach|np.any(dot[:,reach]>0,axis=1)
        if np.array_equal(new,reach):break
        reach=new
    kept=np.flatnonzero(reach);removed=np.flatnonzero(~reach)
    meta=dict(source=str(src),sha256=hashlib.sha256(raw).hexdigest(),m=m,method=__doc__,reference_center=s['g'].tolist(),source_counts={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax']},retained_polar_ids=kept.tolist(),removed_polar_ids=removed.tolist(),margin=margin)
    (out/'source.json').write_text(json.dumps(meta,indent=2)+'\n')
    if not len(removed):raise ValueError('no unwanted reference stable basin')
    A=[*Y[kept],*-Y[removed]];b=[*[1-margin]*len(kept),*[-1-margin]*len(removed)];edge_rows=[]
    for u,v in s['es']:
        if reach[u]==reach[v]:continue
        if reach[u]:u,v=v,u
        a=Y[u];d=Y[v]-a;dd=d@d;intervals=[]
        for w in kept:
            B=d@Y[w]-2*(a@d);C=a@Y[w]-a@a;disc=B*B+4*dd*C
            if disc<=0:continue
            lo=(B-np.sqrt(disc))/(2*dd);hi=(B+np.sqrt(disc))/(2*dd)
            if hi>0 and lo<1:intervals.append((max(0.,lo),min(1.,hi),int(w)))
        intervals.sort(key=lambda r:r[1],reverse=True);start=1.;covered=False
        for lo,hi,w in intervals:
            if (not covered and hi>=1-1e-12) or (covered and hi>start):start=min(start,lo);covered=True
        if not covered or start>=1:raise ValueError('retained polar endpoint lacks positive escape interval')
        t=start+(1-start)*1e-5;point=a+t*d;score=np.max(point@Y[kept].T-point@point)
        if score<=0:raise ValueError('computed cut threshold is not strictly in a retained diameter ball')
        A.append(-point);b.append(-1-margin);edge_rows.append(dict(removed=int(u),retained=int(v),safe_from=start,threshold=t,threshold_point=point.tolist(),strict_threshold_escape=float(score)))
    A=np.asarray(A);b=np.asarray(b);np.savez(out/'cut_linear_system.npz',A=A,b=b);(out/'crossing_edge_intervals.json').write_text(json.dumps(edge_rows,indent=2)+'\n');lp=linprog(np.zeros(3),A_ub=A,b_ub=b,bounds=[(None,None)]*3,method='highs',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-10));report=dict(status=int(lp.status),message=str(lp.message),reference_only=True)
    if not lp.success:(out/'finite_cut_result.json').write_text(json.dumps(report,indent=2)+'\n');print('FINITE_POLAR_BASIN_CUT',report,flush=True);return
    if np.max(A@lp.x-b)>1e-8:raise ValueError('cut LP does not satisfy original rows')
    np.save(out/'feasible_reference_point.npy',lp.x);rows=[];best=None;fam=PointCapFamily(m,500)
    seeds=[('linear_feasible',lp.x)]
    for w in np.argsort(-np.sum(X*X,axis=1)):
        center=X[w]/2;radius=np.linalg.norm(center);r=minimize(lambda p:np.sum((p-center)**2),lp.x,jac=lambda p:2*(p-center),constraints=[LinearConstraint(A,-np.inf,b)],method='SLSQP',options=dict(maxiter=500,ftol=1e-13));violation=float(np.maximum(A@r.x-b,0).max())
        if violation>1e-8:continue
        seeds.append((f'witness_{int(w):03d}',r.x))
        if len(seeds)>1 and np.linalg.norm(r.x-center)<radius-1e-8:break
    for label,p in seeds:
        z=np.r_[q,p+s['g']]
        try:t=fam.state(z)
        except (ValueError,AssertionError,np.linalg.LinAlgError) as e:rows.append(dict(label=label,error=repr(e)));continue
        Z0=t['X']-s['g'];Y0=t['H']/(1-t['H']@s['g'])[:,None];referenceU=int((angular_scores(Z0).max(1)<0).sum());referenceS=int((angular_scores(Y0).max(1)<0).sum())
        if referenceS!=1:raise ValueError('basin-cut sufficient inequalities disagree with actual reference S')
        row={k:t[k] for k in ['V','E','F','S','U','Pmax','Qmax','minimum_noncontact']};row.update(label=label,reference_S=referenceS,reference_U=referenceU,actual_centroid=t['g'].tolist(),centroid_movement=float(np.linalg.norm(t['g']-s['g'])),reference_point=p.tolist());np.save(out/(label+'_z.npy'),z);rows.append(row);key=(t['E']>249,t['S']+t['U'],t['Pmax']+t['Qmax'])
        if best is None or key<best[0]:best=(key,row);np.save(out/'best_z.npy',z);(out/'best.json').write_text(json.dumps(row,indent=2)+'\n');print('POLAR_BASIN_PHYSICAL_CUT',row,flush=True)
        if t['S']==t['U']==1 and t['E']<=249:
            np.save(out/'NUMERICAL_NOMINATION_base_H.npy',s['H']);np.save(out/'NUMERICAL_NOMINATION_cap_point.npy',z[-3:]);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');break
    (out/'screen.json').write_text(json.dumps(rows,indent=2)+'\n');(out/'finite_cut_result.json').write_text(json.dumps(report,indent=2)+'\n')

if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 44)
