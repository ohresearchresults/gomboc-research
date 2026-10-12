"""Treat every submitted IEEE coordinate as its exact dyadic rational.
Choose their actual common power-of-two denominator, then use the full exact
point-hull auditor. This is a distinct declared construction, not a tolerance.
"""
import sys,numpy as np
from pathlib import Path
from gmpy2 import mpq
from audit_free_points import audit,ROOT
def run(src,out):
    src=Path(src);X=np.load(src)
    if not np.isfinite(X).all():raise ValueError('nonfinite physical coordinates')
    den=max(float(x).as_integer_ratio()[1] for x in X.ravel())
    if den.bit_length()>1000:raise ValueError('coordinate exponent outside this explicit dyadic-grid implementation')
    assert all(mpq(int(round(float(x)*den)),den)==mpq(float(x)) for x in X.ravel())
    print('EXACT_IEEE_COORDINATES',len(X),'denominator_bits',den.bit_length(),flush=True)
    return audit(src,Path(out),den)
if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2])
