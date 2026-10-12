"""Successive exact own211 cap improvements with one existing mass compensator.

Every accepted stage is a new fully audited homogeneous physical polyhedron.
True hull vertices, not submitted interior controls, seed the next cycle.
No121/211 body is treated as the requested Figure.
"""
import argparse,json,time,hashlib
from pathlib import Path
import numpy as np
from gmpy2 import mpq
from thales_cap_relay import run as scout
from vertex_mass_compensation import run as compensate
from mass_neutral_vertex_flow import run as flow
from exact_barcode_report import report

def run(source,out,rounds,seed):
    source=Path(source);out=Path(out);out.mkdir(parents=True,exist_ok=False);hist=[];start=time.time()
    for k in range(rounds):
        a=json.loads((source/'audit.json').read_text());bars=json.loads((source/'exact_bars.json').read_text());assert a['counts']==[2,1,1]and a['weak']==[0,0,0]and not bars['P'];prior=float(mpq(bars['Q'][0]['depth']))
        if a['V']>=84:print('COMPENSATED_CAP_POINT_BUDGET_REACHED',source,flush=True);break
        d=out/f'round{k:02d}';d.mkdir();c=[mpq(v)for v in a['raw_centroid']];X=np.array([[float(mpq(v)-c[j])for j,v in enumerate(row)]for row in a['raw_vertices']]);np.save(d/'seed.npy',X);(d/'source.json').write_text(json.dumps(dict(source=str(source.resolve()),audit_sha256=hashlib.sha256((source/'audit.json').read_bytes()).hexdigest(),Q=prior),indent=2))
        scout(d/'seed.npy',d/'scout',8000,seed+k*73,True);compensate(d/'scout',d/'compensation',22);recs=json.loads((d/'compensation/results.json').read_text());nom=[r for r in recs if 'exact'in r];valid=[]
        for r in nom:
            p=Path(r['exact']);aa=json.loads((p/'audit.json').read_text());bb=json.loads((p/'exact_bars.json').read_text())
            if aa['counts']==[2,1,1]and aa['weak']==[0,0,0]and len(bb['Q'])==1 and not bb['P']:valid.append((float(mpq(bb['Q'][0]['depth'])),p,r))
        row=dict(round=k,prior_Q=prior,source=str(source))
        if not valid:
            row['result']='no strict exact211 from the finite compensated cap batch';hist.append(row);(out/'history.json').write_text(json.dumps(hist,indent=2));break
        q,p,r=min(valid,key=lambda x:x[0]);winner=r['best'];case=d/'compensation'/f"case{r['case']}";comp=winner['compensation_vertex'];flow(case/f'closed_vertex{comp}.npy',d/'neutral_flow',comp,-1,450);fp=d/'neutral_flow/exact_endpoint_g12';fa=json.loads((fp/'audit.json').read_text());fb=json.loads((fp/'exact_bars.json').read_text())
        if fa['counts']==[2,1,1]and fa['weak']==[0,0,0]and len(fb['Q'])==1 and not fb['P']:
            fq=float(mpq(fb['Q'][0]['depth']))
            if fq<q:q,p=fq,fp
        if q<prior-1e-6:
            aa=json.loads((p/'audit.json').read_text());source=p;row.update(result='strict exact211 improvement, NOTFigure',Q=q,exact=str(p),V=aa['V'],E=aa['E'],F=aa['F'])
        else:row.update(result='no strictly smaller exact Q in this finite batch',best_Q=q)
        row['seconds']=time.time()-start;hist.append(row);(out/'history.json').write_text(json.dumps(hist,indent=2));print('COMPENSATED_CAP_CYCLE',row,flush=True)
        if row['result']!='strict exact211 improvement, NOTFigure':break

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--rounds',type=int,default=8);p.add_argument('--seed',type=int,default=83701);a=p.parse_args();run(a.source,a.out,a.rounds,a.seed)
