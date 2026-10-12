# material-61521e2c50db

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# W51_STACK424 Recovery capsule part 2/3

All three parts are required for the interval theorem. This part contains the complete literal W51_ROBUST_G3 input and generator for the five exact grid endpoints. The input was obtained from figure-0537, SHA-256 05577e4a0b36b334bf63e1fd41ffdbb8b9c663892f7da776c851bf47acf7af21. No external files from that archive are required by this capsule. These exact 32 coordinate rows, not any similarly named scratch object, determine the baseline: input row3 is interior, V31/E87/F58,C174, own211, additional weak000. Baseline volume 534976657/120000000.

Save the source below as stack_family.py, LF and final newline. File bytes4297, SHA-256 e11197d6e58638d3620920800023ea222fcde0f8f3754cfcabef13d81cbe328b. Requires part1 exact_audit.py. Python3.13.5 standard library only. Reconstruction and full exact verification:

    python -B -S stack_family.py stack_exact --powers 2 3 4 5 6

Expected terminal marker STACK_FAMILY_EXACT_PASS 5. Every grid endpoint: V32/E90/F60,C180, strict[4,2,4], additional weak[0,0,0], primitive zero[0,0,0]. At t=1/10^6, actual Q main .7827432103210076; tiny positive bars remain and are not tolerance-discarded. Both raw and cosine zero-margin losses decrease to zero in the family; this does NOT approach own110 in the persistence sense. The certified interval and proof of the limit are in part3.

Expected generated files, bytes and SHA-256 (compact JSON encoding, sorted keys, final LF):
```json
{"T2.audit.json":{"bytes":14420,"sha256":"38a3c8c5438b3c6a89e25d341210e2d31edb9f655ad25cf8ea6d074a57073fd6"},"T2.input.json":{"bytes":3086,"sha256":"3183f7118cf8a62be59bdec69ed4e686c6ce0d78b330c800a222df5e40224977"},"T3.audit.json":{"bytes":14481,"sha256":"cc323c45518220ba68605d283c011bf4c0b8c5879c711a52e8907b7927edb77f"},"T3.input.json":{"bytes":3116,"sha256":"b93a06064b276da25493dde745abe1ec84f0dbbd6da719e8233263e45dacd93d"},"T4.audit.json":{"bytes":14850,"sha256":"83e7c6fad3a3016779d875d076f745f76edb8b692486c8dca25253e132d521e1"},"T4.input.json":{"bytes":3288,"sha256":"00169334b785449f03b87d85e8884adfaad8bf70577dcbf23db8501f7a80ae1c"},"T5.audit.json":{"bytes":15066,"sha256":"d5f983030d9838fe57d0313a0ca0879c805a19af654808e1873302b98f7a17fb"},"T5.input.json":{"bytes":3389,"sha256":"86858a8af0cc0c74735c5438ca81d12dafeb35a2608856f2b05100c1257637a0"},"T6.audit.json":{"bytes":15274,"sha256":"e328282214d70936e141e0463811de1e4aaed5f8809e50469be8af6d6bab7c87"},"T6.input.json":{"bytes":3490,"sha256":"f9a1745cf6741df912947f8be55a2fde5de12856d3dbd95fedc1c52b39ef3206"},"ledger.json":{"bytes":15365,"sha256":"f45e9cf0468eb3b007395f1b69f6571322bc9913363549cd64e1490e0c0b9613"}}
```
The generated manifest.json is1183bytes SHA-256 558385f7f679621aca18a0e206185807b64ea3295d13c0b0345fd16b34482f0e.

