"""Exact exterior-contact motion coupled to the PAIR99 surgery.
Dependencies are the complete S8 generator, RECONSTRUCT.py and BUILD.py.
No floating point and no independent reference centre defines the body.
"""
import json,math,sys
from fractions import Fraction as Q
from pathlib import Path
from itertools import combinations
import BUILD as B,RECONSTRUCT
sys.set_int_max_str_digits(0)
EDIT=[(i,k) for i in [154,177] for k in range(3)]+[(71,0)]+[(i,k) for i in [69,70] for k in range(3)]
def solve(A,b):return [B.dot(row,b) for row in B.inverse(A)]
def coordinates(base,generator,parameter):
 P,keep,faces,labels,_=B.setup(base,'PAIR99')
 oldq={i:tuple(Q(v,r[3]) for v in r[:3]) for i,r in enumerate(RECONSTRUCT.recover(generator)['H'])}
 triples=[]
 for i in range(len(P)):
  owners=[labels0 for labels0 in oldq if labels0!=99 and B.dot(oldq[labels0],P[i])==1]
  tri=max(combinations(owners,3),key=lambda t:abs(B.det(*(oldq[j] for j in t))))
  triples.append(tri)
 d=json.loads(json.dumps(generator));G=d['grid'];D=parameter['denominator'];NN=math.lcm(G,D)
 d['controls']=[[v*(NN//G) for v in row] for row in d['controls']];d['grid']=NN
 delta=[Q(v,D) for v in parameter['numerators']];assert len(delta)==25
 for (i,k),v in zip(EDIT,delta[:13]):d['controls'][i][k]+=int(v*NN)
 H=RECONSTRUCT.recover(d)['H'];q={i:tuple(Q(v,r[3]) for v in r[:3]) for i,r in enumerate(H)}
 PP=[tuple(solve([q[j] for j in tri],[Q(1)]*3)) for tri in triples];X=PP.copy();free={124:[0],112:[0,1],146:[0,1],148:[1],149:[0]}
 u0=[*q[72],q[73][0],q[73][2],*[PP[i][k] for i in [124,112,146,148,149] for k in free[i]]];u=[v+w for v,w in zip(u0,delta[13:])]
 q[72]=tuple(u[:3]);q[73]=(u[3],(1-u[3]*PP[69][0]-u[4]*PP[69][2])/PP[69][1],u[4])
 for i,nn in [(106,[15,71,72]),(109,[15,72,75]),(114,[17,71,73]),(117,[71,72,73]),(120,[3,72,73])]:X[i]=tuple(solve([q[j] for j in nn],[Q(1)]*3))
 k=5
 for i,nn in [(124,[3,72]),(112,[75]),(146,[80]),(148,[69,80]),(149,[3,69])]:
  axes=[a for a in range(3) if a not in free[i]];p=list(PP[i])
  for a in free[i]:p[a]=u[k];k+=1
  ss=solve([[q[j][a] for a in axes] for j in nn],[1-sum(q[j][a]*p[a] for a in free[i]) for j in nn])
  for a,v in zip(axes,ss):p[a]=v
  X[i]=tuple(p)
 assert k==12
 return X,keep,faces,labels,d

def run(base,generator,parameter):
 X,keep,faces,labels,d=coordinates(base,generator,parameter);H=[]
 for cy in faces:
  a,b,c=(X[i] for i in cy[:3]);n=B.cross(B.sub(b,a),B.sub(c,a));h=B.dot(n,a);assert h>0
  assert all(B.dot(n,X[i])==h for i in cy),'coplanarity'
  assert all(B.dot(n,X[i])<h for i in keep if i not in cy),'support'
  for i,j in zip(cy,cy[1:]+cy[:1]):assert all(B.dot(n,B.cross(B.sub(X[j],X[i]),B.sub(X[k],X[i])))>0 for k in cy if k not in [i,j])
  den=math.lcm(*(v.denominator for v in (*n,h)));row=[int(den*v) for v in (*n,h)];gg=math.gcd(*row);H.append([v//gg for v in row])
 assert len(H)==138 and len(set(map(tuple,H)))==138
 labels=dict(input_support_labels=labels,planned_faces=faces,original_vertex_ids=keep)
 return dict(H=H),labels,d
if __name__=='__main__':
 base,gen,par,out=map(Path,sys.argv[1:]);r,l,d=run(json.loads(base.read_text()),json.loads(gen.read_text()),json.loads(par.read_text()));out.mkdir(exist_ok=False)
 for n,x in [('raw.json',r),('LABELS.json',l),('INTERFACE_GENERATOR.json',d)]: (out/n).write_text(json.dumps(x,sort_keys=True,separators=(',',':')))
 print('NEW_EXTERNAL_INTERFACE_RATIONAL_GEOMETRY_BUILT',len(r['H']),flush=True)
