"""Exact rational freeze of full or sparse independently tilted sections.
Shared bottom directions are frozen once as exact dyadic components. Every
later normal, support, vertex, volume and centroid follows by rational plane
recursion on that one physical body. Native B checks the complete own-centroid
strict/weak census; native A independently checks only a B qualifier.
"""
import sys,json,hashlib
from pathlib import Path
import numpy as np
from gmpy2 import mpq
from concave_profile_family import ProfileFamily
from freeze_profile_goal import dot,cross,primitive,encode,check_B,check_A

def run(source,metadata,out):
    source=Path(source);metadata=Path(metadata);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=source.read_bytes();mr=metadata.read_bytes();(out/'controls.npy').write_bytes(raw);(out/'source_metadata.json').write_bytes(mr);a=np.load(out/'controls.npy');meta=json.loads(mr);m,L=int(meta['m']),int(meta['L']);sparse='breaks' in meta;breaks=meta.get('breaks',[list(range(L)) for i in range(m)]);topology=ProfileFamily(m,L,breaks);q=[mpq(float(v)) for v in a];K=topology.K if sparse else m*L
    if len(a)!=K+3*L+m or not np.isfinite(a).all():raise ValueError('invalid tilted physical control layout')
    z=q[K:K+L];tilt=[q[K+L+2*k:K+L+2*k+2] for k in range(L)];n0=[[mpq(float(np.cos(t))),mpq(float(np.sin(t)))] for t in a[-m:]];h0=[];free=[]
    for i in range(m):
        if sparse:
            offset=topology.offset[i];h0.append(q[offset]);free.append(q[offset+1:topology.offset[i+1]])
        else:h0.append(q[i]);free.append([q[m+k*m+i] for k in range(L-1)])
    ns=[];hs=[];ss=[];h=h0.copy();n=[p.copy() for p in n0];last=[None]*m
    for k in range(L):
        slope=[]
        for i in range(m):
            j=max(j for j,t in enumerate(breaks[i]) if t<=k)
            if j<len(breaks[i])-1:value=free[i][j]
            else:
                if k==breaks[i][-1]:last[i]=h[i]/(1-z[k])
                value=last[i]
            slope.append(value)
        ns.append([p.copy() for p in n]);hs.append(h.copy());ss.append(slope.copy())
        if k<L-1:
            n=[[n[i][j]+slope[i]*(tilt[k+1][j]-tilt[k][j]) for j in range(2)] for i in range(m)];h=[h[i]-slope[i]*(z[k+1]-z[k]) for i in range(m)]
    fullX=[]
    for k in range(L):
        for i in range(m):
            j=(i+1)%m;det=ns[k][i][0]*ns[k][j][1]-ns[k][i][1]*ns[k][j][0]
            if det<=0:raise ValueError('exact tilted section normal directions change order')
            x=(hs[k][i]*ns[k][j][1]-ns[k][i][1]*hs[k][j])/det;y=(ns[k][i][0]*hs[k][j]-hs[k][i]*ns[k][j][0])/det;fullX.append([x,y,z[k]+tilt[k][0]*x+tilt[k][1]*y])
    fullX.append([mpq(0),mpq(0),mpq(1)]);X=[fullX[int(i)] for i in topology.kept];planes=[]
    for i,start,end in topology.segments:
        slope=ss[start][i];planes.append([ns[start][i][0]-slope*tilt[start][0],ns[start][i][1]-slope*tilt[start][1],slope,hs[start][i]+slope*z[start]])
    planes.append([tilt[0][0],tilt[0][1],mpq(-1),-z[0]])
    for j,row in enumerate(planes):
        face=set(topology.faces[j])
        for i,x in enumerate(X):
            gap=row[3]-dot(row[:3],x)
            if (i in face and gap!=0) or (i not in face and gap<=0):raise ValueError('exact tilted body fails complete maximal-facet incidence')
    six=mpq(0);numerator=[mpq(0)]*3
    for tri in topology.T:
        aa,bb,cc=[X[int(i)] for i in tri];v=dot(aa,cross(bb,cc));six+=v
        for j in range(3):numerator[j]+=v*(aa[j]+bb[j]+cc[j])
    if six<=0:raise ValueError('exact tilted volume is not positive')
    volume=six/6;centroid=[v/(4*six) for v in numerator];translation=[mpq(float(v)) for v in centroid];shifted=[[x[j]-translation[j] for j in range(3)] for x in X];own_centroid=[centroid[j]-translation[j] for j in range(3)];rows=[]
    for row in planes:
        d=row[3]-dot(row[:3],translation)
        if d<=0:raise ValueError('exact dyadic coordinate translation is not interior')
        rows.append(primitive([*row[:3],d]))
    body={'H':sorted(set(rows))};(out/'H.json').write_bytes(encode(body));construction=dict(method=__doc__,source=str(source),source_sha256=hashlib.sha256(raw).hexdigest(),metadata_source=str(metadata),metadata_sha256=hashlib.sha256(mr).hexdigest(),m=m,L=L,breaks=breaks,bottom_normal_components=[[str(x) for x in v] for v in n0],bottom_supports=list(map(str,h0)),free_vertical_coefficients=[[str(x) for x in v] for v in free],levels=list(map(str,z)),section_tilts=[[str(x) for x in v] for v in tilt],translation=list(map(str,translation)),physical_vertices=[[str(x) for x in v] for v in shifted],maximal_facets=topology.faces,edges=topology.eu.tolist(),uniform_volume=str(volume),own_volume_centroid=list(map(str,own_centroid)),C2E=2*topology.E,VplusEplusF=topology.V+topology.E+topology.F)
    (out/'construction_exact.json').write_text(json.dumps(construction,indent=2)+'\n');B=check_B.run(body);(out/'audit_B.json').write_bytes(encode(B));got={tuple(mpq(v) for v in p) for p in B['raw_vertices']};expected={tuple(p) for p in shifted}
    if got!=expected or mpq(B['ordinary_volume'])!=volume or [mpq(v) for v in B['raw_centroid']]!=own_centroid:raise ValueError('native exact hull/mass differs from the rational tilted physical construction')
    qualified=B['counts']==[1,1,0] and B['weak']==[0,0,0] and 34<=2*B['E']<500;result={k:B[k] for k in ['V','E','F','counts','weak','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};result.update(C2E=2*B['E'],VplusEplusF=B['V']+B['E']+B['F'],B_qualified=qualified,independent_A_qualified=False,audit_B_sha256=hashlib.sha256(encode(B)).hexdigest());(out/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
    if qualified:
        A=check_A.run(body);(out/'audit_A.json').write_bytes(encode(A));different=[k for k in set(A)|set(B) if A.get(k)!=B.get(k)];(out/'independent_comparison.json').write_text(json.dumps(dict(differing_fields=different),indent=2)+'\n')
        if different:raise ValueError('independent native exact auditors disagree')
        result.update(independent_A_qualified=True,audit_A_sha256=hashlib.sha256(encode(A)).hexdigest());(out/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
    print('EXACT_TILTED_GOAL_AUDIT',result,flush=True);return result

if __name__=='__main__':run(sys.argv[1],sys.argv[2],sys.argv[3])
