"""New primal vertices in an outward Thales-ball slice of the unwanted facet.

Each added point is beyond the nominated stable facet and strictly inside the
ball with diameter [0,parent]. Thus it has a positive reference escape chord.
The new solid's mass is then closed to zero in the physical Thales chart.
Only a complete own-centroid audit may establish the requested Figure.
"""
import argparse,json,time,hashlib
from pathlib import Path
import numpy as np
from vertex_geometry import geometry
from support_geometry import escape
from persistence_birth import evaluate as all_persistence,bars_loss
from section_polish import roots
from primal_log_thales import Chart,evaluate
from constrained_mass_projection import project
from thales_mass_close import run as gradual_close
from exact_audit_vertices import audit
from exact_barcode_report import report

def run(source,out,trials,seed,scout_only=False):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);loaded=Path(source).read_bytes();(out/'source.npy').write_bytes(loaded);X=np.load(out/'source.npy');g=geometry(X,False);X=g['Z'][g['vertices']];X/=np.max(np.linalg.norm(X,axis=1));assert len(X)<=83 and np.sum(escape(X)[0]<0)==1;g=geometry(X,False);T=g['T'];owners={}
    for f,t in enumerate(T):
        for i,j in zip(t,np.roll(t,-1)):owners.setdefault(tuple(sorted((int(i),int(j)))),[]).append(f)
    qe=np.array(list(owners.values()));junior=roots(g['H'],qe,2)[1];h=1/np.linalg.norm(g['H'][junior]);normal=g['H'][junior]*h;foot=normal*h;b=np.eye(3)[np.argmin(abs(normal))];b-=normal*(b@normal);b/=np.linalg.norm(b);B=np.column_stack((b,np.cross(normal,b)));caps=(X@normal+np.linalg.norm(X,axis=1))/2-h;parents=np.flatnonzero(caps>1e-8);assert len(parents)>0
    np.save(out/'centered_seed.npy',X);(out/'definition.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),source_sha256=hashlib.sha256(loaded).hexdigest(),junior_facet=int(junior),facet_vertices=T[junior].tolist(),normal=normal.tolist(),offset=h,parent_candidates=parents.tolist(),seed=seed,formula='ball(parent/2,norm(parent)/2) intersect outward plane slice n.x=h+height; then literal convex hull and actual uniform mass closure'),indent=2));rng=np.random.default_rng(seed);rows=[];best={};start=time.time()
    for it in range(trials):
        parent=int(rng.choice(parents));v=X[parent];height=caps[parent]*np.exp(rng.uniform(np.log(1e-5),np.log(.95)));delta=h+height-normal@v/2;radius=np.sqrt((v@v)/4-delta**2);theta=rng.uniform(0,2*np.pi);r=radius*np.sqrt(rng.random())*.98;point=v/2+normal*delta+B@np.array([r*np.cos(theta),r*np.sin(theta)]);assert point@normal>h and point@(v-point)>0
        Y=np.vstack((X,point));assert np.sum(escape(Y)[0]<0)==1;loss,_,inf=all_persistence(Y,.03);gy=geometry(Y,False);Href=gy['H']/(1+gy['H']@gy['g'])[:,None];oy={}
        for f,tri in enumerate(gy['T']):
            for i,j in zip(tri,np.roll(tri,-1)):oy.setdefault(tuple(sorted((int(i),int(j)))),[]).append(f)
        refQ=bars_loss(Href,np.array(list(oy.values())),.03)[2];row=dict(it=it,parent=parent,height=float(height),point=point.tolist(),P=inf['Pmax'],Q=inf['Qmax'],loss=loss,reference_U=1,reference_S=int(np.sum(escape(Href)[0]<0)),reference_Q=max(refQ,default=0.));rows.append(row)
        if row['reference_Q']<best.get('reference',dict(reference_Q=np.inf))['reference_Q']:best['reference']=row
        if row['reference_S']==1:
            np.save(out/f'reference110_candidate{it}.npy',Y);(out/f'reference110_candidate{it}.json').write_text(json.dumps(row,indent=2));print('THALES_CAP_REFERENCE110_ONLY',out,row,flush=True)
        for lim in [1e-10,1e-7,1e-5,.001,.01,1.]:
            if row['P']>lim:continue
            key=f'P{lim:g}'
            if row['Q']<best.get(key,dict(Q=np.inf))['Q']:best[key]=row
    (out/'screen.json').write_text(json.dumps(rows,indent=2));(out/'best.json').write_text(json.dumps(best,indent=2));print('THALES_CAP_SCREEN',out,{k:(v['P'],v['Q'])for k,v in best.items()},flush=True)
    if scout_only:return
    selected=[]
    for row in list(best.values())+sorted(rows,key=lambda r:r['loss'])[:8]:
        if row['it']not in [r['it']for r in selected]:selected.append(row)
    history=[]
    for row in selected:
        d=out/f"case{row['it']}";d.mkdir();Y=np.vstack((X,row['point']));np.save(d/'reference.npy',Y);(d/'nomination.json').write_text(json.dumps(row,indent=2));rec=dict(case=row['it'],initial=row)
        try:
            c=Chart(Y);z,e=project(c,c.z0.copy(),.03);np.save(d/'closed.npy',e['X']);rec['closure']='direct constrained physical mass projection'
        except (ValueError,AssertionError,np.linalg.LinAlgError)as err:
            rec['direct_closure_error']=repr(err);gradual_close(d/'reference.npy',d/'gradual_closure',150,.8)
            if (d/'gradual_closure/closed.npy').exists():
                Y=np.load(d/'gradual_closure/closed.npy');np.save(d/'closed.npy',Y);rec['closure']='gradual physical centroid descent then exact-mass-tolerance correction'
        if (d/'closed.npy').exists():
            Y=np.load(d/'closed.npy');gg=geometry(Y,False);_,_,inf=all_persistence(Y,.03);S=int(np.sum(escape(gg['H'])[0]<0));U=int(np.sum(escape(gg['Z'])[0]<0));rec.update(S=S,U=U,P=inf['Pmax'],Q=inf['Qmax'],mass_norm=float(np.linalg.norm(gg['g'])),V=len(gg['vertices']))
            if S==U==1:
                aa=audit(d/'closed.npy',d/'exact_goal_nomination_g12',10**12);report(d/'exact_goal_nomination_g12');rec.update(exact_counts=aa['counts'],exact_weak=aa['weak'])
        else:rec['closure']='finite physical mass closure failed'
        rec['seconds']=time.time()-start;history.append(rec);(out/'trials.json').write_text(json.dumps(history,indent=2));print('THALES_CAP_CLOSED',out,rec,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--trials',type=int,default=4000);p.add_argument('--seed',type=int,default=82701);p.add_argument('--scout-only',action='store_true');a=p.parse_args();run(a.source,a.out,a.trials,a.seed,a.scout_only)
