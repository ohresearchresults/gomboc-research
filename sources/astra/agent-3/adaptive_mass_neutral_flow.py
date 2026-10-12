"""Adaptive local vertex freedoms on the actual uniform-centroid manifold.

One compensator solves three mass equations. All additional freedoms are
literal coordinates of chosen vertices. At a constrained endpoint, every
frozen vertex is tested by a fresh linear descent problem; the most useful
predicted enlargement is then tried on the real convex hull. No relaxed
graph, reference-only census or LP residual is an acceptance certificate.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from vertex_geometry import geometry
from support_geometry import escape
from persistence_birth import evaluate
from mass_neutral_vertex_flow import guards,close
from goal_nomination import preserve
from exact_audit_vertices import audit
from exact_barcode_report import report
OPT=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-10,time_limit=15.)

def linear_step(X,g,G,v,J,comp,free,trust):
    cols=np.array([3*i+k for i in free for k in range(3)]);C=-np.linalg.solve(g['Dg'][:,3*comp:3*comp+3],g['Dg'][:,cols]);D=np.zeros((X.size,len(cols)));D[cols,np.arange(len(cols))]=1;D[3*comp:3*comp+3]=C;JV=J@D;target=np.minimum(1e-8,v*.9);A=np.vstack((-JV,C,-C));b=np.r_[v-target,np.full(6,trust)];grad=G.ravel()@D
    r=linprog(grad,A_ub=A,b_ub=b,bounds=[(-trust,trust)]*len(cols),method='highs',options=OPT)
    return r,D

def run(source,out,comp,primary,stages,steps):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(source);assert len(X)<=84
    if primary<0:primary+=len(X)
    X,g=close(X,comp);free=[primary];history=[];start=time.time();np.save(out/'initial.npy',X);(out/'method.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),compensator=comp,initial_free=free,stages=stages,steps_per_stage=steps,root_policy='one U and at most two S; exempt roots may disappear',centroid_tolerance=1e-14),indent=2))
    for stage in range(stages):
        trust=.003
        for it in range(steps):
            g=geometry(X);loss,G,info=evaluate(X,.03);S=int(np.sum(escape(g['H'])[0]<0));U=int(np.sum(escape(g['Z'])[0]<0));v,J=guards(g);row=dict(stage=stage,it=it,free=free.copy(),S=S,U=U,P=info['Pmax'],Q=info['Qmax'],loss=loss,guard=float(min(v)),mass_norm=float(np.linalg.norm(g['g'])),trust=trust,seconds=time.time()-start);history.append(row);np.save(out/'latest.npy',X);(out/'history.json').write_text(json.dumps(history,indent=2))
            if it%20==0:print('ADAPTIVE_MASS_NEUTRAL',out,row,flush=True)
            if S==U==1:preserve(X,out/f'goal_stage{stage}_it{it}','own110 in adaptive mass-neutral coordinate flow');return
            assert U==1 and S<=2 and np.linalg.norm(g['g'])<1e-12
            r,D=linear_step(X,g,G,v,J,comp,free,trust)
            if not r.success:row['error']=r.message;trust*=.4
            else:
                step=(D@r.x).reshape(X.shape);ok=False
                for k in range(18):
                    try:yy,gg=close(X+2.**-k*step,comp)
                    except (ValueError,np.linalg.LinAlgError):continue
                    if len(gg['vertices'])<12:continue
                    SS=int(np.sum(escape(gg['H'])[0]<0));UU=int(np.sum(escape(gg['Z'])[0]<0))
                    if SS==UU==1:preserve(yy,out/f'goal_stage{stage}_it{it}_line{k}','own110 in adaptive mass-neutral line search')
                    if UU!=1 or not 1<=SS<=2:continue
                    vv,_=guards(gg)
                    if min(vv)<1e-12:continue
                    val,_,_=evaluate(yy,.03)
                    if val<loss-max(1e-13,abs(loss)*1e-9):X=yy;ok=True;row.update(alpha=2.**-k,predicted_change=float(r.fun));break
                if ok and k==0:trust=min(.02,trust*1.3)
                if not ok:trust*=.4
            if trust<1e-10:break
        np.save(out/f'stage{stage}_endpoint.npy',X);g=geometry(X);loss,G,info=evaluate(X,.03);v,J=guards(g);nominees=[]
        for candidate in range(len(X)):
            if candidate==comp or candidate in free:continue
            r,D=linear_step(X,g,G,v,J,comp,free+[candidate],.001)
            nominees.append(dict(vertex=candidate,success=bool(r.success),predicted_change=float(r.fun)if r.success else None,message=r.message))
        (out/f'stage{stage}_freedom_scout.json').write_text(json.dumps(nominees,indent=2));good=[r for r in nominees if r['success']]
        if not good:break
        chosen=min(good,key=lambda r:r['predicted_change']);free.append(chosen['vertex']);print('ADAPTIVE_VERTEX_FREED',out,chosen,'now',free,flush=True)
    np.save(out/'endpoint.npy',X);a=audit(out/'endpoint.npy',out/'exact_endpoint_g12',10**12);report(out/'exact_endpoint_g12');print('ADAPTIVE_MASS_NEUTRAL_EXACT_END',out,a['counts'],a['weak'],flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--compensator',type=int,required=True);p.add_argument('--primary',type=int,default=-1);p.add_argument('--stages',type=int,default=18);p.add_argument('--steps',type=int,default=180);a=p.parse_args();run(a.source,a.out,a.compensator,a.primary,a.stages,a.steps)
