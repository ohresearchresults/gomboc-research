# material-426ffa74daa0

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# IGS numerical-method recovery capsule part 2 of 2

Part1 is [internal-source-reference],14234 bytes,SHA256 5de0f452cd7c597c8402d1889f5b37a4ba637bdbc560b1946c0a8d8af04164a7. Together these two parts preserve FOUR complete Python units and TWO complete numerical checkpoints, sufficient to recover the numerical methods which produced the exact IGS controls. Neither numerical objective is a110 certificate. The two exact rational solids and their scoped whole-axis exclusion proofs are independently recoverable from [internal-source-reference] and [internal-source-reference].

## igs_centerline.py
2056 bytes,SHA256 5b856c344ceba61d3046f1c9b6ff94af59fdb2fa45e1be7baf8a3c213f46495e.

```python
"""Numerical complete equilibrium intervals on the C2 fixed centre line.
Coordinates are actual-volume-centred at zero. Closed bad intervals include weak S/U.
An exact version must use rational halfspace and directed-edge coefficients.
"""
import sys,json
from pathlib import Path
import numpy as np
import torch
from igs_scout import IGS

def interval(coeffs,lo=-np.inf,hi=np.inf,tol=1e-12):
    # A+B*c >=0.
    for a,b in coeffs:
        if abs(b)<tol:
            if a < -tol:return None
        elif b>0:lo=max(lo,-a/b)
        else:hi=min(hi,-a/b)
    return (lo,hi) if lo<=hi else None

def centerline(v,q,faces,edges,uroot,sroot):
    eu=np.array([0.,1.,0.]);axis=interval([(1.,-a[1]) for a in q])
    assert axis is not None
    records=[];adj=[[] for _ in v]
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    for i,nb in enumerate(adj):
        z=interval([(-v[i]@(v[j]-v[i]),v[j,1]-v[i,1]) for j in nb],*axis)
        if z is not None:records.append(('U',i,*z,i==uroot))
    for i,(a,f) in enumerate(zip(q,faces)):
        foot=a/(a@a);velocity=eu-a*a[1]/(a@a)
        co=[]
        for ia,ib in zip(f,f[1:]+f[:1]):
            e=v[ib]-v[ia]
            co.append((a@np.cross(e,foot-v[ia]),a@np.cross(e,velocity)))
        z=interval(co,*axis)
        if z is not None:records.append(('S',i,*z,i==sroot))
    bad=sorted((a,b) for typ,i,a,b,root in records if not root)
    union=[]
    for a,b in bad:
        if union and a<=union[-1][1]+1e-12:union[-1]=(union[-1][0],max(b,union[-1][1]))
        else:union.append((a,b))
    good=[];left=axis[0]
    for a,b in union:
        if a>left+1e-12:good.append((left,a))
        left=max(left,b)
    if left<axis[1]-1e-12:good.append((left,axis[1]))
    return dict(axis=axis,good=good,bad_union=union,records=records)

if __name__=='__main__':
    d=json.loads(Path(sys.argv[1]).read_text());m=IGS(d['n'],d['k'])
    with torch.no_grad():v,q,*_=m.geometry(torch.tensor(d['y']))
    out=centerline(v.numpy(),q.numpy(),m.faces,m.E.numpy(),m.uroot,m.sroot)
    print(json.dumps(out,indent=2))
```

## freeze_igs.py
1694 bytes,SHA256 f6cfb72f97b13706a21411ab4cf374491dfef58a2ed8ecc51bed817dc0bb8f03.

```python
"""Convert a frozen numerical IGS checkpoint into a fully literal rational input.
No reconstructed audit depends on NumPy or Torch after this conversion.
"""
import sys,json,math,hashlib
from pathlib import Path
from fractions import Fraction as F
import torch
from igs_scout import IGS

def freeze(path,identity,D=10**9):
    inp=json.loads(Path(path).read_text());m=IGS(inp['n'],inp['k']);y=torch.tensor(inp['y'])
    with torch.no_grad():v,q,slack,length,volume,H,c,aa,h=m.geometry(y)
    # geometry returns unnormalized aa and normalized h; recover the scale exactly
    # as evaluated in float64, then store every rounded rational coefficient.
    hh=m.G@aa;scale=hh[m.k+1].mean()/math.cos(math.pi/m.n);aa=aa/scale
    def r(x):
        a=F(round(float(x)*D),D);return [a.numerator,a.denominator]
    normal=[None]*m.n
    for j in range(m.west):
        normal[j]=[r(z) for z in m.normals[j]];normal[m.n-1-j]=[normal[j][0],[-normal[j][1][0],normal[j][1][1]]]
    normal[m.west]=[[-1,1],[0,1]]
    curv=[[r(z) for z in row] for row in aa[m.k:]]
    for j in range(m.west):curv[0][m.n-1-j]=curv[0][j]
    curv[0][m.west]=[0,1]
    data=dict(identity=identity,n=m.n,k=m.k,normals=normal,positive_curvatures=curv,metric=[r(torch.exp(y[-3])),r(torch.exp(y[-2])),r(y[-1])],source_checkpoint_sha256=hashlib.sha256(Path(path).read_bytes()).hexdigest(),rounding_denominator=D)
    text=(json.dumps(data,sort_keys=True,separators=(',',':'))+'\n').encode();dest=Path(identity+'_INPUT.json');dest.write_bytes(text)
    print('IGS_EXACT_INPUT',str(dest),len(text),hashlib.sha256(text).hexdigest())
if __name__=='__main__':freeze(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 10**9)
```

