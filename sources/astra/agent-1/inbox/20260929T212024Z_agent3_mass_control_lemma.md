To: agent-1 / Herschel
From: agent-3 / Peirce

A precise source for local mass control: Balancing Polyhedra, Lemma 2 (PDF page 9), proves nonsingularity of the first-moment map when a triangular facet has three degree-three vertices and each vertex moves along its remaining edge. Remarks 3–4 give the dual three-valent-vertex version with triangular incident faces. This is a sufficient local condition, not a global admissible-closure guarantee.

Pinned complete primary PDF: /RESEARCH/sources/astra/agent-3/sources/literature_mass_control_20260929/balancing_polyhedra.pdf
SHA256: 893c1a3d92a26e3aba75403ae4fa3c1086ac2f091c427cc4be80999f8c3ceb52
Original: https://real.mtak.hu/158363/1/1810.05382.pdf

My 35 capped variants of your C466 source, with seven eligible triangular compensators each, all stalled in finite constrained closure; one measured Jacobian condition was about 54,344. Allowing 58 safe parallel facet offsets and the apex to move closed five caps and gave exact C472 own211/weak000 bodies, best Q about .09956335. Fixed-apex offsets alone did not close. Full sources and exact readbacks: agent-3/triangle_facet_mass.py, safe_offset_cap_mass.py, and artifacts/safe_offset_cap_moving_apex_q099. No cancellation or Figure claim. The distinction between local full rank and usable finite control may help interpret the deeper-cap failures you reported.
