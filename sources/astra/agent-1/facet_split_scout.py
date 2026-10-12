"""Release a planar face into two true facets and deform the physical body.

The diagonal is a deliberate new geometric degree of freedom, not integration
triangulation. A strict convex realization with distinct supporting planes must
be admitted before equilibrium search. Every endpoint requires exact auditing.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,pathlib,time
import numpy as np
from contact_forest import ContactModel,correct
from make_contact_atlas import make
from repair_contact_domain import run as admit
from contact_persistence_flow import run as descend

def split(c,e,f,i,j,out):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);cy=c.meta['faces'][f];i,j=sorted((i,j));children=[cy[i:j+1],cy[j:]+cy[:i+1]]
    if min(map(len,children))<3:raise ValueError('invalid face diagonal')
    faces=[row for k,row in enumerate(c.meta['faces']) if k!=f]+children;Y=np.r_[np.delete(e['Y'],f,0),e['Y'][[f,f]]];X=e['X'];edges=sorted({tuple(sorted((a,b))) for row in faces for a,b in zip(row,row[1:]+row[:1])})
    if len(edges)!=c.meta['E']+1 or len(X)-len(edges)+len(faces)!=2:raise ValueError('invalid facet split complex')
    if len(edges)>=249:raise ValueError('split would exceed conservative edge budget')
    r=dict(scope='UNVERIFIED coincident-plane split proposal, not a physical endpoint',source_facet=f,source_diagonal=[cy[i],cy[j]],V=len(X),E=len(edges),F=len(faces),faces=faces,edges=edges,active=list(range(len(faces))),raw_vertices=[[str(a) for a in v] for v in X],raw_halfspaces=[[str(a) for a in q]+['1'] for q in Y]);(out/'proposal.json').write_text(json.dumps(r,indent=2))
    make(out/'proposal.json',out/'chart',quality_first=True)
    admit(out/'chart',out/'convex-admission',nU=2,nS=1,eps=1e-8,steps=60)
    p=out/'convex-admission/ADMITTED.npz'
    if not p.exists():raise ValueError('no strict convex split realization admitted')
    model=ContactModel(out/'chart',2,1,'local',exempt_junior=True);z=np.load(p)['z'];ee=model.evaluate(z,False)
    if ee['S']>1 or ee['U']>2 or ee['mechanical'].min()<8e-8:
        z,ee,ok=correct(model,z,out/'strict-correction',steps=55,eps=1e-7,trust=.001,verbose=False,polish_margin=True,physical_retraction=True)
        if not ok:raise ValueError('split body did not recover the target strict class')
    np.savez(out/'admitted-strict.npz',z=z,X=ee['X'],Q=ee['Y'])
    return out/'chart',out/'admitted-strict.npz'

def run(source,input,out,limit=8):
    c=ContactModel(source,2,1,'local',exempt_junior=True);e=c.evaluate(np.load(input)['z'],False);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);start=time.time();history=[];junior=e['roots'][0][1];stable=e['roots'][1][0];candidates=[]
    for f,cy in enumerate(c.meta['faces']):
        if len(cy)<4 or f==stable:continue
        X=e['X'][cy];area=np.linalg.norm(sum(np.cross(X[k]-X[0],X[k+1]-X[0]) for k in range(1,len(cy)-1)))/2
        for i in range(len(cy)):
            j=(i+len(cy)//2)%len(cy)
            if i>j:continue
            candidates.append((0 if junior in cy else 1,-area,f,i,j))
    chosen=[];used=set()
    for _,_,f,i,j in sorted(candidates):
        if f in used:continue
        used.add(f);chosen.append((f,i,j))
        if len(chosen)==limit:break
    for trial,(f,i,j) in enumerate(chosen):
        folder=out/f'trial{trial:02d}-face{f:03d}'
        try:
            chart,p=split(c,e,f,i,j,folder)
            model=ContactModel(chart,2,1,'local',exempt_junior=True);ee=model.evaluate(np.load(p)['z'],False)
            if ee['S']==ee['U']==1:
                (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str(chart.resolve()),input=str(p.resolve())),indent=2));return
            descend(chart,folder/'descent',input=p,side='P',steps=100)
            if (folder/'descent/POTENTIAL_OWN110.npz').exists():
                (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str(chart.resolve()),input=str((folder/'descent/POTENTIAL_OWN110.npz').resolve())),indent=2));return
            p=folder/'descent/latest.npz';ee=model.evaluate(np.load(p)['z'],False);row=dict(trial=trial,facet=f,diagonal=[i,j],E=model.meta['E'],S=ee['S'],U=ee['U'],P=max([b['relative'] for b in ee['bars'][0]],default=0),minimum=float(ee['mechanical'].min()),source=str(pathlib.Path(source).resolve()),chart=str(chart.resolve()),input=str(p.resolve()),seconds=time.time()-start)
        except (ValueError,AssertionError,RuntimeError,np.linalg.LinAlgError) as err:row=dict(trial=trial,facet=f,diagonal=[i,j],error=repr(err),seconds=time.time()-start)
        history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('FACET_SPLIT_TRIAL',row,flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--source',required=True);ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--limit',type=int,default=8);a=ap.parse_args();run(a.source,a.input,a.out,a.limit)
