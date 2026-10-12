import json,numpy as np
from fractions import Fraction as F
from scipy.optimize import differential_evolution,minimize
A=json.load(open('/mnt/data/c182/B.json'));H=np.array(json.load(open('/mnt/data/c182/raw.json'))['H'],float);H=H[:,:3]/H[:,3:]
g=np.array([float(F(x)) for x in A['raw_centroid']]);P=np.array([[float(F(x)) for x in p] for p in A['raw_vertices']]);X=P-g;b=1-H@g

def metrics(n):
 n=n/np.linalg.norm(n);h=np.max(np.abs(X@n));r=np.min(b/np.linalg.norm(np.cross(H,n),axis=1));return h,r,r/h

def obj(t):return -metrics(np.r_[1.,t])[2]
r=differential_evolution(obj,[(.05,.65),(-.05,.05)],seed=182,maxiter=150,popsize=12,tol=1e-10,polish=True)
print('disk opt',r.x,metrics(np.r_[1,r.x]))
for n in [[94,34,1],[100,30,1],[1000,*np.rint(r.x*1000).astype(int)],[100,*np.rint(r.x*100).astype(int)]]:print('disk simple',n,metrics(np.array(n,float)))

def cylinder(n):
 n=n/np.linalg.norm(n);c=np.max(np.linalg.norm(np.cross(X,n),axis=1));L=np.min(b/np.abs(H@n));return c,L,L/c
r=differential_evolution(lambda t:-cylinder(np.r_[t,1.])[2],[(-.1,.1),(-.2,.2)],seed=183,maxiter=150,popsize=12,tol=1e-10,polish=True)
print('rod opt',r.x,cylinder(np.r_[r.x,1.]))
for n in [[0,0,1],[-4,8,100],[*np.rint(r.x*1000).astype(int),1000],[*np.rint(r.x*100).astype(int),100]]:print('rod simple',n,cylinder(np.array(n,float)))
