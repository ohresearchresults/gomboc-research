"""Finite screening of actual one-support transverse edge contractions.
Only proposal rankings; full exact audits must validate the final halfspaces.
"""
import sys,json,itertools
from pathlib import Path
import numpy as np
R=Path(__file__).resolve().parent;sys.path[:0]=[str(R/'parent/parent/mechanism/parent_sources')]
from atlas_opt import Atlas
from numeric import recover,snapped,mechanics

def seed(data,fs,keep,drop,moved):
 z,nf=snapped(data,fs,keep,drop,moved);X=recover(z);plan=next(t for t in z['plan'] if t[0]==moved)
 C=X[plan[1]];q=recover(data)[moved];q+=C.T@np.linalg.solve(C@C.T,np.ones(len(C))-C@q)
 z['controls'][moved]=np.rint(q*z['grid']).astype(np.int64).tolist()
 return z,nf

def main(out):
 d=json.loads((R/'parent/BASIN69_96/GENERATOR.json').read_text());fs=json.loads((R/'parent/BASIN69_96/faces.json').read_text());m=Atlas(d,fs);s=m.state(m.u0,False);plans={i:(deps,axes) for i,deps,axes in d['plan']};downstream={j for i,deps,axes in d['plan'] for j in deps};out=Path(out);out.mkdir(exist_ok=False)
 rows=[];forbid={3,137};protected=[{3,17,49,57,73,88,134,135,136},{71,94,109,116,119,126}]
 for a,b in sorted(m.ef):
  if any(set(m.owners[v])==p for v in [a,b] for p in protected) or m.Uroot in (a,b):continue
  for keep,drop in [(a,b),(b,a)]:
   diff=set(m.owners[drop])-set(m.owners[keep]);union=set(m.owners[drop])|set(m.owners[keep])
   if len(diff)!=1 or {16,18,71,94}<=union:continue
   moved=diff.pop()
   if moved in downstream or moved==3 or len(plans[moved][0])>=3:continue
   try:
    z,nf=seed(d,fs,keep,drop,moved);nm=Atlas(z,nf);ns=nm.state(nm.u0,False)
    ms=ns['cs'].max(1);mu=ns['cu'].max(1);ms=np.delete(ms,3);mu=np.delete(mu,nm.Uroot)
    merit=np.linalg.norm(np.minimum(np.r_[ms,mu]-1e-6,0))
    rr=dict(keep=keep,drop=drop,moved=moved,union=sorted(union),gap=float(s['gaps'][keep,moved]),score=float(merit),mingap=float(ns['gaps'][~nm.inc].min()),mindet=float(ns['det'].min()),max_moved=float(np.linalg.norm(s['q'][moved]-ns['q'][moved])))
    if rr['mingap']>0 and rr['mindet']>0:
     rr['counts']=mechanics(ns['q'],nf,P=ns['P'],tol=1e-13)['counts'];p=out/f'K{keep}_D{drop}_M{moved}';p.mkdir();(p/'GENERATOR.json').write_text(json.dumps(z,sort_keys=True,separators=(',',':')));(p/'faces.json').write_text(json.dumps(nf,separators=(',',':')))
    rows.append(rr)
   except (AssertionError,ValueError,np.linalg.LinAlgError,StopIteration) as e:rows.append(dict(keep=keep,drop=drop,moved=moved,error=str(e)))
 rows.sort(key=lambda r:(0 if 'counts' in r else 1,r.get('score',1e100)));(out/'SCREEN.json').write_text(json.dumps(rows,indent=2))
 print('tested',len(rows),'valid',sum('counts' in r for r in rows));print(json.dumps(rows[:25],indent=2))
if __name__=='__main__':main(sys.argv[1])
