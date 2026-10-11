import json,numpy as np
from scipy.linalg import svd
from scipy.optimize import linprog
from contact_model import Model
m=Model(json.load(open('next646_A_best.json')),json.load(open('RECHART646/147_150_oldnewlast_0p0/TOP.json')));x=m.x0;G=m.geom(x);v,J,wit=m.witness(G)
print('stat',m.stat(G),'bad',[(i,float(z)) for i,z in enumerate(v) if z<0]);print('minplus',min(v[v>0]));ii=np.argsort(v)[:12];print('low',list(zip(ii.tolist(),v[ii].tolist())))
_,s,vt=svd(G['J'].reshape(-1,m.k),full_matrices=False);print('singular',s[[0,-1]]);W=vt.T/np.maximum(s,1e-6)
bad=v<0;coeff=bad.astype(float);target=np.where(bad,v,np.minimum(.7*v,2e-6));AU=np.column_stack([-J@W,coeff]);BU=v-target
sl=1-G['P']@G['q'].T;vv,ff=np.where(m.mask);sel=np.argsort(sl[vv,ff])[:1200];ii=vv[sel];jj=ff[sel]
sJ=-(np.einsum('ikp,ik->ip',G['PJ'][ii],G['q'][jj])+np.einsum('ikp,ik->ip',G['qJ'][jj],G['P'][ii]));AU=np.vstack([AU,np.column_stack([-sJ@W,np.zeros(len(ii))])]);BU=np.r_[BU,sl[ii,jj]-np.minimum(sl[ii,jj]*.2,1e-6)];scale=np.maximum(np.linalg.norm(AU[:,:-1],axis=1),1e-3);AU/=scale[:,None];BU/=scale
for trust in [.002,1e-4,1e-6]:
 obj=np.zeros(m.k+1);obj[-1]=-1;lim=trust/np.sqrt(m.k);r=linprog(obj,A_ub=AU,b_ub=BU,bounds=[(-lim,lim)]*m.k+[(-1,.1)],method='highs',options={'dual_feasibility_tolerance':1e-8,'primal_feasibility_tolerance':1e-8});print('LP',trust,r.success,r.x[-1]);dx=W@r.x[:-1]
 for al in [1,.25,.01,.0001]:
  Gn=m.geom(x+al*dx,False);vn,_,_=m.witness(Gn);sn=m.stat(Gn);good=~bad;fail=vn[good]-np.minimum(v[good]*.5,1.4e-6);im=vn[bad]-v[bad]
  print(al,'normdx',np.linalg.norm(dx),'sl',sn['slack'],'good',fail.min(),'badim',im.min(),'minv',vn.min(),'linearerror',np.max(np.abs(vn-v-al*(J@dx))))
