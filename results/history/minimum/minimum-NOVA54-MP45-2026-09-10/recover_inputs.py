from pathlib import Path
import hashlib,json,re,subprocess,sys

def pin(b):
    return len(b),hashlib.sha256(b).hexdigest()

raw=Path(sys.argv[1]).read_bytes()
assert pin(raw)==(3204366,'60e55fd7ae0576c644d1cfc87d6c2fb825fe4c41d336382b24611bfa8d116d26')
s=raw.decode('utf-8')
a=s.index('# Immutable parent result payloads')
a=s.index('# NOVA24_C32_TYPE139_WHOLE_ACTUAL_U_GE_2_V1',a)
parent=s[a:].rstrip()+'\n'
b=json.dumps({'version':2,'result_markdown':parent},ensure_ascii=False,separators=(',',':')).encode('utf-8')
assert pin(b)==(39914,'3b737649ca4e531383c349e6a3e088fdf458b5b826662c391f655f628f843a94')
a=s.index(chr(39)*3+'NOVA54_MP9_ACTUAL_MOMENTS_V1 complete self-contained recovery.')
e=s.index('\n```',a)
code=s[a:e]+'\n'
pat=(r'\n\n## 2026-09-09T02:54:11\.640Z\n\n'
     r'### Late recovery slot-1 [^\n]*\n\nSource: [^\n]*\n\n')
code,n=re.subn(pat,'',code)
assert n==1
b=code.encode('utf-8')
assert pin(b)==(33040,'627b00c5e6f5c6e697fe537d407e3fddc294c4dbefdfe65857ad65680f9fc219')
Path('recover_nova54.py').write_bytes(b)
subprocess.run([sys.executable,'-S','recover_nova54.py','extract'],check=True)
expected={
 'comb.py':(9699,'f614a76308d54aad24ed1ec06fb6658506aaf96f3907b2b770861e439595d82b'),
 'locator.py':(12050,'295c928614be33ecbac935ac7d9ee44ea2aa0c8901eaeff762ec455816d2602d'),
 'reconstruct.py':(2490,'567944e388b4ad65b858bbb0f2728fbbe4a269b84f574f583d2b6ac738ad16f6'),
 'exact_check.py':(13163,'0a60f2ac77565b7c78be08cfda038cb472c4fdd0fce3bbf06a8e5ed48160348b'),
 'plan.json':(22604,'121ee1d69b7f24b2933327196aa967f7deaeeae4f9c3adabef644f565d055418')}
for name,value in expected.items():
    assert pin((Path('nova54_recovery')/name).read_bytes())==value

a=s.index(chr(34)*3+'NOVA24_C32_QUAD_TEN_WHOLE_TYPES_V1: complete source-only recovery.')
e=s.index('\n```',a)
part1=s[a:e]+'\n'
a=s.index('```text\n',e)+8
e=s.index('\n```',a)
q=part1+s[a:e]+'\n'
assert pin(q.encode())==(24286,'71d9d61527f5e9c44d2c6ec5174e925ef8d98444c257c23766dfa2ce7e209f87')
wrong='efb10a4657a891cd13f6f62db94164bd4b3005e908dc55aae87db450f704d'
right='efb10a4657a891cd13f6f62db94164bd4b3005e908dc55aae87db450930f704d'
assert q.count(wrong)==1
q=q.replace(wrong,right)
assert pin(q.encode())==(24289,'fc6fb7a3b0fd6e44fa4e69145e38453d131136e34cbe1cd9033e27791954f5f2')
d=Path('quad_recovery');d.mkdir(exist_ok=True)
(d/'recover_quad10.py').write_bytes(q.encode())
subprocess.run([sys.executable,'-S','recover_quad10.py','extract'],cwd=d,check=True)
print('NOVA54_PARENT139_AND_MP9_SOURCE_RECOVERY_PASS')
print('QUAD_WRAPPER_THREE_CHARACTER_REPAIR_AUTHENTICATED_OUTPUT_LENGTH_AUDIT_STILL_REQUIRED')
