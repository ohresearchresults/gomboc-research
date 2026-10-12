"""Literal graph coarsening followed by physical own110 realization.

An edge is actually removed from the new incidence graph. Degree-two vertices
and digon faces are removed before reconstruction. Geometric closeness ranks
proposals only; exact contact reconstruction and native hull audit decide the
real vertices, maximal facets, mass and equilibrium census of every survivor.
"""
import argparse,json,time,hashlib,importlib.util
from pathlib import Path
import numpy as np
from gmpy2 import mpq
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
from contact_numpy import Chart
from contact_quota_polish import metric,guards
from exact_contact_audit import audit
from exact_barcode_report import report

def load(source):
 a=json.loads((Path(source)/'audit.json').read_text());cc=list(map(mpq,a['raw_centroid']));X=np.array([[float(mpq(v)-cc[k])for k,v in enumerate(x)]for x in a['raw_vertices']]);s=float(max(np.linalg.norm(X,axis=1)));X/=s;Y=[]
 for n,h in zip(a['normals'],a['offsets']):
  nn=list(map(mpq,n));hh=mpq(h)-sum(u*v for u,v in zip(nn,cc));Y.append([float(v/hh)*s for v in nn])
 return a,X,np.array(Y)

def normalize(fc,X,Y):
 fc=[list(c)for c in fc];Y=list(Y)
 for iteration in range(len(X)+len(fc)):
  changed=False;rows=[];norm=[];seen=set()
  for cy,y in zip(fc,Y):
   cc=[]
   for i in cy:
    if not cc or cc[-1]!=i:cc.append(i)
   if len(cc)>1 and cc[0]==cc[-1]:cc.pop()
   if len(cc)<3:changed=True;continue
   assert len(set(cc))==len(cc),'non-simple proposed boundary'
   key=tuple(sorted(cc))
   if key in seen:changed=True;continue
   seen.add(key);rows.append(cc);norm.append(y)
  fc,Y=rows,norm;degree=np.zeros(len(X),int)
  for cy in fc:degree[cy]+=1
  delete={int(i)for i in np.flatnonzero((degree>0)&(degree<3))}
  if delete:fc=[[i for i in cy if i not in delete]for cy in fc];changed=True
  if not changed:break
 else:raise ValueError('topological cleanup failed to terminate')
 active=sorted({i for cy in fc for i in cy});mapping={i:j for j,i in enumerate(active)};fc=[[mapping[i]for i in cy]for cy in fc];owners={}
 for f,cy in enumerate(fc):
  for i,j in zip(cy,cy[1:]+cy[:1]):owners.setdefault(tuple(sorted((i,j))),[]).append(f)
 assert all(len(v)==2 for v in owners.values()),'nonmanifold proposal';assert len(active)-len(owners)+len(fc)==2,'Euler failure'
 return fc,X[active],np.array(Y),active,list(owners)

