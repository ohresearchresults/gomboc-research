"""Exact D132 co-record from the six-part S8 source capsule.
Usage: python -B -S REPLAY_D132.py S8_SOURCE NEW_OUT
Assertions must remain enabled. No third-party dependency is used.
"""
from pathlib import Path
from fractions import Fraction as F
from math import lcm,gcd
import json,hashlib,sys
if not __debug__:raise RuntimeError('Assertions must be enabled')
sys.set_int_max_str_digits(0)
source=Path(sys.argv[1]).resolve();out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=False);sys.path.insert(0,str(source))
import REPLAY,RECONSTRUCT,check_A,check_B,centred_mass
canon=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def save(n,x):
 b=canon(x);(out/n).write_bytes(b);return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def bits(x):return max(abs(x.numerator).bit_length(),x.denominator.bit_length())
REPLAY.sources();parentraw=RECONSTRUCT.recover(REPLAY.generator('S8'));base=check_A.run(parentraw);REPLAY.validate(base,'S8')
P=[tuple(map(F,p))for p in base['raw_vertices']];a,b,c=[P[i]for i in (127,133,136)];n=check_A.cross(check_A.sub(b,a),check_A.sub(c,a));h=check_A.dot(n,a)
row=(*n,h);D=lcm(*(v.denominator for v in row));row=tuple(int(D*v)for v in row);g=gcd(*row);row=tuple(v//g for v in row)
if row[-1]<0:row=tuple(-v for v in row)
assert row[-1]>0
vals=[check_A.dot(row[:3],p)-row[-1]for p in P]
assert [i for i,v in enumerate(vals)if v>0]==[132];assert [i for i,v in enumerate(vals)if v==0]==[127,133,136]
raw={'H':sorted([tuple(r)for r in parentraw['H']]+[row])};files={};files['raw.json']=save('raw.json',raw)
a=check_A.run(raw);b=check_B.run(raw);assert a==b
assert a['raw_vertices']==[p for i,p in enumerate(base['raw_vertices'])if i!=132]
assert [a[k]for k in ('V','E','F')]==[176,312,138] and a['counts']==[1,1,0]and a['weak']==[0,0,0]
assert all(a[k]==0 for k in ('face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count'))
files['A.json']=save('A.json',a);files['B.json']=save('B.json',b);files['CENTRED_MASS.json']=save('CENTRED_MASS.json',centred_mass.run(a))
g=tuple(map(F,a['raw_centroid']));Z=[tuple(v-w for v,w in zip(tuple(map(F,p)),g))for p in a['raw_vertices']]
stats=dict(name='COORD_S8_D132_C624',V=176,E=312,F=138,C=624,counts=a['counts'],weak=a['weak'],stable=a['stable_face_ids'],unstable=a['unstable_vertices'],saddles=a['saddle_edges'],raw_coordinate_bits=max(bits(v)for p in a['raw_vertices']for v in map(F,p)),support_bits=max(abs(v).bit_length()for r in raw['H']for v in r),centroid_bits=max(map(bits,g)),centred_coordinate_bits=max(bits(v)for p in Z for v in p),centred_common_denominator_bits=lcm(*(v.denominator for p in Z for v in p)).bit_length(),volume_bits=bits(F(a['ordinary_volume'])),first_moment_bits=max(bits(F(v))for v in a['raw_first_moments']),parent_deleted_rawlex_vertex=132,cut_face_parent_vertices=[127,133,136],primitive_zero_counts=[a[k]for k in ('face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count')])
files['STATS.json']=save('STATS.json',stats);files['RAW_COMPLEX.json']=save('RAW_COMPLEX.json',dict(vertices=a['raw_vertices'],faces=a['faces'],true_edges=a['edges']))
receipt=dict(status='COORD_S8_D132_C624_FULL_EXACT_PASS',stats=stats,files=files);save('RECEIPT.json',receipt);print(json.dumps(receipt,sort_keys=True),flush=True)
