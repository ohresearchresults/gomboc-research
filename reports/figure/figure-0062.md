# figure-0062

AI research report · 2026-08-25 UTC

---

# Radial PL–Morse search — final mathematical determination

## Verdict

**Fallback. No own-centroid homogeneous polyhedral Gömböc was found.** The exact final body is a finite rational convex polyhedron with exact uniform-volume centroid at the origin and strict incidence separation, but its actual equilibrium class is **`(S,U,H)=(2,3,3)`**, not `(1,1,0)`. That fails the run's explicit acceptance gate, which excludes artificial centers, wall points, and incomplete graph-only audits. :contentReference[oaicite:0]{index=0} This resolves the ambiguity noted after the prior wrapper-only result. :contentReference[oaicite:1]{index=1}

Literal `OUTCOME.json`:

```json
{
  "outcome": "fallback",
  "headline": "STRONGEST MATERIALIZED RADIAL PL-MORSE NEAR-REALIZATION (NO WINNER IN THIS DIRECTION)",
  "primary_source": "projective_n16.npz:points",
  "primary_counts": [
    2,
    3,
    3
  ],
  "vertices": 16,
  "edges": 42,
  "maximal_faces": 28,
  "hard_score": -0.5663819905515062,
  "radius": {
    "absolute_fraction": "1840113847577893/11258999068426240000000",
    "absolute": 1.6343494092100502e-07,
    "normalized": 2.324997244714258e-07,
    "method": "mpmath.iv enclosure of recentered volume centroid, all support determinants, and every equilibrium witness"
  },
  "exact_volume": "519505763641569373/6000000000000000000",
  "minimum_raw_convexity_separation": "692804337163/1000000000000000000",
  "auxiliary_source": "cap_actual_1.npz:points",
  "coherent_projective_source": "projective_bridge_out.npz"
}
```

`candidate.json` also says `outcome="fallback"`, stores `expected_counts=[2,3,3]`, and has `tree_cotree_matching=null`; `matching.json` is literally `null`. The selected fallback is not a near-zero wall: a positive interval perturbation ball preserves its wrong `(2,3,3)` class.

## Independent exact-verifier result

The archived `Fraction` verifier was rerun after unpacking its dependencies:

```json
{
  "verified": true,
  "counts": [2,3,3],
  "vertices": 16,
  "maximal_faces": 28,
  "true_edges": 42,
  "volume_exact": "519505763641569373/6000000000000000000",
  "centroid_exact": ["0","0","0"],
  "moment4_exact": ["0","0","0"]
}
```

A separately written standard-library reconstruction printed:

```text
V,E,F = 16 42 28
volume = 519505763641569373/6000000000000000000
moment4 = (0,0,0); centroid = (0,0,0)
stable faces = [(0,1,7),(4,8,13)]
unstable vertices = [0,1,7]
saddle edges = [(0,(0,1)),(2,(0,7)),(6,(1,7))]
(S,U,H) = (2,3,3)
minimum raw support separation = 692804337163/1000000000000000000
```

## Exact finite reconstruction

Use the following integer-millionth points `q_i`:

```text
0  (353027,-641390,875161)
1  (42690,399014,-1927087)
2  (126761,-315378,239459)
3  (6498,-160717,227747)
4  (-144327,55825,75828)
5  (17321,-166216,92745)
6  (-18908,-129710,288695)
7  (-315906,284372,1188068)
8  (-65313,-50933,-17336)
9  (-91362,-10590,-32735)
10 (-40780,-87242,41860)
11 (-37623,-57618,-157023)
12 (-76615,-8363,-131343)
13 (-37152,-101957,209016)
14 (34652,-196176,210910)
15 (151554,-367414,584897)
```

Define

```text
C_x =  39389134183774743/207802305456627749200000
C_y = -577143018991064971/2078023054566277492000000
C_z =  104135886676119513/1039011527283138746000000
v_i = q_i/10^6 - C  (coordinatewise).
```

This compact formula expands all 48 exact rational V-coordinates. The exact outward maximal-face cycles are:

```text
F00 0 1 7
F01 2 1 0
F02 3 5 14
F03 3 14 15
F04 4 7 1
F05 4 13 7
F06 5 11 2
F07 6 3 15
F08 6 13 3
F09 6 15 7
F10 8 11 5
F11 8 13 4
F12 9 8 4
F13 10 5 3
F14 10 8 5
F15 10 13 8
F16 11 1 2
F17 11 8 9
F18 11 9 12
F19 11 12 1
F20 12 4 1
F21 12 9 4
F22 13 6 7
F23 13 10 3
F24 14 2 15
F25 14 5 2
F26 15 0 7
F27 15 2 0
```

All 28 maximal faces are triangles, so this is also the boundary triangulation. For each cycle `(i,j,k)`, set

```text
N=(v_j-v_i)×(v_k-v_i),  h=N·v_i,  and use N·x<=h.
```

Every listed orientation has `h>0`. To obtain the exact primitive integer H-row, clear the four denominators in `(N_x,N_y,N_z,h)`, divide by their integer gcd, and reverse signs only if the final `H` is negative. This deterministic generator reproduces every archived H-plane; no unexpanded geometric choice remains.

Complete true-edge/maximal-face incidence:

```text
E00 0-1 : F00,F01  SADDLE
E01 0-2 : F01,F27
E02 0-7 : F00,F26  SADDLE
E03 0-15 : F26,F27
E04 1-2 : F01,F16
E05 1-4 : F04,F20
E06 1-7 : F00,F04  SADDLE
E07 1-11 : F16,F19
E08 1-12 : F19,F20
E09 2-5 : F06,F25
E10 2-11 : F06,F16
E11 2-14 : F24,F25
E12 2-15 : F24,F27
E13 3-5 : F02,F13
E14 3-6 : F07,F08
E15 3-10 : F13,F23
E16 3-13 : F08,F23
E17 3-14 : F02,F03
E18 3-15 : F03,F07
E19 4-7 : F04,F05
E20 4-8 : F11,F12
E21 4-9 : F12,F21
E22 4-12 : F20,F21
E23 4-13 : F05,F11
E24 5-8 : F10,F14
E25 5-10 : F13,F14
E26 5-11 : F06,F10
E27 5-14 : F02,F25
E28 6-7 : F09,F22
E29 6-13 : F08,F22
E30 6-15 : F07,F09
E31 7-13 : F05,F22
E32 7-15 : F09,F26
E33 8-9 : F12,F17
E34 8-10 : F14,F15
E35 8-11 : F10,F17
E36 8-13 : F11,F15
E37 9-11 : F17,F18
E38 9-12 : F18,F21
E39 10-13 : F15,F23
E40 11-12 : F18,F19
E41 14-15 : F03,F24
```

Thus `(V,E,F)=(16,42,28)`, Euler gives `16-42+28=2`, and mechanical complexity is `16+42+28-2=84`.

## Exact own-centroid and convexity certificate

For the outward boundary triangles, let

```text
D = sum det(v_i,v_j,v_k),
M = sum det(v_i,v_j,v_k)(v_i+v_j+v_k).
```

Exact arithmetic gives

```text
D      = 519505763641569373/1000000000000000000
Volume = D/6 = 519505763641569373/6000000000000000000
       ≈ 0.08658429394026156216666666667
M      = (0,0,0)
centroid = M/(4D) = (0,0,0).
```

All exact face supports are positive, so the origin is strictly interior. With raw cross-product normals, the minimum nonincident slack is

```text
692804337163/1000000000000000000 = 6.92804337163e-7,
```

attained at both `(F17,V12)` and `(F18,V8)`. The minimum scale-invariant origin-to-support-plane distance is `0.0349115090165677`, at `F00`.

## Complete equilibrium outcome and margins

The exact classifier uses:

- face: the orthogonal projection `hN/(N·N)` must satisfy every oriented in-face edge predicate;
- vertex: `v_i·(v_i-v_j)>0` for every true neighbor;
- edge: its foot must have `0<t<1` and lie in the strict positive cone of the two incident maximal-face normals (`alpha>0,beta>0`).

It evaluated all 28 maximal faces, all 16 vertices with their complete true-neighbor sets, and all 42 true edges/full normal cones. The only equilibria are:

```text
stable:   F00=(0,1,7), F11=(8,13,4)
unstable: V0, V1, V7
saddles:  E00=(0,1), E02=(0,7), E06=(1,7)
```

The selector's intended pair is `F00,V1`:

