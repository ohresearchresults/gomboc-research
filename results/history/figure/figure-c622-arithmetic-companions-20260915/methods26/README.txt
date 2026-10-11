C622 arithmetic experiments, all numerical except separately audited G10.
Dependencies: complete canonical C622 FULL76 source and its cold proof.
Python3.13.5, NumPy2.3.5, SciPy1.17.0; OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1.
Reproduce the 13-grid screen:
python -B COARSEN_SCREEN.py FULL76_SOURCE C622_FULL_PROOF NEW_SCREEN
First integer proposal attempt:
python -B INTEGER_SNAP.py FULL76_SOURCE C622_FULL_PROOF NEW_MIP_A --grid 1000000000 --radius 2 --goal 5e-9 --iterations 4 --seconds 60
Second integer proposal attempt:
python -B INTEGER_SNAP_FEAS.py FULL76_SOURCE C622_FULL_PROOF NEW_MIP_B --grid 1000000000 --radius 3 --goal 1e-9 --iterations 4 --seconds 60 --feasibility
Both observed INTEGER_SNAP_NO_INCUMBENT after status1/time cutoff. A timing cutoff is not a deterministic mathematical exclusion and not guaranteed to recur on another machine.
Conditioning experiment, unmodified complete SVD_REPAIR.py and dependencies in FULL76:
python -B FULL76_SOURCE/methods/SVD_REPAIR.py --generator C622_FULL_PROOF/C622_ROUTED/GENERATOR.json --out NEW_CONDITION --goal 1e-6 --steps 40 --tree
The final conditioned generator and selected rooted witnesses are stored literally here, but this proposal is not a certified own110 or a certified nonwinner: its minimum selected numerical witness is negative. Source check_B at the start classified the input, not this final proposal.
The stable/candidate numerical screen uses inherited incidence; exact incidence and equilibrium checks were separately completed only for grid1e10.
COORD_C622_GRID10_OWN110 is recovered and fully certified by the separate canonical RECOVER_G10.py capsule.
