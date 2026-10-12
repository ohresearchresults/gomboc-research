# material-7d3e8927d60d

AI research material

---

#!/usr/bin/env python3
"""Original H5 polynomial on a five-parameter prism; no quadratic lowering.
Current target: one rooted tree. This executable never asserts all-root coverage.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product
from math import comb
import json, hashlib, sys, time, platform
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
DIM=5  # x, r, p, q, lambda
ZERO=(0,)*DIM
class P:
    def __init__(self,x=0):
        if isinstance(x,P): self.d=x.d.copy()
        elif isinstance(x,dict):self.d={k:F(v) for k,v in x.items() if v}
        else:self.d={} if not x else {ZERO:F(x)}
    def __add__(self,b):
        d=self.d.copy()
        for k,v in P(b).d.items():d[k]=d.get(k,F(0))+v
        return P(d)
    __radd__=__add__
    def __neg__(self):return P({k:-v for k,v in self.d.items()})
    def __sub__(self,b):return self+-P(b)
    def __rsub__(self,b):return P(b)+-self
    def __mul__(self,b):
        d={}
        for k,v in self.d.items():
            for l,w in P(b).d.items():
                kl=tuple(a+c for a,c in zip(k,l));d[kl]=d.get(kl,F(0))+v*w
        return P(d)
    __rmul__=__mul__
    def __truediv__(self,b):return self*(1/F(b))
    def __pow__(self,n):
        z=P(1)
        for _ in range(n):z=z*self
        return z
    def value(self,pt):return sum((v*np.prod([a**b for a,b in zip(pt,k)]) for k,v in self.d.items()),F(0))
    def __eq__(self,b):return self.d==P(b).d

def variable(i):
    k=[0]*DIM;k[i]=1;return P({tuple(k):1})
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
FACES=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),(9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
FAN=((0,1,2,8),(0,9,8,2),(0,9,2,3),(0,9,3,4),(0,4,5,7),(0,4,7,9),(0,6,7,5),(0,7,8,9))
TREE=((0,1),(1,2),(3,2),(4,3),(5,6),(6,0),(7,0),(8,2),(9,3))
XY=((i,j)for i in range(3)for j in range(i,3))
PAIRS=tuple(XY)

def geometry(check=True):
    x,r,p,q,l=(variable(i)for i in range(5));s=1-l
    B=((P(F(1,4)),P(0)),(1-3*x/4,P(0)),(1-p,p),(q,1-q),(P(0),1-3*r/4),(P(0),P(F(1,4))),(P(F(1,16)),P(F(1,16))))
    z=[(s*a,s*b,P(0))for a,b in B]+[(P(0),P(0),P(1)),(l,P(0),P(1)),(P(0),l,P(1))]
    area=(31-24*x*p-24*r*q)/64
    bx=F(509,3072)-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8
    by=F(509,3072)-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8
    V=area*s*s/3+l/6
    J=(s**3*bx/4+s*s*l*(1-3*x*p/4)/24+l*l/24,s**3*by/4+s*s*l*(1-3*r*q/4)/24+l*l/24,area*s*s/12+l/12+l*l/24)
    if check:
        vf=P(0);jf=[P(0)for _ in range(3)]
        for ids in FAN:
            a,b,c,d=(z[i]for i in ids)
            vol=dot(sub(b,a),cross(sub(c,a),sub(d,a)))/6;vf+=vol
            for k in range(3):jf[k]+=vol*sum(z[i][k]for i in ids)/4
        assert vf==V and all(jf[k]==J[k]for k in range(3))
    G=[]
    for i,j in TREE:
        u=tuple(V*z[i][k]-J[k]for k in range(3));d=sub(z[j],z[i])
        G.append([-(u[a]*d[b]+u[b]*d[a])/2 for a,b in PAIRS])
    for row in G:
        for poly in row:
            assert all(k[0]<=3 and k[1]<=3 and k[2]+k[3]<=3 and k[4]<=4 for k in poly.d)
    perm=(5,4,3,2,1,0,6,7,9,8)
    def ref(poly):
        return P({(k[1],k[0],k[3],k[2],k[4]):v for k,v in poly.d.items()})
    for i in range(10):
        for k in range(3):
            assert ref(z[perm[i]][k]) == z[i][(1,0,2)[k]]
    assert ref(V)==V and all(ref(J[k])==J[(1,0,2)[k]] for k in range(3))
    return G

BOX=((F(15,16),F(1)),(F(1,4),F(1,2)),(F(0),F(1,64)))
DEG=(3,3,4)
TRI=tuple((i,j) for i in range(4)for j in range(4-i))
INDICES=tuple(product(range(4),range(4),TRI,range(5)))

def univ(a,b,n,i,k):
    return sum((F(comb(k,h)*comb(i,h),comb(n,h))*a**(k-h)*(b-a)**h for h in range(min(k,i)+1)),F(0))

def tensor(G,box=BOX,exact=False):
    keys=sorted({k for row in G for p in row.d})
    coeff=np.array([[[p.d.get(k,F(0)) for p in row]for row in G] for k in keys],dtype=object if exact else float)
    U=[{(i,k):univ(a,b,n,i,k) for i in range(n+1)for k in range(n+1)} for (a,b),n in zip(box,DEG)]
    tb={(i,j,a,b):F(comb(i,a)*comb(j,b),comb(3,a+b)*comb(a+b,a)) if a<=i and b<=j else F(0) for i,j in TRI for a in range(4)for b in range(4-a)}
    trans=np.array([[U[0][ix,k[0]]*U[1][ir,k[1]]*tb[ip,iq,k[2],k[3]]*U[2][il,k[4]] for k in keys] for ix,ir,(ip,iq),il in INDICES],dtype=object if exact else float)
    vals=np.einsum('ak,kbc->abc',trans,coeff) if not exact else (trans@coeff.reshape(len(keys),-1)).reshape(len(INDICES),9,6)
    mats=np.zeros((len(INDICES),9,3,3),dtype=object if exact else float)
    for e,(i,j) in enumerate(PAIRS):mats[:,:,i,j]=vals[:,:,e];mats[:,:,j,i]=vals[:,:,e]
    return mats

def find(B,maxiter=100):
    # Maximize a common eigenvalue lower bound, sum nonnegative weights =1.
    edges=B.shape[1];rows=[]
    for v in np.eye(3):rows.extend(np.einsum('i,neij,j->ne',v,B,v).tolist())
    best=None
    for step in range(maxiter):
        cons=np.column_stack([-np.array(rows),np.ones(len(rows))])
        lp=linprog(np.r_[np.zeros(edges),-1.],A_ub=cons,b_ub=np.zeros(len(rows)),A_eq=[np.r_[np.ones(edges),0]],b_eq=[1],bounds=[(0,None)]*edges+[(None,None)],method='highs')
        if not lp.success:return None,{'error':lp.message}
        w=lp.x[:edges];b=np.einsum('neij,e->nij',B,w);ev,evec=np.linalg.eigh(b);low=float(ev[:,0].min());bound=float(lp.x[-1]);best=(w,low,bound)
        print('ITER',step,'LOW',low,'LP',bound,'ROWS',len(rows),flush=True)
        if low>1e-7:return w,{'min_eigenvalue':low,'LP_bound':bound,'iterations':step+1}
        if bound < -1e-8:return None,{'LP_bound':bound,'iterations':step+1}
        bad=np.where(ev[:,0]<bound-max(1e-10,abs(bound)*1e-4))[0]
        if not len(bad):return w,{'min_eigenvalue':low,'LP_bound':bound,'iterations':step+1}
        # Include all current violating eigenvectors, aggregated only as linear cuts.
        for n in bad:
            v=evec[n,:,0];rows.append(np.einsum('i,eij,j->e',v,B[n],v).tolist())
    return best[0],{'min_eigenvalue':best[1],'LP_bound':best[2],'iterations':maxiter}

def search_main(outdir):
    start=time.time();G=geometry();print('POLY',time.time()-start,flush=True)
    B=tensor(G);print('TENSOR',B.shape,time.time()-start,flush=True)
    old=np.array([0,8324309,18456120,9753139,12482147,29902002,21082282,0,0],float);old/=old.sum()
    ev=np.linalg.eigvalsh(np.einsum('neij,e->nij',B,old));print('OLD_MIN',ev.min(),flush=True)
    w,meta=find(B)
    result={'box':[[str(a),str(b)]for a,b in BOX],'weights':None if w is None else w.tolist(),'meta':meta,'elapsed':time.time()-start,'scope':'Numerical one-tree candidate only; no exact certificate asserted.'}
    (outdir/'h5_original_band_search.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


# Exact durable certificate: all entries below are integers, not float inputs.
WEIGHT_INTS=(13996235,7149463,13426643,6625331,26409982,17217951,15174395,0,0)
DENOMINATOR=100000000
GAP=F(1,100000)

def all_covered(support):
    edges=tuple(sorted({tuple(sorted((a,b))) for face in FACES
                      for a,b in zip(face,face[1:]+face[:1])}))
    adj={i:tuple(b if a==i else a for a,b in edges if i in(a,b)) for i in range(10)}
    assert len(edges)==17 and len(set(support))==len(support)
    assert len(dict(support))==len(support)
    assert all(tuple(sorted(e)) in edges for e in support)
    roots=[]
    for root in range(10):
        if root in dict(support):continue
        missing=[i for i in range(10) if i!=root and i not in dict(support)]
        for values in product(*(adj[i] for i in missing)):
            out=dict(support);out.update(zip(missing,values));ok=True
            for i in range(10):
                v=i
                for _ in range(10):
                    if v==root:break
                    v=out[v]
                if v!=root:ok=False;break
            if ok:roots.append((root,tuple(sorted(out.items()))))
    assert len(set(roots))==len(roots)
    return edges,roots

def exact_blocks(G,w):
    polys=[sum(w[e]*G[e][a] for e in range(9)) for a in range(6)]
    keys=sorted({k for p in polys for k in p.d})
    coeff=np.array([[p.d.get(k,F(0)) for p in polys] for k in keys],dtype=object)
    uni=[{(i,k):univ(a,b,n,i,k) for i in range(n+1) for k in range(n+1)}
         for (a,b),n in zip(BOX,DEG)]
    tri={(i,j,a,b):F(comb(i,a)*comb(j,b),comb(3,a+b)*comb(a+b,a))
         if a<=i and b<=j else F(0) for i,j in TRI for a in range(4) for b in range(4-a)}
    trans=np.array([[uni[0][ix,k[0]]*uni[1][ir,k[1]]*tri[ip,iq,k[2],k[3]]*uni[2][il,k[4]]
                    for k in keys] for ix,ir,(ip,iq),il in INDICES],dtype=object)
    # Every multiply/add is Fraction arithmetic. No floating-point certificate test.
    return trans@coeff

def dump(obj):return (json.dumps(obj,sort_keys=True,indent=2)+'\n').encode('utf-8')

def verify_main(outdir):
    if not __debug__:raise RuntimeError('Assertions must be enabled')
    w=tuple(F(i,DENOMINATOR) for i in WEIGHT_INTS)
    assert sum(w)==1 and all(v>=0 for v in w)
    G=geometry(check=True)  # Full five-variable oriented-fan and reflection identities.
    vals=exact_blocks(G,w);records=[];mins=[]
    for index,row in zip(INDICES,vals):
        aa,bb,cc,dd,ee,ff=map(F,row)
        a,d,f=aa-GAP,dd-GAP,ff-GAP
        minors=(a,a*d-bb*bb,a*d*f+2*bb*cc*ee-a*ee*ee-d*cc*cc-f*bb*bb)
        assert all(v>0 for v in minors),(index,minors)
        mins.append(minors)
        records.append({'index':[index[0],index[1],list(index[2]),index[3]],
                        'matrix_upper_triangle':list(map(str,row)),
                        'shifted_leading_minors':list(map(str,minors))})
    assert len(records)==800 and len(mins)*3==2400
    support=tuple(edge for edge,weight in zip(TREE,w) if weight)
    edges,roots=all_covered(support)
    count={r:sum(rr==r for rr,_ in roots) for r in range(10) if any(rr==r for rr,_ in roots)}
    assert len(roots)==20 and count=={2:15,8:4,9:1}
    perm=(5,4,3,2,1,0,6,7,9,8)
    reflected=tuple((perm[r],tuple(sorted((perm[i],perm[j]) for i,j in arrows))) for r,arrows in roots)
    reflected_support=tuple((perm[i],perm[j]) for i,j in support)
    _,refroots=all_covered(reflected_support)
    assert set(refroots)==set(reflected)
    certificate={'title':'H5_ORIGINAL_CUBIC_MACRO_BAND_20_ROOTED_TREES_V1',
                 'box_x_r_lambda':[[str(a),str(b)] for a,b in BOX],
                 'physical_triangle':'p>=0, q>=0, p+q<=1',
                 'tensor_degrees_x_r_pq_lambda':[3,3,3,4],
                 'weights_denominator':DENOMINATOR,'weight_numerators':list(WEIGHT_INTS),
                 'tree':TREE,'uniform_matrix_gap':str(GAP),'blocks':records}
    data=dump(certificate);name='h5_original_band_matrices.json';(outdir/name).write_bytes(data)
    report={'title':certificate['title'],'scope':'20 complete rooted trees on this prism, and their reflected counterparts on the reflected prism. NOT all48790 trees, NOT whole H5 or E17.',
      'parameter_box_x_r_lambda':certificate['box_x_r_lambda'],'physical_triangle':certificate['physical_triangle'],
      'reflected_box_x_r_lambda':[certificate['box_x_r_lambda'][1],certificate['box_x_r_lambda'][0],certificate['box_x_r_lambda'][2]],
      'facets':FACES,'edges':edges,'actual_moments':'Exact oriented fan: V and all three J polynomials; full five-variable identities.',
      'reflection_identities':34,'fan_moment_identities':4,
      'tree':TREE,'weight_numerators':list(WEIGHT_INTS),'weight_denominator':DENOMINATOR,
      'sum_weights':str(sum(w)),'positive_support':support,'covered_rooted_trees':roots,
      'covered_by_root':count,'reflected_label_permutation':perm,'reflected_covered_rooted_trees':reflected,
      'coefficient_matrices':800,'positive_shifted_leading_minors':2400,
      'gap_per_weight':str(GAP),'minimum_shifted_leading_minors':[str(min(m[i] for m in mins)) for i in range(3)],
      'weighted_mean_arrow_upper_bound':'-3*trace(M)/50000, strictly, for every nonzero PSD M',
      'closed_boundaries':'Collapsed indexed limits are included algebraically, not asserted to be proper E17 bodies.',
      'matrix_file':{'filename':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()},
      'search_dependency_versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':__import__('scipy').__version__}}
    raw=dump(report);rn='h5_original_band_report.json';(outdir/rn).write_bytes(raw)
    print('H5_ACTUAL_FAN_AND_REFLECTION_IDENTITIES_PASS',4,34)
    print('H5_ORIGINAL_CUBIC_MACRO_BAND_20_ROOTED_TREES_PASS',800,2400,20)
    print('MATRICES_BYTES_SHA256',len(data),hashlib.sha256(data).hexdigest())
    print('REPORT_BYTES_SHA256',len(raw),hashlib.sha256(raw).hexdigest())

def main():
    import argparse
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--search',action='store_true',help='Numerical proposal only; does not replace exact default verification')
    ap.add_argument('--out',type=Path,default=Path('.'))
    args=ap.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    if args.search:search_main(args.out)
    else:verify_main(args.out)

if __name__=='__main__':main()
