# material-d94997fdde50

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""ROOT_MASS_CONDITIONED_LOWER_CONVEX_ORDER_V1.
Self-contained exact certificates and actual homogeneous-polytope controls.
CPython >=3.11, standard library only; assertions must remain enabled.
  python -S root_mass_lower_exact.py build
  python -S root_mass_lower_exact.py check
All inputs are literal below. No random numbers or external input files.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import hashlib
import json
import sys
assert __debug__
IDENTITY='ROOT_MASS_CONDITIONED_LOWER_CONVEX_ORDER_V1'
OUTPUT='root_mass_lower_exact.json'
Z=(F(0),F(0),F(0))

class Quad:
    """Exact Q(sqrt(21)); comparison uses integer/rational squares only."""
    def __init__(self,a=0,b=0):self.a=F(a);self.b=F(b)
    @staticmethod
    def co(x):return x if isinstance(x,Quad) else Quad(x)
    def __add__(self,x):
        x=self.co(x);return Quad(self.a+x.a,self.b+x.b)
    __radd__=__add__
    def __neg__(self):return Quad(-self.a,-self.b)
    def __sub__(self,x):return self+-self.co(x)
    def __rsub__(self,x):return self.co(x)+-self
    def __mul__(self,x):
        x=self.co(x);return Quad(self.a*x.a+21*self.b*x.b,self.a*x.b+self.b*x.a)
    __rmul__=__mul__
    def __truediv__(self,x):
        x=self.co(x);n=x.a*x.a-21*x.b*x.b
        assert n!=0
        return self*Quad(x.a/n,-x.b/n)
    def __rtruediv__(self,x):return self.co(x)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        q=Quad(1)
        for _ in range(n):q=q*self
        return q
    def __eq__(self,x):
        x=self.co(x);return self.a==x.a and self.b==x.b
    def sign(self):
        a,b=self.a,self.b
        sg=lambda x:(x>0)-(x<0)
        if b==0:return sg(a)
        if b>0:return 1 if a>=0 else sg(21*b*b-a*a)
        return -1 if a<=0 else sg(a*a-21*b*b)
    def __lt__(self,x):return (self-x).sign()<0
    def __le__(self,x):return (self-x).sign()<=0
    def __gt__(self,x):return (self-x).sign()>0
    def __ge__(self,x):return (self-x).sign()>=0
    def __repr__(self):return f'({self.a})+({self.b})*sqrt(21)'

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def add(a,b):
    c=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=x
    return trim(c)

def scale(a,s):return trim([s*x for x in a])
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)

def power(a,n):
    b=[F(1)]
    for _ in range(n):b=mul(b,a)
    return b

def ev(a,x):
    y=F(0)
    for c in reversed(a):y=y*x+c
    return y

def integral(a,l,r):return sum((c*(r**(i+1)-l**(i+1))/(i+1) for i,c in enumerate(a)),F(0))
def compose(a,l,r):
    out=[F(0)]
    for i,c in enumerate(a):out=add(out,scale(power([l,r-l],i),c))
    return out

def bernstein(a,l,r):
    p=compose(a,l,r);n=len(p)-1
    b=[sum((p[i]*F(comb(j,i),comb(n,i)) for i in range(j+1)),F(0)) for j in range(n+1)]
    out=[F(0)]
    for j,c in enumerate(b):out=add(out,scale(mul([F(0)]*j+[F(1)],power([F(1),F(-1)],n-j)),c*comb(n,j)))
    assert out==p
    return b

def certify(p,l,r,depth=0):
    b=bernstein(p,l,r)
    if min(b)>=0:return [{'interval':[l,r],'coefficients':b}]
    assert depth<16,('not certified',l,r,b)
    mid=(l+r)/2
    return certify(p,l,mid,depth+1)+certify(p,mid,r,depth+1)

def hinge_poly(values,mid):
    v=sorted(values);n=len(v)
    d=[power([x,F(-1)],n) if x>mid else [F(0)] for x in v]
    for k in range(1,n):
        d=[scale(power([v[i],F(-1)],n-k),F(comb(n,k))) if v[i]==v[i+k] and v[i]>mid
           else [F(0)] if v[i]==v[i+k]
           else scale(sub(d[i+1],d[i]),1/(v[i+k]-v[i])) for i in range(len(d)-1)]
    return scale(d[0],F(1,n))

