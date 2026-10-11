"""Exact minimum insertion count for free ascent returning to an unchanged old vertex.
The centre and old vertex positions are frozen. This is not a changed-mass exclusion.
Requires the completely journaled FOUR_FRONTIERS_EXACT_CORE_20260915.
Usage: python -B -S endpoint_domination.py CORE PARENT_AUDIT OUTPUT
"""
import hashlib,json,sys
from pathlib import Path
from fractions import Fraction as Q
from math import lcm
sys.set_int_max_str_digits(0)
blob=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def run(core,parent):
 core,parent=Path(core),Path(parent)
 for name,r in json.loads((core/'CORE_MANIFEST.json').read_text()).items():
  b=(core/name).read_bytes();assert len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256']
 pb=parent.read_bytes();assert hashlib.sha256(pb).hexdigest()=='2426da394eda9520bd30b2b8b3e1f00d043697353bb6bc73658f5983653c11ec'
 a=json.loads(pb);P=[tuple(map(Q,p))for p in a['raw_vertices']];g=tuple(map(Q,a['raw_centroid']));D=lcm(*(x.denominator for p in P+[g]for x in p));X=[tuple(int(x*D)-int(c*D) for x,c in zip(p,g))for p in P]
 def dot(u,v):return sum(x*y for x,y in zip(u,v))
 u=X[7];A=dot(u,u);B=[dot(v,v)for v in X];C=[dot(u,v)for v in X];targets=[j for j,b in enumerate(B)if b>A]
 assert targets==[85,91,145,147,150]
 assert all(C[j]<0 and C[j]*C[j]<A*B[j]for j in targets)
 assert all(B[85]>B[j]for j in targets if j!=85)
 # Both cosines are negative. Squaring therefore reverses the comparison
 # of their absolute values: this proves cos(phi85)>cos(phij).
 assert all(C[85]*C[85]*B[j]<C[j]*C[j]*B[85]for j in targets if j!=85)
 sys.path.insert(0,str(core));import fixed_chain
 bound=fixed_chain.run(a)
 rows=[]
 for j in targets:
  rows.append({'target':j,'squared_norm_gain_relative_floor_1e12':(B[j]-A)*10**12//A,'negative_cosine':True,'apex_strictly_longer_and_smaller_angle':j!=85})
 ints=blob({'D':str(D),'X':[[str(v)for v in x]for x in X]})
 return {'status':'C602_ALL_OLD_ENDPOINTS_MINIMUM_FIVE_LINKS_PASS','parent_audit_sha256':hashlib.sha256(pb).hexdigest(),'source':7,'dominant_target':85,'eligible_old_targets':targets,'targets':rows,'all_other_old_vertices_have_radius_at_most_source':True,'minimum_free_links_to_any_old_target':5,'minimum_new_intermediate_vertices_before_first_old_target':4,'fixed_pair_certificate':bound,'exact_common_integer_input_sha256':hashlib.sha256(ints).hexdigest(),'scope':'Exact unchanged C602 vertices and its own filled centroid, both frozen. A strictly radial-ascending chain from old7 first rejoining a distinct unchanged old vertex needs at least five links and four new intermediate vertices. No changed supporting geometry, affine metric, added-material centroid, or global complexity bound is excluded.'}
if __name__=='__main__':
 z=run(sys.argv[1],sys.argv[2]);Path(sys.argv[3]).write_bytes(blob(z));print(z['status'],z['eligible_old_targets'],flush=True)
