"""Actual uniform-mass mechanics in a fixed exact combinatorial contact chart.

Numerical search only. A nomination must be reconstructed and audited rationally
with freeze_atlas.py. Forest roots use genuine primal/polar persistence; centres
are always integrated from this same physical boundary.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import argparse,json,pathlib,time
import numpy as np
import torch
from scipy.linalg import svd
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
from atlas_repair import Atlas
from geometry import arrows
from soft_forest_polish import forest
from bottleneck_capacity import capacities
from persistence_search import pairs

torch.set_num_threads(1)
torch.set_default_dtype(torch.float64)


class ContactModel(Atlas):
    def __init__(self,source,nU=1,nS=1,merit='direct',exempt_junior=False,excluded_roots=None,escape_floor=2e-9,route_data=None):
        super().__init__(source)
        self.root_counts=(nU,nS)
        self.merit=merit
        self.exempt_junior=exempt_junior
        self.escape_floor=escape_floor
        self.route_data=route_data
        if merit=='fixed-route':
            if route_data is None:raise ValueError('Fixed-route correction needs the full explicit route data')
            for side,n in enumerate([self.meta['V'],self.F]):
                if len(route_data['parents'][side])!=n or len(route_data['roots'][side])!=self.root_counts[side]:raise ValueError('Fixed-route dimensions do not match the physical body')
        self.excluded_roots=((),()) if excluded_roots is None else tuple(tuple(map(int,x)) for x in excluded_roots)
        if len(self.excluded_roots)!=2:raise ValueError('Explicit root exclusions need primal and polar entries')

    def encode(self,A):
        z=np.empty(self.free)
        for p in self.meta['plan']:
            z[p['free_indices']]=A[p['node'],p['free_axes']]
        return z

    def evaluate(self,z,jacobian=True):
        zz=torch.tensor(z)
        A=self.reconstruct(zz).detach().numpy()
        Y=A[:self.F];X=A[self.F:]
        a=X[self.tri]
        six=np.einsum('ij,ij->i',a[:,0],np.cross(a[:,1],a[:,2]))
        volume=six.sum()/6
        g=(six[:,None]*a.sum(1)).sum(0)/(4*six.sum())
        gap=1-Y@X.T
        if not np.isfinite(A).all() or volume<=0 or gap[~self.inc].min()<=0 or abs(gap[self.inc]).max()>1e-7 or (1-Y@g).min()<=0:
            raise ValueError('invalid complete physical contact domain')
        turns=[]
        for f,cy in enumerate(self.meta['faces']):
            for k in range(1,len(cy)-1):
                turns.append(float(np.cross(X[cy[k]]-X[cy[0]],X[cy[k+1]]-X[cy[0]])@Y[f]))
        if min(turns)<=0:
            raise ValueError('invalid maximal facet orientation')
        P=X-g;Q=Y/(1-Y@g)[:,None]
        roots=[];selected=[];values=[];su=[];barsets=[];mechanical_weights=[]
        for side,(pts,edges,n) in enumerate(zip((P,Q),(self.eu,self.es),self.root_counts)):
            rs=list(map(int,self.route_data['roots'][side])) if self.merit=='fixed-route' else [int(np.argmax((pts*pts).sum(1)))]
            if rs[0] in self.excluded_roots[side]:raise ValueError('The fixed excluded target became the global radial maximum')
            pp,h=pairs(pts,edges)
            bars=1-h[pp[:,1]]/(pts[pp[:,0]]**2).sum(1)
            if n>1 and self.merit!='fixed-route':
                eligible=[int(pp[i,0]) for i in np.argsort(-bars) if int(pp[i,0]) not in self.excluded_roots[side]]
                rs.extend(eligible[:n-1])
            W=arrows(pts)
            weights=np.ones(len(pts))
            if self.merit=='fixed-route':
                jj=np.array(self.route_data['parents'][side],int);ii=np.arange(len(pts));sg=np.ones(len(pts));sg[rs]=-1;val=sg*W[ii,jj]
            elif self.merit=='shortest':
                from shortest_escape_forest import shortest_forest
                jj,weights,sg,_=shortest_forest(pts,rs,self.escape_floor);ii=np.arange(len(pts));raw=sg*W[ii,jj]
                val=weights*(raw-self.escape_floor)+self.escape_floor
            elif self.merit=='capacity':
                val,ii,jj,sg=capacities(pts,rs)
            else:
                jj=W.argmax(1) if self.merit=='local' else forest(pts,rs)
                ii=np.arange(len(pts));sg=np.ones(len(pts));sg[rs]=-1
                val=sg*W[ii,jj]
            keep=np.ones(len(pts),bool)
            if self.exempt_junior:keep[rs[1:]]=False
            roots.append(rs);selected.append((ii[keep],jj[keep],sg[keep]));values.append(val[keep])
            mechanical_weights.append(weights[keep])
            su.append(int(np.sum(W.max(1)<0)))
            barsets.append([dict(birth=int(i),edge=int(k),relative=float(v)) for (i,k),v in zip(pp,bars)])
        out=dict(A=A,X=X,Y=Y,P=P,Q=Q,g=g,volume=float(volume),gaps=gap,
                 mechanical=np.concatenate(values),S=su[1],U=su[0],roots=roots,
                 bars=barsets,minimum_gap=float(gap[~self.inc].min()),minimum_turn=min(turns))
        if not jacobian:
            return out
        DA=torch.func.jacrev(self.reconstruct)(zz).detach().numpy()
        DY=DA[:self.F];DX=DA[self.F:]
        a,b,c=X[self.tri[:,0]],X[self.tri[:,1]],X[self.tri[:,2]]
        Ddet=np.einsum('ti,tip->tp',np.cross(b,c),DX[self.tri[:,0]])+np.einsum('ti,tip->tp',np.cross(c,a),DX[self.tri[:,1]])+np.einsum('ti,tip->tp',np.cross(a,b),DX[self.tri[:,2]])
        Dg=(np.einsum('tp,ti->ip',Ddet,a+b+c-4*g)+np.einsum('t,tip->ip',six,DX[self.tri].sum(1)))/(4*six.sum())
        DP=DX-Dg
        den=1-Y@g;Dden=-np.einsum('icp,c->ip',DY,g)-Y@Dg
        DQ=DY/den[:,None,None]-Y[:,:,None]*Dden[:,None,:]/den[:,None,None]**2
        mechJ=[]
        for pts,Dpts,(ii,jj,sg),weights in zip((P,Q),(DP,DQ),selected,mechanical_weights):
            src=pts[ii];delta=pts[jj]-src;rr=(src*src).sum(1);dd=(delta*delta).sum(1);ds=np.sqrt(rr*dd)
            val=(src*delta).sum(1)/ds
            gi=(delta-src)/ds[:,None]-val[:,None]*(src/rr[:,None]-delta/dd[:,None])
            gj=src/ds[:,None]-val[:,None]*delta/dd[:,None]
            mechJ.append((weights*sg)[:,None]*(np.einsum('ic,icp->ip',gi,Dpts[ii])+np.einsum('ic,icp->ip',gj,Dpts[jj])))
        fi,vi=np.where((~self.inc)&(gap<.05))
        gapJ=-np.einsum('ic,icp->ip',Y[fi],DX[vi])-np.einsum('ic,icp->ip',X[vi],DY[fi])
        out.update(DA=DA,DX=DX,DY=DY,DP=DP,DQ=DQ,Dg=Dg,DV=Ddet.sum(0)/6,J=np.vstack(mechJ),gapJ=gapJ,gapv=gap[fi,vi])
        return out

    def metric(self,e):
        scale=np.r_[np.full(self.F*3,np.sqrt(np.mean(e['Y']**2))),np.full(len(e['X'])*3,np.sqrt(np.mean(e['P']**2)))]
        metric=e['DA'].reshape(-1,self.free)/scale[:,None]
        _,ss,Vt=svd(metric,full_matrices=False,check_finite=False)
        if ss.min()<1e-14:
            raise ValueError('singular contact chart')
        return Vt.T/ss


def correct(model,z,out,steps=200,eps=1e-8,trust=.02,verbose=True,polish_margin=False,physical_retraction=False,edge_limit=None,edge_minimum=None,hard_side=None,acceptance='relative',geometry_event_tolerance=None):
    if model.merit=='shortest' and eps!=model.escape_floor:raise ValueError('Shortest path hinge floor must equal the corrector margin')
    if edge_limit is not None and edge_minimum is not None:raise ValueError('Select one explicit edge-length bound per correction')
    if hard_side not in (None,'P','Q'):raise ValueError('Unknown explicit hard mechanical side')
    if acceptance not in ('relative','armijo'):raise ValueError('Unknown explicit step acceptance rule')
    if hard_side is not None and model.root_counts[0 if hard_side=='P' else 1]!=1:
        raise ValueError('Hard single-root protection requires exactly one allowed root on that side')
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True)
    start=time.time();history=[];z=z.copy();d=model.free
    def values(e,derivative=False):
        v=e['mechanical'];J=e['J'] if derivative else None
        edge_bound=edge_limit if edge_limit is not None else edge_minimum
        if edge_bound is not None:
            u,w,limit=edge_bound;direction=-1 if edge_limit is not None else 1;delta=e['X'][w]-e['X'][u];length=np.linalg.norm(delta);radius=np.sqrt(np.mean(np.sum(e['P']**2,axis=1)))
            v=np.r_[v,direction*(length/radius-limit)+eps]
            if derivative:
                dr=np.einsum('ic,icp->p',e['P'],e['DP'])/(len(e['P'])*radius)
                dl=(delta/length)@(e['DX'][w]-e['DX'][u])/radius-length*dr/radius**2
                J=np.vstack([J,direction*dl])
        return v,J
    for it in range(steps):
        e=model.evaluate(z);v,Jac=values(e,True);merit=float(np.maximum(eps-v,0).sum())
        nprimal=len(e['P'])-(len(e['roots'][0])-1 if model.exempt_junior else 0)
        hard=np.zeros(len(v),bool)
        if hard_side=='P':hard[:nprimal]=True
        elif hard_side=='Q':hard[nprimal:nprimal+len(e['Q'])]=True
        row=dict(it=it,S=e['S'],U=e['U'],merit=merit,minimum=float(v.min()),noncontact=e['minimum_gap'],turn=e['minimum_turn'],trust=trust,seconds=time.time()-start,
                 Pmax=max([b['relative'] for b in e['bars'][0]],default=0),Qmax=max([b['relative'] for b in e['bars'][1]],default=0))
        history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2))
        np.savez(out/'latest.npz',z=z,X=e['X'],Q=e['Y'])
        if verbose:print('CONTACT_CORRECTION',json.dumps(row),flush=True)
        if e['S']==e['U']==1:
            np.savez(out/'POTENTIAL_OWN110.npz',z=z,X=e['X'],Q=e['Y'])
            print('POTENTIAL_ACTUAL_CENTROID_OWN110_REQUIRES_EXACT',flush=True)
            # Preserve every numerical own110 immediately. A requested guard
            # margin is a separate claim and must not suppress this candidate.
            return z,e,bool(not polish_margin or v.min()>.8*eps)
        if geometry_event_tolerance is not None:
            events=[]
            for side,(pts,edges) in enumerate([(e['P'],model.eu),(e['Q'],model.es)]):
                lengths=np.linalg.norm(pts[edges[:,0]]-pts[edges[:,1]],axis=1)/np.sqrt(np.mean(pts*pts));j=int(lengths.argmin());events.append(dict(side=side,edge=edges[j].tolist(),relative_length=float(lengths[j])))
            event=min(events,key=lambda r:r['relative_length'])
            if event['relative_length']<geometry_event_tolerance:
                (out/'EDGE_EVENT.json').write_text(json.dumps(dict(**event,threshold=geometry_event_tolerance,scope='A numerical near-contact proposes a new physical topology; no exact edge-count claim'),indent=2));return z,e,False
        if v.min()>.8*eps and e['U']<=model.root_counts[0] and e['S']<=model.root_counts[1]:
            np.savez(out/'NOMINATION.npz',z=z,X=e['X'],Q=e['Y'])
            return z,e,True
        W=model.metric(e);n=len(v);I=eye(d);O=csr_matrix((d,n));bound=trust/np.sqrt(d)
        gapA=e['gapJ']@W;gapb=e['gapv']*.8
        gapkeep=gapb<=bound*np.abs(gapA).sum(1)+1e-10
        mechA=Jac@W;mscale=np.maximum(bound*np.abs(mechA).sum(1),1e-12)
        gapA=gapA[gapkeep];gapb=gapb[gapkeep];gscale=np.maximum(bound*np.abs(gapA).sum(1),1e-12)
        from scipy.sparse import diags
        mat=vstack([hstack([-csr_matrix(mechA/mscale[:,None]),-diags(1/mscale),csr_matrix((n,d))]),hstack([I,O,-I]),hstack([-I,O,-I]),hstack([-csr_matrix(gapA/gscale[:,None]),csr_matrix((len(gapb),n+d))])],format='csr')
        rhs=np.r_[(v-eps)/mscale,np.zeros(2*d),gapb/gscale]
        slack_bounds=[(0,0) if is_hard else (0,None) for is_hard in hard]
        lp=linprog(np.r_[np.zeros(d),np.ones(n),np.full(d,1e-7)],A_ub=mat,b_ub=rhs,bounds=[(-bound,bound)]*d+slack_bounds+[(0,None)]*d,method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        if not lp.success:
            trust*=.5
            if trust<1e-9:break
            continue
        dz=W@lp.x[:d];accepted=False
        for level in range(16):
            candidate=z+dz*2**-level
            try:
                if physical_retraction:
                    from contact_retraction import retract
                    candidate,ee,_=retract(model,e,dz,2**-level)
                else:ee=model.evaluate(candidate,False)
            except (ValueError,np.linalg.LinAlgError,RuntimeError):continue
            candidate_values,_=values(ee)
            if ee['S']==ee['U']==1:
                np.savez(out/'POTENTIAL_OWN110.npz',z=candidate,X=ee['X'],Q=ee['Y'])
                print('POTENTIAL_ACTUAL_CENTROID_OWN110_PROPOSAL_REQUIRES_EXACT',flush=True)
                return candidate,ee,bool(not polish_margin or candidate_values.min()>.8*eps)
            if hard_side is not None:
                cp=len(ee['P'])-(len(ee['roots'][0])-1 if model.exempt_junior else 0)
                hard_values=candidate_values[:cp] if hard_side=='P' else candidate_values[cp:cp+len(ee['Q'])]
                if np.min(hard_values)<.8*eps:continue
            newmerit=float(np.maximum(eps-candidate_values,0).sum())
            predicted=merit-float(np.maximum(eps-(v+Jac@dz*2**-level),0).sum())
            required=merit*1e-5 if acceptance=='relative' else max(1e-14,1e-4*max(predicted,0))
            if newmerit<merit-required:
                row.update(acceptance=acceptance,predicted_progress=predicted,actual_progress=merit-newmerit,alpha=2**-level)
                z=candidate;accepted=True;break
        if accepted and level==0:trust=min(.12,trust*1.2)
        if not accepted:trust*=.4
        if trust<1e-9:break
    return z,model.evaluate(z,False),False


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--source',required=True);ap.add_argument('--out',required=True);ap.add_argument('--input');ap.add_argument('--nU',type=int,default=1);ap.add_argument('--nS',type=int,default=1);ap.add_argument('--steps',type=int,default=200);ap.add_argument('--epsilon',type=float,default=1e-8);ap.add_argument('--merit',choices=['direct','capacity','local','shortest'],default='direct');ap.add_argument('--polish-margin',action='store_true');a=ap.parse_args()
    model=ContactModel(a.source,a.nU,a.nS,a.merit,escape_floor=a.epsilon)
    z=np.load(a.input)['z'] if a.input else model.initial
    correct(model,z,a.out,a.steps,a.epsilon,polish_margin=a.polish_margin)
