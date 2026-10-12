# figure-0470

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Quiet Finch 32 — exact C40 fixed-profile mono-U atlas and a certified raw-profile interval

## Outcome

I completed the requested **finite 315,000 rooted-tree atlas** for the literal raw profile underlying `C40_PACKET2X2_COARSE100`. The result is an exact scoped obstruction, not a numerical screen:

> **For this fixed raw C40 profile, no SPD Gram matrix can give strict `U=1` with additional-weak-U `=0`. Therefore no invertible affine image of this fixed raw shape can be strict `110/weak000`.**

The parent body itself remains the already-audited exact `V10/E20/F12/C40`, strict `(S,U,H)=(2,2,2)`, weak `000`, with `S=[0,9]`, `U=[1,3]`, and explicit mixed saddles `H=[[0,3],[5,6]]`; I do **not** infer H from Morse count. Its complete physical and same-centre-polar packets are the exact 2-node packets recorded by the parent.

Because the exact atlas excludes every weak-free U1 metric for this fixed raw geometry, there is no rational feasible U1 Gram matrix on which a further S/H audit could produce a candidate. I therefore do not manufacture a full-orbit S/H claim: the new theorem is an exact U-side affine-orbit obstruction sufficient to exclude `110/weak000` on this profile.

I then made the requested **controlled raw-profile change**, varying only `kappa[0][0]=t` while fixing both knots and the other seven curvature coefficients. Using exact polynomial matrices and Bernstein certificates, I prove the same affine U1 obstruction for **every real `t` in the closed interval `[99/100,103/100]`**. All curvatures stay positive there, so the support-stack chart retains `V10/E20/F12/C40` by the positive-curvature incidence theorem. This closes a genuine one-parameter C40 subchart across *all* SPD affine metrics; it is not another finite metric sample and does not reuse the sterile shear ray.

No strict `110/weak000` C40 body is promoted in this handoff.

## 1. Source authority and literal profile

The continuation parent is immutable `figure-0466`, SHA-256
`7939f2aab5f6b71911d2546a87ee7e3888f045b957e7fec261e0531f15272b63`. Its literal `C40_PACKET2X2_COARSE100` data are:

~~~text
knots = [19/25, 81/100]
kappa = [
  [103/100, 7/50],
  [54/5,    119/25],
  [53/25,   971/100],
  [21/100,  17/100]
]

parent presentation affine map A =
[3/4,   0,      0]
[13/10, 99/50,  0]
[23/20, 97/100, 17/25]
~~~

The fixed-geometry atlas works in the **raw** profile and replaces the presentation `A` by an arbitrary SPD Gram matrix `G=A^T A`; this is exactly the fixed-shape reduction recorded in the branch.

The verifier independently reconstructs the raw profile and checks

~~~text
raw volume = 470168128829/250000000000
raw centroid = (
  1037375653957897/1116346962000000,
 -151195195979711/223269392400000,
  23905595267/37211565400
)
true V/E/F/C = 10/20/12/40
true undirected edges = 20
spanning trees = 31500
root-labelled spanning trees = 315000
~~~

The true graph is the ten-vertex C40 stack graph already used by the exact tree reduction. The supplied metric material establishes why weak-free mono-U is exactly a finite rooted-tree sign problem: a positive escape strictly increases squared `G`-radius, so one positive escape chosen from every nonroot forms an acyclic tree directed to the sole strict-U root.

## 2. Exact blocker certificate for all 315,000 rooted trees

For centered raw vertex `p_i=x_i-c` and directed true-edge vector `e_ij=x_j-x_i`, define

~~~text
D_ij(G) = p_i^T G e_ij
B_ij    = p_i e_ij^T + e_ij p_i^T
~~~

so exactly

~~~text
tr(B_ij G) = 2 D_ij(G).
~~~

If a required set of positive arrows has equal-weight matrix sum

~~~text
S = sum B_ij
~~~

with `S` negative definite, then no SPD `G` can satisfy those arrow signs: every required arrow would give `tr(B_ij G)>0`, hence `tr(SG)>0`, while `S<0` and `G>0` imply `tr(SG)<0`.

