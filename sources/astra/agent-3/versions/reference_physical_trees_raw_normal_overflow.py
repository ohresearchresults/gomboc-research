"""Reference-centre cells from physical face and vertex escape trees.

The fixed body is unchanged. A successful reference cell is NOT an own-centroid
body. Exact reference census is recorded separately from the actual mass centre.
"""
import argparse
import json
from pathlib import Path

import numpy as np
from gmpy2 import mpq
from scipy.optimize import linprog

from sources.N40.N40_RECOVER import census


def widest(weights, neighbours, root):
    N = len(weights)
    cap = np.full(N, -np.inf)
    cap[root] = np.inf
    done = np.zeros(N, bool)
    selected = np.full(N, -1, int)
    for _ in range(N):
        j = int(np.argmax(np.where(done, -np.inf, cap)))
        if done[j] or not np.isfinite(cap[j]) and j != root:
            raise ValueError('disconnected escape graph')
        done[j] = True
        for i in range(N):
            if done[i]:
                continue
            for k, v in enumerate(neighbours[i]):
                if v == j:
                    value = min(cap[j], weights[i][k])
                    if value > cap[i]:
                        cap[i], selected[i] = value, k
    return selected


def run(source, out, trials):
    source, out = Path(source), Path(out)
    out.mkdir(parents=True, exist_ok=False)
    a = json.loads(source.read_text())
    Xq = [tuple(map(mpq, x)) for x in a['raw_vertices']]
    X = np.array(Xq, float)
    cq = tuple(map(mpq, a['raw_centroid']))
    c = np.array(cq, float)
    Z = X-c
    R = np.sqrt(np.mean(np.sum(Z*Z, axis=1)))
    normals = np.array([[float(mpq(v)) for v in row] for row in a['normals']])
    offsets = np.array([float(mpq(v)) for v in a['offsets']])
    nl = np.linalg.norm(normals, axis=1)
    normals, offsets = normals/nl[:,None], offsets/nl
    owners = {tuple(e):[] for e in a['edges']}
    vn = [set() for _ in X]
    for i,j in a['edges']:
        vn[i].add(j);vn[j].add(i)
    for f,cy in enumerate(a['faces']):
        for i,j in zip(cy,cy[1:]+cy[:1]):
            owners[tuple(sorted((i,j)))].append(f)
    vN=[sorted(v) for v in vn]
    VM=[];VB=[]
    for i,ns in enumerate(vN):
        e=X[ns]-X[i];M=e/np.linalg.norm(e,axis=1)[:,None];VM.append(M);VB.append(M@Z[i])
    FN=[];FM=[];FB=[]
    for f,cy in enumerate(a['faces']):
        js=np.roll(cy,-1);e=X[js]-X[cy];M=np.cross(normals[f],e)/np.linalg.norm(e,axis=1)[:,None]
        FM.append(M);FB.append(np.einsum('ic,ic->i',M,Z[cy]));FN.append([next(k for k in owners[tuple(sorted((i,j)))] if k!=f)for i,j in zip(cy,js)])
    roots=[int(np.argmax(np.sum(Z*Z,axis=1))),int(np.argmin(offsets-normals@c))]
    groups=[(VM,VB,vN,roots[0]),(FM,FB,FN,roots[1])]
    rng=np.random.default_rng(773208)
    eps=R*1e-10
    records=[];best=None
    for trial in range(trials):
        AA=[];bb=[];choices=[]
        for M,B,N,root in groups:
            if trial==0:
                chosen=np.array([np.argmax(b)for b in B])
            else:
                sigma=[0.,1e-9,1e-7,1e-5,1e-3,.03][(trial-1)%6]*R
                weights=[b+rng.normal(size=len(b))*sigma for b in B]
                chosen=widest(weights,N,root)
            choices.append(chosen.tolist())
            for i in range(len(M)):
                if i==root:
                    AA.extend(-M[i]);bb.extend(-B[i]-eps)
                else:
                    AA.append(M[i][chosen[i]]);bb.append(B[i][chosen[i]]-eps)
        AA.extend(normals);bb.extend(offsets-normals@c-eps)
        A=np.zeros((len(AA)+6,4));A[:len(AA),:3]=AA;b=np.r_[bb,np.zeros(6)]
        for j in range(3):
            A[len(AA)+2*j,j]=1;A[len(AA)+2*j,3]=-1
            A[len(AA)+2*j+1,j]=-1;A[len(AA)+2*j+1,3]=-1
        sol=linprog([0,0,0,1],A_ub=A,b_ub=b,bounds=[(None,None)]*3+[(0,None)],method='highs',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-10))
        row=dict(trial=trial,status=int(sol.status),message=sol.message)
        if sol.success:
            delta=sol.x[:3];minimum=float(min(np.array(bb)-np.array(AA)@delta));row.update(linf=float(sol.x[3]),distance=float(np.linalg.norm(delta)),minimum_slack=minimum,delta=delta.tolist(),witnesses=choices)
            if best is None or row['distance']<best['distance']:
                best=row
        records.append(row)
    (out/'trials.json').write_text(json.dumps(records,indent=2))
    report=dict(source=str(source.resolve()),own_census=a['counts'],own_center=a['raw_centroid'],fixed_roots=roots,epsilon=eps,successful_LPs=sum(r['status']==0 for r in records),scope='finite reference-point cell search; body and its actual volume centroid remain unchanged')
    if best is not None:
        rc=tuple(cq[j]+mpq(float(best['delta'][j]))for j in range(3))
        K=dict(points=Xq,faces=a['faces'],edges=a['edges'],edge_faces=list(owners.values()))
        ce=census(K,rc)
        report.update(best=best,reference_center=list(map(str,rc)),reference_census=ce)
        np.save(out/'reference_center.npy',np.array(rc,float))
    (out/'result.json').write_text(json.dumps(report,indent=2))
    print('PHYSICAL_REFERENCE_CELLS',dict(successful_LPs=report['successful_LPs'],distance=None if best is None else best['distance'],reference_census=None if best is None else ce),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--trials',type=int,default=80);a=p.parse_args();run(a.source,a.out,a.trials)
