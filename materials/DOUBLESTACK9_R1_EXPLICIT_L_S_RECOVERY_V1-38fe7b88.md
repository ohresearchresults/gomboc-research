# material-38fe7b889dbb

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# DOUBLESTACK9_R1_EXPLICIT_L_S_RECOVERY_V1

Two new explicitly parameterized actual V10/E17/F9 controls, named DOUBLESTACK9_R1_EXPLICIT_L and DOUBLESTACK9_R1_EXPLICIT_S. These are NOT aliases for similarly named controls in older coordinator outputs. Both have strict (S,U,H)=(4,4,6), no weak equilibria and zero vanishing signs among all 68 edge primitives. They are not class110 and do not improve either global bound.

The actual true facets, genuine edges, own volume centroid and full 9x9 boundary trace matrix are reconstructed exactly from nine rational halfspaces. Facet degrees in original plane order: (4,3,3,3,5,4,3,4,5). FULL253 order is (2,4,8,5,3,0,1,7,6). The literal tree 1->0,2->1,3->2,4->3,5->4,6->5,7->0,8->7 uses true adjacent facets. Root0 and high pair5,6 have empty triple intersection. Both controls satisfy Lambda05+Lambda06>51/25, each summand>209/225, Lambda01<1/32, 2Lambda01+Lambda07<1/10 and Lambda01+Lambda02+Lambda07+Lambda08<1. Nevertheless -A21-A54-2A65 is SPD for their actual centered poles, excluding any common SPD metric with all three arrows nonnegative.

Five-pole coordinates x=q5,y=q6,z=q4,a=q2,b=q1 give a=-alpha*x-beta*y-c*z and b=m*x+n*y+ell*z. All required six sums are positive, but m and n are NEGATIVE, so requiring individually positive target coefficients would miss these actual controls. Both have min(t1,t2)>1/8 in SHARP_FIVE_POLE_THREE_ARROWS_V1 and therefore also satisfy its general SOS obstruction.

Observed diagnostics, rounded only here; JSON output is exact rational:
L: trace sum 2.065024448758199; alpha=.8524906032183813,beta=.5641207915967442,c=.9978788753868312,m=-.010341705693257876,n=-.011273721367564764,ell=.9878001818597921; s1=1.5111845121067178,s2=1.5232944929526635,t1=1.7689099395934946,t2=3.591732983994058; H=-739.8727420304934,Psi=-4899.157979061191.
S: trace sum 2.066502524436218; alpha=.8566763349501313,beta=.5706953516835659,c=.9997869320487063,m=-.0010462568534490395,n=-.0011412884039744442,ell=.9987637399633219; s1=1.5011097119030568,s2=1.5022807021511095,t1=1.7518750224604234,t2=3.50897447821551; H=-699.4917654753364,Psi=-4326.26276076828.

The full-rank strict five-vector and rank-two tangent controls in the output test the exact criterion's boundary. Those auxiliary vector controls are not claimed to be polytopes.

## Reconstruction capsule
Save the following complete block as five_pole_bridge.py, UTF-8, LF, final newline. Python3 standard library only, no external dependencies, no random seed, all exact inputs literal in main and double_stack. Run and verify: python five_pole_bridge.py
Expected terminal marker ACTUAL_E17_FIVE_POLE_RECONSTRUCTION_PASS.
Source five_pole_bridge.py: 10149 bytes; SHA256 7dcc5421559adee6ccf038437b080f8c761df3699a31fb62cfda1d4a9e502be8.
Output five_pole_bridge_report.json: 163272 bytes; SHA256 9720a943e41862caf3cdfc8407bdade591cb8821906f54bf0b482422dd5b599c.
These pins and checks were observed by the coordinator. They supersede any ephemeral intermediate source/report sizes or decimal coefficients for these new object names. The script is self-contained, including the full five-pole criterion, actual-body reconstruction and all inputs.