- `F00`: signs `+++`; exact minimum predicate `66123660273420517231375842960552451382487/16234555113799042906250000000000000000000>0`; normalized margin `+0.18902710743054488`.
- `V1`: signs `++++++`; exact minimum predicate `3737011446237282148207175176829/1039011527283138746000000000000>0`; normalized margin `+0.9808154726231694`.

Every unwanted equilibrium, with decisive exact signs, is:

1. **Extra stable `F11=(8,13,4)`**: `+++`; exact minimum `30084590659019034680336429164237427799/519505763641569373000000000000000000000000>0`; normalized `+0.03119590389545555`.
2. **Extra unstable `V0`**, neighbors `(1,2,7,15)`: `++++`; exact minimum `104083699685082904880974444723/207802305456627749200000000000>0`; normalized `+0.41153659935710923`.
3. **Extra unstable `V7`**, neighbors `(0,1,4,6,13,15)`: `++++++`; exact minimum `879352741498554687672443572003/1039011527283138746000000000000>0`; normalized `+0.5663819905515062`.
4. **Saddle `E00=(0,1)`**, incident to `F00,F01`: `++++`; `t=3355258723969303032814977600581/9383669889362654103524816037594; 1-t=6028411165393351070709838437013/9383669889362654103524816037594; alpha=2019144119789791596693711091343333825977750000/9046711798953080810235586404929090894130666387; beta=4007494562025485892810657149124390992878000000/2467285036078112948246069019526115698399272651`; normalized `+0.35756359329869764`.
5. **Saddle `E02=(0,7)`**, incident to `F00,F26`: `++++`; `t=577775134107735121878574961369/1457127875606289809551018533372; 1-t=879352741498554687672443572003/1457127875606289809551018533372; alpha=11623083125402037348576134659365038808489437500/5060372722208955067165766730308228597848999809; beta=94492806812906118933485926875604548826884687500/5060372722208955067165766730308228597848999809`; normalized `+0.39651642369914264`.
6. **Saddle `E06=(1,7)`**, incident to `F00,F04`: `++++`; `t=1050133661815092775233141162994/1705004851291314138449450288355; 1-t=654871189476221363216309125361/1705004851291314138449450288355; alpha=145882996786903904090047581212171069721770000/612542082373883927178209326589261895099848371; beta=637406701011844822227066535704844218883212000/612542082373883927178209326589261895099848371`; normalized `+0.3840875813228588`.

Every other feature has at least one exact negative predicate. The nearest non-equilibrium walls are face `F10=(8,11,5)` at `-0.016986461066200196`, edge `E35=(8,11)` at `-0.0469197174638131`, and vertex `V8` at `-0.0790473295042838`. Hence the actual class's minimum absolute normalized all-feature sign margin is `0.016986461066200196`; its minimum positive equilibrium margin is `0.03119590389545555`.

The target-oriented hard components are:

```json
{
  "target_face": 0.18902710743054488,
  "other_faces": -0.03119590389545555,
  "target_vertex": 0.9808154726231694,
  "other_vertices": -0.5663819905515062,
  "edges": -0.39651642369914264,
  "origin": 0.017735752005462277
}
```

and the hard score is `-0.5663819905515062`, dominated by extra maximum `V7`. The Morse identity checks: `S+U-H=2+3-3=2`.

## Directed interval perturbation certificate

The interval audit put independent `L_infinity` boxes around all 48 coordinates, recomputed interval volume and centroid, recentered the boxes, and then enclosed every support determinant and every face/vertex/edge equilibrium witness. It certified

```text
r_low = 1840113847577893/11258999068426240000000
      = 1.6343494092100502e-7
normalized by RMS radius = 2.324997244714258e-7.
```

A rerun gave `passes(r_low)=True`. The next binary endpoint

```text
r_high = 920056923788951/5629499534213120000000
       = 1.6343494092100582e-7
       = r_low + 9/11258999068426240000000
```

returned `False`. That upper failure is only enclosure conservatism; the positive lower endpoint certifies a nonzero open `(2,3,3)` chamber.

## Actual smallest coupled obstruction

Relative to retaining target `F00,V1`, the required change is one `S-H` cancellation and two `U-H` cancellations. All three saddles are exactly the three boundary edges of `F00`, and all three vertices of `F00` are unstable. The extra stable face connects to that triangle through the shortest dual strip

