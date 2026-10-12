
## 2026-09-15T16:46:46.887Z

## Cap-centroid theory attribution and the current constructive landscape

The general existence observation in16:25:06.400Z is a published theorem, not a new research claim. Read the primary Gilboa–Haim-Kislev–Slomka paper **Isobarycentric Inequalities**, arXiv:2202.07527v1, Theorem1.1, Lemmas2.1–2.3 (PDF pages1,5–6; screenshots of pages1 and6 inspected), subsequently IMRN2023,14,12298–12323. Theorem1.1 gives a prescribed-barycentre halfspace for a finite absolutely continuous measure under its stated hypotheses, and its maximum-mass property; the convex uniform-body case has uniqueness of an active cutting plane. Source: https://arxiv.org/abs/2202.07527 and https://arxiv.org/pdf/2202.07527 . This broad theorem does not supply equilibrium control or an edge budget. It strengthens the interpretation of the already certified C598 single-cut root without identifying that root with its rational C664 approximation.

For our bounded convex Q and m interior Q, a self-contained special-case proof uses y=x-m and F(a)=integral_Q max(1-a.y,0)dy. A ball centred at0 inside Q makes F coercive: F(a)>=integral_ball max(-a.y,0)dy=c|a|,c>0. F is continuous and differentiable (each zero set is a null hyperplane; at a=0 the integrand is locally positive), so a minimizer satisfies gradient F=-integral_{Q intersect {a.y<=1}}y=0. If m differs from g(Q), its cut must be active. The signed-indicator strict monotonicity argument already journaled gives uniqueness. For any measurable A subset Q with centroid m, volume(A)=integral_A(1-a.y)<=F(a)=volume(Q intersect {a.y<=1}), with equality only for the same cut body up to null sets. Thus one-cut restoration is globally available and volume-maximal, but does not promise monostability. This is a direct proof of the applicable published special case, not an independent novelty assertion.

**New coordinator finite candidate, not yet persisted:** COORD_C598_PROJECTIVE_METRIC_OWN334_G1E12 is a rational positive-denominator projective/affine image of the exact C598. Complete independently implemented A/B audits have both finished, agree on all bytes, and give164/299/137,C598,own334/weak000. A third centred-integer integration has finished over324 positive tetrahedra with zero centred first moments. Every maximal facet cycle and true-edge image was compared exactly. This body is still ephemeral/not yet persisted until the next complete source capsule; accepted S8/C624 remains unchanged and no descendant has been dispatched or promoted from it. The important new opportunity is an own334 body with twelve-edge headroom, rather than the parent own(19,27,44); its arithmetic cost increases.

The coordinator also built actual-volume parallel-support deformation and metric searches. Numerical consistency matrices suggest offset-space dimension38 for both C602 and C598 (34 after translation/scale gauge); no exact rank theorem is yet claimed. Soft penalty searches admitted negative global support slacks and are invalid as constructions. Subsequent hard linear type-cone searches retained positive numerical global slacks but gave no own110. An additional eight hard healthy-mechanics trials, C602 targets7->11,29,85,5 with and without affine metric, retained numerical121 and changed the chosen negative exits only about1e-7. This is a finite unsuccessful experiment, not an impossibility theorem. The complete sources, exact input identities, parameters and saved outcomes are being packaged; do not treat their current local files as already durable methods. Their failure indicates that reducing a sum of mechanical residuals can buy many new critical points, whereas fixed-normal healthy-guard preservation can freeze the current near-boundary chamber. This is a constructive-search diagnosis, not a proven whole-family obstruction.

Calm Finch31 is now active on asg_9_3jUNaB9fDmUrfQOxs-5B7l, specifically C598 whole-reference-basin/mass surgery, not idle as the pre-dispatch16:25:06.400Z entry said. The other four directions remain active and useful. Latest processed scheduler event1344; no stored result has arrived since the current frontier assignments. Original missing V>=9,F>=9 proofs and older pending source capsules remain explicitly unresolved.

## 2026-09-15T16:48:11.005Z

## Recovery capsule: COORD_C598_PROJECTIVE_METRIC_OWN334_G1E12 — complete exact construction and audit driver

This entry persists the exact finite nonwinner, not a new own110 record. The body is164/299/137,C598,strict334/weak000. Two complete independent auditors and third centred-integer mass integration have executed. A fresh source-only cold run also regenerated the parent audit, transformed H, both new audits and the whole-complex comparison; marker C598_PROJECTIVE_METRIC_SOURCE_ONLY_REPLAY_PASS. The complete small construction/audit source below is sufficient independently of its numerical discovery. The separate complete numerical discovery method and bounded-search checkpoints will be preserved in the following methods capsule; they are not needed to reconstruct these exact rational output bytes.

