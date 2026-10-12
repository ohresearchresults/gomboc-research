# material-1e95ebe0da23

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J92 exact negative controls: LOW polar bridges and physical centroid repair

These are NOT own110 constructions. The exact own/reference censuses were executed in GMP with all true facets/edges, homogeneous volume/centroid, direct and global strict/weak tests and every positive P/Q bar. All three have additionalweak000 and primitive incidence zero000.

- J92_DIRECT9_G12: V142/E213/F73, own(29,27,54), reference(1,2,1) at the exact KF27C_LOW_G8 own centre. The old unique U is cut away. Reference P~.5931639584288503, Q empty.
- J92_DETOUR10_G12: V148/E222/F76, own(34,18,50), reference(1,2,1). The exact old U survives on supports67/68/69, but another reference U appears on13/22/78. Reference P~.5745964203039161, Q empty.
- J92_DETOUR_CAP_G12: V126/E189/F65, own and reference(2,5,5). Its own centre differs from the exact LOW centre by approximately(-1.2363050696e-12,-1.7233459066e-12,-9.0171927396e-13), NOT zero. The new centring cut support79 is strictly stable alongside15. It retains the old U. Reference Q~.445763265225504 and four positive P. This is a separate body derived from the .03-bump detour, not from the zero-bump DETOUR10 body.

The first70 H rows are exactly C390's67 rows plus KF27C_LOW_G8's three literal truncation rows. Only added numerical rows were rounded from their exact binary64 values, nearest ties-to-even on10^12. The exact endpoint inputs below are authoritative and need no numerical optimizer. The LOW input used here is the literal KF27C_LOW_G8 from parent figure-0579; it is not a new object or record.

## Complete dependencies and commands

This material plus the COMPLETE immutable source [internal-source-reference], RECOVERED_COORDINATOR_HANDOFF_6ab90121-cacc-83eb-b9f3-db03e57337c2.md,55922B/SHA0ed03f6169363c17184bdf01ef4d581e69b8f632e68fa41249e6f04d3c36094a, suffices for exact reconstruction. The latter contains the full nine-unit unencoded J90 core, including exact90.cpp and the complete67-row C390 input. A computational worker continuing from the LOW scientific result also receives literal parent figure-0579. No old sandbox, FULL76, numerical package or ZIP is required for these exact controls.

Save the three complete units below under their headings in one directory. Run `python REPLAY92.py --j90-source RECOVERED_COORDINATOR_HANDOFF_6ab90121-cacc-83eb-b9f3-db03e57337c2.md`. Environment: Python3.13.5 standard library; C++17 with GMP/GMPXX6.3. The expected terminal marker is J92_EXACT_RECOVERY_COMPLETE_NO_110. All input/output bytes and hashes are below. The exact audits were all executed individually and passed. A separate clean aggregate replay reproduced LOW and both DIRECT9 reports, then its containing tool call hit45 seconds while processing the DETOUR own bars; that aggregate call did not reach its final marker. Do not misreport this limited replay as an independent verification or completed aggregate run.

The generated refaudit92.cpp has SHA d9d4cf19e9c121b1ff395a983607adc60520a2e676f429ba6a889d78a031a618. It integrates and cross-checks actual own mass FIRST, then uses the separately supplied exact reference centre for the reference census. It emits both `centroid` (reference) and `own_centroid`; they are not conflated.

