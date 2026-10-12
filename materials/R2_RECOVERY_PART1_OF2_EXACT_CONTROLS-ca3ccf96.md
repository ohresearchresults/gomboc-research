# material-ca3ccf961d92

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Recovery capsule part 1/2: R2_NONLINEAR_ESCAPE_RETRACTION
This capsule preserves four exact non-target bodies. R2_BEST (grid1e10), R2_G8, R2_G7 all V58/E168/F112,C336, own211/additionalweak000/primitivezero000, P0/Q1. Depths .3860491795645384/.3860491799813634/.38604918772613195. R2_G6 is meaningful coarse negative: samecomplex,own11/14/23,weak000/zero000,P13Q10. None is110. Part2 preserves complete executed numerical producing source; not needed to reconstruct literal endpoints. Do not advance canonical own110/C622 to any of these controls.
Required exact auditor dependency: [internal-source-reference], JB_C168_OWN211_EXACT_RECOVERY_V1.md13684B,SHA2b1c5045a6bac634a6858e76e723cf3820fe4185a0ef3253bb1a845d696b84e2. Its exact_poly.py6134B SHA898f77989193886996d6f2dc121ccdfdf611b8a9ac52fd3207557eac6a69c0c4 is complete stdlib source. Recovered here with matching sourcehash; triple enumeration certifies true maximal triangular hull, actual filledvolume/moments, strict/closedweak S/U/H and both complete rational P/Q landscapes. Nontriangular maximalfacets explicitly rejected, not silentlytriangulated. No claim of second independent hull engine.

Write both blocks verbatim with LF final newline. R2_BEST.json2179B SHA119fa76fbc2ee00387cba4d488be9a5876484e64f78f734448674ac59a327bb4; recover_r2.py1020B SHA8f9f3407b51635bf7dada0f23d34c25680a4bd5db56602a21f506433d3572701. Commands:
```
python -B -S recover_r2.py
python -B -S exact_poly.py R2_BEST.json
python -B -S exact_poly.py R2_G8.json
python -B -S exact_poly.py R2_G7.json
python -B -S exact_poly.py R2_G6.json
```
Observed R2_RECOVERY_PASS and four EXACT_POLY_AUDIT_PASS lines with classes above. InputG8 1827B SHA0c18a964ab348bd517b14a9c3a1d01c78c0c237e4b905b98233a7926ba49568f;G7 1652B SHA7b0cdc42b58f0159c39aee198b31b8f65e410fe2fc62c19aee54eb0315020cb5;G6 1477B SHA097c3cbc58a21672332659a8c3a7b9fde7225fe4ace4ad954a58bbfa11ac9efb.
Audit receipts: R2_BEST_AUDIT.json6630B SHA451436b8a953b6c3db036d7b23c25a77597b8e9c4512f2c07cd1def14e720b20;R2_G8_AUDIT.json6052B SHA20296e3f57a4330775efcf6cc8835a6be92087e54b31b15c6b6c6ea5ed64fc65;R2_G7_AUDIT.json5766B SHA41cc63f0e89bec7bebd1b1edfe33587b7d9803e3b58aee7331357bb73514cef2;R2_G6_AUDIT.json16975B SHAf42b62952871014ac87e3d1be00c57972fe75ed1a00eeceffa8a202c1d4e4749. Observed CPython3.13.5. All complete exactgeometry/mass/bar fractions regenerate without optimizer or originating sandbox.
For fine R2_BEST S=[49,101],U=[57],H=[[36,57]]. SoleQpeak101elder49,component32/cut20,attainingpath[101,103,104,105,102,110,106,108,109,107,91,93,94,92,82,84,85,83,98,70,71,68,97,96,95,88,75,49]. Complete component/cut/birth/death/mass remain in deterministic audit. OldSQP1peak97/elder48 labels are not this newhull's labels.

