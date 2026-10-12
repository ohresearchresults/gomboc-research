"""Full exact label/complex readback, independent centred integer integration,
arithmetic statistics and actual-edge basin census for the new rational body."""
import sys,json,math
from fractions import Fraction as Q
from pathlib import Path
import BUILD as B,CRITICAL,ENERGY_CERT
sys.set_int_max_str_digits(0)
def bits(seq):
 seq=list(map(Q,seq));return [max(abs(v.numerator).bit_length() for v in seq),max(v.denominator.bit_length() for v in seq)]
def canonical(cy):
 k=cy.index(min(cy));return cy[k:]+cy[:k]
def reach(graph,root):
 seen={root}
 while True:
  new=seen|{i for i,a in enumerate(graph) if set(a)&seen}
  if new==seen:return seen
  seen=new

def run(base,parameters,a):
 P,keep,faces,labels=CRITICAL.points(base,parameters);X=[tuple(map(Q,p)) for p in a['raw_vertices']];lookup={p:i for i,p in enumerate(X)}
 oldnew={i:lookup[P[i]] for i in keep};newold={v:k for k,v in oldnew.items()};assert len(oldnew)==len(X)==173
 for f,cy in enumerate(faces):assert canonical([oldnew[i] for i in cy])==a['faces'][f]
 E={tuple(sorted((i,j))) for cy in faces for i,j in zip(cy,cy[1:]+cy[:1])};EE={tuple(sorted((newold[i],newold[j]))) for i,j in a['edges']};assert E==EE
 assert (a['V'],a['E'],a['F'],a['counts'],a['weak'])==(173,309,138,[4,6,8],[0,0,0]);assert a['active_input_indices']==list(range(138))
 assert a['face_primitive_zero_count']==a['vertex_max_zero_count']==a['edge_primitive_zero_count']==0
 V=Q(a['ordinary_volume']);M=tuple(map(Q,a['raw_first_moments']));g=tuple(map(Q,a['raw_centroid']));g0=tuple(map(Q,base['raw_centroid']));assert M==B.mul(V,g)
 error=max(abs(x-y) for x,y in zip(g,g0));assert error<Q(1,10**12)
 D=math.lcm(*(v.denominator for p in X for v in p),*(v.denominator for v in g));Z=[tuple(int((p[k]-g[k])*D) for k in range(3)) for p in X]
 volume6=0;first24=(0,0,0);tri=0
 for cy in a['faces']:
  cy=cy[2:]+cy[:2]
  for k in range(1,len(cy)-1):
   x,y,z=(Z[i] for i in (cy[0],cy[k],cy[k+1]));w=B.det(x,y,z);assert w>0;volume6+=w;first24=B.add(first24,B.mul(w,B.add(B.add(x,y),z)));tri+=1
 assert first24==(0,0,0) and Q(volume6,6*D**3)==V
 graph=[[] for p in X]
 for i,j in a['edges']:
  e=B.sub(Z[j],Z[i])
  if B.dot(Z[i],e)>0:graph[i].append(j)
  if B.dot(Z[j],e)<0:graph[j].append(i)
 root=max(range(len(X)),key=lambda i:B.dot(Z[i],Z[i]));R=reach(graph,root);bad=set(range(len(X)))-R
 assert all(set(graph[i])<=bad for i in bad)
 C=math.lcm(*(v.denominator for v in g));cg=tuple(int(C*v) for v in g)
 N=a['normals'];H=[int(h)*C-B.dot(n,cg) for n,h in zip(N,a['offsets'])];assert min(H)>0
 edgefaces={}
 for f,cy in enumerate(a['faces']):
  for i,j in zip(cy,cy[1:]+cy[:1]):edgefaces.setdefault(tuple(sorted((i,j))),[]).append(f)
 polar=[[] for n in N];de=[]
 for fs in edgefaces.values():
  i,j=fs;de.append((i,j));prod=B.dot(N[i],N[j])
  if H[i]*prod>H[j]*B.dot(N[i],N[i]):polar[i].append(j)
  if H[j]*prod>H[i]*B.dot(N[j],N[j]):polar[j].append(i)
 proot=max(range(len(N)),key=lambda i:Q(B.dot(N[i],N[i]),H[i]**2));PR=reach(polar,proot);pbad=set(range(len(N)))-PR
 raw,_=CRITICAL.build(base,parameters);oldraw,_=B.raw(base,'PAIR99',[Q(0)]*3)
 changed=[labels[i] for i,(x,y) in enumerate(zip(oldraw['H'],raw['H'])) if x!=y]
 assert changed==[44,72,73,81,100,'PAIR99_CUT_0','PAIR99_CUT_1']
 for label in [0,2,35]:assert raw['H'][labels.index(label)]==oldraw['H'][labels.index(label)]
 oldeta=[Q(v,1<<120) for v in [-333412176052727923408714378468258183,32223247221739879834538304508376034,11398562434443787228821663143046664]]
 oldP,_,_,_,_=B.points(base,'PAIR99',oldeta);oldcapsraw,_=B.raw(base,'PAIR99',oldeta)
 vsR120=[i for i in keep if P[i]!=oldP[i]];assert len(vsR120)==23
 capids=sorted(i for cap in B.CASES['PAIR99']['caps'] for i in cap['vertices']);assert len(capids)==13
 vsR120supports=[labels[i] for i,(x,y) in enumerate(zip(oldcapsraw['H'],raw['H'])) if x!=y]
 PP=[tuple(map(Q,p)) for p in base['raw_vertices']];maxmove=max(B.dot(B.sub(P[i],PP[i]),B.sub(P[i],PP[i])) for i in keep)
 rho=Q(ENERGY_CERT.run(base)['Euclidean_centre_radius']);assert error<rho
 U=sorted(newold[i] for i in a['unstable_vertices']);S=[labels[f] for f in a['stable_face_ids']];HH=sorted(sorted(newold[i] for i in e) for e in a['saddle_edges'])
 return dict(status='NEW_CRITICAL_DISK_FULL_READBACK_AND_THIRD_MASS_PASS',identity=parameters['identity'],V=a['V'],E=a['E'],F=a['F'],counts=a['counts'],weak=a['weak'],
  original_vertex_ids=keep,old_to_new=oldnew,new_to_old=newold,support_labels=labels,changed_support_labels=changed,changed_vertices=CRITICAL.CHANGED,changed_vertices_vs_parent_R120=vsR120,restored_cap_vertices=capids,changed_support_labels_vs_parent_R120=vsR120supports,
  stable_original_labels=S,unstable_original_vertices=U,saddle_original_edges=HH,
  ordinary_volume=str(V),raw_first_moments=list(map(str,M)),raw_centroid=list(map(str,g)),target_centroid=list(map(str,g0)),centroid_error_infinity=str(error),
  centred_first_moments=[0,0,0],tetrahedra=tri,max_vertex_displacement_squared=str(maxmove),
  primal_root=newold[root],primal_root_reaching=sorted(newold[i] for i in R),primal_closed_unwanted=sorted(newold[i] for i in bad),primal_boundary=[sorted((newold[i],newold[j])) for i,j in a['edges'] if (i in bad)!=(j in bad)],
  polar_root=labels[proot],polar_closed_unwanted=[labels[i] for i in sorted(pbad)],polar_boundary=[[labels[i],labels[j]] for i,j in de if (i in pbad)!=(j in pbad)],
  arithmetic=dict(support_bits=max(abs(v).bit_length() for r in raw['H'] for v in r),raw_vertices=bits(v for p in X for v in p),volume=bits([V]),moments=bits(M),centroid=bits(g),centred_vertices=bits(p[k]-g[k] for p in X for k in range(3)),common_centred_denominator_bits=D.bit_length()))
if __name__=='__main__':
 base=json.loads(Path(sys.argv[1]).read_text());param=json.loads(Path(sys.argv[2]).read_text());a=json.loads(Path(sys.argv[3]).read_text());r=run(base,param,a);Path(sys.argv[4]).write_text(json.dumps(r,sort_keys=True,separators=(',',':')))
 print(r['status'],r['counts'],r['stable_original_labels'],r['unstable_original_vertices']);print(r['arithmetic']);print('volume',float(Q(r['ordinary_volume'])),'g',list(map(lambda s:float(Q(s)),r['raw_centroid'])),'centre_error',float(Q(r['centroid_error_infinity'])),'maxmove',float(Q(r['max_vertex_displacement_squared']))**.5);print('basins',len(r['primal_closed_unwanted']),len(r['primal_boundary']),len(r['polar_closed_unwanted']),len(r['polar_boundary']))