The verifier exhaustively evaluates exact Fraction matrices for all 40 directed true edges and obtains:

~~~text
negative-definite 2-arrow blockers: 0
negative-definite 3-arrow blockers: 774
canonical lex-first triplets actually used in the tree cover: 558
~~~

Those triplets cover **314,967 / 315,000** rooted trees. Root-by-root exact coverage is

~~~text
root 0: 31467 by triplets + 33 residual = 31500
root 1: 31500 by triplets
root 2: 31500 by triplets
root 3: 31500 by triplets
root 4: 31500 by triplets
root 5: 31500 by triplets
root 6: 31500 by triplets
root 7: 31500 by triplets
root 8: 31500 by triplets
root 9: 31500 by triplets
~~~

All 33 residual root-0 trees contain the common six-arrow backbone

~~~text
3->0, 1->5, 2->3, 6->2, 5->9, 9->6.
~~~

For the literal base profile, the four-arrow subset

~~~text
3->0, 2->3, 6->2, 9->6
~~~

has a negative-definite equal-weight sum. Exact Sylvester certificate for `-S`:

~~~text
-S00 = 389001795661/31250000000 > 0
leading 2x2 minor =
  2058049473739321656751/30517578125000000000 > 0
-det(S) =
  1770828329375200626923085614345606385675163
  /15577881744582868050000000000000000000000000 > 0
~~~

so it kills all remaining 33 trees. The root-exit negativity inequalities are not even needed for the contradiction.

This proves the exact fixed-profile statement:

~~~text
NO SPD G HAS strict U=1 AND additional-weak-U=0
FOR C40_PACKET2X2_COARSE100.
~~~

The result intentionally does **not** claim that a boundary metric with one strict U plus extra weak-U events is absent. Such a boundary is unacceptable for `weak000` anyway. The theorem excludes every open weak-free U1 chamber in the entire affine orbit.

## 3. Controlled raw-profile theorem: `kappa[0][0]=t`

I next vary only

~~~text
kappa[0][0] = t
~~~

and keep

~~~text
knots = [19/25,81/100]
kappa[0][1] = 7/50
kappa[1] = [54/5,119/25]
kappa[2] = [53/25,971/100]
kappa[3] = [21/100,17/100].
~~~

For `t in [99/100,103/100]`, every curvature is strictly positive. Instead of recomputing rational centroids by division, the interval verifier writes `V(t)` and first moment `M(t)` polynomially and uses

~~~text
pnum_i(t) = V(t) x_i(t) - M(t)
C_ij(t)   = pnum_i e_ij^T + e_ij pnum_i^T
          = V(t) B_ij(t).
~~~

Since `V(t)>0`, `C_ij` and `B_ij` have the same trace sign against SPD `G`.

The **same 558 canonical triplet blockers** cover the same 314,967 combinatorial rooted trees throughout the interval. For the 33 residual trees I use the more interval-robust common-backbone quadruple

~~~text
3->0, 2->3, 5->9, 9->6.
~~~

For every one of these 559 blocker sums `S(t)`, negative definiteness is certified on the whole closed interval by the three signed Sylvester polynomials

~~~text
q1(t) = -S00(t)
q2(t) = S00(t) S11(t) - S01(t)^2
q3(t) = -det S(t).
~~~

After the affine change `t = 99/100 + (4/100)u`, `0<=u<=1`, **every Bernstein coefficient of every q1,q2,q3 is strictly positive**. The maximum degrees are `[3,4,5]`. Across all blockers, the smallest exact Bernstein coefficients in the three tests are respectively

~~~text
310505498111879649524297
/375000000000000000000000

2630401852836767798435489716959463410109136333
/3515625000000000000000000000000000000000000000

189275415338805165842362883072221068190457627049862944140687
/17578125000000000000000000000000000000000000000000000000000000
~~~

all strictly positive. The volume polynomial itself has Bernstein coefficients

~~~text
1406973584111/750000000000,
470168128829/250000000000,
~~~

also both positive.

Therefore:

> **For every real `t in [99/100,103/100]`, and every SPD affine Gram matrix G, the resulting positive-curvature C40 stack cannot have strict U=1 with additional-weak-U=0. Hence this entire one-parameter raw-profile family contains no affine strict110/weak000 member.**

