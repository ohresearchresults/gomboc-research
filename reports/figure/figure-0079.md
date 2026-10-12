# figure-0079

AI research report · 2026-08-26 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Exact whole-block continuation — negative handoff

## Verdict

**No homogeneous convex polyhedral Gömböc was found.** The strongest realized endpoint is an exact, uniform-density, own-centroid, open `(S,U,H)=(2,1,1)` body. It has one residual stable–saddle pair and is not a Gömböc.

The acceptance gate is a finite materialized body at its own uniform-volume centroid with strict `(1,1,0)`, complete incidence and all-feature witnesses, exact/directed verification, and OBJ/STL; near-wall or auxiliary-center objects do not qualify.

The supplied journal records the requested seed as exact `(V,E,F,C)=(16,42,28,84)`, centroid zero, class `(2,3,3)`, with defect strip `F11→F05→F04→F00`, extra `V0,V7`, and saddles `(0,1),(0,7),(1,7)`. Its literal coordinate artifact was not present in the attachment, so I do not claim direct coordinate surgery on it. The assignment allowed abandoning it for a better small topology; the continued exact Santaló/projective topology begins at one pair `(2,1,1)` and hard-wires the own centroid.

## Strongest exact body: `postwall22`

- `P: (V,E,F,C)=(40,60,22,120)`; dual/source `Q:(22,60,40)`.
- Final uniform-volume centroid: exactly `(0,0,0)`; exact first moment `(0,0,0)`.
- Exact Fraction volume is emitted by the verifier; decimal `0.020771447001019006`. Pre-gauge centroid `(-0.004351446834865003, -0.004477272839241133, 8.225820822586442e-05)`.
- Strict class `(2,1,1)`; minimum normalized inactive separation `P=1.2999276831226195e-05`, `Q=3.9778129616448567e-05`.
- Directed coordinate radius `1/274877906944=2^-38`, independently perturbing every pre-gauge source coordinate and recomputing the polar, centroid, and gauge.

### Deterministic exact source

Each hexadecimal literal is interpreted as its exact IEEE-754 dyadic rational. Form `P0={x:q_i·x≤1}`, compute its exact uniform centroid `c`, and set `b_i=q_i/(1-q_i·c)`. Then `{x:b_i·x≤1}=P0-c`, hence the final centroid is exactly zero.

