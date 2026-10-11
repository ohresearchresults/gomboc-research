"""Positive-stress chart fitted to an actual filled-centroid C650 realization.
The polar origin is a positive barycentric combination, so it stays interior.
"""
from pathlib import Path
from fractions import Fraction as F
import json,itertools,collections,time,sys
import numpy as np
from scipy.optimize import linprog
from fit_restoration import embedded_faces
from numeric import topology,mechanics


def reference(R,allowed):
    A0=json.loads((R/'parent650/C650/A.json').read_text());raw=json.loads((R/'parent650/C650/RAW.json').read_text())
    q=np.array([[t/h[3] for t in h[:3]] for h in raw['H']]);P=np.array([[float(F(t)) for t in p] for p in A0['raw_vertices']]);owners,ef=topology(A0['faces'])
    G=sorted(tuple(sorted(v)) for v in ef.values());rotation={int(k):v for k,v in json.loads((R/'C650_rotation.json').read_text()).items()}
    af,_,_=embedded_faces(allowed,rotation);poss={tuple(sorted(cy)) for cy in af if len(cy)==3};choices=[]
    for f,cy in enumerate(owners):
        if tuple(sorted(cy)) not in poss:continue
        B=q[cy].mean(0);u=P[f]/np.linalg.norm(P[f]);slack=1-P@B;den=P@u;ii=[j for j in range(len(P)) if j!=f and den[j]>1e-10]
        limit=min(slack[ii]/den[ii]);z=(q-B)@(-u);score=limit/(z.max()+limit)
        if limit>0:choices.append((score,limit,f,cy))
    score,limit,outer,cy=max(choices);d=limit*.5;B=q[cy].mean(0);ez=-P[outer]/np.linalg.norm(P[outer]);e1=q[cy[1]]-q[cy[0]];e1/=np.linalg.norm(e1);e2=np.cross(ez,e1);O=np.array([e1,e2,ez]);r=(q-B)@O.T
    cap=np.column_stack([d*r[:,:2]/(r[:,2,None]+d),r[:,2]/(r[:,2]+d)])
    s0=d-ez@B;C=np.array([d*e1,d*e2,ez]);a=np.array([-d*e1@B,-d*e2@B,-ez@B]);o0=a/s0;linear=(C-o0[:,None]*ez[None,:])/s0;beta=ez/s0
    # A strictly positive barycentric representation of the original polar origin.
    AA=np.column_stack([-np.eye(len(q)),np.ones(len(q))]);eq=np.zeros((4,len(q)+1));eq[:3,:len(q)]=q.T;eq[3,:len(q)]=1
    lp=linprog(np.r_[np.zeros(len(q)),-1.],A_ub=AA,b_ub=np.zeros(len(q)),A_eq=eq,b_eq=[0,0,0,1],bounds=[(0,None)]*(len(q)+1),method='highs')
    assert lp.success and lp.x[-1]>0;gamma=lp.x[:-1];lam=gamma*(r[:,2]+d)/s0;lam/=lam.sum();assert np.linalg.norm(lam@cap-o0)<1e-12
    gf,grot,df=embedded_faces(G,rotation);planes=[]
    for fac in gf:
        triples=np.array(list(itertools.combinations(fac,3)));xy1=np.column_stack([cap[:,:2],np.ones(len(q))]);tr=triples[np.argmax(abs(np.linalg.det(xy1[triples])))];planes.append(np.linalg.solve(xy1[tr],cap[tr,2]))
    planes=np.array(planes);omega={}
    for u,v in G:
        f,g=df[u,v],df[v,u];delta=cap[v,:2]-cap[u,:2];rd=np.array([-delta[1],delta[0]]);omega[u,v]=float((planes[g,:2]-planes[f,:2])@rd/(delta@delta))
    boundary={tuple(sorted((cy[k],cy[(k+1)%3]))) for k in range(3)};sgn=1 if np.median([w for e,w in omega.items() if e not in boundary])>0 else -1
    omega={e:w*sgn for e,w in omega.items()};assert min(w for e,w in omega.items() if e not in boundary)>0
    ref=dict(G=G,rotation=rotation,outer_nodes=cy,outer_primal_id=outer,boundary=sorted(boundary),omega=[[u,v,w] for (u,v),w in sorted(omega.items())],xy_boundary=cap[cy,:2].tolist(),lam=lam.tolist(),linear=linear.tolist(),beta=beta.tolist(),height_sign=sgn,original_q=q.tolist(),original_P=P.tolist(),original_cap=cap.tolist(),schlegel_d=d,relative_visibility=score,origin_weights_gamma=gamma.tolist())
    print('REFERENCE','outer',outer,cy,'d',d,'visibility',score,'cond_linear',np.linalg.cond(linear),'weights',min(omega.values()),max(omega.values()),'lambda',lam.min(),lam.max(),flush=True)
    (R/'TUTTE_C650_REFERENCE.json').write_text(json.dumps(ref,separators=(',',':')))
    return ref

