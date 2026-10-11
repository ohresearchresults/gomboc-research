# Numerical reconstruction and Jacobian demonstration, not an exact census.
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import itertools
from fractions import Fraction
import numpy as np
from scipy.spatial import ConvexHull
from coarse125 import build

def cycle(points,normal):
    u=np.cross(normal,np.eye(3)[np.argmin(abs(normal))])
    u/=np.linalg.norm(u)
    v=np.cross(normal,u);v/=np.linalg.norm(v)
    p=points-points.mean(0)
    return np.argsort(np.arctan2(p@v,p@u))

def cosines(P):
    e=P[None,:,:]-P[:,None,:]
    den=np.linalg.norm(P,axis=1)[:,None]*np.linalg.norm(e,axis=2)
    a=np.einsum('ik,ijk->ij',P,e)/np.maximum(den,1e-30)
    np.fill_diagonal(a,-10)
    return a

def widest(A,root):
    n=len(A);cap=np.full(n,-np.inf);cap[root]=np.inf
    done=np.zeros(n,bool);pred=np.full(n,-1,int)
    for k in range(n):
        j=int(np.argmax(np.where(done,-np.inf,cap)))
        done[j]=True
        cand=np.minimum(A[:,j],cap[j])
        good=(cand>cap)&(~done)
        cap[good]=cand[good];pred[good]=j
    src=np.array([i for i in range(n) if i!=root])
    return src,pred[src]

def edge_values(P,DP,src,dst):
    p=P[src];w=P[dst];e=w-p
    rp=np.linalg.norm(p,axis=1);re=np.linalg.norm(e,axis=1)
    if min(rp)<=0 or min(re)<=0:raise ValueError('zero vector')
    a=np.einsum('ij,ij->i',p,e)/(rp*re)
    gp=((w-2*p)/(rp*re)[:,None]-a[:,None]*p/rp[:,None]**2
        +a[:,None]*e/re[:,None]**2)
    gw=p/(rp*re)[:,None]-a[:,None]*e/re[:,None]**2
    J=np.einsum('ij,ijk->ik',gp,DP[src])
    J+=np.einsum('ij,ijk->ik',gw,DP[dst])
    return a,J

