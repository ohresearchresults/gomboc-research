# material-5d6c204d5c80

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

"""Exact one-unused-triangle actuator minor on the author's algebraic control.
The exact body's existence/unique root box is the premise in immutable result
minimum-0241, SHA256
08bb47a0c75336c8605fdad5d2cf800e1e0059f4667088a638a8009efa3d968d.
This script proves a NEW nonzero actuator minor over that entire rational box;
it does not independently re-prove existence or the original census.
CPython >=3.10, standard library, assertions enabled. No external inputs.
Usage: python -B -S contact_neutral_actuator.py build|check
"""
from fractions import Fraction as F
from pathlib import Path
import json, sys, hashlib
R=F(21,20)
PARAMS=tuple(F(x,10**8) for x in (225082171,-82658883,-186396676,144995592,245518313,21525122,27871567,70099732,28332266))
FACES=((0,1,2,3,4,5,6),(9,8,7),(7,1,0),(7,2,1),(7,8,3,2),(8,4,3),(8,9,5,4),(9,6,5),(9,7,0,6))
C=tuple(F(n,10**30) for n in (-417819504419730630621198890185,406482606157541070247829267790,-1253550426273930071347650412813))
RAD=F(1,10**24)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(c,a): return tuple(c*x for x in a)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a): return dot(a[0],cross(a[1],a[2]))
def solve(a,b=(1,1,1)):
 d=det(a)
 assert d
 return tuple(det(tuple(tuple(b[i] if j==k else a[i][j] for j in range(3)) for i in range(3)))/d for k in range(3))
def initial():
 m,cx,cy,d,ax,u,v,w,t=PARAMS
 a=(R,-F(1)); b=add(a,mul(m,(-F(1),R))); c=(cx,cy)
 aa=(ax,R*R+1-R*ax); bb=add(aa,mul(d,sub(b,a))); cc=add(aa,mul(d,sub(c,a)))
 delta=sub(aa,cc); lam=(5*R*R-5*R*cc[0]+2*cc[1])/(5*R*delta[0]-2*delta[1])
 p0=add(cc,mul(lam,delta))
 bot=(p0,(R,F(0)),(R,F(1)),add(bb,mul(u,sub(aa,bb))),add(bb,mul(v,sub(cc,bb))),add(cc,mul(w,sub(bb,cc))),add(cc,mul(t,sub(aa,cc))))
 x=[z+(F(1),) for z in bot]+[z+(-F(1),) for z in (a,b,c)]
 return x,[solve([x[i] for i in f[:3]]) for f in FACES]
def outer(a,b): return tuple(tuple(x*y for y in b) for x in a)
def moment_triangle(vertices):
 s=tuple(sum(x[i] for x in vertices) for i in range(3))
 return tuple(tuple((s[i]*s[j]+sum(x[i]*x[j] for x in vertices))/12 for j in range(3)) for i in range(3))
def matvec(A,v): return tuple(dot(row,v) for row in A)
def affine_range(f):
 value=f(C)
 coefficients=[]
 for j in range(3):
  point=list(C); point[j]+=1
  coefficients.append(f(point)-value)
 error=RAD*sum(abs(x) for x in coefficients)
 return value-error,value+error,tuple(coefficients)
def paired_leaf(x,p):
 # r3 is prescribed, r2 and r5 solve the true COM and Q23=t.
 # In particular r7 stays exactly fixed, unlike the parent's two-corrector arc.
 a=x[7]; r=p[2]; s=p[3]; qf=(F(0),F(0),F(1))
 ell=sub(s,mul(2,r)); z=cross(a,ell)
 TG=moment_triangle([x[i] for i in FACES[2]])
 TR=moment_triangle([x[i] for i in FACES[3]])
 DG=det([x[i] for i in FACES[2]]); DR=det([x[i] for i in FACES[3]])
 assert DG>0 and DR>0
 w3=(F(80000,370881),F(10988501,14128800),-F(441,800))
 ep=sub(ell,mul(dot(a,ell)/dot(a,a),a))
 base=mul((1-dot(r,w3))/dot(ep,ep),ep)
 assert dot(a,base)==0 and dot(ell,base)+dot(r,w3)==1
 assert dot(a,w3)==0 and dot(sub(p[4],mul(2,p[3])),w3)==1
 b1prime=solve((qf,p[3],p[4]),(F(0),-dot(x[2],w3),F(0)))
 assert dot(b1prime,(-F(1),R,F(0)))==1
 def response(w,v):
  bp=solve((qf,r,s),(F(0),-dot(x[1],w),-dot(x[1],v)))
  e=(F(0),F(1),F(0))
  return dot(bp,e)-R*R*dot(v,e)
 Pbase=response(base,w3); Pz=response(z,(F(0),)*3)
 load=add(mul(DG,matvec(TG,base)),mul(DR,matvec(TR,w3)))
 def nJ(U):
  rJ=(U[0],U[1],x[8][0]*U[0]+x[8][1]*U[1]-1)
  return sub(qf,mul(F(1,2),rJ))
 def denominator(U): return DG*dot(nJ(U),matvec(TG,z))
 def correction_numerator(U): return -dot(nJ(U),load)
 def primal_numerator(U): return Pbase*denominator(U)+Pz*correction_numerator(U)
 dlo,dhi,dc=affine_range(denominator)
 nlo,nhi,nc=affine_range(primal_numerator)
 assert dlo>0 and nlo>0
 lower,upper=nlo/dhi,nhi/dlo
 assert F(29536,100)<lower<=upper<F(29537,100)
 return {'prescribed_r3_velocity':w3,'G_velocity_base':base,
         'G_velocity_neutral':z,'G_velocity_formula':'base + correction_numerator(U)/denominator(U) * neutral',
         'centroid_weight_DG':DG,'centroid_weight_DR':DR,
         'denominator_at_C':denominator(C),'denominator_coefficients':dc,
         'denominator_interval':[dlo,dhi],
         'correction_numerator_at_C':correction_numerator(C),
         'correction_numerator_coefficients':affine_range(correction_numerator)[2],
         'P12_numerator_at_C':primal_numerator(C),'P12_numerator_coefficients':nc,
         'P12_derivative_exact_interval':[lower,upper],
         'P12_derivative_simple_interval':[F(29536,100),F(29537,100)],
         'other_three_first_derivatives':[F(1),F(1),F(1)],
         'fixed_poles':[0,1,4,6,7,8],
         'implicit_poles':[2,5],
         'radius_note':'Analytic local interval by the invertible true COM/contact IFT; no numerical radius asserted.'}
