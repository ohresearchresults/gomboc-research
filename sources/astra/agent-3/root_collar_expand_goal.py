"""Grow a root-star/collar physical polyhedron up to the actual edge budget.

Each candidate is an intersection of unchanged rational source halfspaces.
Exact contact identity, not a generic-simple bound or rounded plane grouping,
determines the screened incidence. New goal searches vary the entire resulting
contact realization, including every vertex and maximal plane and filled mass.
"""
import argparse,json,time,importlib.util,hashlib
from pathlib import Path
import numpy as np
from literal_support_subset_goal import Source
from contact_numpy import Chart
from bounded_convex_goal import run as convex_goal
from contact_physical_110 import realize

def save_proposal(S,ids,g,out):
    out.mkdir(parents=True,exist_ok=False);scale=np.sqrt(np.mean(g['Z']**2));X=g['Z']/scale;Y=g['H']*scale
    p=dict(V=g['V'],E=g['E'],F=g['F'],faces=g['faces'],edges=g['edges'],raw_vertices=X.tolist(),raw_halfspaces=[list(q)+[1.]for q in Y],active=list(range(len(ids))),retained_source_face_ids=list(ids),source=str(S.path.resolve()),source_sha256=hashlib.sha256(S.path.read_bytes()).hexdigest(),scope='new normalized full contact realization, seed incidence from exact literal source subset; physical validity and native exact own-centroid audit required')
    (out/'proposal.json').write_text(json.dumps(p,indent=2));np.save(out/'seed_vertices.npy',X)
    spec=importlib.util.spec_from_file_location('collar_peeling','sources/peer_balanced_contact/make_contact_atlas.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);meta,q,*_=mod.make(out/'proposal.json',out/'peeling',balanced=True)
    for plan in meta['plan']:plan['fixed']={}
    D=max(float(x).as_integer_ratio()[1]for x in q);meta.update(grid=D,free_controls=[int(float(x)*D)for x in q]);(out/'construction.json').write_text(json.dumps(meta,indent=2));c=Chart(out/'construction.json');z=c.physical(c.q0,require_valid=False);(out/'seed_readback.json').write_text(json.dumps(dict(valid=bool(z['valid']),minimum_noncontact=float(min(z['noncontact'])),minimum_turn=z['min_turn'],point_error=float(max(abs(z['X']-X).ravel())),contact_error=z['contact_error']),indent=2));return c,z

def run(source,core,out,width=3,steps=600):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);S=Source(source);initial=tuple(json.loads(Path(core).read_text())['retained']);seed=S.geometry(initial);start=time.time();allend=[]
    for mode in ['bars','census','volume']:
        md=out/mode;md.mkdir();beam=[(initial,seed)];seen={initial};hist=[];terminal=[];serial=0
        for level in range(S.n-len(initial)):
            pool=[]
            for parent,(ids,g)in enumerate(beam):
                found=False
                for added in range(S.n):
                    if added in ids:continue
                    ii=tuple(sorted((*ids,added)))
                    if ii in seen:continue
                    seen.add(ii);serial+=1
                    try:gg=S.geometry(ii)
                    except(ValueError,np.linalg.LinAlgError,ZeroDivisionError):continue
                    if gg['E']>248:continue
                    found=True;row=dict(level=level,serial=serial,added=added,parent=parent,retained=list(ii),**{k:gg[k]for k in ['V','E','F','S','U','Pmax','Qmax','volume']})
                    if gg['S']==gg['U']==1:S.freeze(ii,md/f'exact_goal_{serial:06d}','literal apex-star collar addition, actual numerical centroid110 and exact-incidence E<=248')
                    if mode=='bars':score=gg['Pmax']+gg['Qmax']+1e-7*(gg['S']+gg['U'])
                    elif mode=='census':score=gg['S']+gg['U']+.5*(gg['Pmax']+gg['Qmax'])
                    else:score=gg['volume']
                    pool.append((score,ii,gg,row))
                if not found:terminal.append((ids,g))
            if not pool:break
            pool.sort(key=lambda r:r[0]);beam=[(ids,g)for _,ids,g,_ in pool[:width]];row=dict(level=level,trials=serial,mode=mode,best=pool[0][3],seconds=time.time()-start);hist.append(row);(md/'history.json').write_text(json.dumps(hist,indent=2));print('ROOT_COLLAR_EXPAND',row,flush=True)
        terminal.extend(beam);unique={i:g for i,g in terminal};rank=sorted(unique.items(),key=lambda p:p[1]['Pmax']+p[1]['Qmax'])[:width]
        for k,(ids,g)in enumerate(rank):
            d=md/f'endpoint{k:02d}';c,z=save_proposal(S,ids,g,d);allend.append((d,c,z));(d/'screen.json').write_text(json.dumps({x:g[x]for x in ['V','E','F','S','U','Pmax','Qmax','volume']},indent=2))
    for d,c,z in allend:
        if z['valid']:
            convex_goal(d/'construction.json',d/'convex_110',steps)
            startq=d/'convex_110/endpoint_q.npy'
        else:startq=None
        realize(d/'construction.json',d/'full_physical_110',steps,1e-8,startq,True)
    print('ROOT_COLLAR_FINITE_STOP',len(allend),time.time()-start,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('core');p.add_argument('out');p.add_argument('--width',type=int,default=3);p.add_argument('--steps',type=int,default=600);a=p.parse_args();run(a.source,a.core,a.out,a.width,a.steps)
