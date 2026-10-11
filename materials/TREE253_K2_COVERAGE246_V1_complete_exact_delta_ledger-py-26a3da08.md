# material-26a3da08956d

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

"""TREE253_K2_COVERAGE246_V1. Exact delta from accepted214 and frozen10/13.
Recover both frozen common-root capsules and their exact source dependencies.
python -S coverage246.py ; python -S coverage246.py --verify
The old214 is an explicitly inherited theorem, not rerun by this source.
"""
from pathlib import Path
import sys,json,hashlib
import common_roots as cr
fm=cr.fm
assert __debug__
HERE=Path(__file__).resolve().parent
OLD_WHOLE=list(range(10))+[12,16,18]
W06=[4,8,9,10,11,13,14,15,17,19,20,24,25,26,39,41,43,44,46,48]
OPEN28=[10,13,15,17,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,37,38,43,44,48,51,52,53,54]
PINS={
10:[[54157,'aee672519acddbe8ddab607742fd93d89ddc916fc646ef58bb1689bc8806f0f6'],[5116,'f3f2b9d91eba533e154b7d3a41b065d30d0463cd93d4194c92a20e68990dbaa0']],
13:[[55137,'048c59685d993834a5863af88806c7cea203edeb36eb8c58d54c1d967e3c556b'],[5116,'d4797f84e0d43381d390af92c3dfc55febad0842fa0e958b13832e1470a61aa2']]}
PERMS={(10,11):[0,7,4,9,2,6,8,5,1,3],(13,14):[0,8,4,9,2,6,5,7,1,3]}
FP=[4,3,2,1,0,7,8,5,6]

def build():
    old={(i,r) for i in range(55) for r in range(10) if r in (0,9) or i in OLD_WHOLE}
    assert len(old)==214
    prior=old|{(10,1),(11,8)};assert len(prior)==216
    covered=set(prior);reports=[];transports=[];inp=fm.inputs()
    for a,b in sorted(PERMS):
        data=(HERE/f'common_certificate_{a}_root.json').read_bytes();assert fm.pin(data)==PINS[a][0]
        rec=json.loads(data);assert rec['native_index']==a and rec['mode']=='root'
        report=cr.check(rec);assert fm.pin(fm.enc(report))==PINS[a][1]
        assert report['roots']==list(range(1,9))
        assert report['total_leading_minors']==10*report['total_blocks']
        reports.append({'native_index':a,'record_pin':PINS[a][0],'report_pin':PINS[a][1],
                        'blocks':report['total_blocks'],'leading_minors':report['total_leading_minors']})
        pa,ea,fa=fm.geometry(inp[a]);pb,eb,fb=fm.geometry(inp[b]);p=PERMS[a,b]
        assert sorted(p)==list(range(10))
        assert all(p[pa[j]]==pb[9-j] for j in range(10))
        assert sorted(tuple(sorted((p[i],p[j]))) for i,j in ea)==eb
        for j,cy in enumerate(fa):
            assert {p[pa[v]] for v in cy}=={pb[v] for v in fb[FP[j]]}
        transports.append({'source':a,'target':b,'vertex_permutation':p,'facet_permutation':FP,
                           'source_path':pa,'target_path':pb,'root_position_map':list(reversed(range(10)))})
        covered|={(a,r) for r in range(1,9)}|{(b,r) for r in range(1,9)}
    added=sorted(covered-prior);universe={(i,r) for i in range(55) for r in range(10)}
    whole=[i for i in range(55) if all((i,r) in covered for r in range(10))]
    assert len(added)==30 and len(covered)==246 and len(universe-covered)==304
    assert whole==list(range(15))+[16,18]
    wclosed=sorted(q for q in covered if q[0] in W06);wopen=sorted(q for q in universe-covered if q[0] in W06)
    assert len(wclosed)==96 and len(wopen)==104
    result={'identity':'TREE253_K2_COVERAGE246_V1',
        'inherited214_source':'[internal-source-reference]',
        'inherited216_increment_source':'[internal-source-reference]',
        'case10_sources':['[internal-source-reference]','[internal-source-reference]'],
        'case13_sources':['[internal-source-reference]','[internal-source-reference]'],
        'whole_native_rows':whole,'excluded':sorted(covered),'remaining':sorted(universe-covered),
        'new30':added,'direct_matrix_reports':reports,'actual_facet_path_transports':transports,
        'open_class_representatives':[i for i in OPEN28 if i not in (10,13)],
        'w06':{'excluded':wclosed,'remaining':wopen,'whole':[i for i in W06 if i in whole]},
        'scope':'native incidence/root POSITION domains; not global types',
        'unchanged':['C>=34','global632_types_52585_joint_roots','TREE410_17383_of_24847']}
    return fm.enc(result)
if __name__=='__main__':
    assert sys.argv[1:] in ([],['--verify'])
    data=build();p=HERE/'coverage246.json'
    if sys.argv[1:]:assert p.read_bytes()==data
    else:p.write_bytes(data)
    print('TREE253_K2_COVERAGE246_EXACT_PASS 216 30 246 304 17 96 104 26')
    print('OUTPUT',*fm.pin(data))