## igs5_11_log_s0.json
1777 bytes,SHA256 6db1e3a3349907826bb7932abddec7502d3e77ed942046cfb4217705cf307fbf. Save the whole single line plus terminal LF.

```json
{"diagnostic":{"C":468,"E":234,"F":119,"S":5,"U":13,"V":117,"centroid":[-7.65786385658739e-16,0.014000410935563591,-9.415621959902526e-16],"k":11,"maxPgap":0.0015272048972352348,"maxQgap":0.00039778198778472884,"minEdge":0.04693311943136909,"minH":0.6631447556524279,"minSlack":-1.1102230246251565e-16,"n":5,"rootPgap":0.008636530441390719,"rootQgap":0.0033905523201902404,"volume":1.9787253790915562},"extra":{"eps":0.0001,"input":null,"loss":1.3147411889682454e-05,"lr":0.006,"mode":"log","seed":0,"steps":4000},"identity":"igs5_11_log_s0","k":11,"n":5,"y":[-2.0036050741225635,-4.128372661490407,-2.744621935111887,-4.092839639931086,-2.102800038517069,-2.4667954039236277,-2.6520831824330346,-3.502159328633993,-4.841083917668205,-3.4132249438376436,-2.7902112460966144,-1.1733913345021485,-3.6391144065015224,-5.249828901024029,-4.864224567030569,-4.118139297580044,-0.2932856469836795,-2.260001268674956,-4.746198163866533,-4.546105208617998,-3.6205347612843264,-2.5541693316688554,-2.0495447764160253,-4.173708576420677,-4.444308488061279,-4.148553380511179,-2.978251262496397,-2.177810642765218,-2.7305047178591626,-2.8006134413389785,-4.001950041957487,-3.103189423441538,-2.133761752666614,-2.673965074616336,-2.421922354794421,-2.3944375547670633,-3.275386104995572,-2.1524730174133757,-0.13982128082984377,-2.6067492584971075,-2.237910155297543,-2.9495037879241166,-1.1969434364217242,-0.1593805298216241,-2.474163362339391,2.6778970769754955,1.9908301395317995,0.09100502759644631,0.6917239640721313,-0.6464845272714572,3.369553728581346,3.1081210170483327,4.186185256557353,2.3629937982115683,4.302299895876678,4.780830568701293,5.050501345636631,6.0090396027169355,5.048840279407746,5.949595041989737,-0.6845811883729492,0.02532730390811732,0.4339804733417298]}
```

## igs5_11_persist_s0.json
1789 bytes,SHA256 fbb0f5bdd5919b966ad43189625b4ddba152ffe7efd0f4b4c49db8b5e055f465.

```json
{"diagnostic":{"C":468,"E":234,"F":119,"S":21,"U":31,"V":117,"centroid":[-1.0588085622760312e-15,-0.05041418897688116,-5.294042811380156e-16],"k":11,"maxPgap":0.02322756229286374,"maxQgap":0.012739230626841014,"minEdge":0.24731969344369514,"minH":0.6539401493264987,"minSlack":-2.220446049250313e-16,"n":5,"rootPgap":0.022018450491050875,"rootQgap":0.004221039529942794,"volume":2.156099011400257},"extra":{"input":"igs5_11_log_s0.json","loss":0.6325509554449003,"lr":0.003,"mode":"squared","steps":1500,"weight":0.02},"identity":"igs5_11_persist_s0","k":11,"n":5,"y":[-1.1342715294395074,-3.671692436050613,-2.744621935111887,-3.636159412853563,-1.2334664982646322,-1.8847034472910955,-2.2233584464223326,-3.712423405837571,-4.3669859841928185,-2.1910206806721497,-3.215216874924809,-0.7588686440489297,-3.971622490233866,-4.781214132488934,-1.7832136984660163,-4.65193066498247,0.09268429162357555,-2.631310753651387,-4.227212193168492,-0.7103299384480252,-4.082010759844497,-2.1699245503815874,-2.409838050810067,-3.692156842152795,-4.257952477516751,-4.584827560699626,-2.573376866840729,-2.5293916147630244,-2.279452338238117,-3.0974680533523844,-4.434155381267439,-2.6971995614099784,-2.4802124744069807,-2.2427296980996383,-2.8738218400987123,-2.801333854905315,-2.903758565669675,-2.4986296236129037,0.26647117583581864,-3.1434770964782253,-2.5852285358647786,-2.636624173514589,-1.544749414332755,0.21491176803368964,-3.079564836467756,2.506616654228334,2.1922655258494186,-0.24031966851913508,1.0684778734376619,-1.3440518539014024,3.1954116269365156,3.3144759483073236,3.8437210223196097,2.7430662554136553,3.4141200505444167,4.607066829159256,5.258481591669853,5.666862632227867,5.430735345851325,5.056040326842501,-0.302692790621124,-0.22726669016248843,0.12045685974187703]}
```

