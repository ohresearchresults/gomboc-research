"""Four literal added points, with three cap heights closing uniform mass.

One prescribed cap targets the junior stable basin. Three compensation caps
are chosen from strict nonstable old facets. Each new point has a positive
reference escape chord to an old point. All mass and signs are recomputed on
the actual combined convex hull. Local pyramid moments only seed the solve.
"""
import argparse,json,time,itertools
from pathlib import Path
import numpy as np
from vertex_geometry import geometry
from persistence_birth import evaluate,bars_loss
from support_geometry import escape
from exact_audit_vertices import audit
from exact_barcode_report import report

def run(scout,out,number):
    scout=Path(scout);out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(scout/'centered_seed.npy');assert len(X)+4<=84;g=geometry(X,False);T=g['T'];H=g['H'];n=H/np.linalg.norm(H,axis=1)[:,None];cent=X[T].mean(1);h=np.einsum('fc,fc->f',n,X[T[:,0]]);area=np.linalg.norm(np.cross(X[T[:,1]]-X[T[:,0]],X[T[:,2]]-X[T[:,0]]),axis=1)/2;vmax=escape(H,angular=True)[0];candidates=[]
    for f in range(len(T)):
        if vmax[f]<=1e-5:continue
        c=cent[f];normal=n[f];gap=h-n@c;cos=n@normal;sel=(cos>0)&(np.arange(len(T))!=f);maximum=float(min(gap[sel]/cos[sel]))*.8
        f0=X@c-c@c;beta=X@normal-2*(c@normal);disc=beta*beta+4*f0;root=np.where((disc>0)&(f0>0),(beta+np.sqrt(np.maximum(disc,0)))/2,-np.inf);parent=int(root.argmax());maximum=min(maximum,float(root[parent])*.9)
        if maximum<=1e-6:continue
        candidates.append(dict(facet=f,parent=parent,maximum=maximum,capacity=float(area[f]*maximum/3),guard=float(vmax[f])))
    candidates=sorted(candidates,key=lambda c:c['capacity'],reverse=True)[:48];assert len(candidates)>=3
    ids=np.array([r['facet']for r in candidates]);M=(area[ids]/3)[:,None]*cent[ids];triples=np.array(list(itertools.combinations(range(len(ids)),3)));mat=np.transpose(M[triples],(0,2,1));det=np.linalg.det(mat);keep=abs(det)>1e-15;triples=triples[keep];inv=np.linalg.inv(mat[keep]);limits=np.array([r['maximum']for r in candidates]);source_rows=json.loads((scout/'screen.json').read_text());selected=[]
    for row in sorted(source_rows,key=lambda r:r['reference_Q'])[:number//2]+sorted((r for r in source_rows if r['reference_S']==2),key=lambda r:r['Q'])[:number//2]:
        if row['it']not in [r['it']for r in selected]:selected.append(row)
    (out/'definition.json').write_text(json.dumps(dict(source_scout=str(scout.resolve()),compensation_facets=candidates,triple_count=len(triples),maximum_vertices=len(X)+4,formula='convex hull(source points, prescribed point, and three facet_centroid + height * unit_normal points); actual filled-volume centroid solved by Newton',scope='a numerical construction proposal until complete exact audit'),indent=2));np.save(out/'source.npy',X);records=[];start=time.time()
    for order,row in enumerate(selected):
        primary=np.array(row['point']);base=np.vstack((X,primary));gg=geometry(base,False);moment=gg['g']*gg['V'];delta=-np.einsum('tij,j->ti',inv,moment);admitted=np.all((delta>1e-10)&(delta<limits[triples]),axis=1);indices=np.flatnonzero(admitted);best=None;record=dict(order=order,source_case=row['it'],primary=row,linear_feasible_triples=len(indices))
        if len(indices):
            objective=np.sum(delta[indices]/limits[triples[indices]],axis=1);indices=indices[np.argsort(objective)[:5]]
            for tr in indices:
                cc=triples[tr];ff=ids[cc];dd=delta[tr].copy();ok=False
                for iteration in range(14):
                    Y=np.vstack((base,cent[ff]+dd[:,None]*n[ff]));gy=geometry(Y);norm=np.linalg.norm(gy['g']);ref=escape(Y)[0]
                    if np.sum(ref<0)!=1:break
                    if norm<1e-13:ok=True;break
                    J=np.column_stack([gy['Dg'][:,3*(len(base)+j):3*(len(base)+j)+3]@n[ff[j]]for j in range(3)])
                    try:step=-np.linalg.solve(J,gy['g'])
                    except np.linalg.LinAlgError:break
                    good=False
                    for k in range(14):
                        ds=dd+2.**-k*step
                        if min(ds)<=0 or np.any(ds>=limits[cc]):continue
                        yy=np.vstack((base,cent[ff]+ds[:,None]*n[ff]));fy=geometry(yy,False)
                        if np.sum(escape(yy)[0]<0)==1 and np.linalg.norm(fy['g'])<norm*(1-1e-5):dd=ds;good=True;break
                    if not good:break
                if not ok:continue
                loss,_,inf=evaluate(Y,.03);sy=int(np.sum(escape(gy['H'])[0]<0));uy=int(np.sum(escape(gy['Z'])[0]<0));candidate=dict(compensation_facets=ff.tolist(),compensation_heights=dd.tolist(),S=sy,U=uy,P=inf['Pmax'],Q=inf['Qmax'],Q_bars=inf['Q'],loss=loss,mass_norm=float(norm),V=len(gy['vertices']),volume=float(gy['V']))
                if best is None or candidate['loss']<best[0]['loss']:best=(candidate,Y.copy())
                if sy==uy==1:break
        if best:
            candidate,Y=best;d=out/f"case{row['it']}";d.mkdir();np.save(d/'points.npy',Y);(d/'construction.json').write_text(json.dumps(dict(source=str((out/'source.npy').resolve()),primary=primary.tolist(),**candidate),indent=2));record.update(result='uniform centroid closure numerical',candidate=candidate,evidence=str(d))
            if candidate['S']==candidate['U']==1:
                a=audit(d/'points.npy',d/'exact_nomination_g12',10**12);report(d/'exact_nomination_g12');record['exact_counts']=a['counts'];record['exact_weak']=a['weak']
        else:record['result']='no admitted three-cap mass closure in finite tested triples'
        record['seconds']=time.time()-start;records.append(record);(out/'trials.json').write_text(json.dumps(records,indent=2))
        if order%10==0 or(best and best[0]['S']<=2):print('MASS_COMPENSATED_CAPS',record,flush=True)
    print('MASS_COMPENSATED_CAPS_DONE',out,len(records),sum(r['result']=='uniform centroid closure numerical'for r in records),time.time()-start,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('scout');p.add_argument('out');p.add_argument('--number',type=int,default=200);a=p.parse_args();run(a.scout,a.out,a.number)
