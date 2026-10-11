"""Export the verified exact geometry and a clearly labelled viewing derivative."""
import hashlib, json, sys
from fractions import Fraction
from pathlib import Path
sys.set_int_max_str_digits(0)
root=Path(__file__).resolve().parent
receipt=json.loads((root/'replay-1/receipt.json').read_text())
assert receipt['accepted']
audit=json.loads((root/'replay-1/A.json').read_text())
assert hashlib.sha256((root/'replay-1/A.json').read_bytes()).hexdigest()==receipt['outputs']['A.json']['sha256']
geometry={k:audit[k] for k in ['V','E','F','raw_vertices','faces','edges','raw_centroid','raw_volume',
    'counts','weak','stable_face_ids','unstable_vertices']}
geometry['frame']='Exact raw coordinates. Uniform filled solid; equilibrium checks use its true volume centroid.'
(root/'geometry-exact.json').write_text(json.dumps(geometry,indent=2)+'\n')
def metrics(points):
    values=[Fraction(x) for p in points for x in p]
    return {'coordinateCount':len(values),'nonIntegerCoordinates':sum(x.denominator!=1 for x in values),
        'maxNumeratorDigits':max(len(str(abs(x.numerator))) for x in values),
        'maxDenominatorDigits':max(len(str(x.denominator)) for x in values)}
arithmetic={'raw':metrics(audit['raw_vertices']),'centred':metrics(audit['vertices']),
    'supportDenominator':100000000,
    'note':'Representation size is not manufacturing tolerance. Viewing coordinates are rounded derivatives.'}
(root/'coordinate-complexity.json').write_text(json.dumps(arithmetic,indent=2)+'\n')
lines=['# C746 viewing derivative ONLY; decimal coordinates are not the exact certificate.',
    '# See RAW.json and geometry-exact.json for exact geometry; the solid is uniformly filled.']
lines += ['v '+' '.join(format(float(Fraction(x)),'.17g') for x in p) for p in audit['raw_vertices']]
lines += ['f '+' '.join(str(i+1) for i in face) for face in audit['faces']]
(root/'model-viewing.obj').write_text('\n'.join(lines)+'\n')
print(json.dumps(arithmetic,indent=2))
