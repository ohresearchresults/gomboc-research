# material-91f6e267b22b

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

#!/usr/bin/env python3
"""Exact identities for the sharp adjacent-pair trace maximum on ALL triangular bipyramids."""
from fractions import Fraction as F
from itertools import combinations, permutations
from pathlib import Path
import hashlib, json, sys

class P:
    def __init__(self, value=0):
        if isinstance(value,P):self.c=dict(value.c)
        elif isinstance(value,dict):self.c={k:F(v) for k,v in value.items() if v}
        else:self.c={} if not value else {(0,0):F(value)}
    def __add__(self,b):
        b=P(b); c=dict(self.c)
        for k,v in b.c.items():c[k]=c.get(k,F(0))+v
        return P(c)
    __radd__=__add__
    def __neg__(self):return P({k:-v for k,v in self.c.items()})
    def __sub__(self,b):return self+-P(b)
    def __rsub__(self,b):return P(b)+-self
    def __mul__(self,b):
        b=P(b);c={}
        for (i,j),v in self.c.items():
            for (k,l),w in b.c.items():c[(i+k,j+l)]=c.get((i+k,j+l),F(0))+v*w
        return P(c)
    __rmul__=__mul__
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        out=P(1)
        for _ in range(n):out=out*self
        return out
    def diff(self,k):
        c={}
        for ij,v in self.c.items():
            if ij[k]:a=list(ij);a[k]-=1;c[tuple(a)]=ij[k]*v
        return P(c)
    def at(self,h,u):return sum((v*h**i*u**j for (i,j),v in self.c.items()),F(0))
    def usub(self,expr):
        out=P(0)
        for (i,j),v in self.c.items():out+=P({(i,0):v})*expr**j
        return out
    def rem(self,mod):
        assert all(j==0 for i,j in self.c) and all(j==0 for i,j in mod.c)
        out=P(self); degree=max(i for i,j in mod.c); lead=mod.c[(degree,0)]
        while out.c and max(i for i,j in out.c)>=degree:
            d=max(i for i,j in out.c);out-=P({(d-degree,0):out.c[(d,0)]/lead})*mod
        return out
    def coefficients(self):return [[i,j,str(v)] for (i,j),v in sorted(self.c.items())]

