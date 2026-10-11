"""Finite incidence turnover: delete a triangular support and split an old quad.
All row labels in the input are original C626 labels. Numerical output needs exact audit.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from flexible import *
from REFINE import warm,correct
import argparse,hashlib,platform,time,scipy
sys.path.insert(0,str(ROOT/'parent'));import RECONSTRUCT,check_B
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def exact_mixed(G):
 Y=[[F(v,G['grid']) for v in r] for r in G['controls']];Y[G['n_supports']]=[F(0),F(0),F(1)]
 for i,deps,axes in G['plan']:
  if not deps:continue
  rest=[k for k in range(3) if k not in axes];A=[[Y[j][a] for a in axes] for j in deps];b=[1-sum(Y[j][a]*Y[i][a] for a in rest) for j in deps]
  # Generic exact Gaussian elimination, dimension at most three.
  C=[row+[x] for row,x in zip(A,b)];n=len(deps)
  for k in range(n):
   p=next(j for j in range(k,n) if C[j][k]);C[k],C[p]=C[p],C[k];d=C[k][k];C[k]=[x/d for x in C[k]]
   for j in range(n):
    if j!=k:
     d=C[j][k];C[j]=[x-d*y for x,y in zip(C[j],C[k])]
  for a,row in zip(axes,C):Y[i][a]=row[-1]
 return Y

def open_contact(G,point):
 G=copy.deepcopy(G);n=G['n_supports'];assert point>=n;Y=exact_mixed(G);mapping={i:i-(i>point) for i in range(len(Y)) if i!=point};plan=[];changed=[]
 for i,deps,axes in G['plan']:
  if i==point:continue
  dd=[j for j in deps if j!=point];aa=axes
  if len(dd)!=len(deps):
   assert not dd,'This exact turnover opens a one-equation support solve';aa=[];changed.append([i,deps,axes,dd,aa])
  plan.append([mapping[i],[mapping[j] for j in dd],aa])
 removed=G['groups'].pop(point-n);G['plan']=plan;D=10**12;G['grid']=D;G['controls']=[[round(y*D) for y in row] for i,row in enumerate(Y) if i!=point]
 return G,dict(opened_original_group=removed,removed_contact_node=point,old_to_new=mapping,changed_plan=changed)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--delete',type=int,required=True);ap.add_argument('--point',type=int,choices=[179,180],required=True);ap.add_argument('--sign',type=int,choices=[-1,1],required=True);ap.add_argument('--eps',type=str,default='1/10000000');ap.add_argument('--warm',type=int,default=1500);ap.add_argument('--steps',type=int,default=70);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--loose',action='store_true');a=ap.parse_args();out=a.out;out.mkdir(parents=True,exist_ok=False)
 G=json.load(open(ROOT/'parent/GENERATOR.json'));G,change=open_contact(G,a.point);support=18 if a.point==179 else 127;G['controls'][support][2]+=a.sign*round(F(a.eps)*G['grid']);Y=exact_mixed(G);Q=np.array(Y[:G['n_supports']],float);GG,change2=delete_generator(G,a.delete,Q);raw=RECONSTRUCT.recover(GG);rep=check_B.run(raw);(out/'INITIAL_GENERATOR.json').write_bytes(B(GG));(out/'INITIAL_B.json').write_bytes(B(rep));(out/'CHANGES.json').write_bytes(B([change,change2]));print('TURNOVER_INITIAL_EXACT_B',rep['V'],rep['E'],rep['F'],rep['counts'],rep['weak'],flush=True)
 Q=np.array([[float(F(v,r[-1])) for v in r[:3]] for r in raw['H']]);s=FlexibleAtlas(GG,rep,Q);s.checkpoint_dir=out
 if a.loose:
  s.floor[:s.mechlen-2]=1e-7;s.floor[s.mechlen-2:s.mechlen]=1e-5;s.floor[s.mechlen:s.mechlen+s.nq]=1e-9;s.floor[s.mechlen+s.nq:-s.nq-1]=1e-6
 (out/'INPUT.json').write_bytes(B(dict(delete=a.delete,point=a.point,sign=a.sign,eps=a.eps,warm=a.warm,steps=a.steps,loose=a.loose,versions=[platform.python_version(),np.__version__,scipy.__version__])))
 t=time.time();z=warm(s,a.warm) if a.warm else np.zeros(s.n);(out/'WARM_Z.json').write_bytes(B([float(x).hex() for x in z]));z,h=correct(s,z,a.steps);v,J,g=s.evaluate(z);GG=copy.deepcopy(s.G);GG['grid']=10**12;GG['controls']=np.rint(g['Y']*GG['grid']).astype(np.int64).tolist();(out/'GENERATOR.json').write_bytes(B(GG));(out/'Z.json').write_bytes(B([float(x).hex() for x in z]));(out/'RECORDS.json').write_bytes(B(h));status=dict(mech=float(v[:s.mechlen].min()),slack=float(g['slack'].min()),det=float(g['v6'].min()),n=s.n,time=time.time()-t,gen_sha=hashlib.sha256(B(GG)).hexdigest());(out/'STATUS.json').write_bytes(B(status));print('TURNOVER_FINAL_NUMERICAL_ONLY',json.dumps(status),flush=True)
if __name__=='__main__':main()
