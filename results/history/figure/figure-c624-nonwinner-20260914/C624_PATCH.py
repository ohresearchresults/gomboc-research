"""Exact C624/121 extension of the complete persisted C626 exact capsule.
Usage: python -B -S C624_PATCH.py C626_EXACT_SOURCE fresh-output A|B|MASS|FINISH
A requires a new output directory; other stages continue that same directory.
"""
import hashlib,json,subprocess,sys
from pathlib import Path
assert __debug__
sys.set_int_max_str_digits(0)
source,out=map(lambda x:Path(x).resolve(),sys.argv[1:3]);stage=sys.argv[3]
assert stage in ('A','B','MASS','FINISH')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,sort_keys=True,separators=(',',':')),encoding='utf-8')
def run(name,*args):subprocess.run([sys.executable,'-B','-S',str(source/name),*map(str,args)],check=True)
manifest=json.loads((source/'MANIFEST.json').read_text())
for name,record in manifest.items():
 p=source/name;assert p.stat().st_size==record['bytes'] and digest(p)==record['sha256']
if stage=='A':
 out.mkdir(parents=True,exist_ok=False)
 p=source/'G14/GENERATOR.json';assert digest(p)=='2a478cf7e3b6caafd094a14504f4a2004e3e67ba948d6052575dd1ce0da3ccb3'
 d=json.loads(p.read_text());assert len(d['controls'])==180
 d['controls'][120]=[109895360315786,133285035064734,-7988556289011]
 d['controls'].append([52795281954120,30769038499280,-12141254049517])
 d['plan'].remove([120,[],[]]);d['plan'] += [[180,[101,102,121],[0,1,2]],[120,[180],[0]]]
 d['groups'].append([101,102,120,121]);dump(out/'GENERATOR.json',d)
 run('RECONSTRUCT.py',out/'GENERATOR.json',out/'raw.json')
 run('check_A.py',out/'raw.json',out/'A.json')
elif stage=='B':run('check_B.py',out/'raw.json',out/'B.json')
elif stage=='MASS':
 sys.path.insert(0,str(source));import centred_mass
 dump(out/'CENTRED_MASS.json',centred_mass.run(json.loads((out/'A.json').read_text())))
else:
 expected={'GENERATOR.json':(12993,'9794a36115719432a426f28f25ec8a16f28224237acc2b94b2acb4625dcfbede'),'raw.json':(21418,'0c4c48f26393826d341e55ac9ae0da5610b084345ffabada6deb6255de9409e5'),'A.json':(450492,'7719a4e491bda5d20c3480dbf4cb8475a75baa735d55122717fc8f029f005722'),'B.json':(450492,'7719a4e491bda5d20c3480dbf4cb8475a75baa735d55122717fc8f029f005722')}
 for name,(size,sha) in expected.items():assert (out/name).stat().st_size==size and digest(out/name)==sha
 a=json.loads((out/'A.json').read_text());assert (a['V'],a['E'],a['F'],a['counts'],a['weak'])==(177,312,137,[1,2,1],[0,0,0])
 assert a['stable_face_ids']==[3] and a['unstable_vertices']==[96,163] and a['saddle_edges']==[[163,166]]
 assert json.loads((out/'CENTRED_MASS.json').read_text())['filled_first_moments']==[0,0,0]
 print('C624_EXACT_NONWINNER_121_TWO_AUDITS_AND_CENTRED_MASS_COLD_PASS')
