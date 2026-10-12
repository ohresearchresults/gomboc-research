# material-56d0fc2042ea

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Short root-escaping polar chains followed by true mass closure

Finite constructive scout, not a universal obstruction. Source endpoint is the exact C426 G12 capsule [internal-source-reference], dependent on RECOVER_C508.py [internal-source-reference]. Complete normal/persistence optimizer code is [internal-source-reference], whose earlier empirical prose is corrected by [internal-source-reference]. Newly exact nonwinner output SHORT4_C420_G12/G6 is completely recoverable from [internal-source-reference] plus att66 only. It hasV140/E210/F72,C420,strict(1,31,30),weak000,zero real-edge primitives0/0,stableinput0. Canonical own110/weak000 remainsC622.

## Method and geometric scope
Remove all19 inactive constraints from C426. At its dominant physical peak u, define q=alpha*u/(u.u). Between the stable root normal r and q, use N equal angular increments and N equal logarithmic radial increments. If ||q||/||r||<cos(phi/N)^N, every new normal has a strict escape toward its predecessor at the old origin. Old normals retain their S1 escape; adding these H-constraints therefore preserves S1 at that origin, NOT necessarily at the new homogeneous center. Add the new inequalities, recompute the full hull and its actual filled center, then vary all nonroot normals using the full analytic-gradient mass-constrained optimizer. The source has at most73+N facets, so for N<=8 the family has C<=474 independent of triangulation. No density change is allowed.

The finite raw chain scout used all pairs N in{3,4,6,8},alpha in{1.05,1.2,1.4}. The capacity condition rejected(3,1.4),(4,1.4). The ten feasible seeds gave many stable equilibria at the new center: S36 to49, despite S1 at the old origin. For N4,alpha1.2, actual centroid=(-.012653579556896792,-.015032991807889586,-.02694048456456466),numericalC432/S48/U18,value.25946571697106874. This is a direct finite illustration that polar escape at the old center is not enough.

Mass closure was attempted for N3/alpha1.05,N4/alpha1.2,N6/alpha1.4. Full-active parameters bound.3,eps1e-6,freevolume,sumobjective,ftol1e-11; first two max1000iterations, lastmax500. All three ultimately produced terminal success=True/Optimization terminated successfully receipts. The N6 launch in the initial three-command shell timed out before a receipt; it was restarted as the explicit500-iteration run. No still-running local process was used as evidence.

N3:1948evaluations, best recorded iteration746,C426,S1,U29,value.17401873823007583, actualcentroidnorm<1.3e-11,minimumflow-6.032907506892116e-10; this numerically feasible best was not promoted as an exact endpoint. Terminal value.17401873824422523 and tighter centroid/flow were observed. Dominant numerical bar .11406497266121701.
N4:351evaluations,best iteration249,C420,S1,U31,value.16744951927988713,actualvolume.783585870302649,centroid(2.248307251169164e-14,-2.5539998485636864e-14,4.540116200869184e-14),minimumflow-9.947598300641403e-13. Largest bar .11210279166461684,peak91,death78--81,48dyingvertices. G12 rounding and exact rational ties-even G6 both passed full true complex/filled mass/strict+weak census and separate threeaxisprojectedmass equality. Actual G12volume.7835858703026649,centroid(2.3953623449361008e-14,-4.678951977535019e-14,-5.98205676996172e-14); G6volume.7835859311173672,centroid(-2.2000819203003852e-8,5.729983098477844e-9,1.8112857038946233e-8). Polar maximum shortest depth58 for both. Exact identity and hashes are in [internal-source-reference], not in the floating search trace.
N6:236evaluations,bestiteration183,C426,S1,U30,value.20521917845143017,volume.7548584191836785,centroid(1.2166838482088263e-14,3.775052621217046e-14,3.842531849601821e-13),minimumflow-2.2444268665822165e-12. Not promoted as exact.

Conclusion: these SHORT pole-to-peak chain seeds can be mass-closed and modestly reduce the numerical persistence sum(C426.1719997240 to C420.1674495193), but did NOT remove the deep extra basin or attain110. Stronger raw cuts do not automatically improve the mass-closed basin. This is a bounded scout, not a proof against all finite chains. The exact C420 body and complete source remain useful nonrecord continuation inputs.

