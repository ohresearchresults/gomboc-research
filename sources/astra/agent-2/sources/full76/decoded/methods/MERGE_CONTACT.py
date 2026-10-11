"""Nonsimple physical-vertex union by exact identification of two free contact nodes.
Duplicated support equations are removed, and their freed coordinates are restored
from the actual parent mixed realization. No triangulation diagonal is counted.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from flexible import *
from TURNOVER import exact_mixed
from CROSS_CAP import inherited
from TREE_REPAIR import arrows
from SVD_CORRECT import repair
import argparse,hashlib,platform,scipy
sys.path.insert(0,str(ROOT/'parent'));import RECONSTRUCT
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def merge(G,rep,a,b,lam=F(1,2)):
 G=copy.deepcopy(G);n=G['n_supports'];assert a>=n and b>=n and a!=b;Y=exact_mixed(G);plan={i:(d,ax) for i,d,ax in G['plan']};assert plan[a]==plan[b]==([],[])
 ga,gb=G['groups'][a-n],G['groups'][b-n];assert len(set(ga)&set(gb))==2;owners=[[f for f,cy in enumerate(rep['faces']) if v in cy] for v in range(rep['V'])];va=owners.index(ga);vb=owners.index(gb);assert sorted([va,vb]) in [sorted(e) for e in rep['edges']]
 union=sorted(set(ga+gb));Y[a]=[(1-lam)*u+lam*v for u,v in zip(Y[a],Y[b])];mapping={i:i-(i>b) for i in range(len(Y)) if i!=b};alias=lambda i:mapping[a if i==b else i];newplan=[];changed=[]
 for i,deps,axes in G['plan']:
  if i==b:continue
  dd=list(dict.fromkeys(a if j==b else j for j in deps));aa=axes
  if len(dd)!=len(deps):
   choices=list(itertools.combinations(range(3),len(dd)));aa=list(max(choices,key=lambda ax:abs(np.linalg.det(np.array([[float(Y[j][k]) for k in ax] for j in dd])))));changed.append([i,deps,axes,dd,aa])
  newplan.append([alias(i),[alias(j) for j in dd],aa])
 G['groups'][a-n]=union;G['groups'].pop(b-n);G['plan']=newplan;G['grid']=10**12;G['controls']=[[round(x*G['grid']) for x in row] for i,row in enumerate(Y) if i!=b]
 keep=min(va,vb);gone=max(va,vb);old=[i for i in range(rep['V']) if i!=gone];vmap={i:k for k,i in enumerate(old)};vmap[gone]=vmap[keep];fs=[]
 for cy in rep['faces']:
  out=[]
  for v in cy:
   k=vmap[v]
   if not out or k!=out[-1]:out.append(k)
  if out[0]==out[-1]:out.pop()
  assert len(set(out))==len(out) and len(out)>=3;fs.append(out)
 nr=copy.deepcopy(rep);nr['V']-=1;nr['E']-=1;nr['faces']=fs;nr['raw_vertices']=[rep['raw_vertices'][i] for i in old];nr['edges']=sorted({tuple(sorted((u,v))) for cy in fs for u,v in zip(cy,cy[1:]+cy[:1])});assert nr['V']-len(nr['edges'])+len(fs)==2
 changes=dict(parent_contact_nodes=[a,b],parent_groups=[ga,gb],child_group=union,lam=str(lam),parent_vertex_ids=[va,vb],physical_old_to_new=vmap,contact_old_to_new={i:alias(i) for i in range(len(Y))},changed_plan_before_reindex=changed)
 return G,nr,changes

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--generator',type=Path,default=ROOT/'parent/GENERATOR.json');ap.add_argument('--report',type=Path,default=ROOT/'baseline/A.json');ap.add_argument('--nodes',type=int,nargs=2,required=True);ap.add_argument('--lam',default='1/2');ap.add_argument('--goal',type=float,default=1e-7);ap.add_argument('--steps',type=int,default=120);ap.add_argument('--dynamic',action='store_true');ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False);G=json.load(open(a.generator));rep=json.load(open(a.report));GG,nr,changes=merge(G,rep,*a.nodes,F(a.lam));raw=RECONSTRUCT.recover(GG);Q=np.array([[float(F(x,row[-1])) for x in row[:3]] for row in raw['H']]);s=FlexibleAtlas(GG,nr,Q)
 if not a.dynamic:
  s.forcedp,mp,ch=inherited(rep,s.owners);oldraw=RECONSTRUCT.recover(G);q=np.array([[float(F(x,r[-1])) for x in r[:3]] for r in oldraw['H']]);c=np.array([float(F(x)) for x in rep['raw_centroid']]);sp=np.argmax(arrows(q/(1-q@c)[:,None]),axis=1);s.forcedq={i:int(sp[i]) for i in range(s.nq) if i!=3};(a.out/'WITNESSES.json').write_bytes(B(dict(primal=s.forcedp,polar=s.forcedq)))
 (a.out/'SOURCE_GENERATOR.json').write_bytes(B(G));(a.out/'NOMINAL_COMPLEX.json').write_bytes(B(nr));(a.out/'INITIAL_GENERATOR.json').write_bytes(B(GG));(a.out/'CHANGES.json').write_bytes(B(changes));(a.out/'INPUT.json').write_bytes(B(dict(nodes=a.nodes,lam=a.lam,goal=a.goal,steps=a.steps,dynamic=a.dynamic,versions=[platform.python_version(),np.__version__,scipy.__version__])));s.last=None;print('MERGE_CONTACT_START',changes,s.n,flush=True);repair(s,np.zeros(s.n),a.out,steps=a.steps,goal=a.goal)
if __name__=='__main__':main()
