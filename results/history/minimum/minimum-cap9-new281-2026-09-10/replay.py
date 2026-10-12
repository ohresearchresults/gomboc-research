"""NEW complete source-only CAP9 recovery; never decodes the malformed parent.
CPython3.13.5; all/check/seed modes. Save all five source units together.
Full: python -S replay.py. Frozen: python -S replay.py check.
Tiny exact checkpoint only: python -S replay.py seed.
Numerical: numpy2.3.5,scipy1.17.0,threadpoolctl3.6.0,OpenBLAS0.3.30/Haswell.
"""
from pathlib import Path
import hashlib,json,os,subprocess,sys
assert __debug__
S={'engine.py': [3924, '382527ea22bb7a02d448ac2eb1f9c1b5785f15384df6c9248f1639714b87ab00'], 'build.py': [2924, '7ee0832cf805272cc47e587dff7a8710250eef481b7a5ca55af9e36633dcec78'], 'verify.py': [5792, 'c572e6bb3ff4ef19db498b436972f4304229ab3f26562a74a179765519bea8f9'], 'frames.py': [4681, 'c4389bb0b7e05e0c0294f1214fe29eb8b913c6fadd94d902681c9c52795e4158']}
O={'cap9_new.json': [3829595, 'b0cfc1a3d46eec19e3e5d0f1603de276edb45da7cc06b069e7299b4c1ae7654c'], 'cap9_checked.json': [817, '3e23d591677593fa852949daf2642c45f556b73d1da0b755d42818f1572167ac'], 'frames_new.json': [1616, 'd21bf29911fc161ad993af4267e8b57dc3f8a9f9b85908283a0141c67360a988'], 'build.log': [440, '57a4d7214ccc6c95a481cb295f0a67e53e629c0a061ffb53484ce3282719d3bb'], 'verify.log': [720, '1c2f9948ca653242b9080d82af7bb218e598cc1ba9ec070b156f62d17b9f85fd'], 'frames.log': [305, 'abf49bcced761cc9f3055a0ece58a2342b34b93498a89a9654ac343bd97f0999'], 'seed0.json': [4455, '2e45acd9ffdd7a7eab8251713114d36599b83d03259d1b146080a73ebe231455']}
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
for n,want in S.items():assert pin(Path(n).read_bytes())==want,('SOURCE_PIN',n)
mode=sys.argv[1] if len(sys.argv)>1 else 'all'
assert mode in ('all','check','seed')
# This exact record belongs to the full checkpoint, not an unrelated smoke test.
import verify as v
W=v.weights(0);g=[900]+[9]*8;mu=[[100*w[i]+9 for i in range(1,9)] for w in W]
r=dict(ordinal=0,parent=[0]*9,rows=[0],g=g,mu=mu)
for w,u in zip(W,mu):
 a=v.scalar_matrix([0]*9,g,u,w,[0]*45,1);v.fraction_ldl(a,v.bareiss(a))
b=v.serial(r);assert pin(b)==O['seed0.json'];Path('seed0.json').write_bytes(b)
print('EXACT_LITERAL_STAR_CHECKPOINT_PASS',0,168,flush=True)
if mode=='seed':
 print('SEED',*pin(b));print('SEED_ONLY_NOT_281_TREE_REPLAY');raise SystemExit(0)
def run(args,log):
 env=os.environ.copy()
 for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):env[k]='1'
 env['PYTHONHASHSEED']='0'
 p=subprocess.run([sys.executable]+args,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,env=env)
 Path(log).write_bytes(p.stdout);sys.stdout.buffer.write(p.stdout);sys.stdout.buffer.flush()
 assert p.returncode==0,('CHILD_EXIT',args,p.returncode)
if mode=='all':run(['build.py'],'build.log')
assert pin(Path('cap9_new.json').read_bytes())==O['cap9_new.json']
run(['-S','verify.py'],'verify.log');run(['-S','frames.py'],'frames.log')
for n,want in O.items():
 if n=='build.log' and mode=='check':continue
 assert pin(Path(n).read_bytes())==want,('OUTPUT_PIN',n)
print('ALL_NEW_CAP9_SOURCE_COEFFICIENT_REPORT_STREAM_FRAME_PINS_PASS')
print('NOVA24_CAP9_NEW_281_RESTORED_COMPLETE_RECOVERY_PASS')
print('REMAINING_TREE_ORDINALS 253 266 272 278 285')
