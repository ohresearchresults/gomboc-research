# material-3f9a05fbc239

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Whole actual-centroid H5 box exclusion by 49 paired reciprocal-arrow duals.
Standard-library exact rational verification; Python>=3.11, tested3.13.5.
Run with assertions enabled: python -B -S h5_paired_arrow_box_exact.py
All five source dependencies are identified in the accompanying recovery note.
"""
from pathlib import Path
from math import comb
import hashlib,json,sys
from h5_pair_box_geometry import *
from h5_paired_arrow_witnesses import EPS,decoded


def trig_majorants(U):
    # Machin: pi/4=4atan(1/5)-atan(1/239). Even number of terms
    # gives a strict lower bound on atan(1/5); atan(1/239)<1/239.
    pilo=16*sum(((-1)**k*Q(1,5)**(2*k+1)/Q(2*k+1) for k in range(6)),Q(0))-4*Q(1,239)
    assert pilo>Q(333,106)
    values=[]
    for m in (10,9):
        z=Q(333,106)/(2*m)
        c=1-z*z/2+z**4/24
        assert 0<c<1
        upper=c**(2*m)
        assert U*upper<4
        values.append(upper)
    return values


def sum_bound():
    # The eigenvalues of H, up to scale, are (p*q,q,1), 1<=p,q<=4.
    # Eigenvalues of the normalized inverse are (1,p,p*q)/(p*q+p+1).
    u,v=Poly.variable(0),Poly.variable(1);p=1+3*u;q=1+3*v
    S=p*q+q+1;T=p*q+p+1
    tables=[]
    for a,b in ((p*q,Poly(1)),(q,p),(Poly(1),p*q)):
        poly=17*S*T-21*(a*T+b*S)
        assert all(e[0]<=2 and e[1]<=2 and e[2:]==(0,0,0) for e in poly.c)
        table=[]
        for i in range(3):
            row0=[]
            for j in range(3):
                value=sum((coef*Q(comb(i,e[0]),comb(2,e[0]))*Q(comb(j,e[1]),comb(2,e[1]))
                           for e,coef in poly.c.items() if e[0]<=i and e[1]<=j),Q(0))
                assert value>=0;row0.append(value)
            table.append(row0)
        tables.append(table)
    expected=[[[27,Q(135,2),225],[Q(135,2),Q(603,4),Q(945,2)],[36,0,0]],
              [[27,Q(135,2),225],[Q(135,2),Q(981,4),945],[225,945,3969]],
              [[27,Q(135,2),36],[Q(135,2),Q(603,4),0],[225,Q(945,2),0]]]
    assert tables==expected
    return tables


def serial(x):
    if isinstance(x,Q):return str(x)
    if isinstance(x,Interval):return [str(x.a),str(x.b)]
    if isinstance(x,dict):return {k:serial(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [serial(v) for v in x]
    return x


def main():
    if not __debug__:raise RuntimeError('Assertions are required; do not use -O')
    assert EPS==Q(1,5000)
    symbols=symbolic_moments();BI=box_data(EPS)
    # Fixed C is the centre reference throughout the moving-centroid box.
    basebound=exact_bound(B0,C,Q(241,50))
    assert BI['U_upper']<Q(498,100)
    trig=trig_majorants(BI['U_upper'])
    tables=sum_bound()
    witnesses=decoded()
    true_spokes={(t,b) for t in (7,8,9) for b in range(7) if tuple(sorted((t,b))) in B0['edges']}
    true_polar={f for f in range(1,9) if (0,f) in B0['dual']}
    assert true_spokes=={(7,0),(7,5),(7,6),(8,1),(8,2),(9,3),(9,4)}
    assert true_polar==set(range(1,8))
    required={(t,b,f) for t,b in true_spokes for f in true_polar}
    cases={(r['top'],r['spoke'],r['polar']) for r in witnesses}
    assert len(witnesses)==len(cases)==49 and cases==required
    records=[];gaps=[]
    for r in witnesses:
        t,b,f=r['top'],r['spoke'],r['polar'];labs=r['labels']
        assert len(labs)==11
        assert ['primal'] in labs and ['polar'] in labs
        assert all(lab[0] in ('psd','primal','polar','order') for lab in labs)
        y,z,center=exact_dual(labs,b,f,top=t)
        assert sum(y)==1 and len(z)==2
        errors=[row_error(lab,b,f,t,BI) for lab in labs]
        total=sum((v*e for v,e in zip(y,errors)),Q(0))
        margin=center+total
        assert margin<0
        gaps.append(-margin)
        records.append({'top':t,'spoke':b,'polar':f,'labels':labs,'positive_weights':y,
                        'equality_weights':z,'centre_margin':center,'row_error_bounds':errors,
                        'weighted_error':total,'whole_box_margin':margin})
    assert min(gaps)>Q(1,100000)
    controls=[census(B0,M) for M in (((5,1,2),(1,3,-1),(2,-1,4)),((3,1,-1),(1,5,2),(-1,2,4)))]
    assert all(not r['weak_edges'] and not r['zero_primitives'] for r in controls)
    report={'theorem':'H5_W_A_PAIRED_ARROW_RECIPROCAL_WHOLE_BOX_V1',
            'theta_centre':THETA,'radius_each_coordinate':EPS,'maximal_facets':FACES,
            'true_edges':B0['edges'],'true_dual_edges':B0['dual'],
            'centre_volume':B0['volume'],'centre_centroid':B0['g'],'fixed_reference_C':C,
            'reference_inverse':CI,'actual_moment_polynomial_identities':symbols,
            'geometry':{k:v for k,v in BI.items() if k not in ('v','poles')},
            'centre_true_edge_factor_certificate':basebound,'finite_height_cosine_majorants':trig,
            'adjacent_gap_upper_bounds':[BI['U_upper']*x for x in trig],
            'normalized_metric_floor':LOW,'normalized_metric_ceiling':UP,'normalized_sum_ceiling':SUM,
            'sum_LMI_bernstein_coefficients':tables,'coordinate_absolute_bounds':XB,
            'case_count':len(records),'minimum_strict_Farkas_gap':min(gaps),'cases':records,
            'actual_centre_nonattaining_controls':controls,
            'scope':'Every actual homogeneous H5 body in the full five-dimensional closed box, and its coordinate reflection, has S>=2 or U>=2 for every physical SPD metric. Extra weak equilibria are allowed. Not all H5/E17 and no110 attainment.'}
    raw=(json.dumps(serial(report),sort_keys=True,indent=2)+'\n').encode()
    path=Path(sys.argv[1] if len(sys.argv)>1 else 'H5_PAIRED_ARROW_BOX_EXACT.json');path.write_bytes(raw)
    print(path.name,len(raw),hashlib.sha256(raw).hexdigest())
    print('H5_W_A_PAIRED_ARROW_RECIPROCAL_WHOLE_BOX_PASS')


if __name__=='__main__':main()
