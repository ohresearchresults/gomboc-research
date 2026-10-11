# material-713ebf374485

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced; request-derived-context-removed.

---

# Recovery capsule part 3/3 — FULL_AFFINE_DLV_FINITE_SCOUTS

Completes the NUMERICAL producing-method capsule with part1 [internal-source-reference] and part2 [internal-source-reference]. This is not an accepted110 construction or a universal affine exclusion. Literal local source/JSON files were reread directly before this ledger; transient context synopses with different hashes, trial indices, counts or bounds are NOT authoritative. In particular the mobile campaign did not produce a feasible S23/U1 improvement, the MILP pilot had FOUR time-limit/no-primal rows, and raw DLV facets/vertices are numerically symmetry-sensitive.


## Recovery and numerical verification
Save the code below as dlv_seed_scout.py, UTF-8/LF final newline:3192bytes,SHA25612bddec5a362d942af6ac44943c2214956b4ff665135db83751cb6925b6cccdc. Requires complete c2_inputs.py/scout_affine.py from part1. All seven producing sources across parts1–3 are complete and have literal inputs, every nondefault parameter and seeded RNG states. CPython3.13.5,NumPy2.3.5,SciPy1.17.0,binary64, BLAS/OMP/MKL thread count1 were observed. Run `python -B scout_affine.py 12`, `python -B guard_affine.py`, `python -B mobile_guard_affine.py`, `python -B dlv_seed_scout.py` with OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1. Expected terminal counts are48,32,64,3, with markers from their literal sources. Do not run the full disjunctive main and call it a replay of the interrupted four-row pilot.

Observed output receipts (not a promise of bitwise optimizer stability across platforms): affine_scout.json43494bytes SHA8466cf12de60f71fd175bacbdf420b4c2b423e16095872dcad89bf2ea5ba012d; guard_affine.json28150bytes SHA0fd1145c375f9349dbf21aef79ea6201b3d82df008fe7cce64adfd34525598e7; mobile_guard_affine.json54736bytes SHA13f72de1895322d62ee92a55c19b29fe90e5680d60c268ef2dd261b53d86beeb; disjunctive_affine.json837bytes SHAee1c1a7386022c8deda58f8c375c56b09fb84f37bf06e9f3be4de42069dada38; dlv_seed_scout.json25822bytes SHAbc93a42850bf3b1d2c508bb78d85fee44789fb777318fb7dd8f900d33ab5caeb. These hashes identify producing ledgers; no affine metric is promoted as an exact object on the strength of a hash or the local files. The smallest complete deterministic input/source is preserved here independently of those sandbox files.

## Observed finite affine ledger
All48 unguarded trials ran;12 each for S3_G6,CHAIN_G5,PAIRDELETE_G6,MASS_G8. Lowest loss by family: CHAIN trial10,5.6021540573025e-6,S3/U3; MASS trial8,2.2486780784950696e-6,S3/U3; PAIR trial8,9.869460116335313e-6,S3/U3; S3 trial8,1.1466829516117147e-7,S3/U2. The tiny losses use highly ill-conditioned full-SPD metrics. Neither a vanishing cosine loss nor these floating S/U counts establish convergence to110.

All32 fixed-U1 guard endpoints satisfy the recorded numerical slack cutoff−1e-9; best CHAIN trial4 loss.03579640504236608,S5/U1; MASS trial0 .04422524848531115,S25/U1; PAIR trial1 .03904533920597576,S5/U1; S3 trial5 .001408906610125584,S3/U1. Fixed original escape choices restrict this campaign to one U1 cell per shape.

All64 mobile-U1 guard trials ran. Numerically feasible by slack≥−1e-9: CHAIN4/16,best trial3 .03631158707393474,S5/U1; MASS4/16,best trial11 .04422524848530697,S25/U1; PAIR8/16,best trial10 .039057424117434826,S5/U1; S3 8/16,best trial3 .0013620550971222166,S3/U1. Other rows are rejected guard failures, even when their raw counts/loss appear more attractive. The complete source allows edge and root turnover. This finite result does not close full-SPD U1 geometry.

