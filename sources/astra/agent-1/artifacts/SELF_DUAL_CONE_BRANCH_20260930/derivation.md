# Negative self-polar physical construction

Background primary sources found by ordinary web search:
- Alathea Jensen, Self-Polar Polytopes, arXiv:1902.00784, https://arxiv.org/abs/1902.00784
- Joao Gouveia and Bruno F. Lourenco, Self-Dual Polyhedral Cones and Their Slack Matrices, https://arxiv.org/abs/2207.11747; journal DOI10.1137/22M1519869, https://epubs.siam.org/doi/full/10.1137/22M1519869.
These are background sources for negative self-polarity and self-dual cones, not evidence of a qualifying Figure. No claimed monomonostatic theorem was found or assumed.

Own derivation (to be checked by the actual physical census):
Let P=-P^polar in Euclidean R3, with vertices x_i. Then P={x: x_i dot x>=-1 for all i}; its polar vertices are exactly -x_i. At origin the two radial escape problems are isometric, so strictS=strictU. This does not transfer through a displaced centroid.

Choose one vertex w and a rational point v violating only the inequality w dot v>=-1. It is outside only the opposite facet F_w. It lies strictly inside all other inequalities, so the cut H_v={x:v dot x>=-1} removes only w. Since every vertex of F_w and v itself lie inside H_v, stacking v on F_w and cutting w commute. The negative polar swaps these two operations. Therefore
P_new = conv(P union {v}) intersect H_v = conv((P intersect H_v) union {v})
is again negative self-polar. Its literal vertex list is all old vertices except w, the new point v, and cut intersections on the genuine edges incident to w. Those intersections are rational when old points and v are rational. Both sides of the self-polar identity will be checked, not inferred from a guessed incidence.

For a self-polar body, V=F and Euler gives E=2V-2. V<=125 implies E<=248 and 2E<=496 (also V+E+F<=498). We will still count the actual maximal hull facets and edges.

The homogeneous lift cone C=cone{(x_i,1)} is self-dual in Euclidean R4. A common orthogonal O4 change of section preserves this property. With t in R3, use the explicitly rational orthogonal map
O(t) = [[I-2tt^T/(1+|t|^2), 2t/(1+|t|^2)],[-2t^T/(1+|t|^2),(1-|t|^2)/(1+|t|^2)]].
The actual physical section coordinates are
x' = (((1+|t|^2)I-2tt^T)x+2t)/(1-|t|^2-2t dot x).
Only positive denominators are admitted. This is a single Euclidean embedding, not independent primal/dual metrics. A numerical root for the actual uniform volume centroid selects t. A root solver or self-polarity residual is not the goal; actual S/U/H/weak checks must hold on the same physical hull.

Final exact acceptance, if a numeric own110 is found, may use an exact rational full-contact reconstruction near that physical body. Negative self-polarity is a search device and need not be preserved by the final rationalization; the actual exact uniform centroid and complete census govern the goal.
