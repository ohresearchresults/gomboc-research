# material-d6b2efc0e71f

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

#!/usr/bin/env python3
"""Both selected facets are actual triangles; the bipyramid sharp bound does not extend to E17."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json, sys
PIN='d2f4cb8a50970bb8f6aa528ca8a3e903ca565361172f61e23032d861d4b053ff'
assert hashlib.sha256(Path(__file__).with_name('pair_trace_e17.py').read_bytes()).hexdigest()==PIN
import pair_trace_e17 as p

def build():
    vs=[tuple(map(F,x)) for x in [(0,0,0),(0,0,1),(0,1,0),(1,0,0)]]
    vs += [(F(1,1000),F(4,5),F(1,4)),(F(4,5),F(1,1000),F(1,4))]
    original=p.hull(vs);assert original['f_vector']==[6,11,7]
    root=p.facet_with_vertices(original,{2,3,4,5});b=p.facet_with_vertices(original,{0,1,2});c=p.facet_with_vertices(original,{0,1,3})
    planes=[original['faces'][i]['plane'] for i in (root,b,c)]
    total=original['Lambda'][root][b]+original['Lambda'][root][c]
    assert total==F(96701835614000,47674994261293)>F(253,125)
    original['selected_indices']=[root,b,c];original['selected_sum']=total
    once=p.truncate(vs,4,F(1,100));assert p.hull(once)['f_vector']==[8,14,8]
    final=p.truncate(once,4,F(1,100));body=p.hull(final)
    assert body['f_vector']==[10,17,9]
    aa,bb,cc=[p.facet_with_plane(body,z) for z in planes]
    assert len(body['faces'][bb]['vertices'])==len(body['faces'][cc]['vertices'])==3
    assert any(set((bb,cc))==set(edge[2:]) for edge in body['edges'])
    value=body['Lambda'][aa][bb]+body['Lambda'][aa][cc]
    assert F(253,125)<value<F(51,25)
    body['selected_indices']=[aa,bb,cc];body['selected_sum']=value
    body['selected_facet_sizes']=[len(body['faces'][i]['vertices']) for i in (aa,bb,cc)]
    body['selected_gap_over_253_125']=value-F(253,125)
    body['selected_gap_under_51_25']=F(51,25)-value
    assert all(not z for z in body['boundary_contacts'].values())
    assert len(body['S'])+len(body['U'])-len(body['H'])==2
    assert (len(body['S']),len(body['U']),len(body['H']))!=(1,1,0)
    return {'identity':'ACTUAL_ADJACENT_TRIANGLES_E17_EXCEED_BIPYRAMID_SHARP_BOUND_V1',
            'base_source_sha256':PIN,'cut_fractions':['1/100','1/100'],
            'six_vertex_parent':original,'e17_control':body}

def main():
    assert len(sys.argv)==2 and sys.argv[1] in ('build','check')
    obj=p.encode(build());data=(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode()
    path=Path('triangle_pair_e17_report.json')
    if sys.argv[1]=='build':path.write_bytes(data)
    else:assert path.read_bytes()==data
    b=obj['e17_control']
    print('ACTUAL_TRIANGLE_PAIR_E17_EXACT_PASS',*b['f_vector'],len(b['S']),len(b['U']),len(b['H']))
    print('SELECTED_FACET_SIZES',*b['selected_facet_sizes'])
    print('BIPYRAMID_BOUND_BROKEN_BUT_51_25_NOT_CROSSED',b['selected_sum'])
    print('REPORT',len(data),hashlib.sha256(data).hexdigest())
    print('NOT_TREE253_NOT_GOMBOC_NOT_A_NEW_LOWER_BOUND')
if __name__=='__main__':main()
