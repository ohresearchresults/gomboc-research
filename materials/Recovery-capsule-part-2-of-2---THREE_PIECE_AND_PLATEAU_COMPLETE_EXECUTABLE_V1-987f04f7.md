# material-987f04f7f70f

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Recovery capsule part 2 of 2: complete standalone executed source

Object: THREE_PIECE_ZERO_END_ALL_FACETS_AND_ARBITRARY_CONCAVE_PLATEAUX_V1.
Proof and precise scope: [internal-source-reference].
Save the complete code below as homothetic_three_piece_and_plateau.py with LF and one final newline,14574B,SHA25611e7ec2681f37702b5829eee2e492e9d476d2f982d08485211a9f78170747293.
CPython3.13.5,SymPy1.14.0,assertions enabled. No external computational dependencies beyond SymPy. Run python -B homothetic_three_piece_and_plateau.py > three_plateau.log. Expected report1232934B,SHAc0ac4ee26585930711ba638cbb7452ecb694d0022a899bd6a8416af863957df8; log589B,SHA505ee0822ba9fd5c2a16488a9257fbceef5cd23e800304e115ed862e511e62dc. Normal and fresh source-only execution completed with identical bytes. Final marker THREE_PIECE_AND_ARBITRARY_CONCAVE_PLATEAU_EXACT_RECOVERY_PASS.

