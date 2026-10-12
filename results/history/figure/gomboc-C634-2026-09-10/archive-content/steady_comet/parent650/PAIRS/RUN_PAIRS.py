import json,sys,subprocess,hashlib
from pathlib import Path
from RECONSTRUCT import recover
from EXTRA_PAIRS import summarize
sys.set_int_max_str_digits(0)
raw=recover(json.loads(Path("GENERATOR_652.json").read_text()))
for drop in [102,120]:
 out={"H":[row for i,row in enumerate(raw["H"]) if i!=drop]}
 Path(f"RAW_{drop}.json").write_text(json.dumps(out,sort_keys=True,separators=(",",":")))
 for auditor in ["A","B"]:
  subprocess.run([sys.executable,"check_"+auditor+".py",f"RAW_{drop}.json",f"{auditor}_{drop}.json"],check=True)
 aa=Path(f"A_{drop}.json").read_bytes();bb=Path(f"B_{drop}.json").read_bytes();assert aa==bb
 res=json.loads(aa);assert (res["V"],res["E"],res["F"],res["counts"],res["weak"])==(189,323,136,[1,2,1],[0,0,0])
 summarize(drop)
 print("STAR_PAIR_EXACT",drop,len(aa),hashlib.sha256(aa).hexdigest(),res["unstable_vertices"],res["saddle_edges"],flush=True)
print("TWO_STAR_PAIR_NONWINNERS_TWO_FULL_EXACT_AUDITS_PASS",flush=True)

expected=json.loads(Path("EXPECTED_PAIRS.json").read_text())
for name,(size,sha) in expected.items():
 b=Path(name).read_bytes();assert len(b)==size and hashlib.sha256(b).hexdigest()==sha,name
print("TWO_STAR_PAIR_SOURCE_ONLY_FROZEN_OUTPUTS_REPLAY_PASS",flush=True)
