"""Physical blends of own-S1 and own-U1 high-valence-apex constructions.
Each source is put in one actual-centroid Euclidean similarity frame, with the
same genuine farthest apex at (0,0,1) and the largest polar direction in the
positive x half-plane. Top candidates are matched cyclically, other supports
by an explicit assignment. The interpolated halfspaces define a NEW uniformly
filled body. Its actual hull, centroid, complete barcodes and census are freshly
computed; endpoint/reference-center properties are never inherited.
"""
import sys,json,hashlib,time
from pathlib import Path
import numpy as np
from scipy.optimize import linear_sum_assignment
from scipy.spatial import QhullError
from apex_polygon_supports import ApexFamily

class NumericalFamily(ApexFamily):
    def __init__(self,m):
        super().__init__(m,True,249)
        # Explicit independent NumPy mass map for discovery over changing hulls.
        self.physical=self.independent_physical

def framed(q,m):
    f=NumericalFamily(m);s=f.state(q);u=np.array([0.,0.,1.])-s['g'];radius=np.linalg.norm(u);ez=u/radius;polar=s['Y'][np.argmax(np.sum(s['Y']**2,1))];ex=polar-ez*(polar@ez);ex/=np.linalg.norm(ex);ey=np.cross(ez,ex);R=np.column_stack([ex,ey,ez]);H=(s['H']/(1-s['H']@s['g'])[:,None])@R*radius;H[:m,2]=1.;qq=f.pack(H);t=f.state(qq);return H,dict(original_centroid=s['g'].tolist(),rotation=R.tolist(),scale=radius,framed_centroid=t['g'].tolist(),framed_counts=[t['S'],t['U']])

def run(sourceA,sourceB,out,m=44,samples=3200):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);sources=[]
    for name,src in [('A',sourceA),('B',sourceB)]:
        src=Path(src);raw=src.read_bytes();(out/(name+'_source_q.npy')).write_bytes(raw);sources.append(dict(source=str(src),sha256=hashlib.sha256(raw).hexdigest()))
    A,am=framed(np.load(out/'A_source_q.npy'),m);B,bm=framed(np.load(out/'B_source_q.npy'),m)
    if len(A)!=len(B):raise ValueError('physical blend pools must have the same explicit number of supports')
    if len(A)>(249+m+3)//3:raise ValueError('blend pool exceeds the genuine apex edge budget')
    np.save(out/'A_framed_H.npy',A);np.save(out/'B_framed_H.npy',B);(out/'source.json').write_text(json.dumps(dict(sources=sources,frames=[am,bm],m=m,samples=samples,seed=940271,method=__doc__),indent=2)+'\n');(out/'producer.py').write_bytes(Path(__file__).read_bytes());fam=NumericalFamily(m);rng=np.random.default_rng(940271);rows=[];best=None;fewest=np.inf;start=time.time();orders=[]
    orderA=np.argsort(np.arctan2(A[:m,1],A[:m,0]));A=np.r_[A[orderA],A[m:]]
    parameters=[]
    for phase in [0.,-.03,.03,-.12,.12,-.3,.3]:
        for scale in [.9,1.,1.1]:
            ts=np.unique(np.r_[np.linspace(0,1,61),np.logspace(-8,-1,15),1-np.logspace(-8,-1,15)])
            parameters.extend((float(t),phase,scale,1.) for t in ts)
    parameters.extend((float(rng.uniform()),float(rng.uniform(-.5,.5)),float(np.exp(rng.uniform(-.3,.3))),float(np.exp(rng.uniform(-.25,.25)))) for _ in range(max(0,samples-len(parameters))))
    for k,(t,phase,scale,anisotropy) in enumerate(parameters):
        R=np.array([[np.cos(phase),-np.sin(phase),0],[np.sin(phase),np.cos(phase),0],[0,0,1.]]);BB=B@R;BB[:,:2]*=[scale*anisotropy,scale/anisotropy];orderB=np.argsort(np.arctan2(BB[:m,1],BB[:m,0]));top=BB[orderB];costs=[np.sum((A[:m,:2]-np.roll(top,j,axis=0)[:,:2])**2) for j in range(m)];shift=int(np.argmin(costs));top=np.roll(top,shift,axis=0);a=A[m:];b=BB[m:];ra=np.linalg.norm(a,axis=1);rb=np.linalg.norm(b,axis=1);cost=1-(a/ra[:,None])@(b/rb[:,None]).T+.05*(np.log(ra)[:,None]-np.log(rb)[None,:])**2;ii,jj=linear_sum_assignment(cost)
        if not np.array_equal(ii,np.arange(len(a))):raise ValueError('incomplete support matching')
        endpoint=np.r_[top,b[jj]];H=(1-t)*A+t*endpoint;q=fam.pack(H)
        try:s=fam.state(q)
        except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError):continue
        objective=float(np.log1p(s['P']/.02).sum()+np.log1p(s['Q']/.02).sum());row={j:s[j] for j in ['V','E','F','S','U','Pmax','Qmax','minimum_noncontact']};row.update(sample=k,t=t,phase=phase,scale=scale,anisotropy=anisotropy,objective=objective);rows.append(row);key=(s['S']+s['U'],objective)
        if best is None or key<best:
            best=key;np.save(out/'best_q.npy',q);np.save(out/'best_H.npy',H);(out/'best.json').write_text(json.dumps(dict(row,top_shift=shift,top_A_order=orderA.tolist(),top_B_order=orderB.tolist(),free_B_assignment=jj.tolist()),indent=2)+'\n');print('COMPLEMENTARY_PHYSICAL_BLEND',row,flush=True)
        if s['S']==s['U']==1:
            np.save(out/'NUMERICAL_NOMINATION_q.npy',q);np.save(out/'NUMERICAL_NOMINATION_H.npy',H);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');(out/'screen.json').write_text(json.dumps(rows,indent=2)+'\n');return row
        if k%100==0:(out/'screen.json').write_text(json.dumps(rows,indent=2)+'\n')
    (out/'screen.json').write_text(json.dumps(rows,indent=2)+'\n');(out/'FINITE_SCREEN_END.json').write_text(json.dumps(dict(goal_complete=False,rows=len(rows),seconds=time.time()-start),indent=2)+'\n')

if __name__=='__main__':run(sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4]) if len(sys.argv)>4 else 44)
