# figure-0457

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Steady Finch 43 — exact handoff: whole tangent-axis closure for the surviving C616 entrance

## Disposition

No new own110/additionalweak000 body is promoted. The authoritative entrance remains **QC52_SURVIVING_ROOT124_G9_F8B57E0F**, the source-complete f8b57e0f surviving realization, not the unrecovered historical 8adb object. It is V174/E308/F136, C616, own121/additionalweak000, with S input/face 3, U raw 94/124 and H124–134; its complete physical bar and one-cap exclusion are the inherited certified data.

The new exact result closes a previously open finite window: **every positive parameter of the specific tangent-axis affine family used by the QC52 gate-opening countercontrol is excluded from own110/additionalweak000.** The earlier parent proved only that sufficiently large tangent stretch opens L and Psi while eventually forcing two strict U; it explicitly left the finite initial interval and the full affine orbit open. This handoff proves the entire one-dimensional axis, including compression, by an exhaustive exact root-interval sweep. It is a scoped obstruction, not a full-affine or changed-contact exclusion.

## Exact parent replay actually used

I reconstructed the literal 22-file parent capsule and cold-replayed the surviving G9 case. Observed markers were:

- `QC52_SURVIVING_SOURCE_RECOVERY_PASS 22`
- `QC52_SURVIVING_EXACT_A_PASS ROOT124_G9`
- `QC52_SURVIVING_AB_MASS_BASIN_PASS ROOT124_G9`
- `QC52_SURVIVING_TRANSPORT_PASS`
- `QC52_SURVIVING_CONTROLS_PASS`
- `QC52_SURVIVING_REPLAY_PASS ROOT124_G9`

The exact `A.json` consumed by the new proof is **230639 bytes**, SHA-256 **bf713a4201231250cfb98d45cc35f47f27afee73a7938f700ce51359ef3b19f5**. It reproduces V174/E308/F136, strict121, weak000, centered-denominator bit length40995, all308 true edges and all136 maximal faces. The inherited physical elder bar is birth² `[383520428998,383520428999]/10^12`, death `[383260792369,383260792370]/10^12`, delta `[259636629,259636630]/10^12`, normalized delta/V^(2/3) `[418537478,418537479]/10^12`; strict death component `{124}`, complete cut `109–124,120–124,124–134`, and attaining path `[124,134,144,145,147,148,149,150,151,153,155,161,162,164,169,167,165,163,160,157,154,152,100,94]`. The same actual filled centroid is used for the polar.

## New theorem: no positive lambda on the QC52 tangent axis can be own110/weak000

The exact primitive tangent direction selected from stable face3 is

`v = (19228187656214963, 0, -7024844512164006)`.

The verifier independently checks `n_3·v=0`, `0<(w-g)·v<(z-g)·v` for `w=120,z=134`, the source root/star identities, and the exact parent hash. Put `P=vv^T/(v·v)` and `lambda=s^2>0`. Positive scalar factors do not affect equilibrium signs, so the physical affine metric is

`G_lambda = I + (lambda-1)P`.

For every directed true physical edge `i→j`, with centered `y_i` and `d=y_j-y_i`,

`E_ij(lambda)=y_i·d + (lambda-1)(y_i·v)(d·v)/(v·v)`

is affine in `lambda`. For each directed true dual edge in the same-physical-centroid polar, multiplying the inverse-metric score by positive `lambda` gives

`lambda F_ij(lambda)=lambda q_i·d + (1-lambda)(q_i·v)(d·v)/(v·v)`,

again affine in `lambda`. Therefore the strict-U parameter set of every physical vertex and every polar vertex (equivalently every primal stable facet) is one open interval in `lambda>0`. The program below constructs these intervals using only integer arithmetic, sorts every exact endpoint, and exhaustively sweeps all root-count chambers and every boundary.

Observed exact proof output:

