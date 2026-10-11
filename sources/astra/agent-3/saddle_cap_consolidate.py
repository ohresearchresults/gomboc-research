"""Consolidate literal saddle-relay cap hulls with no more than 84 vertices.

The saved floating point coordinates define new physical convex hulls.  All
strict candidates are subsequently rounded to explicit rationals and audited
with their own filled-volume centroids.  A 121 result is a partial only.
"""
import argparse, json, time, hashlib
from pathlib import Path
import numpy as np
from gmpy2 import mpq
from polyhedral_stable_cap import Cap
from free_vertex_consolidate import run as consolidate
from exact_audit_vertices import audit
from exact_barcode_report import report

def run(scout, out, iterations):
    scout=Path(scout); out=Path(out); out.mkdir(parents=True,exist_ok=False)
    definition=json.loads((scout/'definition.json').read_text())
    source=Path(definition['source']); c=Cap(source,'saddle')
    assert hashlib.sha256((source/'audit.json').read_bytes()).hexdigest()==definition['audit_sha256']
    nominees=json.loads((scout/'best_by_Q.json').read_text())
    records=[]; start=time.time()
    for label in ['Q0.001','Q0.01','Q0.1','Q1e-05']:
        if label not in nominees: continue
        d=out/label; d.mkdir(); row=nominees[label]
        g,info=c.score(row['controls']); X=g['Z']
        assert len(X)<=84 and all(len(f)==3 for f in g['faces'])
        np.save(d/'initial.npy',X)
        (d/'construction.json').write_text(json.dumps(dict(
            source_audit=str((source/'audit.json').resolve()),
            source_audit_sha256=definition['audit_sha256'],
            nomination=row,actual_initial_diagnostics=info,
            scope='literal binary64 coordinates in initial.npy define a new homogeneous convex hull; all triangles are actual proposal facets, with at most84inputpoints',
        ),indent=2))
        consolidate(d/'initial.npy',d/'consolidate',iterations,'121')
        stages=json.loads((d/'consolidate/stages.json').read_text())
        candidates=sorted((s for s in stages if s['result']=='strict121 numerical'),key=lambda s:s['P'])
        record=dict(label=label,initial=info,stages=stages)
        if candidates:
            chosen=candidates[0]; exact=d/'exact_best_g11'
            a=audit(chosen['path'],exact,10**11); report(exact)
            b=json.loads((exact/'exact_bars.json').read_text())
            record.update(exact=str(exact),counts=a['counts'],weak=a['weak'],V=a['V'],E=a['E'],F=a['F'],P=max((float(mpq(v['depth']))for v in b['P']),default=0.),Q=max((float(mpq(v['depth']))for v in b['Q']),default=0.))
        record['seconds']=time.time()-start; records.append(record)
        (out/'trials.json').write_text(json.dumps(records,indent=2))
        print('SADDLE_CAP_CONSOLIDATED',record,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('scout');p.add_argument('out');p.add_argument('--iterations',type=int,default=5000);a=p.parse_args();run(a.scout,a.out,a.iterations)
