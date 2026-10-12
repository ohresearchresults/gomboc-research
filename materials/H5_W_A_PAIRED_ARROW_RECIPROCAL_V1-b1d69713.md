# material-b1d69713ad02

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# H5: paired true arrows and one reciprocal metric exclude a full five-dimensional box

## Statement and scope
Let theta=(x,r,p,q,lambda) range independently over the closed box with centre (3/20,3/20,3/20,9/20,13/100) and radius 1/5000 in each coordinate. Construct the actual H5 convex polytope described below and centre it at its uniform VOLUME centroid. For EVERY physical positive definite metric M, the numbers of proper stable and unstable equilibria obey S>=2 or U>=2. Extra physical weak equilibria are allowed in this assertion. The coordinate-reflected box (x,r,p,q,lambda) -> (r,x,q,p,lambda) has the same exclusion.

This closes a genuine full-dimensional part of the 10/17/9 layer, including the point where the unchanged, individually optimized orthogonal-factor reflection-product template fails for EVERY auxiliary reference. It does not close whole H5, does not close E17, does not improve the global lower complexity bound 34, and supplies no attaining110 body. The canonical attaining upper bound remains C622.

This is a coordinator analytic proof with a finite exact rational certificate. The program was run both normally and in a source-only directory; the outputs were byte-identical. It is not a proof-assistant formalization. The exact sources, inputs, reconstruction commands and arithmetic margins are included or referenced below. Floating linear programming only located the integer directions. It is not part of the proof run.

## Actual geometry, incidence and mass
Put s=1-lambda. The seven planar basal points, labelled 0 through 6, are
(1/4,0), (1-3x/4,0), (1-p,p), (q,1-q), (0,1-3r/4), (0,1/4), (1/16,1/16).
The spatial basal points are (s*b_x,s*b_y,0). The three top points are 7=(0,0,1), 8=(lambda,0,1), 9=(0,lambda,1).
The nine oriented maximal face cycles are
(6,5,4,3,2,1,0), (8,7,0,1), (7,6,0), (1,2,8), (9,8,2,3), (9,3,4), (4,5,7,9), (6,7,5), (7,8,9).
Only their 17 genuine edges are used. In particular the true top-to-basal spokes are 7->0,5,6; 8->1,2; 9->3,4. The basal polar vertex q0 has exactly seven true neighbours q1,...,q7.

The complete exact geometry source is h5_reference_core.py, [internal-source-reference]. The additional interval source embedded at the end of this material treats all five parameters independently. It proves all 34 facet-incidence polynomial identities, strict nonincidence supports, rank three of an incident normal triple at every vertex, and outward orientation of every maximal facet. Every one of the 68 vertex triples not contained in a listed facet has vertices strictly on both sides throughout the box, so there is no unlisted maximal supporting plane.

Let A=(31-24*x*p-24*r*q)/64,
bx=509/3072-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8,
by=509/3072-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8.
The actual six-volume and six-first-moment vector are
D=lambda+2*A*s*s,
Kx=3*s^3*bx/2+s*s*lambda*(1-3*x*p/4)/4+lambda^2/4,
Ky=3*s^3*by/2+s*s*lambda*(1-3*r*q/4)/4+lambda^2/4,
Kz=A*s*s/2+lambda/2+lambda^2/4.
The program proves symbolically that the oriented boundary triangulation gives exactly D and K, as polynomials in the five variables: D has 9 monomials and the K coordinates have 20,20,9. Thus g=K/D is the actual uniform volume centroid, not a separately chosen moment vector. The polar normalization uses this same g. Throughout the box D>0 and 0<gamma=g_z<1/2.

At the central shape, Vol=6497249/48000000 and
g=(92526062243/415823936000,87300500333/415823936000,7672449/25988996).
All moving vertices below are v_i=raw_i-g and all q_f are the actual polar vertices at that origin.