Literal observed disjunctive pilot ledger (save this exact formatted text with no final newline to recover disjunctive_affine.json837bytes):
```json
[
  {
    "cuts": 11,
    "message": "Time limit reached. (HiGHS Status 13: model_status is Time limit reached; primal_status is None)",
    "name": "S3_G6",
    "root": 68,
    "status": 1,
    "trial": 0
  },
  {
    "cuts": 16,
    "message": "Time limit reached. (HiGHS Status 13: model_status is Time limit reached; primal_status is None)",
    "name": "S3_G6",
    "root": 68,
    "status": 1,
    "trial": 1
  },
  {
    "cuts": 13,
    "message": "Time limit reached. (HiGHS Status 13: model_status is Time limit reached; primal_status is None)",
    "name": "S3_G6",
    "root": 26,
    "status": 1,
    "trial": 0
  },
  {
    "cuts": 3,
    "message": "Time limit reached. (HiGHS Status 13: model_status is Time limit reached; primal_status is None)",
    "name": "S3_G6",
    "root": 63,
    "status": 1,
    "trial": 0
  }
]
```

## DLV finite halfspace scout: exact binary64 input checkpoints, numerical controls
The code uses radial formulas(1)–(5) from Domokos–Lángi–Várkonyi, arXiv2112.06079v2 / DOI10.1007/s00605-023-01847-w. The primary paper establishes allowable Cn/Dn symmetry and existence, NOT an E≤249 body. Here the radial surface is only a source of77 nominal support normals; there is no claim that every sampled parameter satisfies the paper's small-parameter convexity theorem or has its smooth centre. Only the bounded finite intersection at its actual volume centroid is evaluated. Its centre is recomputed, never set to the smooth source's centre.

The three retained parameter arrays, in exact Python binary64 repr and order [c,d,shift,warp,cap,aspect], are:
0:[0.348924535735755,0.430846292422864,0.09177882694238823,1.1380793703098433,0.919385164669734,0.5366341588107586]
1:[0.2286120132045184,0.35184658419274134,-0.05235369067970339,1.2729454408210938,0.8947215520204572,0.5461429524620107]
2:[0.21075988583083555,0.32866098715047964,-0.06079203628228995,1.1026087116023102,0.9851448939381748,0.5456455760197303]
They reconstruct the nominal halfspaces directly with planes(z), without rerunning differential evolution. Seeded DE remains available as the complete producing method.

Actual retained numerical census/loss: trial0 V104/E159/F57,C318,S5/U5,4.403216859125533e-6,cz≈.26859536062394807; trial1 V107/E162/F57,C324,S5/U5,2.6320101310806837e-6,cz≈.2151034538122895; trial2 V106/E160/F56,C320,S4/U7,8.899476177442652e-7,cz≈.16300768516909206. No strictH/fullweak audit was performed by this scout. Finite differences only preserve reflection symmetry to floating precision and create very small bevels/edges; coalescence affects numerical incidence and scores. These are nomination controls, not exact polyhedron classes. Explicit symmetry enforcement and rational freezing are distinct subsequent geometries, not silent changes to these checkpoints.