This is a scoped subchart theorem only. It does not cover changing other curvature coordinates, moving the knots, C42, incidence-changing descendants, or profiles outside the stated interval.

## 4. Why no new S/H endpoint is audited

The requested workflow says to rationalize a feasible U1 cone and then audit full S/U/H and same-centre polar mechanics. The exact atlas finds **no feasible weak-free U1 cone**, so that branch of the workflow never arises. The existing literal parent already has a full exact maximal-face/true-edge audit with `S=[0,9]`, `U=[1,3]`, `H=[[0,3],[5,6]]`, weak `000`, and complete P/Q landscapes.

Thus I make no unsupported claim such as `H=0` for another metric. The new obstruction is entirely on the U side and is already sufficient to close the fixed raw profile and the stated one-parameter raw family against `110/weak000`.

## 5. Durable exact recovery capsule

Environment: **CPython 3.13.5, standard library only**.

### Files and hashes

~~~text
VERIFY_C40_COARSE100_U1_ATLAS.py
  7610 bytes
  SHA-256 e904042fd0f1811046b2bcf6812aa40ce0ebd453694cb34f14d337c720b757d5

C40_COARSE100_U1_ATLAS.json
  5742 bytes
  SHA-256 0822771eda02e5e281dd82c1b58369e712a623b64196b03e0d3295e60127029d

canonical blocker-bank payload SHA-256
  fa5dc65717adfbac8b36eadecd141b1e68188193a2993c3ae6185568da32fe14

VERIFY_C40_COARSE100_U1_INTERVAL.py
  6947 bytes
  SHA-256 d7cd89e209628c9a1b3d442ea59a6590c4e748cbe2b53d6b1902fec6993bbe07

C40_COARSE100_U1_INTERVAL.json
  1904 bytes
  SHA-256 7ebf5ebba56de6a7e9dceca822eb321b6e0d8112a75cfc8717ab8a61b05d2516
~~~

Run in a fresh directory:

~~~text
python -B -S VERIFY_C40_COARSE100_U1_ATLAS.py C40_COARSE100_U1_ATLAS.json
python -B -S VERIFY_C40_COARSE100_U1_INTERVAL.py VERIFY_C40_COARSE100_U1_ATLAS.py C40_COARSE100_U1_INTERVAL.json
~~~

Observed cold-replay markers:

~~~text
C40_COARSE100_U1_ATLAS_EXACT_PASS 774 558 33 315000 5742 0822771eda02e5e281dd82c1b58369e712a623b64196b03e0d3295e60127029d 7610 e904042fd0f1811046b2bcf6812aa40ce0ebd453694cb34f14d337c720b757d5 fa5dc65717adfbac8b36eadecd141b1e68188193a2993c3ae6185568da32fe14

C40_COARSE100_U1_INTERVAL_EXACT_PASS 558 33 1904 7ebf5ebba56de6a7e9dceca822eb321b6e0d8112a75cfc8717ab8a61b05d2516 6947 d7cd89e209628c9a1b3d442ea59a6590c4e748cbe2b53d6b1902fec6993bbe07 310505498111879649524297/375000000000000000000000 2630401852836767798435489716959463410109136333/3515625000000000000000000000000000000000000000 189275415338805165842362883072221068190457627049862944140687/17578125000000000000000000000000000000000000000000000000000000
~~~

Fresh-directory replay reproduced both output hashes byte-for-byte.

Convenience copies from this execution: atlas verifier (`VERIFY_C40_COARSE100_U1_ATLAS.py`), atlas report (`C40_COARSE100_U1_ATLAS.json`), interval verifier (`VERIFY_C40_COARSE100_U1_INTERVAL.py`), interval report (`C40_COARSE100_U1_INTERVAL.json`). These links are supplements; the complete runnable source is embedded below.

### Complete source: `VERIFY_C40_COARSE100_U1_ATLAS.py`

~~~python
from fractions import Fraction as F
from itertools import combinations
from math import gcd,lcm
from pathlib import Path
import hashlib,json,sys

