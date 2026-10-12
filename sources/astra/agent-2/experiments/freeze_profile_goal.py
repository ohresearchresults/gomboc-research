"""Complete rational physical freeze and native independent A/B goal audit.
Each shared horizontal normal is frozen once as its exact binary64 rational
components. Retained support heights and section levels are exact dyadics;
all dependent heights and physical vertices are then derived rationally.
Uniform volume and centroid are integrated exactly on the genuine facets.
A small dyadic translation merely supplies a positive-offset H representation;
the auditors still compute the body's OWN centroid, without substitution.
"""
import sys,json,hashlib
from pathlib import Path
import numpy as np
from gmpy2 import mpq
from concave_profile_family import ProfileFamily
from freeze_triangle_cap_goal import primitive,encode,check_B,check_A

def dot(a,b):return sum((x*y for x,y in zip(a,b)),mpq(0))
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]

def run(source,metadata,out):
    source=Path(source);metadata=Path(metadata);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=source.read_bytes();mr=metadata.read_bytes();(out/'controls.npy').write_bytes(raw);(out/'source_metadata.json').write_bytes(mr);values=np.load(out/'controls.npy');meta=json.loads(mr);m,L=int(meta['m']),int(meta['L']);breaks=meta['breaks'];fam=ProfileFamily(m,L,breaks);K=fam.K
    if len(values)!=K+L+m or not np.isfinite(values).all():raise ValueError('invalid exact profile input controls')
    controls=[mpq(float(x)) for x in values[:K]];z=[mpq(float(x)) for x in values[K:K+L]]+[mpq(1)];n=[[mpq(float(np.cos(t))),mpq(float(np.sin(t)))] for t in values[-m:]];h=[[mpq(0) for i in range(m)] for k in range(L+1)]
    for i,bb in enumerate(breaks):
        full=bb+[L];v=controls[fam.offset[i]:fam.offset[i+1]]+[mpq(0)]
        for j,(a,b) in enumerate(zip(full[:-1],full[1:])):
            for k in range(a,b):
                t=(z[k]-z[a])/(z[b]-z[a]);h[k][i]=(1-t)*v[j]+t*v[j+1]
    allX=[]
    for k in range(L):
        for i in range(m):
            j=(i+1)%m;det=n[i][0]*n[j][1]-n[i][1]*n[j][0]
            if det<=0:raise ValueError('frozen shared normal directions are not strictly ordered')
            allX.append([(h[k][i]*n[j][1]-n[i][1]*h[k][j])/det,(n[i][0]*h[k][j]-h[k][i]*n[j][0])/det,z[k]])
    allX.append([mpq(0),mpq(0),mpq(1)]);X=[allX[int(i)] for i in fam.kept];planes=[]
    for i,a,b in fam.segments:
        slope=(h[b][i]-h[a][i])/(z[b]-z[a]);planes.append([*n[i],-slope,h[a][i]-slope*z[a]])
    planes.append([mpq(0),mpq(0),mpq(-1),-z[0]])
    for j,row in enumerate(planes):
        face=set(fam.faces[j])
        for i,x in enumerate(X):
            gap=row[3]-dot(row[:3],x)
            if (i in face and gap!=0) or (i not in face and gap<=0):raise ValueError('exact frozen profile loses a declared maximal facet or genuine vertex')
    six=mpq(0);numerator=[mpq(0)]*3
    for tri in fam.T:
        a,b,c=[X[int(i)] for i in tri];v=dot(a,cross(b,c));six+=v
        for j in range(3):numerator[j]+=v*(a[j]+b[j]+c[j])
    if six<=0:raise ValueError('exact physical volume is not positive')
    volume=six/6;centroid=[v/(4*six) for v in numerator];translation=[mpq(float(v)) for v in centroid];shifted=[[x[j]-translation[j] for j in range(3)] for x in X];own_centroid=[centroid[j]-translation[j] for j in range(3)];rows=[]
    for row in planes:
        d=row[3]-dot(row[:3],translation)
        if d<=0:raise ValueError('dyadic coordinate translation is not strictly interior')
        rows.append(primitive([*row[:3],d]))
    body={'H':sorted(set(rows))};(out/'H.json').write_bytes(encode(body));construction=dict(method=__doc__,source=str(source),source_sha256=hashlib.sha256(raw).hexdigest(),metadata_source=str(metadata),metadata_sha256=hashlib.sha256(mr).hexdigest(),m=m,L=L,breaks=breaks,shared_normal_components=[[str(x) for x in a] for a in n],retained_support_values=list(map(str,controls)),levels=list(map(str,z)),full_section_supports=[[str(x) for x in a] for a in h],translation=list(map(str,translation)),physical_vertices=[[str(x) for x in a] for a in shifted],maximal_facets=fam.faces,edges=fam.eu.tolist(),uniform_volume=str(volume),own_volume_centroid=list(map(str,own_centroid)),C2E=2*fam.E,VplusEplusF=fam.V+fam.E+fam.F)
    (out/'construction_exact.json').write_text(json.dumps(construction,indent=2)+'\n');B=check_B.run(body);(out/'audit_B.json').write_bytes(encode(B));got={tuple(mpq(v) for v in p) for p in B['raw_vertices']};expected={tuple(p) for p in shifted}
    if got!=expected or mpq(B['ordinary_volume'])!=volume or [mpq(x) for x in B['raw_centroid']]!=own_centroid:raise ValueError('native B hull or actual uniform mass differs from the rational physical construction')
    qualified=B['counts']==[1,1,0] and B['weak']==[0,0,0] and 34<=2*B['E']<500;result={k:B[k] for k in ['V','E','F','counts','weak','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};result.update(C2E=2*B['E'],VplusEplusF=B['V']+B['E']+B['F'],B_qualified=qualified,independent_A_qualified=False,audit_B_sha256=hashlib.sha256(encode(B)).hexdigest());(out/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
    if qualified:
        A=check_A.run(body);(out/'audit_A.json').write_bytes(encode(A));different=[k for k in set(A)|set(B) if A.get(k)!=B.get(k)];(out/'independent_comparison.json').write_text(json.dumps(dict(differing_fields=different),indent=2)+'\n')
        if different:raise ValueError('independent native exact audits disagree')
        result.update(independent_A_qualified=True,audit_A_sha256=hashlib.sha256(encode(A)).hexdigest());(out/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
    print('EXACT_PROFILE_GOAL_AUDIT',result,flush=True);return result

if __name__=='__main__':run(sys.argv[1],sys.argv[2],sys.argv[3])
