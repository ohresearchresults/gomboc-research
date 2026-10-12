"""Exact physical hull of a literal subset of an already exact convex body.

All parent inequalities remain valid and guarantee boundedness. Numerical
facets nominate extra planes only. Rational halfspace inclusion plus an exact
vertex-set equality proves that the final body is exactly the requested hull.
"""
import argparse,json,itertools,hashlib,time
from pathlib import Path
from math import lcm,gcd
import numpy as np
from scipy.spatial import ConvexHull
from gmpy2 import mpq
from exact_audit_vertices import check_B,dot,cross,sub
from exact_barcode_report import report

def run(source,ids,out):
 source=Path(source);out=Path(out);out.mkdir(parents=True,exist_ok=False);a=json.loads((source/'audit.json').read_text());ids=list(map(int,ids));assert len(ids)==len(set(ids));original=[tuple(map(mpq,a['raw_vertices'][i]))for i in ids];mean=tuple(mpq(float(v))for v in np.array(original,float).mean(0));P=[sub(p,mean)for p in original];planes=[];inc=[set()for _ in range(a['V'])]
 for f,cy in enumerate(a['faces']):
  for i in cy:inc[i].add(f)
 for nn,hh in zip(a['normals'],a['offsets']):
  n=tuple(map(mpq,nn));h=mpq(hh)-dot(n,mean);assert h>0;planes.append((n,h))
 hull=ConvexHull(np.array(P,float));new_triples=[]
 for tri in hull.simplices:
  labels=[ids[i]for i in tri]
  if set.intersection(*(inc[i]for i in labels)):continue
  p,q,r=[P[i]for i in tri];n=cross(sub(q,p),sub(r,p));h=dot(n,p)
  if h<0:n=tuple(-v for v in n);h=-h
  assert h>0 and all(dot(n,x)<=h for x in P),'numerical facet nomination was not exactly supporting';planes.append((n,h));new_triples.append(labels)
 rows=set()
 for n,h in planes:
  row=(*n,h);D=lcm(*(int(v.denominator)for v in row));ii=tuple(int(v*D)for v in row);gg=gcd(*ii);rows.add(tuple(v//gg for v in ii))
 raw=dict(H=sorted(rows));B=lambda x:json.dumps(x,default=str,sort_keys=True,separators=(',',':')).encode();(out/'raw.json').write_bytes(B(raw));(out/'coordinates.json').write_bytes(B(dict(points=P,source_vertex_ids=ids,density=1)));(out/'construction.json').write_bytes(B(dict(source=str(source.resolve()),source_audit_sha256=hashlib.sha256((source/'audit.json').read_bytes()).hexdigest(),source_vertex_ids=ids,translation=mean,new_plane_triples=new_triples,definition='literal convex hull of these exact parent vertices, uniformly filled; literal dyadic interior translation, verified against every exact supporting plane')));t=time.time();r=check_B.run(raw);found={tuple(map(mpq,p))for p in r['raw_vertices']};assert found==set(P),'exact halfspace hull differs from requested literal vertex subset';lookup={p:i for p,i in zip(P,ids)};r['source_vertex_ids']=[lookup[tuple(map(mpq,p))]for p in r['raw_vertices']];(out/'audit.json').write_bytes(B(r));s={k:r[k]for k in ['V','E','F','counts','weak','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};s.update(C_2E=2*r['E'],VplusEplusF=r['V']+r['E']+r['F'],goal_met=r['counts']==[1,1,0]and r['weak']==[0,0,0]and 34<=2*r['E']<500 and r['V']+r['E']+r['F']<500,audit_sha256=hashlib.sha256((out/'audit.json').read_bytes()).hexdigest(),seconds=time.time()-t);(out/'summary.json').write_text(json.dumps(s,indent=2));report(out);print('EXACT_LITERAL_VERTEX_SUBSET',out,s,flush=True)
 if s['goal_met']:
  from goal_nomination import ExactGoalCandidateFound
  raise ExactGoalCandidateFound('Exact literal vertex subset Figure at '+str(out))
 return r

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('ids');p.add_argument('out');a=p.parse_args();run(a.source,json.loads(Path(a.ids).read_text()),a.out)
