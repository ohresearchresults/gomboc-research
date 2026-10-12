# material-324764f69cf1

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J118 numerical methods — complete source part 2 of 2

Requires all four source units in [internal-source-reference] and their literal geometry115.py/J117 input dependencies. The separate floating-checkpoint capsule records completed-prefix inputs; the exact C408 bodies do NOT depend on numerical reruns and recover directly from [internal-source-reference] plus exact115.cpp.

## Finite mechanism and executed sequence
For current own-centred junior vertex p, unit e=p/|p| and an old polar point r, the ball with centre r/2 and radius|r|/2 consists of w with w.(r-w)>=0. Its maximizer of w.p is h=(r+|r|e)/2. If cap=h.p>1, the literal fractions below choose w=h*(1+f*(cap-1))/cap with w.p>1 and w.(r-w)>0. Convert to a PHYSICAL new cut n=w/(1+w.g). This old-centre outgoing witness only proposes geometry; it does not certify the actual new mass. A finite cut may be followed by retiring/replacing a junior-incident old plane. ClassRepair then reintegrates the ACTUAL mass while moving all normals. Both its virtual guards and the floating clean filter are only proposals; exact115 certifies frozen bodies.

Executed `cuts118.py CLASS118_SMALL.json CUTS118.json`:108 admitted proposals, all E<=249. Candidate CUT6 has parent57,f=.3; its actual rawS32/U8 has mainP.3242529774755976 and genuine tiny extraP/Q. `cutrepair118.py CUTS118_CUT6.json CUTREPAIR118_6.json 2 45` completedone repair (3iterations) to numericalS1/U2,Q[],P.32434860024843143,V136/E204/F70. Stronger CUT0 repair also succeeded but returned worseP.3304200808229388; CUT10's two completed repairs failed badly. Do not keep only the smallest raw P while dropping other bars.
`python surgery118.py CUTREPAIR118_6.json SURGERY118.json replace` evaluated270 replacements, all withinE249. TOP0 has parent69,f=.6,retired/replaced input69; one4-iteration repair gives numericalP.32319788589208537,S1/U2,Q[],still136/204/70. TOP2 givesP.3237364780180183 after5iterations; TOP5 gives worseP.331015814485872 after5iterations. The endpoint with TOP0 is the sole source for the rational C408 G5/G6/G7 freezes. Thus the second step replaces the newly introduced support without spending another facet.
`python iterate118.py SURGERYREPAIR118_0.json ITERATE118_A.json 3 5 25` completed285 finite proposals and5 repairs at iteration0, accepted0, then terminated normally. This particular top5 ranking/retirement policy stalled; it is not a proof against finite surgery, other roots, extra cuts or actual110. All normative claims are restricted to completed executions. No noisy floating positive bar is asserted absent without the separate exact audit.

## cuts118.py — 2043B, SHA09c4f3fe0e88f650ea2697784c5906af56389a6c216d5f5df1eef928afaf33c6
```python
"""Finite physical cuts with an old-centre outgoing polar witness.
The old-centre condition is ONLY a geometric proposal; every result uses
its rebuilt actual body and homogeneous centroid. Numerical, not exact.
"""
import os
os.environ.setdefault('OMP_NUM_THREADS','1');os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import sys,json
from pathlib import Path
import numpy as np
from bottleneck118 import read_source,report

def run(source,out):
 n=read_source(source);m,t,qt,c=report(n);u=c['P'][0][1];p=m['p'][u];e=p/np.linalg.norm(p);g=m['g'];q=m['q']
 records=[];candidates=[]
 for j in m['active']:
  r=q[j];h=(r+np.linalg.norm(r)*e)/2;cap=h@p
  if cap<=1+1e-8:continue
  for frac in [.01,.03,.1,.3,.6,.9]:
   # w tends to the tangent ball extremum without reaching its zero chord.
   w=h*((1+frac*(cap-1))/cap)
   chord=w@(r-w)
   if chord<=0 or 1+w@g<=0:continue
   z=np.r_[n,(w/(1+w@g))[None,:]]
   try:mm,tt,qq,cc=report(z)
   except (ValueError,AssertionError):continue
   rec=dict(parent=int(j),fraction=frac,cap=float(cap),chord=float(chord),normal=z[-1].tolist(),census=cc)
   records.append(rec)
   if cc['E']<=249:
    score=sum(x[0] for x in cc['P'])+sum(x[0] for x in cc['Q'])
    candidates.append((score,z,rec))
 candidates.sort(key=lambda x:x[0]);selected=[]
 # Retain complete best proposals, not only a selected summary.
 for rank,(score,z,rec) in enumerate(candidates[:12]):
  name=Path(out).with_name(Path(out).stem+f'_CUT{rank}.json')
  name.write_text(json.dumps(dict(normals=z.tolist(),source=Path(source).name,proposal=rec),indent=2)+'\n')
  selected.append(dict(rank=rank,file=name.name,score=score,**rec))
 Path(out).write_text(json.dumps(dict(source=Path(source).name,records=records,selected=selected),indent=2)+'\n')
 print('SCANNED',len(records),'WITHIN_BUDGET',len(candidates),flush=True)
 for r in selected:
  cc=r['census'];print(r['rank'],r['parent'],r['fraction'],cc['E'],len(cc['S']),len(cc['U']),[x[0] for x in cc['P']], [x[0] for x in cc['Q']],flush=True)
if __name__=='__main__':run(*sys.argv[1:])
```