```text
QC52_TANGENT_ALL_POSITIVE_LAMBDA_EXCLUDES_OWN110_PASS
parent 174 308 136 [1, 2, 1] [0, 0, 0]
centroid_common_denominator_bits 40995
strict_root_intervals 149 113 event_groups 504
minimum_open_strict_root_sum 3
unique_minimum_interval_lambda_floor15 (999999991717228, 999999991717229, 1000000000000000) (1000000016662957, 1000000016662958, 1000000000000000)
unique_minimum_endpoint_sha256 dc211f9112ad0487563301d11e5b8906585aeb8fb485713087a52f52601a8d6e b1665e306fc06344d574a23568b087ecb2d2ade2c3665d7f31150bfbe7b8d60d
boundary_events ('end', 'Q', 26) ('start', 'Q', 29)
unique_minimum_roots_U (94, 124) S (3,)
key_root_intervals_floor12 U94 (None, (44394943855421, 44394943855422, 1000000000000)) U124 ((882695671000, 882695671001, 1000000000000), (1062443887500, 1062443887501, 1000000000000)) S3 (None, None) S26 ((453550455914, 453550455915, 1000000000000), (999999991717, 999999991718, 1000000000000)) S29 ((1000000016662, 1000000016663, 1000000000000), (1158099819684, 1158099819685, 1000000000000))
open_strict11_intervals 0 endpoint_strict11_weakfree 0
```

The exact endpoints themselves are about 41.5k-bit rationals; the program reconstructs them. Their canonical `num/den` strings hash to the two SHA-256 values above, so decimals are not substituted for the proof.

### Geometric meaning

The unique open chamber with globally minimal strict-root total has exactly U94,U124 and S3, so the minimum is three strict roots. Its lambda endpoints lie in

- lower `[0.999999991717228,0.999999991717229)`;
- upper `[1.000000016662957,1.000000016662958)`.

At the lower boundary polar root/facet26 ends and is weak at the event; at the upper boundary polar root/facet29 starts and is weak at the event. Stable face3 is strict for every `lambda>0`. U124, however, remains strict throughout the much wider exact interval whose endpoints lie in `[0.882695671000,0.882695671001)` and `[1.062443887500,1.062443887501)`. Thus enough motion along this axis to eliminate U124 necessarily encounters an additional stable root long before U124 can disappear. The exhaustive 504-event sweep proves that going still farther never reaches another strict1/1 chamber.

At an endpoint of a strict-root interval, the interval owner has all incident radial derivatives nonpositive and at least one zero. Hence an isolated parameter with strict(S,U)=(1,1) cannot evade the open-chamber sweep without producing an additional weak equilibrium. The verifier explicitly establishes `endpoint_strict11_weakfree 0`. Therefore **for every real lambda>0**, this tangent-axis affine image fails own110/additionalweak000.

The actual mass treatment is exact: an invertible linear image sends the homogeneous filled centroid to `A_s g`, and that same physical center is used for the polar. Incidence is unchanged, so each member has true V174/E308/F136, E308, C616.

## Construction consequence

The parent countercontrol showed that favorable local L/Psi gates can coexist with a worsening global physical basin. The new sweep closes the remaining loophole: **there is no useful finite parameter window anywhere on this exact tangent axis.** Near identity the immediate obstruction is polar: face26 is stable just below the tiny S1 chamber and face29 becomes stable just above it, while physical U124 requires order-10^-1 lambda motion to disappear.

This does not exclude a second tangent direction, general SPD/affine motion, projective motion, a changed 124 star, changed 120 exits, stable20-gon motion, support replacement, multiple cuts, or another incidence/material architecture.

## Other work attempted, not promoted

Finite full-SPD affine and projective numerical searches and direct free-contact/generator-chart motion produced no whole-feature strict11 candidate. These are finite negative experiments only and are not used as exclusions.

Exact one-auditor support-deletion scouts also produced large root counts: delete3 → V175/E308/F135 strict38/72/108; delete44 →173/306/135 strict72/64/134; delete72 →173/306/135 strict70/61/129; delete99 →172/305/135 strict60/45/103; delete73 →173/306/135 strict60/51/109; delete15 →174/307/135 strict80/41/119; delete75 →174/307/135 strict82/53/133. They reported weak000 in the primary exact auditor but were not independently B-audited or given complete basin certificates, so they are not promoted bodies or family exclusions.

## Most useful continuation

