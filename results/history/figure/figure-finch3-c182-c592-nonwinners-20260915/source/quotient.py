"""Finite joint vertex/facet quotient. Exact generator, not zero-epsilon claim.
Input radial atlas numbering is bound to its literal generator. Coincident internal
facet vertices of degree two are deleted; all remaining contacts are reconstructed."""
import json,itertools,argparse
from fractions import Fraction as F
import numpy as np
import radial
from implicit import Manifold
from pathlib import Path

def build(G,vm=True,fm=True,weight=.5):
 raw,p=radial.reconstruct(G);P=np.array(p,float);q=np.array([[float(F(v,h[-1])) for v in h[:3]] for h in raw['H']]);faces=G['faces'];n=len(q);V=len(P);mp={i:(65 if vm and i==67 else i) for i in range(V)}
 if vm:P[65]=(1-weight)*P[65]+weight*P[67]
 if fm:q[121]=(1-weight)*q[121]+weight*q[122]
 def cyc(c):
  out=[]
  for i in c:
   i=mp[i]
   if not out or i!=out[-1]:out.append(i)
  if len(out)>1 and out[0]==out[-1]:out.pop()
  return out
 ff=[cyc(c) for c in faces]
 if fm:
  e=[]
  for c in [ff[121],ff[122]]:e+=list(zip(c,c[1:]+c[:1]))
  d={(a,b) for a,b in e if (b,a) not in e};out=[min(a for a,b in d)]
  while True:
   b=next(b for a,b in d if a==out[-1])
   if b==out[0]:break
   out.append(b)
  ff[121]=out;ff[122]=[]
 # Remove non-extreme valence-two boundary point83 in the merged-facet case.
 if fm:ff=[[i for i in c if i!=83] for c in ff]
 vp=[i for i in range(V) if not(vm and i==67) and not(fm and i==83)];fp=[i for i in range(n) if not(fm and i==122)];imap={i:k for k,i in enumerate(vp)};PP=P[vp];qq=q[fp];FF=[[imap[i] for i in ff[f]] for f in fp]
 assert all(len(set(c))>=3 for c in FF)
 pri=[G['priority'][f] for f in fp]+[G['priority'][n+i] for i in vp];labels=[G['parent_labels'][i] for i in vp]
 M=Manifold(PP,qq,FF);z=np.r_[PP.ravel(),qq.ravel()];zz,ok=M.project(z,maxit=15);PP=zz[:M.V*3].reshape(-1,3);qq=zz[M.V*3:].reshape(-1,3)
 H=radial.make(PP,qq,FF,0,10**12,pri);H['priority']=pri;H['parent_labels']=labels;H['operation']={'merge_vertices':[65,67] if vm else [],'merge_facets':[121,122] if fm else [],'drop_collinear_vertex':83 if fm else None,'weight':str(weight)}
 return H
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--start',default='IMPGLOBAL_GENERATOR_G6.json');a.add_argument('--tag',default='QUOT');args=a.parse_args();G=json.load(open(args.start));stats=[]
 for vm,fm in [(True,False),(False,True),(True,True)]:
  for k,w in enumerate([0.,.5,1.]):
   name=f'{args.tag}_{int(vm)}{int(fm)}_{k}';H=build(G,vm,fm,w);Path(name+'.json').write_text(json.dumps(H,sort_keys=True,separators=(',',':')))
   try:
    raw,p=radial.reconstruct(H);PP=np.array(p,float);qq=np.array([[float(F(v,r[-1])) for v in r[:3]] for r in raw['H']]);M=Manifold(PP,qq,H['faces']);R=M.evaluate(np.r_[PP.ravel(),qq.ravel()],np.zeros((M.K,1)));s=M.res(R)[2];row={'name':name,'projection_class':s,'min_s':float(R['s'].min()),'min_t':float(R['det'].min()),'V':M.V,'E':len(M.E),'F':M.n}
   except Exception as e:row={'name':name,'error':str(e)}
   stats.append(row);print(row,flush=True)
 Path(args.tag+'_PROPOSALS.json').write_text(json.dumps(stats,sort_keys=True,separators=(',',':')))
