# material-e3238a156044

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Four further exact nonwinners, including a simple C92 strict222 body

No110. Complete recovery dependencies: [internal-source-reference] (recover_d2_v21.py and d2_vertex_exact.py), and its unchanged d2_exact.py dependency [internal-source-reference]. No original numerical sandbox is needed. Every complete exact new input is literal below.

D2_ENERGY250_G3: V41/E106/F67,C212,strict7/3/8,additionalweak000,centred common-multiplier46bits. D2_ENERGY250_G4: V49/E128/F81,C256,strict334,additionalweak000,59bits. These two independent roundings derive from call228 of a COMPLETED250-iteration energy-gated D2 vertex method. Numerical precursorV53/E138/F87,S3U3 is NOT the exact roundedG3/G4 complex. G3/G4 changes of incidence are genuine exact rounding effects, not tolerance deletion.

D2_V21_SPD_G3 and D2_V21_SPD_G6 are invertible rational affine images of EXACT D2_V21_E46_G3 (notG4/G6), both V21/E46/F27,C92. G3 is own323/weak000,87 centred-multiplier bits; G6 is own222/weak000,127bits. G6 is a useful simpler nonsymmetric-metric entrance with203 true-edge headroom, not target110 and not an equilibrium improvement over all historical S1/U2 bodies. The matrix acts on column vectors. It breaks orthogonal D2/C2 symmetry; therefore BASE/top-root and paired-critical constraints of the original Euclidean symmetric body cannot be imposed on the transformed geometry. Its residual affine symmetry is not an orthogonal symmetry claim.

Exact G6 stable facets19,21; unstable vertices6,12; saddle edges17,45, all in the inherited exact parent ordering. G3 has S17,19,21,U6,12,H5,17,45. BASE is not the sole prescribed root after shear. Own G6 centre=(-13226937098227501/36150818400000000,-407110576818913/702932580000000,-120482561947/253055728800). The complete audit includes transformed exact coordinates/face cycles/true edges, actual mass at two origins, affine-volume/centroid crosschecks, direct feet versus same-centre polarS, and all mixed/weak tests. The maximal complex is preserved by the invertible affine map of the completely reconstructed parent, not inferred from a new triangulated hull. One inherited full mechanics auditor, not independent duplicate verification.

Write the complete units below as UTF8/LF+terminal newline. recover_d2_more.py3278B SHA5bf8a151a6a3c267050947f4ca87db13c116b1a79e0c0262d44c67f415436d3d; exact_affine.py5353B SHAa2208b78a5b36c2cc4d0761f330962db73fffb304b437782cfe6d1449a6b7354. CPython3.13.5 standard library only. Command `python -B -S recover_d2_more.py D2_MORE`; expected `D2_FOUR_MORE_EXACT_RECOVERY_PASS 10`. All ten input/H/full-audit byte receipts were freshly cold-reproduced. Original search sources and numerical finite ledger are preserved separately; exact endpoints do not depend on numerical replay.

