"""Define a new rational contact body in a shallower exact construction chart.

The source rational controls are evaluated at high precision. Target free
controls are rounded once to an explicitly saved rational grid. Those target
controls define a NEW exact body, which must undergo its own complete rational
audit. Agreement with the numerical source is not a proof of its census.
"""
import argparse,json,pathlib,hashlib
import numpy as np
import mpmath as mp

def reconstruct(meta,integers,D,dps):
    mp.mp.dps=dps;q=[mp.mpf(i)/D for i in integers];A=[None]*meta['nodes']
    for p in meta['plan']:
        i=p['node'];deps=p['deps'];axes=p['axes'];v=[mp.mpf(0)]*3
        for k,j in zip(p['free_axes'],p['free_indices']):v[k]=q[j]
        if deps:
            mat=mp.matrix([[A[j][k] for k in axes] for j in deps]);rhs=mp.matrix([1-sum(A[j][k]*v[k] for k in range(3)) for j in deps]);sol=mp.lu_solve(mat,rhs)
            for k,x in zip(axes,sol):v[k]=x
        A[i]=v
    return A

def run(source,input,target,out,source_grid=10**15,target_grid=10**50):
    source=pathlib.Path(source);input=pathlib.Path(input);target=pathlib.Path(target);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);sm=json.loads((source/'chart.json').read_text());tm=json.loads((target/'chart.json').read_text());assert sm['faces']==tm['faces'] and sm['nodes']==tm['nodes']
    d=np.load(input);z=d['z'] if 'z' in d else d['q'];ints=[int(round(float(x)*source_grid)) for x in z]
    A80=reconstruct(sm,ints,source_grid,80);A120=reconstruct(sm,ints,source_grid,120);difference=max(abs(a-b) for va,vb in zip(A80,A120) for a,b in zip(va,vb))
    if difference>mp.mpf('1e-60'):raise ValueError('high precision source reconstruction did not stabilize')
    free=[None]*tm['free_coordinates']
    for p in tm['plan']:
        for k,j in zip(p['free_axes'],p['free_indices']):free[j]=int(mp.nint(A120[p['node']][k]*target_grid))
    (out/'target_controls.json').write_text(json.dumps(dict(grid=target_grid,integers=free),separators=(',',':')))
    (out/'source_controls.json').write_text(json.dumps(dict(grid=source_grid,integers=ints),separators=(',',':')))
    receipt=dict(scope='New rational target controls; complete exact target-body audit required',source_chart=str(source.resolve()),target_chart=str(target.resolve()),numerical_source=str(input.resolve()),source_depth=sm['max_depth'],target_depth=tm['max_depth'],precision_dps=[80,120],maximum_reconstruction_difference=mp.nstr(difference,12),source_grid=source_grid,target_grid=target_grid,source_sha256=hashlib.sha256(input.read_bytes()).hexdigest(),source_chart_sha256=hashlib.sha256((source/'chart.json').read_bytes()).hexdigest(),target_chart_sha256=hashlib.sha256((target/'chart.json').read_bytes()).hexdigest())
    (out/'receipt.json').write_text(json.dumps(receipt,indent=2));print('RECHARTED_NEW_RATIONAL_CONTROLS',receipt,flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--source',required=True);ap.add_argument('--input',required=True);ap.add_argument('--target',required=True);ap.add_argument('--out',required=True);a=ap.parse_args();run(a.source,a.input,a.target,a.out)
