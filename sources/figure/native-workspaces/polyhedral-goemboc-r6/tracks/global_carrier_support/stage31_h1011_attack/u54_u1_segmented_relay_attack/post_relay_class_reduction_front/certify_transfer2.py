#!/usr/bin/env python3
"""Primary exact certificate for ordered transfer epoch 2 (H910/U10 alias wall)."""
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

import front_common as fc


FAR_PARAMETER = Q(27, 1000)
ROOT_WIDTH = Q(1, 10**30)
ALIASES = {"edge:(9, 10):one_minus_t", "vertex:10:9"}
EXPECTED_BEFORE = {
    "class": [2, 3, 3],
    "stable_faces": fc.rc.FAR_FEATURES["stable_faces"],
    "unstable_vertices": [1, 8, 54],
    "saddle_edges": [[1, 54], [5, 6], [10, 11]],
}
EXPECTED_AFTER = {
    "class": [2, 4, 4],
    "stable_faces": fc.rc.FAR_FEATURES["stable_faces"],
    "unstable_vertices": [1, 8, 10, 54],
    "saddle_edges": [[1, 54], [5, 6], [9, 10], [10, 11]],
}


def strict_receipt(rows, excluded, hi):
    digest=hashlib.sha256(); counts={}; leaves=0; worst=None; count=0
    for index,(name,polynomial,family) in enumerate(rows):
        counts[family]=counts.get(family,0)+1
        if name in excluded: continue
        value=polynomial.eval(Q(0)); expected=(value>0)-(value<0)
        sign,row_leaves,margin=fc.rc.ex.bernstein_sign(polynomial,Q(0),hi,max_depth=60)
        if sign!=expected: raise AssertionError(("non-target not strict",name,expected,sign))
        count+=1; leaves+=row_leaves; worst=margin if worst is None else min(worst,margin)
        digest.update(f"{name}|{family}|{sign}|{'|'.join(polynomial.exact())}\n".encode())
        if index and index%1000==0:
            print(json.dumps({"phase":"transfer2_strict_audit","completed":index,"total":len(rows)}),flush=True)
    return {"primitive_count":len(rows),"family_counts":counts,"strict_other_primitive_count":count,
            "strict_other_bernstein_leaf_count":leaves,
            "strict_other_minimum_bernstein_log10_abs":worst,
            "strict_other_primitive_digest":digest.hexdigest()}


def fresh_audit(endpoint,labels,faces):
    sys.path.insert(0,str(fc.TRACK)); from actual_hull_mechanics import evaluate
    points=np.asarray([[float(v) for v in endpoint[label]] for label in labels])
    mechanics=evaluate(labels,points); actual_faces=fc.chart.common.actual_faces(labels,points)
    signature=fc.chart.signature(mechanics)
    checks={"face_ledger_unchanged":fc.rc.face_sets(actual_faces)==fc.rc.face_sets(faces),
            "f_vector_61_162_103":signature["f_vector"]==[61,162,103],
            "active_labels_61":signature["active_labels"]==fc.rc.EXPECTED_ACTIVE,
            "numerical_class_matches_exact":signature["class"]==EXPECTED_AFTER["class"],
            "numerical_stable_faces_match_exact":signature["stable_faces"]==EXPECTED_AFTER["stable_faces"],
            "numerical_unstable_vertices_match_exact":signature["unstable_vertices"]==EXPECTED_AFTER["unstable_vertices"],
            "numerical_saddle_edges_match_exact":signature["saddle_edges"]==EXPECTED_AFTER["saddle_edges"],
            "rails_37":fc.rc.forced_rails().issubset(fc.rc.edge_set(actual_faces))}
    return signature,checks