def hinge(values,t):
    v=sorted(values);n=len(v);d=[max(x-t,F(0))**n for x in v]
    for k in range(1,n):
        d=[comb(n,k)*max(v[i]-t,F(0))**(n-k) if v[i]==v[i+k]
           else (d[i+1]-d[i])/(v[i+k]-v[i]) for i in range(len(d)-1)]
    return d[0]/n

def density_pieces(L,t,k):
    h2=3/(L+t*k*(k+1))
    return h2,scale(power([k,(1-k)/t],2),h2),scale(power([L,F(-1)],2),h2/(L-t)**2)

def lower_parameters(L,t,k):
    h2,p1,p2=density_pieces(L,t,k)
    moments=[integral(mul(p1,[F(0)]*j+[F(1)]),0,t)+integral(mul(p2,[F(0)]*j+[F(1)]),t,L) for j in range(3)]
    assert moments[0]==1 and moments[1]==1
    expected=h2*(L*(L*L+2*L*t+3*t*t)+k*(k+3)*t**3)/30
    assert moments[2]==expected
    return h2,k*k*h2,expected

def lower_tail_poly(L,t,k,mid):
    h2=3/(L+t*k*(k+1))
    if mid<t:return [F(1),F(-1),h2*k*k/2,h2*k*(1-k)/(3*t),h2*(1-k)**2/(12*t*t)]
    return scale(power([L,F(-1)],4),h2/(12*(L-t)**2))

def scalar_control():
    # Symmetric exact radial law: beta has total mass and first moment both 3.
    atoms=[(F(0),F(2,5)),(F(4,5),F(11,10)),(F(6,5),F(11,10)),(F(2),F(2,5))]
    assert sum(w for z,w in atoms)==3 and sum(z*w for z,w in atoms)==3
    H=F(2,5)+sum(w*z*z for z,w in atoms)/5
    assert H==F(736,625) and F(11,10)<H<F(4,3)
    def law_poly(mid):
        out=[F(0)]
        for z,w in atoms:out=add(out,scale(hinge_poly([F(1),z,z,z],mid),w/3))
        return out
    knots=[F(0),F(4,5),F(1),F(6,5),F(2)]
    certs=[]
    for l,r in zip(knots,knots[1:]):
        mid=(l+r)/2;p=law_poly(mid)
        lo=lower_tail_poly(F(2),F(1),F(0),mid)
        up=scale(power([F(2),F(-1)],2),F(1,4))
        gaps=[sub(p,lo),sub(up,p)]
        entry={'interval':[l,r],'law_polynomial':p,'lower_unconditioned':lo,'upper_frustum':up,'certificates':[]}
        for gap in gaps:entry['certificates'].append({'power_coefficients':gap,'cells':certify(gap,l,r)})
        for x in [l,mid,r]:
            actual=sum(w*hinge([F(1),z,z,z],x)/3 for z,w in atoms)
            assert actual==ev(p,x) and ev(lo,x)<=actual<=ev(up,x)
        certs.append(entry)
    # Algebraic lower comparator with root d0 < 1/4 < actual formal root 2/5.
    s=Quad(0,1);t=(-2+2*s)/5;k=F(1,2)
    h2,d0,H0=lower_parameters(F(2),t,k)
    assert d0==Quad(F(51,40),F(-9,40))
    assert H0==Quad(F(86,125),F(14,125))
    assert 0<d0<F(1,4)<F(2,5)<F(1,2)
    assert H0>F(6,5)>H
    assert 21>F(32,7)**2 and 21<F(23,5)**2
    # Earlier three-node candidate fails the unconditional lower tail at t=1.
    old=[(F(0),F(2,5)),(F(2),F(1,10)),(F(28,25),F(5,2))]
    oldH=F(2,5)+sum(w*z*z for z,w in old)/5
    assert oldH==F(692,625)
    oldgap=sum(w*hinge([F(1),z,z,z],F(1))/3 for z,w in old)-F(1,8)
    assert oldgap==F(-1,40)
    return {'status':'FORMAL_SCALAR_RADIAL_LAW_NOT_A_BODY_NOT_FULL_LAMBDA_OR_SPD',
            'boundary_atoms_z_mass':atoms,'L':F(2),'root_mass':F(2,5),'second_moment':H,
            'all_old_upper_and_new_unconditioned_lower_tail_certificates':certs,
            'algebraic_lower_comparator':{'field':'Q(sqrt(21))','t':t,'k':k,'height_squared':h2,'root_density':d0,'second_moment':H0},
            'rational_separation':F(6,5)-H,
            'rejected_earlier_control':{'atoms':old,'second_moment':oldH,'unconditioned_call_gap_at_1':oldgap}}

