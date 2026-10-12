"""Optional attachment audit; not an input dependency of the root3 theorem.
python -S provenance.py CURRENT_JOURNAL PRIOR_JOURNAL
"""
from pathlib import Path
import ast,hashlib,json,re,subprocess,sys

def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
base=Path(__file__).resolve().parent
current=Path(sys.argv[1]).resolve();prior=Path(sys.argv[2]).resolve()
assert pin(current.read_bytes())==[3235486,'1078a1c318b1d9a06cd0dd06b93e78ab7a0c305c03f6522a8044d0861918db3d']
assert pin(prior.read_bytes())==[3204366,'60e55fd7ae0576c644d1cfc87d6c2fb825fe4c41d336382b24611bfa8d116d26']
s=current.read_text();a=s.index('# Immutable parent result payloads')
a=s.index('# NOVA54_MP45_FULL_TENSOR_RIGIDITY_AND_NORM_FRONTIER_V2',a)
p=s[a:];b=json.dumps({'version':2,'result_markdown':p},ensure_ascii=False,separators=(',',':')).encode()
assert pin(b)==[39588,'0a98364ee55c3f09547ba8066a783f79a5e89ad9e2571bb1311a08f257d09875']
print('IMMUTABLE_PARENT_AUTHENTICATED',*pin(b),flush=True)
blocks=re.findall(r'```python\n(.*?)\n```',p,re.S);assert len(blocks)==4
out=base/'provenance_recovery';out.mkdir(exist_ok=True)
for name,code in zip(('recover_inputs.py','mp45_norm80_parent.py','mp45_mass_gate.py','targeted_plans_parent.py'),blocks):
 (out/name).write_text(code+'\n')
with (out/'extraction.log').open('w')as log:
 subprocess.run([sys.executable,'-S','recover_inputs.py',str(prior)],cwd=out,stdout=log,stderr=subprocess.STDOUT,check=True)
for name,length,digest in [
 ('comb.py',9699,'f614a76308d54aad24ed1ec06fb6658506aaf96f3907b2b770861e439595d82b'),
 ('locator.py',12050,'295c928614be33ecbac935ac7d9ee44ea2aa0c8901eaeff762ec455816d2602d'),
 ('exact_check.py',13163,'0a60f2ac77565b7c78be08cfda038cb472c4fdd0fce3bbf06a8e5ed48160348b')]:
 b=(out/'nova54_recovery'/name).read_bytes();assert pin(b)==[length,digest]
 assert b==(base/'nova54_recovery'/name).read_bytes()
 print('AUTHENTICATED_METHOD_SOURCE',name,*pin(b),flush=True)
for name,missing in [('comb.py','root_code'),('exact_check.py','volume_relations'),('reconstruct.py','iterjobs')]:
 tree=ast.parse((out/'nova54_recovery'/name).read_text())
 assert missing not in {n.name for n in ast.walk(tree)if isinstance(n,(ast.FunctionDef,ast.ClassDef))}
 print('PARENT_REFERENCES_MISSING_INTERFACE',name,missing,flush=True)
(out/'prepare.py').write_bytes((base/'prepare.py').read_bytes())
with (out/'prepare.log').open('w')as log:
 subprocess.run([sys.executable,'-S','prepare.py'],cwd=out,stdout=log,stderr=subprocess.STDOUT,check=True)
assert (out/'input.json').read_bytes()==(base/'input.json').read_bytes()
print('TARGETED_55_LITERAL_PLAN_INPUT_REPRODUCED',*pin((out/'input.json').read_bytes()),flush=True)
for name,length,digest in [
 ('universal285.json',1289123,'3a00b679c994255debd3acbe5d3230e336d1e292b9cf88507dc1d2c61fc94496'),
 ('universal285_verification.json',41790,'067c8ae69857aece263ccaeb5b1e05e4d401d90f13f5d8ee8d64e3847358acec')]:
 b=(base/'quad_recovery'/name).read_bytes();assert pin(b)==[length,digest]
 print('CORRECT_UNIVERSAL_OUTPUT_PIN',name,*pin(b),flush=True)
print('PARENT_LENGTHS_1330807_AND_41787_CORRECTED_TO_1289123_AND_41790',flush=True)
print('NOVA54_OPTIONAL_JOURNAL_PROVENANCE_AUDIT_PASS',flush=True)
