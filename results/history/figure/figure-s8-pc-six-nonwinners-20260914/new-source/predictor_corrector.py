"""Finite own-COM contact-atlas continuation of a single U/H barrier.
Keep all initially positive adjacent exits positive. The projected minimum-norm
step changes the bad exit rather than flattening hundreds of positive exits.
This is numerical discovery; a sequence of successful endpoints is NOT an
interval proof that the connecting continuous path has no additional events.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from forest_repair import Atlas,paths,mechanics
from minnorm_qp import solve

def main(a):
    a.out.mkdir(parents=True,exist_ok=False);d=json.loads((a.input/'GENERATOR.json').read_text())
    fs=json.loads((a.input/'TOPOLOGY.json').read_text()) if (a.input/'TOPOLOGY.json').exists() else json.loads((a.input/'A.json').read_text())['faces']
    m=Atlas(d,fs);m.data['grid']=a.output_grid;u=m.u0.copy();um=np.zeros((len(m.owners),len(m.owners)),bool);sm=np.zeros((m.nphys,m.nphys),bool)
    for (i,j),ff in m.ef.items():um[i,j]=um[j,i]=True;sm[tuple(ff)]=sm[tuple(ff[::-1])]=True
    sf=np.full(m.nphys,a.floor);uf=np.full(len(m.owners),a.floor)
    st=m.state(u,False);m.uparent,_=paths(st['cu'],m.Uroot,um,uf);m.sparent,_=paths(st['cs'],m.Sroot,sm,sf);st=m.state(u,False)
    cfg=a.input/'CONTINUATION.json'
    if cfg.exists():
        cfg=json.loads(cfg.read_text());floors=np.array(cfg['floors']);good=np.array(cfg['good'],bool);bad=np.where(~good)[0];gain=cfg['next_gain']
    else:
        floors=np.maximum(a.floor,np.minimum(.1*st['vals'],a.floorcap));good=st['vals']>0;bad=np.where(~good)[0];gain=a.gain
    sf[m.si]=floors[:len(m.si)];uf[m.ui]=floors[len(m.si):]
    sgood=np.ones(m.nphys,bool);ugood=np.ones(len(m.owners),bool);sgood[m.si]=good[:len(m.si)];ugood[m.ui]=good[len(m.si):]
    hist=[];t0=time.monotonic()
    def dump(n,x):(a.out/n).write_text(json.dumps(x,sort_keys=True,separators=(',',':')))
    def checkpoint():
        m.save(u,a.out/'GENERATOR.json');dump('TOPOLOGY.json',fs);dump('history.json',hist)
        dump('CONTINUATION.json',dict(floors=floors.tolist(),good=good.tolist(),next_gain=gain))
    for it in range(a.steps):
        st=m.state(u,False)
        # All initially good identities must use currently positive edges.
        uallowed=um&((st['cu']>0)|(~ugood[:,None]));sallowed=sm&((st['cs']>0)|(~sgood[:,None]))
        try:
            m.uparent,_=paths(st['cu'],m.Uroot,uallowed,uf);m.sparent,_=paths(st['cs'],m.Sroot,sallowed,sf)
        except AssertionError:
            print('NO_POSITIVE_GOOD_ROUTE',it,flush=True);break
        st=m.state(u);oldbad=float(st['vals'][bad].min()) if len(bad) else 1.
        if st['vals'].min()>0 and oldbad>0:print('NUMERICAL_ALL_POSITIVE',it,flush=True);break
        goals=floors.copy();goals[bad]=np.minimum(st['vals'][bad]+gain,a.floor)
        geom=np.r_[st['dq'].reshape(-1,m.np)/2,st['dP'].reshape(-1,m.np)]
        _,ss,Vt=svd(geom,full_matrices=False,check_finite=False);select=ss>a.svd_cutoff;W=Vt[select].T/ss[select]
        vi,qi=np.where((~m.inc)&(st['gaps']<a.gapcut))
        A=np.r_[st['J'],m.gap_jac(st,vi,qi),st['ddet']]@W
        b=np.r_[goals-st['vals'],a.gapfloor-st['gaps'][vi,qi],a.tetrafloor-st['det']]
        z,rr=solve(A,b,bound=None,tol=a.qp_tolerance,seconds=a.qp_seconds,maxsteps=a.qp_steps)
        rec=dict(it=it,oldbad=oldbad,gain=gain,qp={k:v for k,v in rr.items() if k!='sec'},rank=int(select.sum()));hist.append(rec)
        accepted=False
        if z is not None:
            du=W@z
            for ls in range(a.line_steps):
                step=2.**(-ls)
                try:sn=m.state(u+step*du,False)
                except (np.linalg.LinAlgError,ValueError,FloatingPointError):continue
                un=u+step*du
                target=floors.copy();target[bad]=np.minimum(st['vals'][bad]+gain*step*.8,a.floor)
                def geometric(s):return s['gaps'][~m.inc].min()>a.gapfloor*.5 and s['det'].min()>a.tetrafloor*.5 and s['h'].min()>.02
                def violation(s):return float(np.maximum(target-s['vals'],0).sum())
                corrections=0
                if geometric(sn):
                    for corrections in range(a.correctors):
                        if np.all(sn['vals'][good]>=floors[good]*.9) and np.all(sn['vals'][bad]>=target[bad]):break
                        sn=m.state(un)
                        vi2,qi2=np.where((~m.inc)&(sn['gaps']<a.gapcut))
                        A2=np.r_[sn['J'],m.gap_jac(sn,vi2,qi2),sn['ddet']]@W
                        b2=np.r_[target-sn['vals'],a.gapfloor-sn['gaps'][vi2,qi2],a.tetrafloor-sn['det']]
                        z2,qr2=solve(A2,b2,bound=None,tol=a.qp_tolerance,seconds=a.qp_seconds,maxsteps=a.qp_steps)
                        if z2 is None:break
                        v0=violation(sn);corrected=False
                        for cl in range(12):
                            un2=un+2.**(-cl)*(W@z2)
                            try:sn2=m.state(un2,False)
                            except (np.linalg.LinAlgError,ValueError,FloatingPointError):continue
                            if geometric(sn2) and violation(sn2)<v0*(1-1e-6*2.**(-cl)):
                                un,sn=un2,sn2;corrected=True;break
                        if not corrected:break
                valid=geometric(sn) and sn['vals'][good].min()>a.good_safety*a.floor
                if valid and sn['vals'][bad].min()>oldbad+gain*step*.01:
                    u=un;accepted=True;rec['correctors']=corrections
                    rec.update(step=step,newbad=float(sn['vals'][bad].min()),mingood=float(sn['vals'][good].min()),norm=float(np.linalg.norm(z)))
                    gain=min(a.max_gain,gain*(1.3 if ls==0 else .8 if ls>2 else 1.));break
        if not accepted:gain*=.25
        checkpoint()
        if it%5==0:print(a.out.name,rec,flush=True)
        if gain<a.min_gain:print('GAIN_LIMIT',it,flush=True);break
    checkpoint();rd=json.loads((a.out/'GENERATOR.json').read_text());rm=Atlas(rd,fs);rs=rm.state(rm.u0,False)
    rep=mechanics(rs['q'],fs,P=rs['P'],tol=1e-12);dump('NUMERICAL.json',rep)
    dump('METHOD.json',{k:str(v) if isinstance(v,Path) else v for k,v in vars(a).items()})
    print('FROZEN_NUMERICAL_COUNTS',[len(rep[k]) for k in ('S','U','H')],'seconds',time.monotonic()-t0,flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('input',type=Path);p.add_argument('out',type=Path);p.add_argument('--correctors',type=int,default=8);p.add_argument('--output-grid',type=int,default=10**12);p.add_argument('--steps',type=int,default=30);p.add_argument('--gain',type=float,default=.001);p.add_argument('--max-gain',type=float,default=.002);p.add_argument('--min-gain',type=float,default=1e-10);p.add_argument('--floor',type=float,default=1e-7);p.add_argument('--floorcap',type=float,default=1e-4);p.add_argument('--gapcut',type=float,default=.03);p.add_argument('--gapfloor',type=float,default=1e-7);p.add_argument('--tetrafloor',type=float,default=1e-10);p.add_argument('--svd-cutoff',type=float,default=1e-8);p.add_argument('--qp-tolerance',type=float,default=1e-10);p.add_argument('--qp-seconds',type=float,default=4.);p.add_argument('--qp-steps',type=int,default=2500);p.add_argument('--line-steps',type=int,default=20);p.add_argument('--good-safety',type=float,default=.05);main(p.parse_args())
