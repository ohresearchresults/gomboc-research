# material-9b2da50e764e

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J76 — two exact nonwinning nonlinear controls

The literal checkpoints below define two homogeneous convex bodies, not a claim about reproducibility of a floating optimizer. Both descend from literal R22-B7 (parent figure-0566, SHA1dd2a815454fdcdf5442f539f13181506b8ecd85c884a433f8061ea92c9f08be).

J76_QUADRATIC_FRAGMENTED_G10 has V75/E219/F146,C438, own(S,U,H)=(55,45,98), additional weak000,44 positive P bars and54 positive Q bars. Maximal depths are .023102789457120288 and .007400897636789993. Its much smaller large depths do not represent cancellation: the landscape fragmented severely.

J76_CAP_QUADRATIC_G10 has V75/E204/F131,C408, own(9,13,20), additional weak000,12 positive P bars and8 positive Q bars. Maximal depths are .09771043661350104 and .062076458956418376. The parent18-gon is restored exactly. Floating nomination with a relative1e-13 floor reported8P/7Q; this exact endpoint has12P/8Q and the additional positive bars are not discarded. The near-unchanged main depths and new roots are not progress to110.

These are finite controls of the selected quadratic experiments, not exclusions of all nonlinear deformations or all choices of objective. No new own110 or canonical record is claimed. They corroborate the earlier coupled-branch observation that a small sum or maximum of persistence depths can hide many genuine equilibria.

## Dependency and commands
Both complete source/data units below require the already stored exact source [internal-source-reference], J75_REFERENCE110_CAP233.py.txt,11412B,SHAe16788d0d477fef56c4a8ac979d2b201c9691d0f6ee302939f7699209a740b82. Save that source as J75_REFERENCE110_CAP233.py alongside these units. It supplies all75 parent rows, the true maximal supporting hull, volume integration and exact S/U/H predicates. No old optimizer, sandbox, or FULL76 is necessary.

Save code as controls76.py and the one-line JSON as J76_CHECKPOINTS.json, each with exactly one terminating LF. Executed environment CPython3.13.5,NumPy2.3.5,SciPy1.17.0. Run OPENBLAS_NUM_THREADS=1 python controls76.py. Input receipts: controls76.py3138B,SHA8ab70aa6f844fec5915dac5a993f4e90348b72e4f47f8fc5d117609a590c29cc; J76_CHECKPOINTS.json6731B,SHAb4b057bae30f95d97523a1d1b0dad5539922c88d3faea9aee63bdd93a1b27b66. Observed output J76_CONTROLS_EXACT.json85742B,SHA45dc3700fc6477e491ef48e0cd13952e81a77cfff5a633c14e291dc8ec73cd00; terminal J76_NONLINEAR_CONTROLS_EXACT_PASS_NO_110. Output includes exact volume, centroid, complete census and every positive rational bar without a numerical cutoff. A second positive-tetrahedron mass sum at the actual centroid matches; this is the coordinator's own executed engine, not independent verification by another copy.