PARENT_ASSIGNMENT='figure-0466'
PARENT_SHA256='7939f2aab5f6b71911d2546a87ee7e3888f045b957e7fec261e0531f15272b63'
NAME='C40_PACKET2X2_COARSE100'
KNOTS=[F(19,25),F(81,100)]
KAPPA=[[F(103,100),F(7,50)],[F(54,5),F(119,25)],[F(53,25),F(971,100)],[F(21,100),F(17,100)]]
FACES=[[0,2,1],[0,3,2],[0,4,3],[0,1,4],[1,2,6,5],[2,3,7,6],[3,4,8,7],[4,1,5,8],[9,5,6],[9,6,7],[9,7,8],[9,8,5]]
EXPECTED_RAW_VOLUME=F(470168128829,250000000000)
EXPECTED_RAW_CENTROID=(F(1037375653957897,1116346962000000),-F(151195195979711,223269392400000),F(23905595267,37211565400))
QUAD_LABELS=((3,0),(2,3),(6,2),(9,6))

def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def det3(M):
 return M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])-M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])+M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])
def addM(A,B):return tuple(tuple(A[i][j]+B[i][j] for j in range(3)) for i in range(3))
def sumM(ms):
 S=((F(0),F(0),F(0)),(F(0),F(0),F(0)),(F(0),F(0),F(0)))
 for M in ms:S=addM(S,M)
 return S
def negdef(M):
 # Sylvester on -M: -M00>0, det leading2(-M)>0, det(-M)>0.
 return M[0][0]<0 and M[0][0]*M[1][1]-M[0][1]*M[0][1]>0 and det3(M)<0
def nd_certificate(M):
 return {'minus_m00':-M[0][0],'leading2':M[0][0]*M[1][1]-M[0][1]*M[0][1],'minus_det':-det3(M)}
def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,tuple):return [enc(v) for v in x]
 if isinstance(x,list):return [enc(v) for v in x]
 if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
 return x

def build_raw():
 kn=KNOTS;K=KAPPA;ts=[F(0)]+kn+[F(1)]
 def G(t,s):return min(t,s)*(1-max(t,s))
 def vals(t):return [sum((K[j][k]*G(t,kn[k]) for k in range(2)),F(0)) for j in range(4)]
 def sec(t):
  f=vals(t);ar=(f[0]+f[1])*(f[2]+f[3]);return ar,ar*(f[1]-f[0])/2,ar*(f[3]-f[2])/2,ar*t
 V=F(0);M=[F(0)]*3
 for a,b in zip(ts,ts[1:]):
  aa,mm,bb=sec(a),sec((a+b)/2),sec(b)
  z=[(b-a)*(x+4*y+w)/6 for x,y,w in zip(aa,mm,bb)];V+=z[0]
  for i in range(3):M[i]+=z[i+1]
 c=tuple(m/V for m in M)
 raw=[(F(0),F(0),F(0))]
 for t in kn:
  f=vals(t);raw += [(-f[0],-f[2],t),(f[1],-f[2],t),(f[1],f[3],t),(-f[0],f[3],t)]
 raw.append((F(0),F(0),F(1)))
 assert V==EXPECTED_RAW_VOLUME and c==EXPECTED_RAW_CENTROID
 return V,tuple(M),c,raw

def graph_edges():
 E=set()
 for cy in FACES:
  for a,b in zip(cy,cy[1:]+cy[:1]):E.add(tuple(sorted((a,b))))
 E=sorted(E);assert len(E)==20
 return E

def directed_forms(raw,c,E):
 X=[tuple(raw[i][k]-c[k] for k in range(3)) for i in range(10)]
 labels=[]; mats=[]
 for i,j in E:
  for a,b in ((i,j),(j,i)):
   p=X[a];e=tuple(X[b][k]-p[k] for k in range(3))
   # B = p e^T + e p^T = 2*sym(p e^T); sign(tr(BG)) = sign(2 D_ab(G)).
   B=tuple(tuple(p[r]*e[s]+e[r]*p[s] for s in range(3)) for r in range(3))
   labels.append((a,b));mats.append(B)
 return X,labels,mats

