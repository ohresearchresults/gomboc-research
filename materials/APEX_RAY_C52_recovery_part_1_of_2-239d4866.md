# material-239d4866c1f0

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Recovery capsule part 1/2: APEX-RAY-C52 exact source and inputs
Object identity APEX-RAY-C52. Part1 contains the complete runnable rational certificate/replay, exact parameters and output receipts. Part2 supplies its geometric proof, meaning, scope and limitations. Both are required scientific evidence; this part alone suffices to reproduce the exact computation. Nothing depends on an originating sandbox. No third-party dependencies: observed CPython3.13.5 standard library only.

Save the three fenced files as UTF-8/LF, one final newline. Extraction from this material saved as capsule.md:
python -B -S -c 'import pathlib,re,sys;p=pathlib.Path(sys.argv[2]);p.mkdir(parents=True,exist_ok=True);s=pathlib.Path(sys.argv[1]).read_text();[(p/n).write_text(t,encoding="utf-8",newline="\n") for n,t in re.findall(r"### File: ([^\n]+)\n```(?:python|json)\n(.*?)```",s,re.S)]' capsule.md SOURCE

Reconstruction and verification: cd SOURCE && python -B -S replay_apex.py OUT. Expected nine APEX_RATIONAL_PAIR_PASS lines, APEX_RATIONAL_NINE_PAIRS_PASS 9 108, C2_OWN110_SCOPED_C_GE_52_PASS [(5,4),(5,5),(5,6),(5,7),(6,4),(6,5),(6,6),(7,5)]. Individual command: python -B -S certify_apex.py 6 6 --n 128 --p-bins 256 --depth 10 --out CERT_6_6_256.json. Elapsed console time is nondeterministic; output JSON bytes are deterministic.

Input receipts: certify_apex.py4705B SHA260e6f60b56067f22379f61a806a0bd2378e4e078d36945c97cd56e41abdc46e;replay_apex.py1816B SHA33edac97cfa4556cc833994dfaa63c994535ecfcdb03f6264fa51a8f12b12f35;EXACT_OUTPUTS.json1170B SHA744f8881d35a37926405669e4fd5aaa768dc37d0598984f449c18af881e5145e. All output filenames/bytes/hashes are literal in the manifest. Nine outputs were cold-regenerated together and matched; (6,6) was separately rerun. These are reproducibility checks, not two independently authored mathematical proof programs. Actual pair leaf counts1,1,8,13,24,1,11,35,14 in sorted manifest order total108. EVERY leaf has positive rational moment and geometric flag False. All exact inputs: n128,p_bins256,maxdepth10,2^-80 downward quantization, UMAX literal in source, no seed/floating optimizer.

Provenance correction: ephemeral compacted notes gave alternate source/output hashes, different leaf counts and geometric-placeholder claims that did not match actual runtime files. They were not published into scientific state. These literal units and successful cold-replay receipts are authoritative. All nine use moment positivity, including (4,6),(6,4). The empty-range guard was corrected from low>=3 to low>3; none of these nine has low>=3 and their output bytes did not change.

