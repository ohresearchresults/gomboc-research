"""Finite noncritical homogeneous cap insertions with whole-body own-census checks."""
import argparse,hashlib,itertools,json
from pathlib import Path
import numpy as np
from geometry import census,mass,write_json


def main():
    ap=argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('output')
    ap.add_argument('--caps',type=int,default=4);ap.add_argument('--height',type=float,default=.0001)
    args=ap.parse_args();data=Path(args.input).read_bytes();p=np.array(json.loads(data)['points'],float)
    p-=mass(p)[1];p/=max(np.linalg.norm(p,axis=1));recipes=[];tested=0
    initial=census(p);assert initial['U']==1 and initial['S_uncertain']==initial['U_uncertain']==0
    original_count=len(p);used=[]
    for cap in range(args.caps):
        r=census(p,True);c=np.array(r['centroid']);q=r['q'];rank=[]
        for f,group in enumerate(r['groups']):
            ids=r['hull'].simplices[group[0]]
            if f in r['stable'] or max(ids)>=original_count or tuple(sorted(ids)) in used:
                continue
            tri=p[ids];area=np.linalg.norm(np.cross(tri[1]-tri[0],tri[2]-tri[0]))
            rank.append((-area,f,ids))
        accepted=False
        for _,f,ids in sorted(rank,key=lambda item:item[0]):
            normal=q[f]/np.linalg.norm(q[f])
            for weights in itertools.permutations([.6,.25,.15]):
                foot=np.array(weights)@p[ids]
                slacks=1-q@(foot-c);slopes=q@normal
                eligible=[j for j in range(len(q)) if j!=f and slopes[j]>0]
                height=min([args.height]+[.45*slacks[j]/slopes[j] for j in eligible])
                if height<1e-8:
                    continue
                candidate=np.r_[p,(foot+height*normal)[None,:]];tested+=1
                rr=census(candidate)
                if rr['S']==initial['S'] and rr['U']==1 and rr['S_uncertain']==rr['U_uncertain']==0:
                    p=candidate;used.append(tuple(sorted(ids)));accepted=True
                    recipes.append(dict(face_points=ids.tolist(),weights=list(weights),height=float(height),normal=normal.tolist()))
                    break
            if accepted:
                break
        if not accepted:
            break
    result=dict(input=args.input,input_sha256=hashlib.sha256(data).hexdigest(),config=vars(args),
                actual_caps=len(recipes),tested=tested,recipes=recipes,points=p.tolist(),census=census(p))
    write_json(args.output,result)
    print('NONCRITICAL_CAP_INSERTIONS',len(recipes),tested,result['census']['S'],result['census']['U'],result['census']['E_proposal'])


if __name__=='__main__':
    main()
