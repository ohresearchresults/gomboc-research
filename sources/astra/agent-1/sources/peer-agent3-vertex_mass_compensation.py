"""Keep a new cap's reference census while closing mass with one old vertex.

The three coordinates of an existing vertex solve the three actual uniform
centroid equations. Reference S2/U1 is checked at every accepted finite step.
Only one point is added, so an input with at most83points remains under both
complexity bounds. No claim of existence follows from a failed Newton trial.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from vertex_geometry import geometry
from support_geometry import escape
from persistence_birth import evaluate
from exact_audit_vertices import audit
from exact_barcode_report import report

def reference_census(g):
    den=1+g['H']@g['g']
    if min(den)<=0:return None
    H=g['H']/den[:,None]
    return [int(np.sum(escape(H)[0]<0)),int(np.sum(escape(g['X'])[0]<0))]

def run(scout,out,number):
    scout=Path(scout);out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(scout/'centered_seed.npy');assert len(X)<=83;np.save(out/'source.npy',X)
    rows=json.loads((scout/'screen.json').read_text());selected=sorted((r for r in rows if 1<=r['reference_S']<=2),key=lambda r:r['reference_Q'])[:number];history=[];start=time.time();best=np.inf
    for row in selected:
        d=out/f"case{row['it']}";d.mkdir();base=np.vstack((X,row['point']));np.save(d/'initial.npy',base);(d/'primary.json').write_text(json.dumps(row,indent=2));baseg=geometry(base);rc=reference_census(baseg);assert rc is not None and rc[1]==1 and 1<=rc[0]<=2;trials=[];good=[]
        for index in range(len(X)):
            Y=base.copy();record=dict(compensation_vertex=index);status='finite constrained mass closure failed'
            for iteration in range(16):
                gy=geometry(Y);norm=np.linalg.norm(gy['g'])
                if norm<1e-13:status='actual uniform centroid closure numerical';break
                J=gy['Dg'][:,3*index:3*index+3]
                try:delta=-np.linalg.solve(J,gy['g'])
                except np.linalg.LinAlgError:record['error']='singular local mass derivative';break
                ok=False
                for k in range(15):
                    yy=Y.copy();yy[index]+=2.**-k*delta
                    if np.linalg.norm(yy[index]-base[index])>.05:continue
                    gg=geometry(yy,False)
                    rc=reference_census(gg)
                    if rc is None or rc[1]!=1 or not 1<=rc[0]<=2:continue
                    if np.linalg.norm(gg['g'])<norm-max(1e-15,norm*1e-5):Y=yy;ok=True;break
                if not ok:break
            finalg=geometry(Y,False)
            record.update(status=status,iterations=iteration,mass_norm=float(np.linalg.norm(finalg['g'])),moved_point=Y[index].tolist(),displacement=float(np.linalg.norm(Y[index]-base[index])))
            if status=='actual uniform centroid closure numerical':
                gg=geometry(Y,False);_,_,info=evaluate(Y,.03);S=int(np.sum(escape(gg['H'])[0]<0));U=int(np.sum(escape(gg['Z'])[0]<0));record.update(S=S,U=U,P=info['Pmax'],Q=info['Qmax'],V=len(gg['vertices']));np.save(d/f'closed_vertex{index}.npy',Y);good.append(record)
                if S==U==1:
                    aa=audit(d/f'closed_vertex{index}.npy',d/f'exact_goal_vertex{index}',10**12);report(d/f'exact_goal_vertex{index}')
                    if aa['counts']==[1,1,0]and aa['weak']==[0,0,0]and 34<=2*aa['E']<500 and aa['V']+aa['E']+aa['F']<500:
                        from goal_nomination import ExactGoalCandidateFound
                        raise ExactGoalCandidateFound('Exact Figure candidate preserved at '+str(d/f'exact_goal_vertex{index}'))
            trials.append(record)
        (d/'compensation_trials.json').write_text(json.dumps(trials,indent=2));result=dict(case=row['it'],source_Q=row['reference_Q'],successful_compensators=len(good),seconds=time.time()-start)
        if good:
            winner=min(good,key=lambda a:a['Q']);result['best']=winner
            if winner['Q']<best:
                best=winner['Q'];p=d/f"closed_vertex{winner['compensation_vertex']}.npy";aa=audit(p,d/'exact_best_g12',10**12);report(d/'exact_best_g12');result['exact']=str(d/'exact_best_g12')
        history.append(result);(out/'results.json').write_text(json.dumps(history,indent=2));print('VERTEX_MASS_COMPENSATION',result,flush=True)
    print('VERTEX_MASS_COMPENSATION_DONE',out,len(history),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('scout');p.add_argument('out');p.add_argument('--number',type=int,default=30);a=p.parse_args();run(a.scout,a.out,a.number)