## controls76.py
```python
"""Exact nonwinning controls nominated by J76 low-degree warp experiments.
Inputs are complete literal integer checkpoints in J76_CHECKPOINTS.json.
Requires J75_REFERENCE110_CAP233.py (immutable source [internal-source-reference]).
"""
from fractions import Fraction as F
from itertools import groupby
from pathlib import Path
import json,hashlib
import J75_REFERENCE110_CAP233 as m

def gate(u,v):
 A=m.dot(u,u);B=m.dot(u,v);C=m.dot(v,v);D=A+C-2*B
 if D==0 or B>=A:return A
 if B>=C:return C
 return (A*C-B*B)/D

def all_positive_bars(x,edges):
 edges=sorted({tuple(sorted(e)) for e in edges});birth=[m.dot(v,v) for v in x]
 weight={e:gate(x[e[0]],x[e[1]]) for e in edges};par=list(range(len(x)));peak=par.copy();out=[]
 def find(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 for level,ee in groupby(sorted(edges,key=lambda e:(-weight[e],e)),key=lambda e:weight[e]):
  adj={}
  for i,j in ee:
   a,b=find(i),find(j)
   if a!=b:adj.setdefault(a,set()).add(b);adj.setdefault(b,set()).add(a)
  unseen=set(adj);groups=[]
  while unseen:
   a=min(unseen);unseen.remove(a);cc={a};todo=[a]
   while todo:
    for b in adj[todo.pop()]:
     if b in unseen:unseen.remove(b);cc.add(b);todo.append(b)
   groups.append(sorted(cc))
  for cc in groups:
   elder=max(cc,key=lambda a:(birth[peak[a]],-peak[a]))
   for a in cc:
    if a!=elder and birth[peak[a]]>level:
     out.append({'peak':peak[a],'elder':peak[elder],'birth':birth[peak[a]],'death':level,'depth':(birth[peak[a]]-level)/birth[peak[a]]})
   for a in cc:par[a]=elder
 assert len({find(i) for i in range(len(x))})==1
 return sorted(out,key=lambda b:(-b['depth'],b['peak']))

def main():
 src=json.loads(Path('J76_CHECKPOINTS.json').read_text());reports=[]
 for obj in src['objects']:
  p=[tuple(F(v,obj['D']) for v in row) for row in obj['rows']]
  if obj['restore_parent_plane']:
   for i in m.PATCH:
    x,_,z=p[i];p[i]=(x,(-F(68526367,100000)-272*x-409*z)/1000,z)
  K=m.hull(p);V,M=m.mass(K);c=m.mul(M,1/V);census=m.census(K,c)
  vv,mm=m.mass(K,c,positive=True);assert (vv,mm)==(V,M)
  x=[m.sub(v,c) for v in K['points']]
  ns=[m.cross(m.sub(x[f[1]],x[f[0]]),m.sub(x[f[2]],x[f[0]])) for f in K['faces']]
  q=[m.mul(n,1/m.dot(n,x[f[0]])) for n,f in zip(ns,K['faces'])]
  P=all_positive_bars(x,K['edges']);Q=all_positive_bars(q,K['edge_faces'])
  if census['weak']==[0,0,0]:
   assert len(P)==census['strict'][1]-1 and len(Q)==census['strict'][0]-1
  report={'name':obj['name'],'VEF':[len(x),len(K['edges']),len(q)],'centroid':c,'volume':V,'census':census,'P_bars':P,'Q_bars':Q}
  reports.append(report)
  print('EXACT_CONTROL',obj['name'],report['VEF'],census['strict'],census['weak'],'P',len(P),max((float(b['depth']) for b in P),default=0),'Q',len(Q),max((float(b['depth']) for b in Q),default=0),flush=True)
 bb=(json.dumps(reports,sort_keys=True,separators=(',',':'),default=str)+'\n').encode();Path('J76_CONTROLS_EXACT.json').write_bytes(bb)
 print('RECEIPT',len(bb),hashlib.sha256(bb).hexdigest(),flush=True)
 assert all(r['census']['strict']!=[1,1,0] for r in reports)
 print('J76_NONLINEAR_CONTROLS_EXACT_PASS_NO_110',flush=True)
if __name__=='__main__':main()
```

