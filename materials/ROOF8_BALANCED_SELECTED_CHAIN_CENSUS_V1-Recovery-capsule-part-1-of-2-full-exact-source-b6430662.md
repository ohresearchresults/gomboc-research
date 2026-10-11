# material-b6430662481d

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""ROOF8_BALANCED_SELECTED_CHAIN_CENSUS_V1; exact standard-library generator.
Combinatorial rooted-pair domains, not geometric realizations or 110 attainers.
Run with assertions enabled: python -S roof8_balanced_chain_census.py build|check
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib,json,sys
assert __debug__
FACES=[(0,1,2,3,4,5,6,7),(0,8,1),(1,8,2),(2,8,3),
       (3,8,9,4),(4,9,5),(5,9,6),(6,9,7),(7,9,8,0)]
VERT=[(-2,-1,0),(-3,F(-1,2),0),(-3,F(1,2),0),(-2,1,0),
      (2,1,0),(3,F(1,2),0),(3,F(-1,2),0),(2,-1,0),(-1,0,1),(1,0,1)]
CYCLES={8:(1,2,3,4,8),9:(4,5,6,7,8)}

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def scale(a,s):return tuple(s*x for x in a)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def edge(a,b):return tuple(sorted((a,b)))

def true_complex():
 P=[tuple(map(F,v)) for v in VERT];arcs={};normals=[]
 for cy in FACES:
  n=cross(sub(P[cy[1]],P[cy[0]]),sub(P[cy[2]],P[cy[0]]));assert any(n)
  normals.append(n)
  for i,p in enumerate(P):
   value=dot(n,sub(p,P[cy[0]]))
   assert value==0 if i in cy else value<0
  for a,b in zip(cy,cy[1:]+cy[:1]):
   assert (a,b) not in arcs;arcs[a,b]=1
 assert len(arcs)==34 and all((b,a) in arcs for a,b in arcs)
 edges=sorted({edge(a,b) for a,b in arcs});assert len(edges)==17
 hull=set()
 for i,j,k in combinations(range(10),3):
  n=cross(sub(P[j],P[i]),sub(P[k],P[i]))
  if not any(n):continue
  values=[dot(n,sub(p,P[i])) for p in P]
  if min(values)>=0 or max(values)<=0:hull.add(tuple(t for t,v in enumerate(values) if not v))
 assert hull=={tuple(sorted(cy)) for cy in FACES}
 dual=[]
 for a,b in edges:
  fs=tuple(i for i,cy in enumerate(FACES) if a in cy and b in cy)
  assert len(fs)==2;dual.append(fs)
 triangles=[(cy[0],cy[j],cy[j+1]) for cy in FACES for j in range(1,len(cy)-1)]
 T=F(0);mom=(F(0),)*3
 for i,j,k in triangles:
  d=det(P[i],P[j],P[k]);T+=d;mom=add(mom,scale(add(add(P[i],P[j]),P[k]),d))
 c=scale(mom,1/(4*T));assert T>0
 assert T/6==F(13,3) and c==(0,0,F(15,52))
 X=[sub(p,c) for p in P]
 Q=[scale(n,1/dot(n,X[cy[0]])) for n,cy in zip(normals,FACES)]
 moment=(F(0),)*3;total=F(0)
 for i,j,k in triangles:
  d=det(X[i],X[j],X[k]);assert d>0;total+=d
  moment=add(moment,scale(add(add(X[i],X[j]),X[k]),d))
 assert total==T and moment==(0,0,0)
 G=[[dot(a,b) for b in X] for a in X];J=[[dot(a,b) for b in Q] for a in Q]
 U=[i for i in range(10) if all(G[i][j]<G[i][i] for j in range(10) if edge(i,j) in edges)]
 S=[i for i in range(9) if all(J[i][j]<J[i][i] for j in range(9) if i!=j)]
 H=[];deg=[];harmless=[]
 for eid,((a,b),(f,g)) in enumerate(zip(edges,dual)):
  slopes=[G[a][b]-G[a][a],G[a][b]-G[b][b],J[f][g]-J[f][f],J[f][g]-J[g][g]]
  if max(slopes)<0:H.append(eid)
  elif max(slopes)==0:deg.append([eid,slopes])
  elif any(v==0 for v in slopes):harmless.append([eid,slopes])
 assert len(U)>1 and (len(S),len(U),len(H))!=(1,1,0)
 degrees=[sum(v in e for e in edges) for v in range(10)]
 assert degrees==[3]*8+[5,5]
 for x,cy in CYCLES.items():
  assert set(cy)=={i for i,f in enumerate(FACES) if x in f}
  for i in range(5):
   e=tuple(sorted(set(FACES[cy[i]])&set(FACES[cy[(i+1)%5]])))
   assert len(e)==2 and x in e and e in edges
 return edges,dual,{'scope':'ACTUAL_OWN_COM_NEGATIVE_CONTROL_NOT_110',
  'vertices':P,'maximal_faces':FACES,'true_edges':edges,'dual_pairs_in_edge_order':dual,
  'f_vector':[10,17,9],'volume':T/6,'centroid_raw':c,'centered_vertices':X,'poles':Q,
  'M_diagonal':[1,1,1],'N_diagonal':[1,1,1],'vertex_degrees':degrees,
  'strict_stable_facets':S,'strict_unstable_vertices':U,'strict_saddle_edge_ids':H,
  'degenerate_edge_records':deg,'harmless_zero_edge_records':harmless,
  'S_U_H':[len(S),len(U),len(H)]}

