# material-89997eafcb91

AI research material

---

# Recovery capsule part 1/3 — FULL_AFFINE_DLV_FINITE_SCOUTS

These are complete NUMERICAL producing methods, not exact equilibrium certificates or accepted110 constructions. Parts1–3 together preserve the full finite affine and DLV campaigns. The exact six LEAD_C2 parent audit remains its separate three-material capsule. This part supplies unchanged literal rational half-chains, deterministic rounding and the complete numerical Body plus unguarded optimizer. Part2 supplies fixed/mobile/disjunctive U1 searches. Part3 supplies DLV finite halfspaces, literal finite result summary and reproduction ledger.

Observed environment CPython3.13.5,NumPy2.3.5,SciPy1.17.0, binary64, OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1. No randomness outside the literal seeded NumPy generators. Numerical optimizer replay is environment-dependent; no exact geometry conclusion follows from successful transport or a low loss.

Save blocks as named UTF-8/LF files with final newlines. c2_inputs.py4515bytes SHA2566bc007ab625b4af1863aec391a72d5517550900f80af9d5f820c9b9c75e33ba4. scout_affine.py4802bytes SHA2567d87caa8f0c0da24a57365ee0cabdb493c1b3dc9d685264eb08a208f2fc86cf6.
Run `python -B scout_affine.py 12`. Explicit argument12 is REQUIRED to reproduce the observed48trials; default30 was not run. Observed terminal marker AFFINE_SCOUT_FINISHED48 (stdout has a separating space). The actual input centroids, maximal-face merging, true-edge construction and every directed physical/polar score are rebuilt as specified below. 1e-9 facet coalescence and floating signs are nomination only. Unstable/stable roots are free through dropping the smallest maximum, not fixed to the axial carriers. No strictH or fullweak audit is claimed by this scout.