Do not spend another direction optimizing `s` on this tangent axis. Instead alter the coefficients responsible for flanking polar roots26/29 while simultaneously moving the U124 basin, or deliberately leave the retained-star hypotheses. The two-edge headroom E308→E310 remains available. A high-value finite move is a coupled contact/material change involving the stable20-gon and the 124/120/134 neighborhood, or a changed 120 exit/root identity, followed by complete actual-centroid physical and polar basin reconstruction. Temporary extra roots during discovery are acceptable; the exact endpoint alone must return to strict110/weak000.

For any successor retain the parent's whole physical component/cut as a global regression target rather than L/Psi alone, and rebuild the maximal hull after every incidence change.

## Durable exact recovery capsule

Exact parent/checkpoint: `figure-0434`, SHA-256 `037b2078e4f89986594472b0f6e0df78ecf3cb43bbfb82dee2eea017099c529f`, case `QC52_SURVIVING_ROOT124_G9_F8B57E0F`.

Reconstruct its literal 22-file capsule and A report:

```sh
python -B -S QC52_SURVIVING_RECOVER.py QC52_SURVIVING
python -B -S QC52_SURVIVING/RECONCILE_REPLAY.py --case ROOT124_G9 --out ROOT124_PROOF
```

Required checkpoint: `ROOT124_PROOF/ROOT124_G9/A.json`, 230639 bytes, SHA-256 `bf713a4201231250cfb98d45cc35f47f27afee73a7938f700ce51359ef3b19f5`.

Save the following complete source as `QC52_TANGENT_ALL_LAMBDA.py`. It is 8477 bytes, SHA-256 `e328007a42b128fcc665a489f08683bbee57e00b2d6ecdd90693ea0d87f7ecdc`.

Run:

```sh
python -B -S QC52_TANGENT_ALL_LAMBDA.py ROOT124_PROOF/ROOT124_G9/A.json
```

Expected terminal marker: `QC52_TANGENT_ALL_POSITIVE_LAMBDA_EXCLUDES_OWN110_PASS`.

Observed environment: CPython3.13.5, standard library only, assertions enabled. No NumPy/SciPy, randomness, floating-point comparison or optimizer is used by the exact proof.