```python
from fractions import Fraction
Q_HEX = [
  ['0x1.c17104ee3855bp-1', '0x1.07bc2560fdbf0p-1', '-0x1.7cf05e7c06f27p+7'],
  ['0x1.a78ea2c80df0ep-2', '0x1.d6a3835bc2fcbp-1', '-0x1.072b1b3220a68p+8'],
  ['0x1.5b4c0df834fe6p-1', '0x1.8017f5ce609c7p-1', '-0x1.c0787109fc1d1p+7'],
  ['0x1.fe59274708366p-1', '0x1.65b9eb7814a8ep-3', '-0x1.268ab467c2b58p+7'],
  ['0x1.f6a530d0ebf20p-1', '0x1.ec0b5a3b243fcp-3', '-0x1.355433782c057p+7'],
  ['-0x1.e33b73ee1802fp-1', '-0x1.6898062110470p-3', '-0x1.60afb0df76639p+6'],
  ['-0x1.f65cd4188677fp-1', '0x1.3ba2ec3996fbfp-3', '-0x1.0c3f78c7c3060p+7'],
  ['-0x1.b5c21f63f66d2p-1', '0x1.08e965b94c6d5p-1', '-0x1.66b09a9813197p+7'],
  ['-0x1.5efb524667179p-2', '-0x1.d80bc3e44243fp-1', '-0x1.881bc89bda294p+2'],
  ['-0x1.4e7c920d35a17p-1', '0x1.809de8662f9a7p-1', '-0x1.a6eec65869bc4p+7'],
  ['-0x1.89851baa2d872p-2', '0x1.e198bf3e8a181p-1', '-0x1.06494e90b492bp+8'],
  ['0x1.e928eb6b72b4ap-1', '-0x1.97af0ec5182d8p-3', '-0x1.6aab5369e5159p+6'],
  ['0x1.a49d453b447e4p-1', '-0x1.eb6c08c56c86ap-2', '-0x1.9c0e1a733b7e1p+5'],
  ['0x1.439a4f3d49a31p-2', '-0x1.d3fc145161feep-1', '-0x1.a9d9d7d2baa81p+0'],
  ['0x1.3060c46c8f27cp-1', '-0x1.76dfba6a4f214p-1', '-0x1.21ed0cfa3d3a6p+4'],
  ['-0x1.4405ea98b2962p-1', '-0x1.67ef86a0c8a42p-1', '-0x1.8cc2607fa6722p+4'],
  ['-0x1.a58785d753029p-1', '-0x1.e5ffc10a55cacp-2', '-0x1.9e7ab9f002449p+5'],
  ['-0x1.6f4c5c3b43b25p-9', '0x1.7eaed96aab053p-9', '0x1.6dd46a981ba03p+8'],
  ['0x1.bd50a391af669p-6', '0x1.91c26c404d84dp-1', '-0x1.f2f315aeafc66p+7'],
  ['-0x1.22b620382be9dp-3', '0x1.40aad1f8d86b5p-2', '-0x1.8671d85af39a7p+7'],
  ['0x1.2957bf93a4218p-7', '-0x1.09ff88efb8375p+0', '0x1.39dfb49c05948p+0'],
  ['0x1.90f3781558455p-7', '-0x1.07d2619dd366ap+0', '-0x1.d80f6000bbbf2p-8'],
]
Q = [tuple(Fraction.from_float(float.fromhex(x)) for x in r) for r in Q_HEX]
```

Boundedness is witnessed by positive source tetrahedron `(3,16,17,19)` with weights `(0.247051026191826, 0.250901747034251, 0.255060614471617, 0.246986612302306)`.

### Complete maximal faces

F00=(0,2,4,3,1); F01=(0,1,6,9,8,7,5); F02=(0,5,2); F03=(1,3,10,11,12,13,6); F04=(3,4,10); F05=(14,16,15); F06=(14,15,18,17,19,20); F07=(17,18,22,21); F08=(23,25,27,26,24); F09=(21,22,28); F10=(7,8,29,19,17,21,28); F11=(11,30,31,12); F12=(30,32,33,34,31); F13=(35,37,36); F14=(32,35,36,33); F15=(23,24,38); F16=(14,20,25,23,38,16); F17=(2,5,7,28,22,18,15,16,38,24,26,37,35,32,30,11,10,4); F18=(8,9,29); F19=(6,13,39,27,25,20,19,29,9); F20=(26,27,39,34,33,36,37); F21=(12,31,34,39,13).

### Complete true edges and incident faces

(0,1)[F00,F01]; (0,2)[F00,F02]; (0,5)[F01,F02]; (1,3)[F00,F03]; (1,6)[F01,F03]; (2,4)[F00,F17]; (2,5)[F02,F17]; (3,4)[F00,F04]; (3,10)[F03,F04]; (4,10)[F04,F17]; (5,7)[F01,F17]; (6,9)[F01,F19]; (6,13)[F03,F19]; (7,8)[F01,F10]; (7,28)[F10,F17]; (8,9)[F01,F18]; (8,29)[F10,F18]; (9,29)[F18,F19]; (10,11)[F03,F17]; (11,12)[F03,F11]; (11,30)[F11,F17]; (12,13)[F03,F21]; (12,31)[F11,F21]; (13,39)[F19,F21]; (14,15)[F05,F06]; (14,16)[F05,F16]; (14,20)[F06,F16]; (15,16)[F05,F17]; (15,18)[F06,F17]; (16,38)[F16,F17]; (17,18)[F06,F07]; (17,19)[F06,F10]; (17,21)[F07,F10]; (18,22)[F07,F17]; (19,20)[F06,F19]; (19,29)[F10,F19]; (20,25)[F16,F19]; (21,22)[F07,F09]; (21,28)[F09,F10]; (22,28)[F09,F17]; (23,24)[F08,F15]; (23,25)[F08,F16]; (23,38)[F15,F16]; (24,26)[F08,F17]; (24,38)[F15,F17]; (25,27)[F08,F19]; (26,27)[F08,F20]; (26,37)[F17,F20]; (27,39)[F19,F20]; (30,31)[F11,F12]; (30,32)[F12,F17]; (31,34)[F12,F21]; (32,33)[F12,F14]; (32,35)[F14,F17]; (33,34)[F12,F20]; (33,36)[F14,F20]; (34,39)[F20,F21]; (35,36)[F13,F14]; (35,37)[F13,F17]; (36,37)[F13,F20].

