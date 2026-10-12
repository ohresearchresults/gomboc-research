"""Optional finite numerical reruns. Exact REPLAY is independent of these."""
import os,sys,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parent
mode,exact_output,new_output=sys.argv[1:]
commands={
 'reference6':['patch_search.py','ref','4'],
 'reference12':['atlas_search.py','ref','8'],
 'guard':['guard_search.py'],
 'local_mass':['local_mass.py'],
 'two_roots':['tworoot_search.py'],
 'free_metric':['free_metric_search.py'],
 'shift124':['shift_compensate.py']}
assert mode in commands
out=Path(new_output).resolve();assert not out.exists()
env=os.environ.copy();env['OPENBLAS_NUM_THREADS']='1';env['OMP_NUM_THREADS']='1';env['NH72_BASE_REPORT']=str(Path(exact_output).resolve()/'BASE/B.json');env['NH72_LOCAL_MASS_CHECKPOINT']=str(ROOT/'LOCAL_MASS_CHECKPOINT.json')
command=commands[mode];args=[sys.executable,str(ROOT/command[0]),*command[1:],str(out)]
if mode=='free_metric':args.append('5')
subprocess.run(args,env=env,check=True)