```text
F11=[8,13,4] --E23=[4,13]-- F05=[4,13,7]
                --E19=[4,7] -- F04=[4,7,1]
                --E06=[1,7] -- F00=[0,1,7].
```

The smallest remaining coupled geometric block is therefore `F11`, this four-face strip, the complete saddle boundary `E00,E02,E06` of `F00`, and extra maxima `V0,V7`. A single edge flip or one local pair cancellation can only transfer the defect; a new connected topology must perform all three cancellations while simultaneously preserving zero first moment.

## Auxiliary and projective artifacts do not hide a winner

The auxiliary radial PL–Morse body has `origin_reference_counts=[1,1,0]` and origin hard score `+0.024882597990616467`, but its exact own centroid is

```text
(-4602219476730606988093879/5905327935904546228000000,
 -18063487533767456524791/38384631583379550482000000,
 33181789312942365875436983/76769263166759100964000000)
```

and its own-centroid class is `[4,8,10]`; it is only an artificial-center realization.

Literal `projective_bridge.json`:

```json
{
  "source_file": "projective_bridge_out.npz",
  "parameter_a": [
    -8.048081497725992,
    -6.392537041068807,
    -2.785187083802077
  ],
  "denominator_min": 0.43221391686360555,
  "map_residual_max": 0.0,
  "centered_centroid_residual": 0.002994652008916864,
  "auxiliary_origin_counts": [
    8,
    1,
    7
  ],
  "centered_own_counts": [
    5,
    4,
    7
  ],
  "centered_hard_score": -0.5433857317125519
}
```

So that bridge endpoint is not exactly centered and is `[5,4,7]`, not `(1,1,0)`. The prose report's separate claim of a centered `(1,2,1)` bridge is contradicted by this machine artifact and is not accepted. The final outcome, candidate, incidence, and exact verifier all agree on `(2,3,3)`.

## Self-contained independent verifier

The following stock-Python script contains the exact generator and independently enumerates all supporting triples, maximal faces, true edges, volume/centroid, and full equilibrium cones. Its decisive output is the transcript above.

