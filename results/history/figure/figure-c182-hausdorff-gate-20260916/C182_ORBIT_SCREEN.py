"""Finite nonlocal affine/projective own-mass screen of exact C182.

This is a numerical search, not an exclusion proof. Actual filled centroid is
integrated on every projective trial; an affine-only trial uses the same code.
Input geometry is pinned to the independently audited FINCH3 C182 report.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import argparse,hashlib,json,sys,time
from pathlib import Path
from fractions import Fraction as F
import numpy as np
import scipy
from scipy.optimize import differential_evolution,minimize

SHA='caf78ccee9abec82174d346227b2da7d99a13b823c88a4ef405e3e8cb9d1967d'
TAU=1e-5

def encode(v):return (json.dumps(v,sort_keys=True,separators=(',',':'))+'\n').encode()

def prepare(path):
    bb=Path(path).read_bytes(); assert len(bb)==51790 and hashlib.sha256(bb).hexdigest()==SHA
    a=json.loads(bb); p=np.array([[float(F(x)) for x in r] for r in a['raw_vertices']])
    g=np.array([float(F(x)) for x in a['raw_centroid']]); p-=g
    val,vec=np.linalg.eigh(p.T@p/len(p)); W=(vec/np.sqrt(val)).T
    p=p@W.T
    ns=np.array(a['normals'],dtype=float); hs=np.array(a['offsets'],dtype=float)-ns@g
    q=(ns/hs[:,None])@np.linalg.inv(W)
    faces=a['faces']; tris=np.array([(f[0],f[j],f[j+1]) for f in faces for j in range(1,len(f)-1)])
    edges=np.array(a['edges']); adj=[[] for _ in p]; dual=[[] for _ in q]
    for i,j in edges:adj[i].append(j);adj[j].append(i)
    for i,j in edges:
        ff=[k for k,f in enumerate(faces) if i in f and j in f]; assert len(ff)==2
        k,l=ff;dual[k].append(l);dual[l].append(k)
    def rows(adj):
        i=np.array([k for k,row in enumerate(adj) for _ in row]);j=np.array([v for row in adj for v in row]);starts=np.cumsum([0]+[len(row) for row in adj[:-1]])
        return i,j,starts
    return p,q,tris,W,rows(adj),rows(dual)

class Orbit:
    def __init__(self,path,mode):
        self.p,self.q,self.tris,self.W,self.pe,self.qe=prepare(path);self.mode=mode;self.evals=0
    def shape(self,x):
        if self.mode=='projective':
            w=x[5:8];w=w/(1+np.max(np.abs(self.p@w)))
        else:w=np.zeros(3)
        den=1+self.p@w
        assert den.min()>0
        Y=self.p/den[:,None]
        a,b,c=[Y[self.tris[:,k]] for k in range(3)]
        det=np.einsum('ij,ij->i',a,np.cross(b,c));total=det.sum()
        if total<=0:raise FloatingPointError('bad volume')
        g=(det[:,None]*(a+b+c)).sum(axis=0)/(4*total)
        q=self.q+w;h=1-q@g
        if h.min()<=0:raise FloatingPointError('outside own centroid')
        q=q/h[:,None]
        A=np.array([[np.exp(x[0]),x[2],x[3]],[0,np.exp(x[1]),x[4]],[0,0,np.exp(-x[0]-x[1])]])
        return (Y-g)@A.T, q@np.linalg.inv(A),w,A,g,float(total/6),float(den.min())
    @staticmethod
    def exits(X,edges):
        i,j,starts=edges;d=X[j]-X[i];norm=np.einsum('ij,ij->i',d,d)
        eta=np.einsum('ij,ij->i',X[i],d)/norm
        e=np.maximum.reduceat(eta,starts)
        root=int(np.argmax(np.einsum('ij,ij->i',X,X)))
        return e,root
    def evaluate(self,x,detail=False):
        self.evals+=1
        try:
            P,Q,w,A,g,vol,dmin=self.shape(np.asarray(x));pu,ru=self.exits(P,self.pe);qs,rs=self.exits(Q,self.qe)
            pp=np.maximum(TAU-pu,0);qq=np.maximum(TAU-qs,0);pp[ru]=0;qq[rs]=0
            loss=float(pp@pp+qq@qq)
            if not np.isfinite(loss):raise FloatingPointError('nonfinite')
        except (FloatingPointError,np.linalg.LinAlgError,AssertionError):return 1e20 if not detail else {'invalid':True}
        if not detail:return loss
        return {'x':list(map(float,x)), 'loss':loss,'S':int(sum(qs<0)),'U':int(sum(pu<0)),
            'S_indices':np.where(qs<0)[0].tolist(),'U_indices':np.where(pu<0)[0].tolist(),
            'root_face':rs,'root_vertex':ru,'min_required_primal_eta':float(np.min(np.delete(pu,ru))),
            'min_required_dual_eta':float(np.min(np.delete(qs,rs))),
            'small_abs_eta':float(min(np.min(abs(qs)),np.min(abs(pu)))),
            'A':A.tolist(),'w':w.tolist(),'pre_affine_centroid':g.tolist(),'pre_affine_volume':vol,
            'projective_denominator_min':dmin,'affine_condition_number':float(np.linalg.cond(A)),
            'numerical_110':bool(sum(qs<0)==1 and sum(pu<0)==1 and np.min(np.delete(pu,ru))>1e-8 and np.min(np.delete(qs,rs))>1e-8)}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--audit',required=True);ap.add_argument('--out',required=True);ap.add_argument('--mode',choices=['affine','projective'],required=True);ap.add_argument('--seed',type=int,default=182091);ap.add_argument('--iterations',type=int,default=250);a=ap.parse_args()
    mode=a.mode;obj=Orbit(a.audit,mode);bounds=[(-2,2),(-2,2),(-4,4),(-4,4),(-4,4)]+([(-4,4)]*3 if mode=='projective' else [])
    n=len(bounds);records=[{'phase':'whitened',**obj.evaluate(np.zeros(n),True)}]
    opts={'maxiter':400,'maxfun':8000,'ftol':1e-14,'gtol':1e-9,'maxls':30}
    r=minimize(obj.evaluate,np.zeros(n),method='L-BFGS-B',bounds=bounds,options=opts)
    records.append({'phase':'local_from_whitened','success':bool(r.success),'message':str(r.message),**obj.evaluate(r.x,True)})
    print(mode,'local',records[-1],flush=True)
    best=[float('inf')]
    def callback(x,convergence):
        value=obj.evaluate(x)
        if value<best[0]*.9:
            best[0]=value;d=obj.evaluate(x,True);print(mode,'de_progress',d['loss'],d['S'],d['U'],flush=True)
        return False
    de=differential_evolution(obj.evaluate,bounds,popsize=12,maxiter=a.iterations,tol=1e-10,atol=0,seed=a.seed,polish=False,workers=1,updating='immediate',callback=callback,x0=r.x)
    records.append({'phase':'differential_evolution','success':bool(de.success),'message':str(de.message),'nit':int(de.nit),'nfev':int(de.nfev),**obj.evaluate(de.x,True)})
    for k,x in enumerate(de.population[np.argsort(de.population_energies)[:4]]):
        r=minimize(obj.evaluate,x,method='L-BFGS-B',bounds=bounds,options=opts)
        records.append({'phase':'local_polish_'+str(k),'success':bool(r.success),'message':str(r.message),**obj.evaluate(r.x,True)})
        print(mode,records[-1]['phase'],records[-1]['loss'],records[-1].get('S'),records[-1].get('U'),flush=True)
    result={'input_sha256':SHA,'mode':mode,'seed':a.seed,'tau':TAU,'bounds':bounds,'de_popsize':12,'de_maxiter':a.iterations,'de_tol':1e-10,'de_atol':0,'local_options':opts,'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__,'whitening':obj.W.tolist(),'records':records,'evaluations':obj.evals,'terminal':'C182_FINITE_NONLOCAL_ORBIT_SCREEN_COMPLETE','certified_exclusion':False}
    Path(a.out).write_bytes(encode(result));print(result['terminal'],mode,'any_numerical110',any(x.get('numerical_110',False) for x in records),flush=True)
if __name__=='__main__':main()
