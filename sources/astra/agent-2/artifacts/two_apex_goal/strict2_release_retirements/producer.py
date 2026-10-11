"""Retire free planes and restore the body's actual centroid by moving vertex v.
Only leaves of the current positive stable-escape tree are proposed. Each
physical deletion is followed by a three-variable actual-volume Newton solve;
the final hull and all numerical equilibria are re-evaluated. The purpose is
to free enough true edge budget to truncate and release the second star.
"""
import sys,json,hashlib,time
from pathlib import Path
import numpy as np
from scipy.spatial import QhullError
from flexible_two_apex_supports import FlexibleTwoApexFamily

def compact(q,m,n):
    old=FlexibleTwoApexFamily(m,n).state(q);A=old['A'];first=[int(i) for i in A if i<m];second=[int(i) for i in A if m<=i<m+n];other=[int(i) for i in A if i>=m+n]
    if min(len(first),len(second))<3 or old['active_anchors']!=[0,1]:raise ValueError('both genuine common vertices are required for this surgery')
    f=FlexibleTwoApexFamily(len(first),len(second));qq=f.pack(old['H'][first+second+other],q[-3:]);return qq,len(first),len(second),f.state(qq)

def balance(q,fam,target):
    q=q.copy();trace=[]
    for it in range(14):
        s=fam.state(q);r=s['g']-target;error=float(abs(r).max());trace.append(dict(it=it,error=error,centroid=s['g'].tolist()))
        if error<2e-13:return q,s,trace
        columns=[]
        for j in range(3):
            z=q.astype(complex);z[len(q)-3+j]+=1e-25j;columns.append(np.imag(fam.independent_physical(z,s['R'],s['T'],s['A'])[3])/1e-25)
        J=np.column_stack(columns)
        if np.linalg.cond(J)>1e10:raise ValueError('centroid control by the second vertex is singular')
        step=np.linalg.solve(J,-r);size=np.linalg.norm(step)
        if size>.25:step*=.25/size
        accepted=False
        for back in range(15):
            trial=q.copy();trial[-3:]+=2**-back*step
            try:t=fam.state(trial)
            except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError):continue
            if np.linalg.norm(t['g']-target)<np.linalg.norm(r)*(1-1e-7):q=trial;accepted=True;break
        if not accepted:raise ValueError('actual-centroid Newton solve has no admitted improving step')
    raise ValueError('actual-centroid Newton solve did not close')

def run(src,out,m=44,n=20,rounds=7,width=3,unstable_limit=None,release_only=False):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=src.read_bytes();(out/'source_q.npy').write_bytes(raw);q=np.load(out/'source_q.npy');q,m,n,first=compact(q,m,n);target=first['g'].copy()
    if first['S']!=1:raise ValueError('this retirement search requires actual S1')
    if unstable_limit is not None and first['U']>unstable_limit:raise ValueError('source exceeds the requested actual unstable count')
    states=[(q,m,n,'source')];rows=[];start=time.time();best=None
    (out/'source.json').write_text(json.dumps(dict(path=str(src),sha256=hashlib.sha256(raw).hexdigest(),m=m,n=n,centroid_target=target.tolist(),unstable_limit=unstable_limit,release_only=release_only,method=__doc__),indent=2)+'\n');(out/'producer.py').write_bytes(Path(__file__).read_bytes())
    initial={k:first[k] for k in ['V','E','F','S','U','Pmax','Qmax','minimum_noncontact']};initial.update(m=m,n=n,post_truncation_edge_bound=3*first['F']-m)
    initial['post_release_edge_bound']=3*first['F']-m-3
    if first['U']==1 or 3*first['F']-m-(3 if release_only else 0)<=249:
        label='NUMERICAL_NOMINATION' if first['U']==1 else ('READY_FOR_RELEASE' if release_only else 'READY_FOR_TRUNCATION');np.save(out/(label+'_q.npy'),q);(out/(label+'.json')).write_text(json.dumps(initial,indent=2)+'\n');return initial
    for round in range(rounds):
        next_states=[]
        for q,mm,nn,parent in states:
            q,mm,nn,s=compact(q,mm,nn);Y=s['Y'];rad=np.sum(Y*Y,1);raw_escape=Y@Y.T-rad[:,None];np.fill_diagonal(raw_escape,-np.inf);sr=int(np.argmax(rad));parents=raw_escape.argmax(1);indegree=np.bincount(parents[np.arange(len(Y))!=sr],minlength=len(Y));leaves=[int(s['A'][i]) for i in range(s['F']) if i!=sr and indegree[i]==0 and s['A'][i]>=mm+nn]
            for removed in leaves:
                H=np.delete(s['H'],removed,axis=0);fam=FlexibleTwoApexFamily(mm,nn);qq=fam.pack(H,q[-3:]);label=f'r{round:02d}_c{len(rows):04d}_drop{removed:03d}'
                try:qq,t,trace=balance(qq,fam,target)
                except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError) as e:rows.append(dict(label=label,parent=parent,removed=removed,error=repr(e)));continue
                row={k:t[k] for k in ['V','E','F','S','U','Pmax','Qmax','minimum_noncontact']};row.update(label=label,m=mm,n=nn,parent=parent,removed=removed,centroid_error=float(abs(t['g']-target).max()),post_truncation_edge_bound=3*t['F']-mm,post_release_edge_bound=3*t['F']-mm-3)
                np.save(out/(label+'_q.npy'),qq);(out/(label+'_mass_trace.json')).write_text(json.dumps(trace,indent=2)+'\n');rows.append(row)
                if t['S']==t['U']==1:
                    np.save(out/'NUMERICAL_NOMINATION_q.npy',qq);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');return row
                if t['S']!=1 or t['active_anchors']!=[0,1]:continue
                if unstable_limit is not None and t['U']>unstable_limit:continue
                key=(t['F'],t['Pmax']);next_states.append((key,qq,mm,nn,label))
                if best is None or key<best[0]:best=key,row;np.save(out/'best_q.npy',qq);(out/'best.json').write_text(json.dumps(row,indent=2)+'\n');print('ACTUAL_MASS_BALANCED_SECOND_STAR',row,flush=True)
                if t['U']==1:
                    np.save(out/'NUMERICAL_NOMINATION_q.npy',qq);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');return row
                if 3*t['F']-mm-(3 if release_only else 0)<=249:
                    ready='READY_FOR_RELEASE' if release_only else 'READY_FOR_TRUNCATION';np.save(out/(ready+'_q.npy'),qq);(out/(ready+'.json')).write_text(json.dumps(row,indent=2)+'\n');(out/'screen.json').write_text(json.dumps(rows,indent=2)+'\n');return row
        (out/'screen.json').write_text(json.dumps(rows,indent=2)+'\n')
        if not next_states:break
        next_states.sort(key=lambda x:x[0]);states=[(q,mm,nn,label) for _,q,mm,nn,label in next_states[:width]]
    (out/'FINITE_BRANCH_END.json').write_text(json.dumps(dict(seconds=time.time()-start,goal_complete=False),indent=2)+'\n');return None if best is None else best[1]

if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 44,int(sys.argv[4]) if len(sys.argv)>4 else 20)
