import ast,base64,hashlib,json,lzma,re
from pathlib import Path,PurePosixPath
from datetime import datetime,timezone
root=Path(__file__).resolve().parent
def sha(b):return hashlib.sha256(b).hexdigest()
raw=(root/'result.json').read_bytes()
if len(raw)!=66742 or sha(raw)!='85e93472381d4e9a3a387f0ac15db225cdafb73714d5756015418e1d4f8a8899':raise ValueError('Immutable result pin differs')
md=json.loads(raw)['result_markdown']
if (root/'result.md').read_bytes()!=md.encode()or len(md.encode())!=66491 or sha(md.encode())!='43832e896a41eb4fab3f92f57a89e2ee9bdc4b26de2ba21713c9e9994d8cc62a':raise ValueError('Markdown pin differs')
def extract(text):
 blocks=re.findall(r'^\x60\x60\x60python\n(.*?)^\x60\x60\x60',text,re.M|re.S)
 if len(blocks)!=1:raise ValueError('Ambiguous literal recovery program')
 tree=ast.parse(blocks[0])
 definitions=[n for n in tree.body if isinstance(n,ast.Assign)and any(isinstance(t,ast.Name)and t.id=='CAPSULE'for t in n.targets)]
 if len(definitions)!=1:raise ValueError('Ambiguous CAPSULE literal')
 value=ast.literal_eval(definitions[0].value)
 if not isinstance(value,str):raise ValueError('Nonliteral source encoding')
 cap=value.encode()
 if len(cap)!=47415 or sha(cap)!='012c8f94ad4856bf5f78869631b2f68260b0f3fa30f3701441e11c338f58e260':raise ValueError('Encoded capsule pin differs')
 return cap,blocks[0].encode()
cap,decoder=extract(md)
backend=json.loads(Path('/REDACTED_HOME/pro-research/output/reconnect-20260915-1337-ZxwYPN/finch-result.json').read_text())['result_markdown']
if extract(backend)[0]!=cap:raise ValueError('Backend/native scientific capsule differs')
dec=lzma.LZMADecompressor(memlimit=134217728);decoded=dec.decompress(base64.b85decode(cap),max_length=153198)
if not dec.eof or dec.unused_data or len(decoded)!=153197 or sha(decoded)!='329a8dba873495371cfeec2dcaf576381eac153b1b3b2d7021dcecab8d69dbaf':raise ValueError('Decoded source-map pin differs')
files=json.loads(decoded)
if not isinstance(files,dict)or len(files)!=24:raise ValueError('Wrong source count')
for name,text in files.items():
 p=PurePosixPath(name)
 if not isinstance(text,str)or not p.parts or p.is_absolute()or '..'in p.parts or chr(92)in name or str(p)!=name:raise ValueError('Unsafe path')
 if name.endswith('.py'):ast.parse(text,filename=name)
 elif name.endswith('.json'):json.loads(text)
cases=json.loads(files['NEW_CASES.json'])
if len(cases)!=21 or not {'D16_ONE_GRID7','MARGIN2_GRID6','FINCH_SEQUENTIAL'}<=set(cases):raise ValueError('Wrong declared case registry')
outputs={'source/'+name:text.encode()for name,text in files.items()}
outputs.update({'SOURCE_CAPSULE.b85':cap,'restore_original.py':decoder})
for name in [*outputs,'integrity-receipt.json']:
 if(root/name).exists():raise FileExistsError(root/name)
for name,b in outputs.items():
 p=root/name;p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('xb')as f:f.write(b)
 if p.read_bytes()!=b:raise ValueError('Archive readback differs')
receipt={'at':datetime.now(timezone.utc).isoformat(),'identity':'FINCH2_D16_ONE_GRID7_AND_MARGIN2_GRID6','assignmentId':'asg_H3ra-BoBapByCvkuPQyS6dpc','resultSha256':sha(raw),'sourceFiles':24,'registeredCases':21,'standalone':True,'completeSourcePreservedLocally':True,'capsuleBytes':len(cap),'capsuleSha256':sha(cap),'decodedBytes':len(decoded),'decodedSha256':sha(decoded),'backendAndNativeCapsuleEqual':True,'authorPerFileManifestPresent':False,'verification':'Immutable result and Markdown pins, literal AST extraction without execution, encoded/full-source-map pins, all JSON/Python syntax,21-case registry and exact written-file readbacks verified. Local per-file hashes recorded; no nonexistent author per-file manifest claimed.','localMathematicalOrNumericalReplay':False,'scope':'Author exact C612 own121weak000 D16_ONE_GRID7 and C616 own121weak000 MARGIN2_GRID6, further finite nonwinners and scoped four-witness centre-only obstruction. Not an own110 improvement. Worker mentions stale C628 benchmark; canonical current positive record is C624.','files':{n:{'bytes':len(b),'sha256':sha(b)}for n,b in outputs.items()}}
with(root/'integrity-receipt.json').open('x')as f:json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in receipt.items()if k!='files'}))
