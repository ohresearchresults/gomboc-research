import sympy as sp,time,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent
N=137
E=[tuple(map(int,l.split())) for l in (ROOT/'H213_edges.txt').read_text().splitlines()]
adj=[set() for _ in range(N)]
for u,v in E:adj[u].add(v);adj[v].add(u)
B=[1,6,11]; bpos={1:(-1,-1),6:(1,-1),11:(0,1)}
ints=[v for v in range(N) if v not in B];idx={v:i for i,v in enumerate(ints)}
L=sp.zeros(len(ints)); rx=sp.zeros(len(ints),1);ry=sp.zeros(len(ints),1)
for v in ints:
 i=idx[v];L[i,i]=len(adj[v])
 for w in adj[v]:
  if w in idx:L[i,idx[w]]-=1
  else:rx[i]+=bpos[w][0];ry[i]+=bpos[w][1]
from sympy.polys.matrices import DomainMatrix
from sympy.polys.domains import ZZ
dL=DomainMatrix.from_Matrix(L).convert_to(ZZ)
dR=DomainMatrix.from_Matrix(rx.row_join(ry)).convert_to(ZZ)
num,den=dL.solve_den(dR,method='rref')
S=num.to_Matrix()/int(str(den))
p={B[i]:tuple(map(sp.Rational,bpos[B[i]])) for i in range(3)}
for v in ints:p[v]=(sp.cancel(S[idx[v],0]),sp.cancel(S[idx[v],1]))
bedges=[(1,6),(1,11),(6,11)]
ws=sp.symbols('w0:3'); eq=[]
for v in B:
 rx0=sp.Rational(0);ry0=sp.Rational(0)
 for w in adj[v]:
  e=tuple(sorted((v,w)));dx=p[w][0]-p[v][0];dy=p[w][1]-p[v][1]
  if e in bedges:
   k=bedges.index(e);rx0+=ws[k]*dx;ry0+=ws[k]*dy
  else:rx0+=dx;ry0+=dy
 eq.extend([rx0,ry0])
solw=sp.solve(eq,ws,dict=True)[0]
assert all(sp.simplify(e.subs(solw))==0 for e in eq)
text=''.join(f'{v} {p[v][0]} {p[v][1]}\n' for v in range(N))
(ROOT/'H213_tutte_xy_exact.txt').write_text(text)
assert hashlib.sha256(text.encode()).hexdigest()=='683b5646c4fffcb1515e551a006f42aa5bab8977ad1aeb573f2af5e8cd8da817'
for w in ws: print(w,sp.factor(solw[w]))