## W and A locate the two proper roots without enumerating rooted trees
For a two-plane body centred at g=(g_H,gamma), let B_g and T_g be the centred basal and top polygons. Assume
W: -(1-2*gamma) B_g - 2*gamma T_g is contained in B_g,
A: q.a>-1 for every nonbasal polar vertex q and every top vertex a.
The top-face polar vertex has q.a=1 automatically. The other A guards are checked explicitly.

First choose a basal vertex b of maximal squared M norm within the base. If a top neighbour a had b^T M(a-b)>=0, the W image z=-(1-2*gamma)b-2*gamma*a would satisfy
z^T M z = b^T M b + 4*gamma*b^T M(a-b) + 4*gamma^2*(a-b)^T M(a-b) > b^T M b.
This contradicts z in B_g. For basal neighbours b', the identity 2*b^T M(b'-b)=||b'||_M^2-||b||_M^2-||b'-b||_M^2 makes the derivative strictly negative, even in a norm tie. Therefore some basal vertex is a proper unstable equilibrium for every M.

Next choose a nonbasal polar vertex q of maximal squared M^-1 norm among all nonbasal polar vertices. Let mu=min_{a in T_g} q.a>-1 and d=1-gamma+gamma*mu. Set u=(1-2*gamma)/d, v=gamma*(1+mu)/d. Both are positive and u+v=1. The point z=-u*q-v*q0 belongs to the actual polar and lies on a face dual to a top vertex attaining mu. To check this, top inequalities follow from q.a>=mu. For a basal b, W evaluated at a minimizing top vertex gives q.b>=-(1+2*gamma*mu)/(1-2*gamma), which is exactly z.b<=1. The top-dual face cannot contain q0, so z lies in the convex hull of nonbasal polar vertices.

If q^T M^-1(q0-q)>=0, then ||z||_(M^-1)^2=||q||_(M^-1)^2+2v*q^T M^-1(q0-q)+v^2*||q0-q||_(M^-1)^2>||q||_(M^-1)^2, a contradiction. Other true polar-neighbour derivatives are strictly negative by maximality within the nonbasal set. Hence a nonbasal face is a proper stable equilibrium for every M.

Under hypothetical S=U=1, choose a top vertex j with maximal top M norm. It is not the unique U, because a basal U already exists. Its two top-neighbour derivatives are strictly negative by the norm identity, so at least one of its true basal-spoke derivatives must be nonnegative. Similarly q0 is not the unique polar U, because a nonbasal proper S already exists. At least one q0->q_f derivative is nonnegative. Therefore a joint S1U1 metric belongs to at least one of exactly 7*7=49 paired-arrow cases. The case also carries the two inequalities that j has maximal top norm. This reasoning permits equality on the escaping arrows and hence includes additional weak equilibria. It does not assume that the basal face is stable or that the unique unstable root is a top vertex; those would be the wrong root directions.

In the stated box all 147 W guards are strictly positive, with lower bound
199548965666886955524992931/8115403461314776000000000000.
All 21 nontrivial A guards are strictly positive, with lower bound
581634455856564209530558547/8115403461314776000000000000.
These are exact interval bounds on the whole box, not sampled values. This W-and-A reduction does not require the seven-turn reflection-product lower estimate.

## A fixed actual reference and both finite-height gaps
Use one FIXED reference C built at the central body, not a reference moving with theta. Let a=v9 at that centre, write a=(b0,h), h=1-g_z, and set
W9=[[223142,-130077],[-130077,219126]]/1000000,
C=[[W9+b0*b0^T,h*b0],[h*b0^T,h*h]].
All entries are rational, and C is positive definite.

For any actual centred P, define U_C(P)=max (w^T C^-1 w)(n^T C n), over w in P, n in Ppolar and w.n=0. Its self-polar identity and its application to BOTH finite-height gaps are in the fully read source [internal-source-reference], SHA14c4a841bc3e3482a2e68b20110ccdc434ae3682bc2c5d51bfd3f00b769f93c8. This does not assume that the polar has a uniform centroid at zero. Under joint S1U1, the transported physical metric H=C^(1/2) M C^(1/2) obeys lambda1(H)/lambda2(H) <= f(10)*U_C and lambda2(H)/lambda3(H) <= f(9)*U_C, where f(m)=cos(pi/(2m))^(2m).