```python
"""Exact five-pole obstruction on actual E17 double-stack bodies.
Python 3 standard library only. All input numbers are literal rational values.
The program reconstructs the actual convex polytope, volume centroid, true faces,
true edges, and the full nine-by-nine boundary matrix before testing three arrows.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json, sys, hashlib

def vec(v): return tuple(map(F,v))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(t,a): return tuple(t*x for x in a)
def dot(a,b): return sum((x*y for x,y in zip(a,b)), F(0))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def solve(rows,rhs):
    a,b,c=rows; d=det(a,b,c)
    if not d: return None
    return mul(1/d,add(add(mul(rhs[0],cross(b,c)),mul(rhs[1],cross(c,a))),mul(rhs[2],cross(a,b))))
def columns_solve(cols,rhs): return solve(tuple(zip(*cols)),rhs)
def hull_face(ids,X,n):
    drop=max(range(3),key=lambda k:abs(n[k])); keep=[k for k in range(3) if k!=drop]
    pts=sorted(ids,key=lambda i:tuple(X[i][k] for k in keep))
    def turn(i,j,k):
        a,b,c=[tuple(X[t][p] for p in keep) for t in (i,j,k)]
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    def half(seq):
        h=[]
        for i in seq:
            while len(h)>1 and turn(h[-2],h[-1],i)<=0: h.pop()
            h.append(i)
        return h
    h=half(pts)[:-1]+half(pts[::-1])[:-1]
    assert len(h)==len(ids)>=3, ('REDUNDANT_OR_NONVERTEX',ids,h)
    if dot(cross(sub(X[h[1]],X[h[0]]),sub(X[h[2]],X[h[1]])),n)<0: h.reverse()
    for j in range(len(h)):
        assert dot(cross(sub(X[h[(j+1)%len(h)]],X[h[j]]),sub(X[h[(j+2)%len(h)]],X[h[(j+1)%len(h)]])),n)>0
    return h

def body(planes):
    vertices=set()
    for ix in combinations(range(len(planes)),3):
        v=solve([planes[i][0] for i in ix],[planes[i][1] for i in ix])
        if v is not None and all(dot(n,v)<=b for n,b in planes): vertices.add(v)
    X=sorted(vertices); assert len(X)>=4
    faces=[hull_face([i for i,v in enumerate(X) if dot(n,v)==b],X,n) for n,b in planes]
    edges={}
    for fi,face in enumerate(faces):
        for i,j in zip(face,face[1:]+face[:1]): edges.setdefault(tuple(sorted((i,j))),[]).append(fi)
    assert all(len(fs)==2 for fs in edges.values())
    assert len(X)-len(edges)+len(faces)==2
    apex=tuple(sum(v[k] for v in X)/len(X) for k in range(3))
    assert all(dot(n,apex)<b for n,b in planes)
    D=F(0); moments=vec((0,0,0))
    for face in faces:
        for j in range(1,len(face)-1):
            a,b,c=[X[i] for i in (face[0],face[j],face[j+1])]
            d=det(sub(a,apex),sub(b,apex),sub(c,apex)); assert d>0
            D+=d; moments=add(moments,mul(d,add(add(apex,a),add(b,c))))
    g=mul(1/(4*D),moments); V=D/6
    Q=[mul(1/(b-dot(n,g)),n) for n,b in planes]
    Y=[sub(v,g) for v in X]
    weights=[]; centroids=[]
    for face in faces:
        dd=F(0); m=vec((0,0,0))
        for j in range(1,len(face)-1):
            a,b,c=[Y[i] for i in (face[0],face[j],face[j+1])]
            d=det(a,b,c); assert d>0
            dd+=d; m=add(m,mul(d,add(add(a,b),c)))
        weights.append(3*dd/D); centroids.append(mul(1/(3*dd),m))
    L=[[weights[j]*(1-dot(q,centroids[j])) for j in range(len(Q))] for q in Q]
    for i,q in enumerate(Q):
        assert L[i][i]==0 and sum(L[i])==3
        assert all(L[i][j]>0 for j in range(len(Q)) if i!=j)
        assert tuple(sum(L[i][j]*Q[j][k] for j in range(len(Q))) for k in range(3))==mul(-1,q)
    stable=[]; unstable=[]; saddle=[]; weak=[]
    for i,q in enumerate(Q):
        p=mul(1/dot(q,q),q); vals=[1-dot(Q[j],p) for j in range(len(Q)) if j!=i]
        if min(vals)>=0:
            (stable if min(vals)>0 else weak).append(('F',i))
    neighbors={i:set() for i in range(len(X))}
    for u,v in edges: neighbors[u].add(v); neighbors[v].add(u)
    for i,x in enumerate(Y):
        vals=[dot(x,sub(Y[j],x)) for j in neighbors[i]]
        if max(vals)<=0: (unstable if max(vals)<0 else weak).append(('V',i))
    primitives=[]
    for (i,j),(a,b) in sorted(edges.items()):
        vals=[dot(Y[i],sub(Y[j],Y[i])),dot(Y[j],sub(Y[i],Y[j])),dot(Q[a],sub(Q[b],Q[a])),dot(Q[b],sub(Q[a],Q[b]))]
        primitives.extend(vals)
        if max(vals)<=0: (saddle if max(vals)<0 else weak).append(('E',i,j))
    return dict(vertices=X,faces=faces,edges=edges,volume=V,centroid=g,centered=Y,poles=Q,Lambda=L,
                equilibrium=[len(stable),len(unstable),len(saddle)],weak=weak,primitive_zeroes=sum(v==0 for v in primitives))

def double_stack(r,h,k,alpha,gamma,e):
    u=(1-alpha)/2; v=(1-gamma)/2
    a,b,c,d=e,e*(1+h),e,e*(1+k)
    return [(vec(n),F(q)) for n,q in [
      ((-1,0,0),0),((0,-1,0),0),((1,1,0),1),
      ((1-h/u,1,1),1),
      ((1+h/alpha+a*(1-u)/alpha,1+h/alpha+a*u/alpha,1),1+h/alpha+a*u/alpha),
      ((1+b,1-h/u-b,1),1),
      ((-k/v,-r,-1),0),
      ((k/gamma+c*(1-v)/gamma,k/gamma-r+c*v/gamma,-1),k/gamma+c*v/gamma),
      ((d,-r-k/v-d,-1),0)]]

FULL_ORDER=(2,4,8,5,3,0,1,7,6)
def symouter(a,b): return [[(a[i]*b[j]+a[j]*b[i])/2 for j in range(3)] for i in range(3)]
def arrow(a,b): return symouter(a,sub(b,a))
def stress(Q):
    terms=[(F(-1),arrow(Q[2],Q[1])),(F(-1),arrow(Q[5],Q[4])),(F(-2),arrow(Q[6],Q[5]))]
    return [[sum(w*A[i][j] for w,A in terms) for j in range(3)] for i in range(3)]
def leading(A): return [A[0][0],A[0][0]*A[1][1]-A[0][1]*A[1][0],det(*A)]

def sharp_criterion(s1,s2,t1,t2):
    assert min(s1,s2,t1,t2)>0
    A,C=1+s1+s2,t1+t2; B,D=s1-s2,t1-t2
    p=B*B+2*B*D; L=A*A+2*A*C-p-1
    assert L==2*(s1+s2+t1+t2)+4*(s1*s2+s1*t2+s2*t1)
    K=L*L-4*p; assert K>4*(t1+t2)**2>0
    H=D*D-2*L*t1*t2
    psi=D**4-4*L*t1*t2*D*D+16*p*t1*t1*t2*t2
    feasible=H>0 and psi>0
    if feasible:
        tau=2*H/K
        assert 0<tau<F(1,2)
        assert K*tau*tau-4*H*tau+16*(t1*t2)**2<0
    return dict(s1=s1,s2=s2,t1=t1,t2=t2,A=A,B=B,C=C,D=D,p=p,L=L,K=K,psi=psi,
                BD=B*D,positive_branch=H,feasible=feasible)

def criterion_controls():
    # A full-rank positive example with genuinely split target b, all arrows strict.
    x,y,z=vec((F(3,10),0,F(1,5))),vec((F(1,10),F(1,100),-F(3,100))),vec((0,0,1))
    aa,bb,cc,m,n,ell=F(1,1000),F(1),F(1,1000),F(1,500),F(1,100),F(999,1000)
    a=mul(-1,add(add(mul(aa,x),mul(bb,y)),mul(cc,z)))
    b=add(add(mul(m,x),mul(n,y)),mul(ell,z))
    G=[[dot(u,v) for v in (x,y,z)] for u in (x,y,z)]
    vals=[dot(y,sub(x,y)),dot(x,sub(z,x)),dot(a,sub(b,a))]
    assert min(leading(G))>0 and min(vals)>0
    c=sharp_criterion(aa/bb,(aa+m)/(bb+n),cc/bb,(cc+ell)/(bb+n)); assert c['feasible']
    # Exact tangency: rank-two closure exists, but the theorem excludes EVERY SPD.
    t=F(301,5400); s=F(1,10); r=9*t/2; tau=r*r
    coefx,coefz=F(71,250),-9*t/5
    H=[[tau,coefx*tau+coefz*tau,tau],
       [coefx*tau+coefz*tau,coefx*coefx*tau+2*coefx*coefz*tau+coefz*coefz,coefx*tau+coefz],
       [tau,coefx*tau+coefz,F(1)]]
    def form(u,v): return sum(u[i]*H[i][j]*v[j] for i in range(3) for j in range(3))
    xx,yy,zz=vec((1,0,0)),vec((0,1,0)),vec((0,0,1))
    av=vec((-s,-1,-t)); bv=vec((0,0,8*t))
    zeros=[form(yy,sub(xx,yy)),form(xx,sub(zz,xx)),form(av,sub(bv,av))]
    tangent=sharp_criterion(s,s,t,9*t)
    assert tangent['positive_branch']>0 and tangent['psi']==0 and not tangent['feasible']
    assert zeros==[0,0,0] and det(*H)==0
    assert H[0][0]*H[2][2]-H[0][2]**2>0
    return dict(strict_control=dict(Gram=G,arrows=vals,criterion=c),tangent_control=dict(Gram=H,arrows=zeros,criterion=tangent))

def five_coefficients(Q):
    # x=q5, y=q6, z=q4, a=q2, b=q1. All are the SAME actual centered body's poles.
    x,y,z=Q[5],Q[6],Q[4]
    av=columns_solve((x,y,z),Q[2]); bv=columns_solve((x,y,z),Q[1]); assert av is not None and bv is not None
    aa,bb,cc=mul(-1,av); m,n,ell=bv
    assert aa>0 and bb>0 and cc>0
    assert bb+n>0 and aa+m>0 and cc+ell>0
    s1,t1=aa/bb,cc/bb; s2,t2=(aa+m)/(bb+n),(cc+ell)/(bb+n)
    ans=sharp_criterion(s1,s2,t1,t2)
    ans.update(alpha=aa,beta=bb,c=cc,m=m,n=n,ell=ell)
    return ans

def clean(o):
    if isinstance(o,F): return str(o)
    if isinstance(o,dict): return {str(k):clean(v) for k,v in o.items()}
    if isinstance(o,(list,tuple)): return [clean(v) for v in o]
    return o

def main():
    out={'criterion_controls':criterion_controls()}
    for name,h,k,e in [('DOUBLESTACK9_R1_EXPLICIT_L',F(1,1000),F(1,500),F(1,1000000)),('DOUBLESTACK9_R1_EXPLICIT_S',F(1,10000),F(1,5000),F(1,100000000))]:
        P=body(double_stack(F(1,2),h,k,F(1,10),F(1,10),e))
        assert [len(P['vertices']),len(P['edges']),len(P['faces'])]==[10,17,9]
        Q=[P['poles'][i] for i in FULL_ORDER]
        L=[[P['Lambda'][i][j] for j in FULL_ORDER] for i in FULL_ORDER]
        assert all(len(set(P['faces'][FULL_ORDER[i]])&set(P['faces'][FULL_ORDER[j]]))==2 for i,j in ((1,0),(2,1),(3,2),(4,3),(5,4),(6,5),(7,0),(8,7)))
        assert not set(P['faces'][FULL_ORDER[0]])&set(P['faces'][FULL_ORDER[5]])&set(P['faces'][FULL_ORDER[6]])
        assert L[0][5]+L[0][6]>F(51,25)
        assert min(L[0][5],L[0][6])>F(209,225)
        assert L[0][1]<F(1,32) and 2*L[0][1]+L[0][7]<F(1,10)
        assert L[0][1]+L[0][2]+L[0][7]+L[0][8]<1
        assert P['equilibrium']==[4,4,6] and not P['weak'] and P['primitive_zeroes']==0
        S=stress(Q); assert min(leading(S))>0
        coeff=five_coefficients(Q); assert not coeff['feasible']
        P['FULL_poles']=Q; P['FULL_Lambda']=L; P['stress']=S; P['stress_leading_minors']=leading(S); P['five_coefficients']=coeff
        out[name]=P
        print(name,'counts',P['equilibrium'],'T',float(L[0][5]+L[0][6]),'BD',float(coeff['BD']),'psi',float(coeff['psi']),'branch',float(coeff['positive_branch']),flush=True)
    text=json.dumps(clean(out),sort_keys=True,indent=2)+'\n'
    target=Path('five_pole_bridge_report.json'); target.write_text(text)
    print('ACTUAL_E17_FIVE_POLE_RECONSTRUCTION_PASS')
    for p in (Path(__file__),target):
        data=p.read_bytes(); print(p.name,len(data),hashlib.sha256(data).hexdigest())
if __name__=='__main__': main()
```
