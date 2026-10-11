"""Add true polar vertices (physical cutting planes) then release all normals.
Every trial is re-hulled and integrated; <=84 supplied planes implies E<=246.
"""
import sys,json,hashlib,time,numpy as np
from free_support_continuation import ROOT,run,geometry
from support_search import complex_for
from support_persistence import edge_graphs,barcode
from support_forest import points
source=ROOT/sys.argv[1];out=ROOT/sys.argv[2];out.mkdir(exist_ok=False);H=np.load(source);history=[];start=time.time()
for iteration in range(6):
 ds,xm,tr,tm,ym=complex_for(H);X,Q=points(H,ds,tr,tm);eu,es=edge_graphs(ds,xm);pp,pw,pb=barcode(X,xm,eu);kk=int(np.argmax(pb));a,b=X[pp[kk,1:]];d=b-a;t=np.clip(-a@d/(d@d),0,1);death=np.sum((a+t*d)**2);aa=X[eu[:,0]];dd=X[eu[:,1]]-aa;tt=np.clip(-np.sum(aa*dd,1)/np.sum(dd*dd,1),0,1);r2=np.sum((aa+tt[:,None]*dd)**2,1);angle=1-np.sum(Q[es[:,0]]*Q[es[:,1]],1)/(np.linalg.norm(Q[es[:,0]],axis=1)*np.linalg.norm(Q[es[:,1]],axis=1));weights=angle/(.01+abs(r2-death));chosen=np.argsort(-weights);active=np.flatnonzero(ym);count=84-len(active)
 if count<=0:print('SUPPORT_BUDGET_FILLED',len(active),flush=True);break
 chosen=chosen[:count];offset=[.001,.01,.0001,.005][iteration%4];new=(Q[es[chosen,0]]+Q[es[chosen,1]])/2*(1+offset);H=np.vstack([Q[active],new]);src=out/f'round{iteration}_input.npy';np.save(src,H);(out/f'round{iteration}_recipe.json').write_text(json.dumps(dict(parent=str(source),parent_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),principal_death=death,selected_dual_edges=es[chosen].tolist(),offset=offset,active_parent=active.tolist(),Fbefore=len(active),supplied=len(H)),indent=2)+'\n');dest=out/f'round{iteration}';run(src,dest,929840+iteration,jitter=1e-8);H=np.load(dest/'final.npy');info=geometry(H,.00001)[2];row=dict(iteration=iteration,V=info['V'],F=info['F'],E_bound=info['E_bound'],Pmax=info['Pmax'],Qmax=info['Qmax'],source=str(dest/'final.npy'),seconds=time.time()-start);history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n');print('SUPPORT_ENRICHMENT_ENDPOINT',row,flush=True);source=dest/'final.npy'
 if max(info['Pmax'],info['Qmax'])<1e-10:print('POTENTIAL_REQUIRES_EXACT',flush=True);break
