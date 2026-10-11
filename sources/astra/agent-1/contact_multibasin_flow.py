"""Move all stable basins while preserving one ACTUAL unstable equilibrium.

Finite numerical research, not a certificate. The objective is the sum of
concave penalties of every positive polar persistence interval, recomputed on
the same uniformly filled contact body after each step. Extra stable roots are
allowed during the search. A complete own110 candidate is saved immediately
and still requires an independent exact audit.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,pathlib,time
import numpy as np
from scipy.optimize import linprog,minimize,LinearConstraint,Bounds
from contact_forest import ContactModel,correct
from contact_persistence_flow import normalized_volume,objective as largest_bar
from contact_retraction import retract
from merge_contact_facets import run as merge_facets
from merge_contact_vertices import run as merge_vertices

class UniqueUnstable(ContactModel):
    def __init__(self,source,merit='local'):
        super().__init__(source,1,1,merit,exempt_junior=False)
        # The S count is deliberately unrestricted. Only the physical primal
        # escape conditions below are retained as equilibrium constraints.
        self.root_counts=(1,self.F)
    def evaluate(self,z,jacobian=True):
        e=super().evaluate(z,jacobian);e['mechanical']=e['mechanical'][:len(e['X'])]
        if jacobian:e['J']=e['J'][:len(e['X'])]
        return e

class UniqueStable(ContactModel):
    def __init__(self,source,merit='local'):
        super().__init__(source,1,1,merit,exempt_junior=False)
        self.root_counts=(self.meta['V'],1)
    def evaluate(self,z,jacobian=True):
        e=super().evaluate(z,jacobian);e['mechanical']=e['mechanical'][len(e['X']):]
        if jacobian:e['J']=e['J'][len(e['X']):]
        return e

class EssentialMaxima(ContactModel):
    """Keep the two essential radial maxima strict; all extra roots may vary."""
    def __init__(self,source):
        super().__init__(source,1,1,'local',exempt_junior=False);self.root_counts=(self.meta['V'],self.F)
    def evaluate(self,z,jacobian=True):
        e=super().evaluate(z,jacobian);idx=[e['roots'][0][0],len(e['X'])+e['roots'][1][0]];e['mechanical']=e['mechanical'][idx]
        if jacobian:e['J']=e['J'][idx]
        return e

def objective(c,e,eta,derivative=True,side='Q'):
    total=0.;grad=np.zeros(c.free)
    selected=1 if side=='Q' else 0;edges=c.es if side=='Q' else c.eu
    for bar in e['bars'][selected]:
        birth=bar['birth'];u,v=edges[bar['edge']];P=e[side];a=P[u];d=P[v]-a;t=np.clip(-a@d/(d@d),0,1);f=a+t*d;h=f@f;born=P[birth]@P[birth];value=max(0.,1-h/born)
        total+=eta*np.log1p(value/eta)
        if derivative:
            D=e['D'+side];dh=2*f@((1-t)*D[u]+t*D[v]);db=2*P[birth]@D[birth];grad+=eta/(eta+value)*(-dh/born+h*db/born**2)
    return float(total),grad

def run(source,input,out,etas=(.05,.015,.004,.001,.0001),steps=100,eps=1e-7,side='Q',bar_cap=None):
    if side not in ('P','Q'):raise ValueError('Unknown physical landscape')
    Model=UniqueUnstable if side=='Q' else UniqueStable;guard='U' if side=='Q' else 'S';unconstrained='S' if side=='Q' else 'U';selected=1 if side=='Q' else 0;bestname='best-own211' if side=='Q' else 'best-own121'
    source=pathlib.Path(source);input=pathlib.Path(input);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);c=Model(source);z=np.load(input)['z'];e=c.evaluate(z);assert 17<=c.meta['E']<249 and e[guard]==1
    volume_floor=.2*normalized_volume(e)[0];history=[];initial_max=max((b['relative'] for b in e['bars'][selected]),default=0);best211=initial_max if e[unconstrained]<=2 else 1.;start=time.time();event_id=0
    if bar_cap is not None and initial_max>bar_cap+1e-12:raise ValueError('Initial physical body exceeds the explicit bar-depth cap')
    (out/'definition.json').write_text(json.dumps(dict(source=str(source.resolve()),input=str(input.resolve()),etas=list(etas),steps_per_eta=steps,epsilon=eps,bar_cap=bar_cap,guard='Only actual-centroid unique-'+guard+' conditions; other count may vary',objective='sum eta*log(1+relative_'+side+'_bar/eta)',scope='Numerical full physical body search; no exact goal claim'),indent=2))
    for phase,eta in enumerate(etas):
        trust=.025
        for it in range(steps):
            e=c.evaluate(z);value,gradient=objective(c,e,eta,side=side);nv,DV=normalized_volume(e);v=e['mechanical'];qmax=max((b['relative'] for b in e['bars'][selected]),default=0);lengths=[float(np.min(np.linalg.norm(A[ed[:,0]]-A[ed[:,1]],axis=1))/np.sqrt(np.mean(A*A))) for A,ed in [(e['X'],c.eu),(e['Y'],c.es)]]
            row=dict(phase=phase,it=it,eta=eta,S=e['S'],U=e['U'],E=c.meta['E'],objective=value,Pmax=max((b['relative'] for b in e['bars'][0]),default=0),Qmax=max((b['relative'] for b in e['bars'][1]),default=0),minimum=float(v.min()),gap=e['minimum_gap'],turn=e['minimum_turn'],lengths=lengths,trust=trust,seconds=time.time()-start,chart=str(source.resolve()));history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));np.savez(out/'latest.npz',z=z,X=e['X'],Q=e['Y']);(out/'latest-source.json').write_text(json.dumps(row,indent=2))
            if it%5==0:print('MULTIBASIN',json.dumps(row),flush=True)
            if e['S']==e['U']==1:
                np.savez(out/'POTENTIAL_OWN110.npz',z=z,X=e['X'],Q=e['Y']);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str(source.resolve()),input=str((out/'POTENTIAL_OWN110.npz').resolve())),indent=2));return
            if e[unconstrained]==2 and e[guard]==1 and qmax<best211-1e-7:
                best211=qmax;np.savez(out/(bestname+'.npz'),z=z,X=e['X'],Q=e['Y']);(out/(bestname+'.json')).write_text(json.dumps(row,indent=2))
            if min(lengths)<1e-8:
                kind='vertices' if lengths[0]<lengths[1] else 'facets';p=out/f'event{event_id:03d}-{kind}';event_id+=1;np.savez(out/'event-input.npz',z=z,X=e['X'],Q=e['Y'])
                try:(merge_vertices if kind=='vertices' else merge_facets)(source,out/'event-input.npz',p,1e-8,1 if side=='Q' else c.meta['V'],c.F if side=='Q' else 1,'balanced')
                except (ValueError,RuntimeError,AssertionError,np.linalg.LinAlgError) as error:
                    (out/'UNADMITTED_TOPOLOGY.json').write_text(json.dumps(dict(kind=kind,error=repr(error),source=str(source.resolve())),indent=2));return
                source=p/'chart';c=Model(source);z=np.load(p/'realization.npz')['z'];e=c.evaluate(z,False)
                if not 17<=c.meta['E']<249:raise ValueError('event violated edge budget')
                if e[guard]!=1 or e['mechanical'].min()<.8*eps:
                    z,e,ok=correct(c,z,p/'uniqueU-correction',steps=80,eps=eps,trust=.002,verbose=False,polish_margin=True,physical_retraction=True)
                    if not ok:return
                continue
            if e[guard]!=1:raise ValueError('actual unique-'+guard+' class lost')
            W=c.metric(e);d=c.free;bound=trust/np.sqrt(d);A=np.vstack([-e['J']@W,-e['gapJ']@W,-DV@W]);rhs=np.r_[v-eps,.8*e['gapv'],nv-volume_floor];keep=rhs<=bound*np.abs(A).sum(1)+1e-10;A=A[keep];rhs=rhs[keep];scale=np.maximum(bound*np.abs(A).sum(1),1e-12);A/=scale[:,None];rhs/=scale;gg=gradient@W
            if bar_cap is not None:
                biggest,gb=largest_bar(c,e,side);rowb=gb@W;sc=max(bound*np.abs(rowb).sum(),1e-12);A=np.vstack([A,rowb/sc]);rhs=np.r_[rhs,(bar_cap-biggest)/sc]
            lp=linprog(gg,A_ub=A,b_ub=rhs,bounds=[(-bound,bound)]*d,method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
            if not lp.success or gg@lp.x>-1e-12:
                trust*=.5
                if trust<1e-8:break
                continue
            descent=.8*(gg@lp.x);qp=minimize(lambda x:(.5*x@x,x),.8*lp.x,jac=True,method='SLSQP',bounds=Bounds(-bound,bound),constraints=[LinearConstraint(A,-np.inf,rhs),LinearConstraint(gg,-np.inf,descent)],options={'ftol':1e-13,'maxiter':90})
            if np.max(A@qp.x-rhs)>1e-8 or gg@qp.x>descent+1e-8:
                trust*=.5
                if trust<1e-8:break
                continue
            dz=W@qp.x;accepted=False
            for level in range(9):
                try:
                    zz,ee,receipt=retract(c,e,dz,2**-level)
                    if ee[guard]!=1 or ee['mechanical'].min()<.8*eps:
                        zz,ee,ok=correct(c,zz,out/f'correct-p{phase}-{it:04d}-{level}',steps=14,eps=eps,trust=.003,verbose=False,polish_margin=True,physical_retraction=True)
                        if not ok:continue
                    if ee['S']==ee['U']==1:
                        np.savez(out/'POTENTIAL_OWN110.npz',z=zz,X=ee['X'],Q=ee['Y']);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str(source.resolve()),input=str((out/'POTENTIAL_OWN110.npz').resolve())),indent=2));return
                    new=objective(c,ee,eta,False,side=side)[0];R=np.sqrt(np.mean(np.sum(ee['P']**2,axis=1)))
                    if bar_cap is not None and max((b['relative'] for b in ee['bars'][selected]),default=0)>bar_cap+1e-12:continue
                    if ee['volume']/R**3>volume_floor and ee['mechanical'].min()>.8*eps and new<value-1e-11:
                        z=zz;accepted=True;row['accepted_alpha']=2**-level;row['retraction']=receipt;break
                except (ValueError,RuntimeError,AssertionError,np.linalg.LinAlgError):continue
            if accepted and level==0:trust=min(.12,trust*1.2)
            if accepted and level>=3:trust*=.7
            if not accepted:trust*=.4
            if trust<1e-8:break

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',required=True);p.add_argument('--input',required=True);p.add_argument('--out',required=True);p.add_argument('--steps',type=int,default=100);p.add_argument('--etas',default='.05,.015,.004,.001,.0001');p.add_argument('--side',choices=['P','Q'],default='Q');p.add_argument('--bar-cap',type=float);a=p.parse_args();run(a.source,a.input,a.out,tuple(map(float,a.etas.split(','))),a.steps,side=a.side,bar_cap=a.bar_cap)
