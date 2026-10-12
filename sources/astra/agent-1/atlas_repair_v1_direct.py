"""Own-mass bottleneck/L1 repair inside a complete contact-preserving chart.
The seed/plan are explicitly peer2's pinned C498 selected-hull data. Torch
reconstruction, analytic physical derivatives, conditioned L1 corrector and
fresh strict domain checks are this agent's independent numerical experiment.
Only rational free-control reconstruction plus full exact audit may accept it.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,torch,pathlib,json,time,argparse
from scipy.linalg import svd
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
from soft_forest_polish import forest
from geometry import arrows
torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

class Atlas:
    def __init__(self,folder):
        folder=pathlib.Path(folder);self.meta=json.loads((folder/'chart.json').read_text());d=np.load(folder/'data.npz');self.initial=d['q'];self.A0=d['A'];self.tri=d['tri'];self.eu=d['eu'];self.es=d['es'];self.inc=d['incidence'];self.F=self.meta['F'];self.n=self.meta['nodes'];self.groups=[]
        for g in self.meta['levels']:self.groups.append({k:torch.tensor(v,dtype=torch.int64) if k not in ['level','degree'] else v for k,v in g.items()})
        self.tris=torch.tensor(self.tri);self.free=len(self.initial)
    def reconstruct(self,z):
        A=torch.zeros((self.n,3))
        for g in self.groups:
            ids=g['nodes'];degree=g['degree'];vs=torch.zeros((len(ids),3))
            if degree<3:vs=vs.scatter(1,g['rest'],z[g['indices']])
            if degree:
                dep=A[g['deps']];mat=torch.gather(dep,2,g['axes'][:,None,:].expand(-1,degree,-1));rhs=1-(dep*vs[:,None,:]).sum(2);sol=torch.linalg.solve(mat,rhs[...,None])[:,:,0];vs=vs.scatter(1,g['axes'],sol)
            A=A.index_copy(0,ids,vs)
        return A
    def evaluate(self,z,jacobian=True):
        zz=torch.tensor(z);A=self.reconstruct(zz).detach().numpy();Y=A[:self.F];X=A[self.F:];a=X[self.tri];six=np.einsum('ij,ij->i',a[:,0],np.cross(a[:,1],a[:,2]));V=six.sum()/6;g=(six[:,None]*a.sum(1)).sum(0)/(4*six.sum());gap=1-Y@X.T
        if not np.isfinite(A).all() or V<=0 or np.min(gap[~self.inc])<=0 or np.max(abs(gap[self.inc]))>1e-7 or np.min(1-Y@g)<=0:raise ValueError('invalid full physical incidence/mass domain')
        turns=[]
        for f,cy in enumerate(self.meta['faces']):
            for k in range(1,len(cy)-1):turns.append(float(np.cross(X[cy[k]]-X[cy[0]],X[cy[k+1]]-X[cy[0]])@Y[f]))
        if min(turns)<=0:raise ValueError('invalid maximal facet orientation')
        P=X-g;Q=Y/(1-Y@g)[:,None];pa=[];sg=[];vals=[];su=[]
        for pts in [P,Q]:
            root=int(np.argmax((pts*pts).sum(1)));parents=forest(pts,[root]);sign=np.ones(len(pts));sign[root]=-1;W=arrows(pts);vals.append(sign*W[np.arange(len(pts)),parents]);pa.append(parents);sg.append(sign);su.append(int(np.sum(W.max(1)<0)))
        out=dict(X=X,Y=Y,P=P,Q=Q,g=g,volume=V,gaps=gap,mechanical=np.r_[tuple(vals)],S=su[1],U=su[0],parents=pa,signs=sg,minimum_gap=float(gap[~self.inc].min()),minimum_turn=min(turns))
        if not jacobian:return out
        DA=torch.func.jacrev(self.reconstruct)(zz).detach().numpy();DY=DA[:self.F];DX=DA[self.F:];a,b,c=X[self.tri[:,0]],X[self.tri[:,1]],X[self.tri[:,2]];Ddet=np.einsum('ti,tip->tp',np.cross(b,c),DX[self.tri[:,0]])+np.einsum('ti,tip->tp',np.cross(c,a),DX[self.tri[:,1]])+np.einsum('ti,tip->tp',np.cross(a,b),DX[self.tri[:,2]]);Dg=(np.einsum('tp,ti->ip',Ddet,a+b+c-4*g)+np.einsum('t,tip->ip',six,DX[self.tri].sum(1)))/(4*six.sum());DP=DX-Dg;den=1-Y@g;Dden=-np.einsum('icp,c->ip',DY,g)-Y@Dg;DQ=DY/den[:,None,None]-Y[:,:,None]*Dden[:,None,:]/den[:,None,None]**2;mechJ=[]
        for pts,Dpts,parents,sign in zip([P,Q],[DP,DQ],pa,sg):
            delta=pts[parents]-pts;rr=(pts*pts).sum(1);dd=(delta*delta).sum(1);ds=np.sqrt(rr*dd);value=(pts*delta).sum(1)/ds;gi=(delta-pts)/ds[:,None]-value[:,None]*(pts/rr[:,None]-delta/dd[:,None]);gj=pts/ds[:,None]-value[:,None]*delta/dd[:,None];mechJ.append(sign[:,None]*(np.einsum('ic,icp->ip',gi,Dpts)+np.einsum('ic,icp->ip',gj,Dpts[parents])))
        fi,vi=np.where((~self.inc)&(gap<.05));gapJ=-np.einsum('ic,icp->ip',Y[fi],DX[vi])-np.einsum('ic,icp->ip',X[vi],DY[fi]);out.update(DA=DA,J=np.vstack(mechJ),gapJ=gapJ,gapv=gap[fi,vi]);return out

def run(source,out,steps=300,eps=1e-8):
    chart=Atlas(source);z=chart.initial.copy();out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);history=[];trust=.02;start=time.time()
    reconstruction=chart.reconstruct(torch.tensor(z)).detach().numpy();error=float(np.max(abs(reconstruction-chart.A0)));(out/'source.json').write_text(json.dumps(dict(source=str(pathlib.Path(source).resolve()),initial_reconstruction_error=error,epsilon=eps,chart_vertices=chart.meta['V'],chart_edges=chart.meta['E'],chart_facets=chart.F),indent=2));assert error<1e-10
    for it in range(steps):
        e=chart.evaluate(z);v=e['mechanical'];merit=float(np.maximum(eps-v,0).sum());row=dict(it=it,S=e['S'],U=e['U'],merit=merit,minimum=float(min(v)),noncontact=e['minimum_gap'],minimum_turn=e['minimum_turn'],trust=trust,seconds=time.time()-start);history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));np.savez(out/'latest.npz',z=z,X=e['X'],Q=e['Y']);print('CONTACT_L1',json.dumps(row),flush=True)
        if e['S']==e['U']==1 and min(v)>eps*.8:
            np.savez(out/'NOMINATION_OWN110.npz',z=z,X=e['X'],Q=e['Y']);print('POTENTIAL_CONTACT_BODY_REQUIRES_RATIONAL_PLAN_AUDIT',flush=True);return
        scale=np.r_[np.full(chart.F*3,np.sqrt(np.mean(e['Y']**2))),np.full(len(e['X'])*3,np.sqrt(np.mean(e['P']**2)))];metric=e['DA'].reshape(-1,len(z))/scale[:,None];_,ss,Vt=svd(metric,full_matrices=False,check_finite=False)
        if min(ss)<1e-14:raise ValueError('singular selected contact chart')
        W=Vt.T/ss;d=len(z);n=len(v);I=eye(d);O=csr_matrix((d,n));A=vstack([hstack([-csr_matrix(e['J']@W),-eye(n),csr_matrix((n,d))]),hstack([I,O,-I]),hstack([-I,O,-I]),hstack([-csr_matrix(e['gapJ']@W),csr_matrix((len(e['gapv']),n+d))])],format='csr');b=np.r_[v-eps,np.zeros(2*d),e['gapv']*.8];bound=trust/np.sqrt(d);lp=linprog(np.r_[np.zeros(d),np.ones(n),np.full(d,1e-7)],A_ub=A,b_ub=b,bounds=[(-bound,bound)]*d+[(0,None)]*(n+d),method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        if not lp.success:trust*=.5;print('CONTACT_LP_UNRESOLVED',lp.message,flush=True);continue
        dz=W@lp.x[:d];accepted=False
        for level in range(15):
            candidate=z+dz*2**-level
            try:ee=chart.evaluate(candidate,False);newmerit=float(np.maximum(eps-ee['mechanical'],0).sum())
            except Exception:continue
            if newmerit<merit*(1-1e-5):z=candidate;accepted=True;break
        if accepted and level==0:trust=min(.15,trust*1.2)
        if not accepted:trust*=.4
        if trust<1e-9:print('CONTACT_L1_LOCAL_STALL',flush=True);break

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--source',required=True);ap.add_argument('--out',required=True);ap.add_argument('--steps',type=int,default=300);ap.add_argument('--epsilon',type=float,default=1e-8);a=ap.parse_args();run(a.source,a.out,a.steps,a.epsilon)
