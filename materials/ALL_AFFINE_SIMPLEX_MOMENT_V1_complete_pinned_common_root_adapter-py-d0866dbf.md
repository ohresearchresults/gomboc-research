# material-d0866dbf849c

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Complete pinned adapter: common-root certificates with affine-simplex moments.
Commands: python affine_roots.py locate INDEX MODE
          python -S affine_roots.py check RECORD.json
MODE is root, oriented or edge. All eight internal roots are simultaneous.
All generated proposals are ephemeral until their complete data are stored.
"""
from pathlib import Path
import hashlib,sys
assert __debug__
HERE=Path(__file__).resolve().parent
PINS={'common_roots.py':[6011,'4d3e16daf49c9dbb4c4d5a88fce37f0337409502be51f1049ceaac3f6c4f0d62']}
for name,pin in PINS.items():
    b=(HERE/name).read_bytes();assert [len(b),hashlib.sha256(b).hexdigest()]==pin
import affine_moments as am
am.fm.system=am.system
_base_check=am.fm.check
_LEAF='TREE253_K2_AFFINE_SIMPLEX_MOMENT_CERTIFICATE_V1'
def _affine_check(record):
    assert record['identity']==_LEAF
    copied=dict(record);copied['identity']='TREE253_K2_ALL_FACET_FLIP_CERTIFICATE_V1'
    report=_base_check(copied)
    report['identity']='AFFINE_SIMPLEX_MOMENT_EXACT_VERIFICATION_V1'
    return report
am.fm.check=_affine_check
source=(HERE/'common_roots.py').read_text()
source=source.replace('import flip_moments as fm','import affine_moments as am\nfm=am.fm')
source=source.replace('TREE253_K2_ALL_FACET_FLIP_CERTIFICATE_V1',_LEAF)
source=source.replace('ALL_FACET_FLIP_COMMON_ROOTS','ALL_AFFINE_SIMPLEX_COMMON_ROOTS')
source=source.replace('COMMON_ROOT','AFFINE_ROOT')
source=source.replace('common_','affine_')
exec(compile(source,str(HERE/'affine_roots.py'),'exec'),globals(),globals())