def exact_transfer_checkpoint(points, faces, expected):
    """Fresh exact checkpoint with H910 required alive after this transfer."""
    support = fc.rc.ex.supporting_cell(points, faces)
    ledger, mechanics = fc.rc.ex.classify_point(points, faces)
    if support["f_vector"] != [61, 162, 103] or support["euler"] != 2:
        raise AssertionError(("f-vector", support))
    if support["active_labels"] != fc.rc.EXPECTED_ACTIVE:
        raise AssertionError(("active labels", support["active_labels"]))
    for key, value in expected.items():
        if mechanics[key] != value:
            raise AssertionError((key, mechanics[key], value))
    if fc.rc.BASE not in {frozenset(face) for face in faces}:
        raise AssertionError("enlarged base absent")
    missing = sorted(fc.rc.forced_rails() - set(support["edges"]))
    if missing:
        raise AssertionError(("forced rails absent", missing))
    constant_path = {
        label: tuple(fc.rc.ex.P((value,)) for value in xyz)
        for label, xyz in points.items()
    }
    turns = fc.rc.base_turn_rows(constant_path, faces)
    if len(turns) != 18 or any(poly.eval(Q(0)) == 0 for _, poly, _ in turns):
        raise AssertionError("base-turn contract")
    d6, m24 = fc.rc.ex.exact_centroid_numerators(points, faces)
    centroid = tuple(value / (4 * d6) for value in m24)
    h910 = ledger["edge"][(9, 10)]
    h910_components = {name: h910[name] for name in ("t", "one_minus_t", "beta1", "beta2")}
    if not all(value > 0 for value in h910_components.values()):
        raise AssertionError(("H910 is not fully alive", h910_components))
    return {
        "coordinate_hash": fc.canonical_hash({
            str(label): [fc.rc.ex.qs(value) for value in points[label]]
            for label in sorted(points)
        }),
        "exact_uniform_volume_centroid": [fc.rc.ex.qs(value) for value in centroid],
        "support": {key: value for key, value in support.items() if key != "edges"},
        "mechanics": mechanics,
        "base_face_present": True, "base_turn_count": 18,
        "forced_rail_count": 37, "missing_forced_rails": [],
        "h910_alive_components": {key: fc.rc.ex.qs(value) for key, value in h910_components.items()},
    }


