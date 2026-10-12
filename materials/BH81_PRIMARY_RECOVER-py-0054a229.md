# material-0054a22972a0

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# BH81 primary capsule extraction and exact transport correction

Dependency: complete `BH81_FINITE_PRIMARY.md`, immutable material `[internal-source-reference]`,18447bytes,SHA256c97bda903918b05112ff8d03e8b030d02df4620b7c7c75ed7703ac0b097f37fa. Together these TWO materials form a complete self-contained five-body primary recovery capsule. The first material has a one-character transcription error in rational_points: the inner tuple closes with `]` instead of `)`. This exact patch restores the independently cold-executed8408byte core; it does not change any mathematical input or endpoint. Always attach BOTH materials to a fresh worker using these bodies.

Save the following complete source as RECOVER_PRIMARY.py next to BH81_FINITE_PRIMARY.md and run `python RECOVER_PRIMARY.py`. It extracts all three literal blocks, fixes exactly one known character, checks each complete source byte count and SHA256, runs full exact reconstruction, and checks all five complete output bytes and hashes. Python3.13.5, standard library only. Expected terminal `BH81_PRIMARY_DURABLE_COLD_PASS`. This launcher is an explicit exact recovery patch; endpoint hashes refer to the already observed cold replay recorded in the first material.

```python
from pathlib import Path
import hashlib,json,re,subprocess,sys
sys.set_int_max_str_digits(0)
p=Path('BH81_FINITE_PRIMARY.md')
b=p.read_bytes()
assert len(b)==18447
assert hashlib.sha256(b).hexdigest()=='c97bda903918b05112ff8d03e8b030d02df4620b7c7c75ed7703ac0b097f37fa'
s=b.decode('utf-8')
expected={
 'BH81_CORE.py':(8408,'12132578b6ae9379baab76276b077b0a9548332bd8202b8a9c432b63519b58f1'),
 'CUT_INPUTS.json':(5275,'3d24c6af88b91e0eed55087e1c94231c2aa6938d4643a43b58725aa5164fba1a'),
 'exact_new.py':(1973,'28effc70b91a2fdf4713522b9c04c30e2ff194a57aedd0b26bdc0520c16234cc')}
for name,(size,sha) in expected.items():
 m=re.search(r'## '+re.escape(name)+r'\n```(?:python|json)\n(.*?)\n```',s,re.S)
 assert m,name
 text=m.group(1)
 if name=='BH81_CORE.py':
  old="return [tuple(F(x,raw['grid']) for x in row] for row in raw['points']]"
  new="return [tuple(F(x,raw['grid']) for x in row) for row in raw['points']]"
  assert text.count(old)==1
  text=text.replace(old,new)
 if name.endswith('.py'):text+='\n'
 data=text.encode('utf-8')
 assert len(data)==size,(name,len(data),size)
 assert hashlib.sha256(data).hexdigest()==sha,name
 Path(name).write_bytes(data)
subprocess.run([sys.executable,'exact_new.py'],check=True)
outputs={
 'CUT121_EXACT.json':(31411,'c745dee9dc5732fcb4ab8c2eed9380921683d07c99cc52b5850db03b54e0d68d'),
 'LOW121_EXACT.json':(29855,'d77653ab141e4978e434ae7ba1c58041a8e8277a80537eb99720754b796a2396'),
 'MASS132_EXACT.json':(31960,'caca567bee0c7ab81bbcc5e5a3727e7d65e3ba7f77335a76fe746e0c4d55ba91'),
 'MICRO_EXACT.json':(39163,'70efa26463d1b1bcd54a456bec977705c5a43e68d3781651bb24d55485d8ec17'),
 'RADIAL_EXACT.json':(27878,'cecb4fa2f222a44b3bfd3341d7cf4f03bc508aa810642b4f66790f8a5c42d357')}
for name,(size,sha) in outputs.items():
 data=Path(name).read_bytes()
 assert len(data)==size,name
 assert hashlib.sha256(data).hexdigest()==sha,name
print('BH81_PRIMARY_DURABLE_COLD_PASS')
```