class TutteBody:
    def __init__(self,ref,edges):
        self.ref=ref;self.N=len(ref['original_q']);self.edges=sorted(map(tuple,edges));self.faces,self.rot,self.df=embedded_faces(self.edges,{int(k):v for k,v in ref['rotation'].items()})
        self.B=list(ref['outer_nodes']);self.boundary={tuple(e) for e in ref['boundary']};self.outer=next(i for i,c in enumerate(self.faces) if set(c)==set(self.B) and len(c)==3)
        self.internal=[i for i in range(self.N) if i not in self.B];self.idx={i:k for k,i in enumerate(self.internal)};self.xyB=np.array(ref['xy_boundary']);self.free_edges=[e for e in self.edges if e not in self.boundary];self.EF=np.array(self.free_edges,int)
        ww={(u,v):w for u,v,w in ref['omega']};self.w0=np.array([ww[e] for e in self.free_edges]);self.log0=np.log(self.w0);self.lam=np.array(ref['lam']);self.linear=np.array(ref['linear']);self.height_sign=ref['height_sign']
        self.invlinear=np.linalg.inv(self.linear)
        self.BI=np.zeros((len(self.internal),len(self.free_edges)));self.BB=np.zeros((3,len(self.free_edges)))
        for k,(a,b) in enumerate(self.free_edges):
            for v,sgn in [(a,1),(b,-1)]:
                if v in self.idx:self.BI[self.idx[v],k]=sgn
                else:self.BB[self.B.index(v),k]=sgn
        bedges=sorted(self.boundary);self.bedges=bedges;K=np.zeros((6,3))
        for k,(a,b) in enumerate(bedges):
            for v,u in [(a,b),(b,a)]:K[2*self.B.index(v):2*self.B.index(v)+2,k]=self.xyB[self.B.index(u)]-self.xyB[self.B.index(v)]
        self.Kinv=np.linalg.pinv(K)
        adj=collections.defaultdict(list)
        for u,v in self.edges:
            f,g=self.df[u,v],self.df[v,u];adj[f].append((g,u,v));adj[g].append((f,v,u))
        done={self.outer};todo=collections.deque([self.outer]);self.plan=[]
        while todo:
            f=todo.popleft()
            for g,u,v in adj[f]:
                if g not in done:done.add(g);todo.append(g);self.plan.append((f,g,u,v))
        self.vface=[next(i for i,c in enumerate(self.faces) if v in c) for v in range(self.N)]
        self.primal_faces=[[self.df[i,j] for j in self.rot[i]] for i in range(self.N)]
        st=self.state(self.log0,orient=False)
        for i,cy in enumerate(self.primal_faces):
            if np.dot(np.cross(st['P'][cy[1]]-st['P'][cy[0]],st['P'][cy[2]]-st['P'][cy[0]]),st['q'][i])<0:self.primal_faces[i]=cy[::-1]
    def state(self,logw,orient=True):
        w=np.exp(logw);L=(self.BI*w[None,:])@self.BI.T;rhs=-self.BI@(w[:,None]*(self.BB.T@self.xyB));xy=np.zeros((self.N,2));xy[self.B]=self.xyB;xy[self.internal]=np.linalg.solve(L,rhs)
        delta=xy[self.EF[:,1]]-xy[self.EF[:,0]]
        # BI has + at the first endpoint: boundary force is sum w*(neighbor-self).
        forces=self.BB@(w[:,None]*delta);bw=self.Kinv@(-forces.ravel());omega=dict(zip(self.free_edges,w));omega.update(zip(self.bedges,bw))
        plane=np.zeros((len(self.faces),3))
        for f,g,u,v in self.plan:
            dd=xy[v]-xy[u];ww=omega[tuple(sorted((u,v)))];dg=ww*np.array([-dd[1],dd[0]]);plane[g]=plane[f]+np.r_[dg,-dg@xy[u]]
        plane*=self.height_sign
        z=np.array([plane[f,:2]@xy[v]+plane[f,2] for v,f in enumerate(self.vface)]);cap=np.column_stack([xy,z]);o=self.lam@cap
        normals=np.column_stack([plane[:,:2],-np.ones(len(plane))]);h=-plane[:,2]-normals@o;pcap=normals/h[:,None];P=pcap@self.linear;q=(cap-o)@self.invlinear.T
        out=dict(q=q,P=P,cap=cap,planes=plane,weights=w,xy=xy,omega=omega,origin=o,denom=h)
        if orient:
            rr=mechanics(q,self.primal_faces,P=P,details=False,tol=1e-10);out.update(audit=rr)
        return out

if __name__=='__main__':
    R=Path(__file__).parent;H=[tuple(map(int,l.split())) for l in (R/'H213_edges.txt').read_text().splitlines()];H249=list(map(tuple,json.loads((R/'H249_RESTORATION.json').read_text())['edges']))
    ref=reference(R,H)
    for name,edges in [('G650',ref['G']),('H249',H249),('H213',H)]:
        body=TutteBody(ref,edges);st=body.state(body.log0);print('TUTTE_BODY',name,st['audit'],flush=True)
        if name=='G650':
            want=np.array(ref['original_P']);got=st['P'];cost=np.linalg.norm(got[:,None,:]-(want+np.array(ref['beta']))[None,:,:],axis=2);print('REFERENCE_ERROR',cost.min(1).max(),flush=True)
        np.savez(R/(name+'_FITTED_TUTTE.npz'),q=st['q'],P=st['P'],logw=body.log0,cap=st['cap']);(R/(name+'_FITTED_TUTTE_faces.json')).write_text(json.dumps(body.primal_faces,separators=(',',':')))
