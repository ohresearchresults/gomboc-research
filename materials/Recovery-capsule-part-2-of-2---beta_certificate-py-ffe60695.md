# material-ffe60695e60c

AI research material

---

#!/usr/bin/env python3
"""Exact full-beta/full-projective-pencil cut-stack U2 certificate.

Dependency: the recovered pencil_certificate.py, SHA256
b1e887ff04f59652ee400a9988d813ea63a5cc71859755d38086c0f6ca74f7b1.
Its two-part immutable recovery capsule is identified in the companion proof.
No symbolic cache, external geometry or random seed is used here.  `build`
discovers coefficients numerically then checks them exactly; `verify` never
calls a numerical optimizer.  Assertions must be enabled.  Tested numerical
stack and exact output pins are in the companion proof.
"""
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
import argparse
import hashlib
import json
from fractions import Fraction as F
from math import lcm
from pathlib import Path
import numpy as np
import sympy as s
import pencil_certificate as pc

IDENTITY = 'FULL_CUT_STACK_FULL_BETA_FULL_PROJECTIVE_PENCIL_V1'
GAMMA = F(1,2**40)
ETA = F(1,2**68)
DELTA = F(1,2**83)
SCALE_EXPECTED = 537407782912


def geometry():
    """Differentiate the actual uniform-cell centroid, not assigned masses."""
    source = Path(pc.__file__).read_bytes()
    assert hashlib.sha256(source).hexdigest() == 'b1e887ff04f59652ee400a9988d813ea63a5cc71859755d38086c0f6ca74f7b1'
    a,Z,g,D,N,Q,R = pc.symbolic_geometry()
    r = s.Rational
    p = [r(1,5),r(2,5),r(3,5)]
    q = [r(1,4),r(1,3),r(1,2)]
    u = [r(1,5),r(2,5),r(2,5)]
    ps = r(4,5)
    d = [1+a*x for x in p]
    e = [1+(1-a)*x for x in q]
    ds = 1+a*ps
    w = [p[2]/d[2],p[1]/(d[1]*d[2]),p[0]/s.prod(d),
         (ps-sum(p[i]*u[i] for i in range(3)))/(ds*s.prod(d)),
         q[2]/e[2],q[1]/(e[1]*e[2]),q[0]/s.prod(e)]
    lam = [s.Integer(-1),s.Integer(-1),r(3,10)]
    for xs,den in [([-x for x in p],d),(q,e)]:
        for i in range(3):
            z = int(i == 2)
            A = q[2]*z-xs[i]
            lam.append(s.cancel((-(1-z)+(1-u[2])*A)/den[i]))
    lam += [s.Integer(0)]
    assert len(lam) == 10 and lam[8] == 0 and lam[9] == 0
    ell = s.cancel(sum(ww*sum(lam[i] for i in tet) for ww,tet in zip(w,pc.TETS))/(4*sum(w)))
    e3 = s.Matrix([0,0,1])
    R1,R2 = [],[]
    for i,j in pc.ARROWS:
        du,dv = lam[i]-ell,lam[j]-lam[i]
        zz,edge = Z[i]-g,Z[j]-Z[i]
        h1 = du*(e3*edge.T+edge*e3.T)/2+dv*(zz*e3.T+e3*zz.T)/2
        h2 = du*dv*e3*e3.T
        R1.append((Q*h1).applyfunc(s.cancel))
        R2.append((Q*h2).applyfunc(s.cancel))
    assert all(s.Poly(x,a,domain=s.QQ).degree() <= 17 for hh in R1+R2 for x in hh)
    # Bernstein coefficients in beta in[0,1], degree2, around beta0=2/5.
    BB = [[R[i]-r(2,5)*R1[i]+r(4,25)*R2[i] for i in range(34)],
          [R[i]+r(1,10)*R1[i]-r(6,25)*R2[i] for i in range(34)],
          [R[i]+r(3,5)*R1[i]+r(9,25)*R2[i] for i in range(34)]]
    B = np.empty((18,3,34,6),dtype=object)
    scale = 1
    for b,SS in enumerate(BB):
        for h,M in enumerate(SS):
            for k,(i,j) in enumerate(pc.PAIRS):
                for n,x in enumerate(pc.bernstein(s.expand(M[i,j]),a)):
                    B[n,b,h,k] = x
                    scale = lcm(scale,x.denominator)
    for index in np.ndindex(B.shape):
        B[index] = int(B[index]*scale)
    assert scale == SCALE_EXPECTED
    corner_norms = []
    for aa in [-r(5,4),s.Integer(3)]:
        for beta in [s.Integer(0),s.Integer(1)]:
            for z,l in zip(Z,lam):
                zz = (z+(beta-r(2,5))*l*e3).subs(a,aa)
                corner_norms.append(sum(x*x for x in zz))
    assert max(corner_norms) == r(16097,625) < 36
    return a,Z,lam,B,scale,N,Q


