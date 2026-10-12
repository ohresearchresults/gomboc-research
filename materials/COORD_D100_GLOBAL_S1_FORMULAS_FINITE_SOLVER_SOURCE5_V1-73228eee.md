# material-73228eeec330

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# COORD_D100_GLOBAL_S1_FORMULAS_FINITE_SOLVER_SOURCE5_V1

## Status and dependencies

This is a complete reusable exact-formula generator/solver interface and a finite unsuccessful disconnected-component search. It is NOT a new physical body and NOT a global affine-orbit exclusion. Accepted own110 record remains C622. The independently proved D100 Euclidean monostable-component exclusion is the separate material [internal-source-reference], not a consequence of a timeout.

Required complete dependencies: [internal-source-reference] (seed6, SHA572f9bc48c511c01950ed7f8435ea46aded86eec9f05a9a67c54319308aaf85c) and [internal-source-reference] (component5, SHAc20501687f00c2fe8ab00c9377dcd8f213ea238e4eb3b70b67c1bff91b5ddd6c). No historical worker-result dependency. These supply the exact actual-filled-centroid D100 seed and metric_component.py geometry/17-core definitions.

## Exact query semantics

H=[[a,d,e],[d,b,f],[e,f,c]], trace(H)=1, is the metric on the physical OWN-CENTERED polar. The physical Gram metric is proportional to inverse(H), not H. For all180 directed adjacent polar edges the code clears rational denominators and gcd to primitive integer coefficients for E_ij=Qi^T H(Qj-Qi), preserving signs. A strict root has all three adjacent E<0; a nonroot must have at least one E>0, so weak stable faces are excluded. The all-root formula permits every one of60 surviving roots with an exact-one sequential Boolean encoding. Outside the Euclidean component is the disjunction that at least one of its17 defining core rows is <=0.

The exact nonlinear query adds a>0,ab-d^2>0,det(H)>0. These are Sylvester's complete SPD conditions for this symmetric3x3 matrix. The root47 and root1 variants only fix the surviving root. U and H counts remain unrestricted, so even a genuine SPD SAT model still needs the full coupled physical U/H audit before it could be an own110 candidate.

The exact linear outer relaxation removes the nonlinear SPD minors and adds q^THq>0 for every primitive integer direction q in [-2,2]^3 up to sign (49 directions), keeping trace and a>0. These are necessary conditions, not a replacement for SPD. An UNSAT result for this relaxation would exclude its specified query; SAT can be indefinite. No such nontrivial UNSAT was obtained.

## Actually completed finite executions

Seven exact formula runs were completed using the already installed shared library libz3.so.4, whose Z3_get_full_version returned4.13.3.0, through the complete standard-library ctypes interface in global_s1_ctypes.py. z3py was absent; an attempted pip installation failed due unavailable DNS, so no z3py execution or4.15.4 result is claimed.

- Identity fixed H=I/3 without outside restriction: SAT, as expected.
- Identity fixed H=I/3 WITH outside restriction: UNSAT, as expected. This is only an identity control, NOT the global outside query.
- All-root nonlinear outside query,20seconds: UNKNOWN timeout.
- Root47 nonlinear outside query,15seconds: UNKNOWN timeout.
- Root1 nonlinear outside query,15seconds: UNKNOWN timeout.
- Root47 linear49-direction outer relaxation,15seconds: UNKNOWN timeout.
- Root1 linear49-direction outer relaxation,15seconds: UNKNOWN timeout.

Full observed versions, timeout parameters, solver responses/statistics and formula receipts are literal OBSERVATIONS.json in this capsule. CPU time/statistics may change on rerun; UNKNOWN establishes no exclusion.

One all-root numerical MILP outer-relaxation round completed, with a30-second limit and max_rounds=4 requested. The next round was interrupted by the enclosing40-second container limit. Therefore ONLY ONE completed round is counted, NOT four. The complete producer stores intermediate results after each completed round. It maximizes a strict escape margin delta with all roots, directed escape selectors, at least one violated17-core row,49 necessary PSD direction cuts and adaptive rationalized negative-eigenvector cuts. All M, coefficient normalization, bounds, SciPy HiGHS settings and thresholds are in the source. NumPy2.3.5/SciPy1.17.0, OPENBLAS_NUM_THREADS=1,OMP_NUM_THREADS=1.

The one proposed matrix had numerical stable-root1 and delta~.0205069, but eigenvalues[-.0379289717294808,.004519410888007705,1.0334095608414735], so it was rejected. The stored IEEE754HEX matrix is checked EXACTLY indefinite on replay: its leading2x2 principal minor is
-391184979469731560372463205723827/10384593717069655257060992658440192 <0.
No physical affine image or exact nonwinner body is promoted from it.

## Complete recovery and observed cold check

The five-source dictionary below includes global_s1_ctypes.py, linear_s1_ctypes.py, search_other_components.py, OBSERVATIONS.json and REPLAY.py. Decode it exactly. First restore BOTH required materials and run their seed A/B/mass and88-certificate component replay into a fresh root as instructed by att_c205. Then use the complete decoder below to install this addition as root/orbit, copying the unchanged metric_component.py from root/component. Run:

