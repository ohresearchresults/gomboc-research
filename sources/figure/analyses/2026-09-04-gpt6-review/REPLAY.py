"""Replay the exact AX10 certificates with Python's standard library only."""
from pathlib import Path
import subprocess
import sys
import hashlib
import json

if not __debug__:
    raise RuntimeError('Exact checkers require assertions; run Python without -O')
root = Path(__file__).resolve().parent
manifest = json.loads((root/'CERTIFICATE_SHA256.json').read_text())
for name, expected in manifest.items():
    if hashlib.sha256((root/name).read_bytes()).hexdigest() != expected:
        raise RuntimeError('Frozen package hash mismatch: '+name)
print('FROZEN_PACKAGE_HASHES_PASS', flush=True)
checks = [
    'verify_ax10_centroid_obstruction.py',
    'independent_ax10_replay.py',
    'verify_ax10_four_face_capacity.py',
    'verify_ax10_patch_atlas.py',
    'independent_ax10_capacity_replay.py',
]
for name in checks:
    run = subprocess.run([sys.executable, str(root/name)], cwd=root, text=True, capture_output=True)
    if run.returncode:
        print(run.stdout, end='')
        print(run.stderr, end='', file=sys.stderr)
        raise SystemExit(run.returncode)
    print(name+': '+run.stdout.strip().splitlines()[-1], flush=True)
for name, expected in manifest.items():
    if hashlib.sha256((root/name).read_bytes()).hexdigest() != expected:
        raise RuntimeError('Replay changed frozen bytes: '+name)
print('ALL_AX10_EXACT_REPLAY_CHECKS_PASS_WITH_IDENTICAL_CERTIFICATE_BYTES')
