"""Combine both protected C626 contacts with S8's two nonsimple cap unions.
C626 owner labels and S8 owner labels are explicitly compared by containment.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from union_atlas import *
from SVD_CORRECT import repair
from TREE_REPAIR import arrows
import argparse,hashlib,platform,scipy
sys.path.insert(0,str(ROOT/'parent'));import RECONSTRUCT,check_B
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def inherited(older,ownnew):
 ownold=[[older['active_input_indices'][f] for f,cy in enumerate(older['faces']) if v in cy] for v in range(older['V'])];mapping=[next(i for i,o in enumerate(ownnew) if set(old)<=set(o)) for old in ownold];assert len(set(mapping))==len(ownnew)
 X=np.array([[float(F(x)) for x in row] for row in older['raw_vertices']]);c=np.array([float(F(x)) for x in older['raw_centroid']]);up=np.argmax(arrows(X-c),axis=1);root=next(i for i,x in enumerate(X) if list(x)==[0.,0.,1.]);newroot=mapping[root];choices={i:set() for i in range(len(ownnew))}
 for i in range(len(ownold)):
  if i==root:continue
  j=int(up[i]);seen={i}
  while mapping[j]==mapping[i]:
   assert j not in seen;seen.add(j);j=int(up[j])
  choices[mapping[i]].add(mapping[j])
 # A rooted quotient of a directed tree is reachable; choose edges to settled nodes.
 result={};seen={newroot}
 while len(seen)<len(ownnew):
  new=[]
  for i in range(len(ownnew)):
   opts=sorted(choices[i]&seen)
   if i not in seen and opts:result[i]=opts[0];new.append(i)
  assert new,'Inherited quotient graph has no route to root';seen.update(new)
 return result,mapping,choices

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--s8',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--steps',type=int,default=80);ap.add_argument('--goal',type=float,default=1e-7);ap.add_argument('--geometry',choices=['c626','s8','condition','stress'],default='s8');ap.add_argument('--condition',type=Path);ap.add_argument('--witness',choices=['c626','s8','condition','dynamic'],default='c626');a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False);G=json.load(open(a.s8/'GENERATOR.json'));rep=json.load(open(a.s8/'B.json'));raw=RECONSTRUCT.recover(G);Q=np.array([[float(F(x,r[-1])) for x in r[:3]] for r in raw['H']]);geometry_raw=raw
 if a.geometry=='c626':geometry_raw=json.load(open(ROOT/'baseline/raw.json'))
 if a.geometry=='condition':geometry_raw=json.load(open(a.condition/'raw.json'))
 Q=np.array([[float(F(x,r[-1])) for x in r[:3]] for r in geometry_raw['H']])
 if a.geometry=='stress':
  from numeric import Chart
  chart=Chart(a.s8);edge=next(i for i,p in enumerate(chart.edges) if list(p)==[87,127]);w=chart.w.copy();w[edge]=0;Q=chart.solve(w)[0]
 s=UnionAtlas(G,rep,[87,127],Q);(a.out/'INITIAL_GENERATOR.json').write_bytes(B(s.G));(a.out/'PATCH.json').write_bytes(B(s.patch));old=json.load(open(a.condition/'A.json')) if a.witness=='condition' else json.load(open(ROOT/'baseline/A.json')) if a.witness=='c626' else rep
 if a.witness!='dynamic':
  s.forcedp,mapping,choices=inherited(old,s.owners);rawold=json.load(open(a.condition/'raw.json')) if a.witness=='condition' else json.load(open(ROOT/'baseline/raw.json')) if a.witness=='c626' else raw;q=np.array([[float(F(x,r[-1])) for x in r[:3]] for r in rawold['H']]);c=np.array([float(F(x)) for x in old['raw_centroid']]);qp=q/(1-q@c)[:,None];sw=np.argmax(arrows(qp),axis=1);s.forcedq={i:int(sw[i]) for i in range(s.nq) if i!=s.S};(a.out/'INHERITANCE.json').write_bytes(B(dict(mapping=mapping,choices={k:sorted(v) for k,v in choices.items()},primal=s.forcedp,polar=s.forcedq)))
 s.last=None;v,J,g=s.evaluate(np.zeros(s.n));(a.out/'INITIAL_Q_HEX.json').write_bytes(B([[float(x).hex() for x in row] for row in Q]));(a.out/'INPUT.json').write_bytes(B(dict(steps=a.steps,goal=a.goal,witness=a.witness,geometry=a.geometry,versions=[platform.python_version(),np.__version__,scipy.__version__])));print('CROSS_CAP_START',s.n,s.nv,s.patch,'mech',v[:s.mechlen-2].min(),flush=True);repair(s,np.zeros(s.n),a.out,steps=a.steps,goal=a.goal)
if __name__=='__main__':main()
