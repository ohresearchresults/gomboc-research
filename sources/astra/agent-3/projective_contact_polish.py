"""Exact projective body then full-contact mechanical correction and descent.

Every physical change has its own rational reconstruction and mass audit.
The projective transformation preserves the source incidence, including all
nontriangular facets; subsequent full contact controls retain that incidence.
"""
import argparse,json,importlib.util,time
from pathlib import Path
import numpy as np
from gmpy2 import mpq
from exact_projective_audit import audit as projective_audit
from exact_contact_audit import audit as contact_audit
from exact_barcode_report import report
from contact_numpy import Chart
from contact_quota_polish import run as quota
from contact_polynomial_flow import run as flow

def run(source,out,target,steps,eps):
    source=Path(source);out=Path(out);out.mkdir(parents=True,exist_ok=False)
    a=projective_audit(source,out/'exact_projective');report(out/'exact_projective')
    g=[mpq(v)for v in a['raw_centroid']];X=np.array([[float(mpq(v)-g[j])for j,v in enumerate(x)]for x in a['raw_vertices']]);Y=[]
    for n,h in zip(a['normals'],a['offsets']):
        n=[mpq(v)for v in n];hh=mpq(h)-sum(u*v for u,v in zip(n,g));Y.append([float(v/hh)for v in n])
    p=dict(V=a['V'],E=a['E'],F=a['F'],raw_vertices=X.tolist(),raw_halfspaces=[n+[1.]for n in Y],active=list(range(a['F'])),faces=a['faces'],edges=a['edges'])
    (out/'proposal.json').write_text(json.dumps(p,indent=2));file=Path('sources/peer_balanced_contact/make_contact_atlas.py');spec=importlib.util.spec_from_file_location('pinned_projective_contact_peeling',file);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);meta,q,*_=mod.make(out/'proposal.json',out/'peeling',balanced=True)
    for p in meta['plan']:p['fixed']={}
    grid=10**16;meta.update(grid=grid,free_controls=[int(round(v*grid))for v in q]);(out/'construction.json').write_text(json.dumps(meta,indent=2));c=Chart(out/'construction.json');c.physical(c.q0);np.save(out/'q0.npy',c.q0)
    a=contact_audit(out/'construction.json',out/'q0.npy',out/'exact_initial',10**14);report(out/'exact_initial')
    S,U=(2,1)if target=='211'else(1,2);quota(out/'exact_initial/construction.json',out/'repair',S,U,600,eps)
    qp=out/'repair/success_q.npy'
    if not qp.exists():print('PROJECTIVE_CONTACT_FINITE_REPAIR_FAILED',out,flush=True);return
    a=contact_audit(out/'exact_initial/construction.json',qp,out/'exact_repaired',10**14);report(out/'exact_repaired')
    if a['counts']==[1,1,0]and a['weak']==[0,0,0]:print('PROJECTIVE_CONTACT_EXACT_POTENTIAL_REVIEW',out/'exact_repaired',flush=True);return
    flow(out/'exact_repaired/construction.json',out/'flow',steps,.03,eps,1e-9,target,True)
    qp=out/'flow/potential_q.npy'
    if not qp.exists():qp=out/'flow/latest_q.npy'
    a=contact_audit(out/'exact_repaired/construction.json',qp,out/'exact_final',10**14);report(out/'exact_final');print('PROJECTIVE_CONTACT_EXACT_ENDPOINT',out,a['counts'],a['weak'],flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--target',choices=['121','211'],default='211');p.add_argument('--steps',type=int,default=500);p.add_argument('--epsilon',type=float,default=1e-7);a=p.parse_args();run(a.source,a.out,a.target,a.steps,a.epsilon)
