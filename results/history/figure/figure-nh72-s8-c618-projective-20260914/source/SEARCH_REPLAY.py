"""Re-execute one preserved finite NUMERICAL search from the exact coarsened source.
Usage: python SEARCH_REPLAY.py EXPERIMENT_NAME exact-replay-output fresh-search-output
Floating paths can vary by BLAS/solver version; they are not exact acceptance proofs.
"""
from pathlib import Path
import json,sys,subprocess
R=Path(__file__).resolve().parent
if len(sys.argv)!=4:raise SystemExit(__doc__)
name=sys.argv[1];base=Path(sys.argv[2]).resolve();out=Path(sys.argv[3]).resolve()
exp=json.loads((R/'EXPERIMENTS.json').read_text())[name]['config'].copy()
if name.startswith(('direct','forest')):script='centroid_metric.py'
elif name.startswith('iso_'):script='search_family.py'
elif name.startswith('monitor'):script='monitored_search.py'
elif name.startswith('turnover'):script='root_turnover.py'
elif name.startswith('pullback'):script='pullback_centroid.py'
elif name.startswith('psd'):script='metric_cone.py'
elif name.startswith('milp'):script='metric_milp.py'
elif name.startswith('guard'):script='guarded_continue.py'
else:raise ValueError(name)
report=base/Path(exp.pop('report')).parent.name/'A.json';exp.pop('out')
if not report.exists():
 # The optional DEL84 input is reproduced without altering n_supports or anchor137.
 assert report.parent.name=='DEL84'
 from RECONSTRUCT import recover
 from endpoint import dump
 import check_A
 H=recover(json.loads((R/'BASE_GENERATOR.json').read_text()))['H'];raw={'H':[h for i,h in enumerate(H) if i!=84]}
 report.parent.mkdir(parents=True,exist_ok=False);dump(report.parent/'raw.json',raw);dump(report,check_A.run(raw))
command=[sys.executable,str(R/'numerical'/script),str(report),str(out)]
for key,value in exp.items():command += ['--'+key,str(value)]
subprocess.run(command,check=True)