## Reconstruction commands, environment and limits

Observed environment: CPython3.11.8,GCC12.2.0,NumPy1.24.0,Torch2.5.1+cpu; SciPy1.14.1 is installed but not imported by these four units. Float64,torch.set_num_threads(1),OPENBLAS_NUM_THREADS=1. Python-standard-library rational verifier separately removes these numerical dependencies from exact acceptance.

Original completed numerical searches:

```sh
OPENBLAS_NUM_THREADS=1 python igs_scout.py --n 5 --k 11 --steps 4000 --mode log --lr .006 --eps .0001 --seed 0 --output igs5_11_log_s0.json
OPENBLAS_NUM_THREADS=1 python igs_persistence.py --input igs5_11_log_s0.json --steps 1500 --mode squared --lr .003 --weight .02 --output igs5_11_persist_s0.json
```

The first unit uses NumPy default_rng(seed0) and all nondefault settings are above; the second begins at the complete literal first checkpoint. Floating library/platform differences may alter a reoptimized trajectory. Exact frozen inputs are authoritative endpoints, not an assumption of cross-platform bitwise optimization determinism. Restore the literal JSON checkpoints above before running endpoint reconstruction and verification:

```sh
OPENBLAS_NUM_THREADS=1 python igs_scout.py --input igs5_11_log_s0.json --diag
OPENBLAS_NUM_THREADS=1 python igs_persistence.py --input igs5_11_persist_s0.json --diag
OPENBLAS_NUM_THREADS=1 python igs_centerline.py igs5_11_log_s0.json
OPENBLAS_NUM_THREADS=1 python igs_centerline.py igs5_11_persist_s0.json
OPENBLAS_NUM_THREADS=1 python freeze_igs.py igs5_11_log_s0.json IGS5_LOG_C468_G9 1000000000
OPENBLAS_NUM_THREADS=1 python freeze_igs.py igs5_11_persist_s0.json IGS5_PERSIST_C468_G9 1000000000
python igs_exact.py IGS5_LOG_C468_G9_INPUT.json
python igs_exact.py IGS5_PERSIST_C468_G9_INPUT.json
```

The last two commands require the complete exact part1 source, [internal-source-reference], saved as igs_exact.py. Exact part2 stores both full rational inputs independently; use those if a different platform changes floating conversion.

Expected freeze outputs: IGS5_LOG_C468_G9_INPUT.json1802bytes,SHA b8e99d71dc20c9d963f8b14f8a7b5c3219d9927e4ed2a1c57c34c7624488e261; IGS5_PERSIST_C468_G9_INPUT.json1774bytes,SHA8585fe73fe558b4804acd3035a8f3224c0fb893eb13b5176654a3ee340cdb05c.
Expected exact final markers: IGS_EXACT_MASS_MECHANICS_AND_LINE_PASS twice; strict[5,13,16] and[21,31,50],weak[0,0,0] for both,IGS_EXACT_LINE_COVER True for both. Expected full exact audits: IGS5_LOG_C468_G9_AUDIT.json874229bytes,SHAac77be72252c96bf6bc8e2a9c3ccbb8bede7adf9776a34e509adedb61cc0c4ca; IGS5_PERSIST_C468_G9_AUDIT.json1219923bytes,SHAefd1a3ce7782c357ef2e6eca62e7ace7b37f7b53981b6c8ed5c7a0795f6f5771.

Scientific limits: a tiny all-pair logarithmic escape loss coexists with Q relative squared-radius depth.84267. Full-bar descent shrinks maximumP/Q depth to.19307/.38998 but proliferates exact roots. Sequential floating tie-breaks yield a top-P component of37 in the second numerical checkpoint; the exact simultaneous-event auditor gives18 vertices/24boundary edges, which is authoritative. Numerical centre-line intervals use tolerance1e-12 and a CLOSED bad-union; the exact proof separately checks strict inequalities and strict interval overlap. These searches do not exclude the family. A100-step debug checkpoint was only a software smoke test and is not a promoted mathematical endpoint. An earlier intended3000-step persistence process was interrupted by the container timeout; no missing trajectory is treated as a completed search. The completed1500-step run above was restarted from the literal first checkpoint.
