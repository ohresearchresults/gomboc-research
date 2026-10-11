"""Explicit finite physical crossings of almost-incident old face/vertex pairs.
The old contact chart predicts a point outside its old supporting plane; the
new hull is then rebuilt and its actual volume centroid and census calculated.
This changes the physical body, never merely its integration triangulation.
"""
import sys,json,hashlib,time
from pathlib import Path
import numpy as np
from scipy.spatial import QhullError
import jax
import jax.numpy as jnp
from physical_multiple_cap_family import MultipleCapFamily
from apex_polygon_direct_goal import minimum_route

def run(src,out,m=44,points=2,edge_limit=249,geometry='caps',second_apex=20):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=src.read_bytes();(out/'source_z.npy').write_bytes(raw);z=np.load(out/'source_z.npy')
    if geometry=='caps':fam=MultipleCapFamily(m,points,edge_limit)
    elif geometry=='flexible-two-apex':
        from flexible_two_apex_supports import FlexibleTwoApexFamily
        fam=FlexibleTwoApexFamily(m,second_apex,edge_limit)
    else:raise ValueError('unknown physical family')
    s=fam.state(z)
    gaps=1-s['Y']@s['Z'].T;contacts=np.zeros_like(gaps,dtype=bool)
    for i,f in enumerate(s['faces']):contacts[i,f]=True
    pairs=np.argwhere(~contacts);pairs=pairs[np.argsort(gaps[~contacts])[:12]]
    @jax.jit
    def old_gaps(q):
        X,Z,Y,g,v=fam.physical(q,s['R'],s['T'],s['A'])
        return 1-jnp.sum(Y[pairs[:,0]]*Z[pairs[:,1]],axis=1)
    J=np.asarray(jax.jacfwd(old_gaps)(z));rows=[];best=None
    (out/'source.json').write_text(json.dumps(dict(path=str(src),sha256=hashlib.sha256(raw).hexdigest(),m=m,points=points,geometry=geometry,second_apex=second_apex,edge_limit=edge_limit,method=__doc__,source_minimum=float(gaps[~contacts].min())),indent=2)+'\n');same=None
    for k,(f,v) in enumerate(pairs):
        grad=J[k];norm=grad@grad
        if norm<1e-30:continue
        for target in [1e-9,1e-8,1e-7,1e-6,1e-5,1e-4,1e-3,.01]:
            zz=z-(gaps[f,v]+target)*grad/norm;label=f'pair{k:02d}_target{target:g}';oldvalue=float(old_gaps(zz)[k])
            if oldvalue>=-1e-12:continue
            try:t=fam.state(zz)
            except (ValueError,QhullError,np.linalg.LinAlgError):continue
            ur=int(np.argmax(np.sum(t['Z']**2,1)));sr=int(np.argmax(np.sum(t['Y']**2,1)))
            uc=minimum_route(t['Z'],ur,1e-6)[2];sc=minimum_route(t['Y'],sr,1e-6)[2]
            row={k:t[k] for k in ['V','E','F','S','U','Pmax','Qmax','minimum_noncontact']}
            row.update(label=label,old_face=int(f),old_vertex=int(v),old_chart_gap=oldvalue,ucost=uc,scost=sc,objective=uc+sc)
            np.save(out/(label+'_z.npy'),zz);rows.append(row)
            if best is None or row['objective']<best['objective']:
                best=row;np.save(out/'best_z.npy',zz);(out/'best.json').write_text(json.dumps(row,indent=2)+'\n');print('LITERAL_MULTICAP_CONTACT_CROSSING',row,flush=True)
            if (t['S'],t['U'])==(s['S'],s['U']) and (same is None or row['objective']<same['objective']):
                same=row;np.save(out/'same_census_z.npy',zz);(out/'same_census.json').write_text(json.dumps(row,indent=2)+'\n')
            if t['S']==t['U']==1:
                np.save(out/'NUMERICAL_NOMINATION_z.npy',zz)
                if geometry=='caps':np.save(out/'NUMERICAL_NOMINATION_base_H.npy',t['baseH']);np.save(out/'NUMERICAL_NOMINATION_cap_points.npy',t['cap_points'])
                else:np.save(out/'NUMERICAL_NOMINATION_H.npy',t['H'])
                (out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');(out/'screen.json').write_text(json.dumps(rows,indent=2)+'\n');return row
    (out/'screen.json').write_text(json.dumps(rows,indent=2)+'\n');return best

if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 44,int(sys.argv[4]) if len(sys.argv)>4 else 2)
