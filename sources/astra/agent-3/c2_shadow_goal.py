"""C2-symmetric homogeneous goal construction with positive escape paths.

Four exact coplanar basal points give a stable facet. Every other input has a
positive chord to a retained ancestor ending at the axial apex. Raising that
apex preserves all reference escape paths. C2 symmetry reduces mass closure to
one axial equation. Final acceptance still uses the exact actual centroid.
With <=85 inputs and the genuine >=4-vertex base, E<=248 and V+E+F<=498.
"""
import argparse,json,time,hashlib
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
from vertex_geometry import geometry
from support_geometry import escape
from direct_face_polish import face_scores
from goal_nomination import preserve


def body(P,selected,base,root,height=1.):
    upper=P[sorted(selected-{root})]
    q=np.array([base[0],base[0]*[-1,-1,1],base[1],base[1]*[-1,-1,1]])
    X=np.vstack((q,upper,upper*[-1,-1,1],[0.,0.,height]))
    assert len(X)<=85
    assert min(X[4:-1,2],default=height)>q[0,2]
    return X


def mass(X):
    g=geometry(X,False)
    return float(g['g'][2]),float(g['V']),g


def parents(P,root,cut,good,rng):
    n=len(P);allowed=P[:,2]>cut;allowed[root]=True
    distance=np.full(n,np.inf);distance[root]=0;parent=np.full(n,-1,int)
    order=np.argsort(np.sum(P*P,axis=1))[::-1]
    for i in order:
        if i==root or not allowed[i]:continue
        js=np.flatnonzero(good[i]&allowed&np.isfinite(distance))
        if not len(js):continue
        costs=distance[js]+rng.uniform(0,.3,len(js));j=int(js[np.argmin(costs)]);parent[i]=j;distance[i]=distance[j]+1
    paths={}
    for i in np.flatnonzero(np.isfinite(distance)):
        chain={root};j=int(i)
        while j!=root:
            assert j>=0 and j not in chain;chain.add(j);j=int(parent[j])
        paths[int(i)]=chain
    return parent,paths


def classify(g):
    centre=np.array([0.,0.,g['g'][2]]);gg=dict(g,Z=g['X']-centre)
    vf,_,_=face_scores(gg,False);nonbase=~np.all(g['T']<4,axis=1)
    vu,_=escape(gg['Z'][g['vertices']],angular=True)
    return 1+int(sum(vf[nonbase]<0)),int(sum(vu<0))


