# material-0924e0f84995

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# RAW_HEX6_ALL_ROOT_PSD_COLLAR_V1 — mandatory recovery correction

## Canonical recovery set
BOTH this correction and immutable material [internal-source-reference] are required. The latter is the complete source capsule with one copied stencil line wrong; by itself it is NOT the canonical runnable certificate. This exact correction reconstructs the actually executed source and certificate. No mathematical premise or result is changed.

Input material [internal-source-reference], name RAW_HEX6_ALL_ROOT_PSD_COLLAR_V1.md, has20409 UTF-8 bytes and SHA2566918f3e3e0bbf80f361b0c573da41b2d605622ffdf25cb3f44ea826243b0cfea. At UTF-16 offset10042 starts the unique three-line anchor shown literally in the script. Its middle line was inadvertently copied from a later stencil. The correct middle line is 2:151 20:526 30:322. The later legitimate occurrence of 2:160 16:111 21:136 22:93 is NOT changed.

The coordinator checked that applying the reverse one-line replacement to the fully executed local capsule reproduces the stored material's ENTIRE hash and byte count. Thus this is the complete sole difference, not a guessed partial repair. The repaired capsule is20403bytes SHA256486b7e0f705097bc63e5379acbdd73e6f2ff4528f292908613e5e8adcfd0eb0f. Its autonomous source verify_raw_hex6_psd.py is16609bytes SHA256552a806d0e75ec0e707ae8bdeaf6c0aa57022e997c532df232832ef96aeddd96. All307 stencils,1150 arrow terms and921 exact leading-minor checks remain literal in the repaired source.

## Recovery
Save the exact text bytes of [internal-source-reference] as input_capsule.md. Save the following complete script as repair_raw_hex6_psd.py. It requires only Python>=3.10 standard library.

    python repair_raw_hex6_psd.py input_capsule.md
    python verify_raw_hex6_psd.py --output raw_hex6_allroot_psd_report.json
    python -c "import hashlib,pathlib; b=pathlib.Path('raw_hex6_allroot_psd_report.json').read_bytes(); assert len(b)==1434; assert hashlib.sha256(b).hexdigest()=='b0bac651b5fd3152045ef4dccc050c5a8e127c4b8767df89ceaf8ea05b56349c'; print('RAW_HEX6_CAPSULE_PINS_OK')"

Expected markers in order: RAW_HEX6_COPY_REPAIR_OK; RAW_HEX6_ALLROOT_PSD_COLLAR_VERIFIED; RAW_HEX6_CAPSULE_PINS_OK.

```python
#!/usr/bin/env python3
"""Repair the one exact copied stencil line; verify every reconstructed byte."""
from pathlib import Path
import hashlib
import sys


def checked(data: bytes, length: int, digest: str) -> None:
    if len(data) != length or hashlib.sha256(data).hexdigest() != digest:
        raise ValueError('Unexpected exact source bytes; do not apply a guessed repair')


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python repair_raw_hex6_psd.py input_capsule.md')
    raw = Path(sys.argv[1]).read_bytes()
    checked(raw, 20409, '6918f3e3e0bbf80f361b0c573da41b2d605622ffdf25cb3f44ea826243b0cfea')
    before = (b'10:181 15:58 19:236 32:524\n'
              b'2:160 16:111 21:136 22:93\n'
              b'1:71 8:236 21:513 25:180')
    after = (b'10:181 15:58 19:236 32:524\n'
             b'2:151 20:526 30:322\n'
             b'1:71 8:236 21:513 25:180')
    if raw.count(before) != 1:
        raise ValueError('Repair anchor is not unique')
    fixed = raw.replace(before, after, 1)
    checked(fixed, 20403, '486b7e0f705097bc63e5379acbdd73e6f2ff4528f292908613e5e8adcfd0eb0f')
    marker = b'```python\n'
    if fixed.count(marker) != 1 or not fixed.endswith(b'```\n'):
        raise ValueError('Unexpected source-fence layout')
    source = fixed.split(marker, 1)[1][:-4]
    checked(source, 16609, '552a806d0e75ec0e707ae8bdeaf6c0aa57022e997c532df232832ef96aeddd96')
    Path('RAW_HEX6_ALL_ROOT_PSD_COLLAR_V1.corrected.md').write_bytes(fixed)
    Path('verify_raw_hex6_psd.py').write_bytes(source)
    print('RAW_HEX6_COPY_REPAIR_OK')


if __name__ == '__main__':
    main()
```

## Scientific scope retained
The exact actual body RAW_TRANSLATED_HEX6_1over5_24over25_49over50_2over9_99over100_V1 and its same-true-graph actual-own-centred coordinate collar of radius10^-12 admit no complete weak true rooted tree for any nonzero PSD, at any root.43350 rooted true trees are covered. This NEW rational translated raw body is not the fixed-pole star-centred atlas member. The global bracket remains34..622. The preceding physical-contact census [internal-source-reference] remains independently useful, but its formerly open rank-two-connected alternative on this body is now closed by this full-tree certificate.
