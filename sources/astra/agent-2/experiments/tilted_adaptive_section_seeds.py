"""New quadrilateral-section bodies with tilted axes and adaptive section levels.
Each trial first rigidly reframes the accepted parent's unique farthest vertex
as (0,0,1), with a chosen direction inside its actual support cone. Section
levels are then greedily placed where linear interpolation of the parent's
sectional support functions has greatest error. Literal polygonal sections
and a small explicit concave rounding define a NEW homogeneous body, whose
true hull, complete equilibrium census, and actual mass are reconstructed.
"""
import json,hashlib,time
from pathlib import Path
import numpy as np
from parallel_section_family import SectionFamily

def run(out):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);src=Path('artifacts/baseline/numerical.npz');raw=src.read_bytes();data=np.load(src,allow_pickle=True);original=data['X'];apex=original[np.sum(original*original,1).argmax()];edges=np.asarray(sorted({tuple(sorted((a,b))) for f in data['faces'] for a,b in zip(f,f[1:]+f[:1])}),int);rows=[];best=None;fewest=None;start=time.time();axes=[]
    for angle in [0,20,40,55,65]:
        for azimuth in ([0] if angle==0 else np.linspace(0,2*np.pi,8,endpoint=False)):
            a=np.deg2rad(angle);ez=np.array([np.sin(a)*np.cos(azimuth),np.sin(a)*np.sin(azimuth),np.cos(a)]);others=np.linalg.norm(original-apex,axis=1)>1e-8
            if np.max((original-apex)[others]@ez)>=-1e-7:continue
            ex=np.cross([0.,1.,0.],ez);ex/=np.linalg.norm(ex);ey=np.cross(ez,ex);R=np.column_stack([ex,ey,ez]);axes.append((angle,float(azimuth),R))
    (out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(raw).hexdigest(),method=__doc__,incidence_source='same numerical.npz face ordering',axes_admitted=len(axes)),indent=2)+'\n')
    (out/'tilted_adaptive_section_seeds.py').write_bytes(Path(__file__).read_bytes())
    for axis,(angle,azimuth,R) in enumerate(axes):
        X=(original-apex)@R+[0.,0.,1.];bottom=X[:,2].min()+.002;knots=np.unique(np.r_[bottom,X[(X[:,2]>bottom)&(X[:,2]<1-1e-8),2],1.]);sections=[]
        for z in knots[:-1]:
            a,b=X[edges[:,0]],X[edges[:,1]];active=(a[:,2]<=z)&(b[:,2]>=z)|(b[:,2]<=z)&(a[:,2]>=z);active&=abs(a[:,2]-b[:,2])>1e-14;a,b=a[active],b[active];t=(z-a[:,2])/(b[:,2]-a[:,2]);sections.append((a+t[:,None]*(b-a))[:,:2])
        for m,L in [(8,15),(12,10),(16,7),(20,6),(24,5),(30,4),(40,3)]:
            for phase in [0.,.33]:
                theta=2*np.pi*(np.arange(m)+phase)/m;n=np.c_[np.cos(theta),np.sin(theta)];support=np.r_[[np.max(P@n.T,axis=0) for P in sections],np.zeros((1,m))];selected=[0,len(knots)-1]
                while len(selected)<L+1:
                    selected.sort();interpolation=np.stack([np.interp(knots,knots[selected],support[selected,i]) for i in range(m)],axis=1);error=np.max(support-interpolation,axis=1);error[selected]=-np.inf;k=int(error.argmax());selected.append(k)
                selected.sort();ids=selected[:-1];z=knots[ids];h=support[ids]+.001*(1-z[:,None])+.0005*(z[:,None]-bottom)*(1-z[:,None]);q=np.r_[h.ravel(),z];label=f'axis{axis:02d}_m{m}_L{L}_ph{phase:g}';fam=SectionFamily(n,L)
                try:s=fam.state(q)
                except (ValueError,AssertionError,np.linalg.LinAlgError) as e:rows.append(dict(label=label,error=repr(e)));continue
                row={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax','minimum_noncontact']};row.update(label=label,m=m,L=L,tilt_degrees=angle,azimuth=azimuth,phase=phase,rotation=R.tolist(),level_indices=list(map(int,ids)));np.save(out/(label+'_q.npy'),q);np.save(out/(label+'_normals.npy'),n);rows.append(row);key=s['Pmax']+s['Qmax'];count=s['S']+s['U']
                if best is None or key<best:
                    best=key;(out/'best_bars.json').write_text(json.dumps(row,indent=2)+'\n');print('TILTED_ADAPTIVE_SECTION',row,flush=True)
                if fewest is None or count<fewest:fewest=count;(out/'fewest.json').write_text(json.dumps(row,indent=2)+'\n')
                if s['S']==s['U']==1:
                    np.save(out/'NUMERICAL_NOMINATION_q.npy',q);np.save(out/'NUMERICAL_NOMINATION_normals.npy',n);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');(out/'screen.json').write_text(json.dumps(rows,indent=2)+'\n');return
        (out/'screen.json').write_text(json.dumps(rows,indent=2)+'\n')
    (out/'FINITE_SCREEN_END.json').write_text(json.dumps(dict(goal_complete=False,seconds=time.time()-start,rows=len(rows)),indent=2)+'\n')

if __name__=='__main__':run('artifacts/parallel_section_goal/tilted_adaptive_seeds')
