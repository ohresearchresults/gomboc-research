"""Delete the unique simple unstable vertex from an exact S8 deletion body.
The three edge-slide directions have this same endpoint at s=1. This endpoint
is NOT covered by the open-interval certificate; run both exact hull auditors.
"""
from fractions import Fraction as Q
from math import lcm,gcd
from pathlib import Path
import json,sys
sys.set_int_max_str_digits(0)
def sub(x,y):return tuple(a-b for a,b in zip(x,y))
def cross(x,y):return (x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def build(data):
 P=[tuple(map(Q,p)) for p in data['raw_vertices']];adj=[set() for _ in P]
 for a,b in data['edges']:adj[a].add(b);adj[b].add(a)
 uu=[i for i in data['unstable_vertices'] if len(adj[i])==3];assert len(uu)==1;u=uu[0];a,b,c=sorted(adj[u]);n=cross(sub(P[b],P[a]),sub(P[c],P[a]));h=dot(n,P[a])
 if dot(n,P[u])<h:n=tuple(-x for x in n);h=-h
 assert h>0 and all(dot(n,p)<=h for i,p in enumerate(P) if i!=u)
 d=lcm(*(x.denominator for x in (*n,h)));row=[int(x*d) for x in (*n,h)];g=gcd(*row);row=[x//g for x in row]
 return {'H':[list(n)+[h] for n,h in zip(data['normals'],data['offsets'])]+[row]}
if __name__=='__main__':
 raw=build(json.loads(Path(sys.argv[1]).read_text()));Path(sys.argv[2]).write_text(json.dumps(raw,sort_keys=True,separators=(',',':')))