def build():
 x,p=initial(); qf=(F(0),F(0),F(1)); a=x[7]; r=p[2]; s=p[3]
 ell=sub(s,mul(2,r)); z=cross(a,ell)
 assert dot(a,z)==dot(ell,z)==0 and dot(z,z)>0
 TG=moment_triangle([x[7],x[1],x[0]])
 assert all(dot(r,v)==1 for v in (x[7],x[1],x[0]))
 image=matvec(TG,z)
 # J=F5, apex x8; all end apex heights are -1, hence c_J=1/2.
 cj=(dot(qf,x[8])+3)/4
 assert cj==F(1,2)
 def rj(U): return (U[0],U[1],x[8][0]*U[0]+x[8][1]*U[1]-1)
 def chi(U): return dot(sub(qf,mul(cj,rj(U))),image)
 cchi=chi(C)
 grad=(-cj*(image[0]+x[8][0]*image[2]),-cj*(image[1]+x[8][1]*image[2]),F(0))
 error=RAD*sum(abs(t) for t in grad)
 lo,hi=cchi-error,cchi+error
 assert lo>0 or hi<0
 # Simpler rational public certificate, strict and independently checked.
 denominator=10**6
 lower=F((lo.numerator*denominator)//lo.denominator,denominator)
 upper=F(-((-hi.numerator*denominator)//hi.denominator),denominator)
 assert lower<lo<=hi<upper and lower*upper>0
 # Source-side compatibility identity for the raw two-coordinate EF response.
 b=x[1]; rho=dot(r,r); foot=mul(1/rho,r)
 theta=(foot[2]-b[2])/(a[2]-b[2]); lam=rho*(1-theta)
 d=sub(s,r)
 assert sub(ell,sub(d,mul(lam,b)))==mul(-rho*theta,a)
 return {'paired_leaf':paired_leaf(x,p),'source_result':'minimum-0241','source_sha256':'08bb47a0c75336c8605fdad5d2cf800e1e0059f4667088a638a8009efa3d968d','premise':'The true uniform-COM body is the unique root in the parent isolating cube; not the rational center C.','G':2,'J':5,'target':3,'root_center':C,'root_radius':RAD,'neutral_vector':z,'triangle_second_moment':TG,'centroid_direction_without_nonzero_surface_factor':image,'chi_center':cchi,'chi_linear_coefficients':grad,'chi_exact_interval':[lo,hi],'chi_simple_interval':[lower,upper],'terminal_marker':'ONE_UNUSED_TRIANGLE_CONTACT_NEUTRAL_MINOR_PASS'}
def clean(v):
 if isinstance(v,F): return str(v)
 if isinstance(v,dict): return {k:clean(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)): return [clean(x) for x in v]
 return v
def main():
 assert __debug__ and sys.version_info >= (3,10)
 assert len(sys.argv)==2 and sys.argv[1] in ('build','check')
 data=(json.dumps(clean(build()),indent=2,sort_keys=True)+'\n').encode()
 out=Path('contact_neutral_actuator_report.json')
 if sys.argv[1]=='build': out.write_bytes(data)
 else: assert out.read_bytes()==data
 print('ONE_UNUSED_TRIANGLE_CONTACT_NEUTRAL_MINOR_PASS')
 print('CHI_INTERVAL',*build()['chi_simple_interval'])
 print('PAIRED_P12_DERIVATIVE',*build()['paired_leaf']['P12_derivative_simple_interval'])
 for f in (Path(__file__),out):
  raw=f.read_bytes(); print(f.name,len(raw),hashlib.sha256(raw).hexdigest())
if __name__=='__main__': main()
