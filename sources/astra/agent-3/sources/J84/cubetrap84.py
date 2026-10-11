"""Exact robust U trap for an unchanged J82_G6 surface, arbitrary centre drift."""
import json
from fractions import Fraction as R
from exact84 import load,topology,mass,dot,sub,ROOT
P,F=load();ed,_=topology(P,F);V,g=mass(P,F)
threshold={}
for a,b in ed:
    for i,j in [(a,b),(b,a)]:
        d=sub(P[j],P[i]);f=dot(sub(P[i],g),d)
        threshold[i,j]=max(R(0),-f/sum(abs(x) for x in d))
# Least possible maximum threshold on a directed route to 0.
dist=[None]*len(P);dist[0]=R(0)
for _ in range(len(P)):
    changed=False
    for (i,j),t in threshold.items():
        if dist[j] is not None:
            d=max(t,dist[j])
            if dist[i] is None or d<dist[i]:dist[i]=d;changed=True
    if not changed:break
assert all(d is not None for d in dist)
root0=min(t for (i,j),t in threshold.items() if i==0)
critical=max(dist);eps=min(root0,critical)
print('root0_limit',float(root0),'trap_limit',float(critical),'combined',float(eps))
for rho in [R(1,1000),R(1,100),R(1,40),R(1,20),eps*R(99,100)]:
    B=[i for i,d in enumerate(dist) if d>rho]
    valid=B and rho<root0
    print('rho',float(rho),'Bsize',len(B),'valid',bool(valid))
# Use a simple exact radius below the maximal threshold.
rho=R(int(float(eps)*10000),10000)
assert rho>0 and rho<eps
B=[i for i,d in enumerate(dist) if d>rho]
cut=[(i,j) for i,j in threshold if i in B and j not in B]
proof=[]
for i,j in cut+[(i,j) for i,j in threshold if i==0]:
    d=sub(P[j],P[i]);f=dot(sub(P[i],g),d);L=sum(abs(x) for x in d);upper=f+rho*L
    assert upper<0
    proof.append({'edge':[i,j],'f_own':str(f),'L1':str(L),'upper':str(upper)})
out={'rho':str(rho),'own_centroid':[str(x) for x in g],'B':B,'cut':[list(e) for e in cut],
     'proof':proof,'root0_limit':str(root0),'minimax_limit':str(critical),'distances':[str(x) for x in dist],
     'scope':'Unchanged hull and every arbitrary reference centre in closed infinity cube. No inference for changed cut/interface geometry.'}
(ROOT/'J84_CUBE_TRAP.json').write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
print('J84_REFERENCE_CUBE_U_GE_2_EXACT_PASS',str(rho),len(B),len(cut))
