"""Explicit physical crossings of nearly incident support/vertex pairs.
Each trial changes one raw supporting normal and rebuilds the complete hull.
Require a genuine change of the polar triangulation/active facets, rather
than relabeling integration triangles. Apex candidate retirement is allowed.
"""
import sys,json,hashlib
from pathlib import Path
import numpy as np
from scipy.spatial import QhullError
from apex_polygon_supports import ApexFamily
from apex_polygon_direct_goal import minimum_route
from support_persistence import ROOT

def run(src,out,m=44,edge_limit=248):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);q=np.load(src);fam=ApexFamily(m,allow_top_retirement=True,edge_limit=edge_limit);s=fam.state(q);H=s['H'];X=s['X'];N=len(H);oldfaces={tuple(sorted(map(int,t))) for t in s['R'][1:]};stable_root=int(s['A'][np.argmax(np.sum(s['Y']**2,1))]);rows=[];best=None
    (out/'source.npy').write_bytes(src.read_bytes());(out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(src.read_bytes()).hexdigest(),apex_candidates=m,edge_limit=edge_limit,method=__doc__),indent=2)+'\n')
    incidence=np.zeros((N,len(X)),bool);incidence[:m,0]=True
    for v,trip in enumerate(s['R'][1:],1):incidence[trip,v]=True
    gaps=1-H@X.T;gaps[incidence]=np.inf;near=np.argsort(gaps.ravel())[:12]
    for rank,index in enumerate(near):
        i,v=map(int,np.unravel_index(index,gaps.shape));gap=float(gaps[i,v]);d=X[v].copy()
        if i<m:d[2]=0
        denominator=float(d@X[v])
        if denominator<1e-14:continue
        for exponent in [10,9,8,7,6,5,4]:
            target=10.**(-exponent);HH=H.copy();HH[i]+=d*(gap+target)/denominator;qq=fam.pack(HH);label=f'pair{rank:02d}_e{exponent}';np.save(out/(label+'_q.npy'),qq)
            try:
                t=fam.state(qq);faces={tuple(sorted(map(int,a))) for a in t['R'][1:]};changed=faces!=oldfaces
                if not changed:raise ValueError('no true polar facet change')
                si=np.flatnonzero(t['A']==stable_root)
                if not len(si):raise ValueError('designated elder stable plane retired')
                _,_,uc=minimum_route(t['Z'],0,1e-7);_,_,sc=minimum_route(t['Y'],int(si[0]),1e-7)
                row={k:t[k] for k in ['V','E','F','S','U','Pmax','Qmax','minimum_noncontact']};row.update(label=label,plane=i,old_vertex=v,old_gap=gap,requested_violation=target,objective=uc+sc,ucost=uc,scost=sc,removed_polar_facets=len(oldfaces-faces),new_polar_facets=len(faces-oldfaces));np.save(out/(label+'_H.npy'),t['H'])
                key=(t['S']+t['U'],uc+sc)
                if best is None or key<best[0]:best=(key,row);np.save(out/'best_q.npy',qq);np.save(out/'best_H.npy',t['H']);(out/'best.json').write_text(json.dumps(row,indent=2)+'\n');print('PHYSICAL_CONTACT_CROSSING',row,flush=True)
                if t['S']==t['U']==1:
                    from audit_free_supports import audit
                    (out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');audit(out/(label+'_H.npy'),out/'exact_nomination_g16',10**16);return row
            except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError) as e:row=dict(label=label,plane=i,old_vertex=v,old_gap=gap,requested_violation=target,error=repr(e))
            rows.append(row)
    (out/'screen.json').write_text(json.dumps(rows,indent=2)+'\n');return None if best is None else best[1]

if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 44,int(sys.argv[4]) if len(sys.argv)>4 else 248)
