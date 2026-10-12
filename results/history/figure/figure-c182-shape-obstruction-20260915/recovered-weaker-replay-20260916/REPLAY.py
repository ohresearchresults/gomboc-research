"""Rebuild C182 and prove the two geometric gates using only literal raw H data.
Usage: python -B -S REPLAY.py NEW_OUTPUT_DIRECTORY
"""
import hashlib
import json
import sys
from pathlib import Path

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / 'core'))
import check_A
import check_B
import centred_mass
import exact_shape_gate

def info(b):
    return {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}

def encoded(x):
    return json.dumps(x, sort_keys=True, separators=(',', ':')).encode()

def main(out):
    expected = json.loads((HERE / 'EXPECTED.json').read_text())
    for name, digest in expected['inputs'].items():
        assert info((HERE / name).read_bytes()) == digest, name
    out.mkdir(parents=True, exist_ok=False)
    raw = json.loads((HERE / 'raw.json').read_text())
    for name, module in [('A', check_A), ('B', check_B)]:
        result = module.run(raw)
        b = encoded(result)
        filename = name + '.json'
        assert info(b) == expected['outputs'][filename], filename
        (out / filename).write_bytes(b)
        print(name, result['V'], result['E'], result['F'], result['counts'], result['weak'], flush=True)
    assert (out / 'A.json').read_bytes() == (out / 'B.json').read_bytes()
    b = encoded(centred_mass.run(result))
    assert info(b) == expected['outputs']['MASS.json']
    (out / 'MASS.json').write_bytes(b)
    gate = exact_shape_gate.run(HERE / 'raw.json', out / 'A.json', out / 'B.json')
    b = encoded(gate)
    assert info(b) == expected['outputs']['GATE.json']
    (out / 'GATE.json').write_bytes(b)
    print(gate['status'], flush=True)
    print('C182_GEOMETRIC_OBSTRUCTION_SOURCE_ONLY_PASS', flush=True)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    main(Path(sys.argv[1]).resolve())
