"""Explicit vanishing-edge contraction proposals and physical re-admission.

Numerical distances choose a proposed topology. Each accepted search body is
rebuilt with the resulting contact equations and checked for every support and
facet orientation. Only a separate rational audit establishes exact complexity.
"""
import argparse,json,pathlib
import numpy as np
import networkx as nx
from contact_forest import ContactModel
from make_contact_atlas import make

def run(source,input,out,tol=1e-7,nU=2,nS=1,strategy='quality'):
    c=ContactModel(source,nU,nS,'local',exempt_junior=True);e=c.evaluate(np.load(input)['z'],False)
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);X=e['X'];par=np.arange(len(X))
    def root(i):
        while par[i]!=i:par[i]=par[par[i]];i=par[i]
        return i
    scale=np.sqrt(np.mean(e['P']**2));merged=[]
    for i,j in c.eu:
        length=np.linalg.norm(X[i]-X[j])
        if length<tol*scale:
            par[root(int(i))]=root(int(j));merged.append([int(i),int(j),float(length)])
    if not merged:raise ValueError('no vertex contraction proposed at explicit threshold')
    groups={}
    for i in range(len(X)):groups.setdefault(root(i),[]).append(i)
    mapping={i:k for k,group in enumerate(groups.values()) for i in group}
    Y=np.array([X[group].mean(0) for group in groups.values()]);faces=[];normals=[]
    for f,cy in enumerate(c.meta['faces']):
        ids=[mapping[i] for i in cy];new=[i for k,i in enumerate(ids) if i!=ids[k-1]]
        if len(new)<3:continue
        if len(set(new))!=len(new):raise ValueError('contraction creates a pinched face')
        faces.append(new);normals.append(e['Y'][f])
    if len(set(tuple(sorted(cy)) for cy in faces))!=len(faces):raise ValueError('contraction creates duplicate faces')
    edges=sorted({tuple(sorted((i,j))) for cy in faces for i,j in zip(cy,cy[1:]+cy[:1])})
    if len(Y)-len(edges)+len(faces)!=2:raise ValueError('contraction fails Euler identity')
    if not 17<=len(edges)<c.meta['E']:raise ValueError('contraction does not reduce within requested search range')
    adjacency={edge:[] for edge in edges}
    for f,cy in enumerate(faces):
        for i,j in zip(cy,cy[1:]+cy[:1]):adjacency[tuple(sorted((i,j)))].append(f)
    if any(len(v)!=2 for v in adjacency.values()):raise ValueError('contracted boundary is not a closed manifold')
    graph=nx.Graph();graph.add_edges_from(edges)
    if nx.node_connectivity(graph)<3:raise ValueError('contracted graph is not 3-connected')
    proposal=dict(scope='UNVERIFIED edge-contraction topology proposal',source=str(pathlib.Path(source).resolve()),input=str(pathlib.Path(input).resolve()),threshold=tol,merged_edges=merged,vertex_groups=list(groups.values()),V=len(Y),E=len(edges),F=len(faces),faces=faces,edges=edges,active=list(range(len(faces))),raw_vertices=[[str(x) for x in v] for v in Y],raw_halfspaces=[[str(x) for x in q]+['1'] for q in normals])
    (out/'proposal.json').write_text(json.dumps(proposal,indent=2));make(out/'proposal.json',out/'chart',balanced=strategy=='balanced',quality_first=strategy=='quality')
    child=ContactModel(out/'chart',nU,nS,'local',exempt_junior=True);ee=child.evaluate(child.initial,False)
    summary=dict(scope='Numerical physical body; exact audit required',V=len(ee['X']),E=child.meta['E'],F=child.F,C2E=2*child.meta['E'],S=ee['S'],U=ee['U'],minimum=float(ee['mechanical'].min()),noncontact=ee['minimum_gap'],turn=ee['minimum_turn'],bars=ee['bars'])
    (out/'summary.json').write_text(json.dumps(summary,indent=2));np.savez(out/'realization.npz',z=child.initial,X=ee['X'],Q=ee['Y']);print('RECONSTRUCTED_VERTEX_CONTRACTION',summary,flush=True)
    return summary

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--source',required=True);ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--tol',type=float,default=1e-7);ap.add_argument('--nU',type=int,default=2);ap.add_argument('--nS',type=int,default=1);ap.add_argument('--strategy',choices=['quality','balanced','greedy'],default='quality');a=ap.parse_args();run(a.source,a.input,a.out,a.tol,a.nU,a.nS,a.strategy)
