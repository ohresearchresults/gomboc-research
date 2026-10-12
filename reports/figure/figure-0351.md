# figure-0351

AI research report · 2026-09-09 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Clear Lynx 14 — C650 polar sparsification / physical realization handoff

## Finite verdict

**The pure topology gate is solved exactly, much more strongly than requested.** Starting from the durable exact `COORD_CONDITIONED_CONTACT35_H137_C650_D1000000000000` parent, whose accepted primal is `(V,E,F)=(190,325,137)`, `C=650`, homogeneous own-centred strict `(1,1,0)` / weak `(0,0,0)`, I reconstructed its canonical 137-vertex polar/support graph `G` and proved that its **minimum** spanning simple 3-vertex-connected subgraph has

```text
n = 137
m_min = 213
f = 78
```

Thus the specific C650 incidence graph admits an abstract coarsening all the way to primal

```text
(V,E,F) = (78,213,137),   C = V+E+F-2 = 426 = 2E,
```

not merely the requested `E<=249 / C<=498`. The journal had isolated exactly this spanning-3-connected optimization and physical follow-through as the missing gate; the current assignment repeats that requirement explicitly.

**The physical gate is not solved.** I constructed an **exact rational convex Maxwell/Tutte realization of the minimum 213-edge polar graph**, polarized it, integrated the true uniform filled volume, translated to its own exact volume centroid, and exhaustively audited maximal faces, primal vertices and all 213 true-edge four-component cones. Its exact strict/weak class is

```text
(S,U,H) = (2,2,2), weak = (2,2,2), degeneracies = 0.
```

So this is a real homogeneous own-centred convex `C426` nonwinner, not merely an abstract graph. The remaining exact packet in this canonical realization is:

```text
stable support rows:       [23, 53]
unstable primal vertices:  face-id 2, face-id 3
saddle polar/true edges:   (1,11), (56,92)
```

No `(1,1,0)` object is promoted here.

---

## 1. Canonical exact reconstruction of the C650 polar graph

The parent is not reconstructed by inference. I decoded the journal's literal seventeen-file capsule. The journal specifies that whitespace-stripping its 19,565-character base85 block, then `base64.b85decode` + `lzma.decompress`, gives 66,810 UTF-8 bytes with SHA-256

```text
081ff87dc9dd54f14cba01f745b659c7bdd7f76dffac35b115a12f5ba4dc0048
```

and that `python3 -S REPLAY_ALL.py` rebuilds the exact parent and audits. I reran the C650 portion; it reproduced the durable hashes/markers, including `A.json` = 339,478 bytes with SHA-256

```text
452379cd81e5d00b666d98d49eea352df4be9762475c63d6eab3323e633a7e02.
```

### Deterministic graph generator from the exact parent audit

`A.json["faces"]` has 137 ordered maximal primal-face vertex cycles, indexed by the support row `0..136`. Construct `edge_to_faces` by taking every consecutive pair of primal vertex IDs on every cycle. Every true primal edge occurs in exactly two cycles. Replace each primal edge by the sorted pair of its two incident face/support IDs. Sort these 325 pairs lexicographically. This gives the polar graph `G`.

Complete generator:

```python
import json, collections, hashlib
A=json.load(open('C650/A.json'))
faces=A['faces']
ef=collections.defaultdict(list)
for fi,cyc in enumerate(faces):
    for a,b in zip(cyc,cyc[1:]+cyc[:1]):
        ef[tuple(sorted((a,b)))].append(fi)
assert set(map(tuple,A['edges']))==set(ef)
assert all(len(x)==2 for x in ef.values())
G=sorted(tuple(sorted(x)) for x in ef.values())
assert len(G)==325 and len(set(G))==325
blob=''.join(f'{u} {v}\n' for u,v in G).encode()
assert hashlib.sha256(blob).hexdigest() ==  '3039216e06fa3dd0d5790c6cb53cdc79eeb1bed17c98357cbea64c866a6d88fe'
# exact planar rotation at support fi: for each consecutive primal edge on face fi,
# take the other incident support in the same order.
rot={}
for fi,cyc in enumerate(faces):
    r=[]
    for a,b in zip(cyc,cyc[1:]+cyc[:1]):
        pair=ef[tuple(sorted((a,b)))]
        r.append(pair[0] if pair[1]==fi else pair[1])
    rot[fi]=r
```

Canonical C650 polar edge-list SHA-256:

```text
3039216e06fa3dd0d5790c6cb53cdc79eeb1bed17c98357cbea64c866a6d88fe
```

Degree histogram reconstructed independently:

```text
{3:44, 4:30, 5:30, 6:15, 7:7, 8:5, 9:3, 10:1, 11:1, 21:1}
```

which matches the durable journal's 137-support / 325-edge accounting.

---

## 2. Exact minimum spanning simple 3-connected subgraph: H213

The canonical lexicographically sorted edge list is below. This is the literal defining data; no optimizer is needed to reconstruct it.