def is_tree(n,edges):
 if len(edges)!=n-1:return False
 p=list(range(n))
 def root(x):
  while p[x]!=x:x=p[x]
  return x
 for a,b in edges:
  a=root(a);b=root(b)
  if a==b:return False
  p[a]=b
 return True

def parents(n,edges,root):
 adj=[[] for _ in range(n)]
 for a,b in edges:adj[a].append(b);adj[b].append(a)
 p=[-1]*n;p[root]=root;queue=[root]
 for a in queue:
  for b in sorted(adj[a]):
   if p[b]<0:p[b]=a;queue.append(b)
 assert len(queue)==n
 return p

def determinant(A):
 A=[list(map(F,row)) for row in A];out=F(1)
 for j in range(len(A)):
  k=next((i for i in range(j,len(A)) if A[i][j]),None)
  if k is None:return F(0)
  if k!=j:A[k],A[j]=A[j],A[k];out=-out
  v=A[j][j];out*=v
  for i in range(j+1,len(A)):
   factor=A[i][j]/v
   for h in range(j,len(A)):A[i][h]-=factor*A[j][h]
 return out

def tree_number(n,edges):
 L=[[0]*n for _ in range(n)]
 for a,b in edges:L[a][a]+=1;L[b][b]+=1;L[a][b]-=1;L[b][a]-=1
 d=determinant([row[:-1] for row in L[:-1]]);assert d.denominator==1
 return int(d)

def patterns(x,pv,pq,edges,dual,mask):
 z=17-x;cy=CYCLES[x];out=[]
 for start in range(5):
  for direction in (-1,1):
   path=[cy[(start+direction*j)%5] for j in range(5)]
   if pq[0]!=path[0] or any(pq[path[j]]!=path[j+1] for j in range(4)):continue
   closing=tuple(sorted(set(FACES[path[0]])&set(FACES[path[-1]])))
   assert len(closing)==2 and x in closing
   closing_id=edges.index(closing)
   assert mask>>closing_id&1
   assert [e for eid,e in enumerate(edges) if x in e and mask>>eid&1]==[closing]
   if closing==edge(x,z):
    assert pv[z]==x;kind='XZ_CLOSING_546'
   else:
    assert pv[z] in range(8);kind='BASE_ESCAPE_SUPPORT_497'
   out.append({'pole_chain':path,'base_arrow':[0,path[0]],'closing_edge':closing,
               'primal_z_parent':pv[z],'criterion':kind})
 assert len(out)<=1
 return out

