# figure-0454

Historical AI scientific report · saved 2026-09-21 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Bright Raven 76 continuation — finite whole-P interface cut

## Outcome

No strict own110/additional-weak000 body was found. The strongest new durable descendant is **`BR76_A_WHOLEP_CUT31_M61_M95_G3`**, obtained from the literal authoritative parent `BR76_DUAL5_A100_HG3` by adding one exact physical halfspace row `[31,-61,-95]` at denominator 1000. The parent is exactly the A body from `figure-0453`: V114/E171/F59/C342, strict121/weak000/zero000, sole stable face, two unstable vertices and one complete 31/31 physical basin. :contentReference[oaicite:0]{index=0}

The new body is **V116/E174/F60/C348, strict121/weak000/primitivezero000**, with S=`[0]`, U=`[7,39]`, H=`[[78,80]]`, `Qbars=[]`, and exactly one physical P bar. It therefore remains a nonwinner, but it is a genuine finite actual-material change beyond A's certified local neighborhood and materially restructures the entire physical basin rather than merely improving one root score.

## Exact finite change and local-barrier crossing

Parent input SHA-256: `790be9210f8f83698d14b56044ba2972fdf3e3e1a8ef12af0b913ed69a6de65f`.

Child definition is exactly the 59 literal parent H rows, unchanged, plus the 60th row

`[31,-61,-95]`

with common denominator `1000`, i.e. the added halfspace is `31x-61y-95z <= 1000`.

The row is active. True incidence changes from V114/E171/F59 to V116/E174/F60; no combinatorial count is inferred from a triangulation. Actual homogeneous volume and centroid are recomputed from the changed filled solid. Exact child input is 959 bytes, SHA-256 `acce43f39b046f6b088bb20289b4b399cb146ddc141cde727317dc468e6310d5`; exact report is 27250 bytes, SHA-256 `fc137e6a86ef71e4f327f3c4c9b1191853727a32dfcac8379df44d23730d1677`.

Exact volume is

`49882526271751199705825991725630259353509045226677157955848165068837934647711033254495983538379156051223162953571902200884435888983353378537576383991172793059289262118793594937883434450271475850379355220708266468447317606479886756007351894718342547108712439914457831325845407132646062092404491928045396581256043696731673201579432843686777978649559396651238948078923329963079877795417582353913225641632376093590084246917027017978787078978407127402056781415965906473750/567086003380000172678193644172750354373876573894226359511975316004186660718423467797274147707578459763010729627244011646478359002950655357953361611593480229861368542780828192674001016681885304439805648349169577940587096428134643083719987871080334587107626167382368765201025324191088219032987694387895226109437553101565208379737400868251660576799558158286061762827401245827503641099434480476893524844276238192757616475454647167851202769597129333250392050139711038113`

≈ `87.96289447180251`.

The exact centroid is emitted verbatim in the byte-pinned report and certificate by the recovery capsule below; numerically it is approximately

`(0.0028030051201756766, 0.012405840995052299, 0.01158957156994503)`.

This is the actual uniformly-filled volume centroid, not a free recentering.

More strongly, using the new plane normal `n=(31,-61,-95)`, exact support arithmetic gives

`h_A(n)-h_child(n) > (3/5)*||n||`.

Hence `d_H(A_centered, child_centered) > 3/5`, which is far beyond A's certified `15719/100000` physical-persistence radius. The recovery script checks this by exact squared rational inequality. Thus the construction genuinely crosses the local obstruction described for A. :contentReference[oaicite:1]{index=1}

## Full mechanics and whole-basin evidence

Exact strict/additional-weak census at the child's own centroid:

- strict `(S,U,H)=(1,2,1)`;
- additional weak `(0,0,0)`;
- primitive zero counters `(0,0,0)`;
- stable face `[0]`;
- unstable vertices `[7,39]`;
- saddle edge `[[78,80]]`;
- 228 positive centered tetrahedra in the exact mass identity;
- `Qbars=[]` exactly.

The single P bar is peak `7` → elder `39`, dying on true edge `[78,80]`. Its complete strict-upper component is

`[0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,18,20,21,24,30,32,33,43,44,46,47,48,49,52,57,72,78]`.

Its complete 31-edge cut is

`[[1,17],[1,38],[3,11],[5,35],[6,22],[8,11],[9,19],[10,19],[12,23],[14,114],[15,22],[18,28],[20,27],[21,25],[24,50],[25,32],[27,43],[29,46],[30,42],[31,47],[33,34],[33,59],[36,57],[44,70],[48,65],[49,51],[49,56],[57,79],[72,111],[78,80],[78,105]]`.

An attaining path at the death level is

`[7,4,3,0,2,5,6,15,20,43,46,47,52,72,78,80,79,40,38,39]`.

