# material-12c3e1fa0644

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Complete literal recovery of two exact NONWINNERS, own176/weak000/C508.
Not own110. Run in an empty directory: python RECOVER_C508.py
Tested Python 3.13.5, numpy 2.3.5, scipy 1.17.0.
"""
"""Rebuild exact rational clipping bodies; scipy proposes, integers certify.
Input G6.json and checkpoint containing grid,new_normals. No optimizer required.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import sys,json,math,hashlib,itertools,time
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import numpy as np
from scipy.spatial import ConvexHull
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def prim(a):
 a=tuple(map(int,a));g=math.gcd(*a);a=tuple(x//g for x in a)
 return tuple(-x for x in a) if a[-1]<0 else a
def vertex(a,b,c):
 ds=det(a[:3],b[:3],c[:3])
 if not ds:return None
 bc=cross(b[:3],c[:3]);ca=cross(c[:3],a[:3]);ab=cross(a[:3],b[:3])
 return prim(tuple(a[3]*bc[k]+b[3]*ca[k]+c[3]*ab[k] for k in range(3))+(ds,))
def vs(a,b):return tuple(a[k]*b[3]-b[k]*a[3] for k in range(3))
def fsum(xs):
 if not xs:return F(0)
 if len(xs)==1:return xs[0]
 k=len(xs)//2;return fsum(xs[:k])+fsum(xs[k:])
def original_planes(d):
 P=[tuple(v) for v in d['points']];scale=d['grid'];h=ConvexHull(np.array(P,float))
 out=set()
 for tri in h.simplices:
  u,v,w=[P[i] for i in tri];a=cross(sub(v,u),sub(w,u));b=dot(a,u)
  if b<0:a=tuple(-x for x in a);b=-b
  assert b>0 and all(dot(a,p)<=b for p in P)
  out.add(prim(tuple(scale*x for x in a)+(b,)))
 return sorted(out)
def audit(g6,checkpoint):
 started=time.time();old=original_planes(g6);grid=checkpoint['grid']
 planes=old+[prim(tuple(v)+(grid,)) for v in checkpoint['new_normals']]
 assert all(q[3]>0 for q in planes)
 q=np.array([[x/a[3] for x in a[:3]] for a in planes]);dual=ConvexHull(q)
 verts=set();invalid=[]
 for t in dual.simplices:
  v=vertex(*(planes[i] for i in t))
  if v is None:continue
  if any(dot(a[:3],v[:3])>a[3]*v[3] for a in planes):invalid.append([int(x) for x in t]);continue
  verts.add(v)
 assert not invalid,('invalid dual proposals',invalid)
 verts=sorted(verts,key=lambda v:tuple(F(x,v[3]) for x in v[:3]))
 vp=np.array([[x/v[3] for x in v[:3]] for v in verts]);facets=[];active=[]
 for fi,a in enumerate(planes):
  ids=[i for i,v in enumerate(verts) if dot(a[:3],v[:3])==a[3]*v[3]]
  if len(ids)<3:continue
  k=max(range(3),key=lambda k:abs(a[k]));ax=[j for j in range(3) if j!=k]
  arr=vp[ids][:,ax];cen=arr.mean(0);angles=np.arctan2(arr[:,1]-cen[1],arr[:,0]-cen[0]);ids=[ids[j] for j in np.argsort(angles)]
  if dot(cross(vs(verts[ids[1]],verts[ids[0]]),vs(verts[ids[2]],verts[ids[1]])),a[:3])<0:ids.reverse()
  for j in range(len(ids)):
   x,y,z=[verts[ids[(j+k)%len(ids)]] for k in range(3)]
   assert dot(cross(vs(y,x),vs(z,y)),a[:3])>0,('flat/concave facet',fi)
  facets.append(ids);active.append(fi)
 edges=defaultdict(list);tri=[]
 for f,ids in enumerate(facets):
  for j,i in enumerate(ids):
   k=ids[(j+1)%len(ids)];edges[tuple(sorted((i,k)))].append((f,i,k))
  for j in range(1,len(ids)-1):tri.append((ids[0],ids[j],ids[j+1]))
 assert all(len(fs)==2 and fs[0][1:]==fs[1][1:][::-1] for fs in edges.values())
 assert len(verts)-len(edges)+len(facets)==2
 assert len({i for ids in facets for i in ids})==len(verts)
 # Every vertex link is a cycle, ruling out pinched boundary identifications.
 for i in range(len(verts)):
  inc=[f for f,ids in enumerate(facets) if i in ids];adj={f:set() for f in inc}
  for e,fs in edges.items():
   if i in e:f,g=fs[0][0],fs[1][0];adj[f].add(g);adj[g].add(f)
  assert all(len(adj[f])==2 for f in inc)
  seen=set();stack=inc[:1]
  while stack:
   f=stack.pop()
   if f not in seen:seen.add(f);stack+=list(adj[f]-seen)
  assert len(seen)==len(inc)
 vols=[];mom=[[],[],[]]
 for t in tri:
  a,b,c=[verts[i] for i in t];dd=det(a[:3],b[:3],c[:3]);assert dd>0
  v=F(dd,6*a[3]*b[3]*c[3]);vols.append(v)
  for k in range(3):mom[k].append(v*(F(a[k],a[3])+F(b[k],b[3])+F(c[k],c[3]))/4)
 V=fsum(vols);M=[fsum(x) for x in mom];center=[x/V for x in M]
 B=math.lcm(*(x.denominator for x in center));C=tuple(x.numerator*(B//x.denominator) for x in center)
 assert all(dot(a[:3],C)<a[3]*B for a in planes)
 Q=[planes[i][3]*B-dot(planes[i][:3],C) for i in active]
 def vg(i,j):
  v,w=verts[i],verts[j]
  return dot(tuple(B*v[k]-v[3]*C[k] for k in range(3)),tuple(v[3]*w[k]-w[3]*v[k] for k in range(3)))
 def fg(f,g):
  a,b=planes[active[f]],planes[active[g]]
  return Q[f]*dot(a[:3],b[:3])-Q[g]*dot(a[:3],a[:3])
 vadj=[set() for _ in verts];fadj=[set() for _ in facets]
 for (i,j),fs in edges.items():
  f,g=fs[0][0],fs[1][0];vadj[i].add(j);vadj[j].add(i);fadj[f].add(g);fadj[g].add(f)
 def classify(values):
  return 'strict' if all(v<0 for v in values) else ('weak' if all(v<=0 for v in values) else 'excluded')
 vc=[classify([vg(i,j) for j in vadj[i]]) for i in range(len(verts))]
 fc=[classify([fg(f,g) for g in fadj[f]]) for f in range(len(facets))]
 ec=[];zerosV=zerosF=0
 for i,j in edges:
  zerosV+=int(vg(i,j)==0)+int(vg(j,i)==0)
  f,g=edges[i,j][0][0],edges[i,j][1][0]
  zerosF+=int(fg(f,g)==0)+int(fg(g,f)==0)
  ec.append(classify([vg(i,j),vg(j,i),fg(f,g),fg(g,f)]))
 strict=[fc.count('strict'),vc.count('strict'),ec.count('strict')];weak=[fc.count('weak'),vc.count('weak'),ec.count('weak')]
 if weak==[0,0,0]:assert strict[0]+strict[1]-strict[2]==2
 identity=hashlib.sha256(json.dumps({'planes':planes,'vertices':verts,'facets':facets,'active':active},sort_keys=True,separators=(',',':')).encode()).hexdigest()
 report=dict(name=checkpoint['name'],V=len(verts),E=len(edges),F=len(facets),C=2*len(edges),strict=strict,weak=weak,zero_primitives=[zerosV,zerosF],active_original=sum(i<len(old) for i in active),active_new=sum(i>=len(old) for i in active),old_planes=len(old),input_planes=len(planes),volume_float=float(V),centroid_float=[float(x) for x in center],centroid_bits=B.bit_length(),volume_num_bits=V.numerator.bit_length(),volume_den_bits=V.denominator.bit_length(),vertex_bits=max(abs(x).bit_length() for v in verts for x in v),strict_U=[i for i,x in enumerate(vc) if x=='strict'],strict_S_input=[active[i] for i,x in enumerate(fc) if x=='strict'],geometry_sha256=identity,elapsed_seconds=time.time()-started)
 return report,dict(planes=planes,vertices=verts,facets=facets,active=active,centroid_homogeneous=list(C)+[B],volume=[V.numerator,V.denominator])

from collections import deque,Counter
def run(path,old_count=84):
 d=json.loads(Path(path).read_text());points=[tuple(F(z,p[3]) for z in p[:3]) for p in d['vertices']]
 vv=[[],[],[]];mm=[[],[],[]]
 for ids in d['facets']:
  for j in range(1,len(ids)-1):
   a,b,c=[points[i] for i in (ids[0],ids[j],ids[j+1])];n=cross(sub(b,a),sub(c,a))
   for k in range(3):
    s=a[k]+b[k]+c[k];sq=a[k]**2+b[k]**2+c[k]**2
    vv[k].append(n[k]*s/6);mm[k].append(n[k]*(s*s+sq)/48)
 V=F(*d['volume']);B=d['centroid_homogeneous'][3];C=d['centroid_homogeneous'][:3]
 vols=[fsum(v) for v in vv];mom=[fsum(m) for m in mm]
 assert all(v==V for v in vols)
 assert all(m==V*F(c,B) for m,c in zip(mom,C))
 normals=[d['planes'][i] for i in d['active']];q=[a[3]*B-dot(a[:3],C) for a in normals]
 rev=[[] for _ in normals]
 for f,a in enumerate(normals):
  aa=dot(a[:3],a[:3])
  for g,b in enumerate(normals):
   if f!=g and q[f]*dot(a[:3],b[:3])-q[g]*aa>0:rev[g].append(f)
 dist=[None]*len(normals);queue=deque()
 for i,fi in enumerate(d['active']):
  if fi<old_count:dist[i]=0;queue.append(i)
 while queue:
  g=queue.popleft()
  for f in rev[g]:
   if dist[f] is None:dist[f]=dist[g]+1;queue.append(f)
 new=[dist[i] for i,fi in enumerate(d['active']) if fi>=old_count]
 assert all(x is not None for x in new)
 out=dict(projected_volume_three_axes_equal=True,projected_first_moments_equal=True,maximum_new_shortest_depth=max(new),new_depth_histogram=dict(sorted(Counter(new).items())),active_input_indices_at_maxdepth=[fi for i,fi in enumerate(d['active']) if dist[i]==max(new)])
 Path(str(Path(path).with_suffix(''))+'_MASS_DEPTH.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
 print('PROJECTED_MASS_AND_POLAR_DEPTH_PASS',json.dumps(out,sort_keys=True))

G6={"grid":1000000,"points":[[-662782,-214465,-845973],[-414228,-151742,533649],[-161896,254607,812156],[365352,256078,682778],[-4963,148822,-521027],[472559,520988,212704],[79060,562904,-173068],[201613,126680,-443592],[329321,453145,628173],[223093,597478,579771],[-19072,614025,655946],[-249702,561436,698505],[-441568,542642,645050],[81579,740260,404654],[-621409,499632,558154],[-759574,464284,346398],[-876227,418544,281729],[-762901,475717,422075],[-969023,321126,89302],[-933907,249672,-106357],[-931297,367490,186346],[-990566,281683,-2502],[-1004114,233262,-93695],[-1009407,175066,-181963],[-1003594,111429,-275498],[-985825,56733,-362387],[-963561,3357,-431336],[-926489,-29260,-514430],[-874803,-74796,-604952],[-797712,-129095,-709746],[212288,-80824,-582533],[-530449,-300001,-896862],[-453991,-363552,-909506],[-263404,-613951,20338],[-477834,-372599,114345],[-600760,-232410,-880486],[-364153,-430343,-913823],[217011,-462047,-780335],[486981,106570,612006],[157779,-569803,63306],[-149044,-601434,-828255],[-98079,-133974,751134],[19869,-745421,-660667],[119026,-858571,-341744],[285028,-657317,-632695],[168908,-413062,260503]]}
CHECKPOINT={"g6_sha256":"63ead46daff5c7c9cd4344699cbe551a7e92b2a2851703aacfa55eb1621b6aa5","grid":1000000000000,"name":"G6_CHAIN_M60_I1_G12","new_normals":[[2434132816490,-97078584420,-398834534390],[2413399775672,1970402792,-498663761618],[2385078218776,96201617398,-596592276071],[2336558981293,217495628022,-717709427412],[2286046158226,331286870390,-813270640317],[2226035201166,440307274616,-907511135646],[2156847802768,546678948835,-998650206164],[2082699286913,652475729176,-1077827944470],[2007734674055,746921948716,-1147464965957],[1923738611994,842074578816,-1214490604605],[1825937965044,939690656343,-1282180295403],[1725757681310,1026985006258,-1344066028004],[1629461436336,1107908706329,-1392328165719],[1520517588189,1191556694050,-1438165529443],[1402690792169,1268561613057,-1483681560835],[1275008896269,1343679815185,-1524228753615],[1136910583136,1413162210713,-1561849689961],[962433246722,1496782461268,-1588729381609],[770117355205,1571075925496,-1608209833487],[584418520551,1635859475650,-1609758490848],[401313246560,1690397152517,-1598016759570],[200501559274,1745648453154,-1562010886766],[16258116306,1785591203043,-1516932500553],[-158470701934,1807099230045,-1471670253294],[-352636045545,1818287377453,-1408580410550],[-554779597658,1809266989272,-1336861291873],[-767240457452,1779613710004,-1248524774610],[-982766259472,1724579241402,-1146517878821],[-1189981866520,1644855085658,-1034914387412],[-1385347197961,1539021396939,-917384874526],[-1560194565649,1416110685809,-792769268778],[-1716590800533,1268708053361,-671363318549],[-1849977370079,1112070498362,-535838053657],[-1954882081172,949073061492,-414041592079],[-2035313209231,786892983532,-289026805728],[-2092255383599,628149778638,-182103408852],[-2133145563018,454276067910,-88877399550],[-2154683092821,290871712535,10794232353],[-2159527602413,114129851786,103844692216],[-2149307681632,-75488579503,153417025530],[-2125952079704,-252286510777,181050217308],[-2088023458726,-430912074107,192372581644],[-2029786348353,-619204927672,200221842239],[-1958482082887,-799059062345,176995196108],[-1874405244003,-967587614124,136612775068],[-1769307701825,-1134494743861,103179159617],[-1629639440506,-1309998247123,69403730378],[-1466340073635,-1473305220228,31181699769],[-1285329829135,-1617285434072,14514037064],[-1085795837561,-1741641761042,-1661882042],[-896457840731,-1834007237833,16303655684],[-932613236960,-1765214769944,304361462556],[-960286794695,-1651311611715,581871498171],[-977054089694,-1492156213690,843843368621],[-968448484707,-1292045730133,1088904411786],[-933280187399,-1074412317063,1294812839228],[-852091184883,-808312305925,1486078906659],[-757966867143,-493409274763,1625531502274],[-619355160564,-125578494862,1703044741335],[-124890960139,-85886414013,1740467219812]],"parent":[-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58]}
EXPECTED={12:('ba0d5d46957d91b0ef99e0ddb475c0f18ded3b513125e67ecde46c026ca6fb63','504c86dedd6b9293ce1bf0c34f3db8349f0fe95db534f6b88e28c6e57cfe6f35'),5:('0e46277b37be19e5a35a391f73f7a16957edf93a9e4b4128144ce8eb17b637fd','986270e0b0f5d396fe78b5ecc93ed28b6154999dc3d9c2e79fa016c8a3c67510')}
def main():
 raw=json.dumps(G6,separators=(',',':')).encode()
 assert hashlib.sha256(raw).hexdigest()==CHECKPOINT['g6_sha256']
 Path('G6.json').write_bytes(raw)
 for digits in (12,5):
  cp=dict(CHECKPOINT);cp['name']='G6_CHAIN_M60_I1_G'+str(digits);cp['grid']=10**digits
  cp['new_normals']=[[round(F(x,10**(12-digits))) for x in row] for row in CHECKPOINT['new_normals']]
  raw=(json.dumps(cp,sort_keys=True,separators=(',',':'))+'\n').encode()
  assert hashlib.sha256(raw).hexdigest()==EXPECTED[digits][0]
  Path(cp['name']+'.json').write_bytes(raw)
  report,geometry=audit(G6,cp)
  assert (report['V'],report['E'],report['F'],report['C'])==(164,254,92,508)
  assert report['strict']==[1,7,6] and report['weak']==[0,0,0] and report['zero_primitives']==[0,0]
  assert report['active_new']==60 and report['active_original']==32
  path=Path(cp['name']+'_EXACT_GEOMETRY.json')
  raw=(json.dumps(geometry,sort_keys=True,separators=(',',':'))+'\n').encode()
  assert hashlib.sha256(raw).hexdigest()==EXPECTED[digits][1]
  path.write_bytes(raw)
  report.pop('elapsed_seconds')
  Path(cp['name']+'_EXACT_REPORT_STABLE.json').write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
  print('G6_CHAIN_EXACT_AUDIT_PASS',cp['name'],flush=True)
  run(path)
  result=json.loads(Path(str(path.with_suffix(''))+'_MASS_DEPTH.json').read_text())
  assert result['maximum_new_shortest_depth']==59 and result['active_input_indices_at_maxdepth']==[143]
 print('C508_RECOVERY_COMPLETE_NONWINNER_176_WEAK000',flush=True)
if __name__=='__main__':main()