## recover_d2_more.py
```python
"""Recover four further exact D2-derived nonwinners; none110.
Requires exact_affine.py, recover_d2_v21.py, d2_vertex_exact.py, d2_exact.py.
"""
from pathlib import Path
import json,sys,hashlib
from d2_vertex_exact import convert,raw
from exact_affine import audit_affine
from recover_d2_v21 import ROWS
DATA = {'D2_ENERGY250_G3.json': {'denominator': 1000, 'name': 'D2_ENERGY250_G3', 'representatives': [[0, 0, 1000], [0, 1240, -1000], [0, 1257, -953], [152, 1215, -1000], [265, 0, 539], [513, 0, -233], [631, 830, -1000], [631, 645, -1000], [632, 387, -1000], [645, 456, -994], [633, 342, -1000], [646, 448, -993], [667, 292, -965], [635, 0, -1000], [639, 283, -998], [646, 250, -995], [641, 201, -997], [640, 0, -998]]}, 'D2_ENERGY250_G4.json': {'denominator': 10000, 'name': 'D2_ENERGY250_G4', 'representatives': [[0, 0, 10000], [0, 12397, -10000], [0, 12574, -9532], [1516, 12147, -10000], [2652, 0, 5386], [5129, 0, -2335], [6313, 8295, -10000], [6307, 6454, -10000], [6317, 3867, -10000], [6445, 4559, -9941], [6333, 3425, -9998], [6457, 4475, -9926], [6673, 2923, -9647], [6352, 0, -9996], [6386, 2826, -9982], [6462, 2505, -9950], [6412, 2010, -9973], [6398, 0, -9981]]}, 'D2_V21_SPD_G3.json': {'denominator': 1000, 'integer_matrix': [[2060, 4000, 768], [0, 1337, 1216], [0, 0, 1000]], 'name': 'D2_V21_SPD_G3'}, 'D2_V21_SPD_G6.json': {'denominator': 1000000, 'integer_matrix': [[2060271, 4000000, 768481], [0, 1336957, 1216440], [0, 0, 1000000]], 'name': 'D2_V21_SPD_G6'}}
EXPECTED = {'D2_ENERGY250_G3.json': (903, '2f030c001a52b9130dac900ab72e52eab96dcdd51720e7fb99e25acbdf1b08f7'), 'D2_ENERGY250_G3_audit.json': (12629, '30eccc1c1f4174f5e18acb67a0026296ca9b622fef9ce18120923d592fe5b6ca'), 'D2_ENERGY250_G3_H.json': (5238, '626d17bc77b6eb2effc300b1c9e351d9cbf1ce98eeb5fadc98b9a25c50fe9487'), 'D2_ENERGY250_G4.json': (948, 'a9eb8b045b29fe3ac4add51bbade7729cb442c443fffc29244e2c96b479d135c'), 'D2_ENERGY250_G4_audit.json': (15103, '5aed3b6ccdd43b8b6a7090f0bec31efcbfba0994e144231925e7bd8685850e7f'), 'D2_ENERGY250_G4_H.json': (10258, 'b6e86205c50fec775851a1958900f4cfd3bbe3f8bccfcb672ab0518701c106a8'), 'D2_V21_SPD_G3.json': (213, 'f5558107576c89e950314cdc9912c588c07dee79e2e6740aca46214381a30ddb'), 'D2_V21_SPD_G3_audit.json': (6080, 'dd55dd4525d4efe1961f91c4051e0fc1a071330042d8caaea3af64fbc488a1ff'), 'D2_V21_SPD_G6.json': (234, '54c5716d4c2a63b508a09d03aeac46a3acc6396be9c872c0aa477afd276afb69'), 'D2_V21_SPD_G6_audit.json': (6420, '63f6aab6970939e89f4748f954e0dc28ceab7a7b767499da1ef8c353124aaf82')}
def main():
    out=Path(sys.argv[1] if len(sys.argv)>1 else 'D2_MORE');out.mkdir(parents=True,exist_ok=True)
    _,parent=convert(dict(name='D2_V21_E46_G3',denominator=1000,representatives=ROWS[3]));count=0
    for fn,d in DATA.items():
        items=[(fn,d)]
        if 'integer_matrix' in d:a=audit_affine(parent,d)
        else:
            h,a=convert(d);items.append((d['name']+'_H.json',h))
        items.append((d['name']+'_audit.json',a))
        for name,obj in items:
            b=raw(obj);assert (len(b),hashlib.sha256(b).hexdigest())==EXPECTED[name],name;(out/name).write_bytes(b);count+=1
        print(d['name'],a['V'],a['E'],a['F'],a['strict'],a['additional_weak'])
    print('D2_FOUR_MORE_EXACT_RECOVERY_PASS',count)
if __name__=='__main__':main()
```

