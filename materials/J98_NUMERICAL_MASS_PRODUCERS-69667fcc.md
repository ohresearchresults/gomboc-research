# material-69667fcc4fde

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# J98 complete numerical physical-mass and capacity producers

Complete dependencies: numerical cover producers [internal-source-reference], literal R82 input in [internal-source-reference], and CAPEXACT98_INPUT.json in [internal-source-reference]. The separately stored NUMERICAL98_GEOMETRIES.json freezes every serialized endpoint, so reconstruction need not rerun optimizers. That exact checkpoint is required by replay_geometry98.py below. The exact mass-capacity proof does NOT depend on these numerical solvers; use its own literal core/capacity/release/repair materials instead.

Observed Python3.13.5, NumPy2.3.5, SciPy1.17.0; OPENBLAS_NUM_THREADS=1. Run after the numerical cover workflow: `python masscover98.py`, `python capacity98.py`, `python twostepmass98.py`, `python elderrelease98.py`, `python dualcapacity98.py`. To recover stored endpoint hulls directly instead: `python replay_geometry98.py`; expected marker `J98_FROZEN_GEOMETRY_REPLAY_FINISHED_NOT_EXACT 34 18`. Eighteen records are failed nomination policies with no serialized endpoint, not missing successful constructions. Every actual trial integrates the filled global convex hull, never a sum of overlapping independent pyramids.

## Evidence scope and executed work

The distributed one-step mass sweep completed ten optimization states, then was stopped during the fifth-controller solve at scale.5. Its source contains the complete larger sweep, but no completion marker or last two states is claimed. The recorded one-step endpoints did not restore the old centroid; local optimizer failure alone is not an exclusion. The exact global one-step capacity inequalities were developed to replace that weak inference. The two-step sweep completed all five chain counts1--5, reduced moment residual approximately.13544 to.10981, and increased E from239 to274. It also did not close mass; finite failure is not a two-step family exclusion. All points, ordered chain pairs, old witnesses and solver parameters needed to continue these nonwinners are in the frozen checkpoint plus these complete producers.

The fixed-direction elder-height scan alone changed from a positive to a negative capacity gap near height.62--.6338; a negative value in one direction is inconclusive. Optimizing the separating direction recovered a positive numerical gap about.0039508 at ceiling.6338 and .0001056 at ceiling.70. The .6339 version was subsequently certified exactly in J98_EXACT_ELDER_RELEASE_CAPACITY plus its mandatory input repair. Without any elder ceiling the numerical optimizer returned the zero-direction floor, which is NOT a proof of moment or convex-body feasibility. All numerical census limitations from geom98.py still apply.

Source manifest:
masscover98.py4053B SHA49cf3b2ca0c1373376332ca1b71fc83fdb6a017e895d0a5fcd3213f510f03eda;
capacity98.py2161B SHAa5fd2f3a83350dfd65c2a524b6454580770aa4bbff8e5f9bf79ce95106d880f4;
twostepmass98.py3649B SHA7ff0c222b0800503fc765a8f3e2b34a10433060cd28235ffdaa67182132e09ff;
dualcapacity98.py2113B SHA64d5f99dd3c6a12f7460a84532ecdced4fae7eef941bcecf21309c4920a85047;
elderrelease98.py1307B SHA40e07e12d87279786fcacf7ff1d6f2aacc1202dbbae2b983b387ed5fc51bd807;
replay_geometry98.py2006B SHA2cb3bc5fd5481b591ec0354e2f6b06562fc39e4c31510f8e9e2e8c6b2dab08e4.