### Exhaustive equilibrium classification

The following signed margins exhaust every maximal face, actual vertex, and true edge/full two-face normal cone. Positive means equilibrium of that type; negative means the closest violated witness. Exact residuals, derivatives, `t,alpha,beta`, cone coefficients, and every sign are in the linked audit CSVs.

**Faces:**  
F00:-0.4653067948@F01; F01:-4.478449514e-07@F10; F02:-0.4555259632@F01; F03:-0.5843116506@F00; F04:-0.5840066817@F00; F05:-0.8340344341@F06; F06:-0.6035848544@F07; F07:-0.5171083457@F10; F08:-0.9610234944@F16; F09:-0.5595598867@F10; F10*:+1.231113396e-05@F01; F11:-0.8373470036@F03; F12:-0.9363363586@F11; F13:-0.8809976913@F12; F14:-1.008120353@F12; F15:-0.9725171799@F16; F16:-0.8936390313@F05; F17*:+0.9547023614@F20; F18:-0.1334598091@F01; F19:-0.6292871748@F18; F20:-0.726603607@F17; F21:-2.100916056e-06@F20.

**Vertices:**  
V00:-0.03226663892@V02[0,1,2]; V01:-0.3418264161@V06[0,1,3]; V02:-0.08600623668@V05[0,2,17]; V03:-0.05836584855@V10[0,3,4]; V04:-0.0815792045@V02[0,4,17]; V05:-0.0851434439@V07[1,2,17]; V06:-0.8936057982@V13[1,3,19]; V07*:+0.7016697268@V05[1,10,17]; V08:-0.4965576962@V29[1,10,18]; V09:-0.5929725356@V06[1,18,19]; V10:-0.2817420482@V04[3,4,17]; V11:-0.02718623787@V10[3,11,17]; V12:-0.2497896002@V31[3,11,21]; V13:-0.1614038557@V12[3,19,21]; V14:-0.2785934623@V20[5,6,16]; V15:-0.01605403487@V18[5,6,17]; V16:-0.05566846421@V15[5,16,17]; V17:-0.2289754434@V19[6,7,10]; V18:-0.01496181025@V22[6,7,17]; V19:-0.746054726@V20[6,10,19]; V20:-0.5692347125@V25[6,16,19]; V21:-0.3586595579@V22[7,9,10]; V22:-0.06390250086@V28[7,9,17]; V23:-0.1183286097@V24[8,15,16]; V24:-0.0426460401@V38[8,15,17]; V25:-0.07481307835@V27[8,16,19]; V26:-0.01590822775@V24[8,17,20]; V27:-0.1345734645@V26[8,19,20]; V28:-0.05113032292@V07[9,10,17]; V29:-0.2972235652@V19[10,18,19]; V30:-0.04779595459@V11[11,12,17]; V31:-0.269783832@V34[11,12,21]; V32:-0.03345482674@V30[12,14,17]; V33:-0.302005227@V36[12,14,20]; V34:-0.257240208@V33[12,20,21]; V35:-0.02724326516@V32[13,14,17]; V36:-0.2127802071@V37[13,14,20]; V37:-0.08560754546@V35[13,17,20]; V38:-0.04391886405@V16[15,16,17]; V39:-0.0003028155621@V27[19,20,21].