```text
0 52
0 133
0 134
1 6
1 11
1 34
2 55
2 67
2 134
3 51
3 69
3 109
4 5
4 7
4 10
5 7
5 8
6 11
6 34
6 114
7 9
7 10
8 9
8 23
9 57
10 11
12 42
12 81
12 136
13 40
13 51
13 71
14 15
14 82
14 129
15 75
15 78
16 20
16 58
16 97
17 18
17 19
17 21
18 19
18 76
19 60
20 21
20 59
21 60
22 23
22 32
22 57
23 57
24 100
24 114
24 115
25 26
25 36
25 65
26 27
26 82
27 61
27 82
28 35
28 62
28 64
29 41
29 49
29 70
30 64
30 135
30 136
31 64
31 66
31 135
32 33
32 93
33 37
33 94
34 100
35 64
35 98
36 37
36 65
37 94
38 39
38 43
38 133
39 43
39 68
40 45
40 69
41 42
41 70
42 80
43 44
44 45
44 68
45 71
46 73
46 77
46 88
47 78
47 102
47 103
48 49
48 79
48 86
49 106
50 89
50 123
50 124
51 109
52 91
52 133
53 54
53 55
53 134
54 96
54 116
55 67
55 101
56 57
56 92
56 95
58 59
58 120
59 60
61 63
61 82
62 63
62 81
63 81
64 66
64 81
64 98
64 99
64 135
65 95
66 99
67 101
68 69
70 71
72 73
72 83
72 103
73 104
74 75
74 76
74 112
75 76
77 83
77 89
78 84
79 86
79 124
80 81
80 82
81 136
83 84
84 102
85 86
85 87
85 105
87 106
87 108
88 89
88 123
90 91
90 117
90 125
91 125
92 113
92 114
93 94
93 95
96 117
96 118
97 120
97 122
98 99
100 101
102 103
104 105
104 123
105 124
106 107
107 108
107 110
108 110
109 110
111 112
111 117
111 130
112 131
113 115
113 127
115 116
116 118
118 119
119 128
119 129
120 121
121 122
121 125
122 132
126 127
126 128
126 129
127 128
130 131
130 132
131 132
```

Canonical text SHA-256:

```text
171a223c0e2ee52c36ba1076ec588d34aa056cc07efbde2f5d2c6104a805d911
```

Exact degree histogram:

```text
{3:130, 4:4, 5:1, 6:1, 9:1}
```

so the minimum degree is 3 and only 15 degree-excess units above cubic remain.

### Spanning / simplicity / 3-connectivity / planarity

* vertices are exactly `0..136`;
* all 213 pairs are distinct, loop-free, and are C650 polar edges;
* an independent standard-library check deleted **every one of the C(137,2)=9,316 vertex pairs** and found the remaining 135-vertex graph connected each time; hence vertex connectivity is at least 3. Since vertices of degree 3 exist, `kappa(H213)=3` exactly;
* filter the exact C650 cyclic rotation at each support to the H213 neighbors. Directed face traversal gives exactly 78 faces, uses all 426 directed edges once, and gives `137-213+78=2`. Thus the inherited rotation is a cellular sphere embedding. Planarity also follows immediately because H213 is a subgraph of the exact convex C650 polar graph.

Canonical filtered-rotation SHA-256:

```text
84a66b01a7ca3211da3e4bef6c0a616e07c75fa821630b493ed9465ad9dddf0e
```

Canonical face-cycle SHA-256 (cycles canonicalized up to rotation/reversal and sorted):

```text
014c7bb6258de3ad9d386d9046d61ee3d8f866a9f769974bec57ad6193d285da
```

Face-size histogram:

```text
{3:32, 4:21, 5:10, 6:3, 7:1, 8:2, 9:2, 10:1, 11:1, 12:2, 17:1, 31:1, 44:1}
```

---

## 3. Exact global minimum certificate: no 212-edge solution exists

I first found H213 by a binary edge-selection MILP with lazy 2-vertex-deletion connectivity cuts (SciPy 1.17.0 / HiGHS). The **minimum claim does not rely on trusting the MILP solver**: I extracted and exactified a rational LP-dual certificate that gives a lower bound `851/4 = 212.75`; edge count is integral, hence every spanning 3-connected subgraph has at least 213 edges.

Let `x_e in [0,1]` for each of the 325 C650 edges. Every spanning 3-connected subgraph satisfies:

1. `sum_{e incident v} x_e >= 3` for every vertex `v`;
2. after deleting any two vertices `a,b`, every nontrivial set `S subset V\{a,b}` has at least one selected crossing edge not incident to `a,b`;
3. `x_e <= 1`.

The exact dual uses only the following degree and seven connectivity inequalities. Unlisted multipliers are zero.

### Degree multipliers `y_v`

