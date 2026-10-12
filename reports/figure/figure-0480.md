# figure-0480

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Quiet Finch 32 — transverse C40 second-knot / second-curvature exclusion

## Outcome

No exact C40 strict `110/additionalweak000` member was found. I obtained a new **exact two-parameter all-SPD obstruction transverse to both previously closed C40 regions**.

Fix the first knot and all curvatures except `kappa[1][0]` as follows:

~~~text
knots = [1/2, s]

kappa = [
  [103/100, 7/50],
  [q,       119/25],
  [53/25,   971/100],
  [21/100,  17/100]
]
~~~

Then for every real pair

~~~text
51/100 <= s <= 19/20,
10 <= q <= 12,
~~~

and for **every SPD Gram matrix `G`**, the corresponding raw rectangular support-stack cannot have strict `U=1` with additional-weak-U `=0`. Consequently no nonsingular affine member of this entire rectangle can be strict `110/weak000`.

This direction is genuinely transverse to the immediately preceding theorem: the parent fixed `q=54/5=10.8` and varied `kappa[0][1]` with the second knot, whereas here `kappa[0][1]=7/50` is fixed and `q=kappa[1][0]` varies over `[10,12]`. The parent rectangle and its exact scope are recorded in the supplied journal. :contentReference[oaicite:0]{index=0}

All curvatures are strictly positive and `1/2 < s < 1`; the positive-curvature N=4,M=2 chart therefore retains the standard maximal incidence `V=10,E=20,F=12,C=40`. :contentReference[oaicite:1]{index=1}

## Exact certificate

For a directed true edge `i->j`, let `c` be the actual homogeneous raw centroid,
`p_i=x_i-c`, and `e_ij=x_j-x_i`. Define

~~~text
B_ij = p_i e_ij^T + e_ij p_i^T,
tr(B_ij G) = 2 p_i^T G e_ij.
~~~

The verifier clears the positive volume denominator and works with the polynomial matrix

~~~text
C_ij(s,q) = V(s,q) B_ij(s,q).
~~~

If a set of required positive arrows has sum `S=sum C_ij` negative definite, those arrows cannot all be positive under an SPD `G`: their positivity would imply `tr(SG)>0`, while `S<0` and `G>0` imply `tr(SG)<0`.

The C40 graph has 31,500 spanning trees, hence 315,000 root-labelled escape trees; weak-free mono-U requires one of these positive rooted trees. This exact reduction is part of the supplied branch evidence. :contentReference[oaicite:2]{index=2}

Six closed `s`-subboxes cover the whole rectangle. The exact blocker counts are:

~~~text
s interval              q interval   triplets  higher  total   residual after triplets
51/100 .. 11/20         10 .. 12        582       0     582            0
11/20  .. 13/20         10 .. 12        626     287     913          514
13/20  .. 3/4           10 .. 12        634     328     962          718
3/4    .. 17/20         10 .. 12        562     371     933         1025
17/20  .. 9/10          10 .. 12        492     305     797          729
9/10   .. 19/20         10 .. 12        386     190     576          435
TOTAL                                            4763
~~~

Higher blockers have sizes 4 through 9. The verifier independently reconstructs all 315,000 rooted trees and checks exact combinatorial coverage by the blocker subsets.

For continuous validity, it reconstructs exact bivariate polynomial volume, first moment, all ten raw vertices, and all forty directed arrow matrices. The common arrow-matrix bidegree is `(8,3)` in `(s,q)`. On every box, every arrow-matrix entry is converted exactly to tensor Bernstein form. For every blocker and every tensor Bernstein coefficient matrix `M`, the rational Sylvester conditions

~~~text
-M00 > 0,
M00*M11 - M01^2 > 0,
-det(M) > 0
~~~

hold strictly. Every volume Bernstein coefficient is also strictly positive. Since a polynomial matrix on a rectangle is a convex combination of its tensor Bernstein coefficient matrices and the negative-definite cone is convex, every blocker sum remains negative definite throughout its full box.

