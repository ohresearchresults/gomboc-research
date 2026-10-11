# material-6918f3e3e0bb

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# RAW_HEX6_ALL_ROOT_PSD_COLLAR_V1

## Result and exact scope
This upgrades the distinct rational control in [internal-source-reference] from exclusion of singular-disconnected U1 components to a COMPLETE all-root nonzero-PSD weak-tree exclusion. The body is RAW_TRANSLATED_HEX6_1over5_24over25_49over50_2over9_99over100_V1: the literal changed six-pole raw source at cuts(1/5,24/25,49/50,2/9,99/100), translated by its actual uniform VOLUME centroid. It is NOT the fixed-pole star-centred algebraic atlas member for those fractions.

There are4335 true spanning trees per root and43350 rooted trees over all10 roots. The literal307 positive-definite stencils below, with1150 positive arrow terms, cover EVERY such tree. All921 leading principal minors were checked by exact rational arithmetic. This proves that every physical SPD has at least TWO strict unstable vertices, regardless of weak equilibria. More strongly, no nonzero PSD has a complete weak true rooted tree at any root.

The same conclusion holds for EVERY full-dimensional homogeneous own-centred body with the SAME true labelled faces/edges whose actual centred coordinates differ coordinatewise by at most10^-12 from this exact body. This is a closed relative coordinate collar, not an unrestricted box of independent nonplanar vertices and not a whole E17 incidence/moduli exclusion. No attaining example or global bound changes;34..622 remains accepted.

## Proof certified by the complete source
For each directed true edge e=(i,j), let A_e=sym[X_i(X_j-X_i)^T]. Its integer coefficient row r_e is a positive multiple scale_e of the physical six-entry arrow row. The code fixes S_e=max|r_e| and verifies Q=-sum_e(weight_e/S_e) A(r_e) positive definite. If all selected arrows of a tree were nonnegative under a nonzero PSD M, then tr(QM)<=0, whereas Q>0 gives tr(QM)>0. Exhaustive combinations of9 among17 edges, cycle rejection and orientation from every root cover ALL true rooted trees. No singular metric is discarded.

The source also proves the collar quantitatively. With R=max_i||X_i||_1 and coordinate error eta<=1, each physical A_e changes in operator norm by at most8(R+1)eta. For a stencil put alpha_e=weight_e*scale_e/S_e and ell=det(Q)/tr(Q)^2<=lambda_min(Q). The exact bound eta<=ell/[16(R+1)sum alpha_e] leaves the perturbed stencil at least ell/2 times I. All307 bounds admit eta=10^-12. The original actual uniform centroid, true maximal supporting facets, positive fan volumes, and graph incidence are checked exactly as part of the same script.

## Recovery and verification
All coordinates, incidence, integration fans and307 stencils are literal in the autonomous source below. Python3.13.5 standard library was used; Python>=3.10 is sufficient. No numerical search package is needed to recover or verify the result. The executed heuristic search is not a premise of the proof.

Save the fenced source verbatim as verify_raw_hex6_psd.py, with LF newlines and a final newline. Its length is16609 bytes and SHA256 is552a806d0e75ec0e707ae8bdeaf6c0aa57022e997c532df232832ef96aeddd96.

Reconstruction/verification command:

    python verify_raw_hex6_psd.py --output raw_hex6_allroot_psd_report.json

Expected terminal marker: RAW_HEX6_ALLROOT_PSD_COLLAR_VERIFIED.
Expected output: raw_hex6_allroot_psd_report.json,1434 bytes,SHA256 b0bac651b5fd3152045ef4dccc050c5a8e127c4b8767df89ceaf8ea05b56349c.
Coverage digest: ca1ad66655fda6ac022cbefc95e8f7b766b0865aa5b4549eb388cac805def4f4.

Additional pin check:

    python -c "import hashlib,pathlib; b=pathlib.Path('raw_hex6_allroot_psd_report.json').read_bytes(); assert len(b)==1434; assert hashlib.sha256(b).hexdigest()=='b0bac651b5fd3152045ef4dccc050c5a8e127c4b8767df89ceaf8ea05b56349c'; print('RAW_HEX6_CAPSULE_PINS_OK')"