```python
"""Exact shallow-pyramid family illustrating noncoercivity of raw chord-margin losses.
Input: literal W51_ROBUST_G3, denominator 1000, figure-0537.
Stack above the junior stable facet [10,29,30] along its COM normal.
Run: python -B -S stack_family.py OUTDIR --powers 2 3 4 5 6
Requires exact_audit.py in the same directory; standard library only.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import lcm
from pathlib import Path
import argparse,json,hashlib
from exact_audit import audit,dot,sub,cross,mul,add
POINTS=[[-2678,-1136,975],[-2745,-769,406],[-2212,-627,45],[96,-637,-245],[465,1184,-402],[80,119,-1160],[294,781,-935],[157,537,-1075],[311,1098,-580],[681,814,-815],[565,-379,-1032],[883,11,-962],[947,461,-856],[1007,793,-634],[840,1037,-473],[1206,848,-369],[1174,1065,103],[1389,818,-95],[1535,736,189],[1603,668,465],[1571,172,-108],[1639,563,721],[1644,425,972],[1609,244,1244],[1506,4,1547],[1301,-295,1859],[970,-604,2131],[548,-896,2304],[78,-1126,2365],[-418,-1288,2323],[-968,-1386,2170],[-1604,-1391,1853]]
DEN=1000

def make(t):
    base=audit(POINTS,DEN)
    face=next(f for f in base['facets'] if set(f['vertices'])=={10,29,30})
    n=tuple(face['normal']);h=F(face['offset'],DEN);c=tuple(F(s) for s in base['centroid']);nn=dot(n,n)
    hc=h-dot(n,c)
    apex=add(c,mul((1+t)*hc/nn,n))
    p=[tuple(F(x,DEN) for x in row) for row in POINTS]+[apex]
    D=lcm(*(x.denominator for row in p for x in row));rows=[[int(x*D) for x in row] for row in p]
    return dict(name='W51_SHALLOW_STACK_T_'+str(t).replace('/','_'),denominator=D,points=rows),base,face,apex

def margins(data,result):
    # All max/min operations exact. Raw margins normalized by source squared radius.
    p=[tuple(F(x,data['denominator']) for x in row) for row in data['points']]
    c=tuple(F(s) for s in result['centroid']);x=[sub(p[i],c) for i in result['vertices']]
    q=[]
    for face in result['facets']:
        n=tuple(face['normal']);h=F(face['offset'],data['denominator']);q.append(mul(1/(h-dot(n,c)),n))
    output={}
    for name,z in [('P',x),('Q',q)]:
        r=[dot(a,a) for a in z];root=max(range(len(z)),key=lambda i:r[i])
        raw=[max(dot(z[i],sub(z[j],z[i]))/r[i] for j in range(len(z)) if j!=i) for i in range(len(z))]
        defects=[max(F(0),-w) for i,w in enumerate(raw) if i!=root]
        cosine=[]
        for i in range(len(z)):
            if i==root:continue
            pairs=[(dot(z[i],sub(z[j],z[i])),dot(sub(z[j],z[i]),sub(z[j],z[i]))) for j in range(len(z)) if j!=i]
            cosine.append(F(0) if any(a>=0 for a,b in pairs) else min(a*a/(r[i]*b) for a,b in pairs))
        output[name]=dict(cosine_squared_loss=str(sum(cosine)),cosine_squared_loss_float=float(sum(cosine)),cosine_worst_defect=float(max(cosine))**.5,root=root,raw_min_nonroot=str(min(w for i,w in enumerate(raw) if i!=root)),loss=str(sum(v*v for v in defects)),loss_float=float(sum(v*v for v in defects)),worst_defect=float(max(defects)))
    return output

def main():
    ap=argparse.ArgumentParser();ap.add_argument('outdir');ap.add_argument('--powers',type=int,nargs='+',default=[2,3,4,5,6]);a=ap.parse_args();out=Path(a.outdir);out.mkdir(parents=True,exist_ok=True);ledger=[]
    for k in a.powers:
        t=F(1,10**k);data,base,face,apex=make(t);res=audit(data['points'],data['denominator']);loss=margins(data,res)
        for suffix,obj in [('input',data),('audit',res)]:
            (out/(f'T{k}.{suffix}.json')).write_text(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n')
        row=dict(power=k,t=str(t),V=res['V'],E=res['E'],F=res['F'],strict=res['strict'],weak=res['additional_weak'],zeros=res['primitive_zero'],P=[b['depth_float'] for b in res['P']],Q=[b['depth_float'] for b in res['Q']],raw=loss)
        ledger.append(row);print('STACK_EXACT',json.dumps(row),flush=True)
    (out/'ledger.json').write_text(json.dumps(ledger,sort_keys=True,separators=(',',':'))+'\n')
    manifest={f.name:dict(bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest()) for f in sorted(out.glob('*.json')) if f.name!='manifest.json'}
    (out/'manifest.json').write_text(json.dumps(manifest,sort_keys=True,separators=(',',':'))+'\n')
    print('STACK_FAMILY_EXACT_PASS',len(ledger))
if __name__=='__main__':main()
```
