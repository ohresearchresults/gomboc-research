# material-d806da2e587c

AI research material

---

# J119_RETIREMENT_RELAY_AND_FREEZE_SOURCES.md

Complete runnable source units. Write each fenced block under its named filename, retaining its final newline. Dependencies are explicit imports. Search uses CPython3.13.5, NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu, one thread; exact auditing uses g++14.2.0 and GMP6.3.0. Floating search/bar floors are not exact-equilibrium evidence. Exact endpoint recovery is preserved separately.

## retire_orbit119.py

Bytes: 1657; SHA-256: 7b24a708f2d7c2191ea50903126042243e0e74f6b18b912c45360108e63af628.

```python
"""Finite facet retirement followed by actual-mass projective/affine repair.
No new facet is charged for the orbit. Numerical admission only.
"""
import json,sys,time
from pathlib import Path
import numpy as np,torch
from scipy.optimize import minimize
from orbit119 import Orbit,read_h
from prune119 import stats

def restore(n,prefix,steps=100):
 o=Orbit(n);base=o.evaluate(np.zeros(8));qr=base['Q'][0][1] if base['Q'] else None
 with torch.no_grad():q0=o.tensors(torch.zeros(8))[1]
 allowed=(qr,int((q0*q0).sum(1).argmax()))
 def fun(x):return np.dot(x,x)/2,x
 def con(x):return o.constraints(torch.tensor(x),allowed,1e-7).detach().numpy()
 def jac(x):return torch.autograd.functional.jacobian(lambda y:o.constraints(y,allowed,1e-7),torch.tensor(x),vectorize=True,strategy='forward-mode').detach().numpy()
 res=minimize(fun,np.zeros(8),jac=True,method='SLSQP',bounds=[(-.3,.3)]*8,constraints=[dict(type='ineq',fun=con,jac=jac)],options=dict(maxiter=steps,ftol=1e-12,disp=False))
 c=o.evaluate(res.x);margin=float(con(res.x).min());ok=margin>=-1e-10 and len(c['S'])<=2 and len(c['U'])==1
 r=dict(status=int(res.status),message=str(res.message),nit=res.nit,ok=ok,margin=margin,body=c,base=base)
 Path(prefix+'.json').write_text(json.dumps(r,indent=2)+'\n')
 print('RETIRE_ORBIT_REPAIR',prefix,res.status,res.nit,margin,len(c['S']),len(c['U']),c['Q'][0][0] if c['Q'] else 0,ok,flush=True)
 return r

def main(inp,out,indices):
 n=read_h(inp);outdir=Path(out);outdir.mkdir(exist_ok=True)
 for i in indices:
  new=np.delete(n,i,axis=0);restore(new,str(outdir/f'delete{i}'))
if __name__=='__main__':main(sys.argv[1],sys.argv[2],[int(x) for x in sys.argv[3:]])
```

## retire_sequence119.py

Bytes: 1907; SHA-256: a59ec738fceadd714ea63f96538175f47d76193b132b956e84c52a70ce1d8f1e.

```python
"""Finite support-budget search: deletion + shared physical orbit repair.
The transcript records every attempted repair and every literal floating body.
"""
import sys,json,time
from pathlib import Path
import numpy as np
from orbit119 import read_h
from prune119 import stats
from retire_orbit119 import restore

def main(inp,out,maxsteps=6,tries=8):
 out=Path(out);out.mkdir(exist_ok=True);n=read_h(inp);start=time.time();ledger=[]
 for step in range(1,maxsteps+1):
  choices=[]
  for i in range(len(n)):
   nn=np.delete(n,i,axis=0)
   try:c=stats(nn)
   except Exception as e:continue
   gap=max(0,-c['minp'])+max(0,-c['minq'])
   choices.append((gap,i,c))
  choices.sort(key=lambda a:a[0]);good=[];trials=[]
  for rank,(gap,i,c) in enumerate(choices[:tries]):
   r=restore(np.delete(n,i,axis=0),str(out/f'step{step}_rank{rank}_delete{i}'),steps=70)
   r['deleted']=i;r['raw_gap']=gap;trials.append(r)
   if r['ok']:
    good.append(r)
    # A cheap deletion keeps the extra stable basin near its old scale.
    if r['body']['Q'][0][0]<.23:break
  if not good:
   ledger.append(dict(step=step,success=False,trials=trials));break
  best=min(good,key=lambda r:r['body']['Q'][0][0] if r['body']['Q'] else 0);n=np.array(best['body']['n']);ledger.append(dict(step=step,success=True,chosen=best['deleted'],body=best['body'],trials=trials))
  Path(out/f'checkpoint{step}.json').write_text(json.dumps(best['body'],indent=2)+'\n')
  Path(out/'ledger.json').write_text(json.dumps(ledger,indent=2)+'\n')
  print('RETIRE_SEQUENCE119',step,'F',len(n),'Q',best['body']['Q'][0][0] if best['body']['Q'] else 0,'seconds',time.time()-start,flush=True)
 Path(out/'ledger.json').write_text(json.dumps(ledger,indent=2)+'\n');print('RETIRE_SEQUENCE119_COMPLETE',len(ledger),flush=True)
if __name__=='__main__':main(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 6,int(sys.argv[4]) if len(sys.argv)>4 else 8)
```

