"""Move a global finite projective/affine proposal into a conditioned full contact atlas."""
from model import *
from global_family import Global
import argparse,copy

def atlas(G):
 X=np.array(G['controls'],float)/G['grid'];X[G['n_supports']]=[0,0,1]
 for i,deps,axes in G['plan']:
  if deps:
   rest=[a for a in range(3) if a not in axes];X[i,axes]=np.linalg.solve(X[np.ix_(deps,axes)],1-X[np.ix_(deps,rest)]@X[i,rest])
 return X

def run(input,row,tag):
 data=json.load(open(input));r=data[row] if row is not None else min((r for r in data if 114 in r['S'] and 82 in r['U']),key=lambda x:x['cost']);z=np.array(r['x']);G,meta=setup();X=atlas(G);n=G['n_supports']
 a=z[5:8];L=np.array([[np.exp(z[0]),z[2],z[3]],[0.,np.exp(z[1]),z[4]],[0.,0.,np.exp(-z[0]-z[1])]])
 apex=L@np.array([0.,0.,1.])/(1+a[2]);en=apex/np.linalg.norm(apex);e=np.eye(3)[np.argmin(abs(en))];e-=en*(e@en);e/=np.linalg.norm(e);f=np.cross(en,e);B=np.stack([e,f,en])/np.linalg.norm(apex);C=B@L
 P=X[n:];Q=X[:n];P=(P/(1+P@a)[:,None])@C.T;Q=np.linalg.solve(C.T,(Q+a).T).T;Y=np.r_[Q,P]
 oldplan=G['plan'];newplan=[]
 for i,deps,axes in oldplan:
  aa=max(itertools.combinations(range(3),len(deps)),key=lambda ax:abs(np.linalg.det(Y[np.ix_(deps,ax)]))) if deps else ()
  newplan.append([i,deps,list(aa)])
 D=10**15;H=copy.deepcopy(G);H['plan']=newplan;H['grid']=D;H['controls']=np.rint(Y*D).astype(np.int64).tolist()
 for i,deps,axes in newplan:
  for ax in axes:H['controls'][i][ax]=0
 H['controls'][n]=[0,0,D]
 par=json.load(open(HERE/'seed/PARENT_A.json'));owners=[[] for p in par['raw_vertices']]
 for f,cy in enumerate(par['faces']):
  for i in cy:owners[i].append(par['active_input_indices'][f])
 meta['triples']=[max(itertools.combinations(ow,3),key=lambda a:abs(np.linalg.det(Q[list(a)]))) for ow in owners]
 new=np.array(json.load(open(HERE/'junction/SELECTORS.json'))['new_raw_points'],float)/1e12
 if len(z)>8:new+=z[8:].reshape(5,3)
 new=(new/(1+new@a)[:,None])@C.T;meta['new_points']=new.tolist();meta['global_row']=r
 # The reference coordinates are not used by own-mass descent; transform for consistency.
 m=np.array([float(QQ) for QQ in map(Qq,[])]) if False else np.array([float(QQ) for QQ in map(__import__('fractions').Fraction,meta['reference'])]);mt=C@m/(1+a@m);meta['reference']=[str(v) for v in mt]
 (HERE/(tag+'_GENERATOR.json')).write_text(json.dumps(H,sort_keys=True,separators=(',',':')));(HERE/(tag+'_META.json')).write_text(json.dumps(meta,sort_keys=True,separators=(',',':')))
 M=Model(H,meta);R=M.evaluate(M.z0);np.save(HERE/(tag+'.npy'),M.z0);print(json.dumps({'chosen':r,'new':M.summary(R),'max_jac':float(np.max(abs(R['dP']))),'new_axes':sum(a[2]!=b[2] for a,b in zip(oldplan,newplan))}),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('tag');p.add_argument('--row',type=int);a=p.parse_args();run(a.input,a.row,a.tag)
