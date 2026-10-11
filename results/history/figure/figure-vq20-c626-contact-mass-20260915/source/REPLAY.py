"""Complete standard-library source-only exact replay for VQ20_RL07_C626_Z87_127_G1E9."""
import argparse,copy,hashlib,itertools,json,sys
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
sys.set_int_max_str_digits(0)
if not __debug__:raise RuntimeError('Assertions must be enabled; never run with -O')
ROOT=Path(__file__).resolve().parent;sys.path.insert(0,str(ROOT/'parent'))
import RECONSTRUCT,check_A,check_B,centred_mass,chart,chart_audit
NAME='VQ20_RL07_C626_Z87_127_G1E9'
CASES=[
 ('parent','baseline','94b1784349c731f5b19e99444c6eb14507b42a954ea2824f9a4eda6470bbf4ed','bb013ccd179cd000f50b09f030b731bd85661d149e9cd2039d08b0952de877c4',[179,314,137],[1,1,0]),
 ('candidate','endpoint','0d2c8ecffe15e6c36d1ac56ef3167dcf9c2de3d68e416ab165fd5d8ffcd4ea68','da2fa56ff31186699a59b79a1a2bce6362aa362bcd34c735c2fb0a2424d811dd',[178,313,137],[1,1,0]),
 ('nonwinner_warm','nonwinner_warm','4e7470fb802b0eb44bb60e9cba993dc8622c369c07764b179fe53d8560be49e3','f440856cca0bc3ebd73e4ca53822ac027d9764a95fc7f29a7fa5046f2f99ae20',[178,313,137],[95,97,190]),
 ('nonwinner_pentagon','nonwinner_pentagon','e66d560d700c3b8059d08a5bb181e284db859207bdc9e6d8e162858f12144a15','c5ff20a236c0d53c8ff03865968f5707b8d2e33ecf58be50dc2b8f048dd268ac',[178,313,137],[1,2,1])]