## apex_relay119.py

Bytes: 4217; SHA-256: 6413bbfeedebda3230498993d600c7e230779b8a13ae266759c214afeca20ded.

```python
"""Apex-preserving polar relays, with true mixed-face budget and actual mass.
Every new H plane contains one exact old physical vertex, using affine
combinations of its three incident old H normals. Floating construction and
census in this producer nominate bodies only. Coefficient quantization preserves
the apex incidence algebraically; it does not by itself certify equilibrium.
"""
import json,sys,math
from pathlib import Path
import numpy as np
from orbit119 import read_h,geometry,scores,bars
from prune119 import stats

def reference(n,g):
 G=geometry(n);active=sorted(G['faces']);remap={a:i for i,a in enumerate(active)};pe=G['pe'];qe=np.array([[remap[int(a)],remap[int(b)]] for a,b in G['qe']],int)
 p=G['v']-g;an=n[active];q=an/(1-an@g)[:,None];pc,pw=scores(p);qc,qw=scores(q)
 return dict(S=[active[i] for i in np.where(qc<-1e-10)[0]],U=np.where(pc<-1e-10)[0].tolist(),P=bars(p,pe),Q=bars(q,qe))

def build(n,links,side=1,power=1.0,angular=1.0):
 G=geometry(n);g=G['g'];p=G['v']-g;q=n/(1-n@g)[:,None];pr=int(np.argmax((p*p).sum(1)));qr=int(np.argmax((q*q).sum(1)));qc,_=scores(q);jun=[int(i) for i in np.where(qc<-1e-10)[0] if i!=qr];assert len(jun)==1;jun=jun[0]
 apex=G['v'][pr];s=p[pr];ss=s@s;c=s/ss;u=q[jun];z=q[qr];assert abs(z@s-1)<1e-8
 incident=np.where(abs(n@apex-1)<1e-8)[0];assert len(incident)==3
 udot=u@s;ut=u-udot*c;alpha=u@u-udot/ss;assert alpha>0
 virtual=ut*alpha/(ut@ut);target=z-c;r0=np.linalg.norm(virtual);rz=np.linalg.norm(target);e=virtual/r0;f=np.cross(s,e);f/=np.linalg.norm(f);signed=np.arctan2(target@f,target@e)
 if side==-1:signed=signed-2*np.pi if signed>0 else signed+2*np.pi
 t=np.linspace(0,1,links+1);angles=signed*t**angular;dirs=np.cos(angles)[:,None]*e+np.sin(angles)[:,None]*f
 cos=np.einsum('ij,ij->i',dirs[:-1],dirs[1:]);
 if cos.min()<=0:raise ValueError('nonpositive directional chord')
 cost=np.r_[0,np.cumsum(-np.log(cos))];slack=np.log(rz/r0)-cost[-1]
 if slack<=0:raise ValueError('no radial slack')
 radius=r0*np.exp(cost+slack*t**power);v=radius[:,None]*dirs;w=v[1:-1]+c
 assert np.max(abs(w@s-1))<1e-10
 qchain=np.vstack([u,w,z]);guards=np.einsum('ij,ij->i',qchain[:-1],qchain[1:]-qchain[:-1]);assert guards.min()>0
 nn=w/(1+w@g)[:,None];coef=nn@np.linalg.inv(n[incident]);assert np.max(abs(coef.sum(1)-1))<1e-8
 D=10**10;first=np.rint(coef[:,:2]*D).astype(np.int64);coeff=np.column_stack([first,D-first.sum(1)])
 nn=coeff@n[incident]/D;new=np.vstack([n,nn]);out=stats(new);ref=reference(new,g)
 # All new facets contain the old apex. Surface grouping is only numerical here.
 G2=geometry(new);pa=G2['v']-G2['g'];idx=int(np.argmin(np.linalg.norm(G2['v']-apex,axis=1)));degree=sum(idx in ed for ed in G2['pe'])
 out.update(n=new.tolist(),links=links,side=side,power=power,angular=angular,apex=apex.tolist(),apex_index=idx,apex_degree=int(degree),incident=incident.tolist(),coeff_D=D,coeff=coeff.tolist(),old_count=len(n),old_g=g.tolist(),virtual=virtual.tolist(),target=target.tolist(),virtual_ratio=rz/r0,virtual_angle=abs(signed),slack=float(slack),minimum_reference_chain_guard=float(guards.min()),reference=ref,apex_distance_error=float(np.linalg.norm(G2['v'][idx]-apex)))
 return out

def main(inp,prefix,links):
 n=read_h(inp);out=Path(prefix);out.mkdir(exist_ok=True);ledger=[]
 for side in [1,-1]:
  for power in [.3,.5,.8,1.,1.5,2.,3.]:
   for angular in [.8,1.,1.2]:
    try:r=build(n,links,side,power,angular)
    except (ValueError,AssertionError,np.linalg.LinAlgError) as e:continue
    name=f'L{links}_s{side}_p{power}_a{angular}.json';Path(out/name).write_text(json.dumps(r,indent=2)+'\n')
    rec=dict(name=name,VEF=r['VEF'],S=len(r['S']),U=len(r['U']),refS=len(r['reference']['S']),refU=len(r['reference']['U']),P=[b[0] for b in r['P'] if b[0]>1e-12],Q=[b[0] for b in r['Q'] if b[0]>1e-12],degree=r['apex_degree'],slack=r['slack']);ledger.append(rec)
    print('APEX_RELAY119',name,rec['VEF'],(rec['S'],rec['U']),'reference',(rec['refS'],rec['refU']),'PQmax',max(rec['P'],default=0),max(rec['Q'],default=0),'degree',rec['degree'],flush=True)
 Path(out/'ledger.json').write_text(json.dumps(ledger,indent=2)+'\n');print('APEX_RELAY119_FINISHED',len(ledger),flush=True)
if __name__=='__main__':main(sys.argv[1],sys.argv[2],int(sys.argv[3]))
```

