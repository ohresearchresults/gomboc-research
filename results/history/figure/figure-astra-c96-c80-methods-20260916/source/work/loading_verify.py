"""Standard-library-only verification of a complete loading exclusion tree."""
import argparse,hashlib,json
from fractions import Fraction
from math import gcd
from pathlib import Path


def dual_from_basis(rows,indices):
    """Solve four exact equations in at most four unknown multipliers."""
    n=len(indices);assert 0<n<=4
    matrix=[[Fraction(rows[i][j])for i in indices]+[Fraction(j==3)]for j in range(4)]
    rank=0;pivots=[]
    for col in range(n):
        pivot=next((j for j in range(rank,4)if matrix[j][col]),None)
        assert pivot is not None
        matrix[rank],matrix[pivot]=matrix[pivot],matrix[rank]
        divisor=matrix[rank][col];matrix[rank]=[v/divisor for v in matrix[rank]]
        for j in range(4):
            if j!=rank:
                multiplier=matrix[j][col];matrix[j]=[v-multiplier*w for v,w in zip(matrix[j],matrix[rank])]
        pivots.append((rank,col));rank+=1
    assert all(not any(row[:n]) and row[n]==0 for row in matrix[rank:])
    answer=[Fraction(0)]*n
    for row,col in pivots:answer[col]=matrix[row][-1]
    return list(zip(indices,answer))


def main():
    ap=argparse.ArgumentParser();ap.add_argument('certificate');ap.add_argument('audit')
    ap.add_argument('--out');args=ap.parse_args()
    source=Path(args.audit).read_bytes();a=json.loads(source)
    binary=Path(args.certificate).read_bytes();c=json.loads(binary)
    assert hashlib.sha256(source).hexdigest()==c['input_sha256']
    assert c['complete'] and len(c['roots'])==a['F']
    points=[[Fraction(v)for v in p]for p in a['raw_vertices']]
    assert all(v.denominator==1 for p in points for v in p)
    points=[list(map(int,p))for p in points]
    scale=max(abs(v)for p in points for v in p);assert scale==c['coordinate_scale']
    rows=[];facets=[]
    def append(n,h):
        div=gcd(*n,h);n=[v//div for v in n];h//=div
        rows.append([n[0]*scale,n[1]*scale,n[2]*scale,max(abs(v)for v in n)*scale,h])
        return len(rows)-1
    for n,h in zip(a['normals'],a['offsets']):append(n,int(h))
    for face,n in zip(a['faces'],a['normals']):
        indices=[]
        for i,j in zip(face,face[1:]+face[:1]):
            e=[points[j][k]-points[i][k]for k in range(3)]
            k=[n[1]*e[2]-n[2]*e[1],n[2]*e[0]-n[0]*e[2],n[0]*e[1]-n[1]*e[0]]
            indices.append(append(k,sum(k[t]*points[i][t]for t in range(3))))
        facets.append(indices)
    compact=c.get('format')=='dag_row_basis_v1'
    if not compact:assert rows==c['all_integer_rows'] and facets==c['facet_disjunctions']
    seen=set();leaves=0;negative_bounds=0;maximum_depth=0;expanded=0
    def verify(index,root,path,assigned):
        nonlocal leaves,negative_bounds,maximum_depth,expanded
        if not compact:assert index not in seen
        seen.add(index);expanded+=1;maximum_depth=max(maximum_depth,len(path))
        node=c['nodes'][index]
        if compact:
            node={'dual':dual_from_basis(rows,node[1])}if node[0]=='L'else{'facet':node[1],'children':node[2]}
        else:assert node['rows']==path and 'unfinished'not in node
        if 'dual'in node:
            ids=list(range(a['F']))+path;acc=[Fraction(0)for _ in range(5)]
            for row,weight in node['dual']:
                weight=Fraction(weight);assert weight>0 and row in ids
                for j in range(5):acc[j]+=weight*rows[row][j]
            assert acc[:4]==[0,0,0,1] and acc[4]<=0
            leaves+=1;negative_bounds+=int(acc[4]<0);return
        face=node['facet'];assert face!=root and face not in assigned
        assert 0<=face<a['F'] and len(node['children'])==len(facets[face])
        for child,row in zip(node['children'],facets[face]):
            verify(child,root,path+[row],assigned|{face})
    for root,index in enumerate(c['roots']):verify(index,root,[],set())
    assert len(seen)==len(c['nodes'])
    report=dict(status='EXACT_ALL_INTERIOR_LOADING_EXCLUSION_PASS',audit_sha256=c['input_sha256'],
                certificate_sha256=hashlib.sha256(binary).hexdigest(),roots=a['F'],nodes=len(seen),
                leaves=leaves,expanded_nodes=expanded,strictly_negative_dual_bounds=negative_bounds,maximum_depth=maximum_depth,
                conclusion='For this fixed C96 shape every interior reference point has at least two stable-or-weak maximal facets. In particular no reference point gives nondegenerate S=1. No claim for affine or non-affine changes of shape.')
    if args.out:Path(args.out).write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
    print(json.dumps(report,sort_keys=True,indent=2))


if __name__=='__main__':main()
