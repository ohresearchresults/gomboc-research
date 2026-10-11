"""Propose literal facet unions, then rebuild and exactly audit new bodies.
Distances only choose proposals; they never define coplanarity or true counts.
The full point/support contact equations define the new physical realization.
Method motivated by peer1's explicit contact events; pinned peeling code used.
"""
import argparse,json,time,hashlib,importlib.util
from pathlib import Path
from collections import Counter
import numpy as np
from gmpy2 import mpq
from contact_numpy import Chart
from contact_quota_polish import metric,run as quota
from contact_polynomial_flow import correct
from section_polish import roots
from exact_contact_audit import audit
from exact_barcode_report import report

def run(source,out,number):
 source=Path(source);out=Path(out);out.mkdir(parents=True,exist_ok=False);a=json.loads((source/'audit.json').read_text());gq=[mpq(v)for v in a['raw_centroid']];g=np.array(list(map(float,gq)));X=np.array([[float(mpq(v))for v in x]for x in a['raw_vertices']])-g;Y=[]
 for n,h in zip(a['normals'],a['offsets']):
  nn=[mpq(v)for v in n];hh=mpq(h)-sum(u*v for u,v in zip(nn,gq));Y.append([float(v/hh)for v in nn])
 Y=np.array(Y);faces=a['faces'];owners={tuple(e):[]for e in a['edges']}
 for f,cy in enumerate(faces):
  for i,j in zip(cy,cy[1:]+cy[:1]):owners[tuple(sorted((i,j)))].append(f)
 pairs=np.array(list(owners.values()));length=np.linalg.norm(Y[pairs[:,0]]-Y[pairs[:,1]],axis=1)/np.sqrt(np.mean(Y*Y));ids=np.argsort(length)[:number];peeling=Path('sources/peer_balanced_contact/make_contact_atlas.py');spec=importlib.util.spec_from_file_location('pinned_union_peeling',peeling);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);hist=[];start=time.time()
 for attempt,k in enumerate(ids):
  d=out/f'pair{attempt:02d}';d.mkdir();f1,f2=map(int,pairs[k]);row=dict(attempt=attempt,facets=[f1,f2],relative_polar_length=float(length[k]));boundary=[];sets=[set(zip(faces[f],faces[f][1:]+faces[f][:1]))for f in [f1,f2]]
  for i,j in sets[0]|sets[1]:
   if (j,i)not in sets[0]|sets[1]:boundary.append((i,j))
  nxt=dict(boundary);assert len(nxt)==len(boundary);cy=[min(nxt)]
  while nxt[cy[-1]]!=cy[0]:
   v=nxt[cy[-1]];assert v not in cy;cy.append(v)
  assert len(cy)==len(boundary);fc=[v for f,v in enumerate(faces)if f not in [f1,f2]]+[cy];normals=np.vstack(([q for f,q in enumerate(Y)if f not in [f1,f2]],(Y[f1]+Y[f2])/2));ed=sorted({tuple(sorted((i,j)))for f in fc for i,j in zip(f,f[1:]+f[:1])});assert len(X)-len(ed)+len(fc)==2;proposal=dict(scope='unverified facet-union topology and approximate coordinates; must reconstruct a valid physical body',V=len(X),E=len(ed),F=len(fc),raw_vertices=X.tolist(),raw_halfspaces=[q.tolist()+[1.]for q in normals],active=list(range(len(fc))),faces=fc,edges=ed,exact_parent=str(source.resolve()),parent_audit_sha256=hashlib.sha256((source/'audit.json').read_bytes()).hexdigest());(d/'proposal.json').write_text(json.dumps(proposal,indent=2))
  try:
   meta,q,A,*_=mod.make(d/'proposal.json',d/'peeling',balanced=True)
   for p in meta['plan']:p['fixed']={}
   grid=10**16;meta.update(free_controls=[int(round(v*grid))for v in q],grid=grid,proposal=str((d/'proposal.json').resolve()),scope='rational contact reconstruction defines a new body; source planes not approximately merged');(d/'construction.json').write_text(json.dumps(meta,indent=2));c=Chart(d/'construction.json');q=c.q0;gg=c.physical(q,require_valid=False);rr=[roots(gg['Z'],c.pe,2),roots(gg['H'],c.qe,1)]
   if not gg['valid']:
    W=metric(c,gg);q,good,it=correct(c,q,W,rr,1e-7,1e-9)
    if not good:raise ValueError('new contact proposal not admitted as a physical convex body')
   gg=c.physical(q);np.save(d/'physical_q.npy',q);a0=audit(d/'construction.json',d/'physical_q.npy',d/'exact_initial_g14',10**14);report(d/'exact_initial_g14');row.update(initial_counts=a0['counts'],V=a0['V'],E=a0['E'],F=a0['F'])
   quota(d/'exact_initial_g14/construction.json',d/'repair121',1,2,400,1e-7)
   if(d/'repair121/success_q.npy').exists():
    aa=audit(d/'exact_initial_g14/construction.json',d/'repair121/success_q.npy',d/'exact_repair_g14',10**14);report(d/'exact_repair_g14');row.update(result='complete exact new body',counts=aa['counts'],evidence=str(d/'exact_repair_g14'))
   else:row['result']='physical union but finite quota repair failed'
  except (ValueError,AssertionError,np.linalg.LinAlgError)as err:row.update(result='explicitly rejected proposal',error=repr(err))
  row['seconds']=time.time()-start;hist.append(row);(out/'trials.json').write_text(json.dumps(hist,indent=2));print('FACET_UNION_SCOUT',row,flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--number',type=int,default=8);a=p.parse_args();run(a.source,a.out,a.number)