**Edges/full normal cones:**  
(0,1):-148.3001583[F00,F01;-111-1]; (0,2):-272.2074611[F00,F02;-111-1]; (0,5):-311.8506128[F01,F02;11-11]; (1,3):-221.3404782[F00,F03;1-1-11]; (1,6):-92.88364674[F01,F03;-11-11]; (2,4):-0.0815792045[F00,F17;1-111]; (2,5):-0.08600623668[F02,F17;-1111]; (3,4):-280.0749469[F00,F04;11-11]; (3,10):-1040.832896[F03,F04;-111-1]; (4,10):-0.2817420482[F04,F17;1-111]; (5,7):-0.0851434439[F01,F17;-1111]; (6,9):-147.3148951[F01,F19;1-1-11]; (6,13):-30.13554954[F03,F19;-111-1]; (7,8):-0.0001473988697[F01,F10;111-1]; (7,28):-0.05113032292[F10,F17;1-111]; (8,9):-88.76679596[F01,F18;-11-11]; (8,29):-75.09657273[F10,F18;-11-11]; (9,29):-358.8901071[F18,F19;1-1-11]; (10,11):-0.02718623787[F03,F17;1-111]; (11,12):-165.3748925[F03,F11;11-11]; (11,30):-0.04779595459[F11,F17;1-111]; (12,13):-0.1614038557[F03,F21;1-111]; (12,31):-0.2497896002[F11,F21;-1111]; (13,39)*:+1.603243293e-05[F19,F21;1111]; (14,15):-180.3830036[F05,F06;111-1]; (14,16):-101.0639682[F05,F16;11-11]; (14,20):-65.40477027[F06,F16;-11-11]; (15,16):-0.05566846421[F05,F17;1-111]; (15,18):-0.01605403487[F06,F17;-1111]; (16,38):-0.04391886405[F16,F17;1-111]; (17,18):-195.7705019[F06,F07;111-1]; (17,19):-89.7954697[F06,F10;-111-1]; (17,21):-153.1838755[F07,F10;111-1]; (18,22):-0.01496181025[F07,F17;-1111]; (19,20):-52.79332624[F06,F19;-111-1]; (19,29):-291.5077856[F10,F19;1-1-11]; (20,25):-40.66619974[F16,F19;-111-1]; (21,22):-256.5636052[F07,F09;-111-1]; (21,28):-344.4493206[F09,F10;-111-1]; (22,28):-0.06390250086[F09,F17;-1111]; (23,24):-7.71061139[F08,F15;-111-1]; (23,25):-6.626865271[F08,F16;111-1]; (23,38):-45.33467994[F15,F16;111-1]; (24,26):-0.01590822775[F08,F17;1-111]; (24,38):-0.0426460401[F15,F17;-1111]; (25,27):-5.997427026[F08,F19;-111-1]; (26,27):-0.1345734645[F08,F20;1-111]; (26,37):-1.123821814[F17,F20;11-11]; (27,39):-0.0003028155621[F19,F20;1-111]; (30,31):-104.6993482[F11,F12;11-11]; (30,32):-0.03345482674[F12,F17;1-111]; (31,34):-0.269783832[F12,F21;-1111]; (32,33):-28.54789593[F12,F14;11-11]; (32,35):-0.02724326516[F14,F17;1-111]; (33,34):-0.257240208[F12,F20;1-111]; (33,36):-0.302005227[F14,F20;-1111]; (34,39):-2.73777092e-06[F20,F21;11-11]; (35,36):-1.913980103[F13,F14;1-11-1]; (35,37):-0.08560754546[F13,F17;1-111]; (36,37):-0.2127802071[F13,F20;-1111].