Thus the parent packet is not simply relabeled: roots change `3/37 -> 7/39`, the death edge changes `76-78 -> 78-80`, V/F/E change, and the strict-upper component grows `31 -> 33` while the cut remains 31 edges. The complete physical radial relative bar `(birth-death)/R^2` is approximately `0.5236152701894085`, versus A's approximately `0.608565442002`, a reduction of about **13.96%**. This is a whole-bar comparison, not a local hinge score. It is still a deep basin, so no closeness-to-own110 claim is made.

## Finite construction evidence and interpretation

A bounded numerical one-cut scout nominated this exact grid row while rebuilding the changed halfspace body and actual volume centroid for each trial. The relevant finite window sampled 12,000 tangent-perturbed cut directions around the unwanted physical root using NumPy RNG seed `7721`, tangent amplitudes from `[0.05,0.1,0.2,0.35,0.55,0.8,1.1,1.5,2.0,2.8]`, and radial cut fractions uniformly in `[0.55,0.99]`; 11,506 distinct rounded grid-1000 rows were visited, with 1,175 numerical S1/U2/E<=310 cases. No numerical S1/U1 was found in that finite window. This is finite nomination evidence only, not an exclusion.

The useful new mechanism is **large finite physical support cutting while preserving the sole stable chamber**. A single active cut already crosses the exact Hausdorff barrier and changes the entire 31/31 basin interface without rebirthing a polar/stable basin. However it only transfers/restructures the second physical root rather than eliminating it. Further local cuts tested numerically often retained S1/U2, so the next useful move should not repeat infinitesimal clipping; it should combine multiple interface cuts or retained-support motion with actual-mass compensation and permit root exchange.

## Most useful continuation

Use this child as a material exact checkpoint when studying finite support replacement, but A remains the cleaner high-headroom seed if a larger coordinated mechanism is available. The child still has only F60 and E174, leaving 45 support slots under the sufficient `F<=105 => E<=309` ceiling and 136 raw edge slots below E310.

A promising next operation is to act simultaneously on several carriers of the 33-vertex strict-upper component, especially across multiple cut exits rather than the death edge alone, while keeping the existing sole stable face or recovering S1 afterward. The physical root identity should be allowed to change. Every promoted successor must rebuild the actual homogeneous mass and whole P/Q barcode; the present finite single/pair/multicut failures do not exclude such a construction.

## Durable exact recovery capsule

Dependency is exactly the immutable parent `figure-0453`, SHA `ebd4b95a60285b9204b5be5399a7931f595828518ecf16e8ef88d2e91dc3bb8f`. Unpack its source-only bundle so that `exact_hpoly.py` (8946 bytes, SHA `54e4c8f2f6f1b45955f42b6518c4a1586d94cccc8f4dfe3ae866cf5b22f3aca6`) and `EXACT_OUT/BR76_DUAL5_A100_HG3.json` are present. Save the complete patch below as `RECOVER_BR76_WHOLEP_CUT.py`.

Patch source is 3823 bytes, SHA-256 `4b5d96454614070366af2b98469124b2060a3a1fc482b90aeface8a6569a88c4`.

Run:

`python -B -S RECOVER_BR76_WHOLEP_CUT.py BR76_WHOLEP_CUT_REPLAY BR76_PACKET_BUNDLE`

Observed terminal output includes:

`BR76_WHOLEP_CUT_EXACT121_FULL_BASIN_CROSSES_PARENT_RADIUS_PASS`

and receipts

- input: 959 bytes, SHA `acce43f39b046f6b088bb20289b4b399cb146ddc141cde727317dc468e6310d5`;
- report: 27250 bytes, SHA `fc137e6a86ef71e4f327f3c4c9b1191853727a32dfcac8379df44d23730d1677`;
- certificate: 10881 bytes, SHA `4daebf0864aa636a8c6c3af0aa1aaf1b5f107c614a2e17463f53c49f36687dcc`.

