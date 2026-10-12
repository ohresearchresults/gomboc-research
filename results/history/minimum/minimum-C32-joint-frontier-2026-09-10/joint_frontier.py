"""C32_ELEVEN_FRAME_INCIDENCE_FRONTIER_V1. CPython 3.13.5, stdlib only.
Run after the inline recover_c32_complete.py: python -S joint_frontier.py
No locator, coefficient replay, random seed, or external geometric input.
"""
from itertools import combinations,permutations,product
from collections import Counter
from functools import lru_cache
from pathlib import Path
import json,hashlib,sys
assert __debug__
PARENT=['asg_OJ_qMzsRl-4mqDIQPGHGscQE','2cd8dc8ea75a5a8d1eaa9fabfca75a65181325fab676cd95dec5cd1c16426a59']
CATPIN=[240929,'efb10a4657a891cd13f6f62db94164bd4b3005e908dc55aae87db450930f704d']
TREES={253:(0,0,1,2,3,4,5,0,7),266:(0,0,1,2,3,4,5,4,0),272:(0,0,1,2,3,4,5,5,0),278:(0,0,1,2,3,4,5,6,0),285:(0,0,1,2,3,4,5,6,7)}
FRAMES={253:[[]],266:[[(5,7),(6,7)],[(6,7),(7,5)],[(7,5),(7,6)]],272:[[(6,4),(6,7)],[(6,4),(7,6)],[(6,7),(7,4)],[(7,4),(7,6)]],278:[[(6,4),(7,5)],[(7,4),(7,5)]],285:[[]]}
PRIMAL=[(0,0,1,2,3,4,5,6,0),(0,0,8,2,3,4,5,6,0)]
WHOLE={33,34,72,139,149,152,159,163,164,178,192,217,284,288,293,294,295}
PARTIAL={35:3,45:3,47:3,49:3,51:3,53:3,282:0,290:3}
ALL=set(range(9))
def serial(x):return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
def und(a,b):return (min(a,b),max(a,b))
def code(p,root):
 ch=[[] for _ in p]
 for i,j in enumerate(p):
  if i!=root:ch[j].append(i)
 def walk(i):return '('+''.join(sorted(walk(j) for j in ch[i]))+')'
 return walk(root)
CODES={code(p,0):o for o,p in TREES.items()}
def rooted(edges,root):
 adj=[[] for _ in range(9)];p=[-1]*9;p[root]=root;todo=[root]
 for a,b in edges:adj[a].append(b);adj[b].append(a)
 for a in todo:
  for b in adj[a]:
   if p[b]<0:p[b]=a;todo.append(b)
 assert len(todo)==9 and len(edges)==8
 return tuple(p)
def outrows(arcs):
 es=tuple(arcs);return tuple(frozenset(b for a,b in es if a==i) for i in range(9))
def arcs(rows):return tuple((i,j) for i,r in enumerate(rows) for j in sorted(r))
def graph_mask(rows):return sum(1<<(9*i+j) for i,r in enumerate(rows) for j in r)
def from_mask(mask):return tuple(frozenset(j for j in range(9) if mask>>(9*i+j)&1) for i in range(9))
def connected(vs,adj):
 if not vs:return True
 seen={min(vs)};todo=list(seen)
 for v in todo:
  for w in adj[v]&vs:
   if w not in seen:seen.add(w);todo.append(w)
 return seen==vs
def interval(vs,cyc):
 flags=[v in vs for v in cyc]
 return sum(flags[i]!=flags[i-1] for i in range(len(flags)))<=2
