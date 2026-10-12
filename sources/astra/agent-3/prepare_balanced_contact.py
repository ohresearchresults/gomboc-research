"""Prepare a complete balanced contact chart from an own exact physical audit.
Uses the pinned peer1 scientific peeling implementation; preserves provenance.
The rounded free-coordinate start is a new body, checked for strict convexity.
"""
import argparse,json,hashlib,importlib.util
from pathlib import Path
import numpy as np
from contact_numpy import Chart

def prepare(source,out,grid):
 source=Path(source);out=Path(out);out.mkdir(parents=True,exist_ok=False);a=json.loads(source.read_text());bridge=dict(raw_vertices=a['raw_vertices'],raw_halfspaces=[n+[h] for n,h in zip(a['normals'],a['offsets'])],active=list(range(a['F'])),faces=a['faces'],edges=a['edges'],E=a['E']);(out/'source_for_peeling.json').write_text(json.dumps(bridge));path=Path('sources/peer_balanced_contact/make_contact_atlas.py');spec=importlib.util.spec_from_file_location('pinned_balanced_peeling',path);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);meta,q,A,*_=mod.make(out/'source_for_peeling.json',out/'peeling',balanced=True)
 for p in meta['plan']:p['fixed']={}
 meta.update(free_controls=[int(round(float(v)*grid)) for v in q],grid=grid,source_exact_audit=str(source.resolve()),source_exact_audit_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),peeling_source_sha256=hashlib.sha256(path.read_bytes()).hexdigest());(out/'construction.json').write_text(json.dumps(meta,indent=2));c=Chart(out/'construction.json');g=c.physical(c.q0);np.save(out/'initial_q.npy',c.q0);full,D=c.reconstruct(c.q0);sv=np.linalg.svd(D.reshape(-1,c.d),compute_uv=False);report=dict(V=c.V,E=meta['E'],F=c.F,d=c.d,depth=meta['max_depth'],max_source_coordinate_error=float(np.max(abs(full-A))),chart_derivative_condition=float(max(sv)/min(sv)),contact_error=g['contact_error'],min_gap=float(min(g['noncontact'])),min_turn=g['min_turn'],status='numerical strict physical realization, exact audit required for any census claim');(out/'check.json').write_text(json.dumps(report,indent=2));print('BALANCED_CONTACT_READY',out,report,flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source_audit');p.add_argument('out');p.add_argument('--grid',type=int,default=10**16);a=p.parse_args();prepare(a.source_audit,a.out,a.grid)
