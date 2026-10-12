from pathlib import Path
import json,hashlib
import comb
from reconstruct import iterjobs
FS=tuple(tuple(map(int,s)) for s in
 '014 021 032 043 125 154 235 347 365 376 458 487 568 678'.split())
G=comb.catalogue(True)
assert tuple(map(tuple,G[45]['facets']))==FS
parents=comb.parent_trees(G[45],3)
assert len(parents)==9140
assigned={1200,1205,1472,1752,1775,3058,3124,3149,3966,5772,7000}
shape=comb.root_code(parents[1200],3)
triangles={frozenset(f) for f in FS}
selected={}
for index,p in enumerate(parents):
    if comb.root_code(p,3)!=shape:
        continue
    paths=[]
    for i in range(9):
        path=[i]
        while path[-1]!=3:
            path.append(p[path[-1]])
        paths.append(path)
    b=list(reversed(max(paths,key=len)))
    assert len(b)==8
    b.append(next(i for i in range(9) if i not in b))
    if frozenset(b[5:8]) in triangles:
        selected[tuple(p)]=dict(original_index=index,parent=list(p),broom_order=b)
assert len(selected)==66
wanted={p:r for p,r in selected.items() if r['original_index'] not in assigned}
assert len(wanted)==55
meta=json.loads(Path('plan.json').read_bytes())
out=[]
for serial,g,root,p,plan in iterjobs(meta):
    key=tuple(p)
    if root==3 and tuple(map(tuple,g['facets']))==FS and key in wanted:
        out.append(dict(**wanted[key],serial=serial,plan=plan))
assert len(out)==55 and len({r['original_index'] for r in out})==55
out.sort(key=lambda r:r['original_index'])
raw=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode()
Path('mp45_root3_55_old_plans.json').write_bytes(raw)
print('MP45_ROOT3_55_OLD_SUCCESSFUL_PLANS_EXTRACTED_NO_NEW_EXCLUSION_ASSERTED')
print(len(raw),hashlib.sha256(raw).hexdigest())
