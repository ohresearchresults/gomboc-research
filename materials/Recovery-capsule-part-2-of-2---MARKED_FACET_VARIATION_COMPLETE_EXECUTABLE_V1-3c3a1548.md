# material-3c3a1548d164

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Recovery capsule part 2 of 2: complete exact whole-facet variation source

Object TILTED_WHOLE_FACET_VARIATION_AND_WEIGHTED_LINE_REACTIONS_V1. Proof, scope and exact controls are in part1 [internal-source-reference]. Save the following code with LF and one final newline as marked_facet_variation.py,10541B SHAac48faa7324c7d70cd2dca38928f6851fd3f4fa0505afe80f36fa9a9c5317096. CPython3.13.5/SymPy1.14.0/assertions enabled/no inputs. Run python -B marked_facet_variation.py > marked_facet_variation.log. Report20899B SHA4d3f72a33b7b763bf68a39f2457ae9ad0f08122b3f6b843c8ad9ba55a8f0ebc6. Log236B SHA358ea2e20c4d2f8a4772135fa458345f65da1d85208529e2ad205125993f10b4. Normal and fresh source-only runs completed with identical bytes. Terminal marker MARKED_FACET_VARIATION_EXACT_PASS.

```python
"""Actual tilted whole-facet derivatives and weighted-line countercontrols.
CPython 3.13.5 / SymPy 1.14.0, assertions enabled; no inputs or random search.
The two curved controls satisfy geometric weighted line reactions only.
Their trial parabola is NOT their actual first-variation zero set.
"""
from pathlib import Path
import hashlib,json
import sympy as S
Q=S.Rational
t,y,s=S.symbols('t y s',real=True)

def clean(x):return S.factor(S.cancel(x))
def zero(x):assert clean(x)==0,clean(x)
def integrate(poly,var,lo,hi):
    p=S.Poly(S.expand(poly),var)
    return clean(sum(c*(hi**(j+1)-lo**(j+1))/S.Integer(j+1) for (j,),c in p.terms()))
def matrix_clean(M):return M.applyfunc(clean)

def abstract_identities():
    V,J,I,B0,B1,B2,B3,D,p,q=S.symbols('V J I B0 B1 B2 B3 D p q',nonzero=True)
    # Here psi=p+q*Y, with Y centred under the OLD actual body.
    E0=p*B0+q*B1;E1=p*B1+q*B2;E2=p*B2+q*B3
    Vs=V-s*E0;Js=J-s*V*p;mean=-s*E1/Vs
    Is=I-s*E2-s*s*E1*E1/Vs
    edge2=B2+s*D-2*mean*B1+mean*mean*B0
    expr=Js*edge2/(Vs*Is)
    derivative=clean(S.diff(expr,s).subs(s,0)/expr.subs(s,0))
    target=-V*p/J+D/B2+2*B1*E1/(V*B2)+E0/V+E2/I
    zero(derivative-target)
    pure_tilt=clean(target.subs({p:0,q:1}))
    zero(pure_tilt-D/B2-3*B1/V-B3/I)
    x,rho,H0,H1=S.symbols('x rho H0 H1')
    reaction=integrate(x*(x-1)*(x-rho)*(H0+(H1-H0)*x),x,0,1)
    zero(reaction-(5*H0*rho-2*H0+5*H1*rho-3*H1)/60)
    solution=(2*H0+3*H1)/(5*(H0+H1))
    zero(reaction.subs(rho,solution))
    return dict(general_log_derivative=target,pure_tilt_log_derivative=pure_tilt,
                weighted_line_reaction=reaction,weighted_line_fraction=solution,
                fraction_scope='H0,H1>=0, H0+H1>0; fraction lies in [2/5,3/5]')

def triangle_raw(vertices,expr):
    a,b=S.symbols('a b')
    v0,v1,v2=vertices
    point=v0+a*(v1-v0)+b*(v2-v0)
    jac=clean(S.det(S.Matrix.hstack(v1-v0,v2-v0)))
    poly=S.Poly(S.expand(expr.subs({t:point[0],y:point[1]},simultaneous=True)),a,b)
    value=sum(c*S.factorial(i)*S.factorial(j)/S.factorial(i+j+2) for (i,j),c in poly.terms())
    return clean(jac*value)

def tilted_triangle_control():
    ell=1+t+y/4
    original=[S.Matrix((0,-1)),S.Matrix((1,2)),S.Matrix((0,1))]
    V0=triangle_raw(original,ell);mu0=clean(triangle_raw(original,y*ell)/V0)
    p=-mu0;q=S.S.One # psi=y-mu0: a true sign-changing pure tilt.
    ta=s*(p-q)/(1-3*q*s);ya=3*ta-1
    tb=s*(p+q)/(1-q*s);yb=1+tb
    vertices=[S.Matrix((ta,ya)),S.Matrix((1,2)),S.Matrix((tb,yb))]
    # Independent exact first jets of the actual moving triangle integrals.
    jets=[v.applyfunc(lambda z:z.subs(s,0)+s*S.diff(z,s).subs(s,0)) for v in vertices]
    jet=lambda expr:clean(triangle_raw(jets,expr)).series(s,0,2).removeO()
    vj=jet(ell);jj=jet((t-s*(p+q*y))*ell);my=jet(y*ell);yy=jet(y*y*ell)
    yaj=ya.subs(s,0)+s*S.diff(ya,s).subs(s,0)
    ybj=yb.subs(s,0)+s*S.diff(yb,s).subs(s,0)
    ej=[integrate((1+s*(p+q*y)+y/4)*y**j,y,yaj,ybj).series(s,0,2).removeO() for j in range(3)]
    mu=clean(my/vj);ij=clean(yy-my*my/vj)
    b2j=clean(ej[2]-2*mu*ej[1]+mu*mu*ej[0])
    val=lambda z:clean(z.subs(s,0))
    derivative=lambda z:clean(S.diff(z,s).subs(s,0))
    actual_raw=dict(V=(val(vj),derivative(vj)),J=(val(jj),derivative(jj)),
                    mean_y=(val(mu),derivative(mu)),I=(val(ij),derivative(ij)),
                    B2=(val(b2j),derivative(b2j)))
    dlog=clean(derivative(jj)/val(jj)+derivative(b2j)/val(b2j)-derivative(vj)/val(vj)-derivative(ij)/val(ij))
    YY=y-mu0;old_edge=1+y/4
    E=[integrate(old_edge*YY**j,y,-1,1) for j in range(4)]
    D2=integrate((p+q*y)*YY**2,y,-1,1)+Q(5,4)*(p+q)*(1-mu0)**2-Q(3,4)*3*(p-q)*(-1-mu0)**2
    predicted=clean(D2/E[2]+3*E[1]/V0+E[3]/val(ij))
    zero(dlog-predicted);assert dlog!=0
    records=[]
    for value in (Q(-1,1000),S.S.Zero,Q(1,1000)):
        base=[matrix_clean(v.subs(s,value)) for v in vertices]
        assert S.det(S.Matrix.hstack(base[1]-base[0],base[2]-base[0]))>0
        moment=lambda expr:triangle_raw(base,expr)
        V=moment(ell);gt=clean(moment(t*ell)/V);gm=clean(moment(y*ell)/V)
        J=moment((t-value*(p+q*y))*ell);m=clean(J/V);I=clean(moment(y*y*ell)-V*gm*gm)
        ed=ell.subs(t,value*(p+q*y));lo=ya.subs(s,value);hi=yb.subs(s,value)
        edge=[integrate(ed*(y-gm)**j,y,lo,hi) for j in range(3)]
        sigma=S.Matrix([[moment(t*t*ell)/V-gt*gt,moment(t*y*ell)/V-gt*gm,0],
                        [moment(t*y*ell)/V-gt*gm,I/V,0],
                        [0,0,moment(ell**3)/(12*V)]]).applyfunc(clean)
        ee=S.Matrix((value*(p+q*y)-gt,y-gm,0))
        cf=ee.applyfunc(lambda z:integrate(ed*z,y,lo,hi)/edge[0]).applyfunc(clean)
        TF=(ee*ee.T).applyfunc(lambda z:integrate(ed*z,y,lo,hi)/edge[0])
        TF[2,2]=integrate(ed**3,y,lo,hi)/(12*edge[0]);TF=matrix_clean(TF)
        alpha=clean(m*edge[0]/V);pole=S.Matrix((-1,value*q,0))/m
        assert matrix_clean(TF*pole-cf)==S.zeros(3,1)
        heights=[ell.subs({t:v[0],y:v[1]}) for v in base];assert min(heights)>0
        raw=[S.Matrix((v[0],v[1],sg*h/2)) for sg in (-1,1) for v,h in zip(base,heights)]
        faces=[(0,1,2),(3,4,5),(0,1,4,3),(1,2,5,4),(2,0,3,5)]
        interior=sum(raw,S.zeros(3,1))/6;oriented=[]
        for face in faces:
            face=list(face);a,b,c=[raw[j] for j in face[:3]];nn=(b-a).cross(c-a)
            if nn.dot(a-interior)<0:face.reverse()
            a,b,c=[raw[j] for j in face[:3]];nn=(b-a).cross(c-a)
            assert nn.dot(a-interior)>0
            for j,w in enumerate(raw):
                h=clean(nn.dot(w-a));assert h==0 if j in face else h<0
            oriented.append(face)
        edges=sorted({tuple(sorted(e)) for f in oriented for e in zip(f,f[1:]+f[:1])})
        assert len(edges)==9
        assert all(sigma[:k,:k].det()>0 for k in (1,2,3))
        assert all((Q(3,2)*sigma-alpha*TF)[:k,:k].det()>0 for k in (1,2,3))
        records.append(dict(s=value,vertices=raw,maximal_faces=oriented,edges=edges,
                            volume=V,centroid=S.Matrix((gt,gm,0)),Sigma=sigma,
                            marked_alpha=alpha,marked_T=TF,marked_c=cf,marked_pole=pole,R=clean(J*edge[2]/(V*I))))
    return dict(original_mean_y=mu0,tilt=p+q*y,density=ell,actual_raw_first_jets=actual_raw,
                raw_edge_derivative=D2,actual_log_derivative=dlog,predicted_log_derivative=predicted,
                three_exact_polytope_controls=records,
                scope='Genuine whole marked-facet replacement, both signs; true6/9/5, no equilibrium assertion.')

def weighted_line_control(d,z,ru,rl):
    B=(d*d*z*z*rl-(d+2)**2*ru)/4;C=((d+2)**2*ru+d*d*z*z*rl)/2-1
    A=1/((1+d)**2+2*B*(1+d)+C);f=A*(y*y+2*B*y+C)
    u=1+d*z;b=1+d;L=clean(f.subs(y,u)/z)
    RU=(5*ru-2)/(3-5*ru);RL=(5*rl-2)/(3-5*rl)
    determinant=clean((u-RL)-L*z*(b+RU));assert determinant!=0
    k=clean(((RL-1)-L*z*(RU-1))/determinant);beta=clean(RU-1-(b+RU)*k)
    U=(y+1)/(d+2);stem=L*(y-1)/d;ell=1+k*y+beta*t
    assert d>0 and 0<z<1 and Q(2,5)<ru<Q(3,5) and Q(2,5)<rl<Q(3,5)
    assert A>0 and C-B*B>0 and L>0 and u>-1+ru*(d+2) and abs(k)<1
    assert beta<0
    zero(f.subs(y,b)-1);zero(f.subs(y,u)-L*z)
    assert S.diff(f,y).subs(y,u)>L/d>0
    # Along the curved boundary ell is concave, so endpoint positivity is exact and sufficient.
    H=[1-k,1+k,ell.subs({t:1,y:b}),ell.subs({t:L*z,y:u})]
    assert min(H)>0
    pieces=[(-1,1,S.S.Zero),(1,u,stem),(u,b,f)]
    def raw(expr):
        answer=0
        for lo,hi,lower in pieces:
            answer+=integrate(integrate(expr,t,lower,U),y,lo,hi)
        return clean(answer)
    V=raw(ell);J=raw(t*ell);M=raw(y*ell);m=clean(J/V);mu=clean(M/V)
    Y=y-mu;I=raw(ell*Y*Y)
    edge=[integrate((1+k*y)*Y**j,y,-1,1) for j in range(4)]
    R=clean(J*edge[2]/(V*I));assert 0<R<Q(3,2)
    eta=clean(edge[1]/edge[2]);actual_f=m+(J/I)*Y*Y+2*m*eta*Y
    residual=S.Poly(S.expand(f-actual_f),y);assert not residual.is_zero
    Phi=t/J-1/V-Y*Y/I-2*eta*Y/V
    line_reactions=[integrate((y+1)*ell.subs(t,U)*(U-f),y,-1,b),
                    integrate((y-1)*ell.subs(t,stem)*(stem-f),y,1,u)]
    assert line_reactions==[0,0]
    Ft=raw(t*(t-f));area=raw(S.S.One)
    sigma=S.Matrix([[raw(t*t*ell)/V-m*m,raw(t*y*ell)/V-m*mu,0],
                    [raw(t*y*ell)/V-m*mu,I/V,0],[0,0,raw(ell**3)/(12*V)]]).applyfunc(clean)
    TF=S.Matrix([[m*m,-m*edge[1]/edge[0],0],[-m*edge[1]/edge[0],edge[2]/edge[0],0],
                 [0,0,integrate((1+k*y)**3,y,-1,1)/(12*edge[0])]]).applyfunc(clean)
    alpha=clean(m*edge[0]/V)
    assert all(sigma[:i,:i].det()>0 for i in (1,2,3))
    assert all((Q(3,2)*sigma-alpha*TF)[:i,:i].det()>0 for i in (1,2,3))
    return dict(parameters=dict(d=d,z=z,rho_upper=ru,rho_stem=rl),
                actual_support=dict(upper=U,lower_pieces=pieces,affine_height=ell),
                trial_parabola=f,line_slope=L/d,positive_endpoint_heights=H,
                weighted_line_reactions=line_reactions,unweighted_trial_Ft=Ft,area=area,
                actual_volume=V,actual_centroid=S.Matrix((m,mu,0)),Sigma=sigma,
                marked_B=edge,marked_alpha=alpha,marked_T=TF,R=R,
                actual_parabola_residual=tuple(residual.all_coeffs()),actual_density_t_reaction=raw(t*Phi),
                scope='Actual curved homogeneous body, no finite polytope census; NOT self-consistent or supercritical.')

def encode(x):
    if isinstance(x,S.MatrixBase):return [[encode(v) for v in row] for row in x.tolist()]
    if isinstance(x,S.Basic):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x

def main():
    assert __debug__ and S.__version__=='1.14.0'
    controls=[weighted_line_control(Q(11,2),Q(49,50),Q(299,500),Q(51,100)),
              weighted_line_control(S.Integer(110),Q(19,20),Q(5,12),Q(5,11))]
    assert controls[0]['unweighted_trial_Ft']<0<controls[1]['unweighted_trial_Ft']
    report=dict(identity='TILTED_WHOLE_FACET_VARIATION_AND_WEIGHTED_LINE_REACTIONS_V1',
                identities=abstract_identities(),tilted_triangle=tilted_triangle_control(),
                exact_opposite_sign_line_controls=controls)
    data=(json.dumps(encode(report),sort_keys=True,indent=2)+'\n').encode()
    Path('marked_facet_variation_report.json').write_bytes(data)
    print('ACTUAL_TILTED_WHOLE_FACET_DERIVATIVE_AND_6_9_5_CONTROLS_PASS')
    print('EXACT_WEIGHTED_LINE_REACTIONS_AND_OPPOSITE_TRIAL_FT_SIGNS_PASS')
    print('REPORT',len(data),hashlib.sha256(data).hexdigest())
    print('MARKED_FACET_VARIATION_EXACT_PASS')
if __name__=='__main__':main()
```