## cutrepair118.py — 1175B, SHAf20b8b104d5e24fc3b0edd43d542adbac3c9a015f6df976e4b568c3267da713e
```python
"""Completed-prefix finite-cut repair; all accepted claims are numerical.
Use exact115 separately after a rational freeze for exact equilibrium claims.
"""
import os
os.environ.setdefault('OMP_NUM_THREADS','1');os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import sys,json
from pathlib import Path
from bottleneck118 import read_source,report
from class118 import ClassRepair,clean

def run(source,out,rounds=3,limit=45):
 n=read_source(source);rs=[]
 for k in range(rounds):
  try:z,r=ClassRepair(n,margin=1e-5,bound=.05).run(limit)
  except Exception as e:
   rs.append(dict(error=repr(e)));break
  rs.append(r);n=z;c=r['census'];print(k,r['status'],r['iterations'],r['min_constraint'],len(c['S']),len(c['U']),[a[0] for a in c['P']],flush=True)
  Path(out).write_text(json.dumps(dict(normals=n.tolist(),receipts=rs,source=Path(source).name,params=dict(rounds=rounds,limit=limit,margin=1e-5,bound=.05)),indent=2)+'\n')
  if clean(c):print('NUMERIC_REPAIR_SUCCESS_NOT_EXACT',flush=True);break
 print('FINISHED',len(rs),flush=True)
if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 3,int(sys.argv[4]) if len(sys.argv)>4 else 45)
```

## surgery118.py — 2451B, SHA8a8960fc0a98bcfb9d015f4a6a8ad02854cc0ad73df50ca4f3a98188615577b5
```python
"""Finite new polar cut plus retirement of an old junior-incident support.
Proposals use a previous-centre polar witness; numerical endpoints ALWAYS
rebuild the full actual hull, volume and centroid before their comparison.
"""
import os
os.environ.setdefault('OMP_NUM_THREADS','1');os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import sys,json
from pathlib import Path
import numpy as np
from bottleneck118 import read_source,report

def run(source,out,mode='replace'):
 n=read_source(source);m,t,qt,c=report(n);birth=c['P'][0][1];p=m['p'][birth];e=p/np.linalg.norm(p);g=m['g'];q=m['q']
 retire=m['triples'][birth].tolist() if mode=='replace' else [None]
 rows=[];proposals=[]
 for j in m['active']:
  r=q[j];h=(r+np.linalg.norm(r)*e)/2;cap=h@p
  if cap<=1+1e-8:continue
  for frac in [.03,.1,.3,.6,.9]:
   w=h*((1+frac*(cap-1))/cap)
   if w@(r-w)<=0 or 1+w@g<=0:continue
   nn=w/(1+w@g)
   for old in retire:
    z=np.r_[n,nn[None,:]] if old is None else n.copy()
    if old is not None:z[old]=nn
    try:mm,tt,qq,cc=report(z)
    except (ValueError,AssertionError):continue
    a=dict(parent=int(j),fraction=frac,retire=old,normal=nn.tolist(),census=cc);rows.append(a)
    if cc['E']>249:continue
    # Extra-basin penalty, not a license to discard their positive bars.
    pb=sorted([v[0] for v in cc['P']],reverse=True);qb=[v[0] for v in cc['Q']]
    score=sum(pb)+sum(qb)+3*sum(pb[1:])+3*sum(qb)
    proposals.append((score,z,a))
 proposals.sort(key=lambda x:x[0]);selected=[]
 # Keep geometrically distinct parent/retired-support choices.
 seen=set()
 for score,z,a in proposals:
  key=(a['parent'],a['retire'])
  if key in seen:continue
  seen.add(key);rank=len(selected)
  name=Path(out).with_name(Path(out).stem+f'_TOP{rank}.json')
  name.write_text(json.dumps(dict(normals=z.tolist(),source=Path(source).name,proposal=a),indent=2)+'\n')
  selected.append(dict(rank=rank,file=name.name,score=score,**a))
  if len(selected)==12:break
 Path(out).write_text(json.dumps(dict(source=Path(source).name,mode=mode,retire_pool=retire,records=rows,selected=selected),indent=2)+'\n')
 print('EVALUATED',len(rows),'WITHIN_BUDGET',len(proposals),flush=True)
 for a in selected:
  cc=a['census'];print(a['rank'],a['parent'],a['fraction'],a['retire'],cc['E'],len(cc['S']),len(cc['U']),[v[0] for v in cc['P'][:4]],[v[0] for v in cc['Q'][:3]],flush=True)
if __name__=='__main__':run(sys.argv[1],sys.argv[2],sys.argv[3] if len(sys.argv)>3 else 'replace')
```

