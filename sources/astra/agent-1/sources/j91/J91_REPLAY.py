"""Cold recovery of four exact J91 homogeneous own211 nonwinners.
Requires the nine-unit J90_CORE_REPLAY.sh extracted from immutable material
att_eec035833d797b567d6e_01 and this complete J91 exact-recovery bundle.
No floating geometry, numerical optimizer, originating sandbox or download.
"""
from pathlib import Path
from fractions import Fraction as F
import subprocess,json,hashlib,sys,os
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent
os.chdir(ROOT)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def command(args,src=None,dst=None):
    with (open(src,'rb') if src else open(os.devnull,'rb')) as i:
        with (open(dst,'wb') if dst else open(os.devnull,'wb')) as o:
            subprocess.run(args,stdin=i,stdout=o,check=True)
def main():
    manifest=json.loads(Path('J91_EXACT_MANIFEST.json').read_text())
    for name,item in manifest['inputs'].items():
        assert Path(name).stat().st_size==item['bytes'] and sha(name)==item['sha256'],name
    for p in ['exact90.cpp','make_vfaudit90.py','J90_DETACHED_C390_G8.txt']:
        assert Path(p).is_file(), 'Extract complete J90_CORE_REPLAY.sh first: missing '+p
    command(['g++','-O2','-std=c++17','exact90.cpp','-o','exact90','-lgmpxx','-lgmp'])
    command(['./exact90'],'J90_DETACHED_C390_G8.txt','J90_DETACHED_C390_G8_AUDIT.json')
    command([sys.executable,'make_vfaudit90.py'])
    command(['g++','-O2','-std=c++17','vfaudit90.cpp','-o','vfaudit90','-lgmpxx','-lgmp'])
    base=json.loads(Path('J90_DETACHED_C390_G8_AUDIT.json').read_text())
    names=['J91_CAPFLOW_C452_G18','J91_OUTER_C494_G18','J91_REBALANCED_C434_G18']
    for name in names:
        data=json.loads(Path(name+'_INPUT.json').read_text())
        assert data['base']=='J90_DETACHED_C390_G8'
        vertices=base['vertices']+data['apexes'];faces=data['faces']
        with open(name+'_VF.txt','w') as f:
            f.write(f'{len(vertices)} {len(faces)}\n')
            for p in vertices:f.write(' '.join(p)+'\n')
            for cy in faces:f.write(' '.join(map(str,[len(cy),*cy]))+'\n')
        command(['./vfaudit90'],name+'_VF.txt',name+'_AUDIT.json')
    command([sys.executable,'momentfix91.py'])
    names.append('J91_EXACT_CENTER_C434')
    command(['./vfaudit90'],names[-1]+'_VF.txt',names[-1]+'_AUDIT.json')
    for name in names:
        d=json.loads(Path(name+'_AUDIT.json').read_text())
        assert d['strict']==[2,1,1] and d['weak']==[0,0,0] and d['primitive_zeros']==[0,0,0]
        assert not d['P'] and len(d['Q'])==1 and F(d['Q'][0]['depth'])>0
        expected=[138,226,90] if 'CAPFLOW' in name else ([139,247,110] if 'OUTER' in name else [135,217,84])
        assert [d['V'],d['E'],d['F']]==expected and d['C']==2*d['E']
        print('J91_EXACT_OWN211_NOT110',name,expected,'Q',float(F(d['Q'][0]['depth'])))
    exact=json.loads(Path('J91_EXACT_CENTER_C434_AUDIT.json').read_text())
    rounded=json.loads(Path('J91_REBALANCED_C434_G18_AUDIT.json').read_text())
    assert exact['centroid']==base['centroid'] and exact['volume']==rounded['volume']
    for name,item in manifest['outputs'].items():
        assert Path(name).stat().st_size==item['bytes'] and sha(name)==item['sha256'],name
    print('J91_FOUR_EXACT_NONWINNERS_RECOVERED_NO_110')
    print('J91_EXACT_SAME_CENTRE_C434_CONFIRMED')
    print('J91_COMPLETE_EXACT_RECOVERY_PASS')
if __name__=='__main__':main()
