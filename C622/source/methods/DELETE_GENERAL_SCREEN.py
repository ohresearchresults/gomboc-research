"""Finite actual-hull support-deletion screen; no tolerance result is acceptance."""

import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
import argparse, json, sys, hashlib
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from numeric import Chart

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "parent"))
import RECONSTRUCT, check_A, check_B, centred_mass

B = lambda x: json.dumps(x, sort_keys=True, separators=(",", ":")).encode()
ap = argparse.ArgumentParser()
ap.add_argument("--generator", type=Path, required=True)
ap.add_argument("--out", type=Path, required=True)
a = ap.parse_args()
a.out.mkdir(parents=True, exist_ok=False)
G = json.loads(a.generator.read_text())
(a.out / "SOURCE_GENERATOR.json").write_bytes(B(G))
raw = RECONSTRUCT.recover(G)
Q = np.array([[float(F(x, row[-1])) for x in row[:3]] for row in raw["H"]])
records = []
c = object.__new__(Chart)
for f in range(len(Q)):
    if f == 3:
        continue
    try:
        r = c.actual(np.delete(Q, f, axis=0), tol=1e-10)
        r.pop("Q")
        r["deleted_input"] = f
        records.append(r)
        if r["counts"] == [1, 1, 0] and 2 * r["E"] < 624:
            out = a.out / str(f)
            out.mkdir()
            rr = {"H": raw["H"][:f] + raw["H"][f + 1 :]}
            (out / "raw.json").write_bytes(B(rr))
            A = check_A.run(rr)
            BB = check_B.run(rr)
            assert A == BB
            for n, x in [("A", A), ("B", BB), ("MASS", centred_mass.run(A))]:
                (out / (n + ".json")).write_bytes(B(x))
            print(
                "EXACT_DELETION",
                f,
                A["V"],
                A["E"],
                A["F"],
                A["counts"],
                A["weak"],
                flush=True,
            )
        print(
            "DELETE_GENERAL_NUMERICAL",
            f,
            r["V"],
            r["E"],
            r["F"],
            r["counts"],
            flush=True,
        )
    except (ValueError, AssertionError, ZeroDivisionError) as e:
        records.append(dict(deleted_input=f, error=str(e)))
    (a.out / "RESULTS.json").write_bytes(B(records))
print("FINITE_DELETION_SCREEN_COMPLETE", len(records), flush=True)