def proposals(a,X,Y,number):
 faces=a['faces'];owners={tuple(e):[]for e in a['edges']}
 for f,cy in enumerate(faces):
  for i,j in zip(cy,cy[1:]+cy[:1]):owners[tuple(sorted((i,j)))].append(f)
 edges=np.array(list(owners));dual=np.array(list(owners.values()));pdist=np.linalg.norm(X[edges[:,0]]-X[edges[:,1]],axis=1)/np.sqrt(np.mean(X*X));qdist=np.linalg.norm(Y[dual[:,0]]-Y[dual[:,1]],axis=1)/np.sqrt(np.mean(Y*Y));ans=[]
 for kind,length,pairs in [('facet_union',qdist,dual),('vertex_union',pdist,edges)]:
  for k in np.argsort(length)[:number]:
   i,j=map(int,pairs[k]);XX=X.copy()
   if kind=='facet_union':
    both=set(zip(faces[i],faces[i][1:]+faces[i][:1]))|set(zip(faces[j],faces[j][1:]+faces[j][:1]));boundary=[(u,v)for u,v in both if (v,u)not in both];nxt=dict(boundary);assert len(nxt)==len(boundary);cy=[min(nxt)]
    while nxt[cy[-1]]!=cy[0]:
     z=nxt[cy[-1]];assert z not in cy;cy.append(z)
    assert len(cy)==len(boundary);fc=[cy0 for f,cy0 in enumerate(faces)if f not in [i,j]]+[cy];yy=np.linalg.lstsq(X[cy],np.ones(len(cy)),rcond=None)[0];YY=np.vstack(([y for f,y in enumerate(Y)if f not in [i,j]],yy))
   else:
    fc=[[i if v==j else v for v in cy]for cy in faces];XX[i]=(X[i]+X[j])/2;YY=Y.copy()
   try:fc,xx,yy,active,ee=normalize(fc,XX,YY)
   except (ValueError,AssertionError):continue
   ans.append(dict(kind=kind,pair=[i,j],length=float(length[k]),faces=fc,X=xx,Y=yy,active=active,edges=ee,E=len(ee),gain=a['E']-len(ee)))
 return sorted(ans,key=lambda r:(r['length']/max(r['gain'],1),r['kind'],r['pair']))

