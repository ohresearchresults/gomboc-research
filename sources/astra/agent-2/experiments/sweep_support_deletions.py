"""All literal single-support retirements of a pinned exact physical parent.
Clustering in numerical nomination is declared. Acceptance always requires an
exact rebuilt body; the exact freeze deletes unchanged rational halfspaces.
"""
import sys,json,time,hashlib
from pathlib import Path
from collections import defaultdict
import numpy as np
from gmpy2 import mpq
from scipy.spatial import QhullError
from geometry import hull_from_supports,mass,angular_scores
from support_persistence import ROOT,barcode

def sweep(src,out):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);r=json.loads(src.read_text());g=np.array([float(mpq(x)) for x in r['raw_centroid']]);Y=np.array([[float(mpq(x,mpq(h))) for x in n] for n,h in zip(r['normals'],r['offsets'])]);Y=Y/(1-Y@g)[:,None];rows=[];start=time.time()
    for i in range(len(Y)):
        H=np.delete(Y,i,axis=0)
        try:
            X,N,faces,tri,E,ids=hull_from_supports(H,tol=1e-10);vol,c=mass(X,tri);Z=X-c;Q=N/(1-N@c)[:,None];adj=defaultdict(list)
            for j,f in enumerate(faces):
                for a,b in zip(f,f[1:]+f[:1]):adj[tuple(sorted((a,b)))].append(j)
            assert all(len(x)==2 for x in adj.values())
            pp,pw,P=barcode(Z,np.ones(len(Z)),np.array(list(adj)));qp,qw,Qb=barcode(Q,np.ones(len(Q)),np.array(list(adj.values())));P/=np.sum(Z[pp[:,0]]**2,1);Qb/=np.sum(Q[qp[:,0]]**2,1);us=angular_scores(Z).max(1);ss=angular_scores(Q).max(1)
            row=dict(deleted=i,V=len(X),E=E,F=len(N),S=int((ss<0).sum()),U=int((us<0).sum()),Pmax=float(P.max()),Qmax=float(Qb.max()),centroid=c.tolist(),U1_guard=float(np.sort(us)[1]),S2_guard=float(np.sort(ss)[2]))
            rows.append(row)
            if row['S']<=2 and row['U']==1:print('LITERAL_RETIREMENT_NUM211',row,flush=True)
        except (ValueError,QhullError,np.linalg.LinAlgError,AssertionError) as e:rows.append(dict(deleted=i,error=type(e).__name__,message=str(e)))
    rows.sort(key=lambda x:(x.get('S',999)+x.get('U',999),x.get('E',999),x.get('Qmax',999)))
    (out/'screen.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(src.read_bytes()).hexdigest(),clustering_tolerance=1e-10,numerical_only=True,rows=rows,seconds=time.time()-start),indent=2)+'\n')
    return rows

def exact(src,indices,out):
    sys.set_int_max_str_digits(0);sys.path.insert(0,str(ROOT/'sources/full76/decoded/methods/parent'));import check_B
    check_B.Q=mpq;src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);r=json.loads(src.read_text());H={'H':[[*n,h] for i,(n,h) in enumerate(zip(r['normals'],r['offsets'])) if i not in indices]};B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode();(out/'H.json').write_bytes(B(H));(out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(src.read_bytes()).hexdigest(),deleted_indices=indices),indent=2)+'\n');z=check_B.run(H);raw=B(z);(out/'audit.json').write_bytes(raw);s={k:z[k] for k in ['V','E','F','counts','weak','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};s.update(C2E=2*z['E'],VplusEplusF=z['V']+z['E']+z['F'],audit_sha256=hashlib.sha256(raw).hexdigest());(out/'summary.json').write_text(json.dumps(s,indent=2)+'\n');print('EXACT_LITERAL_RETIREMENT',indices,s,flush=True);return z

if __name__=='__main__':
    if sys.argv[1]=='sweep':sweep(ROOT/sys.argv[2],ROOT/sys.argv[3])
    elif sys.argv[1]=='exact':exact(ROOT/sys.argv[2],[int(v) for v in sys.argv[3].split(',')],ROOT/sys.argv[4])
    else:raise ValueError('choose explicit sweep or exact mode')
