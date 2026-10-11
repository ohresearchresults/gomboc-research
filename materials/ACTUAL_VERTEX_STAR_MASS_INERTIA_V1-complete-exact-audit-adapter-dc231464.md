# material-dc231464476b

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

#!/usr/bin/env python3
"""Exact actual-covariance/star-mass inequalities on two distinct E17 controls."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,sys
PINS={'pair_trace_e17.py':'d2f4cb8a50970bb8f6aa528ca8a3e903ca565361172f61e23032d861d4b053ff',
      'triangle_pair_e17.py':'d6b2efc0e71f367e8a8cb8a1a536547dace53066ded6ee865ea77de61d8f7465'}
for name,pin in PINS.items():assert hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()==pin
import pair_trace_e17 as p
import triangle_pair_e17 as t

def inv3(a):
    determinant=p.det(*a);assert determinant>0
    co=[p.cross(a[1],a[2]),p.cross(a[2],a[0]),p.cross(a[0],a[1])]
    return [[co[j][i]/determinant for j in range(3)] for i in range(3)]
def quad(a,x):return sum(x[i]*a[i][j]*x[j] for i in range(3) for j in range(3))
def inspect(body):
    Sigma=body['covariance'];inv=inv3(Sigma);vs=[p.sub(v,body['centroid']) for v in body['vertices']]
    assert all(sum(Sigma[i][k]*inv[k][j] for k in range(3))==int(i==j) for i in range(3) for j in range(3))
    rows=[]
    for v,x in enumerate(vs):
        inc=[i for i,face in enumerate(body['faces']) if v in face['vertices']]
        mass=sum(body['d'][i] for i in inc)
        b=tuple(sum(body['d'][i]*body['q'][i][k] for i in inc) for k in range(3))
        assert p.dot(b,x)==mass
        values=[mass-p.dot(b,y) for j,y in enumerate(vs) if j!=v]
        ell=min(values);upper=max(values);assert 0<ell<=upper<=3
        L=quad(inv,x);variance=quad(Sigma,b);moment=mass*mass+variance
        M=[[Sigma[i][j]-x[i]*x[j]/15 for j in range(3)] for i in range(3)]
        minors=[M[0][0],M[0][0]*M[1][1]-M[0][1]**2,p.det(*M)]
        assert all(z>0 for z in minors) and 0<L<15
        refined_cap=12*L/(5*(1+L));gap=refined_cap-mass
        range_gap=4*(ell+upper)*mass-3*ell*upper-5*moment
        assert gap>0 and range_gap>=0 and variance>=mass*mass/L
        assert F(12,5)*mass-moment>0 and refined_cap<F(9,4)
        rows.append({'vertex':v,'incident_facets':inc,'star_mass':mass,'b':b,'L':L,
          'variance':variance,'second_moment':moment,'other_vertex_interval':[ell,upper],
          'old_cap_gap':F(9,4)-mass,'inertia_cap':refined_cap,'inertia_cap_gap':gap,
          'range_second_moment_gap':range_gap,'coarse_second_moment_gap':F(12,5)*mass-moment,
          'inertia_cauchy_gap':variance-mass*mass/L,'Sigma_minus_vv_15_minors':minors})
    return rows

def main():
    assert len(sys.argv)==2 and sys.argv[1] in ('build','check')
    obj={'identity':'ACTUAL_VERTEX_STAR_MASS_INERTIA_V1',
         'mixed_facet_control':inspect(p.build()['e17_control']),
         'two_triangle_control':inspect(t.build()['e17_control'])}
    data=(json.dumps(p.encode(obj),sort_keys=True,separators=(',',':'))+'\n').encode();path=Path('star_mass_inertia_report.json')
    if sys.argv[1]=='build':path.write_bytes(data)
    else:assert path.read_bytes()==data
    print('ACTUAL_STAR_MASS_INERTIA_EXACT_PASS 2 20 60')
    print('ALL_TWENTY_ACTUAL_INERTIA_CAPS_STRONGER_THAN_9_4')
    print('REPORT',len(data),hashlib.sha256(data).hexdigest())
    print('NECESSARY_CONDITIONS_NOT_TREE253_EXCLUSION')
if __name__=='__main__':main()
