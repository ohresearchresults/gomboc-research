import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

assert __debug__, 'Run without python -O'
sys.set_int_max_str_digits(0)

CHILD_SHA = 'd200af2491ba532cd9307caceb4d780e9a661a4c9094da10e4e0c3562875204d'
PARENT_SHA = '2426da394eda9520bd30b2b8b3e1f00d043697353bb6bc73658f5983653c11ec'
TRIAL = (Q(874577931702,10**12),
         Q(454209162144,10**12),
         Q(-558471315966,10**12))


def add(a,b):
    return tuple(x+y for x,y in zip(a,b))


def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))


def scale(t,a):
    return tuple(t*x for x in a)


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def determinant(a,b,c):
    return dot(a,cross(b,c))


def checked_json(path,expected):
    data=Path(path).read_bytes()
    assert hashlib.sha256(data).hexdigest()==expected
    return json.loads(data)


def encoded(x):
    if isinstance(x,Q):
        return str(x)
    if isinstance(x,dict):
        return {k:encoded(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):
        return [encoded(v) for v in x]
    return x


def run(child,parent):
    P=[tuple(map(Q,row)) for row in child['raw_vertices']]
    normals=[tuple(Q(v,h) for v in n)
             for n,h in zip(child['normals'],child['offsets'])]
    c0=tuple(map(Q,parent['raw_centroid']))
    r=(Q(0),Q(0),Q(1))
    assert r in P
    assert max(map(abs,c0))<=Q(1,50)
    assert (child['V'],child['E'],child['F'])==(163,296,135)
    assert child['counts']==[17,26,41] and child['weak']==[0,0,0]

    # Exact supporting-normal test at the old reference centre.
    radii=[]
    r2=dot(sub(r,c0),sub(r,c0))
    for x in P:
        if x==r:
            continue
        e=sub(x,r)
        delta=-dot(sub(r,c0),e)
        assert delta>0
        assert dot(sub(x,c0),sub(x,c0))<r2
        radii.append(delta/(2*sum(map(abs,e))))
    rho=min([Q(1,1000)]+radii)
    assert rho>0

    old_r2=Q(2603,2500)
    assert old_r2<Q(1021,1000)**2
    old_shifted_r2=Q(1023,1000)**2
    new_r2=Q(829**2+409**2+519**2,10**6)
    assert new_r2-old_shifted_r2==Q(38677,500000)>0
    apex_dot_bound=Q(21,1000)*(Q(9,10)+Q(47,100))
    apex_dot_bound-=Q(979,1000)*Q(154,100)
    assert apex_dot_bound==Q(-147889,100000)<0
    assert Q(17,20)<=TRIAL[0]<=Q(9,10)
    assert Q(43,100)<=TRIAL[1]<=Q(47,100)
    assert Q(-57,100)<=TRIAL[2]<=Q(-27,50)

    V0=Q(0)
    M0=(Q(0),)*3
    face_data=[]
    for cy in child['faces']:
        W=Q(0)
        S=(Q(0),)*3
        for j in range(1,len(cy)-1):
            a,b,c=P[cy[0]],P[cy[j]],P[cy[j+1]]
            w=determinant(a,b,c)
            assert w>0
            W+=w
            S=add(S,scale(w,add(add(a,b),c)))
        f=W/6
        bf=scale(Q(1,6),S)
        face_data.append((f,bf))
        V0+=f
        M0=add(M0,scale(Q(1,24),S))
    assert V0==Q(child['ordinary_volume'])
    assert M0==tuple(map(Q,child['raw_first_moments']))

    visible=[]
    k=(Q(0),)*3
    k0=Q(0)
    B=[[Q(0) for j in range(3)] for i in range(3)]
    b0=(Q(0),)*3
    V=V0
    M=M0
    for f,(q,(vf,bf)) in enumerate(zip(normals,face_data)):
        gap=dot(q,TRIAL)-1
        assert gap!=0, 'Trial lies on a visibility boundary'
        if gap<0:
            continue
        visible.append(f)
        k=add(k,scale(vf,q))
        k0-=vf
        b0=sub(b0,scale(Q(1,4),bf))
        for i in range(3):
            for j in range(3):
                B[i][j]+=bf[i]*q[j]/4
        V+=vf*gap
        M=add(M,scale(gap/4,add(scale(vf,TRIAL),bf)))
    d=sub(add(M0,b0),scale(V0+k0,c0))
    L=[[B[i][j]+(k0/4 if i==j else 0)-c0[i]*k[j]
        for j in range(3)] for i in range(3)]
    value=add(add(d,tuple(dot(row,TRIAL) for row in L)),
              scale(dot(k,TRIAL)/4,TRIAL))
    assert value==sub(M,scale(V,c0))
    J=[[L[i][j]+TRIAL[i]*k[j]/4
        +(dot(k,TRIAL)/4 if i==j else 0)
        for j in range(3)] for i in range(3)]
    return encoded(dict(
        status='EXACT_OPPOSITE_BOX_GATE_AND_CHAMBER_MASS_FORMULAS_PASS',
        reference_centroid=c0,reference_root=list(r),
        actual_centroid_cube_radius=rho,
        squared_radius_separation=Q(38677,500000),
        apex_against_new_point_upper=apex_dot_bound,
        proposal_only_point=TRIAL,visible_supports=visible,
        chamber_k=k,chamber_k0=k0,chamber_B=B,chamber_b0=b0,
        closure_d=d,closure_L=L,closure_value_at_trial=value,
        closure_J_at_trial=J,
        trial_ordinary_volume=V,trial_raw_first_moments=M,
        trial_own_centroid=scale(1/V,M),
        trial_mass_is_exactly_closed=(value==(0,0,0)),
        new_endpoint_promoted=False))


if __name__=='__main__':
    if len(sys.argv)!=4:
        raise SystemExit('Usage: python -S opposite_mass_gate.py C592_A.json C602_A.json output.json')
    child=checked_json(sys.argv[1],CHILD_SHA)
    parent=checked_json(sys.argv[2],PARENT_SHA)
    result=run(child,parent)
    Path(sys.argv[3]).write_text(
        json.dumps(result,sort_keys=True,separators=(',',':')),
        encoding='utf-8')
    print(result['status'])
