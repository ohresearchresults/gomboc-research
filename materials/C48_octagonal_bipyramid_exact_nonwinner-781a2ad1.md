# material-781a2ad11df7

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

# C48 exact bipyramid nonwinner: fixed-apex coarsening seed

Object identity: C48_OCT_COARSEN_234_1112131415 (descriptive only). This is a useful exact nonwinner, NOT an own110 record.

## Literal vertices
Base vertices, cyclic order in z=0:
0=(81893,11577,0)
1=(72672,34322,0)
2=(24199,97028,0)
3=(-77460,-36801,0)
4=(-70503,-52637,0)
5=(-56512,-69350,0)
6=(-31747,-82556,0)
7=(-7429,-85720,0)

Apices:
8=(-11151,-85321,50)
9=(4579,-84983,-1250)

The apex segment meets z=0 exactly at q=(-10546,-85308,0), strictly inside the octagon.

## Exact mass data
Base area = 29718409009/2.
Base area centroid =
(102613703651380/29718409009,
 -100925661844464/29718409009,
 0).

Uniform filled volume = 19316965855850/3.
Uniform filled centroid =
(212971034177953/59436818018,
 -707180719415589/29718409009,
 -300).

The centroid follows from the exact two-pyramid formula
g_xy = 3 c_B/4 + (h_+ a_+ + h_- a_-)/(4(h_++h_-)),
g_z=(h_+-h_-)/4
with h_+=50,h_-=1250.

## Maximal complex and exact expected census
Ordinary octagonal bipyramid:
V=10, E=24, F=16, C=48.
Every maximal face is one apex joined to one cyclic base edge. True edges are the 8 base-cycle edges plus all 16 apex-to-base edges.

At the exact uniform filled centroid with the standard Euclidean metric the strict census is (S,U,H)=(2,2,2), additional weak=(0,0,0), primitive-zero=(0,0,0).
Using local base labels 0..7 and apices 8,9:
stable facets are (8,1,2) and (9,2,3);
unstable vertices are 2 and 3;
mixed true-edge equilibria are edges (0,9) and (2,3).
Morse check: 2+2-2=2.

This material preserves the exact object itself. It does not promote the prior 3003-subset enumeration to a separate theorem capsule and does not claim an affine-orbit exclusion.
