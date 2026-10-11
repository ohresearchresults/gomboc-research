"""Exact arbitrary-reference census, explicitly NOT the homogeneous own census."""
import hashlib,json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def scale(t,a):return tuple(t*x for x in a)
def sign(x):return(x>0)-(x<0)


def main():
    data=(ROOT/'work/pyramid-101-exact/A.json').read_bytes()
    assert hashlib.sha256(data).hexdigest()=='f17bb48815e8ff86697936d33af34e8e28170808674e9149dbae23c5228a19f7'
    a=json.loads(data);g=(7695683,168054,-75622586)
    p=[tuple(map(F,row))for row in a['raw_vertices']];x=[sub(v,g)for v in p]
    sf=[];sw=[];uv=[];uw=[];eh=[];ew=[];edge_faces={};adj=[set()for _ in p];zero=0
    for f,face in enumerate(a['faces']):
        n=tuple(a['normals'][f]);hc=F(a['offsets'][f])-dot(n,g);assert hc>0
        foot=tuple(v+w for v,w in zip(g,scale(hc/dot(n,n),n)))
        first=[];second=[]
        for i,j in zip(face,face[1:]+face[:1]):
            e=sub(p[j],p[i]);first.append(sign(dot(n,cross(x[i],e))))
            second.append(sign(dot(n,cross(e,sub(foot,p[i])))))
            edge_faces.setdefault(tuple(sorted((i,j))),[]).append(f);adj[i].add(j);adj[j].add(i)
        assert first==second;zero+=first.count(0)
        if min(first)>0:sf.append(f)
        elif min(first)>=0:sw.append(f)
    for i in range(len(p)):
        value=max(dot(x[i],sub(p[j],p[i]))for j in range(len(p))if i!=j)
        neighbor=max(dot(x[i],sub(p[j],p[i]))for j in adj[i]);assert sign(value)==sign(neighbor)
        if value<0:uv.append(i)
        elif value==0:uw.append(i)
    for i,j in a['edges']:
        e=sub(p[j],p[i]);ee=dot(e,e);t=-dot(x[i],e)/ee;z=tuple(v+t*w for v,w in zip(x[i],e))
        n,m=[tuple(a['normals'][f])for f in edge_faces[(i,j)]]
        nn,mm,nm=dot(n,n),dot(m,m),dot(n,m);delta=nn*mm-nm*nm;assert delta>0
        ca=(mm*dot(z,n)-nm*dot(z,m))/delta;cb=(nn*dot(z,m)-nm*dot(z,n))/delta
        first=list(map(sign,[t,1-t,ca,cb]))
        d=cross(n,m);second=list(map(sign,[t,1-t,dot(cross(z,m),d),dot(cross(n,z),d)]))
        assert first==second;zero+=first.count(0)
        if min(first)>0:eh.append([i,j])
        elif min(first)>=0:ew.append([i,j])
    counts=[len(sf),len(uv),len(eh)];weak=[len(sw),len(uw),len(ew)]
    assert counts==[1,1,0] and weak==[0,0,0] and zero==0
    own=tuple(map(F,a['raw_centroid']));moment=scale(F(a['ordinary_volume']),sub(own,g));assert moment!=(0,0,0)
    result=dict(status='EXACT_REFERENCE_110_NOT_HOMOGENEOUS_110',shape='C80_OWN211',
                source_audit_sha256=hashlib.sha256(data).hexdigest(),reference=list(g),reference_counts=counts,
                reference_weak=weak,reference_stable_faces=sf,reference_unstable_vertices=uv,
                reference_saddle_edges=eh,primitive_zero_count=zero,actual_own_counts=a['counts'],
                actual_own_centroid=a['raw_centroid'],nonzero_physical_first_moment_about_reference=list(map(str,moment)),
                conclusion='This C80 shape admits reference110, but the reference is not its homogeneous volume centroid. It remains own211 and is NOT a homogeneous Gomboc.')
    b=json.dumps(result,sort_keys=True,indent=2)+'\n';(ROOT/'work/reference-c80-certificate.json').write_text(b)
    print(b);print('REFERENCE_CERTIFICATE_SHA256',hashlib.sha256(b.encode()).hexdigest())


if __name__=='__main__':main()
