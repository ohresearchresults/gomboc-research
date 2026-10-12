"""Regenerate the exact C602 parent complex from its small rational contact atlas."""
import hashlib,json,sys
from pathlib import Path
import RECONSTRUCT,check_A
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent

def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def checked_write(name,data,expected_size,expected_hash):
    assert len(data)==expected_size and hashlib.sha256(data).hexdigest()==expected_hash,name
    (ROOT/name).write_bytes(data)
def main():
    raw=RECONSTRUCT.recover(json.loads((ROOT/'GENERATOR.json').read_text()))
    assert len(raw['H'])==136
    a=check_A.run(raw)
    assert [a[k] for k in ['V','E','F']]==[167,301,136]
    assert a['counts']==[1,2,1] and a['weak']==[0,0,0]
    checked_write('PARENT_A.json',canon(a),440262,'2426da394eda9520bd30b2b8b3e1f00d043697353bb6bc73658f5983653c11ec')
    z={'H':raw['H'],'faces':a['faces'],'vertices':a['raw_vertices']}
    checked_write('PARENT_COMPLEX.json',canon(z),106068,'20024df3ddf7d5a5915fe06e6039838e7727dbdfe23bb2d6d291eeb9596d139c')
    print('COORD_C592_EXACT_PARENT_RECONSTRUCTED_FROM_9492_BYTE_ATLAS',flush=True)
if __name__=='__main__':main()