## iterate118.py — 2969B, SHAe05c6a99988a49d24eb35a885c1aadf48a8b33d6b4f951aaff269695e8f8758f
```python
"""Finite cut/retirement and actual-centred class retraction.
No permanent old reference centre, forest, or face lattice is imposed.
The top-K finite search and thresholds are explicit; failure is local-policy
failure, not a no-go theorem. All accepted results remain numerical.
"""
import os
os.environ.setdefault('OMP_NUM_THREADS','1');os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import sys,json
from pathlib import Path
import numpy as np
from bottleneck118 import read_source,report
from class118 import ClassRepair,clean

def run(source,out,steps=3,top=5,limit=25):
 n=read_source(source);trace=[];history=[]
 for it in range(steps):
  m,tt,qt,c=report(n);oldP=sum(v[0] for v in c['P']);p=m['p'][c['P'][0][1]];e=p/np.linalg.norm(p)
  retirees=m['triples'][c['P'][0][1]].tolist();candidates=[];scans=[]
  for j in m['active']:
   r=m['q'][j];h=(r+np.linalg.norm(r)*e)/2;cap=h@p
   if cap<=1+1e-8:continue
   for f in [.03,.1,.3,.6,.9]:
    w=h*((1+f*(cap-1))/cap)
    if w@(r-w)<=0 or 1+w@m['g']<=0:continue
    nn=w/(1+w@m['g'])
    for k in retirees:
     z=n.copy();z[k]=nn
     try:cc=report(z)[3]
     except (ValueError,AssertionError):continue
     rec=dict(parent=int(j),fraction=f,retire=int(k),normal=nn.tolist(),census=cc);scans.append(rec)
     if cc['E']>249:continue
     pb=sorted([v[0] for v in cc['P']],reverse=True);qb=[v[0] for v in cc['Q']]
     score=sum(pb)+sum(qb)+3*(sum(pb[1:])+sum(qb))
     candidates.append((score,z,rec))
  candidates.sort(key=lambda x:x[0]);repairs=[];best=None
  for rank,(score,z,rec) in enumerate(candidates[:top]):
   try:zz,rr=ClassRepair(z,margin=1e-5,bound=.05).run(limit)
   except Exception as error:repairs.append(dict(rank=rank,proposal=rec,error=repr(error)));continue
   cc=rr['census'];ps=sum(v[0] for v in cc['P']);repairs.append(dict(rank=rank,proposal=rec,receipt=rr))
   if clean(cc) and cc['E']<=249 and ps<oldP-1e-7 and (best is None or ps<best[0]):best=(ps,zz,rec,rr)
  history.append(dict(it=it,retirees=retirees,scans=scans,repairs=repairs))
  if best is None:print('NO_FINITE_ACCEPTED_STEP',it,'P',oldP,'scanned',len(scans),flush=True);break
  n=best[1];trace.append(dict(it=it,P=best[0],proposal=best[2],receipt=best[3],normals=n.tolist()))
  Path(out).write_text(json.dumps(dict(normals=n.tolist(),trace=trace,history=history,source=Path(source).name,params=dict(steps=steps,top=top,limit=limit,margin=1e-5,bound=.05)),indent=2)+'\n')
  print('ACCEPTED',it,best[0],best[2]['parent'],best[2]['fraction'],best[2]['retire'],best[3]['census']['E'],flush=True)
 Path(out).write_text(json.dumps(dict(normals=n.tolist(),trace=trace,history=history,source=Path(source).name,params=dict(steps=steps,top=top,limit=limit,margin=1e-5,bound=.05)),indent=2)+'\n')
 print('FINISHED',len(trace),report(n)[3],flush=True)
if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 3,int(sys.argv[4]) if len(sys.argv)>4 else 5,int(sys.argv[5]) if len(sys.argv)>5 else 25)
```
