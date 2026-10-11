# material-d39feff62a40

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# W51 reference geometry: root-sensitive exclusion and a simple exact free110 point

This result does NOT construct the requested homogeneous own110 figure. The physical body is the unchanged literal W51_ROBUST_G3, V31/E87/F58,C174, own211, additional weak000 and primitive000. Its actual uniform centroid and volume remain those corrected in [internal-source-reference]. The exact input is independently supplied here; this capsule needs only exact_audit.py from [internal-source-reference], not FULL76 or a sandbox.

## Exact scientific findings
1. At the prescribed rational reference c=(4/5,11/10,-3/20), this SAME physical body has strict110, additional weak000, primitive000, P0/Q0. U is input vertex0; S is canonical facet2, vertex cycle[4,28,16]. This is a free-reference/nonhomogeneous equilibrium fact, NOT its uniform centre of mass. The same census also holds at (39/50,11/10,-4/25), (79/100,109/100,-13/100), and (4/5,109/100,-13/100), checked rationally. The first point alone suffices for reconstruction.
2. For retained roots U0 and S3=[4,31,30], the entire interior-reference strict110 problem is exactly infeasible. A five-node rational disjunctive cover proves this, not a numerical LP or one frozen witness assignment. The forced unresolved groups are S41=[10,30,31], S53=[10,29,30], U31, S50=[10,28,29], then U5 has no possible escape witness. The selected plane IDs in the literal generated certificate are357,393,228,384; leaf U5 planes83..86 all have strictly negative maximum slack.
3. The alternate retained pair U0/S53 is also exactly excluded, in four nodes. These exclusions DO NOT apply to other root pairs: the explicit free110 point above demonstrates the importance of changing the stable root.
4. An exploratory exact sweep of U0 with S0 through S42 completed43 cases:21 free-reference110 cases and22 exact exclusions. It was stopped there because positive cells, not an all-root exclusion, had been found. No claim concerning all1798 possible root pairs is made. The two endpoint facts above and the default five-node exclusion are the principal reusable outputs; the full sweep can be reconstructed by invoking Search for the stated43 pairs, with the literal input.

## Why the cover is exact
All coordinates of the variable reference C are in the input's integer-grid units. The body inequalities are strict in the interior. For a primal vertex i and adjacent j with e=p_j-p_i, escape is e.C<p_i.e. Its negation is the strict-U root inequality. For a facet i with normal n, offset h, and adjacent facet m,k, define A=(n.n)m-(n.m)n and b=(n.n)k-(n.m)h. A polar escape is A.C>b; strict stability of the retained primal facet uses A.C<b for all adjacent facets. These formulas use positive support distances and the actual polar at C.

The search clips a bounded rational three-dimensional polytope, enumerating exact vertices and active planes. An edge joins two vertices whose common active normals have rank at least2. Every crossing intersection is rational. Lower-dimensional closed cells have no strict feasible point and are rejected. For each nonroot, ALL adjacent escape choices are retained as a disjunction. A witness positive throughout the cell interior covers its group; a witness with nonpositive maximum is impossible. The remaining choices are explicitly branched until a group is impossible or all groups hold. At a successful full-dimensional cell, averaging its vertices gives an exact strict point. This is complete for the stated roots when status is chosen_root_strict110_excluded. An interrupted/limited search is labelled incomplete. Neither strict110 nor no-weak conclusions are inferred from a tolerance.

## Reproduction
Save exact_reference_cells.py and reference_audit.py from the full sources below, plus exact_audit.py from [internal-source-reference]. Save the following exact compact JSON lines, each with final LF:

