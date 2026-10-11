# material-edbe5555a5e8

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# J98 exact four-point cover and finite one-step mass-capacity obstruction

Required complete dependency: J98_EXACT_GEOMETRY_CORE.md, material [internal-source-reference]. Extract that core and both FILE blocks below together using its complete extractor. No numerical experiment output is needed for the DEFAULT verifier. The literal scientific parent remains figure-0581; the four-point body below is a new, distinct conditional control, not an alias of R82, C434, LOW, or an own110 body.

## Recovery and expected outputs

Run `python -B -S capexact98.py`. Expected final marker: `J98_EXACT_ONE_STEP_ELDER_CAPACITY_OBSTRUCTION_PASS_NOT_110`; intermediate marker: `WHOLE_OLD_JUNIOR_COMPONENT_REMOVED_EXACTLY referenceS 9`. Exact boundary, all inequalities and integrations were run successfully by the coordinator. This is the originating exact computation, not an independent second author verification. `--fraction` uses the standard-library rational fallback and is much slower; default uses the complete GMP adapter from the core. The optional `--nominate` mode belongs to the separately preserved numerical producers and requires GREEDY_COVER98_RESULTS.json plus geom98.py/cover98.py; it is NOT needed to recover or verify this exact result.

Source/input manifest: capexact98.py 10854 bytes SHA 1a47dbff2c409a649564487b306b6efefc0f3b4a3cf87a67ea20eb1e4c22d9c3; CAPEXACT98_INPUT.json 8295 bytes SHA 79820cee41fbf3c524386bd86f1be4ce455923f713f8c3372794160ce7c8c1ae. Reproduced output CAPEXACT98_CERTIFICATE.json 2850 bytes SHA c08e0a4145dc5927fd37efe1be327ab7784c57a77bb3ed3ff2c411fb126e4478. All source/input bytes follow literally. Output is deterministic under the observed Python3.13.5/GMP environment.

## What was proved

B is the convex hull of all original R82 vertices and the four raw points in CAPEXACT98_INPUT.json, divided by 10^8. Its exact maximal boundary is V128/E231/F105, C462. Every new point has an exact positive radial escape chord to its specified old witness at the ORIGINAL uniform centroid c. The complete old junior support-sublevel component at r=6339/10000 is empty in B, certified by classifying ALL new polar vertices, not by a direction sample. Nevertheless B has exact reference S9 and U1 at c: removal of one old component at one level does not prevent new minima at higher levels. The full OWN strict/weak census was not certified by this capsule and is not claimed. B's exact own-volume interval is (1972126536549,1972126536550)/10^12; its actual own-centroid shift is x in(-50417416771,-50417416770)/10^12, y in(4130038085,4130038086)/10^12, z in(68748521960,68748521961)/10^12. Physical mass is not closed.

Let Omega be the exact 33-plane outer body constructed below. It contains the convex hull of ALL old one-step diameter witness balls, intersected with the unchanged old elder H18 halfspace. Every number of old one-step-safe added controllers preserving that halfspace lies in Omega. For w=(-590685,48387,805450)/10^6 and D={x:w dot(x-c)<=0}, write J(T)=integral_T w dot(x-c) dx. Every measurable filled L with B subset L subset Omega satisfies
J(L)>=J(B)+J(Omega intersect D)-J(B intersect D)=gamma.
This takes ALL available negative shell moment and discards all positive shell moment, so it is a generous relaxation that does not assume a fixed controller count or even convexity of the additional material. Exact integration gives J(B) in(168329182229,168329182230)/10^12, available negative moment at most a value in(155453283224,155453283225)/10^12, and gamma in(12875899004,12875899005)/10^12>0. Omega volume is in(3432879053712,3432879053713)/10^12. Therefore w dot(g_L-c)>=gamma/Vol(Omega)>0.003750758125. Such controllers cannot restore c for THIS literal primary patch.

The gap is a global finite-capacity exclusion inside this specified envelope, not a failed optimizer, a Jacobian rank defect, or a general U1 exclusion. New-to-new chains, another primary covering patch, lifting/replacing the elder support, cuts, changed old geometry and unrestricted centre changes are not excluded. A subsequent J98 release certificate weakens the elder guard to allow a substantial lift; its separate input and proof must be read before using that stronger result.

