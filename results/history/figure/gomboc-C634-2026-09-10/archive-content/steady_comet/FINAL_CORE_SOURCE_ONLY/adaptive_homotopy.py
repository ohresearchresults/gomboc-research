"""Mass-aware contact choice by feasible first-order physical progress.
This is numerical discovery; acceptance here never replaces exact reconstruction/audits.
"""
from pathlib import Path
import json,time,itertools,sys,numpy as np
from scipy.optimize import linprog
from atlas_opt import Atlas,optimize
from numeric import recover,mechanics,merge_faces
from condition_events import merge_rechart

def candidate_screen(m,st,u,H,keep,limit=40):
    vals=st['vals'];J=st['J'];sel=(~m.inc)&(st['gaps']<.03);vs,ns=np.nonzero(sel);gv=st['gaps'][vs,ns];G=-(np.einsum('ijk,ij->ik',st['dP'][vs],st['q'][ns])+np.einsum('ij,ijk->ik',st['P'][vs],st['dq'][ns]));A=np.vstack([-J,-G]);b=np.r_[vals-keep*2,gv-1e-11];scale=np.maximum(np.linalg.norm(A,axis=1),1e-3);A/=scale[:,None];b/=scale;rank=[]
    for (a,bv),pol in m.ef.items():
        if tuple(sorted(pol)) in H or m.Uroot in (a,bv):continue
        try:merge_faces(m.faces,a,bv)
        except Exception:continue
        ts=[(v,j) for v,w in ((a,bv),(bv,a)) for j in set(m.owners[w])-set(m.owners[v])]
        if not ts:continue
        tg=min(ts,key=lambda p:st['gaps'][p]/np.linalg.norm(st['q'][p[1]]));rank.append((np.linalg.norm(st['P'][a]-st['P'][bv]),a,bv,tg,pol))
    rank.sort();scored=[]
    for rank0,(length,a,bv,tg,pol) in enumerate(rank[:limit]):
        v,j=tg;gradient=-(np.einsum('jk,j->k',st['dP'][v],st['q'][j])+np.einsum('j,jk->k',st['P'][v],st['dq'][j]));gap=st['gaps'][tg];objective=gradient/max(gap,1e-8)
        lp=linprog(objective,A_ub=A,b_ub=b,bounds=[(-.0005,.0005)]*m.np,method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9,'time_limit':3.0})
        if not lp.success:continue
        direction=lp.x
        for ls in range(18):
            nu=u+2.**(-ls)*direction
            try:new=m.state(nu,False)
            except Exception:continue
            if new['gaps'][~m.inc].min()>-1e-11 and new['vals'].min()>keep*1.1 and new['det'].min()>0 and new['h'].min()>0:
                gain=(gap-new['gaps'][tg])/gap
                if gain>0:scored.append((float(gain),rank0,a,bv,tg,pol,nu))
                break
    scored.sort(key=lambda p:(-p[0],p[1]));return scored

