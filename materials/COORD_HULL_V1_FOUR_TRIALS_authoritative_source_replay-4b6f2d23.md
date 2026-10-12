# material-4b6f2d23e6a2

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# COORD_HULL_V1_FOUR_TRIALS: authoritative source-based recovery

This complete recovery supersedes the attempted split encoded FROZEN capsule. The earlier part2 [internal-source-reference] is transcription-corrupted and part3 [internal-source-reference] is truncated; exclude both. Even the correct individual spans in [internal-source-reference] and [internal-source-reference] are NOT a complete accepted recovery capsule. Do not claim the copied encoded materials were cold-recovered. The authoritative compact route is the complete production source, exact immutable input and every run option plus verified deterministic replay below.

## Complete dependency graph
1. Original exact NC57 input capsule in accepted immutable result figure-0398,73935bytes,SHA b6c84be62ea56d1c11575d4d6309563f525d734f79b0ad2a299f0b7abd2ccdd3. Reconstruct its37literal files and input reports by its complete command `python -B -S RECOVER_NC57.py NC57_SOURCE 4`.
2. Complete HULL_LP.py source in [internal-source-reference],6471bytes,SHAff8e633486cd8117106117a64c81c31a66aadac7489ee82054ae61e916420185.
3. The complete replay driver below, with the literal16-output manifest and every non-default run parameter.
No originating sandbox, Library file, unpreserved coordinate checkpoint, or omitted helper is necessary. Exact parent inputs: C372_ALT_FULL_G4/REPORT.json14190bytes,SHA639b7dd56caf48ee99f1175e20b1f305100dc0fb3f75440dd20aba8df57b4cb5; C378_ALT_POLY_G6/REPORT.json18534bytes,SHAfc46fb08252486d5c2474d70c6834b2f4849f8de25bcf18ccb059a7aa9ced661.

## Findings and status
All four400-or-fewer-step numerical endpoints are NONWINNERS. Actual configured cap is300 for each, perturbation0, initial trust.005. C372 seed37201/gamma.001 ended after102iterations with numericalS2U2 (best checkpointS2U1); seed37202/gamma.0001 after31 withS2U1. C378 seed37801/gamma.001 after40 withS2U1; seed37802/gamma.0001 after35 withS2U1. These are finite unsuccessful numerical trials, not exact own211 certificates, global exclusions or a new record. Canonical own110 remainsC622. Their source/checkpoints are retained because they reveal the limits of angular escape optimization near nearly coplanar facets.

The complete frozen BEST/FINAL coordinate hex arrays and OPTIONS/SUMMARY are reconstructed by deterministic execution in the specified environment. Two fresh cold replay directories were compared against every original byte for all16files. The observed terminal was COORD_HULL_V1_ALL16_OUTPUTS_COLD_REPLAY_IDENTICAL. This is a tested source-based recovery in CPython3.13.5,NumPy2.3.5,SciPy1.17.0,Torch2.10.0+cpu,CPU binary64,one BLAS/OMP/MKL/Torch thread,assertions. No cross-hardware or cross-version optimizer bit-identity is claimed; manifest assertions reject a divergent reproduction rather than silently substitute another object. This verifies recovery, NOT exact mechanics of the floating endpoints. The complete sources+exact inputs+all parameters are the construction definition.

## Command and expected artifacts
Save source below as REPLAY_HULL_V1.py, UTF8 with final newline. Run `python REPLAY_HULL_V1.py HULL_LP.py NC57_SOURCE NEW_OUT`. The output directory must be new. The driver checks source/inputSHA, executes four fully specified commands, requires COORD_HULL_LP_FINISHED in each log, then checks every output filename/bytecount/SHA listed literally in EXPECTED. Every BEST/FINAL contains all float.hex coordinate rows; no coordinate is abbreviated. Options and summaries reproduce too. Logs and trajectory files may additionally be written; only the16listed outputs define this captured recovery. No immutable complete optimization trajectory is claimed.