```python
#!/usr/bin/env python3
"""Exact continuation from BR76_DUAL5_A100_HG3 by one finite physical cut.
Requires parent figure-0453 bundle unpacked so that
exact_hpoly.py and EXACT_OUT/BR76_DUAL5_A100_HG3.json are beside this script
(or pass parent directory as argv[2]). CPython 3.13.5 stdlib only.
"""
import hashlib,json,math,sys
from fractions import Fraction as F
from pathlib import Path
PARENT_INPUT_SHA='790be9210f8f83698d14b56044ba2972fdf3e3e1a8ef12af0b913ed69a6de65f'
HPOLY_SHA='54e4c8f2f6f1b45955f42b6518c4a1586d94cccc8f4dfe3ae866cf5b22f3aca6'
CHILD_INPUT_SHA='acce43f39b046f6b088bb20289b4b399cb146ddc141cde727317dc468e6310d5'
CHILD_REPORT_SHA='fc137e6a86ef71e4f327f3c4c9b1191853727a32dfcac8379df44d23730d1677'
NEW_ROW=[31,-61,-95]
COMP=[0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,18,20,21,24,30,32,33,43,44,46,47,48,49,52,57,72,78]
CUT=[[1,17],[1,38],[3,11],[5,35],[6,22],[8,11],[9,19],[10,19],[12,23],[14,114],[15,22],[18,28],[20,27],[21,25],[24,50],[25,32],[27,43],[29,46],[30,42],[31,47],[33,34],[33,59],[36,57],[44,70],[48,65],[49,51],[49,56],[57,79],[72,111],[78,80],[78,105]]
PATH=[7,4,3,0,2,5,6,15,20,43,46,47,52,72,78,80,79,40,38,39]
def sha(b):return hashlib.sha256(b).hexdigest()
def main(out='BR76_WHOLEP_CUT_REPLAY',parent='.'):
    parent=Path(parent); out=Path(out);out.mkdir(parents=True,exist_ok=True)
    hp=parent/'exact_hpoly.py'; pin=parent/'EXACT_OUT'/'BR76_DUAL5_A100_HG3.json'
    assert sha(hp.read_bytes())==HPOLY_SHA
    assert sha(pin.read_bytes())==PARENT_INPUT_SHA
    sys.path.insert(0,str(parent)); from exact_hpoly import audit,dot
    p=json.loads(pin.read_text())
    child={'denominator':1000,'name':'BR76_A_WHOLEP_CUT31_M61_M95_G3','rows':p['rows']+[NEW_ROW]}
    ib=json.dumps(child,sort_keys=True,separators=(',',':')).encode();assert len(ib)==959 and sha(ib)==CHILD_INPUT_SHA
    (out/(child['name']+'.json')).write_bytes(ib)
    r=audit(child);ob=json.dumps(r,sort_keys=True,separators=(',',':')).encode();assert len(ob)==27250 and sha(ob)==CHILD_REPORT_SHA
    (out/(child['name']+'_REPORT.json')).write_bytes(ob)
    assert [r[x] for x in ['V','E','F','C']]==[116,174,60,348]
    assert r['strict']==[1,2,1] and r['weak']==[0,0,0] and r['primitive_zero']==[0,0,0]
    assert r['stable']==[0] and r['unstable']==[7,39] and r['saddles']==[[78,80]]
    assert len(r['Pbars'])==1 and r['Qbars']==[]
    bg=r['Pbar_geometry'][0]; assert bg['component']==COMP and bg['cut']==CUT and bg['path']==PATH
    # Exact proof this is outside A's certified d_H <= 15719/100000 neighborhood.
    pr=json.loads((parent/'EXACT_OUT'/'BR76_DUAL5_A100_HG3_REPORT.json').read_text())
    ca=tuple(map(F,pr['centroid'])); cc=tuple(map(F,r['centroid'])); n=tuple(NEW_ROW)
    Vp=[tuple(map(F,v)) for v in pr['vertices']]
    hp0=max(dot(n,v) for v in Vp)-dot(n,ca)
    hc0=F(1000)-dot(n,cc)
    gap=hp0-hc0; n2=sum(x*x for x in n)
    assert gap>0 and gap*gap>F(9,25)*n2 # support distance > 3/5 > 15719/100000
    cV=[tuple(map(F,v)) for v in r['vertices']]; P=[tuple(v[i]-cc[i] for i in range(3)) for v in cV]
    R2=max(dot(x,x) for x in P); rel=F(r['Pbars'][0]['gap'])/R2
    cert={'marker':'BR76_WHOLEP_CUT_EXACT121_FULL_BASIN_CROSSES_PARENT_RADIUS_PASS','parent':'BR76_DUAL5_A100_HG3','new_row':NEW_ROW,'V_E_F_C':[116,174,60,348],'strict':[1,2,1],'weak':[0,0,0],'component':COMP,'cut':CUT,'path':PATH,'support_displacement_gt':'3/5','relative_Pbar':str(rel),'volume':r['volume'],'centroid':r['centroid']}
    cb=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();(out/'BR76_WHOLEP_CUT_CERTIFICATE.json').write_bytes(cb)
    print(cert['marker']);print('INPUT',len(ib),sha(ib));print('REPORT',len(ob),sha(ob));print('CERT',len(cb),sha(cb))
if __name__=='__main__':main(sys.argv[1] if len(sys.argv)>1 else 'BR76_WHOLEP_CUT_REPLAY',sys.argv[2] if len(sys.argv)>2 else '.')
```

## Evidence tier and limits

This descendant has one exhaustive exact rational H-polytope maximal-complex/mechanics audit, with the auditor's raw and centered exact mass identities. It is not independently double-audited. The numerical cut search only nominated the rational row; every promoted count, equilibrium classification, mass value and basin claim above comes from the exact replay. No single-cut, multicut, affine, or broader family exclusion is claimed. Canonical accepted own110 remains C622.
