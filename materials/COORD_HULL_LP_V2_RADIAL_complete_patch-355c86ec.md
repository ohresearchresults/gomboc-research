# material-355c86ecf10f

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# COORD_HULL_LP_V2_RADIAL: complete runnable exact patch

Dependency: full HULL_LP.py from immutable material [internal-source-reference] (6471bytes,SHAff8e633486cd8117106117a64c81c31a66aadac7489ee82054ae61e916420185) and the same literal NC57 exact inputs figure-0398. No other implicit dependency. This is a preserved numerical method, not a new exact body or completed search result at capture.

Four completed initial V1 trials encountered a plateau/ill-conditioned near-facet geometry. C372 seed37201/gamma.001 ended S2U2 after102iterations; seed37202/gamma.0001 S2U1 after31. C378 seed37801/gamma.001 ended S2U1 after40, merit~.02469348; seed37802/gamma.0001 S2U1 after35,merit~.01998910. All perturb0,initialtrust.005,stepscap300. These are finite unsuccessful numerical trials, no exclusions. Exact observed checkpoints are being preserved separately; source alone is not a frozen optimizer output.

V2 replaces angle(q,q'-q) by f=q.(q'-q)/||q||^2, whose sign gives the same escape condition, but no division by the small inter-normal distance remains. Positive gamma remains essential; its numerical size now measures RELATIVE RADIAL gain, not angle, so V1/V2 loss or margin magnitudes cannot be compared directly. Every proposal still rebuilds actual hull and filled centroid. Accepted coordinates are no longer recentered/RMS-rescaled after each step, avoiding a source of floating-point merit changes in ill-conditioned facets; the once-only initial normalization remains. This is not a proof that all numerical conditioning is fixed. Candidate count/margin gates still require full exact checks.

Save this source as RADIAL_PATCH.py,911bytes,SHA8963c1281270427bb580315cb42eb5cea7475fca1095589167861b0b5fda9bb1. Run `python -B -S RADIAL_PATCH.py HULL_LP.py HULL_LP_V2.py`; expected terminal `COORD_HULL_LP_RADIAL_PATCHED 6379 5afffaec9998a27a7b76165098d6d4346b127f3a796c432ea83721b3780890da`. Generated complete source HULL_LP_V2.py6379bytes,SHA5afffaec9998a27a7b76165098d6d4346b127f3a796c432ea83721b3780890da. Run the same seven-argument CLI as V1. Frozen outputs must identify every chosen gamma/seed/perturb/steps/trust value. Environment remains CPython3.13.5/NumPy2.3.5/SciPy1.17.0/Torch2.10.0+cpu,threads1,binary64,assertions.

```python
#!/usr/bin/env python3
"""Exact patch from preserved HULL_LP_V1 to radial witness HULL_LP_V2."""
from pathlib import Path
import hashlib,sys
p=Path(sys.argv[1]).read_bytes()
assert hashlib.sha256(p).hexdigest()=='ff8e633486cd8117106117a64c81c31a66aadac7489ee82054ae61e916420185'
s=p.decode()
pairs=[
 ('return (a*d).sum(1)/(torch.linalg.vector_norm(a,dim=1)*torch.linalg.vector_norm(d,dim=1))','return (a*d).sum(1)/(a*a).sum(1)'),
 ("a=np.einsum('ik,ijk->ij',W,D)/(r[:,None]*dn);a[bad]=-np.inf","a=np.einsum('ik,ijk->ij',W,D)/(r[:,None]**2);a[bad]=-np.inf"),
 ("P=trial-np.array(sr['centroid']);P/=np.sqrt((P*P).sum(1).mean())","P=trial"),
 ("version='COORD_HULL_LP_V1'","version='COORD_HULL_LP_V2_RADIAL_NO_RENORMALIZE'"),
]
for a,b in pairs:
 assert s.count(a)==1,a
 s=s.replace(a,b)
Path(sys.argv[2]).write_text(s)
print('COORD_HULL_LP_RADIAL_PATCHED',len(s.encode()),hashlib.sha256(s.encode()).hexdigest())
```
