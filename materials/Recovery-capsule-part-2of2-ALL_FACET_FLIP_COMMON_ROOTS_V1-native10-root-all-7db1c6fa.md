# material-7db1c6faf40f

AI research material · [Export notes](../catalog/coverage.md#text-records)

---


[Encoded source block omitted; the code in this passage is incomplete.]

for name,p in SOURCE_PINS.items():assert pin((HERE/name).read_bytes())==p
raw=lzma.decompress(base64.b64decode(''.join(DATA.split()),validate=True));assert pin(raw)==RAW_PIN
assert len(raw)%2==0
RECORD['coefficients']=list(struct.unpack('<'+'h'*(len(raw)//2),raw))
b=(json.dumps(RECORD,sort_keys=True,separators=(',',':'))+'\n').encode();assert pin(b)==RECORD_PIN
p=HERE/'common_certificate_10_root.json'
if p.exists():assert p.read_bytes()==b
p.write_bytes(b)
subprocess.run([sys.executable,'-S',str(HERE/'common_roots.py'),'check',str(p)],check=True)
assert pin(p.with_suffix('.verified.json').read_bytes())==REPORT_PIN
print('COMMON_ROOT_FROZEN_RECOVERY_PASS',10,'root',*RECORD_PIN)
