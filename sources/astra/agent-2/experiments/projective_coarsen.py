from pathlib import Path
import json,time,sys
import numpy as np
from scipy.optimize import least_squares
from geometry import hull_from_supports,mass,transform,escape
root=Path(__file__).resolve().parents[1];d=np.load(root/'artifacts/baseline/numerical.npz',allow_pickle=True);Y0=d['Y']
out=root/'artifacts/projective_coarsen';out.mkdir(exist_ok=True)

def fit(X,Y,tri,start=None,maxeval=200,margin=1e-7):
    if start is None:start=np.zeros(8)
    def residual(t):
        val=transform(X,Y,tri,t)
        if val is None:return np.full(len(X)+len(Y)-2,1e3)
        Z,Q,c,vol=val
        u,_=escape(Z);s,_=escape(Q)
        u=np.delete(u,np.argmin(u));s=np.delete(s,np.argmin(s))
        return np.r_[np.maximum(margin-u,0),np.maximum(margin-s,0)]
    opt=least_squares(residual,start,max_nfev=maxeval,ftol=1e-11,xtol=1e-11,gtol=1e-12,diff_step=1e-5,bounds=([-0.5]*3+[-0.7]*5,[0.5]*3+[0.7]*5))
    Z,Q,c,vol=transform(X,Y,tri,opt.x);u,_=escape(Z);s,_=escape(Q)
    return opt.x,{'S':int((s<0).sum()),'U':int((u<0).sum()),'cost':float(opt.cost),'floor':float(min(np.sort(u)[1],np.sort(s)[1])),'nfev':opt.nfev,'t':opt.x.tolist()}

if __name__=='__main__':
    test=sys.argv[1] if len(sys.argv)>1 else 'singles'
    if test=='baseline':
        t,r=fit(d['X'],d['Y'],d['tri'],margin=1e-4,maxeval=1000);print(r,flush=True)
        (out/'baseline_fit.json').write_text(json.dumps(r,indent=2)+'\n')
    else:
        rows=[]
        for i in range(len(Y0)):
            X,Y,faces,tri,E,active=hull_from_supports(np.delete(Y0,i,axis=0))
            t,r=fit(X,Y,tri,maxeval=200);r.update(removed=i,E=E,V=len(X),F=len(Y));rows.append(r)
            (out/'singles.json').write_text(json.dumps(rows,indent=2)+'\n')
            if r['S']==r['U']==1:
                np.savez(out/f'single_{i}.npz',X=X,Y=Y,tri=tri,t=t,faces=np.array(faces,dtype=object));print('SURVIVOR',r,flush=True)
            elif i%10==0:print('progress',i,'best',min(rows,key=lambda v:v['cost']),flush=True)
