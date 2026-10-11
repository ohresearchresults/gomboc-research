"""Select the numerically exposed input points; final geometry is exact-audited."""
import hashlib,json,sys
from pathlib import Path
import numpy as np
from geometry import census,write_json

data=Path(sys.argv[1]).read_bytes()
p=np.array(json.loads(data)['points'],float)
ids=census(p,True)['hull'].vertices
out=dict(points=p[ids].tolist(),source_point_ids=ids.tolist(),
         input=sys.argv[1],input_sha256=hashlib.sha256(data).hexdigest(),
         selection='Floating hull selection; this is a proposal, not an exact census.')
write_json(sys.argv[2],out)
print('ACTIVE_POINT_PROPOSAL',len(p),len(ids),ids.tolist())
