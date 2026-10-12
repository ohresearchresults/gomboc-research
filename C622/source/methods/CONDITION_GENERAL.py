"""Same full-contact conditioner applied to an explicitly supplied finite parent.
The final floating/rounded state is numerical-only until separately audited.
"""

from CONDITION import *
import sys

sys.path.insert(0, str(ROOT / "parent"))
import RECONSTRUCT


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--generator", type=Path, required=True)
    ap.add_argument("--report", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--stages", type=int, default=20)
    ap.add_argument("--factor", type=float, default=1.6)
    a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=False)
    G = json.load(open(a.generator))
    rep = json.load(open(a.report))
    raw = RECONSTRUCT.recover(G)
    Q = np.array([[float(F(x, row[-1])) for x in row[:3]] for row in raw["H"]])
    s = FlexibleAtlas(G, rep, Q)
    z = np.zeros(s.n)
    v, J, g = s.evaluate(z)
    target = float(v[: s.mechlen - 2].min())
    factor = a.factor
    records = []
    (a.out / "INPUT.json").write_bytes(
        B(
            dict(
                source_G_sha256=hashlib.sha256(B(G)).hexdigest(),
                stages=a.stages,
                factor=a.factor,
                versions=[platform.python_version(), np.__version__, scipy.__version__],
            )
        )
    )
    for stage in range(a.stages):
        nt = target * factor
        s.floor[: s.mechlen - 2] = nt
        zz, ok, h = project(s, z, steps=60)
        records.append(dict(stage=stage, target=nt, success=ok, inner=h))
        (a.out / "RECORDS.json").write_bytes(B(records))
        print("GENERAL_CONDITION", stage, nt, ok, h[-1], flush=True)
        if ok:
            z = zz
            target = nt
        else:
            factor = 1 + (factor - 1) * 0.5
        v, J, g = s.evaluate(z)
        GG = copy.deepcopy(G)
        GG["grid"] = 10**12
        GG["controls"] = np.rint(g["Y"] * GG["grid"]).astype(np.int64).tolist()
        (a.out / "GENERATOR.json").write_bytes(B(GG))
        (a.out / "Z.json").write_bytes(B([float(x).hex() for x in z]))
        if factor < 1.005:
            break
    status = dict(
        target=target, mech=float(v[: s.mechlen - 2].min()), stages=len(records)
    )
    (a.out / "STATUS.json").write_bytes(B(status))
    print("NUMERICAL_GENERAL_CONDITION_DONE", status, flush=True)


if __name__ == "__main__":
    main()
