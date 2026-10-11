"""Numerical global loading-point diagnostic for the unchanged exact C96 hull.

Three loading coordinates and one common distance margin are continuous.
Every face/vertex chooses an escape or is the unique root. This asks whether
the fixed geometry admits any strict reference-centre110 at all, not whether
that point is the body's own homogeneous centroid. MILP answers are numerical.
"""
import argparse
import json
import warnings
from pathlib import Path
from fractions import Fraction

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix

from geometry import ROOT, write_json


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--out',required=True)
    ap.add_argument('--seconds',type=float,default=45.)
    args=ap.parse_args()
    out=Path(args.out)
    out.mkdir(exist_ok=False)
    a=json.loads((ROOT/'work/baseline-check/A.json').read_text())
    p=np.array(a['raw_vertices'],float)/137000
    ns=np.array(a['normals'],float)
    ns/=np.linalg.norm(ns,axis=1)[:,None]
    h=np.array(a['offsets'],float)/np.linalg.norm(np.array(a['normals'],float),axis=1)/137000
    adjacency=[[] for _ in p]
    for i,j in a['edges']:
        adjacency[i].append(j)
        adjacency[j].append(i)
    features=[]
    for i,js in enumerate(adjacency):
        e=p[js]-p[i]
        normals=e/np.linalg.norm(e,axis=1)[:,None]
        features.append(dict(kind='U',index=i,sign=1.,normals=normals,offsets=normals@p[i]))
    for i,cycle in enumerate(a['faces']):
        ps=p[cycle]
        edges=np.roll(ps,-1,axis=0)-ps
        normals=np.cross(edges,ns[i])
        normals/=np.linalg.norm(normals,axis=1)[:,None]
        features.append(dict(kind='S',index=i,sign=-1.,normals=normals,
                             offsets=np.einsum('ij,ij->i',normals,ps)))
    pos=4
    for f in features:
        f['root']=pos
        pos+=1
        f['witness']=list(range(pos,pos+len(f['offsets'])))
        pos+=len(f['offsets'])
    rows=[]
    lows=[]
    ups=[]
    M=5.

    def add(row,low=-np.inf,up=np.inf):
        rows.append(row);lows.append(low);ups.append(up)

    for n,d in zip(ns,h):
        add({0:-n[0],1:-n[1],2:-n[2],3:-1.},-d)
    for kind in ['U','S']:
        add({f['root']:1. for f in features if f['kind']==kind},1.,1.)
    for f in features:
        add({f['root']:1.,**{i:1. for i in f['witness']}},1.)
        s=f['sign']
        for n,b,w in zip(f['normals'],f['offsets'],f['witness']):
            add({0:-s*n[0],1:-s*n[1],2:-s*n[2],3:-1.,w:-M},-s*b-M)
            # A selected root must satisfy all opposite strict inequalities.
            add({0:s*n[0],1:s*n[1],2:s*n[2],3:-1.,f['root']:-M},s*b-M)
    matrix=lil_matrix((len(rows),pos))
    for i,row in enumerate(rows):
        for j,value in row.items():
            matrix[i,j]=value
    lb=np.r_[p.min(axis=0),0.,np.zeros(pos-4)]
    ub=np.r_[p.max(axis=0),.1,np.ones(pos-4)]
    objective=np.zeros(pos);objective[3]=-1.
    integrality=np.r_[np.zeros(4),np.ones(pos-4)]
    r=milp(objective,integrality=integrality,bounds=Bounds(lb,ub),
           constraints=LinearConstraint(matrix.tocsc(),lows,ups),
           options={'time_limit':args.seconds,'mip_rel_gap':1e-8,'threads':1})
    report=dict(status=int(r.status),message=str(r.message),variables=pos,
                constraints=len(rows),seconds_limit=args.seconds,
                interpretation='Floating MILP diagnostic only; no exact global exclusion.')
    for key in ['mip_gap','mip_node_count','mip_dual_bound','fun']:
        if getattr(r,key,None) is not None:
            report[key]=float(getattr(r,key))
    if r.x is not None:
        c=r.x[:3]
        report.update(centre=c.tolist(),common_margin=float(r.x[3]),roots=[],
                      counts={kind:0 for kind in ['S','U']},root_signs={})
        for f in features:
            vals=f['offsets']-f['normals']@c
            root_test=bool(max(vals)<-1e-9) if f['kind']=='U' else bool(min(vals)>1e-9)
            report['counts'][f['kind']]+=int(root_test)
            if r.x[f['root']]>.5:
                report['roots'].append([f['kind'],f['index']])
                report['root_signs'][f['kind']]=vals.tolist()
        report['own_centroid']=[float(Fraction(x))/137000 for x in a['raw_centroid']]
    write_json(out/'REPORT.json',report)
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
