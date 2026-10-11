"""Run both previously preserved exact auditors; explicitly expect NONWINNERS."""
from pathlib import Path
import hashlib, json, sys
import RECONSTRUCT, check_A, check_B
sys.set_int_max_str_digits(0)
assert not sys.flags.optimize
root=Path(__file__).resolve().parent
expected={
    'C630_COORD_NONWINNER_OWN121': ([180,315,137],358975,'a14590ad90680d5ebfa0f3def830d5c4ee4ee8bf8992c27abce5ad7c388c279b'),
    'C632_COORD_NONWINNER_OWN121': ([181,316,137],366044,'a4df66d298812a6e7cd0d0b3c056696e13cc3075fdf69a866d4e43a6dad84f6e'),
}
for name,(vef,size,sha) in expected.items():
    path=root/name
    raw=RECONSTRUCT.recover(json.loads((path/'GENERATOR.json').read_bytes()))
    a=check_A.run(raw)
    b=check_B.run(raw)
    assert a==b
    assert [a[k] for k in ['V','E','F']]==vef
    assert a['counts']==[1,2,1] and a['weak']==[0,0,0]
    for key in ['face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']:
        assert a[key]==0
    blob=json.dumps(a,sort_keys=True,separators=(',',':')).encode()
    assert len(blob)==size and hashlib.sha256(blob).hexdigest()==sha
    for filename in ['A.json','B.json']:
        with (path/filename).open('xb') as f:f.write(blob)
    print(name,vef,[1,2,1],[0,0,0],sha,'BOTH_EXACT_AUDITORS_AND_AUTHOR_HASH_PASS',flush=True)