## J76_CHECKPOINTS.json
```json
{"D_rule":"Round each decimal output coordinate times10^10 to nearest integer, ties to even; the literal rows, not the optimizer, define these exact bodies.","objects":[{"D":10000000000,"name":"J76_QUADRATIC_FRAGMENTED_G10","nomination_objective":0.09575136159510256,"nomination_path_label":"warp76_d2_08/best.json","nomination_z":[-0.044153473283149405,0.022994511080893964,-0.0338870325029024,0.006991227312746369,0.0010715699622553295,-0.0027861984790105926,-0.01903984657450114,0.009615168039135454,0.026052473057326733,0.0017903495972621507,0.022209156059043656,-0.05833600527895359,0.0816648559562913,0.007345968744201835,-0.06227863278422172,-0.04024697632849093,0.007153398498452101,0.006207108692854675],"restore_parent_plane":false,"rows":[[-11296723833,-3914656602,361842619],[-11349695277,-2927729503,-2042135381],[-10965797679,-2270077089,-3922353856],[-10176960919,-1767856580,-5687362614],[-9397053314,-6921715952,6529189318],[-9356619023,-1487674260,-6924872585],[-8516081072,-8098175165,8847087865],[-8369883271,-1323662837,-7986048763],[-7634188934,-1265481585,-8619051211],[-6427740883,-1295343516,-9347557906],[-6247840867,2518318954,-1250523952],[-6352271141,2260198175,293188536],[-5718688165,2306698049,1062161134],[-5198043607,-1427820286,-9838170754],[-5204120850,2287676059,1615448213],[-5372255322,3377382057,-1724907679],[-4334570043,2111476291,2458507220],[-4337680260,267545845,4275875405],[-4202553186,1796793860,2885342437],[-4190548274,1220029464,3468708398],[-4226347890,4367413441,-2022561529],[-4032435725,4143487399,-576459028],[-3430459973,-1729562214,-10269017603],[-3490147096,4110380158,517180046],[-3356536101,536530136,4137948332],[-3364465487,4662889723,-2901245876],[-2697451015,-1885919036,-10370800554],[-2616272434,632966314,4020922639],[-2951153859,-306703134,4605152314],[-2422193272,4838857224,-3429138950],[-1964927942,-2072309297,-10398061949],[-2328291817,4395450575,860916051],[-2004522695,3891484853,1523645537],[-1552754297,3690535471,1822376285],[-1213970228,-2294144180,-10350023322],[-1184068165,4683042722,-4180187106],[-987256253,3682212919,1897792889],[-468808407,-2546300522,-10223185765],[-406922200,4563383909,-4266417124],[-36401765,3919285683,1736456347],[15528764,816875344,3391110439],[285206907,-2740749105,-10025464476],[210246514,592215846,3399136272],[809475876,760439657,3142701730],[1026727347,-2924181490,-9754778263],[933352809,1665058520,2819375260],[1319824130,4243286776,1468288025],[2528879918,4450894959,-3176848621],[1749649274,-3094888589,-9413858287],[3068556926,-1750692137,-8707502005],[2448232797,-3252382913,-9005679668],[3997534054,4076749012,-1067891870],[3116966420,-3396820485,-8533319347],[3044401882,4793546682,888199740],[3290400332,-4490986631,-7919429517],[3738863752,-3551687708,-8001516388],[3778946454,4117589114,1069559823],[4271509218,3554387479,1137029884],[4315736493,-3690655270,-7418398180],[4114561827,-5249063071,-6592916052],[4552957819,3217690597,1085945322],[4814768192,2872082632,1022214742],[4840983778,-3817073251,-6790241288],[5053951615,2522812940,947171883],[5202724186,-4829097827,-5231737693],[5393702609,-892456970,-5799194810],[5563751188,1786144002,628498010],[5983397316,1009461600,246920152],[5783949468,-4293076648,-4246905694],[6306294542,200097815,-202480860],[6196860246,-3654358313,-3371966772],[6510962085,-589889202,-689177411],[6611321290,-1382795894,-1240853689],[6466608932,-2932339995,-2572399406],[6600068580,-2168376418,-1865461059]]},{"D":10000000000,"name":"J76_CAP_QUADRATIC_G10","nomination_objective":0.561740373380519,"nomination_path_label":"plane76_09/best.json","nomination_z":[-6.785851151083582e-06,6.9862764876608605e-06,5.612046046980959e-06,-1.7151009567650714e-05,-1.0057371574013561e-05,-4.322633576706137e-06,-7.780139286838409e-06,1.1746829927982168e-06,1.4624749614297985e-05,-2.9966175981284494e-05,-1.8713886938389095e-05,-2.8468799810575326e-07,8.449122289393753e-06,6.665660824947803e-06,8.673501130472454e-06],"restore_parent_plane":true,"rows":[[-11439352320,-3850047647,266295300],[-11436501496,-2891672146,-2078816985],[-11012390015,-2268291080,-3885025761],[-10198322614,-1802527493,-5565196714],[-9510349561,-6927906147,6508764126],[-9366781249,-1548307884,-6739766054],[-8478674469,-8202322580,8938594951],[-8378881257,-1404171338,-7749167872],[-7644783862,-1356116125,-8354863972],[-6450154359,-1391949040,-9061725365],[-6145894722,2597790407,-1494933347],[-6241992386,2345578407,36177835],[-5623261691,2386233163,828879522],[-5235326416,-1521596075,-9552645086],[-5121284622,2359328909,1410963356],[-5260945467,3446637620,-1971227126],[-4274006701,2164885586,2318977085],[-4290395146,293710834,4244098519],[-4147898744,1843435058,2773716492],[-4141067888,1258436533,3392058941],[-4113523536,4422673945,-2267680823],[-3937485686,4202479532,-812239692],[-3481033325,-1810023931,-10014111748],[-3329776478,549591108,4149470130],[-3408973422,4159685088,315792005],[-3278647523,4707386099,-3115739365],[-2748904137,-1958529478,-10137910262],[-2607704166,636175385,4067069219],[-2939619121,-310420936,4675119595],[-2370799143,4875225226,-3611566541],[-2016499697,-2134849441,-10193885920],[-2280375774,4424851403,718216046],[-1977913421,3912874071,1432925577],[-1542663427,3702081682,1773361193],[-1264305958,-2344349401,-10181897502],[-1187049608,4712999532,-4311103293],[-993384423,3683152652,1885126294],[-516153608,-2582477220,-10097226646],[-443298468,4592160906,-4372144801],[-65798854,3904274316,1768348859],[-29896655,788216856,3545553384],[245784400,-2761602183,-9946830770],[160767912,561115303,3564596037],[752431513,724002400,3323153935],[997818218,-2929109513,-9726315704],[876487444,1627986313,2986528270],[1262289813,4204547802,1562558770],[2405355091,4462344118,-3190469007],[1733549862,-3083904828,-9436579400],[3076882128,-1717497583,-8776969096],[2446898294,-3226122009,-9078747840],[3863168550,4048235914,-959893855],[3132007421,-3356530913,-8654085023],[2958276328,4725565292,1046949980],[3302493889,-4439618314,-8096080010],[3771237992,-3499264262,-8165843098],[3689046704,4039426379,1282517609],[4185460433,3471806920,1378196174],[4366429786,-3628526067,-7620142921],[4155973041,-5179565467,-6854513203],[4469647113,3135421049,1334811690],[4736015607,2791006407,1274864752],[4910570499,-3748109135,-7021942595],[4981320892,2443767165,1199755224],[5287388150,-4753668046,-5513288084],[5388254589,-833832239,-5916400562],[5506918851,1716171940,863432543],[5948583500,952535591,446799001],[5881236413,-4223893338,-4499587524],[6297954608,159793040,-53833241],[6294629432,-3598078807,-3572388289],[6529763106,-611824649,-601651595],[6656755911,-1384740238,-1223264547],[6554164089,-2893695928,-2704558951],[6669276924,-2149698696,-1922773014]]}]}
```