W51_ROBUST_G3.json (565bytes, SHA256 6fc87990d1c2eff68da3297b39ad3ea51df64ceb78978bd69870fca14e86b414):
```json
{"denominator":1000,"name":"W51_ROBUST_G3","points":[[-2678,-1136,975],[-2745,-769,406],[-2212,-627,45],[96,-637,-245],[465,1184,-402],[80,119,-1160],[294,781,-935],[157,537,-1075],[311,1098,-580],[681,814,-815],[565,-379,-1032],[883,11,-962],[947,461,-856],[1007,793,-634],[840,1037,-473],[1206,848,-369],[1174,1065,103],[1389,818,-95],[1535,736,189],[1603,668,465],[1571,172,-108],[1639,563,721],[1644,425,972],[1609,244,1244],[1506,4,1547],[1301,-295,1859],[970,-604,2131],[548,-896,2304],[78,-1126,2365],[-418,-1288,2323],[-968,-1386,2170],[-1604,-1391,1853]]}
```
W51_free_reference_simple.json (38bytes, SHA256 3f43b54863463c48db97e6bb8af2c0aab37091e37a8473075af51e62f0621d37):
```json
{"reference":["4/5","11/10","-3/20"]}
```
Commands, Python3.13.5 standard library only:
```sh
python -B -S reference_audit.py W51_ROBUST_G3.json W51_free_reference_simple.json W51_free_reference_simple.audit.json
python -B -S exact_reference_cells.py W51_ROBUST_G3.json W51_reference_cover.json 1000000000
python -B -S exact_reference_cells.py W51_ROBUST_G3.json W51_reference_u0_s53.json 1000000000 0 53
```
Expected markers:
```text
REFERENCE_EXACT_AUDIT_PASS W51_ROBUST_G3 [1, 1, 0] [0, 0, 0] [0, 0, 0] own [2, 1, 1] is_own False
EXACT_REFERENCE_COVER chosen_root_strict110_excluded nodes 5 initial vertices 26
EXACT_REFERENCE_COVER chosen_root_strict110_excluded nodes 4 initial vertices 16
```
Output identities: W51_free_reference_simple.audit.json715bytes SHA dba5d9707da091bb8de8af6eb75fe41d8137dfeda00e13486093b3198dedd844; W51_reference_cover.json19073bytes SHA2fbede87389a837489387e0f40441e93e5c0e57a24aa7fe2e2853dd322317e7e; W51_reference_u0_s53.json18799bytes SHA a42482d86367384b6b4a0a9e4d62c6d9ca381d7405c949815c3f788e9ded30be. Timing is not in these canonical files.