## Complete runnable seed generator: short_chain_cut.py

```python
"""Finite whole-basin polar-chain seed from the exact C426 G12 capsule.
Needs FULL92_CYCLE6_G12.json from exact recovery and the complete source
units chain_persistence.py, full_active_persistence.py. No random inputs.
Only writes numerical seeds, never certifies a new exact body.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import json,hashlib,argparse
from pathlib import Path
import numpy as np
from full_active_persistence import FullActive

def construct(n,alpha,output):
 raw=Path('FULL92_CYCLE6_G12.json').read_bytes()
 assert hashlib.sha256(raw).hexdigest()=='5aa97e57704f677ccbb94948894789582c2fba1d75221e7f51ac5330c89cb144'
 cp=json.loads(raw);normals=np.array(cp['new_normals'],float)/cp['grid']
 Path('CUT_BASE_NORMALS.json').write_text(json.dumps({'normals':normals.tolist()}))
 m=FullActive(source='CUT_BASE_NORMALS.json');a=m.initial
 b=max(a['bars'],key=lambda b:b['delta']);u=a['points'][b['peak']]-a['centroid']
 root=normals[0];r0=np.linalg.norm(root);q=alpha*u/(u@u);rn=np.linalg.norm(q)
 e0=root/r0;en=q/rn;phi=np.arccos(np.clip(e0@en,-1.,1.))
 capacity=np.cos(phi/n)**n;assert rn/r0<capacity,'no equal-step root-escaping chain'
 indices=[0]+[i for i in a['active'] if i!=0]
 ns=normals[indices].tolist()
 for i in range(1,n+1):
  t=i/n;direction=(np.sin((1-t)*phi)*e0+np.sin(t*phi)*en)/np.sin(phi)
  radius=r0*(rn/r0)**t;ns.append((radius*direction).tolist())
 Path(output).write_text(json.dumps({'normals':ns,'original_input_ids':None,'source':'exact C426 G12','chain_N':n,'alpha':alpha,'removed_inactive':92-len(indices)},sort_keys=True,indent=2)+'\n')
 d=FullActive(source=output);s=d.summary(d.start.ravel());s.pop('bars')
 return {'N':n,'alpha':alpha,'capacity':float(capacity),'radial_ratio':float(rn/r0),'seed':s}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--N',type=int,default=4);p.add_argument('--alpha',type=float,default=1.2);p.add_argument('--out',default='SHORT_CHAIN_SEED.json');a=p.parse_args();print(json.dumps(construct(a.N,a.alpha,a.out)))
```

Reproduction commands (Python3.13.5,NumPy2.3.5,SciPy1.17.0,oneBLASthread):

    python RECOVER_FULL92_C426.py
    python short_chain_cut.py --N 3 --alpha 1.05 --out CUT_N3_A1_05.json
    python full_active_persistence.py --source CUT_N3_A1_05.json --bound 0.3 --steps 1000 --out MASSCUT_N3_A1_05
    python short_chain_cut.py --N 4 --alpha 1.2 --out CUT_N4_A1_2.json
    python full_active_persistence.py --source CUT_N4_A1_2.json --bound 0.3 --steps 1000 --out MASSCUT_N4_A1_2
    python short_chain_cut.py --N 6 --alpha 1.4 --out CUT_N6_A1_4.json
    python full_active_persistence.py --source CUT_N6_A1_4.json --bound 0.3 --steps 500 --out MASSCUT_N6_A1_4

Floating optimizer paths may vary with environment. For the exact durable C420 endpoint skip optimization and run python RECOVER_SHORT4_C420.py from [internal-source-reference] beside att66 dependency. Observed terminal SHORT4_C420_EXACT_NONWINNER_PASS G12/G6 then SHORT4_C420_RECOVERY_COMPLETE. The script embeds all77 supplied G12 rational normals and exact G6 rounding, not a hash-only checkpoint.
