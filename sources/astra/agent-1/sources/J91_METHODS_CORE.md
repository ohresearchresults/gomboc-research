# J91 numerical methods: core and fixed-cap continuation

Complete source units used for the coordinator's J91 computations. Read with J91_METHODS_OUTER.md, the exact recovery bundle and the complete J90 core in att_eec035833d797b567d6e_01. Numerical reports are nominations: `radial` reports depths greater than1e-14, so absence there is NOT exact absence. Exact own strict/weak claims come only from the rational GMP census. `geometry` supports simple H bodies only; general outer hulls use the explicit maximal-facet builder in the other methods bundle.

Versions: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, PyTorch2.10.0+cpu. Set OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1. All nondefault optimization tolerances, trust steps, constraints and stopping rules are literal in the code. The geometric input is the exact67-row C390 body and exact eight-apex G14 cap file from the J90 core, not an approximate substituted parent. `python capflow91.py 50` performs the fixed eight-cap chart experiment. The preserved endpoint checkpoint contains every binary64 scalar needed for continuation; it does not pretend to include all intermediate apexes.

## File `j90.py`
```python
"""J90 polar bridge / actual-centroid finite support experiment.
Input: exact KF27_NORM_G6 support rows from asg_B9Gl1No1U4tEDt_eCsxtmspZ.
Numerical geometry is nomination, not an exact strict/weak certificate.
"""
import json,math,heapq,sys
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
DATA='''-993833,1254513,683018;-471626,1200365,1003817;-995457,1386643,75843;-933501,1406391,-116805
-847798,1411815,-296888;-742122,1403305,-460930;-1030375,1352642,277140;-1035415,1304898,482603
-820923,1259534,800820;-645520,1241671,907595;-344897,1303538,-835523;-486813,1347984,-731504
-302581,1136731,1088639;-620470,1381663,-606357;-117985,-1029408,-949680;-341519,-1346617,-946031
-845224,-2301513,-904250;586126,630108,-123650;566684,-53179,-821352;845246,316971,-592116
505546,228130,-919679;343159,550457,-1010240;508142,759568,-230147;945099,-314352,-65557
658672,531448,-63675;961302,443358,65115;437146,448117,-978526;920188,21213,-456600
827135,-37656,-576524;835651,697901,68124;177896,1304890,-457704;993635,-166858,-45496
714471,19255,-733103;739028,429443,-29581;1011866,275319,40639;1013711,63223,74117
575369,1096796,-154840;793832,-223483,-467882;852529,699147,-24002;807066,-200402,-439659
424229,-467085,-821695;1014844,-37007,24241;929064,-266318,-225925;1011796,194088,87633
610570,44250,-774933;295755,-1647801,90632;964017,446256,41054;-138005,1046410,1165737
147417,-659636,-919254;308216,996298,-1052245;337770,-436588,-874099;673528,-436709,-605015
544888,-1473565,615887;637761,-299757,-693832;17381,938287,1227361;141417,1089712,-1033406
240411,-1824099,221196;-198021,1249609,-918294;702917,-601833,-488769;669843,-1149804,879205
742618,-595751,1150254;489977,370799,1330298;639149,48887,1290251;565934,205495,1321801
156949,814569,1274930;394626,526624,1326846;282090,678290,1307822;814055,-606715,-189554
814348,-463058,-361503;-28145,1174427,-989123;728719,-865670,1040097;700865,-340107,1234714
509431,-487471,-746902'''
RAW=np.array([list(map(int,s.split(','))) for s in DATA.replace('\n',';').split(';')],dtype=np.int64)
assert RAW.shape==(73,3)

def geometry(y):
    """Simple H geometry; rejects unbounded, nonsimple, duplicated primal vertices."""
    y=np.asarray(y,dtype=np.float64)
    h=ConvexHull(y)
    if np.max(h.equations[:,3])>=0: raise ValueError('unbounded')
    triples=np.sort(h.simplices,axis=1)
    triples=triples[np.lexsort(triples[:,::-1].T)]
    x=np.linalg.solve(y[triples],np.ones((len(triples),3,1)))[:,:,0]
    # Distinct triangles on one plane mean a nonsimple primal vertex: not supported here.
    if len(x)>1:
        dd=np.sum((x[:,None]-x[None,:])**2,axis=2)
        dd+=np.eye(len(x))*1e100
        if dd.min()<1e-25: raise ValueError('nonsimple/duplicate')
    ef={}
    for vi,t in enumerate(triples):
        for a,b in ((t[0],t[1]),(t[1],t[2]),(t[0],t[2])):
            ef.setdefault((int(a),int(b)),[]).append(vi)
    if any(len(z)!=2 for z in ef.values()):raise ValueError('bad incidence')
    ed=np.array(list(ef.values()),int);de=np.array(list(ef),int)
    fs={};tri=[]
    for fi in h.vertices:
        ix=np.where((triples==fi).any(axis=1))[0]
        n=y[fi]/np.linalg.norm(y[fi]);d=x[ix]-x[ix].mean(axis=0)
        u=d[0]/np.linalg.norm(d[0]);v=np.cross(n,u)
        ix=ix[np.argsort(np.arctan2(d@v,d@u))]
        fs[int(fi)]=ix.tolist()
        tri.extend([[int(ix[0]),int(ix[j]),int(ix[j+1])] for j in range(1,len(ix)-1)])
    tri=np.array(tri,int);t=x[tri]
    W=np.einsum('ij,ij->i',t[:,0],np.cross(t[:,1],t[:,2]))
    if W.min()<=0:raise ValueError('orientation')
    vol=W.sum()/6;g=(W[:,None]*t.sum(axis=1)).sum(axis=0)/(4*W.sum())
    p=x-g;q=y/(1-y@g)[:,None]
    return dict(y=y,x=x,p=p,q=q,g=g,vol=vol,triples=triples,edges=ed,dual_edges=de,faces=fs,triangles=tri,active=np.sort(h.vertices))

def radial(x,edges):
    r=np.sum(x*x,axis=1);a=x[edges[:,0]];d=x[edges[:,1]]-a
    den=np.sum(d*d,axis=1)
    if den.min()<=0:raise ValueError('zero edge')
    t=np.clip(-np.sum(a*d,axis=1)/den,0,1);f=a+t[:,None]*d;levels=np.sum(f*f,axis=1)
    par=np.arange(len(x));out=[]
    def root(i):
        while par[i]!=i:par[i]=par[par[i]];i=par[i]
        return i
    for k in np.lexsort((edges[:,1],edges[:,0],-levels)):
        a,b=edges[k];i,j=root(a),root(b)
        if i==j:continue
        if (r[i],-i)<(r[j],-j):i,j=j,i
        dep=1-levels[k]/r[j]
        # Below 1e-14 is not labelled absent; direct-root scores are also returned.
        if dep>1e-14:out.append(dict(depth=float(dep),root=int(j),edge=edges[k].tolist(),birth=float(r[j]),death=float(levels[k])))
        par[j]=i
    return sorted(out,key=lambda v:-v['depth'])

def score(x):
    d=x[None,:,:]-x[:,None,:];den=np.linalg.norm(x,axis=1)[:,None]*np.linalg.norm(d,axis=2)
    np.fill_diagonal(den,1)
    v=np.einsum('ik,ijk->ij',x,d)/den;np.fill_diagonal(v,-np.inf)
    return v

def report(z):
    a=z['active'];P=radial(z['p'],z['edges']);Q=radial(z['q'],z['dual_edges'])
    ps=score(z['p']).max(axis=1);qs=score(z['q'][a]).max(axis=1)
    return dict(V=len(z['x']),E=len(z['edges']),F=len(a),S=a[qs<0].tolist(),U=np.where(ps<0)[0].tolist(),P=P,Q=Q,volume=float(z['vol']),centroid=z['g'].tolist(),sortedPguards=np.sort(ps)[:8].tolist(),sortedQguards=np.sort(qs)[:8].tolist())

def bridge(u,v,links,bend=0.,power=1.,radial_bend=0.):
    a=np.linalg.norm(u);b=np.linalg.norm(v);uu=u/a;vv=v/b
    th=math.acos(np.clip(uu@vv,-1,1));w=np.cross(uu,vv);w/=np.linalg.norm(w)
    t=np.arange(1,links)/links;s=t**power
    dirs=(np.sin((1-s)*th)[:,None]*uu+np.sin(s*th)[:,None]*vv)/math.sin(th)
    dirs+=bend*np.sin(np.pi*s)[:,None]*w;dirs/=np.linalg.norm(dirs,axis=1)[:,None]
    rr=a*np.exp(math.log(b/a)*t+radial_bend*np.sin(np.pi*t))
    new=rr[:,None]*dirs;seq=np.vstack([u,new,v]);guards=np.sum(seq[:-1]*np.diff(seq,axis=0),axis=1)
    return new,dict(theta=th,R=b/a,links=links,bend=bend,power=power,radial_bend=radial_bend,min_chain_guard=float(guards.min()))

def main():
    out=Path(__file__).parent
    z=geometry(RAW/1e6);r=report(z)
    (out/'J90_PARENT_NUMERICAL.json').write_text(json.dumps(r,indent=2)+'\n')
    print('PARENT',json.dumps(r),flush=True)
    # Translate reference so parent uniform centroid is the origin. Drop exact-parent inactive rows.
    y=z['q'][z['active']];ids=z['active'].tolist();i=ids.index(0);j=ids.index(16)
    aa=np.linalg.norm(y[i]);bb=np.linalg.norm(y[j]);th=math.acos(np.clip(y[i]@y[j]/aa/bb,-1,1))
    print('GEOMETRY',aa,bb,th,'links_feasible',[n for n in range(1,21) if th/n<math.pi/2 and bb/aa*math.cos(th/n)**n>1],flush=True)
    table=[];best=None
    for links in [4,6,8,10,12,16,20]:
      for bend in [-1.,-.5,0.,.5,1.]:
       for power in [.7,1.,1.4]:
        for rb in [-.05,0.,.05]:
         new,params=bridge(y[i],y[j],links,bend,power,rb)
         if params['min_chain_guard']<=0:continue
         try:
          q=np.vstack([y,new]);zz=geometry(q);rr=report(zz)
          row=dict(parameters=params,report=rr,delta_centroid=zz['g'].tolist(),referenceS=int(np.sum(score(q).max(1)<0)))
          table.append(row)
          key=(len(rr['S'])+len(rr['U']),sum(b['depth'] for b in rr['P'])+sum(b['depth'] for b in rr['Q']))
          if best is None or key<best[0]:
           best=(key,q,row);print('BEST',key,json.dumps(params),'SU',len(rr['S']),len(rr['U']),'P',[b['depth'] for b in rr['P']],'Q',[b['depth'] for b in rr['Q']],flush=True)
         except (ValueError,np.linalg.LinAlgError):pass
    (out/'J90_BRIDGE_SCAN.json').write_text(json.dumps(table,indent=2)+'\n')
    if best:(out/'J90_BRIDGE_BEST.json').write_text(json.dumps(dict(planes=best[1].tolist(),info=best[2]),indent=2)+'\n')
    print('J90_FINITE_BRIDGE_SCAN',len(table),flush=True)
if __name__=='__main__':main()
```