At the centre, the exact source proves U_C<=241/50. It covers all 289 genuine primal-edge/polar-edge pairs, 214 feasible rational curve pieces, and 428 endpoint/exceptional-fibre tests. Every curve needs just one Bernstein leaf at depth zero. The reduction is exact: an orthogonal-pair maximum can be chosen on a true edge of each polytope. For two edge parameters, orthogonality is bilinear; eliminate one parameter, multiply by the squared linear denominator, and bound the resulting quartic on every feasible rational interval. Vertical fibres and removable singularities are explicitly included. No angular mesh or sampled extremum is substituted for this continuum check.

For the entire box the interval program proves both signs of each centred labelled displacement belong to delta*P0, where
 delta=60118733851342405750585023/7501022756908062061958900000 <1.
Indeed every central polar support applied to either sign is at most delta. Comparing support functions gives
(1-delta)P0 subset P_theta subset (1+delta)P0.
Polarity and scaling then give
U_C(P_theta) <= (241/50)*((1+delta)/(1-delta))^2
=13778177415031287195170947822522639291854966439646575837489/2768352634017083778256523639811064719285678547682125526450 <4.978.
The two finite-height products are strictly below 4; their numerical displays are 3.884854981814003 and 3.7783597684919767. The proof uses rational Machin arctangent bounds to show pi>333/106, followed by cos(z)<1-z^2/2+z^4/24. No floating approximation establishes these inequalities.

## A reciprocal SUM inequality is stronger than two independent metric windows
For any positive definite three-dimensional H whose two consecutive eigenvalue ratios are at most k>=1, put A=H/tr(H), B=H^-1/tr(H^-1). Then
I/(k^2+k+1) <= A,B <= k^2*I/(k^2+k+1),
A+B <= (k^2+1)*I/(k^2+k+1).
These bounds use the fact that B is the normalized inverse of the SAME H. In particular the second line is not justified for arbitrary independent A and B satisfying only the first line.

For completeness the SUM inequality has an elementary exact polynomial certificate. Write the eigenvalues of H up to scale as (p*q,q,1), with 1<=p,q<=k. Put S=p*q+q+1 and T=p*q+p+1. The three SUM eigenvalues have numerators a*T+b*S over S*T, with (a,b)=(p*q,1),(q,p),(1,p*q). Set t=k-1, p=1+t*u, q=1+t*v. The bidegree(2,2) Bernstein coefficient matrices of
(k^2+1)*S*T-(k^2+k+1)*(a*T+b*S)
are the following, with every displayed entry nonnegative for t>=0:

1: [[3t^2,3t^2(t+2)/2,t^2(t+2)^2], [3t^2(t+2)/2,t^2(3t^2+10t+10)/4,t^2(t+2)(t^2+3t+3)/2], [t^2(t+1),0,0]].
2: [[3t^2,3t^2(t+2)/2,t^2(t+2)^2], [3t^2(t+2)/2,t^2(5t^2+16t+16)/4,t^2(t+2)(t^2+3t+3)], [t^2(t+2)^2,t^2(t+2)(t^2+3t+3),t^2(t^2+3t+3)^2]].
3: the transpose of matrix1.

The program independently constructs the k=4 coefficient tables by exact polynomial arithmetic. Put X=M/tr(CM), Y=M^-1/tr(C^-1 M^-1). Their traces satisfy tr(CX)=tr(C^-1 Y)=1. Congruence transforms the normalized windows and SUM inequality into the five necessary positive semidefinite matrices
X-C^-1/21,
16*C^-1/21-X,
Y-C/21,
16*C/21-Y,
17*C/21-C*X*C-Y.
They are linear in the twelve independent entries of symmetric X,Y. Using these constraints is a VALID relaxation of common-inverse physics, not a claim that arbitrary relaxed pairs are physical.