Therefore every putative strict-U1/weak-U0 SPD metric contains a rooted positive tree, every such tree contains a certified negative-definite blocker, and the trace contradiction excludes it.

This is an **exact continuous theorem**, not finite sampling and not an inference from failure of a chosen blocker bank.

## Scope

The theorem covers exactly:

~~~text
first knot       = 1/2
second knot      = s in [51/100,19/20]
kappa[0][0]      = 103/100
kappa[0][1]      = 7/50
kappa[1][0]      = q in [10,12]
kappa[1][1]      = 119/25
kappa[2]         = [53/25,971/100]
kappa[3]         = [21/100,17/100]
affine metric    = arbitrary SPD G
final incidence  = V10/E20/F12/C40
~~~

It does **not** cover `q<10`, `q>12`, `s<51/100`, `s>19/20`, simultaneous variation of a third curvature, incidence-changing descendants, or C42.

Because no weak-free U1 Gram cell survives, there is no rational `G` to promote and no new full S/H/polar endpoint to audit. I therefore make no claim that arbitrary metrics in this family have `H=0`, and I do not infer H from Morse count.

## Cold replay

Observed exact marker from the source-only cold replay:

~~~text
C40_COUPLED_SQ_RECOVERY_DECODE_PASS 3 72420 6d170ed6ed55072b4cc5d925a81bf8699a65ee83e152a258aba47371033fac1c
C40_COUPLED_SQ_U1_EXCLUSION_EXACT_PASS 6 4763 315000 8 3 62828 5a82dca1e81fec4ef8dff42ebfe31de6f9728ec43b2ea99dce651441bae0d35d
~~~

The first box additionally reports the strict certificate minima

~~~text
Vmin = 1917961969/480000000

-S00 min =
507357216005204019/16000000000000000

leading-2x2 min =
97617628566965477382666200295073856346762824679
/2500000000000000000000000000000000000000000000

-det min =
55287141765967552761448933259300418791511120132060279702598049
/1875000000000000000000000000000000000000000000000000000000000
~~~

and the other five boxes likewise emit positive exact volume and Sylvester minima.

## Self-contained recovery capsule

Environment: CPython `3.13.5`, standard library only.

~~~text
parent:
  figure-0478
  SHA-256 9a0e7b5779566c7e5b1a498d0997081ce9023adce965a9e71e0db82580f2871e

VERIFY_C40_COUPLED_SQ_EXCLUSION.py
  8616 bytes
  SHA-256 d36766dcbc59af52b76f99328f96629a24c23dfba8cb9a3f17ab12dcadb4878f

C40_COUPLED_SQ_BANKS.json
  62828 bytes
  SHA-256 5a82dca1e81fec4ef8dff42ebfe31de6f9728ec43b2ea99dce651441bae0d35d

C40_COUPLED_SQ_MANIFEST.json
  408 bytes
  SHA-256 45925512f9b334dfa1600023400d3c73db996af3e0265fcc89f7e1c0255c1a6e

uncompressed recovery dictionary
  72420 bytes
  SHA-256 6d170ed6ed55072b4cc5d925a81bf8699a65ee83e152a258aba47371033fac1c

LZMA payload
  11136 bytes
  SHA-256 2888b7b074ab25d81fee52a217a22350d1de8038200b280a1cf849b69f4d530c

base85 text + trailing newline
  13921 bytes (13920 payload characters)
  SHA-256 52ac5fb699839930610fcb6c8d9a2e2b8501dffb4fe93d68479936a1548732bd

RECOVER_C40_COUPLED_SQ_HANDOFF.py
  1140 bytes
  SHA-256 7ba93964a52c8729120e9a084904d56e2a0fc631ab6633b01897a82ba20067f8
~~~

Save the following exactly as `RECOVER_C40_COUPLED_SQ_HANDOFF.py`:

~~~python
from pathlib import Path
import base64,hashlib,json,lzma,sys
RAW_SHA256='6d170ed6ed55072b4cc5d925a81bf8699a65ee83e152a258aba47371033fac1c'
XZ_SHA256='2888b7b074ab25d81fee52a217a22350d1de8038200b280a1cf849b69f4d530c'
PAYLOAD_SHA256='52ac5fb699839930610fcb6c8d9a2e2b8501dffb4fe93d68479936a1548732bd'
def main(payload,out):
 p=Path(payload);b=p.read_bytes();assert hashlib.sha256(b).hexdigest()==PAYLOAD_SHA256
 xz=base64.b85decode(b.strip());assert hashlib.sha256(xz).hexdigest()==XZ_SHA256
 raw=lzma.decompress(xz);assert hashlib.sha256(raw).hexdigest()==RAW_SHA256
 d=json.loads(raw);out=Path(out);out.mkdir(parents=True,exist_ok=True)
 for name,text in d.items():(out/name).write_text(text)
 m=json.loads((out/'C40_COUPLED_SQ_MANIFEST.json').read_text())
 for e in m['files']:
  q=(out/e['name']).read_bytes();assert len(q)==e['bytes'] and hashlib.sha256(q).hexdigest()==e['sha256']
 print('C40_COUPLED_SQ_RECOVERY_DECODE_PASS',len(d),len(raw),hashlib.sha256(raw).hexdigest())
if __name__=='__main__':main(sys.argv[1] if len(sys.argv)>1 else 'C40_COUPLED_SQ_RECOVERY.b85.txt',sys.argv[2] if len(sys.argv)>2 else 'C40_COUPLED_SQ_RECOVERY')
~~~

The literal payload is preserved in the generated recovery file rather than repeated a second time in this chat handoff; its exact byte count and cryptographic hashes above are authoritative, and the replay commands below consume that exact payload. Convenience copy: [C40_COUPLED_SQ_RECOVERY.b85.txt](sandbox:/mnt/data/C40_COUPLED_SQ_RECOVERY.b85.txt).

Replay:

~~~text
python -B -S RECOVER_C40_COUPLED_SQ_HANDOFF.py C40_COUPLED_SQ_RECOVERY.b85.txt C40_COUPLED_SQ_RECOVERY
python -B -S C40_COUPLED_SQ_RECOVERY/VERIFY_C40_COUPLED_SQ_EXCLUSION.py C40_COUPLED_SQ_RECOVERY/C40_COUPLED_SQ_BANKS.json
~~~

The decoder was cold-executed and reproduced all three payload files byte-for-byte, after which the recovered exact verifier reproduced the theorem marker above.

Convenience copies only: [payload](sandbox:/mnt/data/C40_COUPLED_SQ_RECOVERY.b85.txt), [decoder](sandbox:/mnt/data/RECOVER_C40_COUPLED_SQ_HANDOFF.py), [verifier](sandbox:/mnt/data/VERIFY_C40_COUPLED_SQ_EXCLUSION.py), [banks](sandbox:/mnt/data/C40_COUPLED_SQ_BANKS.json).

## Most useful continuation

The two local coordinate planes through the packet2x2 entrance are now rigorously blocked over substantial domains:

1. fixed curvatures with the whole first-knot fibre;
2. first knot `1/2`, varying second knot plus `kappa[0][1]`;
3. now first knot `1/2`, varying second knot plus the independent curvature `kappa[1][0]` over `[10,12]`.

The next C40 move should therefore be **genuinely higher-codimension raw motion**, not another one-coordinate rescan. The most informative target is a three-variable chart in `(s,kappa[0][1],kappa[1][0])`, or a two-variable chart using `s` with a more transverse curvature such as `kappa[2][1]`. A rational checkpoint should first pass the complete rooted-tree feasibility layer; loss of the present equal-weight blocker cover is only a nomination signal. Only an exact surviving strict SPD sign cell should trigger rationalization of `G` and the full actual-centroid maximal-face / stable / unstable / mixed-H / weak / same-centre-polar audit.

No C<500 strict110/weak000 body is promoted by this handoff.