## exact_reference_cells.py
6970bytes, SHA25615ec3c12cb4764e00e2fe03c12962a5c2259179cd10746d435fc192e879385d6. UTF-8/LF/final newline.
```python
"""Exact chosen-root strict110 reference-cell cover search in dimension three.
Requires exact_audit.py. A free reference point is NOT a homogeneous COM.
Finite incomplete searches are labelled incomplete, never global exclusions.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import gcd
from pathlib import Path
import json,sys,time
from exact_audit import audit,dot,sub,mul,add,cross,det

class Search:
    def __init__(self,data,seconds=20,limit=3000,root_u=None,root_s=None,preaudit=None):
        self.data=data;self.a=preaudit if preaudit is not None else audit(data['points'],data['denominator']);self.p=[tuple(row) for row in data['points']];self.planes=[];self.registry={};self.tree=[];self.start=time.monotonic();self.seconds=seconds;self.limit=limit;self.cache={};self.found=None
        self.ff=self.a['facets'];self.ids=[self.register(tuple(f['normal']),f['offset']) for f in self.ff]
        c=tuple(F(x)*data['denominator'] for x in self.a['centroid']);q=[mul(1/(F(f['offset'])-dot(f['normal'],c)),tuple(f['normal'])) for f in self.ff]
        self.sr=max(range(len(q)),key=lambda i:dot(q[i],q[i]));self.ur=max(self.a['vertices'],key=lambda i:dot(sub(self.p[i],c),sub(self.p[i],c)))
        if root_u is not None:self.ur=root_u
        if root_s is not None:self.sr=root_s
        if self.ur not in self.a['vertices'] or self.sr not in range(len(self.ff)):raise ValueError('Invalid retained root')
        nb={i:[] for i in self.a['vertices']};fn={i:[] for i in range(len(self.ff))}
        for e in self.a['edges']:
            i,j=e['vertices'];a,b=e['owners'];nb[i].append(j);nb[j].append(i);fn[a].append(b);fn[b].append(a)
        self.groups=[];self.roots=[]
        for i in self.a['vertices']:
            hs=[]
            for j in sorted(nb[i]):
                e=sub(self.p[j],self.p[i]);A=e;b=dot(self.p[i],e)
                hs.append(self.register(mul(-1,A),-b) if i==self.ur else self.register(A,b))
            if i==self.ur:self.roots+=hs
            else:self.groups.append(('U_'+str(i),hs))
        for i in range(len(self.ff)):
            hs=[];n=tuple(self.ff[i]['normal']);h=self.ff[i]['offset'];nn=dot(n,n)
            for j in sorted(fn[i]):
                m=tuple(self.ff[j]['normal']);k=self.ff[j]['offset'];nm=dot(n,m);A=sub(mul(nn,m),mul(nm,n));b=nn*k-nm*h
                hs.append(self.register(A,b) if i==self.sr else self.register(mul(-1,A),-b))
            if i==self.sr:self.roots+=hs
            else:self.groups.append(('S_'+str(i),hs))
    def register(self,A,b):
        g=gcd(*A,b);key=tuple(int(x//g) for x in (*A,b))
        if key not in self.registry:self.registry[key]=len(self.planes);self.planes.append((key[:3],key[3]))
        return self.registry[key]
    def slack(self,h,v):
        A,b=self.planes[h];return b-dot(A,v)
    def rank3(self,points):
        if len(points)<4:return False
        p=points[0];d1=next((sub(v,p) for v in points[1:] if v!=p),None)
        if d1 is None:return False
        d2=next((sub(v,p) for v in points[1:] if cross(d1,sub(v,p))!=(0,0,0)),None)
        if d2 is None:return False
        return any(det(d1,d2,sub(v,p))!=0 for v in points[1:])
    def clip(self,poly,h):
        points=list(poly);ss=[self.slack(h,v) for v in points]
        if max(ss)<=0:return None
        out={v:(active|{h} if s==0 else active) for v,active,s in zip(points,poly.values(),ss) if s>=0}
        for i in range(len(points)):
            for j in range(i):
                if ss[i]*ss[j]>=0:continue
                shared=poly[points[i]]&poly[points[j]]
                if len(shared)<2:continue
                normals=[self.planes[k][0] for k in shared]
                if not any(cross(normals[0],n)!=(0,0,0) for n in normals[1:]):continue
                t=ss[i]/(ss[i]-ss[j]);v=add(points[i],mul(t,sub(points[j],points[i])))
                out[v]=out.get(v,frozenset())|shared|{h}
        return out if self.rank3(list(out)) else None
    def visit(self,poly,depth=0):
        if len(self.tree)>=self.limit or time.monotonic()-self.start>self.seconds:raise TimeoutError('finite search bound')
        key=tuple(sorted(poly));node=len(self.tree);self.tree.append(dict(id=node,depth=depth,vertices=len(poly)))
        if key in self.cache:self.tree[node]['cached']=self.cache[key];return False
        options=[]
        for name,hs in self.groups:
            ranges=[(h,min(self.slack(h,v) for v in poly),max(self.slack(h,v) for v in poly)) for h in hs]
            if any(lo>=0 and hi>0 for h,lo,hi in ranges):continue
            possible=[(h,lo,hi) for h,lo,hi in ranges if hi>0]
            if not possible:
                self.tree[node].update(blocked=name,bounds=[dict(plane=h,min=str(lo),max=str(hi)) for h,lo,hi in ranges]);self.cache[key]=node;return False
            options.append((len(possible),sum(hi/(hi-lo) for h,lo,hi in possible),name,possible))
        if not options:
            n=len(poly);c=tuple(sum(v[k] for v in poly)/n for k in range(3));self.found=c;self.tree[node]['free_reference']=[str(x/self.data['denominator']) for x in c];return True
        _,_,name,possible=min(options);self.tree[node].update(split=name,children=[])
        for h,lo,hi in possible:
            child=self.clip(poly,h)
            if child is None:self.tree[node]['children'].append(dict(plane=h,empty_interior=True));continue
            self.tree[node]['children'].append(dict(plane=h,node=len(self.tree)))
            if self.visit(child,depth+1):return True
        self.cache[key]=node;return False
    def run(self):
        poly={tuple(F(x) for x in self.p[i]):frozenset(h for h in self.ids if self.slack(h,self.p[i])==0) for i in self.a['vertices']}
        for h in self.roots:
            poly=self.clip(poly,h)
            if poly is None:break
        initial=len(poly) if poly else 0
        try:found=self.visit(poly) if poly else False;status='free_reference_found' if found else 'chosen_root_strict110_excluded'
        except TimeoutError:status='incomplete'
        return dict(name=self.data.get('name'),status=status,root_U=self.ur,root_S=self.sr,root_S_vertices=self.ff[self.sr]['vertices'],initial_vertices=initial,nodes=len(self.tree),reference=[str(x/self.data['denominator']) for x in self.found] if self.found else None,planes=[dict(A=list(A),b=b) for A,b in self.planes],tree=self.tree,own_strict=self.a['strict'],scope='Only the fixed literal body, retained U/S roots, and free reference location; not own110, not other root pairs, not deformed bodies.')
if __name__=='__main__':
    data=json.load(open(sys.argv[1]));s=Search(data,float(sys.argv[3]) if len(sys.argv)>3 else 20,root_u=int(sys.argv[4]) if len(sys.argv)>4 else None,root_s=int(sys.argv[5]) if len(sys.argv)>5 else None);result=s.run();Path(sys.argv[2]).write_text(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n');print('EXACT_REFERENCE_COVER',result['status'],'nodes',result['nodes'],'initial vertices',result['initial_vertices'])
```

