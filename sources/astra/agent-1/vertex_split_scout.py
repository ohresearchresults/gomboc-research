"""Split a nonsimple vertex by a diagonal of its genuine polar face.
The new graph adds one true edge and one vertex. The coincident-vertex proposal
is not a body until strict convex contact admission succeeds. Mass is always
integrated on the resulting physical primal polyhedron.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,pathlib,time,contextlib
import numpy as np
from contact_forest import ContactModel,correct
from make_contact_atlas import make
from repair_contact_domain import run as admit
from contact_topology_continuation import run as continue_contacts

def polar_faces(c,e):
    result=[]
    for v,x in enumerate(e['X']):
        ids=np.flatnonzero(c.inc[:,v]);Y=e['Y'][ids];centre=Y.mean(0);a=Y[0]-centre;a/=np.linalg.norm(a);b=np.cross(x,a);b/=np.linalg.norm(b);order=np.argsort(np.arctan2((Y-centre)@b,(Y-centre)@a));result.append(ids[order].tolist())
    return result

def proposal(c,e,v,i,j,out):
    polar=polar_faces(c,e);cy=polar[v];i,j=sorted((i,j));children=[cy[i:j+1],cy[j:]+cy[:i+1]];assert min(map(len,children))>=3;dual_faces=[f for k,f in enumerate(polar) if k!=v]+children;X=np.r_[np.delete(e['X'],v,axis=0),e['X'][[v,v]]];Y=e['Y'];edge_faces={}
    for f,face in enumerate(dual_faces):
        for a,b in zip(face,face[1:]+face[:1]):edge_faces.setdefault(tuple(sorted((a,b))),[]).append(f)
    if any(len(fs)!=2 for fs in edge_faces.values()):raise ValueError('split dual boundary is not closed')
    faces=[]
    for f,q in enumerate(Y):
        adj={}
        for edge,(a,b) in edge_faces.items():
            if f not in edge:continue
            adj.setdefault(a,[]).append(b);adj.setdefault(b,[]).append(a)
        if any(len(ns)!=2 for ns in adj.values()):raise ValueError('new primal face is not a cycle')
        start=min(adj);cycle=[start];previous=None;current=start
        while True:
            nxt=next(i for i in adj[current] if i!=previous)
            if nxt==start:break
            if nxt in cycle:raise ValueError('new primal face pinched')
            cycle.append(nxt);previous,current=current,nxt
        if len(cycle)!=len(adj):raise ValueError('new primal face disconnected')
        area=sum(np.cross(X[cycle[k]]-X[cycle[0]],X[cycle[k+1]]-X[cycle[0]]) for k in range(1,len(cycle)-1))
        if area@q<0:cycle.reverse()
        faces.append(cycle)
    edges=sorted({tuple(sorted((a,b))) for face in faces for a,b in zip(face,face[1:]+face[:1])});assert len(edges)==c.meta['E']+1 and len(X)-len(edges)+len(Y)==2
    r=dict(scope='UNVERIFIED coincident-vertex split proposal; strict convex admission required',split_vertex=v,polar_diagonal=[cy[i],cy[j]],V=len(X),E=len(edges),F=len(Y),faces=faces,edges=edges,active=list(range(len(Y))),raw_vertices=[[str(x) for x in row] for row in X],raw_halfspaces=[[str(x) for x in row]+['1'] for row in Y]);out=pathlib.Path(out);out.mkdir();(out/'proposal.json').write_text(json.dumps(r,indent=2));make(out/'proposal.json',out/'chart',quality_first=True)

def run(source,input,out,limit=7,opening=1e-5):
    source=pathlib.Path(source);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);c=ContactModel(source,1,2,'local',exempt_junior=True);e=c.evaluate(np.load(input)['z'],False);assert c.meta['E']<248;polar=polar_faces(c,e);U=e['roots'][0][0];junior=e['roots'][1][1];rank=sorted((0 if v in c.meta['faces'][junior] else 1,-len(face),v) for v,face in enumerate(polar) if len(face)>=4 and v!=U);history=[];start=time.time()
    for trial,(_,_,v) in enumerate(rank[:limit]):
        folder=out/f'trial{trial:02d}-vertex{v:03d}';i=0;j=len(polar[v])//2
        try:
            proposal(c,e,v,i,j,folder)
            with (folder/'calculation.log').open('w') as log,contextlib.redirect_stdout(log):
                admit(folder/'chart',folder/'domain-admission',nU=1,nS=2,eps=1e-8,steps=70)
                admitted=folder/'domain-admission/ADMITTED.npz'
                if not admitted.exists():raise ValueError('no strict convex split realization admitted')
                child=ContactModel(folder/'chart',1,2,'local',exempt_junior=True);z=np.load(admitted)['z'];z,ee,ok=correct(child,z,folder/'finite-opening',steps=90,eps=1e-7,trust=.003,verbose=True,polish_margin=True,physical_retraction=True,edge_minimum=(child.meta['V']-2,child.meta['V']-1,opening));np.savez(folder/'opened.npz',z=z,X=ee['X'],Q=ee['Y'])
                if ee['S']==ee['U']==1:
                    (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str((folder/'chart').resolve()),input=str((folder/'opened.npz').resolve())),indent=2));return
                if not ok:raise ValueError('the finite split opening did not recover the strict own211 class')
                continue_contacts(folder/'chart',folder/'opened.npz',folder/'continuation',side='Q',rounds=10,tol=1e-8,strategy='balanced',flow_steps=100)
            if (folder/'continuation/POTENTIAL_OWN110.json').exists():
                (out/'POTENTIAL_OWN110.json').write_bytes((folder/'continuation/POTENTIAL_OWN110.json').read_bytes());return
            h=folder/'continuation/history.json';row=dict(trial=trial,split_vertex=v,seconds=time.time()-start)
            if h.exists():row['last']=json.loads(h.read_text())[-1]
        except (ValueError,AssertionError,RuntimeError,np.linalg.LinAlgError) as error:row=dict(trial=trial,split_vertex=v,error=repr(error),seconds=time.time()-start)
        history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('VERTEX_SPLIT_TRIAL',json.dumps(row),flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--source',required=True);ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--limit',type=int,default=7);ap.add_argument('--opening',type=float,default=1e-5);a=ap.parse_args();run(a.source,a.input,a.out,a.limit,a.opening)