class Model:
    def __init__(self,config):
        self.config=config
        self.q0=np.array([[float(Fraction(v)) for v in p]
                          for p in config['q']])
        self.apex=set(config['apex']);self.stable=config['stable']
        self.contacts=config['contacts']
        self.quads=[set([j]+ids) for j,ids in self.contacts]
        self.off=[i for i in range(len(self.q0)) if i not in self.apex]
        self.free=[(i,k) for i in range(len(self.q0))
                   for k in range(2 if i in self.apex else 3)]
        self.x0=np.array([self.q0[i,k] for i,k in self.free])

    def decode(self,x,jac=True):
        q=self.q0.copy();D=np.zeros((len(q),3,len(x)))
        for k,(i,d) in enumerate(self.free):
            q[i,d]=x[k];D[i,d,k]=1
        for j,ids in self.contacts:
            A=q[ids];p=np.linalg.solve(A,np.ones(3))
            dp=(-np.linalg.solve(A,np.einsum('ikm,k->im',D[ids],p))
                if jac else np.zeros((3,len(x))))
            e=p.copy();de=dp.copy()
            if j in self.apex:e[2]=0;de[2]=0
            den=p@e;num=1-q[j]@p
            if den<1e-15:raise ValueError('contact projection')
            dden=dp.T@e+p@de
            dnum=-D[j].T@p-q[j]@dp
            t=num/den;dt=(dnum*den-num*dden)/(den*den)
            D[j]=D[j]+e[:,None]*dt+t*de
            q[j]+=t*e
        return q,D

    def topology(self,q):
        if not np.isfinite(q).all() or np.max(q[self.off,2])>=1-1e-9:
            raise ValueError('lost apex plane')
        hull=ConvexHull(q)
        if np.max(hull.equations[:,3])>=-1e-8:
            raise ValueError('origin outside polar')
        gd={}
        for f in hull.simplices:
            fs=set(map(int,f))
            key=('a',) if fs<=self.apex else tuple(sorted(fs))
            if key!=('a',):
                for j,c in enumerate(self.quads):
                    if fs<=c:key=('q',j);break
            gd.setdefault(key,set()).update(fs)
        groups=[tuple(sorted(g)) for g in gd.values()]
        tri=[];v=[];apex=-1
        for g in groups:
            if set(g)<=self.apex:
                p=np.array([0.,0.,1.]);ids=g[:3];apex=len(v)
            else:
                ids=max(itertools.combinations(g,3),
                        key=lambda t:abs(np.linalg.det(q[list(t)])))
                p=np.linalg.solve(q[list(ids)],np.ones(3))
            if max(q@p-1)>2e-8:raise ValueError('infeasible corner')
            tri.append(ids);v.append(p)
        v=np.array(v);faces=[];active=[];tris=[];edges={}
        for f in range(len(q)):
            ix=[i for i,g in enumerate(groups) if f in g]
            if len(ix)<3:continue
            c=np.array(ix)[cycle(v[ix],q[f])].tolist()
            faces.append(c);active.append(f)
            for k in range(1,len(c)-1):tris.append([c[0],c[k],c[k+1]])
            for a,b in zip(c,c[1:]+c[:1]):
                edges.setdefault(tuple(sorted([a,b])),[]).append(f)
        if (apex<0 or len(v)-len(edges)+len(faces)!=2
                or not all(len(fs)==2 for fs in edges.values())):
            raise ValueError('invalid boundary complex')
        return dict(triples=np.array(tri),groups=groups,apex=apex,
                    faces=faces,active=np.array(active),
                    triangles=np.array(tris),edges=edges)

    def geometry(self,x,jac=True):
        q,dq=self.decode(x,jac);t=self.topology(q)
        n=len(t['triples']);v=np.zeros((n,3))
        dv=np.zeros((n,3,len(x)));v[t['apex'],2]=1
        non=np.array([i for i in range(n) if i!=t['apex']])
        tri=t['triples'][non];A=q[tri]
        v[non]=np.linalg.solve(A,np.ones((len(non),3,1))).squeeze(-1)
        if jac:
            rhs=np.einsum('nikj,nk->nij',dq[tri],v[non])
            dv[non]=-np.linalg.solve(A,rhs)
        ix=t['triangles'];r=v[ix]
        w=np.einsum('ij,ij->i',r[:,0],np.cross(r[:,1],r[:,2]))
        vol=w.sum()/6
        moment=(w[:,None]*r.sum(1)).sum(0)/24;g=moment/vol
        if vol<=1e-10 or min(1-q@g)<=1e-8:
            raise ValueError('invalid filled mass')
        if jac:
            dr=dv[ix]
            dw=np.einsum('ikj,ik->ij',dr[:,0],np.cross(r[:,1],r[:,2]))
            dw+=np.einsum('ikj,ik->ij',dr[:,1],np.cross(r[:,2],r[:,0]))
            dw+=np.einsum('ikj,ik->ij',dr[:,2],np.cross(r[:,0],r[:,1]))
            dvol=dw.sum(0)/6
            dm=(np.einsum('ij,ik->kj',dw,r.sum(1))
                +np.einsum('i,ikj->kj',w,dr.sum(1)))/24
            dg=(dm-g[:,None]*dvol)/vol
        else:dg=np.zeros((3,len(x)))
        p=v-g;dp=dv-dg
        h=1-q@g;z=q/h[:,None]
        dh=-np.einsum('iak,a->ik',dq,g)-q@dg
        dz=dq/h[:,None,None]-q[:,:,None]*dh[:,None,:]/h[:,None,None]**2
        return dict(q=q,dq=dq,t=t,v=v,dv=dv,vol=vol,g=g,dg=dg,
                    p=p,dp=dp,z=z,dz=dz)

    def tree(self,x,jac=True):
        m=self.geometry(x,jac);p,z,t=m['p'],m['z'],m['t']
        ia=t['active'];za=z[ia]
        au=cosines(p);ass=cosines(za);ru=t['apex']
        if self.stable not in ia:raise ValueError('lost stable root')
        rs=int(np.where(ia==self.stable)[0][0])
        iu,ju=widest(au,ru);iss,js=widest(ass,rs)
        vu,Ju=edge_values(p,m['dp'],iu,ju)
        vs,Js=edge_values(za,m['dz'][ia],iss,js)
        vals=np.r_[vu,vs];J=np.vstack([Ju,Js])
        info=dict(S=int(np.sum(ass.max(1)<0)),
                  U=int(np.sum(au.max(1)<0)),V=len(p),
                  E=len(t['edges']),F=len(ia),minimum=float(min(vals)),
                  volume=float(m['vol']),centroid=m['g'].tolist())
        m['witnesses']=(iu,ju,iss,js)
        return vals,J,info,m

