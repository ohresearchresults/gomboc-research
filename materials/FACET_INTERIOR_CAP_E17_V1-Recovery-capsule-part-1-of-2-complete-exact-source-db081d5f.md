# material-db081d5ffd40

AI research material

---

"""FACET_INTERIOR_CAP_E17_V1. CPython 3.13.5, standard library only.
Exact family identities and uniform bounds; actual sample hull and mechanics.
The one dependency is the unchanged archived cap_geometry.py (hash checked).
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
import hashlib, json, sys
assert __debug__
_DEP=Path(__file__).with_name('cap_geometry.py').read_bytes()
assert len(_DEP)==4942
assert hashlib.sha256(_DEP).hexdigest()=='192e14a57e44b4f31d4b8af0039616fa4cf004af91322f214eef1472bfb71fb5'
from cap_geometry import add, sub, mul, dot, cross, det, mv, inv, ID, hull, mechanics

FACES=((0,3,2,1),(0,1,9,8),(0,7,3),(0,8,7),(1,2,4,9),
       (2,3,5,4),(3,6,5),(3,7,6),(4,5,6,7,8,9))
TMAX=Q(1,100); HMIN=Q(53,30); HMAX=Q(177,100)

def vertices(t=TMAX,H=HMIN):
    return [(-1,-1,0),(1,-1,0),(1,1,0),(-1,1,0),
            (3,3,H),(-3,3,H),(-3-t,1,H),(-3-Q(6,5)*t,0,H),
            (-3,-3,H),(3,-3,H)]

def delta(q,x,M=ID):
    alpha=dot(q,mv(inv(M),q))
    return (2-dot(q,x))**2-alpha*dot(x,mv(M,x))

def edge_max(q,a,b,M=ID):
    d=sub(b,a); alpha=dot(q,mv(inv(M),q))
    C=alpha*dot(d,mv(M,d))-dot(q,d)**2
    L=-2*(2-dot(q,a))*dot(q,d)-2*alpha*dot(a,mv(M,d))
    candidates=[(delta(q,a,M),Q(0),a),(delta(q,b,M),Q(1),b)]
    assert C>=0
    if C:
        t=L/(2*C)
        if 0<t<1:
            x=add(a,mul(t,d)); candidates.append((delta(q,x,M),t,x))
    return max(candidates,key=lambda r:r[0])

def face_max(P,f,q,M=ID):
    cyc=P['facets'][f]; X=P['X']; candidates=[]
    for i,j in zip(cyc,cyc[1:]+cyc[:1]):
        value,t,x=edge_max(q,X[i],X[j],M)
        candidates.append((value,x,('edge',i,j,t)))
    a=X[cyc[0]]; ds=[sub(X[cyc[k]],a) for k in (1,2)]
    alpha=dot(q,mv(inv(M),q))
    C=[[alpha*dot(d,mv(M,e))-dot(q,d)*dot(q,e) for e in ds] for d in ds]
    L=[-2*(2-dot(q,a))*dot(q,d)-2*alpha*dot(a,mv(M,d)) for d in ds]
    D=C[0][0]*C[1][1]-C[0][1]*C[1][0]
    assert D>=0
    N=inv(M); pole=P['poles'][f]
    beta=dot(pole,mv(N,q)); rho=dot(pole,mv(N,pole))
    assert (D==0)==(beta==0)
    if D:
        u=(C[1][1]*L[0]-C[0][1]*L[1])/(2*D)
        v=(-C[1][0]*L[0]+C[0][0]*L[1])/(2*D)
        x=add(add(a,mul(u,ds[0])),mul(v,ds[1]))
        closed=add(mul((beta-2*rho)/beta**2,mv(N,q)),mul(2/beta,mv(N,pole)))
        assert x==closed and delta(q,x,M)==4*alpha*(rho-beta)/beta**2
        if all(dot(p,x)<=1 for p in P['poles']):
            candidates.append((delta(q,x,M),x,('face',u,v)))
    return max(candidates,key=lambda r:r[0])

# Small exact rational polynomial ring, increasing coefficient order.
class Poly:
    def __init__(self,c=0):
        if isinstance(c,Poly): self.c=c.c; return
        a=list(c) if isinstance(c,(list,tuple)) else [c]
        a=list(map(Q,a))
        while len(a)>1 and a[-1]==0: a.pop()
        self.c=tuple(a)
    def __add__(self,o):
        o=Poly(o); n=max(len(self.c),len(o.c))
        return Poly([(self.c[i] if i<len(self.c) else 0)+(o.c[i] if i<len(o.c) else 0) for i in range(n)])
    __radd__=__add__
    def __neg__(self): return Poly([-v for v in self.c])
    def __sub__(self,o): return self+-Poly(o)
    def __rsub__(self,o): return Poly(o)+-self
    def __mul__(self,o):
        o=Poly(o); a=[Q(0)]*(len(self.c)+len(o.c)-1)
        for i,x in enumerate(self.c):
            for j,y in enumerate(o.c): a[i+j]+=x*y
        return Poly(a)
    __rmul__=__mul__
    def __truediv__(self,q): return Poly([v/Q(q) for v in self.c])
    def __eq__(self,o): return self.c==Poly(o).c
    def at(self,t):
        s=Q(0)
        for a in reversed(self.c): s=s*t+a
        return s
    def bernstein(self):
        n=len(self.c)-1
        power=[a*TMAX**i for i,a in enumerate(self.c)]
        return [sum(power[k]*Q(comb(i,k),comb(n,k)) for k in range(i+1)) for i in range(n+1)]

def serial(x):
    if isinstance(x,Q): return str(x)
    if isinstance(x,Poly): return list(map(str,x.c))
    if isinstance(x,dict): return {str(k):serial(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [serial(v) for v in x]
    return x

def family_geometry():
    t=Poly([0,1]); V=[tuple(Poly(a) for a in v) for v in vertices(t,1)]
    records=[]
    def positive(p,label):
        p=Poly(p); b=p.bernstein()
        assert min(b)>=0 and b[-1]>0,(label,p.c,b)
        # Nonnegative Bernstein coefficients, at least one positive; the
        # final coefficient is positive. Thus p>0 on 0<t<=1/100.
        records.append(dict(label=label,power=p,bernstein=b))
    use={}
    for f,cyc in enumerate(FACES):
        a,b,c=[V[i] for i in cyc[:3]]
        n=cross(sub(b,a),sub(c,a)); h=dot(n,a)
        for i,v in enumerate(V):
            gap=h-dot(n,v)
            if i in cyc: assert gap==0
            else: positive(gap,('support',f,i))
        for i,j in zip(cyc,cyc[1:]+cyc[:1]):
            use.setdefault(tuple(sorted((i,j))),[]).append((f,i,j))
            for k in cyc:
                if k not in (i,j):
                    positive(dot(n,cross(sub(V[j],V[i]),sub(V[k],V[i]))),('turn',f,i,j,k))
    assert len(use)==17 and len(V)-len(use)+len(FACES)==2
    assert all(len(a)==2 and a[0][1:]==a[1][1:][::-1] for a in use.values())
    # Strict supports, strictly convex cycles, and this closed connected
    # two-manifold exhaust the convex hull; the proof gives a normal-fan
    # derivation independently. A positive vertical affine map handles H>0.
    W=Poly(0); J=[Poly(0)]*3
    # An interior average is used ONLY for a positive volume decomposition.
    c=tuple(sum(v[k] for v in V)/10 for k in range(3))
    for f,cyc in enumerate(FACES):
        for j in range(1,len(cyc)-1):
            a,b,d=[V[i] for i in (cyc[0],cyc[j],cyc[j+1])]
            w=det(sub(a,c),sub(b,c),sub(d,c))/6
            positive(w,('volume_tetrahedron',f,j))
            W+=w
            for k in range(3): J[k]+=w*(c[k]+a[k]+b[k]+d[k])/4
    assert W==Poly([Q(52,3),Q(17,10)])
    assert J[0]==Poly([0,-Q(81,20),-Q(107,200)])
    assert J[1]==t/8
    assert J[2]==Poly([Q(34,3),Q(47,40)])
    return dict(parameter_interval=(0,TMAX),height_interval=(HMIN,HMAX),
                vertices_at_height_one=V,facets=FACES,edges=sorted(use),
                height_one_volume=W,height_one_first_moment=J,
                exact_positive_records=records)

def uniform_bounds():
    # g_x negative; denominator 20(51t+520)>=10400.
    gx=3*TMAX*(107*TMAX+810)/10400
    gy=15*TMAX/2080
    assert gx<Q(1,400) and gy<Q(1,10000)
    assert 141*520-51*1360>0
    gamma_min=Q(17,26)
    gamma_max=(141*TMAX+1360)/(4*(51*TMAX+520))
    assert gamma_max<Q(131,200)
    tau_min=HMIN**2*gamma_min
    tau_max=HMAX**2*Q(131,200)
    assert tau_max<Q(103,50)
    # Every raw middle-height witness has two horizontal components bounded
    # after actual centering by 201/100 and 1/400, in either order.
    assert 2+3*TMAX/5+Q(1,400)<Q(201,100)
    witness_lower=2*tau_min-Q(201,100)**2-Q(1,400)**2
    assert witness_lower==Q(774011,18720000)>Q(1,25)
    # Outward x-motion of vertices6,7 only increases raw edge squared norm.
    # Centering costs at most 2(|u_x||g_x|+|u_y||g_y|).
    assert 3+Q(6,5)*TMAX<Q(151,50)
    center_cost=2*(Q(151,50)*Q(1,400)+3*Q(1,10000))
    assert center_cost==Q(157,10000)
    # 4 tau*s minus the limiting t=0 horizontal squared norms.
    # Bound by tau<=103/50; maximize each concave quadratic on [0,1].
    quadratics={'corners':(-2,Q(6,25),-8),
                'spine':(-2,Q(106,25),-4),
                'diagonals':(-2,Q(156,25),-5)}
    maxima={}
    for name,(a,b,c) in quadratics.items():
        t=-b/(2*c)
        assert 0<t<1
        maxima[name]=a+b*t+c*t*t
    assert maxima==dict(corners=-Q(9991,5000),spine=-Q(2191,2500),diagonals=-Q(166,3125))
    edge_upper=max(-Q(1),4*Q(103,50)-9,*maxima.values())+center_cost
    assert edge_upper==-Q(1871,50000)<-Q(3,100)
    return dict(gx_abs_upper=gx,gy_upper=gy,gamma_bounds=(gamma_min,gamma_max),
        tau_bounds=(tau_min,tau_max),centering_cost=center_cost,
        limiting_cross_edge_maxima=maxima,scaled_cap_witness_lower=witness_lower,
        scaled_cap_all_true_edges_upper=edge_upper)

def exact_sample():
    P=hull(vertices()); assert tuple(P['facets'])==FACES
    t=TMAX; H=HMIN; d=51*t+520
    expected_g=(-3*t*(107*t+810)/(20*d),15*t/(4*d),H*(141*t+1360)/(4*d))
    assert P['volume']==H*d/30 and P['g']==expected_g
    b=0; q=P['poles'][b]; R=mechanics(P)
    assert R['S']==[0,1,2,4,5,8] and R['U']==[4,5,7,8,9]
    assert len(R['H'])==9 and not R['zeros']
    edges=sorted(P['edges']); E=[]
    for i,j in edges:
        value,s,x=edge_max(q,P['X'][i],P['X'][j])
        assert value<0
        E.append(dict(edge=(i,j),maximum=value,parameter=s,raw_point=add(x,P['g'])))
    neighbors=sorted({f for fs in P['edges'].values() if b in fs for f in fs if f!=b})
    assert neighbors==[1,2,4,5]
    maxima=[]
    for f in neighbors:
        value,x,where=face_max(P,f,q)
        assert value>0 and where[0]=='face'
        assert all(dot(p,x)<1 for i,p in enumerate(P['poles']) if i!=f)
        maxima.append(dict(facet=f,maximum=value,raw_point=add(x,P['g']),location=where))
    raw_witnesses={1:(0,-2,H/2),2:(-2-Q(3,5)*t,0,H/2),4:(2,0,H/2),5:(0,2,H/2)}
    witnesses=[]
    for f,a in raw_witnesses.items():
        x=sub(a,P['g']); value=delta(q,x)
        assert value>0 and dot(P['poles'][f],x)==1
        assert all(dot(p,x)<1 for i,p in enumerate(P['poles']) if i!=f)
        witnesses.append(dict(facet=f,raw_point=a,delta=value,scaled_delta=value*P['g'][2]**2))
    primitives=[]; X=P['X']; qq=P['poles']
    for (i,j),(f,h) in sorted(P['edges'].items()):
        z=(dot(X[i],sub(X[j],X[i])),dot(X[j],sub(X[i],X[j])),
           dot(qq[f],sub(qq[h],qq[f])),dot(qq[h],sub(qq[f],qq[h])))
        assert all(v!=0 for v in z)
        primitives.append(dict(edge=(i,j),incident_facets=(f,h),values=z))
    return dict(t=t,H=H,vertices=P['vertices'],facets=P['facets'],true_edges=edges,
        volume=P['volume'],centroid=P['g'],poles=P['poles'],root=b,metric=ID,
        mechanics=R,edge_primitives=primitives,cap_edge_maxima=E,
        cap_vertex_maximum=max(delta(q,x) for x in X),
        cap_facet_maxima=maxima,cap_facet_witnesses=witnesses)

def main():
    geometry=family_geometry(); bounds=uniform_bounds(); sample=exact_sample()
    report=dict(name='FACET_INTERIOR_CAP_E17_V1',scope='continuous E17 shape family, Euclidean metric; not global minimum',
                geometry=geometry,uniform_bounds=bounds,actual_sample=sample)
    data=(json.dumps(serial(report),sort_keys=True,indent=2)+'\n').encode()
    p=Path('facet_interior_cap_report.json')
    mode=sys.argv[1] if len(sys.argv)>1 else 'build'
    if mode=='build': p.write_bytes(data)
    elif mode=='check': assert p.read_bytes()==data
    else: raise SystemExit('Use build or check')
    print('REPORT',len(data),hashlib.sha256(data).hexdigest())
    print('CONTINUOUS_TRUE_10_17_9_SUPPORTS_TURNS_AND_MOMENTS_PASS',len(geometry['exact_positive_records']))
    print('ROOT_CAP_MISSES_ENTIRE_TRUE_ONE_SKELETON_UNIFORMLY_PASS')
    print('ALL_FOUR_ROOT_NEIGHBORS_HAVE_STRICT_FACET_INTERIOR_CAP_WITNESSES_PASS')
    print('ACTUAL_SAMPLE_6_5_9_WEAK000_ALL_68_PRIMITIVES_NONZERO_PASS')
    print('FACET_INTERIOR_CAP_E17_V1_PASS')
if __name__=='__main__': main()