## exact_affine.py
```python
"""Full exact audit of an invertible rational affine image of an audited parent.
Dependency d2_exact.py supplies exact arithmetic helpers, not a second auditor.
Own mass recomputed at two origins and compared with affine centroid/volume laws.
"""
from d2_exact import dot,sub,cross,add,mul,det,sign,textfrac
from fractions import Fraction as F
from math import gcd,lcm
from functools import reduce
import json,hashlib,sys
from pathlib import Path

def raw(x):return (json.dumps(x,sort_keys=True,indent=2)+'\n').encode()
def audit_affine(parent,data):
    T=data['integer_matrix'];den=int(data['denominator']);assert den>0 and det(*T)>0
    vv=[tuple(F(x,v[3]) for x in v[:3]) for v in parent['vertices']]
    new=[tuple(sum(F(T[i][j],den)*v[j] for j in range(3)) for i in range(3)) for v in vv]
    L=lcm(*(x.denominator for p in new for x in p));P=[tuple(int(x*L) for x in p) for p in new]
    verts=[]
    for p in P:
        g=reduce(gcd,(*map(abs,p),L));verts.append((*[x//g for x in p],L//g))
    fs=parent['facets'];N=[]
    for f in fs:
        n=cross(sub(P[f[1]],P[f[0]]),sub(P[f[2]],P[f[0]]));g=reduce(gcd,map(abs,n));assert g>0;n=tuple(x//g for x in n);h=dot(n,P[f[0]])
        assert all(dot(n,p)<=h for p in P)
        assert [i for i,p in enumerate(P) if dot(n,p)==h]==sorted(f)
        for u,v in zip(f,f[1:]+f[:1]):
            assert all(dot(n,cross(sub(P[v],P[u]),sub(P[w],P[u])))>=0 for w in f)
        N.append(n)
    edges={}
    triangles=[]
    for i,f in enumerate(fs):
        for a,b in zip(f,f[1:]+f[:1]):edges.setdefault(tuple(sorted((a,b))),[]).append(i)
        triangles += [(f[0],f[j],f[j+1]) for j in range(1,len(f)-1)]
    assert all(len(o)==2 for o in edges.values())
    el=sorted(edges);assert len(P)-len(el)+len(fs)==2
    # Connected maximal complex.
    seen={0}
    while True:
        old=len(seen)
        for a,b in el:
            if a in seen or b in seen:seen.update((a,b))
        if len(seen)==old:break
    assert len(seen)==len(P)
    def mass(origin):
        tets=[det(sub(P[a],origin),sub(P[b],origin),sub(P[c],origin)) for a,b,c in triangles]
        den=4*sum(tets)
        num=tuple(sum(t*(P[a][j]+P[b][j]+P[c][j]+origin[j]) for t,(a,b,c) in zip(tets,triangles)) for j in range(3))
        return den,num
    D,C=mass((0,0,0));assert D>0
    D2,C2=mass(P[0]);assert D2==D and C2==C

    X=[sub(mul(D,p),C) for p in P]
    H=[D*dot(n,P[f[0]])-dot(n,C) for n,f in zip(N,fs)];assert min(H)>0
    un=[[] for p in P];sn=[[] for f in fs]
    for a,b in el:
        d=sub(X[b],X[a]);un[a].append(dot(X[a],d));un[b].append(-dot(X[b],d))
        i,j=edges[(a,b)]
        nij=dot(N[i],N[j]);ni=dot(N[i],N[i]);nj=dot(N[j],N[j])
        sn[i].append(nij*H[i]-ni*H[j]);sn[j].append(nij*H[j]-nj*H[i])
    U=[i for i,s in enumerate(un) if max(s)<0]
    WV=[i for i,s in enumerate(un) if max(s)==0]
    S=[i for i,s in enumerate(sn) if max(s)<0]
    # Direct feet: strict face foot lies in no other support plane.
    footS=[];boundaryfeet=[]
    for i,n in enumerate(N):
        norm=dot(n,n);ss=[H[i]*dot(n,m)-H[j]*norm for j,m in enumerate(N) if j!=i]
        if max(ss)<0:footS.append(i)
        elif max(ss)==0:boundaryfeet.append(i)
    assert S==footS
    Saddles=[];WE=[];edge_rows=[]
    for eid,(a,b) in enumerate(el):
        d=sub(X[b],X[a]);dd=dot(d,d);xd=dot(X[a],d);tn=-xd
        if 0<tn<dd:
            p=add(mul(dd,X[a]),mul(tn,d));i,j=edges[(a,b)]
            aa=dot(N[i],N[i]);ab=dot(N[i],N[j]);bb=dot(N[j],N[j]);assert aa*bb-ab*ab>0
            u=dot(p,N[i])*bb-dot(p,N[j])*ab
            v=dot(p,N[j])*aa-dot(p,N[i])*ab
            if u>0 and v>0:Saddles.append(eid)
            elif u>=0 and v>=0:WE.append(eid)
        edge_rows.append([a,b,*edges[(a,b)]])
    if not WV and not WE:assert len(S)+len(U)-len(Saddles)==2
    result=dict(name=data['name'],V=len(P),E=len(el),F=len(fs),C=2*len(el),strict=[len(S),len(U),len(Saddles)],additional_weak=[0,len(WV),len(WE)],
      stable_faces=S,unstable_vertices=U,saddle_edges=Saddles,weak_vertices=WV,weak_edges=WE,boundary_face_feet=boundaryfeet,
      volume=textfrac(D,24*L**3),centroid=[textfrac(c,D*L) for c in C],
      centred_scale_bits=(D*L).bit_length(),vertex_denominator_lcm_bits=L.bit_length(),
      primitive_zero_U_arrows=sum(s==0 for a in un for s in a),primitive_zero_Q_arrows=sum(s==0 for a in sn for s in a),
      vertices=[list(v) for v in verts],facets=fs,edges=edge_rows,
      checks=['invertible-rational-affine-map-of-complete-exact-parent','exact-all-supports-and-facet-incidences','exact-polygon-convexity','true-two-owner-edges','Euler-connected','two-origin-exact-mass','affine-centroid-and-volume-crosscheck','all-centred-supports-positive','direct-feet-polar-S-crosscheck','all-vertex-and-mixed-edge-strict-weak'])
    oldc=tuple(F(c) for c in parent['centroid']);expectedc=tuple(sum(F(T[i][j],den)*oldc[j] for j in range(3)) for i in range(3))
    assert expectedc==tuple(F(c,D*L) for c in C)
    assert F(result['volume'])==F(parent['volume'])*F(det(*T),den**3)
    return result

if __name__=='__main__':
    parent=json.load(open(sys.argv[1]));data=json.load(open(sys.argv[2]));a=audit_affine(parent,data);bs=raw(a);name=data['name']+'_audit.json';Path(name).write_bytes(bs);print('EXACT_AFFINE_FULL_AUDIT_PASS',a['V'],a['E'],a['F'],a['strict'],a['additional_weak'],len(bs),hashlib.sha256(bs).hexdigest())
```
