"""Exact finite support-offset changes at the remaining Q saddle and S facet.
Every sampled body is actually re-integrated and completely exactly audited.
No linearized mass surrogate or reference-centre census is used for acceptance.
"""
import argparse,json,time,hashlib
from pathlib import Path
from math import lcm,gcd
from gmpy2 import mpq
from exact_audit_vertices import check_B

def run(source,out):
 p=Path(source);out=Path(out);out.mkdir(parents=True,exist_ok=False);a=json.loads((p/'audit.json').read_text());b=json.loads((p/'exact_bars.json').read_text());bar=b['Q'][0];peak=bar['peak'];edge=bar['attaining_edge'];c=[mpq(v) for v in a['raw_centroid']];Q=[]
 for n,h in zip(a['normals'],a['offsets']):
  n=[mpq(v) for v in n];h=mpq(h)-sum(v*w for v,w in zip(n,c));Q.append([v/h for v in n])
 B=lambda x:json.dumps(x,default=str,sort_keys=True,separators=(',',':')).encode();(out/'source.json').write_bytes(B(dict(audit=str((p/'audit.json').resolve()),audit_sha256=hashlib.sha256((p/'audit.json').read_bytes()).hexdigest(),centred_supports=Q,centering=c,peak=peak,saddle_polar_edge=edge)));hist=[];t0=time.time();trial=0
 for pattern in ['saddle_pair','saddle_first','saddle_second','peak','pair_and_peak']:
  for t in [mpq(-1,5),mpq(-1,20),mpq(-1,100),mpq(-1,1000),mpq(1,10000),mpq(1,1000),mpq(1,100),mpq(3,100),mpq(6,100),mpq(9,100),mpq(1,10),mpq(11,100),mpq(12,100),mpq(14,100),mpq(17,100),mpq(1,5),mpq(1,4),mpq(1,3),mpq(1,2)]:
   offsets=[mpq(1)]*len(Q)
   for f in (edge if pattern in ['saddle_pair','pair_and_peak'] else edge[:1] if pattern=='saddle_first' else edge[1:] if pattern=='saddle_second' else []):offsets[f]=1-t
   if pattern in ['peak','pair_and_peak']:offsets[peak]=1+t
   rows=[]
   for n,h in zip(Q,offsets):
    den=lcm(*(int(v.denominator) for v in (*n,h)));r=[int(v*den) for v in (*n,h)];g=gcd(*r);rows.append([v//g for v in r])
   dest=out/f'trial{trial:03d}';dest.mkdir();raw={'H':rows};(dest/'raw.json').write_bytes(B(raw));(dest/'definition.json').write_bytes(B(dict(pattern=pattern,t=t,source='../source.json')));rep=check_B.run(raw);(dest/'audit.json').write_bytes(B(rep));summary={k:rep[k] for k in ['V','E','F','counts','weak']};summary.update(pattern=pattern,t=str(t),C2E=2*rep['E'],VplusEplusF=rep['V']+rep['E']+rep['F'],goal_met=rep['counts']==[1,1,0] and rep['weak']==[0,0,0] and 34<=2*rep['E']<500 and rep['V']+rep['E']+rep['F']<500);(dest/'summary.json').write_text(json.dumps(summary,indent=2));hist.append(summary);(out/'trials.json').write_text(json.dumps(hist,indent=2));print('EXACT_OFFSET',trial,summary,flush=True)
   if summary['goal_met']:(dest/'GOAL_CANDIDATE_COMPLETE.json').write_text(json.dumps(summary,indent=2));return
   trial+=1
 print('EXACT_OFFSET_SWEEP_DONE',len(hist),time.time()-t0,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');a=p.parse_args();run(a.input,a.out)
