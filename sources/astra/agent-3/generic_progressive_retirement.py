"""Progressive literal point retirement with free physical coordinates.

Higher-complexity intermediates are explicitly numerical unless an exact
checkpoint is present. Every candidate with a possible improved own110 edge
record receives a complete literal-binary64 exact hull and equilibrium audit.
"""
import argparse,json,time,hashlib
from pathlib import Path
import numpy as np
from vertex_geometry import geometry
from direct_face_polish import guards,run as repair
from goal_nomination import preserve

def run(source,out,rounds,attempts):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(source);g=geometry(X,False);X=g['Z'][g['vertices']];X/=max(np.linalg.norm(X,axis=1));np.save(out/'initial.npy',X);(out/'definition.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),sha256=hashlib.sha256(Path(source).read_bytes()).hexdigest(),scope='literal point hulls and actual filled centroids; intermediate census numerical until exact checkpoint',exact_checkpoint_threshold_Ctri=622),indent=2));history=[];start=time.time()
 for stage in range(rounds):
  d=out/f'stage{stage:03d}';d.mkdir();g=geometry(X,False);X=g['Z'][g['vertices']];X/=max(np.linalg.norm(X,axis=1));np.save(d/'parent.npy',X);rows=[]
  for removed in range(len(X)):
   Y=np.delete(X,removed,axis=0)
   try:
    gg=geometry(Y,False);v,_,cc=guards(gg,False);row=dict(removed=removed,merit=float(np.maximum(1e-8-v,0).sum()),minimum=float(min(v)),**cc)
   except(ValueError,np.linalg.LinAlgError)as err:row=dict(removed=removed,error=repr(err),merit=float('inf'))
   rows.append(row)
  (d/'screen.json').write_text(json.dumps(rows,indent=2));eligible=[r for r in rows if 'error'not in r];eligible.sort(key=lambda r:(not(r['S']==r['U']==1),r['merit'],-r['minimum']));accepted=None
  for k,row in enumerate(eligible[:attempts]):
   p=d/f"remove{row['removed']}";p.mkdir();Y=np.delete(X,row['removed'],axis=0);np.save(p/'input.npy',Y);(p/'nomination.json').write_text(json.dumps(row,indent=2));rec=dict(stage=stage,removed=row['removed'],initial=row)
   try:
    if row['S']==row['U']==1:YY=Y;info=row;np.save(p/'numerical_own110.npy',YY)
    else:
     YY,info=repair(p/'input.npy',p/'repair',500,1e-8)
     if YY is None:rec['result']='finite actual-centroid correction failed';(p/'result.json').write_text(json.dumps(rec,indent=2));continue
    gg=geometry(YY,False);vv,_,cc=guards(gg,False);assert cc['S']==cc['U']==1;YY=YY[gg['vertices']];np.save(p/'candidate.npy',YY);ctri=2*(cc['V']+cc['F_triangles']-2);rec.update(result='numerical physical own110 candidate',V=cc['V'],Ctri=ctri,minimum=float(min(vv)),candidate=str((p/'candidate.npy').resolve()))
    if ctri<622:
     exact=p/'exact_checkpoint';preserve(YY,exact,'progressive literal vertex retirement; potential smaller own110 figure');a=json.loads((exact/'nomination.json').read_text());rec['exact']=a
     if a['counts']!=[1,1,0]or a['weak']!=[0,0,0]:rec['result']='numerical own110 rejected by exact audit';(p/'result.json').write_text(json.dumps(rec,indent=2));continue
     rec.update(result='exact own110 weak000 checkpoint',exact_path=str(exact.resolve()))
    (p/'result.json').write_text(json.dumps(rec,indent=2));accepted=(YY,rec);break
   except(ValueError,AssertionError,np.linalg.LinAlgError)as err:rec.update(result='explicit rejected physical candidate',error=repr(err));(p/'result.json').write_text(json.dumps(rec,indent=2))
  if accepted is None:
   r=dict(stage=stage,V=len(X),result='no admitted retirement in finite screened/corrected batch',seconds=time.time()-start);history.append(r);(out/'history.json').write_text(json.dumps(history,indent=2));print('PROGRESSIVE_RETIREMENT_FINITE_STOP',r,flush=True);return
  X,r=accepted;r['seconds']=time.time()-start;history.append(r);np.save(out/'latest.npy',X);(out/'history.json').write_text(json.dumps(history,indent=2));print('PROGRESSIVE_RETIREMENT',r,flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--rounds',type=int,default=110);p.add_argument('--attempts',type=int,default=8);a=p.parse_args();run(a.source,a.out,a.rounds,a.attempts)
