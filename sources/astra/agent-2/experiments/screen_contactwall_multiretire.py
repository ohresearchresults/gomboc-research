import sys,json,itertools,numpy as np
from canonical_atlas import ROOT,Chart
from geometry import hull_from_supports,mass,angular_scores
from support_persistence import barcode
folder=ROOT/'artifacts/canonical_atlas/contactwall_C494';c=Chart(folder);q=np.load(folder/'screen_projected1/source_q.npy');g=c.graph(q);Y=g['Q'];rows=[]
for n in range(2,6):
 for removed in itertools.combinations([4,18,35,94,99],n):
  try:
   X,H,faces,tr,E,active=hull_from_supports(np.delete(Y,removed,axis=0),tol=1e-10);vol,cent=mass(X,tr);Z=X-cent;Q=H/(1-H@cent)[:,None];edge={}
   for f,vs in enumerate(faces):
    for i,j in zip(vs,vs[1:]+vs[:1]):edge.setdefault(tuple(sorted((i,j))),[]).append(f)
   assert all(len(x)==2 for x in edge.values());depths=[]
   for A,ee in [(Z,np.array(list(edge))),(Q,np.array(list(edge.values())))]:
    pp,ww,bb=barcode(A,np.ones(len(A)),ee);depths.append(float(np.max(bb/np.sum(A[pp[:,0]]**2,axis=1))))
   s=angular_scores(Q).max(1);u=angular_scores(Z).max(1);row=dict(removed=list(removed),V=len(X),E=E,F=len(H),S=int((s<0).sum()),U=int((u<0).sum()),P=depths[0],Q=depths[1],u_guard=float(np.sort(u)[1]),s_guard=float(np.sort(s)[2]));rows.append(row)
  except Exception as e:rows.append(dict(removed=list(removed),error=str(e)))
rows.sort(key=lambda a:(a.get('S',1000)+a.get('U',1000),a.get('E',1000),a.get('Q',1000)));(folder/'screen_projected1/multiretire.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(rows[:10],indent=2))