## double_apex119.py

Bytes: 1521; SHA-256: 872031c8ecc65bc52cb2fad06276ea9ecd1ec399ad2c95e1452090efcc434a02.

```python
"""Two opposed root-preserving planar polar routes. Numerical only."""
import json,sys,itertools
from pathlib import Path
import numpy as np
from apex_relay119 import build,reference
from orbit119 import read_h,geometry
from prune119 import stats

def main(inp,out,links=17):
 n=read_h(inp);g=geometry(n)['g'];out=Path(out);out.mkdir(exist_ok=True);ledger=[]
 for p1,p2 in itertools.product([.3,1.,3.],repeat=2):
  try:a=build(n,links,1,p1,1.);b=build(n,links,-1,p2,1.)
  except (ValueError,AssertionError) as e:continue
  nn=np.vstack([n,np.array(a['n'])[len(n):],np.array(b['n'])[len(n):]])
  r=stats(nn);ref=reference(nn,g);r.update(n=nn.tolist(),reference=ref,old_count=len(n),old_g=g.tolist(),incident=a['incident'],coeff_D=a['coeff_D'],coeff=a['coeff']+b['coeff'],links=[links,links],powers=[p1,p2],apex=a['apex'])
  name=f'L{links}_p{p1}_{p2}.json';Path(out/name).write_text(json.dumps(r,indent=2)+'\n');ledger.append(dict(name=name,VEF=r['VEF'],S=len(r['S']),U=len(r['U']),refS=len(ref['S']),refU=len(ref['U']),P=[bb[0] for bb in r['P'] if bb[0]>1e-12],Q=[bb[0] for bb in r['Q'] if bb[0]>1e-12],refP=[bb[0] for bb in ref['P'] if bb[0]>1e-12],g=r['g']))
  z=ledger[-1];print('DOUBLE_APEX119',name,z['VEF'],(z['S'],z['U']),'ref',(z['refS'],z['refU']),'refP',z['refP'],'g',z['g'],flush=True)
 Path(out/'ledger.json').write_text(json.dumps(ledger,indent=2)+'\n');print('DOUBLE_APEX119_FINISHED',len(ledger),flush=True)
if __name__=='__main__':main(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 17)
```

