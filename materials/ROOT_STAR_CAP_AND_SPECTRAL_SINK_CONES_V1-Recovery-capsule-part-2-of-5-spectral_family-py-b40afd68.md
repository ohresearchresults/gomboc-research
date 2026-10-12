# material-b40afd68d9d1

AI research material

---

"""Exact continuously certified TWO_SINK_PRISMATOID_V1; no floating arithmetic."""
from cap_geometry import *
from math import comb
from pathlib import Path
import argparse, hashlib, platform
import sympy as sp

T=sp.symbols('t'); HALF=sp.Rational(1,2); H=sp.Rational(5,2)
FACETS=((0,3,2,1),(0,1,9,8),(0,6,3),(0,7,6),(0,8,7),(1,2,4,9),(2,3,5,4),(3,6,5),(4,5,6,7,8,9))
B=tuple(map(vec,((23,-13,-10),(-13,22,9),(-10,9,12))))
CUTS=((0,5),(6,7,8))

def vertices(t):
    return [(-2,-2,0),(2,-2,0),(2,2,0),(-2,2,0),(3,3,H),(-1,3,H),(-2,1,H),(-2+t,0,H),(-1,-1,H),(3,-1,H)]

def edges():
    ans={}
    for f,cyc in enumerate(FACETS):
        for a,b in zip(cyc,cyc[1:]+cyc[:1]):ans.setdefault(tuple(sorted((a,b))),[]).append(f)
    assert len(ans)==17 and all(len(v)==2 for v in ans.values())
    return ans
EDGES=edges(); ARCS=sorted(tuple(a) for fs in EDGES.values() for a in (fs,fs[::-1]))

def bernstein(poly):
    poly=sp.Poly(poly,T); n=poly.degree(); aa=[poly.nth(i)*HALF**i for i in range(n+1)]
    return [sp.factor(sum(aa[i]*sp.Rational(comb(k,i),comb(n,i)) for i in range(k+1))) for k in range(n+1)]

def certify(expr, records, label, interior=False):
    expr=sp.cancel(expr); num,den=sp.fraction(expr)
    if den.subs(T,sp.Rational(1,4))<0:num=-num;den=-den
    powers=[0,0];assert num!=0
    if interior:
        # At the two f-vector transition endpoints only, zeros are harmless.
        for i,factor in enumerate((T,HALF-T)):
            while sp.Poly(num,T).rem(sp.Poly(factor,T)).is_zero:
                num=sp.cancel(num/factor);powers[i]+=1
    bn,bd=bernstein(num),bernstein(den)
    assert all(b>0 for b in bn+bd),(label,bn,bd)
    records.append(dict(label=label,interior=interior,endpoint_factor_powers=powers,expression=str(expr),numerator=[str(x) for x in sp.Poly(num,T).all_coeffs()],denominator=[str(x) for x in sp.Poly(den,T).all_coeffs()],bernstein_numerator=list(map(str,bn)),bernstein_denominator=list(map(str,bd))))


def symbolic(records):
    vv=[sp.Matrix(v) for v in vertices(T)]; c=sum(vv,sp.zeros(3,1))/10
    normals=[];heights=[]
    for i,cyc in enumerate(FACETS):
        a,b,d=[vv[k] for k in cyc[:3]];n=(b-a).cross(d-a);h=n.dot(a)
        # Normalize all plane vectors by their fixed positive scale at t=1/4.
        if (h-n.dot(c)).subs(T,sp.Rational(1,4))<0:n=-n;h=-h
        normals.append(n);heights.append(h)
        for j,v in enumerate(vv):
            slack=sp.factor(h-n.dot(v))
            if j in cyc:assert slack==0
            else:certify(slack,records,f'incidence_{i}_{j}',True)
        for a,b,d in zip(cyc,cyc[1:]+cyc[:1],cyc[2:]+cyc[:2]):
            certify(n.dot((vv[b]-vv[a]).cross(vv[d]-vv[b])),records,f'facet_turn_{i}_{a}',True)
    V=0;J=sp.zeros(3,1)
    for cyc in FACETS:
        for j in range(1,len(cyc)-1):
            vs=[c,vv[cyc[0]],vv[cyc[j]],vv[cyc[j+1]]]
            w=sp.det(sp.Matrix.hstack(vs[1]-c,vs[2]-c,vs[3]-c))/6
            certify(w,records,f'volume_tetra_{cyc[0]}_{cyc[j]}_{cyc[j+1]}',True)
            V+=w;J+=w*sum(vs,sp.zeros(3,1))/4
    V=sp.factor(V);g=J.applyfunc(sp.factor)/V;g=g.applyfunc(sp.factor)
    certify(V,records,'true_volume');q=[]
    for i,(n,h) in enumerate(zip(normals,heights)):
        hh=sp.factor(h-n.dot(g));certify(hh,records,f'own_COM_pole_denominator_{i}')
        q.append((n/hh).applyfunc(sp.factor))
    assert sp.expand(V-sp.Rational(5,12)*(105-2*T))==0
    expected_g=sp.Matrix([(-2*T*T+15*T+133)/(4*(105-2*T)),(2*T+105)/(2*(105-2*T)),5*(215-6*T)/(8*(105-2*T))])
    assert all(sp.cancel(a-b)==0 for a,b in zip(g,expected_g))
    return vv,V,g,q


