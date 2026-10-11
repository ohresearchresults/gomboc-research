import json,math,hashlib,sys
from fractions import Fraction as F
from pathlib import Path
r=json.loads(Path(sys.argv[1]).read_text());M=r['M'];Q=[[F(v,M) for v in row] for row in r['free_integer_coordinates']];P=r['anchor_numerator'];W=r['anchor_denominator'];ax=r['dependent_coordinate']
for i in r['contact_rows']:Q[i][ax]=(W-sum(P[j]*Q[i][j] for j in range(3) if j!=ax))/P[ax]
D=math.lcm(*(x.denominator for row in Q for x in row));assert D==r['expected_D'];I=[[int(x*D) for x in row] for row in Q];b=json.dumps(dict(D=D,I=I,scale=1),sort_keys=True,separators=(',',':')).encode();assert hashlib.sha256(b).hexdigest()==r['expected_RAW_sha256'];Path(sys.argv[2]).write_bytes(b)