class Map:
 def __init__(self,faces):
  self.faces=tuple(tuple(f) for f in faces);self.edges={};rot=[{} for _ in range(9)];dart={}
  for i,f in enumerate(self.faces):
   assert len(f)>=3 and len(set(f))==len(f)
   for k,v in enumerate(f):
    w=f[(k+1)%len(f)];prev=f[k-1]
    assert (v,w) not in dart;dart[v,w]=i;rot[v][prev]=w
    self.edges.setdefault(und(v,w),[]).append(i)
  assert len(self.edges)==16 and all(len(v)==2 for v in self.edges.values())
  assert all((b,a) in dart for a,b in dart)
  self.adj=tuple(frozenset(w for a,w in dart if a==v) for v in range(9))
  links=[];dual=[]
  for v in range(9):
   w=min(rot[v]);cy=[];df=[]
   while w not in cy:cy.append(w);df.append(dart[v,w]);w=rot[v][w]
   assert w==cy[0] and set(cy)==set(rot[v]) and len(cy)>=3
   links.append(tuple(cy));dual.append(tuple(df))
  self.links=tuple(links);self.dual_faces=tuple(dual)
 def cut_ok(self,G):
  # Linear-functional cuts of a genuine convex polytope, not fitted metrics.
  for i,S in enumerate(G):
   if S and not connected(set(S),self.adj):return False
   if not connected(ALL-{i}-set(S),self.adj):return False
   if self.adj[i]<=S or not interval(S,self.links[i]):return False
   nonneg=set(S)|{i}
   for f in self.faces:
    if not interval(nonneg,f):return False
    if i in f:
     k=f.index(i);two={f[k-1],f[(k+1)%len(f)]}
     if two<=S and not set(f)-{i}<=S:return False
     if not two&S and (set(f)-{i})&S:return False
  return True
 def projection(self,G,H):
  # Weak two-edge triangle chain, strict missing skip: forced positive dual exit.
  forced=set()
  for f,vs in enumerate(self.faces):
   if len(vs)!=3:continue
   for a,b,c in permutations(vs):
    if a not in G[b] or b not in G[c] or a in G[c]:continue
    other=next(j for j in self.edges[und(a,c)] if j!=f)
    neighbors={j for e,ff in self.edges.items() if f in ff for j in ff if j!=f}
    if other not in H[f] or (H[f]&neighbors)!={other}:return None
    forced.add((f,other))
  return tuple(sorted(forced))
 def no_dominator(self,G,face):
  vs=self.faces[face]
  return not any(all(w==v or w in G[v] or v in G[w] for w in vs) for v in vs)
# All 25 graphs of the immutable parent's 11-frame cover, in exact tree labels.
COVER={}
for o,frames in FRAMES.items():
 xs=set()
 for fr in frames:
  for bits in range(1<<len(fr)):xs.add(tuple(sorted(fr[k] for k in range(len(fr)) if bits>>k&1)))
 COVER[o]=sorted(xs)
 assert len(COVER[o])=={253:1,266:8,272:9,278:6,285:1}[o]
 for extra in COVER[o]:
  ee={(i,TREES[o][i]) for i in range(1,9)}|set(extra);G=outrows(ee)
  orders=[]
  for choices in product(*(sorted(G[i]) for i in range(1,9))):
   p=(0,)+choices
   for i in range(1,9):
    seen=set();j=i
    while j:assert j not in seen;seen.add(j);j=p[j]
   assert code(p,0) in CODES;orders.append(p)
  assert len(orders)<=4 and len(ee)<=10
assert sum(map(len,COVER.values()))==25
@lru_cache(None)
def transports(p,s,o):
 # Every root-preserving isomorphism from literal TREE o to this actual cotree.
 source=TREES[o];cs=[[] for _ in range(9)];ct=[[] for _ in range(9)]
 for i in range(1,9):cs[source[i]].append(i)
 for i in range(9):
  if i!=s:ct[p[i]].append(i)
 def shape(ch,i):return '('+''.join(sorted(shape(ch,j) for j in ch[i]))+')'
 def rec(a,b):
  aa=cs[a];bb=ct[b]
  if len(aa)!=len(bb):return []
  out=[]
  for order in permutations(bb):
   if any(shape(cs,x)!=shape(ct,y) for x,y in zip(aa,order)):continue
   lists=[rec(x,y) for x,y in zip(aa,order)]
   for parts in product(*lists):
    d={a:b}
    for part in parts:d.update(part)
    out.append(d)
  return out
 result=sorted({tuple(d[i] for i in range(9)) for d in rec(0,s)})
 assert result and all(sorted(pi)==list(range(9)) and pi[0]==s and all(p[pi[i]]==pi[source[i]] for i in range(1,9)) for pi in result)
 return result

