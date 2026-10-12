# material-d2f4cb8a5097

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

#!/usr/bin/env python3
"""Exact actual-body controls for adjacent-facet trace sums; standard library only."""
from fractions import Fraction as F
from itertools import combinations
from functools import cmp_to_key
from math import gcd, lcm
from pathlib import Path
import hashlib, json, sys

ZERO=F(0); ONE=F(1)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(a,t): return tuple(t*x for x in a)
def dot(a,b): return sum((x*y for x,y in zip(a,b)),ZERO)
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def mean(vs): return tuple(sum((v[k] for v in vs),ZERO)/len(vs) for k in range(3))
def canonical_plane(n,h):
    den=lcm(*(a.denominator for a in (*n,h)))
    vals=[int(a*den) for a in (*n,h)]
    div=gcd(*vals)
    return tuple(v//div for v in vals)
def order_face(vs, ids, n):
    center=mean([vs[i] for i in ids]); drop=next(k for k in range(3) if n[k])
    axes=[k for k in range(3) if k!=drop]
    vec={i:tuple(vs[i][k]-center[k] for k in axes) for i in ids}
    def half(a): return 0 if a[1]>0 or (a[1]==0 and a[0]>0) else 1
    def cmp(i,j):
        a,b=vec[i],vec[j]; ha,hb=half(a),half(b)
        if ha!=hb:return -1 if ha<hb else 1
        c=a[0]*b[1]-a[1]*b[0]
        assert c, 'A listed point is not a strict face vertex'
        return -1 if c>0 else 1
    seq=sorted(ids,key=cmp_to_key(cmp))
    if dot(cross(sub(vs[seq[1]],vs[seq[0]]),sub(vs[seq[2]],vs[seq[0]])),n)<0:seq.reverse()
    pos=seq.index(min(seq)); return seq[pos:]+seq[:pos]
def hull(vs):
    vs=[tuple(F(x) for x in v) for v in vs]
    assert len(set(vs))==len(vs)
    planes={}
    for i,j,k in combinations(range(len(vs)),3):
        n=cross(sub(vs[j],vs[i]),sub(vs[k],vs[i]))
        if not any(n):continue
        h=dot(n,vs[i]); sl=[h-dot(n,v) for v in vs]
        if min(sl)<0<max(sl):continue
        if max(sl)==0:n=mul(n,-1); h=-h; sl=[-x for x in sl]
        assert max(sl)>0 and min(sl)==0
        key=canonical_plane(n,h)
        planes[key]=[v for v in range(len(vs)) if dot(key[:3],vs[v])==key[3]]
    faces=[]
    for plane,ids in sorted(planes.items()):
        cyc=order_face(vs,ids,plane[:3]); faces.append((plane,cyc))
    active={i for _,cyc in faces for i in cyc}; assert active==set(range(len(vs)))
    edges={}
    for fi,(_,cyc) in enumerate(faces):
        for a,b in zip(cyc,cyc[1:]+cyc[:1]):edges.setdefault(tuple(sorted((a,b))),[]).append(fi)
    assert all(len(fs)==2 for fs in edges.values())
    assert len(vs)-len(edges)+len(faces)==2
    # Every supplied point is an actual vertex, not a point in a face/edge.
    for i in active:
        inc=[p[:3] for p,cyc in faces if i in cyc]
        assert any(det(*triple)!=0 for triple in combinations(inc,3))
    ref=mean(vs); total6=ZERO; first=[ZERO]*3; fdata=[]; second=[[ZERO]*3 for _ in range(3)]
    for plane,cyc in faces:
        n=plane[:3]; n2=dot(n,n); twice_area_over_norm=ZERO; fm=[ZERO]*3
        for j in range(1,len(cyc)-1):
            tri=[vs[cyc[0]],vs[cyc[j]],vs[cyc[j+1]]]
            area_factor=dot(cross(sub(tri[1],tri[0]),sub(tri[2],tri[0])),n)/n2
            assert area_factor>0
            twice_area_over_norm+=area_factor
            for k in range(3):fm[k]+=area_factor*sum(v[k] for v in tri)/3
            six=det(sub(tri[0],ref),sub(tri[1],ref),sub(tri[2],ref)); assert six>0
            tet=[ref]+tri; tsum=[sum(v[k] for v in tet) for k in range(3)]
            total6+=six
            for k in range(3):first[k]+=six*tsum[k]/4
            for k in range(3):
                for l in range(3):second[k][l]+=six*(tsum[k]*tsum[l]+sum(v[k]*v[l] for v in tet))/20
        fdata.append({'plane':plane,'vertices':cyc,'area_over_normal':twice_area_over_norm/2,
                      'centroid':tuple(x/twice_area_over_norm for x in fm)})
    volume=total6/6; centroid=tuple(x/total6 for x in first)
    covariance=[[second[k][l]/total6-centroid[k]*centroid[l] for l in range(3)] for k in range(3)]
    q=[]; d=[]
    for f in fdata:
        n=f['plane'][:3]; hh=f['plane'][3]-dot(n,centroid); assert hh>0
        q.append(tuple(F(x)/hh for x in n));d.append(f['area_over_normal']*hh/volume)
    nf=len(faces)
    lam=[[d[j]*(1-dot(q[i],sub(fdata[j]['centroid'],centroid))) for j in range(nf)] for i in range(nf)]
    assert sum(d)==3
    assert all(sum(lam[i])==3 and lam[i][i]==0 for i in range(nf))
    assert all(lam[i][j]>0 for i in range(nf) for j in range(nf) if i!=j)
    assert all(sum(d[i]*q[i][k] for i in range(nf))==0 for k in range(3))
    assert all(sum(lam[i][j]*q[j][k] for j in range(nf))==-q[i][k] for i in range(nf) for k in range(3))
    assert all(sum(lam[i][k]*lam[k][j] for k in range(nf))+lam[i][j]==4*d[j] for i in range(nf) for j in range(nf))
    centered=[sub(v,centroid) for v in vs]; neighbours={i:[] for i in range(len(vs))}
    for a,b in edges:neighbours[a].append(b);neighbours[b].append(a)
    unstable=[]; weak_vertices=[]
    for i,x in enumerate(centered):
        vals=[dot(x,sub(centered[j],x)) for j in neighbours[i]]
        if max(vals)<0:unstable.append(i)
        elif max(vals)==0:weak_vertices.append(i)
    stable=[]; weak_facets=[]
    for i,pole in enumerate(q):
        foot=mul(pole,1/dot(pole,pole)); sl=[1-dot(p,foot) for j,p in enumerate(q) if j!=i]
        if min(sl)>0:stable.append(i)
        elif min(sl)==0:weak_facets.append(i)
    saddle=[]; weak_edges=[]
    for (a,b),(i,j) in sorted(edges.items()):
        delta=sub(centered[b],centered[a]); t=-dot(centered[a],delta)/dot(delta,delta)
        if not 0<t<1:continue
        ni=dot(q[i],q[i]);nj=dot(q[j],q[j]);g=dot(q[i],q[j]);dd=ni*nj-g*g; assert dd>0
        alpha=(nj-g)/dd; beta=(ni-g)/dd
        if alpha>0 and beta>0:saddle.append((a,b))
        elif alpha>=0 and beta>=0:weak_edges.append((a,b))
    shadows=[(i,j) for i in range(nf) for j in range(nf) if i!=j and dot(q[i],sub(q[j],q[i]))>=0]
    return {'vertices':vs,'faces':fdata,'edges':[(a,b,*fs) for (a,b),fs in sorted(edges.items())],
            'volume':volume,'centroid':centroid,'covariance':covariance,'q':q,'d':d,'Lambda':lam,
            'f_vector':[len(vs),len(edges),nf],'S':stable,'U':unstable,'H':saddle,
            'boundary_contacts':{'vertices':weak_vertices,'facets':weak_facets,'edges':weak_edges},
            'pole_shadows':shadows,'degrees':[len(neighbours[i]) for i in range(len(vs))]}
def facet_with_vertices(body,inds):
    inds=set(inds); result=[i for i,f in enumerate(body['faces']) if inds==set(f['vertices'])]
    assert len(result)==1;return result[0]
def facet_with_plane(body,plane):
    result=[i for i,f in enumerate(body['faces']) if tuple(f['plane'])==tuple(plane)]
    assert len(result)==1;return result[0]
def truncate(vs,index,delta):
    body=hull(vs); neigh=[]
    for a,b,*_ in body['edges']:
        if a==index:neigh.append(b)
        elif b==index:neigh.append(a)
    assert len(neigh)==3
    p=vs[index]; replacements=[add(p,mul(sub(vs[j],p),delta)) for j in sorted(neigh)]
    return [v for i,v in enumerate(vs) if i!=index]+replacements

def build():
    # Labels0=left narrow,1=right narrow,2=right wide,3=left wide,4=apex.
    raw=[(-F(1,2),0,0),(F(1,2),0,0),(1,1,0),(-1,1,0),(F(1,7),F(2,5),1)]
    raw=[tuple(F(x) for x in p) for p in raw]; base=hull(raw)
    a=facet_with_vertices(base,{0,1,4});b=facet_with_vertices(base,{0,1,2,3});c=facet_with_vertices(base,{2,3,4})
    designated=[base['faces'][i]['plane'] for i in (a,b,c)]
    assert base['Lambda'][a][b]==1 and base['Lambda'][a][c]==F(16,15)
    base['selected_indices']=[a,b,c];base['selected_sum']=base['Lambda'][a][b]+base['Lambda'][a][c]
    assert base['selected_sum']==F(31,15)>F(51,25)
    left=facet_with_vertices(base,{0,3,4});n=tuple(F(x) for x in base['faces'][left]['plane'][:3])
    stacked=add(mean([raw[i] for i in (0,3,4)]),mul(n,F(1,100000)))
    first=hull(raw+[stacked]);assert first['f_vector']==[6,11,7]
    cut1=truncate(raw+[stacked],5,F(1,100))
    after1=hull(cut1);assert after1['f_vector']==[8,14,8]
    cut2=truncate(cut1,1,F(1,100))
    body=hull(cut2);assert body['f_vector']==[10,17,9]
    aa,bb,cc=[facet_with_plane(body,p) for p in designated]
    assert any(set((bb,cc))==set(e[2:]) for e in body['edges'])
    total=body['Lambda'][aa][bb]+body['Lambda'][aa][cc]
    assert total>F(51,25)
    assert all(not v for v in body['boundary_contacts'].values())
    assert len(body['S'])+len(body['U'])-len(body['H'])==2
    assert (len(body['S']),len(body['U']),len(body['H']))!=(1,1,0)
    body['selected_indices']=[aa,bb,cc];body['selected_sum']=total
    body['selected_gap_over_51_25']=total-F(51,25)
    body['selected_facet_sizes']=[len(body['faces'][i]['vertices']) for i in (aa,bb,cc)]
    body['selected_planes']=designated
    return {'identity':'PAIR_TRACE_SAME_FVECTOR_E17_CONTROL_V1',
            'parameters':{'stack_normal_coefficient':F(1,100000),'stack_vertex_cut_fraction':F(1,100),
                          'original_vertex_1_cut_fraction':F(1,100)},
            'pyramid':base,'e17_control':body}
def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x

def main():
    assert len(sys.argv)==2 and sys.argv[1] in ('build','check')
    obj=encode(build());data=(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode()
    path=Path('pair_trace_e17_report.json')
    if sys.argv[1]=='build':path.write_bytes(data)
    else:assert path.read_bytes()==data
    b=obj['e17_control'];print('PYRAMID_PAIR_TRACE_EXACT_PASS 31/15 > 51/25')
    print('E17_PAIR_TRACE_EXACT_PASS',*b['f_vector'],len(b['S']),len(b['U']),len(b['H']))
    print('SELECTED_FACET_SIZES',*b['selected_facet_sizes'])
    print('SELECTED_SUM',b['selected_sum'])
    print('REPORT',len(data),hashlib.sha256(data).hexdigest())
    print('NOT_TREE253_NOT_GOMBOC_NO_UNIVERSAL_C_BOUND_CHANGE')
if __name__=='__main__':main()
