"""Exact new-vs-parent incidence, coordinate and filled-mass comparison.
Parent cycles are literal immutable evidence; new cycles come from full A/B.
"""
import json,itertools,sys
from pathlib import Path
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'parent'))
import RECONSTRUCT

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def owners(fs,n):
 out=[set() for _ in range(n)]
 for f,cy in enumerate(fs):
  for i in cy:out[i].add(f)
 return out

def run(a,raw,pair=(67,72)):
 av,bv=pair
 fs=json.loads((R/'C628_WINNER/faces.json').read_text());oo=owners(fs,179);nn=owners(a['faces'],a['V']);union=oo[av]|oo[bv]
 ix={tuple(sorted(o)):i for i,o in enumerate(nn)};assert len(ix)==178
 mapping=[ix[tuple(sorted(union if i in pair else o))] for i,o in enumerate(oo)]
 assert mapping[av]==mapping[bv] and len(set(mapping))==178
 rebuilt=[];oldedges=set()
 for cy in fs:
  cc=[]
  for i,j in zip(cy,cy[1:]+cy[:1]):oldedges.add(tuple(sorted((i,j))))
  for i in cy:
   if not cc or mapping[i]!=cc[-1]:cc.append(mapping[i])
  if cc[0]==cc[-1]:cc.pop()
  k=cc.index(min(cc));rebuilt.append(cc[k:]+cc[:k])
 assert rebuilt==a['faces'];newedges={tuple(sorted((mapping[i],mapping[j]))) for i,j in oldedges if mapping[i]!=mapping[j]}
 assert newedges==set(map(tuple,a['edges']));collapsed=sorted((i,j) for i,j in oldedges if mapping[i]==mapping[j]);assert collapsed==[tuple(sorted(pair))]
 H=RECONSTRUCT.recover(json.loads((R/'C628_WINNER/GENERATOR.json').read_text()))['H'];P=[]
 for ids in oo:
  for i,j,k in itertools.combinations(sorted(ids),3):
   aa,bb,cc=[H[t][:3] for t in [i,j,k]];dv=det(aa,bb,cc)
   if not dv:continue
   xx=cross(bb,cc);yy=cross(cc,aa);zz=cross(aa,bb)
   p=tuple(F(H[i][3]*xx[t]+H[j][3]*yy[t]+H[k][3]*zz[t],dv) for t in range(3));break
  else:raise AssertionError('parent vertex has no independent owner triple')
  assert all(dot(r[:3],p)<=r[3] for r in H)
  P.append(p)
 W=F(0);M=[F(0)]*3
 for fi,cy in enumerate(fs):
  assert all(dot(H[fi][:3],P[i])==H[fi][3] for i in cy)
  for j in range(1,len(cy)-1):
   pp=[P[i] for i in [cy[0],cy[j],cy[j+1]]];d=det(*pp);assert d>0;W+=d/6
   for k in range(3):M[k]+=d*sum(v[k] for v in pp)/24
 newp=[tuple(map(F,p)) for p in a['raw_vertices']]
 changed=sum(any(F(o[k],o[3])!=F(n[k],n[3]) for k in range(3)) for o,n in zip(H,raw['H']));unchanged=[i for i,p in enumerate(P) if p==newp[mapping[i]]]
 oldlex={p:i for i,p in enumerate(sorted(P))};construction_to_oldlex=[oldlex[p] for p in P]
 g=[v/W for v in M];dw=F(a['ordinary_volume'])-W
 return dict(parent_construction_to_rawlex=construction_to_oldlex,parent_to_new_vertex=mapping,collapsed_parent_edges=collapsed,collapsed_parent_rawlex_edges=[sorted([construction_to_oldlex[i],construction_to_oldlex[j]]) for i,j in collapsed],new_vertex=mapping[av],new_vertex_owners=sorted(union),old_counts=[179,314,137],new_counts=[a['V'],a['E'],a['F']],mapped_edge_set_equals_actual=True,mapped_maximal_faces_equal_actual=True,changed_retained_supports=changed,unchanged_parent_raw_vertices=unchanged,volume_change_sign=(dw>0)-(dw<0),volume_change_decimal=float(dw),centroid_change_decimal=[float(F(v)-w) for v,w in zip(a['raw_centroid'],g)])
if __name__=='__main__':
 p=Path(sys.argv[1]);a=json.loads((p/'A.json').read_text());raw=json.loads((p/'raw.json').read_text());out=run(a,raw);(p/'COMPARISON.json').write_text(json.dumps(out,sort_keys=True,separators=(',',':')));print(json.dumps(out,indent=2))
