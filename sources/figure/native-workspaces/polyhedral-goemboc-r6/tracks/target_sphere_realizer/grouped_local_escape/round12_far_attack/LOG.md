# Round-12 far-cell attack

Write scope: this directory only.  Parent artifacts are read-only inputs.

Starting handoff:

- strict far side of circuit `(198,263,262,11)`;
- actual hull `(V,E,F)=(61,162,103)` and own-centroid class `(S,U,H)=(2,2,2)`;
- all 61 rows, enlarged base, protected `U8`, and positive-dot route `228-198-263-9-8` present;
- the obsolete literal long rail is intentionally not required;
- inherited U-H and round-4/8/10/12 topology guards remain strict;
- freshest read-only numerical checkpoint is `../row54_combined_hard_slp_round13_far_multiguard_best.csv`, with hard margin `-1.6218351836808317e-4` and no mechanics event recorded.

No winner is claimed at handoff.

## Exact support event and next mechanics obstruction

The interrupted numerical chain was recovered from its downstream source
snapshots.  Seven stored checkpoints, from the Round-12 buffer through the
strict quad far side, independently reconstruct as exact rational 61-row
bodies with `(V,E,F)=(61,162,103)` and class `(S,U,H)=(2,2,2)`.  The enlarged
base, `U8`, the positive-dot route `228-198-263-9-8`, and all accumulated
directed guards are strict at every checkpoint.  The obsolete literal long
rail is intentionally not part of this certificate.

An explicit exact rational moving-base path from the recovered pre checkpoint
to the far checkpoint has its first primitive event at the unique degree-four
root of the `(6,198,244,245)` determinant:

- isolating interval
  `[75431166605432580326582003271/967140655691703339764940800000,
  150862333210865160653164006543/1934281311383406679529881600000]`;
- decimal location `0.07799399824783901`;
- cell/wall/cell f-vectors
  `(61,162,103) -> (61,161,102) -> (61,162,103)`;
- exactly five pre-diagonal and five far-diagonal primitives factor through
  the same event polynomial; every other primitive remains strict;
- both open cells and the algebraic wall retain class `(2,2,2)`.

Continuing the same exact valid far side, all 7,904 primitives remain strict
until the unique degree-nine common root
`vertex:6:5 = edge:5,6:one_minus_t`:

- isolating interval
  `[138486478420360146428372282297/60446290980731458735308800000,
  2769729568407202928567445645941/1208925819614629174706176000000]`;
- decimal location `2.291066601001303`;
- exact class transition `(2,2,2) -> (2,3,3)`;
- simultaneous birth of unstable vertex `U6` and saddle `H(5,6)`;
- support stays `(61,162,103)` and all other accumulated guards stay strict.

Thus this branch is a material exact NONWINNER: the first support wall is
crossable without changing the class, but the next real event is a rigorous
`U6/H(5,6)` no-birth-guard obstruction, not a route to `(1,1,0)`.

Reproduction:

```text
./RUN_ALL.sh
EXACT_ROUND12_QUAD_EVENT_AND_U6_H56_OBSTRUCTION_PASS
INDEPENDENT_EXACT_ROUND12_EVENT_CHAIN_PASS
```

The upstream exploratory guarded-continuation traces remain numerical search
evidence.  This exact packet certifies every stored checkpoint as a body and
the complete continuous pre -> support wall -> far -> next-event path; it does
not claim an exact homotopy for the earlier numerical optimizer traces.