### FILE capexact98.py
```python
"""Exact directional capacity obstruction for a literal four-apex R82 cover.
Standard-library verification from literal geometry nominations. --nominate uses
NumPy/SciPy only to propose boundary incidences; every incidence is checked exactly.
The conclusion is conditional on the original one-step witness envelope and on
preserving original elder support18; it is not an exclusion of general U1 extension.
"""
from __future__ import annotations
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
from collections import deque
from itertools import combinations
import json,sys,hashlib
from exact98 import dot,add,sub,mul,cross,det,meet,interval,edge_min
if '--fraction'not in sys.argv:
    from gmpq98 import Q as F
    import exact98
    exact98.F=F

def integral(v,faces):
    W=F(0);T=(F(0),)*3
    for f in faces:
        for j in range(1,len(f)-1):
            a,b,c=(v[k]for k in (f[0],f[j],f[j+1]));ww=det(a,b,c)
            W+=ww;T=add(T,mul(ww,add(add(a,b),c)))
    assert W>0
    return W/6,mul(F(1,24),T)

def validate(v,faces,H=None):
    E={};HH=[];active=set()
    for k,f in enumerate(faces):
        assert len(f)==len(set(f))>=3
        if H is None:
            a,b,c=(v[j]for j in f[:3]);n=cross(sub(b,a),sub(c,a));h=dot(n,a)
        else:n,h=H[k]
        assert dot(n,n)>0
        tight=[]
        for j,x in enumerate(v):
            z=dot(n,x)-h;assert z<=0,(k,j,'outside')
            if z==0:tight.append(j)
        assert set(tight)==set(f),(k,'facet incomplete')
        if H is not None:
            hn,hh=H[k]
            assert cross(n,hn)==(0,0,0) and dot(n,hn)>0
            assert all(dot(hn,v[j])==hh for j in f)
        for j,a in enumerate(f):
            b=f[(j+1)%len(f)]
            for c in f:
                if c not in (a,b):assert dot(n,cross(sub(v[b],v[a]),sub(v[c],v[a])))>0
            E.setdefault(tuple(sorted((a,b))),[]).append((a,b));active.add(a)
        HH.append((n,h))
    for x in E.values():assert len(x)==2 and x[0]==tuple(reversed(x[1]))
    assert len(active)-len(E)+len(faces)==2
    graph={j:set()for j in active}
    for a,b in E:graph[a].add(b);graph[b].add(a)
    seen={next(iter(active))};todo=deque(seen)
    while todo:
        for b in graph[todo.popleft()]:
            if b not in seen:seen.add(b);todo.append(b)
    assert seen==active
    return HH,len(active),len(E)

def solve3(rows,offs):
    a,b,c=rows;A,B,C=offs;den=det(a,b,c)
    assert den
    return mul(1/den,add(add(mul(A,cross(b,c)),mul(B,cross(c,a))),mul(C,cross(a,b))))

def checked_h(H,spec):
    v=[]
    for ii in spec['incident']:
        chosen=None
        for tr in combinations(ii,3):
            rows=[H[k][0]for k in tr]
            if det(*rows)!=0:chosen=tr;break
        assert chosen is not None
        x=solve3([H[k][0]for k in chosen],[H[k][1]for k in chosen]);tight=[]
        for k,(n,h)in enumerate(H):
            z=dot(n,x)-h;assert z<=0
            if z==0:tight.append(k)
        assert tight==ii
        v.append(x)
    act=spec['active'];faces=spec['faces']
    print('CHECKED_H_VERTICES',len(v),'FACETS',len(faces),flush=True)
    validate(v,faces,[H[k]for k in act])
    print('CHECKED_H_BOUNDARY',len(v),flush=True)
    # Every unlisted H row is redundant on this exactly closed convex boundary;
    # listed facets are actual rows of the input system, proving equality of bodies.
    V,M=integral(v,faces)
    return v,V,M

def nominate_h(H,inside):
    import numpy as np
    from scipy.spatial import HalfspaceIntersection
    rows=np.array([[float(z)for z in n]+[-float(h)]for n,h in H]);scale=np.linalg.norm(rows[:,:3],axis=1);rows/=scale[:,None]
    hs=HalfspaceIntersection(rows,np.array([float(x)for x in inside]));v=hs.intersections
    ii=[sorted(f)for f in hs.dual_facets];faces=[];active=[]
    for k,(n,h)in enumerate(H):
        ids=[j for j,z in enumerate(ii)if k in z]
        if len(ids)<3:continue
        pp=v[ids];c=pp.mean(axis=0);nn=rows[k,:3];a=pp[0]-c;a/=np.linalg.norm(a);b=np.cross(nn,a)
        ids=np.array(ids)[np.argsort(np.arctan2((pp-c)@b,(pp-c)@a))].tolist();faces.append(ids);active.append(k)
    return {'incident':ii,'faces':faces,'active':active}

def main(root,nominate=False):
    raw=(root/'KH93_C434_R82_G6.txt').read_bytes();assert hashlib.sha256(raw).hexdigest()=='9765712b5ffaa464ed4d677974256294c6d867b77fe77b930d166853f66a92a7'
    lines=raw.decode().splitlines();N,D=map(int,lines[0].split());A=[tuple(map(int,l.split()))for l in lines[1:]]
    lat=json.loads((root/'R82_LATTICE98.json').read_text());v=[meet(*(A[k]for k in ii),D)for ii in lat['incident_supports']]
    validate(v,lat['faces'],[(a,F(D))for a in A]);VK,MK=integral(v,lat['faces']);g=mul(1/VK,MK);p=[sub(x,g)for x in v]
    print('PARENT_EXACT_GEOMETRY_AND_MASS',flush=True)
    if nominate:
        import numpy as np
        from geom98 import hull_v
        from cover98 import fibonacci_sphere
        source=json.loads((root/'GREEDY_COVER98_RESULTS.json').read_text());rec=next(z for z in source if z['t']==.35 and z['extra']==.02)
        gf=np.array([float(x)for x in g]);ap=np.rint((np.array(rec['apices_centered'])+gf)*10**8).astype(np.int64)
        vv=np.r_[np.array([[float(x)for x in z]for z in v]),ap/10**8];bf=hull_v(vv)['faces']
        spec={'primary_apices_raw_grid8':ap.tolist(),'primary_witness_indices':rec['witnesses'],'primary_faces':bf,
              'outer_directions_grid6':np.rint(fibonacci_sphere(32)*10**6).astype(np.int64).tolist(),'w_grid6':[-590685,48387,805450]}
    else:spec=json.loads((root/'CAPEXACT98_INPUT.json').read_text())
    ap=[tuple(F(int(z),10**8)for z in x)for x in spec['primary_apices_raw_grid8']];vv=v+ap
    for x,wi in zip(ap,spec['primary_witness_indices']):assert dot(sub(x,g),sub(v[wi],x))>0
    BH,bnv,bne=validate(vv,spec['primary_faces']);VB,MB=integral(vv,spec['primary_faces'])
    print('PRIMARY_EXACT',bnv,bne,len(BH),flush=True)
    # Finite exact test of the WHOLE old junior component, not a direction sample.
    py=[mul(F(1,D),a)for a in A];pq=[mul(1/(1-dot(a,g)),a)for a in py]
    ef={}
    for fi,f in enumerate(lat['faces']):
        for j,a in enumerate(f):ef.setdefault(tuple(sorted((a,f[(j+1)%len(f)]))),[]).append(fi)
    r=F(6339,10000);level=1/r**2;adj=[[]for _ in pq]
    for i,j in ef.values():
        if edge_min(pq[i],pq[j])>level:adj[i].append(j);adj[j].append(i)
    component={7};todo=deque([7])
    while todo:
        for z in adj[todo.popleft()]:
            if z not in component:component.add(z);todo.append(z)
    assert 18 not in component
    bq=[mul(1/(hh-dot(n,g)),n)for n,hh in BH];survivors=[]
    for k,(n,hh)in enumerate(BH):
        if dot(bq[k],bq[k])<=level:continue
        source=max(range(len(v)),key=lambda j:dot(n,v[j]))
        ff=lat['incident_supports'][source]
        corner=max(ff,key=lambda j:dot(n,pq[j]))
        if corner in component:survivors.append(k)
    assert not survivors
    bef={}
    for fi,f in enumerate(spec['primary_faces']):
        for j,a in enumerate(f):bef.setdefault(tuple(sorted((a,f[(j+1)%len(f)]))),[]).append(fi)
    bouts=[[]for _ in bq]
    for i,j in bef.values():
        bouts[i].append(dot(bq[i],sub(bq[j],bq[i])))
        bouts[j].append(dot(bq[j],sub(bq[i],bq[j])))
    refS=[i for i,outs in enumerate(bouts)if max(outs)<0]
    ref_polar_zeros=sum(z==0 for outs in bouts for z in outs)
    print('WHOLE_OLD_JUNIOR_COMPONENT_REMOVED_EXACTLY','referenceS',len(refS),flush=True)
    w=tuple(F(z,10**6)for z in spec['w_grid6']);wg=dot(w,g);cut=(w,wg)
    JB=dot(w,sub(MB,mul(VB,g)))
    rup=[]
    for x in p:
        r2=dot(x,x);k=isqrt(r2.numerator*10**12//r2.denominator)+1;rr=F(k,10**6);assert rr*rr>r2;rup.append(rr)
    OH=[]
    for aa in spec['outer_directions_grid6']:
        n=tuple(F(z,10**6)for z in aa);nu=F(isqrt(sum(z*z for z in aa))+1,10**6);assert nu*nu>dot(n,n)
        support=(max(dot(n,x)+nu*rr for x,rr in zip(v,rup))+dot(n,g))/2
        OH.append((n,support))
    # The preserved elder support is the literal old H18, independent of centring.
    OH.append((tuple(F(z,D)for z in A[18]),F(1)))
    for x in vv:assert all(dot(n,x)<=h for n,h in OH)
    inner=sub(g,mul(F(1,100),w))
    if nominate:
        spec['omega']=nominate_h(OH,g);spec['omega_negative']=nominate_h(OH+[cut],inner);spec['primary_negative']=nominate_h(BH+[cut],inner)
        (root/'CAPEXACT98_INPUT.json').write_text(json.dumps(spec,separators=(',',':'))+'\n')
        print('EXACT98_CAPACITY_NOMINATIONS_SAVED',flush=True)
    ov,VO,MO=checked_h(OH,spec['omega']);print('OUTER_WHOLE_EXACT',len(ov),flush=True)
    onv,VON,MON=checked_h(OH+[cut],spec['omega_negative']);print('OUTER_NEGATIVE_EXACT',len(onv),flush=True)
    bnv2,VBN,MBN=checked_h(BH+[cut],spec['primary_negative']);print('PRIMARY_NEGATIVE_EXACT',len(bnv2),flush=True)
    JON=dot(w,sub(MON,mul(VON,g)));JBN=dot(w,sub(MBN,mul(VBN,g)));capacity=JBN-JON;gap=JB-capacity
    assert capacity>0 and gap>F(1,100)
    assert dot(w,w)<F(1001,1000)**2
    # Every filled L between primary B and outer Omega obeys J(L)>=gap and Vol(L)<=VO.
    centre_projection_lower=gap/VO
    assert centre_projection_lower>F(1,1000)
    out={'identity':'J98_FOUR_COVER_G8_ONE_STEP_ELDER_MASS_OBSTRUCTION','primary':'R82 plus literal four raw-grid1e8 apices',
         'whole_old_junior_component_removed_at_support_level':str(r),'old_junior_surviving_polar_vertices':survivors,
         'reference_strict_S':len(refS),'reference_strict_U':1,'reference_polar_chord_zeros':ref_polar_zeros,'own_full_equilibrium_census':'not certified by this capsule',
         'primary_V':bnv,'primary_E':bne,'primary_F':len(BH),'primary_volume':interval(VB),'primary_own_centroid_shift':[interval(x)for x in sub(mul(1/VB,MB),g)],
         'direction_grid6':spec['w_grid6'],'outer_plane_count':len(OH),'outer_V':len(ov),'outer_volume':interval(VO),
         'primary_projected_first_moment':interval(JB),'available_negative_moment_upper':interval(capacity),'strict_positive_gap':interval(gap),
         'projected_centroid_shift_strict_lower':interval(centre_projection_lower),
         'scope':'Every measurable filled body L with B subset L subset Omega has positive w-moment relative to the OLD own centroid. Omega contains the entire convex hull of all old diameter witness balls, intersected with the unchanged elder H18 halfspace. Therefore arbitrary many one-step-safe added controls preserving that elder plane cannot restore the OLD centroid for this literal primary B. This does not exclude new-to-new escape chains, release of the elder support, deleting old material, or another primary covering patch.'}
    (root/'CAPEXACT98_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));print('J98_EXACT_ONE_STEP_ELDER_CAPACITY_OBSTRUCTION_PASS_NOT_110')
if __name__=='__main__':main(Path(__file__).parent,'--nominate'in sys.argv)
```
### FILE CAPEXACT98_INPUT.json
```json
{"primary_apices_raw_grid8":[[-71227104,4490850,87329532],[-33724808,-25698269,113145470],[-10809318,70913057,4685390],[-82662642,24347695,-23660729]],"primary_witness_indices":[3,2,148,6],"primary_faces":[[163,1,160],[160,1,14],[163,160,162],[161,12,13],[5,1,163],[160,3,161],[160,14,15],[6,5,163],[163,26,28],[163,25,26],[31,25,163],[150,31,163],[160,137,162],[139,137,160],[140,139,160],[161,3,20],[20,3,160],[161,22,23],[13,9,161],[161,9,11],[28,27,163],[27,6,163],[162,134,135],[162,135,148],[162,151,163],[113,112,161],[161,97,113],[49,8,161],[161,8,96],[90,88,161],[89,49,161],[161,88,89],[136,134,162],[137,136,162],[160,141,142],[142,140,160],[18,12,161],[20,18,161],[121,120,122],[47,38,44],[11,10,161],[161,10,22],[162,148,152],[152,151,162],[163,149,150],[151,149,163],[72,71,161],[112,72,161],[66,65,161],[161,65,160],[160,65,141],[71,69,161],[69,66,161],[161,96,116],[19,18,20],[160,15,19],[160,19,20],[117,97,161],[161,116,117],[91,23,92],[161,23,91],[91,90,161],[81,80,82],[79,77,78],[36,35,37],[157,158,29,30],[17,15,14,16],[57,13,12,60],[94,96,8,49,48],[99,100,58,57,60,59],[102,100,99,101],[52,10,11,9,55,56],[58,55,9,13,57],[56,55,58,100,102],[138,159,148,135,134,136,137,139,140,142,141],[32,31,150,153],[34,32,153,154],[154,155,33,34],[113,97,95,50,71,72,112],[69,71,50,0,138,141,65,66],[44,43,41,42,45,46,47],[51,41,43,0,50,95,94,48,54],[17,59,60,12,18,19,15],[102,101,106,108,51,54,53,52,56],[108,106,107,109],[155,154,153,150,149,151,152,148,159,158,157,156],[30,7,156,157],[155,156,7,33],[116,96,94,95,97,117],[93,53,54,48,49,89],[93,92,23,22,10,52,53],[93,89,88,90,91,92],[80,45,42,77,79,82],[86,84,83,85,87],[99,59,17,16,61,62,107,106,101],[80,81,39,46,45],[85,83,103,104],[103,83,84,78,77,42,41,51,108,109,120,121],[84,86,40,39,81,82,79,78],[36,40,86,87,61,16,14,1,5,6,27,28,26,25,31,32,34,33,7,30,29,35],[109,107,62,105,122,120],[104,105,62,61,87,85],[105,104,103,121,122],[39,40,36,37,38,47,46],[29,158,159,138,0,43,44,38,37,35]],"outer_directions_grid6":[[89883,231181,968750],[-379108,-187051,906250],[515345,-150020,843750],[-324081,533498,781250],[-135224,-681992,718750],[608165,446622,656250],[-799944,86895,593750],[559255,-636402,531250],[18253,883142,468750],[-631028,-660882,406250],[936962,62751,343750],[-749339,599491,281250],[150072,-964172,218750],[547243,822260,156250],[-966597,-238539,93750],[877306,-478912,31250],[-323398,945747,-31250],[-398811,-912229,-93750],[903069,400065,-156250],[-924822,311212,-218750],[463909,-840052,-281250],[220543,912796,-343750],[-758214,-509973,-406250],[873474,-131594,-468750],[-532482,658966,-531250],[-49852,-803104,-593750],[543178,523731,-656250],[-695042,-17757,-718750],[470898,-409760,-781250],[-60565,533308,-843750],[-248560,-341948,-906250],[243064,49428,-968750]],"w_grid6":[-590685,48387,805450],"omega":{"incident":[[19,27,32],[30,31,32],[27,30,32],[29,30,31],[27,29,30],[28,31,32],[23,28,32],[26,29,31],[21,26,29],[26,28,31],[23,26,28],[14,19,32],[6,14,32],[11,14,19],[6,11,14],[7,15,32],[10,15,23],[7,10,15],[8,13,21],[0,5,8],[5,8,13],[8,16,21],[8,11,16],[11,16,19],[16,21,29],[0,3,8],[3,8,11],[3,6,11],[0,1,3],[1,3,6],[10,18,23],[18,23,26],[5,10,18],[5,13,18],[18,21,26],[13,18,21],[6,9,32],[1,9,32],[1,6,9],[0,1,2],[0,2,5],[2,7,10],[2,5,10],[20,23,32],[15,20,32],[15,20,23],[24,27,29],[16,24,29],[19,24,27],[16,19,24],[2,4,7],[1,2,4],[4,7,32],[1,4,32]],"faces":[[39,40,19,25,28],[51,39,28,29,38,37,53],[42,40,39,51,50,41],[29,28,25,26,27],[53,52,50,51],[32,33,20,19,40,42],[27,14,12,36,38,29],[50,52,15,17,41],[25,19,20,18,21,22,26],[38,36,37],[41,17,16,30,32,42],[22,23,13,14,27,26],[35,18,20,33],[14,13,11,12],[16,17,15,44,45],[23,22,21,24,47,49],[33,32,30,31,34,35],[23,49,48,0,11,13],[44,43,45],[35,34,8,24,21,18],[30,16,45,43,6,10,31],[47,46,48,49],[31,10,9,7,8,34],[4,2,0,48,46],[6,5,9,10],[8,7,3,4,46,47,24],[4,3,1,2],[9,5,1,3,7],[52,53,37,36,12,11,0,2,1,5,6,43,44,15]],"active":[0,1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,18,19,20,21,23,24,26,27,28,29,30,31,32]},"omega_negative":{"incident":[[7,10,33],[7,32,33],[8,16,33],[16,24,33],[28,31,32],[23,28,32],[7,15,32],[7,10,15],[10,15,23],[26,28,31],[23,26,28],[5,10,33],[27,32,33],[24,27,33],[20,23,32],[15,20,32],[15,20,23],[26,29,31],[24,27,29],[16,24,29],[8,13,33],[5,13,33],[10,18,23],[18,23,26],[5,10,18],[5,13,18],[16,21,29],[21,26,29],[8,16,21],[8,13,21],[18,21,26],[13,18,21],[27,30,32],[27,29,30],[30,31,32],[29,30,31]],"faces":[[21,11,24,25],[6,7,0,1],[29,28,2,20],[24,11,0,7,8,22],[31,29,20,21,25],[8,7,6,15,16],[3,2,28,26,19],[25,24,22,23,30,31],[15,14,16],[31,30,27,26,28,29],[22,8,16,14,5,10,23],[18,13,3,19],[30,23,10,9,17,27],[33,32,12,13,18],[5,4,9,10],[19,26,27,17,35,33,18],[34,32,33,35],[17,9,4,34,35],[4,5,14,15,6,1,12,32,34],[3,13,12,1,0,11,21,20,2]],"active":[5,7,8,10,13,15,16,18,20,21,23,24,26,27,28,29,30,31,32,33]},"primary_negative":{"incident":[[8,99,105],[79,81,104],[8,9,99],[8,9,105],[86,87,99],[11,44,105],[66,94,99],[66,99,105],[81,83,97],[71,83,90],[9,10,99],[10,11,105],[9,10,105],[65,99,104],[65,86,99],[75,76,99],[10,11,75,99],[77,87,99],[76,77,99],[74,79,104],[64,99,104],[64,99,103],[64,103,104],[39,103,104],[95,98,103],[98,99,103],[80,81,97],[80,92,97],[80,81,104],[39,80,104],[80,92,95],[80,95,103],[39,80,103],[94,99,101],[94,100,101],[67,69,72],[71,73,83],[71,72,73],[69,72,73],[66,82,94],[69,82,94],[67,69,82],[67,82,105],[66,82,105],[19,40,71],[40,41,105],[19,40,105],[40,41,71,90],[3,67,105],[78,79,81],[81,83,89],[68,81,89],[83,89,90],[17,41,105],[17,41,90],[25,47,105],[25,47,78],[35,74,105],[74,85,105],[44,85,105],[75,76,85],[76,77,85],[77,85,87],[85,86,87],[65,85,86],[65,85,104],[74,85,104],[11,44,75,85],[63,92,97],[63,97,98],[63,92,98],[62,92,95],[62,95,98],[62,92,98],[93,96,97],[93,97,98],[93,96,101],[93,98,99],[93,99,101],[96,97,102],[96,101,102],[100,101,102],[83,84,94],[84,94,100],[83,84,97],[84,97,100],[70,83,94],[70,73,83],[69,70,94],[69,70,73],[18,19,105],[3,18,105],[18,19,71,72],[3,18,67,72],[68,81,88],[78,81,88],[59,90,91],[89,90,91],[25,26,105],[25,26,78],[60,61,105],[17,60,105],[59,60,61,91],[17,59,60,90],[49,50,105],[48,49,105],[48,49,50,79],[51,52,105],[48,52,105],[48,52,79],[51,52,79],[46,51,105],[46,47,105],[46,47,78],[46,51,78,79],[34,35,74],[34,50,105],[34,35,105],[34,50,74,79],[38,97,100],[38,97,102],[38,100,102],[29,61,91],[29,31,91],[29,31,105],[29,61,105],[27,28,68],[27,28,105],[53,58,105],[28,53,105],[53,58,88],[28,53,68,88],[57,58,105],[26,57,105],[57,58,88],[26,57,78,88],[30,31,105],[27,30,105],[30,31,89,91],[27,30,68,89]],"faces":[[91,48,93],[2,0,3],[10,2,3,12],[16,10,12,11],[11,5,67,16],[103,101,53,54],[92,90,91,93],[92,44,46,90],[99,56,55,98],[135,99,98,133],[139,126,127,137],[129,127,126,131],[124,125,122,123],[139,137,136,138],[136,124,123,138],[118,115,117,116],[115,57,117],[120,119,121],[32,23,29],[45,46,44,47],[54,53,45,47],[67,5,59],[114,111,112,113],[113,112,55,56],[109,106,105,108],[106,104,105],[118,116,104,106],[114,110,107,111],[109,108,107,110],[131,130,128,129],[135,133,132,134],[134,132,128,130],[103,96,102],[102,100,101,103],[122,125,100,102],[72,71,73],[70,68,69],[21,20,22],[64,65,13,14],[43,7,6,39],[42,41,35,93,48],[126,139,51,94,131],[88,89,38,35,41,40],[89,88,86,87],[37,36,9,47,44,92],[92,93,35,38,37],[89,87,36,37,38],[57,115,118,19,66,58],[67,60,15,16],[18,15,60,61],[61,62,17,18],[99,135,95,49,114,113,56],[110,114,49,1,19,118,106,109],[29,28,26,27,30,31,32],[8,26,28,1,49,95,94,51,50],[42,43,39,40,41],[87,86,82,84,8,50,52,9,36],[84,82,83,85],[63,62,61,60,67,59,58,66,65,64],[14,4,63,64],[62,63,4,17],[130,131,94,95,135,134],[97,52,50,51,139,138],[103,54,47,9,52,97,96],[138,123,122,102,96,97],[71,30,27,68,70,73],[77,75,74,76,78],[88,40,39,6,33,34,83,82,86],[71,72,24,31,30],[76,74,79,80],[75,69,68,27,26,8,84,85,119,120,79,74],[75,77,25,24,72,73,70,69],[25,77,78,33,6,7,0,2,10,16,15,18,17,4,14,13,20,21],[85,83,34,81,121,119],[80,81,34,33,78,76],[81,80,79,120,121],[24,25,21,22,23,32,31],[13,65,66,19,1,28,29,23,22,20],[128,132,133,98,55,112,111,107,108,105,104,116,117,57,58,59,5,11,12,3,0,7,43,42,48,91,90,46,45,53,101,100,125,124,136,137,127,129]],"active":[3,8,9,10,11,17,18,19,25,26,27,28,29,30,31,34,35,38,39,40,41,44,46,47,48,49,50,51,52,53,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105]}}
```