## J92_ENDPOINTS_INPUT.json
```json
{
  "denominator":1000000000000,"base_denominator":100000000,
  "base_file":"J90_DETACHED_C390_G8.txt",
  "base_sha256":"d3302ed3cf30d52bff82c336fbd705016c8b0b93b9a9a34ac1e8477f0a06e808",
  "low_rows":[[-36360454,-31213549,42273558],[-42575066,-16376129,44614942],[-34061100,-28210691,45960444]],
  "added_rows":{
    "J92_DIRECT9_G12":[[-1266553341461,1076424374749,520381910329],[-1577121046748,774486994439,404987427656],[-1805324288945,399564540996,254470616320],[-1930034379539,-28619929276,76330581223],[-1935530487001,-485321672937,-119528905635],[-1812979107979,-942088639480,-321295879823],[-1561541456029,-1368439295177,-515919809859],[-1188995947940,-1733806735297,-689917834204]],
    "J92_DETOUR10_G12":[[-1185541829457,1227190259321,318023577973],[-1436144980399,1069295568722,23343401429],[-1632356645327,821422722405,-270111470891],[-1758552052981,493095109827,-543116901218],[-1802542420292,99623826321,-776452372824],[-1756604946075,-338485185264,-952149190291],[-1618288814050,-796514019924,-1054745191532],[-1390923255328,-1246865987466,-1072457878712],[-1083771029812,-1660678914824,-998187220999]],
    "J92_DETOUR_CAP_G12":[[-1178335824654,1236800532215,307317219525],[-1422967687357,1086979264558,746321262],[-1614497894374,844404174653,-304211581084],[-1737288917451,517992501916,-586513691035],[-1779229423834,123154017198,-825219919896],[-1732856936083,-318891898623,-1001088281905],[-1596168858185,-782316151322,-1098111691165],[-1373042618947,-1238311075862,-1104856301164],[-1073212840032,-1657024529327,-1015471765384],[1919175325984,-313097941305,1717401662311]]
  },
  "expected_files":{
    "J92_DIRECT9_G12.txt":{"bytes":3208,"sha256":"cbc1447cc1661c0aa1d0f3c50ac65ba90c43dbed9eaa11d16aa14f262819db7a"},
    "J92_DIRECT9_G12_AUDIT.json":{"bytes":4276224,"sha256":"705e01adc6849ade9096bc388313b5316517a03347f33a5ff91695b2c1f30a7e"},
    "J92_DIRECT9_G12_REF_AUDIT.json":{"bytes":177064,"sha256":"a0ae3cc08104a90d33d5efadf7cc513868014bfb998b6648b096111f412cfdbd"},
    "J92_DETOUR10_G12.txt":{"bytes":3254,"sha256":"8522d89ad1965f96c3ed610b7027b551e87bd049d6267d50400390161064b1cb"},
    "J92_DETOUR10_G12_AUDIT.json":{"bytes":4041387,"sha256":"eeb43b4f04f86fe8acdaa3ec88959129cde477454cb2bc32e812cd1d9dbfc242"},
    "J92_DETOUR10_G12_REF_AUDIT.json":{"bytes":178751,"sha256":"007da6daacdcc9efa18c55cb446ce299096c5766cd19e4572b6fba81588f7a98"},
    "J92_DETOUR_CAP_G12.txt":{"bytes":3297,"sha256":"debec20c20d3ec5150c83a6e53749239ef988fd9adad97b6010193d749ac0942"},
    "J92_DETOUR_CAP_G12_AUDIT.json":{"bytes":422828,"sha256":"c32a925faa72b56a027b457ce5067b1af891476404181d9761515d748ff0c071"},
    "J92_DETOUR_CAP_G12_REF_AUDIT.json":{"bytes":446015,"sha256":"b72c095fd50e9fc0c6ee4cee4fd0cb2c42885406a212e6d9ceeb762b311b4206"},
    "J92_LOW_G8.txt":{"bytes":2026,"sha256":"7479724e50c1591e0bf34a8a29e2b69b400f96a7151dfcd69f1bdb3516d2de10"},
    "J92_LOW_G8_AUDIT.json":{"bytes":133708,"sha256":"b464e9c1ef30fbd933b75f35f00903ee41caa6ee41ac7564ff8cc2329d2e9f57"}
  },
  "strict":{"J92_DIRECT9_G12":[29,27,54],"J92_DETOUR10_G12":[34,18,50],"J92_DETOUR_CAP_G12":[2,5,5]},
  "reference_strict":{"J92_DIRECT9_G12":[1,2,1],"J92_DETOUR10_G12":[1,2,1],"J92_DETOUR_CAP_G12":[2,5,5]}
}
```

## make_refaudit92.py
```python
"""Generate reference-centre variant; integrate true own mass before recentering.
The exact rational reference point is read AFTER the H input. No own/reference
identity is asserted unless it is literally true. Reuses unchanged exact hull,
incidence, weak-equilibrium and bar algorithms from the complete J90 source.
"""
from pathlib import Path
import hashlib
src=Path('exact90.cpp').read_text()
assert hashlib.sha256(src.encode()).hexdigest()=='ace049716ec9ca6a016a0001bacbf2ef3196b406bf58ee03656725a77b16fa64'
key=' std::cerr<<"EXACT_MASS_DONE\\n";'
assert src.count(key)==1
new=r''' VQ own_g=g;for(auto&a:g){assert(std::cin>>a);a.canonicalize();}
 p.clear();q.clear();for(auto&a:x)p.push_back(sub(a,g));for(int f:active){VQ nn=qvec(n[f]);Q h=hh[f]-dot(nn,g);assert(h>0);q.push_back(mul(nn,Q(1/h)));}
 std::cerr<<"EXACT_OWN_MASS_THEN_REFERENCE_CENTRE_DONE\n";'''
src=src.replace(key,new)
key='std::cout<<",\\\"active_input_planes\\\":";'
assert src.count(key)==1
src=src.replace(key,'std::cout<<",\\\"own_centroid\\\":";vprint(own_g);'+key)
src=src.replace('EXACT_HULL_MASS_DIRECT_GLOBAL_CENSUS_FULL_BARS_PASS','EXACT_HULL_OWN_MASS_REFERENCE_CENSUS_FULL_BARS_PASS').replace('J90_EXACT_PASS','J92_REFERENCE_PASS')
Path('refaudit92.cpp').write_text(src)
print('J92_REFERENCE_AUDITOR_GENERATED',hashlib.sha256(src.encode()).hexdigest())
```