def run(pool,out,trials,seed):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);P=np.load(pool);root=int(np.argmax(P[:,2]));assert np.array_equal(P[root],[0.,0.,1.])
    # Each representative contributes both C2 images. A witness can use either.
    e=np.stack((P[None]-P[:,None],(P*[-1,-1,1])[None]-P[:,None]));dot=np.einsum('ic,aijc->aij',P,e);den=np.sqrt(np.sum(P*P,axis=1)[None,:,None]*np.sum(e*e,axis=3));weights=np.max(dot/np.maximum(den,1e-100),axis=0);np.fill_diagonal(weights,-np.inf);good=weights>1e-7
    rng=np.random.default_rng(seed);history=[];closed=0;bestS=10**9;start=time.time()
    (out/'definition.json').write_text(json.dumps(dict(pool=str(Path(pool).resolve()),pool_sha256=hashlib.sha256(Path(pool).read_bytes()).hexdigest(),root=root,seed=seed,max_inputs=85,max_edges=248,method='C2 paired positive-shadow forest with four coplanar base vertices; actual axial volume-centroid closure by raising apex; exact own110 required'),indent=2))
    for case in range(trials):
        cut=float(P[:,2].min()+rng.uniform(.001,.45)**1.3)
        parent,paths=parents(P,root,cut,good,rng);reachable=np.array(list(paths))
        lower=np.flatnonzero(P[:,2]<cut);crossings=[]
        for i in lower:
            for j in reachable:
                if j==root or not good[i,j]:continue
                for sign in (1.,-1.):
                    pp=P[j]*[sign,sign,1.]
                    if P[i]@(pp-P[i])<=0:continue
                    alpha=(cut-P[i,2])/(pp[2]-P[i,2]);b=P[i]+alpha*(pp-P[i]);b[2]=cut
                    if b@(pp-b)>1e-12:crossings.append((int(i),int(j),b))
        # A basal point may be any point strictly inside the parent's Thales
        # ball; it need not lie on one of the scaffold's original edges.
        for j in reachable:
            if j==root or len(paths[int(j)]-{root})>40:continue
            radius2=float(P[j]@P[j]/4-(cut-P[j,2]/2)**2)
            if radius2<=1e-8:continue
            for _ in range(4):
                angle=rng.uniform(0,2*np.pi);radius=np.sqrt(radius2)*rng.uniform(.3,.98)
                b=np.r_[P[j,:2]/2+radius*np.array([np.cos(angle),np.sin(angle)]),cut]
                assert b@(P[j]-b)>0
                crossings.append((-1,int(j),b))
        if len(crossings)<2:continue
        chosen=None
        for _ in range(20):
            pair=rng.choice(len(crossings),2,replace=False);a,b=[crossings[int(i)]for i in pair]
            if abs(np.linalg.det(np.array([a[2][:2],b[2][:2]])))<.015:continue
            selected=paths[a[1]]|paths[b[1]]
            if len(selected-{root})>40:continue
            chosen=(a,b,selected);break
        if chosen is None:continue
        a,b,selected=chosen;base=np.array([a[2],b[2]])
        X=body(P,selected,base,root);gz,V,_=mass(X);moment=gz*V
        # Add whole ancestor paths according to their actual first-moment
        # contribution. All selected inputs retain a positive escape witness.
        for iteration in range(12):
            options=[]
            available=[j for j in paths if j not in selected and len((selected|paths[j])-{root})<=40]
            available.sort(key=lambda j:P[j,2]+rng.uniform(0,.18))
            for j in available[:36]:
                ss=selected|paths[j];YY=body(P,ss,base,root);z,vol,_=mass(YY);options.append((z*vol,ss,z,vol))
            if not options:break
            mm,ss,z,vol=min(options,key=lambda x:x[0])
            if mm>=moment-1e-11:break
            selected=ss;moment=mm;gz,V=z,vol
        X=body(P,selected,base,root);gz,V,g=mass(X)
        row=dict(case=case,cut=cut,inputs=len(X),initial_centroid_z=gz,initial_moment_z=gz*V,selected=sorted(selected),base_edges=[[a[0],a[1]],[b[0],b[1]]],base_points=base.tolist())
        if gz < -1e-9:
            upper=2.
            while mass(body(P,selected,base,root,upper))[0]<0 and upper<64:upper*=2
            try:
                tip=brentq(lambda h:mass(body(P,selected,base,root,h))[0],1.,upper,xtol=5e-15,rtol=9e-16)
                Y=body(P,selected,base,root,tip);zz,V,g=mass(Y);S,U=classify(g);closed+=1;bestS=min(bestS,S);row.update(tip=tip,centroid_z=zz,S=S,U=U,V_hull=len(g['vertices']))
                d=out/f'closed{case:05d}';d.mkdir();np.save(d/'physical_points.npy',Y);np.save(d/'parent_indices.npy',parent);(d/'construction.json').write_text(json.dumps(row,indent=2))
                if S==U==1:preserve(Y,d/'exact_goal','C2 positive-shadow body with uniform mass closed axially; numerical actual-centroid census110')
            except(ValueError,np.linalg.LinAlgError)as err:row['closure_error']=repr(err)
        history.append(row)
        if case%10==0:
            (out/'history.json').write_text(json.dumps(history,indent=2));print('C2_SHADOW_GOAL',dict(case=case,closed=closed,bestS=None if bestS==10**9 else bestS,last_gz=gz,seconds=time.time()-start),flush=True)
    (out/'history.json').write_text(json.dumps(history,indent=2));print('C2_SHADOW_FINITE_STOP',trials,closed,None if bestS==10**9 else bestS,flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('pool');p.add_argument('out');p.add_argument('--trials',type=int,default=300);p.add_argument('--seed',type=int,default=98401);a=p.parse_args();run(a.pool,a.out,a.trials,a.seed)