```text
y=1:   [1,2,4,5,9,10,11,12,22,23,25,26,27,28,30,31,33,34,35,36,37,41,49,56,61,62,63,66,67,70,71,93,98,99,101,109,135,136]
y=3/4: [80]
y=1/2: [0,3,13,14,15,16,17,18,19,20,21,24,38,39,40,43,44,45,46,47,48,50,51,52,53,54,58,59,60,68,69,72,73,74,75,76,77,78,79,83,84,85,86,87,88,89,90,91,92,95,96,97,100,102,103,104,105,106,107,108,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134]
y=1/4: [42]
```

### Seven valid 2-vertex-deletion cut multipliers

For each row `(weight; ban={a,b}; S={...})`, the cut is the set of original C650 edges with neither endpoint banned and exactly one endpoint in `S`.

```text
1/2 ; ban={2,100}  ; S={55,67,101}
1   ; ban={10,34}  ; S={1,6,11}
1/2 ; ban={26,36}  ; S={25,65}
1/4 ; ban={26,41}  ; S={12,27,28,30,31,35,42,61,62,63,64,66,80,81,82,98,99,135,136}
1   ; ban={28,30}  ; S={31,35,64,66,98,99,135}
1/4 ; ban={12,61}  ; S={28,30,31,35,62,63,64,66,81,98,99,135,136}
1/4 ; ban={26,61}  ; S={27,82}
```

### Upper-bound multipliers `w_e` on `x_e<=1`

```text
w=1:
(1,11) (1,34) (2,67) (4,5) (4,10) (10,11) (12,136) (22,23)
(25,26) (25,36) (26,27) (27,61) (28,35) (28,62) (30,135) (30,136)
(31,66) (31,135) (33,37) (35,98) (36,37) (41,70) (61,63) (62,63)
(66,99) (67,101) (70,71) (98,99)

w=1/2:
(2,134) (3,109) (6,114) (13,71) (34,100) (45,71) (48,49)
(49,106) (51,109) (56,92) (56,95) (93,95) (100,101) (109,110)

w=1/4:
(12,42) (41,42)
```

For every original edge `e=(u,v)` the replay checks exactly

```text
y_u + y_v + sum_{cuts crossed by e} y_cut - w_e <= 1.
```

Therefore, multiplying the valid primal inequalities by these nonnegative dual weights gives

```text
|E_selected| >= 3*sum_v y_v + sum_cut y_cut - sum_e w_e
             = 851/4
             = 212.75.
```

Since the left side is an integer, `|E_selected|>=213`. H213 has 213 edges, so **213 is the exact minimum for this specific C650 polar graph.** This certificate is stronger than heuristic failure and stronger than the generic Ota-Hagita `<=272` existence bound.

---

## 4. Exact convex / positive-stress realization of H213

This part is constructive and exact. It proves that the minimum graph is not merely Steinitz-existential.

### Exact Tutte disk

Use the deterministic H213 rotation described above. Choose the triangular face

```text
outer face-id 3 = [1,6,11]
```

under the deterministic face enumeration: scan directed edges lexicographically; an unvisited `u->v` starts a face; at `v`, continue through the predecessor of `u` in the filtered cyclic rotation.

Fix planar boundary positions

```text
p_1  = (-1,-1)
p_6  = ( 1,-1)
p_11 = ( 0, 1).
```

For every other support vertex `v`, solve the exact unit-spring Tutte equations

```text
deg_H(v) * p_v = sum_{w~v} p_w.
```

The 134x134 coefficient matrix is an integer reduced Laplacian, so the unique solution is rational. SymPy 1.14.0 `DomainMatrix.solve_den` solves both coordinates exactly. Canonical exact XY serialization SHA-256:

```text
683b5646c4fffcb1515e551a006f42aa5bab8977ad1aeb573f2af5e8cd8da817
```

### Exact equilibrium stress

Set `omega_e=1` on every non-outer-boundary edge. The three outer-edge stresses are the unique rational values making the three boundary vertices equilibrated:

```text
omega_(1,6)  = -3975020208044236037132700849064167748613055
                /7409136625438368337108070963931321725078284

omega_(1,11) = -33678230867548844273631982400919490673199
                /1058448089348338333872581566275903103582612

omega_(6,11) = -320628155822873462371534760805344222354643
                /2116896178696676667745163132551806207165224
```

All 210 non-boundary stresses are exactly `+1`; all three boundary stresses are strictly negative in this outer-face convention.

### Exact Maxwell lifting

Put the outer face at `z=0`. For a directed edge `u->v` with current face `f` and opposite face `g`, write the face plane as

```text
z = grad_f dot (x,y) + c_f.
```

Using `R90(dx,dy)=(-dy,dx)`, propagate

```text
grad_g - grad_f = omega_uv * R90(p_v-p_u)
c_g - c_f       = -(grad_g-grad_f) dot p_u.
```

Exact equilibrium makes this path-independent. Every lifted support vertex receives the same `z` from all incident face planes. Translate the 137 lifted polar vertices by their exact arithmetic mean; call the resulting vectors `q_i`. The origin is then a strict convex combination of all vertices and lies in the interior.