```python
"""Whole facets of three-piece zero-end profiles and arbitrary concave plateaux.
CPython 3.13.5, SymPy 1.14.0; assertions enabled; no external input or helper.
Polynomial certificates are global. Geometric controls are not localization.
Analytical arbitrary-base input: [internal-source-reference].
Integration/census routines adapted from exact [internal-source-reference].
"""
from pathlib import Path
import hashlib, json, itertools, math
from fractions import Fraction
import sympy as S
Q=S.Rational
a,b,q,z,x=S.symbols('a b q z x',real=True)

def clean(v):return S.factor(S.cancel(v))
def matzero(v):assert v.applyfunc(clean)==S.zeros(*v.shape),v

def integ(expr,lo,hi):
    p=S.Poly(S.expand(expr),z)
    return clean(sum(c*(hi**(i+1)-lo**(i+1))/S.Integer(i+1) for (i,),c in p.terms()))

def polynomial_system():
    pieces=[(-a,0,(z+a)/a),(0,1,1+(q-1)*z),(1,1+b,q*(1-(z-1)/b))]
    def moment(hp,zp):return clean(sum(integ(h**hp*z**zp,lo,hi) for lo,hi,h in pieces))
    V=moment(2,0);M=moment(2,1);E=moment(2,2);N4=moment(4,0)
    records=[]
    for idx in (0,1):
        lo,hi,h=pieces[idx];Dn=clean(h.subs(z,0)*V+S.diff(h,z)*M)
        P3=integ(h**3,lo,hi);P20=integ(h**2,lo,hi);P21=integ(z*h**2,lo,hi)
        P10=integ(h,lo,hi);P11=integ(z*h,lo,hi);P12=integ(z*z*h,lo,hi)
        Hn=clean(N4*V-Dn*P3)
        Cn=clean(Dn*(V*P21-M*P20))
        Rn=clean(Q(9,4)*V**2*(V*E-M*M)-Dn*(V*V*P12-2*V*M*P11+M*M*P10))
        Dtn=clean(Hn*Rn-Cn*Cn)
        records.append(dict(piece_index=idx,Dnum=Dn,H_scaled=Hn,C_scaled=Cn,R_scaled=Rn,det_scaled=Dtn))
    return dict(V=V,M=M,E=E,N4=N4,pieces=pieces,gates=records)

def power_bernstein_certificate(expr,chart):
    nn,dd=S.fraction(clean(expr))
    dpoly=S.Poly(dd,a,b,q,domain=S.QQ)
    assert dpoly.terms() and all(c>0 for _,c in dpoly.terms())
    poly=S.Poly(nn,a,b,q,domain=S.QQ);dq=poly.degree(q)
    if chart=='outer_full':qn=a*b+x*(a+b+1);qd=a*(b+1)
    elif chart=='middle_falling':qn=b+x;qd=b+1
    else:raise ValueError(chart)
    expanded=sum(c*a**ia*b**ib*qn**iq*qd**(dq-iq) for (ia,ib,iq),c in poly.terms())
    pp=S.Poly(S.expand(expanded),a,b,x,domain=S.QQ)
    terms={ij:Fraction(c) for ij,c in pp.terms()}
    blocks=[];negative=zeros=count=0;first_witness=last_witness=None
    for ia,ib in sorted({ij[:2] for ij in terms}):
        values={ix:c for (ja,jb,ix),c in terms.items() if (ja,jb)==(ia,ib)}
        degree=max(values);controls=[]
        for k in range(degree+1):
            val=sum(c*Fraction(math.comb(k,j),math.comb(degree,j)) for j,c in values.items() if j<=k)
            assert val>=0,(chart,ia,ib,k,val)
            controls.append(val);count+=1;zeros+=val==0
        if controls[0]>0 and first_witness is None:first_witness=(ia,ib,0,str(controls[0]))
        if controls[-1]>0 and last_witness is None:last_witness=(ia,ib,degree,str(controls[-1]))
        blocks.append(dict(a_power=ia,b_power=ib,degree=degree,controls=list(map(str,controls))))
    # Positive endpoint witnesses and nonnegative Bernstein controls imply
    # strict positivity for every a,b>0 and every x in the CLOSED unit interval.
    assert first_witness is not None and last_witness is not None
    return dict(chart=chart,substitution=qn/qd,cleared_positive_power=dq,
                original_denominator=dd,positive_denominator_terms=dpoly.terms(),
                degrees=pp.degree_list(),polynomial_terms=pp.terms(),blocks=blocks,
                control_count=count,zero_controls=zeros,negative_controls=negative,
                strict_endpoint_witnesses=(first_witness,last_witness))

def all_certificates(system):
    out={}
    for gate,chart in zip(system['gates'],('outer_full','middle_falling')):
        for name in ('H_scaled','R_scaled','det_scaled'):
            out[chart+'_'+name]=power_bernstein_certificate(gate[name],chart)
    return out

def polygon_moments(points):
    area=S.S.Zero;first=S.zeros(2,1);second=S.zeros(2)
    for aa,bb in zip(points,points[1:]+points[:1]):
        det=S.det(S.Matrix.hstack(aa,bb));area+=det/2;first+=det*(aa+bb)/6
        ss=aa+bb;second+=det*(ss*ss.T+aa*aa.T+bb*bb.T)/24
    assert area>0
    g=(first/area).applyfunc(clean);cov=(second/area-g*g.T).applyfunc(clean)
    assert cov.det()>0
    return area,g,cov

def positive_definite(matrix):
    matrix=matrix.applyfunc(clean)
    minors={str(ids):clean(matrix.extract(ids,ids).det())
            for k in range(1,matrix.rows+1) for ids in itertools.combinations(range(matrix.rows),k)}
    assert all(v>0 for v in minors.values()),minors
    return minors

def exact_polytope(vertices,cycles):
    interior=sum(vertices,S.zeros(3,1))/len(vertices) # orientation ONLY, never the mass centre
    faces=[]
    for old in cycles:
        f=list(old);aa,bb,cc=[vertices[i] for i in f[:3]];n=(bb-aa).cross(cc-aa)
        assert n.dot(n)>0
        if n.dot(aa-interior)<0:f.reverse()
        aa,bb,cc=[vertices[i] for i in f[:3]];n=(bb-aa).cross(cc-aa)
        assert n.dot(aa-interior)>0
        for j,v in enumerate(vertices):
            value=clean(n.dot(v-aa));assert value==0 if j in f else value<0
        faces.append(tuple(f))
    edges=sorted({tuple(sorted(e)) for f in faces for e in zip(f,f[1:]+f[:1])})
    assert len(vertices)-len(edges)+len(faces)==2
    incidence={e:[j for j,f in enumerate(faces) if e in [tuple(sorted(ab)) for ab in zip(f,f[1:]+f[:1])]] for e in edges}
    assert all(len(v)==2 for v in incidence.values())
    V=S.S.Zero;first=S.zeros(3,1);second=S.zeros(3)
    for f in faces:
        aa=vertices[f[0]]
        for k in range(1,len(f)-1):
            bb,cc=vertices[f[k]],vertices[f[k+1]];det=S.det(S.Matrix.hstack(aa,bb,cc));v=aa+bb+cc
            V+=det/6;first+=det*v/24
            second+=det*(v*v.T+aa*aa.T+bb*bb.T+cc*cc.T)/120
    V=clean(V);assert V>0
    g=(first/V).applyfunc(clean);cov=(second/V-g*g.T).applyfunc(clean);positive_definite(cov)
    data=[]
    for f in faces:
        aa,bb,cc=[vertices[i] for i in f[:3]];n=(bb-aa).cross(cc-aa)
        support=clean(n.dot(aa-g));assert support>0
        mass=S.S.Zero;moment1=S.zeros(3,1);moment2=S.zeros(3)
        for k in range(1,len(f)-1):
            bb,cc=vertices[f[k]],vertices[f[k+1]];w=clean(n.dot((bb-aa).cross(cc-aa)));assert w>0
            v=aa+bb+cc;mass+=w;moment1+=w*v/3
            moment2+=w*(v*v.T+aa*aa.T+bb*bb.T+cc*cc.T)/12
        cf=(moment1/mass-g).applyfunc(clean)
        T=(moment2/mass-(moment1/mass)*g.T-g*(moment1/mass).T+g*g.T).applyfunc(clean)
        alpha=clean(support*mass/(2*n.dot(n)*V));pole=(n/support).applyfunc(clean)
        matzero(T*pole-cf)
        gap=(Q(3,2)*cov-alpha*T).applyfunc(clean)
        data.append(dict(vertices=f,alpha=alpha,c=cf,T=T,pole=pole,gap=gap,
                         positive_principal_minors=positive_definite(gap)))
    centered=[v-g for v in vertices];poles=[f['pole'] for f in data]
    stable=[i for i,v in enumerate(poles) if all(v.dot(w)-v.dot(v)<0 for j,w in enumerate(poles) if j!=i)]
    unstable=[i for i,v in enumerate(centered) if all(v.dot(centered[j]-v)<0 for e in edges if i in e for j in e if j!=i)]
    saddles=[];weak=[];primitives=[]
    for e in edges:
        i,j=e;k,l=incidence[e];aa,bb=centered[i],centered[j];cc,dd=poles[k],poles[l]
        values=[clean(aa.dot(bb)-aa.dot(aa)),clean(aa.dot(bb)-bb.dot(bb)),clean(cc.dot(dd)-cc.dot(cc)),clean(cc.dot(dd)-dd.dot(dd))]
        if all(t<0 for t in values):saddles.append(e)
        if all(t<=0 for t in values) and any(t==0 for t in values):weak.append(e)
        primitives.append(dict(edge=e,facets=(k,l),values=values))
    if not weak:assert len(stable)+len(unstable)-len(saddles)==2
    return dict(vertices=vertices,faces=faces,edges=edges,volume=V,centroid=g,Sigma=cov,facet_moments=data,
                own_euclidean=dict(S=stable,U=unstable,H=saddles,physical_weak_edge_packets=weak),all_edge_primitives=primitives)

def profile_polytope(base,aa,bb,qq):
    assert aa>0 and bb>0 and bb/(bb+1)<=qq<=(aa+1)/aa
    levels=[(-aa,S.S.Zero),(S.S.Zero,S.S.One),(S.S.One,qq),(1+bb,S.S.Zero)]
    merged=[]
    if qq==1+1/aa:levels.pop(1);merged.append('left_and_middle')
    elif qq==bb/(bb+1):levels.pop(2);merged.append('middle_and_right')
    vertices=[];rings=[]
    for zz,h in levels:
        if h==0:rings.append([len(vertices)]);vertices.append(S.Matrix((0,0,zz)))
        else:
            ring=[]
            for v in base:ring.append(len(vertices));vertices.append(S.Matrix((h*v[0],h*v[1],zz)))
            rings.append(ring)
    faces=[];n=len(base)
    for low,high in zip(rings,rings[1:]):
        for j in range(n):
            jj=(j+1)%n
            if len(low)==1:face=(low[0],high[j],high[jj])
            elif len(high)==1:face=(low[j],low[jj],high[0])
            else:face=(low[j],low[jj],high[jj],high[j])
            faces.append(face)
    return exact_polytope(vertices,faces),merged

def actual_polytope_controls(system):
    square=[S.Matrix(p) for p in [(-1,-1),(1,-1),(1,1),(-1,1)]]
    pentagon=[S.Matrix(p) for p in [(0,0),(3,0),(4,1),(2,3),(-1,2)]]
    triangle=[S.Matrix(p) for p in [(0,0),(3,0),(1,2)]]
    cases=[('square_flat_top',square,Q(2),Q(3),Q(1)),
           ('pentagon_falling_middle',pentagon,Q(2),Q(1),Q(3,4)),
           ('triangle_rising_middle',triangle,Q(1),Q(2),Q(3,2)),
           ('square_left_merge',square,Q(2),Q(1),Q(3,2)),
           ('square_right_merge',square,Q(1),Q(2),Q(2,3))]
    records=[]
    for name,raw,aa,bb,qq in cases:
        area,bg,bc=polygon_moments(raw);base=[v-bg for v in raw]
        body,merged=profile_polytope(base,aa,bb,qq);values={a:aa,b:bb,q:qq}
        V=system['V'].subs(values);M=system['M'].subs(values);E=system['E'].subs(values);N4=system['N4'].subs(values)
        mu=clean(M/V);cv=S.zeros(3);cv[:2,:2]=N4/V*bc;cv[2,2]=clean(E/V-mu*mu)
        assert body['volume']==area*V
        matzero(body['centroid']-S.Matrix((0,0,mu)));matzero(body['Sigma']-cv)
        records.append(dict(name=name,raw_base=raw,base_centroid=bg,parameters=(aa,bb,qq),merged=merged,body=body))
    return records

def curved_plateau_control():
    # Actual continuous concave profile: quadratic left tail, a plateau,
    # and a square-root-of-quadratic right tail. Both endpoint heights vanish.
    hleft=1-z*z/4;right_squared=1-(z-1)**2/9
    def moment(hp,zp):
        assert hp%2==0
        return clean(integ(z**zp*hleft**hp,-2,0)+integ(z**zp,0,1)+integ(z**zp*right_squared**(hp//2),1,4))
    V=moment(2,0);M=moment(2,1);E=moment(2,2);N4=moment(4,0);mu=clean(M/V);variance=clean(E-M*M/V)
    assert mu!=Q(1,2)
    Sin=clean(Q(1,3)-mu+mu*mu);Sout=clean(variance-Sin);H=clean(N4-1);C=clean(Q(1,2)-mu)
    Vout=clean(V-1);ratio=clean(Vout/H)
    assert 0<ratio<=Q(5,3) and H>0 and Sin>0 and Sout>0
    assert C*C<=Vout*Sout
    gate=clean(H*(Q(9,4)*variance-Sin)-C*C)
    lower=clean(H*(Q(5,4)*Sin+Q(7,12)*Sout))
    assert gate>=lower>0
    raw=[S.Matrix(p) for p in [(0,0),(3,0),(4,1),(2,3),(-1,2)]]
    area,bg,bc=polygon_moments(raw);base=[v-bg for v in raw]
    cov=S.zeros(3);cov[:2,:2]=N4/V*bc;cov[2,2]=variance/V;facets=[]
    for aa,bb in zip(base,base[1:]+base[:1]):
        d=bb-aa;n=S.Matrix((d[1],-d[0]));support=clean(n.dot(aa));assert support>0
        alphaD=clean(support/area);ce=(aa+bb)/2
        Te=(aa*aa.T+bb*bb.T)/3+(aa*bb.T+bb*aa.T)/6
        T=S.zeros(3);T[:2,:2]=Te;T[:2,2]=ce*C;T[2,:2]=(ce*C).T;T[2,2]=Sin
        pole=S.Matrix((n[0]/support,n[1]/support,0));cf=S.Matrix((ce[0],ce[1],C))
        matzero(T*pole-cf)
        gap=(Q(3,2)*cov-alphaD*T/V).applyfunc(clean)
        facets.append(dict(vertices=[(aa[0],aa[1],0),(bb[0],bb[1],0),(bb[0],bb[1],1),(aa[0],aa[1],1)],
                           alpha=alphaD/V,T=T,c=cf,pole=pole,gap=gap,positive_principal_minors=positive_definite(gap)))
    return dict(profile=dict(left=hleft,left_interval=(-2,0),plateau_interval=(0,1),right_squared=right_squared,right_interval=(1,4)),
                raw_base=raw,base_centroid=bg,actual_volume=area*V,actual_centroid=(0,0,mu),Sigma=cov,
                profile_moments=dict(V=V,M=M,E=E,N4=N4,S=variance,Sin=Sin,Sout=Sout,H=H,C=C,tail_ratio=ratio,gate=gate,strict_gate_lower_bound=lower),
                whole_flat_facets=facets,scope='Five whole rectangular flat facets and curved lateral tails. No finite V/E/F or equilibrium census.')

def encode(v):
    if isinstance(v,S.MatrixBase):return [[encode(t) for t in row] for row in v.tolist()]
    if isinstance(v,S.Basic):return str(v)
    if isinstance(v,Fraction):return str(v)
    if isinstance(v,dict):return {str(k):encode(t) for k,t in v.items()}
    if isinstance(v,(tuple,list)):return [encode(t) for t in v]
    return v

def main():
    assert __debug__ and S.__version__=='1.14.0'
    system=polynomial_system();cert=all_certificates(system);controls=actual_polytope_controls(system);curved=curved_plateau_control()
    total=sum(c['control_count'] for c in cert.values());zeros=sum(c['zero_controls'] for c in cert.values())
    n=S.symbols('n',positive=True);sharp=clean(Q(3,2)/(1+Q(2,5)/n))
    assert S.limit(sharp,n,S.oo)==Q(3,2)
    report=dict(identity='THREE_PIECE_ZERO_END_ALL_FACETS_AND_ARBITRARY_CONCAVE_PLATEAUX_V1',
                arbitrary_base_source='[internal-source-reference]',polynomial_system=system,
                global_positive_certificates=cert,total_controls=total,zero_controls=zeros,negative_controls=0,
                actual_polytopes=controls,actual_curved_plateau=curved,
                sharp_sequence=dict(base='square [-1,1]^2',parameters=dict(a=1/n,b=1/n,q=1),test=(1,0,0),marked='central x=1 whole facet',ratio=sharp),
                scope='Every whole facet for three affine pieces with both end heights zero; arbitrary convex base and affine images. Every constant-maximum-height whole facet for arbitrary concave tails. Not arbitrary concave profiles, equilibrium exclusion or a new own110 body.')
    data=(json.dumps(encode(report),sort_keys=True,indent=2)+'\n').encode();Path('homothetic_three_piece_and_plateau_report.json').write_bytes(data)
    print('EXACT_THREE_PIECE_ZERO_END_ALL_FACETS_PASS',len(cert),total,zeros)
    for cc in controls:
        p=cc['body'];own=p['own_euclidean']
        print('ACTUAL',cc['name'],'VEF',len(p['vertices']),len(p['edges']),len(p['faces']),
              'OWN',len(own['S']),len(own['U']),len(own['H']),'WEAK_PACKETS',len(own['physical_weak_edge_packets']))
    print('ACTUAL_ASYMMETRIC_CURVED_PLATEAU_FIVE_WHOLE_FACETS_PD_PASS',curved['actual_centroid'][2])
    print('REPORT',len(data),hashlib.sha256(data).hexdigest())
    print('THREE_PIECE_AND_ARBITRARY_CONCAVE_PLATEAU_EXACT_RECOVERY_PASS')
if __name__=='__main__':main()
```
