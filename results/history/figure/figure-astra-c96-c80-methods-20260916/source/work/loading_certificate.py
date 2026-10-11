"""Exact-leaf branch certificate search for fixed-body monostable loading.

LPs only propose pruning. Each pruning leaf requires an independently checked
nonnegative rational dual identity; an unfinished tree proves nothing globally.
"""
import argparse,hashlib,itertools,json,time
from fractions import Fraction as F
from math import gcd
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from geometry import write_json


def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def solve(a,b):
    m=[list(map(F,row))+[F(rhs)]for row,rhs in zip(a,b)];n=len(b)
    for i in range(n):
        k=next((j for j in range(i,n) if m[j][i]),None)
        if k is None:return None
        m[i],m[k]=m[k],m[i];d=m[i][i];m[i]=[v/d for v in m[i]]
        for j in range(n):
            if j!=i:
                d=m[j][i];m[j]=[v-d*w for v,w in zip(m[j],m[i])]
    return [row[-1]for row in m]


def inequalities(a):
    p=[tuple(map(F,row))for row in a['raw_vertices']]
    assert all(v.denominator==1 for row in p for v in row)
    p=[tuple(map(int,row))for row in p];scale=max(abs(x)for row in p for x in row)
    rows=[]
    def add(n,b):
        d=gcd(*n,b);n=[x//d for x in n];b//=d
        rows.append([*(x*scale for x in n),max(map(abs,n))*scale,b]);return len(rows)-1
    for n,b in zip(a['normals'],a['offsets']):add(n,int(b))
    facets=[]
    for n,face in zip(a['normals'],a['faces']):
        ids=[]
        for i,j in zip(face,face[1:]+face[:1]):
            edge=[y-x for x,y in zip(p[i],p[j])];k=cross(n,edge)
            ids.append(add(k,dot(k,p[i])))
        facets.append(ids)
    return rows,facets,scale


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',default='work/baseline-check/A.json')
    ap.add_argument('--out',required=True);ap.add_argument('--nodes',type=int,default=5000)
    ap.add_argument('--seconds',type=float,default=55.);args=ap.parse_args()
    source=Path(args.input).read_bytes();a=json.loads(source);rows,facets,scale=inequalities(a)
    ar=np.array(rows,float);ar/=ar[:,3,None];aa=ar[:,:4];bb=ar[:,4]
    base=list(range(a['F']));nodes=[];roots=[];start=time.time();counts=dict(lp=0,certified_leaves=0,unknown=0)
    def visit(ids,root,assigned):
        index=len(nodes);node=dict(rows=ids[len(base):]);nodes.append(node)
        if len(nodes)>args.nodes or time.time()-start>args.seconds:
            node['unfinished']='bounded search budget';counts['unknown']+=1;return index
        lp=linprog([0,0,0,-1],A_ub=aa[ids],b_ub=bb[ids],bounds=[(None,None)]*4,
                   method='highs',options={'threads':1,'primal_feasibility_tolerance':1e-9})
        counts['lp']+=1
        if not lp.success:
            node['unfinished']='LP did not produce usable optimum: '+lp.message;counts['unknown']+=1;return index
        active=[ids[i]for i,v in enumerate(lp.ineqlin.marginals)if v< -1e-10]
        if lp.x[3]<1e-8:
            if len(active)<=4:
                pool=active+[ids[i]for i,v in enumerate(lp.ineqlin.residual)if abs(v)<1e-7 and ids[i]not in active]
            else:pool=active
            for subset in itertools.combinations(pool,4):
                dual=solve([[rows[i][j]for i in subset]for j in range(4)],[0,0,0,1])
                if dual is not None and min(dual)>=0 and sum(v*rows[i][4]for i,v in zip(subset,dual))<=0:
                    node['dual']=[[i,str(v)]for i,v in zip(subset,dual)if v]
                    counts['certified_leaves']+=1;return index
        # Branch on one stable facet, excluding the permitted surviving facet.
        available=[f for f in range(a['F']) if f!=root and f not in assigned]
        violated=[f for f in available if min(aa[facets[f]]@lp.x-bb[facets[f]])> -1e-9]
        if not violated:
            node['unfinished']='positive loading proposal or unresolved numerical boundary'
            node['proposal']=lp.x.tolist();counts['unknown']+=1;return index
        f=max(violated,key=lambda f:(-len(facets[f]),min(aa[facets[f]]@lp.x-bb[facets[f]])))
        node['facet']=f;node['children']=[visit(ids+[i],root,assigned|{f})for i in facets[f]]
        return index
    for root in range(a['F']):
        roots.append(visit(base,root,set()))
        if len(nodes)>args.nodes or time.time()-start>args.seconds:
            break
    report=dict(input=args.input,input_sha256=hashlib.sha256(source).hexdigest(),coordinate_scale=scale,
                all_integer_rows=rows,facet_disjunctions=facets,roots=roots,nodes=nodes,counts=counts,
                elapsed=time.time()-start,complete=len(roots)==a['F']and counts['unknown']==0)
    write_json(args.out,report)
    print('LOADING_BRANCH_SEARCH',report['complete'],len(nodes),counts,report['elapsed'],flush=True)


if __name__=='__main__':main()
