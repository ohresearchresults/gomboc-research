"""Exact finite independent-star trials on literal S8.
Uses unchanged ATLAS57 source capsule; no numerical optimizer or fitted centre.
"""
import argparse,hashlib,json,sys
from fractions import Fraction as F
from itertools import combinations
from math import gcd,lcm
from pathlib import Path
sys.set_int_max_str_digits(0)
def enc(o):return json.dumps(o,sort_keys=True,separators=(',',':'),default=str).encode()
def save(p,o):
 b=enc(o);p.write_bytes(b);return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def add(a,b):return [x+y for x,y in zip(a,b)]
def sub(a,b):return [x-y for x,y in zip(a,b)]
def scale(t,a):return [t*x for x in a]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def plane(a,b,c):
 n=cross(sub(b,a),sub(c,a));return n,dot(n,a)
def mass(P,faces):
 D=F(0);L=[F(0)]*3
 for cy in faces:
  for j in range(1,len(cy)-1):
   a,b,c=[P[i] for i in (cy[0],cy[j],cy[j+1])];dd=dot(a,cross(b,c));assert dd>=0
   D+=dd;L=add(L,scale(dd,add(add(a,b),c)))
 return D/6,scale(F(1,24),L)
def graph(faces):
 ee={}
 for f,cy in enumerate(faces):
  for i,j in zip(cy,cy[1:]+cy[:1]):ee.setdefault(tuple(sorted((i,j))),[]).append(f)
 assert all(len(ff)==2 for ff in ee.values());return ee

def star(P,q,faces,i):
 ow=[f for f,cy in enumerate(faces) if i in cy];tri=[f for f in ow if len(faces[f])==3];large=[f for f in ow if len(faces[f])>3]
 assert len(ow)==3 and len(tri)==2 and len(large)==1
 cy=faces[large[0]];k=cy.index(i);a,b=cy[k-1],cy[(k+1)%len(cy)];d=sub(P[b],P[a]);c=next(j for f in tri for j in faces[f] if j not in [i,a,b]);w=abs(dot(sub(P[a],P[c]),cross(sub(P[i],P[c]),sub(P[b],P[c]))))/6
 cons=[(1-dot(n,P[i]),-dot(n,d),['fixed',f]) for f,n in enumerate(q) if f not in tri]
 for f in tri:
  n,h=plane(*(P[j] for j in faces[f]));n1,h1=plane(*(add(P[j],d) if j==i else P[j] for j in faces[f]));dn,dh=sub(n1,n),h1-h
  cons.append((h,dh,['height',f]))
  for j,p in enumerate(P):
   if j!=i:cons.append((h-dot(n,p),dh-dot(dn,p),['rotating',f,j]))
 assert all(g>=0 for g,v,label in cons)
 lo=max(-g/v for g,v,_ in cons if v>0);hi=min(-g/v for g,v,_ in cons if v<0);assert lo<0<hi
 return {'vertex':i,'a':a,'b':b,'c':c,'direction':d,'K':scale(w/4,d),'tetrahedron_volume':w,'interval':[lo,hi],'triangles':tri,'nontriangle':large[0]}

