"""Exchange a physical own211 state for a one-stable family, or vice versa.
The actual volume centroid is integrated throughout. An exchange is not a goal
claim; all intermediate extra equilibria remain counted and saved.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,pathlib,numpy as np
from contact_multibasin_flow import UniqueStable,UniqueUnstable,run as multi
from contact_forest import correct
from contact_topology_continuation import run as continuation
from merge_contact_facets import run as merge_facets
from merge_contact_vertices import run as merge_vertices
from repair_contact_domain import run as domain_admit

def run(source,input,out,side='P',compound_cleanup=False,merit='local'):
    source=pathlib.Path(source);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);Base=UniqueStable if side=='P' else UniqueUnstable;Model=lambda chart:Base(chart,merit=merit);history=[]
    (out/'definition.json').write_text(json.dumps(dict(source=str(source.resolve()),input=str(pathlib.Path(input).resolve()),side=side,compound_cleanup=compound_cleanup,merit=merit,scope='Physical uniform-centroid class exchange; no exact goal claim'),indent=2))
    for stage in range(30):
        p=out/f'exchange{stage:03d}';p.mkdir();c=Model(source);z=np.load(input)['z'];z,e,ok=correct(c,z,p/'correction',steps=200,eps=1e-7,trust=.02,verbose=True,polish_margin=True,physical_retraction=True);np.savez(p/'exchanged.npz',z=z,X=e['X'],Q=e['Y']);input=p/'exchanged.npz';lengths=[float(np.min(np.linalg.norm(A[ed[:,0]]-A[ed[:,1]],axis=1))/np.sqrt(np.mean(A*A))) for A,ed in [(e['X'],c.eu),(e['Y'],c.es)]];row=dict(stage=stage,S=e['S'],U=e['U'],E=c.meta['E'],corrected=bool(ok),bars=e['bars'],lengths=lengths,chart=str(source.resolve()),input=str(input.resolve()));history.append(row);(out/'exchange-history.json').write_text(json.dumps(history,indent=2));(out/'exchange-summary.json').write_text(json.dumps(row,indent=2))
        if e['S']==e['U']==1:
            (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str(source.resolve()),input=str(input.resolve())),indent=2));return
        if ok:break
        if min(lengths)>=1e-7:return
        kind='vertices' if lengths[0]<lengths[1] else 'facets';body=p/('merge-'+kind);nU,nS=(len(e['X']),1) if side=='P' else (1,c.F)
        try:
            if kind=='vertices':merge_vertices(source,input,body,1e-7,nU,nS,'balanced')
            else:merge_facets(source,input,body,1e-7,nU,nS,'balanced',cleanup=compound_cleanup)
        except (ValueError,AssertionError,RuntimeError,np.linalg.LinAlgError) as error:
            (p/'INITIAL_PROPOSAL_UNADMITTED.json').write_text(json.dumps(dict(error=repr(error)),indent=2))
            if not (body/'chart/chart.json').exists():return
            try:domain_admit(body/'chart',body/'domain-admission',nU=nU,nS=nS,eps=1e-9,steps=80)
            except (ValueError,AssertionError,RuntimeError,np.linalg.LinAlgError) as err:
                (p/'DOMAIN_ADMISSION_FAILED.json').write_text(json.dumps(dict(error=repr(err)),indent=2));return
            input=body/'domain-admission/ADMITTED.npz'
            if not input.exists():return
        else:input=body/'realization.npz'
        source=body/'chart'
        if not 17<=Model(source).meta['E']<249:raise ValueError('exchange event violated edge budget')
    if not ok:return
    multi(source,input,out/'multibasin',etas=(.015,.004,.001,.0001,.00001),steps=110,side=side)
    if (out/'multibasin/POTENTIAL_OWN110.json').exists():(out/'POTENTIAL_OWN110.json').write_bytes((out/'multibasin/POTENTIAL_OWN110.json').read_bytes());return
    final=json.loads((out/'multibasin/latest-source.json').read_text());continuation(final['chart'],out/'multibasin/latest.npz',out/'strict-continuation',side=side,rounds=20,flow_steps=150)
    if (out/'strict-continuation/POTENTIAL_OWN110.json').exists():(out/'POTENTIAL_OWN110.json').write_bytes((out/'strict-continuation/POTENTIAL_OWN110.json').read_bytes())

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',required=True);p.add_argument('--input',required=True);p.add_argument('--out',required=True);p.add_argument('--side',choices=['P','Q'],default='P');p.add_argument('--compound-cleanup',action='store_true');p.add_argument('--merit',choices=['local','capacity'],default='local');a=p.parse_args();run(a.source,a.input,a.out,a.side,a.compound_cleanup,a.merit)