For every H213 face `F`, the corresponding primal vertex `P_F` is the unique exact solution

```text
q_i dot P_F = 1   for all i in F.
```

The replay verifies all additional incidences exactly and every nonincident inequality strictly. The minimum nonincidence gap is exactly

```text
1382951671074730364861071489704561
/66114220181725757804883126314811016274315
≈ 2.091761299268843e-8 > 0.
```

Thus the actual polar graph is exactly H213. Canonical exact serialization hashes:

```text
lifted/translated polar Q: 28586210ced36d21de5d5070c604dea1b71a2509d3b26025b1e50195e052babc
polar primal P:             20a66a7c67ac79a1eb195f0f9fad866d0d011d568313afcc8fa4b893f574fec5
```

This realization therefore has exact combinatorics

```text
polar  Q: (V,E,F)=(137,213,78)
primal P: (V,E,F)=(78,213,137).
```

---

## 5. True filled-volume centroid and exact mechanics of the H213 realization

The primal is triangulated only for integration inside its true maximal faces. With origin interior, for each oriented triangle `(a,b,c)` the replay uses

```text
dV = det(a,b,c)/6
M  += det(a,b,c)*(a+b+c)/24.
```

There are 152 integration triangles. The exact rational volume is positive; numerically

```text
V ≈ 32757.230152789558.
```

The exact raw filled-volume centroid reconstructed from the rational sums is numerically

```text
c ≈ (-6.947597066931016,
      7.6044355825038465,
    -241.50337104146334).
```

Translate `P` by `-c`. Equivalently normalize the polar support rows by

```text
n_i = q_i / (1 - q_i dot c).
```

All denominators are strictly positive. Mechanics are then checked at the actual own centroid `0`, not at the Tutte/Maxwell construction origin.

### Stable faces

For support `i`, the exact neighbor primitives are

```text
||n_i||^2 - n_j dot n_i,  j~i.
```

Exactly two supports have every primitive strictly positive:

```text
S = [23,53].
```

### Unstable vertices

For primal vertex `x_F` and every true-edge neighbor `x_G`, check

```text
-x_F dot (x_G-x_F) > 0.
```

Exactly two are strict maxima:

```text
U = [2,3].
```

The deterministic face cycles are

```text
face 2 = [0,134,2,67,101,100,34,1,11,10,4,5,8,23,22,32,33,37,36,25,26,27,61,63,62,28,35,98,99,66,31,135,30,136,12,42,41,70,71,45,44,43,38,133]
face 3 = [1,6,11].
```

### True-edge saddles

For each of the 213 true edges, let primal endpoints be `a,b`, `d=b-a`, and let `n_i,n_j` be its two incident support normals. The replay checks all four exact components:

```text
t       = -(a dot d)/(d dot d)
1-t
alpha,beta solving a+t*d = alpha*n_i + beta*n_j.
```

A saddle requires all four strictly positive. Exactly two edges qualify:

```text
H = [(1,11),(56,92)].
```

No face, vertex or edge primitive is zero. Therefore the **exact strict and weak census is `(2,2,2)`**, with zero degeneracies. This is a true homogeneous own-volume-centred nonwinner, not a reference-centre artifact.

---

## 6. Numerical continuation attempts inside the physical realization space

These are intentionally **not** upgraded to impossibility theorems.

* All 32 triangular choices for the unit-weight Tutte outer face were materialized numerically and audited at their own filled centroid. None was `(1,1,0)`; the best class was `(2,2,2)`.
* With outer face `[1,6,11]`, 1,000 positive random spring-weight Tutte/Maxwell realizations (lognormal edge weights with sigma chosen from `0.2,0.5,1,1.5,2`) produced no `(1,1,0)`; best remained `(2,2,2)`.
* On the exact `[1,6,11]` realization after exact own-centering, 1,000,000 random SPD metric samples (random orthogonal eigenbasis, log-eigen spread up to the clipped `[-9,9]` range) never achieved `S=U=1`; the minimum observed pair was `S=2,U=2`. This only says the obvious five-dimensional affine/metric orbit was not enough in that search.
* A separate projective-origin scan also reached only nonwinner cells before its bounded run ended. I do **not** use it as an exclusion.

The precise exact obstruction at the canonical rational point is therefore the two-pair packet `S=[23,53], U=[2,3], H=[(1,11),(56,92)]`, not abstract nonrealizability of H213.

---

## 7. Exact minimum verifier source

Dependency: **Python 3.13.5 standard library only.** It consumes the canonical `C650_polar_edges.txt`, `H213_edges.txt`, and filtered `H213_rotation.txt` supplied in the capsule. The parent graph file is also reproducible by the `A.json` generator above.

