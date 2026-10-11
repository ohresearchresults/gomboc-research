# material-66573d2de273

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# C622_STRESS_SCOPED_CORE_V1 — command correction and completed audit

## Complete dependency and correction

The complete18-source recovery remains unchanged in the three materials, in order:
1. [internal-source-reference]
2. [internal-source-reference]
3. [internal-source-reference]

Its decoded JSON has53710bytes, SHA25619e8fdbcd27fa682fa0c9fcc71d0ac83b2ab409cf2a480d3e3d9d92d68895da1. The exact later delta/checkpoint is the fully read immutable parent figure-0380, SHA256522bb3deeabb87145caf7dc68e421bddc9fcf832d99015b966781c85ca8df7aa. A descendant must retain this explicit parent; these scoped helper sources do not replace it.

**Documentation correction:** Part3's AUDIT_GENERATOR example names a nonexistent generator inside observed/HOMO_LAST_POSITIVE. That directory contains the numerical checkpoint files, not GENERATOR.json. The complete exact positive generator is **delta/inputs/C622_HOMOTOPY_POSITIVE.json**. No code or defining coordinate is changed by this correction. The first attempted command failed with FileNotFoundError before reading a body or creating a proof directory; it is not a failed geometric audit.

Correct commands after source recovery, with new output directories:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B CORE/CHECK_SCOPED_CORE.py
python -B -S CORE/PREPARE_SCOPED.py NEW_CHART_DIRECTORY
python -B -S CORE/AUDIT_GENERATOR.py delta/inputs/C622_HOMOTOPY_POSITIVE.json NEW_PROOF_DIRECTORY
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B delta/RESUME_STRESS.py --checkpoint delta/observed/HOMO_LAST_POSITIVE --stages 1 --base CORE --chart NEW_CHART_DIRECTORY --pair 13 68 --out NEW_CHECKPOINT_DIRECTORY --steps 1 --goal 1e-8
```

The last command is existing-checkpoint replay, not additional optimization. Only the numerical checkpoint folder remains observed/HOMO_LAST_POSITIVE. Do not run the old all76-file-bound PREPARE.py or REPLAY_DELTA.py against this new explicitly scoped core; its complete new wrappers supply the narrower reconstruction/audit contract.

## Newly observed scoped two-auditor completion

The lead executed the corrected AUDIT_GENERATOR command and read its completed terminal output. Independent complete A and B agree byte-for-byte, and the separate centred integer tetrahedron integration confirms actual filled volume and all three zero first moments. Observed markers:

```text
SCOPED_FULL_A_COMPLETE 176 311 137 [1, 1, 0]
SCOPED_TWO_INDEPENDENT_EXACT_AUDITS_PASS
```

Observed positive-body values:
- actual(V,E,F)=(176,311,137), strict(S,U,H)=(1,1,0), weak=(0,0,0);
- generator12920bytes, SHA256ad652fe1f1fb4e076cd9ec0081d1fec6605655e9a762f9020ed2b0a6198b80e2;
- raw17968bytes, SHA256a22e204f37ff13f017183bf3f7c96b948a4439c1c5b28e4df3dbaccd17faec62;
- A=B365643bytes, SHA256ddf606a8a975ced91634963115ccd5e0b74e2bebce3a71b1c78420b683c4b131;
- centred mass marker EXACT_CENTRED_INTEGER_TETRAHEDRA_PASS,348positive tetrahedra, volume agrees with A/B, filled first moments[0,0,0]; common centred denominator67269bits, maximum centred integer coordinate67269bits.

These match the immutable parent's body. This result establishes that the smaller complete helper unit is sufficient for the selected exact C622 continuation; it does not introduce a new body or edge record. The original C622 retained endpoint and its full FULL76 recovery remain separate and unchanged. Exact runtime CPython3.13.5 standard library, assertions enabled. Numerical import/preparation runtime NumPy2.3.5,SciPy1.17.0; inherited stress discovery additionally JAX0.9.0.1.