```python
"""Exact all-parameter exclusion for the QC52 tangent-axis affine family.
Input: A.json from QC52_SURVIVING_ROOT124_G9_F8B57E0F.
Proves that for every lambda=s^2>0, the affine metric
G_lambda = I + (lambda-1) vv^T/(v.v) cannot have strict (S,U)=(1,1)
with additional-weak=000. Uses only integer sign arithmetic on the true
primal and dual edge graphs; no floating point is used for the proof.
"""
import json,sys,math,hashlib
from functools import cmp_to_key
from pathlib import Path
sys.set_int_max_str_digits(0)
VAX=(19228187656214963,0,-7024844512164006)
EXPECTED_PARENT_A_BYTES=230639
EXPECTED_PARENT_A_SHA='bf713a4201231250cfb98d45cc35f47f27afee73a7938f700ce51359ef3b19f5'

def parse_rat(s):
 s=str(s)
 if '/' in s:
  a,b=s.split('/');return int(a),int(b)
 return int(s),1

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def ratcmp(x,y):
 return (x[0]*y[1]>y[0]*x[1])-(x[0]*y[1]<y[0]*x[1])
def rateq(x,y):return x[0]*y[1]==y[0]*x[1]
def ratlt(x,y):return x[0]*y[1]<y[0]*x[1]
def ratstr(x):return f'{x[0]}/{x[1]}'

def read_parent(path):
 raw=Path(path).read_bytes()
 assert len(raw)==EXPECTED_PARENT_A_BYTES and hashlib.sha256(raw).hexdigest()==EXPECTED_PARENT_A_SHA
 A=json.loads(raw);assert [A['V'],A['E'],A['F']]==[174,308,136] and A['counts']==[1,2,1] and A['weak']==[0,0,0]
 return A

def build(A):
 v=VAX;vv=dot(v,v)
 cs=[parse_rat(s) for s in A['raw_centroid']]
 C=math.lcm(*(b for _,b in cs));M=[a*(C//b) for a,b in cs]
 VA=[]
 for row in A['raw_vertices']:
  rr=[parse_rat(s) for s in row];b=math.lcm(*(q for _,q in rr));a=[p*(b//q) for p,q in rr];VA.append((a,b))
 edges=[tuple(e) for e in A['edges']];faces=A['faces']
 assert A['stable_face_ids']==[3] and A['unstable_vertices']==[94,124] and A['saddle_edges']==[[124,134]]
 ef={}
 for fi,f in enumerate(faces):
  for i,j in zip(f,f[1:]+f[:1]):ef.setdefault(tuple(sorted((i,j))),[]).append(fi)
 assert set(ef)==set(edges) and all(len(z)==2 for z in ef.values())
 dual=sorted(tuple(sorted(z)) for z in ef.values());assert len(dual)==308
 N=[list(map(int,n)) for n in A['normals']];H=list(map(int,A['offsets']))
 assert dot(N[3],v)==0 and {120,124,134}.issubset(set(faces[3]))
 assert tuple(sorted((120,124))) in set(edges) and tuple(sorted((124,134))) in set(edges)
 def cv(i):
  ai,bi=VA[i];return [C*ai[k]-bi*M[k] for k in range(3)],bi
 zw,bw=cv(120);zz,bz=cv(134);aw=dot(zw,v);az=dot(zz,v)
 assert aw>0 and az>0 and aw*bz<az*bw
 S=[H[i]*C-dot(N[i],M) for i in range(len(N))];assert min(S)>0
 Pc={}
 for i,j in edges:
  for ii,jj in ((i,j),(j,i)):
   ai,bi=VA[ii];aj,bj=VA[jj]
   z=[C*ai[k]-bi*M[k] for k in range(3)]
   e=[bi*aj[k]-bj*ai[k] for k in range(3)]
   aa=dot(z,e);bb=dot(z,v)*dot(e,v)
   Pc[ii,jj]=(aa*vv-bb,bb)
 Qc={}
 for i,j in dual:
  for ii,jj in ((i,j),(j,i)):
   e=[S[ii]*N[jj][k]-S[jj]*N[ii][k] for k in range(3)]
   aa=dot(N[ii],e);bb=dot(N[ii],v)*dot(e,v)
   Qc[ii,jj]=(bb,aa*vv-bb)
 Pa=[[] for _ in VA]
 for i,j in edges:Pa[i].append(j);Pa[j].append(i)
 Qa=[[] for _ in N]
 for i,j in dual:Qa[i].append(j);Qa[j].append(i)
 return Pc,Qc,Pa,Qa,C

def root_interval(i,adj,coef):
 lo=None;hi=None
 for j in adj[i]:
  a,b=coef[i,j]
  if b==0:
   if a>=0:return None
   continue
  n,d=-a,b
  if d<0:n,d=-n,-d
  if n<=0:
   if b>0:return None
   continue
  r=(n,d)
  if b>0:
   if hi is None or ratlt(r,hi):hi=r
  else:
   if lo is None or ratlt(lo,r):lo=r
 if lo is not None and hi is not None and not ratlt(lo,hi):return None
 return (lo,hi)

def sweep(intervalsP,intervalsQ):
 events=[]
 for typ,D in [('P',intervalsP),('Q',intervalsQ)]:
  for i,(lo,hi) in D.items():
   if lo is not None:events.append((lo,'start',typ,i))
   if hi is not None:events.append((hi,'end',typ,i))
 events.sort(key=cmp_to_key(lambda a,b: ratcmp(a[0],b[0])))
 groups=[];k=0
 while k<len(events):
  e=events[k][0];g=[]
  while k<len(events) and rateq(events[k][0],e):g.append(events[k]);k+=1
  groups.append((e,g))
 activeP={i for i,(lo,hi) in intervalsP.items() if lo is None}
 activeQ={i for i,(lo,hi) in intervalsQ.items() if lo is None}
 min_open=10**9;best_open=[];candidate_open=[];event_target=[]
 def note_open(a,b):
  nonlocal min_open,best_open
  p,q=len(activeP),len(activeQ);tot=p+q
  rec=(a,b,tuple(sorted(activeP)),tuple(sorted(activeQ)))
  if tot<min_open:min_open=tot;best_open=[rec]
  elif tot==min_open:best_open.append(rec)
  if p==1 and q==1:candidate_open.append(rec)
 if groups:note_open(None,groups[0][0])
 else:note_open(None,None)
 for gi,(e,g) in enumerate(groups):
  endP={i for _,kind,typ,i in g if kind=='end' and typ=='P'};endQ={i for _,kind,typ,i in g if kind=='end' and typ=='Q'}
  startP={i for _,kind,typ,i in g if kind=='start' and typ=='P'};startQ={i for _,kind,typ,i in g if kind=='start' and typ=='Q'}
  strictP=activeP-endP;strictQ=activeQ-endQ
  weakP=endP|startP;weakQ=endQ|startQ
  if len(strictP)==1 and len(strictQ)==1 and not weakP and not weakQ:
   event_target.append((e,tuple(strictP),tuple(strictQ)))
  activeP=strictP|startP;activeQ=strictQ|startQ
  nxt=groups[gi+1][0] if gi+1<len(groups) else None
  note_open(e,nxt)
 return dict(min_open=min_open,best_open=best_open,candidate_open=candidate_open,event_target=event_target,groups=groups)

def main():
 assert len(sys.argv)==2 and __debug__
 A=read_parent(sys.argv[1]);Pc,Qc,Pa,Qa,C=build(A)
 PI={i:z for i in range(len(Pa)) if (z:=root_interval(i,Pa,Pc)) is not None}
 QI={i:z for i in range(len(Qa)) if (z:=root_interval(i,Qa,Qc)) is not None}
 sw=sweep(PI,QI)
 assert not sw['candidate_open']
 assert not sw['event_target']
 assert sw['min_open']==3
 assert len(sw['best_open'])==1
 lo,hi,pr,qr=sw['best_open'][0]
 assert pr==(94,124) and qr==(3,) and lo is not None and hi is not None
 assert ratlt(lo,(1,1)) and ratlt((1,1),hi)
 def roots_at_one(adj,coef):
  out=[]
  for i,js in enumerate(adj):
   if all(coef[i,j][0]+coef[i,j][1]<0 for j in js):out.append(i)
  return tuple(out)
 assert roots_at_one(Pa,Pc)==(94,124)
 assert roots_at_one(Qa,Qc)==(3,)
 print('QC52_TANGENT_ALL_POSITIVE_LAMBDA_EXCLUDES_OWN110_PASS')
 print('parent',A['V'],A['E'],A['F'],A['counts'],A['weak'])
 print('centroid_common_denominator_bits',C.bit_length())
 print('strict_root_intervals',len(PI),len(QI),'event_groups',len(sw['groups']))
 print('minimum_open_strict_root_sum',sw['min_open'])
 def digest(r):return hashlib.sha256(ratstr(r).encode()).hexdigest()
 def floorbr(r,scale=10**15):
  q=(r[0]*scale)//r[1];return (q,q+1,scale)
 lg=next(g for e,g in sw['groups'] if rateq(e,lo));hg=next(g for e,g in sw['groups'] if rateq(e,hi))
 assert [(k,t,i) for _,k,t,i in lg]==[('end','Q',26)]
 assert [(k,t,i) for _,k,t,i in hg]==[('start','Q',29)]
 print('unique_minimum_interval_lambda_floor15',floorbr(lo),floorbr(hi))
 print('unique_minimum_endpoint_sha256',digest(lo),digest(hi))
 print('boundary_events',('end','Q',26),('start','Q',29))
 print('unique_minimum_roots_U',pr,'S',qr)
 def ib(z):
  a,b=z;return (None if a is None else floorbr(a,10**12),None if b is None else floorbr(b,10**12))
 print('key_root_intervals_floor12','U94',ib(PI[94]),'U124',ib(PI[124]),'S3',ib(QI[3]),'S26',ib(QI[26]),'S29',ib(QI[29]))
 print('open_strict11_intervals',len(sw['candidate_open']),'endpoint_strict11_weakfree',len(sw['event_target']))
if __name__=='__main__':main()
```

## Acceptance boundary

No exact descendant body is promoted, so there is no new whole-basin/body census to substitute for the parent evidence. The new accepted scientific item is the exact all-parameter tangent-axis exclusion above. The surviving C616 entrance remains own121/weak000, and the canonical accepted own110 record remains C622. The open problem is still a genuine finite whole physical-basin cancellation with actual uniform mass and E<=310, but this specific affine tangent axis should now be treated as closed.
