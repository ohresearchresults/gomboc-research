# material-1531cf8a7e4f

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Exact profile identities and real-facet controls for the all-pairs cap 2.
Dependency: the complete lower_class_exact.py recovery input identified below.
CPython >=3.11; standard library only; assertions must remain enabled.
"""
from pathlib import Path
import hashlib
import json
import sys
from fractions import Fraction as F
from itertools import combinations
BASE_SHA='7b1d742018e07b604636ade49d3c200ae8f788e235b3d4c6f2ab7def349e57f7'
base=Path(__file__).resolve().with_name('lower_class_exact.py')
assert __debug__ and len(base.read_bytes())==12936
assert hashlib.sha256(base.read_bytes()).hexdigest()==BASE_SHA
from lower_class_exact import (make, polygon, det2, sub, dot, serial, equilibria,
                               pa, ps, pm, pc, pp, pt, pe)

IDENTITY='LOWER_EQUALITY_ALL_TRUE_FACET_PAIRS_CAP_2_V1'
OUTPUT='lower_all_pairs_certificate.json'

def sump(*args):
    out={}
    for p in args: out=pa(out,p)
    return out

def prodp(*args):
    out=pc(1)
    for p in args:out=pm(out,p)
    return out

def pshift(poly):
    """Exact substitution r=h+1-s; both sides use the same two exponent slots."""
    h={(1,0):F(1)};s={(0,1):F(1)};r=sump(h,pc(1),pt(s,-1))
    out={}
    for (i,j),v in poly.items():out=pa(out,pt(pm(pp(r,i),pp(s,j)),v))
    return out

def polyrows(poly):
    return [[i,j,v] for (i,j),v in sorted(poly.items())]

def profile_polynomials():
    r={(1,0):F(1)};s={(0,1):F(1)};one=pc(1);w=ps(one,s)
    D=sump(pp(r,2),pm(s,pa(one,r)))
    J=sump(pp(r,3),pm(s,sump(one,r,pp(r,2))))
    N=sump(pm(pp(r,2),pa(one,pt(s,2))),pm(pp(s,2),pa(one,pt(r,2))))
    den=pm(D,N);hinge=ps(pa(r,s),one)
    ap=prodp(r,s,pa(one,pt(s,2)),hinge,sump(pp(r,2),pt(r,2),pc(3)))
    am=prodp(pp(r,2),s,pa(one,pt(r,2)),w,hinge)
    bp=pt(prodp(r,w,pa(one,pt(s,2)),J),3)
    bm=pt(prodp(pp(s,2),pa(one,pt(r,2)),J),3)
    assert sump(ap,am,bp,bm)==pt(den,3)
    A=pa(ap,am)
    assert A==pt(prodp(r,s,hinge,sump(pp(r,2),pm(r,s),r,pt(s,2),one)),3)
    gaps={
        'UU':ps(ps(pt(den,2),ap),pt(bp,F(2,3))),
        'LL':ps(ps(pt(den,2),am),pt(bm,F(2,3))),
        'UL':ps(ps(ps(pt(den,2),ap),am),pt(pa(bp,bm),F(1,3))),
        'UM':ps(ps(pt(den,2),ap),pt(pa(pt(bp,2),bm),F(1,3))),
        'LM':ps(ps(pt(den,2),am),pt(pa(bp,pt(bm,2)),F(1,3))),
        'MM':pt(A,F(2,3))}
    # A second use of exponent slot 0: h=r+s-1 >0 after substitution.
    h=r
    b2=sump(pt(pp(w,3),2),pt(prodp(s,pp(w,2)),18),
            pt(prodp(pp(s,2),w),13),pt(pp(s,3),3))
    b1=sump(pt(pp(w,3),14),pt(prodp(s,pp(w,2)),27),
            pt(prodp(pp(s,2),w),21),pt(pp(s,3),6))
    F_UU=sump(pm(pp(h,4),pa(one,pt(s,2))),
              prodp(pp(h,3),ps(pc(3),pt(s,2)),pa(one,pt(s,3))),
              pm(pp(h,2),b2),prodp(h,s,b1),pt(pm(s,ps(pc(3),pt(s,2))),2))
    F_UM=sump(pp(h,4),pm(pp(h,3),ps(pc(3),pt(s,2))),
              prodp(pp(h,2),ps(pc(2),s),w),pt(pm(s,h),3),
              pm(s,ps(pc(3),pt(s,2))))
    F_LM=sump(pm(pp(h,3),pa(one,s)),prodp(pp(h,2),ps(pc(3),s),pa(one,s)),
              pt(pm(h,pa(one,s)),3),pm(w,pa(one,pt(s,2))))
    F_UL=sump(pp(h,4),pm(pp(h,3),ps(pc(4),pt(s,3))),
              pt(prodp(pp(h,2),ps(pc(3),s),w),2),
              pm(h,pa(pm(w,ps(pc(4),s)),pt(pp(s,2),3))),one)
    # This one is already positive in r,s,1-s, so no substitution is required.
    F_LL=sump(pt(pm(pp(r,2),pa(one,pm(s,w))),2),
              prodp(r,s,sump(pc(3),s,pt(pm(s,w),2))),
              pm(s,sump(pc(3),pt(s,3),pm(s,w))))
    assert pshift(gaps['UU'])==pm(s,F_UU)
    assert gaps['LL']==pm(pp(r,2),F_LL)
    assert pshift(gaps['UM'])==pm(s,F_UM)
    assert pshift(gaps['LM'])==pm(pshift(r),F_LM)
    assert pshift(gaps['UL'])==F_UL
    return {'r_s':{'D':D,'J':J,'N':N,'den':den,'ap':ap,'am':am,'bp':bp,'bm':bm,'A':A},
            'gap_numerators_r_s':gaps,
            'positive_factors':{'UU_h_s':F_UU,'LL_r_s':F_LL,'UM_h_s':F_UM,
                                'LM_h_s':F_LM,'UL_h_s':F_UL}}

def profile_values(s,r):
    s=F(s);r=F(r);assert 0<s<1 and r>1-s
    D=r*r+s*(1+r);J=r**3+s*(1+r+r*r);N=r*r*(1+2*s)+s*s*(1+2*r)
    den=D*N;h=r+s-1;mu=N/(4*D);alpha=3*J/(4*D)
    ap=r*s*(1+2*s)*h*(r*r+2*r+3)
    am=r*r*s*(1+2*r)*(1-s)*h
    bp=3*r*(1-s)*(1+2*s)*J
    bm=3*s*s*(1+2*r)*J
    assert min(ap,am,bp,bm)>0 and ap+am+bp+bm==3*den
    gaps={'UU':2*den-ap-2*bp/3,'LL':2*den-am-2*bm/3,
          'UL':2*den-ap-am-(bp+bm)/3,'UM':2*den-ap-(2*bp+bm)/3,
          'LM':2*den-am-(bp+2*bm)/3,'MM':2*(ap+am)/3}
    b2=2*(1-s)**3+18*s*(1-s)**2+13*s*s*(1-s)+3*s**3
    b1=14*(1-s)**3+27*s*(1-s)**2+21*s*s*(1-s)+6*s**3
    positive={
        'UU':s*((1+2*s)*h**4+(3-2*s)*(1+3*s)*h**3+b2*h*h+s*b1*h+2*s*(3-2*s)),
        'LL':r*r*(2*r*r*(1+s*(1-s))+r*s*(3+s+2*s*(1-s))+s*(3+3*s+s*(1-s))),
        'UL':h**4+(4-3*s)*h**3+2*(3-s)*(1-s)*h*h+((1-s)*(4-s)+3*s*s)*h+1,
        'UM':s*(h**4+(3-2*s)*h**3+(2-s)*(1-s)*h*h+3*s*h+s*(3-2*s)),
        'LM':r*((1+s)*h**3+(3-s)*(1+s)*h*h+3*(1+s)*h+(1-s)*(1+2*s)),
        'MM':2*r*s*h*(r*r+r*s+r+2*s+1)}
    assert gaps==positive and min(gaps.values())>0
    return {'s':s,'rho':r,'D':D,'J':J,'N':N,'den':den,'h':h,'mu':mu,'alpha':alpha,
            'ap':ap,'am':am,'bp':bp,'bm':bm,'gap_numerators':gaps}

def audit(o):
    B=o['B'];n=len(B);A,c=polygon(B);P=o['raw_points'];g=o['geometry']
    p=profile_values(o['s'],o['rho']);den=p['den']
    us=[det2(B[i],B[(i+1)%n])/(2*A) for i in range(n)]
    vs=[det2(sub(B[i],c),sub(B[(i+1)%n],c))/(2*A) for i in range(n)]
    assert sum(us)==sum(vs)==1 and min(us)>=0 and min(vs)>0 and max(vs)<=F(1,3)
    if n>3:assert max(vs)<F(1,3)
    plus=[(p['ap']*u+p['bp']*v)/den for u,v in zip(us,vs)]
    minus=[(p['am']*u+p['bm']*v)/den for u,v in zip(us,vs)]
    assert sum(plus)+sum(minus)==3
    faces=[]
    for f in g['faces']:
        ids=set(f['cycle']);r=dict(f)
        if ids==set(range(n)):
            assert f['root_trace']==0
            r.update({'kind':'R','base_edge':None});faces.append(r);continue
        found=[]
        for j in range(n):
            low={j,(j+1)%n,n+j,n+(j+1)%n};up={n+j,n+(j+1)%n,2*n}
            il=all(dot(f['normal'],P[z])==f['h'] for z in low)
            iu=all(dot(f['normal'],P[z])==f['h'] for z in up)
            if il or iu:found.append((j,il,iu))
        assert len(found)==1
        j,il,iu=found[0]
        assert f['root_trace']==(minus[j] if il else 0)+(plus[j] if iu else 0)
        kind='M' if il and iu else ('L' if il else 'U')
        assert (kind=='M')==(us[j]==0)
        r.update({'kind':kind,'base_edge':j});faces.append(r)
    pairs=[]
    for i,j in combinations(range(len(faces)),2):
        f,k=faces[i],faces[j];types={f['kind'],k['kind']}
        if 'R' in types:boundtype='UL'
        elif types=={'U'}:boundtype='UU'
        elif types=={'L'}:boundtype='LL'
        elif types=={'M'}:boundtype='MM'
        elif types=={'U','L'}:boundtype='UL'
        elif types=={'U','M'}:boundtype='UM'
        elif types=={'L','M'}:boundtype='LM'
        else:raise AssertionError(types)
        T=f['root_trace']+k['root_trace'];gap=p['gap_numerators'][boundtype]/den
        assert 0<T<=2-gap<2
        shared=set(f['cycle'])&set(k['cycle']);adjacent=len(shared)==2
        # Maximal true facets intersect at a true edge or at most one vertex.
        assert len(shared)<=2
        pairs.append({'faces':[i,j],'cycles':[f['cycle'],k['cycle']],
                      'kinds':[f['kind'],k['kind']],'bound_type':boundtype,
                      'adjacent':adjacent,'root_disjoint_edge':adjacent and not (shared&set(range(n))),
                      'trace':T,'profile_gap':gap,'residual_after_profile_bound':2-gap-T})
    return {'input_B':B,'profile':p,'planar_area':A,'planar_centroid':c,
            'origin_cone_fractions':us,'centroid_cone_fractions':vs,'raw_points':P,
            'geometry':g,'actual_facets':faces,'all_pairs':pairs}

def build_report():
    poly=profile_polynomials()
    literal_polys={group:{name:polyrows(p) for name,p in rows.items()} for group,rows in poly.items()}
    Blist=[[(0,0),(2,0),(0,2)],[(0,0),(3,0),(4,1),(1,4),(0,2)],
           [(0,0),(1,0),(100,50),(50,100),(0,1)]]
    profiles=[(F(1,100),2),(F(1,2),2),(F(3,4),F(1,2)),
              (F(99,100),F(1,50)),(F(99,100),100)]
    controls=[]
    for B in Blist:
        A,c=polygon([tuple(map(F,b)) for b in B])
        for O in [c,(0,0),(F(1),0)]:
            for s,r in profiles:
                q=audit(make(B,s,r,O));q['recovery_original_B']=B;q['recovery_origin']=O
                controls.append(q)
    sharp=[]
    for R in [2,5,20,100]:
        B=[(0,0),(1,0),(R,F(R,2)),(F(R,2),R),(0,1)]
        o=make(B,F(1,R),2);q=audit(o);q['R']=R
        assert q['geometry']['f_vector']==[10,17,9]
        q['euclidean_equilibria']=equilibria(o['raw_points'],o['geometry'])
        assert not q['euclidean_equilibria']['boundary_entities']
        assert q['euclidean_equilibria']['strict_counts_S_U_H']!=[1,1,0]
        n=5;target_u=F(3*R+2,3*R+4)
        target_v=F(2,3)-F(2*(3*R+2)**2,3*R*(3*R+4)**2)
        target_T=(q['profile']['ap']*target_u+q['profile']['bp']*target_v)/q['profile']['den']
        tt=[p for p in q['all_pairs'] if p['adjacent'] and p['kinds']==['U','U']]
        assert len(tt)==2 and all(p['trace']==target_T for p in tt)
        q['sharp_pair_formula']={'u':target_u,'v':target_v,'T':target_T}
        sharp.append(q)
    count_all=sum(len(q['all_pairs']) for q in controls)
    count_adj=sum(p['adjacent'] for q in controls for p in q['all_pairs'])
    count_rootdisjoint=sum(p['root_disjoint_edge'] for q in controls for p in q['all_pairs'])
    assert len(controls)==45 and count_adj==710 and count_rootdisjoint==320
    return {'identity':IDENTITY,'recovery_input_base_sha256':BASE_SHA,
            'coefficientwise_polynomial_identities':literal_polys,
            'finite_exact_controls':controls,'sharp_E17_controls':sharp,
            'counts':{'control_bodies':len(controls),'all_facet_pairs':count_all,
                      'adjacent_pairs':count_adj,'root_disjoint_adjacent_pairs':count_rootdisjoint,
                      'sharp_controls':len(sharp)},
            'scope':{'all_two_distinct_true_facets_in_one_kink_equality_class':True,
                     'FULL253_E17_lower_equality_excluded_without_terminal_triangle_assumption':True,
                     'whole_FULL253_mechanical_excluded':False,
                     'whole_E17_layer_excluded':False,'universal_C_lower_bound':34,
                     'exact_minimum_found':False}}

def main():
    if len(sys.argv)!=2 or sys.argv[1] not in ('build','check'):
        raise SystemExit('Usage: python -S lower_all_pairs_exact.py build|check')
    r=build_report();data=(json.dumps(serial(r),sort_keys=True,indent=2)+'\n').encode('utf-8')
    p=Path(OUTPUT)
    if sys.argv[1]=='build':p.write_bytes(data)
    else:assert p.read_bytes()==data
    print('LOWER_ALL_PAIRS_COEFFICIENT_IDENTITIES_PASS',6)
    print('LOWER_ALL_PAIRS_TRUE_GEOMETRY_PASS',r['counts']['control_bodies'])
    print('LOWER_ALL_PAIRS_EXACT_TRACE_CAP_PASS',r['counts']['all_facet_pairs'])
    print('LOWER_ALL_PAIRS_ADJACENCY_CONTROLS_PASS',r['counts']['adjacent_pairs'],r['counts']['root_disjoint_adjacent_pairs'])
    print('LOWER_ALL_PAIRS_SHARP_E17_CONTROLS_PASS',r['counts']['sharp_controls'])
    print('LOWER_ALL_PAIRS_RECOVERY_PASS',len(data),hashlib.sha256(data).hexdigest())
if __name__=='__main__':main()
