"""Optional finite numerical experiments. Requires NumPy2.3.5/SciPy1.17.0.
The exact construction does not depend on repeating these floating searches.
"""
import os,sys,json,subprocess
from pathlib import Path
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;mode=sys.argv[1];data=Path(sys.argv[2]).resolve();out=Path(sys.argv[3]).resolve();base=data/'BASE/B.json';gen=R/'BASE_GENERATOR.json'
if mode in ['fan_physical','fan_metric']:
 import CRITICAL,check_B
 d=json.loads(base.read_text());p=json.loads((R/'OLD_PARAMETERS.json').read_text());raw,_=CRITICAL.build(d,p);a=check_B.run(raw);old=data/'NUMERICAL_OLD_PARENT.json';old.write_text(json.dumps(a))
 args=['fan_search.py',base,old,mode.split('_')[1],'8',out]
elif mode in ['contact_physical','contact_metric']:args=['interface_search.py',base,gen,mode.split('_')[1],'6',out]
elif mode=='mass_energy':args=['interface_mass.py',base,gen,out]
elif mode=='guarded':args=['guarded_interface.py',base,gen,R/'CHECKPOINT.json',out]
else:raise ValueError('Unknown finite experiment')
subprocess.run([sys.executable,str(R/args[0]),*map(str,args[1:])],check=True,cwd=R)
