# Astra C96 side research — preserved, independently replayed, no own110

The original Astra gpt-6-astra/max task finished with partial progress. C80 own211 is a useful nonwinner, not an improvement of the C622 homogeneous Gömböc record. See JOURNAL-NOTE.md for the concise integration and REPORT.md for the full scientific handoff and scope limits.

- RESULT.json and REPORT.md: exact original handoff.
- RECOVER_EXACT.py: complete self-contained exact-body/certificate package.
- RECOVER_RESEARCH.py: larger self-contained package including numerical methods and checkpoints.
- source/: fresh operator reconstruction from RECOVER_RESEARCH.py; no dependency on the agent's temporary workspace.
- operator-replay.txt and integrity-receipt.json: local verification receipt.
- TASK.json and INPUT-MANIFEST.json: original task and source provenance.

From this directory run `python3 -B -S RECOVER_EXACT.py new-exact-directory` (destination must not exist). Expected marker: ALL_RETAINED_EXACT_BODIES_AND_CERTIFICATES_COLD_PASS_NO_OWN110. Exact replay uses only the Python standard library; the numerical searches were not rerun by the operator.

Source preservation and exact reproduction are distinct from a formal review of every general mathematical argument. The fixed-shape certificate was fully checked; the affine disk/slab computations were checked, with the argument and its strict condition-number restriction retained in REPORT.md.
