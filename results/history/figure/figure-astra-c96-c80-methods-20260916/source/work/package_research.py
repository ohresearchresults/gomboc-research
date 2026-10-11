"""Build portable source/data capsules and pin all exact replay expectations."""
import base64,hashlib,json,lzma,textwrap
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CASES=['baseline-check','polar-exact','flow25-exact','pyramid-101-exact','pyramid-final-exact',
       'rounder25-exact','capped-bulk-exact','support-conditioned-exact','support-polar-exact']
CERTIFICATES=['shape-certificate.json','radius-certificate.json','radius-thick-certificate.json',
              'reference-c80-certificate.json','loading-compact.json']


def digest(data):return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
def put(path,value):path.write_text(json.dumps(value,sort_keys=True,indent=2)+'\n')


def capsule(files,name):
    mapping={str(p.relative_to(ROOT)):p.read_text()for p in sorted(files)}
    source=json.dumps(mapping,sort_keys=True,separators=(',',':')).encode()
    encoded=base64.b85encode(lzma.compress(source,preset=9)).decode()
    # No shell trick: the generated portable program validates paths and bytes.
    script='''import base64,hashlib,json,lzma,pathlib,subprocess,sys
payload="""PAYLOAD"""
source=lzma.decompress(base64.b85decode("".join(payload.split())))
assert hashlib.sha256(source).hexdigest()=="SOURCE_SHA"
destination=pathlib.Path(sys.argv[1]);destination.mkdir(parents=True,exist_ok=False)
for name,text in json.loads(source).items():
    path=pathlib.PurePosixPath(name)
    assert not path.is_absolute() and ".." not in path.parts
    output=destination.joinpath(*path.parts);output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(text)
subprocess.run([sys.executable,"-B","-S",str(destination/"work/replay_exact.py")],check=True)
'''.replace('PAYLOAD','\n'+'\n'.join(textwrap.wrap(encoded,100))+'\n').replace('SOURCE_SHA',hashlib.sha256(source).hexdigest())
    out=ROOT/'work'/name;out.write_text(script)
    return dict(path=str(out),source_mapping=digest(source),program=digest(script.encode()),files=len(mapping))


def main():
    manifest=dict(cases={},certificates={},dependencies='Exact replay: CPython standard library only; numerical searches: NumPy2.5.3, SciPy1.18.1, one BLAS/OpenMP thread.')
    files=[ROOT/'tools/exact_points.py',*(ROOT/'tools/core'/s for s in ['check_A.py','check_B.py','centred_mass.py'])]
    files += [ROOT/'work'/s for s in ['replay_exact.py','shape_certificate.py','radius_certificate.py',
                                   'radius_thick_certificate.py','reference_certificate.py','loading_verify.py']]
    for name in CASES:
        folder=ROOT/'work'/name;definition='POINTS.json'if(folder/'POINTS.json').exists()else'raw.json'
        a=json.loads((folder/'A.json').read_text());data=(folder/definition).read_bytes();files.append(folder/definition)
        manifest['cases'][name]=dict(definition=definition,definition_sha256=hashlib.sha256(data).hexdigest(),
             signature=[a['V'],a['E'],a['F'],a['counts'],a['weak']],mass=json.loads((folder/'MASS.json').read_text()),
             files={s:digest((folder/s).read_bytes())for s in ['raw.json','A.json','B.json','MASS.json']})
    for name in CERTIFICATES:
        manifest['certificates'][name]=digest((ROOT/'work'/name).read_bytes())
    files.append(ROOT/'work/loading-compact.json')
    put(ROOT/'work/EXACT_MANIFEST.json',manifest);files.append(ROOT/'work/EXACT_MANIFEST.json')
    exact=capsule(files,'RECOVER_EXACT.py')
    research_files=list(set(files+list((ROOT/'work').glob('*.py'))+[ROOT/'input/POINTS25.json',ROOT/'input/c96/planar25.py',ROOT/'work/NOTES.md']))
    research_files=[p for p in research_files if p.name not in ['RECOVER_EXACT.py','RECOVER_RESEARCH.py']]
    # Literal saved numerical checkpoints make continuation independent of replaying optimizers.
    research_files += [p for p in (ROOT/'work').glob('*/BEST.json')]
    research_files += [ROOT/'work'/n for n in ['caps4.json','caps12.json','derivative-check.json']]
    research=capsule(research_files,'RECOVER_RESEARCH.py')
    receipt=dict(exact=exact,research=research)
    put(ROOT/'work/CAPSULE_RECEIPT.json',receipt);print(json.dumps(receipt,indent=2))


if __name__=='__main__':main()
