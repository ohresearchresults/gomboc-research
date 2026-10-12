"""C32_ELEVEN_FRAME_CANONICAL_JOINT_QUOTIENT_V1.
CPython 3.13.5, stdlib; run after joint_frontier.py join:
python -S quotient_frontier.py > quotient_frontier.log
The complete generator and both exact inputs are supplied inline in the handoff.
"""
import json
from pathlib import Path
from collections import Counter
from joint_frontier import PARENT,CATPIN,WHOLE,PRIMAL,Map,serial,pin,outrows,graph_mask,rooted,code,CODES
assert __debug__
INPIN=[10444324,'4ddd4d8f8b33c502ceedb617ab7f1c75c5dd3b22dbca0d30a6235ef991df9e93']
b=Path('joint_frontier.json').read_bytes();assert pin(b)==INPIN
x=json.loads(b);assert x['parent']==PARENT and x['catalogue_pin']==CATPIN
rows=[];total=Counter();active=Counter()
def mask_image(mask,pi):
 return sum(1<<(9*pi[i]+pi[j]) for i in range(9) for j in range(9) if mask>>(9*i+j)&1)
def tree_image(p,pi):
 out=[0]*9
 for i in range(9):out[pi[i]]=pi[p[i]]
 return tuple(out)
for r in x['maps']:
 aut=r['automorphisms'];fa=r['facet_automorphisms'];M=Map(r['facets'])
 states={};branches={};zerochoices=set()
 for ri,(bi,toggle,s,hm,ws,fp,fq) in enumerate(r['records']):
  pi=r['brooms'][bi]
  ee=[(pi[i],pi[PRIMAL[0][i]]) for i in range(1,9)]
  if toggle:ee.append((pi[2],pi[8]))
  gm=graph_mask(outrows(ee))
  images=[(mask_image(gm,a),mask_image(hm,b)) for a,b in zip(aut,fa)];key=min(images)
  z=states.setdefault(key,dict(matches=set(),origins=set()))
  for ai,k in enumerate(images):
   if k!=key:continue
   a,b=aut[ai],fa[ai];z['origins'].add((ri,ai))
   for choice in {w[0] for w in ws}:
    p=[0]*9
    for i in range(9):p[pi[i]]=pi[PRIMAL[choice][i]]
    p1=tree_image(p,a);s1=b[s];z['matches'].add((p1,s1))
  for choice in {w[0] for w in ws}:
   p=[0]*9
   for i in range(9):p[pi[i]]=pi[PRIMAL[choice][i]]
   keyb=min((tree_image(p,a),b[s]) for a,b in zip(aut,fa))
   branches.setdefault(keyb,set()).add((ri,choice))
   if choice==0:zerochoices.add((bi,s))
 assert len(branches)==len(zerochoices)
 for (gm,hm),z in states.items():
  assert 1<=len(z['matches'])<=2
  for p,s in z['matches']:
   u=next(i for i in range(9) if p[i]==i)
   pe={tuple(sorted((i,p[i]))) for i in range(9) if i!=u}
   assert pe<=M.edges.keys() and all(i==u or gm>>(9*i+p[i])&1 for i in range(9))
   dp=rooted([tuple(M.edges[e]) for e in sorted(M.edges) if e not in pe],s)
   assert code(dp,s) in CODES and all(i==s or hm>>(9*i+dp[i])&1 for i in range(9))
 qstates=[[g,h,sorted(z['matches']),sorted(z['origins'])] for (g,h),z in sorted(states.items())]
 qbranches=[[p,s,sorted(orig)] for (p,s),orig in sorted(branches.items())]
 counts=dict(graph_orbits=len(states),matching_orbits=len(branches),two_matching_states=sum(len(z['matches'])==2 for z in states.values()))
 total.update(counts)
 if r['id'] not in WHOLE:active.update(counts)
 rows.append(dict(id=r['id'],counts=counts,states=qstates,matching_branches=qbranches))
