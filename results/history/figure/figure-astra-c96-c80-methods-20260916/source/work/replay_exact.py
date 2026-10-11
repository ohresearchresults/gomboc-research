"""Cold replay of every retained exact body and all new exact certificates."""
import hashlib,json,subprocess,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'tools'),str(ROOT/'tools/core')]
from exact_points import encoded,make
import check_A,check_B,centred_mass


def main():
    manifest=json.loads((ROOT/'work/EXACT_MANIFEST.json').read_text())
    for name,case in manifest['cases'].items():
        folder=ROOT/'work'/name
        source=(folder/case['definition']).read_bytes()
        assert hashlib.sha256(source).hexdigest()==case['definition_sha256']
        definition=json.loads(source)
        raw=make(definition['points'])if 'points'in definition else definition
        a=check_A.run(raw);b=check_B.run(raw);assert a==b
        m=centred_mass.run(a)
        assert [a['V'],a['E'],a['F'],a['counts'],a['weak']]==case['signature']
        assert a['weak']==[0,0,0]
        assert all(a[key]==0 for key in ['face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count'])
        for filename,value in [('raw.json',raw),('A.json',a),('B.json',b),('MASS.json',m)]:
            data=encoded(value);assert hashlib.sha256(data).hexdigest()==case['files'][filename]['sha256']
            assert len(data)==case['files'][filename]['bytes']
            target=folder/filename
            if target.exists():assert target.read_bytes()==data
            else:target.write_bytes(data)
        print('EXACT_RETAINED_BODY_PASS',name,case['signature'],flush=True)
    for script in ['shape_certificate.py','radius_certificate.py','radius_thick_certificate.py','reference_certificate.py']:
        subprocess.run([sys.executable,'-B','-S',str(ROOT/'work'/script)],cwd=ROOT,check=True)
    subprocess.run([sys.executable,'-B','-S',str(ROOT/'work/loading_verify.py'),
                    str(ROOT/'work/loading-compact.json'),str(ROOT/'work/baseline-check/A.json')],cwd=ROOT,check=True)
    for name,expected in manifest['certificates'].items():
        data=(ROOT/'work'/name).read_bytes()
        assert hashlib.sha256(data).hexdigest()==expected['sha256'] and len(data)==expected['bytes']
    print('ALL_RETAINED_EXACT_BODIES_AND_CERTIFICATES_COLD_PASS_NO_OWN110',flush=True)


if __name__=='__main__':main()
