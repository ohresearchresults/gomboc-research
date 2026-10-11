"""Exact scoped certificate for the two opposed-witness traps before quotient.
It does not exclude a different witness choice, centre, geometry or contact chart."""
import sys,json
from fractions import Fraction as F
from pathlib import Path
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return [x-y for x,y in zip(a,b)]
def eta(a,b):
 d=sub(b,a);return dot(a,d)/dot(d,d)
def check(generator,audit):
 G=json.load(open(generator));A=json.load(open(audit));import radial
 raw,P=radial.reconstruct(G);g=list(map(F,A['raw_centroid']));Z=[sub(p,g) for p in P];E={tuple(sorted((i,j))) for c in G['faces'] for i,j in zip(c,c[1:]+c[:1])};Q=[]
 for h in raw['H']:
  n=[F(v,h[-1]) for v in h[:3]];b=1-dot(n,g);Q.append([v/b for v in n])
 adj={i:set() for i in range(len(Q))}
 for e in E:
  fs=[f for f,c in enumerate(G['faces']) if set(e)<=set(c)];assert len(fs)==2;a,b=fs;adj[a].add(b);adj[b].add(a)
 out=[]
 for name,X,a,b,neigh in [('primal',Z,G['parent_labels'].index(67),G['parent_labels'].index(69),None),('dual',Q,121,122,adj)]:
  x=eta(X[a],X[b]);y=eta(X[b],X[a]);assert x+y==-1 and x<0 and y<0
  max_flags=[]
  for i,j in [(a,b),(b,a)]:
   nbr=sorted(neigh[i]) if neigh is not None else sorted(v if u==i else u for u,v in E if i in (u,v))
   mx=max(eta(X[i],X[k]) for k in nbr);max_flags.append(mx==eta(X[i],X[j]))
  out.append({'type':name,'pair':[a,b],'eta_decimal':[float(x),float(y)],'sum_exact':-1,'both_selected_maxima':max_flags})
 tau=F(1,10**6);bound=2*(tau+F(1,2))**2
 return {'marker':'OPPOSED_ETA_IDENTITY_AND_SCOPED_LOSS_BOUND_PASS','pairs':out,'half_squared_loss_bound_for_these_four_targets':str(bound),'scope':'these four directed witnesses only; witness switching and geometry/contact changes remain allowed'}
if __name__=='__main__':
 print(json.dumps(check(sys.argv[1],sys.argv[2]),sort_keys=True,separators=(',',':')))
