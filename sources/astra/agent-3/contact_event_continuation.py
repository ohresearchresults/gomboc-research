"""Full physical contact optimization interleaved with exact hull events.

Each new stage uses the actual maximal-face incidence from a complete exact
hull audit. The combinatorics of an invalid intermediate chart are discarded.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

from contact_physical_110 import realize
from exact_contact_rehull import run as rehull


def make_chart(source, out):
    source, out = Path(source), Path(out)
    out.mkdir(parents=True, exist_ok=False)
    a = json.loads((source/'audit.json').read_text())
    proposal = dict(a)
    proposal['raw_halfspaces'] = [list(n)+[h] for n, h in zip(a['normals'], a['offsets'])]
    proposal['active'] = list(range(a['F']))
    proposal['source'] = str(source.resolve())
    proposal['source_audit_sha256'] = hashlib.sha256((source/'audit.json').read_bytes()).hexdigest()
    (out/'proposal.json').write_text(json.dumps(proposal, indent=2))
    spec = importlib.util.spec_from_file_location('contact_event_peel', 'sources/peer_balanced_contact/make_contact_atlas.py')
    peel = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(peel)
    meta, q, *_ = peel.make(out/'proposal.json', out/'peeling', balanced=True)
    for p in meta['plan']:
        p['fixed'] = {}
    grid = max(float(v).as_integer_ratio()[1] for v in q)
    meta.update(grid=grid, free_controls=[int(round(float(v)*grid)) for v in q],
                scope='new exact contact chart seeded by binary64 images of an exact hull; source equality is not presumed')
    (out/'construction.json').write_text(json.dumps(meta, indent=2))
    return out/'construction.json'


def run(source, out, cycles, steps, angular):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=False)
    history = []
    for it in range(cycles):
        d = out/f'cycle{it:02d}'
        d.mkdir()
        chart = make_chart(source, d/'chart')
        exact = realize(chart, d/'repair', steps, 1e-9, angular_vertices=angular)
        if exact is not None:
            row = dict(cycle=it, result='exact own110 above goal complexity', exact=str(exact.resolve()))
            history.append(row)
            (out/'history.json').write_text(json.dumps(history, indent=2))
            return
        a = rehull(chart, d/'repair/endpoint_q.npy', d/'exact_hull')
        row = {k:a[k] for k in ['V', 'E', 'F', 'counts', 'weak']}
        row.update(cycle=it, exact=str((d/'exact_hull').resolve()), source=str(Path(source).resolve()))
        history.append(row)
        (out/'history.json').write_text(json.dumps(history, indent=2))
        print('EXACT_CONTACT_EVENT_STAGE', row, flush=True)
        source = d/'exact_hull'


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('source')
    p.add_argument('out')
    p.add_argument('--cycles', type=int, default=8)
    p.add_argument('--steps', type=int, default=180)
    p.add_argument('--angular-vertices', action='store_true')
    a = p.parse_args()
    run(a.source, a.out, a.cycles, a.steps, a.angular_vertices)