def main():
    source_path=fc.HERE/"transfer1_far.csv"; source_cert=fc.HERE/"transfer1_certificate.json"
    source_verify=fc.HERE/"transfer1_verification.json"; rechart_path=fc.HERE/"transfer2_rechart_audit.json"
    if json.loads(source_cert.read_text()).get("verdict")!="EXACT_ORDERED_TRANSFER1_D_EPOCH_PASS":
        raise AssertionError("transfer1 primary")
    if json.loads(source_verify.read_text()).get("verdict")!="INDEPENDENT_CLEAN_ROOM_EXACT_ORDERED_TRANSFER1_D_VERIFICATION_PASS":
        raise AssertionError("transfer1 independent")
    if json.loads(rechart_path.read_text()).get("verdict")!="EXACT_TRANSFER2_FRESH_165D_RECHART_H910_FIRST_JET_PASS":
        raise AssertionError("transfer2 rechart")
    source=fc.rc.ex.read_rows(source_path); original=fc.rc.ex.read_rows(fc.SOURCE)
    faces=json.loads(fc.FACES.read_text()); labels=sorted(source)
    velocity={label:tuple((source[label][axis]-original[label][axis])/Q(1,100) for axis in range(3)) for label in labels}
    path=fc.affine_path(source,velocity); endpoint=fc.evaluate_path(path,FAR_PARAMETER)
    endpoint_path=fc.HERE/"transfer2_far.csv"; endpoint_path.write_bytes(fc.rc.exact_csv_bytes(endpoint))
    print(json.dumps({"phase":"transfer2_endpoint_materialized","sha256":fc.sha256(endpoint_path)}),flush=True)
    rows=list(fc.rc.primitive_rows(path,faces))
    if len(rows)!=7922: raise AssertionError(("primitive count",len(rows)))
    lookup={name:poly for name,poly,_ in rows}; target=lookup["edge:(9, 10):one_minus_t"]
    aliases={name for name,poly,_ in rows if poly==target}
    if aliases!=ALIASES: raise AssertionError(("complete zero family",aliases))
    if target.eval(0)>=0 or target.eval(FAR_PARAMETER)<=0: raise AssertionError("target endpoint signs")
    root=fc.rc.ex.isolate_monotone_root(target,Q(0),FAR_PARAMETER,ROOT_WIDTH)
    strict=strict_receipt(rows,aliases,FAR_PARAMETER)
    source_checkpoint=fc.rc.exact_checkpoint(source,faces,EXPECTED_BEFORE)
    endpoint_checkpoint=exact_transfer_checkpoint(endpoint,faces,EXPECTED_AFTER)
    signature,fresh_checks=fresh_audit(endpoint,labels,faces)
    exact_endpoint_ledger, exact_endpoint_signature = fc.rc.ex.classify_point(endpoint, faces)
    if exact_endpoint_signature != EXPECTED_AFTER:
        raise AssertionError(("fresh exact endpoint", exact_endpoint_signature))
    hull_only_checks = {
        key: value for key, value in fresh_checks.items()
        if not key.startswith("numerical_")
    }
    if not all(hull_only_checks.values()):
        raise AssertionError(("fresh numerical hull",hull_only_checks,signature))
    pre=fc.rc.ex.bernstein_sign(target,Q(0),root["lo"],max_depth=60)
    post=fc.rc.ex.bernstein_sign(target,root["hi"],FAR_PARAMETER,max_depth=60)
    if (pre[0],post[0])!=(-1,1): raise AssertionError(("target open signs",pre[0],post[0]))
    row230={"source":fc.rc.row230_values(source,faces),"endpoint":fc.rc.row230_values(endpoint,faces)}
    if any(Q(v)<=0 for packet in row230.values() for v in packet.values()): raise AssertionError("row230")
    d_alias={name:(lookup[name].eval(FAR_PARAMETER)>0)-(lookup[name].eval(FAR_PARAMETER)<0)
             for name in ("edge:(1, 54):one_minus_t","vertex:54:1")}
    if set(d_alias.values())!={1}: raise AssertionError(("D transfer lost",d_alias))
    certificate={
        "version":1,"event":"ordered transfer epoch 2: H910/U10 exact alias wall",
        "source_hashes":{**fc.bindings(),fc.rc.relative(source_path):fc.sha256(source_path),
            fc.rc.relative(source_cert):fc.sha256(source_cert),fc.rc.relative(source_verify):fc.sha256(source_verify),
            fc.rc.relative(rechart_path):fc.sha256(rechart_path),
            fc.rc.relative(fc.HERE/"front_common.py"):fc.sha256(fc.HERE/"front_common.py"),
            fc.rc.relative(Path(__file__)):fc.sha256(Path(__file__))},
        "epoch":{"local_far_parameter":fc.rc.ex.qs(FAR_PARAMETER),
                 "original_far_lambda":fc.rc.ex.qs(Q(1,100)+FAR_PARAMETER)},
        "exact_root":{"complete_zero_family":sorted(aliases),"lo":fc.rc.ex.qs(root["lo"]),
            "hi":fc.rc.ex.qs(root["hi"]),"decimal_interval":[float(root["lo"]),float(root["hi"])],
            "original_lambda_interval":[float(Q(1,100)+root["lo"]),float(Q(1,100)+root["hi"])],
            "value_lo":fc.rc.ex.qs(root["value_lo"]),"value_hi":fc.rc.ex.qs(root["value_hi"]),
            "polynomial_degree":target.degree,"polynomial_exact":target.exact(),
            "polynomial_digest":fc.canonical_hash(target.exact()),
            "derivative_sign":root["derivative_sign"],"simple_root":True,
            "pre_sign":pre[0],"post_sign":post[0],"pre_bernstein_leaf_count":pre[1],
            "post_bernstein_leaf_count":post[1]},
        "exhaustive_strict_other_primitives":strict,
        "open_side_class_contract":{"before":EXPECTED_BEFORE,"after":EXPECTED_AFTER,
                                    "class_transition_delta":[0,1,1]},
        "source_checkpoint":source_checkpoint,"far_checkpoint":endpoint_checkpoint,
        "fresh_exact_signature":exact_endpoint_signature,
        "fresh_numerical_diagnostic":{"signature":signature,"checks":fresh_checks,
            "acceptance_boundary":"floating mechanics is diagnostic only; exact rational mechanics is authoritative"},
        "fresh_hull_checks":hull_only_checks,"row230_squared_margins":row230,
        "D_aliases_remain_positive":d_alias,
        "generated_file_sha256":{fc.rc.relative(endpoint_path):fc.sha256(endpoint_path)},
        "verdict":"EXACT_ORDERED_TRANSFER2_H910_EPOCH_PASS"}
    output=fc.HERE/"transfer2_certificate.json"; output.write_text(json.dumps(certificate,indent=2)+"\n")
    print(json.dumps({"verdict":certificate["verdict"],"root":certificate["exact_root"]["decimal_interval"],
        "strict_other":strict["strict_other_primitive_count"],"class":exact_endpoint_signature["class"],
        "far_sha256":fc.sha256(endpoint_path)},indent=2),flush=True)


if __name__=="__main__": main()
