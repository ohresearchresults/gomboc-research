"""Complete source-only exact replay: physical hull, all equilibria and weak cases.
No cached geometry is an input. NumPy/SciPy are NOT needed for this certificate.
"""

import argparse, copy, hashlib, json, shutil, sys
from pathlib import Path
from fractions import Fraction as F

sys.set_int_max_str_digits(0)
if not __debug__:
    raise RuntimeError("Assertions must be enabled")
ROOT = Path(__file__).resolve().parent
sys.path[:0] = [str(ROOT / "methods"), str(ROOT / "methods/parent")]
import G_FREE_CODEC, RECONSTRUCT, check_A, check_B, centred_mass, VERIFY_EXTRA, ESCAPE_CERT, AUDIT, chart, VERIFY_WINNER

B = lambda x: json.dumps(x, sort_keys=True, separators=(",", ":")).encode()
H = lambda x: hashlib.sha256(x).hexdigest()


def put(path, x):
    b = B(x)
    path.write_bytes(b)
    return H(b)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    out = a.out.resolve()
    out.mkdir(parents=True, exist_ok=False)
    expected = json.loads((ROOT / "EXPECTED.json").read_text())
    if (ROOT / "MANIFEST.json").exists():
        for name, h in json.loads((ROOT / "MANIFEST.json").read_text()).items():
            assert H((ROOT / name).read_bytes()) == h, name
    results = {}
    reports = {}
    raws = {}
    gens = {}
    for name, want in expected["cases"].items():
        folder = out / name
        folder.mkdir()
        G = G_FREE_CODEC.decode(
            json.loads((ROOT / "inputs" / (name + ".json")).read_text())
        )
        assert H(B(G)) == want["generator_sha256"]
        put(folder / "GENERATOR.json", G)
        raw = RECONSTRUCT.recover(G)
        put(folder / "raw.json", raw)
        pair = []
        for label, fun in [("A", check_A.run), ("B", check_B.run)]:
            print("START", name, label, flush=True)
            rep = fun(raw)
            h = put(folder / (label + ".json"), rep)
            assert h == want["report_sha256"]
            assert len(B(rep)) == want["report_bytes"]
            print(
                "COMPLETE",
                name,
                label,
                rep["V"],
                rep["E"],
                rep["F"],
                rep["counts"],
                rep["weak"],
                h,
                flush=True,
            )
            pair.append(rep)
        rep, rr = pair
        assert rep == rr
        assert [rep[k] for k in ["V", "E", "F"]] == want["VEF"]
        assert rep["counts"] == want["counts"] and rep["weak"] == want["weak"] == [
            0,
            0,
            0,
        ]
        for key in [
            "face_primitive_zero_count",
            "vertex_max_zero_count",
            "edge_primitive_zero_count",
        ]:
            assert rep[key] == 0
        assert rep["edge_primitive_count"] == 4 * rep["E"]
        mass = centred_mass.run(rep)
        put(folder / "CENTRED_MASS.json", mass)
        g = list(map(F, rep["raw_centroid"]))
        X = [list(map(F, row)) for row in rep["raw_vertices"]]
        z = [[v - c for v, c in zip(row, g)] for row in X]
        bits = {
            k: AUDIT.bits(v)
            for k, v in dict(
                H=raw["H"],
                raw=X,
                volume=rep["ordinary_volume"],
                moment=rep["raw_first_moments"],
                centroid=g,
                centred=z,
            ).items()
        }
        put(folder / "BITS.json", bits)
        if name != "C620_121_NONWINNER":
            atlas = VERIFY_EXTRA.atlas(G, raw, rep)
            put(folder / "ATLAS.json", atlas)
            atlas_summary = {k: v for k, v in atlas.items() if k != "free_indices"}
        else:
            assert rep["active_input_indices"] == [i for i in range(137) if i != 114]
            atlas_summary = {
                "status": "Finite input contacts reconstructed; ghost contact is not claimed as a maximal physical vertex",
                "inactive_input_support": 114,
            }
        if name in expected["escape_hashes"]:
            floor = {
                "CONDITIONED_C626": F(1, 125000),
                "CONDITIONED_C624": F(6, 1000000),
                "C622_ROUTED": F(1, 100000000),
            }.get(name, F(1, 10000000))
            up = F(9, 20000000) if name == "PARENT" else None
            esc = ESCAPE_CERT.run(raw, rep, floor, up)
            h = put(folder / "ESCAPE.json", esc)
            assert h == expected["escape_hashes"][name]
        rec = dict(
            generator_sha256=H(B(G)),
            raw_sha256=H(B(raw)),
            report_sha256=H(B(rep)),
            V=rep["V"],
            E=rep["E"],
            F=rep["F"],
            C=2 * rep["E"],
            strict=rep["counts"],
            weak=rep["weak"],
            bits=bits,
            mass=mass,
            atlas=atlas_summary,
        )
        put(folder / "RECEIPT.json", rec)
        results[name] = rec
        reports[name] = rep
        raws[name] = raw
        gens[name] = G
    # The reconditioned same-incidence body and exact >160/9 improvement in the defined minimum escape margin.
    assert (
        VERIFY_EXTRA.owners(reports["PARENT"]).keys()
        == VERIFY_EXTRA.owners(reports["CONDITIONED_C626"]).keys()
    )
    base = out / "baseline"
    base.mkdir()
    for n in ["raw.json", "A.json", "B.json"]:
        shutil.copyfile(out / "PARENT" / n, base / n)
    extra = VERIFY_EXTRA.verify(out, out / "C624_NONSIMPLE", out / "C624_EXTRA")
    winner_extra = VERIFY_WINNER.verify(out, out / "C622_ROUTED", out / "C622_EXTRA")
    assert (
        VERIFY_EXTRA.owners(reports["CONDITIONED_C624"]).keys()
        == VERIFY_EXTRA.owners(reports["C624_NONSIMPLE"]).keys()
    )
    for case in ["C624_NONSIMPLE", "C622_ROUTED"]:
        cr = out / (case + "_CHART")
        cb = cr / "baseline"
        cb.mkdir(parents=True)
        for n in ["raw.json", "A.json", "B.json"]:
            shutil.copyfile(out / case / n, cb / n)
        chartdata = chart.recover(root=cr)
        put(cr / "chart_exact.json", check_A.encode(chartdata))
    # Maximal-chart output is available to continuation; refinements are not true edges.
    seed = chart.recover(root=out)
    put(out / "chart_exact.json", check_A.encode(seed))
    controls = []
    for HH, c, w in [
        (
            [[-1, -1, -1, 1], [-1, 1, 1, 1], [1, -1, 1, 1], [1, 1, -1, 1]],
            [4, 4, 6],
            [0, 0, 0],
        ),
        (
            [[1, 0, 0, 1], [-2, 3, 0, 1], [1, -3, 0, 1], [0, 0, 1, 1], [0, 0, -1, 1]],
            [4, 4, 6],
            [1, 2, 3],
        ),
    ]:
        aa = check_A.run({"H": HH})
        bb = check_B.run({"H": HH})
        assert aa == bb and aa["counts"] == c and aa["weak"] == w
        controls.append(dict(strict=c, weak=w))
    for HH in (
        [[1, 0, 0, -1]] * 4,
        [[1, 0, 0, 1]] * 4,
        [[1, 0, 0, 1], [-1, 0, 0, 1], [0, 1, 0, 1], [0, -1, 0, 1]],
    ):
        for fun in [check_A.run, check_B.run]:
            try:
                fun({"H": HH})
            except (AssertionError, ValueError):
                pass
            else:
                raise AssertionError("Malformed/unbounded fixture accepted")
    put(out / "CONTROLS.json", controls)
    receipt = dict(
        status=expected["terminal"],
        cases=results,
        conditioned_margin_strict_improvement_factor="160/9",
        nonsimple_successor_extra=extra,
        winner_extra=winner_extra,
        invalid_and_weak_fixtures_pass=True,
        new_record_below_624=True,
    )
    put(out / "RECEIPT.json", receipt)
    print(expected["terminal"], H(B(receipt)), flush=True)


if __name__ == "__main__":
    main()