**Exact dependency, not a renamed body:** canonical COORD_C602_TO91_CHAIN6_G1E12 from C598_JUNCTION91_AND_ALL_OLD_ENDPOINT_BOUND,15:33:50.633Z. Its complete nine-source capsule depends on FOUR_FRONTIERS_EXACT_CORE_20260915, three complete parts14:47:44.818Z/14:54:38.487Z/14:56:12.493Z. Parent raw.json is28264bytes/SHA1286c05904d1aee57346b1bbeb200d8998b1656b0319d2cf56b2bfbb071c3599; parent complete A record435251bytes/SHA97e6687a0fd4a47515153da6efe8ed9168ea0e2b5ec603b2e1ef7c6b8bf230b9. Those literal capsules contain every original control, five added rational rows, maximal-hull reconstruction and both independent auditors, so no originating sandbox is required.

**Complete new input.** Put D=1000000000000. For column vectors, y=L^T x/(1+b.x), where
b=[231165476175,-287690514274,-722193871745]/D,
L=[[6195174799506,0,0],[-1419836775816,189361598103,0],[-4331762107070,485380338385,852421755373]]/D.
Final coordinates are every y minus the actual new filled-volume centroid. No exponential or floating rounding occurs in reconstruction. The minimum denominator over all parent vertices is exactly55561225651/200000000000>0, and every diagonal of L is positive. Thus the physical projective/affine map preserves maximal incidence and true edges. The code checks the complete vertex, maximal-facet cyclic-order and true-edge correspondence explicitly too.

Save the following entire source as PM598_RECOVER.py. Python3.13.5 standard library, assertions enabled. Arguments are the recovered canonical core directory, exact parent raw.json, and a new output directory. Core check_A.py is the complete support-triple audit; check_B.py is the independent plane-pair clipping audit and imports none of A's geometry/mass/mechanics; centred_mass.py is the third independent fan/centred-integer integration. Their exact source bytes are already in the named canonical core capsule.

```python
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
from hashlib import sha256
import json,subprocess,sys
sys.set_int_max_str_digits(0)
assert __debug__
core=Path(sys.argv[1]).resolve()
parent=Path(sys.argv[2]).resolve()
out=Path(sys.argv[3]).resolve()
assert not out.exists()
out.mkdir(parents=True)
def digest(p):
 b=p.read_bytes()
 return len(b),sha256(b).hexdigest()
def dump(p,a):
 p.write_text(json.dumps(a,sort_keys=True,separators=(',',':')))
assert digest(parent)==(28264,'1286c05904d1aee57346b1bbeb200d8998b1656b0319d2cf56b2bfbb071c3599')
D=1000000000000
b=tuple(F(v,D) for v in [231165476175,-287690514274,-722193871745])
L=tuple(tuple(F(v,D) for v in row) for row in [[6195174799506,0,0],[-1419836775816,189361598103,0],[-4331762107070,485380338385,852421755373]])
assert all(L[i][i]>0 for i in range(3))
assert all(L[i][j]==0 for i in range(3) for j in range(i+1,3))
raw=json.loads(parent.read_text());H=[]
for n0,n1,n2,d in raw['H']:
 rhs=[F(n,d)+c for n,c in zip((n0,n1,n2),b)];z=[]
 for i in range(3):
  z.append((rhs[i]-sum(L[i][j]*z[j] for j in range(i)))/L[i][i])
 k=lcm(*(v.denominator for v in z));row=[int(v*k) for v in z]+[k]
 g=gcd(*row);row=[v//g for v in row]
 assert row[3]>0
 H.append(row)
assert len(H)==len(set(map(tuple,H)))==137
dump(out/'raw.json',{'H':H})
assert digest(out/'raw.json')==(42455,'df60591a327f8d36f1c1e66f7d7d4db48cf14433a3bb59e4bd9a668c88c79fcd')
for script,src,dst in [('check_A.py',parent,out/'PARENT_A.json'),('check_A.py',out/'raw.json',out/'A.json'),('check_B.py',out/'raw.json',out/'B.json')]:
 subprocess.run([sys.executable,'-B','-S',str(core/script),str(src),str(dst)],check=True)
assert digest(out/'PARENT_A.json')==(435251,'97e6687a0fd4a47515153da6efe8ed9168ea0e2b5ec603b2e1ef7c6b8bf230b9')
assert digest(out/'A.json')==(504653,'d01383b4720b9615d019f4a229429b97a57f16755998b305033b5ff3506b2752')
assert (out/'A.json').read_bytes()==(out/'B.json').read_bytes()
P=json.loads((out/'PARENT_A.json').read_text());A=json.loads((out/'A.json').read_text())
assert [A[k] for k in ('V','E','F')]==[164,299,137]
assert A['counts']==[3,3,4] and A['weak']==[0,0,0]
assert A['active_input_indices']==list(range(137))
assert A['stable_face_ids']==[104,114,125]
assert A['unstable_vertices']==[0,162,163]
assert A['saddle_edges']==[[1,65],[2,92],[5,6],[162,163]]
assert all(A[k]==0 for k in ['face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count'])
X=[tuple(map(F,r)) for r in A['raw_vertices']]
lookup={p:i for i,p in enumerate(X)};pts=[];den=[]
for row in P['raw_vertices']:
 p=tuple(map(F,row));s=1+sum(v*c for v,c in zip(p,b));assert s>0
 den.append(s)
 pts.append(tuple(sum(p[i]*L[i][j] for i in range(3))/s for j in range(3)))
assert min(den)==F(55561225651,200000000000)
assert len(set(pts))==len(X)==164 and set(pts)==set(X)
mp=[lookup[p] for p in pts]
assert sorted(sorted([mp[i],mp[j]]) for i,j in P['edges'])==A['edges']
for cy,old in zip(A['faces'],P['faces']):
 mapped=[mp[i] for i in old]
 assert len(mapped)==len(cy) and set(mapped)==set(cy)
 assert any(cy==mapped[k:]+mapped[:k] for k in range(len(cy)))
sys.path.insert(0,str(core))
from centred_mass import run as mass
M=mass(A)
assert M['tetrahedra']==324
assert M['common_centred_denominator_bits']==92094
assert M['filled_first_moments']==[0,0,0]
dump(out/'MASS.json',M)
assert digest(out/'MASS.json')==(223,'228edbb5a0f660741a63f224022c51e3183e46730dff92dfd46140fd03c151c2')
print('PM598_EXACT_TWO_AUDITS_WHOLE_COMPLEX_AND_CENTRED_MASS_PASS')
```