def mass_close(M,x,g0):
    ci=[k for k,(i,j) in enumerate(M.free) if i==M.stable]
    x=x.copy()
    for step in range(12):
        m=M.geometry(x);err=m['g']-g0
        if np.linalg.norm(err)<2e-15:return x
        dx=np.linalg.solve(m['dg'][:,ci],-err);ok=False
        for j in range(12):
            y=x.copy();y[ci]+=2.**-j*dx
            try:
                if np.linalg.norm(M.geometry(y,False)['g']-g0)<np.linalg.norm(err):
                    x=y;ok=True;break
            except (ValueError,np.linalg.LinAlgError):pass
        if not ok:raise ValueError('mass closure failed')
    raise ValueError('mass closure residual')

def frame_matrix(m):
    iu,ju,iss,js=m['witnesses'];ia=m['t']['active'];blocks=[]
    systems=[(m['p'],m['dp'],iu,ju),
             (m['z'][ia],m['dz'][ia],iss,js)]
    for P,D,src,dst in systems:
        e=P[dst]-P[src]
        blocks.append((D[src]/np.linalg.norm(P[src],axis=1)[:,None,None])
                      .reshape(-1,D.shape[-1]))
        blocks.append(((D[dst]-D[src])/np.linalg.norm(e,axis=1)[:,None,None])
                      .reshape(-1,D.shape[-1]))
    return np.vstack(blocks)

def whitener(M,x,m):
    ci=[k for k,(i,j) in enumerate(M.free) if i==M.stable]
    fp=[k for k in range(len(x)) if k not in ci]
    T=np.zeros((len(x),len(fp)));T[fp,np.arange(len(fp))]=1
    T[ci]=-np.linalg.solve(m['dg'][:,ci],m['dg'][:,fp])
    C=frame_matrix(m)
    U,s,vt=np.linalg.svd(C@T,full_matrices=False)
    keep=s>s[0]*1e-11
    W=T@(vt[keep].T/s[keep])
    return W,C

if __name__=='__main__':
    original=Model(build(0));g0=original.geometry(original.x0,False)['g']
    coarse=Model(build(7));x=coarse.x0
    vals,J,info,m=coarse.tree(x)
    print('UNMODIFIED_PCW125_NUMERICAL',info)
    x=mass_close(coarse,x,g0)
    vals,J,info,m=coarse.tree(x)
    print('MASS_CLOSED_PCW125_NUMERICAL',info)
    print('CAP',m['q'][coarse.stable].tolist())
    W,C=whitener(coarse,x,m)
    orth_error=np.linalg.norm((C@W).T@(C@W)-np.eye(W.shape[1]))
    max_row=float(np.max(np.linalg.norm(J@W,axis=1)))
    print('FRAME_RANK',W.shape[1])
    print('ORTHOGONALITY_ERROR',orth_error)
    print('MAXIMUM_ARROW_JACOBIAN_ROW_NORM',max_row)
    assert orth_error<1e-6
    assert max_row<=np.sqrt(2)+1e-6
    print('This is a numerical derivative check, not an equilibrium certificate.')