def paths_dfs(M):
 # Directed Hamiltonian paths: short leaf, root, then the seven-edge long arm.
 raw=[]
 def walk(p,used):
  if len(p)==9:raw.append(tuple(p[1:]+p[:1]));return
  for w in sorted(M.adj[p[-1]]-used):walk(p+[w],used|{w})
 for v in range(9):walk([v],{v})
 return set(raw)
def paths_subsets(M):
 # Independent exhaustion of all binomial(16,8) true-edge subsets.
 result=set();ee=sorted(M.edges)
 for ids in combinations(range(16),8):
  adj=[[] for _ in range(9)]
  for k in ids:
   a,b=ee[k];adj[a].append(b);adj[b].append(a)
  ends=[i for i in range(9) if len(adj[i])==1]
  if len(ends)!=2 or any(len(a) not in (1,2) for a in adj):continue
  p=[ends[0]]
  while len(p)<9:
   ns=[w for w in adj[p[-1]] if len(p)==1 or w!=p[-2]]
   if not ns:break
   p.append(ns[0])
   if len(set(p))!=len(p):break
  if len(p)!=9 or p[-1]!=ends[1] or len(set(p))!=9:continue
  for q in (p,p[::-1]):result.add(tuple(q[1:]+q[:1]))
 return result

def run_map(m):
 M=Map(m['facets']);D=Map(M.dual_faces);assert {frozenset(f) for f in D.dual_faces}=={frozenset(f) for f in M.faces}
 assert sorted(M.edges)==[tuple(e) for e in m['edges']]
 aut=[tuple(a) for a in m['automorphisms']];fsets=list(map(frozenset,M.faces));fperm=[]
 for a in aut:
  assert sorted(a)==list(range(9))
  fperm.append(tuple(fsets.index(frozenset(a[v] for v in f)) for f in M.faces))
 def orbit(pi):return min(tuple(a[v] for v in pi) for a in aut)
 def rootpair(u,s):return min((a[u],b[s]) for a,b in zip(aut,fperm))
 allpaths=paths_dfs(M);assert allpaths==paths_subsets(M)
 brooms=sorted({orbit(pi) for pi in allpaths if frozenset(pi[5:8]) in fsets})
 assert sum(frozenset(pi[5:8]) in fsets for pi in allpaths)==len(aut)*len(brooms)
 root_pre={min(a[u] for a in aut):0 for u in range(9)};root_post=root_pre.copy()
 for pi in {orbit(pi) for pi in allpaths}:root_pre[min(a[pi[0]] for a in aut)]+=1
 for pi in brooms:root_post[min(a[pi[0]] for a in aut)]+=1
 counts=Counter();states={};coarse=[];coarse_roots=set();strict_graphs=0
 @lru_cache(None)
 def qcut(mask):return D.cut_ok(from_mask(mask))
 for bi,pi in enumerate(brooms):
  base={(pi[i],pi[PRIMAL[0][i]]) for i in range(1,9)};opt=(pi[2],pi[8])
  GP=[outrows(base),outrows(base|{opt})]
  pcut=[M.cut_ok(g) for g in GP]
  if und(*opt) in M.edges and pcut[1]:assert frozenset(pi[i] for i in (1,2,8)) in fsets
  for choice,p in enumerate(PRIMAL):
   pe={und(pi[i],pi[p[i]]) for i in range(1,9)}
   if not pe<=M.edges.keys():continue
   counts['actual_primal_tree_options']+=1
   de=[tuple(M.edges[e]) for e in sorted(M.edges) if e not in pe]
   rooted(list(pe),pi[0]);assert len(set(de))==8
   for s in range(9):
    counts['rooted_complements']+=1;dp=rooted(de,s);treecode=code(dp,s)
    if treecode not in CODES:continue
    o=CODES[treecode];counts['five_shape_complements']+=1
    for toggle in (0,1):
     if choice and not toggle:continue
     G=GP[toggle]
     if not pcut[toggle] or not M.no_dominator(G,s):continue
     # Every isomorphism, not an arbitrary assignment of the canonical dual labels.
     for sigma in transports(dp,s,o):
      for exid,extra in enumerate(COVER[o]):
       he={(sigma[i],sigma[TREES[o][i]]) for i in range(1,9)}|{(sigma[i],sigma[j]) for i,j in extra}
       H=outrows(he);hm=graph_mask(H);counts['raw_frame_graph_instances']+=1
       if not qcut(hm) or not D.no_dominator(H,pi[0]):continue
       ph=M.projection(G,H)
       if ph is None:continue
       hp=D.projection(H,G)
       if hp is None:continue
       key=(bi,toggle,s,hm);wit=(choice,o,sigma,exid)
       if key not in states:states[key]={'witnesses':set(),'forced_primal':hp,'forced_dual':ph}
       states[key]['witnesses'].add(wit)
       assert states[key]['forced_primal']==hp and states[key]['forced_dual']==ph
  # Independent minimal-graph coarse ledger for root comparisons.
  for choice,p in enumerate(PRIMAL):
   pe={und(pi[i],pi[p[i]]) for i in range(1,9)}
   if not pe<=M.edges.keys():continue
   for s in range(9):
    dp=rooted([tuple(M.edges[e]) for e in sorted(M.edges) if e not in pe],s)
    if code(dp,s) not in CODES:continue
    H=outrows((i,dp[i]) for i in range(9) if i!=s)
    if not M.no_dominator(GP[0],s) or M.projection(GP[0],H) is None:continue
    coarse.append((bi,choice,s,CODES[code(dp,s)]));coarse_roots.add(rootpair(pi[0],s))
 records=[];roots=set();matches=set();frame_types=Counter()
 for (bi,toggle,s,hm),r in sorted(states.items()):
  pi=brooms[bi];choices=sorted({w[0] for w in r['witnesses']});H=from_mask(hm)
  # Re-enumerate both actual complementary choices from the final graph itself.
  eligible=[]
  for choice,p in enumerate(PRIMAL):
   if choice and not toggle:continue
   pe={und(pi[i],pi[p[i]]) for i in range(1,9)}
   if not pe<=M.edges.keys():continue
   dp=rooted([tuple(M.edges[e]) for e in sorted(M.edges) if e not in pe],s)
   if all(i==s or dp[i] in H[i] for i in range(9)):eligible.append(choice)
  assert choices==eligible
  if len(choices)==2:
   e0=und(pi[1],pi[2]);e1=und(pi[2],pi[8]);common=set(M.edges[e0])&set(M.edges[e1])
   assert len(common)==1
   f=next(iter(common));assert set(M.faces[f])=={pi[1],pi[2],pi[8]}
   for e in (e0,e1):assert next(j for j in M.edges[e] if j!=f) in H[f]
  for choice in choices:matches.add((bi,choice,s))
  for w in r['witnesses']:frame_types[w[1]]+=1
  roots.add(rootpair(pi[0],s))
  records.append([bi,toggle,s,hm,sorted(r['witnesses']),r['forced_primal'],r['forced_dual']])
 assert roots<=coarse_roots
 counts['brooms']=len(brooms);counts['joint_nonnegative_graph_states']=len(records);counts['matching_cases']=len(matches);counts['joint_root_orbits']=len(roots)
 counts['coarse_cases']=len(coarse);counts['coarse_root_orbits']=len(coarse_roots)
 ur=sorted(root_pre);sr=sorted({min(a[s] for a in fperm) for s in range(9)})
 uremaining={min(a[u] for a in aut) for u,s in roots};sremaining={min(a[s] for a in fperm) for u,s in roots}
 return dict(id=m['id'],facets=M.faces,edges=sorted(M.edges),dual_facets=D.faces,automorphisms=aut,facet_automorphisms=fperm,
  root_pre_terminal=sorted(root_pre.items()),root_post_terminal=sorted(root_post.items()),brooms=brooms,
  counts=dict(counts),records=records,remaining_joint_roots=sorted(roots),coarse_joint_roots=sorted(coarse_roots),
  closed_U=[u for u in ur if u not in uremaining],closed_S=[s for s in sr if s not in sremaining],
  all_joint_roots=m['joint_root_representatives'])

