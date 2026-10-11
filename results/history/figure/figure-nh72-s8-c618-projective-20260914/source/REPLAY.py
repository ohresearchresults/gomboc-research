"""Source-only replay of S8's two deleted bodies and two new rational physical images.
No saved vertices, centroid, incidence or audit result is an input.
Usage: python -B -S REPLAY.py --out ABSENT_DIRECTORY [--case NAME]
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib,sys,subprocess,concurrent.futures
assert __debug__
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent
from endpoint import build,dump,inverse,mv,dot
import check_A,check_B,centred_mass,details,pullback_identity

def meta(data):return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
def sources():
 manifest=json.loads((R/'MANIFEST.json').read_text())
 for name,value in manifest.items():assert meta((R/name).read_bytes())==value,name
 return len(manifest)+1

def validate(a,name):
 p=json.loads((R/'PARAMETERS.json').read_text())[name]
 assert [a[k] for k in ('V','E','F')]==p['expected_VEF']
 assert a['counts']==p['expected_counts'] and a['weak']==[0,0,0]
 assert a['active_input_indices']==list(range(136))
 assert a['centred_first_moments']==a['centred_centroid']==[0,0,0]
 assert a['edge_primitive_count']==1236 and a['integration_triangle_count']==346
 assert all(a[k]==0 for k in ['face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count'])
 assert a['counts']!=[1,1,0], 'Update the expected object and independent winner gates explicitly'

def one(name,out):
 sources();build(name,out);raw=json.loads((out/'raw.json').read_text())
 a=check_A.run(raw);validate(a,name);dump(out/'A.json',a);print('COMPLETE_EXACT_A',name,flush=True)
 b=check_B.run(raw);validate(b,name);dump(out/'B.json',b);assert (out/'A.json').read_bytes()==(out/'B.json').read_bytes();print('COMPLETE_EXACT_B',name,flush=True)
 dump(out/'CENTRED_MASS.json',centred_mass.run(a));details.run(out);pullback_identity.run(out)
 expected=json.loads((R/'EXPECTED.json').read_text())[name]
 for file,value in expected.items():assert meta((out/file).read_bytes())==value,(name,file)
 print('ONE_FINITE_OWN_CENTROID_NONWINNER_COLD_PASS',name,flush=True)

def fixtures():
 cases=[('tetra',[[-1,-1,-1,1],[-1,1,1,1],[1,-1,1,1],[1,1,-1,1]],[4,4,6],[0,0,0]),('weak_prism',[[1,0,0,1],[-2,3,0,1],[1,-3,0,1],[0,0,1,1],[0,0,-1,1]],[4,4,6],[1,2,3])]
 result=[]
 for name,H,c,w in cases:
  a=check_A.run({'H':H});b=check_B.run({'H':H});assert a==b and a['counts']==c and a['weak']==w
  assert not(c==[1,1,0] and w==[0,0,0]);result.append(dict(name=name,counts=c,weak=w,winner_rejected=True))
 tetra=cases[0][1]
 for bad in [tetra+tetra[:1],[row[:] if i else row[:3]+[0] for i,row in enumerate(tetra)]]:
  for implementation in (check_A,check_B):
   try:implementation.run({'H':bad})
   except (AssertionError,ValueError):pass
   else:raise AssertionError('Malformed input was accepted')
 return result

def compare(base,changed):
 a=json.loads((base/'A.json').read_text());b=json.loads((changed/'A.json').read_text());d=json.loads((changed/'DETAILS.json').read_text());p=json.loads((changed/'INPUT.json').read_text());D=p['D'];t=tuple(F(x,D) for x in p['t']);A=[[F(x,D) for x in row] for row in p['A']];Ai=inverse(A);mapping=d['base_vertex_of_new']
 for i,row in enumerate(b['raw_vertices']):
  y=mv(Ai,tuple(map(F,row)));den=1-dot(t,y);assert den>0
  assert tuple(x/den for x in y)==tuple(map(F,a['raw_vertices'][mapping[i]]))
 assert {tuple(sorted(mapping[i] for i in e)) for e in b['edges']}==set(map(tuple,a['edges']))
 def cy(c):
  k=c.index(min(c));return c[k:]+c[:k]
 assert [cy([mapping[i] for i in c]) for c in b['faces']]==[cy(c) for c in a['faces']]
 return dict(parent_vertices=len(mapping),all_raw_vertices_inverted=True,all_maximal_cycles_equal_under_map=True,all_true_edges_equal_under_map=True)

def main():
 p=argparse.ArgumentParser();p.add_argument('--out',required=True,type=Path);p.add_argument('--case',choices=['DEL99','DEL117','P4_DEL99','P4_DEL117']);args=p.parse_args()
 if args.case:one(args.case,args.out);return
 n=sources();args.out.mkdir(parents=True,exist_ok=False);names=['DEL99','DEL117','P4_DEL99','P4_DEL117']
 def job(name):
  with (args.out/(name+'.log')).open('w') as log:
   subprocess.run([sys.executable,'-B','-S',str(R/'REPLAY.py'),'--out',str(args.out/name),'--case',name],stdout=log,stderr=subprocess.STDOUT,check=True)
 with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:list(pool.map(job,names))
 comp={str(k):compare(args.out/('DEL'+str(k)),args.out/('P4_DEL'+str(k))) for k in [99,117]}
 receipt=dict(status='NH72_S8_C618_FOUR_NONWINNERS_SOURCE_ONLY_COLD_PASS',source_files=n,cases={name:json.loads((R/'EXPECTED.json').read_text())[name] for name in names},complete_independent_A_B_identical=True,third_filled_mass=True,finite_projective_denominators=True,label_and_incidence_comparisons=comp,fixtures=fixtures())
 sources();dump(args.out/'RECEIPT.json',receipt);print(receipt['status'],flush=True)
if __name__=='__main__':main()