## File `masscaps90.py`
```python
"""Mass-balanced finite outward pyramids on fixed maximal facets.
Analytic incremental moments nominate the added apex heights. Actual closed
boundary, support inequalities, uniform mass, and full numerical root/bar census
are rebuilt. No small-bar cutoff is an exact weak-equilibrium certificate.
"""
import json,sys,itertools
from pathlib import Path
import numpy as np
from scipy.optimize import linprog,root
from j90 import geometry,report,score
ROOT=Path(__file__).parent

def poly(points,faces):
 x=np.array(points);faces=[list(c) for c in faces];ys=[];tris=[];ed={}
 for fi,cy in enumerate(faces):
  a,b,c=x[cy[:3]];n=np.cross(b-a,c-a);h=n@a
  if h<0:cy=list(reversed(cy));a,b,c=x[cy[:3]];n=np.cross(b-a,c-a);h=n@a
  assert h>0
  ys.append(n/h)
  for a,b in zip(cy,cy[1:]+cy[:1]):ed.setdefault(tuple(sorted([a,b])),[]).append(fi)
  tris.extend([[cy[0],cy[j],cy[j+1]] for j in range(1,len(cy)-1)])
 y=np.array(ys)
 if np.max(x@y.T-1)>1e-8:raise ValueError('combined pyramids are not convex')
 assert all(len(v)==2 for v in ed.values());assert len(x)-len(ed)+len(faces)==2
 t=x[np.array(tris)];D=np.einsum('ij,ij->i',t[:,0],np.cross(t[:,1],t[:,2]));assert D.min()>0;vol=D.sum()/6;g=(D[:,None]*t.sum(1)).sum(0)/(4*D.sum())
 return dict(x=x,p=x-g,y=y,q=y/(1-y@g)[:,None],vol=vol,g=g,edges=np.array(list(ed)),dual_edges=np.array(list(ed.values())),faces={i:c for i,c in enumerate(faces)},active=np.arange(len(faces)))

def face_data(z,fi):
 cy=z['faces'][fi];x=z['x'][cy];t=np.array([[x[0],x[j],x[j+1]] for j in range(1,len(x)-1)]);a=np.linalg.norm(np.cross(t[:,1]-t[:,0],t[:,2]-t[:,0]),axis=1)/2;cf=(a[:,None]*t.mean(1)).sum(0)/a.sum();n=z['y'][fi]/np.linalg.norm(z['y'][fi]);return cf,n,float(a.sum())

def add_caps(z,apexes):
 x=z['x'].tolist();faces=[]
 for fi,cy in z['faces'].items():
  if fi not in apexes:faces.append(cy);continue
  w=apexes[fi];ix=len(x);x.append(w.tolist())
  for a,b in zip(cy,cy[1:]+cy[:1]):faces.append([a,b,ix])
 return poly(x,faces)

def reference(z):
 zz=z.copy();zz['p']=z['x'];zz['q']=z['y'];zz['g']=np.zeros(3);return report(zz)

def balanced(z,si,w,tag):
 cf,n,A=face_data(z,si);height=(w-cf)@n;assert height>0
 moment=A*height*(3*cf+w)/12
 U=report(z)['U'][0];S=report(z)['S'];choices=[]
 for fi,cy in z['faces'].items():
  if fi==si or fi in S or U in cy:continue
  c,v,a=face_data(z,fi);slack=1-z['y']@c;den=z['y']@v;ix=[j for j in range(len(den)) if j!=fi and den[j]>0];cap=min(slack[ix]/den[ix])
  if cap<=1e-10:continue
  choices.append((fi,c,v,a,cap*.8,len(cy)))
 # Each unknown is cap volume, so first derivative of moment is base centroid.
 C=np.array([x[1] for x in choices]).T;cost=np.array([x[-1] for x in choices],float)
 bounds=[(0,a*cap/3) for _,c,n,a,cap,k in choices]
 op=linprog(cost,A_eq=C,b_eq=-moment,bounds=bounds,method='highs')
 if not op.success:return None,dict(reason='linear moment capacity infeasible')
 selected=np.where(op.x>1e-12)[0]
 if sum(choices[i][-1] for i in selected)+len(z['edges'])+len(z['faces'][si])>249:return None,dict(reason='true-edge budget',selected=[choices[i][0] for i in selected])
 # Exact quadratic pyramid moment, solved numerically here, then rebuilt.
 def eq(v):
  total=moment.copy()
  for j,i in enumerate(selected):
   _,c,n,a,cap,k=choices[i];h=3*v[j]/a;total+=v[j]*(c+h*n/4)
  return total
 initial=op.x[selected]
 if len(selected)==3:sol=root(eq,initial,tol=1e-12);vv=sol.x
 else:
  from scipy.optimize import least_squares
  scale=max(float(np.linalg.norm(moment)),float(np.max(initial)));sol=least_squares(lambda v:eq(v*scale)/scale,initial/scale,bounds=(np.zeros(len(selected)),np.array([bounds[i][1] for i in selected])/scale),gtol=1e-13,xtol=1e-13,ftol=1e-13,max_nfev=500);vv=sol.x*scale
 if np.max(abs(eq(vv)))>1e-11 or min(vv)<=0:return None,dict(reason='quadratic moments not closed',residual=eq(vv).tolist(),volumes=vv.tolist())
 ap={si:w};extra=[]
 for v,i in zip(vv,selected):
  fi,c,n,a,cap,k=choices[i];h=3*v/a
  if h>cap:return None,dict(reason='height capacity',fi=fi)
  ap[fi]=c+h*n;extra.append(dict(face=fi,height=float(h),volume=float(v),apex=ap[fi].tolist()))
 try:zz=add_caps(z,ap)
 except Exception as e:return None,dict(reason=str(e))
 return zz,dict(primary_face=si,primary_apex=w.tolist(),primary_volume=float(A*height/3),compensators=extra,residual=eq(vv).tolist(),source=tag)

def main(src,tag='MASSCAP'):
 y=np.array(json.loads(Path(src).read_text())['planes']);z=geometry(y);z=geometry(z['q'][z['active']]);r=report(z);si=r['Q'][0]['root'];f=z['y'][si]/sum(z['y'][si]**2);table=[];best=None
 for ci in z['faces'][si]:
  for lam in [.15,.35,.65]:
   for beta in [.001,.003,.006]:
    w=(1-lam)*f+lam*z['x'][ci]+beta*f
    if np.max(np.delete(z['y']@w,si))>=1:continue
    try:single=add_caps(z,{si:w});ref=reference(single)
    except Exception:continue
    if len(ref['U'])!=1 or len(ref['S'])>2:continue
    zz,meta=balanced(z,si,w,src);rec=dict(corner=ci,lam=lam,beta=beta,reference=ref,balance=meta)
    if zz is not None:
     rr=report(zz);rec['report']=rr;key=(len(rr['S'])+len(rr['U']),sum(b['depth'] for b in rr['P'])+sum(b['depth'] for b in rr['Q']))
     if best is None or key<best[0]:
      best=(key,zz,rec);print('BEST',ci,lam,beta,'VEF',rr['V'],rr['E'],rr['F'],'SU',len(rr['S']),len(rr['U']),'Q',[b['depth'] for b in rr['Q']],'g',rr['centroid'],flush=True)
      (ROOT/f'J90_{tag}_BEST.json').write_text(json.dumps(dict(planes=zz['y'].tolist(),points=zz['x'].tolist(),faces=zz['faces'],info=rec),indent=2)+'\n')
    table.append(rec)
 (ROOT/f'J90_{tag}_SCAN.json').write_text(json.dumps(dict(original_planes=z['y'].tolist(),source=src,results=table),separators=(',',':'))+'\n')
 print('MASSCAP_FINISHED',len(table),'success',sum('report'in t for t in table),'failures',[t['balance'].get('reason') for t in table if 'report'not in t],flush=True)
if __name__=='__main__':main(sys.argv[1],sys.argv[2] if len(sys.argv)>2 else 'MASSCAP_E')
```

