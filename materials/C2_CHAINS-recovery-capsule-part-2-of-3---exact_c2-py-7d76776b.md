# material-7d76776bac62

AI research material

---

"""Exact, exhaustive rational-polyhedron audit for fresh C2 chain candidates.
Standard-library only, Python3.13.5. Input: scale and complete integer source rows.
Exhaustive supporting triples, maximal polygon facets, exact filled mass, complete
strict/additional-weak mechanics and exact simultaneous-level P/Q barcodes.
No float tolerance or Qhull nomination is used in this verifier.
"""
import json,sys,math,hashlib
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from collections import defaultdict,deque

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(k,a):return tuple(k*x for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def enc(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [enc(v) for v in x]
    return x

def polygon(points,ids,n):
    drop=max(range(3),key=lambda j:abs(n[j]));axes=[j for j in range(3) if j!=drop]
    rows=sorted((points[i][axes[0]],points[i][axes[1]],i) for i in ids)
    def area(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lo=[];hi=[]
    for p in rows:
      while len(lo)>=2 and area(lo[-2],lo[-1],p)<=0:lo.pop()
      lo.append(p)
    for p in reversed(rows):
      while len(hi)>=2 and area(hi[-2],hi[-1],p)<=0:hi.pop()
      hi.append(p)
    cyc=[r[2] for r in lo[:-1]+hi[:-1]]
    assert len(cyc)>=3
    if dot(cross(sub(points[cyc[1]],points[cyc[0]]),sub(points[cyc[2]],points[cyc[0]])),n)<0:cyc.reverse()
    k=cyc.index(min(cyc));return cyc[k:]+cyc[:k]

def complex_hull(points):
    assert len(set(points))==len(points)
    planes={}
    for ia,ib,ic in combinations(range(len(points)),3):
      a,b,c=points[ia],points[ib],points[ic];n=cross(sub(b,a),sub(c,a))
      if n==(0,0,0):continue
      h=dot(n,a);side=0;bad=False;zeros=[]
      for j,p in enumerate(points):
        v=dot(n,p)-h
        if v:
          s=1 if v>0 else -1
          if side and side!=s:bad=True;break
          side=s
        else:zeros.append(j)
      if bad:continue
      assert side,'input is not three-dimensional'
      if side>0:n=mul(-1,n);h=-h
      g=math.gcd(*n);n=tuple(v//g for v in n);h//=g
      planes[(*n,h)]=zeros
    assert len(planes)>=4
    raw=[]
    for key,ids in planes.items():raw.append((polygon(points,ids,key[:3]),key))
    raw.sort(key=lambda x:tuple(x[0]))
    used=sorted(set(i for cyc,key in raw for i in cyc));mapping={x:i for i,x in enumerate(used)}
    P=[points[i] for i in used];faces=[[mapping[i] for i in cyc] for cyc,key in raw];eq=[key for cyc,key in raw]
    owners=defaultdict(list)
    for f,cyc in enumerate(faces):
      n=eq[f][:3];h=eq[f][3]
      assert all(dot(n,p)<=h for p in points)
      assert all(dot(n,P[i])==h for i in cyc)
      for a,b in zip(cyc,cyc[1:]+cyc[:1]):owners[tuple(sorted((a,b)))].append((f,a,b))
    edges=sorted(owners);adj=[[] for p in P];fa=[[] for f in faces]
    for a,b in edges:
      o=owners[(a,b)];assert len(o)==2 and o[0][1:]==o[1][:0:-1]
      adj[a].append(b);adj[b].append(a);fa[o[0][0]].append(o[1][0]);fa[o[1][0]].append(o[0][0])
    assert len(P)-len(edges)+len(faces)==2
    seen={0};stack=[0]
    while stack:
      for j in adj[stack.pop()]:
        if j not in seen:seen.add(j);stack.append(j)
    assert len(seen)==len(P)
    return P,used,faces,eq,edges,owners,adj,fa

def mass(P,faces,origin=(0,0,0)):
    v6=0;m=(0,0,0)
    for cyc in faces:
      a=sub(P[cyc[0]],origin)
      for j in range(1,len(cyc)-1):
        b=sub(P[cyc[j]],origin);c=sub(P[cyc[j+1]],origin);d=det(a,b,c)
        v6+=d;m=add(m,mul(d,add(add(a,b),c)))
    assert v6>0
    return F(v6,6),add(origin,tuple(F(v,4*v6) for v in m))

def landscape(X,edges):
    birth=[dot(x,x) for x in X];levels={};adj=[[] for _ in X]
    weights=[]
    for eid,(i,j) in enumerate(edges):
      a=birth[i];c=birth[j];b=dot(X[i],X[j]);w=a if b>=a else c if b>=c else F(a*c-b*b,a+c-2*b)
      weights.append(w);levels.setdefault(w,[]).append(eid);adj[i].append((j,eid));adj[j].append((i,eid))
    par=list(range(len(X)));peak=list(range(len(X)));members=[{i} for i in range(len(X))];bars=[]
    def find(i):
      while par[i]!=i:par[i]=par[par[i]];i=par[i]
      return i
    for w in sorted(levels,reverse=True):
      local=defaultdict(set)
      for eid in levels[w]:
        i,j=edges[eid];a,b=find(i),find(j)
        if a!=b:local[a].add(b);local[b].add(a)
      remaining=set(local)
      while remaining:
        first=min(remaining);group={first};stack=[first];remaining.remove(first)
        while stack:
          for j in local[stack.pop()]:
            if j not in group:group.add(j);stack.append(j);remaining.remove(j)
        elder=max(group,key=lambda r:(birth[peak[r]],-peak[r]));elder_peak=peak[elder]
        for r in sorted(group):
          p=peak[r]
          if r==elder or birth[p]<=w:continue
          comp=sorted(i for i in members[r] if birth[i]>w);comp_set=set(comp)
          cut=[list(e) for e in edges if (e[0] in comp_set)!=(e[1] in comp_set)]
          prev={p:None};queue=deque([p])
          while queue and elder_peak not in prev:
            i=queue.popleft()
            for j,eid in sorted(adj[i]):
              if weights[eid]>=w and j not in prev:prev[j]=i;queue.append(j)
          assert elder_peak in prev
          path=[elder_peak]
          while path[-1]!=p:path.append(prev[path[-1]])
          path.reverse();lookup={e:weights[k] for k,e in enumerate(edges)}
          death_edges=[sorted((a,b)) for a,b in zip(path,path[1:]) if lookup[tuple(sorted((a,b)))]==w]
          assert death_edges
          bars.append(dict(peak=p,elder=elder_peak,birth=birth[p],death=w,relative=(birth[p]-w)/w,component=comp,cut=cut,path=path,death_edges=death_edges))
        united=set().union(*(members[r] for r in group))
        for r in group:par[r]=elder
        members[elder]=united
    assert len({find(i) for i in range(len(X))})==1
    return dict(nodes=X,edges=edges,births=birth,edge_minima=weights,bars=bars)

def audit(data):
    scale=int(data['scale']);source=[tuple(map(int,p)) for p in data['rows']];n=data.get('n')
    P,used,faces,eq,edges,owners,adj,fa=complex_hull(source)
    V,c=mass(P,faces);origin=tuple(F(sum(p[j] for p in P),len(P)) for j in range(3));V2,c2=mass(P,faces,origin)
    assert V==V2 and c==c2
    L=math.lcm(*(x.denominator for x in c));C=tuple(int(x*L) for x in c);X=[sub(mul(L,p),C) for p in P]
    supports=[L*h-dot(n,C) for *n,h in eq];assert min(supports)>0
    normals=[q[:3] for q in eq];q=[tuple(F(v,h) for v in nn) for nn,h in zip(normals,supports)]
    strict={'S':[],'U':[],'H':[]};weak={'S':[],'U':[],'H':[]};zeros={'S':0,'U':0,'H':0}
    for i,x in enumerate(X):
      vals=[dot(x,sub(X[j],x)) for j in adj[i]];zeros['U']+=sum(v==0 for v in vals)
      if max(vals)<0:strict['U'].append(i)
      elif max(vals)==0:weak['U'].append(i)
    for f,nn in enumerate(normals):
      vals=[dot(nn,normals[g])*supports[f]-dot(nn,nn)*supports[g] for g in fa[f]];zeros['S']+=sum(v==0 for v in vals)
      if max(vals)<0:strict['S'].append(f)
      elif max(vals)==0:weak['S'].append(f)
      # Independent actual facet-foot polygon inclusion calculation.
      foot=[];cyc=faces[f];norm2=dot(nn,nn)
      for a,b in zip(cyc,cyc[1:]+cyc[:1]):
        foot.append(dot(cross(sub(X[b],X[a]),sub(mul(supports[f],nn),mul(norm2,X[a]))),nn))
      assert (min(foot)>0)==(f in strict['S'])
      assert (min(foot)==0)==(f in weak['S'])
    for a,b in edges:
      d=sub(X[b],X[a]);dd=dot(d,d);ad=dot(X[a],d);rnum=sub(mul(dd,X[a]),mul(ad,d))
      f,g=[v[0] for v in owners[(a,b)]];nf,ng=normals[f],normals[g];aa=dot(nf,nf);bb=dot(ng,ng);ab=dot(nf,ng);D=aa*bb-ab*ab;assert D>0
      A=dot(rnum,nf)*bb-dot(rnum,ng)*ab;B=dot(rnum,ng)*aa-dot(rnum,nf)*ab
      assert mul(D,rnum)==add(mul(A,nf),mul(B,ng))
      vals=[-ad,dd+ad,A,B];zeros['H']+=sum(v==0 for v in vals)
      if min(vals)>0:strict['H'].append([a,b])
      elif min(vals)==0:weak['H'].append([a,b])
    if not any(weak.values()):assert len(strict['S'])+len(strict['U'])-len(strict['H'])==2
    dualedges=sorted({tuple(sorted(v[0] for v in owners[e])) for e in edges})
    PS=landscape(X,edges);QS=landscape(q,dualedges)
    assert len(PS['bars'])==len(strict['U'])-1 if not any(weak.values()) else True
    assert len(QS['bars'])==len(strict['S'])-1 if not any(weak.values()) else True
    tree=None
    if n is not None:
      # Source-indexed chains remain valid even if some inputs are non-extreme.
      Y=[sub(mul(L,p),C) for p in source];arrows=[]
      for side in range(2):
        for i in range(n):
          a=side*n+i;b=a+1 if i<n-1 else 2*n;arrows.append((a,b))
      for a in range(2*n+1,len(Y)):
        b=max(range(2*n+1),key=lambda b:dot(Y[a],sub(Y[b],Y[a])));arrows.append((a,b))
      dots=[dot(Y[a],sub(Y[b],Y[a])) for a,b in arrows]
      cos2=[F(v*v,dot(Y[a],Y[a])*dot(sub(Y[b],Y[a]),sub(Y[b],Y[a]))) for v,(a,b) in zip(dots,arrows)]
      low=None;high=None;impossible=False
      for a,b in arrows:
        d=sub(source[b],source[a]);val=dot(source[a],d);dy=d[1]
        if dy>0:high=min(high,F(val,dy)) if high is not None else F(val,dy)
        elif dy<0:low=max(low,F(val,dy)) if low is not None else F(val,dy)
        elif val<=0:impossible=True
      tree=dict(source_arrows=arrows,all_actual_positive=min(dots)>0,minimum_actual_integer_dot=min(dots),minimum_positive_cosine_squared=min(cos2) if min(dots)>0 else None,root_source=2*n,root_canonical=used.index(2*n) if 2*n in used else None,axis_interval_raw=[low,high],axis_interval_empty=impossible or (low is not None and high is not None and low>=high),actual_raw_centroid_y=c[1])
    return enc(dict(identity=data['identity'],scale=scale,source_rows=source,extreme_source_indices=used,
      V=len(P),E=len(edges),F=len(faces),C=2*len(edges),facets=faces,raw_support_planes=eq,edges=edges,
      actual_volume=V/scale**3,actual_centroid=tuple(v/scale for v in c),centred_integer_multiplier=L,centred_integer_offset=C,
      strict=strict,additional_weak=weak,primitive_zero_counts=zeros,physical_landscape=PS,polar_landscape=QS,tree=tree,
      markers=['EXHAUSTIVE_MAXIMAL_HULL_PASS','EXACT_TWO_ORIGIN_MASS_PASS','STRICT_WEAK_FULL_S_U_H_PASS','SIMULTANEOUS_LEVEL_P_Q_PASS']))

def main():
    p=Path(sys.argv[1]);data=json.loads(p.read_text());out=Path(sys.argv[2]) if len(sys.argv)>2 else p.with_suffix('.audit.json')
    result=audit(data);raw=(json.dumps(result,sort_keys=True,indent=2)+'\n').encode();out.write_bytes(raw)
    print(result['identity'],[result[x] for x in ['V','E','F','C']],{k:len(v) for k,v in result['strict'].items()},
      {k:len(v) for k,v in result['additional_weak'].items()},result['primitive_zero_counts'],
      'P',len(result['physical_landscape']['bars']),'Q',len(result['polar_landscape']['bars']),
      'TREE',result['tree']['all_actual_positive'] if result['tree'] else None,flush=True)
    print(out.name,len(raw),hashlib.sha256(raw).hexdigest(),flush=True)
    print('EXACT_C2_CONSTRUCTION_AUDIT_PASS',flush=True)
if __name__=='__main__':main()
