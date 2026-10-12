"""Finite changed-base homogeneous pyramid search, not an exclusion certificate.
Base: literal C80 planar points, one/two added outward points, then a planar
area-preserving affine transformation. Apex: h between R and q/2, tangent a
inside the diameter ball of the selected base vertex. C<32 is rejected.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,hashlib,json,sys
from pathlib import Path
import numpy as np
import scipy
from scipy.spatial import ConvexHull,QhullError
from scipy.optimize import differential_evolution,minimize
POINTS=[[-66294190,2608697],[-66539507,-12351907],[-63292228,17048174],[-63717145,-27612608],[-57823754,30439587],[-57515357,-42510726],[-50192873,42502470],[-47518485,-56391110],[-40722545,52969394],[-33461658,-68086491],[-15099182,-76015914],[-29598263,61750890],[7302524,-77602682],[32327466,106281898],[79500788,46525186],[84345871,39971911],[90059112,29647108],[97069983,-15011783],[94470034,18198055],[97382431,4337405]]
TAU=1e-4

def polygon(P):
    ix=ConvexHull(P).vertices;B=P[ix];N=np.roll(B,-1,axis=0)
    cross=B[:,0]*N[:,1]-B[:,1]*N[:,0];area2=cross.sum();assert area2>0
    centre=((B+N)*cross[:,None]).sum(axis=0)/(3*area2)
    return B-centre,ix,centre

def score(X):
    n=len(X)-1;B=X[:n];A=X[n]
    D=np.stack([np.roll(B,1,axis=0)-B,np.roll(B,-1,axis=0)-B,A-B],axis=1)
    den=np.einsum('ijk,ijk->ij',D,D)
    if np.min(den)<1e-20:raise ValueError('collapsed edge')
    z=np.einsum('ik,ijk->ij',B,D)/den
    e=np.r_[z.max(axis=1),np.max((B-A)@A/np.einsum('ij,ij->i',B-A,B-A))]
    root=int(np.argmax(np.einsum('ij,ij->i',X,X)))
    loss=np.maximum(TAU-e,0);loss[root]=0
    return e,root,loss

def census(B,a,h):
    n=len(B);P=np.vstack([np.c_[B,np.zeros(n)],np.r_[a,h]]);g=np.r_[a,h]/4;P-=g
    D=np.roll(P[:n],-1,axis=0)-P[:n];normal=np.cross(D,P[n]-P[:n]);height=np.einsum('ij,ij->i',normal,P[:n])
    if np.min(height)<=0:raise ValueError('invalid support')
    Q=np.vstack([normal/height[:,None],[0,0,-4/h]])
    u,s=score(P),score(Q);loss=float(u[2]@u[2]+s[2]@s[2])
    return loss,P,Q,u,s,g

class Family:
    def __init__(self,ears,witness):
        B,_,_=polygon(np.array(POINTS,dtype=float));self.B=B/np.max(np.linalg.norm(B,axis=1));self.ears=ears;self.witness=witness;self.evals=0
    def evaluate(self,x,detail=False):
        self.evals+=1
        try:
            P=self.B.copy()
            for k in range(self.ears):
                angle,r=x[2*k:2*k+2];P=np.vstack([P,np.exp(r)*np.array([np.cos(angle),np.sin(angle)])])
            j=2*self.ears;stretch,shear=x[j:j+2];T=np.array([[np.exp(stretch),shear],[0,np.exp(-stretch)]])
            B,ix,bc=polygon(P@T.T);n=len(B)
            if n<8:raise ValueError('C below32 rejected')
            Q0=np.max(np.linalg.norm(B,axis=1));B/=Q0
            N=np.roll(B,-1,axis=0);D=N-B;R=np.min((D[:,0]*(-B[:,1])-D[:,1]*(-B[:,0]))/np.linalg.norm(D,axis=1))
            ordered=np.argsort(np.linalg.norm(B,axis=1))[::-1];w=int(ordered[self.witness%len(B)]);b=B[w];q=np.linalg.norm(b)
            if R>=q/2 or R<=0:
                val=10+100*(max(0,R-q/2+.01))**2
                return {'invalid':'no admissible height for selected witness','R':float(R),'loss':float(val)} if detail else val
            h=R+(q/2-R)/(1+np.exp(-x[j+2]));v=np.array(x[j+3:j+5]);v=v/np.sqrt(1+v@v);rad=np.sqrt(q*q/4-h*h);a=b/2+rad*v
            loss,PP,QQ,u,s,g=census(B,a,h)
            if not detail:return loss
            return {'x':list(map(float,x)),'loss':loss,'n':n,'C':4*n,'S':int(sum(s[0]<0)),'U':int(sum(u[0]<0)),'root_vertex':u[1],'root_face':s[1],
                'min_nonroot_u':float(np.min(np.delete(u[0],u[1]))),'min_nonroot_s':float(np.min(np.delete(s[0],s[1]))),'primal_eta':u[0].tolist(),'dual_eta':s[0].tolist(),
                'R':float(R),'Q':1.,'h':float(h),'a':a.tolist(),'base':B.tolist(),'base_original_hull_indices':ix.tolist(),'apex_witness_base_index':w,
                'raw_points':np.vstack([np.c_[B,np.zeros(n)],np.r_[a,h]]).tolist(),'own_centroid':g.tolist(),
                'numerical110':bool(sum(u[0]<0)==1 and sum(s[0]<0)==1 and min(np.min(np.delete(u[0],u[1])),np.min(np.delete(s[0],s[1])))>1e-8)}
        except (ValueError,FloatingPointError,QhullError,AssertionError,np.linalg.LinAlgError):
            return {'invalid':'invalid geometric state','loss':1e6} if detail else 1e6

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--ears',type=int,choices=[1,2],default=1);ap.add_argument('--seed',type=int,default=160926);ap.add_argument('--witness',type=int,default=0);ap.add_argument('--iterations',type=int,default=250);ap.add_argument('--polish',type=int,default=2000);ap.add_argument('--out',required=True);a=ap.parse_args()
    f=Family(a.ears,a.witness);bounds=[v for _ in range(a.ears) for v in [(-np.pi,np.pi),(np.log(1.1),np.log(8.))]]+[(-1.5,1.5),(-2.,2.),(-5.,5.),(-4.,4.),(-4.,4.)]
    best=[float('inf')];records=[]
    def cb(x,conv):
        loss=f.evaluate(x)
        if loss<best[0]*.8:
            best[0]=loss;d=f.evaluate(x,True);records.append({'phase':'de_improvement',**d});print('improvement',loss,d.get('C'),d.get('S'),d.get('U'),flush=True)
        return False
    de=differential_evolution(f.evaluate,bounds,seed=a.seed,popsize=12,maxiter=a.iterations,tol=1e-10,atol=0,polish=False,updating='immediate',workers=1,callback=cb)
    records.append({'phase':'de_final','success':bool(de.success),'message':str(de.message),**f.evaluate(de.x,True)})
    for k,x in enumerate(de.population[np.argsort(de.population_energies)[:4]]):
        r=minimize(f.evaluate,x,method='Nelder-Mead',bounds=bounds,options={'maxiter':a.polish,'xatol':1e-10,'fatol':1e-15})
        d=f.evaluate(r.x,True);records.append({'phase':'polish'+str(k),'success':bool(r.success),'message':str(r.message),**d});print('polish',k,d['loss'],d.get('C'),d.get('S'),d.get('U'),flush=True)
    out={'family':'C80 changed planar base via added outer points and planar determinant-one affine map; homogeneous filled volume','ears':a.ears,'witness_rank':a.witness,'seed':a.seed,'bounds':bounds,'iterations':a.iterations,'polish_maxiter':a.polish,'popsize':12,'tau':TAU,'evaluations':f.evals,'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__,'records':records,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'terminal':'CHANGED_BASE_PYRAMID_FINITE_SCREEN_COMPLETE','certified_exclusion':False}
    Path(a.out).write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n');print(out['terminal'],'best',min(x['loss'] for x in records),'numerical110',any(x.get('numerical110',False) for x in records),flush=True)
if __name__=='__main__':main()
