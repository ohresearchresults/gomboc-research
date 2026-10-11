"""Screen returned reference centres; these are NEVER own-mass claims."""
import argparse,json
from fractions import Fraction
from pathlib import Path
import numpy as np
from geometry import escape_table,write_json


def main():
    ap=argparse.ArgumentParser();ap.add_argument('search');ap.add_argument('audit');ap.add_argument('output')
    args=ap.parse_args();d=json.loads(Path(args.search).read_text());a=json.loads(Path(args.audit).read_text())
    p=np.array([[float(Fraction(v))for v in row]for row in a['raw_vertices']])
    n=np.array(a['normals'],float);h=np.array(a['offsets'],float)
    own=np.array([float(Fraction(v))for v in a['raw_centroid']]);scale=d['coordinate_scale'];rows=[]
    for i,node in enumerate(d['nodes']):
        prop=node.get('proposal')
        if prop is None or prop[-1]<=1e-8:continue
        g=np.array(prop[:3])*scale;x=p-g;dist=h-n@g
        if min(dist)<=0:continue
        q=n/dist[:,None];ue=escape_table(x).max(axis=1);se=escape_table(q).max(axis=1)
        rows.append(dict(node=i,reference=g.tolist(),reference_S=int(sum(se< -1e-9)),
                         reference_U=int(sum(ue< -1e-9)),S_uncertain=int(sum(abs(se)<=1e-9)),
                         U_uncertain=int(sum(abs(ue)<=1e-9)),centre_displacement=float(np.linalg.norm(g-own)/scale)))
    write_json(args.output,dict(input=args.search,rows=rows,own_centroid=own.tolist(),warning='All counts are about a chosen reference, not the homogeneous volume centroid.'))
    print('REFERENCE_LOADING_PROPOSALS',len(rows),sorted({(r['reference_S'],r['reference_U'])for r in rows}),
          'closest',sorted(rows,key=lambda r:r['centre_displacement'])[:2])


if __name__=='__main__':main()
