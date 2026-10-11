"""Rechart the exact E110 retired body around the previously certified reference.
Then deform real filled geometry while separately minimizing own-centroid distance.
"""
import sys,json,numpy as np,jax
from scipy.linalg import svdvals
from gmpy2 import mpq
from canonical_reference_atlas_threshold import ROOT,make,Chart
from canonical_reference_mass_closure import run
from geometry import angular_scores
f=ROOT/'artifacts/canonical_atlas/reference110_C220';ref=json.loads((ROOT/'artifacts/reference110_exact_C490/audit.json').read_text());center=np.array([float(mpq(v)) for v in ref['reference_center']]);src=ROOT/'artifacts/reference_retirement_C490/exact_final/audit.json';make(src,f,center,quality_floor=.01);c=Chart(f);g=c.graph(c.q);J=np.asarray(jax.jacfwd(c.reconstruct)(c.q)).reshape(-1,len(c.q));sv=svdvals(J);report=dict(depth=c.meta['max_depth'],condition=float(sv[0]/sv[-1]),reconstruction_error=float(abs(np.asarray(c.reconstruct(c.q))-c.A).max()),minimum_noncontact=g['minimum'],actual_centroid=g['c'].tolist(),refS=int((angular_scores(g['Y']).max(1)<0).sum()),refU=int((angular_scores(g['X']).max(1)<0).sum()));(f/'check.json').write_text(json.dumps(report,indent=2)+'\n');np.save(f/'initial_q.npy',c.q);print('SMALL_REFERENCE_CHART',report,flush=True);run(f,f/'mass_closure',f/'initial_q.npy',iters=2000)
