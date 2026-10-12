"""Exact rational one-control family between the two grid-1e6 endpoints.
This constructs symbolic geometry/mass and a univariate candidate escape wall.
It asserts no interval census unless all later certificates explicitly succeed.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import gcd,lcm
from itertools import combinations
import sympy as sp,json,sys,time,pickle
sys.set_int_max_str_digits(0);R=Path(__file__).parent;D0=R/'C642_GRID6_UNREPAIRED_OWN121';t=sp.Symbol('t');start=time.time()
def say(*a):print(round(time.time()-start,2),*a,flush=True)
g=json.loads((D0/'GENERATOR.json').read_text());a=json.loads((D0/'A.json').read_text());b=json.loads((R/'C642_GRID6_REPAIR169/A.json').read_text());raw=json.loads((D0/'RAW.json').read_text());D=g['grid'];n=g['n_supports'];X=[[sp.Rational(v,D) for v in row] for row in g['controls']];X[n]=[sp.Rational(0),sp.Rational(0),sp.Rational(1)];X[169][1]+=t/D
for i,deps,axes in g['plan']:
 if deps:
  rest=[j for j in range(3) if j not in axes];A=sp.Matrix([[X[v][j] for j in axes] for v in deps]);rhs=sp.Matrix([1-sum(X[v][j]*X[i][j] for j in rest) for v in deps]);sol=A.inv()*rhs
  for j,val in zip(axes,sol):X[i][j]=sp.cancel(val)
q=X[:n];changed=[i for i,row in enumerate(q) if any(t in z.free_symbols for z in row)];assert changed==[40,44,45,69];say('changed rows',changed)
H=[]
for row in q:
 dens=[sp.fraction(z)[1] for z in row];den=sp.lcm(dens);rr=[sp.cancel(z*den) for z in row]+[den];fac=sp.gcd_list(rr);rr=[sp.cancel(z/fac) for z in rr]
 if rr[3].subs(t,0)<0:rr=[-z for z in rr]
 H.append(rr)
assert all(sp.cancel(q[i][j].subs(t,0)-sp.Rational(raw['H'][i][j],raw['H'][i][3]))==0 for i in range(n) for j in range(3));say('H degrees',[(i,[sp.degree(v,t) for v in H[i]]) for i in changed])
faces=a['faces'];owners=[[] for _ in a['raw_vertices']]
for i,cy in enumerate(faces):
 for v in cy:owners[v].append(i)
P=[];changing=[]
for v,ids in enumerate(owners):
 if not(set(ids)&set(changed)):P.append([sp.Rational(z) for z in a['raw_vertices'][v]]);continue
 rows=next(rr for rr in combinations(ids,3) if sp.Matrix([H[i][:3] for i in rr]).det().subs(t,0)!=0);A=sp.Matrix([H[i][:3] for i in rows]);rhs=sp.Matrix([H[i][3] for i in rows]);p=[sp.cancel(z) for z in A.inv()*rhs];P.append(p)
 if any(t in z.free_symbols for z in p):changing.append(v)
 assert all(sp.cancel(p[j].subs(t,0)-sp.Rational(a['raw_vertices'][v][j]))==0 for j in range(3))
 assert all(sp.cancel(sum(q[i][j]*p[j] for j in range(3))-1)==0 for i in ids)
say('changing vertices',changing)
assert set(tuple(z.subs(t,1) for z in p) for p in P)==set(tuple(map(sp.Rational,p)) for p in b['raw_vertices']);say('both endpoint vertex sets exact')
tris=[(cy[0],cy[j],cy[j+1]) for cy in faces for j in range(1,len(cy)-1)];dv=[];dm=[[],[],[]]
for v,w,z in tris:
 if not({v,w,z}&set(changing)):continue
 det=sp.cancel(sp.Matrix([P[v],P[w],P[z]]).det());d0=det.subs(t,0);dv.append((det-d0)/6)
 for j in range(3):
  term=sp.cancel(det*(P[v][j]+P[w][j]+P[z][j])/24);dm[j].append(term-term.subs(t,0))
say('variable integration terms',len(dv))
V=sp.cancel(sp.Rational(a['ordinary_volume'])+sum(dv));say('V degrees',[sp.degree(z,t) for z in sp.fraction(V)])
M=[]
for j in range(3):
 v=sp.cancel(sp.Rational(a['raw_first_moments'][j])+sum(dm[j]));M.append(v);say('M degrees',j,[sp.degree(z,t) for z in sp.fraction(v)])
assert V.subs(t,1)==sp.Rational(b['ordinary_volume']);assert [z.subs(t,1) for z in M]==list(map(sp.Rational,b['raw_first_moments']));say('both endpoint masses exact')
u=169;v=167;wall=sp.cancel(sum((V*P[u][j]-M[j])*(P[v][j]-P[u][j]) for j in range(3)));N,De=sp.fraction(wall);poly=sp.Poly(N,t);pp=sp.Poly(De,t);say('wall degrees',poly.degree(),pp.degree(),'coeffbits',max(abs(int(c)).bit_length() for c in poly.all_coeffs()))
assert wall.subs(t,0)<0 and wall.subs(t,1)>0
with open(R/'SYMBOLIC_PAIR.pkl','wb') as f:pickle.dump(dict(t=t,g=g,H=H,q=q,P=P,V=V,M=M,wall=wall,faces=faces,owners=owners,changing=changing),f)
(R/'SYMBOLIC_PAIR_WALL.json').write_text(json.dumps(dict(numerator_ascending=[str(poly.nth(i)) for i in range(poly.degree()+1)],denominator_ascending=[str(pp.nth(i)) for i in range(pp.degree()+1)]),sort_keys=True,separators=(',',':')));say('SYMBOLIC_PAIR_DEFINED')
