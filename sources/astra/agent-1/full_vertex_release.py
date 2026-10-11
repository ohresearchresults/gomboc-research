"""Release all excess contacts at several nonsimple vertices simultaneously.
Triangulating their true polar faces adds exactly sum(degree-3) primal edges.
The coincident initial geometry is only a proposal. Complete convex-domain
admission and finite opening precede every physical equilibrium calculation.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,pathlib,json,contextlib,time
import numpy as np
from vertex_split_scout import polar_faces
from contact_forest import ContactModel,correct
from make_contact_atlas import make
from repair_contact_domain import run as admit
from contact_topology_continuation import run as continue_contacts

def propose(c,e,vertices,rotation,out):
    polar=polar_faces(c,e);dual=[];owners=[]
    for v,cy in enumerate(polar):
        if v in vertices:
            off=rotation%len(cy);cy=cy[off:]+cy[:off]
            for j in range(1,len(cy)-1):dual.append([cy[0],cy[j],cy[j+1]]);owners.append(v)
        else:dual.append(cy);owners.append(v)
    X=e['X'][owners];Y=e['Y'];edgefaces={}
    for f,cy in enumerate(dual):
        for a,b in zip(cy,cy[1:]+cy[:1]):edgefaces.setdefault(tuple(sorted((a,b))),[]).append(f)
    if any(len(v)!=2 for v in edgefaces.values()):raise ValueError('polar triangulation is not a closed manifold')
    faces=[]
    for i,q in enumerate(Y):
        adj={}
        for ed,(a,b) in edgefaces.items():
            if i in ed:adj.setdefault(a,[]).append(b);adj.setdefault(b,[]).append(a)
        if any(len(ns)!=2 for ns in adj.values()):raise ValueError('new primal face is not a cycle')
        start=min(adj);cy=[start];previous=None;current=start
        while True:
            nxt=next(j for j in adj[current] if j!=previous)
            if nxt==start:break
            if nxt in cy:raise ValueError('new face pinched')
            cy.append(nxt);previous,current=current,nxt
        if len(cy)!=len(adj):raise ValueError('new face disconnected')
        area=sum(np.cross(X[cy[k]]-X[cy[0]],X[cy[k+1]]-X[cy[0]]) for k in range(1,len(cy)-1))
        if area@q<0:cy.reverse()
        faces.append(cy)
    edges=sorted({tuple(sorted((a,b))) for cy in faces for a,b in zip(cy,cy[1:]+cy[:1])});added=[ed for ed in edges if owners[ed[0]]==owners[ed[1]]];expected=sum(len(polar[v])-3 for v in vertices)
    assert len(added)==expected and len(edges)==c.meta['E']+expected and len(X)-len(edges)+len(Y)==2
    out=pathlib.Path(out);out.mkdir();r=dict(scope='UNVERIFIED coincident multi-vertex contact release; no body claim before complete convex admission',released_vertices=vertices,fan_rotation=rotation,old_vertex_owner=owners,new_edges=added,V=len(X),E=len(edges),F=len(Y),faces=faces,edges=edges,active=list(range(len(Y))),raw_vertices=[[str(x) for x in p] for p in X],raw_halfspaces=[[str(x) for x in p]+['1'] for p in Y]);(out/'proposal.json').write_text(json.dumps(r,indent=2));make(out/'proposal.json',out/'chart',quality_first=True);return added

class FiniteOpening(ContactModel):
    def __init__(self,source,edges,opening):
        super().__init__(source,1,2,'local',exempt_junior=True);self.open_edges=np.array(edges,int);self.opening=opening
    def evaluate(self,z,jacobian=True):
        e=super().evaluate(z,jacobian);u,v=self.open_edges.T;delta=e['X'][v]-e['X'][u];length=np.linalg.norm(delta,axis=1);r=np.sqrt(np.mean(np.sum(e['P']**2,axis=1)));e['mechanical']=np.r_[e['mechanical'],length/r-self.opening+1e-7]
        if jacobian:
            dr=np.einsum('ic,icp->p',e['P'],e['DP'])/(len(e['P'])*r);J=np.einsum('ic,icp->ip',delta/length[:,None],e['DX'][v]-e['DX'][u])/r-length[:,None]*dr/r**2;e['J']=np.vstack([e['J'],J])
        return e

def run(source,input,out,vertices,rotations=3,opening=.002):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);c=ContactModel(source,1,2,'local',exempt_junior=True);e=c.evaluate(np.load(input)['z'],False);assert c.meta['E']+sum(int(c.inc[:,v].sum())-3 for v in vertices)<249;history=[];start=time.time()
    for r in range(rotations):
        p=out/f'fan{r:02d}';row=dict(rotation=r,vertices=vertices)
        try:
            added=propose(c,e,vertices,r,p)
            with (p/'calculation.log').open('w') as log,contextlib.redirect_stdout(log):
                admit(p/'chart',p/'convex-admission',nU=1,nS=2,eps=1e-9,steps=100);nom=p/'convex-admission/ADMITTED.npz'
                if not nom.exists():raise ValueError('finite family has no admitted convex initial point')
                cc=FiniteOpening(p/'chart',added,opening);z,ee,ok=correct(cc,np.load(nom)['z'],p/'finite-opening',steps=140,eps=1e-7,trust=.004,verbose=True,polish_margin=True,physical_retraction=True);np.savez(p/'opened.npz',z=z,X=ee['X'],Q=ee['Y']);row.update(opened=bool(ok),S=ee['S'],U=ee['U'],E=cc.meta['E'])
                if ee['S']==ee['U']==1:
                    (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str((p/'chart').resolve()),input=str((p/'opened.npz').resolve())),indent=2));return
                if ok:
                    continue_contacts(p/'chart',p/'opened.npz',p/'continuation',side='Q',rounds=16,tol=1e-8,strategy='balanced',flow_steps=140)
                    if (p/'continuation/POTENTIAL_OWN110.json').exists():(out/'POTENTIAL_OWN110.json').write_bytes((p/'continuation/POTENTIAL_OWN110.json').read_bytes());return
                    if (p/'continuation/history.json').exists():row['last']=json.loads((p/'continuation/history.json').read_text())[-1]
        except (ValueError,AssertionError,RuntimeError,np.linalg.LinAlgError) as error:row['error']=repr(error)
        row['seconds']=time.time()-start;history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('FULL_VERTEX_RELEASE',json.dumps(row),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',required=True);p.add_argument('--input',required=True);p.add_argument('--out',required=True);p.add_argument('--vertices',type=int,nargs='+',required=True);p.add_argument('--rotations',type=int,default=3);p.add_argument('--opening',type=float,default=.002);a=p.parse_args();run(a.source,a.input,a.out,a.vertices,a.rotations,a.opening)
