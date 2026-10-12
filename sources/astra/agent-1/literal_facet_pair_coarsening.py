"""Replace two adjacent H inequalities by an explicit convex combination.
This is a literal new uniformly filled convex body. The old body is contained
in it, but neither its centroid nor its equilibrium census is inherited.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,pathlib,time,itertools
from fractions import Fraction
import numpy as np
from scipy.spatial import QhullError
from geometry import halfspace_mesh,census
from persistence_search import polar_edges
from make_contact_atlas import make
from contact_forest import ContactModel

def run(parent,out,weights=(.1,.25,.5,.75,.9)):
    parent=pathlib.Path(parent);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);H=json.loads((parent/'H.json').read_text())['H'];Q=np.array([[float(Fraction(int(v),int(row[3]))) for v in row[:3]] for row in H]);m=halfspace_mesh(Q);original=census(m,0);assert original['S']==original['U']==1;g=m['g'];edges=polar_edges(m);order=np.argsort(np.linalg.norm(Q[edges[:,0]]-Q[edges[:,1]],axis=1));history=[];start=time.time();best=(999,999,999)
    (out/'definition.json').write_text(json.dumps(dict(parent=str(parent.resolve()),weights=list(weights),source_census=original,reference_centroid=g.tolist(),scope='Literal pair replacement; reference and actual-centroid counts are separate'),indent=2))
    for rank,k in enumerate(order):
        i,j=map(int,edges[k])
        for lam in weights:
            R=np.r_[np.delete(Q,[i,j],axis=0),((1-lam)*Q[i]+lam*Q[j])[None]]
            try:
                mm=halfspace_mesh(R);cc=census(mm,0);reference=dict(mm);reference['g']=g;rr=census(reference,0);row=dict(edge_index=int(k),pair=[i,j],weight=lam,referenceS=rr['S'],referenceU=rr['U'],reference_margin=min(rr['min_primal_nonroot'],rr['min_polar_nonroot']),seconds=time.time()-start,**cc)
                key=(rr['S']+rr['U'],cc['S']+cc['U'],cc['E'])
                if cc['E']<original['E'] and (key<best or rr['S']==rr['U']==1 or cc['S']==cc['U']==1):
                    folder=out/f'pair{i:03d}-{j:03d}-weight{lam:g}';folder.mkdir();np.savez(folder/'body.npz',Q=R,X=mm['X'],reference=g);(folder/'summary.json').write_text(json.dumps(row,indent=2));row['folder']=str(folder.resolve());best=min(best,key);print('COARSENING_CANDIDATE',json.dumps(row),flush=True)
                    if cc['S']==cc['U']==1 and min(cc['min_primal_nonroot'],cc['min_polar_nonroot'])>1e-9:
                        Y=R[mm['active']];proposal=dict(scope='Numerical hull after pair replacement; exact contact reconstruction pending',V=len(mm['X']),E=len(mm['edges']),F=len(Y),faces=mm['faces'],edges=mm['edges'].tolist(),active=list(range(len(Y))),raw_vertices=[[str(x) for x in p] for p in mm['X']],raw_halfspaces=[[str(x) for x in q]+['1'] for q in Y]);(folder/'proposal.json').write_text(json.dumps(proposal,indent=2));make(folder/'proposal.json',folder/'chart',balanced=True);c=ContactModel(folder/'chart',1,1,'local');e=c.evaluate(c.initial,False)
                        if e['S']!=1 or e['U']!=1 or e['mechanical'].min()<=1e-9:raise ValueError('the reconstructed contact body did not retain strict own110')
                        np.savez(folder/'realization.npz',z=c.initial,X=e['X'],Q=e['Y']);(out/'NUMERICAL_LOWER_C_OWN110.json').write_text(json.dumps(dict(chart=str((folder/'chart').resolve()),input=str((folder/'realization.npz').resolve()),E=c.meta['E'],S=e['S'],U=e['U'],scope='Rational audit required; body may remain over budget'),indent=2));history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));return
            except (ValueError,AssertionError,QhullError,RuntimeError,np.linalg.LinAlgError) as err:row=dict(edge_index=int(k),pair=[i,j],weight=lam,error=repr(err))
            history.append(row)
        if rank%10==0:(out/'history.json').write_text(json.dumps(history,indent=2));print('PAIR_SCREEN',rank,'best_reference_own_E',best,flush=True)
    (out/'history.json').write_text(json.dumps(history,indent=2));print('FINITE_PAIR_SCREEN_COMPLETE',len(history),best,flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--parent',required=True);ap.add_argument('--out',required=True);a=ap.parse_args();run(a.parent,a.out)
