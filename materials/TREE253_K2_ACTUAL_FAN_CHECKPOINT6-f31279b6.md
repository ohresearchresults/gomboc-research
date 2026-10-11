# material-f31279b6749c

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# TREE253_K2_ACTUAL_FAN_CHECKPOINT6

## Accepted scope and proof

This is a new exact coordinator result, not the unpreserved numerical assertion in the parent. Native parents read completely this turn: minimum-0078, SHA 2a0d3544bfb7f0c3b6366bdda3555bc650eede67a1444d51a2d7207a0079eecd; and minimum-0069, SHA d0f91982420a008eef0bc169a4c7b9f999710361057096a930facbf9715942ff. Their full-OJ TREE253 hypothesis and their literal 55 incidence rows remain authoritative. The new result excludes root positions 2,3,4,5,6,7 for native parent55 index 4. Positions are along the actual complementary Hamilton path, beginning at the endpoint with smaller native vertex number. Native index 4 is exactly `013 018 0237 078 1245 1278 134 2356 346 456`. No relabelling of facet incidences is performed.

Let x_i be the ten actual vertices at their actual homogeneous volume centroid 0, M positive definite, and A=X M X^T nonzero positive semidefinite. For the required complementary path directed toward root r, put L_i=2e_i e_i^T-e_i e_p^T-e_p e_i^T. The parent's Theorem A proves x_i^T M(x_p-x_i)>=0, hence tr(A L_i)<=0, even at weak arrows. It does not require off-tree arrows to be negative.

For each selected actual apex a, triangulate each genuine polygonal facet not containing a by the specified fan diagonals. The resulting actual tetrahedra cover the convex body, have positive volume fractions theta_aT summing to one, and satisfy sum_T theta_aT X^T 1_T=0 by the true volume centroid formula. The stored integers define g_a, symmetric C_a with sum_a C_a=0 exactly, and mu_aTi>=0 such that every B_aT=g_a 1_T^T+1_T g_a^T+C_a+sum_i mu_aTi L_i satisfies B_aT-I positive definite. Averaging each actual fan and summing fans yields tr[A sum_aT theta_aT B_aT]<=0: centroid terms vanish, C terms cancel, and arrow terms are nonpositive. But every summand has strictly positive trace against nonzero A, contradiction. This uses one actual body, its actual masses, and one metric, not independent occurrence Gram matrices. There is no metric-conditioning or numerical-margin hypothesis on realizations. Diagonals are integration aids, not mechanical edges.

Six explicit certificates contain 90 integer 10x10 matrices. Exact Bareiss leading minors and independent Fraction LDL each pass all 900 leading-minor identities. Thus index4 has only root positions 1 and 8 left after combining with the parent's endpoint exclusions. No whole incidence domain is removed; C>=34 and the 632/52585 global register remain unchanged.

## Reproduction and provenance

Save the following complete code as recover_checkpoint6.py, UTF-8/LF with terminal LF: 16630 bytes, SHA b20721e6f93dfe6fec104e159bda7f87870e91e516e005c9a5b626d2641e4ac5. Run `python -S recover_checkpoint6.py`. This expands eight complete source/input units, verifies their bytes, invokes the independent standard-library exact checker, and compares the complete report. Observed terminal markers: `TREE253_K2_EXACT_FAN_CERTIFICATES_PASS 6 90` and `TREE253_K2_CHECKPOINT6_COLD_REPLAY_PASS`. A cold replay completed successfully. Matrix-stream SHA is 5a62e678617cc565e200b06b7547d952521aebdb94e79fe746909bfa82b5b783. The expanded exact certificates are 10163 bytes, SHA 7cfb73ec8e20870a5469b5e59f0a23c67081f7c8f071b39188ecc7a0c3694e8b.

The numerical locator is also preserved completely, but is not imported during exact verification. Observed environment CPython3.13.5, numpy2.3.5, scipy1.17.0, one BLAS thread through threadpoolctl. For original index4 root4, the eigen-cut LP locator was used; the other five used the convex smoothed minimum-eigenvalue locator with temperatures (.1,.03,.01,.003,.001,.0003,.0001), at most1500 L-BFGS-B iterations per temperature, box bounds given in the complete code, zero initial point and no randomness. Coefficients were rounded to integers at scale2^24 and accepted only after exact verification. Re-running a floating locator need not reproduce identical coefficient bytes; the literal accepted integer checkpoint, independent of the locator, is included losslessly. Unsuccessful locator attempts are UNKNOWN, not exclusions. No upper bound or minimum is claimed.


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]