def main():
 raw=Path('c32_catalogue.json').read_bytes();assert pin(raw)==CATPIN
 cat=json.loads(raw);assert cat['types']==296 and cat['joint_root_orbits']==21682
 rows=[];tot=Counter()
 if len(sys.argv)>1 and sys.argv[1]=='part':
  a,b=map(int,sys.argv[2:]);assert 0<=a<b<=296
  rows=[run_map(m) for m in cat['maps'][a:b]]
  Path('part_%03d_%03d.json'%(a,b)).write_bytes(serial(dict(parent=PARENT,range=[a,b],rows=rows)))
  print('PART_PASS',a,b,sum(r['counts']['joint_nonnegative_graph_states'] for r in rows));return
 if len(sys.argv)>1:
  assert sys.argv[1:] == ['join']
  for a in range(0,296,40):
   b=min(a+40,296);p=json.loads(Path('part_%03d_%03d.json'%(a,b)).read_bytes())
   assert p['parent']==PARENT and p['range']==[a,b] and [r['id'] for r in p['rows']]==list(range(a,b))
   rows.extend(p['rows'])
 else:
  rows=[run_map(m) for m in cat['maps']]
 for r in rows:tot.update(r['counts'])
 newU=[];newS=[];unconditional=[];newjoint=[];remainder=[];newwhole=[]
 for r in rows:
  k=r['id']
  if k in WHOLE:continue
  if not r['remaining_joint_roots']:newwhole.append(k)
  for u in r['closed_U']:
   if PARTIAL.get(k)!=u:newU.append([k,u])
  for s in r['closed_S']:newS.append([k,s])
  for u,n in r['root_post_terminal']:
   if n==0 and PARTIAL.get(k)!=u:unconditional.append([k,u])
  rem=set(map(tuple,r['remaining_joint_roots']))
  for u,s in r['all_joint_roots']:
   if PARTIAL.get(k)==u:assert (u,s) not in rem;continue
   (remainder if (u,s) in rem else newjoint).append([k,u,s])
 priorwhole=sum(len(r['all_joint_roots']) for r in rows if r['id'] in WHOLE)
 priorpartial=sum(sum(u==PARTIAL.get(r['id']) for u,s in r['all_joint_roots']) for r in rows if r['id'] not in WHOLE)
 assert priorwhole==868 and priorpartial==55
 assert len(newjoint)+len(remainder)+priorwhole+priorpartial==21682
 assert tot['brooms']==43234 and tot['actual_primal_tree_options']==57350 and tot['rooted_complements']==516150 and tot['five_shape_complements']==40008
 active=Counter()
 for r in rows:
  if r['id'] not in WHOLE:active.update(r['counts'])
 report=dict(tag='C32_ELEVEN_FRAME_INCIDENCE_FRONTIER_V1',parent=PARENT,catalogue_pin=CATPIN,
  inherited_whole_types=sorted(WHOLE),inherited_partial_U=sorted(PARTIAL.items()),trees=TREES,frames=FRAMES,graphs=COVER,
  primal_trees=PRIMAL,counts=dict(tot),counts_outside_inherited_whole=dict(active),
  new_unconditional_U=unconditional,new_target_U=newU,new_target_S=newS,new_whole_types=newwhole,
  prior_whole_joint_orbits=priorwhole,prior_partial_joint_orbits=priorpartial,
  newly_excluded_joint_roots=newjoint,remaining_joint_roots=remainder,maps=rows)
 out=serial(report);Path('joint_frontier.json').write_bytes(out)
 print('INDEPENDENT_DFS_AND_ALL_12870_EDGE_SUBSETS_PER_MAP_PASS',296,43234)
 print('ALL_TRUE_EDGE_PRIMAL_AND_DUAL_TRANSPORTS_MATCHINGS_PASS')
 print('COUNTS',json.dumps(dict(tot),sort_keys=True,separators=(',',':')))
 print('OUTSIDE_ACCEPTED_17',json.dumps(dict(active),sort_keys=True,separators=(',',':')))
 print('NEW_UNCONDITIONAL_U',unconditional)
 print('NEW_TARGET_U',len(newU),newU)
 print('NEW_TARGET_S',len(newS),newS)
 print('JOINT_ROOT_PARTITION',priorwhole,priorpartial,len(newjoint),len(remainder))
 print('NEW_WHOLE_TYPES',newwhole)
 print('GRAPH_SURVIVAL_NOT_PHYSICAL_ATTAINABILITY_NO_C34_CLAIM')
 print('REPORT',*pin(out));print('SOURCE',*pin(Path(__file__).read_bytes()))
if __name__=='__main__':main()
