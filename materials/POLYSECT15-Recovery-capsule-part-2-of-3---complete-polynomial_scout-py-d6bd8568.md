# material-d6bd8568a4f6

AI research material

---

"""Finite floating scout for polynomial circular-section centres.
NOT a proof, not a global optimum. Python3.13.5/NumPy2.3.5/SciPy1.17.0.
Run OPENBLAS_NUM_THREADS=1 python polynomial_scout.py.
No randomness. All initial data, bounds, meshes and optimizer parameters literal.
The accepted rational model is independently specified and certified by
polynomial_sections.py; its recovery does not depend on optimizer repeatability.
"""
import numpy as np,json
from scipy.optimize import minimize,brentq
from numpy.polynomial.polynomial import polyval,polyder,polymul,polyadd

def unpack(v,degree):
    a=v[0];p=np.r_[1.,v[1:degree],0.];q=v[degree:2*degree+1]
    w=1/((2*np.arange(degree+1)+1)*(2*np.arange(degree+1)+3))
    p[-1]=-np.dot(p[:-1],w[:-1])/w[-1]
    return a,p,q

def quantities(v,degree,y):
    a,p,q=unpack(v,degree);D=polyadd(polymul(p,p),np.r_[0,polymul(q,q)])
    Dy=polyval(y,polyder(D));Dv=polyval(y,D);R=(1-y)*Dv;T=Dv-(1-y)*Dy
    N=polyval(y,2*polyder(p))+4*y*polyval(y,polyder(p,2))
    L=polyval(y,6*polyder(q))+4*y*polyval(y,polyder(q,2))
    K=(1-y)**3*(N*N+y*L*L)
    return Dv,1-a*a*K,(T-a*np.sqrt(np.maximum(R,0))*Dy)/np.maximum(Dv,1e-15),(T+a*np.sqrt(np.maximum(R,0))*Dy)/np.maximum(Dv,1e-15)

def solve(degree,margin=.04):
    k=brentq(lambda k:np.sin(k)-k*np.cos(k),4,5,xtol=1e-14)
    xx=np.linspace(0,1,2001); yy=xx*xx
    p=np.polynomial.polynomial.polyfit(yy,np.cos(k*xx),degree); p/=p[0]
    q=np.polynomial.polynomial.polyfit(yy,np.sinc(k*xx/np.pi)*k,degree)
    v=np.r_[.015,p[1:degree],q]
    nodes=np.linspace(0,1,1601)
    def constraints(v):
        D,K,A,B=quantities(v,degree,nodes)
        return np.r_[D-.02,K-margin,A-margin,B-margin]
    res=minimize(lambda v:-v[0],v,method='SLSQP',bounds=[(.001,.2)]+[(-2000,2000)]*(len(v)-1),constraints={'type':'ineq','fun':constraints},options={'maxiter':600,'ftol':1e-10})
    a,p,q=unpack(res.x,degree);fine=quantities(res.x,degree,np.linspace(0,1,100001))
    return dict(degree=degree,margin=margin,variables=res.x.tolist(),amplitude=a,P_shape=p.tolist(),Q_shape=q.tolist(),success=bool(res.success),message=res.message,iterations=res.nit,dense_minima=[float(v.min()) for v in fine])
if __name__=='__main__':
    out=[solve(d) for d in [2,3,4,5]]
    print(json.dumps(out,indent=2))
