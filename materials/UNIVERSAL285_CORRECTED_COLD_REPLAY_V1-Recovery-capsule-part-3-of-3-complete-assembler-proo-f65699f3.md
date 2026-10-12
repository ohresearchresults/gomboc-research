# material-f65699f3e7d7

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# UNIVERSAL285_CORRECTED_COLD_REPLAY_V1

## Object and evidence status

This is a fresh coordinator cold reconstruction and exact replay of the inherited NOVA24_UNIVERSAL_285_TREE_COVARIANCE_V1 certificate, not a new lower bound. The deterministic generator reproduced all 285 coefficient records, 17,416 integer positive-definite blocks and 156,744 positive leading minors. The independently implemented standard-library scalar/Bareiss/Fraction-LDL verifier reproduced the exact accepted data and report hashes. No numerical tolerance is used in acceptance.

The remaining rooted nine-vertex shape is exactly parent (0,0,1,2,3,4,5,6,0), ordinal278 in this canonical rooted-tree order. This number is not a polytope or face-lattice index. Universal285 alone does NOT prove V>=10. Its remaining broom is excluded by immutable result minimum-0054, SHA256 4e39e8c2a461dc76a76e49153b9f70ace7e0e287cb3fe5e6b3c3733a8c24d774. The separate V<=8/F<=8 finite capped-vector theorem is in minimum-0024, SHA256 b578a01ead261c6f7745122c22f4bb4767884e46ac46e1531b4e749a19332f95. Both results were read completely in this coordinator segment, but their own recovery programs were not executed in this replay. The F9 result's historical C32 conclusion is superseded by V10; no proof claim is inferred from a filename.

## Complete dependencies and exact repair

All THREE parts of this capsule are mandatory. Part1 is material [internal-source-reference], save literally as universal285_part1.txt, 12079bytes, SHA256 74233c80e38f06ad34a4eb03bb021a7d3ee717ad277edf80a3ffe810f0f55199. Part2 is [internal-source-reference], save literally as universal285_part2.txt, 12231bytes, SHA256 2994af9cce727f52469520689a306ad05f4799ef689f2667241f52ad2c17de1d. These are complete exact extractions, respectively UTF16 intervals [1025907,1037986) and [1038027,1050258), from [internal-source-reference], archive SHA256 db8099898f50df5541a8bfdc98ad81032beee03b6c18555b3fb4cc75951a8ae7. No originating sandbox is needed.

Remove only the enclosing text fences, concatenate the two complete spans in order, and apply the ONE historical catalogue-hash correction encoded below. It changes neither universal source code nor coefficients. The corrected recover_quad10.py is 24289bytes, SHA256 fc6fb7a3b0fd6e44fa4e69145e38453d131136e34cbe1cd9033e27791954f5f2. Its complete nine-source bundle is checked during extraction. Whitespace-free base85 is 20038bytes/SHA256 bd39c1d965fd9c5e64d34d20a7b98eec55f08497df518319b3c1f3be41f77022; decompressed JSON is 48676bytes/SHA256 94ba86676388c079c531c90afe7c298f7470b8edf13760567d1ae9ea1c45f239.

Save the following complete source as replay_universal285.py, UTF8/LF/finalLF. Its exact length is 2189bytes, SHA256 d4670f21f46acfddf5aaa7bf509beca83baf32025b127b75da148417538e4412.

```python
"""UNIVERSAL285_CORRECTED_COLD_REPLAY_V1. All three capsule parts are required.
python -S replay_universal285.py extract
python replay_universal285.py build
python -S replay_universal285.py check
"""
from pathlib import Path
import hashlib,json,os,subprocess,sys
assert __debug__
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
def read_pinned(name,want):
    b=Path(name).read_bytes();assert pin(b)==want,(name,pin(b));return b
parts=[('universal285_part1.txt',[12079,'74233c80e38f06ad34a4eb03bb021a7d3ee717ad277edf80a3ffe810f0f55199']),('universal285_part2.txt',[12231,'2994af9cce727f52469520689a306ad05f4799ef689f2667241f52ad2c17de1d'])]
s=[]
for name,want in parts:
    b=read_pinned(name,want)
    assert b.startswith(b'```text\n') and b.endswith(b'```\n')
    s.append(b[len(b'```text\n'):-len(b'```\n')])
src=b''.join(s)
bad=b'efb10a4657a891cd13f6f62db94164bd4b3005e908dc55aae87db450f704d'
good=b'efb10a4657a891cd13f6f62db94164bd4b3005e908dc55aae87db450930f704d'
assert src.count(bad)==1 and src.count(good)==0
src=src.replace(bad,good)
assert pin(src)==[24289,'fc6fb7a3b0fd6e44fa4e69145e38453d131136e34cbe1cd9033e27791954f5f2']
Path('recover_quad10.py').write_bytes(src)
subprocess.run([sys.executable,'-S','recover_quad10.py','extract'],check=True)
mode=sys.argv[1] if len(sys.argv)>1 else 'check'
assert mode in ('extract','build','check')
env=dict(os.environ,OPENBLAS_CORETYPE='SkylakeX',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',PYTHONHASHSEED='0')
if mode=='build':
    assert sys.version_info[:3]==(3,13,5)
    subprocess.run([sys.executable,'build_universal.py'],env=env,check=True)
if mode!='extract':
    data_pin=[1289123,'3a00b679c994255debd3acbe5d3230e336d1e292b9cf88507dc1d2c61fc94496']
    report_pin=[41790,'067c8ae69857aece263ccaeb5b1e05e4d401d90f13f5d8ee8d64e3847358acec']
    read_pinned('universal285.json',data_pin)
    subprocess.run([sys.executable,'-S','verify_universal.py','universal285.json'],env=env,check=True)
    read_pinned('universal285_verification.json',report_pin)
    print('UNIVERSAL285_CORRECTED_COLD_REPLAY_V1_EXACT_DATA_AND_REPORT_PASS')
else:print('UNIVERSAL285_CAPSULE_SOURCES_ONLY_NO_MATHEMATICAL_REPLAY')
```

