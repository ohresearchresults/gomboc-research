# figure-0059

Historical AI scientific report · saved 2026-08-25 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Complexity-200 projective/metric branch — self-contained final handoff

## Determination

**No winner was found.** This branch did not produce a strict own-volume-centroid `(S,U,H)=(1,1,0)` body. The run’s acceptance gate requires an explicit finite body at its own exact centroid and rejects a near-state or wall state. :contentReference[oaicite:0]{index=0} The journal was also correct that the previous wrapper was not usable as evidence. :contentReference[oaicite:1]{index=1}

Forensic inspection of the worker-local archive found that the intended earlier driver never started:

```text
SyntaxError: '(' was never closed
localized_projective_search.py, line 107
```

Its status contained only `summary_loaded=false`. Therefore the previous wrapper’s claimed branch enumeration, topology inventory, strongest-state export, and independent verification had **zero completed mathematical coverage**. Everything below was reconstructed and executed afresh in this saved conversation.

## Reconstructed branch and completed coverage

The recovered Q-polar has 36 Q-vertices, 66 maximal Q-faces and 100 Q-edges. Its polar has

```text
(V,E,F,C)=(66,100,36,200),   C=V+E+F-2.
```

At every accepted Q-state the three projective variables were solved from the three first-moment equations for `(Q+p)^°`; centroid displacement was not merely penalized. The five metric variables define a trace-zero symmetric matrix `S`, with `A=exp(S)`, hence `det A=1` exactly and centroid zero is preserved.

The localized family varied 58 degrees of freedom: available coordinates of Q-vertices

```text
{1,4,5,6,7,11,12,15,16,19,20,24,25,27,28,31,32},
```

the common bottom height, `p∈R^3`, and the five metric variables. Completed work was:

- 300 exact-recentered Adam steps;
- all four retained stable-face/unstable-vertex choices `{7,20}×{14,59}` screened at seven trust radii;
- 150 nonlinear, exactly recentered evaluations along LP rays;
- sequential max-min continuation through the fixed realization cell to its limiting circuit;
- 760 valid controlled local circuit perturbations spanning 129 distinct Q-hull signatures;
- metric-only polishing of the eight leading changed cells;
- explicit crossing of the limiting diagonal flip and a new-cell continuation.

No evaluated state had `(1,1,0)`.

The natural retained branch `F7/V59` improved from fixed-witness common margin `-0.09556307196` at the recovered seed to `-0.01129072585` after nonlinear continuation, then to `-0.0097284013614` after exact nonlinear LP-ray evaluation. A radius-2 linearization predicted only `+7.5576e-5`, but direct nonlinear evaluation remained negative. The alternative branches were materially worse: at the screened nonlinear state `F20/V59=-0.07619883039`, while both branches retaining vertex 14 were `-0.5456869590`; even their radius-2 linear predictions remained negative.

## Strongest robust materialized state

This is the best exactly centered materialization that retains the intended `(36,66,100)` incidence, exactly the original four defects, and comfortable distance from every incidence wall. It is a strict open **`(2,2,2)`**, not a near `(1,1,0)` state.

### Deterministic H/V generator

The self-contained verifier at the end contains a compressed, checksummed payload with the complete 36×3 decimal Q matrix, all 66 Q-facet active sets defining the primal vertices, all 36 maximal primal face cycles, the exact-centering root, and the metric. Running it writes readable `payload.json`, `H.csv`, `V.csv`, and `body.obj`. It uses no worker-local input.

The reconstruction is

```text
N=Q+p,
S=[[m0,m1,m2],[m1,m3,m4],[m2,m4,-m0-m3]],
A=exp(S),
H=N A^-1,
N[FACE_IDS[j][:3]] w_j=(1,1,1)^T,
v_j=A w_j.
```

Metric parameters:

```text
m=(1.6838380427460675,
   0.6600630240038552,
   0.8965417820334370,
  -1.4953993047035408,
  -0.5191542070962939).
```

Numerically,

```text
A=
[[7.140128182588781,  0.9927985345941814,  2.372704272827779],
 [0.9927985345941812,0.41244364502225717,0.05861881326041836],
 [2.372704272827779, 0.05861881326041832,1.5670842207795537]],
det(A)=1 exactly by trace(S)=0
(binary64: 1.0000000000000082).
```

### Centroid isolation

Interpreting the payload’s listed Q entries as exact decimal rationals, the projective-centering root is

