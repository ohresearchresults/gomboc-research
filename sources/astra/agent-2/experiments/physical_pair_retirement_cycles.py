"""Explicit physical point retirements at surplus-root near-collision stalls.
Deleting a submitted point defines a new convex body, never an approximate
combinatorial relabelling. Search remains numerical, with full exact dyadic
audits for any apparent110 and for the final body of this finite experiment.
"""
import sys,json,hashlib
from pathlib import Path
import numpy as np
from free_hull_one_root_slack import run as correct
from free_hull_metric121 import state
from geometry import angular_scores
from audit_binary_points import run as audit
from support_persistence import ROOT

def merits(X):
    s=state(X);n=len(X);active=np.ones(n+len(s['Q']),bool);active[:n]=False;active[np.unique(s['T'])]=True;ur=int(np.argmax(np.sum(s['Z']**2,1)));sr=int(np.argmax(np.sum(s['Q']**2,1)));active[ur]=False;active[n+sr]=False
    return s,ur,float(np.maximum(1e-7-s['guards'][active],0).sum())

def run(src,out,cycles=40):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=src.read_bytes();(out/'source.npy').write_bytes(raw);(out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(raw).hexdigest(),rule='explicit deletion of either endpoint of surplus-root best escape chord, followed by physical own110 correction'),indent=2)+'\n');X=np.load(src);ledger=[]
    for k in range(cycles):
        s,ur,m=merits(X);u=angular_scores(s['Z']);extra=[int(i) for i in np.flatnonzero(u.max(1)<0) if i!=ur]
        if s['S']==s['U']==1:
            p=out/f'NUMERICAL_GOAL_{k}.npy';np.save(p,X);r=audit(p,out/f'goal_exact_{k}');(out/'GOAL_AUDIT_RECEIPT.json').write_text(json.dumps(dict(counts=r['counts'],weak=r['weak'],V=r['V'],E=r['E'],F=r['F'],needs_independent_audit=True),indent=2)+'\n');break
        if not extra or len(X)<=12:
            (out/'FINITE_STOP.json').write_text(json.dumps(dict(reason='no surplus unstable root nomination or finite point-count floor',S=s['S'],U=s['U'],V=s['V']),indent=2)+'\n');break
        i=min(extra,key=lambda v:u[v].max());j=int(np.argmax(u[i]));distance=float(np.linalg.norm(X[i]-X[j]));choices=[]
        for deleted in [i,j]:
            A=np.delete(X,deleted,axis=0)
            try:
                t,tr,mm=merits(A)
                if t['E']<17:continue
            except (ValueError,np.linalg.LinAlgError,AssertionError):continue
            choices.append((t['S']+t['U'],mm,deleted,A,t))
        if not choices:raise ValueError('no physical deletion admitted within the search domain')
        _,mm,deleted,A,t=min(choices,key=lambda r:r[:3]);d=out/f'cycle{k:02d}';d.mkdir();p=d/'literal_retirement.npy';np.save(p,A);record=dict(cycle=k,source_supplied=len(X),root_pair=[i,j],pair_distance=distance,deleted=int(deleted),retired_body=dict(S=t['S'],U=t['U'],V=t['V'],E=t['E'],F=t['F'],merit=mm),choices=[dict(deleted=int(c[2]),S=c[4]['S'],U=c[4]['U'],V=c[4]['V'],E=c[4]['E'],merit=c[1]) for c in choices]);(d/'retirement.json').write_text(json.dumps(record,indent=2)+'\n');print('LITERAL_PAIR_RETIREMENT',record,flush=True)
        X=correct(p,d/'one_root',steps=500,eps=1e-7);t,tr,mm=merits(X);record['after_correction']=dict(S=t['S'],U=t['U'],V=t['V'],E=t['E'],F=t['F'],merit=mm);ledger.append(record);(out/'ledger.json').write_text(json.dumps(ledger,indent=2)+'\n');np.save(out/'latest.npy',X)
    np.save(out/'final.npy',X)
    if not (out/'GOAL_AUDIT_RECEIPT.json').exists():audit(out/'final.npy',out/'exact_final')
    return X
if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 40)
