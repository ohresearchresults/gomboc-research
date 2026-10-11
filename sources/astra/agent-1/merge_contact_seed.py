"""Propose an explicit contact complex by merging adjacent nearly planar faces.
The numerical input is only a proposal. A contact chart reconstructs it, and all
strict physical gaps/orientations are checked before any scientific use.
"""
import numpy as np,json,pathlib,argparse
from scipy.spatial import ConvexHull
from make_contact_atlas import make
from atlas_repair import Atlas
from geometry import arrows

def run(input,out,tol=1e-7):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);X=np.load(input)['X'];h=ConvexHull(X);T=h.simplices.copy();a=X[T];flip=(np.cross(a[:,1]-a[:,0],a[:,2]-a[:,0])*h.equations[:,:3]).sum(1)<0;T[flip]=T[flip][:,[0,2,1]];par=np.arange(len(T))
    def find(i):
        while par[i]!=i:par[i]=par[par[i]];i=par[i]
        return i
    for i,nn in enumerate(h.neighbors):
        for j in nn:
            if np.max(abs(h.equations[i]-h.equations[j]))<tol:par[find(i)]=find(int(j))
    groups={}
    for i in range(len(T)):groups.setdefault(find(i),[]).append(i)
    faces=[]
    for ids in groups.values():
        edge={}
        for tri in T[ids]:
            for i,j in zip(tri,np.roll(tri,-1)):
                if (j,i) in edge:del edge[j,i]
                else:edge[i,j]=1
        nxt={int(i):int(j) for i,j in edge};start=min(nxt);cy=[start];p=nxt[start]
        while p!=start:
            if p in cy:raise ValueError('merged patch has noncyclic boundary')
            cy.append(p);p=nxt[p]
        assert len(cy)==len(edge);faces.append(cy)
    while True:
        degree={i:sum(i in cy for cy in faces) for i in set(sum(faces,[]))};bad={i for i,k in degree.items() if k<3}
        if not bad:break
        faces=[[i for i in cy if i not in bad] for cy in faces]
        if any(len(cy)<3 for cy in faces):raise ValueError('merge destroys a true face')
    active=sorted(set(sum(faces,[])));mapping={i:j for j,i in enumerate(active)};P=X[active];faces=[[mapping[i] for i in cy] for cy in faces];edges=sorted({tuple(sorted((i,j))) for cy in faces for i,j in zip(cy,cy[1:]+cy[:1])});assert len(P)-len(edges)+len(faces)==2;Y=[]
    import itertools
    for cy in faces:
        ids=max(itertools.combinations(cy,3),key=lambda v:abs(np.linalg.det(P[list(v)])));Y.append(np.linalg.solve(P[list(ids)],np.ones(3)))
    Y=np.array(Y);proposal=dict(scope='UNVERIFIED numericalcontactcomplexproposal,notanexactaudit',V=len(P),E=len(edges),F=len(faces),raw_vertices=[[str(v) for v in p] for p in P],raw_halfspaces=[[str(v) for v in q]+['1'] for q in Y],active=list(range(len(Y))),faces=faces,edges=edges,source=str(pathlib.Path(input).resolve()),merge_tolerance=tol);(out/'proposal.json').write_text(json.dumps(proposal,indent=2));make(out/'proposal.json',out/'chart');c=Atlas(out/'chart');e=c.evaluate(c.initial,False);rp=arrows(e['X']).max(1);rq=arrows(e['Y']).max(1);summary=dict(V=len(P),E=len(edges),F=len(faces),referenceS=int(np.sum(rq<0)),referenceU=int(np.sum(rp<0)),min_referenceP=float(np.sort(rp)[1]),min_referenceQ=float(np.sort(rq)[1]),ownS=e['S'],ownU=e['U'],minimum_gap=e['minimum_gap'],minimum_turn=e['minimum_turn'],centroid=e['g'].tolist());(out/'summary.json').write_text(json.dumps(summary,indent=2));np.savez(out/'realization.npz',z=c.initial,X=e['X'],Q=e['Y']);print('MERGED_CONTACT_REALIZATION',summary,flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--tol',type=float,default=1e-7);a=ap.parse_args();run(a.input,a.out,a.tol)