```text
p0=-0.0003555653988535481138649682962405249983406477791564749216105303870340985187677792951113688182855191643
p1=-0.002222438459256060263393104504999859614144407201865025608434440165058699871628858718193489738458734891
p2=-0.1912405104100839661846697208321858012088458706023981720582337215131906561715489228151359277025095106.
```

A 100-decimal-digit interval Krawczyk calculation on the unnormalized first-moment equations used the box `X_i=p_i±10^-18` and obtained

```text
K0=[-0.000355565398853548113864968296243034114273650983604194751933093528017029117726245115002865919275556750463074,
    -0.000355565398853548113864968296238015882407644574708755091287967246051167919809313475219871717295481577888464]
K1=[-0.00222243845925606026339310450500228470022848544474696516186896988657268516589823627756010063287909403532323,
    -0.00222243845925606026339310450499743452806032895898308605499991044354471457735948115882687884403837574181321]
K2=[-0.191240510410083966184669720832188801396198448390227666270551502464193811131217854049088806667996929084688,
    -0.191240510410083966184669720832182801021493292814568677845915940562187501211879991581183048737022092144901].
```

Thus `K(X)⊂int(X)`, proving a unique centering root in that box. The high-precision first moment is below `1.2×10^-99` componentwise, centroid below `4.4×10^-102`, pre-metric volume

```text
10.85431898955679769256302691267239014549462026302394709869983967101410574193289625556869818847051898,
```

and centering-Jacobian determinant `-124837568.0613322708914…`. The metric therefore leaves the own centroid exactly at zero.

### Actual full-lattice equilibrium audit

Independent reconstruction from the generated V-coordinates gives

```text
(V,E,F,C)=(66,100,36,200)
binary64 full-hull centroid=(6.29e-16,8.37e-17,2.18e-16)
centroid norm=6.71e-16
(S,U,H)=(2,2,2).
```

All actual maximal faces are rebuilt from Qhull’s triangulated output and match the 36 payload cycles exactly. Consecutive cycle pairs yield exactly 100 true edges, each with exactly two incident maximal faces. Every vertex is tested against all other vertices—the complete tangent-cone test, equivalent to auditing its full normal cone—not against a fixed witness row.

Positive equilibria and normalized margins:

| type | feature | margin |
|---|---|---:|
| stable | Q-face 7, retained | `+0.0535464637126795` |
| stable | Q-face 20, unwanted | `+0.0097284013614036` |
| unstable | vertex 59, retained | `+0.509236293081010` |
| unstable | vertex 14, unwanted | `+0.00971857828830802` |
| saddle | edge `(2,3)`, unwanted | `+0.00890577983030672` |
| saddle | edge `(29,47)`, unwanted | `+0.00602080602035096` |

Complete edge-component vectors `(t,1-t,λ1/|q|,λ2/|q|)` are

```text
(2,3):   (0.9910942201696933,0.00890577983030672,1.28244458571334,1.35271087236714)
(29,47): (0.00602080602035096,0.9939791939796491,0.555226752674236,0.675801123153321).
```

Nearest rejected features:

```text
face Q25     -0.000953162134369208
vertex 15    -0.00371939575679786
edge (29,51) -0.00167024411931763
edge (3,5)   -0.00312927845734184.
```

Therefore the minimum absolute equilibrium-sign clearance is `0.000953162134369208`; the smallest positive equilibrium margin is `0.00602080602035096`. This is decisively `(2,2,2)`.

Raw incidence and boundedness margins:

```text
all 36 Q rows are hull vertices
Q maximal faces / triangulated facets = 66 / 68
minimum raw normalized inactive Q-plane distance = 0.005628842865433636
origin-to-Q-boundary margin = 0.4954216507593087
minimum projective denominator = 0.8245543155609020
maximum generated H-inequality violation = 5.11e-15
minimum raw inactive primal slack 1-H_i·v_j = 0.009322619995256298.
```

## Precise observed obstruction

Allowing the comfortable Q-cell floor to collapse improved the scalar fixed-witness objective to `-0.00314434006532834`, but the actual class worsened to `(2,3,3)`:

```text
positive faces: Q7 0.01442919, Q20 0.00310963
positive vertices: 3 0.00305066, 14 0.00303930, 59 0.29121038
positive edges: (2,3) 0.00304658, (3,5) 0.000983558, (29,47) 0.00305519
Q inactive slack: 5.06730344e-5
projective denominator: 0.8299990968.
```

The limiting reciprocal incidences were

```text
facet (23,28,29) versus Q24: 5.06730344e-5
facet (23,24,29) versus Q28: 5.45396448e-5,
```

