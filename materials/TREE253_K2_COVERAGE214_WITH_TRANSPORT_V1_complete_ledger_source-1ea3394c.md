# material-1ea3394c2941

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

"""TREE253_K2_COVERAGE214_WITH_TRANSPORT_V1, complete deterministic ledger.

Save this full literal material as coverage214.py. Reconstruct its exact inputs
using the complete commands/dependency map in proof40
[internal-source-reference], SHA
32d9113122c34015de2497bec5704b9bc680d5689ddc4c0bcd5474d8f338729d,
and the complete transport source [internal-source-reference], SHA
4a4c26be277540ea88a012c66cf7a8373bd65d0f4c935ae717a99b4acf8c3c1a.
Both should be recovered in the same directory as this script. The first
source maps all nine native case files, the shared exact checkers and the
pinned output reports; the second reproduces transport_37_classes.json.
No further hidden input or numerical optimization is required.

Reconstruction command: python -S coverage214.py
Verification command:   python -S coverage214.py --verify
Expected marker: TREE253_K2_COVERAGE_EXACT_PASS 150 40 24 214 336 13 64 136 28
Expected output: coverage214.json, with OUTPUT_PIN below.

This ledger checks pins, incidence/root alignment, explicit transport maps,
non-overlap of direct new records with the earlier150, and exact set closure.
It is NOT a substitute for the mathematical proofs or matrix checkers. The
old endpoint theorem and old38/native4 sources are already accepted proofs;
their explicit domains/coverage are literal below. Every theorem/certificate
used has its exact source references in SOURCES and CASE_SOURCES. All nine
checkpoint40 reports must be reproduced by their frozen exact checker before
this program accepts their record lists. The complete source and both decoded
integers and reproduced reports are immutable dependencies, not merely hashes.

Transports apply only to internal-root universal incidence/path exclusions.
In particular they DO NOT transport the endpoint theorem using path geometry
alone: that theorem additionally uses the full native pole-domain hypotheses.
Each native domain has its OWN endpoint theorem. Native numbers always mean
pZ parent55_index, not global632 polyhedral-type IDs. Explicit native vertex
and facet permutations are retained and no pole-labelled domain is aliased.

Result scope: 214/550 native incidence/root pairs excluded,336 unresolved;
13 whole native domains excluded,42 not wholly excluded. Exactly28 of37
facet/path representatives remain wholly open at internal roots. W06 has
64/200 excluded136 unresolved, whole native4,8,9 closed17 placements remaining.
Universal C>=34, global632/52585 and TREE41017383/24847 remain unchanged.
"""
from pathlib import Path
import hashlib,json,sys
assert __debug__
ROOT=Path(__file__).resolve().parent
OUTPUT_PIN=[27649, '336d0feefc4ece0f7aacedfef04315d9d9a492e35638c2a228a3885362051464']
TRANSPORT_PIN=[5872,'403b00acabd759d695eb748568b0cd17b1fae94b5bedcaea40cb7a6f6df1adb8']
CASE_PINS={0:[29354,'960b9d9f570c954ea8c57334f7e42be187a53a9ed08076b67d5b439208b6ca65'],1:[29156,'010ac21d4e32eb0c342ef2cb988398a70e312bfca0254dfe214ea006f7c3510f'],2:[15880,'60758b9d5b0200bd7e2aaccedbf286a5692c98e119c87a5c3a9312deee8a04c9'],3:[14309,'1c0b77e02863c5c0862ce67864dd8e379c343360a5fc97d33fa7005d277e378b'],5:[11121,'38d40db498f315da9fdbc74a80d5e8e3193e9e4f605ba89c93ebd62ce73ca73d'],6:[11688,'d459310e83380f7d9085af514fdf097c312e7c87249684b4313704ba867c749d'],7:[11335,'e4117f52a47f28968c87b3125999e94046cff17afb025b2635f78cb0c271d808'],8:[6253,'1a80d70438d18b72d06a860ffe1e2f814c8cf7d858f4af32b4754a457927d6b1'],9:[6261,'28c9f2eed87f08cb09b1ab9dbe6b5667a61163d73f3739d22e5fcdf8bfae1d84']}
SOURCES={
'endpoints':{'assignment_id':'minimum-0078','sha256':'2a0d3544bfb7f0c3b6366bdda3555bc650eede67a1444d51a2d7207a0079eecd','theorem':'B: own native pole-domain simple endpoints; application also uses theorem A'},
'checkpoint38':{'parts':['[internal-source-reference]','[internal-source-reference]','[internal-source-reference]'],'proof':'[internal-source-reference]','source_pin':[38101,'ea3892417235991b9b97013fbb3ddfd8cdfd727cadd07e31b619a760f012992e'],'domain':'universal genuine incidence/weak path, own uniform-volume centroid, one SPD metric'},
'native4':{'parts':['[internal-source-reference]','[internal-source-reference]'],'proof':'[internal-source-reference]','source_pin':[15582,'14ca6e44721923fc7662496ebc5698571b63bb20b28c2132d74ce5607b9d310e'],'domain':'native4 internal positions1,8'},
'checkpoint40':{'shared_source':'[internal-source-reference]','proof':'[internal-source-reference]','methods':'[internal-source-reference]','domain':'universal genuine incidence/weak path, own uniform-volume centroid, one SPD metric'},
'path_transport':{'source':'[internal-source-reference]','output_pin':TRANSPORT_PIN,'theorem':'actual maximal-facet/path relabelling; root reflection; no full pole-graph identification'}}
CASE_SOURCES={0:['[internal-source-reference]','[internal-source-reference]'],1:['[internal-source-reference]','[internal-source-reference]'],2:['[internal-source-reference]'],3:['[internal-source-reference]'],5:['[internal-source-reference]'],6:['[internal-source-reference]'],7:['[internal-source-reference]'],8:['[internal-source-reference]'],9:['[internal-source-reference]']}
OLD38={i:tuple(range(3,7)) for i in (2,3,5,6,7)}
OLD38.update({i:tuple(range(2,8)) for i in (4,8,9)})
NEW40={0:tuple(range(1,9)),1:tuple(range(1,9)),2:(1,2,7,8),3:(1,2,7,8),5:(1,2,7,8),6:(1,2,7,8),7:(1,2,7,8),8:(1,8),9:(1,8)}
W06=(4,8,9,10,11,13,14,15,17,19,20,24,25,26,39,41,43,44,46,48)

