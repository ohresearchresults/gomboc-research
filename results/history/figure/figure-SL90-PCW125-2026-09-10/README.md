# Protected PCW125 coarsening and relative derivative normalization

Original complete report: REPORT.md; immutable result SHA-256 e5781929322e9594285962bb84597984f4414518069a9255b8b37b9c1689cf9e. Both literal source files and all 132 parent control triples are preserved.

Local run of `python3 -S coarse125.py` passed parent-source pins and protected-contact/boundedness checks for both PCW125 and CAP16. Each has the proved combinatorial budget E <= 323. This is NOT a new exact equilibrium census or a new Gömböc; the C634 benchmark is unchanged.

Generated files and SHA-256:

- PCW125_CONFIG.json: 9852 bytes, e980e5f5d3f3de72b901d4abf0c145f24733339569e788c8aa7392cd5f136037
- PCW125_RAW.json: 66862 bytes, 0559412b5a680b5d8c6644435ba7b76159d917733b6c1d6ce2879dcc13772742
- PCW125_CAP16_UNAUDITED_CONFIG.json: 9888 bytes, 779b5cdfca54d41fbcfff3b475008334ec7935a69b53829f358022a9793771e6
- PCW125_CAP16_UNAUDITED_RAW.json: 69313 bytes, b50bbfd58b11a3638a78a0d037679425360971806bc3934554d6134ab3f7d6fa

The report derives a sqrt(2) bound on normalized Jacobian row norms including actual centroid derivatives. relative_whitener.py is preserved but not locally run. Numerical S/U counts 52/70 and 14/18 are author-reported, not exact classification. The author explicitly reports SYSTEM ERROR prevented observation of later optimizer completions; no later state is inferred.