## All 49 cases have exact strict dual contradictions throughout the box
For each true spoke j->b and basal polar escape 0->f, include
v_j^T X(v_b-v_j)>=0,
q0^T Y(q_f-q0)>=0,
v_j^T X v_j-v_l^T X v_l>=0 for each other top l.
Each positive semidefinite matrix above can be tested on any integer direction, giving a necessary linear inequality. The exact input contains 49 records, each with eleven such scalar/positive-semidefinite row labels. Both escaping-arrow rows appear in every record. Some top-order rows need not carry positive weight and are then omitted. All eleven selected inequality weights are strictly positive.

Represent the inequalities at the central shape as A0*x<=b and the two trace equations as E*x=e=(1,1). For every record, reconstruct y,z by solving the exact 13-by-13 rational linear system
A0^T*y+E^T*z=0, sum(y)=1.
The program proves all y_i>0 and b.y+e.z<0. The two equality multipliers z are unrestricted in sign. The input is the integer directions and exact case labels, not rounded dual weights.

To make these contradictions uniform over the full box, only the escape/order rows vary: C, all positive-semidefinite tests, and the trace equations remain fixed. The spectral upper windows give coordinate bounds |X_ij|<=(16/21)*(C^-1_ii+C^-1_jj)/2 and |Y_ij|<=(16/21)*(C_ii+C_jj)/2. Exact interval evaluation bounds the difference between each varying row and its central row by err_i=sum_j sup|A_ij(theta)-A0_ij| times the corresponding coordinate bound. Thus any feasible actual metric pair would satisfy A0*x<=b+err. The same positive central dual gives
(b+err).y+e.z<0.
All 49 of these strict inequalities are checked as rational numbers. The minimum positive contradiction gap is greater than 1/100000 (its floating display is approximately1.0206340361e-5). Since the 49 cases exhaust the necessary true paired arrows, S1U1 is impossible on the whole box.

## Controls, chronology and limitations
The centre retains the exact own446 weak000 control M=[[5,1,2],[1,3,-1],[2,-1,4]] and own435 weak000 control M9=[[3,1,-1],[1,5,2],[-1,2,4]]. Both have no zero primitive. In the latter, top9 is strictly maximal among the three top norms. They are genuine physical controls, not110 constructions.

The all-reference barrier in [internal-source-reference] remains correct: at this same shape, U_C*exp(delta9)>14/3 for every reference, so the unchanged scalar mixed ceiling exceeds3.7 whereas the largest top9 reflection target is below3.6. The present proof bypasses that template by preserving a joint relation between M and its inverse and actual nonroot arrows. It does not contradict the geodesic optimization theorem. A proposed multi-reference investigation led to the stronger connection, but the successful certificate uses just ONE reference and the reciprocal SUM facet.

The general paired-arrow criterion applies whenever W and A hold and the relevant finite-height cone can be certified. Extending it to a broad H5 parameter region is the next mathematical question. Pointwise tests at other tapers, or numerical feasible points of the relaxed cone, are not a whole-region theorem and are not physical110 examples. Neither a cut-iteration limit nor a failed sufficient certificate proves feasibility.

## Complete recovery, including the one-byte source repair
Save this material as H5_W_A_PAIRED_ARROW_RECIPROCAL_V1.md. The exact ordinary proof run requires five Python source files, plus a one-time repair of the archived witness-source transport typo:

