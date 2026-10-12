# material-7b1d742018e0

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Exact actual-polytope audits for a one-kink homothetic section family.
CPython >=3.11, standard library only. Assertions must remain enabled.
All inputs and non-default parameters are literal in this source.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sys
assert __debug__
Z=(F(0),)*3

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def scale(a,t):return tuple(t*x for x in a)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def det2(a,b):return a[0]*b[1]-a[1]*b[0]

def cycle(P,ids,n):
    drop=next(i for i in range(3) if n[i]);keep=[i for i in range(3) if i!=drop]
    pts=sorted((P[i][keep[0]],P[i][keep[1]],i) for i in ids)
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
    if dot(cross(sub(P[cyc[1]],P[cyc[0]]),sub(P[cyc[2]],P[cyc[0]])),n)<0:cyc.reverse()
    j=cyc.index(min(cyc));return tuple(cyc[j:]+cyc[:j])

def hull(P):
    planes={}
    for i,j,k in combinations(range(len(P)),3):
        n=cross(sub(P[j],P[i]),sub(P[k],P[i]));h=dot(n,P[i])
        if n==Z:continue
        vals=[dot(n,p)-h for p in P]
        if all(v==0 for v in vals):continue
        if all(v<=0 for v in vals):pass
        elif all(v>=0 for v in vals):n=scale(n,-1);h=-h
        else:continue
        ids=tuple(i for i,p in enumerate(P) if dot(n,p)==h)
        planes.setdefault(ids,(n,h))
    faces=sorted((cycle(P,ids,n),n,h) for ids,(n,h) in planes.items())
    edges=sorted({tuple(sorted((cyc[j],cyc[(j+1)%len(cyc)]))) for cyc,n,h in faces for j in range(len(cyc))})
    verts=sorted({i for cyc,n,h in faces for i in cyc})
    vol=F(0);mom=Z
    for cyc,n,h in faces:
        a=P[cyc[0]]
        for j in range(1,len(cyc)-1):
            b,c=P[cyc[j]],P[cyc[j+1]];v=det(a,b,c)/6
            vol+=v;mom=add(mom,scale(add(add(a,b),c),v/4))
    assert vol>0 and len(verts)-len(edges)+len(faces)==2
    g=scale(mom,1/vol)
    assert all(dot(n,g)<h for cyc,n,h in faces)
    data=[]
    for cyc,n,h in faces:
        v0=P[cyc[0]];av=Z;area_mom=Z;Aweight=F(0)
        for j in range(1,len(cyc)-1):
            a,b=P[cyc[j]],P[cyc[j+1]]
            nv=cross(sub(a,v0),sub(b,v0));w=dot(n,nv)
            assert w>0
            av=add(av,scale(nv,F(1,2)));Aweight+=w
            area_mom=add(area_mom,scale(add(add(v0,a),b),w/3))
        center=scale(area_mom,1/Aweight)
        pole=scale(n,1/(h-dot(n,g)))
        d=dot(av,sub(v0,g))/vol
        assert d>0
        data.append({'cycle':cyc,'normal':n,'h':h,'center':center,'pole':pole,'d':d})
    assert sum(f['d'] for f in data)==3
    assert all(sum((f['d']*f['pole'][j] for f in data),F(0))==0 for j in range(3))
    return {'volume':vol,'centroid':g,'faces':data,'edges':edges,'vertices':verts,'f_vector':[len(verts),len(edges),len(data)]}

def polygon(B):
    n=len(B);ar=sum((det2(B[i],B[(i+1)%n]) for i in range(n)),F(0))/2
    assert ar>0
    for i in range(n):
        e=sub(B[(i+1)%n],B[i])
        assert all(det2(e,sub(p,B[i]))>0 for j,p in enumerate(B) if j not in (i,(i+1)%n))
    c=tuple(sum((det2(B[i],B[(i+1)%n])*(B[i][j]+B[(i+1)%n][j]) for i in range(n)),F(0))/(6*ar) for j in range(2))
    return ar,c

