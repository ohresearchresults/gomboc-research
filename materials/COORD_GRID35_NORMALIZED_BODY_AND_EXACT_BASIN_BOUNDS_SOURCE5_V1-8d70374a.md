# material-8d70374ade23

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# COORD_GRID35_NORMALIZED_BODY_AND_EXACT_BASIN_BOUNDS_SOURCE5_V1

## Identity, exact findings, and scope

This is a complete five-source recovery delta for the exact body COORD_GRID35_NORMALIZED_W001_D100000 and a new global radial-escape neighborhood certificate. Its sole unchanged source dependency is **[internal-source-reference]**, SHA256 7b9d113b63af0c9a7e9dda973cddaa2b0adf27dcebe107d615db90323b602d45, the complete18-source COORD_GRID35_MULTIGENERATION_AND_NEAR_WALL_V1. Recover that material's LEAD_GATE_SOURCE first. DEPENDENCY.json binds the five exact files actually used from that dependency. No old normalized optimizer checkpoint or missing sandbox is needed to reconstruct the selected body or this certificate. This does not claim that the separate fourteen-source normalized/projective search package has been canonically preserved.

The body is actual V35/E99/F66, C198, own ordinary-filled-volume-centroid strict(2,1,1), weak000, zero primitive counters0. S faces3,57, U raw-lex15, H edge11--17. Raw coordinates17bits, common centred denominator67bits. It is a useful nonwinner, NOT a Gömböc. Exact volume53928718583353/1500000000000000 and centroid(-4188897247624520623,3367172185439624937,476412288260694757)/86285949733364800000.

For vectors v_i write f_ij=v_i dot(v_j-v_i). A positive f arrow strictly increases squared norm. A directed escape tree to one root therefore proves the convex hull has exactly one strict radial maximum. Conversely, a nonempty index set with f_ij<0 for every inside i and outside j contains a strict radial maximum: select a maximum-norm point inside; Cauchy--Schwarz makes its f strictly negative toward every distinct other point inside too. Duplicates within a set are one geometric point, and two disjoint closed sets cannot share a geometric point because their strict cross inequality would fail. Thus two disjoint closed sets certify two distinct maxima. Applied to all supporting poles q_f at the physical body's actual centroid, this gives at least two physical stable faces. It is fixed-origin polarity for mechanics, not a claim that the filled polar centroid equals that origin.

The perturbation convention is per-vector, per-coordinate: |e_ik|<=epsilon*a_i, a_i=max_k|v_ik|. The exact identity is f'_ij=f_ij+e_i dot(v_j-2v_i)+v_i dot e_j+e_i dot e_j-|e_i|^2. Put L_ij=a_i*||v_j-2v_i||_1+a_j*||v_i||_1, D_ij=3(a_i*a_j+a_i^2), and U_ij=3*a_j^2/4 if a_j<=2*a_i, otherwise3*a_i*(a_j-a_i). The scalar maximum of uv-u^2 on |u|<=a_i,|v|<=a_j gives the exact sufficient bounds f-epsilon*L-epsilon^2*D <= f' <= f+epsilon*L+epsilon^2*U.

The script constructs the possible-escape graph using upper bounds>=0 and proves its terminal strongly connected components have strictly negative outward bounds. For the centred polar it retains two disjoint30-pole sink sets at epsilon15412249/100000000; epsilon1/10 is also certified. For the centred primal bank, the guaranteed-escape graph using lower bounds>0 reaches root15 at epsilon5309/50000000. These are **different coordinate spaces**, not comparable raw-shape radii. Every application must check that the new actual-own-centred bank or complete supporting-pole bank satisfies its respective bounds. Arbitrary replacement geometry, additional unbounded new poles, and large material changes are not excluded. The next1e-8 grid point merely fails this sufficient graph certificate, not the geometric property.

The independent exact widest-path diagnostic uses rational weights f_ij/|v_i|^2. A root-reaching tree's minimum edge equals an outward cut's maximum edge. The optimal bottleneck is approximately-0.4546085456597566 for stable-root3 and-0.4581910274442488 for root57; both exact rational values, trees and30-pole cuts are reproduced. The second stable basin is consequently not represented adequately by a single nearly-zero local triangle sign. This is a useful finite geometric obstruction, not a lower-complexity nonexistence theorem.