Reconstruction and verification command: `python -B -S PM598_RECOVER.py CANONICAL_CORE CANONICAL_C598_RAW NEW_OUTPUT`. Expected terminal marker `PM598_EXACT_TWO_AUDITS_WHOLE_COMPLEX_AND_CENTRED_MASS_PASS`. This minimal combined driver is a consolidation of the already executed complete TRANSFORM.py, VERIFY_PM598.py and REPLAY_PM598.py functions, not a claim that this consolidation has yet been cold-executed. The uncombined source-only cold run has finished with all the same mathematical assertions and all specified output hashes; a direct execution of this exact combined source is the next transport check.

**Observed exact outputs and arithmetic:** raw H42455bytes/SHA df60591a327f8d36f1c1e66f7d7d4db48cf14433a3bb59e4bd9a668c88c79fcd. A and B each504653bytes/SHA d01383b4720b9615d019f4a229429b97a57f16755998b305033b5ff3506b2752. Third MASS223bytes/SHA228edbb5a0f660741a63f224022c51e3183e46730dff92dfd46140fd03c151c2. Primitive support maximum594bits; raw-coordinate fractions950; centroid92087; volume46083; raw first moments92174; common centred denominator92094. The old C598 denominator was80232bits. This saves no further edges and worsens arithmetic, but turns own(19,27,44) into own334 with all137 maximal facets and E299 unchanged. It remains a nonwinner, leaving twelve true-edge additions before E311. This exact body, source inputs and full verification now have a canonical recovery path; the accepted winner stays S8/C624.

## 2026-09-15T16:49:08.390Z

### PM598 recovery-source byte identity

The complete PM598_RECOVER.py code block in16:48:11.005Z, extracted as UTF8 with LF and one terminal newline, is3517bytes/SHA256ce93a45eda31171f603d17133a5c8de885cbdb24d5c5ef63b62195d3874c3276. It has no hidden helper besides the three complete already-canonical exact core modules named there. A direct fresh execution of this exact consolidated source has started; the independently executed uncombined cold replay and its output identities remain the established audit evidence until that run terminates. This supplies the recovery-input byte identity omitted from the preceding capsule; its literal source, exact integer input parameters, dependency identities, reconstruction command, complete expected output hashes and terminal marker are all now canonical.

The coordinator's next finite geometric step is to test actual hull changes around the adjacent stable triangles104/125 and the adjacent unwanted extrema162/163 of this exact PM598 body. It is not a change to accepted S8/C624 and not a dispatch based on an unpersisted body. Any numerical hull proposal will be distinguished from a complete maximal-complex and own-centroid audit, especially near small dihedral angles.
