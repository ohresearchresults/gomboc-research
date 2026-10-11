"""Exact all-point radial-ascent graph at the actual rational volume centroid.
This is a graph diagnostic for one finite body, not a neighbourhood lower bound.
"""
import csv,gzip,json,sys,time,hashlib
from pathlib import Path
B=Path(sys.argv[1]);I=[tuple(map(int,r)) for r in csv.reader(gzip.open(B/'vertices.csv.gz','rt'))];report=json.loads((B/'verification_rational.json').read_text());ap=report['unstable_vertex'];N=len(I);h=[None]*N;h[ap]=0;remaining=set(range(N))-{ap};front=[ap];nchecks=0;level=0;start=time.time()
while front:
 new=[]
 for j in front:
  q=I[j]
  for i in list(remaining):
   p=I[i];nchecks+=1
   if sum(p[k]*(q[k]-p[k]) for k in range(3))>0:h[i]=level+1;remaining.remove(i);new.append(i)
 front=new;level+=1
assert not remaining
out=dict(status='EXACT_FIXED_BODY_RADIAL_ASCENT_GRAPH_PASS',vertices=N,base_ranks=[h[i] for i in report['stable_cycle']],maximum_rank=max(h),all_vertices_reach_apex=True,integer_dot_tests=nchecks,centred_table_sha256=hashlib.sha256((B/'vertices.csv.gz').read_bytes()).hexdigest(),elapsed=time.time()-start,scope='One unchanged exactly centred table. No bound for coordinate changes or a range of reference centres.')
(B/'exact_ascent_graph.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
