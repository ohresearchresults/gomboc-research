"""Mass compensation by outward translation of three existing support planes.

A main added point is kept. Only facets away from every nonsimple vertex and
the reference maximum may move. Positive support offsets enlarge the same
body; all new vertices and its actual mass are explicitly recomputed. Three
offsets solve the full first-moment equation using exact-form analytic
derivatives in the current numerical hull cell. No centroid residual is an
equilibrium certificate.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,pathlib,json,itertools,time
import numpy as np
from scipy.spatial import QhullError
from balanced_flower_caps import parent_data
from stable_face_augmentation import halfspaces
from geometry import halfspace_mesh,arrows
from basin_scout import score
from make_contact_atlas import make
from contact_forest import ContactModel

def differential(Q,indices,t):
    support=np.ones(len(Q));support[indices]+=t;R=Q/support[:,None];m=halfspace_mesh(R);X=m['X'];triples=m['triples'];rhs=(triples[:,:,None]==np.asarray(indices)[None,None,:]).astype(float);DX=np.linalg.solve(Q[triples],rhs);T=m['triangles'];a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];det=np.einsum('ij,ij->i',a,np.cross(b,c));Da,Db,Dc=DX[T[:,0]],DX[T[:,1]],DX[T[:,2]];dd=np.einsum('ij,ijk->ik',np.cross(b,c),Da)+np.einsum('ij,ijk->ik',np.cross(c,a),Db)+np.einsum('ij,ijk->ik',np.cross(a,b),Dc);J=(np.einsum('ip,ic->cp',dd,a+b+c)+np.einsum('i,icp->cp',det,Da+Db+Dc))/24
    return m,m['g']*m['volume'],J,R

def choices(Q,m,oldP):
    X=m['X'];degrees=np.zeros(len(X),int);inc=np.zeros((len(Q),len(X)),bool)
    for f,cy in zip(m['active'],m['faces']):inc[f,cy]=True;degrees[cy]+=1
    root=int(np.argmax((X*X).sum(1)));W=arrows(X).max(1);eligible=[];limits=[];columns=[]
    for f,cy in zip(m['active'],m['faces']):
        if root in cy or max(degrees[cy])>3 or min(W[cy])<1e-4:continue
        dx=np.linalg.solve(Q[m['triples']],(m['triples']==f).astype(float)[...,None])[:,:,0];bound=np.inf
        for i in cy:
            step=dx[i];aa=oldP@X[i]-X[i]@X[i];bb=oldP@step-2*X[i]@step;cc=step@step
            positive=aa>1e-12
            if not positive.any() or cc<1e-30:bound=0.;break
            cap=(bb[positive]+np.sqrt(bb[positive]**2+4*cc*aa[positive]))/(2*cc);bound=min(bound,float(cap.max()))
            slope=Q@step;gap=1-Q@X[i];mask=(~inc[:,i])&(slope>1e-12)
            if mask.any():bound=min(bound,float(np.min(gap[mask]/slope[mask])))
        if not bound>1e-8 or not np.isfinite(bound):continue
        x=X[cy];area=np.linalg.norm(np.cross(x[1:-1]-x[0],x[2:]-x[0]),axis=1)/2;c=(area[:,None]*(x[0]+x[1:-1]+x[2:])/3).sum(0)/area.sum();eligible.append(int(f));limits.append(.25*bound);columns.append(area.sum()*c/np.linalg.norm(Q[f]))
    return np.array(eligible,int),np.array(limits),np.array(columns)

def save_body(out,name,Q,m,metadata):
    folder=out/name;folder.mkdir();active=m['active'];Y=Q[active];proposal=dict(scope='Numerical complete hull after literal point addition and support translations; exact audit required',V=len(m['X']),E=len(m['edges']),F=len(active),faces=m['faces'],edges=m['edges'].tolist(),active=list(range(len(active))),raw_vertices=[[str(x) for x in p] for p in m['X']],raw_halfspaces=[[str(x) for x in q]+['1'] for q in Y]);(folder/'proposal.json').write_text(json.dumps(proposal,indent=2));make(folder/'proposal.json',folder/'chart',balanced=True);c=ContactModel(folder/'chart',1,2,'local',exempt_junior=True);e=c.evaluate(c.initial,False);np.savez(folder/'realization.npz',z=c.initial,Q=e['Y'],X=e['X']);(folder/'summary-numerical.json').write_text(json.dumps(metadata,indent=2));return folder

def run(candidate,out,limit=80):
    candidate=pathlib.Path(candidate);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);r=json.loads((candidate/'construction.json').read_text());parent=pathlib.Path(r['parent_audit']).parent;p=parent_data(parent);P=p['P'];v=np.load(candidate/'body.npz')['added_points'][0];Q=halfspaces(np.r_[P,v[None]]);m=halfspace_mesh(Q);ids,bounds,cols=choices(Q,m,P);initialM=m['g']*m['volume'];trials=[];history=[];start=time.time();best=1.
    np.savez(out/'source.npz',Q=Q,X=m['X'],main_vertex=v,old_vertices=P);(out/'definition.json').write_text(json.dumps(dict(candidate=str(candidate.resolve()),parent=str(parent.resolve()),eligible_supports=ids.tolist(),limits=bounds.tolist(),source_E=len(m['edges']),source_moment=initialM.tolist(),scope='Mass-balanced positive existing-support shifts, all actual geometry reevaluated'),indent=2))
    for tr in itertools.combinations(range(len(ids)),3):
        tri=np.array(tr);B=cols[tri].T
        if abs(np.linalg.det(B))<1e-13:continue
        t=np.linalg.solve(B,-initialM)
        if ((t>0)&(t<bounds[tri])).all():trials.append((float(np.max(t/bounds[tri])),ids[tri],bounds[tri],t))
    print('SUPPORT_SHIFT_TRIPLES',len(trials),'ELIGIBLE',len(ids),flush=True)
    for trial,(_,indices,maximum,t) in enumerate(sorted(trials,key=lambda r:r[0])[:limit]):
        try:
            if trial==0:
                _,_,J0,_=differential(Q,indices,t);fd=[];dh=1e-7
                for j in range(3):
                    d=np.zeros(3);d[j]=dh;fd.append((differential(Q,indices,t+d)[1]-differential(Q,indices,t-d)[1])/(2*dh))
                error=float(np.max(abs(np.array(fd).T-J0)));(out/'mass-derivative-check.json').write_text(json.dumps(dict(max_absolute_error=error,step=dh),indent=2));assert error<1e-8
            for iteration in range(16):
                mm,M,J,R=differential(Q,indices,t)
                if np.linalg.norm(M)/mm['volume']<1e-13:break
                direction=np.linalg.solve(J,-M);accepted=False
                for bt in range(14):
                    tt=t+direction*2**-bt
                    if not ((tt>0)&(tt<maximum)).all():continue
                    mn,Mn,_,Rn=differential(Q,indices,tt)
                    if np.linalg.norm(Mn)<np.linalg.norm(M):t=tt;accepted=True;break
                if not accepted:break
            mm,M,J,R=differential(Q,indices,t);error=float(np.linalg.norm(M)/mm['volume']);referenceW=arrows(mm['X']).max(1);s=score(R);row=dict(trial=trial,shifted_supports=indices.tolist(),offsets=t.tolist(),centroid_norm=error,reference_U=int(np.sum(referenceW<0)),reference_nonroot_margin=float(np.sort(referenceW)[1]),seconds=time.time()-start,**s)
            if error<1e-11 and s['U']==1 and 17<=s['E']<249:
                val=max(s['Q'],default=0)
                if s['S']==1 or (s['S']==2 and val<best-1e-11):
                    folder=save_body(out,f'trial{trial:03d}',R,mm,row);row['folder']=str(folder.resolve());best=val;print('BALANCED_SUPPORT_BODY',json.dumps(row),flush=True)
                    if s['S']==1:
                        (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str((folder/'chart').resolve()),input=str((folder/'realization.npz').resolve())),indent=2));history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));return
            history.append(row)
        except (ValueError,AssertionError,RuntimeError,QhullError,np.linalg.LinAlgError) as error:history.append(dict(trial=trial,error=repr(error)))
        (out/'history.json').write_text(json.dumps(history,indent=2))
    print('FINITE_SUPPORT_SHIFT_BALANCE_COMPLETE',len(history),best,flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--candidate',required=True);ap.add_argument('--out',required=True);ap.add_argument('--limit',type=int,default=80);a=ap.parse_args();run(a.candidate,a.out,a.limit)
