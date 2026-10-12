"""Exact free 12-link ascent witness for K99; deliberately NOT a polyhedron.
Input: NH72_CRITICAL_DISK_AND_ENERGY_BARRIER source-only replay BASE/B.json.
The complete 28-source parent recovery capsule is in the canonical journal.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json, sys
assert __debug__
sys.set_int_max_str_digits(0)
LAM=[10000000000,10124705851,10230078287,10314152143,10375296564,
     10412301146,10424442999,10411527617,10373899039,10312418220,
     10228412155,10123599427,10000000000]
GRID=10**12

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def interval(x):
    n=x.numerator*GRID//x.denominator
    return [n,n+1]
def run(path):
    b=Path(path).read_bytes()
    assert len(b)==246114 and sha256(b).hexdigest()=='ae904b54ebc2b09cc034d913b48ae37b7877dc709b521abfc9ff5baca93bcc88'
    a=json.loads(b)
    assert [a[k] for k in ['V','E','F','counts','weak']]==[175,309,136,[1,2,1],[0,0,0]]
    P=[tuple(map(F,p)) for p in a['raw_vertices']];c=tuple(map(F,a['raw_centroid']))
    u=sub(P[111],c);z=sub(P[150],c);D=dot(sub(z,u),sub(z,u));delta=dot(z,z)-dot(u,u)
    assert delta>0 and 11*delta<D<12*delta
    W=[tuple(F(LAM[i],10**10)*(F(12-i,12)*x+F(i,12)*y) for x,y in zip(u,z)) for i in range(13)]
    assert W[0]==u and W[-1]==z
    ascent=[dot(W[i],sub(W[i+1],W[i])) for i in range(12)]
    assert all(x>0 for x in ascent)
    norms=[dot(w,w) for w in W]
    assert all(x<y for x,y in zip(norms,norms[1:]))
    outside={}
    for k,(n,h) in enumerate(zip(a['normals'],a['offsets'])):
        N=tuple(map(F,n));h=F(h);assert h>0
        violations=[(dot(N,tuple(v+t for v,t in zip(w,c)))/h-1) for w in W]
        m=max(violations)
        if m>0:outside[str(a['active_input_indices'][k])]=dict(max_excess=interval(m),vertices=[i for i,v in enumerate(violations) if v>0])
    assert '3' in outside and '17' in outside
    # Labels >=99 in this output are K99 input support labels, not S8 labels.
    report=dict(status='FREE_TWELVE_LINK_CHAIN_PASS_BUT_K99_SUPPORTS_FAIL',
      identity='K99_FREE_ASCENT_111_TO_150_LAMBDA_GRID10',link_count=12,
      interval_denominator=GRID,ratio_D_over_delta=interval(D/delta),
      minimum_strict_ascent=interval(min(ascent)),radial_gain=interval(delta),
      excluded_link_counts=list(range(1,12)),violated_K99_input_supports=outside,
      support_label_rule='K99 j>=99 maps to original S8 support j+1; smaller labels unchanged',
      is_polyhedron=False,accepted_record_advanced=False)
    return report
if __name__=='__main__':
    assert len(sys.argv)==3
    b=json.dumps(run(sys.argv[1]),sort_keys=True,separators=(',',':')).encode()
    Path(sys.argv[2]).write_bytes(b)
    print(b.decode())