def census(edges,dual):
 fullmask=(1<<17)-1
 masks=[];records=[]
 counters={str(x):{'rooted_pairs':0,'covered':0,'xz546':0,'base497':0} for x in (8,9)}
 by_s={str(x):{str(s):{'covered':0,'xz546':0,'base497':0} for s in range(9)} for x in (8,9)}
 choices=0
 for selected in combinations(range(17),9):
  choices+=1
  pe=[edges[i] for i in selected]
  if not is_tree(10,pe):continue
  mask=sum(1<<i for i in selected);de=[dual[i] for i in range(17) if not(mask>>i&1)]
  assert is_tree(9,de);masks.append(mask)
  for x in (8,9):
   pv=parents(10,pe,x)
   for s in range(9):
    pq=parents(9,de,s);found=patterns(x,pv,pq,edges,dual,mask)
    counters[str(x)]['rooted_pairs']+=1
    if not found:continue
    pat=found[0];kind='xz546' if pat['criterion']=='XZ_CLOSING_546' else 'base497'
    counters[str(x)]['covered']+=1;counters[str(x)][kind]+=1
    by_s[str(x)][str(s)]['covered']+=1;by_s[str(x)][str(s)][kind]+=1
    records.append({'primal_edge_mask':mask,'primal_root':x,'dual_root':s,
                    'primal_parent':pv,'dual_parent':pq,'pattern':pat})
 assert choices==24310
 tau=tree_number(10,edges)
 assert tau==len(masks)==tree_number(9,dual)
 assert counters['8']==counters['9']
 for x in (8,9):
  d=counters[str(x)];assert d['rooted_pairs']==9*tau and d['covered']==d['xz546']+d['base497']
  d['not_covered_by_this_unit']=d['rooted_pairs']-d['covered']
  assert d['not_covered_by_this_unit']>0
 # Native reflection swaps apices and the two halves of the base polygon.
 reflection=[7,6,5,4,3,2,1,0,9,8]
 fmap=[next(j for j,g in enumerate(FACES) if {reflection[v] for v in f}==set(g)) for f in FACES]
 assert all(edge(reflection[a],reflection[b]) in edges for a,b in edges)
 keys={(r['primal_edge_mask'],r['primal_root'],r['dual_root']) for r in records}
 assert len(keys)==len(records)
 for mask,x,s in keys:
  rm=sum(1<<edges.index(edge(reflection[a],reflection[b])) for i,(a,b) in enumerate(edges) if mask>>i&1)
  assert (rm,reflection[x],fmap[s]) in keys
 return {'identity':'ROOF8_BALANCED_SELECTED_CHAIN_CENSUS_V1',
  'scope':'ALL_COMBINATORIAL_COMPLEMENTARY_ROOTED_PAIRS_ON_THIS_NATIVE_COMPLEX_WITH_U_ROOT_8_OR_9',
  'not_a_geometric_feasibility_test':True,'not_the_historical_FULL_LOCAL_register':True,
  'edge_order':edges,'dual_pairs_in_same_order':dual,'root_cycles':CYCLES,
  'examined_nine_edge_subsets':choices,'spanning_trees_each_side':tau,
  'all_primal_tree_masks_in_combination_order':masks,
  'rooted_pair_counts':counters,'covered_counts_by_dual_root':by_s,
  'covered_records':records,'reflection_vertex_map':reflection,'reflection_facet_map':fmap,
  'entire_face_lattice_excluded':False,'C_lower_unchanged':34,'C_upper_unchanged':622}

def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,(list,tuple)):return [encode(v) for v in x]
 if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
 return x

def build():
 edges,dual,control=true_complex();out=census(edges,dual);out['actual_geometric_negative_control']=control
 return (json.dumps(encode(out),sort_keys=True,separators=(',',':'))+'\n').encode('utf-8')

if __name__=='__main__':
 if sys.argv[1:] not in (['build'],['check']):raise SystemExit('usage: python -S roof8_balanced_chain_census.py build|check')
 b=build();path=Path('roof8_balanced_chain_census.json')
 if sys.argv[1]=='build':
  if path.exists():assert path.read_bytes()==b
  path.write_bytes(b)
 else:assert path.read_bytes()==b
 out=json.loads(b)
 print('ACTUAL_ROOF8_BALANCED_10_17_9_OWN_COM_NEGATIVE_CONTROL_PASS')
 print('ALL_24310_SUBSETS_AND_COMPLEMENTARY_ROOTED_TREE_PAIRS_PASS')
 print('SELECTED_CHAIN_CLOSING_AND_Z_PARENT_DICHOTOMY_PASS')
 print(json.dumps(out['rooted_pair_counts'],sort_keys=True,separators=(',',':')))
 print(path.name,len(b),hashlib.sha256(b).hexdigest())
 print('ROOF8_BALANCED_SELECTED_CHAIN_CENSUS_RECOVERY_PASS')
