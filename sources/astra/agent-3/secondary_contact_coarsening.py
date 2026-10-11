"""Second topology event from a saved, explicitly unverified contact proposal.

The intermediate can fail convexity. Its formal signs are not evidence for a
physical body. Only a new fully convex realization followed by exact native
hull, filled mass and weak-contact auditing can be admitted.
"""
import argparse,json,hashlib,importlib.util
from pathlib import Path
import numpy as np
from contact_numpy import Chart
from strict110_contact_coarsening import proposals,realize
from exact_contact_audit import audit
from exact_barcode_report import report

def run(source,qsource,out,number,steps):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);c=Chart(source);q=np.load(qsource);g=c.physical(q,require_valid=False);a=dict(V=c.V,F=c.F,E=c.meta['E'],faces=c.faces,edges=c.pe.tolist());pp=proposals(a,g['X'],g['Y'],number);(out/'source.json').write_text(json.dumps(dict(construction=str(Path(source).resolve()),construction_sha256=hashlib.sha256(Path(source).read_bytes()).hexdigest(),q=str(Path(qsource).resolve()),q_sha256=hashlib.sha256(Path(qsource).read_bytes()).hexdigest(),valid=bool(g['valid']),scope='source is an unverified algebraic contact proposal; no physical own-census or complexity result is asserted for it'),indent=2));spec=importlib.util.spec_from_file_location('secondary_contact_peel','sources/peer_balanced_contact/make_contact_atlas.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);rows=[]
 for k,p in enumerate(pp):
  d=out/f'case{k:02d}';d.mkdir();row={key:p[key]for key in ['kind','pair','length','gain']};proposal=dict(V=len(p['X']),F=len(p['Y']),E=p['E'],faces=p['faces'],edges=p['edges'],raw_vertices=p['X'].tolist(),raw_halfspaces=[list(y)+[1.]for y in p['Y']],active=list(range(len(p['Y']))),source=str((out/'source.json').resolve()),scope='second unverified topology proposal; full physical admission required');(d/'proposal.json').write_text(json.dumps(proposal,indent=2))
  try:
   meta,qq,*_=mod.make(d/'proposal.json',d/'peeling',balanced=True)
   for plan in meta['plan']:plan['fixed']={}
   grid=10**16;meta.update(free_controls=[int(round(v*grid))for v in qq],grid=grid,proposal=str((d/'proposal.json').resolve()));(d/'construction.json').write_text(json.dumps(meta,indent=2));cc=Chart(d/'construction.json');r=realize(cc,d/'realize',steps,1e-9,1e-12)
   if r is None:row['result']='finite physical own110 realization failed'
   else:
    aa=audit(d/'construction.json',d/'realize/success_q.npy',d/'exact_g16',10**16);report(d/'exact_g16');row.update(result='fully audited exact physical candidate',V=aa['V'],E=aa['E'],F=aa['F'],counts=aa['counts'],weak=aa['weak'],exact=str((d/'exact_g16').resolve()))
    if aa['counts']==[1,1,0]and aa['weak']==[0,0,0]:
     (out/'accepted.json').write_text(json.dumps(row,indent=2));rows.append(row);(out/'results.json').write_text(json.dumps(rows,indent=2));print('SECONDARY_EXACT_OWN110',row,flush=True);return
  except (ValueError,AssertionError,np.linalg.LinAlgError)as err:row.update(result='explicitly rejected proposal',error=repr(err))
  rows.append(row);(out/'results.json').write_text(json.dumps(rows,indent=2));print('SECONDARY_CONTACT_RESULT',row,flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('q');p.add_argument('out');p.add_argument('--number',type=int,default=6);p.add_argument('--steps',type=int,default=90);a=p.parse_args();run(a.source,a.q,a.out,a.number,a.steps)
