"""Detach the extra stable triangle from the unique unstable apex.
Add one actual point beyond only that facet, with a positive reference radial
escape to the old apex. Replace the visible plane by its three real child
planes, then explicitly perturb the children to release the two newly
nonsimple non-apex corners. The physical centroid and census are recomputed.
"""
import sys,json,hashlib
from pathlib import Path
import numpy as np
from scipy.spatial import QhullError
from apex_polygon_supports import ApexFamily
from support_persistence import ROOT

def run(src,out,m=44,edge_limit=249):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);q=np.load(src);old=ApexFamily(m,allow_top_retirement=True,edge_limit=edge_limit).state(q);X,H=old['X'],old['H'];g=old['g'];roots=np.flatnonzero(old['uguards']<0)
    if list(roots)!=[0]:raise ValueError('source does not have the required actual unique apex U')
    candidates=[i for i in np.flatnonzero(old['sguards']<0) if 0 in old['faces'][i]]
    if len(candidates)!=1:raise ValueError('one unwanted stable apex carrier is required')
    f=candidates[0];owner=int(old['A'][f]);face=old['faces'][f]
    if len(face)!=3:raise ValueError('this literal surgery requires a triangular carrier')
    kept=[int(i) for i in old['A'] if i!=owner];source=dict(path=str(src),sha256=hashlib.sha256(src.read_bytes()).hexdigest(),apex_candidates=m,carrier_owner=owner,carrier_vertices=face,active_original=old['A'].tolist(),centroid=g.tolist(),method=__doc__);(out/'source.json').write_text(json.dumps(source,indent=2)+'\n');rows=[];best=None;rng=np.random.default_rng(33415);normal=old['Y'][f];foot=g+normal/(normal@normal);direction=foot-g
    for t in [.03,.08,.2,.4,.65,.85]:
        base=(1-t)*foot+t*X[0];den=H@direction;num=1-H@base;mask=(den>0)&(np.arange(len(H))!=owner);limit=float(np.min(num[mask]/den[mask]))
        for frac in [.002,.02,.2,.65]:
            height=limit*frac;p=base+height*direction;visible=np.flatnonzero(H@p>1+1e-11)
            if list(visible)!=[owner]:continue
            escape=float((p-g)@(X[0]-p))
            if escape<=0:continue
            children=[];newstar=[]
            for a,b in zip(face,face[1:]+face[:1]):
                h=np.linalg.solve(np.array([X[a],X[b],p]),np.ones(3));children.append(h);newstar.append(0 in [a,b])
            full=np.r_[H[kept],children];star=[j for j,i in enumerate(kept) if abs(H[i,2]-1)<1e-10]+[len(kept)+j for j,v in enumerate(newstar) if v];other=[j for j in range(len(full)) if j not in star];order=star+other;newm=len(star);family=ApexFamily(newm,allow_top_retirement=True,edge_limit=edge_limit)
            if len(full)>family.maxF:raise ValueError('released cap would exceed the declared edge budget')
            child_positions=[order.index(len(kept)+j) for j in range(3)];HH=full[order].copy();HH[:newm,2]=1
            labelbase=f't{t:g}_f{frac:g}';np.save(out/(labelbase+'_cap_point.npy'),p);np.save(out/(labelbase+'_unreleased_H.npy'),HH)
            for exp in [10,9,8,7]:
                for repeat in range(2):
                    P=HH.copy()
                    for j in child_positions:
                        P[j,:2 if j<newm else 3]+=rng.normal(size=2 if j<newm else 3)*10.**(-exp)
                    qq=family.pack(P);label=f'{labelbase}_e{exp}_r{repeat}';np.save(out/(label+'_q.npy'),qq)
                    try:
                        s=family.state(qq);row={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax','minimum_noncontact']};row.update(label=label,new_apex_candidates=newm,apex_degree=sum(0 in ff for ff in s['faces']),fraction=frac,t=t,height=height,reference_newpoint_escape=escape,jitter=10.**(-exp));np.save(out/(label+'_H.npy'),s['H']);key=(s['U'],s['S'],s['Qmax'])
                        if best is None or key<best[0]:best=(key,row);np.save(out/'best_q.npy',qq);np.save(out/'best_H.npy',s['H']);(out/'best.json').write_text(json.dumps(row,indent=2)+'\n');print('PHYSICAL_CARRIER_CAP',row,flush=True)
                        if s['S']==s['U']==1:
                            from audit_free_supports import audit
                            (out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');audit(out/(label+'_H.npy'),out/'exact_nomination_g16',10**16);return row
                    except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError) as e:row=dict(label=label,new_apex_candidates=newm,error=repr(e))
                    rows.append(row)
    (out/'screen.json').write_text(json.dumps(rows,indent=2)+'\n');return None if best is None else best[1]

if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 44,int(sys.argv[4]) if len(sys.argv)>4 else 249)
