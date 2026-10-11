# material-ebd5abd77a31

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Exact true-edge-pair orthogonal-shell bound for the H5 L=3/25 control.
Requires hybrid_reference_frontier.py and its two preserved exact dependencies.
No numerical roots, floating arithmetic, external solver or sampling are used.
"""
from fractions import Fraction as F
from math import comb
import json,hashlib,sys
from pathlib import Path
from hybrid_reference_frontier import body,physical,dot,sub,add,mul,mv,quad,det,inv,strings
THETA=[F(3,20),F(3,20),F(3,20),F(9,20),F(3,25)]
W=[[F(2215,10000),F(-1288,10000)],[F(-1288,10000),F(2146,10000)]]
BOUND=F(24,5);MAX_DEPTH=24

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def padd(a,b):
    c=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=x
    return trim(c)

def pscale(a,s):return trim([s*x for x in a])
def pmul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)

def pval(a,t):
    c=F(0)
    for x in reversed(a):c=c*t+x
    return c

def bernstein(a,l,r):
    n=len(a)-1
    power=[sum((a[j]*comb(j,i)*l**(j-i)*(r-l)**i for j in range(i,n+1)),F(0)) for i in range(n+1)]
    return [sum((power[j]*F(comb(i,j),comb(n,j)) for j in range(i+1)),F(0)) for i in range(n+1)]

def certificate(a,l,r,depth=0):
    b=bernstein(a,l,r)
    if min(b)>=0:return [dict(interval=[l,r],bernstein=b,depth=depth)]
    assert depth<MAX_DEPTH,('UNCERTIFIED_INTERVAL',l,r,a,b)
    mid=(l+r)/2
    return certificate(a,l,mid,depth+1)+certificate(a,mid,r,depth+1)

def reference(g):
    h=1-g[2];m=sub([F(0),THETA[4]],g[:2])
    C=[[W[i][j]+m[i]*m[j] for j in range(2)]+[h*m[i]] for i in range(2)]
    C.append([h*m[0],h*m[1],h*h])
    assert W[0][0]>0 and W[0][0]*W[1][1]-W[0][1]**2>0
    assert C[0][0]>0 and C[0][0]*C[1][1]-C[0][1]**2>0 and det(C)>0
    return C

def bound_all(v,q,edge,C):
    Ci=inv(C);pe=sorted(edge);qe=[edge[e] for e in pe];records=[];all_leaves=0;all_intervals=0;maxdepth=0
    for ei,(i,j) in enumerate(pe):
        a=v[i];u=sub(v[j],a);pp=[quad(a,Ci),2*dot(a,mv(Ci,u)),quad(u,Ci)]
        for fi,(f,g) in enumerate(qe):
            n=q[f];vv=sub(q[g],n)
            A=dot(a,n);B=dot(u,n);cc=dot(a,vv);D=dot(u,vv)
            rec=dict(pair=[ei,fi],primal_edge=[i,j],polar_edge=[f,g],constraint=[A,B,cc,D],points=[],intervals=[])
            def point(s,t):
                if not(0<=s<=1 and 0<=t<=1):return
                w=add(a,mul(s,u));nn=add(n,mul(t,vv));assert dot(w,nn)==0
                value=quad(w,Ci)*quad(nn,C)
                assert value<=BOUND,('POINT_BOUND_FAILED',ei,fi,s,t,value)
                rec['points'].append(dict(s=s,t=t,value=value))
            if cc==0 and D==0:
                if B:
                    s=-A/B;point(s,F(0));point(s,F(1))
                elif A==0:
                    for s in [F(0),F(1)]:
                        for t in [F(0),F(1)]:point(s,t)
                rec['degenerate']=True;records.append(rec);continue
            N0=sub(mul(cc,n),mul(A,vv));N1=sub(mul(D,n),mul(B,vv))
            qq=[quad(N0,C),2*dot(N0,mv(C,N1)),quad(N1,C)]
            product=pmul(pp,qq)
            guard=padd(pscale(pmul([cc,D],[cc,D]),BOUND),pscale(product,-1))
            cuts={F(0),F(1)}
            for x,y in [(cc,D),(A,B),(A+cc,B+D)]:
                if y and 0<-x/y<1:cuts.add(-x/y)
            cuts=sorted(cuts)
            for s in cuts:
                den=cc+D*s
                if den:point(s,-(A+B*s)/den)
                elif A+B*s==0:point(s,F(0));point(s,F(1))
            rec['product_numerator']=product;rec['guard']=guard
            for l,r in zip(cuts,cuts[1:]):
                s=(l+r)/2;den=cc+D*s;assert den
                t=-(A+B*s)/den
                if not(0<=t<=1):continue
                leaves=certificate(guard,l,r)
                all_intervals+=1;all_leaves+=len(leaves);maxdepth=max(maxdepth,max(x['depth'] for x in leaves))
                rec['intervals'].append(dict(interval=[l,r],leaves=leaves))
            records.append(rec)
    assert len(records)==289
    return dict(edge_pair_count=len(records),feasible_intervals=all_intervals,leaf_count=all_leaves,max_depth=maxdepth,records=records)

def main():
    z,v,q,D,g,edges,planar=body(THETA);C=reference(g);Ci=inv(C)
    chi=[quad(v[i],Ci)*quad(q[0],C)/dot(v[i],q[0])**2-1 for i in range(7,10)]
    assert chi[2]==0 and max(chi[:2])<F(1,8)
    report=bound_all(v,q,edges,C)
    out=dict(version=1,theta=THETA,volume=D/6,centroid=g,reference=C,W=W,chi=chi,
             orthogonal_shell_bound=BOUND,max_allowed_depth=MAX_DEPTH,certificate=report,
             physical=physical(v,q,edges))
    path=Path(sys.argv[1] if len(sys.argv)>1 else 'ORTHOGONAL_SHELL_EXACT.json')
    data=(json.dumps(strings(out),sort_keys=True,indent=2)+'\n').encode();path.write_bytes(data)
    print('EDGE_PAIRS',report['edge_pair_count'],'INTERVALS',report['feasible_intervals'],'LEAVES',report['leaf_count'],'MAX_DEPTH',report['max_depth'])
    print(path.name,len(data),hashlib.sha256(data).hexdigest())
    print('H5_ORTHOGONAL_TRUE_EDGE_PAIR_SHELL_24_OVER_5_PASS')
if __name__=='__main__':main()
