from pathlib import Path
import json,lzma,base64,hashlib
R=Path(__file__).parent;full=json.loads((R/'SOURCE_CAPSULE.json').read_text());names=['C634_SOC','C636_H213_SOC','C642_GRID6_UNREPAIRED_OWN121','C642_GRID6_REPAIR169','C636_GRID7','C638_H213_GRID7'];z={}
for k,v in full.items():
 if k.startswith('audit/') or any(k.startswith(n+'/') for n in names):z[k]=v
for f in ['symbolic_pair.py','pair_wall_certificate.py','pair_interval_certificate.py','mass_moments.py','numeric.py','atlas_opt.py','contact_chart.py','condition_events.py','adaptive_homotopy.py','soc_contact.py','close_soc_endpoint.py','restore_h213_thin.py','fit_restoration.py','C650_rotation.json','C650_polar_edges.txt','H213_edges.txt','H213_rotation.txt','H213_faces.json','BUILD_TUTTE_XY.py','REALIZE_AUDIT_H213.py','VERIFY_MIN213.py','C634_SOC_faces.json','C636_H213_RESTORED_FROM_C634_SOC_EPS1E8_faces.json','soc_records/E318_TARGET60_66_RELAXED.json','soc_records/E318_TARGET60_66_RELAXED_faces.json','soc_records/E318_TARGET60_66_FINAL.json','soc_records/E318_TARGET60_66_FINAL_faces.json']:
 z[f]=full[f]
z['rotation_certificate.py']=(R/'rotation_certificate.py').read_text()
z['CORE_REPLAY_ALL.py']=(R/'CORE_REPLAY_ALL.py').read_text();e=json.loads(full['EXPECTATIONS.json']);e['bodies']={n:e['bodies'][n] for n in names};e.pop('C650');
for n in ['C636_GRID7','C638_H213_GRID7']:
 b=(R/n/'MASS_MOMENTS.json').read_bytes();e['moments'][n]=[len(b),hashlib.sha256(b).hexdigest()]
e['rotations']={}
for n in names:
 b=(R/n/'ROTATION_CERTIFICATE.json').read_bytes();e['rotations'][n]=[len(b),hashlib.sha256(b).hexdigest()]
z['EXPECTATIONS.json']=json.dumps(e,sort_keys=True,separators=(',',':'))
z['MANIFEST.json']=json.dumps({k:[len(v.encode()),hashlib.sha256(v.encode()).hexdigest()] for k,v in sorted(z.items())},sort_keys=True,separators=(',',':'))
raw=json.dumps(z,sort_keys=True,separators=(',',':')).encode();xz=lzma.compress(raw,preset=9);b=base64.b85encode(xz).decode();meta=dict(files=len(z),utf8_bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),lzma_bytes=len(xz),base85_chars=len(b),bodies=names)
(R/'CORE_CAPSULE.json').write_bytes(raw);(R/'CORE_CAPSULE.xz').write_bytes(xz);(R/'CORE_CAPSULE.b85').write_text('\n'.join(b[i:i+100] for i in range(0,len(b),100))+'\n');(R/'CORE_META.json').write_text(json.dumps(meta,indent=2));print(meta)
cold=R/'FINAL_CORE_SOURCE_ONLY';assert not cold.exists();cold.mkdir()
for k,v in json.loads(lzma.decompress(base64.b85decode(b))).items():
 p=Path(k);assert not p.is_absolute() and '..' not in p.parts;q=cold/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_text(v)
assert not any(cold.rglob('A.json')) and not (cold/'SYMBOLIC_PAIR.pkl').exists()
print('FRESH_CORE_SOURCE_ONLY',cold)