the four-point circuit `{23,24,28,29}`. Crossing it swaps diagonal `23-29` for `24-28`, remains `(2,3,3)`, and immediately meets another Q wall at `1.16417e-5`.

The remaining obstruction is thus a coupled transfer/circuit cascade:

- stable face 20 approaches transfer to face 25;
- unstable vertex 14 approaches transfer through vertex 15 while vertex 3 appears;
- saddle `(2,3)` transfers toward `(3,5)`;
- saddle `(29,47)` transfers toward `(29,51)`;
- further rows involving vertices 29/50 and edge `(18,19)` activate;
- the Q circuit `{23,24,28,29}` reaches zero before all original four signs reverse.

This is **not** a rigorous local or global infeasibility theorem. No interval branch-and-bound or exact Farkas certificate was obtained. It rules out only the sampled trust regions and materialized cells.

## Standalone reconstruction, verification, and export kernel

The Base85 payload decompresses to canonical JSON with SHA-256

```text
8c148f5657f68bbb30e73cb93a6b1af0e39d8fe8e70a12a40c3af081c5af2720.
```

The script prints the complete audit and true-edge list, writes the uncompressed coordinates/incidence to `payload.json`, writes full H/V coordinates to `H.csv` and `V.csv`, and exports `body.obj`.

```python
#!/usr/bin/env python3
import base64,hashlib,json,zlib
import numpy as np
from scipy.linalg import expm
from scipy.spatial import ConvexHull
BLOB='c-n=Q$*yHP5k&vxj`u6s**I-xh(=-tVpuBi1xU;h|IP~A`xFcwT&ZgNxXCsm?0<g!@wdPG!{7e&`@equ=KFVh+S7kL-+MjXo~~hga!(~op(RZ$2Jx&X`40B6TTA`nM`Og<XPnJrZ|WQxXG>>KouT1v&khakTC=D2pdQ=)?Qy>T#MAb-p2@c!-|PO&9gY*ujj!hkov%FH;d;8(*It&Teui<D`DHtFC%ngG+VIgI-$Q$hcomqXhC6P3>!wh9!`>U)t%6ckaT1e#B9=E>dsbPg%2?P#Wp?VQoa)5tH$bH~Z_sfL*nAXL-SFnI=&qr^@oV9_WY+J{&#b2sv~l*@;FpGUL)qM1#~m(?KYru)csy^~gt#M{JKDN6Tz6Khw-{K$VLL-_$AV&@O1p)^z%3E=S!b`j+HOS3{g3DC&w}j6YddJVP@we_l-j4EEVk#yrdHf`op4Uaa)V1)?i*<vttA|X&@nZ=catyxYbP6)bP7h;?zMbGKfMO08zH9ETSFlI!t>d{wq3SMF;bhdjt{jW>q#~P_%8c+Va>M--|YxiZp(a|%I*2(m#Ggga1R_37M8qpk##R<YRXZnV?NZ<0|LBgdY(oKL~8bK?zXs_k!-Tv#0y2WiHwO&rOEA+>7X7&j}e6@OGCc~srrSGzWOzqtZoQmI`_oD6VsZ*G!C@Vg^f_yF=bso@LNyF2c~hLX=0!k*jCsw=G(7fRX(=qkq3KNWEkVvWyn!kANQ9gH0(Mrn@lu;@h`&RSNnSQzy7Va|N84+oce0tve}%~tXbyDtYY&o?OSWnVr9!wYmT;>Em`_jQQdOR70oymubE!iW3US=YnsL09W%nBO<(D2c$>$DuRgt%PoHhoT-ydtqxD>)r!Akjv9Y(av#K-Q`W(Y=9K*&MIa^d4Y0W=2EPUe5TUg6Qo;x2K%(8LJY;CMr$4WUrv_Hyncz&`Wve`VxjM-b>qL2>ZO^;zLk?$=@P@n2;;d>dIkCAGXHEJ+7`7dr^dndFakeb6Iqn}FIE_jW#+%3CbBlN{RqGr$R?D4&OP@Pq|+`OWBdu^ntH!+eLdat)8nNHvercuV6cD4t5m`(g8{mU~;TJ)up`BI-h&B+xx$4cu(P|?Q8$7^~w;_1ezIqKSu?!5<fX%sy_>EMx4b-L%I-18V2{CRR{t<hrm4X~5tQgIE)VErvDNLn_^gINyFx3bw67^9K&BJ0AZvxx{=uWIzc-W~(rMU4WGl$qT=kednsEDaxPp4q<4s)&NZQ>Yq0i-PS1T4*v@yX~R9rNgs48}K;k^blVXBq+-{@-;HlaUe*FK#qc5v=L#^0ZIs9Y4ou|p|Tp)s6K7HH6a54OL-?X$b+h1lup24PtqJdTDy@@?wF>JVDW){861IZ1d$Vt+FRHL3Eb4q-dBtl%4-Cbh71r^>5ey;VFt{>E3wqHQxzCO{!405lYBp2BN_K;vklC5`_y*8Ne5}Y1`0GT$N^=G0I-;9Gv63zi4jFd8^S?TKh^E2WW6s!SF_&gf)ltxo@j#mEf@>~Rge>eA{SMkoM=ujl0{q6(12TD;JRv|TPwx&w=^`5ZO{|_q^dU@_1b0?wD*CeT|q>GSD-|O9hZXm6|D(ma%76QQ18?14hjJ&jB#?X!`xg*Uk8LlXv|+5z96x6Fh@1f#!q>fgXA5SP4RhN4e@~GhyuhV@>^bm&!p0WPSJ_}Qxzz7VM?+iki4n@Z?PNn6@BvdngLg8CNULbUmx_QBasB(5E9&8SwJkfgDA*E5iLH!px92u)&2#Iua(e@7-Xb?{*3o3qdT1rH}o6Spi~zET#2wQVYx?*Pc&?SDaakTOlke846p@V6Yz31eE{I1TT1#s&iD_}_2E^zKA~O%0Y?};ATTP7Vg{t%x9Yz6&<cWfrny9ZS^=g=22@O;y<WHrQmC+m4mqiMgF%PZBp&Vnpz%=$gh|3eZMbCM$Ez?%DEEN{q+jTC|CtiWlR5VeaJ6d%se?oifn#{M7Y2+e-5?PY%}sklq_Ba+Ab=@V{#Zd)Lob9mWdoT!nnV!je~K|(y6*qW%7GG{(|+BY>lJ&94DMCwE||*vKUUyA4;Qe=1EbNJm%fF@Ai2;qRF_vBel;gJJ(wyf#6WLe8c=Jf0En;#0e{sB@3p`4UgMdj%NMCZKX^_-t#jWa-M|KxqLrDaVtUWO%E{vgUT<0JvW-K%Fm|(Vqq!JCk#Unqz&6mo{vm&x9!&`5jz+;L88q&KBI01|R{jDNg&4uzuq3C&btm~sCmuY}02m6jwE=}h#wAR^mT2)k!e1_$?poiSPZ9*fD2lk5JbwgU<ONaUO{J@tTT%+xL@uUOG(AF)51tT0Q0)s371te{LMDQKd<m;Wk7;<W^7C{HWE8s)uX7l&X>%V_Amp#74bLM7R6HiQGI(1KZW@Zh3t(!FxOqreB21k((2sxp8+lV~!~'
raw=zlib.decompress(base64.b85decode(BLOB)); assert hashlib.sha256(raw).hexdigest()=="8c148f5657f68bbb30e73cb93a6b1af0e39d8fe8e70a12a40c3af081c5af2720"
d=json.loads(raw); Q=np.array(d["Q"],float); p=np.array(d["p"],float); m=np.array(d["m"],float); FI=d["FACE_IDS"]; PF=d["PFACES"]
S=np.array([[m[0],m[1],m[2]],[m[1],m[3],m[4]],[m[2],m[4],-m[0]-m[3]]]); A=expm(S); N=Q+p
W=np.array([np.linalg.solve(N[np.array(ids[:3])],np.ones(3)) for ids in FI]); V=W@A.T; H=N@np.linalg.inv(A)
P0=np.array([np.linalg.solve(Q[np.array(ids[:3])],np.ones(3)) for ids in FI]); den=1+P0@p
hv=ConvexHull(V); r=V.mean(0); vol=0.; mom=np.zeros(3)
for tri in hv.simplices:
 a,b,c=V[tri]; vv=abs(np.linalg.det(np.stack([a-r,b-r,c-r])))/6; vol+=vv; mom+=vv*(r+a+b+c)/4
cen=mom/vol
# Recover maximal faces independently from Qhull's triangulated output.
groups=[]
for eq,tri in zip(hv.equations,hv.simplices):
 n=eq[:3]/np.linalg.norm(eq[:3]); b=eq[3]/np.linalg.norm(eq[:3]); hit=None
 for g in groups:
  if np.linalg.norm(n-g[0])<1e-9 and abs(b-g[1])<1e-9: hit=g; break
 if hit is None: hit=[n,b,set()]; groups.append(hit)
 hit[2].update(map(int,tri))
assert sorted(tuple(sorted(g[2])) for g in groups)==sorted(tuple(sorted(x)) for x in PF)
ef={}
for fi,cyc in enumerate(PF):
 for a,b in zip(cyc,cyc[1:]+cyc[:1]): ef.setdefault(tuple(sorted((a,b))),[]).append(fi)
assert len(ef)==100 and all(len(x)==2 for x in ef.values())
fs=[]
for i,cyc in enumerate(PF):
 n=H[i]; q=n/(n@n); fs.append(min(np.dot(np.cross(V[b]-V[a],q-V[a]),n)/(np.linalg.norm(V[b]-V[a])*np.linalg.norm(n)) for a,b in zip(cyc,cyc[1:]+cyc[:1])))
fs=np.array(fs); vs=np.array([min(v@(v-w)/(np.linalg.norm(v)*np.linalg.norm(v-w)) for j,w in enumerate(V) if j!=i) for i,v in enumerate(V)])
es={}; comps={}
for e,fac in ef.items():
 i,j=e; a,b=V[i],V[j]; z=b-a; t=-a@z/(z@z); q=a+t*z; U=np.column_stack([H[k]/np.linalg.norm(H[k]) for k in fac]); lam=np.linalg.lstsq(U,q,rcond=None)[0]; assert np.linalg.norm(U@lam-q)<1e-11
 c=np.array([t,1-t,lam[0]/np.linalg.norm(q),lam[1]/np.linalg.norm(q)]); es[e]=float(c.min()); comps[e]=c.tolist()
qh=ConvexHull(Q); qraw=[]
for eq in qh.equations:
 z=Q@eq[:3]+eq[3]; z=z[np.abs(z)>1e-10]
 if len(z): qraw.append(-z.max()/np.linalg.norm(eq[:3]))
hi=[1-H[i]@V[j] for j,ids in enumerate(FI) for i in range(36) if i not in set(ids)]
st=np.flatnonzero(fs>1e-9).tolist(); un=np.flatnonzero(vs>1e-9).tolist(); sa=sorted([list(e) for e,s in es.items() if s>1e-9])
out={"VEFC":[66,100,36,200],"centroid":cen.tolist(),"centroid_norm":float(np.linalg.norm(cen)),"volume":vol,"class":[len(st),len(un),len(sa)],"stable_faces":{str(i):float(fs[i]) for i in st},"unstable_vertices":{str(i):float(vs[i]) for i in un},"saddle_edges":{str(e):{"score":es[e],"components":comps[e]} for e in es if es[e]>1e-9},"nearest_rejected_face":max((float(fs[i]),i) for i in range(36) if i not in st),"nearest_rejected_vertex":max((float(vs[i]),i) for i in range(66) if i not in un),"nearest_rejected_edges":sorted([(s,e) for e,s in es.items() if s<=1e-9],reverse=True)[:2],"detA":float(np.linalg.det(A)),"denominator_min":float(den.min()),"Q_raw_inactive_slack":float(min(qraw)),"Q_origin_margin":float(min(-qh.equations[:,3]/np.linalg.norm(qh.equations[:,:3],axis=1))),"H_raw_inactive_slack":float(min(hi)),"H_max_violation":float(np.max(V@H.T-1)),"true_edges":sorted([list(e) for e in ef])}
assert st==[7,20] and un==[14,59] and sa==[[2,3],[29,47]] and np.linalg.norm(cen)<1e-12 and min(qraw)>0.0056 and min(hi)>0.009 and den.min()>0.824
print(json.dumps(out,indent=2,sort_keys=True)); open("payload.json","wb").write(raw); np.savetxt("H.csv",H,delimiter=","); np.savetxt("V.csv",V,delimiter=",")
with open("body.obj","w") as f:
 for v in V: f.write("v %.17g %.17g %.17g\n"%tuple(v))
 for cyc in PF: f.write("f "+" ".join(str(i+1) for i in cyc)+"\n")

```

## Best continuation

The next search should not be another metric-only polish or another continuation of only the four original fixed witnesses. It should vary a connected Q-patch covering both transfer chains and both active circuits simultaneously: at minimum the Q one-rings around `{6,10,11,15}` and `{23,24,28,29}`, together with the dual basins of primal vertices `3,14,15,29,50` and edges `(2,3),(3,5),(29,47),(29,51),(18,19)`. The three centroid equations should remain eliminated by the isolated root solve, and all inactive slacks should remain raw. Rationalization is unwarranted until an actual `(1,1,0)` common margin is comfortably larger than both mechanics and incidence uncertainty.