def make(B,s,rho,O=(0,0)):
    B=[tuple(map(F,b)) for b in B];s=F(s);rho=F(rho);O=tuple(map(F,O))
    ar,c=polygon(B);B=[sub(b,O) for b in B];c=sub(c,O)
    assert 0<s<1 and rho>1-s
    guards=[det2(sub(B[(i+1)%len(B)],b),scale(b,-1)) for i,b in enumerate(B)]
    assert min(guards)>=0
    P=[b+(F(0),) for b in B]+[scale(b,rho)+(s,) for b in B]+[(F(0),F(0),F(1))]
    out=hull(P);D=rho*rho+s*(1+rho);J=rho**3+s*(1+rho+rho*rho)
    mu=(rho*rho*(1+2*s)+s*s*(1+2*rho))/(4*D);alpha=3*J/(4*D)
    assert out['volume']==ar*D/3
    assert out['centroid']==scale(c,alpha)+(mu,)
    n=len(B);zero=sum(q==0 for q in guards);at_vertex=any(b==(0,0) for b in B)
    expected=[2*n+1-int(at_vertex),4*n-zero-int(at_vertex),2*n+1-zero]
    assert out['f_vector']==expected
    for f in out['faces']:
        f['root_ell_mean']=f['center'][2]/mu
        f['root_trace']=f['d']*f['root_ell_mean']
    pairs=[]
    for i,j in combinations(range(len(out['faces'])),2):
        f,h=out['faces'][i],out['faces'][j]
        if len(f['cycle'])==len(h['cycle'])==3 and len(set(f['cycle'])&set(h['cycle']))==2:
            pairs.append({'faces':[i,j],'cycles':[f['cycle'],h['cycle']],'mass':f['d']+h['d'],'trace':f['root_trace']+h['root_trace']})
    return {'B':B,'s':s,'rho':rho,'raw_points':P,'origin_stratum':['interior','edge','vertex'][zero],
            'D':D,'alpha':alpha,'mu':mu,'geometry':out,'adjacent_triangle_pairs':pairs}