## c2_inputs.py
```python
"""Literal rational half-chains from LEAD_C2 recover_lead.py (unchanged coordinates).
Names identify only geometry; this compact numerical input module is not the original audit capsule.
"""
from fractions import Fraction
import numpy as np
BASE = {
'CHAIN_G5': (100000, [[26238,-33183,-449],[28609,-32974,1377],[31068,-32622,3163],[33612,-31201,3205],[36189,-29878,3505],[38688,-28246,2635],[41231,-26550,1567],[45835,-22747,5614],[46527,-23010,-2028],[48629,-20638,-4619],[50610,-17985,-7414],[52269,-15197,-10603],[53678,-12163,-13945],[54713,-8984,-17475],[55455,-5544,-20967],[55775,-2050,-24596],[56060,1993,-27597],[55691,5844,-30890],[55645,10469,-33108],[55107,15007,-35336],[54544,19835,-36915],[53773,24810,-38099],[52919,29976,-38683],[51886,35281,-38777],[50731,40714,-38272],[49323,46257,-37298],[47569,51911,-36024],[45410,57642,-34363],[42821,63379,-32173],[39514,69077,-29756],[34279,75329,-29269],[31227,80399,-23427],[25738,85647,-19474],[19273,90649,-14772],[11522,95090,-8761]], [3500,-33292,1645]),
'MASS_G8': (100000000, [[46382421,-48054707,558586],[45825307,-47286153,14341221],[43659388,-46546805,25556964],[39844021,-46044897,35706454],[35051784,-45498814,45768406],[27669017,-45425310,54661278],[18424788,-43100472,61219880],[7322805,-41293818,65797048],[-4359348,-38109904,69035098],[-16695617,-35242555,69787437],[-29054518,-31779574,68517515],[-40647561,-34852338,62236058],[-51445987,-29826690,57895754],[-60696564,-27076840,51033398],[-68467150,-23593756,43553933],[-74584021,-19930423,35816897],[-79195792,-16457764,28023899],[-82378452,-11837101,21534194],[-84510789,-7713014,15401130],[-85777436,-3401427,10254059],[-86423556,169322,5591161],[-86593792,4578267,1821527],[-86332958,9222169,-703065],[-85730377,14055831,-2524880],[-84795921,19059376,-3880987],[-83503059,24249074,-4944952],[-81802987,29625668,-5929467],[-79623396,35202003,-6975636],[-76865659,40998378,-8146213],[-73417316,46981068,-9637455],[-69095673,53232144,-11265808],[-63662692,59870785,-12480426],[-56842647,66961336,-13139879],[-47993045,74613062,-13023721],[-34535659,83675117,-13894797]], [22268708,-57684805,40585559]),
'PAIRDELETE_G6': (1000000, [[262507,-330829,-5036],[286111,-329211,13754],[310748,-326478,33228],[336163,-312092,32053],[361913,-298813,35049],[386896,-282478,26353],[412248,-265397,15680],[459892,-224813,62243],[465796,-230476,-20073],[486725,-206800,-46244],[506507,-180228,-74215],[523069,-152283,-106117],[537181,-121804,-139465],[547451,-89970,-174774],[554765,-55584,-209769],[557648,-20819,-246362],[560748,19887,-276011],[556643,57941,-309586],[556621,104643,-331171],[550861,149772,-353987],[545521,198301,-369336],[537808,248080,-381136],[529255,299764,-386931],[518920,352822,-387802],[507346,407155,-382774],[493197,462557,-372967],[475626,519088,-360238],[453988,576378,-343663],[427970,633715,-321850],[394688,690602,-297839],[341789,753507,-293577],[311774,803917,-234779],[192098,906188,-148298],[114344,950454,-88467]], [35050,-331697,17377]),
'S3_G8': (100000000, [[26201155,-33655616,-304426],[28617265,-33120450,1376697],[31070109,-32464896,2838362],[33582821,-31157333,3228189],[36140437,-29775004,3395061],[38625047,-28153267,2649611],[41245031,-26513597,1696989],[45532784,-23509183,3302004],[46555913,-22825512,-1935077],[48530136,-20530767,-4605926],[50468319,-17885201,-7416900],[52133372,-15105116,-10589955],[53579221,-12135777,-13957049],[54656999,-8944588,-17454810],[55417423,-5517743,-20947698],[55841751,-2003352,-24528451],[56042281,2011883,-27572830],[55815392,5904673,-30817766],[55668241,10482600,-33082473],[55132940,15058351,-35217718],[54496527,19857345,-36827695],[53728630,24819086,-38021747],[52852649,29968124,-38661153],[51849348,35274959,-38751117],[50674038,40715349,-38342095],[49309121,46261199,-37347087],[47629379,51900385,-35935071],[45476226,57636209,-34285271],[42783118,63400025,-32286031],[39395404,69229508,-30210407],[35238221,75343256,-27214715],[31110825,80324988,-23490703],[25739318,85815461,-19691682],[19429416,90655782,-14560758],[11675984,95194106,-8617459]], [3489864,-33715409,1386565])
}
for g in (4,6):
    s,h,t = BASE['S3_G8']; r=10**(8-g)
    BASE['S3_G'+str(g)] = (10**g, [[round(Fraction(v,r)) for v in row] for row in h], [round(Fraction(v,r)) for v in t])

def literal(name):
    s,h,(xb,yb,zb)=BASE[name]
    rows = h + [[-x,y,-z] for x,y,z in h] + [[0,s,0],[xb,yb,zb],[-xb,yb,zb],[-xb,yb,-zb],[xb,yb,-zb]]
    return s, rows

def points(name):
    s,r=literal(name)
    return np.array(r,dtype=float)/s
```

