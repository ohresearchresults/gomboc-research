"""Combine both verified deliverables into one portable archive, without nested ZIPs."""
import hashlib, json, zipfile
from pathlib import Path

root = Path(__file__).resolve().parent
receipts = json.loads((root/'package-receipts.json').read_text())
destination = root/'GOMBOC_C746_COMPLETE.zip'
pins = {}
with zipfile.ZipFile(destination, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as out:
    for name, receipt in receipts.items():
        source = root/name
        raw = source.read_bytes()
        assert len(raw) == receipt['bytes']
        assert hashlib.sha256(raw).hexdigest() == receipt['sha256']
        del raw
        with zipfile.ZipFile(source) as package:
            manifest = json.loads(package.read('MANIFEST.json'))
            assert set(package.namelist()) == set(manifest) | {'MANIFEST.json'}
            for member, pin in manifest.items():
                assert member not in pins and not member.startswith('/') and '..' not in Path(member).parts
                data = package.read(member)
                assert len(data) == pin['bytes'] and hashlib.sha256(data).hexdigest() == pin['sha256']
                if member == 'README.md':
                    data = (b'# Complete C746 package\n\nEverything is in this archive: source/, exact geometry, viewing model, and both complete local verification runs in replay-1/ and replay-2/. No additional ZIP is required. To run another check, use: python3 verify.py my-fresh-replay\n\nThe viewing OBJ uses rounded coordinates; exact verification uses source/RAW.json.\n\n---\n\n' + data)
                pins[member] = {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
                out.writestr(member, data)
    out.writestr('MANIFEST.json', json.dumps(pins, indent=2)+'\n')
with zipfile.ZipFile(destination) as package:
    assert package.testzip() is None
    assert set(package.namelist()) == set(pins) | {'MANIFEST.json'}
    for name, pin in pins.items():
        data = package.read(name)
        assert len(data) == pin['bytes'] and hashlib.sha256(data).hexdigest() == pin['sha256']
receipt = {'file': destination.name, 'bytes': destination.stat().st_size,
           'sha256': hashlib.sha256(destination.read_bytes()).hexdigest(), 'verifiedMembers': len(pins)}
with (root/'complete-package-receipt.json').open('x') as f:
    f.write(json.dumps(receipt, indent=2)+'\n')
print(json.dumps(receipt, indent=2))
