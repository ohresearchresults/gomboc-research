# material-0e3200d2a882

AI research material

---

# Ordinary bipyramid at its true filled centroid: exact apex support gates

Let the base polygon B lie in z=0. Translate so the line through the two apices crosses z=0 at the planar origin. Write
T = h_+ d,  D = -h_- d,  d=(t,1),
where t is a planar vector and h_+,h_->0. Let c_B be the planar area centroid of B and C=(c_B,0).

Uniform density over the union of the two pyramids gives the exact filled centroid
g = (3/4) C + ((h_+-h_-)/4) d.

Define
alpha = 3 h_+ + h_-,
beta  = h_+ + 3 h_-.

Then
4(T-g) = alpha d - 3 C,
4(D-g) = -beta d - 3 C.

For any base vertex b (embedded as (b,0)), direct expansion gives
4 (T-g)·((b,0)-T)
 = (alpha t - 3 c_B)·b
   + 3 h_+ c_B·t
   - h_+ alpha (1+|t|^2),

and
4 (D-g)·((b,0)-D)
 = (-beta t - 3 c_B)·b
   - 3 h_- c_B·t
   - h_- beta (1+|t|^2).

Let h_B(u)=max_{b in B} u·b be the planar support function; for a polygon the maximum is attained at a vertex. Since each apex is adjacent to every base vertex in an ordinary bipyramid, the top apex T is a strict unstable equilibrium at the true filled centroid exactly when

h_B(alpha t - 3 c_B)
 < h_+ alpha (1+|t|^2) - 3 h_+ c_B·t.

Likewise the bottom apex D is strict unstable exactly when

h_B(-beta t - 3 c_B)
 < h_- beta (1+|t|^2) + 3 h_- c_B·t.

Equality is exactly a weak apex event. Reversing the strict inequality means that apex has at least one strict positive escape to the base.

Scope: these two inequalities classify only the two apex vertices. They do not classify base-vertex unstable equilibria, stable facets, or mixed-edge saddles, so they neither prove nor exclude an own110 ordinary bipyramid. They are an exact reduction for coupled own-centroid searches.