Stars mark equilibria. Thus stable faces are exactly `F10:+1.23111339577e-5` and target `F17:+0.954702361379`; unstable vertex is exactly `V07:+0.701669726781`; saddle is exactly edge `(13,39)` on `F19,F21`, dual Q-edge `(19,21)`, margin `+1.60324329322e-5`. Nearest transfer walls are `F01:-4.47844951356e-7`, `F21:-2.10091605617e-6`, and edge `(34,39)` on `F20,F21` at `-2.73777091966e-6`.

### Directed open-chamber certificate

- `pre_gauge_raw_nonincidence` ≥ `0.0000397019090702517505647069`
- `post_gauge_raw_nonincidence` ≥ `0.0000398813984365891574835396`
- `oriented_six_tetra_volume` ≥ `2.52361803709907683395607833357961162004972376101718142724044996488802932479781746899416396760528528067175871E-7`
- `projective_denominator` ≥ `0.96990837001798248512405581027`
- `face_witness_coefficient` ≥ `3.06339000009358506743E-7`
- `vertex_witness_raw_derivative` ≥ `0.00005739694568905752465664675650`
- `edge_full_cone_or_segment_coefficient` ≥ `8.3504149376414524711627558624990821540838916840563091940138712774806633306504673578168496057548171060736098291E-8`

For every coordinate in the `2^-38` box, the realized f-vectors remain `P:(40,60,22)`, `Q:(22,60,40)`, and class remains `(2,1,1)`. This is an open strict fallback, not a wall point.

Artifacts: source (`postwall22_source_hex.json`), generator (`generate_postwall22.py`), independent Fraction verifier (`verify_postwall22.py`), directed verifier (`verify_interval_postwall22_decimal.py`), exact record (`postwall22_exact.json`), face audit (`face_audit.csv`), vertex audit (`vertex_audit.csv`), edge audit (`edge_audit.csv`), P OBJ (`postwall22_P.obj`), P STL (`postwall22_P.stl`).

## Actual crossed topologies

Every checkpoint below is rebuilt from exact dyadic binary64 values with a directed `2^-70` box, complete original-row incidence signature, exact projective own-centroid identity, and exhaustive all-feature signs.

