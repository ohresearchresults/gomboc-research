"""Correct all physical root guards while bounding the largest remaining bar.
This is a fully coupled actual-centroid inequality system, not a bar cutoff.
The requested cap is a search constraint only; complete exact audit is separate.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,pathlib,json,numpy as np
from contact_forest import ContactModel,correct
from contact_persistence_flow import objective

class Bounded(ContactModel):
    def __init__(self,source,cap,side='Q',weight=10.):
        super().__init__(source,1 if side=='Q' else 2,2 if side=='Q' else 1,'local',exempt_junior=True);self.cap=cap;self.side=side;self.weight=weight
    def evaluate(self,z,jacobian=True):
        e=super().evaluate(z,jacobian);s=1 if self.side=='Q' else 0;largest=max((b['relative'] for b in e['bars'][s]),default=0);e['mechanical']=np.r_[e['mechanical'],self.weight*(self.cap-largest)+1e-7]
        if jacobian:
            _,g=objective(self,e,self.side);e['J']=np.vstack([e['J'],-self.weight*g])
        return e

def run(source,input,out,cap,side='Q',steps=180):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);c=Bounded(source,cap,side);z,e,ok=correct(c,np.load(input)['z'],out/'correction',steps=steps,eps=1e-7,trust=.005,verbose=True,polish_margin=True,physical_retraction=True);np.savez(out/'final.npz',z=z,X=e['X'],Q=e['Y']);r=dict(source=str(pathlib.Path(source).resolve()),input=str(pathlib.Path(input).resolve()),cap=cap,side=side,S=e['S'],U=e['U'],E=c.meta['E'],corrected=bool(ok),minimum=float(e['mechanical'].min()),bars=e['bars'],scope='Numerical actual-body correction; exact audit required');(out/'summary.json').write_text(json.dumps(r,indent=2))
    if e['S']==e['U']==1:
        (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str(pathlib.Path(source).resolve()),input=str((out/'final.npz').resolve())),indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',required=True);p.add_argument('--input',required=True);p.add_argument('--out',required=True);p.add_argument('--cap',type=float,required=True);p.add_argument('--side',choices=['P','Q'],default='Q');p.add_argument('--steps',type=int,default=180);a=p.parse_args();run(a.source,a.input,a.out,a.cap,a.side,a.steps)
