"""Rational physical patch/projective/affine construction from an exact parent.

Only transformation constants are rounded. Every source rational point and
every coplanarity that its affine/projective piece preserves is retained.
Exact supporting-plane tests and nativeB's complete bounded H-hull must prove
that every actual vertex belongs to the literal transformed point set.
"""
import sys,json,hashlib,itertools
from pathlib import Path
from math import gcd,lcm
import numpy as np
from scipy.spatial import ConvexHull
from gmpy2 import mpq as Q
from support_persistence import ROOT
sys.set_int_max_str_digits(0)
sys.path.insert(0,str(ROOT/'sources/full76/decoded/methods/parent'))
import check_B
check_B.Q=Q

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def blob(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()

def run(folder,out,name='best.json',grid=10**14):
    folder=Path(folder);out=Path(out);out.mkdir(parents=True,exist_ok=False)
    source_bytes=(folder/'source.json').read_bytes();candidate_bytes=(folder/name).read_bytes()
    meta=json.loads(source_bytes);row=json.loads(candidate_bytes);src=Path(meta['source']);source=src.read_bytes();old=json.loads(source)
    if hashlib.sha256(source).hexdigest()!=meta.get('source_sha256',meta.get('sha256')):raise ValueError('source hash changed')
    rational=lambda x:Q(int(round(float(x)*grid)),grid)
    c=tuple(map(rational,meta['center']));radius=rational(meta['radius']);assert radius>0
    tr=row.get('transform',dict(normal=row.get('normal'),cut_offset=row['t'][3],patch_vector=row['t'][:3],projective_B=[0,0,0],affine_L=np.eye(3).tolist()))
    n=tuple(map(rational,tr['normal']));d=rational(tr['cut_offset']);a=tuple(map(rational,tr['patch_vector']));b=tuple(map(rational,tr['projective_B']));L=[tuple(map(rational,r)) for r in tr['affine_L']]
    assert dot(L[0],cross(L[1],L[2]))!=0
    X=[];pieces=[];dens=[]
    for raw in old['raw_vertices']:
        p=tuple((Q(x)-z)/radius for x,z in zip(raw,c));height=max(Q(0),dot(n,p)-d);pieces.append(int(height>0));p=tuple(x+height*y for x,y in zip(p,a));den=1+dot(b,p);assert den>0;dens.append(den);p=tuple(x/den for x in p);X.append(tuple(sum(p[i]*L[i][j] for i in range(3)) for j in range(3)))
    approx=np.array([[float(x) for x in p] for p in X]);qh=ConvexHull(approx);center=tuple(map(rational,np.mean(approx[qh.vertices],axis=0)));P=[sub(p,center) for p in X]
    planes=set();bad=[]
    def add_plane(ids,origin):
        aa,bb,cc=[P[i] for i in ids];nn=cross(sub(bb,aa),sub(cc,aa));hh=dot(nn,aa)
        if nn==(0,0,0):return
        signs=[dot(nn,p)-hh for p in P]
        if max(signs)<=0:pass
        elif min(signs)>=0:nn=tuple(-v for v in nn);hh=-hh
        else:
            if origin=='qhull':bad.append(list(map(int,ids)))
            return
        assert hh>0,'declared rational interior origin is not inside'
        den=lcm(*(int(v.denominator) for v in (*nn,hh)));ints=[int(v*den) for v in (*nn,hh)];gg=gcd(*ints);planes.add(tuple(v//gg for v in ints))
    for ids in qh.simplices:add_plane(ids,'qhull')
    # Inherited true facet pieces are explicitly supplied, even when a tiny
    # triangle on them was omitted by floating Qhull.
    for f in old['faces']:
        for side in [0,1]:
            ids=[i for i in f if pieces[i]==side]
            for tri in itertools.combinations(ids,3):
                aa,bb,cc=[P[i] for i in tri]
                if cross(sub(bb,aa),sub(cc,aa))!=(0,0,0):add_plane(tri,'old-facet-piece');break
    body={'H':[list(p) for p in sorted(planes)]}
    (out/'source.json').write_bytes(source_bytes);(out/'nominated_transform.json').write_bytes(candidate_bytes)
    construction=dict(source=str(src),source_sha256=hashlib.sha256(source).hexdigest(),candidate_sha256=hashlib.sha256(candidate_bytes).hexdigest(),grid=grid,pretranslation=list(map(str,c)),prescale_radius=str(radius),patch_normal=list(map(str,n)),patch_offset=str(d),patch_vector=list(map(str,a)),projective_B=list(map(str,b)),affine_L=[[str(v) for v in r] for r in L],posttranslation_interior=list(map(str,center)),physical_points=[[str(v) for v in p] for p in P],piece_membership=pieces,minimum_projective_denominator=str(min(dens)),invalid_qhull_triples=bad,nomination_counts={k:row[k] for k in ['V','E','F','S','U']})
    (out/'construction.json').write_bytes(blob(construction));(out/'H.json').write_bytes(blob(body));print('EXACT_PATCH_PLANES',len(planes),'bad_proposals',len(bad),flush=True)
    r=check_B.run(body);actual={tuple(map(Q,p)) for p in r['raw_vertices']}
    if not actual<=set(P):
        (out/'H_HULL_NOT_LITERAL_HULL.json').write_text(json.dumps(dict(unexpected_vertices=len(actual-set(P)),invalid_qhull_triples=bad),indent=2)+'\n');raise ValueError('exact H hull is not proven equal to literal transformed hull')
    assert all(dot(h[:3],p)<=h[3] for h in body['H'] for p in P)
    (out/'audit.json').write_bytes(blob(r));summary={k:r[k] for k in ['V','E','F','counts','weak','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};summary.update(C2E=2*r['E'],VplusEplusF=r['V']+r['E']+r['F'],audit_sha256=hashlib.sha256(blob(r)).hexdigest(),goal_candidate=(r['counts']==[1,1,0] and r['weak']==[0,0,0] and 17<=r['E']<=248));(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print('EXACT_PHYSICAL_PATCH',summary,flush=True);return r

if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],sys.argv[3] if len(sys.argv)>3 else 'best.json')
