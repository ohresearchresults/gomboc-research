# material-056b8683ac44

AI research material · [Export notes](../catalog/coverage.md#text-records)

---


[Encoded source block omitted; the code in this passage is incomplete.]

"""
for name,expected in SOURCE_PINS.items():assert pin((HERE/name).read_bytes())==expected,name
raw=lzma.decompress(base64.b64decode(DATA));assert pin(raw)==RAW_PIN
assert len(raw)%2==0
RECORD['coefficients']=list(struct.unpack('<'+'h'*(len(raw)//2),raw))
b=(json.dumps(RECORD,sort_keys=True,separators=(',',':'))+'\n').encode();assert pin(b)==RECORD_PIN
p=HERE/'common_certificate_13_root.json';p.write_bytes(b)
subprocess.run([sys.executable,'-S',str(HERE/'common_roots.py'),'check',str(p)],check=True,cwd=HERE)
assert pin(p.with_suffix('.verified.json').read_bytes())==REPORT_PIN
print('COMMON_ROOT_FROZEN_RECOVERY_PASS',13,'root',*pin(b),*REPORT_PIN)