def va(a,b):return tuple(x+y for x,y in zip(a,b))
def vs(a,b):return tuple(x-y for x,y in zip(a,b))
def vm(a,s):return tuple(x*s for x in a)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))

def cycle(raw,ids,n):
    drop=next(i for i in range(3) if n[i]);keep=[i for i in range(3) if i!=drop]
    pts=sorted((raw[i][keep[0]],raw[i][keep[1]],i) for i in ids)
    def turn(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lo=[];hi=[]
    for p in pts:
        while len(lo)>1 and turn(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(hi)>1 and turn(hi[-2],hi[-1],p)<=0:hi.pop()
        hi.append(p)
    cyc=[p[2] for p in lo[:-1]+hi[:-1]]
    assert len(cyc)>=3
    if dot(cross(vs(raw[cyc[1]],raw[cyc[0]]),vs(raw[cyc[2]],raw[cyc[0]])),n)<0:cyc.reverse()
    j=cyc.index(min(cyc));return tuple(cyc[j:]+cyc[:j])

def hull(raw):
    planes={}
    for i,j,k in combinations(range(len(raw)),3):
        n=cross(vs(raw[j],raw[i]),vs(raw[k],raw[i]))
        if n==Z:continue
        b=dot(n,raw[i]);values=[dot(n,p)-b for p in raw]
        if all(s==0 for s in values):continue
        if all(s<=0 for s in values):pass
        elif all(s>=0 for s in values):n=vm(n,-1);b=-b
        else:continue
        ids=tuple(i for i,p in enumerate(raw) if dot(n,p)==b)
        planes.setdefault(ids,(n,b))
    faces=sorted((cycle(raw,ids,n),n,b) for ids,(n,b) in planes.items())
    volume=F(0);moment=Z
    for cyc,n,b in faces:
        a=raw[cyc[0]]
        for j in range(1,len(cyc)-1):
            c=raw[cyc[j]];d=raw[cyc[j+1]];w=det(a,c,d)/6
            volume+=w;moment=va(moment,vm(va(va(a,c),d),w/4))
    assert volume>0
    g=vm(moment,1/volume)
    assert all(dot(n,g)<b for cyc,n,b in faces)
    edges=sorted({tuple(sorted((cyc[j],cyc[(j+1)%len(cyc)]))) for cyc,n,b in faces for j in range(len(cyc))})
    vertices=sorted({i for cyc,n,b in faces for i in cyc})
    assert len(vertices)-len(edges)+len(faces)==2
    return volume,g,faces,edges,vertices

def equilibria(raw,g,faces,edges,vertices):
    stable=[];unstable=[];saddle=[];boundary=[];facet_checks=[];vertex_checks=[];edge_checks=[]
    for f,(cyc,n,b) in enumerate(faces):
        foot=va(g,vm(n,(b-dot(n,g))/dot(n,n)))
        tests=[dot(cross(vs(raw[cyc[(j+1)%len(cyc)]],raw[cyc[j]]),vs(foot,raw[cyc[j]])),n) for j in range(len(cyc))]
        if min(tests)>0:stable.append(f)
        elif min(tests)==0:boundary.append(['facet',f])
        facet_checks.append({'facet':f,'foot':foot,'inside_tests':tests})
    for i in vertices:
        w=vs(raw[i],g);tests=[dot(w,vs(raw[j],raw[i])) for j in vertices if j!=i]
        if max(tests)<0:unstable.append(i)
        elif max(tests)==0:boundary.append(['vertex',i])
        vertex_checks.append({'vertex':i,'normal_cone_tests':tests})
    for a,b in edges:
        common=[j for j,(cyc,n,c) in enumerate(faces) if a in cyc and b in cyc]
        assert len(common)==2
        e=vs(raw[b],raw[a]);t=dot(vs(g,raw[a]),e)/dot(e,e);foot=va(raw[a],vm(e,t));w=vs(foot,g)
        n1,n2=[faces[j][1] for j in common];aa=dot(n1,n1);ab=dot(n1,n2);bb=dot(n2,n2);dd=aa*bb-ab*ab
        assert dd>0
        alpha=(dot(w,n1)*bb-dot(w,n2)*ab)/dd;beta=(dot(w,n2)*aa-dot(w,n1)*ab)/dd
        assert va(vm(n1,alpha),vm(n2,beta))==w
        tests=[t,1-t,alpha,beta]
        if min(tests)>0:saddle.append((a,b))
        elif min(tests)==0:boundary.append(['edge',[a,b]])
        edge_checks.append({'edge':[a,b],'parameter':t,'normal_coefficients':[alpha,beta],'adjacent_facets':common})
    counts=[len(stable),len(unstable),len(saddle)]
    if not boundary:assert counts[0]+counts[1]-counts[2]==2
    return {'counts_S_U_H':counts,'stable_facets':stable,'unstable_vertices':unstable,'saddle_edges':saddle,
            'degenerate_boundary_entities':boundary,'facet_tests':facet_checks,'vertex_tests':vertex_checks,'edge_tests':edge_checks}

def body_control(name,points,k,peak_raw,equilibrium_audit=False):
    raw=[tuple(map(F,p)) for p in points]
    volume,g,faces,edges,vertices=hull(raw);mu=g[2]
    assert min(p[2] for p in raw)==0 and mu>0
    vals=[p[2]/mu for p in raw];L=max(vals);t=peak_raw/mu
    h2,d,second=lower_parameters(L,t,k)
    cones=[];rootmass=F(0)
    for cyc,n,b in faces:
        mass=F(0)
        for j in range(1,len(cyc)-1):
            ids=[cyc[0],cyc[j],cyc[j+1]]
            w=det(*(vs(raw[i],g) for i in ids))/(6*volume)
            assert w>0
            cones.append((w,[F(1)]+[vals[i] for i in ids]));mass+=3*w
        if all(vals[i]==0 for i in cyc):rootmass+=mass
    assert sum(w for w,vs0 in cones)==1
    actualmean=sum(w*sum(vs0,F(0))/4 for w,vs0 in cones)
    actualsecond=sum(w*(sum((v*v for v in vs0),F(0))+sum(vs0,F(0))**2)/20 for w,vs0 in cones)
    assert actualmean==1 and actualsecond==second and rootmass==d
    # All tail thresholds, proved by equality of polynomials on all knot cells.
    knots=sorted(set(vals+[F(1),t]));tails=[]
    for l,r in zip(knots,knots[1:]):
        mid=(l+r)/2;actual=[F(0)]
        for w,vs0 in cones:actual=add(actual,scale(hinge_poly(vs0,mid),w))
        expected=lower_tail_poly(L,t,k,mid)
        assert trim(actual)==trim(expected)
        for x in [l,mid,r]:assert ev(actual,x)==sum(w*hinge(vs0,x) for w,vs0 in cones)
        tails.append({'interval':[l,r],'identical_tail_polynomial':actual})
    data={'name':name,'raw_points':raw,'true_vertices':vertices,'true_edges':edges,'true_facets':[cyc for cyc,n,b in faces],
          'f_vector':[len(vertices),len(edges),len(faces)],'volume':volume,'own_centroid':g,'raw_ell':'z',
          'normalized_vertex_values':vals,'L':L,'t':t,'k':k,'density_height_squared':h2,'root_mass':rootmass,
          'second_moment':actualsecond,'all_tail_equality_certificates':tails}
    if equilibrium_audit:data['euclidean_equilibria']=equilibria(raw,g,faces,edges,vertices)
    return data

def identities():
    controls=[]
    # These parameter triples have mean exactly one and include skew double cones.
    for L in [F(3,2),F(2),F(3),F(7,2)]:
        t=(4-L)/2;h2,d,H=lower_parameters(L,t,F(0))
        assert d==0 and H==(3*L*L-8*L+48)/40
        controls.append({'L':L,'t':t,'second_moment':H})
    # The auxiliary elementary root-cone improvement, integrated exactly.
    L=F(2);c=F(1);d=F(2,5);x=F(2,5)
    floor=sub(scale(power([F(1),-1/L],2),d),[F(0),F(0),3/(L*c*c)])
    b=[F(0),F(0)]+[a/F((i+1)*(i+2)) for i,a in enumerate(floor)]
    inc=2*integral(b,0,x)
    assert inc==F(1688,234375)
    assert inc-F(9,1250)==F(1,468750)
    # Derivative-sign numerators used in the existence/uniqueness proof.
    # For h'=-a(a+h)/(2Lh+at), test the two expanded identities as polynomials in a,h,L,t.
    derivative_checks=[]
    for a,h,L,t in [(F(1),F(2),F(2),F(1)),(F(3),F(2),F(5),F(3)),(F(0),F(2),F(4),F(1))]:
        den=2*L*h+a*t
        left=t*(-a*(a+h))-(h-a)*den
        right=(L-t)*(-a*(a+h))+h*den
        assert left==2*h*(a*(L-t)-L*h)
        assert right==(2*h+a)*(L*h-a*(L-t))
        derivative_checks.append([a,h,L,t,left,right])
    return {'double_cone_moment_controls':controls,'root_floor_call_polynomial':b,'root_floor_variance_increment':inc,
            'root_floor_old_control_gap':F(1,468750),'derivative_identity_substitution_controls_not_a_continuous_proof':derivative_checks}

def report():
    # A centered triangular double cone: lower unconditioned equality.
    base=[(-1,-1),(2,-1),(-1,2)]
    double=[(0,0,0)]+[(x,y,1) for x,y in base]+[(0,0,2)]
    q0=body_control('triangular_double_cone',double,F(0),F(1))
    assert q0['f_vector']==[5,9,6]
    # Nondegenerate and two-plane-merged versions of the same scalar extremal profile.
    B=[(0,0),(3,0),(4,1),(1,4),(0,2)]
    center=(F(8,5),F(7,5))
    Bc=[(F(x)-center[0],F(y)-center[1]) for x,y in B]
    generic=[(x,y,0) for x,y in Bc]+[(2*x,2*y,1) for x,y in Bc]+[(0,0,2)]
    q1=body_control('pentagonal_extremal_generic',generic,F(1,2),F(1))
    assert q1['f_vector']==[11,20,11]
    # The point (0,0,1) is omitted: it is the midpoint of two true vertices, not a vertex.
    merged=[(x,y,0) for x,y in B]+[(2*x,2*y,1) for x,y in B[1:]]+[(0,0,2)]
    q2=body_control('E17_extremal_two_coplanar_wall_merges',merged,F(1,2),F(1),True)
    assert q2['f_vector']==[10,17,9]
    assert q2['L']==F(88,37) and q2['t']==F(44,37)
    assert q2['root_mass']==F(111,484) and q2['second_moment']==F(1672,1369)
    assert q2['euclidean_equilibria']['counts_S_U_H']!=[1,1,0]
    assert not q2['euclidean_equilibria']['degenerate_boundary_entities']
    return {'identity':IDENTITY,'identities':identities(),'formal_control':scalar_control(),'actual_equality_controls':[q0,q1,q2],
            'universal_C_lower_bound_unchanged':34,'E17_equality_is_not_an_attainer_for_the_research_problem':True,
            'no_mechanical_SPD_exclusion_of_the_whole_equality_class_claimed':True,'exact_minimum_found':False}

def serial(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,Quad):return {'rational_part':str(x.a),'sqrt21_part':str(x.b)}
    if isinstance(x,dict):return {k:serial(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [serial(v) for v in x]
    return x

def main():
    if len(sys.argv)!=2 or sys.argv[1] not in ('build','check'):
        raise SystemExit('Usage: python -S root_mass_lower_exact.py build|check')
    obj=report();data=(json.dumps(serial(obj),sort_keys=True,indent=2)+'\n').encode('utf-8');path=Path(OUTPUT)
    if sys.argv[1]=='build':path.write_bytes(data)
    else:assert path.read_bytes()==data
    formal=obj['formal_control'];e17=obj['actual_equality_controls'][-1]
    cells=[c for e in formal['all_old_upper_and_new_unconditioned_lower_tail_certificates'] for d in e['certificates'] for c in d['cells']]
    print('ROOT_MASS_LOWER_ALGEBRA_EXACT_PASS')
    print('FORMAL_FULL_TWO_SIDED_CONVEX_ORDER_PASS',len(cells),sum(len(c['coefficients']) for c in cells))
    print('ROOT_MASS_CONDITIONED_LOWER_REJECTS_FORMAL_PASS',formal['rational_separation'])
    print('ALL_THRESHOLD_EQUALITY_CONTROLS_PASS',len(obj['actual_equality_controls']))
    print('ACTUAL_E17_EQUALITY_TRUE_EDGE_AUDIT_PASS',*e17['f_vector'])
    print('ACTUAL_E17_NOT_110_EUCLIDEAN_PASS',*e17['euclidean_equilibria']['counts_S_U_H'])
    print('ROOT_MASS_LOWER_RECOVERY_PASS',len(data),hashlib.sha256(data).hexdigest())
if __name__=='__main__':main()
