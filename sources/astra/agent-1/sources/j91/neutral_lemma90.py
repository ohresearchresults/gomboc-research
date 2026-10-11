"""Exact witnesses for the finite U1 enlargement lemma and an available rational
three-coordinate centroid correction chart. This checks the chart rank and the
existing eight apex witnesses; it does not instantiate a new corrected body.
"""
import sys,json,itertools
from pathlib import Path
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
base=json.loads(Path('J90_DETACHED_C390_G8_AUDIT.json').read_text());cap=json.loads(Path(sys.argv[1] if len(sys.argv)>1 else 'J90_BALANCED_C452_G14_CAPS.json').read_text());g=tuple(map(F,base['centroid']));X=[tuple(map(F,v)) for v in base['vertices']];P=[sub(x,g) for x in X];R=dot(P[base['U'][0]],P[base['U'][0]])
records=[]
for fi,raw in cap['apexes'].items():
 w=tuple(map(F,raw));a=sub(w,g);af=list(map(float,a));xf=[list(map(float,p)) for p in P]
 j=max(range(len(X)),key=lambda j:sum(af[k]*(xf[j][k]-af[k]) for k in range(3)))
 W=dot(a,sub(X[j],w));assert W>0 and dot(a,a)<R
 records.append(dict(input_plane=int(fi),old_witness_vertex=j,positive_chord=str(W),positive_chord_approx=float(W)))
lines=Path('J90_DETACHED_C390_G8.txt').read_text().splitlines();m,D=map(int,lines[0].split());N=[tuple(map(int,s.split())) for s in lines[1:]]
a,b,c=N[6],N[14],N[16];u=(0,a[2],-a[1]);v=(0,b[2],-b[1]);w=(-c[2],0,c[0]);det=dot(u,cross(v,w));assert det!=0
out=dict(witnesses=records,chart=dict(planes=[6,14,16],directions=[u,v,w],integer_direction_determinant=det,scaled_direction_determinant=str(F(det,D**3)),note='Columns of moment correction are Vcap_j*u_j/4; all three cap volumes are positive. Exact centre correction is not instantiated by this script.'))
Path(sys.argv[2] if len(sys.argv)>2 else 'J90_NEUTRAL_LEMMA.json').write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n');print('J90_EIGHT_EXACT_U_SAFE_CHORDS_AND_CHART_RANK_PASS',[(r['input_plane'],r['old_witness_vertex'],r['positive_chord_approx']) for r in records],det)
