from pathlib import Path
import json,hashlib,lzma,base64,re,shutil
R=Path(__file__).parent
names=sorted(p.name for p in R.iterdir() if p.is_dir() and not p.name.endswith('_COLD') and (p/'GENERATOR.json').exists() and (p/'A.json').exists() and (p/'B.json').exists())
files={};exp={'bodies':{},'C650':{},'symbolic':{},'moments':{}}
def add(dst,src=None):files[dst]=(R/(src or dst)).read_text()
def dig(p):b=p.read_bytes();return [len(b),hashlib.sha256(b).hexdigest()]
for f in ['RECONSTRUCT.py','check_A.py','check_B.py','EXTRA.py']:add('audit/'+f,'parent650/C650/'+f)
add('audit/REPLAY.py','CERTIFY_TEMPLATE.py')
for name in names:
 d=R/name;assert (d/'A.json').read_bytes()==(d/'B.json').read_bytes()
 for f in ['GENERATOR.json','META.json','FROZEN_OUTPUTS.json']:
  if (d/f).exists():add(name+'/'+f)
 if (d/'REPLAY.py').read_text()!=files['audit/REPLAY.py']:add(name+'/REPLAY.py')
 outs=[f for f in ['RAW.json','A.json','B.json','EXTRA.json','DESCRIPTION.json','SUMMARY.json','PAIR.json'] if (d/f).exists()]
 exp['bodies'][name]={f:dig(d/f) for f in outs}
for f in ['GENERATOR.json','EXPECTED.json','RECONSTRUCT.py','check_A.py','check_B.py','EXTRA.py','ARCHITECTURE.py','REPLAY.py']:add('parent650/C650/'+f)
for f in ['RAW.json','A.json','B.json','EXTRA.json','CONTROLS.json','SUMMARY.json','ARCHITECTURE.json']:exp['C650'][f]=dig(R/'parent650/C650'/f)
for f in ['SYMBOLIC_PAIR_WALL.json','PAIR_WALL_CERTIFICATE.json','PAIR_INTERVAL_CERTIFICATE.json']:exp['symbolic'][f]=dig(R/f)
for n in ['C634_SOC','C636_H213_SOC','C642_GRID6_UNREPAIRED_OWN121','C642_GRID6_REPAIR169']:
 if (R/n/'MASS_MOMENTS.json').exists():exp['moments'][n]=dig(R/n/'MASS_MOMENTS.json')
source=['RUN_REPLAYS.py','BUILD_TUTTE_XY.py','VERIFY_MIN213.py','REALIZE_AUDIT_H213.py','REALIZE_SAVE_H213.py','setup_graph.py','numeric.py','atlas_opt.py','contact_chart.py','condition_events.py','adaptive_homotopy.py','soc_contact.py','close_soc_endpoint.py','next_soc.py','restore_h213_edge.py','restore_h213_thin.py','fit_restoration.py','refine_h249.py','tutte_physical.py','tutte_opt.py','tree_repair.py','sqp_repair.py','projected_spring.py','tutte_coarsen.py','greedy_coarsen.py','unrestricted_events.py','screen_snaps.py','close_c644.py','grid_repair.py','quantize_best.py','homotopy_records.py','physical_targets.py','close_near_nonwinner.py','multi_contact.py','forest_subsets.py','forest_greedy.py','symbolic_pair.py','pair_wall_certificate.py','pair_interval_certificate.py','mass_moments.py','start_certificate.py','cold_replay.py','CERTIFY_TEMPLATE.py','NONWINNER_REPLAY.py','refresh_evidence.py']
for f in source:add(f)
for f in ['C650_polar_edges.txt','C650_rotation.json','H213_edges.txt','H213_rotation.txt','H213_faces.json','H249_RESTORATION.json','H213_PRIMAL_CHART_GENERATOR.json','H213_primal_faces.json','TUTTE_C650_REFERENCE.json','immutable_parent.md','C634_SOC_faces.json','C636_H213_RESTORED_FROM_C634_SOC_EPS1E8_faces.json']:
 if (R/f).exists():add(f)
# Complete finite inputs for the strongest successful SOC continuation, not just a path/hash.
for f in ['soc_records/E318_TARGET60_66_RELAXED.json','soc_records/E318_TARGET60_66_RELAXED_faces.json','soc_records/E318_TARGET60_66_FINAL.json','soc_records/E318_TARGET60_66_FINAL_faces.json']:
 if (R/f).exists():add(f)
files['EXPECTATIONS.json']=json.dumps(exp,sort_keys=True,separators=(',',':'))
files['MANIFEST.json']=json.dumps({k:[len(v.encode()),hashlib.sha256(v.encode()).hexdigest()] for k,v in sorted(files.items())},sort_keys=True,separators=(',',':'))
raw=json.dumps(files,sort_keys=True,separators=(',',':')).encode();compressed=lzma.compress(raw,preset=9);b85=base64.b85encode(compressed).decode();meta=dict(files=len(files),utf8_bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),lzma_bytes=len(compressed),base85_chars=len(b85),bodies=names)
(R/'SOURCE_CAPSULE.json').write_bytes(raw);(R/'SOURCE_CAPSULE.xz').write_bytes(compressed);(R/'SOURCE_CAPSULE.b85').write_text('\n'.join(b85[i:i+100] for i in range(0,len(b85),100))+'\n');(R/'CAPSULE_META.json').write_text(json.dumps(meta,indent=2));print(meta)
# A fresh directory is intentional: no cached audit, output, coordinate or pickle inputs.
cold=R/'CAPSULE_SOURCE_ONLY'
if cold.exists():raise SystemExit('Fresh root already exists; leave it unchanged and explicitly choose another root.')
cold.mkdir()
for k,v in json.loads(lzma.decompress(base64.b85decode(b85))).items():
 p=Path(k);assert not p.is_absolute() and '..' not in p.parts;q=cold/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_text(v)
assert not any(cold.rglob('A.json')) and not any(cold.rglob('SYMBOLIC_PAIR.pkl'))
print('FRESH_SOURCE_PACKET',cold)