## Recovery and observed replay

Save the base64 block below as SOURCE5.b64 (whitespace is ignored), and the following complete decoder as RESTORE.py. Run `python3 -B -S RESTORE.py SOURCE5.b64 NEW_SOURCE`, then `python3 -B -S NEW_SOURCE/REPLAY.py LEAD_GATE_SOURCE NEW_PROOF`. Both new destination directories must not exist. Python3.13.5 standard library only; no stochastic or numerical parameters. REPLAY checks every dependency hash, runs two independent complete exact hull/mass/all-feature audits and a third centred integration, then the exact rooted-tree and cut certificates. This exact source-only replay was actually observed in a fresh directory before storage.

Expected terminal markers:

- EXACT_VARIANT_TWO_AUDITS_AND_MASS_PASS
- EXACT_INPUT_HULL_EQUALITY_PASS COORD_GRID35_NORMALIZED_W001_D100000 [2,1,1] [0,0,0]
- EXACT_OWN_CENTRED_PRIMAL_TREE_AND_POLAR_BASIN_CUTS_PASS
- COORD_GRID35_NORMALIZED_BODY_AND_TWO_BASIN_BOUNDS_COLD_PASS

Normalized base64:6780ASCIIbytes, SHA2565bc8ebfddd8cdef31dc86d66dd3f96ad1408a6bddb507965917c7bdf9a7f7cec. Decoded complete five-file JSON map12128bytes, SHA2564a29866559a3800486a66e93c3800f07543fde570f71cef1b0c9ae20347ae080.

Recovered files:

BASIN_GATES.py8681B SHA4c852560bbe8ac80bfdd1135beed1b8e3eed401ebf114b96e93116ce6514cf22;
DEPENDENCY.json591B SHA01cd254541711f07f34aebd7e3c9cf21974c5c48ae8ebcf97ca476a4ff021f58;
EXPECTED.json517B SHA925e17b3ea8d042328ffcc8c4d496c83f6061a459b8b07d16fd0ef32b08cda7e;
INPUT.json822B SHA11af2bb2d0e96073ed84499aa34bd15a88dff1209e167b8fc9a109165a8fc217;
REPLAY.py1122B SHA473d4f5c4d1053940fdc02fa20bd8a15b9c07c8d61b7b5c0cc22e3baa316d75a.

Reproduced outputs, all checked by EXPECTED.json:

A.json=B.json10280B SHA904861a5b7097b235266d033d55004cd5da3c11717c2ac0da44b7e6e336526d3;
RAW.json3748B SHAf042ac1663e5dcb5f689e6ed17032517a46626a7ac3be04d934fa1e62205f189;
MASS.json216B SHA634789f284417937eec9d5219ef852f98c187303483e14b648c3a70c3aea6cb6;
BASIN_GATES.json7604B SHAe578d6eb25c6a279885f306eead3181b3058ed434e332af559526bc096adba1b.

```python
from pathlib import Path
from hashlib import sha256
import base64,zlib,json,sys
s=''.join(Path(sys.argv[1]).read_text().split())
assert len(s)==6780 and sha256(s.encode()).hexdigest()=='5bc8ebfddd8cdef31dc86d66dd3f96ad1408a6bddb507965917c7bdf9a7f7cec'
b=zlib.decompress(base64.b64decode(s,validate=True))
assert len(b)==12128 and sha256(b).hexdigest()=='4a29866559a3800486a66e93c3800f07543fde570f71cef1b0c9ae20347ae080'
p=Path(sys.argv[2]);p.mkdir(parents=True,exist_ok=False)
files=json.loads(b);assert len(files)==5
for n,t in files.items():
    assert Path(n).name==n
    (p/n).write_bytes(t.encode())
print('GRID35_NORMALIZED_BODY_BASIN_FIVE_SOURCE_RECOVERY_PASS')
```


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]
