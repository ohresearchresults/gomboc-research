"""Cycle-free least-deficit escape routing followed by full physical/mass correction.
Dijkstra proposals are numerical choices, not exclusion certificates. A competing
radial extremum may require switching its escape rather than selecting its local
best neighbour (which can create a two-cycle). Exact final auditing is separate.
"""
from MERGE_CONTACT import *
import heapq,time

def routing(A,root,power=2,tie=1e-14):
 W=arrows(A);n=len(A);cost=np.maximum(-W,0)**power+tie;np.fill_diagonal(cost,np.inf);dist=np.full(n,np.inf);dist[root]=0;queue=[(0.,root)];seen=set();nxt={}
 while queue:
  d,j=heapq.heappop(queue)
  if j in seen:continue
  seen.add(j)
  for i in range(n):
   if i in seen:continue
   nd=d+cost[i,j]
   if nd<dist[i]:dist[i]=nd;nxt[i]=j;heapq.heappush(queue,(float(nd),i))
 assert len(seen)==n and len(nxt)==n-1
 for i in range(n):
  s=set();j=i
  while j!=root:assert j not in s;s.add(j);j=nxt[j]
 return nxt,dist

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--generator',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--power',type=int,default=2);ap.add_argument('--epochs',type=int,default=6);ap.add_argument('--steps',type=int,default=20);ap.add_argument('--goal',type=float,default=1e-7);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False);G=json.load(open(a.generator));raw=RECONSTRUCT.recover(G);sys.path.insert(0,str(ROOT/'parent'));import check_B
 rep=check_B.run(raw);(a.out/'INITIAL_B.json').write_bytes(B(rep));(a.out/'SOURCE_GENERATOR.json').write_bytes(B(G));(a.out/'INPUT.json').write_bytes(B(dict(source_G_sha256=hashlib.sha256(B(G)).hexdigest(),power=a.power,epochs=a.epochs,steps=a.steps,goal=a.goal,versions=[platform.python_version(),np.__version__,scipy.__version__])));Q=np.array([[float(F(x,row[-1])) for x in row[:3]] for row in raw['H']]);s=FlexibleAtlas(G,rep,Q);z=np.zeros(s.n);history=[]
 print('INITIAL_ROUTING_B',rep['V'],rep['E'],rep['F'],rep['counts'],rep['weak'],flush=True)
 for epoch in range(a.epochs):
  s.forcedp={};s.forcedq={};s.last=None;v,J,g=s.evaluate(z);X=g['X'];c=g['centroid'] if 'centroid' in g else g['g'];p,pc=routing(X-c,s.U,a.power);q,qc=routing(g['Q']/(1-g['Q']@c)[:,None],s.S,a.power);s.forcedp=p;s.forcedq=q;s.last=None;(a.out/('ROUTES_'+str(epoch)+'.json')).write_bytes(B(dict(primal=p,polar=q)));old=z.copy();z=repair(s,z,a.out/str(epoch),steps=a.steps,goal=a.goal);v,J,g=s.evaluate(z);row=dict(epoch=epoch,minimum=float(v[:s.mechlen-2].min()),slack=float(g['slack'].min()),change=float(np.linalg.norm(z-old)));history.append(row);print('ROOTED_ROUTING_EPOCH',row,flush=True);GG=copy.deepcopy(s.G);GG['grid']=10**12;GG['controls']=np.rint(g['Y']*GG['grid']).astype(np.int64).tolist();(a.out/'GENERATOR.json').write_bytes(B(GG));(a.out/'Z.json').write_bytes(B([float(x).hex() for x in z]));(a.out/'HISTORY.json').write_bytes(B(history));(a.out/'STATUS.json').write_bytes(B(row))
  if row['minimum']>0 and row['slack']>0:print('POSITIVE_NUMERICAL_ROUTING_ONLY',flush=True);break
  if row['change']<1e-15:break
if __name__=='__main__':main()
