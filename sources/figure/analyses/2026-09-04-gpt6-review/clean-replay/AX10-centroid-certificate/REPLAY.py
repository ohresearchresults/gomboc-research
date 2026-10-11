"""Replay the exact AX10 certificates with Python's standard library only."""
from pathlib import Path
import subprocess
import sys

if not __debug__:
    raise RuntimeError('Exact checkers require assertions; run Python without -O')
root = Path(__file__).resolve().parent
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
print('ALL_AX10_EXACT_REPLAY_CHECKS_PASS')
