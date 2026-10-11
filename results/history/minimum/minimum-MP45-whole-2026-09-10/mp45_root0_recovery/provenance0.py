"""Optional exact authentication of immutable E8 and its inherited source units.
Input: research-journal(7).md, 3486698 bytes, SHA256 below.
This journal is not an input to the numerical reconstruction or exact root0 proof.
"""
from pathlib import Path
import sys,json,hashlib,zlib,base64

def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
raw=Path(sys.argv[1]).read_bytes()
assert pin(raw)==[3486698,'3fb11318fc0cab6a8742f00ff0af47b04490fef13d97ae4df84feb9a5fdad48d']
s=raw.decode('utf-8');a=s.index('## Parent asg_E8jhRERA9v_K8-YHafCvHQXS')
a=s.index('# NOVA54_MP45_ROOT3_WHOLE_DOMAIN_V3',a);body=s[a:].rstrip()+'\n'
enc=json.dumps(dict(version=2,result_markdown=body),ensure_ascii=False,separators=(',',':')).encode('utf-8')
assert pin(enc)==[68993,'a8dc9aab660b5e9b5a6b4db109797d548b9562b9dac14a8ca2fa04f55e999eee']
a=body.index(chr(34)*3+'NOVA54_MP45_ROOT3_WHOLE_DOMAIN_V3: complete source-only recovery.')
e=body.index('\n```',a);source=(body[a:e]+'\n').encode('utf-8')
assert pin(source)==[41454,'a9e3efea31bb10acbaa769ed2aa9603ba51417b6e4a6700af28da8df1052dc7b']
text=source.decode('utf-8');b=''.join(text.split("B=r'''",1)[1].split("'''",1)[0].split()).encode('ascii')
assert pin(b)==[38698,'4e58d9936af4d3e1afff389806b2fdec3f482dbdbd7ec8353c440a6a71989a63']
payload=zlib.decompress(base64.b85decode(b))
assert pin(payload)==[101132,'18ee40d76bb29a630350dc639999008553fefe1ecad361b01293d6606340b5e6']
S=json.loads(payload)
names=['nova54_recovery/comb.py','nova54_recovery/locator.py','nova54_recovery/exact_check.py',
 'quad_recovery/engine.py','quad_recovery/build_universal.py','quad_recovery/verify_universal.py','omission.py']
for name in names:assert Path(name).read_bytes()==S[name].encode('utf-8'),('INHERITED_SOURCE_CHANGED',name)
print('IMMUTABLE_E8_PARENT_68993_BYTES_AND_41454_BYTE_RECOVERY_AUTHENTICATED_PASS')
print('SEVEN_INHERITED_SOURCE_UNITS_IDENTICAL_TO_E8_PASS')
print('NO_ROOT3_REPLAY_AND_NO_HISTORICAL_MULTIGRAPH_PLAN_INPUT')