```python
#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import hashlib
ROOT=Path(__file__).resolve().parent

def read_edges(name):
    E=[]
    for line in (ROOT/name).read_text().splitlines():
        if line.strip():
            u,v=map(int,line.split()); assert u<v; E.append((u,v))
    assert len(E)==len(set(E))
    return E
G=read_edges('C650_polar_edges.txt')
H=read_edges('H213_edges.txt')
assert len(G)==325 and len(H)==213 and set(H)<=set(G)
assert hashlib.sha256((ROOT/'C650_polar_edges.txt').read_bytes()).hexdigest()=='3039216e06fa3dd0d5790c6cb53cdc79eeb1bed17c98357cbea64c866a6d88fe'
assert hashlib.sha256((ROOT/'H213_edges.txt').read_bytes()).hexdigest()=='171a223c0e2ee52c36ba1076ec588d34aa056cc07efbde2f5d2c6104a805d911'
N=137
adj=[set() for _ in range(N)]
for u,v in H: adj[u].add(v);adj[v].add(u)
assert min(map(len,adj))>=3
for a in range(N):
  for b in range(a+1,N):
    root=next(v for v in range(N) if v not in (a,b)); seen={root}; st=[root]
    while st:
      u=st.pop()
      for v in adj[u]:
        if v not in (a,b) and v not in seen: seen.add(v);st.append(v)
    assert len(seen)==N-2,(a,b)
rot={}
for line in (ROOT/'H213_rotation.txt').read_text().splitlines():
    i,s=line.split(':',1); rot[int(i)]=[int(x) for x in s.strip().split(',') if x]
assert set(rot)==set(range(N))
for i in range(N): assert set(rot[i])==adj[i] and len(rot[i])==len(adj[i])
seen=set(); face_count=0
for u,v in sorted((u,v) for a,b in H for u,v in ((a,b),(b,a))):
  if (u,v) in seen: continue
  face_count+=1; a,b=u,v
  while (a,b) not in seen:
    seen.add((a,b)); rr=rot[b]; k=rr.index(a); a,b=b,rr[(k-1)%len(rr)]
assert len(seen)==2*len(H) and face_count==78 and N-len(H)+face_count==2
deg_groups={
 F(1,4):{42},
 F(3,4):{80},
 F(1):{1,2,4,5,9,10,11,12,22,23,25,26,27,28,30,31,33,34,35,36,37,41,49,56,61,62,63,66,67,70,71,93,98,99,101,109,135,136},
 F(1,2):{0,3,13,14,15,16,17,18,19,20,21,24,38,39,40,43,44,45,46,47,48,50,51,52,53,54,58,59,60,68,69,72,73,74,75,76,77,78,79,83,84,85,86,87,88,89,90,91,92,95,96,97,100,102,103,104,105,106,107,108,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134}
}
ydeg=[F(0) for _ in range(N)]
for w,S in deg_groups.items():
  for v in S: assert ydeg[v]==0; ydeg[v]=w
cuts=[
 (F(1,2),(2,100),{55,67,101}),
 (F(1),(10,34),{1,6,11}),
 (F(1,2),(26,36),{25,65}),
 (F(1,4),(26,41),{12,27,28,30,31,35,42,61,62,63,64,66,80,81,82,98,99,135,136}),
 (F(1),(28,30),{31,35,64,66,98,99,135}),
 (F(1,4),(12,61),{28,30,31,35,62,63,64,66,81,98,99,135,136}),
 (F(1,4),(26,61),{27,82}),
]
wupper={}
def setw(w,pairs):
  for e in pairs:
    e=tuple(sorted(e)); assert e in set(G) and e not in wupper; wupper[e]=w
setw(F(1),[(1,11),(1,34),(2,67),(4,5),(4,10),(10,11),(12,136),(22,23),(25,26),(25,36),(26,27),(27,61),(28,35),(28,62),(30,135),(30,136),(31,66),(31,135),(33,37),(35,98),(36,37),(41,70),(61,63),(62,63),(66,99),(67,101),(70,71),(98,99)])
setw(F(1,2),[(2,134),(3,109),(6,114),(13,71),(34,100),(45,71),(48,49),(49,106),(51,109),(56,92),(56,95),(93,95),(100,101),(109,110)])
setw(F(1,4),[(12,42),(41,42)])
for e in G:
  u,v=e; lhs=ydeg[u]+ydeg[v]
  for w,ban,S in cuts:
    if u not in ban and v not in ban and ((u in S)!=(v in S)): lhs+=w
  lhs-=wupper.get(e,F(0))
  assert lhs<=1,(e,lhs)
bound=3*sum(ydeg)+sum(w for w,_,_ in cuts)-sum(wupper.values())
assert bound==F(851,4)
print('C650_POLAR_MINIMUM_213_EXACT_CERTIFICATE_PASS')
print('G=(137,325), H=(137,213), faces(H)=78, primal abstract=(78,213,137), C=426')
print('LP_dual_lower_bound=',bound,'integer_lower_bound=213')
```

---

## 8. Exact Tutte coordinate builder source

Dependencies: Python 3.13.5 + **SymPy 1.14.0**. It reconstructs the exact rational XY solution and the three exact boundary stresses from H213.