## polar119.py

Bytes: 1675; SHA-256: d5955057d17ad11c6c0b716ea8e3982d58b67e928dfde70587e3a6e140b94a0e.

```python
"""Actual homogeneous polars of a literal H input; numerical nominations only."""
from pathlib import Path
import json,sys
import numpy as np
from scipy.optimize import minimize
from scipy.spatial import ConvexHull
from orbit119 import read_h,geometry,Orbit

def write_h_float(n,path):
 # The string is an exact rational quantization, not the original polar body.
 D=10**14;N=np.rint(n*D).astype(np.int64);Path(path).write_text(f'{len(N)} {D}\n'+''.join(' '.join(map(str,row))+'\n' for row in N))

def main(inp,prefix):
 n=read_h(inp);G=geometry(n);s=G['g'].copy()
 def polarmass(s):
  h=1-n@s
  if h.min()<=0:return None
  p=n/h[:,None];H=ConvexHull(p);tri=H.simplices.copy();v=p[tri];ori=np.sign(np.einsum('ij,ij->i',np.cross(v[:,1]-v[:,0],v[:,2]-v[:,0]),H.equations[:,:3]));tri[ori<0]=tri[ori<0,::-1]
  v=p[tri];w=np.linalg.det(v)/6;assert w.min()>0
  V=w.sum();g=(w[:,None]*v.sum(1)/4).sum(0)/V
  return V,g
 def fun(s):
  x=polarmass(s)
  return (1e6,np.zeros(3)) if x is None else (np.log(x[0]),4*x[1])
 out=[]
 for name,center in [('centroid',s),('santalo',minimize(fun,s,jac=True,method='BFGS',options=dict(gtol=1e-12,maxiter=100)).x)]:
  nn=G['v']-center
  H=Orbit(nn);r=H.evaluate(np.zeros(8));r.update(center=center.tolist(),name=name,original_h=inp)
  Path(prefix+'_'+name+'.json').write_text(json.dumps(r,indent=2)+'\n');write_h_float(nn,prefix+'_'+name+'_G14.txt')
  out.append(r);print(name,r['VEF'],r['S'],r['U'],'P',[(b[0],b[1]) for b in r['P'] if b[0]>1e-12],'Q',[(b[0],b[1]) for b in r['Q'] if b[0]>1e-12], 'g',r['g'],flush=True)
 Path(prefix+'_summary.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main(sys.argv[1],sys.argv[2])
```

## freeze119.py

Bytes: 1649; SHA-256: 4505aac22c8681a269e8d014e16e0cc65fea9d22cc9304945203e12565b3930c.

```python
"""Literal rational freezes and incidence-preserving relay construction."""
import json,sys,subprocess,hashlib
from pathlib import Path
import numpy as np

def freeze(inp,name,digits):
 n=np.array(json.load(open(inp))['n']);D=10**digits;N=np.rint(n*D).astype(np.int64).tolist();text=f'{len(N)} {D}\n'+''.join(' '.join(map(str,row))+'\n' for row in N);Path(name+'.txt').write_text(text);return N,D

def run(name):
 with open(name+'.txt','rb') as i,open(name+'_AUDIT.json','wb') as o,open(name+'_AUDIT.log','wb') as e:subprocess.run(['./exact115'],stdin=i,stdout=o,stderr=e,check=True)
 r=json.load(open(name+'_AUDIT.json'));print('FREEZE119_EXACT',name,[r[k] for k in ['V','E','F']],r['strict'],r['weak'],r['primitive_zeros'],'P',len(r['P']),'Q',len(r['Q']),flush=True)
 return r

if __name__=='__main__':
 freeze('retire_sequence/checkpoint1.json','J119_RETIRED79_G8',8)
 base,D=freeze('retire_sequence_from4/checkpoint2.json','J119_RETIRED74_G8',8)
 freeze('retire_sequence_from4/checkpoint2.json','J119_RETIRED74_G7',7)
 freeze('retire_sequence_from4/checkpoint3.json','J119_RETIRED73_G8',8)
 a=json.load(open('double_apex74/L17_p1.0_1.0.json'));C=a['coeff_D'];I=a['incident'];rows=[[int(x)*C for x in row] for row in base]
 rows += [[sum(int(co[k])*int(base[I[k]][j]) for k in range(3)) for j in range(3)] for co in a['coeff']]
 name='J119_DOUBLE_APEX_G8';Path(name+'.txt').write_text(f'{len(rows)} {D*C}\n'+''.join(' '.join(map(str,row))+'\n' for row in rows))
 for name in ['J119_RETIRED79_G8','J119_RETIRED74_G8','J119_RETIRED74_G7','J119_RETIRED73_G8','J119_DOUBLE_APEX_G8']:run(name)
 print('FREEZE119_ALL_FIVE_AUDITS_COMPLETED',flush=True)
```