def split_axis(B,axis):
    left,right = pc.split(np.moveaxis(B,axis,0))
    return np.moveaxis(left,0,axis),np.moveaxis(right,0,axis)


def child_bounds(bounds,axis):
    lo,hi,bl,bh = bounds
    if axis == 0:
        mid = (lo+hi)/2
        return [lo,mid,bl,bh],[mid,hi,bl,bh]
    mid = (bl+bh)/2
    return [lo,hi,bl,mid],[lo,hi,mid,bh]


def build(B,a,Z,lam,trees,masks):
    """All returned coefficients are independently checked before output."""
    zfun = s.lambdify(a,[list(z) for z in Z],'numpy')
    lfun = s.lambdify(a,lam,'numpy')
    nodes = []
    calls = 0
    def visit(B,bounds,pending,depth):
        nonlocal calls
        lo,hi,bl,bh = bounds
        aa = -1.25+4.25*float((lo+hi)/2)
        beta = float((bl+bh)/2)
        zz = np.array(zfun(aa),dtype=float)
        zz[:,2] += (beta-.4)*np.array(lfun(aa),dtype=float)
        ev,v = np.linalg.eigh(np.cov(zz.T,bias=True))
        W = (v/np.sqrt(ev))@v.T
        bf = B.reshape(-1,34,6)
        val = np.array(bf,dtype=float)
        C = -np.einsum('ij,bnjk,kl->bnil',W,pc.mats(val/np.max(np.abs(val))),W)
        certs = []
        before = len(pending)
        while len(pending):
            first = int(pending[0])
            calls += 1
            result = pc.robust_stress(C,list(trees[first]))
            if result is None or not pc.exact_positive(bf,*result):
                break
            ids,w = result
            bits = np.uint64(sum(1<<i for i in ids))
            cover = (masks[pending]&bits) == bits
            assert cover[0]
            certs.append([ids,w])
            pending = pending[~cover]
        node = {'bounds':list(map(str,bounds)),'certificates':certs,
                'trees_in':before,'trees_left':len(pending)}
        nodes.append(node)
        print('BETA_NODE',len(nodes),node['bounds'],len(certs),len(pending),flush=True)
        if len(pending):
            if depth >= 7:
                raise RuntimeError('Uncovered leaf: no full rectangle theorem')
            axis = 1 if depth % 2 == 0 else 0
            node['axis'] = axis
            left,right = split_axis(B,axis)
            lb,rb = child_bounds(bounds,axis)
            visit(left,lb,pending,depth+1)
            visit(right,rb,pending,depth+1)
    visit(B,[F(0),F(1),F(0),F(1)],np.arange(len(trees)),0)
    return {'identity':IDENTITY,'nodes':nodes,'calls':calls}