Recorded generated output manifest (not substitute recovery inputs; numerical optimizer reproductions can differ across libraries):
COVER98_DIAGNOSTICS.json2308B SHA76395c12abb95c770834950267b2a8f15ca3fab43570f2c3c2efe87fea9135bc;
DOUBLECOVER98_RESULTS.json56762B SHA36ae551de7923b5d6239a2b3cd0b10ae203e682ca1b725d41f4a397fbed8b953;
REFINED_COVER98_RESULTS.json53111B SHAb62b2faa7c204793177f30fbc0c53e82382a5026a4f22b652846c39acdd357e9;
GREEDY_COVER98_RESULTS.json128106B SHAb4d67e6b7f065ab6cd16d0354b1039a5a2ec17d3903c53fbf9a09868ec6b7adb;
MASSCOVER98_RESULTS.json151531B SHAfba790b0d07dca3cea19a862bf4447ea017768b6468a5addbea94e2582647c26 (ten completed states only);
CAPACITY98_RESULTS.json8764B SHA46830f3ce70624eb5b8b64917f116e5d3a9296e772f3ac2c5d6591208ce1a992;
TWOSTEPMASS98_RESULTS.json75890B SHA0e0344c3a038bcd6e03016d45443afa2e5ddeaeb832da83b7193e6af4fc95ee5;
DUALCAPACITY98_RESULTS.json25860B SHA19e4af4dccf6bac48b64e3515a8cf48ecba3fa63407b277b6ca809bea9889a26;
ELDER_RELEASE98_CAPACITY.json2211B SHA0191baf7334b411fe2caa721a07484e8dbddf3c9dd034113877b8ba05fe3ec0a;
NUMERICAL98_REPLAY.json449051B SHA71d1eb42c24d92cd715f4badfe458cc1641f12285df5435498da1a3d53cb5b88.