## reference_audit.py
3088bytes, SHA256 cc9ccad36da7d80f11bf736bb7186bf75f2a7e1660c1e219f1345413b6fef589. UTF-8/LF/final newline.
```python
"""Exact S/U/H and persistence at an explicitly prescribed reference, not own COM.
Requires exact_audit.py. Standard library only, all decisions rational and unfiltered.
Run: python -B -S reference_audit.py INPUT.json REFERENCE.json OUTPUT.json
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys
from exact_audit import audit,add,sub,mul,dot,cross,persistence

def reference_audit(data,reference):
    a=audit(data['points'],data['denominator']);D=data['denominator'];p=[tuple(F(t,D) for t in row) for row in data['points']];c=tuple(F(v) for v in reference);x=[sub(v,c) for v in p];ff=a['facets'];edges=a['edges'];strict=[[],[],[]];weak=[[],[],[]];zero=[0,0,0];q=[];nb={i:set() for i in a['vertices']}
    for i,f in enumerate(ff):
        n=tuple(f['normal']);height=F(f['offset'],D)-dot(n,c)
        if height<=0:raise ValueError('Reference is not strictly inside the body')
        q.append(mul(1/height,n));cycle=f['vertices'];vals=[-dot(cross(n,sub(p[j],p[k])),x[k]) for k,j in zip(cycle,cycle[1:]+cycle[:1])];zero[0]+=vals.count(0)
        if min(vals)>0:strict[0].append(i)
        elif min(vals)>=0:weak[0].append(i)
    for e in edges:
        i,j=e['vertices'];nb[i].add(j);nb[j].add(i);d=sub(p[j],p[i]);dd=dot(d,d);z=dot(x[i],d);n,m=(tuple(ff[k]['normal']) for k in e['owners']);nn=dot(n,n);mm=dot(m,m);nm=dot(n,m);vals=[-z,dd+z,mm*dot(n,x[i])-nm*dot(m,x[i]),nn*dot(m,x[i])-nm*dot(n,x[i])];zero[2]+=vals.count(0)
        if min(vals)>0:strict[2].append([i,j])
        elif min(vals)>=0:weak[2].append([i,j])
    for i in nb:
        vals=[-dot(x[i],sub(p[j],p[i])) for j in nb[i]];zero[1]+=vals.count(0)
        if min(vals)>0:strict[1].append(i)
        elif min(vals)>=0:weak[1].append(i)
    mp={v:i for i,v in enumerate(a['vertices'])};P=persistence([x[v] for v in a['vertices']],[(mp[e['vertices'][0]],mp[e['vertices'][1]]) for e in edges]);Q=persistence(q,[tuple(e['owners']) for e in edges]);ss=list(map(len,strict));ww=list(map(len,weak))
    if not any(ww):assert ss[0]+ss[1]-ss[2]==2 and len(P)==ss[1]-1 and len(Q)==ss[0]-1
    return dict(name=data.get('name'),reference=[str(v) for v in c],V=a['V'],E=a['E'],F=a['F'],C=a['C'],strict=ss,additional_weak=ww,primitive_zero=zero,strict_ids=strict,weak_ids=weak,P=P,Q=Q,own_strict=a['strict'],own_additional_weak=a['additional_weak'],own_centroid=a['centroid'],reference_is_own_centroid=all(F(v)==w for v,w in zip(a['centroid'],c)),scope='Prescribed-reference audit; this is not an own homogeneous equilibrium claim unless reference_is_own_centroid is true.')
if __name__=='__main__':
    source=Path(sys.argv[1]).read_bytes();ref=Path(sys.argv[2]).read_bytes();r=reference_audit(json.loads(source),json.loads(ref)['reference']);r['input_sha256']=hashlib.sha256(source).hexdigest();r['reference_sha256']=hashlib.sha256(ref).hexdigest();Path(sys.argv[3]).write_text(json.dumps(r,sort_keys=True,separators=(',',':'))+'\n');print('REFERENCE_EXACT_AUDIT_PASS',r['name'],r['strict'],r['additional_weak'],r['primitive_zero'],'own',r['own_strict'],'is_own',r['reference_is_own_centroid'])
```

Original literal coordinate source: figure-0537, SHA05577e4a0b36b334bf63e1fd41ffdbb8b9c663892f7da776c851bf47acf7af21. The exact audit dependency and this material suffice for every principal claim above. The numerical mass-homotopy experiments are separate and are not promoted by this reference-only certificate.
