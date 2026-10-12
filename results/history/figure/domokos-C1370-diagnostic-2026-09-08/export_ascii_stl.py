"""Create a 17-significant-digit ASCII viewing STL from the C1370 exact table."""
import csv,gzip,json,math,sys,hashlib
from pathlib import Path
from fractions import Fraction
sys.set_int_max_str_digits(0)

base=Path(__file__).resolve().parent
source=base/'gomboc-1370'/'verified'
report=json.loads((source/'exact_report.json').read_text())
q=int(report['centred_denominator'])
with gzip.open(source/'vertices.csv.gz','rt')as f:
    rational=[tuple(Fraction(int(x),q)for x in row)for row in csv.reader(f)]
with gzip.open(source/'triangles.csv.gz','rt')as f:
    triangles=[tuple(map(int,row))for row in csv.reader(f)]
points=[tuple(float(x)for x in v)for v in rational]
assert len(points)==258 and len(triangles)==512
assert len(set(points))==258
lines=['solid gomboc_C1370_V258_view']
maximum=Fraction(0)
for tri in triangles:
    a,b,c=(points[i]for i in tri)
    u=[b[k]-a[k]for k in range(3)];v=[c[k]-a[k]for k in range(3)]
    n=[u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]]
    length=math.sqrt(sum(x*x for x in n));assert length>0
    lines.append('  facet normal '+' '.join(format(x/length,'.17g')for x in n))
    lines.append('    outer loop')
    for i in tri:
        text=[format(x,'.17g')for x in points[i]]
        maximum=max(maximum,*(abs(Fraction(x)-y)for x,y in zip(text,rational[i])))
        lines.append('      vertex '+' '.join(text))
    lines.extend(['    endloop','  endfacet'])
lines.append('endsolid gomboc_C1370_V258_view')
target=base/'gomboc_C1370_V258_view.stl'
target.write_text('\n'.join(lines)+'\n',encoding='ascii')
meta=dict(source='gomboc-1370/verified/vertices.csv.gz',
          derived_stl=target.name,stl_in_original_package=False,
          maximum_coordinate_error=float(maximum),
          stl_sha256=hashlib.sha256(target.read_bytes()).hexdigest())
(base/'export-report.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta,indent=2))
