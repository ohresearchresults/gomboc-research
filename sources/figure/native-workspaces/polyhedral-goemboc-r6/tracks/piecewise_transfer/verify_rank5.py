#!/usr/bin/env python3
"""Regenerate and verify the exact rank-five shell artifacts."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def run(name):
    subprocess.run([sys.executable, str(HERE / name)], check=True)


def main():
    run("rank5_exact_reconstruction.py")
    run("rank5_exact_jacobian.py")
    r = json.loads((HERE / "rank5_reconstruction.json").read_text())
    j = json.loads((HERE / "rank5_exact_jacobian.json").read_text())
    assert r["verdict"] == "EXACT_RECONSTRUCTED_RANK5_SHELL_SEED_IS_STRICT_345"
    assert r["f_vector"] == [61, 150, 91]
    assert r["class"] == [3, 4, 5]
    assert r["unstable_vertices"] == [8, 228, 231, 246]
    assert sorted(map(tuple, r["saddle_edges"])) == sorted(
        [(8, 246), (228, 254), (228, 255), (231, 247), (236, 237)]
    )
    assert j["ranks"] == {
        "five_selected_cancellation_gradients": 5,
        "six_selected_cancellation_gradients": 5,
        "six_selected_augmented_value_gradient_rows": 6,
    }
    f = j["exact_affine_farkas_certificate"]
    assert f["lambda_times_gradient_exact"] == ["0/1"] * 5
    assert f["lambda_times_wall_values_sign"] != 0
    g = j["trust_box_10_inequality_farkas_certificate"]
    assert all(z > 0 for z in g["primitive_positive_integer_multipliers"])
    assert g["lambda_times_A_exact"] == ["0/1"] * 5
    assert g["lambda_times_b_sign"] == -1
    print("ALL_EXACT_RANK5_SHELL_AND_FARKAS_VERIFIERS_PASS")


if __name__ == "__main__":
    main()