## Reconstruction and exact acceptance

In a fresh directory containing the three saved parts/source, run:

```sh
python -S replay_universal285.py extract
python replay_universal285.py build
python -S replay_universal285.py check > replay_universal285_transcript.txt
```

Generation environment actually used: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, OpenBLAS0.3.30, Linux x86_64; NumPy ILP64 and SciPy LP64. OPENBLAS_CORETYPE=SkylakeX, OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1, PYTHONHASHSEED=0, four fork workers. All tree inputs, apex choices, eps=1e-7, maxouter=11, rounding power8 and locator loops are inside the pinned sources. No random input. Frozen verification needs only the Python standard library, with assertions enabled. The numeric eps only locates certificates; exact integer positivity decides acceptance.

The newly reproduced files are:
- universal285.json: 1289123bytes, SHA256 3a00b679c994255debd3acbe5d3230e336d1e292b9cf88507dc1d2c61fc94496.
- universal285_verification.json: 41790bytes, SHA256 067c8ae69857aece263ccaeb5b1e05e4d401d90f13f5d8ee8d64e3847358acec.
- replay_universal285_transcript.txt from the displayed check command: 534bytes, SHA256 ce691f7914e07b97382f1db4eb2982717005cb13ae92beab5c44883ebf056228.

Exact check stdout:
```text
QUAD10_SOURCES_AUTHENTICATED_NO_MATHEMATICAL_REPLAY
INDEPENDENT_ROOTED_MULTISET_ENUMERATION_PASS [1, 1, 2, 4, 9, 20, 48, 115, 286]
SCALAR_POLYNOMIAL_INTEGER_BAREISS_AND_FRACTION_LDL_PASS 17416 156744
ACTUAL_NINE_FAN_VOLUME_FIRST_COVARIANCE_AND_WEIGHTED_IDENTITY_PASS 285
BROOM_34_STRICT_REDIRECTIONS_AND_ONLY_ALTERNATE_2_TO_8_PASS
UNIVERSAL_285_EXCLUSION_PASS_ONE_BROOM_REMAINS_NO_V10_CLAIM
REPORT 41790 067c8ae69857aece263ccaeb5b1e05e4d401d90f13f5d8ee8d64e3847358acec
UNIVERSAL285_CORRECTED_COLD_REPLAY_V1_EXACT_DATA_AND_REPORT_PASS
```

The first line refers only to source extraction; the following lines are the mathematical replay. The unrelated ten-whole-C32-types generator contained in the inherited wrapper was NOT run. Newer withdrawn 1330807/41787 variants are NOT the accepted object.

## Mathematical bridge and scope

For a uniform own-centred polytope, every nonroot of a unique-strict-unstable configuration has a true-edge weak escape i->p(i), D_i=x_i^T M(x_p-x_i)>=0. Distinctness gives strict squared-norm growth, hence a rooted spanning tree. Enumerating increasing labels or unordered child multisets gives all286 rooted nine-node shapes.

At a true vertex apex, cone ONE actual boundary triangulation into tetrahedra. For each candidate tetrahedral occurrence let w be its actual determinant magnitude times its actual selection indicator. Unselected zero weight does not imply zero determinant. Either apex fan has total mass D=6Vol(P)>0, zero first moment after centering, and the same second-moment matrix. For four-vertex incidence chi, J=chi chi^T+diag(chi), the identities are sum w=D, X^T sum w chi=0, and sum w X^T J X=20D Cov(P). They hold for true cofacial facets and selected flat cells too.

The integer certificate matrices contain a common first-moment multiplier, nonnegative escape multipliers, and for paired apices opposite common-volume and common-covariance terms. On summing actual weights against G=XMX^T, the moment terms cancel and escape terms are nonpositive. Each exact Q-I is positive definite, while G is nonzero positive semidefinite, forcing the same sum strictly positive. This contradiction excludes the certified tree. All17416 Q blocks were rebuilt as scalar polynomials and checked by both integer Bareiss leading minors and Fraction LDL. The physical nine-vertex fixture additionally checks actual determinant, volume, centroid, covariance and weighted-polynomial identities; it is a regression control, not a 110 body.

This replay repairs the inherited evidence-status gap from encoded-only access to an executed, byte-identical exact certificate. It does not by itself prove ten-vertex impossibility, F>=10, C>=36, or an exact minimum. With the two separate accepted results named above, the existing internal chain remains V>=10,F>=9 and Euler E=V+F-2>=17, so C>=34. The first unresolved joint layer remains (10,17,9). External proof-assistant formalization and peer review are not asserted.