def spanning_trees(E):
 out=[]
 for comb in combinations(range(len(E)),9):
  par=list(range(10))
  def find(x):
   while par[x]!=x:
    par[x]=par[par[x]];x=par[x]
   return x
  ok=True
  for k in comb:
   a,b=E[k];ra,rb=find(a),find(b)
   if ra==rb:ok=False;break
   par[ra]=rb
  if ok:out.append(comb)
 assert len(out)==31500
 return out

def orient_mask(root,comb,E,label_index):
 adj=[[] for _ in range(10)]
 for k in comb:
  a,b=E[k];adj[a].append(b);adj[b].append(a)
 parent={root:-1};q=[root]
 for u in q:
  for v in adj[u]:
   if v not in parent:parent[v]=u;q.append(v)
 assert len(parent)==10
 mask=0
 for i in range(10):
  if i!=root:mask |= 1<<label_index[(i,parent[i])]
 assert mask.bit_count()==9
 return mask,parent

def main(outpath):
 V,M,c,raw=build_raw();E=graph_edges();X,labels,mats=directed_forms(raw,c,E);li={lab:i for i,lab in enumerate(labels)}
 assert len(labels)==40 and len(set(labels))==40
 # Exact equal-weight negative-definite blockers. No 2-arrow blocker exists; 774 triples do.
 pair_count=0
 for C in combinations(range(40),2):
  if negdef(sumM([mats[i] for i in C])):pair_count+=1
 assert pair_count==0
 triples=[]
 for C in combinations(range(40),3):
  S=sumM([mats[i] for i in C])
  if negdef(S):triples.append(C)
 assert len(triples)==774
 triple_masks=[sum(1<<i for i in C) for C in triples]
 # One four-arrow blocker suffices for every arborescence missed by all bad triples.
 quad=tuple(li[x] for x in QUAD_LABELS);quadS=sumM([mats[i] for i in quad]);assert negdef(quadS);quadmask=sum(1<<i for i in quad)
 T=spanning_trees(E)
 root_stats={};residual=[];used=set();covered_total=0
 for root in range(10):
  t3=t4=0
  for ti,comb in enumerate(T):
   mask,parent=orient_mask(root,comb,E,li)
   hit=None
   for bi,b in enumerate(triple_masks):
    if mask & b == b:hit=bi;break
   if hit is not None:
    used.add(hit);t3+=1;covered_total+=1
   else:
    assert mask & quadmask == quadmask
    t4+=1;covered_total+=1
    residual.append({'root':root,'tree_index':ti,'arrows':[(i,parent[i]) for i in range(10) if i!=root]})
  root_stats[root]={'triple':t3,'quad':t4,'total':t3+t4}
 assert covered_total==315000
 assert root_stats[0]=={'triple':31467,'quad':33,'total':31500}
 for r in range(1,10):assert root_stats[r]=={'triple':31500,'quad':0,'total':31500}
 assert len(residual)==33 and all(z['root']==0 for z in residual)
 assert len(used)==558
 # Canonical exact certificate payload. The verifier itself recomputes every matrix and every tree.
 blocker_payload={
  'directed_labels':labels,
  'triples':[[labels[i] for i in C] for C in triples],
  'used_triple_indices':sorted(used),
  'quadruple':[labels[i] for i in quad],
 }
 bb=(json.dumps(enc(blocker_payload),sort_keys=True,separators=(',',':'))+'\n').encode()
 bsha=hashlib.sha256(bb).hexdigest()
 out={
  'parent_assignment':PARENT_ASSIGNMENT,'parent_sha256':PARENT_SHA256,'body':NAME,
  'knots':KNOTS,'kappa':KAPPA,'raw_volume':V,'raw_first_moment':M,'raw_centroid':c,
  'VEFC':[10,20,12,40],'true_edges':E,'directed_edge_forms':40,
  'spanning_trees':len(T),'root_labelled_trees':len(T)*10,
  'equal_weight_negdef_pair_blockers':pair_count,'equal_weight_negdef_triple_blockers':len(triples),
  'canonical_used_triples':len(used),'quadruple_blocker':[labels[i] for i in quad],
  'quadruple_negdef_certificate':nd_certificate(quadS),'coverage_by_root':root_stats,
  'triple_blocker_bank_sha256':bsha,'residual_after_all_triples':residual,
  'conclusion':'NO_SPD_GRAM_WITH_STRICT_U1_AND_ADDITIONAL_WEAK_U0_FOR_THIS_FIXED_RAW_PROFILE',
  'proof':'Any strict-U1/additional-weak-U0 metric has one strict root and a positive escape from every nonroot, hence contains one of the rooted positive spanning trees. Every one of the 315000 oriented spanning trees contains either an exact equal-weight 3-arrow blocker whose doubled symmetric-form sum is negative definite, or (for exactly 33 root-0 trees) the displayed 4-arrow blocker. For SPD G, each required arrow would make tr(B_ij G)>0, whereas a negative-definite blocker sum has negative trace against every SPD G, contradiction. Root-exit inequalities are therefore not even needed. Boundary metrics with extra weak-U events are not claimed excluded by this open-sign atlas, but they cannot satisfy additional-weak-U0.'
 }
 b=(json.dumps(enc(out),sort_keys=True,separators=(',',':'))+'\n').encode();Path(outpath).write_bytes(b)
 src=Path(__file__).read_bytes();print('C40_COARSE100_U1_ATLAS_EXACT_PASS',len(triples),len(used),len(residual),len(T)*10,len(b),hashlib.sha256(b).hexdigest(),len(src),hashlib.sha256(src).hexdigest(),bsha)

