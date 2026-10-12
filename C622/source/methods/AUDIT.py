"""Full finite rational audits, third mass integration, arithmetic and incidence record."""

import argparse, json, sys, hashlib, time
from pathlib import Path
from fractions import Fraction as F

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "parent"))
import RECONSTRUCT, check_A, check_B, centred_mass

B = lambda x: json.dumps(x, sort_keys=True, separators=(",", ":")).encode()
H = lambda x: hashlib.sha256(x).hexdigest()


def bits(x):
    z = []

    def rec(x):
        if isinstance(x, (list, tuple)):
            for y in x:
                rec(y)
        else:
            z.append(F(x))

    rec(x)
    return [
        max(abs(t.numerator).bit_length() for t in z),
        max(t.denominator.bit_length() for t in z),
    ]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("generator", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--expect", type=int, nargs=3)
    a = ap.parse_args()
    out = a.out
    out.mkdir(parents=True, exist_ok=False)
    G = json.load(open(a.generator))
    raw = RECONSTRUCT.recover(G)
    (out / "GENERATOR.json").write_bytes(B(G))
    (out / "raw.json").write_bytes(B(raw))
    t = time.time()
    A = check_A.run(raw)
    (out / "A.json").write_bytes(B(A))
    print("COMPLETED_A", A["V"], A["E"], A["F"], A["counts"], A["weak"], flush=True)
    C = check_B.run(raw)
    (out / "B.json").write_bytes(B(C))
    print("COMPLETED_B", C["V"], C["E"], C["F"], C["counts"], C["weak"], flush=True)
    assert B(A) == B(C)
    mass = centred_mass.run(A)
    (out / "MASS.json").write_bytes(B(mass))
    print("THIRD_MASS", mass, flush=True)
    g = list(map(F, A["raw_centroid"]))
    X = [list(map(F, row)) for row in A["raw_vertices"]]
    centred = [[v - c for v, c in zip(row, g)] for row in X]
    owners = [
        [A["active_input_indices"][f] for f, cy in enumerate(A["faces"]) if v in cy]
        for v in range(A["V"])
    ]
    (out / "OWNERS.json").write_bytes(B(owners))
    s = dict(
        status=(
            "COMPLETED_TWO_EXACT_AUDITS_OWN110"
            if A["counts"] == [1, 1, 0] and A["weak"] == [0, 0, 0]
            else "COMPLETED_TWO_EXACT_AUDITS_NONWINNER"
        ),
        V=A["V"],
        E=A["E"],
        F=A["F"],
        C=2 * A["E"],
        counts=A["counts"],
        weak=A["weak"],
        generator_bytes=len(B(G)),
        generator_sha256=H(B(G)),
        raw_bytes=len(B(raw)),
        raw_sha256=H(B(raw)),
        report_bytes=len(B(A)),
        report_sha256=H(B(A)),
        volume_float=float(F(A["ordinary_volume"])),
        centroid_float=list(map(float, g)),
        moment_float=[float(F(v)) for v in A["raw_first_moments"]],
        bits=dict(
            H=bits(raw["H"]),
            raw=bits(X),
            volume=bits(A["ordinary_volume"]),
            moment=bits(A["raw_first_moments"]),
            centroid=bits(g),
            centred=bits(centred),
        ),
        mass=mass,
        seconds=time.time() - t,
    )
    (out / "RECEIPT.json").write_bytes(B(s))
    print(json.dumps(s), flush=True)
    if a.expect is not None:
        assert A["counts"] == a.expect and A["weak"] == [0, 0, 0]


if __name__ == "__main__":
    main()
