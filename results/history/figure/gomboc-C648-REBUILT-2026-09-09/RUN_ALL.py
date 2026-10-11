from pathlib import Path
import shutil,subprocess,sys
R=Path(__file__).resolve().parent
for tag in ['C648_REBUILT_R7','C648_REBUILT_R12','C648_DIRECT_SEED_NONWINNER']:
 p=R/tag
 for name in ['RECONSTRUCT.py','check_A.py','check_B.py','EXTRA.py','ARCHITECTURE.py']:shutil.copyfile(R/name,p/name)
 shutil.copyfile(R/'EXACT_REPLAY.py',p/'REPLAY.py')
 subprocess.run([sys.executable,'-S',str(p/'REPLAY.py')]+(['--cold'] if '--cold' in sys.argv else []),cwd=p,check=True)
print('NEW_C648_R7_R12_AND_211_SEED_SOURCE_ONLY_ALL_NINE_RECORDS_EACH_PASS',flush=True)
