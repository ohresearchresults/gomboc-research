"""Independent centred integer mass, complete label maps, and arithmetic costs."""
import sys,json,math
from pathlib import Path
from fractions import Fraction as Q
import BUILD
sys.set_int_max_str_digits(0)
def bits(seq):
 vals=list(map(Q,seq));return [max(abs(v.numerator).bit_length() for v in vals),max(v.denominator.bit_length() for v in vals)]
def third_mass(a):
 P=[tuple(map(Q,p)) for p in a['raw_vertices']];g=tuple(map(Q,a['raw_centroid']));D=math.lcm(*(v.denominator for p in P for v in p),*(v.denominator for v in g));X=[tuple(int((p[k]-g[k])*D) for k in range(3)) for p in P];V6=0;M24=(0,0,0);triangles=0
 for cy in a['faces']:
  cy=cy[2:]+cy[:2]
  for j in range(1,len(cy)-1):
   x,y,z=[X[i] for i in (cy[0],cy[j],cy[j+1])];w=BUILD.det(x,y,z);assert w>0;V6+=w;M24=BUILD.add(M24,BUILD.mul(w,BUILD.add(BUILD.add(x,y),z)));triangles+=1
 assert M24==(0,0,0) and Q(V6,6*D**3)==Q(a['ordinary_volume'])
 return dict(status='THIRD_CENTRED_INTEGER_FILLED_MASS_PASS',tetrahedra=triangles,centred_first_moments=[0,0,0],common_denominator_bits=D.bit_length())
def run(base,case,param,a,rootproof):
 eta=[Q(v,1<<param['centre_bits']) for v in param['eta_numerators']];P,keep,faces,labels,ds=BUILD.points(base,case,eta);X=[tuple(map(Q,p)) for p in a['raw_vertices']];lookup={p:i for i,p in enumerate(X)};old_to_new={i:lookup[P[i]] for i in keep};new_to_old={j:i for i,j in old_to_new.items()};assert len(lookup)==len(keep)
 def canonical(cy):
  k=cy.index(min(cy));return cy[k:]+cy[:k]
 for f,cy in enumerate(faces):assert canonical([old_to_new[i] for i in cy])==a['faces'][f]
 expected_edges={tuple(sorted((i,j))) for cy in faces for i,j in zip(cy,cy[1:]+cy[:1])};actual_edges={tuple(sorted((new_to_old[i],new_to_old[j]))) for i,j in a['edges']};assert expected_edges==actual_edges
 assert a['active_input_indices']==list(range(len(faces)))
 U=sorted(new_to_old[i] for i in a['unstable_vertices']);H=sorted(sorted(new_to_old[i] for i in e) for e in a['saddle_edges']);S=a['stable_face_ids'];assert a['counts']==rootproof['counts'] and a['weak']==rootproof['weak'];assert U==rootproof['unstable_vertices'] and H==rootproof['saddle_edges'] and S==rootproof['stable_faces']
 g0=tuple(map(Q,base['raw_centroid']));g=tuple(map(Q,a['raw_centroid']));error=max(abs(x-y) for x,y in zip(g,g0));assert error<Q(1,10**35)
 P0,_,_,_,_=BUILD.points(base,case,[Q(0)]*3);V0,M0=BUILD.mass(P0,faces);gcore=BUILD.mul(1/V0,M0);mass_defect=BUILD.sub(M0,BUILD.mul(V0,g0));assert any(mass_defect)
 maxmove2=max(BUILD.dot(BUILD.sub(P[i],P0[i]),BUILD.sub(P[i],P0[i])) for i in keep)
 desc=dict(primitive_support_bits=max(abs(v).bit_length() for n,h in zip(a['normals'],a['offsets']) for v in (*n,h)),raw_vertex_fraction_bits=bits(v for p in X for v in p),volume_fraction_bits=bits([a['ordinary_volume']]),first_moment_fraction_bits=bits(a['raw_first_moments']),raw_centroid_fraction_bits=bits(g),centred_vertex_fraction_bits=bits(p[k]-g[k] for p in X for k in range(3)))
 return dict(status='EXACT_RATIONAL_PROXY_LABELS_COMPLEX_MASS_AND_ROOT_COMPARISON_PASS',case=case,V=a['V'],E=a['E'],F=a['F'],counts=a['counts'],weak=a['weak'],support_labels=labels,old_to_new=old_to_new,new_to_old=new_to_old,stable_support_labels=[labels[f] for f in S],original_unstable_vertices=U,original_saddle_edges=H,raw_volume=a['ordinary_volume'],raw_first_moments=a['raw_first_moments'],raw_centroid=a['raw_centroid'],target_centroid=base['raw_centroid'],centroid_error_infinity=str(error),uncompensated_volume=str(V0),uncompensated_first_moments=list(map(str,M0)),uncompensated_centroid=list(map(str,gcore)),uncompensated_moment_defect=list(map(str,mass_defect)),max_cap_displacement_squared=str(maxmove2),arithmetic=desc,third_mass=third_mass(a),algebraic_status='The unique parameter root is separately proved by interval Krawczyk and full interval geometry/mechanics; this file independently audits the rational parameter-box centre, not an allegedly rational algebraic root.')
