"""Source-only or frozen replay of NEW nine-pole shadow-graph exclusions.
Save all six source units together, UTF-8/LF/final LF.
Full: python -S replay.py. Frozen: python -S replay.py check.
The 281 parent matrices are NOT a reconstruction input and are NOT replayed.
"""
from pathlib import Path
import hashlib,os,subprocess,sys
assert __debug__
S={'inputs.py': [1569, 'f268a0f9923c2c74b6b8b1c14a542e0b6b2e6b59fe80883ae983a02f382e841e'], 'make.py': [5786, '3e11bedf8f61ba71c028b374bd08f97d0b41b302f5bc1af7ea879a4a128cdc84'], 'check.py': [3973, '3b8c45780c9441d26bb806a77a533cb6e47cb5f425cfc8ea02bcd46caaa2b9eb'], 'cover.py': [5016, '1308a7db5d3059b3489e754476666db6328ee8d1155bd2f00754086877d900c8'], 'ablation.py': [1384, 'ef05b97ab9ffc5952ab4034fe11634c9f1a2a91002489e19546918df47b7122d']}
O={'shadow_exact.json': [251836, '1cf29f366fc666b1e41fd8f8a9a7df3739123a3ba0701c93f3fb13d2c31efd99'], 'shadow_verified.json': [820, '97f5dc06484139d4a383ca1b42aec9e1f033102ebaac6aa3fa1db1914708ee81'], 'shadow_cover.json': [10036, '5bad625f9a57c514229749b6d6b4b2e2f2d4a1bed1d2f4a6c39ade6c120fff0b'], 'omission.json': [142, 'f0a6682f19624cc32757457a1503fefef3512f33c8f4df443cb707ad6b5f4049'], 'make.log': [662, 'aa8722776a5620610e99d793308c3bd28fe5aaa1d8f27e588fce3adbe367e87a'], 'check.log': [655, '49907278c7085d6844d61c44e612f0b32e552f544fd940b44c1a19f267d0f834'], 'cover.log': [315, 'c899dddb6b3503d5596ff656f6da6e4d77a55d9f6dc531552a978ce0e14822ad'], 'ablation.log': [209, 'de2029939a4224bd30756cef862f8bb02df5530c88bcf3d6044c6d55fd506ad5']}
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
for n,w in S.items():assert pin(Path(n).read_bytes())==w,('SOURCE_PIN',n)
mode=sys.argv[1] if len(sys.argv)>1 else 'all';assert mode in ('all','check')
def run(args,log):
 env=os.environ.copy()
 for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):env[k]='1'
 env['PYTHONHASHSEED']='0'
 p=subprocess.run([sys.executable]+args,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,env=env)
 Path(log).write_bytes(p.stdout);sys.stdout.buffer.write(p.stdout);sys.stdout.buffer.flush()
 assert p.returncode==0,('CHILD_EXIT',args,p.returncode)
if mode=='all':run(['make.py'],'make.log')
assert pin(Path('shadow_exact.json').read_bytes())==O['shadow_exact.json']
run(['-S','check.py'],'check.log');run(['-S','cover.py'],'cover.log');run(['-S','ablation.py'],'ablation.log')
for n,w in O.items():
 if n=='make.log' and mode=='check':continue
 assert pin(Path(n).read_bytes())==w,('OUTPUT_PIN',n)
for n,w in S.items():assert pin(Path(n).read_bytes())==w,('SOURCE_CHANGED',n)
print('ALL_NEW_SOURCE_COEFFICIENT_STREAM_COVER_PINS_PASS')
print('NOVA24_F9_11_SHADOW_FRAMES_COMPLETE_REPLAY_PASS')
print('FIVE_FORMS_UNCLOSED_NO_F10_C34_OR_WHOLE_TYPE_PROMOTION')
