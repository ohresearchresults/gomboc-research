import sys,json,numpy as np
from canonical_atlas import ROOT,Chart
from geometry import angular_scores
f=ROOT/'artifacts/canonical_atlas/detached_C496_large';c=Chart(f);q=np.load(f/'own_strict_flow_box/latest_q.npy');g=c.graph(q);X,Y,Z,Q=g['X'],g['Y'],g['Z'],g['Q'];vals=[]
for kind,A in [('U',Z),('S',Q)]:
 a=angular_scores(A);mx=a.max(1);pp=a.argmax(1);ids=np.argsort(mx);vals.append(dict(kind=kind,strict_roots=np.flatnonzero(mx<0).tolist(),smallest_positive=[dict(node=int(i),witness=int(pp[i]),escape=float(mx[i])) for i in ids if mx[i]>0][:15]))
gap=1-Y@X.T;gap[c.incidence]=np.inf;flat=np.argsort(gap.ravel())[:25];tight=[dict(face=int(k//len(X)),vertex=int(k%len(X)),gap=float(gap.ravel()[k])) for k in flat]
bp,bw,bb=__import__('support_persistence').barcode(Q,np.ones(c.F),c.es);j=np.argmax(bb);info=dict(primal_polar=vals,tight_noncontacts=tight,main_bar=bp[j].tolist(),centroid=g['c'].tolist(),volume=g['v']);print(json.dumps(info,indent=2));(f/'active_constraints_diagnostic.json').write_text(json.dumps(info,indent=2)+'\n')
