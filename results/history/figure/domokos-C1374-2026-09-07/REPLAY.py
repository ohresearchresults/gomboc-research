"""Standard-library complete exact replay. Run python -S REPLAY.py (never -O)."""
from pathlib import Path
from math import gcd
from functools import reduce
from collections import defaultdict, Counter
from fractions import Fraction
import sys,json,gzip,csv,hashlib,time,base64,zlib
sys.set_int_max_str_digits(0)
from codec import reconstruct,parse,topology,dot,sub,cross,det
from exact_audit import audit
from independent_audit import run as independent

def complete(I,R):
 cycles=R['maximal_cycles'];inc=defaultdict(list)
 for f,cy in enumerate(cycles):
  n=cross(sub(I[cy[1]],I[cy[0]]),sub(I[cy[2]],I[cy[0]]));h=dot(n,I[cy[0]])
  assert {k for k,p in enumerate(I)if dot(n,p)==h}==set(cy)
  for a,b in zip(cy,cy[1:]+cy[:1]):
   inward=cross(n,sub(I[b],I[a]));assert all(dot(inward,sub(I[k],I[a]))>0 for k in cy if k not in(a,b));inc[tuple(sorted((a,b)))].append(f)
 assert all(len(x)==2 for x in inc.values())
 for v in range(len(I)):
  link=defaultdict(set)
  for cy in cycles:
   if v in cy:
    k=cy.index(v);a,b=cy[k-1],cy[(k+1)%len(cy)];link[a].add(b);link[b].add(a)
  assert link and all(len(x)==2 for x in link.values());seen=set();todo=[next(iter(link))]
  while todo:
   x=todo.pop()
   if x not in seen:seen.add(x);todo.extend(link[x]-seen)
  assert seen==set(link)
 R.update(complete_contact_sets=True,global_polygon_convexity=True,connected_cyclic_links=True,facet_size_distribution=dict(Counter(map(len,cycles))))

def witnesses(raw,I,T,R,P):
 K,pr,po,w=parse(raw)[4:];planes,cycles,E,tf=topology(I,T);A=int(R['centroid_multiplier']);B=tuple(map(int,R['centroid_subtract']));hh=[A*pl[3]-dot(pl[:3],B)for pl in planes]
 assert all(h>0 for h in hh);assert len(w[0])==len(P) and len(w[1])==len(planes)
 assert R['unstable']==[pr] and len(R['stable'])==1 and set(R['stable'][0])==set(cycles[po])
 for which,root in enumerate((pr,po)):
  ww=w[which];assert ww[root]==-1 and sum(j==-1 for j in ww)==1
  for i,j in enumerate(ww):
   if i==root:continue
   assert 0<=j<len(ww) and i!=j
   if which==0:n=P[i];e=sub(P[j],P[i])
   else:n=planes[i][:3];e=tuple(planes[j][k]*hh[i]-n[k]*hh[j]for k in range(3))
   a=dot(n,e);assert a>0 and K*K*a*a>dot(n,n)*dot(e,e)
   seen=set();v=i
   while v!=root:assert v not in seen and v>=0;seen.add(v);v=ww[v]
 return dict(K=K,primal_root=pr,polar_root=po,positive_rooted_primal_polar_witnesses=True)

def main():
 assert __debug__,'Do not use python -O';st=time.time();base=Path(__file__).resolve().parent;raw=(base/'capsule.pn03').read_bytes();summary=json.loads((base/'SUMMARY.json').read_text());sha=hashlib.sha256(raw).hexdigest()
 assert len(raw)==summary['raw_bytes'] and sha==summary['raw_sha256']
 assert zlib.decompress(base64.b85decode(''.join((base/'capsule.b85').read_text().split())))==raw
 I,D,T,_=reconstruct(raw);R,P=audit(I,T,D,expected=(1,1,0));complete(I,R)
 assert [R[k]for k in('V','E','F')]==[summary[k]for k in('V','E','F')]
 assert not R['degeneracies'] and R['zero_edge_primitives']==0
 out=base/'verified';out.mkdir(exist_ok=True)
 for name,rows in [('raw_vertices.csv.gz',I),('vertices.csv.gz',P),('triangles.csv.gz',T)]:
  with gzip.open(out/name,'wt',newline='')as f:csv.writer(f).writerows(rows)
 (out/'exact_report.json').write_text(json.dumps(R,indent=2));print('FIRST_COMPLETE_EXACT_PASS',flush=True)
 B=independent(out);assert B['zero_edge_primitives']==0;print('SECOND_COMPLETE_EXACT_PASS',flush=True)
 ww=witnesses(raw,I,T,R,P)
 # Exact translation covariance of volume/moments. No origin-inside assumption.
 shift=(17*D,-11*D,23*D);II=[tuple(p[k]+shift[k]for k in range(3))for p in I];Wt=0;Mt=[0,0,0]
 for a,b,c in T:
  value=det(II[a],II[b],II[c]);Wt+=value
  for k in range(3):Mt[k]+=value*(II[a][k]+II[b][k]+II[c][k])
 W=int(R['W']);M=tuple(map(int,R['M']));assert Wt==W and Mt==[M[k]+4*W*shift[k]for k in range(3)]
 # Deliberately invalid boundaries are rejected by geometry, not only hash.
 rejected=[]
 bad=T.copy();bad[0]=(bad[0][0],bad[0][2],bad[0][1])
 try:audit(I,bad,D)
 except AssertionError:rejected.append('reversed_triangle')
 else:raise AssertionError('corruption accepted')
 try:audit(I,T[:-1],D)
 except AssertionError:rejected.append('missing_triangle')
 else:raise AssertionError('corruption accepted')
 report=dict(status='FRESH_STANDARD_LIBRARY_COMPLETE_REPLAY_PASS',VEF=[R[k]for k in('V','E','F')],C=2*R['E'],SUH=R['class_SUH'],stable=R['stable'],unstable=R['unstable'],saddles=R['saddles'],degeneracies=R['degeneracies'],centered_moments=R['centred_moments'],capsule_sha256=sha,witnesses=ww,independent_full_audits=2,translation_moment_covariance=True,rejected_corruptions=rejected,seconds=time.time()-st,new_below1000_winner=False)
 (base/'REPLAY_REPORT.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2),flush=True)
if __name__=='__main__':main()
