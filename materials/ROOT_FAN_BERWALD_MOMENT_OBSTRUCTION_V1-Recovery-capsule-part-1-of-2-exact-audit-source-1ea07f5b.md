# material-1ea07f5b736d

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

#!/usr/bin/env python3
"""Exact formal controls for ROOT_FAN_BERWALD_MOMENT_OBSTRUCTION_V1.
Requires Python 3.13.5 and SymPy 1.14.0 (the tested versions).
These data are moments, NOT constructed polyhedra.
Run: python root_fan_berwald_audit.py --output root_fan_berwald_report.json
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sympy as S

R = S.Rational

def datum(a, b, c, d, t, T, u, v):
    a, b, c, d, t, T, u, v = map(R, (a, b, c, d, t, T, u, v))
    assert t > 1 and a > b > 0 and c > 0 and d > 0
    p = u + v
    r = (a+b+c)*u + (a+b+d)*v
    mu = r/(t*T)
    z = S.factor((mu-a-(d-a)*u-(c-a)*v)/(b-a))
    g = S.Matrix([u, v, z])
    g0 = S.ones(3, 1)/4
    alpha = S.Matrix([d-a, c-a, b-a])
    beta = S.Matrix([a+b+c, a+b+d, 0]) - t*T*alpha
    Q0 = (4*S.eye(3)-S.ones(3, 3))/(80*t)
    Q0 += (g-g0)*(g-g0).T/(t-1)
    h = S.Matrix([
        4*r*u-(a+b+2*d)*v,
        4*r*v-(a+b+2*c)*u,
        4*r*z-r-b*p,
    ])/5
    y = S.simplify(h-Q0*beta)
    delta = S.factor((beta.T*y)[0])
    assert delta > 0
    Q = S.simplify(Q0+y*y.T/delta)
    assert S.simplify(Q*beta-h) == S.zeros(3, 1)
    m = 3*p/t
    nw = ((a+b+c)*v+(a+b+d)*u)/(3*p)
    rho0 = S.factor((T-m)**2/(3*T*m*(1-nw/r)))
    Bp = S.factor((
        u*((mu+a+b+c)**2+mu**2+a*a+b*b+c*c)
        +v*((mu+a+b+d)**2+mu**2+a*a+b*b+d*d)
    )/(20*t*mu**2))
    w = S.Matrix([v/(3*p), u/(3*p), R(1, 3)])
    root_centroid = S.simplify((T*g-m*w)/(T-m))
    assert S.simplify(a+(alpha.T*root_centroid)[0]) == 0
    return dict(a=a,b=b,c=c,d=d,t=t,T=T,u=u,v=v,p=p,r=r,mu=mu,
                z=z,g=g,alpha=alpha,beta=beta,Q0=Q0,h=h,y=y,delta=delta,
                Q=Q,m=m,nw=nw,rho0=rho0,Bp=Bp,root_centroid=root_centroid)

def fan_budget(s, rho):
    rho = R(rho)
    return S.factor(s["Bp"]+rho/10+
        (1-(s["T"]+s["p"]/s["t"]+rho)/4)**2/
        (1-s["p"]/s["t"]-rho))

def patch_covariance_lower(s):
    g = s["g"]
    points = [S.zeros(3,1), S.Matrix([0,0,1]),
              S.Matrix([0,1,0]), S.Matrix([1,0,0])]
    first = S.zeros(3,1)
    second = S.zeros(3,3)
    for indices, weight in [([0,1,2],s["u"]/s["t"]),
                            ([0,1,3],s["v"]/s["t"])]:
        vectors = [points[i]-g for i in indices]
        total = sum(vectors,S.zeros(3,1))
        first += weight*total/4
        second += weight*(sum((v*v.T for v in vectors),S.zeros(3,3))
                          +total*total.T)/20
    return S.simplify(second+first*first.T/(1-s["p"]/s["t"]))

def margins(s, rho):
    a,b,c,d,t,T,u,v,p,r,mu,m,z = [
        s[k] for k in ("a","b","c","d","t","T","u","v","p","r","mu","m","z")
    ]
    values = {
        "u_ge_quarter":u-R(1,4), "v_ge_quarter":v-R(1,4),
        "u_le_t_quarter":t/4-u, "v_le_t_quarter":t/4-v,
        "joint_mass_gap":t+1-4*p, "joint_z_upper":t+2-4*p-4*z,
        "z_lower":z-(1-t), "m_ge_13_15":m-R(13,15),
        "t_le_45_7":R(45,7)-t, "mu_ge_quarter":mu-R(1,4),
        "centroid_cone_b":4*mu-b, "centroid_cone_c":4*mu-c,
        "centroid_cone_d":4*mu-d,
        "joint_fan_c":4*t*mu-c*t-a-b-d,
        "joint_fan_d":4*t*mu-d*t-a-b-c,
        "endpoint_corridor":b-4*mu*(T-2),
        "delta":s["delta"],
        "rho_lower":rho-s["rho0"],
        "rho_upper_berwald":R(3,2)*s["rho0"]-rho,
        "remainder_mass":1-p/t-rho,
        "fan_berwald":R(8,5)-fan_budget(s,rho),
    }
    for label,constant,vector in [
        ("x",0,S.Matrix([1,0,0])), ("y",0,S.Matrix([0,1,0])),
        ("ell",a,s["alpha"]),
        ("t_minus_x_y",t,S.Matrix([-1,-1,0])),
        ("z_minus_one_plus_t",t-1,S.Matrix([0,0,1])),
        ("t_minus_x_y_z",t,S.Matrix([-1,-1,-1])),
    ]:
        mean = constant+(vector.T*s["g"])[0]
        variance = (vector.T*s["Q"]*vector)[0]
        values["variance_"+label] = R(3,5)*mean**2-variance

    # A rational sufficient check for the root-band bound:
    # the band cutoff h=1 has mean G at most the prescribed H
    # and already has more G-mass than the formal root needs.
    n1, n2 = a+b+c, a+b+d
    H = m*(r-s["nw"])/(T-m)
    W = t*t*(a-b)*(T-m)/6
    band_W_at_1 = (r/2+R(1,3))/(n1*n2)
    band_Q_at_1 = (r/3+R(1,4))/(n1*n2)
    values["band_h1_mean"] = H*band_W_at_1-band_Q_at_1
    values["band_h1_mass"] = band_W_at_1-W

    Qpatch = patch_covariance_lower(s)
    for size in (1,2,3):
        values["patch_covariance_minor_"+str(size)] = (
            s["Q"]-Qpatch)[:size,:size].det()
    return {k:S.factor(v) for k,v in values.items()}

def serial(value):
    if isinstance(value,S.MatrixBase):
        return [[str(S.factor(value[i,j])) for j in range(value.cols)]
                for i in range(value.rows)]
    return str(S.factor(value))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,
                        default=Path("root_fan_berwald_report.json"))
    args = parser.parse_args()

    old = datum(1,R(1,2),R(2,5),R(2,5),5,R(11,5),R(3,4),R(3,4))
    old_variance = S.factor((old["alpha"].T*old["Q"]*old["alpha"])[0])
    old_variance_excess = S.factor(old_variance-R(3,5)*old["mu"]**2)
    old_fan_excess = S.factor(fan_budget(old,old["rho0"])-R(8,5))
    assert old_variance == R(3220124117,58470830000)
    assert old_variance_excess == R(108137839,7308853750) > 0
    assert old_fan_excess == R(157379933,3218892600) > 0
    assert old["rho0"] == R(169,462)
    assert old["Bp"] == R(148559,108300)

    new = datum(1,R(2,3),R(1,60),R(1,60),R(9,5),R(51,25),
                R(11,32),R(11,32))
    rho = R(1,4)
    new_margins = margins(new,rho)
    assert all(value > 0 for value in new_margins.values())
    assert new["z"] == R(1937,73440)
    assert new["rho0"] == R(1151329,5202000)
    assert fan_budget(new,rho) == R(99145502717513,71366196000000)
    assert S.factor((new["alpha"].T*new["Q"]*new["alpha"])[0]/new["mu"]**2
                    ) == R(140853006074403053,278811909948385000)

    report = {
        "identity":"ROOT_FAN_BERWALD_MOMENT_OBSTRUCTION_V1",
        "status":"Formal moment controls only; the new datum is not a polyhedron.",
        "old":{k:serial(v) for k,v in old.items()},
        "old_variance_excess":serial(old_variance_excess),
        "old_fan_excess":serial(old_fan_excess),
        "new":{k:serial(v) for k,v in new.items()},
        "new_rho":serial(rho),
        "new_fan_budget":serial(fan_budget(new,rho)),
        "new_positive_margins":{k:serial(v) for k,v in new_margins.items()},
    }
    args.output.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n",
                           encoding="utf-8")
    print("ROOT_FAN_BERWALD_EXACT_AUDIT_PASS")
    print("OLD_ENTIRE_COVARIANCE_FIBER_EXCLUDED")
    print("NEW_THRESHOLD_FORMAL_DATA_ONLY_NOT_A_BODY")

if __name__ == "__main__":
    main()