def serial(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:serial(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [serial(v) for v in x]
    return x

# Sparse polynomials in two variables; no numerical interpolation.
def pa(a,b):
    c=dict(a)
    for k,v in b.items():c[k]=c.get(k,F(0))+v
    return {k:v for k,v in c.items() if v}
def pn(a):return {k:-v for k,v in a.items()}
def ps(a,b):return pa(a,pn(b))
def pm(a,b):
    c={}
    for i,x in a.items():
        for j,y in b.items():
            k=tuple(i[z]+j[z] for z in range(2));c[k]=c.get(k,F(0))+x*y
    return {k:v for k,v in c.items() if v}
def pc(x):return {(0,0):F(x)} if x else {}
def pp(a,n):
    r=pc(1)
    for _ in range(n):r=pm(r,a)
    return r
def pt(a,t):return pm(pc(t),a)
def pe(a,x,y):return sum((v*x**i*y**j for (i,j),v in a.items()),F(0))

def polynomial_proof():
    r={(1,0):F(1)};s={(0,1):F(1)};one=pc(1)
    D=pa(pp(r,2),pm(s,pa(one,r)))
    J=pa(pp(r,3),pm(s,pa(pa(one,r),pp(r,2))))
    N=pa(pm(pp(r,2),pa(one,pt(s,2))),pm(pp(s,2),pa(one,pt(r,2))))
    K=pm(pm(s,ps(pa(r,s),one)),pa(pa(pp(r,2),pt(r,2)),pc(3)))
    assert K==ps(ps(pt(pm(D,r),4),pm(r,N)),pt(pm(ps(one,s),J),3))
    gap=ps(pt(pm(D,N),2),pm(pm(r,pa(one,pt(s,2))),pa(K,pt(pm(ps(one,s),J),2))))
    assert all(j>=1 for i,j in gap)
    P={(i,j-1):a for (i,j),a in gap.items()}
    expectedP={(4,1):2,(4,0):1,(3,2):2,(3,1):3,(3,0):-1,
               (2,2):4,(2,0):-1,(1,2):4,(1,1):1,(1,0):1,(0,2):2}
    assert P==expectedP
    # r=(1+t)/(1+z), s=z/(1+z), t,z>0.
    t=r;z=s;R={}
    for (i,j),a in P.items():
        term=pm(pm(pp(pa(one,t),i),pp(z,j)),pp(pa(one,z),5-i-j))
        R=pa(R,pt(term,a))
    expectedR={(4,1):3,(4,0):1,(3,2):4,(3,1):13,(3,0):3,
               (2,3):3,(2,2):13,(2,1):18,(2,0):2,
               (1,4):6,(1,3):21,(1,2):27,(1,1):14,
               (0,5):2,(0,4):12,(0,3):24,(0,2):20,(0,1):6}
    assert R==expectedR and min(R.values())>0 and R[(0,1)]==6
    return {'K_factor':[[i,j,a] for (i,j),a in sorted(K.items())],
            'gap_divided_by_s_P':[[i,j,a] for (i,j),a in sorted(P.items())],
            'positive_transformed_R':[[i,j,a] for (i,j),a in sorted(R.items())]}

def pair_formula(o):
    B=o['B'];s=o['s'];r=o['rho'];A,c=polygon(B);n=len(B)
    D=o['D'];J=r**3+s*(1+r+r*r);N=r*r*(1+2*s)+s*s*(1+2*r)
    K=s*(r+s-1)*(r*r+2*r+3)
    P=2*r**4*s+r**4+2*r**3*s*s+3*r**3*s-r**3+4*r*r*s*s-r*r+4*r*s*s+r*s+r+2*s*s
    delta=s*P/(D*N);assert delta>0
    out=[]
    for p in o['adjacent_triangle_pairs']:
        ids=[]
        for cyc in p['cycles']:
            found=[i for i in range(n) if set(cyc)=={n+i,n+(i+1)%n,2*n}]
            assert len(found)==1;ids.extend(found)
        assert (ids[0]-ids[1])%n in (1,n-1)
        u=sum((det2(B[i],B[(i+1)%n]) for i in ids),F(0))/(2*A)
        v=sum((det2(sub(B[i],c),sub(B[(i+1)%n],c)) for i in ids),F(0))/(2*A)
        assert 0<=u<=1 and 0<v<=F(2,3)
        T=r*(1+2*s)*(K*u+3*(1-s)*J*v)/(D*N)
        assert T==p['trace']
        deficit=delta+r*(1+2*s)*(K*(1-u)+3*(1-s)*J*(F(2,3)-v))/(D*N)
        assert 2-T==deficit and T<2 and deficit>=delta
        out.append({'pair':p,'planar_edges':ids,'area_fraction_u':u,'centroid_cone_fraction_v':v,
                    'exact_T':T,'exact_2_minus_T':deficit,'positive_profile_gap':delta})
    return out

def equilibria(P,h):
    g=h['centroid'];faces=h['faces'];S=[];U=[];H=[];boundary=[]
    for i,f in enumerate(faces):
        cyc=f['cycle'];n=f['normal'];b=f['h']
        foot=add(g,scale(n,(b-dot(n,g))/dot(n,n)))
        ts=[dot(cross(sub(P[cyc[(j+1)%len(cyc)]],P[cyc[j]]),sub(foot,P[cyc[j]])),n) for j in range(len(cyc))]
        if min(ts)>0:S.append(i)
        elif min(ts)==0:boundary.append(['facet',i])
    for i in h['vertices']:
        ts=[dot(sub(P[i],g),sub(P[j],P[i])) for j in h['vertices'] if j!=i]
        if max(ts)<0:U.append(i)
        elif max(ts)==0:boundary.append(['vertex',i])
    for a,b in h['edges']:
        ids=[i for i,f in enumerate(faces) if a in f['cycle'] and b in f['cycle']];assert len(ids)==2
        e=sub(P[b],P[a]);t=dot(sub(g,P[a]),e)/dot(e,e);w=sub(add(P[a],scale(e,t)),g)
        n1,n2=[faces[i]['normal'] for i in ids];aa=dot(n1,n1);bb=dot(n2,n2);ab=dot(n1,n2);dd=aa*bb-ab*ab
        assert dd>0
        x=(dot(w,n1)*bb-dot(w,n2)*ab)/dd;y=(dot(w,n2)*aa-dot(w,n1)*ab)/dd
        assert add(scale(n1,x),scale(n2,y))==w
        ts=[t,1-t,x,y]
        if min(ts)>0:H.append([a,b])
        elif min(ts)==0:boundary.append(['edge',[a,b]])
    if not boundary:assert len(S)+len(U)-len(H)==2
    return {'strict_counts_S_U_H':[len(S),len(U),len(H)],'stable_faces':S,'unstable_vertices':U,'saddle_edges':H,'boundary_entities':boundary}

def report():
    algebra=polynomial_proof();controls=[]
    polygons=[[(0,0),(2,0),(0,2)],[(0,0),(2,0),(2,2),(0,2)],
              [(0,0),(3,0),(4,1),(1,4),(0,2)],
              [(0,0),(2,0),(3,1),(3,2),(1,3),(0,2)]]
    profiles=[(F(1,2),F(2)),(F(3,4),F(1,2)),(F(1,3),F(1))]
    for B in polygons:
        A,c=polygon([tuple(map(F,b)) for b in B])
        for O in [c,(F(1),F(0)),(F(0),F(0))]:
            for s,r in profiles:
                o=make(B,s,r,O);o['pair_certificates']=pair_formula(o);controls.append(o)
    sharp=[]
    for R in [2,5,20,100]:
        B=[(0,0),(1,0),(R,F(R,2)),(F(R,2),R),(0,1)]
        o=make(B,F(1,R),2);assert o['geometry']['f_vector']==[10,17,9]
        cc=F(9*R*R+6*R+4,6*(3*R+4));A,c=polygon(o['B']);assert c==(cc,cc)
        assert A==F(R*(3*R+4),8)
        certs=pair_formula(o);assert len(certs)==2
        expected_u=F(3*R+2,3*R+4)
        expected_v=F(2,3)-F(2*(3*R+2)**2,3*R*(3*R+4)**2)
        assert all(q['area_fraction_u']==expected_u and q['centroid_cone_fraction_v']==expected_v for q in certs)
        o['pair_certificates']=certs;o['euclidean_equilibria']=equilibria(o['raw_points'],o['geometry'])
        assert o['euclidean_equilibria']['strict_counts_S_U_H']!=[1,1,0]
        sharp.append(o)
    # Preserve the complete finite exact exploratory parameter set and outputs.
    scan=[]
    for R in [2,5,20,100]:
        B=[(0,0),(1,0),(R,F(R,2)),(F(R,2),R),(0,1)]
        for s in [F(1,100),F(1,10),F(1,2)]:
            for r in [2,10,100]:
                o=make(B,s,r);cs=pair_formula(o);q=max(cs,key=lambda q:q['exact_T'])
                scan.append({'R':R,'s':s,'rho':r,'max_pair_trace':q['exact_T'],'pair_mass':q['pair']['mass']})
    return {'identity':'LOWER_EQUALITY_TRUE_FVECTOR_AND_ADJACENT_TRIANGLE_CAP_2_V1',
            'polynomial_identities':algebra,'classification_controls':controls,'sharp_E17_controls':sharp,
            'finite_exploration_not_an_infeasibility_proof':scan,
            'universal_C_lower_bound_unchanged':34,'exact_minimum_found':False,
            'no_whole_E17_or_whole_lower_equality_mechanical_exclusion_claimed':True}

OUTPUT='lower_equality_structure.json'
def main():
    if len(sys.argv)!=2 or sys.argv[1] not in ('build','check'):
        raise SystemExit('Usage: python -S lower_class_exact.py build|check')
    o=report();data=(json.dumps(serial(o),sort_keys=True,indent=2)+'\n').encode('utf-8');p=Path(OUTPUT)
    if sys.argv[1]=='build':p.write_bytes(data)
    else:assert p.read_bytes()==data
    pairs=sum(len(c['pair_certificates']) for c in o['classification_controls'])
    print('LOWER_EQUALITY_EXACT_POLYNOMIAL_IDENTITIES_PASS',len(o['polynomial_identities']['positive_transformed_R']))
    print('LOWER_EQUALITY_TRUE_FVECTOR_STRATA_PASS',len(o['classification_controls']))
    print('LOWER_EQUALITY_ACTUAL_TRIANGLE_PAIR_CAP_2_PASS',pairs)
    print('LOWER_EQUALITY_SHARP_E17_CONTROLS_PASS',len(o['sharp_E17_controls']))
    print('LOWER_EQUALITY_FINITE_EXPLORATION_PRESERVED',len(o['finite_exploration_not_an_infeasibility_proof']))
    print('LOWER_EQUALITY_STRUCTURE_RECOVERY_PASS',len(data),hashlib.sha256(data).hexdigest())
if __name__=='__main__':main()
