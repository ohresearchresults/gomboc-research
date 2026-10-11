"""Direct physical face-foot search with a hard own-centroid U=1 guard.

The four basal inputs have one literal height. All other coordinates are
Cartesian free controls; the actual uniform centroid is recomputed and is
never constrained to an auxiliary origin. Thus no centroid restoration chart
can remove otherwise admissible directions. Exact hull auditing is the only
acceptance test. At most85 inputs imply E<=248 when the base is quadrilateral;
if one base input is interior, at most84 are genuine vertices and E<=246.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
from vertex_geometry import geometry
from support_geometry import escape
from direct_face_polish import face_scores,cross_derivative
from goal_nomination import preserve

class Cartesian:
    def __init__(self,X):
        assert len(X)<=85 and np.ptp(X[:4,2])==0
        self.n=len(X);self.d=3*self.n-3;self.B=np.zeros((self.n,3,self.d));k=0
        for i in range(self.n):
            for j in range(3):
                if j==2 and i in (1,2,3):continue
                self.B[i,j,k]=1
                if i==0 and j==2:self.B[:4,2,k]=1
                k+=1
        self.X0=X.copy();self.q=np.zeros(self.d)
    def construct(self,q):return self.X0+np.einsum('icp,p->ic',self.B,q)

def evaluate(F,q,derivative=True,mode='best',mass_gradient=None):
    X=F.construct(q);g=geometry(X,derivative)
    if mass_gradient is not None:
        assert derivative
        # Search model only: use a sampled neighboring-cell mass Jacobian.
        # Geometry, volume, centroid values and every accepted body stay exact
        # evaluations of the literal current/proposed convex hull.
        g['Dg']=mass_gradient;g['DZ']=g['DX']-mass_gradient
    fs,JF,allf=face_scores(g,derivative);mask=~np.all(g['T']<4,axis=1)
    # The physical root is selected from the actual own-centroid radii.
    active=g['vertices'];A=g['Z'][active];root=int(np.argmax(np.sum(A*A,axis=1)));um=np.arange(len(A))!=root
    if derivative:
        uv,up,JU=escape(A,g['DZ'][active],angular=True)
        B=F.B.reshape(X.size,F.d);JF=JF@B;JU=JU@B
    else:uv,up=escape(A,angular=True);JU=None
    if mode=='tree' and derivative:
        # Choose an explicit dual route toward either triangle of the same
        # literal base. Costs nominate directions; no facet is merged.
        T=g['T'];owners={}
        for f,tri in enumerate(T):
            for k in range(3):owners.setdefault(tuple(sorted((int(tri[k]),int(tri[(k+1)%3])))),[]).append((f,k))
        adjacency=np.full((len(T),3),-1,int)
        for pair in owners.values():
            assert len(pair)==2
            (f,k),(h,l)=pair;adjacency[f,k]=h;adjacency[h,l]=f
        dist=np.where(mask,np.inf,0.);used=np.zeros(len(T),bool);choice=np.argmax(allf,axis=1)
        for _ in range(len(T)):
            h=int(np.argmin(np.where(used,np.inf,dist)));used[h]=True
            for f in adjacency[h]:
                k=int(np.flatnonzero(adjacency[f]==h)[0]);cand=dist[h]+max(1e-8-allf[f,k],0)+1e-12
                if not used[f] and cand<dist[f]:dist[f]=cand;choice[f]=k
        # Recompute only the chosen edge's full physical derivative.
        a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];e=b-a;f=c-a;n0=np.cross(e,f);nn=np.linalg.norm(n0,axis=1);n=n0/nn[:,None];DX=g['DX'];de=DX[T[:,1]]-DX[T[:,0]];df=DX[T[:,2]]-DX[T[:,0]];Dn0=cross_derivative(e,de,f,df);Dn=(Dn0-n[:,:,None]*np.einsum('ic,icp->ip',n,Dn0)[:,None,:])/nn[:,None,None]
        R=np.sqrt(np.mean(np.sum(g['Z'][active]**2,axis=1)));DR=np.mean(np.einsum('ic,icp->ip',g['Z'][active],g['DZ'][active]),axis=0)/R
        ia=T[np.arange(len(T)),choice];ib=T[np.arange(len(T)),(choice+1)%3];ee=X[ib]-X[ia];ll=np.linalg.norm(ee,axis=1);t=np.cross(n,ee)/ll[:,None];selected=np.einsum('ic,ic->i',t,g['Z'][ia])/R;Dee=DX[ib]-DX[ia];Dt=cross_derivative(n,Dn,ee,Dee)/ll[:,None,None]-t[:,:,None]*np.einsum('ic,icp->ip',ee,Dee)[:,None,:]/ll[:,None,None]**2;JJ=(np.einsum('icp,ic->ip',Dt,g['Z'][ia])+np.einsum('ic,icp->ip',t,g['DZ'][ia]))/R-selected[:,None]*DR/R;JF=JJ@B
    else:selected=fs
    heights=X[4:,2]-X[0,2]
    # Four cyclic base edges must contain the actual centroid projection.
    base=[];JB=[]
    for i in range(4):
        j=(i+1)%4;e=X[j,:2]-X[i,:2];w=g['g'][:2]-X[i,:2];s=e[0]*w[1]-e[1]*w[0];base.append(s)
        if derivative:
            De=F.B[j,:2]-F.B[i,:2];Dw=g['Dg'][:2]@B-F.B[i,:2];JB.append(De[0]*w[1]+e[0]*Dw[1]-De[1]*w[0]-e[1]*Dw[0])
    base=np.array(base);nextbase=np.roll(X[:4,:2],-1,axis=0);orientation=np.sign(np.sum(X[:4,0]*nextbase[:,1]-X[:4,1]*nextbase[:,0]))
    base*=orientation
    hard=np.r_[uv[um],heights-1e-8,base]
    HJ=np.vstack((JU[um],F.B[4:,2]-F.B[0,2],orientation*np.array(JB)))if derivative else None
    cl=dict(S=1+int(sum(fs[mask]<0)),U=int(sum(uv<0)),V=len(active),base_valid=bool(sum(~mask)in(1,2)and min(heights)>0 and min(base)>0),minU=float(min(uv[um])),face_deficit=float(np.maximum(1e-9-fs[mask],0).sum()),worst_face=float(min(fs[mask])),centroid=g['g'].tolist())
    return g,fs[mask],selected[mask],JF[mask]if derivative else None,hard,HJ,cl

def run(source,out,steps,mode='best',norm='sum',bundles=0):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(source);cy=np.argsort(np.arctan2(X[:4,1],X[:4,0]));X[:4]=X[cy];F=Cartesian(X);q=F.q.copy();g,fs,sel,J,h,HJ,cl=evaluate(F,q,True,mode);assert cl['U']==1 and cl['base_valid']
    floors=np.r_[np.full(len(g['vertices'])-1,min(1e-10,cl['minU']*.05)),np.zeros(len(h)-(len(g['vertices'])-1))]
    np.save(out/'source.npy',X);(out/'method.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),mode=mode,norm=norm,mass_gradient_bundles=bundles,physical_definition='literal Cartesian points with four equal basal heights, uniform solid hull at computed volume centroid',maximum_inputs=85,maximum_E=248),indent=2))
    # Validate a single differentiable hull cell. The source is often within
    # 1e-10 of a real contact event: crossing it is not a derivative test.
    rng=np.random.default_rng(190201);d=rng.normal(size=F.d);d/=np.linalg.norm(d);qc=q+rng.normal(0,1e-3,F.d);gc=evaluate(F,qc,True)[0];eps=1e-7;gp=evaluate(F,qc+eps*d,False)[0];gm=evaluate(F,qc-eps*d,False)[0]
    cell=lambda a:set(tuple(sorted(map(int,t)))for t in a['T'])
    assert cell(gc)==cell(gp)==cell(gm),'derivative nomination crossed a hull cell'
    err=float(max(abs((gp['g']-gm['g'])/(2*eps)-gc['Dg']@F.B.reshape(X.size,F.d)@d)));assert err<1e-7;(out/'gradient_check.json').write_text(json.dumps(dict(actual_centroid_derivative_error=err,scope='generic unchanged hull cell; source contact-event directional data separately preserved')))
    trust=.001;trace=[];start=time.time();scale=1e-2
    for it in range(steps):
        g,fs,sel,J,h,HJ,cl=evaluate(F,q,True,mode);assert cl['U']==1 and cl['base_valid'];m=len(fs);d=F.d
        # The active hull can change; define its fresh positive-escape floor.
        nu=len(g['vertices'])-1;target=np.r_[np.full(nu,min(1e-10,cl['minU']*.05)),np.zeros(len(h)-nu)]
        res=np.maximum(1e-9-fs,0);merit=float(res.sum()if norm=='sum'else max(res,default=0));row=dict(it=it,merit=merit,trust=trust,seconds=time.time()-start,**cl);trace.append(row);np.save(out/'latest.npy',g['X']);(out/'latest.json').write_text(json.dumps(row,indent=2));(out/'trace.json').write_text(json.dumps(trace,indent=2))
        if it%10==0:print('CARTESIAN_SHADOW_FACE',out,row,flush=True)
        if cl['S']==1:preserve(g['X'],out/f'exact_goal_{it:05d}','Cartesian physical actual-centroid hardU1 and all nonbase facet feet excluded')
        I=eye(d);ns=m if norm=='sum'else 1;S=eye(m)if norm=='sum'else np.ones((m,1));O=csr_matrix((d,ns));blocks=[];rhs=[];models=[(J,HJ)]
        for sample in range(bundles):
            delta=rng.normal(0,max(trust*.03,1e-9),d)
            try:
                sampled=geometry(F.construct(q+delta),True);_,_,_,js,_,hs,_=evaluate(F,q,True,mode,sampled['Dg']);models.append((js,hs))
            except(ValueError,np.linalg.LinAlgError):continue
        for js,hs in models:
            blocks.extend((hstack((-csr_matrix(js/scale),-S,csr_matrix((m,d)))),hstack((-csr_matrix(hs/scale),csr_matrix((len(h),ns+d))))));rhs.extend(((sel-1e-9)/scale,(h-target)/scale))
        blocks.extend((hstack((I,O,-I)),hstack((-I,O,-I))));rhs.append(np.zeros(2*d));A=vstack(blocks,format='csr');b=np.concatenate(rhs);row['mass_models']=len(models);lp=linprog(np.r_[np.zeros(d),np.ones(ns),np.full(d,1e-6)],A_ub=A,b_ub=b,bounds=[(-trust,trust)]*d+[(0,None)]*(ns+d),method='highs',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-10,time_limit=15.));ok=False
        if lp.success:
            for k in range(20):
                qq=q+2.**-k*lp.x[:d]
                try:gg,vv,_,_,hh,_,cc=evaluate(F,qq,False)
                except(ValueError,np.linalg.LinAlgError):continue
                if cc['U']!=1 or not cc['base_valid']:continue
                if cc['S']==1:preserve(gg['X'],out/f'exact_goal_{it:05d}_line{k}','Cartesian own110 trial before further optimization')
                rr=np.maximum(1e-9-vv,0);mm=float(rr.sum()if norm=='sum'else max(rr,default=0))
                if mm<merit-max(1e-14,merit*1e-8):q=qq;ok=True;row['alpha']=2.**-k;break
        else:row['lp_error']=lp.message
        if ok:
            if k==0:trust=min(.03,trust*1.4)
            elif k>5:trust*=.7
        else:trust*=.4
        if trust<1e-11:break
    np.save(out/'endpoint.npy',F.construct(q));print('CARTESIAN_SHADOW_FACE_FINITE_STOP',out,trace[-1],flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--steps',type=int,default=1000);p.add_argument('--mode',choices=['best','tree'],default='best');p.add_argument('--norm',choices=['sum','max'],default='sum');p.add_argument('--bundles',type=int,default=0);a=p.parse_args();run(a.source,a.out,a.steps,a.mode,a.norm,a.bundles)
