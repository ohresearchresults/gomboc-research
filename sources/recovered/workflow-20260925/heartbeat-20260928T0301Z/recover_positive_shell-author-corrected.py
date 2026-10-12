#!/usr/bin/env python3
# Complete lossless source-only recovery; no downloaded inputs.
import base64
import hashlib
from pathlib import Path
import subprocess
import sys
import zlib

DATA = (
    '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'
)
PINS = {'positive_shell.py': (11970, '1d21dd11a747bf1ef6a21558bc94e9c2edf55e7dfa7dccd0b3719d85ba8e0799'), 'positive_shell_report.json': (211085, 'cb9a66165b4c1149a12bd1c5cd5af135a8d61f6662fc9f9e0db272875b5122fa'), 'positive_shell_stdout.txt': (1022, 'cb5d95aa2117e5043d2ef963eb18ba5139d25cd115a1ccd77c12cca7fab3dad5')}


def verify(name, data):
    size, digest = PINS[name]
    if len(data) != size or hashlib.sha256(data).hexdigest() != digest:
        raise RuntimeError('Exact pin mismatch: ' + name)

if sys.version_info[:3] != (3, 13, 5):
    raise RuntimeError('Use CPython 3.13.5 for this byte-pinned audit.')
root = Path(sys.argv[1] if len(sys.argv) > 1 else 'shell_rebuild')
root.mkdir(parents=True, exist_ok=True)
source = zlib.decompress(base64.b64decode(DATA, validate=True))
verify('positive_shell.py', source)
(root / 'positive_shell.py').write_bytes(source)
run = subprocess.run([sys.executable, '-B', '-S', 'positive_shell.py'],
                     cwd=root, check=True, stdout=subprocess.PIPE)
(root / 'positive_shell_stdout.txt').write_bytes(run.stdout)
for name in PINS:
    verify(name, (root / name).read_bytes())
print(run.stdout.decode(), end='')
print('SOURCE_ONLY_RECOVERY_ALL_EXACT_PINS_PASS')