### FILE masscover98.py
```python
"""Distributed finite U-safe mass compensation after old-junior component cover.
All trial masses are recomputed on the actual hull. Numerical nomination only.
"""
from pathlib import Path
import json
import numpy as np
from scipy.optimize import minimize
from scipy.spatial import ConvexHull
from geom98 import load_r82,mass,hull_v,numerical_summary
from cover98 import fibonacci_sphere
from greedycover98 import witness_extremum
from refinecover98 import setup,holes

def quick_mass(v):
    h=ConvexHull(v);t=h.simplices.copy()
    a,b,c=np.moveaxis(v[t],1,0);d=np.einsum('ij,ij->i',np.cross(b-a,c-a),h.equations[:,:3]);bad=d<0
    tmp=t[bad,1].copy();t[bad,1]=t[bad,2];t[bad,2]=tmp
    return mass(v,t)

def objective_controls(flat,fixed,g0):
    ap=flat.reshape(-1,3)
    try:V,g=quick_mass(np.r_[fixed,ap+g0]);return V,g
    except Exception:return None,None

def main():
    root=Path(__file__).parent;b=load_r82();g0=b['g'];p=b['v']-g0;elder=b['equations'][18,:3];he=-b['equations'][18,3]-elder@g0
    source=json.loads((root/'GREEDY_COVER98_RESULTS.json').read_text());primary=next(z for z in source if z['t']==.35 and z['extra']==.02)
    base=np.r_[b['v'],np.array(primary['apices_centered'])+g0];vol,gg=quick_mass(base);M0=(gg-g0)*vol
    directions=fibonacci_sphere(800)
    cand=[]
    for n in directions:
        a,w=witness_extremum(p,n,.49,shrink=1e-4)
        if elder@a>=he-1e-4:continue
        cand.append((a,w))
    states=[]
    for scale in [1.,.75,.5]:
        fixed=base.copy();controls=[];witnesses=[];greedytrace=[]
        for step in range(6):
            trials=[]
            for a,w in cand:
                # Scaling toward the witness preserves its convex witness ball.
                aa=p[w]+scale*(a-p[w]);V,g=quick_mass(np.r_[fixed,[aa+g0]])
                trials.append((float(np.linalg.norm(V*(g-g0))),w,aa,V,g))
            trials.sort(key=lambda z:z[0]);best=trials[0];_,w,a,V,g=best
            controls.append(a);witnesses.append(w);fixed=np.r_[fixed,[a+g0]]
            greedytrace.append({'step':step,'witness':w,'moment_norm':best[0],'centroid_shift':(g-g0).tolist()})
            print('GREEDY',scale,step,w,best[0],flush=True)
            if step<2:continue
            k=len(controls);ws=np.array(witnesses);cent=p[ws]/2;rr=(p[ws]*p[ws]).sum(axis=1)/4-1e-8
            def fun(x):
                V,g=objective_controls(x,base,g0)
                if V is None:return 1e3
                return float((V*(g-g0))@(V*(g-g0)))
            def balls(x):return rr-((x.reshape(k,3)-cent)**2).sum(axis=1)
            def eldercons(x):return he-1e-5-x.reshape(k,3)@elder
            op=minimize(fun,np.array(controls).ravel(),method='SLSQP',constraints=[{'type':'ineq','fun':balls},{'type':'ineq','fun':eldercons}],
                options={'maxiter':250,'ftol':1e-22,'eps':1e-7})
            ap=op.x.reshape(k,3);V,g=objective_controls(op.x,base,g0);bod=hull_v(np.r_[base,ap+g0]);ref=numerical_summary(bod,center=g0);own=numerical_summary(bod)
            z={'primary_t':.35,'primary_extra':.02,'scale':scale,'controls_count':k,'witnesses':witnesses.copy(),'controls_centered':ap.tolist(),
               'initial_controls_centered':np.array(controls).tolist(),'solver_success':bool(op.success),'solver_message':str(op.message),
               'solver_iterations':int(op.nit),'min_ball_margin':float(min(balls(op.x))),'min_elder_margin':float(min(eldercons(op.x))),
               'moment_residual_norm':float(np.linalg.norm(V*(g-g0))),'centroid_shift':(g-g0).tolist(),'volume_increment':V-b['volume'],
               'reference':ref,'own':own,'greedy_trace':greedytrace.copy()}
            states.append(z);(root/'MASSCOVER98_RESULTS.json').write_text(json.dumps(states,indent=2)+'\n')
            print('SOLVE',scale,k,op.success,z['moment_residual_norm'],'E',ref['E'],'refSU',len(ref['S']),len(ref['U']),'ownSU',len(own['S']),len(own['U']),flush=True)
            if z['moment_residual_norm']<1e-6:break
    print('J98_DISTRIBUTED_MASS_COVER_NOMINATIONS_FINISHED_NOT_EXACT')
if __name__=='__main__':main()
```
### FILE capacity98.py
```python
"""One-step witness-envelope directional mass-capacity relaxation.
Numerical outer bounds only until directions/heights/integrals are rationally certified.
"""
from pathlib import Path
import json
import numpy as np
from scipy.spatial import HalfspaceIntersection
from geom98 import load_r82,hull_v,mass
from masscover98 import quick_mass
from cover98 import fibonacci_sphere

def hbody(normal,off,inside=None):
    if inside is None:inside=np.zeros(3)
    hh=HalfspaceIntersection(np.c_[normal,-off],inside);v=hh.intersections
    V,g=quick_mass(v);return v,V,V*g

def main():
    root=Path(__file__).parent;b=load_r82();p=b['v']-b['g'];rad=np.linalg.norm(p,axis=1)
    records=json.loads((root/'GREEDY_COVER98_RESULTS.json').read_text());primary=next(z for z in records if z['t']==.35 and z['extra']==.02)
    points=np.r_[p,primary['apices_centered']];base=hull_v(points);V0=base['volume'];M0=V0*base['g'];w=M0/np.linalg.norm(M0)
    n0=base['equations'][:,:3];h0=-base['equations'][:,3]
    _,Vminus,Mminus=hbody(np.r_[n0,[w]],np.r_[h0,0.],inside=-.01*w)
    elder=b['equations'][18,:3];he=-b['equations'][18,3]-elder@b['g'];out=[]
    for elderguard in [False,True]:
        for count in [32,64,128,256,512,1024,2048]:
            n=fibonacci_sphere(count);h=np.max((n@p.T+rad)/2,axis=1)
            if elderguard:n=np.r_[n,[elder]];h=np.r_[h,he]
            verts,V,M=hbody(np.r_[n,[w]],np.r_[h,0.],inside=-.01*w)
            negative_shell_capacity=float(-w@(M-Mminus));projected_M=float(w@M0)
            z={'sphere_count':count,'elder_guard':elderguard,'outer_negative_region_vertices':len(verts),'negative_shell_capacity_upper_numerical':negative_shell_capacity,
              'required_counter_moment':projected_M,'positive_gap_numerical':projected_M-negative_shell_capacity,'negative_outer_volume':V,'primary_negative_volume':Vminus,
              'primary_volume':V0,'primary_M':M0.tolist(),'direction':w.tolist()}
            out.append(z);print(json.dumps(z),flush=True)
    (root/'CAPACITY98_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
    print('J98_ONE_STEP_CAPACITY_RELAXATION_FINISHED_NUMERICAL')
if __name__=='__main__':main()
```
### FILE twostepmass98.py
```python
"""Two-link physical controller escape from the exact one-step capacity obstruction.
Numerical nominations only; actual mass and hull are recomputed at every trial.
"""
from pathlib import Path
import json
import numpy as np
from scipy.optimize import minimize
from geom98 import load_r82,hull_v,numerical_summary
from masscover98 import quick_mass
from cover98 import fibonacci_sphere

def chain_extremum(v,n,shrink=1e-3):
    R=np.linalg.norm(v);u=v/R;phi=np.arccos(np.clip(n@u,-1,1));s=np.sin(phi)
    if s<1e-7:return None
    transverse=(u-(n@u)*n)/s;delta=phi/3;c=np.cos(delta)
    da=np.cos(delta)*n+np.sin(delta)*transverse;db=np.cos(2*delta)*n+np.sin(2*delta)*transverse
    a=R*c*c*(1-shrink)**2*da;b=R*c*(1-shrink)*db
    return np.array([a,b])

def main():
    root=Path(__file__).parent;b=load_r82();g0=b['g'];p=b['v']-g0
    spec=json.loads((root/'CAPEXACT98_INPUT.json').read_text());rawap=np.array(spec['primary_apices_raw_grid8'])/1e8
    base=np.r_[b['v'],rawap];elder=b['equations'][18,:3];he=-b['equations'][18,3]-elder@g0
    ds=fibonacci_sphere(180);radii=np.linalg.norm(p,axis=1);allc=[]
    for n in ds:
        phi=np.arccos(np.clip(p@n/radii,-1,1));order=np.argsort(radii*np.cos(phi/3)**3)[::-1]
        for w in order[:10]:
            ab=chain_extremum(p[w],n)
            if ab is not None and max(ab@elder)<he-1e-4:allc.append((ab,int(w)));break
    print('CANDIDATE_CHAINS',len(allc),flush=True)
    controls=[];ws=[];fixed=base.copy();states=[]
    for step in range(5):
        trials=[]
        for ab,w in allc:
            V,g=quick_mass(np.r_[fixed,ab+g0]);trials.append((float(np.linalg.norm(V*(g-g0))),w,ab,V,g))
        trials.sort(key=lambda z:z[0]);best=trials[0];_,w,ab,V,g=best
        controls.extend(ab);ws.append(w);fixed=np.r_[fixed,ab+g0]
        print('GREEDY',step+1,w,best[0],flush=True)
        k=len(ws);nv=2*k
        def residual(x):
            V,g=quick_mass(np.r_[base,x.reshape(nv,3)+g0]);return V*(g-g0)
        def fun(x):d=residual(x);return d@d
        def chords(x):
            xx=x.reshape(k,2,3);a=xx[:,0];bb=xx[:,1];old=p[ws]
            return np.r_[np.einsum('ij,ij->i',a,bb-a),np.einsum('ij,ij->i',bb,old-bb)]-1e-7
        def guard(x):return he-1e-5-x.reshape(nv,3)@elder
        op=minimize(fun,np.array(controls).ravel(),method='SLSQP',constraints=[{'type':'ineq','fun':chords},{'type':'ineq','fun':guard}],
             options={'maxiter':130,'ftol':1e-22,'eps':5e-8})
        ap=op.x.reshape(nv,3);bod=hull_v(np.r_[base,ap+g0]);ref=numerical_summary(bod,center=g0);own=numerical_summary(bod)
        z={'chain_count':k,'witnesses':ws.copy(),'controllers_centered':ap.tolist(),'initial_controllers_centered':np.array(controls).tolist(),
           'success':bool(op.success),'message':str(op.message),'iterations':int(op.nit),'moment_residual':float(np.linalg.norm(residual(op.x))),
           'minimum_chord_margin':float(min(chords(op.x))),'minimum_elder_margin':float(min(guard(op.x))),
           'reference':ref,'own':own,'centroid_shift':(bod['g']-g0).tolist(),'volume_increment':bod['volume']-b['volume']}
        states.append(z);(root/'TWOSTEPMASS98_RESULTS.json').write_text(json.dumps(states,indent=2)+'\n')
        print('SOLVE',k,op.success,z['moment_residual'],'E',ref['E'],'refSU',len(ref['S']),len(ref['U']),'ownSU',len(own['S']),len(own['U']),flush=True)
        if z['moment_residual']<1e-6 and z['minimum_chord_margin']>-1e-8:break
        # Continue from the optimized finite body, not an obsolete greedy state.
        controls=ap.tolist();fixed=np.r_[base,ap+g0]
    print('J98_TWO_LINK_MASS_SEARCH_FINISHED_NUMERICAL')
if __name__=='__main__':main()
```
### FILE dualcapacity98.py
```python
"""Concave directional mass-capacity separator search on a fixed outer envelope.
Numerical only; a positive value nominates a direction for exact certification.
"""
from pathlib import Path
import json
import numpy as np
from scipy.optimize import minimize
from geom98 import load_r82,hull_v
from cover98 import fibonacci_sphere
from capacity98 import hbody

def main():
    root=Path(__file__).parent;b=load_r82();p=b['v']-b['g'];spec=json.loads((root/'CAPEXACT98_INPUT.json').read_text());points=np.r_[p,np.array(spec['primary_apices_raw_grid8'])/1e8-b['g']]
    B=hull_v(points);MB=B['volume']*B['g'];bn=B['equations'][:,:3];bh=-B['equations'][:,3];n=fibonacci_sphere(256);h=np.max((n@p.T+np.linalg.norm(p,axis=1))/2,axis=1)
    elder=b['equations'][18,:3];out=[]
    for ceiling in [None,.6338,.70]:
        nn=n.copy();hh=h.copy()
        if ceiling is not None:nn=np.r_[nn,[elder]];hh=np.r_[hh,ceiling]
        calls=[];cache={}
        def fg(w):
            key=tuple(w)
            if key in cache:return cache[key]
            if np.linalg.norm(w)<1e-8:return 0.,MB
            unit=w/np.linalg.norm(w)
            _,_,MO=hbody(np.r_[nn,[unit]],np.r_[hh,0.],inside=-.01*unit)
            _,_,MBN=hbody(np.r_[bn,[unit]],np.r_[bh,0.],inside=-.01*unit)
            grad=MB+MO-MBN;value=w@grad;cache[key]=(value,grad);calls.append([w.tolist(),float(value)]);return value,grad
        x0=MB/np.linalg.norm(MB)
        op=minimize(lambda w:-fg(w)[0],x0,jac=lambda w:-fg(w)[1],constraints=[{'type':'ineq','fun':lambda w:1-w@w,'jac':lambda w:-2*w}],method='SLSQP',options={'ftol':1e-12,'maxiter':80})
        val,grad=fg(op.x)
        z={'sphere_count':256,'elder_support_ceiling':ceiling,'success':bool(op.success),'message':str(op.message),'direction':op.x.tolist(),'numerical_gap':float(val),'gradient':grad.tolist(),'calls':calls};out.append(z)
        print(json.dumps({k:v for k,v in z.items()if k!='calls'}),flush=True)
    (root/'DUALCAPACITY98_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
    print('J98_CONCAVE_CAPACITY_DIRECTION_SEARCH_FINISHED_NUMERICAL')
if __name__=='__main__':main()
```
### FILE elderrelease98.py
```python
"""Numerical fixed-direction elder-height release scan; not an exact certificate."""
from pathlib import Path
import json
import numpy as np
from geom98 import load_r82,hull_v
from cover98 import fibonacci_sphere
from capacity98 import hbody

def main():
    root=Path(__file__).parent;b=load_r82();p=b['v']-b['g']
    spec=json.loads((root/'CAPEXACT98_INPUT.json').read_text())
    B=hull_v(np.r_[p,np.array(spec['primary_apices_raw_grid8'])/1e8-b['g']])
    w=np.array([-590685,48387,805450])/1e6;MB=B['volume']*B['g']
    bn=B['equations'][:,:3];bh=-B['equations'][:,3]
    _,_,MBN=hbody(np.r_[bn,[w]],np.r_[bh,0.],inside=-.01*w)
    n=fibonacci_sphere(1024);h=np.max((n@p.T+np.linalg.norm(p,axis=1))/2,axis=1)
    elder=b['equations'][18,:3];he=-b['equations'][18,3]-elder@b['g'];out=[]
    for ceiling in [he,.46,.48,.50,.52,.54,.56,.58,.60,.62,.6338,.66,.70,.80]:
        _,_,MO=hbody(np.r_[n,[elder],[w]],np.r_[h,ceiling,0.],inside=-.01*w)
        cap=float(w@(MBN-MO));gap=float(w@MB)-cap
        out.append({'elder_support_ceiling':float(ceiling),'negative_capacity_upper_numerical':cap,'positive_gap_numerical':gap})
    (root/'ELDER_RELEASE98_CAPACITY.json').write_text(json.dumps(out,indent=2)+'\n')
    print('J98_NUMERICAL_ELDER_HEIGHT_SCAN_FINISHED_NOT_EXACT')
if __name__=='__main__':main()
```
### FILE replay_geometry98.py
```python
"""Rebuild every stored numerical endpoint without rerunning its optimizer.
This is numerical continuation/recovery only, NOT exact own110 verification.
"""
from pathlib import Path
import json,hashlib
import numpy as np
from geom98 import load_r82,hull_v,numerical_summary

def main():
    root=Path(__file__).parent;raw=(root/'NUMERICAL98_GEOMETRIES.json').read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='28892a505871207213fe4f0934fb7f6dd8a9c62ff4a6f87affc2c02d7637bb82'
    data=json.loads(raw);units=data['units'];b=load_r82();g=b['g']
    primary=next(z for z in units['GREEDY_COVER98_RESULTS.json']if z.get('t')==.35 and z.get('extra')==.02)
    raw_primary=np.array(json.loads((root/'CAPEXACT98_INPUT.json').read_text())['primary_apices_raw_grid8'])/1e8
    out=[];skipped=[]
    for name,records in units.items():
        for rec in records:
            prefix=b['v'];extra=None
            if 'apices_centered'in rec:extra=np.array(rec['apices_centered'])+g
            elif 'controls_centered'in rec:
                prefix=np.r_[prefix,np.array(primary['apices_centered'])+g]
                extra=np.array(rec['controls_centered'])+g
            elif 'controllers_centered'in rec:
                prefix=np.r_[prefix,raw_primary];extra=np.array(rec['controllers_centered'])+g
            if extra is None:
                skipped.append([name,rec['original_record_index']]);continue
            body=hull_v(np.r_[prefix,extra]);out.append({'source':name,'index':rec['original_record_index'],
                'reference':numerical_summary(body,center=g),'own':numerical_summary(body)})
    result={'scope':'Numerical replay, finite tolerances and bar floor, no exact equilibrium acceptance',
            'replayed':len(out),'failed_nomination_records_without_endpoint':skipped,'bodies':out}
    (root/'NUMERICAL98_REPLAY.json').write_text(json.dumps(result,indent=2)+'\n')
    print('J98_FROZEN_GEOMETRY_REPLAY_FINISHED_NOT_EXACT',len(out),len(skipped))
if __name__=='__main__':main()
```
