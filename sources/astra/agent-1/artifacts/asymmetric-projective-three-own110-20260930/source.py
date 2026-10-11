"""Single physical caps with a three-coordinate moving-apex mass closure.

The whole uniformly filled hull is reintegrated, and Newton solves its three
first moments. Root escape is an independently checked inequality, not a
weighted mass, shifted reference point, or inherited symmetry claim.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time,hashlib
import numpy as np
from scipy.spatial import ConvexHull,QhullError
from free_primal_goal import mesh_points
from geometry import arrows
from persistence_search import pairs
from cyclic_flower_mass_goal import Found

def mass_apex_jacobian(X):
    h=ConvexHull(X)
    if h.equations[:,3].max()>=-1e-10:raise ValueError('Reference origin outside physical point hull')
    tri=h.simplices.copy();a=X[tri];flip=np.einsum('ij,ij->i',np.cross(a[:,1]-a[:,0],a[:,2]-a[:,0]),h.equations[:,:3])<0
    tri[flip]=tri[flip][:,[0,2,1]];a=X[tri];six=np.einsum('ij,ij->i',a[:,0],np.cross(a[:,1],a[:,2]));T=six.sum();s=a.sum(1)
    if six.min()<=0 or T<=0:raise ValueError('Invalid oriented uniform mass')
    g=(six[:,None]*s).sum(0)/(4*T);ds=np.zeros((len(tri),3));has=np.zeros(len(tri),bool)
    for k in range(3):
        take=tri[:,k]==0;ds[take]=np.cross(a[take,(k+1)%3],a[take,(k+2)%3]);has|=take
    J=(s.T@ds+np.eye(3)*six[has].sum()-4*np.outer(g,ds.sum(0)))/(4*T)
    if not has.any():raise ValueError('Mass-balancing apex is inactive')
    return g,J,float(T/6)

def close_mass(X):
    Y=X.copy()
    for it in range(30):
        g,J,V=mass_apex_jacobian(Y);old=np.linalg.norm(g)
        if old<2e-12:
            W=arrows(Y);w=W.max(1)
            if w[0]>=-1e-10 or w[1:].min()<=1e-10:raise ValueError('Mass root does not retain strict single unstable apex')
            return Y,it
        if np.linalg.cond(J)>1e10:raise ValueError('Physical apex mass Jacobian is singular')
        delta=np.linalg.solve(J,-g);accepted=False
        for j in range(15):
            Z=Y.copy();Z[0]+=delta*2**-j
            try:gz,_,_=mass_apex_jacobian(Z)
            except (ValueError,QhullError):continue
            if np.linalg.norm(gz)<old*(1-1e-4*2**-j):Y=Z;accepted=True;break
        if not accepted:raise ValueError('Physical apex mass Newton failed line search')
    raise ValueError('Physical apex mass Newton exhausted finite steps')

def projective_moments(X):
    h=ConvexHull(X)
    if h.equations[:,3].max()>=-1e-10:raise ValueError('Projective mass source does not contain the origin')
    tri=h.simplices.copy();a=X[tri];flip=np.einsum('ij,ij->i',np.cross(a[:,1]-a[:,0],a[:,2]-a[:,0]),h.equations[:,:3])<0
    tri[flip]=tri[flip][:,[0,2,1]];a=X[tri];six=np.einsum('ij,ij->i',a[:,0],np.cross(a[:,1],a[:,2]));s=a.sum(1)
    if six.min()<=0:raise ValueError('Invalid projective uniform tetrahedral mass')
    g=(six[:,None]*s).sum(0)/(4*six.sum())
    M=(np.einsum('t,ti,tj->ij',six,s,s)+np.einsum('t,tki,tkj->ij',six,a,a))/(20*six.sum())
    return g,5*M-4*np.outer(g,g)

def close_projective_mass(X):
    Y=X.copy()
    for it in range(30):
        g,K=projective_moments(Y);old=np.linalg.norm(g)
        if old<2e-12:
            W=arrows(Y);w=W.max(1)
            if w[0]>=-1e-10 or w[1:].min()<=1e-10:raise ValueError('Projective mass root does not retain single unstable vertex')
            return Y,it
        if np.linalg.cond(K)>1e10:raise ValueError('Physical projective mass Jacobian is singular')
        db=np.linalg.solve(K,g);accepted=False
        for j in range(15):
            den=1+Y@db*2**-j
            if den.min()<=1e-7:continue
            Z=Y/den[:,None]
            try:gz,_=projective_moments(Z)
            except (ValueError,QhullError):continue
            if np.linalg.norm(gz)<old*(1-1e-4*2**-j):Y=Z;accepted=True;break
        if not accepted:raise ValueError('Physical projective mass Newton failed line search')
    raise ValueError('Physical projective mass Newton exhausted finite steps')

def run(source,out,rounds=24,samples=1800,seed=934821,closure='apex'):
    if closure not in ('apex','projective'):raise ValueError('Unknown explicit uniform mass closure')
    mass_close=close_mass if closure=='apex' else close_projective_mass
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);data=pathlib.Path(source).read_bytes();(out/'source_body.npz').write_bytes(data)
    X=np.load(out/'source_body.npz')['X'];m=mesh_points(X);X=X[m['active']];rng=np.random.default_rng(seed);start=time.time();hist=[]
    if m['row']['U']!=1 or max(abs(m['g']))>2e-9:raise ValueError('Centred single-U physical entrance required')
    if np.argmax(np.linalg.norm(X,axis=1))!=0:raise ValueError('The selected apex must be the unique unstable vertex')
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes());(out/'definition.json').write_text(json.dumps(dict(source=str(pathlib.Path(source).resolve()),sha256=hashlib.sha256(data).hexdigest(),rounds=rounds,samples=samples,seed=seed,closure=closure,
        scope='Literal asymmetric cap/replacement, explicit physical mass closure, fresh maximal hull; only own110 qualifies'),indent=2))
    g,J,_=mass_apex_jacobian(X);d=rng.normal(size=3);d/=np.linalg.norm(d);h=1e-6;Y=X.copy();Y[0]+=h*d;Z=X.copy();Z[0]-=h*d;fd=(mass_apex_jacobian(Y)[0]-mass_apex_jacobian(Z)[0])/(2*h);err=float(max(abs(fd-J@d)))
    (out/'directional_check.json').write_text(json.dumps(dict(step=h,error=err,finite_difference=fd.tolist(),analytic=(J@d).tolist()),indent=2))
    if err>2e-7:raise ValueError('Physical mass-apex derivative check failed')
    if closure=='projective':
        _,K=projective_moments(X);gp,_=projective_moments(X/(1+h*(X@d))[:,None]);gm,_=projective_moments(X/(1-h*(X@d))[:,None]);fd=(gp-gm)/(2*h);err=float(max(abs(fd+K@d)))
        (out/'projective_directional_check.json').write_text(json.dumps(dict(step=h,error=err,finite_difference=fd.tolist(),analytic=(-K@d).tolist()),indent=2))
        if err>2e-7:raise ValueError('Physical projective mass derivative check failed')
    def inspect(Y,label):
        mm=mesh_points(Y);row=mm['row']
        if 17<=row['E']<=249 and row['S']==row['U']==1:
            np.savez(out/'POTENTIAL_OWN110.npz',X=Y,Q=mm['Q']);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(**label,**row),indent=2));raise Found()
        return mm
    try:
        for k in range(rounds):
            m=inspect(X,dict(round=k,stage='entrance'));st=m['row'];pp,h=pairs(m['R'],m['eq']);bars=1-h[pp[:,1]]/np.sum(m['R'][pp[:,0]]**2,axis=1);bestscore=(st['S'],float(max(bars,default=0)));best=None
            stable=np.flatnonzero(arrows(m['R']).max(1)<0);bottom=float(X[:,2].min());targets=[int(j) for j in stable if np.linalg.norm(m['R'][j,:2])>1e-8]
            if not targets:raise ValueError('No unwanted stable carrier selected')
            deletable=[int(i) for i in range(1,len(X)) if X[i,2]>bottom+1e-8];p=out/f'round{k:02d}';p.mkdir();np.savez(p/'parent.npz',X=X);tested=0;failures={}
            for j in range(samples):
                target=int(rng.choice(targets));R=m['R'][target];n=R/np.linalg.norm(R);bound=(X@R+np.linalg.norm(X,axis=1)*np.linalg.norm(R))/2;parents=np.flatnonzero(bound>1+1e-7)
                if not len(parents):continue
                parent=int(rng.choice(parents));v=X[parent];d=n+rng.choice([.01,.04,.12,.4,1.])*rng.normal(size=3);d/=np.linalg.norm(d);q=v/2+(1-10**rng.uniform(-6,-.3))*np.linalg.norm(v)/2*d
                if q@R<=1+1e-7 or q[2]<=bottom+1e-9 or q@(v-q)<=1e-11:continue
                raw=np.r_[X,[q]];alternatives=[None]
                if st['E']>243:alternatives.extend(map(int,rng.choice(deletable,size=min(9,len(deletable)),replace=False)))
                label=dict(round=k,sample=j,target=target,parent=parent,point=q.tolist())
                for removed in alternatives:
                    try:
                        Y=raw if removed is None else np.delete(raw,removed,axis=0);Y,ni=mass_close(Y);attempt=dict(**label,explicitly_removed_old_vertex=removed,mass_iterations=ni);mm=inspect(Y,attempt);tested+=1;row=mm['row']
                        if not 17<=row['E']<=249:continue
                        if row['U']!=1 or max(abs(mm['g']))>2e-9:raise ValueError('Independent actual mass/unstable readback failed')
                        pp,h=pairs(mm['R'],mm['eq']);bb=1-h[pp[:,1]]/np.sum(mm['R'][pp[:,0]]**2,axis=1);qmax=float(max(bb,default=0));score=(row['S'],qmax)
                        if score<bestscore:
                            if mm['active'][0]!=0:raise ValueError('Mass-balancing apex lost')
                            bestscore=score;best=(Y[mm['active']],dict(**attempt,**row,Qmax=qmax));np.savez(p/'best.npz',X=best[0]);(p/'best.json').write_text(json.dumps(best[1],indent=2));print('ASYMMETRIC_PHYSICAL_CAP',json.dumps({a:b for a,b in best[1].items() if a!='point'}),flush=True)
                    except (ValueError,RuntimeError,AssertionError,QhullError,np.linalg.LinAlgError) as err:
                        key=str(err).split('\n')[0];failures[key]=failures.get(key,0)+1
            rec=dict(round=k,parent=st,tested=tested,failures=failures,adopted=best is not None,seconds=time.time()-start)
            if best is not None:X,rec['result']=best;np.savez(out/'latest.npz',X=X)
            hist.append(rec);(out/'history.json').write_text(json.dumps(hist,indent=2))
            if best is None:break
    except Found:return
    (out/'FINITE_END.json').write_text(json.dumps(dict(rounds=len(hist),seconds=time.time()-start,scope='Finite asymmetric physical cap search ended without a qualifying body'),indent=2))

if __name__=='__main__':
    import sys
    run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 24,int(sys.argv[4]) if len(sys.argv)>4 else 1800)