## R2_BEST.json
```json
{"denominator":10000000000,"name":"R2_BEST","points":[[-10171822863,-892876721,894156507],[-10008534855,-661888443,2839633922],[-9994313119,-998019718,-1000972534],[-9983086023,-1925828138,1341810806],[-9654716833,-97723285,-2458670677],[-9612974070,335080851,4451530915],[-9620549472,-3099707153,-82253580],[-9419701148,-1316206803,-2866837918],[-8838417242,1227370289,6074801177],[-9153349077,1238629008,-3387223034],[-8976807502,-4123056155,-1422046821],[-8655598105,908936360,-4475345202],[-8404667118,-3979540746,-3205428402],[-8462199760,-1311662631,-4693564593],[-7675438861,1901442613,7665167970],[-8135368919,-4931363046,-2649647066],[-7219823947,-869355347,-6269100807],[-7245340797,-5127411121,-4083795676],[-6735831294,2139766772,-6242777065],[-6565156501,-6541239471,-2765331573],[-6176296790,2487977372,9064488401],[-6204280005,-5189808910,-5319842320],[-5743364182,-6575675199,-3985415752],[-5538988007,166919335,-7560053552],[-4401258356,-7865121590,-2697755270],[-5177130735,-4723995728,-6534923257],[-4381031568,3116651097,10165252188],[-4288055223,-3590256382,-7616128363],[-4350291947,-6290433118,-5635654279],[-3219974241,1835927730,-8189346958],[-1528535003,-8648480812,-1884425884],[-2921490047,-2624769950,-8446131639],[-3507241728,-5000763171,-7235413312],[-2336556465,3781142966,10898193355],[-2314638288,-7146917227,-5497339636],[-1776541106,-5115042604,-7637967884],[-707584120,-2417374785,-8764481631],[1413463948,-8167161591,235893315],[231947689,-5162652287,-7627763505],[-45194439,-7659678512,-4846148881],[150044691,4480769145,11256192197],[1068558113,317720560,-7436742737],[1438751725,-7493918366,-4754318990],[2812399643,5214303853,11003872357],[5191368874,23060814,-5374455276],[5621352680,-1877776585,-4288161558],[6561528579,3487977653,-4496946371],[6148464699,6104507833,9832755214],[9797685452,6803886052,7255620211],[15067867011,7226869208,58898881],[363050133,4130082905,-5508087374],[5585677694,1252650869,5779471819],[-190945194,57158649,7521165167],[1488479736,-1102657053,6177939034],[3086744458,-6807320867,-2121077680],[1635234255,1684511317,-6798490301],[7603298648,-1159645808,-2204109365],[8853845747,1214794178,-2852086596]]}
```

## recover_r2.py
```python
"""Recover three coarser rational controls from literal R2_BEST.json."""
import json,hashlib
from pathlib import Path
p=Path('R2_BEST.json');b=p.read_bytes()
assert len(b)==2179 and hashlib.sha256(b).hexdigest()=='119fa76fbc2ee00387cba4d488be9a5876484e64f78f734448674ac59a327bb4'
x=json.loads(b)
checks={8:(1827,'0c18a964ab348bd517b14a9c3a1d01c78c0c237e4b905b98233a7926ba49568f'),7:(1652,'7b0cdc42b58f0159c39aee198b31b8f65e410fe2fc62c19aee54eb0315020cb5'),6:(1477,'097c3cbc58a21672332659a8c3a7b9fde7225fe4ace4ad954a58bbfa11ac9efb')}
for k,(size,sha) in checks.items():
    def rnd(a):
        b=10**(10-k);q,r=divmod(a,b)
        return q+int(2*r>b or(2*r==b and q%2))
    z=dict(denominator=10**k,name=f'R2_G{k}',points=[[rnd(v) for v in p] for p in x['points']])
    data=(json.dumps(z,separators=(',',':'))+'\n').encode()
    assert len(data)==size and hashlib.sha256(data).hexdigest()==sha
    Path(z['name']+'.json').write_bytes(data)
    print('R2_RECOVER_INPUT_PASS',z['name'],size,sha)
print('R2_RECOVERY_PASS')
```