```python
import sympy as sp,time,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent
N=137
E=[tuple(map(int,l.split())) for l in (ROOT/'H213_edges.txt').read_text().splitlines()]
adj=[set() for _ in range(N)]
for u,v in E:adj[u].add(v);adj[v].add(u)
B=[1,6,11]; bpos={1:(-1,-1),6:(1,-1),11:(0,1)}
ints=[v for v in range(N) if v not in B];idx={v:i for i,v in enumerate(ints)}
L=sp.zeros(len(ints)); rx=sp.zeros(len(ints),1);ry=sp.zeros(len(ints),1)
for v in ints:
 i=idx[v];L[i,i]=len(adj[v])
 for w in adj[v]:
  if w in idx:L[i,idx[w]]-=1
  else:rx[i]+=bpos[w][0];ry[i]+=bpos[w][1]
from sympy.polys.matrices import DomainMatrix
from sympy.polys.domains import ZZ
dL=DomainMatrix.from_Matrix(L).convert_to(ZZ)
dR=DomainMatrix.from_Matrix(rx.row_join(ry)).convert_to(ZZ)
num,den=dL.solve_den(dR,method='rref')
S=num.to_Matrix()/int(str(den))
p={B[i]:tuple(map(sp.Rational,bpos[B[i]])) for i in range(3)}
for v in ints:p[v]=(sp.cancel(S[idx[v],0]),sp.cancel(S[idx[v],1]))
bedges=[(1,6),(1,11),(6,11)]
ws=sp.symbols('w0:3'); eq=[]
for v in B:
 rx0=sp.Rational(0);ry0=sp.Rational(0)
 for w in adj[v]:
  e=tuple(sorted((v,w)));dx=p[w][0]-p[v][0];dy=p[w][1]-p[v][1]
  if e in bedges:
   k=bedges.index(e);rx0+=ws[k]*dx;ry0+=ws[k]*dy
  else:rx0+=dx;ry0+=dy
 eq.extend([rx0,ry0])
solw=sp.solve(eq,ws,dict=True)[0]
assert all(sp.simplify(e.subs(solw))==0 for e in eq)
text=''.join(f'{v} {p[v][0]} {p[v][1]}\n' for v in range(N))
(ROOT/'H213_tutte_xy_exact.txt').write_text(text)
assert hashlib.sha256(text.encode()).hexdigest()=='683b5646c4fffcb1515e551a006f42aa5bab8977ad1aeb573f2af5e8cd8da817'
for w in ws: print(w,sp.factor(solw[w]))
```

---

## 9. Exact positive-stress realization / own-centroid mechanics audit source

Dependency: **Python 3.13.5 standard library only** once the exact XY file from the preceding builder exists.

