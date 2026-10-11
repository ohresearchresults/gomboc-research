# Positive basin transfers on actual own211 bodies

The complete method is `basin_transfer.py`. It deforms physical support normals, rebuilds the hull, integrates the same uniformly filled body, and keeps one primal maximum and two polar maxima. It selects a new polar arrow from outside the elder root's entire positive-reachability set into that set. All old positive arrows are initially retained; the junior root's negative guard is released when the junior root itself is the transfer source. The identity a.(b-a)+b.(a-b)=-|a-b|^2 explains why a target in a preserved return component is unsuitable. Relevant external scoped observation: `sources/J121_fixed_policy_exit.md`, exact source SHA fc95dbc358a615d254209a2ed7014fce814c4a8b3fbe019e52822cb20222c0be.

A whole-support Jacobian includes the actual centroid derivative. A linear predictor is followed by own211 correction and complete body checks; accepted stages increase the elder's positive-reachable set. The latest implementation additionally enforces positive margin1e-7 and rejects finite states with actual/committed capacity margin below8e-8, avoiding numerical boundary drift.

## Exact endpoint comparison
- `artifacts/A1_TRANSFER_INITIAL_G15`: V156/E234/F80,C468,own211,weak000,primitive000; soleQ .1121557474039721. Elder support18 is reachable from25 of84 supplied supports,22 of80 active facets.
- `artifacts/A1_BASIN_TRANSFER_CHECKPOINT_G15`: V154/E231/F79,C462,own211,weak000,primitive000; soleQ .3068431396600983. Elder18 is reachable from43 of84 supplied supports,39 of79 active facets. Junior stable carrier changes fromsupport7 tosupport5. Audit SHA 14a21a0a87bbd30f9888c0ff98582fb04b49affc92b265b396eae5e8f8695e95.
- `artifacts/exact-basin-transfer-reach.json` supplies exact positive adjacency and reachable sets for both physical bodies. `exact_polar_reach.py` derives integer sign n_i.(s_i n_j-s_j n_i) where s_i=h_i D-n_i.G>0 and G/D is the audited actual centroid.

The surviving basin became deeper. This is a constructive source for changing its ownership and carrier, not a persistence improvement and not the requested figure. Numerical continuation reached51 of84 supports after25accepted stages, stillown211; phase2 is ongoing. All true hull counts remain below the requested limit.
