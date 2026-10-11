# material-63d4abb4fe15

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# COORD_HULL_LP_V3_ROOTED: complete incidence-adaptive radial rooted-witness patch

Dependencies: complete HULL_LP.py from [internal-source-reference], complete RADIAL_PATCH.py from [internal-source-reference], and the exact original NC57 REPORT inputs in accepted result figure-0398. No floating descendant is an implicit input. V1 source6471bytes,SHAff8e633486cd8117106117a64c81c31a66aadac7489ee82054ae61e916420185. The V2 patch generates HULL_LP_V2.py6379bytes,SHA5afffaec9998a27a7b76165098d6d4346b127f3a796c432ea83721b3780890da.

This is a complete preserved numerical method, not a new exact construction or a completed-search claim at capture. Numerical maxima, facet merging and gamma margins are proposal gates only. Full exact rational reconstruction, true maximal incidence, actual filled centroid, strict/weak S/U/H and independent full verification remain required for any new own110.

## Motivation and scope
For radial escape f(a,b)=a.(b-a)/|a|^2, the exact identity |a|^2 f(a,b)+|b|^2 f(b,a)=-|a-b|^2<0 for distinct a,b prohibits a positive two-cycle. More generally a positive escape strictly increases radius. Greedy local escape targets can nevertheless form infeasible cycles and a numerical optimizer can approach nearly coincident polar points with tiny loss without cancelling the extra stable equilibrium. Initial V2 diagnostics found such polar two-cycles; their numerical endpoints are not themselves exact certificates. This source addresses that algorithmic limitation by constructing a root-reaching acyclic target graph at every actual-hull trial.

Reverse Dijkstra uses edge cost max(gamma-escape,0)^2+(gamma^2+1e-24)*1e-6. Every assigned parent was settled earlier, so each target path reaches the actual largest-radius root. Roots and trees refresh at EVERY trial. Primal and polar escape targets are both differentiated through the filled-solid centroid. The reported margin/loss/merit now concern selected ROOT-REACHING edges; local_escape_margin separately records the greedy all-pair maxima. Actual numerical S/U counts still use all pairs. The method preserves incidence-adaptive hull rebuilding and does NOT reintroduce frozen-triangle convexity constraints. It is a search restriction/heuristic, not a geometric impossibility theorem or a proof of convergence.

## Exact source reconstruction
Save the following as ROOTED_PATCH.py, UTF8 with one final newline. Observed local source1762bytes,SHA989c7f64e46a4af35cb5d17ef9c1aba8f3ab0a6c2959e462679aec228cf0560f. Execute `python -B -S ROOTED_PATCH.py HULL_LP_V2.py HULL_LP_V3.py`. Generated complete source HULL_LP_V3.py7153bytes,SHAd049cd5a5cb87a97c0a9276139d6576931bf71fb49427974753be1d15ff1a98a. Expected terminal COORD_HULL_LP_ROOTED_PATCHED followed by7153 and thatSHA. The full source chain and NC57 exact input capsule are required, not this patch alone.

Run the unchanged seven-argument CLI `python HULL_LP_V3.py REPORT.json NEW_OUT steps gamma seed perturb initial_trust`. CPython3.13.5,NumPy2.3.5,SciPy1.17.0,Torch2.10.0+cpu,CPU binary64,one thread,assertions enabled. Each finite run must separately preserve its options/checkpoints or verified deterministic reproduction; this material does not invent an observed endpoint. A completed run emits COORD_HULL_LP_FINISHED. The numerical root/facet indices are newly rebuilt hull indices, NOT the parent's REPORT facet labels; owners must be tracked explicitly.

```python
#!/usr/bin/env python3
"""Exact patch: radial hull LP with acyclic actual-root-reaching witnesses."""
from pathlib import Path
import hashlib,sys
raw=Path(sys.argv[1]).read_bytes()
assert hashlib.sha256(raw).hexdigest()=='5afffaec9998a27a7b76165098d6d4346b127f3a796c432ea83721b3780890da'
s=raw.decode()
helper='''def rooted_targets(A,root,gamma):
 # Reverse Dijkstra: every parent was settled earlier; strictly positive costs.
 cost=np.maximum(gamma-A,0)**2+(gamma*gamma+1e-24)*1e-6
 n=len(A);distance=np.full(n,np.inf);distance[root]=0.;done=np.zeros(n,dtype=bool);parent=np.full(n,-1,dtype=int)
 for _ in range(n):
  k=int(np.argmin(np.where(done,np.inf,distance)));assert np.isfinite(distance[k]);done[k]=True
  cand=cost[:,k]+distance[k];better=(~done)&(cand<distance)
  distance[better]=cand[better];parent[better]=k
 ids=np.array([i for i in range(n) if i!=root]);assert np.all(parent[ids]>=0)
 return ids,parent[ids]

'''
s=s.replace('def state(P,gamma):',helper+'def state(P,gamma):')
a="ut=aU[ui].argmax(1);st=aS[si].argmax(1);e=np.r_[u[ui],s[si]];d=np.maximum(gamma-e,0)"
b="ui,ut=rooted_targets(aU,ru,gamma);si,st=rooted_targets(aS,rs,gamma);e=np.r_[aU[ui,ut],aS[si,st]];d=np.maximum(gamma-e,0)"
assert s.count(a)==1;s=s.replace(a,b)
a="margin=float(e.min()),loss=float(d@d)"
b="margin=float(e.min()),local_escape_margin=float(np.r_[u[ui],s[si]].min()),loss=float(d@d)"
assert s.count(a)==1;s=s.replace(a,b)
a="version='COORD_HULL_LP_V2_RADIAL_NO_RENORMALIZE'"
b="version='COORD_HULL_LP_V3_RADIAL_ROOTED',tree_cost='max(gamma-escape,0)^2+(gamma^2+1e-24)*1e-6',tree_refresh='every_trial'"
assert s.count(a)==1;s=s.replace(a,b)
Path(sys.argv[2]).write_text(s)
print('COORD_HULL_LP_ROOTED_PATCHED',len(s.encode()),hashlib.sha256(s.encode()).hexdigest())
```