```python
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,collections,sys
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent;N=137
H=[tuple(map(int,l.split())) for l in (ROOT/'H213_edges.txt').read_text().splitlines()]
rot={}
for line in (ROOT/'H213_rotation.txt').read_text().splitlines():
 i,s=line.split(':',1);rot[int(i)]=[int(x) for x in s.strip().split(',')]
seen=set();faces=[];dface={}
for u,v in sorted((u,v) for a,b in H for u,v in ((a,b),(b,a))):
 if (u,v) in seen: continue
 cyc=[];a,b=u,v;fid=len(faces)
 while (a,b) not in seen:
  seen.add((a,b));dface[(a,b)]=fid;cyc.append(a)
  rr=rot[b];k=rr.index(a);c=rr[(k-1)%len(rr)];a,b=b,c
 faces.append(cyc)
assert len(faces)==78 and len(seen)==426
xy={}
for line in (ROOT/'H213_tutte_xy_exact.txt').read_text().splitlines():
 v,x,y=line.split();xy[int(v)]=(F(x),F(y))
stress={e:F(1) for e in H}
stress[(1,6)]=F(-3975020208044236037132700849064167748613055,7409136625438368337108070963931321725078284)
stress[(1,11)]=F(-33678230867548844273631982400919490673199,1058448089348338333872581566275903103582612)
stress[(6,11)]=F(-320628155822873462371534760805344222354643,2116896178696676667745163132551806207165224)
outer_f=next(i for i,c in enumerate(faces) if set(c)=={1,6,11} and len(c)==3)
fadj=collections.defaultdict(list)
for u,v in H:
 a=dface[(u,v)];b=dface[(v,u)];fadj[a].append((b,u,v));fadj[b].append((a,v,u))
planes={outer_f:((F(0),F(0)),F(0))};dq=collections.deque([outer_f])
while dq:
 f=dq.popleft();(gx,gy),cc=planes[f]
 for g,u,v in fadj[f]:
  if g in planes: continue
  dx=xy[v][0]-xy[u][0];dy=xy[v][1]-xy[u][1];w=stress[tuple(sorted((u,v)))]
  dg=(-w*dy,w*dx);planes[g]=((gx+dg[0],gy+dg[1]),cc-dg[0]*xy[u][0]-dg[1]*xy[u][1]);dq.append(g)
assert len(planes)==78
for u,v in H:
 a=dface[(u,v)];b=dface[(v,u)]
 for t in (u,v):
  vals=[]
  for f in (a,b):
   (gx,gy),cc=planes[f];vals.append(gx*xy[t][0]+gy*xy[t][1]+cc)
  assert vals[0]==vals[1]
Q=[]
for v in range(N):
 vals=[]
 for f,c in enumerate(faces):
  if v in c:
   (gx,gy),cc=planes[f];vals.append(gx*xy[v][0]+gy*xy[v][1]+cc)
 assert vals and all(z==vals[0] for z in vals);Q.append((xy[v][0],xy[v][1],vals[0]))
s=tuple(sum(q[k] for q in Q)/N for k in range(3));q=[tuple(Q[i][k]-s[k] for k in range(3)) for i in range(N)]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(a,t):return tuple(x*t for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det3(a,b,c):return dot(a,cross(b,c))
def solve3(A):
 d=det3(A[0],A[1],A[2]);assert d
 num=add(add(cross(A[1],A[2]),cross(A[2],A[0])),cross(A[0],A[1]));return mul(num,F(1,d))
P=[]
for cyc in faces:
 tri=None
 for i in range(len(cyc)-2):
  for j in range(i+1,len(cyc)-1):
   for k in range(j+1,len(cyc)):
    if det3(q[cyc[i]],q[cyc[j]],q[cyc[k]])!=0:tri=(cyc[i],cyc[j],cyc[k]);break
   if tri:break
  if tri:break
 p=solve3([q[i] for i in tri]);assert all(dot(q[i],p)==1 for i in cyc);P.append(p)
min_gap=None
for f,cyc in enumerate(faces):
 inc=set(cyc)
 for i in range(N):
  z=1-dot(q[i],P[f])
  if i in inc:assert z==0
  else:assert z>0;min_gap=z if min_gap is None or z<min_gap else min_gap
inc_faces=[]
for i in range(N):
 cyc=[dface[(i,j)] for j in rot[i]]
 if len(cyc)>=3:
  a,b,c=P[cyc[0]],P[cyc[1]],P[cyc[2]]
  if dot(cross(sub(b,a),sub(c,a)),q[i])<0:cyc=list(reversed(cyc))
 inc_faces.append(cyc)
V=F(0);M=[F(0),F(0),F(0)];tri_count=0
for cyc in inc_faces:
 a=P[cyc[0]]
 for k in range(1,len(cyc)-1):
  b=P[cyc[k]];c=P[cyc[k+1]];d=det3(a,b,c);assert d>0;V+=d/F(6);tri_count+=1
  for j in range(3):M[j]+=d*(a[j]+b[j]+c[j])/F(24)
cent=tuple(x/V for x in M);X=[sub(p,cent) for p in P]
h=[F(1)-dot(qi,cent) for qi in q];assert min(h)>0;n=[mul(q[i],F(1,h[i])) for i in range(N)]
adj=[set() for _ in range(N)]
for u,v in H:adj[u].add(v);adj[v].add(u)
stable=[];weakS=[];face_zero=0
for i in range(N):
 vals=[dot(n[i],n[i])-dot(n[j],n[i]) for j in adj[i]]
 if all(z>0 for z in vals):stable.append(i)
 if all(z>=0 for z in vals):weakS.append(i)
 face_zero+=sum(z==0 for z in vals)
fneigh=[set() for _ in faces]
for u,v in H:
 a=dface[(u,v)];b=dface[(v,u)];fneigh[a].add(b);fneigh[b].add(a)
unstable=[];weakU=[];vertex_zero=0
for f,x in enumerate(X):
 vals=[-dot(x,sub(X[g],x)) for g in fneigh[f]]
 if all(z>0 for z in vals):unstable.append(f)
 if all(z>=0 for z in vals):weakU.append(f)
 vertex_zero+=sum(z==0 for z in vals)
saddles=[];weakH=[];edge_zero=0
for u,v in H:
 f=dface[(u,v)];g=dface[(v,u)];a=X[f];d=sub(X[g],X[f]);dd=dot(d,d);t=-dot(a,d)/dd;z=add(a,mul(d,t));ni=n[u];nj=n[v];aa=dot(ni,ni);bb=dot(ni,nj);cc=dot(nj,nj);rr=dot(z,ni);ss=dot(z,nj);D=aa*cc-bb*bb;assert D>0
 al=(rr*cc-ss*bb)/D;be=(ss*aa-rr*bb)/D;vals=(t,1-t,al,be);edge_zero+=sum(x==0 for x in vals)
 if all(x>0 for x in vals):saddles.append((u,v))
 if all(x>=0 for x in vals):weakH.append((u,v))
assert stable==[23,53] and unstable==[2,3] and saddles==[(1,11),(56,92)]
assert [len(weakS),len(weakU),len(weakH)]==[2,2,2] and [face_zero,vertex_zero,edge_zero]==[0,0,0]
assert min_gap==F(1382951671074730364861071489704561,66114220181725757804883126314811016274315)
print('EXACT H213 REALIZATION')
print('polar n,m,f',N,len(H),len(faces),'min noninc gap',min_gap)
print('volume',V,'centroid',cent,'triangulation',tri_count)
print('class',len(stable),len(unstable),len(saddles),'S',stable,'U',unstable,'H',saddles)
print('weak',len(weakS),len(weakU),len(weakH),'zeros',face_zero,vertex_zero,edge_zero)
```