```python
#!/usr/bin/env python3
"""Reproduce all four completed V1 trials and verify every captured output byte.
Usage: python REPLAY_HULL_V1.py HULL_LP.py NC57_SOURCE NEW_OUT
"""
from pathlib import Path
import concurrent.futures,hashlib,json,subprocess,sys
assert __debug__
EXPECTED=json.loads(r'''{"HULL_372_37201/BEST.json":[5557,"cea3c9eed6fbd633618caca64bfff563bf3eaf75d8e7e824e277dddf39c36ecc"],"HULL_372_37201/FINAL.json":[5557,"ffc048f76e1c98c0e7185a6b39f3a826bc369df8b25b0e345f2368f102a9e917"],"HULL_372_37201/OPTIONS.json":[452,"e152e5aaa0eb437e0b15f4a2fb0c3cffe32ffedee59a7450bd697b5833a23a96"],"HULL_372_37201/SUMMARY.json":[947,"56cbb984e54291605d9466c902fe682884ec36a1eb280cf71b8daecf795a92a4"],"HULL_372_37202/BEST.json":[5558,"7c7c6535e03da525c8b76489120e8ac6c9b9ce71803a8ff3fffb703df353e8c2"],"HULL_372_37202/FINAL.json":[5558,"7c7c6535e03da525c8b76489120e8ac6c9b9ce71803a8ff3fffb703df353e8c2"],"HULL_372_37202/OPTIONS.json":[452,"c35f39fd6d6453ff8cdbf844dd7d3872a3c3804fef53c5971ee8aa73026ae867"],"HULL_372_37202/SUMMARY.json":[947,"79a184d6d8c0ea31da835e1512621fccbd6bf0a9711bb85a87aa86b8480eef58"],"HULL_378_37801/BEST.json":[5626,"096f7ef0976932a21712547d3a6cce2450237dd97fb899580e3de674bc022096"],"HULL_378_37801/FINAL.json":[5627,"a9187d5dd5bdde6b896cf5c6eee7058d8b5d292566d65e28a2da475dbc0cc929"],"HULL_378_37801/OPTIONS.json":[452,"a7b8ec01788c3e4dd74c993ae04ec32d07fda35f8cd8e379117758a300de8f8f"],"HULL_378_37801/SUMMARY.json":[947,"fa2c0b9ea6e7c99af1ab03d22c30a60af52adcc90ce65c5150ae2acc387cd032"],"HULL_378_37802/BEST.json":[5629,"54cacc9c46a07d50c5a2616b7cd8440509c2eab69d7f735ecc7820c3c34f3c4a"],"HULL_378_37802/FINAL.json":[5629,"54cacc9c46a07d50c5a2616b7cd8440509c2eab69d7f735ecc7820c3c34f3c4a"],"HULL_378_37802/OPTIONS.json":[452,"ff9b45a399910bbc93a60ebb8c94419eff4aa469edb3389039e266cbf1dbc1cc"],"HULL_378_37802/SUMMARY.json":[949,"ab7ec0efa34978371815297a5d5613bd2130d3ffd55588da8a9f7aa107de0fad"]}''')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
source=Path(sys.argv[1]).resolve();inputs=Path(sys.argv[2]).resolve();out=Path(sys.argv[3]).resolve()
assert sha(source)=='ff8e633486cd8117106117a64c81c31a66aadac7489ee82054ae61e916420185'
parents={372:('C372_ALT_FULL_G4','639b7dd56caf48ee99f1175e20b1f305100dc0fb3f75440dd20aba8df57b4cb5'),
         378:('C378_ALT_POLY_G6','fc46fb08252486d5c2474d70c6834b2f4849f8de25bcf18ccb059a7aa9ced661')}
out.mkdir(parents=True,exist_ok=False)
jobs=[]
for n,(label,h) in parents.items():
 p=inputs/'proof'/label/'REPORT.json';assert sha(p)==h
 for offset,gamma in [(1,'.001'),(2,'.0001')]:
  seed=n*100+offset;name=f'HULL_{n}_{seed}'
  args=[sys.executable,'-B',str(source),str(p),str(out/name),'300',gamma,str(seed),'0','.005']
  jobs.append((name,args))
def run(job):
 name,args=job
 with (out/(name+'.log')).open('w') as stream:subprocess.run(args,stdout=stream,stderr=subprocess.STDOUT,check=True)
 assert 'COORD_HULL_LP_FINISHED' in (out/(name+'.log')).read_text()
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:list(pool.map(run,jobs))
for name,value in EXPECTED.items():
 p=out/name;assert [p.stat().st_size,sha(p)]==value,name
(out/'MANIFEST.json').write_text(json.dumps(EXPECTED,sort_keys=True,separators=(',',':'))+'\n')
print('COORD_HULL_V1_ALL16_OUTPUTS_COLD_REPLAY_IDENTICAL')
```
