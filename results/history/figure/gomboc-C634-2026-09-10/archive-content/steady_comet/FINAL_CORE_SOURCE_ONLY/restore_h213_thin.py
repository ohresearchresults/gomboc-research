"""Restore the literal H213 edge (26,82) by a local exact contact release.
Only the free x/y controls of support 27 and one incidence equation change.
The physical apex remains (0,0,1); its role is never substituted for the filled centroid.
"""
from pathlib import Path
from fractions import Fraction as Q
import sys,json,numpy as np
from numeric import recover,mechanics,topology
from fit_restoration import embedded_faces
sys.set_int_max_str_digits(0);R=Path(__file__).parent
name=sys.argv[1] if len(sys.argv)>1 else 'C640_CONTACT60_121';src=R/name;g=json.loads((src/'GENERATOR.json').read_text());a=json.loads((src/'A.json').read_text());raw=json.loads((src/'RAW.json').read_text());qq=[[Q(int(t),int(h[3])) for t in h[:3]] for h in raw['H']];X=recover(g);n=g['n_supports'];node=next(n+i for i,cy in enumerate(g['groups']) if set(cy)=={26,27,65,82});assert [n+i for i,cy in enumerate(g['groups']) if 27 in cy]==[137,node]
assert not any(27 in dep for i,dep,axes in g['plan'])
_,ef=topology(a['faces']);edges={tuple(sorted(v)) for v in ef.values()};assert (26,82) not in edges;edges.add((26,82));rotation={int(k):v for k,v in json.loads((R/'C650_rotation.json').read_text()).items()};pf,rot,df=embedded_faces(edges,rotation);faces=[[df[i,j] for j in rot[i]] for i in range(n)];sign=1 if X[node,0]>0 else -1
for k in range(4,13):
 z=json.loads(json.dumps(g));D=z['grid'];
 if D%10**k:continue
 z['groups'][node-n]=[26,65,82]
 for j,r in enumerate(z['plan']):
  if r[0]==27:z['plan'][j]=[27,[137],[2]]
 z['controls'][27][0]=round(qq[27][0]*D)-sign*(D//10**k);z['controls'][27][1]=round(qq[27][1]*D)
 q=recover(z)[:n];from numeric import vertices
 owners=[None]*len(pf)
 for f,cy in enumerate(pf):owners[f]=cy
 P=vertices(q,owners)
 fs=[cy[:] for cy in faces]
 for i,cy in enumerate(fs):
  if q[i]@np.cross(P[cy[1]]-P[cy[0]],P[cy[2]]-P[cy[0]])<0:fs[i]=cy[::-1]
 try:rr=mechanics(q,fs,tol=1e-11)
 except Exception as ex:print('RESTORE_ERROR',k,repr(ex),flush=True);continue
 tag=f'C{2*rr["E"]}_H213_RESTORED_FROM_{name}_EPS1E{k}'
 print('RESTORE',k,'q27sign',sign,'node',node,rr,flush=True)
 if rr['counts']==[1,1,0] and rr['min_gap']>1e-10 and rr['max_incidence_error']<1e-8 and min(rr['polar_escape_min'],rr['primal_escape_min'])>1e-8:
  (R/(tag+'_GENERATOR.json')).write_text(json.dumps(z,sort_keys=True,separators=(',',':')));(R/(tag+'_faces.json')).write_text(json.dumps(fs,separators=(',',':')));(R/(tag+'_numeric.json')).write_text(json.dumps(rr,indent=2));print('RESTORE_NUMERIC_WINNER',tag,flush=True);break
