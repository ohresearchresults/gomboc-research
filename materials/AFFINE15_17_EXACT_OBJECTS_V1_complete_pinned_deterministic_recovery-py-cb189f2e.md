# material-cb189f2e4fd6

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Deterministic zero-start recovery of two exact affine moment certificates.
This is not a floating-point proof. A recovered record must match its frozen
byte hash and then pass the independent stdlib rational/integer checker.
The numerical regeneration environment is pinned; a different BLAS build may
abort with a hash mismatch. No original sandbox or random seed is needed.
Commands: python recover_affine15_17.py recover 15
          python recover_affine15_17.py recover 17
          python -S recover_affine15_17.py verify 15
          python -S recover_affine15_17.py verify 17
Recover the five exact dependency files listed in PINS into this directory.
"""
from pathlib import Path
import hashlib,json,os,platform,shutil,subprocess,sys,tempfile
assert __debug__
HERE=Path(__file__).resolve().parent
PINS={
'flip_moments.py':[13811,'7542ef43f2e0e5b4759f076086c8de3539da8ef5051c80dae2a71e778a21faa7'],
'native55.txt':[2630,'58126aee072933749b18eca00ac4d32842e56e6ac8d662d06713bacef28bf96e'],
'affine_moments.py':[5980,'fa8371daf690ac9ff0a9a61b3ad8e8ca2dc6652b2a0f76cc70826163fff01805'],
'common_roots.py':[6011,'4d3e16daf49c9dbb4c4d5a88fce37f0337409502be51f1049ceaac3f6c4f0d62'],
'affine_roots.py':[1541,'d0866dbf849c91fd39fec55b162ad74f319eade5180c878f7209713f5d249576']}
EXPECTED={
15:{'record':[65340,'738704cdd17e9dccc0506e3056e99e4c03db9467c8cd94cb332cbfce3c436bb5'],
    'report':[5184,'bf953dd5280224e8da3a1348461e8bd75e5fd181c439a75048152dab1b6321e4'],
    'blocks':1096,'minors':10960,'power':14},
17:{'record':[58226,'200b480c94c248e1e891bf6e2a99f7ff60bc6003063a0aef1e0ce5cfe3716dc6'],
    'report':[5176,'d683b4d96f7a8a12eecc54f85b038066c774bb5d1535e5d58c45528b785badcf'],
    'blocks':1104,'minors':11040,'power':12}}
ENV={'OPENBLAS_CORETYPE':'SkylakeX','OPENBLAS_NUM_THREADS':'1',
     'OMP_NUM_THREADS':'1','MKL_NUM_THREADS':'1','PYTHONHASHSEED':'0'}
def pin(b):return[len(b),hashlib.sha256(b).hexdigest()]
def names(i):return f'affine_certificate_{i}_root.json',f'affine_certificate_{i}_root.verified.json'
def verify(i,directory):
 p,q=names(i);e=EXPECTED[i]
 assert pin((directory/p).read_bytes())==e['record']
 subprocess.run([sys.executable,'-S',str(directory/'affine_roots.py'),'check',str(directory/p)],check=True,env={**os.environ,**ENV})
 assert pin((directory/q).read_bytes())==e['report']
 r=json.loads((directory/q).read_bytes());c=json.loads((directory/p).read_bytes())
 assert r['total_blocks']==e['blocks'] and r['total_leading_minors']==e['minors']
 assert c['rounding_power']==e['power'] and r['roots']==list(range(1,9))
 print('AFFINE15_17_EXACT_VERIFICATION_PASS',i,e['blocks'],e['minors'],*e['record'],flush=True)
def main():
 assert len(sys.argv)==3 and sys.argv[1] in ('recover','verify')
 mode=sys.argv[1];i=int(sys.argv[2]);assert i in EXPECTED
 for name,p in PINS.items():assert pin((HERE/name).read_bytes())==p,(name,p)
 if mode=='verify':verify(i,HERE);return
 # Validate build versions in a fresh child after setting BLAS dispatch.
 guard="import platform,numpy as n,scipy;assert platform.python_version()=='3.13.5';assert n.__version__=='2.3.5';assert scipy.__version__=='1.17.0';assert platform.machine()=='x86_64';assert n.show_config(mode='dicts')['Build Dependencies']['blas']['version']=='0.3.30'"
 subprocess.run([sys.executable,'-c',guard],check=True,env={**os.environ,**ENV})
 with tempfile.TemporaryDirectory(prefix='affine_exact_recovery_') as tmp:
  work=Path(tmp)
  for name in PINS:shutil.copyfile(HERE/name,work/name)
  subprocess.run([sys.executable,str(work/'affine_roots.py'),'locate',str(i),'root'],check=True,cwd=work,env={**os.environ,**ENV})
  verify(i,work)
  for name in names(i):shutil.copyfile(work/name,HERE/name)
 print('AFFINE15_17_DETERMINISTIC_RECOVERY_PASS',i,*EXPECTED[i]['record'],flush=True)
if __name__=='__main__':main()
