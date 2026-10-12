"""Exact section/slab and segment/cylinder certificates for Finch C182.
Requires the complete FINCH3 source capsule; source_root is its directory.
Uses only the Python standard library and the parent's exact clip auditor.
"""
import argparse, hashlib, json, sys
from fractions import Fraction as F
from pathlib import Path
sys.set_int_max_str_digits(0)
SCALE=10**12

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def encoded(x): return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def bind(b,spec):
    assert len(b)==spec['bytes'] and hashlib.sha256(b).hexdigest()==spec['sha256']
def floor12(x): return (x.numerator*SCALE)//x.denominator

def main():
    p=argparse.ArgumentParser();p.add_argument('source_root');p.add_argument('--out',required=True);a=p.parse_args()
    assert __debug__
    root=Path(a.source_root).resolve();sys.path[:0]=[str(root),str(root/'core')]
    import radial,check_B
    case=json.loads((root/'CASES.json').read_bytes())['C182_TWO_PLANE222']
    gb=(root/case['generator']).read_bytes();bind(gb,case['generator_info'])
    raw,_=radial.reconstruct(json.loads(gb))
    for i,row in case['replace'].items():raw['H'][int(i)]=row
    bind(encoded(raw),case['raw']);A=check_B.run(raw);bind(encoded(A),case['audit'])
    assert [A['V'],A['E'],A['F'],*A['counts'],*A['weak']]==[54,91,39,2,2,2,0,0,0]
    g=tuple(map(F,A['raw_centroid']));X=[tuple(F(t)-c for t,c in zip(v,g)) for v in A['raw_vertices']]
    H=[tuple(map(F,row[:3])) for row in raw['H']]
    d=[F(row[3])-dot(n,g) for n,row in zip(H,raw['H'])]
    assert all(t>0 for t in d)
    # Disk radius 31/400 in n-perp, slab halfwidth 7/400.
    n=(8,3,0);nn=dot(n,n);R=F(31,400);h=F(7,400)
    ds=[]
    for u,b in zip(H,d):
        projected=dot(u,u)-F(dot(u,n)**2,nn)
        assert projected>=0 and b*b>R*R*projected
        if projected:ds.append(b*b/(R*R*projected)-1)
    ss=[1-dot(n,x)**2/(h*h*nn) for x in X];assert min(ss)>0
    # Segment of half-length 363/1000 along m, cylinder radius 121/1000.
    m=(-7,12,100);mm=dot(m,m);L=F(363,1000);r=F(121,1000)
    ls=[]
    for u,b in zip(H,d):
        um=dot(u,m)
        assert b*b*mm>L*L*um*um
        if um:ls.append(b*b*mm/(L*L*um*um)-1)
    cs=[1-(dot(x,x)-dot(m,x)**2/F(mm))/(r*r) for x in X];assert min(cs)>0
    report={'object':'FINCH_C182_TWO_PLANE222_SECTION_CERTIFICATE','parent_case':'C182_TWO_PLANE222','parent_raw':case['raw'],'parent_audit':case['audit'],'centroid':'own exact uniform filled-volume centroid from parent clip audit','all_supplied_rows':len(H),'all_vertices':len(X),'census':[A['V'],A['E'],A['F'],*A['counts'],*A['weak']],
        'disk_slab':{'normal':n,'disk_radius':str(R),'slab_halfwidth':str(h),'radius_to_halfwidth':str(R/h),'minimum_disk_relative_squared_slack_floor_1e12':floor12(min(ds)),'minimum_slab_relative_squared_slack_floor_1e12':floor12(min(ss))},
        'segment_cylinder':{'axis':m,'segment_halflength':str(L),'cylinder_radius':str(r),'halflength_to_radius':str(L/r),'minimum_segment_relative_squared_slack_floor_1e12':floor12(min(ls)),'minimum_cylinder_relative_squared_slack_floor_1e12':floor12(min(cs))},
        'consequences':{'stable_facets_at_least':2,'unstable_vertices_at_least':2,'all_affine_images_with_condition_number_less_than_31_over_7_have_S_at_least':2,'all_affine_images_with_condition_number_less_than_3_have_U_at_least':2}}
    b=encoded(report);out=Path(a.out);out.mkdir(parents=True,exist_ok=False);(out/'SHAPE.json').write_bytes(b)
    print('C182_EXACT_DISK_SLAB_AND_SEGMENT_CYLINDER_PASS')
    print(b.decode());print('REPORT_BYTES_SHA256',len(b),hashlib.sha256(b).hexdigest())
if __name__=='__main__':main()
