"""Retain the genuine high-valence apex of a literal vertex augmentation.
The supplied ordinary-H continuation requires <=84 supports. Here we instead
preserve all actual contacts, so the measured E<249 body can have >84 facets.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,pathlib,time,contextlib
import numpy as np
from stable_face_augmentation import halfspaces
from geometry import halfspace_mesh
from make_contact_atlas import make
from contact_forest import ContactModel,correct
from contact_persistence_flow import run as descend

def run(source,out,limit=6,selection='score'):
    source=pathlib.Path(source);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);P=np.load(source/'original.npz')['X'];h=json.loads((source/'screen.json').read_text());h=[r for r in h if 'E' in r and 17<=r['E']<249]
    if selection=='score':h=sorted(h,key=lambda r:r['score'])
    elif selection=='qdepth':h=sorted(h,key=lambda r:(max(r['Q'],default=0),r['score']))
    else:raise ValueError('unknown explicit selection rule')
    (out/'selection.json').write_text(json.dumps(dict(source=str(source.resolve()),selection=selection,limit=limit),indent=2));history=[];start=time.time()
    for trial,r in enumerate(h[:limit]):
        folder=out/f'trial{trial:02d}-sample{r["sample"]:05d}';folder.mkdir();q=halfspaces(np.r_[P,np.array(r['added_vertex'])[None]]);m=halfspace_mesh(q);Q=q[m['active']];X=m['X'];F=len(Q);E=len(m['edges']);faces=m['faces']
        proposal=dict(scope='Numerical full-contact representation of literal vertex augmentation, not exact certificate',V=len(X),E=E,F=F,faces=faces,edges=m['edges'].tolist(),active=list(range(F)),raw_vertices=[[str(x) for x in row] for row in X],raw_halfspaces=[[str(x) for x in row]+['1'] for row in Q],source=str((source/'screen.json').resolve()),sample=r['sample']);(folder/'proposal.json').write_text(json.dumps(proposal,indent=2));make(folder/'proposal.json',folder/'chart',balanced=True)
        try:
            c=ContactModel(folder/'chart',1,2,'local',exempt_junior=True);z=c.initial.copy();e=c.evaluate(z,False)
            with (folder/'calculation.log').open('w') as log,contextlib.redirect_stdout(log):
                z,e,ok=correct(c,z,folder/'strict-correction',steps=100,eps=1e-7,trust=.002,verbose=True,polish_margin=True,physical_retraction=True)
                np.savez(folder/'corrected.npz',z=z,X=e['X'],Q=e['Y'])
                if e['S']==e['U']==1 and e['mechanical'].min()>1e-9:
                    (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str((folder/'chart').resolve()),input=str((folder/'corrected.npz').resolve()))));return
                if ok:descend(folder/'chart',folder/'descent',side='Q',input=folder/'corrected.npz',steps=120)
            if (folder/'descent/POTENTIAL_OWN110.npz').exists():
                (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str((folder/'chart').resolve()),input=str((folder/'descent/POTENTIAL_OWN110.npz').resolve()))));return
            if (folder/'descent/latest.npz').exists():e=c.evaluate(np.load(folder/'descent/latest.npz')['z'],False)
            row=dict(trial=trial,sample=r['sample'],E=E,F=F,S=e['S'],U=e['U'],Pmax=max((b['relative'] for b in e['bars'][0]),default=0),Qmax=max((b['relative'] for b in e['bars'][1]),default=0),minimum=float(e['mechanical'].min()),strict_corrected=ok,seconds=time.time()-start)
        except (ValueError,AssertionError,RuntimeError,np.linalg.LinAlgError) as err:row=dict(trial=trial,sample=r['sample'],error=repr(err),seconds=time.time()-start)
        history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('CONTACT_AUGMENTATION',json.dumps(row),flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--source',required=True);ap.add_argument('--out',required=True);ap.add_argument('--limit',type=int,default=6);ap.add_argument('--selection',choices=['score','qdepth'],default='score');a=ap.parse_args();run(a.source,a.out,a.limit,a.selection)