if __name__=='__main__':
 main(sys.argv[1] if len(sys.argv)>1 else '/mnt/data/C40_COARSE100_U1_ATLAS.json')
~~~

### Complete source: `VERIFY_C40_COARSE100_U1_INTERVAL.py`

~~~python
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import hashlib,importlib.util,json,sys

ATLAS_SOURCE_SHA256='e904042fd0f1811046b2bcf6812aa40ce0ebd453694cb34f14d337c720b757d5'
PARENT_ASSIGNMENT='figure-0466'
PARENT_SHA256='7939f2aab5f6b71911d2546a87ee7e3888f045b957e7fec261e0531f15272b63'
NAME='C40_PACKET2X2_COARSE100_KAPPA00_INTERVAL'
INTERVAL=(F(99,100),F(103,100))
ROBUST_QUAD_LABELS=((3,0),(2,3),(5,9),(9,6))

class P:
 def __init__(self,c=0):
  if isinstance(c,P): z=list(c.c)
  elif isinstance(c,(list,tuple)): z=[F(x) for x in c]
  else: z=[F(c)]
  while len(z)>1 and z[-1]==0:z.pop()
  self.c=tuple(z)
 def __add__(self,o):
  o=P(o);n=max(len(self.c),len(o.c));return P([(self.c[i] if i<len(self.c) else 0)+(o.c[i] if i<len(o.c) else 0) for i in range(n)])
 __radd__=__add__
 def __neg__(self):return P([-x for x in self.c])
 def __sub__(self,o):return self+(-P(o))
 def __rsub__(self,o):return P(o)-self
 def __mul__(self,o):
  o=P(o);r=[F(0)]*(len(self.c)+len(o.c)-1)
  for i,a in enumerate(self.c):
   for j,b in enumerate(o.c):r[i+j]+=a*b
  return P(r)
 __rmul__=__mul__
 def affine(self,a,h):
  a=F(a);h=F(h);res=P(0);pw=P(1);lin=P([a,h])
  for z in self.c:res+=z*pw;pw*=lin
  return res
 def bernstein(self,a,b):
  q=self.affine(a,F(b)-F(a));n=len(q.c)-1
  if n==0:return [q.c[0]]
  return [sum((q.c[i]*F(comb(k,i),comb(n,i)) for i in range(k+1)),F(0)) for k in range(n+1)]

def detp(M):
 return M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])-M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])+M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])
def sump(ms):return [[sum((M[i][j] for M in ms),P(0)) for j in range(3)] for i in range(3)]
def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,tuple):return [enc(v) for v in x]
 if isinstance(x,list):return [enc(v) for v in x]
 if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
 return x

