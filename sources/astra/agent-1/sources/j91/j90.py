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
