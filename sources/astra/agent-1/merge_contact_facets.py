"""Propose facet unions at short polar edges, then reconstruct all contacts.

The distance threshold only proposes a new combinatorial complex. It never
certifies coplanarity or a hull count. New free controls reconstruct an actual
body with the proposed facets exactly coplanar; complete strict noncontacts and
orientations are checked numerically, and a separate rational audit is required.
"""
import argparse,json,pathlib
import numpy as np
from contact_forest import ContactModel
from make_contact_atlas import make

def run(source,input,out,tol=1e-9,nU=2,nS=1,strategy='balanced',cleanup=False):
    c=ContactModel(source,nU,nS,'local');z=np.load(input)['z'] if input else c.initial;e=c.evaluate(z,False);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);Y=e['Y'];parent=np.arange(c.F)
    def root(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    scale=np.sqrt(np.mean(Y*Y));merged=[]
    for i,j in c.es:
        length=np.linalg.norm(Y[i]-Y[j])
        if length<tol*scale:
            parent[root(int(i))]=root(int(j));merged.append([int(i),int(j),float(length)])
    groups={}
    for i in range(c.F):groups.setdefault(root(i),[]).append(i)
    if len(groups)==c.F:raise ValueError('no facet union proposed at this explicit threshold')
    faces=[];normals=[]
    for ids in groups.values():
        boundary={}
        for f in ids:
            cy=c.meta['faces'][f]
            for i,j in zip(cy,cy[1:]+cy[:1]):
                if (j,i) in boundary:del boundary[j,i]
                else:
                    if (i,j) in boundary:raise ValueError('duplicate oriented patch edge')
                    boundary[i,j]=1
        nxt={i:j for i,j in boundary}
        if len(nxt)!=len(boundary):raise ValueError('facet union boundary is not a single polygon')
        start=min(nxt);cy=[start];k=nxt[start]
        while k!=start:
            if k in cy:raise ValueError('facet union has pinched or multiply connected boundary')
            cy.append(k);k=nxt[k]
        if len(cy)!=len(boundary):raise ValueError('facet union has extra boundary components')
        faces.append(cy);normals.append(Y[ids].mean(0))
    surviving_groups=list(groups.values());retired_groups=[]
    while True:
        degree={i:sum(i in cy for cy in faces) for i in set(sum(faces,[]))};bad={i for i,d in degree.items() if d<3}
        if not bad:break
        faces=[[i for i in cy if i not in bad] for cy in faces]
        degenerate=[i for i,cy in enumerate(faces) if len(cy)<3]
        if degenerate:
            if not cleanup:raise ValueError('facet union would destroy an additional facet')
            retired_groups.extend(surviving_groups[i] for i in degenerate);retain=[i for i in range(len(faces)) if i not in degenerate];faces=[faces[i] for i in retain];normals=[normals[i] for i in retain];surviving_groups=[surviving_groups[i] for i in retain]
            if len(faces)<4:raise ValueError('compound union leaves fewer than four facets')
    active=sorted(set(sum(faces,[])));ix={i:j for j,i in enumerate(active)};faces=[[ix[i] for i in cy] for cy in faces];X=e['X'][active]
    edges=sorted({tuple(sorted((i,j))) for cy in faces for i,j in zip(cy,cy[1:]+cy[:1])})
    if len(X)-len(edges)+len(faces)!=2:raise ValueError('proposed facet union fails Euler identity')
    if len(edges)<17:raise ValueError('proposed complexity is below the requested search range')
    if cleanup:
        import networkx as nx
        graph=nx.Graph();graph.add_edges_from(edges)
        if nx.node_connectivity(graph)<3:raise ValueError('compound union graph is not 3-connected')
        boundary={edge:0 for edge in edges}
        for cy in faces:
            for i,j in zip(cy,cy[1:]+cy[:1]):boundary[tuple(sorted((i,j)))]+=1
        if any(count!=2 for count in boundary.values()):raise ValueError('compound union is not a closed manifold')
    proposal=dict(scope='UNVERIFIED numerical facet-union proposal, not an audit',source=str(pathlib.Path(source).resolve()),input=str(input),threshold=tol,groups=surviving_groups,compound_cleanup=cleanup,retired_facet_groups=retired_groups,retained_vertex_indices=active,merged_polar_edges=merged,V=len(X),E=len(edges),F=len(faces),faces=faces,edges=edges,active=list(range(len(faces))),raw_vertices=[[str(x) for x in v] for v in X],raw_halfspaces=[[str(x) for x in q]+['1'] for q in normals])
    (out/'proposal.json').write_text(json.dumps(proposal,indent=2));make(out/'proposal.json',out/'chart',balanced=strategy=='balanced',quality_first=strategy=='quality');child=ContactModel(out/'chart',nU,nS,'local');ee=child.evaluate(child.initial,False);summary=dict(V=len(ee['X']),E=child.meta['E'],F=child.F,C2E=2*child.meta['E'],S=ee['S'],U=ee['U'],minimum=float(ee['mechanical'].min()),noncontact=ee['minimum_gap'],turn=ee['minimum_turn'],bars=ee['bars']);(out/'summary.json').write_text(json.dumps(summary,indent=2));np.savez(out/'realization.npz',z=child.initial,X=ee['X'],Q=ee['Y']);print('RECONSTRUCTED_FACET_UNION_REQUIRES_EXACT',summary,flush=True)
    return summary

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--source',required=True);ap.add_argument('--input');ap.add_argument('--out',required=True);ap.add_argument('--tol',type=float,default=1e-9);ap.add_argument('--nU',type=int,default=2);ap.add_argument('--nS',type=int,default=1);ap.add_argument('--strategy',choices=['balanced','greedy','quality'],default='balanced');ap.add_argument('--compound-cleanup',action='store_true');a=ap.parse_args();run(a.source,a.input,a.out,a.tol,a.nU,a.nS,a.strategy,a.compound_cleanup)
