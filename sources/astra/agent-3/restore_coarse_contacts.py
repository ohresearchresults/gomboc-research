"""Restore literal maximal-face contacts after free-coordinate point retirement.

Parent point identities are replayed from saved data with exact array checks.
An exact literal subset supplies the prospective polyhedral graph. Corrected
free points seed new contact equations; no approximate coplanarity is counted.
"""
import argparse,json,hashlib,importlib.util
from pathlib import Path
import numpy as np
from vertex_geometry import geometry
from literal_vertex_subset import run as subset
from contact_numpy import Chart
from strict110_contact_coarsening import realize
from exact_contact_audit import audit
from exact_barcode_report import report

def replay(source,stages):
 source=Path(source);history=json.loads((source/'history.json').read_text());ids=np.arange(len(np.load(source/'initial.npy')));rows=[];last=None
 for row in history[:stages]:
  assert 'candidate'in row;stage=source/f"stage{row['stage']:03d}";parent=np.load(stage/'parent.npy');assert len(parent)==len(ids);d=Path(row['candidate']).parent;ids=np.delete(ids,row['removed']);raw=d/'repair/success.npy'
  if not raw.exists():raw=d/'numerical_own110.npy'
  X=np.load(raw);g=geometry(X,False);ids=ids[g['vertices']];candidate=np.load(row['candidate']);assert np.array_equal(X[g['vertices']],candidate),'stored point identity mismatch';last=candidate;rows.append(dict(stage=row['stage'],candidate=row['candidate'],source_ids=ids.tolist(),sha256=hashlib.sha256(Path(row['candidate']).read_bytes()).hexdigest()))
 assert last is not None;return ids,last,rows

def run(parent,retirement,out,stages):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);ids,X,rows=replay(retirement,stages);(out/'point_identity_replay.json').write_text(json.dumps(rows,indent=2));(out/'retained_original_ids.json').write_text(json.dumps(ids.tolist()));a=subset(parent,ids,out/'exact_original_subset');lookup={int(i):x for i,x in zip(ids,X)};XX=np.array([lookup[i]for i in a['source_vertex_ids']]);faces=a['faces'];YY=np.array([np.linalg.lstsq(XX[cy],np.ones(len(cy)),rcond=None)[0]for cy in faces]);p=dict(V=a['V'],E=a['E'],F=a['F'],raw_vertices=XX.tolist(),raw_halfspaces=[list(y)+[1.]for y in YY],active=list(range(a['F'])),faces=faces,edges=a['edges'],scope='unverified exact-contact topology seeded by freely deformed physical points; planes must be reconstructed and audited, never approximately merged',topology_source=str((out/'exact_original_subset').resolve()),point_source=rows[-1]);(out/'proposal.json').write_text(json.dumps(p,indent=2));spec=importlib.util.spec_from_file_location('restored_contact_peel','sources/peer_balanced_contact/make_contact_atlas.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);meta,q,*_=mod.make(out/'proposal.json',out/'peeling',balanced=True)
 for plan in meta['plan']:plan['fixed']={}
 grid=10**16;meta.update(free_controls=[int(round(v*grid))for v in q],grid=grid,proposal=str((out/'proposal.json').resolve()));(out/'construction.json').write_text(json.dumps(meta,indent=2));c=Chart(out/'construction.json');q=realize(c,out/'realize',350,1e-9,1e-11)
 if q is not None:
  aa=audit(out/'construction.json',out/'realize/success_q.npy',out/'exact_restored_g16',10**16);report(out/'exact_restored_g16');print('RESTORED_CONTACT_EXACT',{k:aa[k]for k in ['V','E','F','counts','weak']},flush=True)
 else:print('RESTORED_CONTACT_FINITE_FAILURE',out,flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('parent');p.add_argument('retirement');p.add_argument('out');p.add_argument('--stages',type=int,default=7);a=p.parse_args();run(a.parent,a.retirement,a.out,a.stages)