def verify(record,B,scale,N,Q,a,trees,masks):
    """Exact matrix positivity plus complete recursive rectangular coverage."""
    assert record['identity'] == IDENTITY
    denmax = max(pc.bernstein(Q,a))
    assert denmax == pc.DENMAX_EXPECTED
    assert min(pc.bernstein(N,a)) == F(2008125,128)
    assert F(2008125,128)/202125 > F(1,16)
    pos = 0
    rows = 0
    leaves = 0
    def visit(B,bounds,pending,scale,depth):
        nonlocal pos,rows,leaves
        assert pos < len(record['nodes'])
        node = record['nodes'][pos]
        pos += 1
        assert node['bounds'] == list(map(str,bounds))
        assert node['trees_in'] == len(pending)
        bf = B.reshape(-1,34,6)
        for ids,w in node['certificates']:
            assert ids == sorted(set(ids)) and ids and len(ids) == len(w)
            assert all(type(i) is int and 0 <= i < 34 for i in ids)
            assert all(type(x) is int and x > 0 for x in w)
            P = -sum(ww*bf[:,i,:] for i,ww in zip(ids,w))
            threshold = GAMMA*sum(w)*scale*denmax
            P *= threshold.denominator
            for j in [0,3,5]:
                P[:,j] -= threshold.numerator
            assert pc.positive_rows(P)
            rows += len(P)
            bits = np.uint64(sum(1<<i for i in ids))
            cover = (masks[pending]&bits) == bits
            assert len(pending) and cover[0]
            pending = pending[~cover]
        assert node['trees_left'] == len(pending)
        if len(pending):
            axis = node['axis']
            assert axis == (1 if depth % 2 == 0 else 0)
            left,right = split_axis(B,axis)
            lb,rb = child_bounds(bounds,axis)
            factor = 2**(17 if axis == 0 else 2)
            visit(left,lb,pending,scale*factor,depth+1)
            visit(right,rb,pending,scale*factor,depth+1)
        else:
            assert 'axis' not in node
            leaves += 1
    visit(B,[F(0),F(1),F(0),F(1)],np.arange(len(trees)),scale,0)
    assert pos == len(record['nodes'])
    assert 7*(24*36+24*6+8) == 7112
    assert 7112*ETA < F(1,32)
    assert 1+12*7112*32 == 2731009 < 2**22
    assert 12*2**23+24+2**24*ETA < 2**27
    assert 2**27*ETA == GAMMA/2
    assert 60*8+16*20*64 == 20960 < 2**15
    assert 2**15*DELTA == ETA
    return {'identity':IDENTITY,'rooted_trees':len(trees),'nodes':pos,'leaves':leaves,
            'integer_stresses':sum(len(n['certificates']) for n in record['nodes']),
            'coefficient_matrix_checks':rows,'degrees':[17,2],'scale':scale,
            'gamma':str(GAMMA),'refill_vertex_radius':str(ETA),
            'nine_transverse_parameter_radius':str(DELTA),
            'scope':'Every beta in(0,1) and every a in(-5/4,3), with p,q,u,s fixed; plus the explicit nine-transverse-parameter tube. Not a whole E17 incidence.',
            'marker':'FULL_BETA_FULL_PROJECTIVE_PENCIL_GAMMA_TUBE_EXACT_PASS'}


def main():
    if not __debug__:
        raise RuntimeError('Assertions must remain enabled')
    parser = argparse.ArgumentParser()
    parser.add_argument('mode',choices=['build','verify'])
    parser.add_argument('--certificate',default='beta_stresses.json')
    parser.add_argument('--report',default='beta_verification.json')
    args = parser.parse_args()
    print('BETA_SYMBOLIC_BEGIN',flush=True)
    a,Z,lam,B,scale,N,Q = geometry()
    trees,masks = pc.all_trees()
    print('BETA_SYMBOLIC_READY',flush=True)
    path = Path(args.certificate)
    if args.mode == 'build':
        record = build(B,a,Z,lam,trees,masks)
        result = verify(record,B,scale,N,Q,a,trees,masks)
        certificate_sha = pc.write_json(path,record)
    else:
        record = json.loads(path.read_text(encoding='utf-8'))
        result = verify(record,B,scale,N,Q,a,trees,masks)
        certificate_sha = hashlib.sha256(path.read_bytes()).hexdigest()
    result['certificate_bytes'] = path.stat().st_size
    result['certificate_sha256'] = certificate_sha
    pc.write_json(Path(args.report),result)
    print(json.dumps(result,sort_keys=True,indent=2))
    print(result['marker'])

if __name__ == '__main__':
    main()
