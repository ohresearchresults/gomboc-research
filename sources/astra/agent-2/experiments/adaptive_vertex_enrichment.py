"""Successive finite physical edge-near additions with <=84 submitted points.
No class is assumed during continuation; all small positive bars are retained.
Per-round exact freezing is a separate program. This driver only discovers shapes.
"""
import sys,json,hashlib,time,numpy as np
from scipy.spatial import ConvexHull
from free_vertex_continuation import ROOT,run,evaluate
from support_persistence import barcode
from geometry import mass
source=ROOT/sys.argv[1];out=ROOT/sys.argv[2];out.mkdir(exist_ok=False);current=np.load(source);history=[];start=time.time()
for iteration in range(10):
 hull=ConvexHull(current);X=current[hull.vertices];cent=np.asarray(evaluate(X,.01)[2]['centroid']);X-=cent;X/=np.linalg.norm(X,axis=1).max();h=ConvexHull(X);edges=np.unique(np.sort(np.concatenate([h.simplices[:,[0,1]],h.simplices[:,[1,2]],h.simplices[:,[2,0]]]),axis=1),axis=0);p,w,bars=barcode(X,np.ones(len(X)),edges);kk=int(np.argmax(bars));root=int(p[kk,0]);a,b=X[p[kk,1:]];d=b-a;t=np.clip(-a@d/(d@d),0,1);death=np.sum((a+t*d)**2);mid=(X[edges[:,0]]+X[edges[:,1]])/2;r2=np.sum(mid*mid,1);angle=1-np.sum(X[edges[:,0]]*X[edges[:,1]],axis=1)/(np.linalg.norm(X[edges[:,0]],axis=1)*np.linalg.norm(X[edges[:,1]],axis=1));weights=angle/(.02+abs(r2-death));order=np.argsort(-weights);count=84-len(X)
 if count<=0:print('POINT_BUDGET_FILLED',len(X),flush=True);break
 offset=[.005,.0001,.02,.001][iteration%4];chosen=order[:count];P=np.vstack([X,mid[chosen]*(1+offset)]);src=out/f'round{iteration}_input.npy';np.save(src,P);recipe=dict(parent=str(source),parent_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),root=root,Pdeath=death,chosen_edges=edges[chosen].tolist(),offset=offset,Vbefore=len(X),N=len(P));(out/f'round{iteration}_recipe.json').write_text(json.dumps(recipe,indent=2)+'\n');dest=out/f'round{iteration}';run(src,dest,929000+iteration,0,3500);candidate=np.load(dest/'final.npy');info=evaluate(candidate,.00001)[2];row=dict(iteration=iteration,V=info['V'],Pmax=info['Pmax'],Qmax=info['Qmax'],Pcount=len(info['P']),Qcount=len(info['Q']),source=str(dest/'final.npy'),seconds=time.time()-start);history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n');print('ENRICHMENT_ENDPOINT',row,flush=True)
 if max(info['Pmax'],info['Qmax'])<1e-10:print('POTENTIAL_REQUIRES_EXACT',flush=True);break
 current=candidate;source=dest/'final.npy'
