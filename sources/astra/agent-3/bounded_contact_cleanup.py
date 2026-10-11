"""New exact-contact bodies nominated by collisions in a <=84-plane family.

Closeness only nominates a DIFFERENT contact graph. Literal rational contact
reconstruction, strict noncontacts, and the complete exact hull audit determine
the new body. No coordinates are merely relabelled or approximately merged.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np

from contact_numpy import Chart
from contact_physical_110 import PhysicalGuards, realize
from strict110_contact_coarsening import normalize
from support_geometry import geometry


def groups(n,edges,length,cutoff):
    parent=list(range(n))
    def root(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]];i=parent[i]
        return i
    for (i,j),d in zip(edges,length):
        if d<cutoff:
            a,b=root(int(i)),root(int(j));parent[b]=a
    vals={}
    for i in range(n):vals.setdefault(root(i),[]).append(i)
    return list(vals.values())


def proposal(Q,primal_cut,dual_cut):
    g=geometry(Q,False);X=g['Z'];Y=g['H'];faces=g['faces'];R=np.sqrt(np.mean(np.sum(X*X,axis=1)))
    owners={}
    for f,cy in enumerate(faces):
        for i,j in zip(cy,cy[1:]+cy[:1]):owners.setdefault(tuple(sorted((i,j))),[]).append(f)
    pe=np.array(list(owners));qe=np.array(list(owners.values()))
    vg=groups(len(X),pe,np.linalg.norm(X[pe[:,0]]-X[pe[:,1]],axis=1)/R,primal_cut)
    fg=groups(len(Y),qe,np.linalg.norm(Y[qe[:,0]]-Y[qe[:,1]],axis=1)*R,dual_cut)
    if len(vg)==len(X)and len(fg)==len(Y):raise ValueError('no nominated graph change')
    vi={v:k for k,grp in enumerate(vg)for v in grp}
    XX=np.array([X[grp].mean(0)for grp in vg]);newfaces=[];YY=[]
    for grp in fg:
        directed=set()
        for f in grp:
            cy=faces[f]
            for a,b in zip(cy,cy[1:]+cy[:1]):
                if (b,a)in directed:directed.remove((b,a))
                else:directed.add((a,b))
        nxt=dict(directed)
        if len(nxt)!=len(directed)or not nxt:raise ValueError('nominated facet union is not a simple disk')
        cy=[min(nxt)]
        while nxt[cy[-1]]!=cy[0]:
            z=nxt[cy[-1]]
            if z in cy:raise ValueError('facet union boundary has more than one cycle')
            cy.append(z)
        if len(cy)!=len(nxt):raise ValueError('facet union has another boundary component')
        newfaces.append([vi[i]for i in cy]);YY.append(Y[grp].mean(0))
    fc,xx,yy,active,ee=normalize(newfaces,XX,np.array(YY))
    assert 17<=len(ee)<=246 and len(yy)<=84
    return dict(V=len(xx),F=len(yy),E=len(ee),faces=fc,edges=ee,raw_vertices=xx.tolist(),
                raw_halfspaces=[list(v)+[1.]for v in yy],active=list(range(len(yy))),
                primal_groups=vg,dual_groups=fg,primal_cutoff=primal_cut,dual_cutoff=dual_cut,
                scope='new proposed contact graph and seed coordinates, not yet asserted a physical convex body')


def run(sources,out,attempts,steps):
    out=Path(out);out.mkdir(parents=True,exist_ok=False)
    spec=importlib.util.spec_from_file_location('bounded_cleanup_peel','sources/peer_balanced_contact/make_contact_atlas.py');peel=importlib.util.module_from_spec(spec);spec.loader.exec_module(peel)
    records=[];eligible=[];case=0;seen=set()
    for source in sources:
        Q=np.load(source)
        for pc,dc in [(a,b)for a in [1e-7,1e-5,1e-3]for b in [0.,1e-6,1e-4]]:
            row=dict(case=case,source=str(Path(source).resolve()),primal_cutoff=pc,dual_cutoff=dc);d=out/f'case{case:03d}';case+=1;d.mkdir()
            try:
                p=proposal(Q,pc,dc);key=json.dumps([p['faces'],p['V'],p['F']])
                if key in seen:row['result']='duplicate prospective topology';records.append(row);continue
                seen.add(key);p.update(source=str(Path(source).resolve()),source_sha256=hashlib.sha256(Path(source).read_bytes()).hexdigest());(d/'proposal.json').write_text(json.dumps(p,indent=2))
                meta,q,*_=peel.make(d/'proposal.json',d/'peeling',balanced=True)
                for plan in meta['plan']:plan['fixed']={}
                grid=max(float(v).as_integer_ratio()[1]for v in q);meta.update(grid=grid,free_controls=[int(round(float(v)*grid))for v in q]);(d/'construction.json').write_text(json.dumps(meta,indent=2))
                c=Chart(d/'construction.json');g=c.physical(c.q0,require_valid=False);v,_,turn,_,cl=PhysicalGuards(c,True).evaluate(g)
                merit=float(np.maximum(1e-9-v,0).sum()+np.maximum(1e-11-g['noncontact'],0).sum()+np.maximum(1e-12-turn,0).sum())
                row.update(V=p['V'],E=p['E'],F=p['F'],merit=merit,valid=bool(g['valid']),result='unverified prospective contact seed',**cl);eligible.append((merit,d,row))
            except(ValueError,AssertionError,np.linalg.LinAlgError)as err:row.update(result='rejected prospective topology',error=repr(err))
            records.append(row)
    (out/'screen.json').write_text(json.dumps(records,indent=2));eligible.sort(key=lambda r:r[0])
    for merit,d,row in eligible[:attempts]:
        print('BOUNDED_CONTACT_GOAL_NOMINATION',d,row,flush=True)
        exact=realize(d/'construction.json',d/'goal_repair',steps,1e-9,angular_vertices=True)
        if exact is not None:raise AssertionError('an admitted own110 body in this bounded family should have triggered the goal certificate')
    print('BOUNDED_CONTACT_FINITE_STOP',len(eligible),min(attempts,len(eligible)),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('out');p.add_argument('sources',nargs='+');p.add_argument('--attempts',type=int,default=8);p.add_argument('--steps',type=int,default=180);a=p.parse_args();run(a.sources,a.out,a.attempts,a.steps)