def blob(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def sha(x):return hashlib.sha256(x).hexdigest()
def put(p,x):
 b=blob(x);p.write_bytes(b);return sha(b)
def owners(rep):
 return {frozenset(rep['active_input_indices'][f] for f,cy in enumerate(rep['faces']) if v in cy):v for v in range(rep['V'])}
def atlas_audit(G,raw,rep):
 n=G['n_supports'];D=G['grid'];Y=[[F(x,D) for x in row] for row in G['controls']];Y[n]=[F(0),F(0),F(1)]
 for i,deps,axes in G['plan']:
  if deps:
   rest=[a for a in range(3) if a not in axes]
   A=[[Y[j][a] for a in axes] for j in deps];rhs=[1-sum(Y[j][a]*Y[i][a] for a in rest) for j in deps]
   for a,value in zip(axes,RECONSTRUCT.solve(A,rhs)):Y[i][a]=value
  assert all(check_A.dot(Y[i],Y[j])==1 for j in deps)
 Q=[tuple(F(v,row[3]) for v in row[:3]) for row in raw['H']];assert list(map(tuple,Y[:n]))==Q
 own=owners(rep);X=[tuple(map(F,row)) for row in rep['raw_vertices']]
 for j,group in enumerate(G['groups']):
  v=own[frozenset(group)];assert tuple(Y[n+j])==X[v]
  triple=next(t for t in itertools.combinations(group,3) if check_A.det(*(Q[i] for i in t)))
  assert chart.inv3([Q[i] for i in triple],[F(1)]*3)==tuple(Y[n+j])
 axes={i:a for i,d,a in G['plan']};free=[(i,k) for i in range(len(Y)) if i!=n for k in range(3) if k not in axes[i]]
 assert all(Y[i][k]==F(G['controls'][i][k],D) for i,k in free)
 contacts=sum(len(x) for x in G['groups']);assert contacts==sum(len(d) for i,d,a in G['plan'])
 return dict(nodes=len(Y),support_nodes=n,designated_contacts=len(G['groups']),contact_equations=contacts,apex_fixed_coordinates=3,free_coordinates=len(free),free_indices=free,exact_forward_inverse_pass=True)
def bits(raw,a):
 c=tuple(map(F,a['raw_centroid']));X=[tuple(map(F,row)) for row in a['raw_vertices']]
 z=[tuple(v-g for v,g in zip(row,c)) for row in X]
 b={k:chart_audit.stats(a[k]) for k in ('raw_vertices','raw_centroid','ordinary_volume','raw_first_moments')}
 b['H_integers']=chart_audit.stats(raw['H']);b['centred_vertices']=chart_audit.stats(z);return b
def connectivity(n,edges):
 adj=[set() for _ in range(n)]
 for i,j in edges:adj[i].add(j);adj[j].add(i)
 tested=0
 for k in range(3):
  for gone in itertools.combinations(range(n),k):
   deleted=set(gone);start=next(i for i in range(n) if i not in deleted);seen={start};todo=[start]
   while todo:
    i=todo.pop()
    for j in adj[i]-deleted-seen:seen.add(j);todo.append(j)
   assert len(seen)==n-k;tested+=1
 return tested

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);args=ap.parse_args();out=args.out.resolve();out.mkdir(parents=True,exist_ok=False)
 # Source MANIFEST is also verified when running the decoded capsule.
 if (ROOT/'MANIFEST.json').exists():
  for name,want in json.loads((ROOT/'MANIFEST.json').read_text())['files'].items():assert sha((ROOT/name).read_bytes())==want
 reports={};raws={};receipts={}
 for source,label,gsha,rsha,vef,counts in CASES:
  folder=out/label;folder.mkdir();gb=(ROOT/source/'GENERATOR.json').read_bytes();assert sha(gb)==gsha;G=json.loads(gb);raw=RECONSTRUCT.recover(G);rawsha=put(folder/'raw.json',raw);pair=[]
  for name,fun in [('A',check_A.run),('B',check_B.run)]:
   print('START',label,name,flush=True);a=fun(raw);h=put(folder/(name+'.json'),a);pair.append(a)
   assert h==rsha;print('COMPLETE',label,name,[a[k] for k in ('V','E','F')],a['counts'],a['weak'],h,flush=True)
  a,b=pair;assert a==b and [a[k] for k in ('V','E','F')]==vef and a['counts']==counts and a['weak']==[0,0,0]
  assert a['active_input_indices']==list(range(137));assert all(a[k]==0 for k in ('face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count'))
  mass=centred_mass.run(a);put(folder/'CENTRED_MASS.json',mass)
  atlas=atlas_audit(G,raw,a);put(folder/'CONTACT_ATLAS.json',atlas)
  rec=dict(generator_sha256=gsha,report_sha256=rsha,raw_sha256=rawsha,V=vef[0],E=vef[1],F=vef[2],C=2*vef[1],strict=counts,weak=[0,0,0],mass=mass,atlas={k:v for k,v in atlas.items() if k!='free_indices'})
  if label in ('baseline','endpoint'):
   rec['bits']=bits(raw,a);put(folder/'BITS.json',rec['bits'])
   assert a['stable_face_ids']==[3] and a['unstable_vertices']==([97] if label=='baseline' else [96])
   assert a['raw_vertices'][a['unstable_vertices'][0]]==['0','0','1'] and len(a['faces'][3])==20
   assert len(next(o for o,v in owners(a).items() if v==a['unstable_vertices'][0]))==44
  put(folder/'RECEIPT.json',rec);reports[label]=a;raws[label]=raw;receipts[label]=rec
 before,after=map(owners,(reports['baseline'],reports['endpoint']))
 removed=before.keys()-after.keys();added=after.keys()-before.keys()
 assert removed=={frozenset([87,108,127]),frozenset([87,122,127])} and added=={frozenset([87,108,122,127])}
 assert before[frozenset([16,18,71,94])]==89 and after[frozenset([16,18,71,94])]==88
 assert after[frozenset([87,108,122,127])]==50
 new=reports['endpoint'];assert new['edge_primitive_count']==1252 and new['integration_triangle_count']==352
 incidence=dict(removed=[sorted(o) for o in sorted(removed,key=lambda o:sorted(o))],added=[sorted(o) for o in added],preserved_quad=[16,18,71,94],preserved_quad_lex=88,new_quad_lex=50,degree_histogram=dict(Counter(map(len,after))),facet_histogram=dict(Counter(map(len,new['faces']))),stable_face_cycle=new['faces'][3])
 put(out/'INCIDENCE.json',incidence)
 seed=chart.recover(root=out);assert len(seed['edges'])==314 and seed['outer']==103 and seed['boundary']==[3,130,35]
 h=put(out/'chart_exact.json',check_A.encode(seed));assert h=='14b68b4b81fb2b59c7064e55a0203d4f66f79d31ce42d5e596f5f8a4808a46b1'
 Q0=[tuple(F(v,r[-1]) for v in r[:3]) for r in raws['baseline']['H']];Q=[tuple(F(v,r[-1]) for v in r[:3]) for r in raws['endpoint']['H']]
 p=chart_audit.verify_geometry(Q0,seed,False);assert not p['zero_edges'] and p['positive_interior_count']==311;put(out/'PARENT_STRESS.json',p)
 st=chart_audit.verify_geometry(Q,seed,True);h=put(out/'STRESS.json',st);assert h=='a44f62e158ea5c9fb030460b98acf394381d63a38f61eb54a86e6ebb5e1b83f9'
 assert st['zero_edges']==[242] and st['zero_endpoint_pairs']==[[87,127]] and st['positive_interior_count']==310 and len(st['negative_outer_edges'])==3
 # A transparent refinement of C628 exposes the already suppressed first diagonal.
 # Panel labels here are a new explicit refinement, not invented C630 scheduler identities.
 refined=copy.deepcopy(seed);assert refined['faces'][89]==[94,71,18,16]
 refined['faces'][89]=[94,71,18];refined['faces'].append([94,18,16]);refined['edges']=sorted({tuple(sorted((i,j))) for cy in refined['faces'] for i,j in zip(cy,cy[1:]+cy[:1])})
 for label,qq,cal,want,zeros in [('baseline',Q0,False,'bdb6d46a5043525b4f094d848b5b4d683ad997e339fbe0ca2875fa8ef07c78e7',[[18,94]]),('endpoint',Q,True,'f2006fdcd14d0124a2c473bd917edd759a96c9ee2d7de43f4727d9628241e405',[[18,94],[87,127]])]:
  rr=chart_audit.verify_geometry(qq,refined,cal);assert rr['zero_endpoint_pairs']==zeros;assert put(out/label/'REFINED_STRESS.json',rr)==want
 dualedges=set()
 for i,j in new['edges']:
  f=[k for k,cy in enumerate(new['faces']) if i in cy and j in cy];assert len(f)==2;dualedges.add(tuple(f))
 assert dualedges==set(map(tuple,seed['edges']))-{(87,127)};conn=connectivity(137,dualedges);assert conn==9454
 controls=[]
 for H,c,w in [([[-1,-1,-1,1],[-1,1,1,1],[1,-1,1,1],[1,1,-1,1]],[4,4,6],[0,0,0]),([[1,0,0,1],[-2,3,0,1],[1,-3,0,1],[0,0,1,1],[0,0,-1,1]],[4,4,6],[1,2,3])]:
  a,b=check_A.run({'H':H}),check_B.run({'H':H});assert a==b and a['counts']==c and a['weak']==w;controls.append(dict(strict=c,weak=w))
 for H in ([[1,0,0,-1]]*4,[[1,0,0,1]]*4,[[1,0,0,1],[-1,0,0,1],[0,1,0,1],[0,-1,0,1]]):
  for fun in (check_A.run,check_B.run):
   try:fun({'H':H})
   except (AssertionError,ValueError):pass
   else:raise AssertionError('Malformed/unbounded control accepted')
 put(out/'CONTROLS.json',controls)
 assert receipts['endpoint']['atlas']['free_coordinates']==316
 receipt=dict(status='VQ20_C626_TWO_EXACT_AUDITS_COLD_SOURCE_ONLY_PASS',body=NAME,V=178,E=313,F=137,C=626,strict=[1,1,0],weak=[0,0,0],stable_input=3,unstable_raw_lex=96,zero_refinement_edges=[[18,94],[87,127]],positive_interior_stresses=310,negative_outer_stresses=3,three_connectivity_cases=conn,source_receipts=receipts,stress_sha256=sha((out/'STRESS.json').read_bytes()),exact_maxwell_and_inverse_roundtrips=True)
 put(out/'RECEIPT.json',receipt);print(receipt['status'],sha((out/'RECEIPT.json').read_bytes()),flush=True)
if __name__=='__main__':main()
