# material-ce75257fec15

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Recovery capsule part 1/2: C2_BASE_ELDER_ROOTC71_G6

This is a useful non-record homogeneous convex body, NOT own110 and NOT the requested endpoint. Exact maximal complex V71/E206/F137/C412; at its actual uniform-volume centroid strict (S,U,H)=(11,1,10), additional weak (0,0,0), P0 and Q10 positive radial bars. TOP is the sole unstable vertex and BASE strictly the unique nearest support plane (global polar radial elder). This repairs the CH95 C412 parent's global root order but does NOT cancel the deep polar basins.

Recovery capsule part2/2 is already immutable complete auditor material [internal-source-reference]: exact_lead.py,11008 bytes,SHA256 6b41211b97ddc5c026736d6a9e5670deb4739cd985fccab7dd40d681224d3923. Select BOTH this material and that source for an executor. Its complete literal source is preserved in the named material, not a missing sandbox file. No ancestor shape data are needed to reconstruct ROOTC: full geometry is below. Scientific derivation was from CH95_MASS_RECON71_G6 in immutable result figure-0508,SHA1496e2f4f33663ee3e62b53fbf258925e93cb8b632498a247eeec8598c3fd5e6.

Save the exact source below as replay_rootc.py beside exact_lead.py. Source receipt:2654 bytes,SHA256 67124b93b7d3fb7a4ed5e7083991f4bcdd1ad5f17028e355caf111fdf16f691a. CPython3.13.5,standard library only,assertions enabled:

    python -B -S replay_rootc.py OUT

Output ROOTC_G6.json:4206 bytes,SHA09be478db5bb0604f5eeba9a252960c185bdfe88f3965d274db6538b5ea6d132. Output ROOTC_G6.audit.json:169018 bytes,SHA0d1cff9f71a403255d66a8e0a84cdfe3df22c4b3ed1f9ab6f61e5299d360902a. The auditor computes the exhaustive integer maximal hull,true edges,two-origin exact uniform volume/moments,rational centroid,strict/additional-weak mechanics,and both full radial landscapes with simultaneous ties. Expected terminal markers LEAD_C2_EXACT_BODY_AUDIT_PASS and ROOTC_G6_EXACT_11_1_10_WEAK000_BASE_ELDER_PASS. This complete source-only reconstruction was observed to finish with both output hashes and markers. It is one computation/replay,not independent audits.

Exact centroid:(0,4292713378904719842688871/751665176295030948125000000,0). Volume:2405328564144099027/2000000000000000000. TOP original input row70 becomes extreme index66; BASE is maximal facet136,primitive raw plane[0,-1,0,493768]. Ten Q bars remain; deepest paired basins each have37 nodes/cut39 and birth-relative depth about0.49919485. No improvement in the accepted own110 C622 endpoint is claimed.

```python
from pathlib import Path
import json,hashlib,sys,subprocess
from fractions import Fraction as F
HERE=Path(__file__).resolve().parent
OUT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else HERE/'ROOTC_RECOVERED'
OUT.mkdir(parents=True,exist_ok=True)
HALF=[[596160, -493510, -106823], [463098, -475480, 196767], [431226, -462724, 253058], [422810, -456188, 362167], [350784, -440120, 466772], [236860, -448937, 543355], [181803, -388987, 617533], [64598, -389823, 651520], [-56739, -350913, 687188], [-164428, -258153, 726453], [-285762, -280261, 690973], [-400447, -315358, 629034], [-493899, -344408, 554730], [-582697, -347322, 473848], [-662593, -306832, 405786], [-726595, -294082, 311123], [-773843, -235965, 256807], [-811353, -178718, 197680], [-837844, -125749, 138405], [-853308, -60371, 106935], [-862576, -6502, 66326], [-865871, 44647, 32979], [-864802, 93817, 3150], [-859597, 145558, -13603], [-850909, 197212, -31952], [-838556, 248615, -53016], [-821565, 305270, -62281], [-799974, 360607, -81023], [-772813, 421423, -82878], [-737761, 482798, -101952], [-693085, 549672, -112378], [-635228, 623181, -113463], [-560652, 699910, -113505], [-483096, 764025, -104540], [-325604, 866770, -87209]]
TAIL=[291014,-493768,460462]
a,b,c=TAIL
rows=HALF+[[-x,y,-z] for x,y,z in HALF]+[[0,1000000,0],[a,b,c],[-a,b,c],[-a,b,-c],[a,b,-c]]
body=dict(identity='C2_BASE_ELDER_ROOTC71_G6',scale=1000000,rows=rows)
p=OUT/'ROOTC_G6.json'
p.write_text(json.dumps(body,sort_keys=True,indent=2)+'\n')
assert len(p.read_bytes())==4206
assert hashlib.sha256(p.read_bytes()).hexdigest()=='09be478db5bb0604f5eeba9a252960c185bdfe88f3965d274db6538b5ea6d132'
verify=HERE/'exact_lead.py'
assert len(verify.read_bytes())==11008
assert hashlib.sha256(verify.read_bytes()).hexdigest()=='6b41211b97ddc5c026736d6a9e5670deb4739cd985fccab7dd40d681224d3923'
o=OUT/'ROOTC_G6.audit.json'
subprocess.run([sys.executable,'-B','-S',str(verify),str(p),str(o)],check=True)
assert len(o.read_bytes())==169018
assert hashlib.sha256(o.read_bytes()).hexdigest()=='0d1cff9f71a403255d66a8e0a84cdfe3df22c4b3ed1f9ab6f61e5299d360902a'
r=json.loads(o.read_text())
assert [r[k] for k in ['V','E','F','C']]==[71,206,137,412]
assert {k:len(v) for k,v in r['strict'].items()}==dict(S=11,U=1,H=10)
assert not any(r['additional_weak'].values())
assert not r['physical_landscape']['bars'] and len(r['polar_landscape']['bars'])==10
q=list(map(F,r['polar_landscape']['births']))
assert r['raw_support_planes'][136]==[0,-1,0,493768]
assert all(q[136]>v for i,v in enumerate(q) if i!=136)
assert r['extreme_source_indices'][r['strict']['U'][0]]==70
print('ROOTC_G6_EXACT_11_1_10_WEAK000_BASE_ELDER_PASS')
```
