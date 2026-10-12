"""Numerical proposal of genuine edge contractions with rational contact charts.
No floating proposal here is an exact acceptance certificate.
"""
import argparse,json,itertools,copy
from pathlib import Path
import numpy as np
from contact_model import Model

def merged_top(top,u,v):
    top=copy.deepcopy(top);old=top['owners'];keep=min(u,v);drop=max(u,v)
    assert tuple(sorted((u,v))) in set(map(tuple,top['edges']))
    union=sorted(set(old[u])|set(old[v]))
    assert len(set(old[u])&set(old[v]))==2
    old[keep]=union;old.pop(drop)
    mapping={i:keep if i==drop else i-int(i>drop) for i in range(len(old)+1)}
    faces=[];edges=set()
    for c in top['faces']:
        cy=[]
        for i in c:
            j=mapping[i]
            if not cy or cy[-1]!=j:cy.append(j)
        if cy[0]==cy[-1]:cy.pop()
        if len(cy)<3 or len(set(cy))!=len(cy):raise ValueError('facet disappears or invalid cycle')
        faces.append(cy)
        edges.update(tuple(sorted((a,b))) for a,b in zip(cy,cy[1:]+cy[:1]))
    top['faces']=faces;top['edges']=sorted(edges)
    assert len(top['owners'])-len(edges)+len(faces)==2
    return top,keep,union

def chart(gen,top,G,u,v,policy='old',alpha=.5):
    n=gen['n_supports'];nt,keep,union=merged_top(top,u,v)
    root=tuple(gen['groups'][0]);assert set(root) not in [set(top['owners'][u]),set(top['owners'][v])]
    groups=[list(root)]+[o for o in nt['owners'] if len(o)>3 and tuple(o)!=root]
    groupindex={tuple(o):n+j for j,o in enumerate(groups)}
    X=np.zeros((n+len(groups),3));X[:n]=G['q'];X[n]=[0,0,1]
    prev={tuple(o):G['P'][i] for i,o in enumerate(top['owners'])}
    for j,o in enumerate(groups[1:],1):X[n+j]=(1-alpha)*G['P'][u]+alpha*G['P'][v] if o==union else prev[tuple(o)]
    adj=[set() for _ in X]
    for j,o in enumerate(groups):
        for i in o:adj[i].add(n+j);adj[n+j].add(i)
    oldrank={}
    for k,(i,deps,axes) in enumerate(gen['plan']):
        ni=i if i<n else groupindex.get(tuple(gen['groups'][i-n]))
        if ni is not None:oldrank[ni]=k
    # The new group can be early or late depending on policy.
    new=groupindex[tuple(union)];oldrank[new]=len(X) if policy.endswith('newlast') else -1
    remains=set(range(len(X)));removed=[]
    while len(remains)>1:
        candidates=[i for i in remains if i!=n and len(adj[i]&remains)<=3]
        if not candidates:raise ValueError('contact graph not root-reserved 3-degenerate')
        if policy.startswith('old'):i=max(candidates,key=lambda i:(oldrank.get(i,-1),i))
        elif policy.startswith('degree'):i=min(candidates,key=lambda i:(len(adj[i]&remains),-oldrank.get(i,-1),i))
        elif policy.startswith('maxdegree'):i=max(candidates,key=lambda i:(len(adj[i]&remains),oldrank.get(i,-1),i))
        else:raise ValueError(policy)
        deps=sorted(adj[i]&remains);d=len(deps)
        if d:
            axes=max(itertools.combinations(range(3),d),key=lambda ax:abs(np.linalg.det(X[np.ix_(deps,ax)])))
            if abs(np.linalg.det(X[np.ix_(deps,axes)]))<1e-12:raise ValueError('singular proposed contact minor')
        else:axes=()
        removed.append([i,deps,list(axes)]);remains.remove(i)
    ng={'version':1,'n_supports':n,'grid':10**12,'controls':np.rint(X*10**12).astype(np.int64).tolist(),'plan':removed[::-1],'groups':groups,'stable':3,'labels':f'RECHART_{len(nt["edges"])*2}_{u}_{v}_{policy}_{alpha}'}
    m=Model(ng,nt);GG=m.geom(m.x0,False)
    assert m.k==len(nt['edges'])+3
    # Confirm each declared polygon cycle is the convex boundary, not a star.
    for f,cy in enumerate(nt['faces']):
        pts=GG['P'][cy];normal=GG['q'][f]
        for a,b in zip(pts,np.roll(pts,-1,axis=0)):
            values=np.cross(b-a,pts-a)@normal
            if values.min() < -1e-10:raise ValueError('nonconvex or reversed facet cycle')
    # Save the realized nodes rather than a table containing unused tentative values.
    ng['controls']=np.rint(GG['X']*ng['grid']).astype(np.int64).tolist()
    return ng,nt,m.stat(GG)

def main():
    p=argparse.ArgumentParser();p.add_argument('--gen',default='condition36_best.json');p.add_argument('--top',default='TOP36.json');p.add_argument('--out',default='RECHART646');p.add_argument('--limit',type=int,default=40);args=p.parse_args()
    gen=json.load(open(args.gen));top=json.load(open(args.top));m=Model(gen,top);G=m.geom(m.x0,False);print('BASE',m.stat(G),flush=True)
    edges=sorted(top['edges'],key=lambda e:np.linalg.norm(G['P'][e[1]]-G['P'][e[0]]));out=Path(args.out);out.mkdir(exist_ok=True)
    allrec=[]
    for u,v in edges[:args.limit]:
        if m.root in (u,v):continue
        for policy in ['old','oldnewlast','degree','degreenewlast','maxdegree','maxdegreenewlast']:
            for alpha in [.0,.5,1.]:
                try:ng,nt,st=chart(gen,top,G,u,v,policy,alpha)
                except (ValueError,np.linalg.LinAlgError):continue
                rec={'u':u,'v':v,'policy':policy,'alpha':alpha,**st};allrec.append(rec)
                if st['slack']>1e-10:
                    name=f'{u}_{v}_{policy}_{alpha}'.replace('.','p');d=out/name;d.mkdir(exist_ok=True)
                    (d/'GENERATOR.json').write_text(json.dumps(ng,sort_keys=True,separators=(',',':')));(d/'TOP.json').write_text(json.dumps(nt,separators=(',',':')))
                    print(name,st,flush=True)
    (out/'SCREEN.json').write_text(json.dumps(allrec,sort_keys=True))
    print('SUMMARY',len(allrec),'valid',sum(r['slack']>1e-10 for r in allrec),flush=True)
    for r in sorted([r for r in allrec if r['slack']>1e-10],key=lambda r:r['min_escape'],reverse=True)[:20]:print('BEST',r,flush=True)
if __name__=='__main__':main()
