"""Source-only exact recovery, independent A/B, own-mass and scoped certificates.
Outputs must be fresh. This script reports nonwinners honestly, never promotes121.
"""
import argparse,json,hashlib,time,sys
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import RECONSTRUCT,check_A,check_B,centred_mass,proof_checks
from recover_cases import generator
from derive import blob
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent
PATH612=[82,85,88,91,96,99,103,106,110,113,117,120,125,130,144,145,147,148,149,150,151,153,155,156,158,159,161,163,164,166,168,171,173,172,170,169,167,165,162,160,157,154,152,100,94]

def digest(b):return hashlib.sha256(b).hexdigest()
def bit(x):
 q=Q(x);return max(abs(q.numerator).bit_length(),q.denominator.bit_length())
def stats(a,raw):
 X=[tuple(map(Q,r)) for r in a['raw_vertices']];g=tuple(map(Q,a['raw_centroid']));deg=Counter(i for e in a['edges'] for i in e)
 return dict(volume_decimal=float(Q(a['ordinary_volume'])),centroid_decimal=list(map(float,g)),facet_histogram=dict(Counter(map(len,a['faces']))),degree_histogram=dict(Counter(deg.values())),bits=dict(H=max(abs(v).bit_length() for r in raw['H'] for v in r),vertices=max(bit(v) for r in X for v in r),volume=bit(a['ordinary_volume']),moments=max(map(bit,a['raw_first_moments'])),centroid=max(map(bit,g)),centred_vertices=max(bit(v-c) for r in X for v,c in zip(r,g))))

def forest612(a):
 X=[tuple(map(Q,r)) for r in a['raw_vertices']];g=tuple(map(Q,a['raw_centroid']));adj=[[] for _ in X]
 for i,j in a['edges']:adj[i].append(j);adj[j].append(i)
 def escape(i,j):return check_A.dot(check_A.sub(X[i],g),check_A.sub(X[j],X[i]))
 su={i:j for i,j in zip(PATH612,PATH612[1:])};root=PATH612[-1]
 for i in range(len(X)):
  if i!=root and i not in su:su[i]=max(adj[i],key=lambda j:(escape(i,j),j))
 assert set(su)==set(range(len(X)))-{root}
 for i,j in su.items():
  assert j in adj[i]
  if i==82:assert escape(i,j)<0
  else:assert escape(i,j)>0
 for i in range(len(X)):
  seen=set()
  while i!=root:assert i not in seen;seen.add(i);i=su[i]
 assert su[88]==91 and su[144]==145
 return dict(status='EXACT_ROOTED_ESCAPE_FOREST_WITH_ONE_NEGATIVE_ARROW',root=root,negative_arrow=[82,85],successors=[su.get(i,-1) for i in range(len(X))],main_path=PATH612,new88_escape=str(escape(88,91)),old146_escape=str(escape(144,145)))

def run(name,out,mass=False,forest=False):
 c=json.loads((ROOT/'NEW_CASES.json').read_text())[name];out=Path(out);out.mkdir(parents=True,exist_ok=False)
 G=generator(c['generator']);gb=blob(G);assert digest(gb)==c['generator_sha256'];assert len(gb)==c['generator_bytes'];(out/'GENERATOR.json').write_bytes(gb)
 H=RECONSTRUCT.recover(G)['H'];assert len(H)==137
 raw={'H':[r for i,r in enumerate(H) if i not in c['deleted']]};rb=blob(raw);assert digest(rb)==c['raw_sha256'];(out/'RAW.json').write_bytes(rb)
 t=time.perf_counter();a=check_A.run(raw);ta=time.perf_counter()-t;t=time.perf_counter();b=check_B.run(raw);tb=time.perf_counter()-t;aa=blob(a);bb=blob(b)
 assert aa==bb and digest(aa)==c['report_sha256'] and len(aa)==c['report_bytes'];print('EXHAUSTIVE_A_B_MATCH',name,flush=True)
 assert [a['V'],a['E'],a['F']]==c['VEF'] and a['counts']==c['strict'] and a['weak']==c['weak']
 assert a['centred_first_moments']==[0,0,0] and a['centred_centroid']==[0,0,0]
 for tag,v in [('A',aa),('B',bb)]:(out/(tag+'.json')).write_bytes(v)
 report=dict(status='FULL_EXACT_NONWINNER_REPLAY_PASS' if a['counts']!=[1,1,0] or a['weak']!=[0,0,0] else 'FULL_EXACT_POSITIVE_REPLAY_PASS',case=name,source_only=True,VEF=c['VEF'],C=2*a['E'],strict=a['counts'],weak=a['weak'],A_seconds=ta,B_seconds=tb,report_bytes=len(aa),report_sha256=digest(aa),S=a['stable_face_ids'],U=a['unstable_vertices'],H=a['saddle_edges'],primitive_zero_counts=[a[k] for k in ['face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']],stats=stats(a,raw))
 if mass:report['third_mass']=centred_mass.run(a)
 if c.get('preserve146'):report['preserved146']=proof_checks.preserved_pair(a,c['deleted'])
 if c.get('four_witness'):
  spec=json.loads((ROOT/'PROOF_SPECS.json').read_text())[c['four_witness']];report['frozen_certificate']=proof_checks.run(a,c['deleted'],spec)
 if forest:
  assert c.get('forest612');report['forest612']=forest612(a)
 (out/'RECEIPT.json').write_bytes(blob(report));print(report['status'],name,report['VEF'],report['strict'],report['weak'],'A/B',ta,tb,flush=True)
 return report
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--case',required=True);p.add_argument('--out',required=True);p.add_argument('--mass',action='store_true');p.add_argument('--forest',action='store_true');args=p.parse_args();run(args.case,args.out,args.mass,args.forest)
