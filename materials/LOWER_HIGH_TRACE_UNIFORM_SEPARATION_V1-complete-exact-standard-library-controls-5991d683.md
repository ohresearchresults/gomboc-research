# material-5991d6830977

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

#!/usr/bin/env python3
"""Exact controls for LOWER_HIGH_TRACE_UNIFORM_SEPARATION_V1.
Standard library only; this is NOT a numerical value of the uniform gap.
"""
from fractions import Fraction as F
from itertools import combinations
from functools import cmp_to_key
from math import gcd, lcm
from pathlib import Path
import hashlib, json, sys

Z=F(0)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(a,t): return tuple(t*x for x in a)
def dot(a,b): return sum((x*y for x,y in zip(a,b)),Z)
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def avg(v): return tuple(sum((p[k] for p in v),Z)/len(v) for k in range(len(v[0])))
def plane_key(n,h):
    den=lcm(*(x.denominator for x in (*n,h)))
    q=[int(x*den) for x in (*n,h)]; g=gcd(*q)
    return tuple(x//g for x in q)
def cycle(v,ids,n):
    c=avg([v[i] for i in ids]); drop=next(k for k in range(3) if n[k]); ax=[k for k in range(3) if k!=drop]
    p={i:tuple(v[i][k]-c[k] for k in ax) for i in ids}
    def half(a): return 0 if a[1]>0 or (a[1]==0 and a[0]>0) else 1
    def cmp(i,j):
        a,b=p[i],p[j]
        if half(a)!=half(b): return -1 if half(a)<half(b) else 1
        w=a[0]*b[1]-a[1]*b[0]; assert w
        return -1 if w>0 else 1
    ids=sorted(ids,key=cmp_to_key(cmp))
    if dot(cross(sub(v[ids[1]],v[ids[0]]),sub(v[ids[2]],v[ids[0]])),n)<0: ids.reverse()
    j=ids.index(min(ids)); return ids[j:]+ids[:j]
def hull(points):
    v=[tuple(F(x) for x in p) for p in points]; assert len(set(v))==len(v)
    planes={}
    for a,b,c in combinations(range(len(v)),3):
        n=cross(sub(v[b],v[a]),sub(v[c],v[a]))
        if not any(n): continue
        h=dot(n,v[a]); sl=[h-dot(n,p) for p in v]
        if min(sl)<0<max(sl): continue
        if max(sl)==0: n=scale(n,-1); h=-h
        pk=plane_key(n,h)
        assert all(dot(pk[:3],p)<=pk[3] for p in v)
        planes[pk]=[i for i,p in enumerate(v) if dot(pk[:3],p)==pk[3]]
    faces=[]; edges={}; ref=avg(v); mass=Z; first=[Z]*3; second=[[Z]*3 for _ in range(3)]
    for pk,ids in sorted(planes.items()):
        ids=cycle(v,ids,pk[:3]); fi=len(faces); area=Z; fm=[Z]*3
        for a,b in zip(ids,ids[1:]+ids[:1]): edges.setdefault(tuple(sorted((a,b))),[]).append(fi)
        for j in range(1,len(ids)-1):
            tri=[v[i] for i in (ids[0],ids[j],ids[j+1])]
            w=dot(cross(sub(tri[1],tri[0]),sub(tri[2],tri[0])),pk[:3])/dot(pk[:3],pk[:3]); assert w>0
            area+=w
            for k in range(3): fm[k]+=w*sum(p[k] for p in tri)/3
            six=det(*(sub(p,ref) for p in tri)); assert six>0
            tet=[ref]+tri; ss=[sum(p[k] for p in tet) for k in range(3)]; mass+=six
            for k in range(3):
                first[k]+=six*ss[k]/4
                for l in range(3): second[k][l]+=six*(ss[k]*ss[l]+sum(p[k]*p[l] for p in tet))/20
        faces.append({'plane':pk,'cycle':ids,'area_over_normal':area/2,'centroid':tuple(x/area for x in fm)})
    assert all(len(x)==2 for x in edges.values())
    assert len(v)-len(edges)+len(faces)==2
    for i in range(len(v)):
        inc=[f['plane'][:3] for f in faces if i in f['cycle']]
        assert any(det(*t)!=0 for t in combinations(inc,3)), 'All supplied points must be true vertices'
    vol=mass/6; g=tuple(x/mass for x in first); poles=[]; d=[]
    covariance=[[second[k][l]/mass-g[k]*g[l] for l in range(3)] for k in range(3)]
    for f in faces:
        n=f['plane'][:3]; h=f['plane'][3]-dot(n,g); assert h>0
        poles.append(tuple(F(x)/h for x in n)); d.append(f['area_over_normal']*h/vol)
    lam=[[d[j]*(1-dot(poles[i],sub(faces[j]['centroid'],g))) for j in range(len(faces))] for i in range(len(faces))]
    assert sum(d)==3 and all(sum(row)==3 and row[i]==0 for i,row in enumerate(lam))
    assert all(sum(d[i]*poles[i][k] for i in range(len(faces)))==0 for k in range(3))
    assert all(sum(lam[i][j]*poles[j][k] for j in range(len(faces)))==-poles[i][k] for i in range(len(faces)) for k in range(3))
    centered=[sub(p,g) for p in v]; neighbours={i:[] for i in range(len(v))}
    for a,b in edges: neighbours[a].append(b); neighbours[b].append(a)
    unstable=[i for i,p in enumerate(centered) if all(dot(p,sub(centered[j],p))<0 for j in neighbours[i])]
    stable=[i for i,q in enumerate(poles) if all(dot(p,q)<dot(q,q) for j,p in enumerate(poles) if i!=j)]
    saddle=[]
    for (a,b),(i,j) in sorted(edges.items()):
        delta=sub(centered[b],centered[a]); t=-dot(centered[a],delta)/dot(delta,delta)
        if not 0<t<1: continue
        ii=dot(poles[i],poles[i]); jj=dot(poles[j],poles[j]); ij=dot(poles[i],poles[j])
        if ii>ij and jj>ij: saddle.append((a,b))
    return {'vertices':v,'faces':faces,'edges':[(a,b,*fs) for (a,b),fs in sorted(edges.items())],
            'volume':vol,'centroid':g,'covariance':covariance,'poles':poles,'d':d,'Lambda':lam,
            'f_vector':[len(v),len(edges),len(faces)],'S':stable,'U':unstable,'H':saddle}
def with_vertices(p,vs):
    out=[i for i,f in enumerate(p['faces']) if set(f['cycle'])==set(vs)]; assert len(out)==1; return out[0]
def with_plane(p,pk):
    out=[i for i,f in enumerate(p['faces']) if f['plane']==pk]; assert len(out)==1; return out[0]
def truncate(v,i,t):
    p=hull(v); ns=[]
    for a,b,*_ in p['edges']:
        if a==i: ns.append(b)
        if b==i: ns.append(a)
    assert len(ns)==3
    return [p for j,p in enumerate(v) if j!=i]+[add(v[i],scale(sub(v[j],v[i]),t)) for j in sorted(ns)]
def root_stats(p,i):
    q=p['poles'][i]; L=max(1-dot(q,sub(v,p['centroid'])) for v in p['vertices'])
    H=1+sum(q[k]*p['covariance'][k][l]*q[l] for k in range(3) for l in range(3))
    return L,p['d'][i],H

def poly(a):
    a=list(map(F,a))
    while len(a)>1 and a[-1]==0: a.pop()
    return tuple(a)
def pa(a,b): return poly([(a[i] if i<len(a) else Z)+(b[i] if i<len(b) else Z) for i in range(max(len(a),len(b)))])
def ps(a,t): return poly([x*t for x in a])
def pm(a,b):
    c=[Z]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return poly(c)
def exact_identities():
    one=poly([1]); s=poly([0,1]); den=poly([1,2]); one_minus_s=poly([1,-1])
    # Bicone coefficients multiplied by the common positive denominator 1+2s.
    au=pm(s,den); al=ps(pm(s,one_minus_s),2)
    bu=ps(pm(one_minus_s,den),3); bl=ps(pm(s,s),6)
    A=pa(au,al); B=pa(bu,bl); two=ps(den,2)
    bounds=[pa(au,ps(bu,F(2,3))),pa(al,ps(bl,F(2,3))),pa(A,ps(B,F(1,3))),
            pa(au,ps(pa(ps(bu,2),bl),F(1,3))),pa(al,ps(pa(bu,ps(bl,2)),F(1,3))),ps(B,F(2,3))]
    expected=[pm(s,den),poly([2,2,-2]),one,s,poly([1,1]),ps(s,2)]
    gaps=[pa(two,ps(b,-1)) for b in bounds]; assert gaps==expected
    assert pa(A,B)==ps(den,3)
    # Frustum top trace w=3r^2 C/(A B); w<3/2 follows from A B-2r^2 C>0.
    aa=poly([1,1,1]); bb=poly([1,2,3]); cc=poly([3,2,1]); r2=poly([0,0,1])
    fr=pa(pm(aa,bb),ps(pm(r2,cc),-2)); assert fr==poly([1,3,0,1,1])
    return {'bicone_gaps_times_1_plus_2s':gaps,'frustum_AB_minus_2r2C':fr}
def planar(B):
    B=[tuple(F(x) for x in p) for p in B]
    ds=[a[0]*b[1]-a[1]*b[0] for a,b in zip(B,B[1:]+B[:1])]; area=sum(ds)/2
    c=tuple(sum(t*(a[k]+b[k]) for a,b,t in zip(B,B[1:]+B[:1],ds))/(6*area) for k in range(2))
    uv=[]
    for a,b,w in zip(B,B[1:]+B[:1],ds):
        aa=sub(a,c); bb=sub(b,c); vv=(aa[0]*bb[1]-aa[1]*bb[0])/(2*area)
        uv.append((w/(2*area),vv)); assert 0<vv<=F(1,3)
    return B,area,c,uv

def equality_controls():
    # Three literal bases: triangle, asymmetric quadrilateral, pentagon. Origin is interior.
    bases=[[(-1,-1),(2,-1),(-1,2)],[(-2,-1),(1,-1),(2,2),(-1,1)],
           [(-2,-1),(1,-2),(3,0),(1,2),(-2,1)]]
    results=[]; pair_count=0
    for B0 in bases:
        B,area,c,uv=planar(B0); k=len(B)
        for s in (F(1,7),F(1,2),F(5,6)):
            p=hull([(0,0,0)]+[(*b,s) for b in B]+[(0,0,1)])
            mu=(1+2*s)/4; assert p['centroid']==(3*c[0]/4,3*c[1]/4,mu)
            assert p['volume']==area/3
            trace=[p['d'][i]*f['centroid'][2]/mu for i,f in enumerate(p['faces'])]
            for j,(u,v) in enumerate(uv):
                ids=(j+1,(j+1)%k+1)
                U=with_vertices(p,(*ids,k+1)); L=with_vertices(p,(0,*ids))
                assert trace[U]==s*u+3*(1-s)*v
                assert trace[L]==2*s*(1-s)*u/(1+2*s)+6*s*s*v/(1+2*s)
            assert sum(trace)==3
            pairs=[trace[i]+trace[j] for i,j in combinations(range(len(trace)),2)]
            assert max(pairs)<2; pair_count+=len(pairs)
            results.append({'kind':'bicone','s':s,'body':p,'trace':trace,'pair_max':max(pairs)})
        for r in (F(1,5),F(1),F(2),F(7)):
            # Shift the planar centroid to zero; this is not a change of physical metric for an equilibrium claim.
            Bc=[sub(b,c) for b in B]
            p=hull([(*b,0) for b in Bc]+[(*(r*x for x in b),1) for b in Bc])
            aa=1+r+r*r; bb=1+2*r+3*r*r; mu=bb/(4*aa)
            assert p['volume']==area*aa/3 and p['centroid']==(0,0,mu)
            root=with_vertices(p,range(k)); top=with_vertices(p,range(k,2*k))
            trace=p['Lambda'][root]; w=3*r*r*(3+2*r+r*r)/(aa*bb)
            assert trace[top]==w and w<F(3,2)
            for j,(_,v) in enumerate(uv):
                side=with_vertices(p,(j,(j+1)%k,j+k,(j+1)%k+k)); assert trace[side]==(3-w)*v
            pairs=[trace[i]+trace[j] for i,j in combinations(range(len(trace)),2)]
            assert max(pairs)<=2; pair_count+=len(pairs)
            results.append({'kind':'frustum','r':r,'body':p,'trace':trace,'pair_max':max(pairs)})
    return results,pair_count

def lower_bracket(L,d,H):
    # For fixed L,d, k=a/h increases with tau; these brackets are literal inputs, checked, not guessed roots.
    def data(k):
        tau=(3*k*k-L*d)/(d*k*(k+1)); h2=d/(k*k)
        assert 0<tau<L
        mean=(h2*L*(L+2*tau)+d*(1+2/k)*tau*tau)/12
        m2=h2*(L*(L*L+2*L*tau+3*tau*tau)+k*(k+3)*tau**3)/30
        return tau,mean,m2
    lo=F(3,4); hi=F(7,8)
    assert data(lo)[1]<1<data(hi)[1]
    for _ in range(80):
        mid=(lo+hi)/2
        if data(mid)[1]<1: lo=mid
        else: hi=mid
    a=data(lo); b=data(hi); assert a[1]<1<=b[1] and a[2]<=b[2]<H
    return {'L':L,'d':d,'H':H,'k_interval':[lo,hi],'tau_interval':[a[0],b[0]],
            'mean_at_endpoints':[a[1],b[1]],'M2_interval':[a[2],b[2]],
            'actual_gap_interval':[H-b[2],H-a[2]],'bisections':80,
            'warning':'This is the gap of this explicit body, NOT the uniform gap over all bodies.'}
def high_trace_controls():
    v=[tuple(F(x) for x in a) for a in ((-F(1,2),0,0),(F(1,2),0,0),(1,1,0),(-1,1,0),(F(1,7),F(2,5),1))]
    p=hull(v); root=with_vertices(p,(0,1,4)); pair=[with_vertices(p,(0,1,2,3)),with_vertices(p,(2,3,4))]
    planes=[p['faces'][i]['plane'] for i in (root,*pair)]
    assert root_stats(p,root)==(F(12,5),F(5,12),F(168,125))
    T=sum(p['Lambda'][root][i] for i in pair); assert T==F(31,15)>F(51,25)
    out=[{'object':'original quadrilateral pyramid from PAIR_TRACE_SAME_FVECTOR_E17_CONTROL_V1',
          'body':p,'root':root,'pair':pair,'trace_sum':T,'lower':lower_bracket(*root_stats(p,root))}]
    left=with_vertices(p,(0,3,4)); n=p['faces'][left]['plane'][:3]
    stack=add(avg([v[i] for i in (0,3,4)]),scale(n,F(1,100000)))
    v=truncate(v+[stack],5,F(1,100)); v=truncate(v,1,F(1,100)); p=hull(v)
    root,a,b=[with_plane(p,t) for t in planes]; T=p['Lambda'][root][a]+p['Lambda'][root][b]
    assert p['f_vector']==[10,17,9] and T>F(51,25)
    assert [len(p[x]) for x in ('S','U','H')]==[5,5,8]
    assert any(set(e[2:])=={a,b} for e in p['edges'])
    out.append({'object':'unchanged PAIR_TRACE_SAME_FVECTOR_E17_CONTROL_V1 e17_control',
                'body':p,'root':root,'pair':[a,b],'trace_sum':T,'lower':lower_bracket(*root_stats(p,root))})
    return out

def merging_controls():
    out=[]
    for e in (F(1),F(1,2),F(1,10),F(1,100)):
        xz=[(-1,0),(1,0),(1,1),(0,1+e),(-1,1)]
        p=hull([(x,y,z) for y in (-1,1) for x,z in xz]); mu=(1+e+e*e/3)/(2+e)
        assert p['volume']==4+2*e and p['centroid']==(0,0,mu)
        root=with_plane(p,(0,0,-1,0)); roofs=[]
        for i,f in enumerate(p['faces']):
            n=f['plane'][:3]
            if n[2]>0: roofs.append(i)
        assert len(roofs)==2
        T=sum(p['Lambda'][root][i] for i in roofs)
        d=(1+e-mu)/(2+e)
        assert all(p['d'][i]==d for i in roofs) and T==(1+e)/mu-1
        out.append({'epsilon':e,'body':p,'bottom_root':root,'roof_pair':roofs,'roof_pair_trace':T,
                    'individual_roof_mass':d})
    cube=hull([(x,y,z) for x in (-1,1) for y in (-1,1) for z in (0,1)])
    root=with_plane(cube,(0,0,-1,0)); top=with_plane(cube,(0,0,1,1))
    assert cube['Lambda'][root][top]==1 and cube['d'][top]==F(1,2)
    return {'sequence':out,'limit_cube':cube,'limit_pair_trace':F(1),
            'limit_individual_roof_mass':F(1,4),'limit_full_root_face_mass':F(1,2)}
def encode(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,dict): return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [encode(v) for v in x]
    return x

def main():
    assert len(sys.argv)==2 and sys.argv[1] in ('build','check')
    eq,n=equality_controls()
    obj={'identity':'LOWER_HIGH_TRACE_UNIFORM_SEPARATION_V1','identities':exact_identities(),
         'equality_controls':eq,'equality_pair_count':n,'high_trace_controls':high_trace_controls(),
         'merging_controls':merging_controls(),
         'uniform_delta_status':'Existence proved analytically; no numerical uniform delta is computed here.'}
    raw=(json.dumps(encode(obj),sort_keys=True,indent=2)+'\n').encode('utf-8')
    path=Path('lower_stability_controls.json')
    if sys.argv[1]=='build': path.write_bytes(raw)
    else: assert path.read_bytes()==raw
    print('LOWER_STABILITY_ENDPOINT_IDENTITIES_PASS 7')
    print('LOWER_STABILITY_EQUALITY_CONTROLS_PASS',len(eq),n)
    print('LOWER_STABILITY_HIGH_TRACE_NONVACUITY_PASS 2')
    print('LOWER_STABILITY_TRUE_E17_NOT_110_PASS 10 17 9 5 5 8')
    print('LOWER_STABILITY_MERGING_ROOT_MASS_PASS 4 1/4 1/2')
    print('LOWER_STABILITY_RECOVERY_PASS',len(raw),hashlib.sha256(raw).hexdigest())
    print('NO_NUMERICAL_UNIFORM_GAP_NO_NEW_COMPLEXITY_BOUND')
if __name__=='__main__': main()
