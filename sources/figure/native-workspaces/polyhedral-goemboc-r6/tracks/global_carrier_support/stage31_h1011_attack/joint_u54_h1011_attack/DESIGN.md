# Joint U54/H1011 bounded sidecar

This directory is isolated from the existing Stage-31 chain. Its source is the
independently verified exact `step13_transfer_far.csv`; its fixed maximal-face
ledger is `continuation/main/exact_full_control_chain_post_faces.json`.

## Search contract

`search_joint_u54_h1011.py` uses the existing 165-mode chart. It solves a finite
rational grid of target-only, topology-guarded, mechanics-guarded, and combined
LPs. Each feasible linear wall is nonlinearly refined against the two raw target
rows, projected back to the exact enlarged-base plane, extended by a rational
post factor, and rebuilt through the fresh hull evaluator.

The final numerical event scan contains 7,922 rows:

- the existing 7,904 support and own-centroid mechanics primitives;
- all 18 directed in-face turns of the enlarged base polygon.

A floating tie is only locator evidence. An exact positive certificate would
need the four raw aliases

```text
vertex:54:1
edge:(1, 54):one_minus_t
edge:(10, 11):t
vertex:10:11
```

to share a nonconstant exact gcd of odd multiplicity, while the other 7,918
rows remain strict through the isolated root interval. The post interval would
then have to reconstruct exactly as class `(2,1,1)` with stable
`{base,S(7,8,245)}`, unstable `{U8}`, and saddle `{H56}`. The current sidecar
does not emit such a certificate skeleton because the fixed-ledger obstruction
below rules out the requested first-event ordering.

## Exact retained-ledger selected-component obstruction

The authoritative Stage-31 owner fixes `SELECTED_COMPONENTS["U54"] == 1` and
`SELECTED_COMPONENTS["H1011"] == "t"`. The statement below is deliberately
limited to that selected pair; it is not a claim about every other defining
component of vertex 54.

For the directed vertex primitive used by `exact_core`,

```text
V(i,j) = -X_i · (p_j-p_i),
X_i = 4*d6*p_i - m24.
```

On the retained base edge `(1,54)`, put `d=p1-p54`. Then

```text
V(54,1) + V(1,54)
= (X_1-X_54) · d
= 4*d6*||d||^2
> 0.
```

At the exact source, `V(54,1)>0` but `V(1,54)<0`. At the nondegenerate,
positive-volume selected U54-neighbor-1 wall, `V(54,1)=0`, so the identity makes
`V(1,54)>0`. Continuity therefore forces `V(1,54)=0` strictly earlier. That
earlier row is the observed `vertex:1:54` / `edge:(1,54):t` mechanics event.
Removing the edge or changing the ledger first would itself violate the
requested no-earlier-event and retained-base/active-row conditions.

`verify_fixed_ledger_obstruction.py` independently recomputes the exact source
signs, the identity, the positive volume and edge length, the face ledger, and
all 37 rails before issuing its receipt.

## Canonical run

```sh
/usr/local/bin/python3 -B verify_fixed_ledger_obstruction.py
/usr/local/bin/python3 -B search_joint_u54_h1011.py
```

The negative search receipt is deliberately not an LP-dual or unrestricted
global impossibility claim. Its exact consequence is limited to the retained
ledger required by this sidecar's contract.
