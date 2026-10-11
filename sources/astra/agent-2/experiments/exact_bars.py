"""Exact normalized upper-level bars on true primal and polar edge graphs."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
import sys,json,hashlib
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def bars(P,edges):
    radii=[dot(x,x) for x in P];events=[]
    for i,j in edges:
        d=sub(P[j],P[i]);t=max(Q(0),min(Q(1),-dot(P[i],d)/dot(d,d)));foot=tuple(a+t*b for a,b in zip(P[i],d));events.append((dot(foot,foot),i,j))
    parent=list(range(len(P)));heir=list(range(len(P)));out=[]
    def find(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    for death,i,j in sorted(events,reverse=True):
        a,b=find(i),find(j)
        if a==b:continue
        if radii[heir[a]]<radii[heir[b]]:a,b=b,a
        root=heir[b];parent[b]=a;birth=radii[root];depth=(birth-death)/birth
        assert depth>=0
        if depth:out.append({'root':root,'death_edge':[i,j],'birth_squared':str(birth),'death_squared':str(death),'relative_depth':str(depth),'relative_depth_float':float(depth),'raw_depth_squared':str(birth-death)})
    assert len({find(i) for i in range(len(P))})==1
    return sorted(out,key=lambda a:Q(a['relative_depth']),reverse=True)
def audit(path):
    p=Path(path);report=json.loads(p.read_text());c=tuple(map(Q,report['raw_centroid']));X=[sub(tuple(map(Q,row)),c) for row in report['raw_vertices']]
    Y=[tuple(Q(x,Q(h)-dot(n,c)) for x in n) for n,h in zip(report['normals'],report['offsets'])]
    adj=defaultdict(list)
    for k,f in enumerate(report['faces']):
        for i,j in zip(f,f[1:]+f[:1]):adj[tuple(sorted((i,j)))].append(k)
    assert all(len(v)==2 for v in adj.values())
    P=bars(X,report['edges']);R=bars(Y,list(adj.values()))
    assert len(P)==report['counts'][1]-1 and len(R)==report['counts'][0]-1
    out={'input_report_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'strict':report['counts'],'weak':report['weak'],'P':P,'Q':R}
    dest=p.with_name(p.stem+'_exact_bars.json');dest.write_text(json.dumps(out,indent=2)+'\n')
    print(p,'P',[r['relative_depth_float'] for r in P],'Q',[r['relative_depth_float'] for r in R],flush=True)
if __name__=='__main__':
    for p in sys.argv[1:]:audit(p)