## dlv_seed_scout.py
```python
"""Numerical finite H-body scout inspired by Domokos-Langi-Varkonyi 2112.06079v2.
Uses their equations (1)-(5), not a claimed certified smooth or finite winner.
Only the final finite convex intersection at its actual volume centroid is counted.
A south supporting plane and four north apex planes control critical carriers.
Every body has <=77 input planes, hence E<=225 if full dimensional and bounded.
"""
import numpy as np,json
from scipy.spatial import HalfspaceIntersection,ConvexHull,QhullError
from scipy.optimize import differential_evolution
from scout_affine import Body

def F(x,c):return (c*x*x+(1-c)*(1-x)**2*c*x/(c+x))/(c*x+(1-c)*(1-x)**2)
def radial(theta,phi,c,d):
 f=np.pi*F(theta/np.pi+.5,c)-np.pi/2
 g=-(np.pi*F(-theta/np.pi+.5,c)-np.pi/2)
 u=np.cos(phi)**2*np.cos(f)**2;v=np.sin(phi)**2*np.cos(g)**2
 return 1+d*(u*np.sin(f)+v*np.sin(g))/(u+v)

def planes(z):
 c,d,shift,warp,cap,aspect=z
 # Nine latitude levels and eight longitude directions. A D2 rather than axisymmetric set.
 s=np.linspace(-.9,.9,9);theta=np.arcsin(np.tanh(warp*np.arctanh(s)))+shift*(1-s*s)
 phi=np.arange(8)*np.pi/4+np.pi/8
 t,p=np.meshgrid(theta,phi,indexing='ij');t=t.ravel();p=p.ravel()
 r=radial(t,p,c,d);eps=1e-5
 rt=(radial(t+eps,p,c,d)-radial(t-eps,p,c,d))/(2*eps)
 rp=(radial(t,p+eps,c,d)-radial(t,p-eps,c,d))/(2*eps)
 u=np.c_[np.cos(t)*np.cos(p),np.cos(t)*np.sin(p),np.sin(t)]
 et=np.c_[-np.sin(t)*np.cos(p),-np.sin(t)*np.sin(p),np.cos(t)]
 ep=np.c_[-np.sin(p),np.cos(p),np.zeros(len(p))]
 n=u-(rt/r)[:,None]*et-(rp/(r*np.cos(t)))[:,None]*ep
 h=r.copy()
 # Physical diagonal map with xy reciprocals changes geometry but preserves D2 symmetry.
 n[:,0]/=aspect;n[:,1]*=aspect
 # Four faces concurrent at the north axial unstable carrier.
 phi4=np.arange(4)*np.pi/2+np.pi/4
 nt=np.c_[np.cos(phi4)*cap,np.sin(phi4)*cap,np.ones(4)]
 nt[:,0]/=aspect;nt[:,1]*=aspect
 n=np.r_[n,nt,[[0,0,-1]]];h=np.r_[h,np.full(4,1+d),1-d]
 return n/h[:,None]

def assess(z,save=False):
 try:
  q=planes(z)
  pts=HalfspaceIntersection(np.c_[q,-np.ones(len(q))],np.zeros(3)).intersections
  b=Body(pts);u,s=b.escapes(np.eye(3))
  # Full actual-centre maximal complex, no raw duplicate input-support self escapes.
  du=np.minimum(np.sort(u)[1:]-1e-5,0);ds=np.minimum(np.sort(s)[1:]-1e-5,0)
  loss=float(du@du+ds@ds)
  return loss,{'z':np.asarray(z).tolist(),'loss':loss,'census':b.census(np.eye(3)),'centroid':b.centroid.tolist(),'volume':float(b.volume),'planes':q.tolist()} if save else None
 except (QhullError,np.linalg.LinAlgError,ValueError,FloatingPointError):return 1e3,None

def main():
 out=[];rng=np.random.default_rng(2026092305)
 bounds=[(.02,.95),(.005,.8),(-.15,.15),(.55,1.8),(.05,1.2),(.5,2.)]
 for trial in range(3):
  f=differential_evolution(lambda z:assess(z)[0],bounds,seed=int(rng.integers(2**31)),popsize=6,
                           maxiter=100,polish=False,tol=1e-8,workers=1,updating='immediate')
  _,row=assess(f.x,True);out.append(row)
  print('DLV_FINITE',trial,row['loss'],row['census'],row['z'],flush=True)
  with open('dlv_seed_scout.json','w') as g:json.dump(out,g,sort_keys=True,indent=2)
 print('DLV_FINITE_H_SCOUT_FINISHED',len(out),flush=True)
if __name__=='__main__':main()
```
