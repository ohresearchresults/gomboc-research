# material-031f65e52f44

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# COORD_LOCAL_LP_V2: avoid premature global escape-tree reversal

Complete exact source dependency: material [internal-source-reference], COORD_TREE_LP_V1_COMPLETE_SOURCE.md, material SHA256 8a0e1e19f3815e45897eb3f7ebc08eee1f79ae2211ed984f7fa5fcfbbc84ccea. Extract its entire TREE_LP.py code (9083 bytes, SHA256 856cbf05e88e788813685866e3ad5046a52f1f37065bd5c4ac54e355224ea5c0). Its NC57 immutable parent input dependencies and Python/NumPy/SciPy/PyTorch versions remain unchanged. This patch is complete and does not omit helpers. Save the following code as LOCAL_PATCH.py, 1036 bytes, SHA256 0e08abb4cf2b060a60b980dc6355c2f49aa37508212274a077695ab928789c30. Run `python -B -S LOCAL_PATCH.py TREE_LP.py LOCAL_LP.py` to create LOCAL_LP.py, 8944 bytes, SHA256 b6679704dd2fb2df6fee0deb7687e6eb73a943e36ffc7f8c4c7bd0d3887f9b03. Terminal COORD_LOCAL_LP_V2_SOURCE reports both size and hash.

V2 chooses each nonroot's currently largest adjacent angular escape, without prematurely requiring the chosen edges to form a global directed tree. It refreshes those witnesses every accepted step. A feasible strictly positive final set cannot contain a cycle because every positive escape strictly increases squared radius. During infeasible continuation, temporary witness cycles are allowed. Actual filled-solid mass, complete fixed-triangle support inequalities, positive-target common deficit, volume/separation guards, and backtracking are otherwise unchanged. This is still a finite restricted numerical method, not a theorem of existence or exclusion. No V2 search has yet run when preserving this patch.

Reason for change: V1's C378 root75 initial shortest-path tree uses 49 negative polar arrows, with the worst approximately -0.96795, although the original body has only two stable equilibria and its second-largest-root local escape deficit is about 7.37e-5. Its first five accepted steps preserve floating convexity but increase the equilibrium count to S5/U19. Forcing an entire root basin to reverse at once while allowing every previously positive witness the same large deficit is the wrong feasibility homotopy. This observation concerns these exact-source starts, not all escape trees.

Fresh-run examples: `python LOCAL_LP.py NC57_SOURCE/proof/C378_ALT_POLY_G6/REPORT.json LOCAL378_R75 120 75 .001 173782`; same for root16, or C372 roots0/107. Numeric terminal marker remains COORD_TREE_LP_FINISHED, and any NUMERICAL_WINNER.json remains only a proposal pending independent exact verification. Preserve actual new frozen checkpoints separately.

```python
#!/usr/bin/env python3
"""Create COORD_LOCAL_LP_V2 from the complete immutable TREE_LP_V1 source."""
from pathlib import Path
import hashlib, sys
p=Path(sys.argv[1]); text=p.read_text()
assert hashlib.sha256(p.read_bytes()).hexdigest()=='856cbf05e88e788813685866e3ad5046a52f1f37065bd5c4ac54e355224ea5c0'
start=text.index('    co=np.maximum(gamma-ar,0)**2')
end=text.index('\ndef convex_data',start)
text=text[:start]+'''    ids=np.array([i for i in range(len(W)) if i!=root],dtype=int)
    targets=[]
    for i in ids:
        ix=np.where(e[:,0]==i)[0]
        targets.append(int(e[ix[np.argmax(ar[ix])],1]))
    return ids,np.array(targets,dtype=int)
'''+text[end:]
text=text.replace('COORD_TREE_LP_V1','COORD_LOCAL_LP_V2').replace("tree_refresh=5","tree_refresh=1").replace('treeage>=5','treeage>=1')
text=text.replace('Own-centroid escape-tree sequential LP','Own-centroid local-witness sequential LP')
Path(sys.argv[2]).write_text(text)
print('COORD_LOCAL_LP_V2_SOURCE',len(text.encode()),hashlib.sha256(text.encode()).hexdigest())
```