1. [internal-source-reference], h5_reference_core.py.txt:9461bytes, SHA54374c6e67c89467a37f68dca0c076ee20a8581acc2791d228f0c8e8f6d9aad8. Copy to h5_reference_core.py.
2. [internal-source-reference], h5_paired_arrow_core.py.txt:3072bytes, SHAfb374f81916be1d3c981cbbd5f19a3bde20a25f323788d79b00d8d9a2b31d5e0. Copy to h5_paired_arrow_core.py.
3. The COMPLETE h5_pair_box_geometry.py source is embedded verbatim below:7391bytes, SHAb88afd5c3395b8ced29c33d684f975b333cb144c7fb7a11fd07c504cead10da5. Direct attempts to store this unit separately were blocked; this transparent source block is the recovery input, not a missing filename.
4. [internal-source-reference], h5_paired_arrow_witnesses.py.txt:11576bytes, SHA56681bc92cc5603db9a2f1c88699973bfa5ab32f9316678a10ded88f989be438. This stored text has ONE extra colon after an assert and is not directly executable. Apply the complete exact repair source [internal-source-reference], h5_repair_witness_source.py.txt:910bytes, SHA085995c1fc18c920f2ff9f4873c043efc0c16b9b2c68672f53c4bdbc537d1037. It verifies the literal input hash, changes only that colon, and writes the tested h5_paired_arrow_witnesses.py:11575bytes, SHA5661daf87600dfc871e9a4656eca05a332db54ee2ed51c9b361c8a4dc8c4729e. Do not silently treat the uncorrected archived input as the tested source.
5. [internal-source-reference], h5_paired_arrow_box_exact.py.txt:5705bytes, SHA3f9a05fbc2398348c28f0d19b90a228e2155e492599ec0ad98053bb2da022753. Copy to h5_paired_arrow_box_exact.py.

Extract the embedded geometry source exactly with this standard-library command:
```python
from pathlib import Path
import hashlib
note=Path('H5_W_A_PAIRED_ARROW_RECIPROCAL_V1.md').read_text()
marker='# Exact embedded source: h5_pair_box_geometry.py\n\n```python\n'
source=note.split(marker,1)[1].split('\n```\n',1)[0]+'\n'
raw=source.encode()
assert len(raw)==7391
assert hashlib.sha256(raw).hexdigest()=='b88afd5c3395b8ced29c33d684f975b333cb144c7fb7a11fd07c504cead10da5'
Path('h5_pair_box_geometry.py').write_bytes(raw)
```
Then run, with assertions enabled:
python -B -S h5_repair_witness_source.py h5_paired_arrow_witnesses.py.txt
python -B -S h5_paired_arrow_box_exact.py

The repair marker is H5_PAIRED_ARROW_EXACT_WITNESS_SOURCE_RESTORED. The proof marker is H5_W_A_PAIRED_ARROW_RECIPROCAL_WHOLE_BOX_PASS. Expected proof output H5_PAIRED_ARROW_BOX_EXACT.json:409556bytes, SHA4394c8370f27230c27c7618fc27a46d3354e64972cedcf78e358bfee2fb25631. It contains every exact dual weight, row error, case margin, geometry guard, reference matrix and physical control. The output is reconstructible from these complete sources; its hash alone is not evidence. The ordinary and source-only tests used CPython3.13.5; the code is standard-library Python>=3.11 and reads no floating locator output.

# Exact embedded source: h5_pair_box_geometry.py

```python
"""Exact interval and polynomial geometry for the whole H5 paired-arrow box.
No numerical library. Includes a symbolic actual-volume-moment identity audit.
Requires h5_paired_arrow_core.py and h5_reference_core.py.
"""
from h5_paired_arrow_core import *

class Interval:
    def __init__(self,a,b=None):self.a=Q(a);self.b=Q(a if b is None else b);assert self.a<=self.b
    @staticmethod
    def cast(x):return x if isinstance(x,Interval) else Interval(x)
    def __add__(self,x):x=self.cast(x);return Interval(self.a+x.a,self.b+x.b)
    __radd__=__add__
    def __neg__(self):return Interval(-self.b,-self.a)
    def __sub__(self,x):return self+-self.cast(x)
    def __rsub__(self,x):return self.cast(x)+-self
    def __mul__(self,x):
        x=self.cast(x);v=(self.a*x.a,self.a*x.b,self.b*x.a,self.b*x.b);return Interval(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,x):
        x=self.cast(x);assert not x.a<=0<=x.b
        return self*Interval(1/x.b,1/x.a)
    def __rtruediv__(self,x):return self.cast(x)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return Interval(1)
        if n%2:return Interval(self.a**n,self.b**n)
        return Interval(0 if self.a<=0<=self.b else min(self.a**n,self.b**n),max(self.a**n,self.b**n))
    def mag(self):return max(abs(self.a),abs(self.b))

