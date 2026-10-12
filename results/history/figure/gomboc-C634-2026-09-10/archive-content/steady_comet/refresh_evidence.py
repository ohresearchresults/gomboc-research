from pathlib import Path
import json,hashlib,sys
sys.set_int_max_str_digits(0);R=Path(__file__).parent
rows=[]
for d in sorted(R.iterdir()):
 if not d.is_dir() or d.name.endswith('_COLD') or not (d/'GENERATOR.json').exists() or not (d/'A.json').exists():continue
 if not (d/'B.json').exists():continue
 a=json.loads((d/'A.json').read_text());assert (d/'A.json').read_bytes()==(d/'B.json').read_bytes(),d
 row=dict(tag=d.name,V=a['V'],E=a['E'],F=a['F'],counts=a['counts'],weak=a['weak'],sources={},outputs={},cold={})
 for name in ['GENERATOR.json','META.json','RECONSTRUCT.py','check_A.py','check_B.py','EXTRA.py','REPLAY.py','FROZEN_OUTPUTS.json']:
  p=d/name
  if p.exists():b=p.read_bytes();row['sources'][name]=[len(b),hashlib.sha256(b).hexdigest()]
 for name in ['RAW.json','A.json','B.json','EXTRA.json','DESCRIPTION.json','SUMMARY.json','PAIR.json']:
  p=d/name
  if p.exists():b=p.read_bytes();row['outputs'][name]=[len(b),hashlib.sha256(b).hexdigest()]
 for key,name in [('description','DESCRIPTION.json'),('summary','SUMMARY.json')]:
  if (d/name).exists():row[key]=json.loads((d/name).read_text())
 cold=R/(d.name+'_COLD')
 if d.name=='C648_REPAIR44':cold=R/'C648_COLD'
 if cold.exists():
  cmp={name:(cold/name).exists() and (cold/name).read_bytes()==(d/name).read_bytes() for name in row['outputs']};row['cold']=dict(directory=cold.name,all_outputs_identical=all(cmp.values()),comparisons=cmp,marker_lines=[l for p in cold.glob('*.log') for l in p.read_text().splitlines() if 'PASS' in l])
  if all(cmp.values()):
   receipt=dict(tag=d.name,source_inputs=row['sources'],checked_outputs=row['outputs'],all_outputs_identical=True,marker_lines=row['cold']['marker_lines']);(cold/'COLD_RECEIPT.json').write_text(json.dumps(receipt,sort_keys=True,separators=(',',':')))
 rows.append(row)
(R/'EVIDENCE_INDEX.json').write_text(json.dumps(rows,indent=2));print('REFRESHED',len(rows));
for r in rows:print(r['tag'],[r[k] for k in ['V','E','F']],r['counts'],r['weak'],r['cold'].get('all_outputs_identical',False))
