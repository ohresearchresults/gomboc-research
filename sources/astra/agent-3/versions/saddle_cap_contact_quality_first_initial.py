"""Full physical contact-chart research for saddle-point hull augmentations.

Maximal old polygons and new horizon triangles are explicit incidence data.
No nearly coplanar triangles are silently counted as one polygon.  Peeling
only parameterizes this incidence; convexity and all equilibria are readmitted
on the newly reconstructed homogeneous body.
"""
import argparse,json,time,hashlib,importlib.util
from pathlib import Path
import numpy as np
from gmpy2 import mpq
from polyhedral_stable_cap import Cap
from contact_numpy import Chart
from contact_quota_polish import run as quota
from contact_polynomial_flow import run as flow
from exact_contact_audit import audit
from exact_barcode_report import report

def exact_record(construction,q,out):
    a=audit(construction,q,out,10**14);report(out)
    b=json.loads((out/'exact_bars.json').read_text())
    return dict(path=str(out),V=a['V'],E=a['E'],F=a['F'],counts=a['counts'],weak=a['weak'],P=max((float(mpq(v['depth']))for v in b['P']),default=0.),Q=max((float(mpq(v['depth']))for v in b['Q']),default=0.))

def run(scout,out,steps):
    scout=Path(scout);out=Path(out);out.mkdir(parents=True,exist_ok=False)
    de=json.loads((scout/'definition.json').read_text());source=Path(de['source'])
    assert hashlib.sha256((source/'audit.json').read_bytes()).hexdigest()==de['audit_sha256']
    cap=Cap(source,'saddle');nominations=json.loads((scout/'best_by_Q.json').read_text())
    peeling=Path('sources/peer_balanced_contact/make_contact_atlas.py')
    spec=importlib.util.spec_from_file_location('pinned_cap_peeling',peeling);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    hist=[];start=time.time()
    for label in ['Q0.001','Q0.01','Q1e-05','Q0.1','Q1e-07','Q1e-10']:
        if label not in nominations:continue
        for quality in [True,False]:
            d=out/(label+('_quality'if quality else'_balanced'));d.mkdir()
            g,info=cap.score(nominations[label]['controls'])
            proposal=dict(V=g['V'],E=g['E'],F=g['F'],raw_vertices=g['Z'].tolist(),raw_halfspaces=[n.tolist()+[1.]for n in g['H']],active=list(range(g['F'])),faces=g['faces'],edges=g['pe'].tolist(),scope='full physical convex-hull proposal; chart reconstruction requires independent readmission',source=str(source.resolve()),nomination=nominations[label],audit_sha256=de['audit_sha256'])
            (d/'proposal.json').write_text(json.dumps(proposal,indent=2));row=dict(label=label,quality_first=quality,initial=info)
            try:
                meta,q,*_=mod.make(d/'proposal.json',d/'peeling',balanced=not quality,quality_first=quality)
                for p in meta['plan']:p['fixed']={}
                grid=10**16;meta.update(free_controls=[int(round(v*grid))for v in q],grid=grid,proposal=str((d/'proposal.json').resolve()))
                (d/'construction.json').write_text(json.dumps(meta,indent=2));c=Chart(d/'construction.json');gg=c.physical(c.q0)
                np.save(d/'initial_q.npy',c.q0)
                row['initial_exact']=exact_record(d/'construction.json',d/'initial_q.npy',d/'exact_initial_g14')
                quota(d/'exact_initial_g14/construction.json',d/'repair121',1,2,400,1e-7)
                if not(d/'repair121/success_q.npy').exists():raise ValueError('finite quota121 correction did not admit a candidate')
                exact=d/'exact_repaired_g14';row['repaired']=exact_record(d/'exact_initial_g14/construction.json',d/'repair121/success_q.npy',exact)
                a=row['repaired']
                if a['counts']==[1,1,0]and a['weak']==[0,0,0]and 34<=2*a['E']<500 and a['V']+a['E']+a['F']<500:
                    (out/'POTENTIAL_GOAL_REQUIRES_SOURCE_REVIEW.json').write_text(json.dumps(row,indent=2));return
                flow(exact/'construction.json',d/'flow121',steps,.03,1e-7,1e-9,'121',True)
                qpath=d/'flow121/potential_q.npy'
                if not qpath.exists():qpath=d/'flow121/latest_q.npy'
                row['flow_exact']=exact_record(exact/'construction.json',qpath,d/'exact_flow_g14')
                row['result']='complete exact endpoint; census determines scope'
            except (ValueError,AssertionError,np.linalg.LinAlgError) as err:
                row.update(result='explicit rejected proposal or finite correction failure',error=repr(err))
            row['seconds']=time.time()-start;hist.append(row);(out/'trials.json').write_text(json.dumps(hist,indent=2));print('SADDLE_CAP_CONTACT',row,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('scout');p.add_argument('out');p.add_argument('--steps',type=int,default=250);a=p.parse_args();run(a.scout,a.out,a.steps)