## freeze_apex119.py

Bytes: 2573; SHA-256: f9034af78b1c825a6ecfdc6955564a8a7a42fd51d40537c58f392640e01aaf8c.

```python
"""Incidence-preserving rationalization of the common-apex actual-mass chart.
Numerical input is a complete n-array and apex in JSON, not an exact claim.
The apex is rounded to 10^-digits. On every identified through-apex plane,
round two normal coordinates and solve the remaining coefficient EXACTLY.
The output is an exact rational H body and requires an independent census.
Uses only Python standard library. For the audited fixtures use digits 8,7,6.
"""
import json,sys,math,subprocess,hashlib
from pathlib import Path
from fractions import Fraction as Q
sys.set_int_max_str_digits(0)

def freeze(inp,out,digits):
 r=json.loads(Path(inp).read_text());D=10**digits
 # Fraction(float) and round implement literal binary64 ties-to-even rounding.
 a=[Q(round(Q(float(x))*D),D) for x in r['apex']];k=max(range(3),key=lambda k:abs(a[k]));assert a[k]
 rows=[];ap=[]
 for i,n in enumerate(r['n']):
  q=[Q(round(Q(float(x))*D),D) for x in n]
  through=abs(sum(float(n[j])*r['apex'][j] for j in range(3))-1)<1e-7
  if through:
   ap.append(i);q[k]=(1-sum(a[j]*q[j] for j in range(3) if j!=k))/a[k]
   assert sum(a[j]*q[j] for j in range(3))==1
  else:assert sum(a[j]*q[j] for j in range(3))<1
  den=math.lcm(*(x.denominator for x in q));row=[int(x*den) for x in q]+[den];gg=math.gcd(*row);rows.append([x//gg for x in row])
 assert len(ap)>=3
 text=f'{len(rows)} 0\n'+''.join(' '.join(map(str,row))+'\n' for row in rows);Path(out+'.txt').write_text(text)
 desc=dict(input=inp,digits=digits,apex=list(map(str,a)),solved_axis=k,through_apex_inputs=ap,sha256=hashlib.sha256(text.encode()).hexdigest())
 Path(out+'_FREEZE.json').write_text(json.dumps(desc,indent=2)+'\n')
 return desc

def run(inp,out,digits):
 desc=freeze(inp,out,digits)
 with open(out+'.txt','rb') as i,open(out+'_AUDIT.json','wb') as o,open(out+'_AUDIT.log','wb') as e:
  subprocess.run(['./exact115'],stdin=i,stdout=o,stderr=e,check=True)
 r=json.loads(Path(out+'_AUDIT.json').read_text());a=list(map(Q,desc['apex']));v=[list(map(Q,x)) for x in r['vertices']];ai=v.index(a);deg=sum(ai in e for e in r['edges'])
 assert r['E']<=3*r['F']-deg-3
 print('EXACT_APEX119',out,[r[k] for k in ['V','E','F','C']],r['strict'],r['weak'],r['primitive_zeros'],'apex',ai,'degree',deg,'P',[float(Q(b['depth'])) for b in r['P']],'Q',[float(Q(b['depth'])) for b in r['Q']],flush=True)
 return r
if __name__=='__main__':
 for kind in ['P','Q']:
  for digits in [8,7,6]:run('apexflow_barrier'+kind+'.last.json','J119_APEX_BARRIER'+kind+'_G'+str(digits),digits)
 print('J119_SIX_INCIDENCE_PRESERVING_FREEZES_COMPLETED',flush=True)
```
