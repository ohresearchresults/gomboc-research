"""Endpoint search after explicit edge identification in a true hull complex.
Intermediate proposals need not keep the original equilibrium census. Only
fully admitted own110 endpoints are retained as contraction nominations, and
each needs its own exact audit. An over-budget reduction is not the goal.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,argparse,time
import numpy as np
import networkx as nx
from contact_forest import ContactModel,correct
from contact_edge_contraction import propose
from make_contact_atlas import make
from repair_contact_domain import run as admit

def run(source,input,out,edges):
    source=pathlib.Path(source);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);c=ContactModel(source,1,1,'local');z=np.load(input)['z'] if input else c.initial;e=c.evaluate(z,False);history=[];start=time.time()
    np.savez(out/'parent.npz',z=z,X=e['X'],Q=e['Y'])
    for index in edges:
        folder=out/f'edge{index:04d}';edge=c.eu[index]
        try:propose(c,e,edge,folder)
        except (ValueError,AssertionError,RuntimeError,np.linalg.LinAlgError) as error:
            folder.mkdir(parents=True,exist_ok=True);(folder/'original_proposal_error.txt').write_text(repr(error))
        if not (folder/'proposal.json').exists():continue
        r=json.loads((folder/'proposal.json').read_text());G=nx.Graph();G.add_edges_from(r['edges']);connectivity=nx.node_connectivity(G)
        if connectivity<3:
            (folder/'rejected_graph.json').write_text(json.dumps(dict(node_connectivity=connectivity,reason='not the graph of a convex 3-polytope')));continue
        make(folder/'proposal.json',folder/'chart-quality',quality_first=True);child=ContactModel(folder/'chart-quality',1,1,'local');zz=child.initial
        try:ee=child.evaluate(zz,False)
        except (ValueError,RuntimeError,np.linalg.LinAlgError):
            admit(folder/'chart-quality',folder/'convex-domain',nU=1,nS=1,eps=1e-8,steps=150)
            if not (folder/'convex-domain/ADMITTED.npz').exists():
                history.append(dict(edge_index=index,edge=edge.tolist(),stage='no convex realization admitted',seconds=time.time()-start));(out/'history.json').write_text(json.dumps(history,indent=2));continue
            zz=np.load(folder/'convex-domain/ADMITTED.npz')['z'];ee=child.evaluate(zz,False)
        np.savez(folder/'convex-input.npz',z=zz,X=ee['X'],Q=ee['Y'])
        before=dict(S=ee['S'],U=ee['U'])
        zz,ee,ok=correct(child,zz,folder/'own110-repair',steps=240,eps=2e-9,trust=.005,verbose=False,polish_margin=True,physical_retraction=True)
        row=dict(edge_index=index,edge=edge.tolist(),V=len(ee['X']),E=child.meta['E'],F=child.F,S=ee['S'],U=ee['U'],minimum=float(ee['mechanical'].min()),accepted=bool(ok and ee['S']==ee['U']==1),before=before,seconds=time.time()-start);history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('DIRECT_CONTRACTION_ENDPOINT',row,flush=True)
        if row['accepted']:
            np.savez(folder/'NOMINATION_OWN110.npz',z=zz,X=ee['X'],Q=ee['Y']);(out/'NOMINATION.json').write_text(json.dumps(dict(folder=str(folder.resolve()),chart=str((folder/'chart-quality').resolve()),**row),indent=2));return

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--source',required=True);ap.add_argument('--input');ap.add_argument('--out',required=True);ap.add_argument('--edges',type=int,nargs='+',required=True);a=ap.parse_args();run(a.source,a.input,a.out,a.edges)
