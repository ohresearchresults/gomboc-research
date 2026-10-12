"""Literal fixed-direction polygon sections sampled from the accepted parent.
The sections are a NEW physical body. A small explicit concave radial rounding
makes all intended quadrilaterals genuine. No parent census is inherited.
"""
import json,hashlib
from pathlib import Path
import numpy as np
from parallel_section_family import SectionFamily

def run(out):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);src=Path('artifacts/baseline/numerical.npz');data=np.load(src,allow_pickle=True);X=data['X']+data['raw_centroid'];edges=np.asarray(sorted({tuple(sorted((a,b))) for f in data['faces'] for a,b in zip(f,f[1:]+f[:1])}),int)
    (out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(src.read_bytes()).hexdigest(),incidence_source='faces in the SAME numerical.npz vertex ordering',exact_parent='artifacts/baseline/B_exact.json',parent_census_inherited=False,method=__doc__),indent=2)+'\n');rows=[]
    for m,L in [(8,15),(10,12),(12,10),(16,7),(20,6),(24,5),(30,4),(40,3)]:
        for phase in [0.,.37]:
            theta=2*np.pi*(np.arange(m)+phase)/m;n=np.c_[np.cos(theta),np.sin(theta)];fam=SectionFamily(n,L)
            for end in [.15,.35,.6]:
                for power in [.7,1.4]:
                    bottom=X[:,2].min()+.002;z=bottom+(end-bottom)*np.linspace(0,1,L)**power;h=[]
                    for height in z:
                        a,b=X[edges[:,0]],X[edges[:,1]];cut=(a[:,2]<height)&(b[:,2]>height)|(a[:,2]>height)&(b[:,2]<height);a,b=a[cut],b[cut];t=(height-a[:,2])/(b[:,2]-a[:,2]);points=a+t[:,None]*(b-a);support=np.max(points[:,:2]@n.T,axis=0);support+=.003*(1-height)+.001*(height-bottom)*(1-height);h.append(support)
                    q=np.r_[np.asarray(h).ravel(),z];label=f'm{m}_L{L}_ph{phase:g}_end{end:g}_pow{power:g}'
                    try:s=fam.state(q)
                    except (ValueError,AssertionError,np.linalg.LinAlgError) as e:rows.append(dict(label=label,error=repr(e)));continue
                    row={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax','minimum_noncontact']};row.update(label=label,m=m,L=L,phase=phase,end=end,power=power);np.save(out/(label+'_q.npy'),q);np.save(out/(label+'_normals.npy'),n);rows.append(row);print('PARALLEL_SECTION_SEED',row,flush=True)
                    if s['S']==s['U']==1:
                        np.save(out/'NUMERICAL_NOMINATION_q.npy',q);np.save(out/'NUMERICAL_NOMINATION_normals.npy',n);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n')
    (out/'screen.json').write_text(json.dumps(rows,indent=2)+'\n')

if __name__=='__main__':
    import sys
    run(sys.argv[1] if len(sys.argv)>1 else 'artifacts/parallel_section_goal/seeds_v2')