def run(startgen,startfaces,outdir,epochs=24):
    R=Path(__file__).parent;out=Path(outdir);out.mkdir(exist_ok=True,parents=True);g=json.loads(Path(startgen).read_text());fs=json.loads(Path(startfaces).read_text());H=set(tuple(map(int,l.split())) for l in (R/'H213_edges.txt').read_text().splitlines());t0=time.time();ledger=[]
    for epoch in range(epochs):
        m=Atlas(g,fs);E=len(m.ef);m.checkpoint=out/f'CURRENT_E{E}_EPOCH{epoch}';(out/f'CURRENT_E{E}_EPOCH{epoch}_faces.json').write_text(json.dumps(fs,separators=(',',':')));st=m.state(m.u0);assert st['vals'].min()>0
        print('ADAPTIVE_EPOCH',epoch,E,'mincos',st['vals'].min(),'elapsed',round(time.time()-t0,2),flush=True)
        if E<=249:print('ADAPTIVE_NUMERIC_E249',flush=True);return
        u=m.u0
        if st['vals'].min()<2.8e-5:
            u,st,status=optimize(m,u=u,steps=220,trust=.0003,keep=1e-6,goal=3e-5)
            print('ADAPTIVE_CONDITION',status,'mincos',st['vals'].min(),'gap',st['gaps'][~m.inc].min(),flush=True)
            z=m.save(u,out/f'E{E}_CONDITIONED_GENERATOR.json');(out/f'E{E}_CONDITIONED_faces.json').write_text(json.dumps(fs,separators=(',',':')))
        keep=max(5e-7,min(1e-5,st['vals'].min()*.28));candidates=candidate_screen(m,st,u,H,keep);print('ADAPTIVE_SCREEN',[(p[:6]) for p in candidates[:12]],flush=True);success=False
        for ri,(gain,oldrank,a,b,tg,pol,seed) in enumerate(candidates[:5]):
            m.checkpoint=out/f'CURRENT_E{E}_EPOCH{epoch}_TRY{ri}';print('ADAPTIVE_TARGET',ri,a,b,pol,tg,'screen_gain',gain,'keep',keep,flush=True)
            u,new,status=optimize(m,u=seed,steps=420,target=tg,trust=.0001,keep=keep,goal=.001,stopgap=8e-10)
            prefix=f'E{E}_EPOCH{epoch}_TRY{ri}_{a}_{b}';z=m.save(u,out/(prefix+'_GENERATOR.json'));(out/(prefix+'_faces.json')).write_text(json.dumps(fs,separators=(',',':')));row=dict(E=E,epoch=epoch,target=[int(x) for x in tg],edge=[a,b],polar=pol,status=status,remaining_gap=float(new['gaps'][tg]),minimum_escape=float(new['vals'].min()));ledger.append(row);(out/'LEDGER.json').write_text(json.dumps(ledger,indent=2));print('ADAPTIVE_TARGET_END',row,flush=True)
            nearest=sorted((np.linalg.norm(new['P'][v]-new['P'][w]),v,w) for v,w in m.ef)
            for dist,v,w in nearest[:10]:
                if dist>.002 or tuple(sorted(m.ef[v,w])) in H:continue
                for grid in [10**12,10**14]:
                    try:
                        zg=json.loads(json.dumps(z));zg['controls']=[[int(round(float(t/z['grid'])*grid)) for t in cr] for cr in z['controls']];zg['grid']=grid
                        zz,ff,depth=merge_rechart(zg,fs,v,w,controls=new['X']);audit=mechanics(recover(zz)[:137],ff,tol=1e-11);print('ADAPTIVE_MERGE',v,w,m.ef[v,w],dist,grid,depth,audit,flush=True)
                        if audit['counts']==[1,1,0] and audit['min_gap']>1e-9 and audit['max_incidence_error']<1e-8 and min(audit['polar_escape_min'],audit['primal_escape_min'])>2e-7:
                            tag=f'C{2*audit["E"]}_ADAPTIVE_{epoch}_{v}_{w}';(out/(tag+'_GENERATOR.json')).write_text(json.dumps(zz,sort_keys=True,separators=(',',':')));(out/(tag+'_faces.json')).write_text(json.dumps(ff,separators=(',',':')));(out/(tag+'_numeric.json')).write_text(json.dumps(dict(removed_polar=m.ef[v,w],**audit),indent=2));g=zz;fs=ff;success=True;(out/'LATEST_GENERATOR.json').write_text(json.dumps(g,sort_keys=True,separators=(',',':')));(out/'LATEST_faces.json').write_text(json.dumps(fs,separators=(',',':')));print('ADAPTIVE_NUMERIC_WINNER',tag,flush=True);break
                    except Exception as exc:print('ADAPTIVE_MERGE_ERROR',v,w,grid,repr(exc),flush=True)
                if success:break
            if success:break
        if not success:print('ADAPTIVE_STOP_NO_NEXT',flush=True);return
    print('ADAPTIVE_EPOCH_BUDGET',flush=True)

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('generator');p.add_argument('faces');p.add_argument('outdir');p.add_argument('--epochs',type=int,default=24);a=p.parse_args();run(a.generator,a.faces,a.outdir,a.epochs)