---

## 10. Most useful continuation

1. **Do not spend more effort on pure sparsification of this fixed graph.** `213` is now the exact minimum, with an exact dual lower-bound certificate. Any 214–249 graph is a deliberate mechanical relaxation, not a topology necessity.
2. **Use H213 as the primary physical skeleton.** The exact Maxwell point is a clean rational interior realization with positive nonincidence gap and no degeneracies. Work in the full realization equations `q_i dot p_F = 1` for the 426 vertex-face incidences. Before gauge there are 411 polar-coordinate variables plus 234 primal-face-plane/vertex variables against 426 incidence equations, so the full realization space is far larger than the five-dimensional metric orbit already screened.
3. **Target the exact two-pair packet directly.** Keep one stable and one unstable owner and drive the other stable/unstable plus both saddles through a death-before-birth cell while preserving all nonincidence signs. Recompute the *filled* centroid inside every actual incidence cell; do not mechanically recenter only at the end and assume signs survive.
4. **If H213 itself appears mechanically blocked, add back a small number of C650 edges strategically.** Since 213 is 36 edges below the requested 249 threshold, there is substantial room to regain realization freedom while still beating `C498`. Choose returned edges by the exact packet stars / mass Jacobian, not by generic degree.
5. A promising exact solver chart is bilinear incidence plus hard moment closure: unknown rational/numerical `q_i,p_F`, equations `q_i·p_F=1` on H incidences, strict `q_j·p_F<1` off incidence, three true volume moments, and selected strict face/vertex/four-edge-cone inequalities. The exact Tutte realization above is a certified starting point. Positive spring weights, projective origin and SPD metric can remain secondary controls rather than the whole search space.
6. The durable C650 exact support coordinates remain valuable as a second initialization: solve the H213 coplanarity/incidence equations with a proximity objective to the accepted C650 support table. That route is more likely to inherit the original strict110 mechanics than the canonical Tutte realization, but it needs a sparse bilinear/continuation solver rather than a dense generic least-squares call.

---

## 11. Recovery capsule / hashes

Supplemental complete archive:

Download `C650_POLAR_MIN213_CLEAR_LYNX14.zip`

```text
size   = 601188 bytes
SHA256 = df78617a54cb258a629de4077dac9657e9b24198a16a45476ad63c53ca5ca9d1
```

It contains the entire decoded 17-file durable C650/PAIR recovery package; exact C650/H213 edge, rotation and face data; the three complete replay sources above; exact Tutte XY, lifted Q and primal P serializations; exact dual-certificate material; bounded heuristic search sources; logs and SHA256SUMS.

Canonical exact object hashes:

```text
C650 polar G edges   3039216e06fa3dd0d5790c6cb53cdc79eeb1bed17c98357cbea64c866a6d88fe
H213 edges           171a223c0e2ee52c36ba1076ec588d34aa056cc07efbde2f5d2c6104a805d911
H213 rotation        84a66b01a7ca3211da3e4bef6c0a616e07c75fa821630b493ed9465ad9dddf0e
H213 faces           014c7bb6258de3ad9d386d9046d61ee3d8f866a9f769974bec57ad6193d285da
exact Tutte XY       683b5646c4fffcb1515e551a006f42aa5bab8977ad1aeb573f2af5e8cd8da817
exact Maxwell Q      28586210ced36d21de5d5070c604dea1b71a2509d3b26025b1e50195e052babc
exact polar P        20a66a7c67ac79a1eb195f0f9fad866d0d011d568313afcc8fa4b893f574fec5
```

Replay commands:

```bash
python3 -S VERIFY_MIN213.py
python3 BUILD_TUTTE_XY.py
python3 -S REALIZE_AUDIT_H213.py
```

Observed exact terminal markers / summaries:

```text
C650_POLAR_MINIMUM_213_EXACT_CERTIFICATE_PASS
G=(137,325), H=(137,213), faces(H)=78, primal abstract=(78,213,137), C=426
LP_dual_lower_bound=851/4 integer_lower_bound=213

EXACT H213 REALIZATION
polar n,m,f 137 213 78
class 2 2 2 S [23,53] U [2,3] H [(1,11),(56,92)]
weak 2 2 2 zeros 0 0 0
```

**Disposition:** H213 is **USED** as the exact graph-theoretic minimum and as an exact convex/homogeneous own-centred physical nonwinner. It is not a Gömböc and must not be promoted as `(1,1,0)` without a new realized mechanical chamber and a fresh full exact audit.
