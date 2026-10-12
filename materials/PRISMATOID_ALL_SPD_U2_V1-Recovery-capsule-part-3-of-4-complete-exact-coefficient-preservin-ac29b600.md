# material-ac29b60083a2

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Exact coefficient-preserving simplification of a complete literal candidate table.
Input is joint_metric_complete.json from joint_metric_probe.py; output is the
final table plus coverage. No implication is inferred from numeric LP status.
"""
from joint_metric_probe import coefficients, trees, pd, ZMAT, matadd,matscale
from pathlib import Path
import json
CC=coefficients(); obj=json.loads(Path('joint_metric_complete.json').read_text())
rows=[]
for c in obj['certificates']:
    old=c['row'];top=max(w for i,w in old);best=old
    for k in range(1,129):
        row=[(i,(2*k*w+top)//(2*top)) for i,w in old];row=[(i,w)for i,w in row if w]
        good=True
        for b in range(4):
            C=ZMAT
            for i,w in row:C=matadd(C,matscale(w,CC[i][b]))
            if not pd(C):good=False;break
        if good:best=row;break
    tup=tuple(map(tuple,best))
    if tup not in rows:rows.append(tup)
rows.sort(key=lambda r:(len(r),sum(w for i,w in r),r))
T=trees();covers=[]
for row in rows:
    mask=sum(1<<i for i,w in row)
    cover=sum(1<<j for j,(m,root,ids) in enumerate(T) if m&mask==mask)
    covers.append(cover)
remaining=(1<<len(T))-1;chosen=[]
while remaining:
    idx=max(range(len(rows)),key=lambda i:((covers[i]&remaining).bit_count(),-len(rows[i]),-sum(w for _,w in rows[i]),-i))
    assert covers[idx]&remaining
    chosen.append(rows[idx]);remaining&=~covers[idx]
chosen.sort()
Path('joint_metric_table.json').write_text(json.dumps(chosen,separators=(',',':'))+'\n')
print('EXACT_PRUNING_ALL_52990_ROOTED_TREES',len(chosen),'of',len(rows),'terms',sum(map(len,chosen)),'max_weight',max(w for r in chosen for i,w in r))
print('TABLE_BEGIN')
for r in chosen:print(' '.join(str(i)+':'+str(w) for i,w in r))
print('TABLE_END')