## File `capflow91.py`
```python
"""J91 finite mass-balanced U-safe cap chart, dynamic polar witness policies.
Numerical nomination: every accepted step is a genuinely convex old-facet cap
complex, has reintegrated own centroid, full root census and all positive bars.
A 1e-14 floating bar nomination floor is not an exact zero certificate.
"""
from pathlib import Path
import json,sys
from fractions import Fraction
import numpy as np,torch
from scipy.optimize import linprog,minimize
from j90 import geometry,report,score,radial
from masscaps90 import face_data,add_caps
ROOT=Path(__file__).resolve().parent
torch.set_default_dtype(torch.float64);torch.set_num_threads(1)

def setup(source=None):
 y=np.loadtxt(ROOT/'J90_DETACHED_C390_G8.txt',skiprows=1)/1e8;raw=geometry(y);g=raw['g'];z=geometry(raw['q']);ids=[6,14,16,19,39,41,43,65]
 cap=json.loads((ROOT/'J90_BALANCED_C452_G14_CAPS.json').read_text())['apexes'];W=np.array([[float(Fraction(s)) for s in cap[str(i)]] for i in ids])-g
 if source is not None:W=np.array(json.loads(Path(source).read_text())['apexes'])
 centres=[];normals=[];areas=[];qrows=[];fi_owner=[];ca=[];cb=[]
 for j,i in enumerate(ids):
  c,n,a=face_data(z,i);centres.append(c);normals.append(n);areas.append(a)
 for fi,cy in z['faces'].items():
  if fi not in ids:
   qrows.append(z['y'][fi]);fi_owner.append(-1);ca.append([0,0,0]);cb.append([0,0,0])
  else:
   j=ids.index(fi)
   for a,b in zip(cy,cy[1:]+cy[:1]):
    qrows.append([0,0,0]);fi_owner.append(j);ca.append(z['x'][a]);cb.append(z['x'][b])
 model=dict(z=z,g=g,ids=ids,W=W,c=np.array(centres),n=np.array(normals),a=np.array(areas),q0=np.array(qrows),owner=np.array(fi_owner),ca=np.array(ca),cb=np.array(cb))
 return model

def run(steps=60,source=None,tag='J91_CAPFLOW'):
 m=setup(source);z=m['z'];ids=m['ids'];W=m['W'];C=torch.tensor(m['c']);N=torch.tensor(m['n']);areas=torch.tensor(m['a']);Y=torch.tensor(z['y']);old=torch.tensor(z['x']);own=m['owner'];moving=np.where(own>=0)[0];Q0=torch.tensor(m['q0']);A=torch.tensor(m['ca'][moving]);B=torch.tensor(m['cb'][moving]);O=torch.tensor(own[moving]);h0=np.sum((W-m['c'])*m['n'],axis=1)
 activepairs=[(j,fi) for j,i in enumerate(ids) for fi in range(len(z['y'])) if fi!=i];jj=torch.tensor([j for j,i in activepairs]);ff=torch.tensor([i for j,i in activepairs]);hist=[];trust=.02
 def fields(w):
  n=torch.linalg.cross(B-A,w[O]-A);h=(n*A).sum(1);q=Q0.clone();q[moving]=n/h[:,None]
  height=((w-C)*N).sum(1);vol=areas*height/3;mom=(vol[:,None]*(3*C+w)/4).sum(0)
  return q,height,mom,vol
 def owncheck(w):
  zz=add_caps(z,{i:w[j] for j,i in enumerate(ids)});return zz,report(zz)
 for k in range(steps):
  zz,rr=owncheck(W);q=zz['q'];main=rr['Q'][0] if rr['Q'] else None
  if main is None:print('REFERENCE_Q_ABSENT',rr,flush=True);break
  peak=main['root'];ea,eb=main['edge'];elder=int(np.argmax(np.sum(q*q,axis=1)));Sroot=set([peak,elder]);qi=np.array([i for i in range(len(q)) if i not in Sroot]);qj=score(q).argmax(1)[qi]
  wi=np.argmax(np.einsum('ik,ijk->ij',W,z['x'][None]-W[:,None]),axis=1)
  def fun(w):
   q,h,mom,v=fields(w)
   # chart constraints and sufficient inherited-old-point U-safe witnesses
   parent=1-(Y[ff]*w[jj]).sum(1)
   mutual=(1-q[moving]@w.T).flatten()
   us=(w*(old[wi]-w)).sum(1)
   dq=q[qj]-q[qi];qc=(q[qi]*dq).sum(1)/(torch.linalg.vector_norm(q[qi],dim=1)*torch.linalg.vector_norm(dq,dim=1))
   d=q[eb]-q[ea];t=torch.clamp(-(q[ea]*d).sum()/(d*d).sum(),0,1);f=q[ea]+t*d;loss=1-(f*f).sum()/(q[peak]*q[peak]).sum()
   return torch.cat([h,parent,mutual,us,qc,mom,loss[None]])
  tW=torch.tensor(W);vals=fun(tW).numpy();J=torch.func.jacrev(fun,chunk_size=64)(tW).numpy().reshape(len(vals),-1)
  nc=len(vals)-4;v=vals[:nc];G=J[:nc];MG=J[nc:nc+3];grad=J[-1]
  target=np.minimum(v,np.full(nc,1e-8));target[:len(W)]=np.minimum(v[:len(W)],1e-7)
  # Exact-incidence rows (each apex lies on its own fan) have zero Jacobian.
  nr=np.linalg.norm(G,axis=1);keep=nr>1e-9;scale=np.maximum(nr[keep],1e-8);GG=G[keep]/scale[:,None];rhs=(target-v)[keep]/scale
  ms=np.maximum(np.linalg.norm(MG,axis=1),1e-6);EE=MG/ms[:,None];ee=-vals[nc:nc+3]/ms
  op=linprog(grad,A_ub=-GG,b_ub=-rhs,A_eq=EE,b_eq=ee,bounds=[(-trust,trust)]*W.size,method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
  rec=dict(k=k,old=float(vals[-1]),trust=trust,lp=op.success,accepted=False)
  if op.success and grad@op.x<-1e-12:
   L=np.vstack([GG,-grad]);lb=np.r_[rhs,-.7*grad@op.x]
   fit=minimize(lambda d:(.5*d@d,d),op.x,jac=True,method='SLSQP',bounds=[(-trust,trust)]*W.size,constraints=[{'type':'ineq','fun':lambda d:L@d-lb,'jac':lambda d:L},{'type':'eq','fun':lambda d:EE@d-ee,'jac':lambda d:EE}],options={'maxiter':150,'ftol':1e-17})
   delta=fit.x if min(L@fit.x-lb)>-1e-8 and max(abs(EE@fit.x-ee))<1e-9 else op.x
   delta=delta.reshape(W.shape)
   for bt in range(20):
    w=W+delta*2**-bt
    # Finite actual moment correction by minimum-norm Newton, not tangent alone.
    for correction in range(8):
     wt=torch.tensor(w);mom=fields(wt)[2].numpy()
     if max(abs(mom))<1e-15:break
     MJ=torch.func.jacrev(lambda a:fields(a)[2])(wt).numpy().reshape(3,-1)
     dw=np.linalg.lstsq(MJ,-mom,rcond=None)[0];w+=dw.reshape(w.shape)
    vv=fun(torch.tensor(w)).numpy();
    if np.min(vv[:nc]-target)<-1e-9 or np.max(abs(vv[nc:nc+3]))>1e-13:continue
    try:zzz,r=owncheck(w)
    except Exception:continue
    loss=r['Q'][0]['depth'] if r['Q'] else 0.
    if len(r['S'])>2 or len(r['U'])!=1 or r['P'] or loss>=rec['old']-1e-12:continue
    W=w;rec.update(accepted=True,alpha=2**-bt,new=loss,report=r,moment=vv[nc:nc+3].tolist(),min_U_guard=float(vv[-4-len(qi)-len(W):-4-len(qi)].min()));break
  hist.append(rec);print(tag,json.dumps(rec),flush=True)
  (ROOT/(tag+'.json')).write_text(json.dumps(dict(base='J90_DETACHED_C390_G8',frame_shift=m['g'].tolist(),cap_ids=ids,apexes=W.tolist(),history=hist,report=owncheck(W)[1]),indent=2)+'\n')
  if rec['accepted']:
   if rec['alpha']>=.5:trust=min(.05,trust*1.25)
  else:trust*=.5
  if trust<1e-7:break
 print('J91_FIXED_CAP_CHART_NUMERICAL_ONLY',flush=True)
if __name__=='__main__':run(int(sys.argv[1]) if len(sys.argv)>1 else 60,sys.argv[2] if len(sys.argv)>2 else None,sys.argv[3] if len(sys.argv)>3 else 'J91_CAPFLOW')
```

