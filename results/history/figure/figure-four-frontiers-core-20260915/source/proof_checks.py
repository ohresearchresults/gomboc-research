"""Pure-rational, source-replayable certificates on the recovered maximal complex.
Four escape halfspaces are inconsistent for the stated frozen geometry only.
The proof does not quantify over geometries or over other witness selections.
"""
import json,sys
from fractions import Fraction as Q
from RECONSTRUCT import solve
from check_A import dot,cross,sub,mul
sys.set_int_max_str_digits(0)

def owner_map(a,deleted):
 keep=[i for i in range(137) if i not in deleted];owners=[[] for _ in range(a['V'])]
 for f,cy in enumerate(a['faces']):
  oi=keep[a['active_input_indices'][f]]
  for v in cy:owners[v].append(oi)
 return {tuple(sorted(o)):v for v,o in enumerate(owners)},keep

def run(a,deleted,spec):
 idx,keep=owner_map(a,deleted);X=[tuple(map(Q,row)) for row in a['raw_vertices']];N=[tuple(map(Q,row)) for row in a['normals']];face={keep[k]:f for f,k in enumerate(a['active_input_indices'])};rows=[];resolved=[]
 for r in spec:
  i=idx[tuple(r['from'])];j=idx[tuple(r['to'])];d=sub(X[j],X[i])
  if r['kind']=='vertex':A=mul(-1,d);b=-dot(X[i],d);lab=['vertex',i,j]
  else:
   f=face[r['support']];assert any(u==i and v==j for u,v in zip(a['faces'][f],a['faces'][f][1:]+a['faces'][f][:1]));n=N[f];A=cross(d,n);b=dot(n,cross(X[i],d));lab=['face',f,i,j]
  rows.append((A,b));resolved.append(lab)
 assert len(rows)==4
 y=solve([[r[0][k] for r in rows] for k in range(3)]+[[Q(1)]*4],[Q(0)]*3+[Q(1)])
 assert all(v>0 for v in y)
 assert all(sum(y[i]*rows[i][0][k] for i in range(4))==0 for k in range(3))
 rhs=sum(y[i]*rows[i][1] for i in range(4));assert rhs>0
 return dict(status='EXACT_FROZEN_FOUR_WITNESS_FARKAS_PASS',rows=resolved,positive_weights=[str(v) for v in y],positive_rhs=str(rhs),rhs_decimal=float(rhs),scope='Only the stated frozen body and four specified escape inequalities; not a contact-chart or equilibrium-class exclusion.')

def preserved_pair(a,deleted):
 idx,keep=owner_map(a,deleted);u=idx[(44,81,100)];v=idx[(80,81,100)];X=[tuple(map(Q,row)) for row in a['raw_vertices']];g=tuple(map(Q,a['raw_centroid']));p=dot(sub(X[u],g),sub(X[v],X[u]));assert p>0
 return dict(status='EXACT_OLD_146_ESCAPE_PRESERVED',original_source_owners=[44,81,100],original_target_owners=[80,81,100],vertices=[u,v],escape=str(p),escape_decimal=float(p))