class Poly:
    zero=(0,)*5
    def __init__(self,c=0):self.c={self.zero:Q(c)} if c else {}
    @staticmethod
    def cast(x):return x if isinstance(x,Poly) else Poly(x)
    @classmethod
    def variable(cls,k):
        x=cls();e=[0]*5;e[k]=1;x.c[tuple(e)]=Q(1);return x
    def __add__(self,x):
        x=self.cast(x);v=Poly();v.c=self.c.copy()
        for e,a in x.c.items():
            v.c[e]=v.c.get(e,Q(0))+a
            if not v.c[e]:del v.c[e]
        return v
    __radd__=__add__
    def __neg__(self):v=Poly();v.c={e:-a for e,a in self.c.items()};return v
    def __sub__(self,x):return self+-self.cast(x)
    def __rsub__(self,x):return self.cast(x)+-self
    def __mul__(self,x):
        x=self.cast(x);v=Poly()
        for e,a in self.c.items():
            for f,b in x.c.items():
                g=tuple(i+j for i,j in zip(e,f));v.c[g]=v.c.get(g,Q(0))+a*b
        v.c={e:a for e,a in v.c.items() if a};return v
    __rmul__=__mul__
    def __truediv__(self,x):return self* (1/Q(x))
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        y=Poly(1)
        for i in range(n):y=y*self
        return y
    def iszero(self):return not self.c


def algebra(theta):
    x,r,p,q,lam=theta;s=1-lam
    b=((Q(1,4),0),(1-3*x/4,0),(1-p,p),(q,1-q),(0,1-3*r/4),(0,Q(1,4)),(Q(1,16),Q(1,16)))
    raw=tuple((s*u,s*v,0) for u,v in b)+((0,0,1),(lam,0,1),(0,lam,1))
    area=(31-24*x*p-24*r*q)/64
    bx=Q(509,3072)-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8
    by=Q(509,3072)-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8
    D=lam+2*area*s*s
    K0=(3*s**3*bx/2+s*s*lam*(1-3*x*p/4)/4+lam*lam/4,
        3*s**3*by/2+s*s*lam*(1-3*r*q/4)/4+lam*lam/4,
        area*s*s/2+lam/2+lam*lam/4)
    planar=(((0,-1),0,0,1),((p,p-3*x/4),s*p*(1-3*x/4),lam*p,3),
            ((1,1),s,lam,4),((q-3*r/4,q),s*q*(1-3*r/4),lam*q,5),
            ((-1,0),0,0,6),((-3,-1),-s/4,0,7),((-1,-3),-s/4,0,2))
    ns=[None]*9;hs=[None]*9;ns[0]=(0,0,-1);hs[0]=0;ns[8]=(0,0,1);hs[8]=1
    for n,h,t,f in planar:ns[f]=n+(h-t,);hs[f]=h
    return raw,ns,hs,planar,D,K0

def symbolic_moments():
    raw,ns,hs,planar,D,K0=algebra(tuple(Poly.variable(i) for i in range(5)))
    dd=Poly();kk=(Poly(),Poly(),Poly())
    count=0
    for f,face in enumerate(FACES):
        for i in face:
            assert Poly.cast(hs[f]-dot(ns[f],raw[i])).iszero();count+=1
        a=raw[face[0]]
        for j in range(1,len(face)-1):
            b,c=raw[face[j]],raw[face[j+1]];d=dot(a,cross(b,c));dd+=d;kk=add(kk,scale(d/4,add(add(a,b),c)))
    assert (dd-D).iszero() and all((a-b).iszero() for a,b in zip(kk,K0))
    return {'facet_incidence_identities':count,'volume_monomials':len(D.c),'first_moment_monomials':[len(a.c) for a in K0]}

