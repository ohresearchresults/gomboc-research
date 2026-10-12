"""Construct prospective <=246-edge contact graphs before equilibrium search.

The source strict110 body only seeds the shape. Multiple genuine topological
edge removals are performed before a single physical realization search.
Numerical success is immediately subjected to the complete exact audit.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np

from strict110_contact_coarsening import load,proposals
from contact_numpy import Chart
from contact_physical_110 import PhysicalGuards,realize


def three_connected(n,edges):
    """For each deleted vertex, require the remainder to be biconnected."""
    if n<4:return False
    adj=[set()for _ in range(n)]
    for i,j in edges:adj[i].add(j);adj[j].add(i)
    if min(map(len,adj))<3:return False
    for removed in range(n):
        disc=[-1]*n;low=[-1]*n;parent=[-1]*n;clock=0;articulation=False
        def visit(u):
            nonlocal clock,articulation
            disc[u]=low[u]=clock;clock+=1;children=0
            for v in adj[u]:
                if v==removed:continue
                if disc[v]<0:
                    parent[v]=u;children+=1;visit(v);low[u]=min(low[u],low[v])
                    if parent[u]>=0 and low[v]>=disc[u]:articulation=True
                elif v!=parent[u]:low[u]=min(low[u],disc[v])
            if parent[u]<0 and children>1:articulation=True
        visit(0 if removed!=0 else 1)
        if articulation or clock!=n-1:return False
    return True


def run(source,out,seeds,steps):
    source,out=Path(source),Path(out);out.mkdir(parents=True,exist_ok=False)
    initial,X0,Y0=load(source);assert initial['counts']==[1,1,0]and initial['weak']==[0,0,0]
    spec=importlib.util.spec_from_file_location('bulk_bound_peel','sources/peer_balanced_contact/make_contact_atlas.py');peel=importlib.util.module_from_spec(spec);spec.loader.exec_module(peel)
    records=[]
    for seed in range(seeds):
        d=out/f'seed{seed:02d}';d.mkdir();rng=np.random.default_rng(926001+seed)
        a=dict(initial);X,Y=X0.copy(),Y0.copy();history=[]
        while a['E']>246:
            opts=proposals(a,X,Y,12)
            if seed%3==1:opts=[p for p in opts if p['kind']=='facet_union']
            if seed%3==2:opts=[p for p in opts if p['kind']=='vertex_union']
            if not opts:raise ValueError('no topological contraction candidate')
            sigma=0. if seed<3 else .5
            costs=np.array([p['length']/max(1,p['gain'])for p in opts])*np.exp(rng.normal(size=len(opts))*sigma)
            chosen=None
            for j in np.argsort(costs):
                p=opts[int(j)]
                if three_connected(len(p['X']),p['edges']):
                    chosen=p;break
            if chosen is None:raise ValueError('none of the finite contractions preserved a 3-connected graph')
            p=chosen;history.append({k:p[k]for k in ['kind','pair','length','gain','E']});X,Y=p['X'],p['Y'];a=dict(V=len(X),F=len(Y),E=p['E'],faces=p['faces'],edges=p['edges'])
        proposal=dict(a,raw_vertices=X.tolist(),raw_halfspaces=[list(y)+[1.]for y in Y],active=list(range(len(Y))),source=str(source.resolve()),source_audit_sha256=hashlib.sha256((source/'audit.json').read_bytes()).hexdigest(),scope='prospective sphere graph with <=246 edges and 3-connectivity; coordinates are an unverified seed, not a claimed physical body')
        (d/'contractions.json').write_text(json.dumps(history,indent=2));(d/'proposal.json').write_text(json.dumps(proposal,indent=2))
        try:
            meta,q,*_=peel.make(d/'proposal.json',d/'peeling',balanced=True)
            for p in meta['plan']:p['fixed']={}
            grid=max(float(v).as_integer_ratio()[1]for v in q);meta.update(grid=grid,free_controls=[int(round(float(v)*grid))for v in q]);(d/'construction.json').write_text(json.dumps(meta,indent=2))
            c=Chart(d/'construction.json');g=c.physical(c.q0,require_valid=False);v,_,t,_,cl=PhysicalGuards(c,True).evaluate(g)
            row=dict(seed=seed,V=a['V'],E=a['E'],F=a['F'],contractions=len(history),initial_valid=bool(g['valid']),initial_counts=cl)
            print('BULK_BOUND_GOAL_GRAPH',row,flush=True)
            result=realize(d/'construction.json',d/'goal_repair',steps,1e-9,angular_vertices=True)
            assert result is None,'a strict110 bounded body must trigger the exact goal certificate'
            row['result']='finite goal realization failed'
        except(ValueError,AssertionError,np.linalg.LinAlgError)as err:
            row=dict(seed=seed,result='explicitly rejected physical construction',error=repr(err),V=a['V'],E=a['E'],F=a['F'])
        records.append(row);(out/'results.json').write_text(json.dumps(records,indent=2))
        print('BULK_BOUND_CASE',row,flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--seeds',type=int,default=6);p.add_argument('--steps',type=int,default=220);a=p.parse_args();run(a.source,a.out,a.seeds,a.steps)