## REPLAY92.py
```python
"""Exact recovery of three J92 negative controls, not a target construction.
Place all files of J92_EXACT_RECOVERY.md in one directory and run:
python REPLAY92.py --j90-source RECOVERED_COORDINATOR_HANDOFF_6ab90121-cacc-83eb-b9f3-db03e57337c2.md
The complete indicated source is immutable run material [internal-source-reference].
This does not require a former sandbox, numerical optimization, or a ZIP.
"""
import argparse,hashlib,json,re,subprocess,sys
from pathlib import Path
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
p=argparse.ArgumentParser();p.add_argument('--j90-source',type=Path,required=True);args=p.parse_args()
b=args.j90_source.read_bytes();assert hashlib.sha256(b).hexdigest()=='0ed03f6169363c17184bdf01ef4d581e69b8f632e68fa41249e6f04d3c36094a'
text=b.decode();obj=json.loads(text.strip().removeprefix('```json').removesuffix('```').strip());report=obj['handoff_markdown']
core=report.split('```bash\n',1)[1].split('\n```',1)[0]+'\n'
assert hashlib.sha256(core.encode()).hexdigest()=='525ebd08fc99ca4a5f46552533508bec54c80465b03a9a7a9f77f939bc4f5efb'
for name,marker,body in re.findall(r"cat > '([^']+)' <<'([^']+)'\n(.*?)\n\2\n",core,re.S):Path(name).write_text(body+'\n')
inp=json.loads(Path('J92_ENDPOINTS_INPUT.json').read_text());base=Path(inp['base_file']).read_bytes();assert hashlib.sha256(base).hexdigest()==inp['base_sha256']
rows=[list(map(int,r.split())) for r in base.decode().splitlines()[1:]]+inp['low_rows'];assert len(rows)==70
Path('J92_LOW_G8.txt').write_text('70 100000000\n'+'\n'.join(' '.join(map(str,r)) for r in rows)+'\n')
for name,add in inp['added_rows'].items():
 rr=[[v*10000 for v in r] for r in rows]+add
 Path(name+'.txt').write_text(f'{len(rr)} 1000000000000\n'+'\n'.join(' '.join(map(str,r)) for r in rr)+'\n')
subprocess.run([sys.executable,'make_refaudit92.py'],check=True)
for source,out in [('exact90.cpp','exact90'),('refaudit92.cpp','refaudit92')]:subprocess.run(['g++','-std=c++17','-O2',source,'-lgmpxx','-lgmp','-o',out],check=True)
def run(exe,raw,out):
 with Path(out).open('wb') as f:subprocess.run(['./'+exe],input=raw,stdout=f,check=True)
run('exact90',Path('J92_LOW_G8.txt').read_bytes(),'J92_LOW_G8_AUDIT.json')
low=json.loads(Path('J92_LOW_G8_AUDIT.json').read_text());g=low['centroid'];old_u=low['vertices'][low['U'][0]]
for name in inp['added_rows']:
 raw=Path(name+'.txt').read_bytes();run('exact90',raw,name+'_AUDIT.json');run('refaudit92',raw+(' '.join(g)+'\n').encode(),name+'_REF_AUDIT.json')
 a=json.loads(Path(name+'_AUDIT.json').read_text());r=json.loads(Path(name+'_REF_AUDIT.json').read_text())
 assert a['strict']==inp['strict'][name] and r['strict']==inp['reference_strict'][name]
 assert a['weak']==r['weak']==a['primitive_zeros']==r['primitive_zeros']==[0,0,0]
 assert r['own_centroid']==a['centroid'] and r['centroid']==g
 assert a['E']<=249 and a['V']-a['E']+a['F']==2
 assert len(a['P'])==a['strict'][1]-1 and len(a['Q'])==a['strict'][0]-1
 retained=old_u in a['vertices'];assert retained==(name!='J92_DIRECT9_G12')
 if name=='J92_DETOUR_CAP_G12':
  assert [a['active_input_planes'][i] for i in a['S']]==[15,79]
  assert all(abs(F(x)-F(y))<F(1,10**10) for x,y in zip(a['centroid'],g))
 print('J92_EXACT_NONWINNER',name,a['V'],a['E'],a['F'],'own',a['strict'],'reference',r['strict'])
for name,meta in inp['expected_files'].items():
 b=Path(name).read_bytes();assert len(b)==meta['bytes'] and hashlib.sha256(b).hexdigest()==meta['sha256'],name
print('J92_EXACT_RECOVERY_COMPLETE_NO_110')
```
