# Exact certificate interpretation

The verifier derives the ordinary volume and first moment by the signed tetrahedron formulas V=Σdet(a,b,c)/6 and M=Σdet(a,b,c)(a+b+c)/24. It reintegrates the translated integer coordinates and checks all three moment numerators vanish.

Every outward maximal plane is tested against EVERY listed point, with the full equality/contact set checked. Display diagonals are merged only for exact coplanarity. Maximal face boundary cycles, supporting normal rank three at every point, positive radial triangulation, closed connected oriented sphere topology, and each vertex link are verified. The resulting boundary is the boundary of the convex hull; all listed points are extreme and the facet and edge lists are maximal and complete.

For a facet its exact perpendicular foot is tested against all oriented boundary half-planes; it is stable precisely when all inequalities are strict. For each nonapex vertex an actual positive dot product (v_j−v_i)·v_i excludes radial support; the apex has strict negative dot products along all incident edge rays. This is the complete vertex normal cone test.

For a true edge a,b put d=b−a, l=d·d, t=−a·d/l and q=a+td. First require 0<t<1. If n,m are its outward adjacent normals, detG=(n·n)(m·m)−(n·m)^2>0. The coefficients of q in cone(n,m) have numerators (q·n)(m·m)−(q·m)(n·m) and (q·m)(n·n)−(q·n)(n·m). Strict positivity of all four conditions is exactly a saddle. The implementation uses equivalent oriented cross-product signs, and the second implementation reconstructs the full cone independently. Weak equilibrium cases with zero are separately rejected. Euler is only a consistency check, never used to infer absence of saddles.

All arithmetic affecting acceptance is integer/rational, without geometric tolerances. The finite exact coordinate list, not the preceding numerical optimizer, is the object being certified.
