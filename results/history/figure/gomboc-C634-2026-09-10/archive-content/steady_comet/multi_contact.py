"""Full filled-centroid contact flow minimizing several true edge lengths at once.
This is numerical discovery, not an exact assertion. All endpoints must be replayed.
"""
from pathlib import Path
import json,time,sys,numpy as np
from scipy.optimize import linprog
from atlas_opt import Atlas,optimize
from numeric import mechanics,recover,merge_faces
from condition_events import merge_rechart

def flow(m,u,selected,steps=420,keep=8e-6,trust=1e-4):
    st=m.state(u);aa=np.array([e[0] for e in selected]);bb=np.array([e[1] for e in selected]);init=np.linalg.norm(st['P'][aa]-st['P'][bb],axis=1);weight=1/np.maximum(init,.001)
    def objective(t,jac=False):
        d=t['P'][aa]-t['P'][bb];ell=np.linalg.norm(d,axis=1);value=float(weight@ell)
        if not jac:return value
        grad=np.einsum('i,ic,icp->p',weight/ell,d,t['dP'][aa]-t['dP'][bb]);return value,grad
    t0=time.time();best=u.copy();bestv=objective(st)
    for it in range(steps):
        st=m.state(u);value,obj=objective(st,True);gmin=st['gaps'][~m.inc].min();vmin=st['vals'].min()
        if value<bestv:bestv=value;best=u.copy()
        if it%25==0:m.save(u,Path(m.checkpoint).with_suffix('.json'));np.savez(Path(m.checkpoint).with_suffix('.npz'),u=u,X=st['X'],P=st['P'],q=st['q'],c=st['c'],vals=st['vals'])
        if it%5==0:print('MULTI_ITER',it,'secs',round(time.time()-t0,2),'value',value,'mincos',vmin,'gap',gmin,'trust',trust,flush=True)
        if gmin<2e-8 and vmin>keep*.9:return u,st,'contact'
        sel=(~m.inc)&(st['gaps']<max(.03,trust*100));vi,qi=np.nonzero(sel);G=m.gap_jac(st,vi,qi);A=np.vstack([-st['J'],-G]);b=np.r_[st['vals']-keep,st['gaps'][vi,qi]-1e-12];scale=np.maximum(np.linalg.norm(A,axis=1),1e-3);obj=obj/max(np.linalg.norm(obj),1e-20)
        lp=linprog(obj,A_ub=A/scale[:,None],b_ub=b/scale,bounds=[(-trust,trust)]*m.np,method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9,'time_limit':4.0})
        if not lp.success:
            print('MULTI_LP_FAIL',it,lp.message,flush=True);trust*=.5
            if trust<1e-9:return best,m.state(best),'LP_stall'
            continue
        du=lp.x;accepted=False
        for ls in range(24):
            lam=2.**(-ls)
            try:new=m.state(u+lam*du,False)
            except Exception:continue
            if new['gaps'][~m.inc].min()>-1e-11 and new['det'].min()>-1e-12 and new['h'].min()>0 and new['vals'].min()>keep*.99 and objective(new)<value-1e-10:
                u=u+lam*du;accepted=True
                if ls<=1:trust=min(trust*1.3,.003)
                elif ls>=3:trust=max(trust*.6,1e-9)
                break
        if not accepted:
            trust*=.4
            if trust<1e-9:return best,m.state(best),'line_stall'
    return best,m.state(best),'budget'

def run(gfile,ffile,outdir,epochs=30):
    R=Path(__file__).parent;out=Path(outdir);out.mkdir(exist_ok=True,parents=True);g=json.loads(Path(gfile).read_text());fs=json.loads(Path(ffile).read_text());H={tuple(map(int,l.split())) for l in (R/'H213_edges.txt').read_text().splitlines()};ledger=[]
    for epoch in range(epochs):
        m=Atlas(g,fs);E=len(m.ef);u=m.u0;st=m.state(u);m.checkpoint=out/f'CURRENT_E{E}_EPOCH{epoch}';(out/f'CURRENT_E{E}_EPOCH{epoch}_faces.json').write_text(json.dumps(fs,separators=(',',':')));print('MULTI_EPOCH',epoch,E,st['vals'].min(),flush=True)
        if E<=249:return
        if st['vals'].min()<2.8e-5:
            u,st,status=optimize(m,u=u,steps=200,trust=.0003,keep=1e-6,goal=3e-5);print('MULTI_CONDITION',status,st['vals'].min(),flush=True)
        rank=[]
        for (a,b),pol in m.ef.items():
            if tuple(sorted(pol)) in H or m.Uroot in (a,b):continue
            try:merge_faces(fs,a,b)
            except Exception:continue
            rank.append((np.linalg.norm(st['P'][a]-st['P'][b]),a,b))
        rank.sort();selected=[(a,b) for _,a,b in rank[:16]];print('MULTI_SELECTED',[(a,b,m.ef[a,b]) for a,b in selected],flush=True);keep=max(5e-7,min(8e-6,.28*st['vals'].min()));u,st,status=flow(m,u,selected,steps=500,keep=keep);gcur=m.save(u,out/f'E{E}_FLOW_GENERATOR.json');print('MULTI_DONE',status,st['vals'].min(),st['gaps'][~m.inc].min(),flush=True)
        nearest=sorted((np.linalg.norm(st['P'][a]-st['P'][b]),a,b) for a,b in m.ef);success=False
        for dist,a,b in nearest[:12]:
            if dist>.002 or tuple(sorted(m.ef[a,b])) in H:continue
            try:
                zz,ff,depth=merge_rechart(gcur,fs,a,b,controls=st['X']);audit=mechanics(recover(zz)[:137],ff,tol=1e-11);print('MULTI_MERGE',a,b,m.ef[a,b],dist,audit,flush=True)
                if audit['counts']!=[1,1,0] or audit['min_gap']<1e-9 or audit['max_incidence_error']>1e-8 or min(audit['primal_escape_min'],audit['polar_escape_min'])<2e-7:continue
                tag=f'C{2*audit["E"]}_MULTI_{epoch}_{a}_{b}';(out/(tag+'_GENERATOR.json')).write_text(json.dumps(zz,sort_keys=True,separators=(',',':')));(out/(tag+'_faces.json')).write_text(json.dumps(ff,separators=(',',':')));(out/(tag+'_numeric.json')).write_text(json.dumps(audit,indent=2));g=zz;fs=ff;row=dict(tag=tag,oldE=E,removed_polar=m.ef[a,b],**audit);ledger.append(row);(out/'LEDGER.json').write_text(json.dumps(ledger,indent=2));(out/'LATEST_GENERATOR.json').write_text(json.dumps(g,sort_keys=True,separators=(',',':')));(out/'LATEST_faces.json').write_text(json.dumps(fs,separators=(',',':')));print('MULTI_NUMERIC_WINNER',tag,flush=True);success=True;break
            except Exception as e:print('MULTI_ERROR',repr(e),flush=True)
        if not success:print('MULTI_STOP_NO_EVENT',flush=True);return

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('generator');p.add_argument('faces');p.add_argument('outdir');p.add_argument('--epochs',type=int,default=30);a=p.parse_args();run(a.generator,a.faces,a.outdir,a.epochs)