`python -B -S RESTORE_ORBIT.py ORBIT5.b64 restored-root`

Proof replay uses CPython3.13.5 standard library plus available libz3.so.4. It reproduces all seven SMT formula files byte-for-byte from their exact seeds and parameters, verifies the stored indefinite matrix's negative rational minor, and reruns both identity controls with expected SAT/UNSAT. This exact formula/identity/indefinite replay completed from the decoded source in the cold-restored seed/component environment. Expected terminal marker:
D100_GLOBAL_S1_SEVEN_EXACT_FORMULAS_IDENTITY_CONTROLS_AND_INDEFINITE_REJECTION_PASS

Optional numerical repeat, not needed for formula replay:
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B restored-root/orbit/search_other_components.py restored-root/seed-proof NEW_MILP.json 30 4`
Optional new exact solver run:
`python -B -S restored-root/orbit/global_s1_ctypes.py restored-root/seed-proof new-absent-output 20000`
Root-specific append47 or1. Linear example:
`python -B -S restored-root/orbit/linear_s1_ctypes.py restored-root/seed-proof new-absent-output 15000 47 2`
A later SAT/UNSAT outcome must be reported as a new execution, not substituted into these historical observations.

Encoded8840ASCII bytes SHA196ac2ba725400ea54670f0fcf5f5e7678ba3549592e5465021ba883ee403a3e; decoded19574bytes SHAa4894f6aac118655bb2731bfd77978909b10114d4f3cfbb14d7e5dc076079c2e.
Files/bytes/SHA:
global_s1_ctypes.py4181/33147c63b8b5fd3bfa0e06ef150494bebeaf9d0498baa5b8d662a883e88f8004;
linear_s1_ctypes.py2370/7342fa2b22f76bc9c3c27aa83a9f49d67f09920e3aebb56ce7db9412931315c0;
search_other_components.py4032/705e92b0b67d06aa0c78dbcdf851ed2f3786546e7ddbbe6413ccc1f6cba381a1;
OBSERVATIONS.json6305/44071c42ca1c8a0886fd8f65a7bce8c0e3de985ea3f30f21a536ad7a1c13811d;
REPLAY.py1893/87bd8679d5b8bc64519db2e1290a02adfb56b505946d91bb289615fb9994559c.

Generated SMT filenames/bytes/SHA:
s1-control-inside.smt2/53038/2f8ce0e85dcb98231bf7806e25c815245656d7ded6b6c598779874d14d9182c4;
s1-control-outside.smt2/55849/fc36dfcde8d4ccc9c36de0835a40083f6ff6839aa2e38ff39b573c2d3eb86807;
s1-global-20s.smt2/55730/bb9337819a43d98b3096e83c1e9b4508abe64ee27e25d07eb6f0987d955b8436;
s1-root47-15s.smt2/47084/0b8aff4349daf8f3db600ca75be3c964b1e66a2fe1ba5577251683848bcce256;
s1-root1-15s.smt2/47084/2bad060cfbc34dfae67d594e98bee5cf6d0510acd82810044eaefc0dbb498f65;
s1-linear-root47-15s.smt2/49909/09ef6a9f45d9e36d29a3344e7dd87dd1d4177655ec4b44db1cb34552c7ae8954;
s1-linear-root1-15s.smt2/49909/bd39c4b1926ed269bfb6cf5e49a4ffe4deaa661aa51f2c104a459ee71409f92b.

```python
from pathlib import Path
import base64,hashlib,json,lzma,subprocess,sys
assert __debug__
s=''.join(Path(sys.argv[1]).read_text().split()).encode()
assert len(s)==8840 and hashlib.sha256(s).hexdigest()=='196ac2ba725400ea54670f0fcf5f5e7678ba3549592e5465021ba883ee403a3e'
b=lzma.decompress(base64.b64decode(s,validate=True))
assert len(b)==19574 and hashlib.sha256(b).hexdigest()=='a4894f6aac118655bb2731bfd77978909b10114d4f3cfbb14d7e5dc076079c2e'
data=json.loads(b);assert len(data)==5
root=Path(sys.argv[2]);out=root/'orbit';out.mkdir(exist_ok=False)
for name,text in data.items():
 p=Path(name);assert not p.is_absolute()and '..'not in p.parts
 (out/p).write_bytes(text.encode())
m=(root/'component/metric_component.py').read_bytes()
assert hashlib.sha256(m).hexdigest()=='7a37b59660fb20a700a8e9d11832f0a6ceef52fb90089627d80cc5b53f7496fb'
(out/'metric_component.py').write_bytes(m)
subprocess.run([sys.executable,'-B','-S',str(out/'REPLAY.py')],check=True)
```

## Complete literal payload

```text
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
```

## Continuation

The exact Euclidean monostable component is closed out constructively by att_c205, but all-root global query remains open. Better root/outside branching, additional exact necessary PSD cuts, or a genuinely different projective/non-affine construction remain meaningful; repeating a timeout is not evidence. These source files permit exact continuation without any originating sandbox.