def load_atlas(path):
 p=Path(path);b=p.read_bytes();h=hashlib.sha256(b).hexdigest();assert h==ATLAS_SOURCE_SHA256,(h,ATLAS_SOURCE_SHA256)
 s=importlib.util.spec_from_file_location('c40_atlas_exact',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def symbolic(m):
 kn=[F(19,25),F(81,100)];T=P([0,1])
 K=[[T,P(F(7,50))],[P(F(54,5)),P(F(119,25))],[P(F(53,25)),P(F(971,100))],[P(F(21,100)),P(F(17,100))]]
 ts=[F(0)]+kn+[F(1)]
 def G(t,s):return min(t,s)*(1-max(t,s))
 def vals(t):return [sum((K[j][k]*G(t,kn[k]) for k in range(2)),P(0)) for j in range(4)]
 def sec(t):
  f=vals(t);ar=(f[0]+f[1])*(f[2]+f[3]);return ar,ar*(f[1]-f[0])*F(1,2),ar*(f[3]-f[2])*F(1,2),ar*t
 V=P(0);M=[P(0)]*3
 for a,b in zip(ts,ts[1:]):
  aa,mm,bb=sec(a),sec((a+b)/2),sec(b);z=[(b-a)*(aa[i]+4*mm[i]+bb[i])*F(1,6) for i in range(4)];V+=z[0]
  for i in range(3):M[i]+=z[i+1]
 raw=[(P(0),P(0),P(0))]
 for t in kn:
  f=vals(t);raw += [(-f[0],-f[2],P(t)),(f[1],-f[2],P(t)),(f[1],f[3],P(t)),(-f[0],f[3],P(t))]
 raw.append((P(0),P(0),P(1)))
 E=m.graph_edges();labels=[];mats=[]
 for i,j in E:
  for a,b in ((i,j),(j,i)):
   # C_ij=V*B_ij where pnum=V*x_i-M. Since V>0, C and B have the same D_ij trace sign.
   p=[V*raw[a][r]-M[r] for r in range(3)];e=[raw[b][r]-raw[a][r] for r in range(3)]
   C=[[p[r]*e[s]+e[r]*p[s] for s in range(3)] for r in range(3)]
   labels.append((a,b));mats.append(C)
 return V,labels,mats

def canonical_cover(m):
 V0,M0,c0,raw0=m.build_raw();E=m.graph_edges();X,labels,mats=m.directed_forms(raw0,c0,E);li={x:i for i,x in enumerate(labels)}
 triples=[C for C in combinations(range(40),3) if m.negdef(m.sumM([mats[i] for i in C]))]
 assert len(triples)==774
 tm=[sum(1<<i for i in C) for C in triples];trees=m.spanning_trees(E);used=set();res=[]
 for root in range(10):
  for ti,tr in enumerate(trees):
   mask,parent=m.orient_mask(root,tr,E,li);hit=None
   for bi,bm in enumerate(tm):
    if mask&bm==bm:hit=bi;break
   if hit is None:res.append((root,ti,mask,parent))
   else:used.add(hit)
 assert len(used)==558 and len(res)==33 and all(z[0]==0 for z in res)
 q=tuple(li[x] for x in ROBUST_QUAD_LABELS);qm=sum(1<<i for i in q)
 assert all(mask&qm==qm for _,_,mask,_ in res)
 return labels,[triples[i] for i in sorted(used)],q,res

def main(atlas_path,out_path):
 m=load_atlas(atlas_path);labels0,blocks,quad,res=canonical_cover(m);V,labels,mats=symbolic(m);assert labels==labels0
 a,b=INTERVAL
 assert a>0 and b==F(103,100) and a<b
 # All profile curvatures remain positive on the whole interval; all other seven kappas are fixed positive.
 assert a>0
 vb=V.bernstein(a,b);assert all(x>0 for x in vb)
 mins=[None,None,None];max_degrees=[0,0,0]
 for C in blocks+[quad]:
  S=sump([mats[i] for i in C]);qs=[-S[0][0],S[0][0]*S[1][1]-S[0][1]*S[0][1],-detp(S)]
  for j,q in enumerate(qs):
   bc=q.bernstein(a,b);assert all(x>0 for x in bc)
   z=min(bc);mins[j]=z if mins[j] is None or z<mins[j] else mins[j];max_degrees[j]=max(max_degrees[j],len(q.c)-1)
 out={
  'parent_assignment':PARENT_ASSIGNMENT,'parent_sha256':PARENT_SHA256,'body_family':NAME,
  'varied_parameter':'kappa[0][0]','closed_interval':INTERVAL,'fixed_knots':[F(19,25),F(81,100)],
  'fixed_other_kappa':[['t',F(7,50)],[F(54,5),F(119,25)],[F(53,25),F(971,100)],[F(21,100),F(17,100)]],
  'base_profile_t':F(103,100),'root_labelled_trees':315000,'canonical_triplet_blockers':len(blocks),'residual_trees':len(res),
  'robust_quadruple_blocker':list(ROBUST_QUAD_LABELS),'volume_bernstein_coefficients':vb,
  'minimum_positive_bernstein_coefficients':mins,'maximum_sylvester_polynomial_degrees':max_degrees,
  'conclusion':'NO_SPD_GRAM_WITH_STRICT_U1_AND_ADDITIONAL_WEAK_U0_FOR_ANY_PROFILE_IN_THIS_CLOSED_T_INTERVAL',
  'proof':'For a strict-U1/additional-weak-U0 metric, every nonroot has a positive escape and therefore contains a rooted positive spanning tree. The same exact 558 triplet blockers cover 314967 rooted trees and the displayed 4-arrow blocker covers the remaining 33. For every blocker, after multiplying B_ij by positive V(t), the three signed Sylvester polynomials -S00, S00*S11-S01^2, and -det(S) have strictly positive Bernstein coefficients on the entire interval. Hence every blocker sum stays negative definite throughout the interval. V(t) itself has strictly positive Bernstein coefficients. Therefore all 315000 rooted positive-tree sign systems are SPD-infeasible for every t in the interval. Boundary metrics with additional weak-U events are outside this open-sign conclusion.'
 }
 data=(json.dumps(enc(out),sort_keys=True,separators=(',',':'))+'\n').encode();Path(out_path).write_bytes(data)
 src=Path(__file__).read_bytes();print('C40_COARSE100_U1_INTERVAL_EXACT_PASS',len(blocks),len(res),len(data),hashlib.sha256(data).hexdigest(),len(src),hashlib.sha256(src).hexdigest(),*[str(x) for x in mins])

if __name__=='__main__':
 if len(sys.argv)!=3:raise SystemExit('usage: python -B -S VERIFY_C40_COARSE100_U1_INTERVAL.py VERIFY_C40_COARSE100_U1_ATLAS.py OUT.json')
 main(sys.argv[1],sys.argv[2])
~~~

## 6. Scientific continuation

The fixed `COARSE100` raw profile is now **closed across its entire nonsingular affine orbit** for the required weak-free mono-U condition, so spending further metric-search effort on it is unjustified. The new interval theorem also closes the nearest one-coordinate curvature segment `kappa[0][0] in [99/100,103/100]` across all SPD metrics.

The next C40 move should therefore change raw geometry outside this certified subchart—preferably the already-identified coupled interface around physical vertex `1`, polar/stable face `0=[0,2,1]`, and shared carriers `0-1,1-2`—by moving another curvature coordinate, a knot, or several coupled profile parameters. For each new rational raw checkpoint, the correct first test is this exact blocker/tree machinery, not blind metric sampling. If a U1 cone finally survives the atlas, rationalize its Gram matrix and only then run the complete face/vertex/mixed-edge and same-centre-polar audit.

The 33-tree residual structure is especially reusable: at the base profile all residual trees are root 0 and share the six-arrow backbone listed above. The fact that a different four-arrow subset stays negative definite over the certified raw interval suggests tracking small negative-definite blocker banks symbolically as raw parameters move; a failure of that cover is a principled signal for where a genuine U1 cell may first become possible.

No global C40 obstruction is claimed. The exact conclusion is limited to the fixed `COARSE100` affine orbit and the explicit one-parameter positive-curvature interval above.