## Complete source
```python
#!/usr/bin/env python3
"""Exact ALL-ROOT, NONZERO-PSD true-tree exclusion and an explicit
actual-own-centred same-graph coordinate collar on ONE rational E17 body.
All decisive operations use integers/Fraction; no numerical solver is needed.
Python >=3.10, standard library only.
"""
from fractions import Fraction as F
from functools import reduce
import hashlib, itertools, json, math, sys, time

FACES=((0,4,6,5),(0,5,7,1),(0,1,2),(0,2,8),(0,8,9,3),(0,3,4),(4,3,9,2,1,7,6),(5,6,7),(9,8,2))
EDGES=((0,1),(0,2),(0,3),(0,4),(0,5),(0,8),(1,2),(1,7),(2,8),(2,9),(3,4),(3,9),(4,6),(5,6),(5,7),(6,7),(8,9))
DIRECTED=tuple((i,j) for i,j in EDGES for i,j in ((i,j),(j,i)))
NEIGHBORS=tuple(tuple(j for a,j in DIRECTED if a==i) for i in range(10))
FAN=((4,3,9),(4,9,2),(4,2,1),(4,1,7),(4,7,6),(5,6,7),(9,8,2))
CUTS=(F(1,5),F(24,25),F(49,50),F(2,9),F(99,100))
P=tuple(tuple(F(k,100000) for k in r) for r in ((60401,-32565),(80000,-20000),(0,60000),(-80000,80000),(-483861,-325040),(-447814,-355009)))
BASE=(F(2615613,500000),F(816129,250000),F(-3))
APEX=(F(0),F(0),F(1))


def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(t,a): return tuple(t*x for x in a)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det3(a): return dot(a[0],cross(a[1],a[2]))
def interpolate(a,b,t): return add(a,mul(t,sub(b,a)))

def solve3(a,b):
    d=det3(a)
    assert d
    return tuple(det3(tuple(tuple(b[i] if j==k else a[i][j] for j in range(3)) for i in range(3)))/d for k in range(3))

def fan_moments(Y):
    ds=[det3(tuple(sub(Y[i],Y[0]) for i in t)) for t in FAN]
    assert all(d>0 for d in ds)
    den=sum(ds)
    g=tuple(sum(d*(Y[0][k]+sum(Y[i][k] for i in t)) for d,t in zip(ds,FAN))/(4*den) for k in range(3))
    return den/6,g

def exact_body():
    qs=tuple(p+(F(1),) for p in P)
    B=tuple(solve3((qs[i],qs[(i+1)%6],BASE),(F(1),)*3) for i in range(6))
    x,y,z,u,v=CUTS
    Y=(APEX,B[1],B[2],B[4],B[5],interpolate(B[0],APEX,x),interpolate(B[0],B[5],y),interpolate(B[0],B[1],z),interpolate(B[3],APEX,u),interpolate(B[3],B[4],v))
    V,g=fan_moments(Y)
    X=tuple(sub(y,g) for y in Y)
    V2,g2=fan_moments(X)
    assert V2==V and g2==(0,0,0)
    # This is a NEW translated rational source body, NOT the fixed-pole
    # star-centred algebraic body for the same five fractions.
    return X,V,g

def geometry_checks(X):
    incid={e:0 for e in EDGES}
    qs=[]
    for face in FACES:
        n=cross(sub(X[face[1]],X[face[0]]),sub(X[face[2]],X[face[0]]))
        h=dot(n,X[face[0]])
        assert h
        if h<0: n=mul(-1,n); h=-h
        assert all(dot(n,X[i])==h for i in face)
        assert all(dot(n,X[i])<h for i in range(10) if i not in face)
        turns=[]
        for k,i in enumerate(face):
            j=face[(k+1)%len(face)]; a=face[(k-1)%len(face)]
            e=tuple(sorted((i,j))); assert e in incid; incid[e]+=1
            turns.append(dot(n,cross(sub(X[i],X[a]),sub(X[j],X[i]))))
        assert all(t>0 for t in turns) or all(t<0 for t in turns)
        qs.append(mul(1/h,n))
    assert all(v==2 for v in incid.values())
    assert len(X)-len(EDGES)+len(FACES)==2
    assert len(set(X))==10
    # Verify three-connectivity of the claimed spherical face graph.
    for removed in itertools.combinations(range(10),2):
        allowed=set(range(10))-set(removed); seen={min(allowed)}
        while True:
            new=seen|{j for i in seen for j in NEIGHBORS[i] if j in allowed}
            if new==seen: break
            seen=new
        assert seen==allowed
    return tuple(qs)

def integral_row(row):
    den=math.lcm(*(x.denominator for x in row))
    v=[int(x*den) for x in row]
    g=math.gcd(*v)
    assert g>0
    return tuple(x//g for x in v)

def arrow_rows(X):
    ans=[]
    for i,j in DIRECTED:
        a=X[i]; e=sub(X[j],a)
        ans.append(integral_row((a[0]*e[0],a[1]*e[1],a[2]*e[2],a[0]*e[1]+a[1]*e[0],a[0]*e[2]+a[2]*e[0],a[1]*e[2]+a[2]*e[1])))
    return tuple(ans)


# Literal exact checkpoint: each line is one positive-definite stencil;
# tokens are DIRECTED-edge-index:positive-integer-weight.
STENCIL_TEXT = """1:88 11:287 33:625
9:332 20:369 29:299
3:97 17:315 33:588
3:130 19:537 24:333
0:369 11:251 14:380
3:182 7:275 19:543
7:233 20:324 31:443
0:127 5:328 9:45
8:453 11:219 33:329
9:458 10:339 12:203
8:222 18:347 23:431
6:204 11:403 16:393
1:140 5:491 21:369
1:191 7:399 10:410
7:249 11:408 16:343
6:205 18:369 23:427
4:273 9:310 29:417
3:93 6:102 11:55
1:123 19:562 24:314
2:453 7:128 19:420
0:156 7:565 12:279
2:50 9:29 18:121
0:209 14:314 17:477
8:339 19:367 28:294
1:23 6:141 21:86
9:248 10:117 29:135
3:280 4:403 15:317
1:82 17:395 33:523
5:69 21:196 25:100 31:135
20:332 27:238 31:431
1:107 19:490 21:227 22:177
3:301 5:456 7:242
4:235 12:341 24:423
4:68 7:201 31:64
2:498 11:149 14:353
2:109 16:104 32:287
5:222 16:233 23:263 32:282
3:188 6:527 32:285
0:180 12:372 24:449
7:405 10:427 12:168
1:70 7:312 20:617
8:275 12:273 28:452
0:229 5:638 21:133
1:119 10:370 32:511
2:214 17:353 33:433
5:499 27:350 31:151
6:420 11:257 33:323
10:259 17:465 28:276
2:53 7:132 12:65
2:397 19:402 21:202
8:201 11:402 16:397
0:153 11:378 33:469
4:72 11:71 16:57
1:207 5:521 7:272
6:125 17:209 28:166
3:187 8:203 11:110
1:29 15:128 20:529 24:314
2:242 12:343 24:415
8:95 13:18 14:624 17:262
6:109 21:418 29:473
4:125 18:477 21:398
3:110 19:432 21:167 22:291
7:304 10:129 14:314 25:252
0:91 7:437 20:472
6:112 21:428 31:459
1:157 5:507 24:336
4:224 14:12 20:517 24:247
7:189 19:239 29:572
2:95 18:123 21:32
3:140 5:401 12:85 21:374
1:251 4:496 7:253
4:89 14:226 21:413 25:271
10:95 13:219 17:633 26:53
0:93 20:585 24:322
1:94 4:235 21:171
1:113 4:241 24:146
5:120 9:218 23:320 29:341
6:442 13:26 19:205 24:327
2:483 19:397 24:121
4:256 12:321 28:424
0:329 13:7 19:534 32:130
0:293 12:158 18:404 21:144
10:153 14:74 19:189 32:584
4:313 9:87 19:445 22:155
9:79 11:197 29:510 33:214
6:276 12:271 28:453
3:253 8:411 17:237 26:99
0:203 16:246 21:551
0:32 5:82 7:11
9:117 10:93 14:511 17:279
10:59 20:227 23:337 24:235 32:142
4:90 13:74 14:457 17:379
2:148 5:265 21:87
6:32 13:6 14:208 17:87
2:227 7:148 18:625
8:144 14:105 26:334 32:418
8:249 17:421 28:330
6:78 16:69 32:353
10:181 15:58 19:236 32:524
2:160 16:111 21:136 22:93
1:71 8:236 21:513 25:180
4:203 27:611 31:185
4:83 15:4 20:263 30:150
11:331 16:123 22:546
2:340 5:550 7:109
5:172 21:380 25:167 29:281
7:250 20:384 29:367
1:154 7:227 13:44 19:575
0:119 25:258 31:313 32:310
0:157 17:380 33:463
9:192 13:12 19:265 29:531
10:46 27:143 31:61
6:274 19:149 21:370 22:207
5:165 18:553 28:282
2:219 11:327 33:454
4:105 25:245 31:228 32:422
8:39 17:210 26:362 30:388
8:131 16:59 23:264 32:546
4:201 11:144 18:655
2:229 13:45 14:232 17:495
10:109 17:262 18:129
6:320 9:267 12:65 30:347
4:142 29:594 32:263
8:89 14:357 21:308 25:246
11:2141 18:3679 22:3221 33:959
2:396 9:317 16:240 22:47
10:101 21:478 25:268 31:153
5:116 8:62 23:567 28:255
3:401 4:428 11:171
11:52 15:8 16:73 24:117
7:203 12:8 18:493 20:297
3:283 6:387 17:164 19:166
4:124 17:107 21:86 22:183
0:328 13:60 17:85 19:526
13:9 17:227 29:411 33:353
4:385 7:58 19:434 22:123
2:229 17:73 18:198
3:77 10:255 12:183 32:485
2:397 18:477 32:126
10:161 16:279 28:560
6:34 13:26 20:202 23:457 24:281
1:229 6:461 11:310
7:75 9:264 10:362 17:299
0:332 11:5 19:529 21:134
8:55 19:69 21:451 22:89 26:336
5:26 18:106 26:37 30:81
1:48 6:267 32:185
4:418 7:39 12:115 18:429
8:49 16:122 26:334 30:495
7:451 11:72 13:102 31:375
6:39 17:210 26:362 30:388
3:33 4:40 17:177
3:302 5:456 27:243
2:487 11:128 18:385
8:87 20:175 23:447 28:290
3:39 7:160 20:301
4:329 11:117 14:292 19:261
0:125 25:251 29:311 32:313
4:413 9:401 16:186
8:198 11:85 19:235 26:281 30:201
2:128 7:420 20:453
3:33 15:143 20:514 24:310
8:122 19:175 29:550 32:153
4:110 20:547 27:107 28:237
8:224 11:143 19:73 29:560
2:160 16:111 21:136 22:93
3:145 9:99 11:274 33:482
1:191 10:387 24:422
1:131 10:374 21:495
4:48 12:58 21:349 22:251 26:293
0:255 5:622 14:63 23:18 32:42
5:231 9:98 11:327 16:344
3:154 5:347 12:176 30:323
0:331 17:3 19:528 21:138
12:15 18:485 20:294 27:205
8:245 11:86 23:142 29:526
5:81 6:475 11:130 24:314
8:265 11:180 26:90 31:464
4:270 7:192 17:193 22:344
6:25 18:94 21:81
1:142 4:217 17:641
5:146 9:100 11:86 18:667
7:249 13:96 17:73 25:357 31:226
6:239 11:172 25:73 31:517
1:149 6:380 13:175 17:297
10:116 14:78 20:248 23:121 32:437
7:350 13:124 19:59 31:329 32:137
10:297 17:424 24:246 27:33
10:67 16:163 26:246 30:525
3:262 6:411 17:162 20:165
6:380 13:17 14:315 19:90 32:199
8:103 18:77 21:481 26:340
3:268 5:144 6:335 17:253
2:116 14:148 21:131 25:105
10:120 12:164 21:639 26:77
0:260 5:686 28:53
9:24 10:297 17:424 30:255
10:125 12:103 18:445 28:327
0:331 19:529 21:110 32:30
2:377 19:400 32:223
3:151 7:102 11:276 33:471
0:328 12:67 17:151 18:454
0:327 11:126 12:104 18:443
1:451 4:474 11:74
4:459 15:27 19:452 30:62
4:222 17:231 18:357 23:42 25:148
4:179 14:174 19:129 32:518
8:218 23:220 29:503 32:60
1:150 8:378 13:175 17:297
2:129 20:541 24:247 27:83
5:179 16:243 28:577
5:83 8:225 11:134 26:348 30:209
2:370 5:526 30:105
5:154 6:412 30:285 32:150
6:107 23:384 31:301 32:209
4:71 7:170 25:111 29:148
0:107 21:324 25:278 31:291
0:338 7:1 11:82 13:35 19:544
6:359 16:81 24:500 30:60
8:40 20:116 23:458 26:65 30:321
10:50 17:263 26:303 30:383
11:66 13:95 27:460 31:378
7:239 16:189 20:291 23:258 32:23
4:132 16:61 26:214 32:592
0:161 16:224 32:615
10:57 21:241 25:129 29:73
8:69 19:76 26:347 30:94 32:414
1:183 2:327 7:346 16:145
3:54 11:83 12:68 21:8 33:287
8:143 17:187 24:37 29:633
10:129 17:332 29:369 30:171
10:166 18:418 26:29 32:386
6:195 17:72 21:324 22:64 33:344
5:151 16:12 21:541 26:297
8:70 18:400 26:217 30:313
0:347 11:75 19:526 24:52
0:294 12:151 18:414 32:141
3:209 8:361 12:173 32:257
1:86 8:287 26:172 32:455
2:426 20:150 31:343 32:81
4:124 17:211 24:165
6:71 18:399 26:218 30:313
4:234 11:33 20:145 25:16 31:72
8:34 16:39 21:177
2:342 5:549 27:109
6:23 11:20 29:82
8:43 17:81 21:292 22:247 26:318 33:19
11:29 21:290 25:247 31:196 33:238
5:52 9:339 10:336 17:272
4:64 19:92 21:535 25:12 26:297
4:314 19:295 27:305 28:87
5:64 7:260 11:43 25:198 29:435
3:129 5:246 19:247 21:378
6:167 13:195 17:501 30:137
4:137 18:446 32:417
1:179 4:467 13:12 32:342
2:394 23:176 29:351 32:79
6:109 23:109 29:252 32:30
2:411 5:338 31:172 32:80
13:122 19:50 27:340 31:329 32:158
3:336 6:351 12:295 21:19
6:137 16:155 21:708
1:23 8:46 11:31
4:46 19:65 21:227 25:377 28:285
5:93 7:210 23:344 29:353
3:111 10:209 12:289 30:390
17:57 19:76 27:72 31:295
10:170 16:81 26:166 32:584
8:91 23:8 26:205 30:104 32:92
6:71 12:62 26:373 30:227 32:267
5:50 7:201 25:235 31:405 32:109
5:390 11:107 12:148 18:294 25:61
3:67 8:70 12:59 21:4
0:113 21:327 25:271 29:289
2:418 7:311 14:32 16:239
17:18 27:1 31:38 33:20
4:463 7:314 16:140 22:82
3:171 10:248 12:230 27:351
5:113 6:60 23:570 28:256
4:327 11:208 20:58 29:407
6:322 11:182 19:431 24:65
0:262 5:680 11:3 24:55
0:262 5:679 17:3 24:56
10:113 18:627 26:1 30:259
0:262 5:681 30:55 32:2
10:261 17:308 21:216 22:215
11:51 21:264 25:229 29:183 33:272
3:109 11:166 12:140 30:16 33:569
1:216 2:345 16:97 30:342
1:267 2:419 18:49 30:265
3:220 4:313 9:260 12:207
10:83 14:530 17:280 27:108
7:287 11:60 13:75 25:374 29:203
8:150 17:169 21:44 29:638
5:177 17:229 18:589 23:5
6:46 12:36 23:444 26:137 30:338
5:5 7:270 11:61 25:247 31:417
16:190 23:421 27:240 32:149
1:180 4:467 28:37 32:316
3:220 10:275 21:426 25:79
5:194 18:634 23:3 32:169
3:110 11:170 12:136 27:13 33:571
1:184 2:327 16:143 27:346
1:133 2:218 18:28 27:121
9:17 11:175 18:523 33:285
11:62 18:395 26:123 30:198 33:222
11:91 18:487 28:130 33:292"""


def all_trees():
    idx={e:i for i,e in enumerate(DIRECTED)}; result=[]
    for edgeids in itertools.combinations(range(17),9):
        parent=list(range(10))
        def find(x):
            while x!=parent[x]: x=parent[x]
            return x
        good=True;adj=[[] for _ in range(10)]
        for k in edgeids:
            a,b=EDGES[k];aa,bb=find(a),find(b)
            if aa==bb: good=False;break
            parent[aa]=bb;adj[a].append(b);adj[b].append(a)
        if not good: continue
        for root in range(10):
            seen={root};queue=[root];mask=0
            for i in queue:
                for j in adj[i]:
                    if j not in seen:
                        seen.add(j);queue.append(j);mask|=1<<idx[j,i]
            assert len(seen)==10 and mask.bit_count()==9
            result.append((root,mask))
    assert len(result)==43350 and len(set(result))==43350
    assert all(sum(r==root for r,m in result)==4335 for root in range(10))
    return sorted(result)


def raw_arrow_row(X,i,j):
    a=X[i];e=sub(X[j],a)
    return (a[0]*e[0],a[1]*e[1],a[2]*e[2],a[0]*e[1]+a[1]*e[0],a[0]*e[2]+a[2]*e[0],a[1]*e[2]+a[2]*e[1])


def verify():
    X,V,g=exact_body();geometry_checks(X)
    R=arrow_rows(X);S=tuple(max(map(abs,r)) for r in R)
    # r_e=(positive scale_e)*the actual physical arrow row.
    scale=[]
    for r,(i,j) in zip(R,DIRECTED):
        a=raw_arrow_row(X,i,j)
        k=next(k for k in range(6) if a[k])
        t=F(r[k])/a[k]
        assert t>0 and all(F(v)==t*u for v,u in zip(r,a))
        scale.append(t)
    # Euclidean norm <=l1 norm, giving an exact rational common vertex bound.
    radius=max(sum(abs(z) for z in x) for x in X)
    stencils=[];terms=0;bound=F(1);minors_checked=0
    for line in STENCIL_TEXT.splitlines():
        pairs=tuple(tuple(map(int,word.split(':'))) for word in line.split())
        assert pairs and all(0<=i<34 and w>0 for i,w in pairs)
        assert len({i for i,w in pairs})==len(pairs)
        c=tuple(-sum(F(w)*R[i][j]/S[i] for i,w in pairs) for j in range(6))
        a,b,d,e,f,h=c; e/=2;f/=2;h/=2
        determinant=a*b*d+2*e*f*h-a*h*h-b*f*f-d*e*e
        assert a>0 and a*b-e*e>0 and determinant>0
        minors_checked+=3
        trace=a+b+d;assert trace>0
        # lambda_min(Q)>=det(Q)/trace(Q)^2; deliberately conservative.
        lower=determinant/(trace*trace)
        mass=sum(F(w)*scale[i]/S[i] for i,w in pairs)
        assert mass>0
        # For max coordinate perturbation eta<=1, every actual A_e changes
        # in operator norm by <=8*(radius+1)*eta. Thus eta<=this bound
        # keeps each stencil Q above lower/2 times the identity.
        bound=min(bound,lower/(16*(radius+1)*mass))
        stencils.append(sum(1<<i for i,w in pairs));terms+=len(pairs)
    assert len(stencils)==307 and terms==1150 and minors_checked==921
    denominator=1
    while F(1,denominator)>bound: denominator*=10
    eta=F(1,denominator)
    assert 0<eta<=1 and eta<=bound
    trees=all_trees();counts=[0]*10;cover_digest=hashlib.sha256()
    for root,mask in trees:
        k=next((k for k,s in enumerate(stencils) if mask&s==s),None)
        assert k is not None, (root,mask)
        counts[root]+=1
        cover_digest.update(f'{root}:{mask}:{k}\n'.encode())
    assert counts==[4335]*10
    return {'theorem':'ALL_ROOT_NONZERO_PSD_WEAK_TREE_EXCLUSION_WITH_EXPLICIT_COLLAR',
            'body_identity':'RAW_TRANSLATED_HEX6_1over5_24over25_49over50_2over9_99over100_V1',
            'not_fixed_pole_star_atlas_member':True,'cuts':[str(t) for t in CUTS],
            'vertices_edges_faces':[10,17,9],'uniform_volume':str(V),
            'exact_own_centroid':[0,0,0],'rooted_true_trees':len(trees),
            'trees_per_root':counts,'pd_stencils':len(stencils),'arrow_terms':terms,
            'exact_positive_leading_minors':minors_checked,
            'coordinate_collar_linf':str(eta),'coordinate_collar_decimal_exponent':len(str(denominator))-1,
            'coverage_digest':cover_digest.hexdigest(),
            'scope':'For every full-dimensional homogeneous own-centred body with these same true labelled faces/edges and each coordinate within the stated closed collar of this exact X, no nonzero PSD form has a complete weak true rooted tree, at any root. Every physical SPD has at least two strict unstable vertices.',
            'limitations':['Not a whole E17 incidence or moduli exclusion.','No new proper110 attaining example.','Global accepted bracket remains 34..622.']}


def main():
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--output',default='raw_hex6_allroot_psd_report.json');args=p.parse_args()
    report=verify();blob=(json.dumps(report,sort_keys=True,indent=2)+'\n').encode()
    with open(args.output,'wb') as f:f.write(blob)
    print(json.dumps(report,sort_keys=True))
    print('REPORT_BYTES',len(blob))
    print('REPORT_SHA256',hashlib.sha256(blob).hexdigest())
    print('RAW_HEX6_ALLROOT_PSD_COLLAR_VERIFIED')

if __name__=='__main__':main()
```