| checkpoint | active original rows | P/Q f-vectors | class | stable rows | saddle Q-edges | topology change | smallest sign bound |
|---|---|---|---|---|---|---:|---:|
| `polar_cma_local_s1.json` | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 24]` | `(40, 60, 22)/(22, 60, 40)` | `(3, 1, 2)` | `[10, 17, 24]` | `(19,24);(21,24)` | `False` | `2.1653527e-06` |
| `cma_cont1.json` | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 24]` | `(40, 60, 22)/(22, 60, 40)` | `(3, 1, 2)` | `[1, 17, 24]` | `(19,24);(21,24)` | `True` | `2.6535305e-06` |
| `cma_all1.json` | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 24]` | `(40, 60, 22)/(22, 60, 40)` | `(3, 1, 2)` | `[10, 17, 24]` | `(19,24);(21,24)` | `True` | `7.7941486e-07` |
| `cma_all2.json` | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 24]` | `(40, 60, 22)/(22, 60, 40)` | `(3, 1, 2)` | `[10, 17, 24]` | `(19,24);(21,24)` | `True` | `4.6392191e-07` |
| `cma_all3.json` | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 24]` | `(40, 60, 22)/(22, 60, 40)` | `(3, 1, 2)` | `[10, 17, 24]` | `(19,24);(21,24)` | `True` | `6.5186003e-08` |
| `jax_refine1.json` | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]` | `(40, 60, 22)/(22, 60, 40)` | `(3, 1, 2)` | `[10, 17, 21]` | `(19,21);(20,21)` | `True` | `2.8795231e-07` |
| `jax_refine2.json` | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]` | `(40, 60, 22)/(22, 60, 40)` | `(2, 1, 1)` | `[10, 17]` | `(19,21)` | `False` | `8.3507047e-08` |

Certified sequence: `(3,1,2)` six times, then `(2,1,1)`. Several incidence signatures change; original row `24` is replaced by rows `20,21`. The final `jax_refine1→jax_refine2` step performs a real `S–H` cancellation inside the same final lattice. No checkpoint is `(1,1,0)`. Full realized incidence for every checkpoint: directed_transition_ledger.json. Replay: rebuild_directed_transition_ledger.py.

## Smallest surviving coupled obstruction

Preserve target `F17,V07`. The remaining basin is extra stable `F10`, saddle `P(13,39)/Q(19,21)`, stable-transfer wall `F01`, and saddle-transfer wall `P(34,39)/Q(20,21)`. Stable equilibrium transfers between rows `10` and `1`; the saddle transfers between the two Q-edges incident to row `21`.

For a strict radial-dominance chain `q0,…,qm`, multiplication of `r_{i+1}cos(delta_i)>r_i`, spherical triangle inequality, and concavity of `log cos` give the necessary condition `r_target cos(Theta/m)^m>r_source`. Exact-coordinate cases:

- `y_patch_gate_exact.json` row `18→17`: angle `179.810375715°`, minimum `12` edges; ratio at `m-1` `0.962495103432`, at `m` `1.00052327417`.
- `postwall22_exact.json` row `10→17`: angle `179.777448552°`, minimum `13` edges; ratio at `m-1` `0.972511762907`, at `m` `1.00471991339`.
- `postwall22_exact.json` row `1→17`: angle `179.780308071°`, minimum `13` edges; ratio at `m-1` `0.972503602205`, at `m` `1.00471255756`.

Thus final rows `10→17` and `1→17` require at least thirteen edges. Also, Cauchy–Schwarz shows `1-a·b/||a||²` and `1-a·b/||b||²` cannot both be negative, so rows `1,10` can only transfer the source; a third row and a long two-dimensional strip are mandatory. Runnable proof: radial_chain_obstruction.py.

## Search boundary

- Exact one-pair seed, seven-row connected Y-patch, row insertion/deactivation and circuit crossings, CMA and differentiable refinement.
- Seven directed-certified checkpoints, ending in the exact open `(2,1,1)` body.
- `3,600` full-hull local samples, `1,496` distinct local signatures, no `(1,1,0)`; best stored non-target score `-1.37803992846e-5`.
- One/two-rail families at 10–24 links and differentiable refinement; best refined rail score `-0.0265916596`, with additional equilibria rather than cancellation.
- Radial-only continuation, best non-target score about `-1.66e-5`.

Numerical nonhits are observations, not global exclusions. Rigorous claims are limited to the exact body/verifier, directed boxes, directed topology ledger, and radial/transfer lemmas.

## Continuation

The next nonredundant move is a jointly optimized thirteen-edge-or-longer bifurcated source strip: one branch from the row-`1/10` basin toward row `17`, a second replacing Q-edges `(19,21)/(20,21)`, with obsolete rows `1,10,18,19,20,21` allowed to deactivate. Maintain exact projective centering and P/Q inactive slack above `10^-5`; enumerate circuit signatures before metric polishing. A single rail is excluded by the obstruction and by the failed long-rail experiments.

## Reproduction

```bash
unzip wholeblock_continuation_v2.zip
cd wholeblock_continuation_v2/postwall22
python generate_postwall22.py
python verify_postwall22.py
python verify_interval_postwall22_decimal.py
cd ../search && python rebuild_directed_transition_ledger.py
cd .. && python radial_chain_obstruction.py
sha256sum -c SHA256SUMS.txt
```

Archive: wholeblock_continuation_v2.zip  
SHA-256: `d09886ddd9a00ef4698e79588b84f9b2910aa77fe43b208c55c6409869666228`  
Guide: README.md  
Manifest: SEARCH_MANIFEST.json

## Final determination

This continuation reduces the coherent defect from `(2,3,3)` to an exact centroid-hardwired open `(2,1,1)` one-pair body and certifies the topology path that removed one pair. The final pair survives. Therefore no requested Gömböc was constructed.
