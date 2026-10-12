# material-e013ad40bbb5

AI research material

---

"""Exact rational H-polyhedron, uniform mass and global strict/weak census.
Standard library only. All independent triples are enumerated, all halfspaces
checked exactly, maximal facets reconstructed, and six positive normal-cone
representations prove boundedness. Origin is interior because every offset>0.
No numerical hull or persistence threshold is used in certification.
Q=[] is certified by the exact single strict polar root and no weak polar roots:
every other polar vertex has a strictly increasing edge, hence no finite positive
zero-dimensional superlevel bar. The Q filtration is not separately replayed.
"""
import sys,json,argparse,hashlib,time
from pathlib import Path
from fractions import Fraction as R
from itertools import combinations
from functools import cmp_to_key
from math import gcd,lcm
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def det(a,b,c):return dot(a,cross(b,c))
def balanced(v):
 if not v:return R(0)
 while len(v)>1:v=[v[i]+v[i+1] if i+1<len(v) else v[i] for i in range(0,len(v),2)]
 return v[0]
def fracstr(n,d=1):return str(R(n,d))

def enumerate_h(planes):
 n=[tuple(p[:3]) for p in planes];h=[p[3] for p in planes];assert min(h)>0
 bound=[];todo=[(j,s) for j in range(3) for s in [-1,1]];vs=set()
 for ids in combinations(range(len(n)),3):
  a,b,c=ids;co=[cross(n[b],n[c]),cross(n[c],n[a]),cross(n[a],n[b])];dd=dot(n[a],co[0])
  if not dd:continue
  for j,s in todo[:]:
   lam=[R(s*v[j],dd) for v in co]
   if min(lam)>=0:
    assert tuple(sum(lam[k]*n[ids[k]][q] for k in range(3)) for q in range(3))==tuple(s if q==j else 0 for q in range(3))
    bound.append({'axis':j,'sign':s,'planes':list(ids),'weights':list(map(str,lam)),'bound':str(sum(lam[k]*h[ids[k]] for k in range(3)))});todo.remove((j,s))
  x=tuple(sum(h[ids[k]]*co[k][j] for k in range(3)) for j in range(3))
  if dd<0:dd=-dd;x=tuple(-v for v in x)
  if any(dot(nn,x)>hh*dd for nn,hh in zip(n,h)):continue
  gg=gcd(*x,dd);vs.add(tuple(v//gg for v in x)+(dd//gg,))
 assert not todo,'Normals do not positively span space; boundedness not established'
 vs=sorted(vs);assert len(vs)>=4
 p=[tuple(R(x[j],x[3]) for j in range(3)) for x in vs];facets=[];active=[]
 for k,(nn,hh) in enumerate(zip(n,h)):
  ids=[i for i,x in enumerate(vs) if dot(nn,x[:3])==hh*x[3]]
  if len(ids)<3:continue
  drop=max(range(3),key=lambda j:abs(nn[j]));axes=[j for j in range(3) if j!=drop]
  ids.sort(key=lambda i:tuple(p[i][j] for j in axes))
  def ori(a,b,c):
   u=[p[b][j]-p[a][j] for j in axes];v=[p[c][j]-p[a][j] for j in axes];return u[0]*v[1]-u[1]*v[0]
  lo=[];up=[]
  for i in ids:
   while len(lo)>1 and ori(lo[-2],lo[-1],i)<=0:lo.pop()
   lo.append(i)
  for i in reversed(ids):
   while len(up)>1 and ori(up[-2],up[-1],i)<=0:up.pop()
   up.append(i)
  f=lo[:-1]+up[:-1]
  if len(f)<3:continue
  if dot(cross(sub(p[f[1]],p[f[0]]),sub(p[f[2]],p[f[0]])),nn)<0:f.reverse()
  assert set(f)==set(ids),'unexpected non-extreme triple intersection'
  ii=f.index(min(f));f=f[ii:]+f[:ii];facets.append(f);active.append(k)
 edges={}
 for j,f in enumerate(facets):
  for a,b in zip(f,f[1:]+f[:1]):edges.setdefault(tuple(sorted((a,b))),[]).append((j,a,b))
 assert {i for f in facets for i in f}==set(range(len(vs)))
 assert all(len(ef)==2 and ef[0][1:]==ef[1][1:][::-1] for ef in edges.values())
 assert len(vs)-len(edges)+len(facets)==2
 return vs,p,facets,active,edges,bound

def certify(data):
 planes=[tuple(map(int,row)) for row in data['planes']]
 assert len(set(planes))==len(planes)
 st=time.monotonic();vs,p,faces,active,edges,bound=enumerate_h(planes)
 print('HULL',len(p),len(edges),len(faces),'seconds',time.monotonic()-st,flush=True)
 ds=[];ms=[[],[],[]]
 for f in faces:
  a=p[f[0]]
  for k in range(1,len(f)-1):
   b,c=p[f[k]],p[f[k+1]];dd=det(a,b,c);assert dd>0;ds.append(dd)
   for j in range(3):ms[j].append(dd*(a[j]+b[j]+c[j]))
 sixV=balanced(ds);V=sixV/6;g=[balanced(v)/(4*sixV) for v in ms]
 K=lcm(*(a.denominator for a in g));G=tuple(int(a*K) for a in g)
 print('MASS','centroid_bits',K.bit_length(),'seconds',time.monotonic()-st,flush=True)
 X=[v[:3] for v in vs];D=[v[3] for v in vs]
 w=[tuple(K*x[j]-d*G[j] for j in range(3)) for x,d in zip(X,D)]
 ni=[planes[k][:3] for k in active];T=[K*planes[k][3]-dot(planes[k][:3],G) for k in active];assert min(T)>0
 U=[];WU=[];pw=[]
 for i,ww in enumerate(w):
  vals=[(dot(ww,tuple(X[j][q]*D[i]-X[i][q]*D[j] for q in range(3))),j) for j in range(len(X)) if j!=i]
  mx,j=max(vals);pw.append(j)
  if mx<0:U.append(i)
  elif mx==0:WU.append(i)
 S=[];WS=[];qw=[]
 for i,nn in enumerate(ni):
  vals=[(dot(nn,nj)*T[i]-dot(nn,nn)*T[j],j) for j,nj in enumerate(ni) if j!=i]
  mx,j=max(vals);qw.append(j)
  if mx<0:S.append(i)
  elif mx==0:WS.append(i)
 H=[];WH=[];events=[];rad=[(dot(ww,ww),d*d) for ww,d in zip(w,D)]
 for (a,b),ef in edges.items():
  d=tuple(X[b][j]*D[a]-X[a][j]*D[b] for j in range(3));dd=dot(d,d);wd=dot(w[a],d);tn=-wd*D[b];td=K*dd
  r=tuple(w[a][j]*dd-d[j]*wd for j in range(3));n,m=ni[ef[0][0]],ni[ef[1][0]];nn,mm,nm=dot(n,n),dot(m,m),dot(n,m);assert nn*mm>nm*nm
  rn,rm=dot(r,n),dot(r,m);ca=rn*mm-rm*nm;cb=rm*nn-rn*nm
  if 0<tn<td and ca>0 and cb>0:H.append([a,b])
  elif 0<=tn<=td and ca>=0 and cb>=0:WH.append([a,b])
  if tn<=0:level=rad[a]
  elif tn>=td:level=rad[b]
  else:level=(rad[a][0]*dd-wd*wd,D[a]*D[a]*dd)
  assert level[0]>0;events.append((level,a,b))
 def cmpfrac(a,b):return (a[0]*b[1]>b[0]*a[1])-(a[0]*b[1]<b[0]*a[1])
 def cmpevent(a,b):return cmpfrac(a[0],b[0]) or ((a[1:] > b[1:])-(a[1:] < b[1:]))
 par=list(range(len(p)))
 def root(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 P=[]
 for level,a,b in sorted(events,key=cmp_to_key(cmpevent),reverse=True):
  i,j=root(a),root(b)
  if i==j:continue
  cc=cmpfrac(rad[i],rad[j])
  if cc<0 or (cc==0 and i>j):i,j=j,i
  if cmpfrac(rad[j],level)>0:
   num=rad[j][0]*level[1]-level[0]*rad[j][1];den=rad[j][0]*level[1]
   dep=R(num,den);P.append({'root':j,'edge':[a,b],'depth':str(dep),'depth_float':float(dep)})
  par[j]=i
 assert len({root(i) for i in range(len(p))})==1
 P.sort(key=lambda b:R(b['depth']),reverse=True)
 assert len(S)+len(U)-len(H)==2 if not (WS or WU or WH) else True
 report={'name':data['name'],'V':len(p),'E':len(edges),'F':len(faces),'C':2*len(edges),'strict':[len(S),len(U),len(H)],'weak':[len(WS),len(WU),len(WH)],'S':S,'U':U,'H':H,'weak_S':WS,'weak_U':WU,'weak_H':WH,'volume':str(V),'centroid':list(map(str,g)),'center_denominator_bits':K.bit_length(),'vertices_homogeneous':[list(v) for v in vs],'facets':faces,'active_input_planes':active,'stable_input_planes':[active[i] for i in S],'U_incident_input_planes':[[active[k] for k,f in enumerate(faces) if i in f] for i in U],'primal_outgoing_max_indices':pw,'polar_outgoing_max_indices':qw,'boundedness_certificates':bound,'P':P,'Q':[] if len(S)==1 and not WS else None,'Q_evidence':'Exact unique strict polar root and no weak polar root implies no positive finite bar' if len(S)==1 and not WS else 'Not computed here','seconds':time.monotonic()-st}
 print('H_EXACT',data['name'],len(p),len(edges),len(faces),report['strict'],report['weak'],'P',[x['depth_float'] for x in P],'Q',report['Q'],'seconds',report['seconds'],flush=True)
 return report

DATA = {'name': 'J89_C444_G10_MINIMAL76', 'planes': [[-9759740520, 11025398055, -5009610205, 10001651257], [-5122988217, 5868306247, -1003478017, 5000353431], [-9060609931, 10567891131, -6682670930, 10002116173], [-7618365170, 10939708724, -7593920013, 10002115449], [-10387317917, 11875734050, -465983767, 10000233981], [-6056276262, 10743309481, -8895133485, 10002290608], [-10031080302, 11460997439, -3520006337, 10001176878], [-2909201330, -12009987267, -11020368860, 10009500344], [-9477754203, 11715999538, 5660072546, 9998208104], [-9014455998, 11353850975, 7183197252, 9997707632], [-1277969332, 3128033295, 16629522802, 9994599860], [-145583606, 1504690879, 17021738269, 9994507222], [-12490184930, 8798118883, -1014047624, 10001962270], [-7688511915, 9640425245, 10746515869, 9996612134], [-3971703317, 3326599352, 729073945, 3334779054], [-2856469597, -13668445125, -11091172828, 10010021050], [-3339322248, 4489448367, 6030625104, 4998063530], [-5639563179, 8136655314, 13262649952, 9995696040], [-4578764434, 7121304951, 14335874544, 9995323920], [-3497421534, 5941758234, 15266584315, 9995014196], [-4390335731, 10723130771, -9673525264, 10002263245], [-8176893330, 10299008887, 9628222537, 9996951823], [-10064668379, 11750829182, 4136623939, 9998771068], [-1412195669, -7076014817, -5555494239, 5005065848], [-10523648960, 11815665581, 1065916555, 9999789034], [-2868848172, 3627589912, 2812754209, 3332438009], [-2397047868, 4608339970, 16037188934, 9994771243], [-10588551374, 11619255553, 2592036125, 9999352039], [-4571308959, 5045270843, 4100916208, 5001000019], [-1146304563, -13617684260, -11373471513, 10007524373], [-1262643199, 10331500644, -10672947171, 10002113880], [-2630359462, 10533426740, -10315856027, 10002200333], [-1749825805, -13503482600, -11280314418, 10009800135], [-246309594, 10234223004, -10788191296, 10001995549], [798632280, 10134118833, -10804533215, 10001842159], [2050576536, 9890752153, -10789331131, 10001664236], [916909346, -17290236405, -8081160756, 10002037021], [2081011717, -2066457596, 17097465114, 9994590963], [9142201427, 2008598420, 864784230, 10002275794], [9152402582, 934943987, 545588088, 10002605013], [5043119142, 10146303100, -9174482527, 10000634970], [9023277932, -342713569, 72608744, 10002758255], [5705766996, -10375218021, 13605652238, 9996178707], [8814979824, -1246719396, -713970155, 10003338235], [1002111658, -280655948, 17189368722, 9994503089], [7173018927, 5522927380, 2935795328, 10001287392], [4216306511, -6146116095, 16020434894, 9995114511], [7646122315, 4630698264, 2964279419, 10001363297], [8073358867, 4003905570, 2719496458, 10001491606], [4496403810, 12938048195, -2942086891, 10002886203], [8485675907, 3627576623, 2125585279, 10001751197], [4524787307, 1328148551, 595478405, 5001084551], [8879508182, 3287110150, 1434567384, 10002070753], [2734635512, 5461662527, -3891406313, 5000014790], [3974826773, -19197172676, -3805560794, 10003038846], [5038502961, -8275655890, 14987975957, 9995581538], [8648213837, 797245931, -3960292099, 10004109686], [3105042322, -4057841563, 16732507504, 9994799488], [6388772861, -12402121995, 11775305641, 9996903319], [4824321001, 3732030134, -10372553705, 9997577250], [6618207579, -14447490777, 9499237310, 9997842676], [4455652289, 9193505896, -10552637181, 10001285205], [8588769190, 1908774631, -3104934910, 10003710734], [5444701480, -18718267098, 223873333, 10001481832], [5569547075, 11639460993, -6388860021, 10000033667], [7601478185, -227055467, -6454771937, 10005191708], [6511884318, -16183483638, 6936787298, 9998885395], [3182862837, -8944326611, 1551582063, 5000163121], [8749349229, 3873617849, 897038629, 10002178562], [5681053076, 12169166665, -4956967003, 9999140999], [-98487857, -4455227271, -11188097040, 10005312707], [6210051878, 7794473524, 1788331093, 10001802766], [2799038635, 13309847658, -2874720650, 10003092902], [1333856381, -5600706374, -10999762629, 10003629623], [3412664239, 9474414073, -10723317370, 10001474902], [4102303542, 9279753898, -10626837939, 10001356355]], 'source_active_plane_indices': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34, 36, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 80, 81, 82], 'source_input_sha256': '9bf5e64f57837cf16c47947ef856a3c078db7fa73f675ce83a2e7fc2316d70f0'}

if __name__ == '__main__':
 raw=(json.dumps(DATA,sort_keys=True,separators=(',',':'))+'\n').encode()
 assert len(raw)==4065 and hashlib.sha256(raw).hexdigest()=='6c615d3a9729fdcf5986913ee6d9feace2610ffb491207c092a7ce85da1d20d3'
 (ROOT/(DATA['name']+'_H_INPUT.json')).write_bytes(raw)
 result=certify(DATA);result.pop('seconds')
 assert [result['V'],result['E'],result['F']]==[148,222,76]
 assert result['strict']==[1,2,1] and result['weak']==[0,0,0]
 assert len(result['P'])==1 and result['Q']==[]
 raw=(json.dumps(result,sort_keys=True,indent=2)+'\n').encode()
 assert len(raw)==122649 and hashlib.sha256(raw).hexdigest()=='345c782c9ef824eb41d182fcfd919e5079a1763dc0a41af3eb9234760d4a2806'
 (ROOT/(DATA['name']+'_CANONICAL_EXACT.json')).write_bytes(raw)
 print('J89_C444_MINIMAL76_EXACT_OWN121_NOT_110_PASS')
