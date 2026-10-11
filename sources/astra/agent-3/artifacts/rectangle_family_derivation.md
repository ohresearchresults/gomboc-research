# Variable-aspect rectangular section family

At ordered internal heights -1<z_i<1, use G_i(z)=(min(z,z_i)+1)(1-max(z,z_i))/2. Give each of the four unit normals (1,0),(0,1),(-1,0),(0,-1) its own positive rational curvature W_ij. Set b_j(z)=sum_i W_ij G_i(z). A linear endpoint-centre term may be added, and an invertible horizontal affine map A applied.

The physical section before A is [-b_left(z),b_right(z)] x [-b_bottom(z),b_top(z)], translated by (z+1)*tilt/2. Each signed support b_j is concave with a strictly downward derivative jump W_ij at every internal height. Thus the intersection of the four concave-bound sets is convex. Positive W makes every internal width positive and every adjacent segment plane distinct. Each internal level has four vertices, with two endpoint tips. Corresponding horizontal edges remain parallel across levels even though width ratios vary; the connecting side faces are genuinely planar quadrilaterals.

The true hull has V=4L+2, E=4(2L+1), F=4(L+1), hence C=16L+8. L=30 gives V122,E244,F124,C488. It is broader than homothetic rectangle sections because x and y widths vary independently. This is an existence/parameter chart, not by itself a monomonostatic construction.

rectangular_sections.py computes physical vertices and all analytic derivatives, integrates uniform density over the exact nominal oriented boundary triangulation, and forms the polar only about that resulting volume centroid. Its primal and polar persistence graphs use true edges/facets. No integration diagonal is counted as a hull edge. Independent live-hull mass checks agree at the tested start, and exact_section_audit.py interprets saved binary64 z,W,A,tilt as exact dyadic rationals, reconstructs all vertices, checks all face support incidences rationally and then invokes complete pair-line hull/mass/equilibrium auditing. Thus the stored construction preserves all quads exactly.

L30seed2 after search and2-step strict physical retraction: exactC488 own121weak000, not110. Evidence artifacts/rect_sections_L30_s2/polish121/exact_binary. Its exact sole relative finite P depth is approximately .3565330576210195; Q has no positive finite bar.