def proposal(P,q,faces,stars,t):
 X=[p[:] for p in P]
 for i,v in t.items():X[i]=add(X[i],scale(v,stars[i]['direction']))
 rows=[];aliases=[];index={}
 for f,cy in enumerate(faces):
  if len(cy)==3:
   n,h=plane(*(X[i] for i in cy))
   if not any(n):continue
  else:n,h=q[f],F(1)
  assert h>0,('height',f)
  assert all(dot(n,X[i])==h for i in cy),('plane',f)
  bad=[j for j,p in enumerate(X) if dot(n,p)>h]
  assert not bad,('support_violation',f,bad)
  v=n+[h];D=lcm(*(x.denominator for x in v));r=[int(D*x) for x in v];g=gcd(*r);r=tuple(x//g for x in r)
  if r not in index:index[r]=len(rows);rows.append(list(r));aliases.append([])
  aliases[index[r]].append(f)
 return {'H':rows},X,aliases

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--parent',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--audit',action='store_true');a=ap.parse_args();assert __debug__
 root=a.parent.resolve();sys.path.insert(0,str(root))
 for name,spec in json.loads((root/'MANIFEST.json').read_bytes()).items():
  b=(root/name).read_bytes();assert len(b)==spec['bytes'] and hashlib.sha256(b).hexdigest()==spec['sha256']
 import exact57,rational56
 from RECONSTRUCT import solve
 d,faces=exact57.source();q=rational56.points(d)[:137];P=exact57.physical(q,faces);assert P==sorted(P);ee=graph(faces);assert (len(P),len(ee),len(faces))==(177,312,137);V0,M0=mass(P,faces)
 a.out.mkdir(parents=True,exist_ok=False)
 trials=[('PAIR',{7:1,111:0},[]),('COMP111',{111:0},[0,16,74]),('COMP7',{7:1},[0,21,87])]
 ids=sorted({i for _,p,c in trials for i in list(p)+c});stars={i:star(P,q,faces,i) for i in ids};save(a.out/'STARS.json',stars)
 summary={}
 for name,primary,comp in trials:
  out=a.out/name;out.mkdir();selected=set(primary)|set(comp);conflicts=[list(ij) for ij in combinations(sorted(selected),2) if ij in ee]
  assert not conflicts,(name,conflicts)
  t={i:stars[i]['interval'][side] for i,side in primary.items()};delta=[F(0)]*3
  for i,v in t.items():delta=add(delta,scale(v,stars[i]['K']))
  if comp:
   sol=solve([[stars[i]['K'][k] for i in comp] for k in range(3)],scale(-1,delta));t.update(zip(comp,sol))
  status={'selected_original_vertices':sorted(selected),'parameters':{str(i):str(v) for i,v in t.items()},'independent_set':True,'isolated_interval_failures':[]}
  for i,v in t.items():
   lo,hi=stars[i]['interval'];
   if not lo<=v<=hi:status['isolated_interval_failures'].append(i)
  try:
   assert not status['isolated_interval_failures'],'outside isolated star interval'
   raw,cloud,aliases=proposal(P,q,faces,stars,t);V,M=mass(cloud,faces);expected=M0[:]
   for i,v in t.items():expected=add(expected,scale(v,stars[i]['K']))
   assert V==V0 and M==expected
   if comp:assert M==M0
   save(out/'RAW.json',raw);save(out/'CLOUD.json',cloud);save(out/'DEFINITION.json',{'parameters':t,'aliases':aliases,'volume':V,'first_moments':M})
   status.update(status='EXACT_SUPPORT_AND_JOINT_MOMENT_PASS',supplied_H=len(raw['H']))
   if a.audit:
    import check_A,check_B,centred_mass
    aa=check_A.run(raw);save(out/'A.json',aa);print(name,'A',aa['V'],aa['E'],aa['F'],aa['counts'],aa['weak'],flush=True)
    bb=check_B.run(raw);save(out/'B.json',bb);assert aa==bb
    assert set(tuple(map(F,p)) for p in aa['raw_vertices'])<={tuple(p) for p in cloud}
    assert F(aa['ordinary_volume'])==V and list(map(F,aa['raw_first_moments']))==M
    cm=centred_mass.run(aa);save(out/'MASS.json',cm)
    status.update(status='TWO_FULL_EXACT_AUDITS_AND_JOINT_MASS_BOUND',V=aa['V'],E=aa['E'],F=aa['F'],C=2*aa['E'],strict=aa['counts'],weak=aa['weak'],stable_faces=aa['stable_face_ids'],unstable_vertices=aa['unstable_vertices'],saddle_edges=aa['saddle_edges'],disposition='ephemeral_not_promoted_pending_canonical_capsule')
  except AssertionError as error:status.update(status='EXACT_PROPOSAL_REJECTED',error=str(error))
  save(out/'STATUS.json',status);summary[name]=status;print(name,status['status'],status.get('error',''),flush=True)
 save(a.out/'SUMMARY.json',summary)
 manifest={}
 for p in sorted(a.out.rglob('*')):
  if p.is_file():b=p.read_bytes();manifest[str(p.relative_to(a.out))]={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
 save(a.out/'OUTPUT_MANIFEST.json',manifest);print('S8_COUPLED_FINITE_TRIALS_FINISHED_READ_EACH_STATUS',flush=True)
if __name__=='__main__':main()