def build():
    h=P({(1,0):1});u=P({(0,1):1})
    A=(2+h*u)*(1+2*h-(1+h)*u);B=(1+h)*(1+h-u)
    Nh=A.diff(0)*B-A*B.diff(0);Nu=A.diff(1)*B-A*B.diff(1)
    R=(h+1)*u*u-2*(h+1)**2*u+2*h*h+h+1
    C=4*h**4+12*h**3+16*h*h+14*h+6
    D=4*h**4+8*h**3+9*h*h+11*h+4
    root=4*h**3+14*h*h+11*h-1
    U=4*h*h+8*h;T=F(9,2)-29*h-14*h*h
    ident={
      'trace_minus_two':A-2*B-h*(u*(1-u)-h*((u-1)**2+1)),
      'u_derivative':Nu-h*(h+1)*R,
      'linear_elimination':(h+1)*Nh-((h+1)**2*u+h*h*(2*h+3))*R-h*(C*u-D),
      'root_elimination':(h+1)*D*D-2*(h+1)**2*C*D+(2*h*h+h+1)*C*C+(h+1)*(h*h+h+2)*(2*h*h+3*h+2)*root,
      'critical_u':C*U-D-(4*h**3+6*h*h+7*h+4)*root,
      'critical_R':R.usub(U)-(4*h*h+4*h-1)*root,
      'critical_value':2*A.usub(U)-2*T*B.usub(U)+root*(8*h**3+40*h*h+33*h-5),
      'value_cubic_remainder':(2*T**3-41*T*T+99*T-49).rem(root)
    }
    assert all(not x.c for x in ident.values())
    lo=F(82123969230105,10**15);hi=F(82123969230106,10**15)
    assert root.at(lo,0)<0<root.at(hi,0)
    # root'(h)=12h^2+28h+11>0 for h>=0: the positive root is unique.
    ulo=U.at(lo,0);uhi=U.at(hi,0);tlo=T.at(hi,0);thi=T.at(lo,0)
    assert 0<ulo<uhi<1 and 2<tlo<thi<F(253,125)<F(51,25)
    assert F(20239840438,10**10)<tlo<thi<F(20239840439,10**10)
    assert A.at(F(1,12),F(2,3))/B.at(F(1,12),F(2,3))==F(1184,585)>2
    # Literal incidence classification. A=0,B=1,C=2,D=3,E=4.
    faces=[frozenset(s) for s in [(0,1,2),(0,1,3),(1,2,3),(0,2,4),(0,3,4),(2,3,4)]]
    adjacent=[(i,j) for i,j in combinations(range(6),2) if len(faces[i]&faces[j])==2]
    contact=[];noncontact=[]
    for i,j in adjacent:
        for a in range(6):
            if a in (i,j):continue
            (contact if faces[a]&faces[i]&faces[j] else noncontact).append((a,i,j))
    orbit=set()
    for perm in permutations((0,2,3)):
        for apex in ((1,4),(4,1)):
            mapping=dict(zip((0,2,3),perm));mapping.update(zip((1,4),apex))
            fm=[faces.index(frozenset(mapping[v] for v in face)) for face in faces]
            orbit.add((fm[5],*sorted((fm[0],fm[1]))))
    assert len(adjacent)==9 and len(contact)==30 and len(noncontact)==6 and orbit==set(noncontact)
    # The physical formula is independent of the imbalance between E_x and E_y.
    physical=[]
    for hh,uu,r in [(F(1,12),F(2,3),F(1,7)),(F(1,12),F(2,3),F(5,6)),(F(3,2),F(4,5),F(2,5))]:
        s=(1+hh)*uu*r;t=(1+hh)*uu*(1-r);V=(1+hh)/6
        g=((1+hh+hh*s)/(4*(1+hh)),(1+hh+hh*t)/(4*(1+hh)),(1-hh)/4)
        nz=(s+t-1)/hh;h0=1-g[0]-g[1]-nz*g[2]
        assert h0==(1+hh-uu)/(4*hh)
        trace=(g[0]+g[1])*(2-nz)/(6*V*h0)
        assert trace==A.at(hh,uu)/B.at(hh,uu)
        physical.append({'h':str(hh),'u':str(uu),'imbalance':str(r),'trace':str(trace)})
    return {'identity':'ALL_TRIANGULAR_BIPYRAMIDS_SHARP_PAIR_TRACE_V1',
      'coefficient_order':'ascending powers of h; root interval specifies the real embedding',
      'root_polynomial':[-1,11,14,4],'root_interval':[str(lo),str(hi)],
      'u_interval':[str(ulo),str(uhi)],'sharp_trace_interval':[str(tlo),str(thi)],
      'trace_minimal_polynomial':[-49,99,-41,2],'sharp_trace_coefficients':['9/2','-29','-14'],
      'attaining_raw_vertices':[[['0'],['0'],['0']],[['0'],['0'],['1']],[['0'],['1'],['0']],
        [['1'],['0'],['0']],[['1/2','-3/2','-1'],['1/2','-3/2','-1'],['0','-1']]],
      'attainer_centroid_formula':['1/4+h*E_x/(4*(1+h))','1/4+h*E_y/(4*(1+h))','(1-h)/4'],
      'attainer_volume_formula':'(1+h)/6','pair_faces':['ABC','ABD'],'root_face':'CDE',
      'counts':{'adjacent_pairs':9,'third_facet_cases':36,'contact_cases':30,'noncontact_cases':6},
      'verified_zero_identities':sorted(ident),'Nh':Nh.coefficients(),'R':R.coefficients(),
      'asymmetric_controls':physical,'scope':'All homogeneous triangular bipyramids, not arbitrary polyhedra or Gombocs.'}

def main():
    assert len(sys.argv)==2 and sys.argv[1] in ('build','check')
    data=(json.dumps(build(),sort_keys=True,separators=(',',':'))+'\n').encode();path=Path('sharp_bipyramid_pair_report.json')
    if sys.argv[1]=='build':path.write_bytes(data)
    else:assert path.read_bytes()==data
    print('ALL_BIPYRAMID_PAIR_INCIDENCES_EXACT_PASS 9 36 30 6')
    print('SHARP_BIPYRAMID_ELIMINATION_EXACT_PASS 8')
    print('SHARP_VALUE_ISOLATED 2.0239840438 2.0239840439')
    print('REPORT',len(data),hashlib.sha256(data).hexdigest())
    print('ALL_TRIANGULAR_BIPYRAMIDS_SHARP_PAIR_TRACE_EXACT_PASS_NOT_C_BOUND')
if __name__=='__main__':main()
