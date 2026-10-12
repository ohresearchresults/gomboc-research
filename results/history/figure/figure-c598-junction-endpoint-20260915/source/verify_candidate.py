"""Exact convex-hull identity, complete reference census, and exposed-chain verification.
Python standard library only. All reference centres are distinguished from own mass.
"""
import json,sys,hashlib
from pathlib import Path
from fractions import Fraction as Q
from math import gcd,lcm
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(a,s):return tuple(x*s for x in a)
def sign(x):return (x>0)-(x<0)
def blob(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def fracrow(r):return tuple(map(Q,r))
def integral(r):
 d=lcm(*(x.denominator for x in r));return tuple(int(x*d) for x in r),d

def census(a,centre):
 X=list(map(fracrow,a['raw_vertices']));N=[tuple(n) for n in a['normals']];F=a['faces'];E=a['edges'];C=lcm(*(x.denominator for x in centre));M=tuple(int(x*C) for x in centre)
 pairs=[integral(p) for p in X];aa=[x for x,b in pairs];bs=[b for x,b in pairs];z=[sub(mul(x,C),mul(M,b)) for x,b in pairs]
 def ed(i,j):return sub(mul(aa[j],bs[i]),mul(aa[i],bs[j]))
 assert all(h*C>dot(n,M) for n,h in zip(N,a['offsets']))
 SF=[];SW=[];UV=[];UW=[];EH=[];EW=[];fs=[];vs=[];es=[];ef={tuple(e):[] for e in E}
 for fi,cy in enumerate(F):
  sg=[sign(dot(N[fi],cross(z[i],ed(i,j)))) for i,j in zip(cy,cy[1:]+cy[:1])];fs.append(sg)
  if min(sg)>0:SF.append(fi)
  elif min(sg)>=0:SW.append(fi)
  for i,j in zip(cy,cy[1:]+cy[:1]):ef[tuple(sorted((i,j)))].append(fi)
 for i in range(len(X)):
  # Positive denominators may be dropped for the maximal sign, not magnitude.
  sg=max(sign(dot(z[i],ed(i,j))) for j in range(len(X)) if j!=i);vs.append(sg)
  if sg<0:UV.append(i)
  elif sg==0:UW.append(i)
 for i,j in E:
  e=ed(i,j);ee=dot(e,e);ze=dot(z[i],e);p=sub(mul(z[i],ee),mul(e,ze));n,m=[N[k] for k in ef[(i,j)]];d=cross(n,m);assert dot(d,d)>0
  vals=[-ze*bs[j],C*ee+ze*bs[j],dot(cross(p,m),d),dot(cross(n,p),d)];sg=list(map(sign,vals));es.append([i,j,*sg])
  if min(sg)>0:EH.append([i,j])
  elif min(sg)>=0:EW.append([i,j])
 out=dict(centre=[str(x) for x in centre],counts=[len(SF),len(UV),len(EH)],weak=[len(SW),len(UW),len(EW)],stable_face_ids=SF,unstable_vertices=UV,saddle_edges=EH,weak_faces=SW,weak_vertices=UW,weak_edges=EW,face_signs=fs,vertex_max_signs=vs,edge_signs=es)
 assert sum(out['weak']) or len(SF)+len(UV)-len(EH)==2
 return out

def run(root,parent,core):
 root=Path(root);parent=Path(parent);core=Path(core);sys.path.insert(0,str(core));import centred_mass
 a=json.loads((root/'A.json').read_text());b=(root/'B.json').read_bytes();assert (root/'A.json').read_bytes()==b
 par=json.loads(parent.read_text());cfg=json.loads((root/'SELECTORS.json').read_text());assert hashlib.sha256(parent.read_bytes()).hexdigest()==cfg['parent_audit_sha256']
 P=list(map(fracrow,par['raw_vertices']))+[tuple(Q(v,cfg['grid']) for v in r) for r in cfg['new_raw_points']];X=list(map(fracrow,a['raw_vertices']));assert len(set(P))==len(P)
 H=json.loads((root/'raw.json').read_text())['H'];assert all(dot(n[:3],p)<=n[3] for n in H for p in P);assert set(X)<=set(P)
 # A and B established bounded full-dimensional intersection H. Its vertices
 # are all input points; all input points satisfy H: both inclusions hold.
 label={p:i for i,p in enumerate(P)};input_labels=[label[x] for x in X];index={p:i for i,p in enumerate(X)};hidden=[i for i,p in enumerate(P) if p not in index]
 assert [a[k] for k in ('V','E','F')]==[164,299,137] and a['counts']==[19,27,44] and a['weak']==[0,0,0]
 assert hidden==[0,1,2,3,4,5,6,8]
 own=census(a,fracrow(a['raw_centroid']));assert all(own[k]==a[k] for k in ['counts','weak','stable_face_ids','unstable_vertices','saddle_edges','face_signs','edge_signs'])
 refcentre=fracrow(par['raw_centroid']);ref=census(a,refcentre);ref['reference']='actual filled-volume centroid of the unchanged C602 parent, NOT child own centroid'
 assert ref['counts']==[3,1,2] and ref['weak']==[0,0,0]
 for r in [own,ref]:r['unstable_input_labels']=[input_labels[k] for k in r['unstable_vertices']]
 chain=[7,167,168,169,170,171,85];edges={tuple(e) for e in a['edges']};links=[]
 for i,j in zip(chain,chain[1:]):
  v,w=index[P[i]],index[P[j]];assert tuple(sorted((v,w))) in edges
  val=dot(sub(P[i],refcentre),sub(P[j],P[i]));assert val>0
  links.append({'input_edge':[i,j],'raw_lex_edge':[v,w],'reference_ascent':str(val)})
 assert tuple(sorted((index[P[171]],index[P[91]]))) not in edges
 assert tuple(sorted((index[P[91]],index[P[85]]))) in edges
 mass=centred_mass.run(a)
 for name,data in [('OWN_CENSUS.json',own),('REFERENCE_CENSUS.json',ref),('MASS.json',mass),('CHAIN.json',links)]: (root/name).write_bytes(blob(data))
 meta={'status':'TO91_CHAIN6_C598_EXACT_NONWINNER_PASS','V_E_F':[a[k] for k in ('V','E','F')],'C':2*a['E'],'own_counts':a['counts'],'own_weak':a['weak'],'reference_counts':ref['counts'],'reference_weak':ref['weak'],'reference_U_input_labels':ref['unstable_input_labels'],'own_U_input_labels':own['unstable_input_labels'],'raw_lex_to_input_label':input_labels,'hidden_parent_vertices':hidden,'true_exposed_chain':chain,'sampling_target':91,'nominal_171_to_91_is_true_edge':False,'retained_old_91_to_85_is_true_edge':True,'centred_denominator_bits':mass['common_centred_denominator_bits'],'parent_audit_sha256':cfg['parent_audit_sha256'],'child_audit_sha256':hashlib.sha256(b).hexdigest(),'raw_sha256':hashlib.sha256((root/'raw.json').read_bytes()).hexdigest()}
 (root/'RECEIPT.json').write_bytes(blob(meta));print(json.dumps(meta,sort_keys=True),flush=True)
if __name__=='__main__':run(*sys.argv[1:])