assert total['graph_orbits']==90962 and total['matching_orbits']==24597
assert active['graph_orbits']==87519 and active['matching_orbits']==23640
assert total['two_matching_states']==0
gained=[]
for r in x['maps']:
 if r['id'] not in WHOLE:
  remaining=set(map(tuple,r['remaining_joint_roots']))
  gained.extend([r['id'],u,s] for u,s in r['coarse_joint_roots'] if (u,s) not in remaining)
assert len(gained)==65
# Small literal whole-root certificate, checked against the complete enumeration.
f62=[[0,1,3],[0,2,4,1],[0,3,6,7,5,2],[1,4,6,3],[2,5,4],[4,5,8],[4,7,6],[4,8,7],[5,7,8]]
r=x['maps'][62];assert r['facets']==f62
pi62=[(8,5,2,4,6,3,0,1,7),(8,5,2,4,6,3,1,0,7)]
assert [tuple(p) for p in r['brooms'] if p[0]==8]==pi62
M=Map(f62);dual_edges=[];profiles=[]
for pi in pi62:
 assert tuple(sorted((pi[2],pi[8]))) not in M.edges
 pe={tuple(sorted((pi[i],pi[PRIMAL[0][i]]))) for i in range(1,9)}
 de=sorted(tuple(sorted(M.edges[e])) for e in sorted(M.edges) if e not in pe);dual_edges.append(de)
 assert all(code(rooted(de,s),s) not in CODES for s in range(9))
 deg=Counter(v for e in de for v in e);profiles.append(sorted(deg.values()))
assert profiles==[[1,1,1,2,2,2,2,2,3],[1,1,1,1,2,2,2,2,4]]
proof62=dict(map=62,U=8,facets=f62,edges=sorted(M.edges),automorphisms=r['automorphisms'],
 terminal_brooms=pi62,dual_complement_edges=dual_edges,degree_profiles=profiles,stable_roots_checked=9)
assert x['new_unconditional_U']==[[k,3] for k in [40,50,102,108,109,113,114,137,191,240,260]]
assert len(x['new_target_U'])==66 and len(x['new_target_S'])==5
assert len(x['newly_excluded_joint_roots'])==7805 and len(x['remaining_joint_roots'])==12954
report=dict(tag='C32_ELEVEN_FRAME_CANONICAL_JOINT_QUOTIENT_V1',parent=PARENT,input_pin=INPIN,
 counts=dict(total),counts_outside_17=dict(active),new_unconditional_U=x['new_unconditional_U'],
 new_target_U=x['new_target_U'],new_target_S=x['new_target_S'],new_whole_types=x['new_whole_types'],
 newly_excluded_joint_roots=x['newly_excluded_joint_roots'],remaining_joint_roots=x['remaining_joint_roots'],
 literal_root62_certificate=proof62,new_cut_gain_over_coarse=gained,maps=rows)
out=serial(report);Path('quotient_frontier.json').write_bytes(out)
print('ALL_VERTEX_FACET_AUTOMORPHISM_AND_BOTH_MATCHING_TRANSPORTS_PASS')
print('COUNTS',json.dumps(dict(total),sort_keys=True,separators=(',',':')))
print('OUTSIDE_17',json.dumps(dict(active),sort_keys=True,separators=(',',':')))
print('ALL_ALT_BRANCHES_RETAINED_THEN_IDENTIFIED_BY_ACTUAL_RELABELING_PASS')
print('CANONICAL62_U8_TWO_COMPLEMENTS_ALL_NINE_S_ROOTS_EXCLUDED_PASS')
print('UNIQUE_COMPATIBLE_MATCHING_FOR_EVERY_PUTATIVE_C32_TARGET_PASS')
print('ADDITIONAL_JOINT_ROOTS_BEYOND_COARSE',len(gained))
print('JOINT_PARTITION',868,55,7805,12954)
print('NEW_UNCONDITIONAL_U',11,'NEW_TARGET_U',66,'NEW_TARGET_S',5,'NEW_WHOLE_TYPES',0)
print('GRAPH_ORBITS_NOT_PHYSICAL_ATTAINABILITY')
print('REPORT',*pin(out));print('SOURCE',*pin(Path(__file__).read_bytes()))
