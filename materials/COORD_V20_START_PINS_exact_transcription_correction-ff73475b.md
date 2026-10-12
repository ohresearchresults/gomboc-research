# material-ff73475bf7ca

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Exact correction to the supplementary numerical starting pin

The START_PINS.json block in [internal-source-reference] has one transcription error, at zero-based indices `['relative_w1000'][15][1]`. Its value must be **-0.21140139112555656**, not the written -0.21180344794548773. This correction affects the supplementary numerical starting point only. It does not alter any core exact G3-G9 body, the three final binary64 pins, their42 hashes, or any exact mechanics report; those are independently preserved in [internal-source-reference].

After this exact scalar replacement, START_PINS.json serialized with sorted keys and compact separators and no final newline is2508 bytes with SHA25635f277f64f8b3d7ee75558862f394ae344ae01b8973e416074834fc2548b9edb, the originally recorded local file hash. All other rows are unchanged. The source argument file for the numerical batch is now the previous complete block PLUS this mandatory correction, not the previous block alone.

Complete runnable patch, save as FIX_START_PINS.py and run `python -B -S FIX_START_PINS.py` beside the extracted START_PINS.json:

```python
import hashlib,json
from pathlib import Path
p=Path('START_PINS.json')
data=json.loads(p.read_text())
assert data['relative_w1000'][15][1] in (-0.21180344794548773,-0.21140139112555656)
data['relative_w1000'][15][1]=-0.21140139112555656
b=json.dumps(data,sort_keys=True,separators=(',',':')).encode('utf-8')
assert len(b)==2508
assert hashlib.sha256(b).hexdigest()=='35f277f64f8b3d7ee75558862f394ae344ae01b8973e416074834fc2548b9edb'
p.write_bytes(b)
print('COORD_V20_NUMERIC_START_PIN_CORRECTED_SHA_PASS')
```

The unchanged COVERAGE.json in the preceding material remains the completed fifty-case numerical table. Its counts are not exact class certificates and it does not provide any global exclusion.
