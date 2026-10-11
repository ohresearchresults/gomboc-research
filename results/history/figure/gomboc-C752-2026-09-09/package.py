import hashlib, json, zipfile
from pathlib import Path
root=Path(__file__).resolve().parent
for n in (1,2): assert json.loads((root/f'replay-{n}/receipt.json').read_text())['accepted']
source=sorted((root/'source').iterdir())+[root/name for name in (
    'README.md','verify.py','source-manifest.json','geometry-exact.json','coordinate-complexity.json','model-viewing.obj')]
evidence=[root/f'replay-{n}'/name for n in (1,2) for name in (
    'A.json','B.json','EXTRA.json','CONTROLS.json','SUMMARY.json','receipt.json','verification.log')]
packages={}
for label,files in [('GOMBOC_C752_SOURCE_AND_MODEL.zip',source),('GOMBOC_C752_FULL_VERIFICATION.zip',evidence)]:
    destination=root/label
    assert not destination.exists()
    pins={}
    with zipfile.ZipFile(destination,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as archive:
        for file in files:
            assert file.is_file() and not file.is_symlink()
            name=str(file.relative_to(root))
            raw=file.read_bytes();pins[name]={'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
            archive.writestr(name,raw)
        archive.writestr('MANIFEST.json',json.dumps(pins,indent=2)+'\n')
    with zipfile.ZipFile(destination) as archive:
        assert archive.testzip() is None
        for name,pin in pins.items():
            raw=archive.read(name)
            assert len(raw)==pin['bytes'] and hashlib.sha256(raw).hexdigest()==pin['sha256']
    packages[label]={'bytes':destination.stat().st_size,'sha256':hashlib.sha256(destination.read_bytes()).hexdigest(),'verifiedMembers':len(pins)}
(root/'package-receipts.json').write_text(json.dumps(packages,indent=2)+'\n')
print(json.dumps(packages,indent=2))
