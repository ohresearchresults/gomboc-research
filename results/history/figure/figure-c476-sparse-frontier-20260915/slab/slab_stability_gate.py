"""Exact central-section/slab certificate forcing at least two stable equilibria.
Usage python -B -S slab_stability_gate.py C476_A C476_RAW OUT
Inputs are the uniform-filled own-centroid C476 affine/deletion body.
General theorem and finite proof are in SLAB_GATE_PROOF.md.
"""
import hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
assert __debug__;sys.set_int_max_str_digits(0)
A_SHA='1634d2baf53c7fa532e1b488c30466160bcacbe7a95b8b840a41f3e1efee9f74'
RAW_SHA='048a888c4ad0c69aaa160f086d3d46bfbd1999fe4649a6a91cb3eefcb205b7c0'
N=(19,-98,-8);R=F(1,3);HEIGHT=F(1,12)
B=lambda o:json.dumps(o,sort_keys=True,separators=(',',':')).encode()
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
def main(ap,rp,out):
 ab=ap.read_bytes();rb=rp.read_bytes();assert hashlib.sha256(ab).hexdigest()==A_SHA and hashlib.sha256(rb).hexdigest()==RAW_SHA
 a=json.loads(ab);raw=json.loads(rb)['H'];P=[tuple(F(x) for x in v)for v in a['raw_vertices']];c=tuple(F(x)for x in a['raw_centroid']);Q=[tuple(F(x)for x in row)for row in raw]
 assert (a['V'],a['E'],a['F'],a['counts'],a['weak'])==(115,238,125,[2,2,2],[0,0,0])
 nn=dot(N,N);vertex_margins=[];plane_margins=[]
 for p in P:
  x=tuple(t-u for t,u in zip(p,c));m=HEIGHT*HEIGHT*nn-dot(N,x)**2;assert m>0;vertex_margins.append(m)
 for row in Q:
  n=row[:3];h=row[3]-dot(n,c);assert h>0
  proj2=nn*dot(n,n)-dot(N,n)**2;assert proj2>=0
  m=nn*h*h-R*R*proj2;assert m>0;plane_margins.append(m/(nn*h*h))
 assert R>HEIGHT>0 and len(P)==115 and len(Q)==125
 # A convenient rationally smaller observed margin certificate avoids printing enormous moments.
 assert min(vertex_margins)>F(34) and min(plane_margins)>F(24,100)
 rec=dict(status='EXACT_C476_CENTRAL_SECTION_SLAB_TWO_STABLE_CERTIFICATE',source_A_sha256=A_SHA,source_raw_sha256=RAW_SHA,normal=list(N),normal_squared=nn,section_disk_radius=str(R),slab_half_height=str(HEIGHT),section_to_slab_ratio=str(R/HEIGHT),tested_vertices=len(P),tested_maximal_supports=len(Q),all_vertex_slab_inequalities_strict=True,all_plane_disk_inequalities_strict=True,vertex_squared_margin_lower_bound='34',relative_plane_squared_margin_lower_bound='6/25',conclusion='Every convex polytope with these two geometric inclusions about the chosen centre has at least two strict stable facet equilibria; C476 satisfies both inclusions about its exact own filled-volume centroid.',scope='Geometric sufficient obstruction, not a global edge-complexity lower bound.')
 out.write_bytes(B(rec));print('EXACT_C476_SLAB_FORCES_TWO_STABLE_PASS',hashlib.sha256(out.read_bytes()).hexdigest())
if __name__=='__main__':main(*map(Path,sys.argv[1:]))