def enc(x):return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
def reconstruct():
    b=(ROOT/'transport_37_classes.json').read_bytes();assert pin(b)==TRANSPORT_PIN
    tr=json.loads(b);assert tr['identity']=='TREE253_K2_PRIMAL_PATH_TRANSPORT_V1'
    classes=tr['classes'];assert len(classes)==37
    assert sorted(i for c in classes for i,_ in c)==list(range(55))
    parents={};internals={};stages=[]
    for i in range(55):
        for r in (0,9):parents[i,r]=['endpoints',i,r]
    assert len(parents)==110
    for i,roots in sorted(OLD38.items()):
        for r in roots:
            assert (i,r) not in parents
            parents[i,r]=['checkpoint38',i,r];internals[i,r]=parents[i,r]
    assert len(parents)==148
    for r in (1,8):
        assert (4,r) not in parents
        parents[4,r]=['native4',4,r];internals[4,r]=parents[4,r]
    assert len(parents)==150
    stages.append(['prior_endpoint_and_actual_centroid_exclusions',len(parents)])
    base=set(parents);blocks=0;minors=0;new=[];report_pins={}
    for i,p in sorted(CASE_PINS.items()):
        data=(ROOT/f'case_{i:02d}.txt').read_bytes();assert pin(data)==p
        meta=json.loads(data.split(b'\n',1)[0]);assert meta['native_index']==i
        assert meta['new_root_positions']==list(NEW40[i])
        reported=[]
        for checker,inp,report,log in meta['commands']:
            assert checker in meta['checker_pins']
            assert pin((ROOT/'shared_code'/checker).read_bytes())==meta['checker_pins'][checker]
            directory=ROOT/f'native_{i:02d}'
            for name in (report,log):
                bb=(directory/name).read_bytes();assert pin(bb)==meta['output_pins'][name]
                report_pins[f'native_{i:02d}/{name}']=pin(bb)
            bb=(directory/inp).read_bytes();assert pin(bb)==meta['input_pins'][inp]
            payload=json.loads(bb);rep=json.loads((directory/report).read_text())
            assert payload['incidences']=={str(i):rep['records'][0]['incidence']}
            assert [(z['native_index'],z['root']) for z in payload['records']]==[(z['native_index'],z['root']) for z in rep['records']]
            assert rep['total_blocks']==sum(z['cells'] for z in rep['records'])
            assert rep['total_positive_leading_minors']==sum(z['positive_leading_minors'] for z in rep['records'])
            for z in rep['records']:
                r=z['root'];assert z['native_index']==i and (i,r) not in parents
                assert z['native_root']==z['path'][r] and sorted(z['path'])==list(range(10))
                assert len(z['edges'])==17 and len(z['faces'])==9
                assert z['positive_leading_minors']==10*z['cells'] and int(z['least_leading_minor'])>0
                parents[i,r]=['checkpoint40',i,r,inp,report]
                internals[i,r]=parents[i,r]
                new.append([i,r]);reported.append(r);blocks+=z['cells'];minors+=z['positive_leading_minors']
        assert sorted(reported)==list(NEW40[i])
    assert len(parents)==190 and len(new)==40 and blocks==3652 and minors==36520
    assert not(base&{tuple(q) for q in new})
    stages.append(['after40_frozen_common_moment_certificates',len(parents)])
    direct=dict(internals);moved=[]
    for t in tr['transports']:
        a=t['source_native_index'];b=t['target_native_index']
        assert a<b and sorted(t['native_vertex_permutation'])==list(range(10))
        assert sorted(t['facet_permutation'])==list(range(9))
        assert t['path_position_permutation']==list(reversed(range(10)))
        for r in range(1,9):
            assert t['native_vertex_permutation'][t['source_path'][r]]==t['target_path'][9-r]
        for src,dst in ((a,b),(b,a)):
            for r in range(1,9):
                if (src,r) not in direct or (dst,9-r) in parents:continue
                basis=['path_transport',src,r,dst,9-r,direct[src,r]]
                parents[dst,9-r]=basis;moved.append([src,r,dst,9-r])
    assert len(moved)==24 and {(a,b) for a,r,b,s in moved}=={(5,12),(6,18),(7,16)}
    assert len(parents)==214
    stages.append(['after24_facet_path_transports',len(parents)])
    universe={(i,r) for i in range(55) for r in range(10)}
    remaining=sorted(universe-set(parents));whole=[i for i in range(55) if all((i,r) in parents for r in range(10))]
    assert len(remaining)==336 and whole==list(range(10))+[12,16,18]
    wclosed=sorted((i,r) for i,r in parents if i in W06)
    wopen=sorted((i,r) for i,r in remaining if i in W06)
    wwhole=[i for i in W06 if i in whole]
    assert len(wclosed)==64 and len(wopen)==136 and wwhole==[4,8,9]
    reps=[]
    for group in classes:
        ids=[i for i,_ in group]
        if all(i in whole for i in ids):continue
        assert all(i not in whole for i in ids)
        assert all((i,r) not in parents for i in ids for r in range(1,9))
        reps.append(min(ids))
    assert len(reps)==28
    output={'identity':'TREE253_K2_COVERAGE214_WITH_TRANSPORT_V1','sources':SOURCES,'case_sources':CASE_SOURCES,
        'case_pins':CASE_PINS,'checked_report_pins':report_pins,'stages':stages,'new40':sorted(new),
        'new_transports':sorted(moved),'excluded':[{'native_index':i,'root_position':r,'basis':parents[i,r]} for i,r in sorted(parents)],
        'remaining':remaining,'whole_native_domains':whole,'open_facet_path_class_representatives':reps,
        'w06':{'indices':W06,'excluded':wclosed,'remaining':wopen,'whole_excluded':wwhole},
        'matrix_evidence40':{'records':40,'positive_definite_10_by_10_blocks':blocks,'positive_leading_minors':minors},
        'not_updated':['universal_C_ge_34','global632_types_and52585_joint_roots','TREE41017383of24847']}
    return enc(output)
if __name__=='__main__':
    assert sys.argv[1:] in ([],['--verify'])
    b=reconstruct()
    if OUTPUT_PIN is not None:assert pin(b)==OUTPUT_PIN
    p=ROOT/'coverage214.json'
    if sys.argv[1:]:assert p.read_bytes()==b
    else:
        if p.exists():assert p.read_bytes()==b
        p.write_bytes(b)
    print('TREE253_K2_COVERAGE_EXACT_PASS 150 40 24 214 336 13 64 136 28')
    print('OUTPUT',*pin(b))