def realize(c,out,steps,eps,gapfloor=1e-10):
 out=Path(out);out.mkdir(exist_ok=False,parents=True);q=c.q0.copy();hist=[];trust=.04;start=time.time()
 for it in range(steps):
  g=c.physical(q,require_valid=False);v,J,cl=guards(c,g,1,1);gap=g['noncontact'];values=np.r_[gap,v];targets=np.r_[np.full(len(gap),gapfloor),np.full(len(v),eps)];merit=float(np.maximum(targets-values,0).sum());row=dict(it=it,S=cl[1],U=cl[0],valid=bool(g['valid']),minimum=float(min(v)),gap=float(min(gap)),turn=g['min_turn'],merit=merit,trust=trust,seconds=time.time()-start);hist.append(row);np.save(out/'latest_q.npy',q);(out/'trace.json').write_text(json.dumps(hist,indent=2))
  if it%10==0:print('STRICT110_COARSEN_REALIZE',out,row,flush=True)
  if g['valid']and cl==[1,1]and 34<=2*c.meta['E']<500 and c.V+c.meta['E']+c.F<500:
   from goal_nomination import ExactGoalCandidateFound
   p=out/f'goal_nomination_it{it}';p.mkdir();np.save(p/'literal_free_controls.npy',q);grid=max(float(z).as_integer_ratio()[1]for z in q);aa=audit(c.path,p/'literal_free_controls.npy',p/'exact_dyadic_controls',grid);report(p/'exact_dyadic_controls')
   if aa['counts']==[1,1,0]and aa['weak']==[0,0,0]:raise ExactGoalCandidateFound('Exact coarsened Figure preserved at '+str(p))
  if g['valid']and cl==[1,1]and min(v)>eps*.85:
   np.save(out/'success_q.npy',q);return q
  W=metric(c,g);d=c.d;JJ=np.vstack((g['Dgap'][~c.incidence],J))@W;bound=trust/np.sqrt(d);keep=values-targets<=bound*np.sum(abs(JJ),axis=1)+1e-9;JJ=JJ[keep];vv=values[keep];tt=targets[keep];m=len(vv);I=eye(d);O=csr_matrix((d,m));sc=.001;A=vstack([hstack([-csr_matrix(JJ/sc),-eye(m),csr_matrix((m,d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr');b=np.r_[(vv-tt)/sc,np.zeros(2*d)];r=linprog(np.r_[np.zeros(d),np.ones(m),np.full(d,1e-5)],A_ub=A,b_ub=b,bounds=[(-bound,bound)]*d+[(0,None)]*(m+d),method='highs',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-10,time_limit=20.))
  if not r.success:row['error']=r.message;trust*=.4
  else:
   dq=W@r.x[:d];ok=False
   for k in range(14):
    qq=q+2.**-k*dq
    try:gg=c.physical(qq,require_valid=False);vv,_,cc=guards(c,gg,1,1);mm=float(np.maximum(targets-np.r_[gg['noncontact'],vv],0).sum())
    except(ValueError,np.linalg.LinAlgError):continue
    if np.isfinite(mm)and mm<merit-max(1e-13,merit*1e-7):q=qq;ok=True;row['alpha']=2.**-k;break
   if ok and k==0:trust=min(.3,trust*1.3)
   if not ok:trust*=.4
  if trust<1e-10:break
 return None

def batch(source,out,number,steps):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);source=Path(source);a,X,Y=load(source);assert a['counts']==[1,1,0]and a['weak']==[0,0,0];props=proposals(a,X,Y,number);spec=importlib.util.spec_from_file_location('pinned_coarsening_peel','sources/peer_balanced_contact/make_contact_atlas.py');peel=importlib.util.module_from_spec(spec);spec.loader.exec_module(peel);records=[]
 for k,p in enumerate(props):
  d=out/f"case{k:03d}_{p['kind']}";d.mkdir();row={key:p[key]for key in ['kind','pair','length','gain']};row['case']=k;proposal=dict(V=len(p['X']),F=len(p['Y']),E=p['E'],faces=p['faces'],edges=p['edges'],raw_vertices=p['X'].tolist(),raw_halfspaces=[list(v)+[1.]for v in p['Y']],active=list(range(len(p['Y']))),retained_original_vertices=p['active'],source=str(source.resolve()),source_audit_sha256=hashlib.sha256((source/'audit.json').read_bytes()).hexdigest(),operation=row,scope='unverified topology and coordinates; actual convex realization and exact audit required');(d/'proposal.json').write_text(json.dumps(proposal,indent=2))
  try:
   meta,q,*_=peel.make(d/'proposal.json',d/'peeling',balanced=True)
   for plan in meta['plan']:plan['fixed']={}
   grid=10**16;meta.update(free_controls=[int(round(v*grid))for v in q],grid=grid,proposal=str((d/'proposal.json').resolve()));(d/'construction.json').write_text(json.dumps(meta,indent=2));c=Chart(d/'construction.json');q=realize(c,d/'realize',steps,1e-8)
   if q is None:row['result']='finite own110 realization failed'
   else:
    aa=audit(d/'construction.json',d/'realize/success_q.npy',d/'exact_g15',10**15);report(d/'exact_g15');row.update(result='new exact physical body',V=aa['V'],E=aa['E'],F=aa['F'],counts=aa['counts'],weak=aa['weak'],exact=str((d/'exact_g15').resolve()))
    if aa['counts']==[1,1,0]and aa['weak']==[0,0,0]:
     (out/'accepted.json').write_text(json.dumps(row,indent=2));records.append(row);(out/'results.json').write_text(json.dumps(records,indent=2));print('EXACT_STRICT110_COARSENED',row,flush=True);return row
  except(ValueError,AssertionError,np.linalg.LinAlgError)as err:row.update(result='explicit rejected proposal',error=repr(err))
  records.append(row);(out/'results.json').write_text(json.dumps(records,indent=2));print('STRICT110_COARSEN_CASE',row,flush=True)
 return None

def run(source,out,rounds,number,steps):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);records=[]
 for k in range(rounds):
  r=batch(source,out/f'round{k:02d}',number,steps)
  if r is None:break
  source=r['exact'];records.append(r);(out/'history.json').write_text(json.dumps(records,indent=2))
  if 34<=2*r['E']<500 and r['V']+r['E']+r['F']<500:
   from goal_nomination import ExactGoalCandidateFound
   raise ExactGoalCandidateFound('Exact own110 coarsened Figure at '+source)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--rounds',type=int,default=32);p.add_argument('--number',type=int,default=14);p.add_argument('--steps',type=int,default=90);a=p.parse_args();run(a.source,a.out,a.rounds,a.number,a.steps)
