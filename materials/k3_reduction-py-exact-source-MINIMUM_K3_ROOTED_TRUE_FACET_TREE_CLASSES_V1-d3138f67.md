# material-d3138f67a9a6

AI research material

---

"""Exact rooted facet/tree classes of the accepted K3 open register.
python -S k3_reduction.py build | check
Requires only the exact k3_census.py and its complete k3_domains.json.
Rooted map equality is checked by literal vertex/facet/tree transport.
"""
from pathlib import Path
import hashlib,json,sys
from collections import Counter
HERE=Path(__file__).resolve().parent
PINS={'k3_census.py':(13141,'9d87d21a211545b6174a755b75feda6620e3df8ac4074f0e4703cc51bb9be68a'),
      'k3_domains.json':(2724409,'f0fae254b43adff66173b78de6f77853370253113b1d331e6f45c9c94ec85ed6')}
for name,want in PINS.items():
    b=(HERE/name).read_bytes();assert (len(b),hashlib.sha256(b).hexdigest())==want
import k3_census as C

def canonical(row,root):
    rot=C.rotations(row['facet_cycles']);marked=frozenset(map(tuple,row['tree_edges']))
    candidates=[C.rooted_code(rot,root,v,s,marked) for v in rot[root] for s in (1,-1)]
    return min(candidates)

def transport(source,target,a,b,root_source,root_target):
    inv={v:i for i,v in enumerate(b)};p=[inv[v] for v in a]
    assert sorted(p)==list(range(10)) and p[root_source]==root_target
    assert {C.edge(p[x],p[y]) for x,y in source['edges']}==set(map(tuple,target['edges']))
    assert {C.edge(p[x],p[y]) for x,y in source['tree_edges']}==set(map(tuple,target['tree_edges']))
    target_faces={tuple(sorted(f)):i for i,f in enumerate(target['facet_cycles'])}
    fperm=[];orientation=[]
    for face in source['facet_cycles']:
        image=tuple(p[v] for v in face);f=target_faces[tuple(sorted(image))];fperm.append(f)
        dest=target['facet_cycles'][f]
        if C.cyc(image)==C.cyc(dest):orientation.append(1)
        else:assert C.cyc(image)==C.cyc(tuple(reversed(dest)));orientation.append(-1)
    assert sorted(fperm)==list(range(9)) and len(set(orientation))==1
    for v,inc in enumerate(source['incidence']):
        assert sorted(fperm[f] for f in inc)==target['incidence'][p[v]]
    return p,fperm,orientation[0]

def local_control():
    y=((1,0),(1,3),(-8,6),(-33,-24));w=(60,14,1,2)
    assert all(sum(w[i]*y[i][j] for i in range(4))==0 for j in range(2))
    arrows=[[sum(a*b for a,b in zip(y[i],y[j]))-sum(a*a for a in y[i]) for j in range(4)] for i in range(4)]
    expected=[[0,0,-9,-34],[-9,0,0,-115],[-108,-90,0,20],[-1698,-1770,-1545,0]]
    assert arrows==expected
    turns=[];origin=[]
    for i in range(4):
        a,b,c=y[i],y[(i+1)%4],y[(i+2)%4]
        turns.append((b[0]-a[0])*(c[1]-b[1])-(b[1]-a[1])*(c[0]-b[0]))
        origin.append(a[0]*b[1]-a[1]*b[0])
    assert turns==[27,345,420,102] and origin==[3,30,390,24]
    return {'identity':'LOCAL_QUADRIVALENT_UNSTABLE_POLE_PATH_NOT_OWN_CENTROID_BODY',
            'y':y,'x':(0,0,1),'weights':w,'arrows':arrows,'turns':turns,'origin_areas':origin}

def build():
    d=json.loads((HERE/'k3_domains.json').read_text());assert d['identity']=='MINIMUM_TREE253_K3_LITERAL_DOMAINS_V1'
    rows=d['rows'];groups={}
    for row in rows:
        for q in row['roots']:
            if q['status']!='open':continue
            key,labels=canonical(row,q['vertex'])
            groups.setdefault(key,[]).append((row['k3_index'],q['vertex'],labels))
    classes=[]
    for group in sorted(groups.values(),key=lambda g:min((i,r) for i,r,_ in g)):
        group=sorted(group);i,r,a=group[0];source=rows[i];members=[]
        for j,s,b in group:
            p,f,o=transport(source,rows[j],a,b,r,s)
            assert source['roots'][r]['tree_index']==rows[j]['roots'][s]['tree_index']
            members.append({'k3_index':j,'root':s,'vertex_map':p,'facet_map':f,'orientation':o})
        classes.append({'class_index':len(classes),'representative':[i,r],
                        'kind':source['kind'],'tree_index':source['roots'][r]['tree_index'],
                        'members':members})
    assert sum(len(c['members']) for c in classes)==11743
    seen={(m['k3_index'],m['root']) for c in classes for m in c['members']};assert len(seen)==11743
    data={'identity':'MINIMUM_K3_ROOTED_TRUE_FACET_TREE_CLASSES_V1','classes':classes}
    summary={'identity':data['identity'],'positions':11743,'classes':len(classes),
             'class_kinds':dict(sorted(Counter(c['kind'] for c in classes).items())),
             'class_trees':dict(sorted(Counter(c['tree_index'] for c in classes).items())),
             'multiplicities':dict(sorted(Counter(len(c['members']) for c in classes).items())),
             'scope':'Only true rooted facet/tree isomorphism; full pole labels need not be fixed. No new exclusion.'}
    print('K3_EXACT_ROOTED_FACET_TREE_CLASSES',summary,flush=True)
    return {'k3_classes.json':C.enc(data),'k3_classes_summary.json':C.enc(summary),
            'k3_quadrivalent_local_control.json':C.enc(local_control())}

def main():
    assert sys.argv[1:] in (['build'],['check'])
    for name,data in build().items():
        p=HERE/name
        if sys.argv[1]=='check' or p.exists():assert p.read_bytes()==data,('OUTPUT_MISMATCH',name)
        else:p.write_bytes(data)
        print('K3_REDUCTION_EXACT_OUTPUT',name,*C.pin(data),flush=True)
    print('K3_ROOTED_TRANSPORT_AND_LOCAL_POLE_CONTROL_PASS',flush=True)
if __name__=='__main__':main()