### File: certify_apex.py
```python
"""Rational apex-ray first-moment certificate; no floating numerical decisions.
All exact circle/normal parameters obey (k+1)atan(u)<157/50<pi.
A pass is a sufficient nonexistence proof for the specified opposite-root depths.
"""
import argparse,bisect,hashlib,json,time
from fractions import Fraction as F
from pathlib import Path
UMAX={4:F(29,40),5:F(72,125),6:F(481,1000),7:F(413,1000),8:F(363,1000)}

def atan_upper(u):
    return sum(((-1)**j*u**(2*j+1)/F(2*j+1) for j in range(41)),F(0))

def pi_lower():
    # Machin pi=16 atan(1/5)-4 atan(1/239), alternating lower/upper.
    a=F(1,5); b=F(1,239)
    al=sum(((-1)**j*a**(2*j+1)/F(2*j+1) for j in range(10)),F(0))
    bu=sum(((-1)**j*b**(2*j+1)/F(2*j+1) for j in range(9)),F(0))
    return 16*al-4*bu

def reim(n,u):
    a,b=F(1),F(0)
    for _ in range(n):a,b=a-b*u,b+a*u
    return a,b

def points(k,n):
    u=UMAX[k]
    assert (k+1)*atan_upper(u)<F(157,50)<pi_lower()
    out=[]
    for j in range(n+1):
        b,a=reim(k+1,u*j/n)
        assert a>=0
        out.append((a,b))
    return out

def lines(k,n):
    pts=points(k,n)
    raw=sorted(set((a/(1-b),-b/(1-b)) for a,b in pts if a>0))
    # Upper envelope of affine reciprocal radial endpoints.
    hull=[]; starts=[]
    for m,c in raw:
        if hull and m==hull[-1][0]:
            if c<=hull[-1][1]:continue
            hull.pop();starts.pop()
        start=None
        while hull:
            pm,pc=hull[-1];start=(pc-c)/(m-pm)
            if len(hull)==1 or start>starts[-1]:break
            hull.pop();starts.pop()
        if not hull:start=None
        hull.append((m,c));starts.append(start)
    return pts,hull,starts[1:]

def G(t,h):return h**3*(t/F(3)-h/F(4))

def interval_bound(ta,tb,inner,hull,starts,np):
    # A disc of radius a at height -b forces a cone from the actual apex.
    rec=[]; zs=[]; peak=F(-1)
    for a,b in inner:
        z=-b
        if z>=ta:continue
        p=a/(tb-z)
        if p>peak:rec.append(p);zs.append(z);peak=p
    target=3*tb/(4*ta)
    pmax=max(F(0),rec[-1] if rec else F(0),min((target-c)/m for m,c in hull))
    if pmax==0:return F(0),False
    step=pmax/np;total=0;precision=2**80
    for j in range(np):
        pl=step*j;ph=step*(j+1)
        hidx=bisect.bisect_right(starts,pl)
        m,c=hull[hidx];line=m*pl+c
        beta=tb+1
        if line>0:beta=min(beta,tb/line)
        i=bisect.bisect_left(rec,ph)
        alpha=ta-zs[i] if i<len(rec) else F(0)
        if alpha>beta:return F(1),True # Uniform geometric contradiction.
        term=(ph*ph-pl*pl)*min(G(ta,alpha),G(ta,beta))
        total+=(precision*term.numerator)//term.denominator
    return F(total,precision),False

def certify(k,l,n=128,np=512,maxdepth=12):
    outer,hull,starts=lines(k,n);inner=points(l,n)
    # Necessary: apex bounds every height, and stable foot (0,-1) belongs to K.
    low=max(max(-b for a,b in outer),max(-b for a,b in inner))
    if low>3:return {'k':k,'l':l,'closed':True,'reason':'root range empty'}
    stack=[(low,F(3),0)];leaves=[];bad=[];calls=0
    while stack:
        ta,tb,dep=stack.pop();calls+=1
        bound,impossible=interval_bound(ta,tb,inner,hull,starts,np)
        if bound>0:
            leaves.append([str(ta),str(tb),str(bound),impossible,dep])
        elif dep<maxdepth:
            mid=(ta+tb)/2
            stack.extend([(mid,tb,dep+1),(ta,mid,dep+1)])
        else:bad.append([str(ta),str(tb),str(bound),dep])
        if calls%100==0:print('WORK',k,l,calls,len(leaves),len(bad),flush=True)
        if len(bad)>8:break
    rows=sorted(leaves,key=lambda a:F(a[0]))
    if not bad and not stack:
        assert rows[0][0]==str(low) and rows[-1][1]=='3'
        assert all(a[1]==b[0] for a,b in zip(rows,rows[1:]))
    return {'k':k,'l':l,'closed':not bad and not stack,'lower_t':str(low),
            'n':n,'p_bins':np,'maxdepth':maxdepth,'calls':calls,
            'leaf_count':len(leaves),'leaves':rows,'bad':bad,'unprocessed':len(stack)}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('k',type=int);ap.add_argument('l',type=int)
    ap.add_argument('--n',type=int,default=128);ap.add_argument('--p-bins',type=int,default=512)
    ap.add_argument('--depth',type=int,default=12);ap.add_argument('--out',default='CERTIFICATE.json')
    args=ap.parse_args();t0=time.monotonic()
    out=certify(args.k,args.l,args.n,args.p_bins,args.depth)
    data=(json.dumps(out,sort_keys=True,indent=2)+'\n').encode()
    Path(args.out).write_bytes(data)
    print('APEX_RATIONAL_PAIR_PASS' if out['closed'] else 'APEX_RATIONAL_PAIR_INCONCLUSIVE',
          args.k,args.l,out.get('leaf_count'),len(data),hashlib.sha256(data).hexdigest(),flush=True)
    print('elapsed',time.monotonic()-t0,flush=True)
```