```python
from fractions import Fraction as F
from itertools import combinations
from math import gcd
from functools import reduce
Q=[(353027,-641390,875161),(42690,399014,-1927087),(126761,-315378,239459),(6498,-160717,227747),(-144327,55825,75828),(17321,-166216,92745),(-18908,-129710,288695),(-315906,284372,1188068),(-65313,-50933,-17336),(-91362,-10590,-32735),(-40780,-87242,41860),(-37623,-57618,-157023),(-76615,-8363,-131343),(-37152,-101957,209016),(34652,-196176,210910),(151554,-367414,584897)]
c=(F(39389134183774743,207802305456627749200000),F(-577143018991064971,2078023054566277492000000),F(104135886676119513,1039011527283138746000000))
P=[tuple(F(x,10**6)-c[j] for j,x in enumerate(q)) for q in Q]
sub=lambda a,b:tuple(x-y for x,y in zip(a,b)); mul=lambda s,a:tuple(s*x for x in a)
dot=lambda a,b:sum((x*y for x,y in zip(a,b)),F(0))
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
# exact complete hull enumeration
G={}
for I in combinations(range(len(P)),3):
 a,b,d=(P[i] for i in I); n=cross(sub(b,a),sub(d,a))
 if n==(0,0,0):continue
 s=[dot(n,sub(x,a)) for x in P]
 if all(x<=0 for x in s):pass
 elif all(x>=0 for x in s):n=mul(-1,n);s=[-x for x in s]
 else:continue
 inc=tuple(i for i,x in enumerate(s) if x==0)
 if len(inc)>=3:G[inc]=n
assert len(G)==28 and all(len(x)==3 for x in G)
faces=[]
for inc,n in G.items():
 i,j,k=inc;a,b,d=P[i],P[j],P[k]
 if dot(cross(sub(b,a),sub(d,a)),n)<0:j,k=k,j
 n=cross(sub(P[j],P[i]),sub(P[k],P[i]));h=dot(n,P[i])
 assert h>0 and all(h-dot(n,x)>=0 for x in P)
 faces.append(((i,j,k),n,h))
faces.sort(key=lambda z:tuple(sorted(z[0])))
# exact volume and first moment
D=sum(det(P[i],P[j],P[k]) for (i,j,k),n,h in faces)
M=tuple(sum(det(P[i],P[j],P[k])*(P[i][r]+P[j][r]+P[k][r]) for (i,j,k),n,h in faces) for r in range(3))
# edges and exact support separation
ef={};sep=[]
for fi,(f,n,h) in enumerate(faces):
 for e in combinations(f,2):ef.setdefault(tuple(sorted(e)),[]).append(fi)
 for i,p in enumerate(P):
  if i not in f:sep.append(h-dot(n,p))
edges=sorted(ef);assert len(edges)==42 and all(len(ef[e])==2 for e in edges) and min(sep)>0
# stable faces: projection q=h*n/|n|^2 and three oriented edge predicates
stable=[]
for fi,(f,n,h) in enumerate(faces):
 q=mul(h/dot(n,n),n); ok=True
 for a,b in zip(f,f[1:]+f[:1]):ok &= dot(cross(sub(P[b],P[a]),sub(q,P[a])),n)>0
 if ok:stable.append(tuple(sorted(f)))
# unstable vertices: v.(v-w)>0 on every true incident edge
nb=[set() for _ in P]
for i,j in edges:nb[i].add(j);nb[j].add(i)
unstable=[i for i,v in enumerate(P) if all(dot(v,sub(v,P[j]))>0 for j in nb[i])]
# saddle edges: interior foot and positive two-face normal-cone coefficients
saddles=[]
for ei,(i,j) in enumerate(edges):
 a,b=P[i],P[j];d=sub(b,a);dd=dot(d,d);t=-dot(a,d)/dd;q=tuple(a[r]+t*d[r] for r in range(3));f1,f2=ef[(i,j)];n1,n2=faces[f1][1],faces[f2][1]
 A,B,C=dot(n1,n1),dot(n1,n2),dot(n2,n2);r1,r2=dot(n1,q),dot(n2,q);g=A*C-B*B;alpha=(r1*C-r2*B)/g;beta=(r2*A-r1*B)/g
 assert tuple(alpha*n1[r]+beta*n2[r] for r in range(3))==q
 if 0<t<1 and alpha>0 and beta>0:saddles.append((ei,(i,j),t,alpha,beta))
print('V,E,F =',len(P),len(edges),len(faces))
print('volume =',D/6)
print('moment4 =',M,'centroid =',tuple(x/(4*D) for x in M))
print('stable faces =',stable)
print('unstable vertices =',unstable)
print('saddle edges =',[(i,e) for i,e,t,a,b in saddles])
print('(S,U,H) =',(len(stable),len(unstable),len(saddles)))
print('minimum exact cross-product support separation =',min(sep))
```

## OBJ/STL reconstruction

After evaluating the exact `v_i`, write OBJ lines `v float(x) float(y) float(z)` and, for each outward face cycle `(i,j,k)`, `f i+1 j+1 k+1`. For ASCII STL, use the same cycles; the outward facet normal is the normalized vector `(v_j-v_i)×(v_k-v_i)`. These instructions reconstruct the same finite mesh geometry. Original artifact hashes are:

```text
ZIP       1b5e333b358f1f7d0a7284e3a3952c3bacffa4452defb7e3fdd571cf71bf51c2
OUTCOME   3e91fa5431872c50678a95cc6b1acac17bad43fe373794cc7d4955b85c02dc01
candidate a6213d6835fb5bff86d41fe27e923d413cbcc7105af890914bc44d36d7994e57
incidence 61a6578cff701c126ccc12979b9a076c034154f65485747be6725e6b0907e603
OBJ       bf21f90cba691d65440ea076e8386c091deca7119dddb3d51b2d697d52c1716f
STL       e24145e802fc8b1b1f8efcc8ced4b8e9db6b29c77e4f9feedd21cf0e7a3b0631
```

## Conclusion

This direction materialized a small exact rational own-centered polyhedron of complexity `84`, with complete actual incidence, exact zero first moment, positive raw support separation, exact full-cone equilibrium classification, and a directed interval perturbation certificate. It is nevertheless **decisively a fallback**: strict class `(2,3,3)`, with one extra stable face, two extra unstable vertices, and three strict saddle edges. The nonredundant continuation is a centroid-coupled replacement of the whole `F11→F00` strip and the three-edge saddle triangle, not further fixed-cell polishing.