def possible(u,v,C,k):
    D=dot(u,mv(C,v));R2=dot(u,mv(C,u))*dot(v,mv(C,v))
    return D>=0 or (k+1)**2*D**2<=(k-1)**2*R2

def sinks(n,arcs):
    reach=[{i} for i in range(n)]
    for a,b in arcs:reach[a].add(b)
    for k in range(n):
        for i in range(n):
            if k in reach[i]:reach[i]|=reach[k]
    used=set();cc=[]
    for i in range(n):
        if i in used:continue
        c={j for j in range(n) if j in reach[i] and i in reach[j]};used|=c;cc.append(c)
    return [sorted(c) for c in cc if not any(a in c and b not in c for a,b in arcs)]

def encode(x):
    if isinstance(x,Q):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [encode(v) for v in x]
    return x

def build():
    records=[];vv,V,g,q=symbolic(records)
    assert B[0][0]>0 and B[0][0]*B[1][1]-B[0][1]**2>0 and det(*B)>0
    # Entire non-affine t-family, all metric eigenframes, including closed cones.
    cones=[('two_fixed_facets',sp.eye(3),7,((0,),(8,))),('two_moving_sinks',sp.Matrix(B),4,CUTS)]
    cuts_record=[]
    for label,C,k,sets in cones:
        for ss in sets:
            for i,j in ARCS:
                if i in ss and j not in ss:
                    u=q[i];v=q[j]-u;d=(u.T*C*v)[0];R2=(u.T*C*u)[0]*(v.T*C*v)[0]
                    certify(-d,records,f'{label}_{i}_to_{j}_negative')
                    certify((k+1)**2*d*d-(k-1)**2*R2,records,f'{label}_{i}_to_{j}_strict_cone')
                    cuts_record.append((label,i,j))
    P=hull(vertices(Q(1,4)));assert tuple(P['facets'])==FACETS
    assert P['volume']==Q(1045,24)
    assert P['g']==vec((Q(1093,3344),Q(211,418),Q(2135,1672)))
    controls={}
    for label,C in [('identity',ID),('moving_sink_center',B)]:
        R=mechanics(P,C);assert not R['zeros'];controls[label]=encode(R)
    assert [len(controls['identity'][x]) for x in ('S','U','H')]==[9,9,16]
    assert [len(controls['moving_sink_center'][x]) for x in ('S','U','H')]==[6,7,11]
    qq=P['poles'];arcs=[(i,j) for i,j in ARCS if possible(qq[i],sub(qq[j],qq[i]),B,4)]
    assert sinks(9,arcs)==[[0,5],[6,7,8]]
    assert all(any(i==j for j,k in arcs) for i in range(9))
    for i,j in arcs:
        u=qq[i];v=sub(qq[j],u);d=dot(u,mv(B,v));r2=dot(u,mv(B,u))*dot(v,mv(B,v))
        assert d>0 or (d<=0 and 25*d*d<9*r2), (i,j)
    good=[];deltas=[];qb=qq[0]
    for i in range(4,10):
        a=P['X'][i];D=(2-dot(qb,a))**2-dot(qb,qb)*dot(a,a);deltas.append((i,str(D)))
        if D>0:good.append(i)
    assert good==[5,6,7,8,9]
    assert all(any(a in good for a in FACETS[j])for i,j in ARCS if i==0)
    return dict(identity='TWO_SINK_PRISMATOID_V1',parameter='0<t<1/2',height='5/2',volume=str(V),centroid=list(map(str,g)),poles=[list(map(str,x))for x in q],facets=FACETS,edges=encode(EDGES),cuts=cuts_record,certificates=records,controls=controls,vertices_at_quarter=encode(P['vertices']),centered_vertices_at_quarter=encode(P['X']),poles_at_quarter=encode(qq),B=encode(B),possible_arcs_at_quarter=arcs,sink_components_at_quarter=sinks(9,arcs),cap_deltas_at_quarter=deltas)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=('build','check'));ap.add_argument('path',nargs='?',default='two_sink_report.json');args=ap.parse_args()
    obj=build();data=(json.dumps(obj,sort_keys=True,indent=2)+'\n').encode()
    if args.mode=='build':Path(args.path).write_bytes(data)
    else:assert Path(args.path).read_bytes()==data
    total=sum(len(r['bernstein_numerator'])+len(r['bernstein_denominator'])for r in obj['certificates'])
    print('TWO_SINK_PRISMATOID_V1_OK');print('certificates',len(obj['certificates']),'positive_coefficients',total,'outgoing_cut_arcs',len(obj['cuts']))
    print('f_vector 10 17 9; own_COM exact; identity_S_U_H 9 9 16; no_zero_primitives')
    print('all_t_open_0_half: cone_I_7_two_fixed_S; cone_B_4_two_disjoint_moving_S')
    print('quarter_sinks',obj['sink_components_at_quarter'],'every_facet_has_possible_exit')
    print('report_bytes',len(data),'sha256',hashlib.sha256(data).hexdigest())
if __name__=='__main__':main()