### File: replay_apex.py
```python
"""Cold exact replay of the nine listed apex-ray moment exclusions."""
import hashlib
import json
from pathlib import Path
import sys
from fractions import Fraction
from certify_apex import certify

HERE = Path(__file__).resolve().parent
SOURCE_SHA = '260e6f60b56067f22379f61a806a0bd2378e4e078d36945c97cd56e41abdc46e'
assert hashlib.sha256((HERE / 'certify_apex.py').read_bytes()).hexdigest() == SOURCE_SHA
manifest = json.loads((HERE / 'EXACT_OUTPUTS.json').read_text())
assert len(manifest) == 9
outdir = Path(sys.argv[1] if len(sys.argv) > 1 else 'APEX_EXACT_REPLAY')
outdir.mkdir(parents=True, exist_ok=True)
total = 0
for filename, receipt in sorted(manifest.items()):
    _, k, l, _ = filename.split('_')
    k, l = int(k), int(l)
    result = certify(k, l, n=128, np=256, maxdepth=10)
    assert result['closed'] and not result['bad'] and not result['unprocessed']
    assert Fraction(result['lower_t']) < 3
    assert all(Fraction(row[2]) > 0 and row[3] is False for row in result['leaves'])
    data = (json.dumps(result, sort_keys=True, indent=2) + '\n').encode('utf-8')
    digest = hashlib.sha256(data).hexdigest()
    assert len(data) == receipt['bytes'] and digest == receipt['sha256']
    (outdir / filename).write_bytes(data)
    total += result['leaf_count']
    print('APEX_RATIONAL_PAIR_PASS', k, l, result['leaf_count'], len(data), digest)
assert total == 108
# Accepted Minimum V>=10,F>=9, C2 parity and valence leave these small budgets.
necessary = {(k, l) for k in range(5, 13) for l in range(4, 13)
             if k+l <= 12 and 2*k+3 <= 4*l and 2*l+3 <= 4*k}
covered = {(int(name.split('_')[1]), int(name.split('_')[2])) for name in manifest}
assert necessary <= covered
print('APEX_RATIONAL_NINE_PAIRS_PASS', len(manifest), total)
print('C2_OWN110_SCOPED_C_GE_52_PASS', sorted(necessary))
```

### File: EXACT_OUTPUTS.json
```json
{
  "CERT_4_6_256.json": {
    "bytes": 329,
    "sha256": "4733ecacc374069b0a6ba9367cedfe17a21d14669149564ef932ab09d7c33312"
  },
  "CERT_5_4_256.json": {
    "bytes": 329,
    "sha256": "020d14ff3f37287f1f277cd5c5096bb225ecd00763a8dcd6d4e1ceb6ec46daa1"
  },
  "CERT_5_5_256.json": {
    "bytes": 1535,
    "sha256": "58d361518caf110042b6889c934fadeea47de561439111d53135eba49d493d39"
  },
  "CERT_5_6_256.json": {
    "bytes": 2388,
    "sha256": "4a5b5328e1c3728ccc8d01ac2a650e7cb519dc42be381bdd3275e2570afe77bf"
  },
  "CERT_5_7_256.json": {
    "bytes": 4251,
    "sha256": "704d17f588765b3a5906816be9fa93140b2ba089be9cae68d994a0eed07cd315"
  },
  "CERT_6_4_256.json": {
    "bytes": 332,
    "sha256": "e2de9ce17da226187c8a058371a00064a6f0dfcb91395868e0034e72fc5171b6"
  },
  "CERT_6_5_256.json": {
    "bytes": 2048,
    "sha256": "c59dd9aeb364863930e7199bd6a620e10d5c82251c1d37409a8aa0e105cc94b7"
  },
  "CERT_6_6_256.json": {
    "bytes": 6975,
    "sha256": "dd9c6ee8a7d8c84244e61fd7a1094eb0e41f23893bbc9ef18323459cc1f6e1ee"
  },
  "CERT_7_5_256.json": {
    "bytes": 2555,
    "sha256": "07b9ba0c97d069de75db98bea87e2418bc4f5cb0a56bef08d95c390e6f1a0b20"
  }
}
```