## scout_affine.py
```python
"""Numerical full-SPD own-centred equilibrium scout on fixed literal C2 inputs.
Facet coalescence is numerical here. Never treat this scout as an exact mechanics certificate.
"""
import json, sys, os
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
from c2_inputs import points, BASE

class Body:
    def __init__(self,p):
        hull=ConvexHull(p)
        vv=np.sort(hull.vertices)
        p=np.asarray(p[vv]); hull=ConvexHull(p)
        self.p=p; self.old_vertex_ids=vv.tolist()
        tri=hull.simplices.copy()
        cross=np.cross(p[tri[:,1]]-p[tri[:,0]],p[tri[:,2]]-p[tri[:,0]])
        flip=np.sum(cross*hull.equations[:,:3],axis=1)<0
        tri[flip] = tri[flip][:,[0,2,1]]
        det=np.sum(p[tri[:,0]]*np.cross(p[tri[:,1]],p[tri[:,2]]),axis=1)
        self.volume=det.sum()/6
        self.centroid=np.sum(det[:,None]*(p[tri[:,0]]+p[tri[:,1]]+p[tri[:,2]]),axis=0)/(4*det.sum())
        self.x=p-self.centroid
        # Merge coplanar hull triangles; these inputs only have a rectangular bottom face.
        reps=[]; group=[]
        for eq in hull.equations:
            matches=[k for k,e in enumerate(reps) if np.linalg.norm(eq-e)<1e-9]
            if matches: group.append(matches[0])
            else: group.append(len(reps));reps.append(eq)
        eq=np.asarray(reps)
        self.q=eq[:,:3]/(-eq[:,3]-eq[:,:3]@self.centroid)[:,None]
        owners={}
        for t,f in zip(tri,group):
            for a,b in zip(t,np.roll(t,-1)):
                owners.setdefault(tuple(sorted((int(a),int(b)))),set()).add(f)
        edges=[]; dual=[]
        for e,fs in sorted(owners.items()):
            if len(fs)==2: edges.append(e);dual.append(sorted(fs))
            else: assert len(fs)==1
        self.e=np.array(edges,int);self.de=np.array(dual,int)
        assert len(self.x)-len(self.e)+len(self.q)==2
        self.pairs=np.r_[self.e,self.e[:,::-1]]
        self.dpairs=np.r_[self.de,self.de[:,::-1]]
        self.dx=self.x[self.pairs[:,1]]-self.x[self.pairs[:,0]]
        self.dq=self.q[self.dpairs[:,1]]-self.q[self.dpairs[:,0]]
        self.fx=self.x[self.pairs[:,0]]
        self.fq=self.q[self.dpairs[:,0]]

    def escapes(self,M):
        N=np.linalg.inv(M)
        rp=np.einsum('ij,jk,ik->i',self.fx,M,self.dx)
        rq=np.einsum('ij,jk,ik->i',self.fq,N,self.dq)
        # Cosine against directed edge is scale independent and root diagnostics are still full-face.
        rp/=np.sqrt(np.einsum('ij,jk,ik->i',self.fx,M,self.fx)*np.einsum('ij,jk,ik->i',self.dx,M,self.dx))
        rq/=np.sqrt(np.einsum('ij,jk,ik->i',self.fq,N,self.fq)*np.einsum('ij,jk,ik->i',self.dq,N,self.dq))
        up=np.full(len(self.x),-np.inf);sq=np.full(len(self.q),-np.inf)
        np.maximum.at(up,self.pairs[:,0],rp);np.maximum.at(sq,self.dpairs[:,0],rq)
        return up,sq

    def census(self,M):
        u,s=self.escapes(M)
        return {'S':np.flatnonzero(s<0).tolist(),'U':np.flatnonzero(u<0).tolist(),
                'nonroot_u_margin':float(np.sort(u)[1]),'nonroot_s_margin':float(np.sort(s)[1]),
                'V':len(u),'E':len(self.e),'F':len(s),'cy':float(self.centroid[1])}

# Lower triangular Cholesky with positive diagonal. Fix last diagonal1, no loss up to scale.
def gram(z):
    L=np.array([[np.exp(z[0]),0,0],[z[2],np.exp(z[1]),0],[z[3],z[4],1.]])
    return L@L.T

def loss(z,body,weight=1):
    u,s=body.escapes(gram(z))
    # Remove one strongest root of each type, penalize every other deficit.
    u=np.sort(u)[1:];s=np.sort(s)[1:]
    margin=1e-5
    a=np.minimum(u-margin,0); b=np.minimum(s-margin,0)
    return float(weight*(a@a)+(b@b))

def main():
    rng=np.random.default_rng(2026092301)
    out=[]
    for name in ['S3_G6','CHAIN_G5','PAIRDELETE_G6','MASS_G8']:
        body=Body(points(name)); print('INPUT',name,body.census(np.eye(3)),flush=True)
        best=(1e99,None,None)
        for i in range(int(sys.argv[1]) if len(sys.argv)>1 else 30):
            if i==0: z=np.zeros(5)
            elif i%4==0 and best[1] is not None: z=best[1]+rng.normal(size=5)*.1
            else:z=np.r_[rng.uniform(-1.5,1.5,2),rng.normal(size=3)*.6]
            fit=minimize(loss,z,args=(body,),method='Nelder-Mead',options={'maxiter':2500,'xatol':1e-9,'fatol':1e-13})
            if fit.fun<best[0]:
                best=(fit.fun,fit.x,body.census(gram(fit.x)))
                print('BEST',name,i,fit.fun,best[2],fit.x.tolist(),flush=True)
            out.append({'name':name,'trial':i,'loss':float(fit.fun),'z':fit.x.tolist(),'M':gram(fit.x).tolist(),'census':body.census(gram(fit.x))})
            if len(best[2]['S'])==len(best[2]['U'])==1:break
        with open('affine_scout.json','w') as f:json.dump(out,f,sort_keys=True,indent=2)
    print('AFFINE_SCOUT_FINISHED',len(out),flush=True)
if __name__=='__main__':main()
```
