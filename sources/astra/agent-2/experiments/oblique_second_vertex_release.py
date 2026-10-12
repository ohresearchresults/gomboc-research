"""Truncate the second common vertex, balance mass, and release its planes.

In the polar at the SOURCE physical centroid, the added normal lies in a
diameter ball of an old normal, so it has a positive escape and introduces no
reference stable equilibrium. Actual uniform mass is then restored by changing
the second common-intersection parameter. The final body is freshly evaluated.
Once the second common intersection is outside the hull, its planes are free
ordinary supports. Its former coplanarity does not save physical edges and is
not retained as an artificial restriction in the released search family.
"""
import sys,json,hashlib
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull,QhullError
from flexible_two_apex_supports import FlexibleTwoApexFamily
from apex_polygon_supports import ApexFamily
from mass_balanced_two_vertex_retirement import compact,balance

def run(src,out,m,n):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=src.read_bytes();(out/'source_q.npy').write_bytes(raw);q=np.load(out/'source_q.npy');q,m,n,s=compact(q,m,n);H=s['H'];g=s['g'];Z=s['Z'];Y=s['Y']
    if s['S']!=1 or s['active_anchors']!=[0,1]:raise ValueError('this release requires one actual stable equilibrium and both common vertices')
    if 3*s['F']-m>249:raise ValueError('the released one-star body would exceed the genuine edge budget')
    incident=np.array([i for i,f in enumerate(s['faces']) if 1 in f]);v=Z[1];foot=v/(v@v);basepoint=foot if s['uguards'][1]<0 else Y[incident].mean(0);circle=ConvexHull(Y[incident,:2]).vertices;chosen=incident[circle[np.linspace(0,len(circle)-1,min(6,len(circle)),dtype=int)]];latent=FlexibleTwoApexFamily(m,n);free=ApexFamily(m,allow_top_retirement=True,edge_limit=249);rows=[];best=None
    (out/'source.json').write_text(json.dumps(dict(path=str(src),sha256=hashlib.sha256(raw).hexdigest(),m=m,n=n,actual_centroid=g.tolist(),source_counts={k:s[k] for k in ['V','E','F','S','U']},post_truncation_edge_bound=3*s['F']-m,method=__doc__),indent=2)+'\n')
    for old_normal in chosen:
        for t in [.1,.35,.7]:
            base=(1-t)*basepoint+t*Y[old_normal];den=Z@v;num=1-Z@base;mask=(den>0)&(np.arange(len(Z))!=1);limit=float(np.min(num[mask]/den[mask]))
            if limit<=0:continue
            for fraction in [.01,.05,.2,.6]:
                p=base+limit*fraction*v;escape=float(p@(Y[old_normal]-p));offset=float(1+p@g)
                if escape<=1e-11 or offset<=0 or list(np.flatnonzero(Z@p>1+1e-11))!=[1]:continue
                HH=np.r_[H,(p/offset).reshape(1,3)];z=latent.pack(HH,q[-3:]);label=f'n{int(old_normal):03d}_t{t:g}_f{fraction:g}'
                try:
                    z,a,trace=balance(z,latent,g);np.save(out/(label+'_latent_q.npy'),z)
                    row={k:a[k] for k in ['V','E','F','S','U','Pmax','Qmax','minimum_noncontact']};row.update(label=label,m=m,n=n,reference_escape=escape,centroid_error=float(abs(a['g']-g).max()),active_anchors=a['active_anchors']);rows.append(row);(out/(label+'_mass_trace.json')).write_text(json.dumps(trace,indent=2)+'\n')
                    if a['S']==a['U']==1:
                        np.save(out/'NUMERICAL_NOMINATION_two_apex_q.npy',z);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');return row
                    if a['active_anchors']!=[0]:continue
                    qq=free.pack(a['H']);b=free.state(qq);row['released_census']=[b['S'],b['U']];row['released_E']=b['E'];row['released_centroid_discrepancy']=float(abs(b['g']-a['g']).max());np.save(out/(label+'_free_q.npy'),qq)
                    if row['released_centroid_discrepancy']>1e-9:raise ValueError('released independent supports change the integrated body beyond floating reconstruction error')
                    if b['S']!=1:continue
                    key=(b['Pmax'],b['U'])
                    if best is None or key<best[0]:
                        best=key,row;np.save(out/'best_free_q.npy',qq);np.save(out/'best_free_H.npy',b['H']);(out/'best.json').write_text(json.dumps(row,indent=2)+'\n');print('OBLIQUE_SECOND_VERTEX_RELEASE',row,flush=True)
                    if b['U']==1:
                        np.save(out/'NUMERICAL_NOMINATION_free_q.npy',qq);np.save(out/'NUMERICAL_NOMINATION_H.npy',b['H']);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');return row
                except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError) as e:rows.append(dict(label=label,error=repr(e)))
                (out/'screen.json').write_text(json.dumps(rows,indent=2)+'\n')
    return None if best is None else best[1]

if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4]))
