"""NEW exact-contact facet-union bodies from bounded shadow candidates.

Numerical closeness nominates topology only. The old body is never recounted by
tolerance. A full rational contact realization with its own homogeneous mass,
strict convexity and complete exact census is necessary for any accepted goal.
"""
import argparse,json,hashlib,importlib.util
from pathlib import Path
import numpy as np
from vertex_geometry import geometry
from bounded_contact_cleanup import groups
from strict110_contact_coarsening import normalize
from contact_numpy import Chart
from contact_physical_110 import PhysicalGuards,realize

def proposal(X,cut):
    g=geometry(X,False);ids=g['vertices'];lookup={int(i):k for k,i in enumerate(ids)};XX=g['Z'][ids];faces=[];Y=[];base=[]
    for i,tri in enumerate(g['T']):
        if np.all(tri<4):base.append(i)
        else:faces.append([lookup[int(v)]for v in tri]);Y.append(g['H'][i])
    # The source construction explicitly sets one shared literal basal height.
    # Only this already-exact plane is combined before NEW union nominations.
    if base:
        directed=set()
        for f in base:
            tri=list(map(int,g['T'][f]))
            for a,b in zip(tri,tri[1:]+tri[:1]):
                if(b,a)in directed:directed.remove((b,a))
                else:directed.add((a,b))
        nxt=dict(directed);cy=[min(nxt)]
        while nxt[cy[-1]]!=cy[0]:cy.append(nxt[cy[-1]])
        faces.append([lookup[v]for v in cy]);Y.append(g['H'][base[0]])
    Y=np.array(Y);R=np.sqrt(np.mean(np.sum(XX*XX,axis=1)));owners={}
    for f,cy in enumerate(faces):
        for a,b in zip(cy,cy[1:]+cy[:1]):owners.setdefault(tuple(sorted((a,b))),[]).append(f)
    if not all(len(v)==2 for v in owners.values()):raise ValueError('source graph is not a closed 2-manifold')
    qe=np.array(list(owners.values()));fg=groups(len(Y),qe,np.linalg.norm(Y[qe[:,0]]-Y[qe[:,1]],axis=1)*R,cut)
    if len(fg)==len(Y):raise ValueError('no facet union nominated')
    ff=[];YY=[]
    for grp in fg:
        directed=set()
        for f in grp:
            cy=faces[f]
            for a,b in zip(cy,cy[1:]+cy[:1]):
                if(b,a)in directed:directed.remove((b,a))
                else:directed.add((a,b))
        nxt=dict(directed)
        if not nxt or len(nxt)!=len(directed):raise ValueError('facet union is not a simple disk')
        cy=[min(nxt)]
        while nxt[cy[-1]]!=cy[0]:
            z=nxt[cy[-1]]
            if z in cy:raise ValueError('multiple union boundary cycles')
            cy.append(z)
        if len(cy)!=len(nxt):raise ValueError('disconnected facet union')
        ff.append(cy);YY.append(Y[grp].mean(0))
    fc,xx,yy,active,edges=normalize(ff,XX,np.array(YY));assert17=17<=len(edges)<=248
    if not assert17 or len(xx)+len(edges)+len(yy)>=500:raise ValueError('nominated graph outside goal complexity')
    return dict(V=len(xx),E=len(edges),F=len(yy),raw_vertices=xx.tolist(),raw_halfspaces=[list(y)+[1.]for y in yy],active=list(range(len(yy))),faces=fc,edges=edges,facet_groups=fg,cutoff=cut,scope='NEW proposed contact graph; no physical validity or census asserted before realization')

def run(source,out,steps):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(source);spec=importlib.util.spec_from_file_location('shadow_union_peel','sources/peer_balanced_contact/make_contact_atlas.py');peel=importlib.util.module_from_spec(spec);spec.loader.exec_module(peel);records=[];seen=set();eligible=[]
    for k,cut in enumerate([1e-8,1e-6,1e-4,.001,.003,.01,.03,.06,.1,.15]):
        d=out/f'case{k:02d}';d.mkdir();row=dict(case=k,cutoff=cut)
        try:
            p=proposal(X,cut);key=json.dumps([p['V'],p['faces']])
            if key in seen:row['result']='duplicate proposed graph';records.append(row);continue
            seen.add(key);p.update(source=str(Path(source).resolve()),sha256=hashlib.sha256(Path(source).read_bytes()).hexdigest());(d/'proposal.json').write_text(json.dumps(p,indent=2));meta,q,*_=peel.make(d/'proposal.json',d/'peeling',balanced=True)
            for plan in meta['plan']:plan['fixed']={}
            grid=max(float(v).as_integer_ratio()[1]for v in q);meta.update(grid=grid,free_controls=[int(round(float(v)*grid))for v in q]);(d/'construction.json').write_text(json.dumps(meta,indent=2));c=Chart(d/'construction.json');g=c.physical(c.q0,require_valid=False);v,_,turn,_,cl=PhysicalGuards(c,True).evaluate(g);merit=float(np.maximum(1e-9-v,0).sum()+np.maximum(1e-11-g['noncontact'],0).sum()+np.maximum(1e-12-turn,0).sum());row.update(V=p['V'],E=p['E'],F=p['F'],valid=bool(g['valid']),merit=merit,census_numerical=cl);eligible.append((merit,d,row))
        except(ValueError,AssertionError,np.linalg.LinAlgError)as e:row.update(result='rejected proposal',error=repr(e))
        records.append(row)
    (out/'screen.json').write_text(json.dumps(records,indent=2));eligible.sort(key=lambda x:x[0])
    for _,d,row in eligible:
        print('SHADOW_EXACT_UNION_GOAL',row,flush=True);realize(d/'construction.json',d/'physical_goal',steps,1e-9,angular_vertices=True)
    print('SHADOW_UNION_FINITE_STOP',len(eligible),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--steps',type=int,default=1200);a=p.parse_args();run(a.source,a.out,a.steps)
