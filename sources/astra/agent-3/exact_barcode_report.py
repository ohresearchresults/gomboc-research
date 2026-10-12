"""Exact rational finite radial bars on a complete physical audit.
Uses the native recovered N40 tied-level graph algorithm, with GMP rationals.
Every depth is normalized by its own finite birth radius squared.
"""
import argparse,json,hashlib
from pathlib import Path
from gmpy2 import mpq
from sources.N40.N40_RECOVER import bars,sub,mul,dot

def report(directory):
 p=Path(directory);raw=(p/'audit.json').read_bytes();a=json.loads(raw);g=tuple(mpq(v) for v in a['raw_centroid']);X=[sub(tuple(mpq(v) for v in row),g) for row in a['raw_vertices']];owners={tuple(e):[] for e in a['edges']}
 for f,vs in enumerate(a['faces']):
  for i,j in zip(vs,vs[1:]+vs[:1]):owners[tuple(sorted((i,j)))].append(f)
 assert all(len(v)==2 for v in owners.values())
 H=[mul(tuple(mpq(v) for v in n),1/(mpq(h)-dot(tuple(mpq(v) for v in n),g))) for n,h in zip(a['normals'],a['offsets'])];P=bars(X,a['edges']);Q=bars(H,list(owners.values()));assert len(P)==a['counts'][1]-1 and len(Q)==a['counts'][0]-1
 d=dict(audit_sha256=hashlib.sha256(raw).hexdigest(),normalization='each finite bar divided by its own birth radius squared',P=P,Q=Q);(p/'exact_bars.json').write_text(json.dumps(d,default=str,indent=2));print('EXACT_BARS',directory,{'P':[float(x['depth']) for x in P],'Q':[float(x['depth']) for x in Q]},flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('directories',nargs='+');a=p.parse_args()
 for d in a.directories:report(d)
