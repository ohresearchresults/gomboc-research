# material-b5ce93ff47f3

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Exact audit for ACTUAL_PROJECTION_MOMENT_CAPACITY_V1.
Python 3.13.5 standard library only. No polyhedron is constructed.
The two controls are formal moment data, not bodies or equilibrium examples.
Run: python exact_capacity_audit.py --out projection_capacity_audit.json
"""
from __future__ import annotations
import argparse
import json
from fractions import Fraction as F
from pathlib import Path


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), F(0))


def mv(a, x):
    return [dot(row, x) for row in a]


def outer(x, y):
    return [[a*b for b in y] for a in x]


def quad(a, x):
    return dot(x, mv(a, x))


def det3(a):
    return sum(((-1)**j*a[0][j]*(a[1][(j+1)%3]*a[2][(j+2)%3]
             -a[1][(j+2)%3]*a[2][(j+1)%3])*(-1)**j for j in range(3)), F(0))


def check_control(name: str, integers: tuple[int, ...], cut: F):
    b, k, t, p, rho, added = [F(i, 10**6) for i in integers]
    T=F(51,25); h=1+b+k; q=t*T; r=h*p; mu=r/q; al=1-b
    z=(1+(k-1)*p-mu)/al; m=3*p/t
    g=[p/2,p/2,z]; lv=[k-1,k-1,b-1]; nv=[h,h,F(0)]
    beta=[nv[i]-q*lv[i] for i in range(3)]
    dg=[v-F(1,4) for v in g]
    Q0=[[(F(4 if i==j else 0)-1)/(80*t)+dg[i]*dg[j]/(t-1)
         for j in range(3)] for i in range(3)]
    rhs=[(2*r*p-(1+b+2*k)*p/2)/5]*2+[(4*r*z-r-b*p)/5]
    y=[rhs[i]-mv(Q0,beta)[i] for i in range(3)]; delta=dot(beta,y)
    assert delta>0
    Qstar=[[Q0[i][j]+y[i]*y[j]/delta for j in range(3)] for i in range(3)]
    v=[beta[2],beta[2],-2*beta[0]]; vv=dot(v,v)
    assert dot(v,beta)==0 and vv>0 and added>0
    Q=[[Qstar[i][j]+added*v[i]*v[j]/vv for j in range(3)] for i in range(3)]
    assert mv(Q,beta)==rhs
    assert Q[0][0]>0 and Q[0][0]*Q[1][1]-Q[0][1]**2>0 and det3(Q)>0
    rho0=(q-3*p)**2/(3*q*(3*p-1))
    rest=1-p/t-rho
    Bp=p/t*((mu+1+b+k)**2+mu**2+1+b*b+k*k)/(20*mu*mu)
    fan=Bp+rho/10+(1-(T+p/t+rho)/4)**2/rest
    AR=t*al*rho/(2*mu); A=t/2-b/al*AR
    W1=al*t*(q-3*p)/6; W2=al*t*p*(r-h/3)/2
    NR=r*AR+W1; NR2=r*r*AR+2*r*W1+W2
    NK=4*t*r/6-b/al*NR; varn=quad(Q,nv)
    NK2=5*t*(r*r+varn)/6-b/al*NR2
    B0=A-F(1,2); B1=NK-h/3; B2=NK2-h*h/4
    M0=A-AR-r*r/(2*h*h)
    M1=t*r/6-W1/al+r**3/(6*h*h)
    M2=5*t*varn/6-W2/al-r**4/(12*h*h)
    RT=p*(q-1)/(q-3*p)
    H=W2/W1
    # The positive root of 3x^2+4(r-H)x-6rH is the old root-band cutoff.
    assert cut>0 and 3*cut*cut+4*(r-H)*cut-6*r*H<0
    oldband=(r*cut*cut/2+cut**3/3)/(h*h)-W1
    tests={
      'p_low':p-F(1,2), 'joint_p':(t+1)/4-p, 'p_upper':t/2-p,
      'mu_low':mu-F(1,4), 'b_support':4*mu-b, 'k_support':4*mu-k,
      'mass_face':4*t*mu-k*t-1-b-k, 'endpoint':b-4*mu*(T-2),
      'centroid_z_upper':t+2-4*p-4*z, 'centroid_z_lower':z-1+t,
      'm_lower':m-F(13,15), 't_upper':F(45,7)-t, 'cov_delta':delta,
      'ell_berwald':F(3,5)*mu*mu-quad(Q,lv), 'Gc_Gd':h-r-q*k,
      'rho_lower':rho-rho0, 'rho_upper':F(3,2)*rho0-rho,
      'fan_rest':rest, 'fan_berwald':F(8,5)-fan, 'K_area':A-F(1,2),
      'Omega_area':M0, 'Omega_first':M1, 'Omega_second':M2,
      'Omega_hankel':M0*M2-M1*M1,
      'outside_first_low':B1-h*B0, 'outside_first_high':t*h*B0-B1,
      'outside_hankel':B0*B2-B1*B1, 'root_band_with_rational_cut':oldband,
      'root_centroid_container':2*A-RT, 'K_berwald':F(3,2)*NK*NK-A*NK2,
    }
    assert len(tests)==30 and all(v>0 for v in tests.values())
    s0=W1*W1/W2; gamma=W2/W1
    kap=4*(r+gamma)*gamma/(3*h*h*s0)
    eps=min(F(1,2),1/(2*kap))
    S=(s0-4*(r+gamma)*gamma*eps**3/(3*h*h))/(1-eps*eps)
    assert S>s0 and 0<eps<1 and kap*eps<=F(1,2)
    Ac=t/2-b/al*s0; Aq=t/2-b/al*S
    def phi(area):
        return 2*h*area*area+(h-3*r)*area-r*t/2+b*t*(q-3*p)/2
    def psi(area):
        return area*h*h*(1+2*area+4*area*area)/6-r*r*(area+t/3) \
               +b/al*(2*r*W1+W2)-5*t*quad(Qstar,nv)/6
    assert Aq<Ac and phi(Aq)<0
    if name=='P1':
        assert phi(A)<0 and phi(Ac)<0
    elif name=='P2':
        assert phi(A)>0 and phi(Ac)>0 and psi(Ac)>0
    else:
        raise ValueError('Unknown control')
    report={
       'kind':'formal moment control, NOT a body',
       'inputs':dict(zip(['b','c_equals_d','t','p','rho','added_covariance'],
                        [b,k,t,p,rho,added])),
       'T':T,'z':z,'root_band_test_cut':cut,
       'positive_selected_tests':tests,
       'A':A,'AR':AR,'W1':W1,'W2':W2,'s0':s0,
       'gamma':gamma,'kappa':kap,'epsilon':eps,'strict_area_lower_bound':S,
       'A_Cauchy':Ac,'A_quantitative':Aq,
       'Phi_A':phi(A),'Phi_Cauchy':phi(Ac),'Phi_quantitative':phi(Aq),
       'Psi_Cauchy':psi(Ac), 'Qstar':Qstar,'Q':Q,
    }
    return report


def stringify(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:stringify(v) for k,v in x.items()}
    if isinstance(x,list):return [stringify(v) for v in x]
    return x


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',default='projection_capacity_audit.json')
    args=ap.parse_args()
    # Exact algebraic audit of the sharp polygon profile moments, degrees 0..8.
    for area in [F(1,2),F(3,4),F(2),F(17,6)]:
        for j in range(9):
            R=2*area
            predicted=2*area*sum((R**i for i in range(j+1)),F(0))/((j+1)*(j+2))
            actual=F(1,j+2) if R==1 else F(1,j+2)+(R*(R**(j+1)-1)/(j+1)-(R**(j+2)-1)/(j+2))/(R-1)
            assert predicted==actual
    reports={
       'identity':'ACTUAL_PROJECTION_MOMENT_CAPACITY_V1',
       'P1':check_control('P1',(269757,48915,1243298,554790,151063,27397),F(79,100)),
       'P2':check_control('P2',(148111,4990,1138318,526978,136441,29360),F(67,100)),
    }
    raw=(json.dumps(stringify(reports),ensure_ascii=True,sort_keys=True,indent=2)+'\n').encode('ascii')
    Path(args.out).write_bytes(raw)
    print('EXACT_PLANAR_PROFILE_MOMENTS_OK')
    print('P1_SELECTED_30_TESTS_PASS_PHI_CAUCHY_FAILS')
    print('P2_SELECTED_30_TESTS_AND_PLANAR_FIRST_PASS_CAPACITY_FAILS')
    print('EXACT_CAPACITY_CONTROLS_OK')


if __name__=='__main__':main()
