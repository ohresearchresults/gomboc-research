"""True contact-graph contractions with direct physical equilibrium repair."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np

from strict110_contact_coarsening import load, proposals
from contact_physical_110 import realize


def run(source, out, rounds, number, steps):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=False)
    spec = importlib.util.spec_from_file_location('direct_contact_peel', 'sources/peer_balanced_contact/make_contact_atlas.py')
    peel = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(peel)
    history = []
    for it in range(rounds):
        source = Path(source)
        a, X, Y = load(source)
        assert a['counts'] == [1, 1, 0] and a['weak'] == [0, 0, 0]
        assert min(a['V'], a['F']) >= 4
        d = out / f'round{it:02d}'
        d.mkdir()
        rows = []
        accepted = None
        for k, p in enumerate(proposals(a, X, Y, number)):
            trial = d / f"case{k:03d}_{p['kind']}"
            trial.mkdir()
            row = {key:p[key] for key in ('kind', 'pair', 'length', 'gain')}
            proposal = dict(V=len(p['X']), F=len(p['Y']), E=p['E'], faces=p['faces'], edges=p['edges'],
                            raw_vertices=p['X'].tolist(), raw_halfspaces=[list(y)+[1.] for y in p['Y']],
                            active=list(range(len(p['Y']))), source=str(source.resolve()),
                            source_audit_sha256=hashlib.sha256((source/'audit.json').read_bytes()).hexdigest(),
                            operation=row, retained_original_vertices=p['active'],
                            scope='prospective contact graph; not asserted to be a convex physical body')
            (trial/'proposal.json').write_text(json.dumps(proposal, indent=2))
            try:
                meta, q, *_ = peel.make(trial/'proposal.json', trial/'peeling', balanced=True)
                for plan in meta['plan']:
                    plan['fixed'] = {}
                grid = 10**16
                meta.update(grid=grid, free_controls=[int(round(z*grid)) for z in q], proposal=str((trial/'proposal.json').resolve()))
                (trial/'construction.json').write_text(json.dumps(meta, indent=2))
                exact = realize(trial/'construction.json', trial/'physical_repair', steps, 1e-9)
                if exact is None:
                    row['result'] = 'finite physical correction failed'
                else:
                    aa = json.loads((exact/'audit.json').read_text())
                    assert aa['E'] < a['E']
                    row.update(result='exact own110 weak000 edge reduction', exact=str(exact.resolve()),
                               V=aa['V'], E=aa['E'], F=aa['F'], counts=aa['counts'], weak=aa['weak'])
                    accepted = row
            except (ValueError, AssertionError, np.linalg.LinAlgError) as err:
                row.update(result='rejected physical construction', error=repr(err))
            rows.append(row)
            (d/'results.json').write_text(json.dumps(rows, indent=2))
            print('DIRECT_COARSEN_CASE', it, k, row, flush=True)
            if accepted is not None:
                break
        if accepted is None:
            print('DIRECT_COARSEN_FINITE_STOP', it, len(rows), flush=True)
            return
        history.append(accepted)
        (out/'history.json').write_text(json.dumps(history, indent=2))
        source = accepted['exact']


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('source')
    p.add_argument('out')
    p.add_argument('--rounds', type=int, default=50)
    p.add_argument('--number', type=int, default=8)
    p.add_argument('--steps', type=int, default=250)
    a = p.parse_args()
    run(a.source, a.out, a.rounds, a.number, a.steps)
