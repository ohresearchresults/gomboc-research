# Directed continuum certificate for `row54_round4_null_cross`

## Verdict and scope

`RUN_ALL.sh` rebuilds the proof object and ends with:

```text
PRE_TO_BUFFER_CONTINUUM_PASS
BUFFERED_CROSS_UNIQUE_CIRCUIT_WALL_PASS root=[0.91728407647098942,0.91728407647098942]
FAR_DEEPEN_CONTINUUM_PASS
FOUR_OLD_UH_GUARDS_PASS
EXACT_DIRECTED_ROUND4_NULL_CROSS_PASS
```

This replaces the 123 sampled points by an exact continuum theorem for four
frozen rational nodes and three explicit plane-preserving polynomial morphs:

1. `source -> pre_buffer`;
2. `pre_buffer -> far_good`;
3. `far_good -> deep_far`.

Each CSV coordinate is read as an exact decimal fraction.  Enlarged-base rows
are then projected, in rational arithmetic, onto the exact plane through rows
0,1,2.  Along every morph those anchors move affinely; the other base rows use
linearly varying exact barycentric coordinates, and all nonbase rows move
affinely.  Consequently base coplanarity is an exact polynomial identity.

The theorem applies only to these frozen rational nodes and these three
replacement morphs.  It does not promote the original binary64 27D chart, its
123 samples, or every possible interpolation between its parameters to a
global statement.

## Complete open-cell audits

For every open fixed-lattice interval, the verifier signs all 7,904 defining
polynomials: volume, all face-support determinants, all face-reference
orientations, every edge norm and Gram factor, every directed face component,
every vertex component, and all four components of every edge decision.

| Continuum interval | Lattice | Polynomials | Primitive digest | Minimum Bernstein coefficient, log10 abs |
|---|---|---:|---|---:|
| `source -> pre_buffer` | pre | 7,904 | `04a35ac195fe553e439c61eccc88bb9f3a6cc232ebfb39ad628909335559cda1` | -44.1929370335 |
| middle, `0 <= t <= root.lo` | pre | 7,904 | `fdf5dfb52e91dd9ef8914b2696b2a0dc139ab01e98c6b552a71d3940cc4de2eb` | -71.1383045817 |
| middle, `root.hi <= t <= 1` | far | 7,904 | `ca802c074a9afae880ab3e97c8d1c5d79df12040a7b213e5a8129171abc576e9` | -72.0726560017 |
| `far_good -> deep_far` | far | 7,904 | `f6ca3e8cd31ddb9334c8117ed8912502767c5bcfd2205c7547ddad31bfd88197` | -44.1929359080 |

All four rational endpoints and every open interval have class `[2,2,2]`.
The pre and far cells both have exact `f=[61,162,103]`, Euler value 2, the
enlarged base face, and all 37 forced rail edges.

## The only real wall on the middle segment

The degree-5 circuit polynomial is

```text
det(P8-P7, P245-P7, P246-P7).
```

Its derivative is strictly negative on the complete local interval `[0,1]`.
It has one root in the exact rational bracket

```text
lo = 1692090460154936367859929 / 1844674407370955161600000
hi = 1692090460154936367859930 / 1844674407370955161600000
width = 1 / 1844674407370955161600000
decimal midpoint = 0.91728407647098942
```

The circuit coefficient digest is
`c2402da1b7b4aa539b2ac90fea0859452fbc77eede465f5029101bd38a0f007c`.

There is no uncertified gap inside that narrow bracket.  On each side, exactly
7,899 primitives remain strictly nonzero throughout the whole root
neighborhood.  The remaining five factor exactly through the circuit:

| Side | Target-factored primitives |
|---|---|
| pre | supports `f4/w245`, `f9/w8`; `Gram(7,246)=det²*q`; `beta1(7,246)=det*q1`; `beta2(7,246)=det*q2` |
| far | supports `f7/w246`, `f8/w7`; `Gram(8,245)=det²*q`; `beta1(8,245)=det*q1`; `beta2(8,245)=det*q2` |

Every quotient has a strict exact Bernstein sign on the root bracket.  Thus
the only zeros there are the required two support slacks, disappearing/new
diagonal Gram, and its two beta numerators; they all occur at the same unique
circuit root.

At the root, the two pre faces

```text
(7,8,246), (7,245,246)
```

merge into the exact supporting quadrilateral `(7,8,245,246)`, then split into

```text
(7,8,245), (8,245,246).
```

The diagonal changes from `(7,246)` to `(8,245)`; all other faces and edges are
unchanged.  The merged wall has exact `f=[61,161,102]`, Euler value 2, base and
all rails.  Its support proof contains 5,900 strict nonmember determinants and
the sole nontrivial member identity

```text
coplanarity(row245 in wall face) = -det(7,8,245,246).
```

The wall mechanics proof signs all 1,933 non-support mechanics/incidence
polynomials, including every Gram.  Its class remains `[2,2,2]`; the local
stable face transfers

```text
(7,245,246) -> (7,8,245,246) -> (7,8,245),
```

while unstable vertices stay `{8,54}` and saddle edges stay
`{(6,7),(198,263)}`.

## Four protected old U/H guards

The verifier separately checks these four requested names on every open piece,
on both root-neighborhood ledgers, and on the grouped-wall bracket:

```text
U263                 vertex:263:10
H(10,263)            edge:10,263:one_minus_t
U1                   vertex:1:54
H(1,54)              edge:1,54:t
```

Within each pair the two denominator-cleared polynomials are literally equal.
Both common numerators are strictly negative throughout; therefore all four
requested nonbirth guards are strictly positive.  No U/H mechanical wall is
hidden before, at, or after the topology flip.

## Exact sources and hashes

Frozen endpoint coordinate hashes:

| Node | Coordinate hash |
|---|---|
| source | `6a046079e645fe2aa1444972df02d0d8c5eaf5f215261a2b6e0a5225626d9d4b` |
| pre buffer | `2253e9964de324226f63be72387870406e8a0288157852d48ebb3b130648d35c` |
| far good | `c958851c5530b9574578e7e382193e54c9a3e1399f50ef3d8f7d441b933d9973` |
| deep far | `a37c1bbbd2c744c62f9408782c1ba37ae93be9e34ab541d6d6ce37b945105007` |

Face ledgers:

| Lattice | Source-file SHA256 | Canonical ledger hash |
|---|---|---|
| pre | `277c9f8373b886d3dda47b03183c9d9a49575100b1339576cfed8af004a218fc` | `4f50f9ffb003c32a424a64132ad9244f2e76dff12f149bbf9e2f7d7052986381` |
| wall | `491b8a64c6af9359e02f1b66404aa2bea3e1dde9ff69b135f550029b4d6f399c` | `4de8e2912b3e8adf0a262dbfed58749ae6649ce04f30bda79a7167cd028baa25` |
| far | `db6b4d8c8b409b756ca1072f26df1c02bd61f91c8a0e0790b5603a80d38ee9ed` | `ef8a1109f97a6f4637d8c55a6e8424f541842208948d396df40ed857a88d6d45` |

The clean-pass certificate SHA256 is
`c7453f272e7a550d5e304c0c3e26c9b9906101b2d663745f1b859fb0049d3936`.
All 14 input hashes, exact circuit coefficients, rational root endpoints,
frozen coordinates, factor ledgers and primitive digests are serialized in
`certificate.json` and `verification_summary.json`.

Reproduce with:

```bash
./RUN_ALL.sh
```