def box_data(eps):
    theta=tuple(Interval(t-eps,t+eps) for t in THETA)
    raw,ns,hs,planar,D,K0=algebra(theta);assert D.a>0
    g=tuple(k/D for k in K0);gamma=g[2];assert gamma.a>0 and gamma.b<Q(1,2)
    vv=tuple(sub(a,g) for a in raw);poles=[];support=[];rank=[]
    for f in range(9):
        h=hs[f]-dot(ns[f],g);h=Interval.cast(h);assert h.a>0
        poles.append(tuple(a/h for a in ns[f]))
        for i in range(10):
            if i not in FACES[f]:
                slack=Interval.cast(hs[f]-dot(ns[f],raw[i]));assert slack.a>0;support.append(slack.a)
    # A uniformly independent incident normal triple at every labelled vertex.
    for i in range(10):
        triples=combinations([f for f in range(9) if i in FACES[f]],3)
        intervals=[Interval.cast(det(tuple(ns[f] for f in t))) for t in triples]
        guards=[min(abs(a.a),abs(a.b)) for a in intervals if a.a>0 or a.b<0]
        assert guards;rank.append(max(guards))
    # Every other vertex triple has vertices strictly on both sides throughout
    # the whole box; there is no unlisted maximal supporting plane.
    triple_guards=[]
    for i,j,k in combinations(range(10),3):
        if any({i,j,k} <= set(face) for face in FACES):continue
        normal=cross(sub(raw[j],raw[i]),sub(raw[k],raw[i]))
        vals=[Interval.cast(dot(normal,sub(a,raw[i]))) for a in raw]
        positive=max(x.a for x in vals);negative=max(-x.b for x in vals)
        assert positive>0 and negative>0
        triple_guards.append(min(positive,negative))
    orient=[]
    for f,face in enumerate(FACES):
        normal=cross(sub(raw[face[1]],raw[face[0]]),sub(raw[face[2]],raw[face[0]]))
        d=Interval.cast(dot(ns[f],normal));assert d.a>0;orient.append(d.a)
    WG=[];AG=[]
    for n,h,t,f in planar:
        for i in range(7):
            for j in range(7,10):
                w=h-2*dot(n,g[:2])+(1-2*gamma)*dot(n,raw[i][:2])+2*gamma*dot(n,raw[j][:2])
                w=Interval.cast(w);assert w.a>0;WG.append(w.a)
        for j in range(7,10):
            a=2*(h-dot(n+(h-t,),g))-(t-dot(n,raw[j][:2]));a=Interval.cast(a);assert a.a>0;AG.append(a.a)
    # Centred homothetic sandwich, with all90 own-centroid labelled displacements.
    delta=max(Interval.cast(dot(q,sub(v,B0['v'][i]))).mag() for i,v in enumerate(vv) for q in B0['poles'])
    assert delta<1
    upper=Q(241,50)*((1+delta)/(1-delta))**2
    return {'v':vv,'poles':tuple(poles),'g':g,'delta':delta,'U_upper':upper,'W_min':min(WG),'A_min':min(AG),
            'support_min':min(support),'rank_min':min(rank),'nonfacet_triples':len(triple_guards),'triple_min':min(triple_guards),'orientation_min':min(orient),'D':D,'W_count':len(WG),'A_count':len(AG)}

PAIR_INDEX=((0,0),(1,1),(2,2),(0,1),(0,2),(1,2))
XB=tuple(UP*(CI[i][i]+CI[j][j])/2 for i,j in PAIR_INDEX)+tuple(UP*(C[i][i]+C[j][j])/2 for i,j in PAIR_INDEX)

def row_error(label,spoke,polar,top,BI):
    if label[0]=='psd':return Q(0)
    center,b=row(label,spoke,polar,top=top);var,b1=row(label,spoke,polar,BI,top)
    return sum((Interval.cast(x-a).mag()*bound for x,a,bound in zip(var,center,XB)),Q(0))

def robust_margin(witness,BI):
    labs=witness['labels'];s=witness['spoke'];f=witness['polar'];t=witness.get('top',9)
    y,z,center=exact_dual(labs,s,f,top=t)
    error=sum((w*row_error(lab,s,f,t,BI) for w,lab in zip(y,labs)),Q(0))
    return center+error,center,error
```
