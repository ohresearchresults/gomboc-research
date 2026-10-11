"""Floating derivative checks and a fixed-output tangent-slice diagnostic.
Not a rigorous interval singular-value estimate and not a feasible-cone exclusion.
Inputs: exact source root, checkpoint directory, absent output directory.
Uses the complete included continuation source to avoid divergent formula copies.
"""
import json,sys
from pathlib import Path
assert len(sys.argv)==4
script=Path(__file__).with_name('close_mass_pc_tiny.py')
text=script.read_text();needle='for it in range(a.steps):';assert text.count(needle)==1
prefix=text[:text.index(needle)];exec(compile(prefix,str(script),'exec'))
st=state(y);W,_,_,E=linear(st);J=st['refJ'][st['refvals']<1e-6]@W
U,ss,Vt=np.linalg.svd(J,full_matrices=True);rank=int((ss>ss[0]*1e-10).sum());Z=Vt[rank:].T;C=E@Z;d=-Z@np.linalg.lstsq(C,st['r'],rcond=1e-11)[0]
rng=np.random.default_rng(14094950);errors=[];wi=st['witnesses']
for _ in range(3):
 v=rng.standard_normal(len(y));v/=np.linalg.norm(v);eps=1e-7
 sp=state(y+eps*v,False,wi);sm=state(y-eps*v,False,wi)
 er=float(np.max(np.abs((sp['refvals']-sm['refvals'])/(2*eps)-st['refJ']@v)));em=float(np.max(np.abs((sp['r']-sm['r'])/(2*eps)-st['dcg']@v)))
 assert er<2e-6 and em<1e-7,(er,em);errors.append(dict(reference_max_error=er,mass_max_error=em))
report=dict(status='NUMERICAL_DERIVATIVES_AND_TANGENT_SLICE_ONLY',active_rows=len(J),active_rank=rank,effective_dimension=W.shape[1],tangent_dimension=Z.shape[1],mass_tangent_singular_values=np.linalg.svd(C,compute_uv=False).tolist(),active_smallest_singular=float(ss[-1]),full_closure_tangent_norm=float(np.linalg.norm(d)),full_closure_tangent_max=float(np.max(np.abs(d))),full_closure_tangent_mass_residual=float(np.linalg.norm(E@d+st['r'])),all_escapes_min_linear=float(np.min(st['refvals']+st['refJ']@W@d)),derivative_errors=errors,seed=14094950,finite_difference_epsilon=1e-7,fixed_output_threshold=1e-6,rank_relative_cut=1e-10)
(a.out/'TANGENT.json').write_text(json.dumps(report,sort_keys=True,separators=(',',':')));print(json.dumps(report),flush=True)
