"""Move an added cap while one old vertex compensates its actual mass.

The three-coordinate tangent satisfies Dg_primary + Dg_comp * J = 0.
The compensator is then corrected by full nonlinear hull integration. Stable
and unstable root exemptions permit the unwanted stable root to disappear.
All other guards, the filled centroid and the new complete hull are checked.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from vertex_geometry import geometry
from support_geometry import escape
from section_polish import roots
from persistence_birth import evaluate
from goal_nomination import preserve
from exact_audit_vertices import audit
from exact_barcode_report import report

def guards(g):
    owners={}
    for f,t in enumerate(g['T']):
        for i,j in zip(t,np.roll(t,-1)):owners.setdefault(tuple(sorted((int(i),int(j)))),[]).append(f)
    rr=[int(np.argmax(np.sum(g['Z']**2,axis=1)))];ss=roots(g['H'],np.array(list(owners.values())),2);vv=[];JJ=[]
    for A,DA,r in [(g['Z'],g['DZ'],rr),(g['H'],g['DH'],ss)]:
        v,w,J=escape(A,DA,angular=True);mask=np.ones(len(A),bool);mask[r]=False;vv.append(v[mask]);JJ.append(J[mask])
    return np.r_[tuple(vv)],np.vstack(JJ)

def close(Y,comp):
    Y=Y.copy()
    for it in range(15):
        g=geometry(Y);norm=np.linalg.norm(g['g'])
        if norm<1e-14:return Y,g
        J=g['Dg'][:,3*comp:3*comp+3];step=-np.linalg.solve(J,g['g']);ok=False
        for k in range(15):
            yy=Y.copy();yy[comp]+=2.**-k*step;gg=geometry(yy,False)
            if np.linalg.norm(gg['g'])<norm*(1-1e-5):Y=yy;ok=True;break
        if not ok:raise ValueError('single-vertex nonlinear mass correction stalled')
    raise ValueError('single-vertex nonlinear mass correction exceeded15steps')

def run(source,out,comp,primary,steps):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(source);assert len(X)<=84
    if primary<0:primary+=len(X)
    assert primary!=comp;X,g=close(X,comp);np.save(out/'initial.npy',X);(out/'method.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),primary=primary,compensator=comp,centroid_tolerance=1e-14,epsilon=1e-9),indent=2));history=[];start=time.time();trust=.005
    for it in range(steps):
        g=geometry(X);loss,G,info=evaluate(X,.03);S=int(np.sum(escape(g['H'])[0]<0));U=int(np.sum(escape(g['Z'])[0]<0));v,J=guards(g);row=dict(it=it,loss=loss,P=info['Pmax'],Q=info['Qmax'],S=S,U=U,guard=float(min(v)),mass_norm=float(np.linalg.norm(g['g'])),V=len(g['vertices']),trust=trust,seconds=time.time()-start);history.append(row);np.save(out/'latest.npy',X);(out/'history.json').write_text(json.dumps(history,indent=2))
        if it%10==0:print('MASS_NEUTRAL_VERTEX_FLOW',out,row,flush=True)
        if S==U==1:preserve(X,out/f'exact_goal_nomination{it}','own110 in compensated primary-cap flow');return
        assert U==1 and S<=2 and np.linalg.norm(g['g'])<1e-12
        C=-np.linalg.solve(g['Dg'][:,3*comp:3*comp+3],g['Dg'][:,3*primary:3*primary+3]);D=np.zeros((X.size,3));D[3*primary:3*primary+3]=np.eye(3);D[3*comp:3*comp+3]=C;JV=J@D;target=np.minimum(1e-9,v*.9);A=np.vstack((-JV,C,-C));b=np.r_[v-target,np.full(6,trust)];r=linprog(G.ravel()@D,A_ub=A,b_ub=b,bounds=[(-trust,trust)]*3,method='highs',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-10,time_limit=15.))
        if not r.success:row['error']=r.message;trust*=.4
        else:
            step=(D@r.x).reshape(X.shape);ok=False
            for k in range(18):
                try:yy,gg=close(X+2.**-k*step,comp)
                except (ValueError,np.linalg.LinAlgError):continue
                SS=int(np.sum(escape(gg['H'])[0]<0));UU=int(np.sum(escape(gg['Z'])[0]<0))
                if SS==UU==1:preserve(yy,out/f'exact_goal_nomination{it}_line{k}','own110 in compensated primary-cap line search')
                if UU!=1 or not 1<=SS<=2:continue
                vv,_=guards(gg)
                if min(vv)<1e-10:continue
                new,_,_=evaluate(yy,.03)
                if new<loss-max(1e-13,abs(loss)*1e-9):X=yy;ok=True;row['alpha']=2.**-k
                if ok:
                    if k==0:trust=min(.05,trust*1.2)
                    break
            if not ok:trust*=.4
        if trust<1e-10:break
    a=audit(out/'latest.npy',out/'exact_endpoint_g12',10**12);report(out/'exact_endpoint_g12');print('MASS_NEUTRAL_VERTEX_FLOW_EXACT_END',out,a['counts'],a['weak'],flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--compensator',type=int,required=True);p.add_argument('--primary',type=int,default=-1);p.add_argument('--steps',type=int,default=1000);a=p.parse_args();run(a.source,a.out,a.compensator,a.primary,a.steps)
