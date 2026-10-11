"""Insert a finite polar relay at an exposed S1 guard, with ACTUAL mass census.
The new point interpolates qi,qj plus an outward qi displacement. No old-centre
classification substitutes for the recomputed uniform-body census.
"""
import numpy as np,json,sys
from pathlib import Path
from flow115 import diagnostics

def relay(inp,out):
    n=np.asarray(json.loads(Path(inp).read_text())['normals']);m,c=diagnostics(n);q=m['q'];g=m['g']
    ids=[int(i) for i in np.argsort(c['qc']/np.sum(q*q,axis=1)) if i!=c['qroot']][:4]
    records=[];best=None
    for i in ids:
      j=int(c['qw'][i]);d=q[j]-q[i];A=q[i]@q[i];D=d@d
      for lam in [.05,.1,.2,.35,.5,.7,.9]:
       for fraction in [.002,.01,.03,.1,.3,.6]:
        eps=fraction*lam*(1-lam)*D/A
        w=(1+eps)*q[i]+lam*d
        if w@(q[j]-w)<=0 or q[i]@(w-q[i])<=0:continue
        z=np.r_[n,(w/(1+w@g))[None,:]]
        try:mm,cc=diagnostics(z)
        except (ValueError,AssertionError):continue
        rec=dict(i=i,j=j,lam=lam,fraction=fraction,eps=float(eps),E=cc['E'],F=cc['F'],S=cc['S'],U=cc['U'],P=sum(x[0] for x in cc['P']),Q=sum(x[0] for x in cc['Q']),minQ=cc['minQ'],minP=cc['minP'])
        records.append(rec)
        if cc['E']<=249 and cc['S']==1 and cc['U']==2 and len(cc['P'])==1 and len(cc['Q'])==0 and cc['minQ']>1e-10 and cc['minP']>1e-9 and rec['P']<sum(x[0] for x in c['P'])+.005:
          # Prefer a nonmicroscopic minimum Q, then smallest remaining P.
          score=rec['P'] + 1e-6/max(rec['minQ'],1e-12)**.25
          if best is None or score<best[0]:best=(score,z,rec)
    Path(str(out)+'.scan.json').write_text(json.dumps(records,indent=2)+'\n')
    if best is None:print('NO_VALID_RELAY',len(records),flush=True);return False
    Path(out).write_text(json.dumps(dict(normals=best[1].tolist(),relay=best[2],source=Path(inp).name),indent=2)+'\n')
    print('RELAY',best[2],flush=True);return True
if __name__=='__main__':relay(sys.argv[1],sys.argv[2])
